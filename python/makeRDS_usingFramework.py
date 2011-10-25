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

from DataFormats.FWLite import Events, Handle
from eventSelection import *
from eventSelectionControlPlots import *
from monteCarloSelectionControlPlots import *
from LumiReWeightingControlPlots import *
from BtaggingReWeightingControlPlots import *
from LeptonsReweightingControlPlots import *
from ROOT import *
from itertools import combinations
from baseControlPlots import getArgSet

from eventSelection import eventCategories, eventCategory, isInCategory

###################
### Run options ###
###################

channel = "Mu_MC" #"Mu_DATA" "El_DATA", "Mu_MC", "El_MC", "Ttbar_Mu_MC", "Ttbar_El_MC"
jobNumber = 1
Njobs = 1
MonteCarloPUFileName="./PUdistMC.root"
DataPUFileName="./PUdistDATA.root"
btagPerfData="../testfiles/performance_ssv_witheff.root"

############
### Maps ###
############

muChannel = { "Mu_DATA"     : True,
              "El_DATA"     : False,
              "Mu_MC"       : True,
              "El_MC"       : False,
              "Ttbar_Mu_MC" : True,
              "Ttbar_El_MC" : False
              }

path = { "Mu_DATA"     : "/home/fynu/tdupree/store/zbb_13Sep/Mu_Data/",
         "El_DATA"     : "/home/fynu/tdupree/store/zbb_13Sep/El_Data/",
         "Ttbar_Mu_MC" : "/home/fynu/tdupree/store/zbb_13Sep/TT_MC/",
         "Ttbar_El_MC" : "/home/fynu/tdupree/store/zbb_13Sep/TT_MC/",
         "Mu_MC"       : "/home/fynu/tdupree/store/zbb_13Sep/DY_MC/",
         "El_MC"       : "/home/fynu/tdupree/store/zbb_13Sep/DY_MC/"
         }

###############################
### Proxy for eventCategory ###
###############################

jetHandle = Handle ("vector<pat::Jet>")
metHandle = Handle ("vector<pat::MET>")
zmuHandle = Handle ("vector<reco::CompositeCandidate>")
zeleHandle = Handle ("vector<reco::CompositeCandidate>")
trigInfoHandle = Handle ("pat::TriggerEvent")
genHandle = Handle ("vector<reco::GenParticle>")

def category(event,muChannel,ZjetFilter,checkTrigger,btagAlgo):
  """Compute the event category for histogramming"""
  if not ZjetFilter=="bcl":
    event.getByLabel (zbblabel.genlabel,genHandle)
    genParticles = genHandle.product()
    if isZbEvent(genParticles,0,False) and not ('b' in ZjetFilter): return [-1]
    if (isZcEvent(genParticles,0,False) and not isZbEvent(genParticles,0,False)) and not ('c' in ZjetFilter): return [-1]
    if (not isZcEvent(genParticles,0,False) and not isZbEvent(genParticles,0,False)) and not ('l' in ZjetFilter): return [-1]
  event.getByLabel(zbblabel.jetlabel,jetHandle)
  event.getByLabel(zbblabel.metlabel,metHandle)
  event.getByLabel(zbblabel.zmumulabel,zmuHandle)
  event.getByLabel(zbblabel.zelelabel,zeleHandle)
  jets = jetHandle.product()
  met = metHandle.product()
  zCandidatesMu = zmuHandle.product()
  zCandidatesEle = zeleHandle.product()
  if checkTrigger:
    event.getByLabel(zbblabel.triggerlabel,trigInfoHandle)
    triggerInfo = trigInfoHandle.product()
  else:
    triggerInfo = None
  return eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, muChannel,btagAlgo)

############################################
### Define RooRealVars and RooCategories ###
############################################

obsSet  = RooArgSet()
rds_zbb = RooDataSet("rds_zbb",  "rds_zbb", obsSet)
escp    = EventSelectionControlPlots(dir=None, muChannel=muChannel[channel], checkTrigger=False, dataset=rds_zbb, mode="dataset")
mscp    = MonteCarloSelectionControlPlots(dir=None, dataset=rds_zbb, mode="dataset")
prcp    = LumiReWeightingControlPlots(dir=None, dataset=rds_zbb, mode="dataset")
brcp    = BtaggingReWeightingControlPlots(dir=None, muChannel=muChannel[channel], dataset=rds_zbb, mode="dataset")
lrcp    = LeptonsReweightingControlPlots(dir=None, muChannel=muChannel[channel], dataset=rds_zbb, mode="dataset")

### input

dirList=list(itertools.islice(os.listdir(path[channel]), jobNumber, None, Njobs))
files=[]
for fname in dirList:
  files.append(path[channel]+"/"+fname)
print "files = ", files  
events = Events (files)

### booking

escp.beginJob(btagging="SSV", zmulabel=zbblabel.zmumulabel, zelelabel=zbblabel.zelelabel)
mscp.beginJob(genlabel=zbblabel.genlabel)
prcp.beginJob(MonteCarloPUFileName, DataPUFileName, MonteCarloHistName="pileup", DataHistName="pileup", vertexlabel=zbblabel.vertexlabel, pulabel=zbblabel.pulabel)
brcp.beginJob(btagPerfData)
lrcp.beginJob()
ntuple = getArgSet([escp, mscp, prcp, brcp, lrcp]) #would it be enought to call rds_zbb.get() or even to use obsSet ???

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
      if i%100==0 :
        print "Processing... event", i, ". Last batch in ", (time.time()-t0),"s."
        t0 = time.time()
      categoryData = category(event,_muChan,ZjetFilter="bcl",checkTrigger=False,btagAlgo="SSV")
      escp.setCategories(map(lambda c:isInCategory(c, categoryData),range(eventCategories())))
      escp.processEvent(event)
      mscp.processEvent(event)
      prcp.processEvent(event)
      brcp.processEvent(event)
      lrcp.processEvent(event)
      rds_zbb.add(ntuple)
      i += 1

    escp.endJob()
    mscp.endJob()
    prcp.endJob()
    brcp.endJob()
    lrcp.endJob()

    ws = RooWorkspace("ws","workspace")
    getattr(ws,'import')(rds_zbb)
    ws.Print()

    ws.writeToFile("File_rds_zbb_"+channel+".root") 
    gDirectory.Add(ws)

