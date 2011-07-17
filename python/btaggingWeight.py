
from eventSelection import *
# we use the class from Andrea, with an additional method to add jets to the "event"
# that class also fills automatically the efficiency and SF.
import ROOT
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
ROOT.gSystem.Load("libUserCodezbb_louvain.so")

class btaggingWeight:
  """compute the event weight based on btagging SF"""

  def __init__(self,jmin1,jmax1,jmin2,jmax2, file="../testfiles/performance_ssv.root"):
    self.engine=ROOT.BTagWeight(jmin1,jmax1,jmin2,jmax2)
    self.jetHandle = Handle ("vector<pat::Jet>")
    self.zmuHandle = Handle ("vector<reco::CompositeCandidate>")
    self.zeleHandle = Handle ("vector<reco::CompositeCandidate>")
    self.myJetSet = ROOT.JetSet(file)

  def setLimits(jmin1,jmax1,jmin2,jmax2):
    self.engine.setLimits(jmin1,jmax1,jmin2,jmax2)

  def setMode(mode):
    if mode=="HE": self.engine.setLimits(1,999,0,999)
    elif mode=="HP": self.engine.setLimits(0,999,1,999)
    elif mode=="HEHE": self.engine.setLimits(2,999,0,999)
    elif mode=="HEHP": self.engine.setLimits(1,999,1,999)
    elif mode=="HPHP": self.engine.setLimits(0,999,2,999)
    else: 
      print "btaggingWeight.py: Unknown mode:",mode
      self.engine.setLimits(0,999,0,999)
    
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
    ntagsHE = 0
    ntagsHP = 0
    # retrieve the jets
    for jet in jets:
      # apply selection
      if not isGoodJet(jet, Z): continue
      # check flavor
      flavor = jet.getPartonFlavor()
      # check btagging
      if isBJet(jet,"HP","SSV"): ntagsHP += 1
      if isBJet(jet,"HE","SSV"): ntagsHE += 1
      # add to the jetset class
      self.myJetSet.add(flavor,jet.et(),jet.eta())
    return self.getWeight(self.myJetSet,ntagsHE,ntagsHP)

  def getWeight(jetset, ntags1, ntags2):
    return self.engine.weight2(jetset, ntags1, ntags2)

