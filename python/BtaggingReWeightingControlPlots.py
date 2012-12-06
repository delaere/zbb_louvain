#! /usr/bin/env python

import ROOT
import sys
import os
from AnalysisEvent import AnalysisEvent
from baseControlPlots import BaseControlPlots
from btaggingWeight import *
from zbbCommons import zbbfile
#from myFuncTimer import print_timing

class BtaggingReWeightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, muChannel=True, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="BtaggingReweighting", dataset=dataset, mode=mode)
      self.muChannel=muChannel
    
    def beginJob(self, perfData=zbbfile.ssvperfData):
      # declare histograms
      self.add("HE","HE",200,0,2)
      self.add("HP","HP",200,0,2)
      self.add("HEexcl","HEexcl",200,0,2)
      self.add("HPexcl","HPexcl",200,0,2)
      self.add("HEHE","HEHE",200,0,2)
      self.add("HEHP","HEHP",200,0,2)
      self.add("HPHP","HPHP",200,0,2)
    
    #@print_timing
    def process(self,event,btagging="CSV"):
      """BtaggingReWeightingControlPlots"""
      result = { }
      result["HE"]     = event.weight(weightList=["Btagging"], muChannel=self.muChannel, Bmode="HE", btagging=btagging)
      result["HP"]     = event.weight(weightList=["Btagging"], muChannel=self.muChannel, Bmode="HP", btagging=btagging)
      result["HEexcl"] = event.weight(weightList=["Btagging"], muChannel=self.muChannel, Bmode="HEexcl", btagging=btagging)
      result["HPexcl"] = event.weight(weightList=["Btagging"], muChannel=self.muChannel, Bmode="HPexcl", btagging=btagging)
      result["HEHE"]   = event.weight(weightList=["Btagging"], muChannel=self.muChannel, Bmode="HEHE", btagging=btagging)
      result["HEHP"]   = event.weight(weightList=["Btagging"], muChannel=self.muChannel, Bmode="HEHP", btagging=btagging)
      result["HPHP"]   = event.weight(weightList=["Btagging"], muChannel=self.muChannel, Bmode="HPHP", btagging=btagging)
      return result

def runTest(path="../testfiles/ttbar/"):
  controlPlots = BtaggingReWeightingControlPlots()

  if os.path.isdir(path):
    dirList=os.listdir(path)
    files=[]
    for fname in dirList:
      files.append(path+fname)
  elif os.path.isfile(path):
    files=[path]
  else:
    files=[]
  events = AnalysisEvent(files)
  prepareAnalysisEvent(events,checkTrigger=False)
  events.addWeight("Btagging",btaggingWeight(0,999,0,999))

  controlPlots.beginJob()
  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    controlPlots.processEvent(event)
    i += 1
  controlPlots.endJob()

