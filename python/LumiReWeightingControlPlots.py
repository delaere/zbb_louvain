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
    
    def beginJob(self, MonteCarloFileName, DataFileName, MonteCarloHistName="pileup", DataHistName="pileup", vertexlabel="goodPV", pulabel="addPileupInfo"):
      # declare histograms
      self.dir.cd()
      self.h_weight = ROOT.TH1F("LumiWeight","LumiWeight",1000,0,10)
      self.h_weightOOTPU = ROOT.TH1F("LumiWeightOOTPU","LumiWeightOOTPU",1000,0,10)
      self.h_weightType = ROOT.TH1F("weightType","weightType",2,0,2)
      self.h_pu_nw = ROOT.TH1F("pu_nw","pu_nw",50,0,50)
      self.h_pv_nw = ROOT.TH1F("pv_nw","pv_nw",50,0,50)
      self.h_pu = ROOT.TH1F("pu","pu",50,0,50)
      self.h_pv = ROOT.TH1F("pv","pv",50,0,50)
      # reweighting engine
      self.engine = LumiReWeighting(MonteCarloFileName, DataFileName, MonteCarloHistName,DataHistName)
      # handles
      self.vertexHandle = Handle ("vector<reco::Vertex>")
      self.vertexlabel = (vertexlabel)

      self.PupInfo = Handle ("std::vector< PileupSummaryInfo >")
      self.pulabel = (pulabel)
    
    def processEvent(self,event, weight = 1.):
      w = self.engine.weight( fwevent=event, PileupSummaryInfo=self.PileupSummaryInfo )
      wprime = self.engine.weightWithOOTPU( fwevent=event, PileupSummaryInfo=self.PileupSummaryInfo )
      w_auto = self.engine.weight_auto(event, PileupSummaryInfo=self.PileupSummaryInfo )
      self.h_weight.Fill(w)
      self.h_weightOOTPU.Fill(wprime)
      if self.engine.checkRelease( fwevent=event ):
        self.h_weightType.Fill(1,weight)
      else:
        self.h_weightType.Fill(0,weight)
      event.getByLabel (self.vertexlabel,self.vertexHandle)
      vs = self.vertexHandle.product()
      npv = vs.size()
      event.getByLabel(self.pulabel, self.PupInfo)
      pileup = self.PupInfo.product()
      for pvi in pileup:
        if pvi.getBunchCrossing()==0:
          npu = pvi.getPU_NumInteractions()
      self.h_pu.Fill(npu, weight)
      self.h_pv.Fill(npv, weight)
      self.h_pu_nw.Fill(npu, weight/w_auto)
      self.h_pv_nw.Fill(npv, weight/w_auto)

    def endJob(self):
      self.dir.cd()
      self.dir.Write()
      if not self.f is None:
        self.f.Close()

def runTest():
  controlPlots = LumiReWeightingControlPlots()
  path="/home/fynu/delaere/zbbAnalysis/CMSSW_4_2_3/src/UserCode/zbb_louvain/testfiles/"
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

