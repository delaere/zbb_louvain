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
parser.add_option("--onlyMu",action="store_true",dest="onlyMu",
                  help="Fill only the muon channel plots.")
parser.add_option("--onlyEle",action="store_true",dest="onlyEle",
                  help="Fill only the electron channel plots.")
parser.add_option("-j", "--jetFlavor", dest="ZjetFilter", default="bcl"
                  help="Jet flavor filter. Examples: --jetFlavor b or --jetFlavor cl")
parser.add_option("--trigger",action="store_true",dest="checkTrigger",
                  help="Check the trigger at the early stage of the .")
parser.add_option("-b","--btag", dest="btagAlgo", default="SSV",
                  help="Choice of the btagging algorithm: SSV (default) or TC.", metavar="ALGO")
parser.add_option("-p", "--PileUpData", dest="PUDataFileName", default="PUdist.root",
                  help="Read estimated PU distribution for data from file.", metavar="file")
parser.add_option("-P", "--PileUpMC", dest="PUMonteCarloFileName", default="PUdistMC.root",
                  help="Read generated PU distribution for MC from file.", metavar="file")
parser.add_option("--noPUweight",action="store_true",dest="noPUweight",
                  help="Do not reweight according to PU.")
parser.add_option("--noBweight",action="store_true",dest="noBweight",
                  help="Do not reweight accodring to btagging.")
parser.add_option("-w","--btagWeight", dest="BtagEffDataFileName", default="performance_ssv.root",
                  help="Read btagging efficiencies and SF from file.", metavar="file")
parser.add_option("--Njobs", type="int", dest='Njobs', default="1",
                  help="Number of jobs when splitting the processing.")
parser.add_option("--jobNumber", type="int", dest='jobNumber', default="0",
                  help="Number of the job is a splitted set of jobs.")

#Njobs, jobNumber
(options, args) = parser.parse_args()

import ROOT
import os
import itertools
from DataFormats.FWLite import Events, Handle
from LumiReWeighting import LumiReWeighting
from objectsControlPlots import *
from eventSelectionControlPlots import *
from vertexAssociationControlPlots import *
from LumiReWeightingControlPlots import *
from btaggingWeight import btaggingWeight
from eventSelection import eventCategories, eventCategory, isInCategory
 #from eventSelection_Test_JES import eventCategories, eventCategory, isInCategory
from monteCarloSelection import isZbEvent, isZcEvent

jetHandle = Handle ("vector<pat::Jet>")
metHandle = Handle ("vector<pat::MET>")
zmuHandle = Handle ("vector<reco::CompositeCandidate>")
zeleHandle = Handle ("vector<reco::CompositeCandidate>")
trigInfoHandle = Handle ("pat::TriggerEvent")
genHandle = Handle ("vector<reco::GenParticle>")

def category(event,muChannel,ZjetFilter,checkTrigger,btagAlgo):
  """Compute the event category for histogramming"""
  if not ZjetFilter=="bcl":
    event.getByLabel ("genParticles",genHandle)
    genParticles = genHandle.product()
    if isZbEvent(genParticles,0,False) and not ('b' in ZjetFilter): return [-1]
    if (isZcEvent(genParticles,0,False) and not isZbEvent(genParticles,0,False)) and not ('c' in ZjetFilter): return [-1]
    if (not isZcEvent(genParticles,0,False) and not isZbEvent(genParticles,0,False)) and not ('l' in ZjetFilter): return [-1]
  event.getByLabel ("cleanPatJets",jetHandle)
  event.getByLabel ("patMETsPF",metHandle)
  event.getByLabel ("Ztighttight",zmuHandle)
  event.getByLabel ("Zelel",zeleHandle)
  jets = jetHandle.product()
  met = metHandle.product()
  zCandidatesMu = zmuHandle.product()
  zCandidatesEle = zeleHandle.product()
  if checkTrigger:
    event.getByLabel ("patTriggerEvent",trigInfoHandle)
    triggerInfo = trigInfoHandle.product()
  else:
    triggerInfo = None
  return eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, muChannel,btagAlgo)

