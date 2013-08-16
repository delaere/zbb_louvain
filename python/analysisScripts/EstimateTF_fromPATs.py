####################################################################
#                                                                  #
# *** EstimateTF_fromPATs.py ****                                  #
#                                                                  #
# Script to estimate distributions of Transfer Functions           #
# (useful for e.g. MadWeight analyses)                             # 
# for both leptons and jets                                        #
#                                                                  #
# Output variables:                                                #
# - E, eta, phi, pT, 1/pT (Reco and Partonic)                      #
# - DeltaE, DeltaEta, DeltaPhi, DeltaPt, DeltaPtinv                #
# (Delta = Partonic - Reco)                                        #
# --> jet: Partonic = b(bar) quark; Reco = b-jets                  #
# --> lep: Partonic = MG leptons;   Reco = selected Z daughters    #
# Matching is done based on DeltaR (and charge for leptons)        #  
#                                                                  #
# To be run e.g. as:                                               #
# >> python EstimateTF_fromPATs.py myDir/ 0 9999 myJobName         #
# - First  argument: Directory with PAT-tuples                     #
# - Second argument: First file in list                            #
# - Third  argument: Number of files per job                       #
# - Fourth argument: Name of job (used for naming of output files) #
#                                                                  #
# Outputs:                                                         #
# - .root file containing trees for leptons and jets               #
# - .lhco file                                                     #
#                                                                  #
# (c) CP3 llbb soldiers                                            #
#                                                                  #
####################################################################

#!/nfs/soft/cms/slc5_amd64_gcc434/cms/cmssw/CMSSW_4_2_7/external/slc5_amd64_gcc434/bin/python
from itertools import combinations
import ROOT
import numpy as n
import sys
import os
from DataFormats.FWLite import Events, Handle
from eventSelection import eventCategories, eventCategory, isInCategory, findBestCandidate, isGoodJet, isBJet,findDijetPair,hasNoOverlap,isZcandidate
from LumiReWeighting import LumiReWeighting
from monteCarloSelection import isZbEvent, isZcEvent, isZlEvent
from math import *
from ROOT import TFile, TTree, TH1F
from array import array

print sys.argv 

#Global variables
idPartons_0 = n.zeros(1, dtype=int) #gen-level origin of Z for DY production
idPartons_1 = n.zeros(1, dtype=int) #gen-level origin of Z for DY production
idMothers_0 = n.zeros(1, dtype=int) #gen-level origin of Z for DY production
idMothers_1 = n.zeros(1, dtype=int) #gen-level origin of Z for DY production
nDYmothers = n.zeros(1, dtype=int) #gen-level origin of Z for DY production
nDY2mothers = n.zeros(1, dtype=int) #gen-level origin of Z for DY production

class zbblabel:
  """labels used in the PAT configuration.
     Note that the use of labels is deprecated in favor of the AnalysisEvent interface."""
  allmuonslabel="allMuons"
  muonlabel="tightMuons"
  allelectronslabel="allElectrons"
  electronlabel="tightElectrons"
  #jetlabel="smearedPatJetsResDown"
  jetlabel="cleanPatJets"
  zmumulabel="zmuTightmuTight"
  zelelabel="zelTightelTight"
  vertexlabel="goodPV"
  pulabel="addPileupInfo"
  triggerlabel="patTriggerEvent"
  metlabel="patType01SCorrectedPFMet"
  rholabel="kt6PFJets"
  genlabel="genParticles" #genlabel="prunedGen"
  genjetlabel="ak5GenJets"
  genInfolabel="generator"

def CodeDYprod(genParticles):

#  npart = 0
#  for part in genParticles:
#    if part.status()!=3: break;
#    print "N=", npart, " id=", part.pdgId(), " nMothers=", part.numberOfMothers()," nDaughters=", part.numberOfDaughters(), " ", part
#    if part.pdgId()==2212: continue;
#    for n in range(0, part.numberOfDaughters()):
#      print "  id=", part.daughter(n).pdgId(), " ", part.daughter(n)
#    npart += 1

