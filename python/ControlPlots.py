#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from objectsControlPlots import *
from eventSelectionControlPlots import *
from vertexAssociationControlPlots import *

def runTest():
  output = ROOT.TFile("controlPlots_Zcc-TuneZ2_2.root", "RECREATE")
  allmuonsPlots = MuonsControlPlots(output.mkdir("allmuons"))
  loosemuonsPlots = MuonsControlPlots(output.mkdir("loosemuons"))
  tightmuonsPlots = MuonsControlPlots(output.mkdir("tightmuons"))
  allelectronsPlots = ElectronsControlPlots(output.mkdir("allelectrons"))
  tightelectronsPlots = ElectronsControlPlots(output.mkdir("tightelectrons"))
  jetmetAK5PFPlots = JetmetControlPlots(output.mkdir("jetmetAK5PF"))
  jetmetAK7PFPlots = JetmetControlPlots(output.mkdir("jetmetAK7PF"))
  vertexPlots = VertexAssociationControlPlots(output.mkdir("vertexAssociation"))
  selectionPlots = EventSelectionControlPlots(output.mkdir("selection"),muChannel=False)

#  path="/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/"
#  path="/storage/data/cms/store/user/favereau/MURun2010A-DiLeptonMu-Dec22/"
#  path="/storage/data/cms/store/user/favereau/ELERun2010A-DiLeptonEle-Dec22/"
#  path="/storage/data/cms/store/user/favereau/ELERun2010B-DiLeptonEle-Dec22/"
#  path="/storage/data/cms/store/user/favereau/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola_2/"
#  path="/storage/data/cms/store/user/favereau/Zbb-TuneZ2/"
  path="/storage/data/cms/store/user/favereau/Zcc-TuneZ2_2/"
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)

  allmuonsPlots.beginJob(muonlabel="allMuons", muonType="none")
  loosemuonsPlots.beginJob(muonlabel="looseMuons", muonType="loose")
  tightmuonsPlots.beginJob(muonlabel="matchedMuons", muonType="tight")
  allelectronsPlots.beginJob(electronlabel="allElectrons", electronType="none")
  tightelectronsPlots.beginJob(electronlabel="matchedElectrons", electronType="tight")
  jetmetAK5PFPlots.beginJob(jetlabel="cleanPatJets")
  jetmetAK7PFPlots.beginJob(jetlabel="cleanPatJetsAK7PF")
  vertexPlots.beginJob()
  selectionPlots.beginJob()

  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    jetmetAK5PFPlots.processEvent(event)
    jetmetAK7PFPlots.processEvent(event)
    allmuonsPlots.processEvent(event)
    loosemuonsPlots.processEvent(event)
    tightmuonsPlots.processEvent(event)
    allelectronsPlots.processEvent(event)
    tightelectronsPlots.processEvent(event)
    vertexPlots.processEvent(event)
    selectionPlots.processEvent(event)
    i += 1

  jetmetAK5PFPlots.endJob()
  jetmetAK7PFPlots.endJob()
  allmuonsPlots.endJob()
  loosemuonsPlots.endJob()
  tightmuonsPlots.endJob()
  allelectronsPlots.endJob()
  tightelectronsPlots.endJob()
  vertexPlots.endJob()
  selectionPlots.endJob()
  output.Close()

runTest()
