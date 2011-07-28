#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from LeptonsReweighting import *

class LeptonsReWeightingControlPlots:
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None):
      # create output file if needed. If no file is given, it means it is delegated
      if dir is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("LeptonsReweighting")
      else :
        self.f = None
        self.dir = dir
    
    def beginJob(self):
      # declare histograms
      self.dir.cd()
      self.h_weight = ROOT.TH1F("weight","weight",200,0,2)
      self.h_weight_w = ROOT.TH1F("weight_w","weight",200,0,2)
      # reweighting engine
      self.engine = LeptonsReWeighting()
    
    def processEvent(self,event, muChannel, weight = 1.):
      w = self.engine.weight(fwevent=event, muChannel=muChannel)
      self.h_weight_w.Fill(w,weight)
      if w!=0 : self.h_weight.Fill(w,weight/w)

    def endJob(self):
      self.dir.cd()
      self.dir.Write()
      if not self.f is None:
        self.f.Close()

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
    controlPlots.processEvent(event,muChannel=1)
    i += 1
  controlPlots.endJob()

