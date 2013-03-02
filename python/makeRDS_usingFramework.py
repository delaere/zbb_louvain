#! /usr/bin/env python

print "beginning of script"

############################################################################################
############################################################################################
###                                                                                      ### 
### makeRDS.py (TdP)                                                                     ### 
###                                                                                      ###  
### Construct a RooDataSet containing standard observables                               ###
###                                                                                      ### 
############################################################################################
############################################################################################

import ROOT
import sys
import os
import itertools
import time

from eventSelection import *
from matrixElementControlPlots import *
from eventSelectionControlPlots import *
from monteCarloSelectionControlPlots import *
from LumiReWeightingControlPlots import *
from BtaggingReWeightingControlPlots import *
from LeptonsReweightingControlPlots import *
from objectsControlPlots import *
from vertexAssociationControlPlots import *
from AnalysisEvent import AnalysisEvent

from ROOT import *
from itertools import combinations
from baseControlPlots import getArgSet
from zbbCommons import zbbfile, zbbme
from optparse import OptionParser

###############
##  USAGE #####
################

narguments = len(sys.argv)
if narguments != 2:
  print "Usage: python ", sys.argv[0], " process"
  print "Examples"

  print "python ", sys.argv[0], " DoubleMu_DataA"
  print "python ", sys.argv[0], " DoubleEle_DataA"
  print "python ", sys.argv[0], " DY_Mu_MC"
  print "python ", sys.argv[0], " DY_El_MC"
  exit()

###################
### Run options ###
###################

print sys.argv
channel = sys.argv[1]
#channel = "DoubleEle_DataA" #"ZZ_El_MC" 
jobNumber = 1
Njobs = 1
MonteCarloPUFileName=zbbfile.pileupMC
DataPUFileName=zbbfile.pileupData
btagPerfData=zbbfile.ssvperfData

btagAlgo="CSV"

from globalLists import pathSkimEMu, checkTrigger, muChannel, dirRDS
path = pathSkimEMu
outputDir=dirRDS
#outputDir=""
#checkTrigger[channel]=False

RooAbsData.setDefaultStorageType(RooAbsData.Tree)

############################################
### Define RooRealVars and RooCategories ###
############################################

obsSet  = RooArgSet()
rds_zbb = RooDataSet("rds_zbb",  "rds_zbb", obsSet)
escp    = EventSelectionControlPlots(dir=None, muChannel=muChannel[channel], checkTrigger=checkTrigger[channel], dataset=rds_zbb, mode="dataset")
jmcp    = JetmetControlPlots(dir=None, dataset=rds_zbb, mode="dataset", muChannel=muChannel[channel])
vacp    = VertexAssociationControlPlots(dir=None, dataset=rds_zbb, mode="dataset")
if zbbme.doMEcontrolPlots:
  mecp	= MatrixElementControlPlots(dir=None, muChannel=muChannel[channel], checkTrigger=checkTrigger[channel], dataset=rds_zbb, mode="dataset")
if channel[-2:] == "MC":
  brcp    = BtaggingReWeightingControlPlots(dir=None, muChannel=muChannel[channel], dataset=rds_zbb, mode="dataset")
  lrcp    = LeptonsReweightingControlPlots(dir=None, muChannel=muChannel[channel], dataset=rds_zbb, mode="dataset")
  mscp    = MonteCarloSelectionControlPlots(dir=None, dataset=rds_zbb, mode="dataset")
  prcp    = LumiReWeightingControlPlots(dir=None, dataset=rds_zbb, mode="dataset")

### input
import glob
files=glob.glob(path[channel]+"*")
print "files = ", files  
events = AnalysisEvent (files)
prepareAnalysisEvent(events, btagging=btagAlgo,ZjetFilter="bcl",checkTrigger=checkTrigger[channel])

