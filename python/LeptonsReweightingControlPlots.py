import ROOT
from PatAnalysis.BaseControlPlots import BaseControlPlots

class LeptonsReweightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, purpose="leptonsReweighting", category=None, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)
      #self.category = [int(s) for s in dir.GetName().split('_') if s.isdigit()]
      #if len(self.category): self.category=self.category[0] 
      #else: self.category=None
    
    def beginJob(self, muChannel = None):
      self._muChannel = muChannel
      # declare histograms
      self.add("weight","weight",200,0,2)
      self.add("weight_OneExtraLep","weight_OneExtraLep",200,0,2)
      self.add("weight_TwoExtraLep","weight_TwoExtraLep",200,0,2)

    def process(self, event):
      """LeptonsReweightingControlPlots"""
      result = { }
      if self._muChannel is None:
        result["weight"] = event.weight(weightList=["Leptons"])
      elif self._muChannel == False:
        result["weight"] = event.weight(weightList=["Leptons"], forceMode="Electron")
      elif self._muChannel == True:
        result["weight"] = event.weight(weightList=["Leptons"], forceMode="Muon")
      result["weight_OneExtraLep"] = event.weight(weightList=["Leptons"], forceMode="3lep")
      result["weight_TwoExtraLep"] = event.weight(weightList=["Leptons"], forceMode="4lep")
      return result

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], LeptonsReweightingControlPlots())