#type of DY production
#it is set to -1 if not found the production mechanism
#is is set to 0 for gg
#is is set to 1 fog qg
#is is set to 2 fog qq 
  
  output = -1
  countgluons = []
  countquarks = []
  idparton_first = []
  idparton_second = []
  idmother_first = []
  idmother_second = []
  NOriginalPartonFound = []
  NMotherFound = []
  
  countZ = 0
  
  for part in genParticles:
    if part.status()!=3: break;

    #Status 3 Z boson
    if part.pdgId() == 23 and part.status() == 3:
      countgluons.append(0)
      countquarks.append(0)
      idparton_first.append(0)
      idparton_second.append(0)
      idmother_first.append(0)
      idmother_second.append(0)
          
      NOriginalPartonFound.append(0)
      NMotherFound.append(0)
      #Z boson mothers
      for n in range(0, part.numberOfMothers()):
	#Z boson second mothers (direct from the proton)

	#print " mother(", n, ")=", part.mother(n).pdgId(), " number of mothers = ", part.mother(n).numberOfMothers()," IDX = ", part.mother(n)


        #Save first 2 mother id's
	if (NMotherFound[countZ] == 0):
	  idmother_first[countZ] = part.mother(n).pdgId()
	elif (NMotherFound[countZ] == 1):
	  idmother_second[countZ] = part.mother(n).pdgId()
	NMotherFound[countZ] += 1


	for n2 in range(0, part.mother(n).numberOfMothers()):	  
	  #Save first 2 second mother id's

	  #print "   mother2(", n2, ")=", part.mother(n).mother(n2).pdgId()," IDX = ", part.mother(n).mother(2)

	  if (NOriginalPartonFound[countZ] == 0):
	    idparton_first[countZ] = part.mother(n).mother(n2).pdgId()
	  elif (NOriginalPartonFound[countZ] == 1):
            idparton_second[countZ] = part.mother(n).mother(n2).pdgId()
	  NOriginalPartonFound[countZ] += 1

	  if abs(part.mother(n).mother(n2).pdgId()) < 7 and part.mother(n).mother(n2).mother().pdgId() == 2212:
	    countquarks[countZ] += 1
	  if part.mother(n).mother(n2).pdgId() == 21 and part.mother(n).mother(n2).mother().pdgId() == 2212:
	    countgluons[countZ] += 1
      
          #for n3 in range(0, part.mother(n).mother(n2).numberOfMothers()):
	    #print "     mother3(", n3, ")=", part.mother(n).mother(n2).mother(n3).pdgId()," IDX = ", part.mother(n).mother(n2).mother(3)


      #print "For Z[", countZ, "], NMotherFound=", NMotherFound[countZ], " NOriginalPartonFound=", NOriginalPartonFound[countZ]
      countZ += 1

  
  if countZ == 1:
    nDYmothers[0] = NMotherFound[0]
    nDY2mothers[0] = NOriginalPartonFound[0]
    
    if countquarks[0] +  countgluons[0] == 2:
      idPartons_0[0] = idparton_first[0]
      idPartons_1[0] = idparton_second[0]
      idMothers_0[0] = idmother_first[0]
      idMothers_1[0] = idmother_second[0]
      if countquarks[0] == 0 and countgluons[0] == 2:
        output = 0
      if countquarks[0] == 1 and countgluons[0] == 1:
        output = 1
      if countquarks[0] == 2 and countgluons[0] == 0:
        output = 2 
    else:
      return output

  #print "output=", output, "___"

  return output

def Delta(par1,par2):
  delta_phi=abs(par2.phi()-par1.phi())
  if delta_phi>pi:
    delta_phi=(2*pi)-delta_phi;
  delta=sqrt((delta_phi)**2 + (par1.eta()-par2.eta())**2)
  return delta

def DumpLHCOEvent(fwevent=None, run=None, event=None, lumi=None, path="", file=None , numberOfInteractions=None):

  """Dump informations about a given event in the LHCO format for MadWeight"""
  # output must be specified
  if file is None:
    print "Output must be specified. Set file argument to the file object opened for writing"
    return
  # in case no fwevent is provided, find it using run,event,(lumi)
  if fwevent is None:
    if (run is None) or (event is None):
      print "DumpLHCOEvent Error: either pass a fwlite event or give both run and event number"
      return
    # find event based on run  and event
    dirList=os.listdir(path)
    files=[]
    for fname in dirList:
      files.append(path+fname)
    events = Events (files)
    # there is the method to(run, event) can we use it ???
    for fwevent in events:
      if fwevent.eventAuxiliary().run()==run and fwevent.eventAuxiliary().id().event()==event and ( lumi is None or fwevent.eventAuxiliary().luminosityBlock()==lumi) :
        break
    if fwevent.eventAuxiliary().run()==run and fwevent.eventAuxiliary().id().event()==event and ( lumi is None or fwevent.eventAuxiliary().luminosityBlock()==lumi) :
      DumpLHCOEvent(fwevent)
    else:
      print "Event not found."
    return
  # in case a fwevent is provided, use it
  # load objects
  jetHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  noPUcorrmetHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  PrimaryVertexHandle = Handle ("vector<reco::Vertex>")
  #RhoHandle = Handle("double")
  fwevent.getByLabel (zbblabel.jetlabel,jetHandle)
  fwevent.getByLabel (zbblabel.metlabel,metHandle)
  fwevent.getByLabel ("patType1SCorrectedPFMet",noPUcorrmetHandle)
  fwevent.getByLabel (zbblabel.zmumulabel,zmuHandle)
  fwevent.getByLabel (zbblabel.zelelabel,zeleHandle)
  fwevent.getByLabel (zbblabel.vertexlabel, PrimaryVertexHandle)
  #fwevent.getByLabel("kt6PFJetsForIsolation","rho",RhoHandle)
  #fwevent.getByLabel("kt6PFJets_rho",RhoHandle)
  jets = jetHandle.product()
  met = metHandle.product()
  noPUcorrmet = noPUcorrmetHandle.product()
  #rho = RhoHandle.product()
  vertices = PrimaryVertexHandle.product()
  if vertices.size()>0 :
    vertex = vertices[0]
  else:
    vertex = None
  zCandidatesMu = zmuHandle.product()
  zCandidatesEle = zeleHandle.product()
  #find the best z candidate
  bestZcandidate = findBestCandidate(None,vertex,zCandidatesMu,zCandidatesEle)
  # loop over jets and print

  bjetp=[]
  for jet in jets:
    if isGoodJet(jet,bestZcandidate) and isBJet(jet, "HE", "SSV"):
      bjetp+=[jet]

  dijet = findDijetPair(bjetp, bestZcandidate)
              
  if dijet[1] is None:
    print "DumpLHCOEvent Error: not enough jets"
    return

  # print event in lhco format
  PrintEvent(fwevent,file)
  PrintLepton(bestZcandidate.daughter(0),file,1)
  PrintLepton(bestZcandidate.daughter(1),file,2)
  PrintJet(dijet[0],file,3)
  PrintJet(dijet[1],file,4)
  # print MET
  PrintMET(met[0],file,numberOfInteractions,5)

