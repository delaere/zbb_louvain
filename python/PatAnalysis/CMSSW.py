import ROOT
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
ROOT.gSystem.Load("libPhysicsToolsUtilities.so")
from types import MethodType
import libPyROOT as _root
from ROOT import TLorentzVector,TVector3
from math import sin

#####################################################
### Definition of the string conversion methods   ###
#####################################################

# reco::Vertex
def _reco_vertex__str__(self):
  theString =  "Vertex position: (%f,%f,%f) +/- (%f,%f,%f)\n" % (self.x(), self.y(),self.z(),self.xError(),self.yError(),self.zError())
  theString += "  Number of tracks: %d\n" % self.tracksSize()
  theString += "  chi2/ndof: %f/%d\n" % (self.chi2(),self.ndof())
  return theString
ROOT.reco.Vertex.__str__ = MethodType(_reco_vertex__str__,None,ROOT.reco.Vertex)

# pat::MET 
def _pat_met__str__(self):
  theString = "Missing Et: %f at phi= %f with a significance of %f\n" % (self.et(),self.phi(),self.significance())
  return theString
ROOT.pat.MET.__str__ = MethodType(_pat_met__str__,None,ROOT.pat.MET)

# pat::Jet
def _pat_Jet__str__(self):
  theString =  "Jet candidate\n"
  theString += "  (pt, eta, phi) = (%f,%f,%f)\n" % (self.pt(), self.eta(), self.phi())
  theString += "  mass = %f GeV\n" % self.mass()
  theString += "  charge: %d\n" % self.charge()
  theString += "  p = %f GeV; mt = %f GeV\n" % (self.p(), self.mt())
  theString += "  nhf=%f\n" % (( self.neutralHadronEnergy() + self.HFHadronEnergy() ) / self.energy())
  theString += "  nef=%f\n" % (self.neutralEmEnergyFraction())
  theString += "  nconstituents=%d\n" % (self.numberOfDaughters())
  theString += "  chf=%f\n" % (self.chargedHadronEnergyFraction())
  theString += "  nch=%d\n" % (self.chargedMultiplicity())
  theString += "  cef=%f\n" % (self.chargedEmEnergyFraction())
  theString += "  B-tagging information:\n"
  theString += "     SSVHE: %f\n" % self.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
  theString += "     SSVHP: %f\n" % self.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
  taginfo = self.tagInfoSecondaryVertex("secondaryVertex")
  if not taginfo is None and self.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")>0:
    sv = taginfo.secondaryVertex(0)
    if not sv is None:
      distance = taginfo.flightDistance(0,True)
      dir = taginfo.flightDirection(0)
      dirv = TVector3(dir.x(),dir.y(),dir.z())
      dirj = TVector3(self.px(),self.py(),self.pz())
      theString += "     details about the secondary vertex:\n"
      theString += "     * number of tracks: %d\n" % sv.tracksSize()
      theString += "     * chi2: %f\n" % sv.chi2()
      theString += "     * distance: %f+/-%f\n" % (distance.value(),distance.error())
      theString += "     * distance significance: %f\n" % distance.significance()
      theString += "     * flight direction: %f,%f,%f\n" % (dir.x(),dir.y(),dir.z())
      theString += "     * dR(jet): %f\n" % dirv.DeltaR(dirj)
      theString += "     * mass: %f\n" % sv.p4().M()
  return theString
ROOT.pat.Jet.__str__ = MethodType(_pat_Jet__str__,None,ROOT.pat.Jet)

# pat::Electron
def _pat_Electron__str__(self):
  theString =  "Electron candidate\n"
  theString += "  (pt, eta, phi) = (%f,%f,%f)\n" % (self.pt(), self.eta(), self.phi())
  theString += "  mass = %f GeV\n" % self.mass()
  theString += "  charge: %d\n" % self.charge()
  theString += "  p = %f GeV; mt = %f GeV\n" % (self.p(), self.mt())
  scEt = (self.ecalEnergy()*sin(self.theta()))
  superclusterEta = abs(self.superCluster().eta())
  theString += "  Number of missing hits: %d\n" % self.gsfTrack().numberOfLostHits()
  theString += "  SuperCluster Et: %f\n" % scEt
  theString += "  HCAL isolation: %f\n"  % (self.dr03HcalTowerSumEt()/scEt)
  theString += "  ECAL isolation: %f\n"  % (self.dr03EcalRecHitSumEt()/scEt)
  theString += "  Tk   isolation: %f\n"  % (self.dr03TkSumPt()/scEt)
  theString += "  H over E: %f\n" % self.hadronicOverEm()
  theString += "  dphi: %f\n" % self.deltaPhiEleClusterTrackAtCalo()
  theString += "  deta: %f\n" % self.deltaEtaEleClusterTrackAtCalo()
  theString += "  inin: %f\n" % self.scSigmaIEtaIEta()
  theString += "  d0: %f\n"   % abs(self.dB())
  theString += "  supercluster eta: %f\n" % self.superCluster().eta()
  if superclusterEta<1.4442 or (superclusterEta>1.566 and superclusterEta<2.5 ):
    theString += " => in fiducial region\n"
  else:
    theString += " => out of fiducial region\n"
  return theString
ROOT.pat.Electron.__str__ = MethodType(_pat_Electron__str__,None,ROOT.pat.Electron)

