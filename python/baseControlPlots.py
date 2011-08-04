#! /usr/bin/env python
import ROOT

class BaseControlPlots:
    """A class to create control plots"""

    def __init__(self, dir=None, purpose="generic"):
      """Initialize the ControlPlots, creating output file if needed. If no file is given, it means it is delegated."""
      # create output file if needed. If no file is given, it means it is delegated
      if dir is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir(purpose)
      else :
        self.f = None
        self.dir = dir
      self.h_vector = { }
    
    def beginJob(self):
      """Declare histograms, and for derived classes instantiate handles. Must be overloaded.""" 
      raise NotImplementedError
      # histograms are added by calling addHisto(*args)

    def addHisto(self,*args):
      """Add one histograms to the list of products. Arguments are as for TH1F."""
      # this fills a distionnary name <-> histogram
      self.dir.cd()
      self.h_vector[args[0]] = ROOT.TH1F(*args)
    
    def processEvent(self, event, weight = 1.):
      """process event and fill histograms"""
      self.fill(self.process(event),weight)
     
    def process(self, event):
      """Process event data to extract histogrammables. Must be overloaded."""
      raise NotImplementedError
      # this is just an example, we never get there
      # that method must return a dictionnary name <-> value that matches self.h_vector
      result = { }
      result["var1"] = 1.
      result["var2"] = 2.3
      result["var3"] = 5.711
      return result
    
    def fill(self, data, weight = 1.):
      """Fills histograms with the data provided as input."""
      for name,value in data.items():
        if isinstance(value,list):
          for val in value: self.h_vector[name].Fill(val,weight)
        else:
          self.h_vector[name].Fill(value,weight)

    def endJob(self):
      """Save and close."""
      self.dir.cd()
      self.dir.Write()
      if not self.f is None:
        self.f.Close()

