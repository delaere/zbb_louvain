import ROOT
from PatAnalysis.BaseControlPlots import BaseControlPlots

class MonteCarloReweightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, purpose="mcReweighting", dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)
    
    def beginJob(self):
      # declare histograms
      self.add("weight","weight",200,0,2)

    def process(self, event):
      """MonteCarloReweightingControlPlots"""
      result = { }
      result["weight"] = event.weight(weightList=["MonteCarlo"])
      return result

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], MonteCarloReweightingControlPlots())

