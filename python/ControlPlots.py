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
parser.add_option("-j", "--jetFlavor", dest="ZjetFilter", default="bcl",
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
                  help="Do not reweight according to btagging.")
parser.add_option("--noLweight",action="store_true",dest="noLweight",
                  help="Do not reweight according to leptons.")
parser.add_option("-w","--btagWeight", dest="BtagEffDataFileName", default="performance_ssv_witheff.root",
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
import time
from DataFormats.FWLite import Events, Handle
from LumiReWeighting import LumiReWeighting
from LeptonsReweighting import LeptonsReWeighting
from btaggingWeight import btaggingWeight
from objectsControlPlots import *
from eventSelectionControlPlots import *
from vertexAssociationControlPlots import *
from LumiReWeightingControlPlots import *
from BtaggingReWeightingControlPlots import *
from LeptonsReweightingControlPlots import *
from eventSelection import eventCategories, eventCategory, isInCategory
from monteCarloSelection import isZbEvent, isZcEvent
#from myFuncTimer import print_timing

jetHandle = Handle ("vector<pat::Jet>")
metHandle = Handle ("vector<pat::MET>")
zmuHandle = Handle ("vector<reco::CompositeCandidate>")
zeleHandle = Handle ("vector<reco::CompositeCandidate>")
trigInfoHandle = Handle ("pat::TriggerEvent")
genHandle = Handle ("vector<reco::GenParticle>")

#@print_timing
def category(event,muChannel,ZjetFilter,checkTrigger,btagAlgo):
  """Compute the event category for histogramming"""
  if not ZjetFilter=="bcl":
    event.getByLabel ("genParticles",genHandle)
    genParticles = genHandle.product()
    if isZbEvent(genParticles,0,False) and not ('b' in ZjetFilter): return [-1]
    if (isZcEvent(genParticles,0,False) and not isZbEvent(genParticles,0,False)) and not ('c' in ZjetFilter): return [-1]
    if (not isZcEvent(genParticles,0,False) and not isZbEvent(genParticles,0,False)) and not ('l' in ZjetFilter): return [-1]
  event.getByLabel("cleanPatJets",jetHandle)
  event.getByLabel("patMETsPF",metHandle)
  #event.getByLabel("ZmuMatchedmuMatched",zmuHandle)
  #event.getByLabel("ZelMatchedelMatched",zeleHandle)
  event.getByLabel("Ztighttight",zmuHandle)
  event.getByLabel("Zelel",zeleHandle)
  jets = jetHandle.product()
  met = metHandle.product()
  zCandidatesMu = zmuHandle.product()
  zCandidatesEle = zeleHandle.product()
  if checkTrigger:
    event.getByLabel("patTriggerEvent",trigInfoHandle)
    triggerInfo = trigInfoHandle.product()
  else:
    triggerInfo = None
  return eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, muChannel,btagAlgo)

