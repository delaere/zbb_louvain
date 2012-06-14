from itertools import combinations
from datetime import datetime
from math import sin
import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from eventSelection import jetId, findBestCandidate, isGoodJet, isBJet, isGoodElectron, isGoodMuon, eventCategory
from zbbCommons import zbblabel

def DumpEventInfo(fwevent=None, run=None, event=None, lumi=None, path="../testfiles/"):
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
  vertexHandle = Handle ("vector<reco::Vertex>")
  electronHandle = Handle ("vector<pat::Electron>")
  muonHandle = Handle ("vector<pat::Muon>")
  jetHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  trigInfoHandle = Handle ("pat::TriggerEvent")
  fwevent.getByLabel (zbblabel.electronlabel,electronHandle)
  fwevent.getByLabel (zbblabel.muonlabel,muonHandle)
  fwevent.getByLabel (zbblabel.jetlabel,jetHandle)
  fwevent.getByLabel (zbblabel.metlabel,metHandle)
  fwevent.getByLabel (zbblabel.zmumulabel,zmuHandle)
  fwevent.getByLabel (zbblabel.zelelabel,zeleHandle)
  fwevent.getByLabel (zbblabel.vertexlabel,vertexHandle)
  fwevent.getByLabel (zbblabel.triggerlabel,trigInfoHandle)
  triggerInfo = trigInfoHandle.product()
  vertices = vertexHandle.product()
  electrons = electronHandle.product()
  muons = muonHandle.product()
  jets = jetHandle.product()
  met = metHandle.product()
  zCandidatesMu = zmuHandle.product()
  zCandidatesEle = zeleHandle.product()
  #rawjet = jet.correctedJet("Uncorrected")

  # category
  catMu = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, vertices, jets, met, runNumber, muChannel=True, btagging="SSV", massWindow=15.)
  catEle = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, vertices, jets, met, runNumber, muChannel=False, btagging="SSV", massWindow=15.)
  print "Event category info in muon channel:",catMu
  print "Event category info in electron channel:",catEle

  # loop on objects
  print len(vertices), "vertices in the event."
  for vertex in vertices:
    PrintVertex(vertex)
  for muon in muons:
    PrintMuon(muon)
  for electron in electrons:
    PrintElectron(electron)
  for jet in jets:
    #rawjet = jet.correctedJet("L5Flavor")
    PrintJet(jet)
  PrintMET(met[0])
  for z in zCandidatesMu:
    PrintCandidate("Z->mumu",z)
  for z in zCandidatesEle:
    PrintCandidate("Z->elel",z)
  # additional composite candidates from the event
  dijetHandle  = Handle ("vector<reco::CompositeCandidate>")
  zmmbbHandle  = Handle ("vector<reco::CompositeCandidate>")
  zeebbHandle  = Handle ("vector<reco::CompositeCandidate>")
  vertexHandle = Handle ("vector<reco::Vertex>")

  fwevent.getByLabel (zbblabel.bblabel,dijetHandle)
  fwevent.getByLabel (zbblabel.zeebblabel,zeebbHandle)
  fwevent.getByLabel (zbblabel.zmmbblabel,zmmbbHandle)
  fwevent.getByLabel(zbblabel.vertexlabel,self.vertexHandle_)
  dijets = dijetHandle.product()
  zeebbs = zeebbHandle.product()
  zmmbbs = zmmbbHandle.product()
  vertices = self.vertexHandle_.product()
  if vertices.size()>0 :
    vertex = vertices[0]
  else:
    vertex = None

  for dijet in dijets:
    PrintCandidate("dijet",dijet)
  for zeebb in zeebbs:
    PrintCandidate("Zbb",zeebb)
  for zmmbb in zmmbbs: 
    PrintCandidate("Zbb",zmmbb)
  # handcrafted candidates: bb Zb Zbb
  bestZcandidate = findBestCandidate(None,vertex,zCandidatesMu,zCandidatesEle)
  if bestZcandidate is not None:
    for jet in jets:
      if isGoodJet(jet,bestZcandidate) and isBJet(jet,"HP") :
        b = ROOT.TLorentzVector(jet.px(),jet.py(),jet.pz(),jet.energy())
        z = ROOT.TLorentzVector(bestZcandidate.px(),bestZcandidate.py(),bestZcandidate.pz(),bestZcandidate.energy())
        Zb = z+b
        PrintLorentzVector("Zb (HP)",Zb)
    for bbpair in combinations(filter(lambda jet: isGoodJet(jet,bestZcandidate) and isBJet(jet,"HP"),jets),2) :
      b1 = ROOT.TLorentzVector(bbpair[0].px(),bbpair[0].py(),bbpair[0].pz(),bbpair[0].energy())
      b2 = ROOT.TLorentzVector(bbpair[1].px(),bbpair[1].py(),bbpair[1].pz(),bbpair[1].energy())
      bb = b1 + b2
      Zbb = bb+z
      PrintLorentzVector("bb (HP)",bb)
      PrintLorentzVector("zbb (HP)",Zbb)
    for jet in jets:
      if isGoodJet(jet,bestZcandidate) and isBJet(jet,"HE") :
        b = ROOT.TLorentzVector(jet.px(),jet.py(),jet.pz(),jet.energy())
        z = ROOT.TLorentzVector(bestZcandidate.px(),bestZcandidate.py(),bestZcandidate.pz(),bestZcandidate.energy())
        Zb = z+b
        PrintLorentzVector("Zb (HE)",Zb)
    for bbpair in combinations(filter(lambda jet: isGoodJet(jet,bestZcandidate) and isBJet(jet,"HE"),jets),2) :
      b1 = ROOT.TLorentzVector(bbpair[0].px(),bbpair[0].py(),bbpair[0].pz(),bbpair[0].energy())
      b2 = ROOT.TLorentzVector(bbpair[1].px(),bbpair[1].py(),bbpair[1].pz(),bbpair[1].energy())
      bb = b1 + b2
      Zbb = bb+z
      PrintLorentzVector("bb (HE)",bb)
      PrintLorentzVector("zbb (HE)",Zbb)