def PrintEvent(event, file) :
  file.write('0 ' + str(event.eventAuxiliary().run()) + ' ' +str(event.eventAuxiliary().id().event())+' \n')
  
def PrintLepton(lepton, file, index) :
  if lepton.isMuon():
    file.write(str(index) + ' 2 ' + str(lepton.eta()) + ' ' + str(lepton.phi()) + ' ' + str(lepton.pt()) + ' ' + str(lepton.mass()) + ' ' + str(lepton.charge()) + ' 0 0 0 0 \n')
  elif lepton.isElectron():
    file.write(str(index) + ' 1 ' + str(lepton.eta()) + ' ' + str(lepton.phi()) + ' ' + str(lepton.pt()) + ' ' + str(abs(lepton.mass())) + ' ' + str(lepton.charge()) + ' 0 0 0 0 \n')
  else:
    print "ERROR: can only handle electrons or muons"

def PrintJet(jet, file, index) :
  file.write(str(index) + ' 4 ' + str(jet.eta()) + ' ' + str(jet.phi()) + ' ' + str(jet.pt()) + ' ' + str(jet.mass()) + ' ' + str(jet.charge()) + ' 2 0 0 0 \n')

def PrintMET(met, file,numberOfInteractions ,index) :
  file.write(str(index) + ' 6 ' + str(met.eta()) + ' ' + str(met.phi()) + ' ' + str(met.pt()) + ' 0 0 0 ' + str(numberOfInteractions) +' 0 0 \n')

###############################
### Proxy for eventCategory ###
###############################

#data muChannel
#def dumpAll(stage=12, muChannel=True, isData=True, path="/home/fynu/vizangarciaj/scratch/DYJets_Summer11_fewfiles/",fileAll="outCMStoTFstudy",RootFile="outCMStoTFstudy",numb=None, Nfiles=10, Suffix=""):

#data elChannel
#def dumpAll(stage=12, muChannel=False, isData=True, path="/home/fynu/vizangarciaj/scratch/DYJets_Summer11_fewfiles/",fileAll="outCMStoTFstudy",RootFile="outCMStoTFstudy",numb=None, Nfiles=10, Suffix=""):

#MC muChannel
def dumpAll(stage=12, muChannel=True, isData=False, path="/home/fynu/vizangarciaj/scratch/DYJets_Summer11_fewfiles/",fileAll="outCMStoTFstudy",RootFile="outCMStoTFstudy",numb=None, Nfiles=10, Suffix=""):

#MC elChannel
#def dumpAll(stage=12, muChannel=False, isData=False, path="/home/fynu/vizangarciaj/scratch/DYJets_Summer11_fewfiles/",fileAll="outCMStoTFstudy",RootFile="outCMStoTFstudy",numb=None, Nfiles=10, Suffix=""):

  if (muChannel):
    print "running muChannel selection for stage ", stage
  else:
    print "running elChannel selection for stage ", stage
  