def runTest(path, levels, outputname="controlPlots.root", ZjetFilter=False, checkTrigger=False, btagAlgo="SSV", onlyMu=False, onlyEle=False, PUDataFileName=None, PUMonteCarloFileName=None, Njobs=1, jobNumber=1, BtagEffDataFileName=None, handleLeptonEff=True):
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
  vertexPlots=[]
  selectionPlots=[]
  lumiReWeightingPlots=[]
  btagReWeightingPlots=[]
  leptonsReWeightingPlots=[]
  for muChannel in [True, False]:
    if muChannel:
      channelDir = output.mkdir("MuMuChannel")
    else:
      channelDir = output.mkdir("EEChannel")
    for level in range(eventCategories()):
      levelDir = channelDir.mkdir("stage_"+str(level),categoryName(level))
      allmuonsPlots.append(MuonsControlPlots(levelDir.mkdir("allmuons")))
      loosemuonsPlots.append(MuonsControlPlots(levelDir.mkdir("loosemuons")))
      tightmuonsPlots.append(MuonsControlPlots(levelDir.mkdir("tightmuons")))
      allelectronsPlots.append(ElectronsControlPlots(levelDir.mkdir("allelectrons")))
      tightelectronsPlots.append(ElectronsControlPlots(levelDir.mkdir("tightelectrons")))
      jetmetAK5PFPlots.append(JetmetControlPlots(levelDir.mkdir("jetmetAK5PF")))
      vertexPlots.append(VertexAssociationControlPlots(levelDir.mkdir("vertexAssociation")))
      selectionPlots.append(EventSelectionControlPlots(levelDir.mkdir("selection"),muChannel,checkTrigger))
      if handlePU: 
        lumiReWeightingPlots.append(LumiReWeightingControlPlots(levelDir.mkdir("lumiReWeighting")))
      if handleBT:
        btagReWeightingPlots.append(BtaggingReWeightingControlPlots(levelDir.mkdir("btagReWeighting"),muChannel))
      if handleLeptonEff:
        leptonsReWeightingPlots.append(LeptonsReWeightingControlPlots(levelDir.mkdir("leptonsReWeighting"),muChannel))

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
      #vertexPlots[level].beginJob(zlabel="ZmuMatchedmuMatched")
      #selectionPlots[level].beginJob(btagging=btagAlgo, zmulabel="ZmuMatchedmuMatched", zelelabel="ZelMatchedelMatched")
      vertexPlots[level].beginJob(zlabel="Ztighttight")
      selectionPlots[level].beginJob(btagging=btagAlgo, zmulabel="Ztighttight", zelelabel="Zelel")
      if handlePU: lumiReWeightingPlots[level].beginJob(MonteCarloFileName=PUMonteCarloFileName, DataFileName=PUDataFileName, MonteCarloHistName="pileup", DataHistName="pileup")
      if handleBT: btagReWeightingPlots[level].beginJob(perfData=BtagEffDataFileName)
      if handleLeptonEff: leptonsReWeightingPlots[level].beginJob()

  # the PU reweighting engine
  if handlePU: 
    PileUp = LumiReWeighting(MonteCarloFileName=PUMonteCarloFileName, DataFileName=PUDataFileName, MonteCarloHistName="pileup", DataHistName="pileup", systematicShift=0)
  # the Beff reweighting engine. From 1 to 5(=infinity) b-jets
  if handleBT:
    BeffW = btaggingWeight(0,999,0,999,file=BtagEffDataFileName)
  if handleLeptonEff:
    LeffW = LeptonsReWeighting()

  # process events
  i = 0
  t0 = time.time()
  for event in events:
    if i%100==0 : 
      print "Processing... event", i, ". Last batch in ", (time.time()-t0),"s."
      t0 = time.time()
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
      # process event
      if len(plots)>0: 
        jetmetAK5PFPlotsData = jetmetAK5PFPlots[plots[0]].process(event)
        allmuonsPlotsData = allmuonsPlots[plots[0]].process(event)
        loosemuonsPlotsData = loosemuonsPlots[plots[0]].process(event)
        tightmuonsPlotsData = tightmuonsPlots[plots[0]].process(event)
        allelectronsPlotsData = allelectronsPlots[plots[0]].process(event)
        tightelectronsPlotsData = tightelectronsPlots[plots[0]].process(event)
        vertexPlotsData = vertexPlots[plots[0]].process(event)
        selectionPlotsData = selectionPlots[plots[0]].process(event)
        if handlePU: 
            lumiReWeightingPlotsData = lumiReWeightingPlots[plots[0]].process(event)
        if handleBT:
          btagReWeightingPlotsData = btagReWeightingPlots[plots[0]].process(event)
        if handleLeptonEff:
          leptonsReWeightingPlotsData = leptonsReWeightingPlots[plots[0]].process(event)
      for level in plots:
        # compute the weight 
        eventWeight = 1 # here, we could have another method to compute a weight (e.g. btag efficiency per jet, ...)
        if handlePU: eventWeight *= PileUp.weight(fwevent=event)
        if handleLeptonEff: eventWeight *= LeffW.weight(fwevent=event,muChannel=muChannel)
	if handleBT:
          catName = categoryName(level%eventCategories())
	  if catName.find("(HEHE") != -1:
	    BeffW.setMode("HEHE")
	    eventWeight *= BeffW.weight(event,muChannel)
	  elif catName.find("(HEHP") != -1:
	    BeffW.setMode("HEHP")
	    eventWeight *= BeffW.weight(event,muChannel)
	  elif catName.find("(HPHP") != -1:
	    BeffW.setMode("HPHP")
	    eventWeight *= BeffW.weight(event,muChannel)
	  elif catName.find("(HE") != -1:
            if catName.find("exclusive") != -1:
              BeffW.setMode("HEexcl")
	      eventWeight *= BeffW.weight(event,muChannel)
            else:
              BeffW.setMode("HE")
	      eventWeight *= BeffW.weight(event,muChannel)
	  elif catName.find("(HP") != -1:
            if catName.find("exclusive") != -1:
              BeffW.setMode("HPexcl")
	      eventWeight *= BeffW.weight(event,muChannel)
            else:
              BeffW.setMode("HP")
	      eventWeight *= BeffW.weight(event,muChannel)
        # security against negative weights 
        if eventWeight<0: eventWeight=0
        # fill the histograms
        jetmetAK5PFPlots[level].fill(jetmetAK5PFPlotsData, eventWeight)
        allmuonsPlots[level].fill(allmuonsPlotsData, eventWeight)
        loosemuonsPlots[level].fill(loosemuonsPlotsData, eventWeight)
        tightmuonsPlots[level].fill(tightmuonsPlotsData, eventWeight)
        allelectronsPlots[level].fill(allelectronsPlotsData, eventWeight)
        tightelectronsPlots[level].fill(tightelectronsPlotsData, eventWeight)
        vertexPlots[level].fill(vertexPlotsData, eventWeight)
        selectionPlots[level].fill(selectionPlotsData, eventWeight)
        if handlePU: 
            lumiReWeightingPlots[level].fill(lumiReWeightingPlotsData) #no weight
        if handleBT:
          btagReWeightingPlots[level].fill(btagReWeightingPlotsData) #no weight
        if handleLeptonEff:
          leptonsReWeightingPlots[level].fill(leptonsReWeightingPlotsData) #no weight
    i += 1

  # save all
  for muChannel in [True, False]:
    if muChannel: 
      plots = levels
    else:
      plots = map(lambda x: x+eventCategories(),levels)
    for level in plots:
     jetmetAK5PFPlots[level].endJob()
     allmuonsPlots[level].endJob()
     loosemuonsPlots[level].endJob()
     tightmuonsPlots[level].endJob()
     allelectronsPlots[level].endJob()
     tightelectronsPlots[level].endJob()
     vertexPlots[level].endJob()
     selectionPlots[level].endJob()
     if handlePU: 
       lumiReWeightingPlots[level].endJob()
     if handleBT:
       btagReWeightingPlots[level].endJob()
     if handleLeptonEff:
       leptonsReWeightingPlots[level].endJob()
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
  levels.sort()
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
  runTest(path=options.path,outputname=options.outputname, levels=levels, ZjetFilter=options.ZjetFilter, checkTrigger=options.checkTrigger, btagAlgo=options.btagAlgo, onlyMu=options.onlyMu,onlyEle=options.onlyEle,PUDataFileName=options.PUDataFileName,PUMonteCarloFileName=options.PUMonteCarloFileName, Njobs=options.Njobs, jobNumber=options.jobNumber, BtagEffDataFileName=options.BtagEffDataFileName, handleLeptonEff=not(options.noLweight))

if __name__ == "__main__":
  main(options)
