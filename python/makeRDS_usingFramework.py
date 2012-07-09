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
from objectsControlPlots import *
from vertexAssociationControlPlots import *

from ROOT import *
from itertools import combinations
from baseControlPlots import getArgSet
from zbbCommons import zbbfile
from eventSelection import eventCategories, eventCategory, isInCategory

###################
### Run options ###
###################

channel = "El_DATA" #"ZZ_El_MC" #"Mu_DATA" "El_DATA", "Mu_MC", "El_MC", "Ttbar_Mu_MC", "Ttbar_El_MC"
jobNumber = 1
Njobs = 1
MonteCarloPUFileName=zbbfile.pileupMC
DataPUFileName=zbbfile.pileupData
btagPerfData=zbbfile.ssvperfData

############
### Maps ###
############

muChannel = { "Mu_DATA"     : True,
              "El_DATA"     : False,
              "Mu_MC"       : True,
              "El_MC"       : False,
              "Ttbar_Mu_MC" : True,
              "Ttbar_El_MC" : False,
              "ZZ_Mu_MC"    : True,
              "ZZ_El_MC"    : False,
              "ZHbb_Mu_MC"  : True,
              "ZHbb_El_MC"  : False
              }

path = { "Mu_DATA"     : "/storage/data/cms/store/user/acaudron/skim/Mu_Data/" ,
         "El_DATA"     : "/storage/data/cms/store/user/acaudron/skim/El_Data/" ,
         "Ttbar_Mu_MC" : "/storage/data/cms/store/user/acaudron/skim/TT_MC/"   ,
         "Ttbar_El_MC" : "/storage/data/cms/store/user/acaudron/skim/TT_MC/"   ,
         "Mu_MC"       : "/storage/data/cms/store/user/acaudron/skim/DY_MC/"   ,
         "El_MC"       : "/storage/data/cms/store/user/acaudron/skim/DY_MC/"   ,
         "ZZ_Mu_MC"    : "/storage/data/cms/store/user/acaudron/skim/ZZ_MC/"   ,
         "ZZ_El_MC"    : "/storage/data/cms/store/user/acaudron/skim/ZZ_MC/"   ,
         "ZHbb_Mu_MC"  : "/storage/data/cms/store/user/acaudron/skim/ZH_MC/"   , 
         "ZHbb_El_MC"  : "/storage/data/cms/store/user/acaudron/skim/ZH_MC/"   ,
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
vertexHandle = Handle ("vector<reco::Vertex>")
#rhoHandle = Handle ("double")


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
  event.getByLabel(zbblabel.vertexlabel,vertexHandle)
  #event.getByLabel("kt6PFJetsForIsolation","rho",rhoHandle)

  runNumber= event.eventAuxiliary().run()
  
  jets = jetHandle.product()
  met = metHandle.product()
  zCandidatesMu = zmuHandle.product()
  zCandidatesEle = zeleHandle.product()
  vertices = vertexHandle.product()
  #rho = rhoHandle.product()
  if checkTrigger:
    event.getByLabel(zbblabel.triggerlabel,trigInfoHandle)
    triggerInfo = trigInfoHandle.product()
  else:
    triggerInfo = None
  #print triggerInfo   
  return eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, vertices, jets, met, runNumber, muChannel, btagAlgo, 15., event.eventAuxiliary().luminosityBlock())

############################################
### Define RooRealVars and RooCategories ###
############################################

checkTrigger = {
              "Mu_DATA"     : True,
              "El_DATA"     : True,
              "Mu_MC"       : False,
              "El_MC"       : False,
              "Ttbar_Mu_MC" : False,
              "Ttbar_El_MC" : False,
              "ZZ_Mu_MC"    : False,
              "ZZ_El_MC"    : False,
              "ZHbb_Mu_MC"  : False,
              "ZHbb_El_MC"  : False
              }

