#!/nfs/soft/cms/slc5_amd64_gcc434/cms/cmssw/CMSSW_4_2_7/external/slc5_amd64_gcc434/bin/python
from itertools import combinations
import ROOT
import numpy as n
import sys
import os
from DataFormats.FWLite import Events, Handle
from eventSelection import eventCategories, eventCategory, isInCategory, findBestCandidate, isGoodJet, isBJet,findDijetPair,hasNoOverlap,isZcandidate, isGoodMet_Sig, JetCorrectionUncertaintyProxy
from LumiReWeighting import LumiReWeighting
from monteCarloSelection import isZbEvent, isZcEvent, isZlEvent
from zbbCommons import zbblabel, isZbbSelection
from math import *
from ROOT import TFile, TTree, TH1F
from array import array




_JECuncertainty = JetCorrectionUncertaintyProxy()

btagAlgo="SSV"
if not isZbbSelection : btagAlgo="CSV"

print sys.argv 

channel = sys.argv[1]

############
### Maps ###
############

muChannel = { "MuA_DATA"     : True ,
              "ElA_DATA"     : False,
              "MuB_DATA"     : True ,
              "ElB_DATA"     : False,
              "Mu_MC"        : True ,
              "El_MC"        : False,
              "Zbb_Mu_MC"    : True ,
              "Zbb_El_MC"    : False,
              "TT_Mu_MC"     : True ,
              "TT_El_MC"     : False,
              "ZZ_Mu_MC"     : True ,
              "ZZ_El_MC"     : False,
              "ZH115_Mu_MC"  : True ,
              "ZH115_El_MC"  : False,
              "ZH120_Mu_MC"  : True ,
              "ZH120_El_MC"  : False,
              "ZH125_Mu_MC"  : True ,
              "ZH125_El_MC"  : False,
              "ZH130_Mu_MC"  : True ,
              "ZH130_El_MC"  : False,
              "ZH135_Mu_MC"  : True ,
              "ZH135_El_MC"  : False,
              "tW_Mu_MC"     : True ,
              "tW_El_MC"     : False,
              "tbarW_Mu_MC"  : True ,
              "tbarW_El_MC"  : False,
              "evtgen_MC"    : False,
              "herwig_MC"    : False,
              "pythia_MC"    : False,
              "ZA_Mu_MC" : True,
              "ZA_El_MC" : False
              }

path = { 
  "MuA_DATA"     : "/nfs/user/acaudron/skim444/Mu_DataA/" ,
  "ElA_DATA"     : "/nfs/user/acaudron/skim444/El_DataA/" ,
  "MuB_DATA"     : "/nfs/user/acaudron/skim444/Mu_DataB/" ,
  "ElB_DATA"     : "/nfs/user/acaudron/skim444/El_DataB/" ,
  "Mu_MC"        : "/nfs/user/acaudron/skim444/DY_MC/"    ,
  "El_MC"        : "/nfs/user/acaudron/skim444/DY_MC/"    ,
  #"Mu_MC"        : "/storage/data/cms/store/user/acaudron/Torino/DYJets_MCMatched_00.root"    , 
  #"El_MC"        : "/storage/data/cms/store/user/acaudron/Torino/DYJets_MCMatched_00.root"    , 
  "Zbb_Mu_MC"    : "/storage/data/cms/store/user/acaudron/Fall11MC_444/zbbProd/"   ,
  "Zbb_El_MC"    : "/storage/data/cms/store/user/acaudron/Fall11MC_444/zbbProd/"   ,
  "TT_Mu_MC"     : "/nfs/user/acaudron/skim444/TT_MC/"    ,
  "TT_El_MC"     : "/nfs/user/acaudron/skim444/TT_MC/"    ,
  "ZZ_Mu_MC"     : "/nfs/user/acaudron/skim444/ZZ_MC/"    ,
  "ZZ_El_MC"     : "/nfs/user/acaudron/skim444/ZZ_MC/"    ,
  "ZH115_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH115_MC/" ,
  "ZH115_El_MC"  : "/nfs/user/acaudron/skim444/ZH115_MC/" ,
  "ZH120_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH120_MC/" ,
  "ZH120_El_MC"  : "/nfs/user/acaudron/skim444/ZH120_MC/" ,
  "ZH125_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH125_MC/" ,
  "ZH125_El_MC"  : "/nfs/user/acaudron/skim444/ZH125_MC/" ,
  "ZH130_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH130_MC/" ,
  "ZH130_El_MC"  : "/nfs/user/acaudron/skim444/ZH130_MC/" ,
  "ZH135_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH135_MC/" ,
  "ZH135_El_MC"  : "/nfs/user/acaudron/skim444/ZH135_MC/" ,
  "tW_Mu_MC"     : "/nfs/user/acaudron/skim444/tW_MC/"    ,
  "tW_El_MC"     : "/nfs/user/acaudron/skim444/tW_MC/"    ,
  "tbarW_Mu_MC"  : "/nfs/user/acaudron/skim444/tbarW_MC/" ,
  "tbarW_El_MC"  : "/nfs/user/acaudron/skim444/tbarW_MC/" ,
  "evtgen_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/evtgen/",
  "herwig_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/herwig/",
  "pythia_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/pythia/",
  "ZA_Mu_MC" : "/nfs/user/acaudron/ZApat/",
  "ZA_El_MC" : "/nfs/user/acaudron/ZApat/"
  }