#def dumpAll(stage=9, muChannel=False, path="/storage/data/cms/store/user/cbeluffi/MC_Zbb_Jan12/TTbar_12_01_12/", fileAll="ttbar_check.lhco",file2j="2jets_ttsemi.lhco", file3j="3jets_ttsemi.lhco"):
  # prepare output
  out_file_INCL= open(fileAll+Suffix+"_"+str(numb)+".lhco","w")
 
  # create root file
  f = TFile( RootFile+Suffix+"_"+str(numb)+".root", 'recreate' )
  tree1 = TTree( 'tree1', 'data' )
  tree2 = TTree( 'tree2', 'data_lep' )

  runNumber =  n.zeros(1, dtype=int) # nbre of primary vertices
  eventNumber =  n.zeros(1, dtype=int) # nbre of primary vertices

  E_j1 = n.zeros(1, dtype=float)
  E_j2 = n.zeros(1, dtype=float)
  phi_j1 = n.zeros(1, dtype=float)
  phi_j2 = n.zeros(1, dtype=float)
  Eta_j1 = n.zeros(1, dtype=float)
  Eta_j2 = n.zeros(1, dtype=float)
  Pt_j1 = n.zeros(1, dtype=float)
  Pt_j2 = n.zeros(1, dtype=float)
  btag_j1= n.zeros(1, dtype=float) # estimator b tag value
  btag_j2= n.zeros(1, dtype=float) # estimator b tag value

  Met=  n.zeros(1, dtype=float)
  Met_phi=  n.zeros(1, dtype=float)
  Met_sig=  n.zeros(1, dtype=float)
  
  noPUcorrMet=  n.zeros(1, dtype=float)
  noPUcorrMet_phi=  n.zeros(1, dtype=float)
  noPUcorrMet_sig=  n.zeros(1, dtype=float)
  
  llM = n.zeros(1, dtype=float)
  bbM = n.zeros(1, dtype=float)


  E_l1 = n.zeros(1, dtype=float)
  E_l2 = n.zeros(1, dtype=float)
  phi_l1 = n.zeros(1, dtype=float)
  phi_l2 = n.zeros(1, dtype=float)
  Eta_l1 = n.zeros(1, dtype=float)
  Eta_l2 = n.zeros(1, dtype=float)
  Pt_l1 = n.zeros(1, dtype=float)
  Pt_l2 = n.zeros(1, dtype=float)
  DR_jet =  n.zeros(1, dtype=float)

  nJets = n.zeros(1, dtype=int)
  nBjetsHE = n.zeros(1, dtype=int)
  nBjetsHP = n.zeros(1, dtype=int)
  nBjetsHEHP = n.zeros(1, dtype=int)

  codeDYprod = n.zeros(1, dtype=int) #gen-level origin of Z for DY production

  isZb =  n.zeros(1, dtype=int) # nbre of primary vertices
  isZc =  n.zeros(1, dtype=int) # nbre of primary vertices
  isZl =  n.zeros(1, dtype=int) # nbre of primary vertices
  Pile_up =  n.zeros(1, dtype=float) # MC pile-up number (not in data)
  nbr_PV =  n.zeros(1, dtype=int) # nbre of primary vertices

  #Block for Jet TF study
  E_b = n.zeros(1, dtype=float)
  E_jb = n.zeros(1, dtype=float)
  E_ab = n.zeros(1, dtype=float)
  E_jab = n.zeros(1, dtype=float)
  DeltaE_jet = n.zeros(1, dtype=float)
  DeltaE_ajet = n.zeros(1, dtype=float)
  phi_b = n.zeros(1, dtype=float)
  phi_jb = n.zeros(1, dtype=float)
  phi_ab = n.zeros(1, dtype=float)
  phi_jab = n.zeros(1, dtype=float)
  Deltaphi_jet = n.zeros(1, dtype=float)
  Deltaphi_ajet = n.zeros(1, dtype=float)
  Eta_b = n.zeros(1, dtype=float)
  Eta_jb = n.zeros(1, dtype=float)
  Eta_ab = n.zeros(1, dtype=float)
  Eta_jab = n.zeros(1, dtype=float)
  DeltaEta_jet = n.zeros(1, dtype=float)
  DeltaEta_ajet = n.zeros(1, dtype=float)

  #leptons
  E_lgm = n.zeros(1, dtype=float)
  E_lrm = n.zeros(1, dtype=float)
  E_lgp = n.zeros(1, dtype=float)
  E_lrp = n.zeros(1, dtype=float)
  DeltaE_lm = n.zeros(1, dtype=float)
  DeltaE_lp = n.zeros(1, dtype=float)
  phi_lgm = n.zeros(1, dtype=float)
  phi_lrm = n.zeros(1, dtype=float)
  phi_lgp= n.zeros(1, dtype=float)
  phi_lrp = n.zeros(1, dtype=float)
  Deltaphi_lm  = n.zeros(1, dtype=float)
  Deltaphi_lp   = n.zeros(1, dtype=float)
  Eta_lgm = n.zeros(1, dtype=float)
  Eta_lrm= n.zeros(1, dtype=float)
  Eta_lgp= n.zeros(1, dtype=float)
  Eta_lrp = n.zeros(1, dtype=float)
  DeltaEta_lm = n.zeros(1, dtype=float)
  DeltaEta_lp  = n.zeros(1, dtype=float)

  PtInv_lm      = n.zeros(1, dtype=float)
  PtInv_lp      = n.zeros(1, dtype=float)
  DeltaPtInv_lm = n.zeros(1, dtype=float)
  DeltaPtInv_lp = n.zeros(1, dtype=float)

  tree1.Branch("runNumber", runNumber, "runNumber/l")
  tree1.Branch("eventNumber", eventNumber, "eventNumber/l")

  tree1.Branch("E_j1",E_j1,"E_j1/D")
  tree1.Branch("E_j2",E_j2,"E_j2/D")
  tree1.Branch("Eta_j1",Eta_j1,"Eta_j1/D")
  tree1.Branch("Eta_j2",Eta_j2,"Eta_j2/D")
  tree1.Branch("phi_j1",phi_j1,"phi_j1/D")
  tree1.Branch("phi_j2",phi_j2,"phi_j2/D")
  tree1.Branch("Pt_j1",Pt_j1,"Pt_j1/D")
  tree1.Branch("Pt_j2",Pt_j2,"Pt_j2/D")
  tree1.Branch("btag_j1",btag_j1,"btag_j1/D")
  tree1.Branch("btag_j2",btag_j2,"btag_j2/D")

  tree1.Branch("llM",llM,"llM/D")
  tree1.Branch("bbM",bbM,"bbM/D")
  

  tree1.Branch("E_l1",E_l1,"E_l1/D")
  tree1.Branch("E_l2",E_l2,"E_l2/D")
  tree1.Branch("Eta_l1",Eta_l1,"Eta_l1/D")
  tree1.Branch("Eta_l2",Eta_l2,"Eta_l2/D")
  tree1.Branch("phi_l1",phi_l1,"phi_l1/D")
  tree1.Branch("phi_l2",phi_l2,"phi_l2/D")
  tree1.Branch("Pt_l1",Pt_l1,"Pt_l1/D")
  tree1.Branch("Pt_l2",Pt_l2,"Pt_l2/D")
  tree1.Branch("DR_jet",DR_jet,"DR_jet/D")

  tree1.Branch("Met", Met, "Met/D")
  tree1.Branch("Met_phi", Met_phi, "Met_phi/D")
  tree1.Branch("Met_sig", Met_sig, "Met_sig/D")

  tree1.Branch("noPUcorrMet", noPUcorrMet, "noPUcorrMet/D")
  tree1.Branch("noPUcorrMet_phi", noPUcorrMet_phi, "noPUcorrMet_phi/D")
  tree1.Branch("noPUcorrMet_sig", noPUcorrMet_sig, "noPUcorrMet_sig/D")

  tree1.Branch("codeDYprod", codeDYprod, "codeDYprod/I")
  tree1.Branch("nDYmothers", nDYmothers, "nDYmothers/I")
  tree1.Branch("nDY2mothers", nDY2mothers, "nDY2mothers/I")
  tree1.Branch("idPartons_0", idPartons_0, "idPartons_0/I")
  tree1.Branch("idPartons_1", idPartons_1, "idPartons_1/I")
  tree1.Branch("idMothers_0", idMothers_0, "idMothers_0/I")
  tree1.Branch("idMothers_1", idMothers_1, "idMothers_1/I")
  tree1.Branch("isZb", isZb, "isZb/I")
  tree1.Branch("isZc", isZc, "isZc/I")
  tree1.Branch("isZl", isZl, "isZl/I")
  tree1.Branch("Pile_up", Pile_up, "Pile_up/D")

  tree1.Branch("nbr_PV", nbr_PV, "nbr_PV/I")

  tree1.Branch("nJets", nJets, "nJets/I")
  tree1.Branch("nBjetsHE", nBjetsHE, "nBjetsHE/I")
  tree1.Branch("nBjetsHP", nBjetsHP, "nBjetsHP/I")
  tree1.Branch("nBjetsHEHP", nBjetsHEHP, "nBjetsHEHP/I")
  
  
  
  #Jet Block for TF study
  
  # Jet Block  -------------------------------------------------
  tree1.Branch("E_b",E_b,"E_b/D")
  tree1.Branch("E_jb",E_jb,"E_jb/D")
  tree1.Branch("DeltaE_jet",DeltaE_jet,"DeltaE_jet/D")
  tree1.Branch("E_ab",E_ab,"E_ab/D")
  tree1.Branch("E_jab",E_jab,"E_jab/D")
  tree1.Branch("DeltaE_ajet",DeltaE_ajet,"DeltaE_ajet/D")  
  tree1.Branch("phi_b",phi_b,"phi_b/D");
  tree1.Branch("phi_ab",phi_ab,"phi_ab/D");
  tree1.Branch("phi_jb",phi_jb,"phi_jb/D");
  tree1.Branch("phi_jab",phi_jab,"phi_jab/D");
  tree1.Branch("Deltaphi_jet",Deltaphi_jet,"Deltaphi_jet/D");
  tree1.Branch("Deltaphi_ajet",Deltaphi_ajet,"Deltaphi_ajet/D");
  tree1.Branch("Eta_b",Eta_b,"Eta_b/D");
  tree1.Branch("Eta_ab",Eta_ab,"Eta_ab/D");
  tree1.Branch("Eta_jb",Eta_jb,"Eta_jb/D");
  tree1.Branch("Eta_jab",Eta_jab,"Eta_jab/D");
  tree1.Branch("DeltaEta_jet",DeltaEta_jet,"DeltaEta_jet/D");
  tree1.Branch("DeltaEta_ajet",DeltaEta_ajet,"DeltaEta_ajet/D");
  #----------------------------------------------------------------

  # Leptons Block -------------------------------------------------
  tree2.Branch("E_lgm",E_lgm,"E_lgm/D")
  tree2.Branch("E_lrm",E_lrm,"E_lrm/D")
  tree2.Branch("DeltaE_lm",DeltaE_lm,"DeltaE_lm/D")
  tree2.Branch("E_lgp",E_lgp,"E_lgp/D")
  tree2.Branch("E_lrp",E_lrp,"E_lrp/D")
  tree2.Branch("DeltaE_lp",DeltaE_lp,"DeltaE_lp/D")
  tree2.Branch("phi_lgm",phi_lgm,"phi_lgm/D");
  tree2.Branch("phi_lgp",phi_lgp,"phi_lgp/D");
  tree2.Branch("phi_lrm",phi_lrm,"phi_lrm/D");
  tree2.Branch("phi_lrp",phi_lrp,"phi_lrp/D");
  tree2.Branch("Deltaphi_lm",Deltaphi_lm,"Deltaphi_lm/D");
  tree2.Branch("Deltaphi_lp",Deltaphi_lp,"Deltaphi_lp/D");
  tree2.Branch("Eta_lgm",Eta_lgm,"Eta_lgm/D");
  tree2.Branch("Eta_lgp",Eta_lgp,"Eta_lgp/D");
  tree2.Branch("Eta_lrm",Eta_lrm,"Eta_lrm/D");
  tree2.Branch("Eta_lrp",Eta_lrp,"Eta_lrp/D");
  tree2.Branch("DeltaEta_lm",DeltaEta_lm,"DeltaEta_lm/D");
  tree2.Branch("DeltaEta_lp",DeltaEta_lp,"DeltaEta_lp/D");

  tree2.Branch("PtInv_lp",     PtInv_lp,     "PtInv_lp/D");
  tree2.Branch("PtInv_lm",     PtInv_lm,     "PtInv_lm/D");
  tree2.Branch("DeltaPtInv_lp",DeltaPtInv_lp,"DeltaPtInv_lp/D");
  tree2.Branch("DeltaPtInv_lm",DeltaPtInv_lm,"DeltaPtInv_lm/D");

  #----------------------------------------------------------------

  # read data
  dirList=os.listdir(path)
  files=[]
  number=0
  numb = int(numb)
  filemin = numb*int(Nfiles)
  #filemax = numb*10 + 10
  filemax = numb*int(Nfiles) + int(Nfiles)
  try:
    dirList.remove("Ready_Files")
  except:
    pass
  try:
    dirList.remove("files.txt")
  except:
    pass
  dirList.sort()
  for fname in dirList:
    number+=1
    if number>filemin and number<=filemax:
      files.append(path+fname)
      print "We will run over file ", fname
  events = Events (files)

  metlabel=zbblabel.metlabel # To be check to load MeT type 1 + phi correction
  jetlabel=zbblabel.jetlabel
  jetalllabel="patJets"
  zmulabel=zbblabel.zmumulabel
  zelelabel=zbblabel.zelelabel
  genpartlabel=zbblabel.genlabel
  labelElectron = zbblabel.electronlabel
  labelMuon = zbblabel.muonlabel
  vertexLabel =zbblabel.vertexlabel

  #RhoHandle = Handle("double")
  jetHandle = Handle ("vector<pat::Jet>")
  jetallHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  noPUcorrmetHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  trigInfoHandle = Handle ("pat::TriggerEvent")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  muonHandle = Handle ("vector<pat::Muon>")
  electronHandle = Handle ("vector<pat::Electron>")
  genpartHandle =  Handle("std::vector<reco::GenParticle>")
  PrimaryVertexHandle = Handle ("vector<reco::Vertex>")

  PULabel = "addPileupInfo"
  PUHandle= Handle("std::vector<PileupSummaryInfo>")

