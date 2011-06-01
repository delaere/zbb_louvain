#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from LumiReWeighting import *

class LumiReWeightingControlPlots:
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, PileupSummaryInfo="addPileupInfo"):
      # create output file if needed. If no file is given, it means it is delegated
      if dir is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("lumiReweighting")
      else :
        self.f = None
        self.dir = dir
      self.PileupSummaryInfo = PileupSummaryInfo
    
    def beginJob(self, MonteCarloFileName, DataFileName, MonteCarloHistName="pileup", DataHistName="pileup"):
      # declare histograms
      self.dir.cd()
      self.h_weight = ROOT.TH1F("LumiWeight","LumiWeight",1000,0,10)
      # reweighting engine
      self.engine = LumiReWeighting(MonteCarloFileName, DataFileName, MonteCarloHistName,DataHistName)
    
    def processEvent(self,event, weight = 1.):
      w = self.engine.weight( fwevent=event, PileupSummaryInfo=self.PileupSummaryInfo )
      self.h_weight.Fill(w)

    def endJob(self):
      self.dir.cd()
      self.dir.Write()
      if not self.f is None:
        self.f.Close()

def runTest():
  controlPlots = LumiReWeightingControlPlots()
  path="/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/"
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)
  controlPlots.beginJob(MonteCarloFileName="pudistCopy.root", DataFileName="pudist.root")
  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    controlPlots.processEvent(event)
    i += 1
  controlPlots.endJob()

