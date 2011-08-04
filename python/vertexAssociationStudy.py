#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from eventSelection import *
from vertexAssociation import *
from vertexAssociationControlPlots import *

def runStudy():
  """Simple steering code for the study of jet-vertex association"""
  print "Setup..."
  # initialization
  jetHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  vertexHandle = Handle ("vector<reco::Vertex>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  trigInfoHandle = Handle ("pat::TriggerEvent")
  genHandle = Handle ("vector<reco::GenParticle>")
  # output file
  output = ROOT.TFile("vjAssociationStudy.root", "RECREATE")
  # plots 
  controlPlots=[]
  for i in range(11):
    controlPlots.append(VertexAssociationControlPlots(output.mkdir("v"+str(i+1))))
  # input files
  print "Opening files..."
  path="../testfiles/ttbar/"
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+"/"+fname)
  events = Events (files)
  # start the loop
  print "Starting..."
  for i in range(11):
    controlPlots[i].beginJob(sigcut = 2.)
  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    i += 1
    # check that the event passes Z+jet selection
    event.getByLabel ("cleanPatJets",jetHandle)
    event.getByLabel ("patMETsPF",metHandle)
    event.getByLabel ("Ztighttight",zmuHandle)
    event.getByLabel ("Zelel",zeleHandle)
    jets = jetHandle.product()
    met = metHandle.product()
    zCandidatesMu = zmuHandle.product()
    zCandidatesEle = zeleHandle.product()
    event.getByLabel ("patTriggerEvent",trigInfoHandle)
    triggerInfo = trigInfoHandle.product()
    if not isInCategory(4, eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met)): continue
    # sort according to #vertices and call controlPlots.processEvent for each bin
    # for data-driven estimate, this is the best (MC could separate jets from PU using genjet association)
    event.getByLabel ("goodPV",vertexHandle)
    vertices = vertexHandle.product()
    nvertices = vertices.size()
    if nvertices>10 : nvertices = 11 #last bin is overflow
    if nvertices==0 : continue #this should not happen
    controlPlots[nvertices-1].processEvent(event)
  # save the result and close the root file
  print "Closing..."
  for i in range(11):
    controlPlots[i].endJob()
  output.Close()