obsSet  = RooArgSet()
rds_zbb = RooDataSet("rds_zbb",  "rds_zbb", obsSet)
escp    = EventSelectionControlPlots(dir=None, muChannel=muChannel[channel], checkTrigger=checkTrigger[channel], dataset=rds_zbb, mode="dataset")
brcp    = BtaggingReWeightingControlPlots(dir=None, muChannel=muChannel[channel], dataset=rds_zbb, mode="dataset")
lrcp    = LeptonsReweightingControlPlots(dir=None, muChannel=muChannel[channel], dataset=rds_zbb, mode="dataset")
jmcp    = JetmetControlPlots(dir=None, dataset=rds_zbb, mode="dataset")
vacp    = VertexAssociationControlPlots(dir=None, dataset=rds_zbb, mode="dataset")
if channel[-2:] == "MC":
  mscp    = MonteCarloSelectionControlPlots(dir=None, dataset=rds_zbb, mode="dataset")
  prcp    = LumiReWeightingControlPlots(dir=None, dataset=rds_zbb, mode="dataset")

### input

#dirList=list(itertools.islice(os.listdir(path[channel]), jobNumber, None, Njobs))
#files=[]
#for fname in dirList:
#  print "fname = ", fname
#  files.append(path[channel]+"/"+fname)
import glob
files=glob.glob(path[channel]+"*")
print "files = ", files  
events = Events (files)

### booking

escp.beginJob(btagging="SSV", zmulabel=zbblabel.zmumulabel, zelelabel=zbblabel.zelelabel)
brcp.beginJob(btagPerfData) 
lrcp.beginJob()             
jmcp.beginJob()             
vacp.beginJob()             
if channel[-2:] == "MC":
  mscp.beginJob(genlabel=zbblabel.genlabel)
  prcp.beginJob(MonteCarloPUFileName, DataPUFileName, MonteCarloHistName="pileup", DataHistName="pileup", vertexlabel=zbblabel.vertexlabel, pulabel=zbblabel.pulabel)

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
      if i%5000==1 :
        print "Processing... event", i, ". Last batch in ", (time.time()-t0),"s."
        t0 = time.time()
      categoryData = category(event,_muChan,ZjetFilter="bcl",checkTrigger=checkTrigger[channel],btagAlgo="SSV")
      escp.setCategories(map(lambda c:isInCategory(c, categoryData),range(eventCategories())))

      escp.processEvent(event)
      brcp.processEvent(event)
      lrcp.processEvent(event)
      jmcp.processEvent(event)
      vacp.processEvent(event)
      if channel[-2:] == "MC":
        mscp.processEvent(event)
        prcp.processEvent(event)
      
      ras_escp=escp._obsSet
      ras_lrcp=lrcp._obsSet
      ras_brcp=brcp._obsSet
      ras_jmcp=jmcp._obsSet
      ras_vacp=vacp._obsSet
      if channel[-2:] == "MC":
        ras_mscp=mscp._obsSet
        ras_prcp=prcp._obsSet

      ras_escp.add(ras_lrcp)
      ras_escp.add(ras_brcp)
      ras_escp.add(ras_jmcp)
      ras_escp.add(ras_vacp)
      if channel[-2:] == "MC":
        ras_escp.add(ras_mscp)
        ras_escp.add(ras_prcp)

      #rds_zbb.add(ntuple)
      rds_zbb.add(ras_escp)
      i += 1

    escp.endJob()
    brcp.endJob()
    lrcp.endJob()
    jmcp.endJob()
    vacp.endJob()
    if channel[-2:] == "MC":
      mscp.endJob()
      prcp.endJob()

    ws = RooWorkspace("ws","workspace")
    getattr(ws,'import')(rds_zbb)
    ws.Print()

    ws.writeToFile("File_rds_zbb_"+channel+".root") 
    gDirectory.Add(ws)

    f=TFile("test.root","RECREATE")
    rds_zbb.Write("test.root")
    rds_zbb_tree = rds_zbb.tree()
    rds_zbb_tree.Write("test.root")
    f.Close()