checkTrigger = {
  "MuA_DATA"     : True ,
  "ElA_DATA"     : True ,
  "MuB_DATA"     : True ,
  "ElB_DATA"     : True ,
  "Mu_MC"        : False,
  "El_MC"        : False,
  "Zbb_Mu_MC"    : False,
  "Zbb_El_MC"    : False,
  "TT_Mu_MC"     : False,
  "TT_El_MC"     : False,
  "ZZ_Mu_MC"     : False,
  "ZZ_El_MC"     : False,
  "ZH115_Mu_MC"  : False,
  "ZH115_El_MC"  : False,
  "ZH120_Mu_MC"  : False,
  "ZH120_El_MC"  : False,
  "ZH125_Mu_MC"  : False,
  "ZH125_El_MC"  : False,
  "ZH130_Mu_MC"  : False,
  "ZH130_El_MC"  : False,
  "ZH135_Mu_MC"  : False,
  "ZH135_El_MC"  : False,
  "tW_Mu_MC"     : False,
  "tW_El_MC"     : False,
  "tbarW_Mu_MC"  : False,
  "tbarW_El_MC"  : False,
  "evtgen_MC"    : False,
  "herwig_MC"    : False,
  "pythia_MC"    : False,
  "ZA_Mu_MC" : False,
  "ZA_El_MC" : False
  }
  
#Global variables
idPartons_0 = n.zeros(1, dtype=int) #gen-level origin of Z for DY production
idPartons_1 = n.zeros(1, dtype=int) #gen-level origin of Z for DY production
idMothers_0 = n.zeros(1, dtype=int) #gen-level origin of Z for DY production
idMothers_1 = n.zeros(1, dtype=int) #gen-level origin of Z for DY production
nDYmothers = n.zeros(1, dtype=int) #gen-level origin of Z for DY production
nDY2mothers = n.zeros(1, dtype=int) #gen-level origin of Z for DY production


def CodeDYprod(genParticles):

  npart = 0
  #print "*****************eventbegins****************"
  for part in genParticles:

  
    if part.status()!=3:
      break
      
    npart += 1

  #print "*****************eventends****************"
  #print ""

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

	print " mother(", n, ")=", part.mother(n).pdgId(), " number of mothers = ", part.mother(n).numberOfMothers()," IDX = ", part.mother(n)


        #Save first 2 mother id's
	if (NMotherFound[countZ] == 0):
	  idmother_first[countZ] = part.mother(n).pdgId()
	elif (NMotherFound[countZ] == 1):
	  idmother_second[countZ] = part.mother(n).pdgId()
	NMotherFound[countZ] += 1


	for n2 in range(0, part.mother(n).numberOfMothers()):	  
	  #Save first 2 second mother id's

	  print "   mother2(", n2, ")=", part.mother(n).mother(n2).pdgId()," IDX = ", part.mother(n).mother(2)

	  if (NOriginalPartonFound[countZ] == 0):
	    idparton_first[countZ] = part.mother(n).mother(n2).pdgId()
	  elif (NOriginalPartonFound[countZ] == 1):
            idparton_second[countZ] = part.mother(n).mother(n2).pdgId()
	  NOriginalPartonFound[countZ] += 1

	  if abs(part.mother(n).mother(n2).pdgId()) < 7 and part.mother(n).mother(n2).mother().pdgId() == 2212:
	    countquarks[countZ] += 1
	  if part.mother(n).mother(n2).pdgId() == 21 and part.mother(n).mother(n2).mother().pdgId() == 2212:
	    countgluons[countZ] += 1
      
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


  return output

