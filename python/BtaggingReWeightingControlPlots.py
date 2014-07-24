import ROOT
from PatAnalysis.BaseControlPlots import BaseControlPlots

class BtaggingReWeightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="BtaggingReweighting", dataset=dataset, mode=mode)
    
    def beginJob(self, btagging="CSV", WP=["M","L"]):
      self._btagging = btagging
      self.WP = WP
      # declare histograms
      self.add(WP[1],WP[1],200,0,2)
      self.add(WP[0],WP[0],200,0,2)
      self.add(WP[1]+"excl",WP[1]+"excl",200,0,2)
      self.add(WP[0]+"excl",WP[0]+"excl",200,0,2)
      self.add(WP[1]+WP[1],WP[1]+WP[1],200,0,2)
      self.add(WP[1]+WP[0],WP[1]+WP[0],200,0,2)
      self.add(WP[0]+WP[0],WP[0]+WP[0],200,0,2)
      
      self.add(WP[0]+WP[0]+"excl",WP[0]+WP[0]+"excl",200,0,2)      
      self.add(WP[1]+WP[0]+"excl",WP[1]+WP[0]+"excl",200,0,2)      
      self.add(WP[1]+WP[1]+"excl",WP[1]+WP[1]+"excl",200,0,2) 
      
      self.add(WP[0]+WP[0]+WP[0]+"excl",WP[0]+WP[0]+WP[0]+"excl",200,0,2) 
      self.add(WP[1]+WP[1]+WP[1]+"excl",WP[1]+WP[1]+WP[1]+"excl",200,0,2)       
         
    def process(self,event):
      """BtaggingReWeightingControlPlots"""
      result = { }
      result[self.WP[1]]     = event.weight(weightList=["Btagging"], forceMode=self.WP[1],     btagging=self._btagging)
      result[self.WP[0]]     = event.weight(weightList=["Btagging"], forceMode=self.WP[0],     btagging=self._btagging)
      result[self.WP[1]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+"excl", btagging=self._btagging)
      result[self.WP[0]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[0]+"excl", btagging=self._btagging)
      result[self.WP[1]+self.WP[1]]   = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+self.WP[1],   btagging=self._btagging)
      result[self.WP[1]+self.WP[0]]   = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+self.WP[0],   btagging=self._btagging)
      result[self.WP[0]+self.WP[0]]   = event.weight(weightList=["Btagging"], forceMode=self.WP[0]+self.WP[0],   btagging=self._btagging)
      
      result[self.WP[1]+self.WP[1]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+self.WP[1]+"excl", btagging=self._btagging)
      result[self.WP[1]+self.WP[0]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+self.WP[0]+"excl", btagging=self._btagging)   
      result[self.WP[0]+self.WP[0]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[0]+self.WP[0]+"excl", btagging=self._btagging)   
      
      result[self.WP[0]+self.WP[0]+self.WP[0]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[0]+self.WP[0]+self.WP[0]+"excl", btagging=self._btagging) 
      result[self.WP[1]+self.WP[1]+self.WP[1]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+self.WP[1]+self.WP[1]+"excl", btagging=self._btagging) 
     
              
      return result

    def processEvent(self,event,weight = 1.,btagging="CSV"):
      """process event and fill histograms"""
      self.fill(self.process(event),weight)

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], BtaggingReWeightingControlPlots())

