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
from ROOT import *

from eventSelection import eventCategories, eventCategory, isInCategory

###################
### Run options ###
###################

channel = "Mu_MC" #"Mu_DATA" "El_DATA", "Mu_MC", "El_MC", "Ttbar_Mu_MC", "Ttbar_El_MC"
jobNumber = 1
Njobs = 1

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
    event.getByLabel ("genParticles",genHandle)
    genParticles = genHandle.product()
    if isZbEvent(genParticles,0,False) and not ('b' in ZjetFilter): return [-1]
    if (isZcEvent(genParticles,0,False) and not isZbEvent(genParticles,0,False)) and not ('c' in ZjetFilter): return [-1]
    if (not isZcEvent(genParticles,0,False) and not isZbEvent(genParticles,0,False)) and not ('l' in ZjetFilter): return [-1]
  event.getByLabel("cleanPatJets",jetHandle)
  event.getByLabel("patMETsPF",metHandle)
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

############################################
### Define RooRealVars and RooCategories ###
############################################

obsSet  = RooArgSet()
rds_zbb = RooDataSet("rds_zbb",  "rds_zbb", obsSet)
escp    = EventSelectionControlPlots(dir=None, muChannel=muChannel[channel], checkTrigger=False, dataset=rds_zbb, mode="dataset")

### input

dirList=list(itertools.islice(os.listdir(path[channel]), jobNumber, None, Njobs))
files=[]
for fname in dirList:
  files.append(path[channel]+"/"+fname)
events = Events (files)

### booking

escp.beginJob(btagging="SSV", zmulabel="Ztighttight", zelelabel="Zelel")

### categories

rooCategories = { }
for i in range(eventCategories()):
  rc = RooCategory("rc_"+str(i),categoryName(i))
  rc.defineType("not_acc",0)
  rc.defineType("acc",1)
  rooCategories[i] = rc
  rds_zbb.addColumn(rc)
  escp._obsSet.add(rc) # this is not clean at all -> shows that this has to move somehow to the base class itself.

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
      for i in range(eventCategories()):
        if isInCategory(i, categoryData):  rooCategories[i].setIndex(1)
	else: rooCategories[i].setIndex(0)
      escp.processEvent(event)
      i += 1

    escp.endJob()

    ws = RooWorkspace("ws","workspace")
    getattr(ws,'import')(rds_zbb)
    ws.Print()

    ws.writeToFile("File_rds_zbb_"+channel+".root") 
    gDirectory.Add(ws)

