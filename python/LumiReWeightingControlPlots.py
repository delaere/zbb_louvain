import ROOT
from PatAnalysis.BaseControlPlots import BaseControlPlots

class LumiReWeightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, purpose="lumiReweighting", dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)
    
    def beginJob(self):
      # declare histograms
      self.add("LumiWeight","LumiWeight",1000,0,10)
      self.add("pu","pu",50,0,50)
      self.add("pv","pv",50,0,50)
      if self._mode=="plots":
        self._dir.cd()
        self.h_weightSetup = ROOT.TH1F("weightSetup","weightSetup",50,0,50)
      self.first = True
    
    def process(self, event):
      """LumiReWeightingControlPlots"""
      if self.first:
        if self._mode=="plots":
          for i in range(50): self.h_weightSetup.SetBinContent(i+1,event.weight(weightList=["PileUp"],npu=i))
        self.first = False
      result = { }
      result["LumiWeight"] = event.weight(weightList=["PileUp"])
      pileup = event.PileupSummaryInfo
      for pvi in pileup:
        if pvi.getBunchCrossing()==0:
          npu = pvi.getPU_NumInteractions()
      result["pu"]= npu
      result["pv"]= event.vertices.size()
      return result

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], LumiReWeightingControlPlots())