if channel[-2:] == "MC":
  events.addWeight("PileUp",LumiReWeighting(MonteCarloFileName=MonteCarloPUFileName, DataFileName=DataPUFileName, systematicShift=0))
  events.addWeight("Btagging",btaggingWeight(0,999,0,999,file=btagPerfData))
  events.addWeight("Leptons",LeptonsReWeighting())


### booking

escp.beginJob()
jmcp.beginJob(btagging=btagAlgo)
vacp.beginJob()
if zbbme.doMEcontrolPlots:
  mecp.beginJob()
if channel[-2:] == "MC":
  brcp.beginJob() 
  lrcp.beginJob()             
  mscp.beginJob()
  prcp.beginJob()
  
ntuple = getArgSet([escp
#                   , mscp
#                   , prcp
#                   , brcp
#                   , lrcp
                    ]) #would it be enought to call rds_zbb.get() or even to use obsSet ???

#ntuple = obsSet
#ntuple = rds_zbb.get()

### categories

escp.defineCategories(categoryNames)

########################
### Run Forest, run! ###
########################

def processInputFile(_muChan=muChannel[channel], _path=path[channel]) :

    print "channel   = ", channel
    print "muChannel = ", _muChan
    print "path      = ", _path

    i=0
    t0 = time.time()
    
    for event in events:
      #if i > 100: break;
      if i%1000==1 :
        print "Processing... event", i, ". Last batch in ", (time.time()-t0),"s."
        t0 = time.time()
      if _muChan :
        categoryData=event.catMu
      else :
        categoryData=event.catEle
      escp.setCategories(map(lambda c:isInCategory(c, categoryData),range(eventCategories())))

      escp.processEvent(event)
      jmcp.processEvent(event)
      vacp.processEvent(event)
      if zbbme.doMEcontrolPlots:
        mecp.processEvent(event)
      if channel[-2:] == "MC":
        brcp.processEvent(event,btagging=btagAlgo)
        lrcp.processEvent(event)
        mscp.processEvent(event)
        prcp.processEvent(event)
      
      ras_escp=escp._obsSet
      ras_jmcp=jmcp._obsSet
      ras_vacp=vacp._obsSet
      if zbbme.doMEcontrolPlots:
        ras_mecp=mecp._obsSet
      if channel[-2:] == "MC":
        ras_lrcp=lrcp._obsSet
        ras_brcp=brcp._obsSet
        ras_mscp=mscp._obsSet
        ras_prcp=prcp._obsSet

      ras_escp.add(ras_vacp)
      ras_escp.add(ras_jmcp)
      if zbbme.doMEcontrolPlots:
        ras_escp.add(ras_mecp)
      if channel[-2:] == "MC":
        ras_escp.add(ras_lrcp)
        ras_escp.add(ras_brcp)
        ras_escp.add(ras_mscp)
        ras_escp.add(ras_prcp)

      #rds_zbb.add(ntuple)
      rds_zbb.add(ras_escp)
      i += 1

    escp.endJob()
    jmcp.endJob()
    vacp.endJob()
    if zbbme.doMEcontrolPlots:
      mecp.endJob()
    if channel[-2:] == "MC":
      brcp.endJob()
      lrcp.endJob()
      mscp.endJob()
      prcp.endJob()

    ws = RooWorkspace("ws","workspace")
    getattr(ws,'import')(rds_zbb)
    ws.Print()

    ras_zbb = rds_zbb.get()
    ws_ras = RooWorkspace("ws_ras","workspace_ras")
    getattr(ws_ras,'import')(ras_zbb)
    ws_ras.Print()
    
    ws_ras.writeToFile(outputDir+"File_rds_zbb_"+channel+".root")
    #ws_ras.writeToFile("test.root")
    gDirectory.Add(ws_ras)

    f=TFile(outputDir+"File_rds_zbb_"+channel+".root","UPDATE")
    #f=TFile("test.root","UPDATE")
    tree_zbb = rds_zbb.tree()
    tree_zbb.Write()
    f.Close()


print "Running processInputFile(", muChannel[channel], ", ", path[channel], ")"
processInputFile(muChannel[channel], path[channel])
