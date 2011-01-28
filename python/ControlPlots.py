#!/usr/bin/env python

from optparse import OptionParser
import sys
usage="""%prog [options]"""
description="""A simple script to generate control plots."""
epilog="""Example:
./ControlPlots.py -i /storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/ -o controlPlots_MURun2010B.root --all
"""
parser = OptionParser(usage=usage,add_help_option=True,description=description,epilog=epilog)
parser.add_option("-i", "--inputPath", dest="path",
                  help="Read input file from DIR.", metavar="DIR")
parser.add_option("-o", "--output", dest='outputname', default="controlPlots.root",
                  help="Save output as FILE.", metavar="FILE")
parser.add_option("--all",action="store_true",dest="all",
                  help="Process all levels.")
parser.add_option("-l", "--level", dest="levels",
                  help="Specify a coma-separated list of levels to be processed. No space is allowed.")
(options, args) = parser.parse_args()
#  path="/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/"
#  path="/storage/data/cms/store/user/favereau/MURun2010A-DiLeptonMu-Dec22/"
#  path="/storage/data/cms/store/user/favereau/ELERun2010A-DiLeptonEle-Dec22/"
#  path="/storage/data/cms/store/user/favereau/ELERun2010B-DiLeptonEle-Dec22/"
#  path="/storage/data/cms/store/user/favereau/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola_2/"
#  path="/storage/data/cms/store/user/favereau/Zbb-TuneZ2/"
#  path="/storage/data/cms/store/user/favereau/Zcc-TuneZ2_2/"

import ROOT
import os
from DataFormats.FWLite import Events, Handle
from objectsControlPlots import *
from eventSelectionControlPlots import *
from vertexAssociationControlPlots import *
from eventSelection import eventCategories, eventCategory

def category(event,muChannel):
  """Compute the event category for histogramming"""
  jetHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  trigInfoHandle = Handle ("vector<bool>")
  event.getByLabel ("cleanPatJets",jetHandle)
  event.getByLabel ("patMETsPF",metHandle)
  event.getByLabel ("Ztighttight",zmuHandle)
  event.getByLabel ("Zelel",zeleHandle)
  #event.getByLabel ("WeightFromTrigger","SelectedTriggers",trigInfoHandle)
  jets = jetHandle.product()
  met = metHandle.product()
  zCandidatesMu = zmuHandle.product()
  zCandidatesEle = zeleHandle.product()
  #triggerInfo = trigInfoHandle.product()
  triggerInfo = None
  return eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, muChannel)

def runTest(path, levels, outputname="controlPlots.root"):
  """produce all the plots in one go"""
  # output file
  output = ROOT.TFile(outputname, "RECREATE")
  # plots
  allmuonsPlots=[]
  loosemuonsPlots=[]
  tightmuonsPlots=[]
  allelectronsPlots=[]
  tightelectronsPlots=[]
  jetmetAK5PFPlots=[]
  jetmetAK7PFPlots=[]
  vertexPlots=[]
  selectionPlots=[]
  for muChannel in [True, False]:
    if muChannel:
      channelDir = output.mkdir("MuMuChannel")
    else:
      channelDir = output.mkdir("EEChannel")
    for level in range(eventCategories()):
      levelDir = channelDir.mkdir("stage_"+str(level))
      allmuonsPlots.append(MuonsControlPlots(levelDir.mkdir("allmuons")))
      loosemuonsPlots.append(MuonsControlPlots(levelDir.mkdir("loosemuons")))
      tightmuonsPlots.append(MuonsControlPlots(levelDir.mkdir("tightmuons")))
      allelectronsPlots.append(ElectronsControlPlots(levelDir.mkdir("allelectrons")))
      tightelectronsPlots.append(ElectronsControlPlots(levelDir.mkdir("tightelectrons")))
      jetmetAK5PFPlots.append(JetmetControlPlots(levelDir.mkdir("jetmetAK5PF")))
      jetmetAK7PFPlots.append(JetmetControlPlots(levelDir.mkdir("jetmetAK7PF")))
      vertexPlots.append(VertexAssociationControlPlots(levelDir.mkdir("vertexAssociation")))
      selectionPlots.append(EventSelectionControlPlots(levelDir.mkdir("selection"),muChannel))

  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)

  # book histograms
  for muChannel in [True, False]:
    if muChannel: 
      plots = levels
    else:
      plots = map(lambda x: x+eventCategories(),levels)
    for level in plots:
      allmuonsPlots[level].beginJob(muonlabel="allMuons", muonType="none")
      loosemuonsPlots[level].beginJob(muonlabel="looseMuons", muonType="loose")
      tightmuonsPlots[level].beginJob(muonlabel="matchedMuons", muonType="tight")
      allelectronsPlots[level].beginJob(electronlabel="allElectrons", electronType="none")
      tightelectronsPlots[level].beginJob(electronlabel="matchedElectrons", electronType="tight")
      jetmetAK5PFPlots[level].beginJob(jetlabel="cleanPatJets")
      jetmetAK7PFPlots[level].beginJob(jetlabel="cleanPatJetsAK7PF")
      vertexPlots[level].beginJob()
      selectionPlots[level].beginJob()

  # process events
  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    for muChannel in [True, False]:
      evtcategory = category(event,muChannel)
      if muChannel: 
        plots = filter(lambda x: x<=evtcategory ,levels)
      else:
        plots = map(lambda x: x+eventCategories(),filter(lambda x: x<=evtcategory ,levels))
      for level in plots:
        jetmetAK5PFPlots[level].processEvent(event)
        jetmetAK7PFPlots[level].processEvent(event)
        allmuonsPlots[level].processEvent(event)
        loosemuonsPlots[level].processEvent(event)
        tightmuonsPlots[level].processEvent(event)
        allelectronsPlots[level].processEvent(event)
        tightelectronsPlots[level].processEvent(event)
        vertexPlots[level].processEvent(event)
        selectionPlots[level].processEvent(event)
    i += 1

  # save all
  for muChannel in [True, False]:
    if muChannel: 
      plots = levels
    else:
      plots = map(lambda x: x+eventCategories(),levels)
    for level in plots:
     jetmetAK5PFPlots[level].endJob()
     jetmetAK7PFPlots[level].endJob()
     allmuonsPlots[level].endJob()
     loosemuonsPlots[level].endJob()
     tightmuonsPlots[level].endJob()
     allelectronsPlots[level].endJob()
     tightelectronsPlots[level].endJob()
     vertexPlots[level].endJob()
     selectionPlots[level].endJob()
  output.Close()

def main(options):
  """simplistic program main"""
  # do basic arg checking
  if options.path is None: 
    print "Error: no input path specified."
    parser.print_help()
    return
  levels = []
  if options.all:
    levels = range(eventCategories())
  elif not options.levels is None:
    levels= map(int,options.levels.split(','))
  if len(levels)==0:
    print "Error: no level specified for processing."
    parser.print_help()
    return
  if min(levels)<0:
    print "Error: levels must be positive integers."
    parser.print_help()
    return
  if max(levels)>=eventCategories():
    print "Error: last level is",eventCategories()-1
    parser.print_help()
    return
  # if all ok, run the procedure
  runTest(path=options.path,outputname=options.outputname, levels=levels)

if __name__ == "__main__":
  main(options)

