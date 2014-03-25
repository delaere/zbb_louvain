import ROOT
from PatAnalysis.BaseControlPlots import BaseControlPlots

class BtaggingReWeightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="BtaggingReweighting", dataset=dataset, mode=mode)
    
    def beginJob(self, btagging="CSV"):
      self._btagging = btagging
      # declare histograms
      self.add("HE","HE",200,0,2)
      self.add("HP","HP",200,0,2)
      self.add("HEexcl","HEexcl",200,0,2)
      self.add("HPexcl","HPexcl",200,0,2)
      self.add("HEHE","HEHE",200,0,2)
      self.add("HEHP","HEHP",200,0,2)
      self.add("HPHP","HPHP",200,0,2)
    
    def process(self,event):
      """BtaggingReWeightingControlPlots"""
      result = { }
      result["HE"]     = event.weight(weightList=["Btagging"], forceMode="HE",     btagging=self._btagging)
      result["HP"]     = event.weight(weightList=["Btagging"], forceMode="HP",     btagging=self._btagging)
      result["HEexcl"] = event.weight(weightList=["Btagging"], forceMode="HEexcl", btagging=self._btagging)
      result["HPexcl"] = event.weight(weightList=["Btagging"], forceMode="HPexcl", btagging=self._btagging)
      result["HEHE"]   = event.weight(weightList=["Btagging"], forceMode="HEHE",   btagging=self._btagging)
      result["HEHP"]   = event.weight(weightList=["Btagging"], forceMode="HEHP",   btagging=self._btagging)
      result["HPHP"]   = event.weight(weightList=["Btagging"], forceMode="HPHP",   btagging=self._btagging)
      return result

    def processEvent(self,event,weight = 1.,btagging="CSV"):
      """process event and fill histograms"""
      self.fill(self.process(event),weight)

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], BtaggingReWeightingControlPlots())

