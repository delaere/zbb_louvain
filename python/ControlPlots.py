#!/usr/bin/env python 

from optparse import OptionParser
from zbbCommons import zbbfile
import sys
usage="""%prog [options]"""
description="""A simple script to generate control plots."""
epilog="""Example:
./ControlPlots.py -i /storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/ -o controlPlots_MURun2010B.root --all
"""
parser = OptionParser(usage=usage,add_help_option=True,description=description,epilog=epilog)
parser.add_option("-i", "--inputPath", dest="path",
                  help="Read input file from DIR.", metavar="DIR")
parser.add_option("-o", "--output", dest='outputname', default=zbbfile.controlPlots,
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
parser.add_option("--trigger",action="store_true",dest="checkTrigger", default=False, 
                  help="Check the trigger at the early stage of the event selection.")
parser.add_option("-b","--btag", dest="btagAlgo", default="CSV",
                  help="Choice of the btagging algorithm: CSV (default) or SSV.", metavar="ALGO")
parser.add_option("-p", "--PileUpData", dest="PUDataFileName", default=zbbfile.pileupData,
                  help="Read estimated PU distribution for data from file.", metavar="file")
parser.add_option("-P", "--PileUpMC", dest="PUMonteCarloFileName", default=zbbfile.pileupMC,
                  help="Read generated PU distribution for MC from file.", metavar="file")
parser.add_option("--noPUweight",action="store_true",dest="noPUweight",
                  help="Do not reweight according to PU.")
parser.add_option("--noBweight",action="store_true",dest="noBweight",
                  help="Do not reweight according to btagging.")
parser.add_option("--noLweight",action="store_true",dest="noLweight",
                  help="Do not reweight according to leptons.")
parser.add_option("-w","--btagWeight", dest="BtagEffDataFileName", default=zbbfile.ssvperfData,
                  help="Read btagging efficiencies and SF from file.", metavar="file")
parser.add_option("--NLO",action="store_true",dest="NLOWeight",
                  help="Weight from NLO corrections .")
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
from AnalysisEvent import AnalysisEvent
from eventSelection import eventCategories, eventCategory, isInCategory, prepareAnalysisEvent
from LumiReWeighting import LumiReWeighting
from LeptonsReweighting import LeptonsReWeighting
from btaggingWeight import btaggingWeight
from objectsControlPlots import *
from eventSelectionControlPlots import *
from vertexAssociationControlPlots import *
from LumiReWeightingControlPlots import *
from BtaggingReWeightingControlPlots import *
from LeptonsReweightingControlPlots import *
from MonteCarloReweighting import *
from zbbCommons import zbblabel
import cProfile

def runTest(path, levels, outputname=zbbfile.controlPlots, ZjetFilter=False, checkTrigger=False, btagAlgo="CSV", onlyMu=False, onlyEle=False, PUDataFileName=None, PUMonteCarloFileName=None,NLOWeight=None, Njobs=1, jobNumber=1, BtagEffDataFileName=None, handleLeptonEff=True):
  """produce all the plots in one go"""
  # Summary flags for the PU and btag reweighting
  handlePU = not (PUDataFileName is None or PUMonteCarloFileName is None)
  handleBT = not (BtagEffDataFileName is None)

  # inputs
  dirList=list(itertools.islice(os.listdir(path), jobNumber, None, Njobs))
  files=[]
  for fname in dirList:
    files.append(path+"/"+fname)

  # output
  output = ROOT.TFile(outputname, "RECREATE")

  # events iterator, plus configuration of standard collections and producers
  events = AnalysisEvent(files)
  prepareAnalysisEvent(events,btagging=btagAlgo,ZjetFilter=ZjetFilter,checkTrigger=checkTrigger)

  # the reweighting codes
  if handlePU: 
    events.addWeight("PileUp",LumiReWeighting(MonteCarloFileName=PUMonteCarloFileName, DataFileName=PUDataFileName, systematicShift=0))
  if handleBT: 
    events.addWeight("Btagging",btaggingWeight(0,999,0,999,file=BtagEffDataFileName))
  if handleLeptonEff: 
    events.addWeight("Leptons",LeptonsReWeighting())
  if NLOWeight: 
    events.addWeight("MonteCarlo",MonteCarloReWeighting())
  
  # prepare the plots
  allmuonsPlots=[]
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
      tightmuonsPlots.append(MuonsControlPlots(levelDir.mkdir("tightmuons")))
      allelectronsPlots.append(ElectronsControlPlots(levelDir.mkdir("allelectrons")))
      tightelectronsPlots.append(ElectronsControlPlots(levelDir.mkdir("tightelectrons")))
      jetmetAK5PFPlots.append(JetmetControlPlots(levelDir.mkdir("jetmetAK5PF"),muChannel))
      vertexPlots.append(VertexAssociationControlPlots(levelDir.mkdir("vertexAssociation")))
      selectionPlots.append(EventSelectionControlPlots(levelDir.mkdir("selection"),muChannel,checkTrigger))
      if handlePU: 
        lumiReWeightingPlots.append(LumiReWeightingControlPlots(levelDir.mkdir("lumiReWeighting")))
      if handleBT:
        btagReWeightingPlots.append(BtaggingReWeightingControlPlots(levelDir.mkdir("btagReWeighting"),muChannel))
      if handleLeptonEff:
        leptonsReWeightingPlots.append(LeptonsReweightingControlPlots(levelDir.mkdir("leptonsReWeighting"),muChannel))

  # book histograms
  for muChannel in [True, False]:
    if muChannel: 
      plots = levels
      zlabel= zbblabel.zmumulabel
    else:
      plots = map(lambda x: x+eventCategories(),levels)
      zlabel= zbblabel.zelelabel
    for level in plots:
      allmuonsPlots[level].beginJob(muonList = "allmuons", muonType="none")
      tightmuonsPlots[level].beginJob(muonType="tight")
      allelectronsPlots[level].beginJob(electronList="allelectrons", electronType="none")
      tightelectronsPlots[level].beginJob(electronType="tight")
      jetmetAK5PFPlots[level].beginJob(btagging=btagAlgo)
      vertexPlots[level].beginJob()
      selectionPlots[level].beginJob()
      if handlePU: lumiReWeightingPlots[level].beginJob()
      if handleBT: btagReWeightingPlots[level].beginJob(perfData=BtagEffDataFileName)
      if handleLeptonEff: leptonsReWeightingPlots[level].beginJob()

  # process events
  i = 0
  t0 = time.time()
  for event in events:
    runNumber= event.run()
    # force JES and JER to 0 for data
    if event.object().event().eventAuxiliary().isRealData():
      zbbsystematics.JERfactor = 0
      zbbsystematics.JESfactor = 0
    # printout
    if i%100==0 : 
      print "Processing... event", i, ". Last batch in ", (time.time()-t0),"s."
      t0 = time.time()
    # loop on channels
    for muChannel in [True, False]:
      if muChannel: 
        categoryData = event.catMu
        plots = [] if onlyEle else filter(lambda x: isInCategory(x,categoryData) ,levels)
      else:
        categoryData = event.catEle
        plots = [] if onlyMu else map(lambda x: x+eventCategories(),filter(lambda x: isInCategory(x,categoryData) ,levels))
      # process event
      if len(plots)>0: 
        jetmetAK5PFPlotsData = jetmetAK5PFPlots[plots[0]].process(event)
        allmuonsPlotsData = allmuonsPlots[plots[0]].process(event)
        tightmuonsPlotsData = tightmuonsPlots[plots[0]].process(event)
        allelectronsPlotsData = allelectronsPlots[plots[0]].process(event)
        tightelectronsPlotsData = tightelectronsPlots[plots[0]].process(event)
        vertexPlotsData = vertexPlots[plots[0]].process(event)
        selectionPlotsData = selectionPlots[plots[0]].process(event)
        if handlePU: lumiReWeightingPlotsData = lumiReWeightingPlots[plots[0]].process(event)
        if handleBT: btagReWeightingPlotsData = btagReWeightingPlots[plots[0]].process(event,btagging=btagAlgo)
        if handleLeptonEff: leptonsReWeightingPlotsData = leptonsReWeightingPlots[plots[0]].process(event)
      for level in plots:
        # compute the weight 
        eventWeight = event.weight(muChannel=muChannel,Bmode=btaggingWeightMode(categoryName(level%eventCategories())), MCmode="mc")
        # fill the histograms
        jetmetAK5PFPlots[level].fill(jetmetAK5PFPlotsData, eventWeight)
        allmuonsPlots[level].fill(allmuonsPlotsData, eventWeight)
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
  runTest(path=options.path,outputname=options.outputname, levels=levels, ZjetFilter=options.ZjetFilter, checkTrigger=options.checkTrigger, btagAlgo=options.btagAlgo, onlyMu=options.onlyMu,onlyEle=options.onlyEle,PUDataFileName=options.PUDataFileName,PUMonteCarloFileName=options.PUMonteCarloFileName, Njobs=options.Njobs, jobNumber=options.jobNumber, BtagEffDataFileName=options.BtagEffDataFileName, handleLeptonEff=not(options.noLweight),NLOWeight=options.NLOWeight)

def btaggingWeightMode(catName):
  if catName.find("(HEHE") != -1:
    return "HEHE"
  elif catName.find("(HEHP") != -1:
    return "HEHP"
  elif catName.find("(HPHP") != -1:
    return "HPHP"
  elif catName.find("(HE") != -1:
    if catName.find("exclusive") != -1:
      return "HEexcl"
    else:
      return "HE"
  elif catName.find("(HP") != -1:
    if catName.find("exclusive") != -1:
      return "HPexcl"
    else:
      return "HP"
  return "None"

if __name__ == "__main__":
  main(options)
  #cProfile.run('main(options)', 'controlPlots.prof')
