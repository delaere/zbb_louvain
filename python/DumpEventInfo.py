from datetime import datetime
from math import sin
import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from eventSelection import eventCategories, eventCategory, jetId

def DumpEventInfo(fwevent=None, run=None, event=None, lumi=None, path=""):
  """Dump informations about a given event"""
  # in case no fwevent is provided, find it using run,event,(lumi)
  if fwevent is None:
    if (run is None) or (event is None):
      print "DumpEventInfo Error: either pass a fwlite event or give both run and event number"
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
      DumpEventInfo(fwevent)
    else:
      print "Event not found."
    return
  # in case a fwevent is provided, use it
  PrintEvent(fwevent)
  # load objects
  electronHandle = Handle ("vector<pat::Electron>")
  muonHandle = Handle ("vector<pat::Muon>")
  jetHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  fwevent.getByLabel ("matchedElectrons",electronHandle)
  fwevent.getByLabel ("matchedMuons",muonHandle)
  fwevent.getByLabel ("cleanPatJets",jetHandle)
  fwevent.getByLabel ("patMETsPF",metHandle)
  fwevent.getByLabel ("Ztighttight",zmuHandle)
  fwevent.getByLabel ("Zelel",zeleHandle)
  electrons = electronHandle.product()
  muons = muonHandle.product()
  jets = jetHandle.product()
  met = metHandle.product()
  zCandidatesMu = zmuHandle.product()
  zCandidatesEle = zeleHandle.product()
  # loop on objects
  for muon in muons:
    PrintMuon(muon)
  for electron in electrons:
    PrintElectron(electron)
  for jet in jets:
    PrintJet(jet)
  PrintMET(met[0])
  for z in zCandidatesMu:
    PrintCandidate("Z->mumu",z)
  for z in zCandidatesEle:
    PrintCandidate("Z->elel",z)
  # additional composite candidates from the event
  # TODO: Zb candidate is missing... we should compute it by hand
  dijetHandle = Handle ("vector<reco::CompositeCandidate>")
  zmmbbHandle = Handle ("vector<reco::CompositeCandidate>")
  zeebbHandle = Handle ("vector<reco::CompositeCandidate>")
  fwevent.getByLabel ("bbbar",dijetHandle)
  fwevent.getByLabel ("Zeebb",zeebbHandle)
  fwevent.getByLabel ("Zmmbb",zmmbbHandle)
  dijets = dijetHandle.product()
  zeebbs = zeebbHandle.product()
  zmmbbs = zmmbbHandle.product()
  for dijet in dijets:
    PrintCandidate("dijet",dijet)
  for zeebb in zeebbs:
    PrintCandidate("Zbb",zb)
  for zmmbb in zmmbbs: 
    PrintCandidate("Zbb",zbb)

def PrintEvent(event) :
  print "================================================================="
  print "Run", event.eventAuxiliary().run(), "Event", event.eventAuxiliary().id().event(), "Lumi", event.eventAuxiliary().luminosityBlock()
  #to print the category, one needs the input collections
  #category = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, self.muChannel)
  #print "Passes selection level", category
  time = event.eventAuxiliary().time().unixTime()
  dtime = datetime.fromtimestamp(time)
  print "Recorded on", dtime.strftime("%Y-%m-%d %H:%M:%S")
  print "-----------------------------------------------------------------"

def PrintMuon(muon) :
  print "-----------------------------------------------------------------"
  PrintCandidate("muon",muon,False)
  if muon.isTrackerMuon():
    print "  Number of hits (all, pixels, strips):",muon.innerTrack().numberOfValidHits(),muon.innerTrack().hitPattern().numberOfValidPixelHits(),muon.innerTrack().hitPattern().numberOfValidStripHits()
  if muon.isGlobalMuon():
    print "  Number of muon hits:",muon.globalTrack().hitPattern().numberOfValidMuonHits()
  if muon.isTrackerMuon() and muon.isGlobalMuon():
    print "  Chi2:",muon.normChi2()
  print "  Isolation: (",muon.trackIso(),"+",muon.caloIso(),")/pt = ",(muon.trackIso()+muon.caloIso())/muon.pt()
  print "-----------------------------------------------------------------"

def PrintElectron(electron) :
  print "-----------------------------------------------------------------"
  PrintCandidate("electron",electron,False)
  print "  Electron id:",electron.electronID("simpleEleId85relIso")
  print "  Number of missing hits:",electron.gsfTrack().numberOfLostHits()
  scEt = (electron.ecalEnergy()*sin(electron.theta()))
  print "  SuperCluster Et:",scEt
  print "  HCAL isolation:",electron.dr03HcalTowerSumEt()/scEt
  print "  ECAL isolation:",electron.dr03EcalRecHitSumEt()/scEt
  print "  Tk   isolation:",electron.dr03TkSumPt()/scEt
  print "  H over E:",electron.hadronicOverEm()
  print "  dphi:",electron.deltaPhiEleClusterTrackAtCalo()
  print "  deta:",electron.deltaEtaEleClusterTrackAtCalo()
  print "  inin:",electron.scSigmaIEtaIEta()
  print "  d0:",abs(electron.dB())
  print "-----------------------------------------------------------------"

def PrintJet(jet) :
  print "-----------------------------------------------------------------"
  PrintCandidate("jet",jet,False)
  print "  nhf=",(( jet.neutralHadronEnergy() + jet.HFHadronEnergy() ) / jet.energy())
  print "  nef=",(jet.neutralEmEnergyFraction())
  print "  nconstituents=",(jet.numberOfDaughters())
  print "  chf=",(jet.chargedHadronEnergyFraction())
  print "  nch=",(jet.chargedMultiplicity())
  print "  cef=",(jet.chargedEmEnergyFraction())
  if jetId(jet,"tight"): jetid=3
  elif jetId(jet,"medium"): jetid=2
  elif jetId(jet,"loose"): jetid=1
  else: jetid=0
  print "  Jet ID:",jetid
  print "  B-tagging information:"
  print "     SSVHE:",jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
  print "     SSVHP:",jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
  print "-----------------------------------------------------------------"

def PrintMET(met) :
  print "-----------------------------------------------------------------"
  print "Missing Et:",met.et(),"at phi=",met.phi()
  print "-----------------------------------------------------------------"

def PrintCandidate(label, candidate, line=True) :
  if line:
    print "-----------------------------------------------------------------"
  print label, "candidate"
  print "  (pt, eta, phi) = (", candidate.pt(), ",", candidate.eta(), ",", candidate.phi(), ")"
  print "  mass =", candidate.mass()
  print "  charge:", candidate.charge()
  print "  p =", candidate.p(), "mt = ", candidate.mt()
  #if candidate.vertex()!=0:
  #  print "  vertex: (",candidate.vertex().x(),",",candidate.vertex().y(),",",candidate.vertex().z(),")"
  if line:
    print "-----------------------------------------------------------------"

