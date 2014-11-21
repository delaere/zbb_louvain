import ROOT
from PatAnalysis.BaseControlPlots import BaseControlPlots
import PatAnalysis.EventSelection

class BtaggingReWeightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, purpose="btaggingReweighting", dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)
    
    def beginJob(self, btagging="CSV", WP=["M","L"]):
      self._btagging = btagging
      self.WP = WP
      self.map = {}
      for cat in PatAnalysis.EventSelection.categoryNames:
          wpcat = "CA8"*cat.count("CA8")+"Subjets"*cat.count("Subjets")+"subjets"*cat.count("subjets")+WP[1]*cat.count("HE")+WP[0]*cat.count("HP")
          if wpcat == "" : continue
          if len(wpcat) <= 2 : wpcat = "AK5"+wpcat
          if wpcat in self.map : continue
          self.map[wpcat] = PatAnalysis.EventSelection.categoryNames.index(cat)
          self.add(wpcat,wpcat,200,0,2)
      # declare histograms
      self.add(WP[1],WP[1],200,0,2)
      self.add(WP[0],WP[0],200,0,2)
      self.add(WP[1]+"excl",WP[1]+"excl",200,0,2)
      self.add(WP[0]+"excl",WP[0]+"excl",200,0,2)
      
      self.add(WP[1]+WP[1],WP[1]+WP[1],200,0,2)
      self.add(WP[1]+WP[0],WP[1]+WP[0],200,0,2)
      self.add(WP[0]+WP[0],WP[0]+WP[0],200,0,2)

      self.add(self.WP[1]+self.WP[1]+"excl", self.WP[1]+self.WP[1]+"excl",200,0,2)
      self.add(self.WP[0]+self.WP[0]+"excl", self.WP[0]+self.WP[0]+"excl",200,0,2)
      self.add(self.WP[1]+self.WP[1]+self.WP[1], self.WP[1]+self.WP[1]+self.WP[1],200,0,2)
      self.add(self.WP[0]+self.WP[0]+self.WP[0], self.WP[0]+self.WP[0]+self.WP[0],200,0,2)
      self.add(self.WP[1]+self.WP[1]+self.WP[1]+"excl", self.WP[1]+self.WP[1]+self.WP[1]+"excl",200,0,2)
      self.add(self.WP[0]+self.WP[0]+self.WP[0]+"excl", self.WP[0]+self.WP[0]+self.WP[0]+"excl",200,0,2)
      self.add("0"+self.WP[1]+"excl", "0"+self.WP[1]+"excl",200,0,2)
      self.add("0"+self.WP[0]+"excl", "0"+self.WP[0]+"excl",200,0,2)
      
         
    def process(self,event):
      """BtaggingReWeightingControlPlots"""
      result = { }
      for wpcat in self.map:
          result[wpcat] = event.weight(weightList=["Btagging"], category=self.map[wpcat], btagging=self._btagging)
      result[self.WP[1]]     = event.weight(weightList=["Btagging"], forceMode=self.WP[1],     btagging=self._btagging)
      result[self.WP[0]]     = event.weight(weightList=["Btagging"], forceMode=self.WP[0],     btagging=self._btagging)
      result[self.WP[1]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+"excl", btagging=self._btagging)
      result[self.WP[0]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[0]+"excl", btagging=self._btagging)
      result[self.WP[1]+self.WP[1]]   = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+self.WP[1],   btagging=self._btagging)
      result[self.WP[1]+self.WP[0]]   = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+self.WP[0],   btagging=self._btagging)
      result[self.WP[0]+self.WP[0]]   = event.weight(weightList=["Btagging"], forceMode=self.WP[0]+self.WP[0],   btagging=self._btagging)
      
      result[self.WP[1]+self.WP[1]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+self.WP[1]+"excl", btagging=self._btagging)
      result[self.WP[0]+self.WP[0]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[0]+self.WP[0]+"excl", btagging=self._btagging)
      result[self.WP[1]+self.WP[1]+self.WP[1]] = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+self.WP[1]+self.WP[1], btagging=self._btagging)
      result[self.WP[0]+self.WP[0]+self.WP[0]] = event.weight(weightList=["Btagging"], forceMode=self.WP[0]+self.WP[0]+self.WP[0], btagging=self._btagging)
      result[self.WP[1]+self.WP[1]+self.WP[1]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[1]+self.WP[1]+self.WP[1]+"excl", btagging=self._btagging)
      result[self.WP[0]+self.WP[0]+self.WP[0]+"excl"] = event.weight(weightList=["Btagging"], forceMode=self.WP[0]+self.WP[0]+self.WP[0]+"excl", btagging=self._btagging)
      result["0"+self.WP[1]+"excl"] = event.weight(weightList=["Btagging"], forceMode="0"+self.WP[1]+"excl", btagging=self._btagging)
      result["0"+self.WP[0]+"excl"] = event.weight(weightList=["Btagging"], forceMode="0"+self.WP[0]+"excl", btagging=self._btagging)
     
              
      return result

    def processEvent(self,event,weight = 1.,btagging="CSV"):
      """process event and fill histograms"""
      self.fill(self.process(event),weight)

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], BtaggingReWeightingControlPlots())

