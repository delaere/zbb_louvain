#! /usr/bin/env python

import ROOT
import sys
import os
from AnalysisEvent import AnalysisEvent
from eventSelection import prepareAnalysisEvent
from baseControlPlots import BaseControlPlots
from LumiReWeighting import *
from zbbCommons import zbblabel,zbbfile
#from myFuncTimer import print_timing

class LumiReWeightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="lumiReweighting", dataset=dataset, mode=mode)
    
    def beginJob(self):
      # declare histograms
      self.add("LumiWeight","LumiWeight",1000,0,10)
      self.add("pu","pu",50,0,50)
      self.add("pv","pv",50,0,50)
      if self._mode=="plots":
        self._dir.cd()
        self.h_weightSetup = ROOT.TH1F("weightSetup","weightSetup",50,0,50)
      self.first = True
    
    #@print_timing
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

def runTest(path="../testfiles/"):
  controlPlots = LumiReWeightingControlPlots()

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
  events.addWeight("PileUp",LumiReWeighting(systematicShift=0))

  controlPlots.beginJob()
  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    controlPlots.processEvent(event)
    i += 1
  controlPlots.endJob()

