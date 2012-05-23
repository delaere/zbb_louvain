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
from zbbCommons import zbblabel
from math import *
from ROOT import TFile, TTree, TH1F
from array import array



print sys.argv 


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
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  fwevent.getByLabel ("cleanPatJets",jetHandle)
  fwevent.getByLabel ("patMETsPF",metHandle)
  fwevent.getByLabel ("ZmuMatchedmuMatched",zmuHandle)
  fwevent.getByLabel ("ZelMatchedelMatched",zeleHandle)
  jets = jetHandle.product()
  met = metHandle.product()
  zCandidatesMu = zmuHandle.product()
  zCandidatesEle = zeleHandle.product()
  #find the best z candidate
  bestZcandidate = findBestCandidate(None,zCandidatesMu,zCandidatesEle)
  # loop over jets and print

  bjetp=[]
  for jet in jets:
    #if isGoodJet(jet,bestZcandidate) and isBJet(jet, "HE", "SSV"):
    if isGoodJet(jet,bestZcandidate): #and isBJet(jet, "HE", "SSV"):
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
#def dumpAll(stage=12, muChannel=True, isData=True, path="/home/fynu/vizangarciaj/scratch/DYJets_Summer11_fewfiles/",fileAll="outCMStoLHCO",RootFile="outCMStoLHCO",numb=None, Nfiles=10, Suffix=""):

#data elChannel
def dumpAll(stage=12, muChannel=False, isData=True, path="/home/fynu/vizangarciaj/scratch/DYJets_Summer11_fewfiles/",fileAll="outCMStoLHCO",RootFile="outCMStoLHCO",numb=None, Nfiles=10, Suffix=""):

#MC muChannel
#def dumpAll(stage=12, muChannel=True, isData=False, path="/home/fynu/vizangarciaj/scratch/DYJets_Summer11_fewfiles/",fileAll="outCMStoLHCO",RootFile="outCMStoLHCO",numb=None, Nfiles=10, Suffix=""):

#MC elChannel
#def dumpAll(stage=12, muChannel=False, isData=False, path="/home/fynu/vizangarciaj/scratch/DYJets_Summer11_fewfiles/",fileAll="outCMStoLHCO",RootFile="outCMStoLHCO",numb=None, Nfiles=10, Suffix=""):

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

  isZb =  n.zeros(1, dtype=int) # nbre of primary vertices
  isZc =  n.zeros(1, dtype=int) # nbre of primary vertices
  isZl =  n.zeros(1, dtype=int) # nbre of primary vertices
  Pile_up =  n.zeros(1, dtype=float) # MC pile-up number (not in data)
  nbr_PV =  n.zeros(1, dtype=int) # nbre of primary vertices

  tree1.Branch("runNumber", runNumber, "runNumber/I")
  tree1.Branch("eventNumber", eventNumber, "eventNumber/I")

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

  tree1.Branch("isZb", isZb, "isZb/I")
  tree1.Branch("isZc", isZc, "isZc/I")
  tree1.Branch("isZl", isZl, "isZl/I")
  tree1.Branch("Pile_up", Pile_up, "Pile_up/D")

  tree1.Branch("nbr_PV", nbr_PV, "nbr_PV/I")

  tree1.Branch("nJets", nJets, "nJets/I")
  tree1.Branch("nBjetsHE", nBjetsHE, "nBjetsHE/I")
  tree1.Branch("nBjetsHP", nBjetsHP, "nBjetsHP/I")
  tree1.Branch("nBjetsHEHP", nBjetsHEHP, "nBjetsHEHP/I")
  
  
  

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

  metlabel="patMETsPF"
  jetlabel="cleanPatJets"
  jetalllabel="patJets"
  zmulabel="ZmuMatchedmuMatched"
  zelelabel="ZelMatchedelMatched"
  genpartlabel="genParticles"
  labelElectron = "matchedElectrons"
  labelMuon = "matchedMuons"
  vertexLabel ="goodPV"

  initLabel= "gluonsInit"
  initqLabel= "quarkInit"
  
  jetHandle = Handle ("vector<pat::Jet>")
  jetallHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  trigInfoHandle = Handle ("pat::TriggerEvent")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  muonHandle = Handle ("vector<pat::Muon>")
  electronHandle = Handle ("vector<pat::Electron>")
  genpartHandle =  Handle("std::vector<reco::GenParticle>")
  PrimaryVertexHandle = Handle ("vector<reco::Vertex>")

#  initHandle = Handle ("edm::OwnVector<reco::Candidate,edm::ClonePolicy<reco::Candidate> >")
#  initqHandle = Handle ("edm::OwnVector<reco::Candidate,edm::ClonePolicy<reco::Candidate> >")

  
  PULabel = "addPileupInfo"
  PUHandle= Handle("std::vector<PileupSummaryInfo>")

  qq_event=0
  gg_event=0
  gg_gen_event=0
  qq_gen_event=0

