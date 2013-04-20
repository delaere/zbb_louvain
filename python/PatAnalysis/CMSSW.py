import ROOT
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
ROOT.gSystem.Load("libPhysicsToolsUtilities.so")
import libPyROOT as _root
from ROOT import TLorentzVector,TVector3

#####################################################
### Definition of the string conversion methods   ###
#####################################################

# reco::Vertex
def _reco_vertex__str__(self):
  theString =  "Vertex position: (%f,%f,%f) +/- (%f,%f,%f)\n" % (self.x(), self.y(),self.z(),self.xError(),self.yError(),self.zError())
  theString += "  Number of tracks: %d\n" % self.tracksSize()
  theString += "  chi2/ndof: %f/%d\n" % (self.chi2(),self.ndof())
  return theString
ROOT.reco.Vertex
_root.MakeRootClass( "reco.Vertex" ).__str__    = _reco_vertex__str__

# pat::MET 
def _pat_met__str__(self):
  theString = "Missing Et: %f at phi= %f with a significance of %f\n" % (self.et(),self.phi(),self.significance())
  return theString
ROOT.pat.MET
_root.MakeRootClass( "pat.MET" ).__str__    = _pat_met__str__

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
ROOT.pat.Jet
_root.MakeRootClass( "pat.Jet" ).__str__    = _pat_Jet__str__

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
  theString += "  HCAL isolation: %f\n"  % self.dr03HcalTowerSumEt()/scEt
  theString += "  ECAL isolation: %f\n"  % self.dr03EcalRecHitSumEt()/scEt
  theString += "  Tk   isolation: %f\n"  % self.dr03TkSumPt()/scEt
  theString += "  H over E: %f\n" % self.hadronicOverEm()
  theString += "  dphi: %f\n" % self.deltaPhiEleClusterTrackAtCalo()
  theString += "  deta: %f\n" % self.deltaEtaEleClusterTrackAtCalo()
  theString += "  inin: %f\n" % self.scSigmaIEtaIEta()
  theString += "  d0: %f\n"   % abs(self.dB())
  theString += "  supercluster eta: %f\n" % self.superCluster().eta(),
  if superclusterEta<1.4442 or (superclusterEta>1.566 and superclusterEta<2.5 ):
    theString += " => in fiducial region\n"
  else:
    theString += " => out of fiducial region\n"
  return theString
ROOT.pat.Electron
_root.MakeRootClass( "pat.Electron" ).__str__    = _pat_Electron__str__

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
ROOT.pat.Muon
_root.MakeRootClass( "pat.Muon" ).__str__    = _pat_Muon__str__

# reco::CompositeCandidate
def _reco_CompositeCandidate__str__(self):
  theString  = "  (pt, eta, phi) = (%f,%f,%f)\n" % (self.pt(), self.eta(), self.phi())
  theString += "  mass = %f GeV\n" % self.mass()
  theString += "  charge: %d\n" % self.charge()
  theString += "  p = %f GeV; mt = %f GeV\n" % (self.p(), self.mt())
  return theString
ROOT.reco.CompositeCandidate
_root.MakeRootClass( "reco.CompositeCandidate" ).__str__    = _reco_CompositeCandidate__str__

#####################################################
### Definition of additional ROOT methods         ###
#####################################################

def _lorentzVector__str__( self ):
  theString =  "(pt, eta, phi) = (%f,%f,%f)\n" % (self.Pt(), self.Eta(), self.Phi())
  theString += "mass = %f, p = %f, mt = %f\n"  % (self.M(), self.P(), self.Mt())
  return theString

_root.MakeRootClass( "TLorentzVector" ).__str__    = _lorentzVector__str__


