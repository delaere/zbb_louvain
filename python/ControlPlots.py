#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from objectsControlPlots import *
from eventSelectionControlPlots import *
from vertexAssociationControlPlots import *

def runTest():
  output = ROOT.TFile("controlPlots.root", "RECREATE")
  muonsPlots = MuonsControlPlots(output.mkdir("muons"))
  electronsPlots = ElectronsControlPlots(output.mkdir("electrons"))
  jetmetPlots = JetmetControlPlots(output.mkdir("jetmet"))
  vertexPlots = VertexAssociationControlPlots(output.mkdir("vertexAssociation"))
  selectionPlots = EventSelectionControlPlots(output.mkdir("selection"))

  path="/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/"
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)

  muonsPlots.beginJob()
  electronsPlots.beginJob()
  jetmetPlots.beginJob()
  vertexPlots.beginJob()
  selectionPlots.beginJob()

  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    jetmetPlots.processEvent(event)
    muonsPlots.processEvent(event)
    electronsPlots.processEvent(event)
    vertexPlots.processEvent(event)
    selectionPlots.processEvent(event)
    i += 1

  jetmetPlots.endJob()
  muonsPlots.endJob()
  electronsPlots.endJob()
  vertexPlots.endJob()
  selectionPlots.endJob()
  output.Close()

runTest()
