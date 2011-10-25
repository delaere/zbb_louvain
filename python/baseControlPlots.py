#! /usr/bin/env python
import ROOT 

def getArgSet(controlplots):
  assert isinstance(controlplots,list)
  merged = ROOT.RooArgSet()
  for ctrlplot in controlplots:
    merged.add(ctrlplot._obsSet)
  return merged

class BaseControlPlots:
    """A class to create control plots"""

    def __init__(self, dir=None, purpose="generic", dataset=None, mode="plots"):
      """Initialize the ControlPlots, creating output file if needed. If no file is given, it means it is delegated."""
      self._mode = mode
      self._purpose = purpose
      # for plots
      if self._mode=="plots":
        # create output file if needed. If no file is given, it means it is delegated
        if dir is None:
          self._f = ROOT.TFile("controlPlots.root", "RECREATE")
          self._dir = self._f.mkdir(purpose)
        else :
          self._f = None
          self._dir = dir
        self._h_vector = { }
      # for ntuples
      if self._mode=="dataset":
        self._obsSet = ROOT.RooArgSet()
        if dataset is None:
          self._rds = ROOT.RooDataSet("rds_zbb",  "rds_zbb", self._obsSet) # Q: is that ok, or do we have to create the rds once the ArgSet is fully defined?
	  self._ownedRDS = True
	else:
	  self._rds = dataset
	  self._ownedRDS = False
        self._rrv_vector = { }
        self._rooCategories = { }
    
    def beginJob(self):
      """Declare histograms, and for derived classes instantiate handles. Must be overloaded.""" 
      raise NotImplementedError

    def defineCategories(self, categories):
      """Define the categories, given a list of names. Only works for datasets"""
      if self._mode!="dataset": return
      for i, name in enumerate(categories):
        rc = ROOT.RooCategory("rc_"+self._purpose+"_"+str(i),name)
	rc.defineType("not_acc",0)
	rc.defineType("acc",1)
	self._rooCategories[i] = rc
	self._rds.addColumn(rc)
	self._obsSet.add(rc)

    def addHisto(self,*args):
      """Add one histograms to the list of products. Arguments are as for TH1F."""
      # this fills a distionnary name <-> histogram
      self._dir.cd()
      self._h_vector[args[0]] = ROOT.TH1F(*args)

    def addVariable(self,*args):
      """Add one variable to the list of products. Arguments are as for RooRealVar."""
      # this fills a distionnary name <-> RooRealVar
      self._rrv_vector[args[0]] = ROOT.RooRealVar(self._purpose+args[0],*(args[1:]))
      self._obsSet.add(self._rrv_vector[args[0]])
      self._rds.addColumn(self._rrv_vector[args[0]])
    
    def add(self, *args):
      """Add one item to the list of products. Arguments are as for TH1F."""
      if self._mode=="plots":
        self.addHisto(*args)
      else:
        self.addVariable(*[args[i] for i in [0,1,3,4]])

    def processEvent(self, event, weight = 1.):
      """process event and fill histograms"""
      self.fill(self.process(event),weight)
     
    def process(self, event):
      """Process event data to extract histogrammables. Must be overloaded."""
      raise NotImplementedError
      # this is just an example, we never get there
      # that method must return a dictionnary name <-> value that matches self._h_vector
      result = { }
      result["var1"] = 1.
      result["var2"] = 2.3
      result["var3"] = 5.711
      return result

    def setCategories(self, categories):
      """Set the categories, given a list of booleans. Only works for datasets"""
      if self._mode!="dataset": return
      for c, flag in enumerate(categories):
        if flag: self._rooCategories[c].setIndex(1)
	else: self._rooCategories[c].setIndex(0)

    def fillPlots(self, data, weight = 1.):
      """Fills histograms with the data provided as input."""
      for name,value in data.items():
        if isinstance(value,list):
          for val in value: self._h_vector[name].Fill(val,weight)
        else:
          self._h_vector[name].Fill(value,weight)

    def fillRDS(self, data):
      """Fills roodataset with the data provided as input."""
      for name,value in data.items():
        if isinstance(value,list):
	  #for now, we only store scalars, not vectors
	  pass
        else:
	  self._rrv_vector[name].setVal(value)
      if self._ownedRDS:
        self._rds.add(self._obsSet)  

    def fill(self, data, weight = 1.):
      """Fills whatever must be filled in"""
      if self._mode=="plots":
        self.fillPlots(data, weight)
      else:
        self.fillRDS(data)

    def endJob(self):
      """Save and close."""
      if self._mode=="plots":
        self._dir.cd()
        self._dir.Write()
        if not self._f is None:
          self._f.Close()
      else:
        if self._ownedRDS:
          ws  = ROOT.RooWorkspace(self._purpose,self._purpose) # need a way to share a workspace (as we do for dirs)
          getattr(ws,'import')(self._rds) 
          ws.writeToFile("File_rds_zbb_"+self._purpose+".root") 

