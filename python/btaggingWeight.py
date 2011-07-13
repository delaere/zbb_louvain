
from eventSelection import *
# we use the class from Andrea, with an additional method to add jets to the "event"
# that class also fills automatically the efficiency and SF (tabulated).
from ROOT import gSystem
gSystem.Load( '../src/BTagWeight_cpp.so' )
from ROOT import BTagWeight,JetSet

class btaggingWeight:
  """compute the event weight based on btagging SF"""

  def __init__(self,jmin,jmax,workingPoint="HE", algo="SSV"):
    self.engine=BTagWeight(jmin,jmax)
    self.workingPoint=workingPoint
    self.algo=algo
    self.jetHandle = Handle ("vector<pat::Jet>")
    self.zmuHandle = Handle ("vector<reco::CompositeCandidate>")
    self.zeleHandle = Handle ("vector<reco::CompositeCandidate>")

  def weight(event,muChannel):
    event.getByLabel("cleanPatJets",jetHandle)
    event.getByLabel("Ztighttight",zmuHandle)
    event.getByLabel("Zelel",zeleHandle)
    jets = self.jetHandle.product()
    zCandidatesMu  = self.zmuHandle.product()
    zCandidatesEle = self.zeleHandle.product()    
    Z = findBestCandidate(muChannel, zCandidatesMu, zCandidatesEle)
    myJetSet = ROOT.JetSet(2011);
    ntags = 0
    # retrieve the jets
    for jet in jets:
      # apply selection
      if not isGoodJet(jet, Z): continue
      # check flavor
      flavor = jet.getPartonFlavor()
      # check btagging
      if isBJet(jet,self.workingPoint,self.algo): ntags += 1
      # add to the jetset class
      algo = 1 # 1=SSVHEM, 2=SSVHPT
      myJetSet.add(flavor,algo,jet.pt(),jet.eta())
    return self.getWeight(myJetSet,ntags)

  def getWeight(jetset, ntags):
    return self.engine.weight(jetset, ntags)

