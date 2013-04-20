# we use the class from Andrea, with an additional method to add jets to the "event"
# that class also fills automatically the efficiency and SF.
import ROOT
import PatAnalysis.CMSSW
from PatAnalysis.EventSelection import categoryName, goodJets, isBjet
from zbbCommons import zbbfile,zbbsystematics

class BtaggingWeight:
  """compute the event weight based on btagging SF"""

  def __init__(self,jmin1,jmax1,jmin2,jmax2, file=zbbfile.ssvperfData, btagging="CSV"):
    self.engine=ROOT.BTagWeight(jmin1,jmax1,jmin2,jmax2)
    self.myJetSet = ROOT.JetSet(zbbsystematics.SF_running_mode,file)
    self.btagging=btagging

  def setLimits(self,jmin1,jmax1,jmin2,jmax2):
    self.engine.setLimits(jmin1,jmax1,jmin2,jmax2)

  def setMode(self,mode):
    #reminder: in the engine, the HP includes always HE.
    if   mode=="HE": self.engine.setLimits(1,999,0,999)
    elif mode=="HP": self.engine.setLimits(1,999,1,999)
    elif mode=="HEexcl": self.engine.setLimits(1,1,0,1)
    elif mode=="HPexcl": self.engine.setLimits(1,1,1,1)
    elif mode=="HEHE": self.engine.setLimits(2,999,0,999)
    elif mode=="HEHP": self.engine.setLimits(2,999,1,999)
    elif mode=="HPHP": self.engine.setLimits(2,999,2,999)
    else: 
      print "btaggingWeight.py: Unknown mode:",mode
      self.engine.setLimits(0,999,0,999)

  def weight(self,event, category=None, forceMode=None):
    """btag eff weight"""
    # for data, immediately return 1.
    if forceMode is None:
      if category is None:
        catname = ""
      else:
        catname = EventSelection.categoryName(category)
    else catname = forceMode
    Bmode=btaggingWeightMode(catname)
    if event.object().event().eventAuxiliary().isRealData() or Bmode=="None":
      return 1.
    if not Bmode is None: 
      self.setMode(Bmode)
    # catname -> muChannel, eleChannel, or both (not none)
    if catname.find("Electron")==0 : 
      theGoodJets = event.goodJets_ele
    elif catname.find("Muon")==0 :
      theGoodJets = event.goodJets_mu
    else:
      theGoodJets = goodJets(event, muChannel, eleChannel)
    # initialize counters
    self.myJetSet.reset()
    ntagsHE = 0
    ntagsHP = 0
    ntagsNoFlvavorHE = 0
    ntagsNoFlvavorHP = 0
    # retrieve the jets
    for index,jet in enumerate(event.jets):
      # apply selection
      if not theGoodJets[index]: continue
      # check flavor
      flavor = jet.partonFlavour()
      # check btagging
      if isBJet(jet,"HP",self.btagging):
        ntagsHP += 1
        if flavor == 0:
          #if jet.et() > 100. : print "WARNING : "+btagging+"HP tagged jet with no flavor and high transverse energy : ", jet.et(), ", eta : ", jet.eta()
          ntagsNoFlvavorHP += 1
      if isBJet(jet,"HE",self.btagging):
        ntagsHE += 1
        if flavor == 0:
          #if jet.et() > 100. : print "WARNING : "+btagging+"HE tagged jet with no flavor and high transverse energy : ", jet.et(), ", eta : ", jet.eta()
          ntagsNoFlvavorHE += 1
      # add to the jetset class
      self.myJetSet.addJet(zbbsystematics.SF_uncert, flavor,jet.et(),jet.eta())
    #if ntagsNoFlvavorHP>=2 and ntagsNoFlvavorHE<2: print "IMPORTANT WARNING : 2 "+btagging+"HP tagged jets with no flavour !! Event should be checked !! Event number : ", event.event()
    #if ntagsNoFlvavorHE>=2 : print "IMPORTANT WARNING : 2 "+btagging+"HE tagged jets with no flavour !! Event should be checked !! Event number : ", event.event()
    return max(self.getWeight(self.myJetSet,ntagsHE,ntagsHP),0.)

  def getWeight(self,jetset, ntags1, ntags2):
    return self.engine.weight2(jetset, ntags1, ntags2)

  def btaggingWeightMode(self,catName):
    if catName.find("(HEHE") != -1:
      return "HEHE"
    elif catName.find("(HEHP") != -1:
      return "HEHP"
    elif catName.find("(HPHP") != -1:
      return "HPHP"
    elif catName.find("(HE") != -1:
      if catName.find("exclusive") != -1:
        return "HEexcl"
      else:
        return "HE"
    elif catName.find("(HP") != -1:
      if catName.find("exclusive") != -1:
        return "HPexcl"
      else:
        return "HP"
    return "None"