# Event loop
  for event in events:
    #if isZbEvent(genparts)==False:
     # continue
      
    #print '----------------------- New Event -------------------------'
    event.getByLabel (jetlabel,jetHandle)
    event.getByLabel (jetalllabel,jetallHandle)
    event.getByLabel (metlabel,metHandle)
    event.getByLabel ("patType1SCorrectedPFMet",noPUcorrmetHandle)
    event.getByLabel (zmulabel,zmuHandle)
    event.getByLabel (zelelabel,zeleHandle)
    event.getByLabel (labelElectron,electronHandle)
    event.getByLabel (labelMuon,muonHandle)
    event.getByLabel (vertexLabel, PrimaryVertexHandle)
    #event.getByLabel("kt6PFJetsForIsolation","rho",RhoHandle)
    #event.getByLabel("kt6PFJets_rho",RhoHandle)
    run = event.eventAuxiliary().run()

    runNumber[0] = event.eventAuxiliary().run()
    eventNumber[0] = event.eventAuxiliary().id().event()
    
    jets = jetHandle.product()
    met = metHandle.product()
    noPUcorrmet = noPUcorrmetHandle.product()
    zCandidatesMu = zmuHandle.product()
    zCandidatesEle = zeleHandle.product()
#    triggerInfo = trigInfoHandle.product()
    vertices = PrimaryVertexHandle.product()
    muons = muonHandle.product()
    electrons = electronHandle.product()
    #rho = RhoHandle.product()
    
    if vertices.size()>0 :
      vertex = vertices[0]
    else:
      vertex = None
    
    #gen level production mechanism of DY production
    #it is set to -1 if not found the production mechanism
    #is is set to 0 for gg
    #is is set to 1 fog qg
    #is is set to 2 fog qq
    
    codeDYprod[0] = -1 
    nDYmothers[0] = -1 
    nDY2mothers[0] = -1 
    idPartons_0[0] = 0
    idPartons_1[0] = 0
    idMothers_0[0] = 0
    idMothers_1[0] = 0
    nbr_PV[0] = vertices.size()
    #gen level info
    Pile_up[0] = 0
    numberOfInteractions = 0
    isZb[0] = 0
    isZc[0] = 0
    isZl[0] = 0	
    triggerInfo = None

    if isData==False:
      event.getByLabel (genpartlabel,genpartHandle)
      event.getByLabel (PULabel,PUHandle)
      PU= PUHandle.product()
      genparts = genpartHandle.product()
      #Number of pile up interactions variable is duplicated. I should remove one
      numberOfInteractions = PUHandle.product()[0].getPU_NumInteractions()
      Pile_up[0] = PUHandle.product()[0].getPU_NumInteractions()

      if isZbEvent(event)==True:
	isZb[0] = 1
      if isZcEvent(event)==True:
	isZc[0] = 1
      if isZlEvent(event)==True:
	isZl[0] = 1
      
    else: #It looks that for MC loading the trigger branch produces a crash
      event.getByLabel(zbblabel.triggerlabel,trigInfoHandle)
      triggerInfo = trigInfoHandle.product()

    #We require the event selection given by the variable "stage"
    #We require in addition at least one Z candidate and 2 jets regardless the value we chose for "stage"

