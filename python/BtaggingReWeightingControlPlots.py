#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from baseControlPlots import BaseControlPlots
from btaggingWeight import *
#from myFuncTimer import print_timing

class BtaggingReWeightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, muChannel=True):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="BtaggingReweighting")
      self.muChannel=muChannel
    
    def beginJob(self, perfData="../testfiles/performance_ssv_witheff.root"):
      # declare histograms
      self.addHisto("HE","HE",200,0,2)
      self.addHisto("HP","HP",200,0,2)
      self.addHisto("HEexcl","HEexcl",200,0,2)
      self.addHisto("HPexcl","HPexcl",200,0,2)
      self.addHisto("HEHE","HEHE",200,0,2)
      self.addHisto("HEHP","HEHP",200,0,2)
      self.addHisto("HPHP","HPHP",200,0,2)
      # reweighting engine
      self.engine = btaggingWeight(0,999,0,999,perfData)
    
    #@print_timing
    def process(self,event):
      """BtaggingReWeightingControlPlots"""
      result = { }
      self.engine.setMode("HE")
      result["HE"] = self.engine.weight(event,self.muChannel)
      self.engine.setMode("HP")
      result["HP"] = self.engine.weight(event,self.muChannel)
      self.engine.setMode("HEexcl")
      result["HEexcl"] = self.engine.weight(event,self.muChannel)
      self.engine.setMode("HPexcl")
      result["HPexcl"] = self.engine.weight(event,self.muChannel)
      self.engine.setMode("HEHE")
      result["HEHE"] = self.engine.weight(event,self.muChannel)
      self.engine.setMode("HEHP")
      result["HEHP"] = self.engine.weight(event,self.muChannel)
      self.engine.setMode("HPHP")
      result["HPHP"] = self.engine.weight(event,self.muChannel)
      return result

def runTest():
  controlPlots = BtaggingReWeightingControlPlots()
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