def Delta(par1,par2):
  delta_phi=abs(par2.phi()-par1.phi())
  if delta_phi>pi:
    delta_phi=(2*pi)-delta_phi;
  delta=sqrt((delta_phi)**2 + (par1.eta()-par2.eta())**2)
  return delta

def DumpLHCOEvent(file, event, dijet, bestZcandidate, met, numberOfInteractions=None):

  """Dump informations about a given event in the LHCO format for MadWeight"""
  # output must be specified
  if file is None:
    print "Output must be specified. Set file argument to the file object opened for writing"
    return
              
  if event is None:
    print "DumpLHCOEvent could not find event"
    return

  if dijet[1] is None:
    print "DumpLHCOEvent Error: not enough jets"
    return


  b1 = _JECuncertainty.jet(dijet[0])
  b2 = _JECuncertainty.jet(dijet[1])
  
  # print event in lhco format
  PrintEvent(event,file)
  PrintLepton(bestZcandidate.daughter(0),file,1)
  PrintLepton(bestZcandidate.daughter(1),file,2)
  PrintJet(dijet[0],b1, file,3)
  PrintJet(dijet[1],b2, file,4)
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

def PrintJet(jet, jet4v, file, index) :
  file.write(str(index) + ' 4 ' + str(jet.eta()) + ' ' + str(jet.phi()) + ' ' + str(jet4v.Pt()) + ' ' + str(jet.mass()) + ' ' + str(jet.charge()) + ' 2 0 0 0 \n')

def PrintMET(met, file,numberOfInteractions ,index) :
  file.write(str(index) + ' 6 ' + str(met.eta()) + ' ' + str(met.phi()) + ' ' + str(met.pt()) + ' 0 0 0 ' + str(numberOfInteractions) +' 0 0 \n')

###############################
### Proxy for eventCategory ###
###############################