# Event loop
  for event in events:
    #if isZbEvent(genparts)==False:
     # continue
      
    #print '----------------------- New Event -------------------------'
    event.getByLabel (jetlabel,jetHandle)
    event.getByLabel (jetalllabel,jetallHandle)
    event.getByLabel (metlabel,metHandle)
    event.getByLabel (zmulabel,zmuHandle)
    event.getByLabel (zelelabel,zeleHandle)
    #event.getByLabel ("ZmuMatchedmuMatched",zmuHandle)
    #event.getByLabel ("ZelMatchedelMatched",zeleHandle)
    event.getByLabel (labelElectron,electronHandle)
    event.getByLabel (labelMuon,muonHandle)
    event.getByLabel (vertexLabel, PrimaryVertexHandle)
#    event.getByLabel (initLabel , initHandle)
#    event.getByLabel (initqLabel , initqHandle)
                
    run = event.eventAuxiliary().run()

    runNumber[0] = event.eventAuxiliary().run()
    eventNumber[0] = event.eventAuxiliary().id().event()

    jets = jetHandle.product()
    met = metHandle.product()
    zCandidatesMu = zmuHandle.product()
    zCandidatesEle = zeleHandle.product()
#    triggerInfo = trigInfoHandle.product()
    vertices = PrimaryVertexHandle.product()
    muons = muonHandle.product()
    electrons = electronHandle.product()

    #I still don't know how to access the primary vertex
    nbr_PV[0] = -1
	
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

      if isZbEvent(genparts)==True:
	isZb[0] = 1
      if isZcEvent(genparts)==True:
	isZc[0] = 1
      if isZlEvent(genparts)==True:
	isZl[0] = 1

    else: #It looks that for MC loading the trigger branch produces a crash
      event.getByLabel(zbblabel.triggerlabel,trigInfoHandle)
      triggerInfo = trigInfoHandle.product()


    gluon=[]
    quark=[]


    #We require the event selection given by the variable "stage"
    #We require in addition at least one Z candidate and 2 jets regardless the value we chose for "stage"

    #categTuple=eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, run ,muChannel, massWindow=60.)#!!!!!!!!!!!!!!!!!!!!!!!temporary mass window    
    #categTuple=eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, run ,muChannel, massWindow=30.)    
    categTuple=eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, run ,muChannel)    
    #if isInCategory(stage, eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, run ,muChannel)) :
    if isInCategory(stage, categTuple) and  isInCategory( 3, categTuple) and categTuple[3]>1:
    
      
    
      DumpLHCOEvent(event, None, None, None, "", out_file_INCL,numberOfInteractions)
      bestZ = findBestCandidate(None,zCandidatesMu,zCandidatesEle)





      bjetp=[]
      for jet in jets:
        #if isGoodJet(jet,bestZ) and isBJet(jet, "HE", "SSV"):
        if isGoodJet(jet,bestZ):# and isBJet(jet, "HE", "SSV"):
          bjetp+=[jet]
      if len(bjetp)>1:
        dijet = findDijetPair(bjetp, bestZ)  
        l1=bestZ.daughter(0)
        l2=bestZ.daughter(1)

        dphi=dijet[0].phi()-dijet[1].phi()
        if(dphi>pi):
          dphi= (2*pi) - dphi
        DR=sqrt(pow(dijet[0].eta()-dijet[1].eta(),2)+pow(dphi,2))

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

        #only fill tree if 2 bjets for the moment
	#print " Met = ", Met[0], " Met_phi = ", Met_phi[0], " Met_sig = ", Met_sig[0]
	#print " nJets = ", nJets[0], " nBJetsHE = ", nBjetsHE[0], " nBJetsHP = ", nBjetsHP[0], "nBJetsHEHP = ", nBjetsHEHP[0]
	#print " Pile_up = ", Pile_up[0], "isZb = ", isZb[0], " isZc = ", isZc[0], " isZl = ", isZl[0]
	#print " btag_j1 = ", btag_j1[0], " btag_j2 = ", btag_j2[0]
	
	
        tree1.Fill()
              
  # close file
  out_file_INCL.close()
  f.Write()
  f.Close()


for num, arg in enumerate(sys.argv):
  print num, arg

#dumpAll(fileAll=sys.argv[1],file2j=sys.argv[2],RootFile=sys.argv[3],numb=sys.argv[4])
#
dumpAll(path=sys.argv[1], numb=sys.argv[2], Nfiles=sys.argv[3], Suffix=sys.argv[4], stage=3)
    