def PrintEvent(event) :
  print "================================================================="
  print "Run", event.eventAuxiliary().run(), "Event", event.eventAuxiliary().id().event(), "Lumi", event.eventAuxiliary().luminosityBlock()
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
  print "  good muon: ", isGoodMuon(muon,"loose"),isGoodMuon(muon,"tight"),isGoodMuon(muon,"matched")
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
  superclusterEta = abs(electron.superCluster().eta())
  print "  supercluster eta:",electron.superCluster().eta(),
  if superclusterEta<1.4442 or (superclusterEta>1.566 and superclusterEta<2.5 ):
    print " => in fiducial region"
  else:
    print " => out of fiducial region"
  print "  trigger object matches:",electron.triggerObjectMatches().size()
  print "  good electron: ", isGoodElectron(electron,"loose"),isGoodElectron(electron,"tight"),isGoodElectron(electron,"matched")
  print "-----------------------------------------------------------------"

def PrintJet(jet) :
  print "-----------------------------------------------------------------"
  PrintCandidate("jet",jet,False)
  #PrintCandidate("rawjet",rawjet,False)
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
  taginfo = jet.tagInfoSecondaryVertex("secondaryVertex")
  if not taginfo is None and jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")>0 :
    sv = taginfo.secondaryVertex(0)
    if not sv is None:
      print "     details about the secondary vertex:"
      print "     * number of tracks:"
      #, sv.tracksSize()
      print "     * chi2:"
      #,sv.chi2()
      #distance = taginfo.flightDistance(0,True)
      #print "     * distance:", distance.value(), "+/-",distance.error()
      #print "     * distance significance:", distance.significance()
      #dir = taginfo.flightDirection(0)
      #print "     * flight direction:",dir.x(),",",dir.y(),",",dir.z()
      #dirv = ROOT.TVector3(dir.x(),dir.y(),dir.z())
      #dirj = ROOT.TVector3(jet.px(),jet.py(),jet.pz())
      #print "     * dR(jet):",dirv.DeltaR(dirj)
      #print "     * mass:",sv.p4().M()
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

def PrintLorentzVector(label, lorentzVector, line=True) :
  if line:
    print "-----------------------------------------------------------------"
  print label, "candidate"
  print "  (pt, eta, phi) = (", lorentzVector.Pt(), ",", lorentzVector.Eta(), ",", lorentzVector.Phi(), ")" 
  print "  mass =", lorentzVector.M()
  print "  p =", lorentzVector.P(), "mt = ", lorentzVector.Mt()
  if line:
    print "-----------------------------------------------------------------"

def PrintVertex(vertex) :
  print "-----------------------------------------------------------------"
  print "Vertex position: (", vertex.x(), ",", vertex.y(), ",",vertex.z(), ") +/- (",vertex.xError(),",",vertex.yError(),",",vertex.zError(),")"
  print "  Number of tracks:", vertex.tracksSize()
  print "  chi2/ndof:",vertex.chi2(),"/",vertex.ndof()
  print "-----------------------------------------------------------------"