# pat::Muon
def _pat_Muon__str__(self):
  theString =  "Muon candidate\n"
  theString += "  (pt, eta, phi) = (%f,%f,%f)\n" % (self.pt(), self.eta(), self.phi())
  theString += "  mass = %f GeV\n" % self.mass()
  theString += "  charge: %d\n" % self.charge()
  theString += "  p = %f GeV; mt = %f GeV\n" % (self.p(), self.mt())
  if self.isTrackerMuon():
    theString += "  Number of hits (all, pixels, strips): %d,%d,%d\n" % (self.innerTrack().numberOfValidHits(),
                                                                         self.innerTrack().hitPattern().numberOfValidPixelHits(),
                                                                         self.innerTrack().hitPattern().numberOfValidStripHits())
  if self.isGlobalMuon():
    theString += "  Number of muon hits: %d\n" % self.globalTrack().hitPattern().numberOfValidMuonHits()
  if self.isTrackerMuon() and self.isGlobalMuon():
    theString += "  Chi2: %f\n" % self.normChi2()
  theString += "  Isolation: (%f+%f)/pt = %f\n" % (self.trackIso(),self.caloIso(),(self.trackIso()+self.caloIso())/self.pt())
  return theString
ROOT.pat.Muon.__str__ = MethodType(_pat_Muon__str__,None,ROOT.pat.Muon)

# reco::CompositeCandidate
def _reco_CompositeCandidate__str__(self):
  theString  = "  (pt, eta, phi) = (%f,%f,%f)\n" % (self.pt(), self.eta(), self.phi())
  theString += "  mass = %f GeV\n" % self.mass()
  theString += "  charge: %d\n" % self.charge()
  theString += "  p = %f GeV; mt = %f GeV\n" % (self.p(), self.mt())
  return theString
ROOT.reco.CompositeCandidate.__str__ = MethodType(_reco_CompositeCandidate__str__,None,ROOT.reco.CompositeCandidate)

# pat::TriggerEvent
def _pat_TriggerEvent__str__(self):
  theString  = "  Fill %d, Orbit %d"%(self.lhcFill(),self.turnCount())
  theString += "  LHC beam mode: %d\n"%self.beamMode()
  theString += "  LHC beam momentum:%d\n"%self.beamMomentum()
  theString += "  LHC master status:%d\n"%self.bstMasterStatus()
  theString += "  LHC beam intensity: beam 1:%d beam2:%d\n"%(self.intensityBeam1(),self.intensityBeam2())
  theString += "  CMS magnet current averaged over run: %f\n" % self.bCurrentAvg()
  theString += "  L1 trigger menu: %s\n"%self.nameL1Menu()
  theString += "  HLT trigger menu: %s\n"%self.nameHltTable()
  theString += "  Flags: Accept:%d Error:%d PhysicsDeclared:%d Running:%d\n"%(self.wasAccept(),self.wasError(),self.wasPhysDecl(),self.wasRun())
  return theString
ROOT.pat.TriggerEvent.__str__ = MethodType(_pat_TriggerEvent__str__,None,ROOT.pat.TriggerEvent)

# PileupSummaryInfo
def _PileupSummaryInfo__str__(self):
  theString  = "  Bunch crossing: %d\n"%self.getBunchCrossing()
  theString += "  Number of (true) PU interactions: (%d) %d\n"%(self.getTrueNumInteractions(),self.getPU_NumInteractions())
  for pu in range(self.getPU_ntrks_highpT().size()):
    theString += "    PU interaction %d:\n"%pu
    if pu<self.getPU_instLumi().size():
      theString += "      Instantaneous luminosity: %f\n"%self.getPU_instLumi()[pu]
    theString += "      Z position: %f\n"%self.getPU_zpositions()[pu]
    theString += "      Number of high (low) Pt tracks: %d (%d)\n"%(self.getPU_ntrks_highpT()[pu],self.getPU_ntrks_lowpT()[pu])
    theString += "      Total Pt of high (low) Pt tracks: %f (%f)\n"%(self.getPU_sumpT_highpT()[pu],self.getPU_sumpT_lowpT()[pu])
  return theString
ROOT.PileupSummaryInfo.__str__ = MethodType(_PileupSummaryInfo__str__,None,ROOT.PileupSummaryInfo)

# reco::GenJet
def _reco_GenJet__str__(self):
  return getattr(self,"print")()
ROOT.reco.GenJet.__str__ = MethodType(_reco_GenJet__str__,None,ROOT.reco.GenJet)

# GenEventInfoProduct
def _GenEventInfoProduct__str__(self):
  theString  = "  alphaQCD=%f; alphaQED=%f"%(self.alphaQCD(),self.alphaQED())
  theString += "  qScale=%f\n"%self.qScale()
  theString += "  signalProcessID: %d\n"%self.signalProcessID()
  theString += "  MC weight: %d\n"%self.weight()
  for w in range(self.weights().size()):
    theString += "    MC weight from list: %f\n"%self.weights()[w]
  return theString
ROOT.GenEventInfoProduct.__str__ = MethodType(_GenEventInfoProduct__str__,None,ROOT.GenEventInfoProduct)


#####################################################
### Definition of additional ROOT methods         ###
#####################################################

def _lorentzVector__str__( self ):
  theString =  "(pt, eta, phi) = (%f,%f,%f)\n" % (self.Pt(), self.Eta(), self.Phi())
  theString += "mass = %f, p = %f, mt = %f\n"  % (self.M(), self.P(), self.Mt())
  return theString

_root.MakeRootClass( "TLorentzVector" ).__str__    = _lorentzVector__str__

