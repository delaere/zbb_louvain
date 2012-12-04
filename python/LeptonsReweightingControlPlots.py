#! /usr/bin/env python

import ROOT
import sys
import os
from AnalysisEvent import AnalysisEvent
from baseControlPlots import BaseControlPlots
from LeptonsReweighting import *
#from myFuncTimer import print_timing

class LeptonsReweightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, muChannel=True, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="LeptonsReweighting", dataset=dataset, mode=mode)
      self.muChannel = muChannel
    
    def beginJob(self):
      # declare histograms
      self.add("weight","weight",200,0,2)
      # reweighting engine
      self.engine = LeptonsReWeighting()

    #@print_timing
    def process(self, event):
      """LeptonsReweightingControlPlots"""
      result = { }
      w = self.engine.weight(fwevent=event, muChannel=self.muChannel)
      result["weight"] = w
      return result


def runTest(path="../testfiles/"):
  controlPlots = LeptonsReweightingControlPlots()

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

  controlPlots.beginJob()
  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    controlPlots.processEvent(event)
    i += 1
  controlPlots.endJob()

