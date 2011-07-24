#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from btaggingWeight import *

class BtaggingReWeightingControlPlots:
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None):
      # create output file if needed. If no file is given, it means it is delegated
      if dir is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("BtaggingReweighting")
      else :
        self.f = None
        self.dir = dir
    
    def beginJob(self, perfData="../testfiles/performance_ssv_witheff.root"):
      # declare histograms
      self.dir.cd()
      self.h_he_w   = ROOT.TH1F("HE_w","HE",100,0,10)
      self.h_hp_w   = ROOT.TH1F("HP_w","HP",100,0,10)
      self.h_hehe_w = ROOT.TH1F("HEHE_w","HEHE",100,0,10)
      self.h_hehp_w = ROOT.TH1F("HEHP_w","HEHP",100,0,10)
      self.h_hphp_w = ROOT.TH1F("HPHP_w","HPHP",100,0,10)
      self.h_he   = ROOT.TH1F("HE","HE",100,0,10)
      self.h_hp   = ROOT.TH1F("HP","HP",100,0,10)
      self.h_hehe = ROOT.TH1F("HEHE","HEHE",100,0,10)
      self.h_hehp = ROOT.TH1F("HEHP","HEHP",100,0,10)
      self.h_hphp = ROOT.TH1F("HPHP","HPHP",100,0,10)
      # reweighting engine
      self.engine = btaggingWeight(0,999,0,999,perfData)
      # handles
    
    def processEvent(self,event, muChannel, weight = 1.):
      self.engine.setMode("HE")
      w = self.engine.weight(event,muChannel)
      self.h_he_w.Fill(w,weight)
      if w!=0 : self.h_he.Fill(w,weight/w)
      self.engine.setMode("HP")
      w = self.engine.weight(event,muChannel)
      self.h_hp_w.Fill(w,weight)
      if w!=0 : self.h_hp.Fill(w,weight/w)
      self.engine.setMode("HEHE")
      w = self.engine.weight(event,muChannel)
      self.h_hehe_w.Fill(w,weight)
      if w!=0 : self.h_hehe.Fill(w,weight/w)
      self.engine.setMode("HEHP")
      w = self.engine.weight(event,muChannel)
      self.h_hehp_w.Fill(w,weight)
      if w!=0 : self.h_hehp.Fill(w,weight/w)
      self.engine.setMode("HPHP")
      w = self.engine.weight(event,muChannel)
      self.h_hphp_w.Fill(w,weight)
      if w!=0 : self.h_hphp.Fill(w,weight/w)

    def endJob(self):
      self.dir.cd()
      self.dir.Write()
      if not self.f is None:
        self.f.Close()

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
    controlPlots.processEvent(event,muChannel=1)
    i += 1
  controlPlots.endJob()

