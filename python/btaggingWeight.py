
from eventSelection import *
# we use the class from Andrea, with an additional method to add jets to the "event"
# that class also fills automatically the efficiency and SF.
import ROOT
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
ROOT.gSystem.Load("libUserCodezbb_louvain.so")

class btaggingWeight:
  """compute the event weight based on btagging SF"""

  def __init__(self,jmin,jmax,workingPoint="HE", algo="SSV", file="../testfiles/performance_ssv.root"):
    self.engine=ROOT.BTagWeight(jmin,jmax)
    self.workingPoint=workingPoint
    self.algo=algo
    self.jetHandle = Handle ("vector<pat::Jet>")
    self.zmuHandle = Handle ("vector<reco::CompositeCandidate>")
    self.zeleHandle = Handle ("vector<reco::CompositeCandidate>")
    self.myJetSet = ROOT.JetSet(file)

  def weight(event,muChannel):
    # retrieve the objects (jets and Z candidates)
    event.getByLabel("cleanPatJets",jetHandle)
    event.getByLabel("Ztighttight",zmuHandle)
    event.getByLabel("Zelel",zeleHandle)
    jets = self.jetHandle.product()
    zCandidatesMu  = self.zmuHandle.product()
    zCandidatesEle = self.zeleHandle.product()    
    Z = findBestCandidate(muChannel, zCandidatesMu, zCandidatesEle)
    # initialize counters
    self.myJetSet.reset()
    ntags = 0
    # algo definition used in the C++ library
    if self.algo=="HE" : algo = 1 
    else algo = 2
    # retrieve the jets
    for jet in jets:
      # apply selection
      if not isGoodJet(jet, Z): continue
      # check flavor
      flavor = jet.getPartonFlavor()
      # check btagging
      if isBJet(jet,self.workingPoint,self.algo): ntags += 1
      # add to the jetset class
      self.myJetSet.add(flavor,jet.et(),jet.eta())
    return self.getWeight(self.myJetSet,algo,ntags)

  def getWeight(jetset, algo, ntags):
    return self.engine.weight(jetset, algo, ntags)