def runTest(path, levels, outputname="controlPlots.root", ZjetFilter=False, checkTrigger=False, btagAlgo="SSV", onlyMu=False, onlyEle=False, PUDataFileName=None, PUMonteCarloFileName=None, Njobs=1, jobNumber=1, BtagEffDataFileName=None):
  """produce all the plots in one go"""
  # output file
  output = ROOT.TFile(outputname, "RECREATE")

  # for the PU
  handlePU = not (PUDataFileName is None or PUMonteCarloFileName is None)

  # for the btag reweighting
  handleBT = not (BtagEffDataFileName is None)

  # prepare the plots
  allmuonsPlots=[]
  loosemuonsPlots=[]
  tightmuonsPlots=[]
  allelectronsPlots=[]
  tightelectronsPlots=[]
  jetmetAK5PFPlots=[]
  jetmetAK7PFPlots=[]
  vertexPlots=[]
  selectionPlots=[]
  lumiReWeightingPlots=[]
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
      selectionPlots.append(EventSelectionControlPlots(levelDir.mkdir("selection"),muChannel,checkTrigger))
      if handlePU: 
        lumiReWeightingPlots.append(LumiReWeightingControlPlots(levelDir.mkdir("lumiReWeighting")))
      #TODO: we do not have control plots for Beff reweighting

  # inputs
  dirList=list(itertools.islice(os.listdir(path), jobNumber, None, Njobs))
  files=[]
  for fname in dirList:
    files.append(path+"/"+fname)
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
      jetmetAK5PFPlots[level].beginJob(jetlabel="cleanPatJets",btagging=btagAlgo)
      jetmetAK7PFPlots[level].beginJob(jetlabel="cleanPatJetsAK7PF",btagging=btagAlgo)
      vertexPlots[level].beginJob()
      selectionPlots[level].beginJob(btagging=btagAlgo)
      if handlePU: 
        lumiReWeightingPlots[level].beginJob(MonteCarloFileName="MCpudist.root", DataFileName="pudist.root", MonteCarloHistName="pileup", DataHistName="pileup")

  # the PU reweighting engine
  if handlePU: 
    PileUp = LumiReWeighting(MonteCarloFileName=PUMonteCarloFileName, DataFileName=PUDataFileName, MonteCarloHistName="pileup", DataHistName="pileup", systematicShift=0)
  # the Beff reweighting engine. From 1 to 5(=infinity) b-jets
  if handleBT:
    BeffW_HE = btaggingWeight(1,5,workingPoint="HE", algo="SSV", file=BtagEffDataFileName)
    BeffW_HP = btaggingWeight(1,5,workingPoint="HP", algo="SSV", file=BtagEffDataFileName)

  # process events
  i = 0
  for event in events:
    if i%100==0 : print "Processing... event ", i
    for muChannel in [True, False]:
      categoryData = category(event,muChannel,ZjetFilter,checkTrigger,btagAlgo)
      if muChannel: 
        if onlyEle:
	  plots = []
	else:
          plots = filter(lambda x: isInCategory(x,categoryData) ,levels)
      else:
        if onlyMu:
	  plots = []
	else:
          plots = map(lambda x: x+eventCategories(),filter(lambda x: isInCategory(x,categoryData) ,levels))
      for level in plots:
        eventWeight = 1 # here, we could have another method to compute a weight (e.g. btag efficiency per jet, ...)
        if handlePU: eventWeight *= PileUp.weight(fwevent=event)
	if handleBT: 
	  #TODO: Note that this is only strictly correct for single bjets, for now.
	  try:
	    HElevels=[5,7,9,10,12,13]
	    HElevels.index(level)
          except:
	    pass
	  else:
            eventWeight *= BeffW_HE.weight(event)
	  try:
	    HPlevels=[6,8,10,11,13,14]
	    HPlevels.index(level)
          except:
	    pass
	  else:
            eventWeight *= BeffW_HP.weight(event)
        jetmetAK5PFPlots[level].processEvent(event, eventWeight)
        #jetmetAK7PFPlots[level].processEvent(event, eventWeight)
        allmuonsPlots[level].processEvent(event, eventWeight)
        loosemuonsPlots[level].processEvent(event, eventWeight)
        tightmuonsPlots[level].processEvent(event, eventWeight)
        allelectronsPlots[level].processEvent(event, eventWeight)
        tightelectronsPlots[level].processEvent(event, eventWeight)
        vertexPlots[level].processEvent(event, eventWeight)
        selectionPlots[level].processEvent(event, eventWeight)
        if handlePU: 
          lumiReWeightingPlots[level].processEvent(event, eventWeight)
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
     if handlePU: 
       lumiReWeightingPlots[level].endJob()
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
  if options.onlyMu and options.onlyEle:
    print "Error: --onlyMu and --onlyEle are exclusive."
    parser.print_help()
    return
  if options.noPUweight:
    options.PUDataFileName = None
    options.PUMonteCarloFileName = None
  else:
    if not os.path.isfile(options.PUDataFileName):
      print "Error: ",options.PUDataFileName, ": No such file."
      parser.print_help()
      return
    if not os.path.isfile(options.PUMonteCarloFileName):
      print "Error: ",options.PUMonteCarloFileName, ": No such file."
      parser.print_help()
      return
  if options.noBweight:
    options.BtagEffDataFileName = None
  else:
    if not os.path.isfile(options.BtagEffDataFileName):
      print "Error: ",options.BtagEffDataFileName, ": No such file."
      parser.print_help()
      return
  if options.Njobs<1:
    print "Error: Njobs must be strictly positive."
    parser.print_help()
    return
  if options.jobNumber>=options.Njobs:
    print "Error: jobNumber must be strictly smaller than Njobs."
    parser.print_help()
    return
  # if all ok, run the procedure
  runTest(path=options.path,outputname=options.outputname, levels=levels, ZjetFilter=options.ZjetFilter, checkTrigger=options.checkTrigger, btagAlgo=options.btagAlgo, onlyMu=options.onlyMu,onlyEle=options.onlyEle,PUDataFileName=options.PUDataFileName,PUMonteCarloFileName=options.PUMonteCarloFileName, Njobs=options.Njobs, jobNumber=options.jobNumber, BtagEffDataFileName=options.BtagEffDataFileName)

if __name__ == "__main__":
  main(options)