def dumpAll(stage=12, muChannel=False, isData=False, path="/home/fynu/vizangarciaj/scratch/DYJets_Summer11_fewfiles/",fileAll="outCMStoLHCO_",RootFile="outCMStoLHCO_",numb=None, Nfiles=10, Suffix=""):

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
  
  import glob 
  

  # read data
  
  #dirList=os.listdir(path)
  dirList=glob.glob(path+"*")
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
  files=glob.glob(path+"*")
  events = Events (files)

   # To be check to load MeT type 1 + phi correction
  jetalllabel="patJets"
  labelElectron = zbblabel.electronlabel
  labelMuon = zbblabel.muonlabel

  RhoHandle = Handle("double")
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
  iEventLoop=0
  for event in events:
    #if iEventLoop > 400: break;
    #if isZbEvent(genparts)==False:
     # continue
      
    #print '----------------------- New Event -------------------------'
    event.getByLabel (zbblabel.jetlabel,jetHandle)
    event.getByLabel (jetalllabel,jetallHandle)
    event.getByLabel (zbblabel.metlabel,metHandle)
    event.getByLabel ("patType1SCorrectedPFMet",noPUcorrmetHandle)
    event.getByLabel (zbblabel.zmumulabel,zmuHandle)
    event.getByLabel (zbblabel.zelelabel,zeleHandle)
    event.getByLabel (labelElectron,electronHandle)
    event.getByLabel (labelMuon,muonHandle)
    event.getByLabel (zbblabel.vertexlabel, PrimaryVertexHandle)
    event.getByLabel("kt6PFJetsForIsolation","rho",RhoHandle)
    run = event.eventAuxiliary().run()

    runNumber[0] = event.eventAuxiliary().run()
    eventNumber[0] = event.eventAuxiliary().id().event()
    
    jets = jetHandle.product()
    met = metHandle.product()
    noPUcorrmet = noPUcorrmetHandle.product()
    zCandidatesMu = zmuHandle.product()
    zCandidatesEle = zeleHandle.product()
    vertices = PrimaryVertexHandle.product()
    muons = muonHandle.product()
    electrons = electronHandle.product()
    rho = RhoHandle.product()
    
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
      event.getByLabel (zbblabel.genlabel,genpartHandle)
      event.getByLabel (PULabel,PUHandle)
      PU= PUHandle.product()
      genparts = genpartHandle.product()
      #Number of pile up interactions variable is duplicated. I should remove one
      numberOfInteractions = PUHandle.product()[0].getPU_NumInteractions()
      Pile_up[0] = PUHandle.product()[0].getPU_NumInteractions()

      if isZbEvent(genparts)==True:
	isZb[0] = 1
      if isZcEvent(genparts)==True:
	isZc[0] = 1
      if isZlEvent(genparts)==True:
	isZl[0] = 1
      
    else: #It looks that for MC loading the trigger branch produces a crash
      event.getByLabel(zbblabel.triggerlabel,trigInfoHandle)
      triggerInfo = trigInfoHandle.product()

    #We require the event selection given by the variable "stage"
    #We require in addition at least one Z candidate and 2 jets regardless the value we chose for "stage"

    #Start procedure selection
    categTuple=eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, vertices,jets, met, run ,muChannel, btagAlgo, event.eventAuxiliary().luminosityBlock())   #defalut mass windows = 15
    
    if isInCategory(stage, categTuple) and isGoodMet_Sig(met[0]):
      

      bestZ = findBestCandidate(muChannel, vertex, zCandidatesMu, zCandidatesEle)
      dijet = findDijetPair(jets, bestZ)  
      
      DumpLHCOEvent(out_file_INCL, event, dijet, bestZ, met, numberOfInteractions)

      if (not dijet[1] is None) and (not dijet[0] is None):
        l1=bestZ.daughter(0)
        l2=bestZ.daughter(1)

        dphi=dijet[0].phi()-dijet[1].phi()
        if(dphi>pi):
          dphi= (2*pi) - dphi
        DR=sqrt(pow(dijet[0].eta()-dijet[1].eta(),2)+pow(dphi,2))

        b1 = _JECuncertainty.jet(dijet[0])
	b2 = _JECuncertainty.jet(dijet[1])
	bb = b1 + b2
	bbM[0] = bb.M()
	
	llM[0] = bestZ.mass()
	
        E_j1[0]=b1.E() 
        E_j2[0]=b2.E()
        Eta_j1[0]=dijet[0].eta()
        Eta_j2[0]=dijet[1].eta()
        phi_j1[0]=dijet[0].phi()
        phi_j2[0]=dijet[1].phi()
        Pt_j1[0]=b1.Pt()
        Pt_j2[0]=b2.Pt()
	if btagAlgo == "SSV":
	  btag_j1[0]=dijet[0].bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
	  btag_j2[0]=dijet[1].bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
        else:
	  btag_j1[0]=dijet[0].bDiscriminator("combinedSecondaryVertexBJetTags")
	  btag_j2[0]=dijet[1].bDiscriminator("combinedSecondaryVertexBJetTags")
        
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
            HE = isBJet(jet,"HE",btagAlgo)
            HP = isBJet(jet,"HP",btagAlgo)
            if HE: nBjetsHE[0] += 1
            if HP: nBjetsHP[0] += 1
            if HE and HP: nBjetsHEHP[0] +=1

        #some gen level information (it requires looping)
	if isData==False:
	  codeDYprod[0] = CodeDYprod(genparts)

        #only fill tree if 2 bjets for the moment
	#print " Met = ", Met[0], " Met_phi = ", Met_phi[0], " Met_sig = ", Met_sig[0]
	#print " nJets = ", nJets[0], " nBJetsHE = ", nBjetsHE[0], " nBJetsHP = ", nBjetsHP[0], "nBJetsHEHP = ", nBjetsHEHP[0]
	#print " Pile_up = ", Pile_up[0], "isZb = ", isZb[0], " isZc = ", isZc[0], " isZl = ", isZl[0]
	#print " btag_j1 = ", btag_j1[0], " btag_j2 = ", btag_j2[0]
	
	#print "[", runNumber[0], ", ", eventNumber[0], "]"
        

	
        tree1.Fill()

    iEventLoop += 1              
  # close file
  out_file_INCL.close()
  f.Write()
  f.Close()


for num, arg in enumerate(sys.argv):
  print num, arg


dumpAll(path=path[channel], isData=checkTrigger[channel], numb=sys.argv[2], Nfiles=sys.argv[3], Suffix=channel+sys.argv[4], stage=10)
    
