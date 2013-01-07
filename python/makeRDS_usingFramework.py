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
from zbbCommons import zbbfile
from optparse import OptionParser

###############
##  USAGE #####
################

narguments = len(sys.argv)
if narguments != 2:
  print "Usage: python ", sys.argv[0], " process"
  print "Examples"

  print "python ", sys.argv[0], " Mu_DATA"
  print "python ", sys.argv[0], " El_DATA"
  print "python ", sys.argv[0], " Mu_MC"
  print "python ", sys.argv[0], " El_MC"
  exit()

###################
### Run options ###
###################

print sys.argv
channel = sys.argv[1]
#channel = "El_DATA" #"ZZ_El_MC" #"Mu_DATA" "El_DATA", "Mu_MC", "El_MC", "Ttbar_Mu_MC", "Ttbar_El_MC"
jobNumber = 1
Njobs = 1
MonteCarloPUFileName=zbbfile.pileupMC
DataPUFileName=zbbfile.pileupData
btagPerfData=zbbfile.ssvperfData

btagAlgo="CSV"


############
### Maps ###
############

muChannel = { "MuA_DATA"     : True ,
              "ElA_DATA"     : False,
              "MuB_DATA"     : True ,
              "ElB_DATA"     : False,
              "Mu_MC"        : True ,
              "El_MC"        : False,
              "TT_Mu_MC"     : True ,
              "TT_El_MC"     : False,
              "ZZ_Mu_MC"     : True ,
              "ZZ_El_MC"     : False,
              "ZH115_Mu_MC"  : True ,
              "ZH115_El_MC"  : False,
              "ZH120_Mu_MC"  : True ,
              "ZH120_El_MC"  : False,
              "ZH125_Mu_MC"  : True ,
              "ZH125_El_MC"  : False,
              "ZH130_Mu_MC"  : True ,
              "ZH130_El_MC"  : False,
              "ZH135_Mu_MC"  : True ,
              "ZH135_El_MC"  : False,
              "evtgen_MC"    : False,
              "herwig_MC"    : False,
              "pythia_MC"    : False,
              }

path = { 
  "MuA_DATA"     : "/nfs/user/acaudron/skim53X/Mu_DataA/" ,
  "ElA_DATA"     : "/nfs/user/acaudron/skim53X/El_DataA/" ,
  "MuB_DATA"     : "/nfs/user/acaudron/skim53X/Mu_DataB/" ,
  "ElB_DATA"     : "/nfs/user/acaudron/skim53X/El_DataB/" ,
  "Mu_MC"        : "/nfs/user/acaudron/skim53X/DY_MC/"    ,
  "El_MC"        : "/nfs/user/acaudron/skim53X/DY_MC/"    ,
  "TT_Mu_MC"     : "/nfs/user/acaudron/skim53X/TT_MC/"    ,
  "TT_El_MC"     : "/nfs/user/acaudron/skim53X/TT_MC/"    ,
  "ZZ_Mu_MC"     : "/nfs/user/acaudron/skim53X/ZZ_MC/"    ,
  "ZZ_El_MC"     : "/nfs/user/acaudron/skim53X/ZZ_MC/"    ,
  "ZH115_Mu_MC"  : "/nfs/user/acaudron/skim53X/ZH115_MC/" ,
  "ZH115_El_MC"  : "/nfs/user/acaudron/skim53X/ZH115_MC/" ,
  "ZH120_Mu_MC"  : "/nfs/user/acaudron/skim53X/ZH120_MC/" ,
  "ZH120_El_MC"  : "/nfs/user/acaudron/skim53X/ZH120_MC/" ,
  "ZH125_Mu_MC"  : "/nfs/user/acaudron/skim53X/ZH125_MC/" ,
  "ZH125_El_MC"  : "/nfs/user/acaudron/skim53X/ZH125_MC/" ,
  "ZH130_Mu_MC"  : "/nfs/user/acaudron/skim53X/ZH130_MC/" ,
  "ZH130_El_MC"  : "/nfs/user/acaudron/skim53X/ZH130_MC/" ,
  "ZH135_Mu_MC"  : "/nfs/user/acaudron/skim53X/ZH135_MC/" ,
  "ZH135_El_MC"  : "/nfs/user/acaudron/skim53X/ZH135_MC/" ,
  "evtgen_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/evtgen/",
  "herwig_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/herwig/",
  "pythia_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/pythia/",
  "ZA_Mu_MC" : "/nfs/user/acaudron/ZApat/",
  "ZA_El_MC" : "/nfs/user/acaudron/ZApat/"
  }

############################################
### Define RooRealVars and RooCategories ###
############################################

checkTrigger = {
  "MuA_DATA"     : True ,
  "ElA_DATA"     : True ,
  "MuB_DATA"     : True ,
  "ElB_DATA"     : True ,
  "Mu_MC"        : False,
  "El_MC"        : False,
  "TT_Mu_MC"     : False,
  "TT_El_MC"     : False,
  "ZZ_Mu_MC"     : False,
  "ZZ_El_MC"     : False,
  "ZH115_Mu_MC"  : False,
  "ZH115_El_MC"  : False,
  "ZH120_Mu_MC"  : False,
  "ZH120_El_MC"  : False,
  "ZH125_Mu_MC"  : False,
  "ZH125_El_MC"  : False,
  "ZH130_Mu_MC"  : False,
  "ZH130_El_MC"  : False,
  "ZH135_Mu_MC"  : False,
  "ZH135_El_MC"  : False,
  "evtgen_MC"    : False,
  "herwig_MC"    : False,
  "pythia_MC"    : False,
  "ZA_Mu_MC" : False,
  "ZA_El_MC" : False
  }

obsSet  = RooArgSet()
rds_zbb = RooDataSet("rds_zbb",  "rds_zbb", obsSet)
escp    = EventSelectionControlPlots(dir=None, muChannel=muChannel[channel], checkTrigger=checkTrigger[channel], dataset=rds_zbb, mode="dataset")
jmcp    = JetmetControlPlots(dir=None, dataset=rds_zbb, mode="dataset")
vacp    = VertexAssociationControlPlots(dir=None, dataset=rds_zbb, mode="dataset")
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
      #if i > 40: break;
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
      if channel[-2:] == "MC":
        brcp.processEvent(event,btagging=btagAlgo)
        lrcp.processEvent(event)
        mscp.processEvent(event)
        prcp.processEvent(event)
      
      ras_escp=escp._obsSet
      ras_jmcp=jmcp._obsSet
      ras_vacp=vacp._obsSet
      if channel[-2:] == "MC":
        ras_lrcp=lrcp._obsSet
        ras_brcp=brcp._obsSet
        ras_mscp=mscp._obsSet
        ras_prcp=prcp._obsSet

      ras_escp.add(ras_vacp)
      ras_escp.add(ras_jmcp)
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
    if channel[-2:] == "MC":
      brcp.endJob()
      lrcp.endJob()
      mscp.endJob()
      prcp.endJob()

    ws = RooWorkspace("ws","workspace")
    getattr(ws,'import')(rds_zbb)
    ws.Print()

    #ws.writeToFile("File_rds_zbb_"+channel+".root") 
    #gDirectory.Add(ws)

    f=TFile("File_rds_zbb_"+channel+".root","RECREATE")
    rds_zbb.Write()
    f.Close()

print "Running processInputFile(", muChannel[channel], ", ", path[channel], ")"
processInputFile(muChannel[channel], path[channel])