# Start procedure selection
    categTuple=eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, vertices,jets, met, run ,muChannel)   #defalut mass windows = 15
    if isInCategory(stage, categTuple) and  isInCategory( 3, categTuple) and categTuple[3]>1:
        
      DumpLHCOEvent(event, None, None, None, "", out_file_INCL,numberOfInteractions)
      bestZ = findBestCandidate(None,vertex,zCandidatesMu,zCandidatesEle)

      bjetp=[]
      for jet in jets:
        if isGoodJet(jet,bestZ) and isBJet(jet, "HE", "SSV"):
          bjetp+=[jet]
      if len(bjetp)>1:
        dijet = findDijetPair(bjetp, bestZ)  
        l1=bestZ.daughter(0)
        l2=bestZ.daughter(1)

        if l1.charge() > 0 and l2.charge() < 0:
          lrecpos = l1
          lrecneg = l2
        elif   l2.charge() > 0 and l1.charge() < 0:
          lrecpos = l2
          lrecneg = l1
        else:
          print "warning, dilepton pair with same sign leptons"
                                                                
        dphi=dijet[0].phi()-dijet[1].phi()
        if(dphi>pi):
          dphi= (2*pi) - dphi
        DR=sqrt(pow(dijet[0].eta()-dijet[1].eta(),2)+pow(dphi,2))

        b1 = ROOT.TLorentzVector(dijet[0].px(),dijet[0].py(),dijet[0].pz(),dijet[0].energy())
	b2 = ROOT.TLorentzVector(dijet[1].px(),dijet[1].py(),dijet[1].pz(),dijet[1].energy())
	bb = b1 + b2
	bbM[0] = bb.M()
	
	llM[0] = bestZ.mass()
	
        E_j1[0]=dijet[0].energy() 
        E_j2[0]=dijet[1].energy()
        Eta_j1[0]=dijet[0].eta()
        Eta_j2[0]=dijet[1].eta()
        phi_j1[0]=dijet[0].phi()
        phi_j2[0]=dijet[1].phi()
        Pt_j1[0]=dijet[0].pt()
        Pt_j2[0]=dijet[1].pt()
	btag_j1[0]=dijet[0].bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
	btag_j2[0]=dijet[1].bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
        DR_jet[0]=DR
      
        E_l1[0]=l1.energy()
        E_l2[0]=l2.energy()
        Eta_l1[0]=l1.eta()
        Eta_l2[0]=l2.eta()
        phi_l1[0]=l1.phi()
        phi_l2[0]=l2.phi()
        Pt_l1[0]=l1.pt()
        Pt_l2[0]=l2.pt()
	

        #info about MET
        Met[0] = met[0].pt()
        Met_phi[0] = met[0].phi()
        Met_sig[0] = 0.
        if met[0].getSignificanceMatrix()(0,0)<1e10 and met[0].getSignificanceMatrix()(1,1)<1e10 : 
          Met_sig[0] = met[0].significance()
	
        #info about MET, collection no PU corr
        noPUcorrMet[0] = noPUcorrmet[0].pt()
        noPUcorrMet_phi[0] = noPUcorrmet[0].phi()
        noPUcorrMet_sig[0] = 0.
        if noPUcorrmet[0].getSignificanceMatrix()(0,0)<1e10 and noPUcorrmet[0].getSignificanceMatrix()(1,1)<1e10 : 
          noPUcorrMet_sig[0] = noPUcorrmet[0].significance()
	

	#info about nJets, nbtagged jets
	nJets[0] = 0
        nBjetsHE[0] = 0
        nBjetsHP[0] = 0
        nBjetsHEHP[0] = 0
        for jet in jets:
          if isGoodJet(jet,bestZ):
            nJets[0] += 1
            HE = isBJet(jet,"HE","SSV")
            HP = isBJet(jet,"HP","SSV")
            if HE: nBjetsHE[0] += 1
            if HP: nBjetsHP[0] += 1
            if HE and HP: nBjetsHEHP[0] +=1

        #some gen level information (it requires looping)
	if isData==False:
	  codeDYprod[0] = CodeDYprod(genparts)

	
	print "tree.Fill for standard selection"
	
	#Block for jet TF study
        
	if isData==False:
          # partonic information for the b-quark
          bq=[]
          bbarq=[]
          bjet=[]
          dR1=10
          dR2=10
          dR3=10
          dR4=10
          #selection of the b-quark

          lp=[]
          lm=[]
          #dRxy; x=gen, y=rec, p=positive, n=negative charge
          dRpp=10
          dRnn=10
          dRpn=10
          dRnp=10
                                                                      
	  
	  for partg in genparts:
            if partg.pdgId()==5  and partg.status()==3:
              bq+=[partg]
            if partg.pdgId()==-5 and partg.status()==3:
              bbarq+=[partg]
            
            #If mu channel search for dimuon pair, if el channel search for dielectron pair
            if muChannel and partg.pdgId()==13 and partg.status()==3:
              lm+=[partg]
            elif muChannel and partg.pdgId()==-13 and partg.status()==3:
              lp+=[partg]
            elif muChannel==False and partg.pdgId()==11 and partg.status()==3:
              lm+=[partg]
            elif muChannel==False and partg.pdgId()==-11 and partg.status()==3:
              lp+=[partg]
              
          if bq and  bbarq :
            dR1= Delta(dijet[0],bq[0])
            dR2= Delta(dijet[1],bbarq[0])
            dR3= Delta(dijet[0],bbarq[0])
            dR4= Delta(dijet[1], bq[0])

          if lp and  lm :
            dRpp= Delta(lrecpos,lp[0])
            dRnn= Delta(lrecneg,lm[0])
            dRnp= Delta(lrecpos,lm[0])
            dRpn= Delta(lrecneg,lp[0])
                                                            
          seuil=0.3
	  print "dR1=", dR1, " dR2=", dR2, " dR3=", dR3, " dR4=", dR4
          if  bq and bbarq:
            print "AFTER IF: dR1=", dR1, " dR2=", dR2, " dR3=", dR3, " dR4=", dR4
            if dR1<seuil and dR2<seuil and dR1<dR4 and dR2<dR3:
              E_b[0]=bq[0].energy()
              E_jb[0]=dijet[0].energy()
              E_ab[0]=bbarq[0].energy()
              E_jab[0]=dijet[1].energy()
              DeltaE_ajet[0]=bbarq[0].energy()-dijet[1].energy()
              DeltaE_jet[0]=bq[0].energy()-dijet[0].energy()
              phi_b[0]=bq[0].phi()
              phi_jb[0]=dijet[0].phi()
              phi_ab[0]=bbarq[0].phi()
              phi_jab[0]=dijet[1].phi()
              delta_phi1=bbarq[0].phi()-dijet[1].phi()
              delta_phi2=bq[0].phi()-dijet[0].phi()
              if delta_phi1>pi:
                delta_phi1=(2*pi)-delta_phi1
              if delta_phi2>pi:
                delta_phi2=(2*pi)-delta_phi2
              Deltaphi_ajet[0]=delta_phi1
              Deltaphi_jet[0]=delta_phi2
              Eta_b[0]=bq[0].eta()
              Eta_jb[0]=dijet[0].eta()
              Eta_ab[0]=bbarq[0].eta()
              Eta_jab[0]=dijet[1].eta()
              DeltaEta_ajet[0]=bbarq[0].eta()-dijet[1].eta()
              DeltaEta_jet[0]=bq[0].eta()-dijet[0].eta()
	      tree1.Fill()
    
            if dR4<seuil and dR3<seuil and dR4<dR1 and dR3<dR2:      
              E_b[0]=bq[0].energy()
              E_jb[0]=dijet[1].energy()
              E_ab[0]=bbarq[0].energy()
              E_jab[0]=dijet[0].energy()
              DeltaE_ajet[0]=bbarq[0].energy()-dijet[0].energy()
              DeltaE_jet[0]=bq[0].energy()-dijet[1].energy()
              phi_b[0]=bq[0].phi()
              phi_jb[0]=dijet[1].phi()
              phi_ab[0]=bbarq[0].phi()
              phi_jab[0]=dijet[0].phi()
              delta_phi1=bbarq[0].phi()-dijet[0].phi()
              delta_phi2=bq[0].phi()-dijet[1].phi()
              if delta_phi1>pi:
                delta_phi1=(2*pi)-delta_phi1
              if delta_phi2>pi:
                  delta_phi2=(2*pi)-delta_phi2
              Deltaphi_ajet[0]=delta_phi1
              Deltaphi_jet[0]=delta_phi2
              Eta_b[0]=bq[0].eta()
              Eta_jb[0]=dijet[1].eta()
              Eta_ab[0]=bbarq[0].eta()
              Eta_jab[0]=dijet[0].eta()
              DeltaEta_ajet[0]=bbarq[0].eta()-dijet[0].eta()
              DeltaEta_jet[0]=bq[0].eta()-dijet[1].eta()
	      tree1.Fill()

          #lepton stuff
          seuil=0.3
          print "dRpp=", dRpp, " dRnn=", dRnn, " dRpn=", dRpn, " dRnp=", dRnp
          if  lp and lm:
            if dRpp<seuil and dRnn<seuil and dRpp<dRnp and dRnn<dRpn:
              E_lgm[0]=lm[0].energy()
              E_lrm[0]=lrecneg.energy()
              E_lgp[0]=lp[0].energy()
              E_lrp[0]=lrecpos.energy()
              DeltaE_lp[0]=lp[0].energy()-lrecpos.energy()
              DeltaE_lm[0]=lm[0].energy()-lrecneg.energy()
              phi_lgm[0]=lm[0].phi()
              phi_lrm[0]=lrecneg.phi()
              phi_lgp[0]=lp[0].phi()
              phi_lrp[0]=lrecpos.phi()
              delta_phi1=lp[0].phi()-lrecpos.phi()
              delta_phi2=lm[0].phi()-lrecneg.phi()
              if delta_phi1>pi:
                delta_phi1=(2*pi)-delta_phi1
              if delta_phi2>pi:
                delta_phi2=(2*pi)-delta_phi2
              Deltaphi_lp[0]=delta_phi1
              Deltaphi_lm[0]=delta_phi2
              Eta_lgm[0]=lm[0].eta()
              Eta_lrm[0]=lrecneg.eta()
              Eta_lgp[0]=lp[0].eta()
              Eta_lrp[0]=lrecpos.eta()
              DeltaEta_lp[0]=lp[0].eta()-lrecpos.eta()
              DeltaEta_lm[0]=lm[0].eta()-lrecneg.eta()

              PtInv_lp[0]=1./lp[0].pt()
              PtInv_lm[0]=1./lm[0].pt()
              DeltaPtInv_lp[0]=1./lp[0].pt()-1./lrecpos.pt()
              DeltaPtInv_lm[0]=1./lm[0].pt()-1./lrecneg.pt()
              
              tree2.Fill()

              
  # close file
  out_file_INCL.close()
  f.Write()
  f.Close()


for num, arg in enumerate(sys.argv):
  print num, arg

#dumpAll(fileAll=sys.argv[1],file2j=sys.argv[2],RootFile=sys.argv[3],numb=sys.argv[4])
#
dumpAll(path=sys.argv[1], numb=sys.argv[2], Nfiles=sys.argv[3], Suffix=sys.argv[4], stage=10)
    
