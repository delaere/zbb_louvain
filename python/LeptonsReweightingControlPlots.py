#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from baseControlPlots import BaseControlPlots
from LeptonsReweighting import *
#from myFuncTimer import print_timing

class LeptonsReWeightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, muChannel=True):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="LeptonsReweighting")
      self.muChannel = muChannel
    
    def beginJob(self):
      # declare histograms
      self.addHisto("weight","weight",200,0,2)
      # reweighting engine
      self.engine = LeptonsReWeighting()

    #@print_timing
    def process(self, event):
      """LeptonsReWeightingControlPlots"""
      result = { }
      w = self.engine.weight(fwevent=event, muChannel=self.muChannel)
      result["weight"] = w
      return result


def runTest():
  controlPlots = LeptonsReWeightingControlPlots()
  path="../testfiles/ttbar/"
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)
  controlPlots.beginJob(perfData="../testfiles/performance_ssv_witheff.root")
  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    controlPlots.processEvent(event)
    i += 1
  controlPlots.endJob()

