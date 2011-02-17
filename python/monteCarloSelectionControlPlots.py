#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from monteCarloSelection import *

class MonteCarloSelectionControlPlots:
    """A class to create control plots for MC event selection"""

    def __init__(self, dir=None):
      # create output file if needed. If no file is given, it means it is delegated
      if dir is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("mcSelection")
      else :
        self.f = None
        self.dir = dir

    def beginJob(self, genlabel="genParticles"):
      # declare histograms
      self.dir.cd()
      self.h_eventType = ROOT.TH1F("eventType","Event Type (0,l,c,b)+Z",4,0,4)
      self.genlabel=genlabel
      self.genHandle = Handle ("vector<reco::GenParticle>")
      self.cjet = 0
      self.bjet = 0
      self.ljet = 0
      self.i = 0
      
    def processEvent(self,event):
      event.getByLabel (self.genlabel,self.genHandle)
      particles = self.genHandle.product()
      self.i += 1
      if isZbEvent(particles):
        self.bjet += 1
        self.h_eventType.Fill(3)
        return
      if isZcEvent(particles):
        self.cjet += 1
        self.h_eventType.Fill(2)
        return
      if isZlEvent(particles):
        self.ljet += 1
        self.h_eventType.Fill(1)
        return
      self.h_eventType.Fill(0)

    def endJob(self):
      self.dir.cd()
      self.dir.Write()
      if not self.f is None:
        self.f.Close()
      print "summary: out of",self.i,"events:",self.cjet,"cZ events",self.bjet,"bZ events and",self.ljet," light jets events."

def runTest():
  controlplots = MonteCarloSelectionControlPlots()
  path="/storage/data/cms/store/user/favereau/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola_387/"
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)
  controlplots.beginJob()
  i = 0
  for event in events:
    if i==10000: break
    if i%1000==0 : print "Processing... event ", i
    controlplots.processEvent(event)
    i += 1
  controlplots.endJob()

runTest()
