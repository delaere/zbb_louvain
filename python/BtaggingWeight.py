# we use the class from Andrea, with an additional method to add jets to the "event"
# that class also fills automatically the efficiency and SF.
import ROOT
import PatAnalysis.CMSSW
from PatAnalysis.EventSelection import categoryName
from ObjectSelection import isBJet
import os
confCfg = os.environ["PatAnalysisCfg"]
if confCfg : from UserCode.zbb_louvain.PatAnalysis.CPconfig import configuration
else : from zbbConfig import configuration

class BtaggingWeight:
  """compute the event weight based on btagging SF"""

  def __init__(self, jmin1, jmax1, jmin2, jmax2, file, btagging="CSV", WP=["M","L"]):
    self.engine=ROOT.BTagWeight(jmin1,jmax1,jmin2,jmax2)
    self.myJetSet = ROOT.JetSet(configuration.SF_running_mode,file)
    self.btagging=btagging
    self.WP=WP
    if "L" in WP or "HE" in WP : self.algo1 = 1
    else :
      self.algo1 = 2
      self.algo2 = 3
    if self.algo1 == 1 :
      if "M" in WP or "HP" in WP : self.algo2 = 2
      else : self.algo2 = 3

  def setLimits(self,jmin1,jmax1,jmin2,jmax2):
    self.engine.setLimits(jmin1,jmax1,jmin2,jmax2)

  def setMode(self,mode):
    #reminder: in the engine, the HP includes always HE.
    if   mode==self.WP[1]: self.engine.setLimits(1,999,0,999)
    elif mode==self.WP[0]: self.engine.setLimits(1,999,1,999)
    elif mode==self.WP[1]+"excl": self.engine.setLimits(1,1,0,1)# M exclu
    elif mode==self.WP[0]+"excl": self.engine.setLimits(1,1,1,1)
    elif mode==self.WP[1]+self.WP[1]: self.engine.setLimits(2,999,0,999)
    elif mode==self.WP[1]+self.WP[0]: self.engine.setLimits(2,999,1,999)
    elif mode==self.WP[0]+self.WP[0]: self.engine.setLimits(2,999,2,999)
    
    elif mode==self.WP[1]+self.WP[1]+"excl": self.engine.setLimits(2,2,0,1)#LL exclu
    elif mode==self.WP[0]+self.WP[0]+"excl": self.engine.setLimits(2,2,2,2)#MM exclu
    elif mode==self.WP[1]+self.WP[0]+"excl": self.engine.setLimits(2,2,1,1)#ML exclu
    
    elif mode==self.WP[1]+self.WP[1]+self.WP[1]: self.engine.setLimits(3,999,0,999)#LLL exclu
    elif mode==self.WP[0]+self.WP[0]+self.WP[0]: self.engine.setLimits(3,999,3,999)#MMM exclu    
    
    elif mode==self.WP[1]+self.WP[1]+self.WP[1]+"excl": self.engine.setLimits(3,3,0,1)#LLL exclu
    elif mode==self.WP[0]+self.WP[0]+self.WP[0]+"excl": self.engine.setLimits(3,3,3,3)#MMM exclu
   
    
    
    else: 
      print "btaggingWeight.py: Unknown mode:",mode
      self.engine.setLimits(0,999,0,999)

  def weight(self,event, category=None, forceMode=None):
    """btag eff weight"""
    # set the mode
    if forceMode is None and  category is not None:
      Bmode=self.btaggingWeightMode(categoryName(category))
    elif forceMode is not None: 
      Bmode=forceMode
    else:
      Bmode="None"
    # for data, immediately return 1.
    if event.object().event().eventAuxiliary().isRealData() or Bmode=="None":
      return 1.
    self.setMode(Bmode)
    # initialize counters
    self.myJetSet.reset()
    ntagsHE = 0
    ntagsHP = 0
    ntagsNoFlvavorHE = 0
    ntagsNoFlvavorHP = 0
    # retrieve the jets
    theGoodJets = event.goodJets_all
    for index,jet in enumerate(event.jets):
      # apply selection
      if not theGoodJets[index]: continue
      # check flavor
      flavor = jet.partonFlavour()
      # check btagging
      if isBJet(jet,self.WP[0],self.btagging):
        ntagsHP += 1
        if flavor == 0:
          #if jet.pt() > 100. : print "WARNING : "+btagging+self.WP[0]+" tagged jet with no flavor and high transverse energy : ", jet.pt(), ", eta : ", jet.eta()
          ntagsNoFlvavorHP += 1
      if isBJet(jet,self.WP[1],self.btagging):
        ntagsHE += 1
        if flavor == 0:
          #if jet.pt() > 100. : print "WARNING : "+btagging+self.WP[1]+" tagged jet with no flavor and high transverse energy : ", jet.pt(), ", eta : ", jet.eta()
          ntagsNoFlvavorHE += 1
      # add to the jetset class
      self.myJetSet.addJet(configuration.SF_uncert, flavor,jet.pt(),jet.eta(), self.algo1, self.algo2)
    #if ntagsNoFlvavorHP>=2 and ntagsNoFlvavorHE<2: print "IMPORTANT WARNING : 2 "+btagging+self.WP[0]+" tagged jets with no flavour !! Event should be checked !! Event number : ", event.event()
    #if ntagsNoFlvavorHE>=2 : print "IMPORTANT WARNING : 2 "+btagging+self.WP[1]+" tagged jets with no flavour !! Event should be checked !! Event number : ", event.event()
    return max(self.getWeight(self.myJetSet,ntagsHE,ntagsHP),0.)

  def getWeight(self,jetset, ntags1, ntags2):
    result = self.engine.weight2(jetset, ntags1, ntags2)
    return result

  def btaggingWeightMode(self,catName):
  
    if catName.find("(HEHEHE") != -1:
      if catName.find("exclusive") != -1:
        return self.WP[1]+self.WP[1]+self.WP[1]+"excl"
      else:
        return self.WP[1]+self.WP[1]+self.WP[1]
    elif catName.find("(HPHPHP") != -1:
      if catName.find("exclusive") != -1:
        return self.WP[0]+self.WP[0]+self.WP[0]+"excl"
      else:
        return self.WP[0]+self.WP[0]+self.WP[0]	
    elif catName.find("(HEHE") != -1:
      if catName.find("exclusive") != -1:
        return self.WP[1]+self.WP[1]+"excl"
      else:
        return self.WP[1]+self.WP[1]
    elif catName.find("(HEHP") != -1:
      if catName.find("exclusive") != -1:
        return self.WP[1]+self.WP[0]+"excl"
      else:
        return self.WP[1]+self.WP[0]
    elif catName.find("(HPHP") != -1:
      if catName.find("exclusive") != -1:
        return self.WP[0]+self.WP[0]+"excl"
      else:
        return self.WP[0]+self.WP[0]
    elif catName.find("(HE") != -1:
      if catName.find("exclusive") != -1:
        return self.WP[1]+"excl"
      else:
        return self.WP[1]
    elif catName.find("(HP") != -1:
      if catName.find("exclusive") != -1:
        return self.WP[0]+"excl"
      else:
        return self.WP[0]
    return "None"

