#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from baseControlPlots import BaseControlPlots
from LumiReWeighting import *
#from myFuncTimer import print_timing

class LumiReWeightingControlPlots(BaseControlPlots):
    """A class to create control plots for lumi reweighting"""

    def __init__(self, dir=None, PileupSummaryInfo="addPileupInfo"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="lumiReweighting")
      self.PileupSummaryInfo = PileupSummaryInfo
    
    def beginJob(self, MonteCarloFileName, DataFileName, MonteCarloHistName="pileup", DataHistName="pileup", vertexlabel="goodPV", pulabel="addPileupInfo"):
      # declare histograms
      self.addHisto("LumiWeight","LumiWeight",1000,0,10)
      self.addHisto("pu","pu",50,0,50)
      self.addHisto("pv","pv",50,0,50)
      # reweighting engine
      self.engine = LumiReWeighting(MonteCarloFileName, DataFileName, MonteCarloHistName,DataHistName, PileupSummaryInfo=self.PileupSummaryInfo)
      # fill the histogram with the configured weights
      self.h_weightSetup = ROOT.TH1F("weightSetup","weightSetup",50,0,50)
      for i in range(50): self.h_weightSetup.SetBinContent(i+1,self.engine.weight(npu=i))
      # handles
      self.vertexHandle = Handle ("vector<reco::Vertex>")
      self.vertexlabel = (vertexlabel)
      self.PupInfo = Handle ("std::vector< PileupSummaryInfo >")
      self.pulabel = (pulabel)
    
    #@print_timing
    def process(self, event):
      """LumiReWeightingControlPlots"""
      result = { }
      result["LumiWeight"] = self.engine.weight( fwevent=event )
      event.getByLabel (self.vertexlabel,self.vertexHandle)
      vs = self.vertexHandle.product()
      npv = vs.size()
      event.getByLabel(self.pulabel, self.PupInfo)
      pileup = self.PupInfo.product()
      for pvi in pileup:
        if pvi.getBunchCrossing()==0:
          npu = pvi.getPU_NumInteractions()
      result["pu"]= npu
      result["pv"]= npv
      return result

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

