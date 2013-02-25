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
from matrixElementControlPlots import *

from ROOT import *
from itertools import combinations
from baseControlPlots import getArgSet
from zbbCommons import zbbfile, isZbbSelection, zbbme
from eventSelection import eventCategories, eventCategory, isInCategory
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

btagAlgo="SSV"
if not isZbbSelection : btagAlgo="CSV"


############
### Maps ###
############

muChannel = { "MuA_DATA"     : True ,
              "ElA_DATA"     : False,
              "MuB_DATA"     : True ,
              "ElB_DATA"     : False,
              "Mu_MC"        : True ,
              "El_MC"        : False,
              "DY_Pt100_Mu_MC"        : True ,
              "DY_Pt100_El_MC"        : False,
              "Zbb_Mu_MC"    : True ,
              "Zbb_El_MC"    : False,
              "TT_Mu_MC"     : True ,
              "TT_El_MC"     : False,
              "ZZ_Mu_MC"     : True ,
              "ZZ_El_MC"     : False,
              "ZH110_Mu_MC"  : True ,
              "ZH110_El_MC"  : False,
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
              "tW_Mu_MC"     : True ,
              "tW_El_MC"     : False,
              "tbarW_Mu_MC"  : True ,
              "tbarW_El_MC"  : False,
              "evtgen_MC"    : False,
              "herwig_MC"    : False,
              "pythia_MC"    : False,
              "ZA_Mu_MC" : True,
              "ZA_El_MC" : False
              }

path = { 
  "MuA_DATA"     : "/nfs/user/acaudron/skim444/Mu_DataA/" ,
  "ElA_DATA"     : "/nfs/user/acaudron/skim444/El_DataA/" ,
  "MuB_DATA"     : "/nfs/user/acaudron/skim444/Mu_DataB/" ,
  "ElB_DATA"     : "/nfs/user/acaudron/skim444/El_DataB/" ,
  "Mu_MC"        : "/nfs/user/acaudron/skim444/DY_MC/"    ,
  "El_MC"        : "/nfs/user/acaudron/skim444/DY_MC/"    ,
  "DY_Pt100_Mu_MC"        : "/nfs/user/acaudron/skim444/DY_Pt100_MC/"    ,
  "DY_Pt100_El_MC"        : "/nfs/user/acaudron/skim444/DY_Pt100_MC/"    ,
  #"Mu_MC"        : "/storage/data/cms/store/user/acaudron/Torino/DYJets_MCMatched_00.root"    , 
  #"El_MC"        : "/storage/data/cms/store/user/acaudron/Torino/DYJets_MCMatched_00.root"    , 
  "Zbb_Mu_MC"    : "/storage/data/cms/store/user/acaudron/Fall11MC_444/zbbProd/"   ,
  "Zbb_El_MC"    : "/storage/data/cms/store/user/acaudron/Fall11MC_444/zbbProd/"   ,
  "TT_Mu_MC"     : "/nfs/user/acaudron/skim444/TT_MC/"    ,
  "TT_El_MC"     : "/nfs/user/acaudron/skim444/TT_MC/"    ,
  "ZZ_Mu_MC"     : "/nfs/user/acaudron/skim444/ZZ_MC/"    ,
  "ZZ_El_MC"     : "/nfs/user/acaudron/skim444/ZZ_MC/"    ,
  "ZH110_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH110_MC/" ,
  "ZH110_El_MC"  : "/nfs/user/acaudron/skim444/ZH110_MC/" ,
  "ZH115_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH115_MC/" ,
  "ZH115_El_MC"  : "/nfs/user/acaudron/skim444/ZH115_MC/" ,
  "ZH120_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH120_MC/" ,
  "ZH120_El_MC"  : "/nfs/user/acaudron/skim444/ZH120_MC/" ,
  "ZH125_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH125_MC/" ,
  "ZH125_El_MC"  : "/nfs/user/acaudron/skim444/ZH125_MC/" ,
  "ZH130_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH130_MC/" ,
  "ZH130_El_MC"  : "/nfs/user/acaudron/skim444/ZH130_MC/" ,
  "ZH135_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH135_MC/" ,
  "ZH135_El_MC"  : "/nfs/user/acaudron/skim444/ZH135_MC/" ,
  "tW_Mu_MC"     : "/nfs/user/acaudron/skim444/tW_MC/"    ,
  "tW_El_MC"     : "/nfs/user/acaudron/skim444/tW_MC/"    ,
  "tbarW_Mu_MC"  : "/nfs/user/acaudron/skim444/tbarW_MC/" ,
  "tbarW_El_MC"  : "/nfs/user/acaudron/skim444/tbarW_MC/" ,
  "evtgen_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/evtgen/",
  "herwig_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/herwig/",
  "pythia_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/pythia/",
  "ZA_Mu_MC" : "/nfs/user/acaudron/ZApat/",
  "ZA_El_MC" : "/nfs/user/acaudron/ZApat/"
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
  return eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, vertices, jets, met, runNumber, muChannel, btagAlgo, event.eventAuxiliary().luminosityBlock())

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
  "DY_Pt100_Mu_MC"        : False,
  "DY_Pt100_El_MC"        : False,
  "Zbb_Mu_MC"    : False,
  "Zbb_El_MC"    : False,
  "TT_Mu_MC"     : False,
  "TT_El_MC"     : False,
  "ZZ_Mu_MC"     : False,
  "ZZ_El_MC"     : False,
  "ZH110_Mu_MC"  : False,
  "ZH110_El_MC"  : False,
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
  "tW_Mu_MC"     : False,
  "tW_El_MC"     : False,
  "tbarW_Mu_MC"  : False,
  "tbarW_El_MC"  : False,
  "evtgen_MC"    : False,
  "herwig_MC"    : False,
  "pythia_MC"    : False,
  "ZA_Mu_MC" : False,
  "ZA_El_MC" : False
  }

obsSet  = RooArgSet()
rds_zbb = RooDataSet("rds_zbb",  "rds_zbb", obsSet)
escp    = EventSelectionControlPlots(dir=None, muChannel=muChannel[channel], checkTrigger=checkTrigger[channel], dataset=rds_zbb, mode="dataset")
brcp    = BtaggingReWeightingControlPlots(dir=None, muChannel=muChannel[channel], dataset=rds_zbb, mode="dataset")
lrcp    = LeptonsReweightingControlPlots(dir=None, muChannel=muChannel[channel], dataset=rds_zbb, mode="dataset")
jmcp    = JetmetControlPlots(dir=None, dataset=rds_zbb, mode="dataset")
vacp    = VertexAssociationControlPlots(dir=None, dataset=rds_zbb, mode="dataset")

if zbbme.doMEcontrolPlots:
  mecp  = MatrixElementControlPlots(dir=None, muChannel=muChannel[channel], checkTrigger=checkTrigger[channel], dataset=rds_zbb, mode="dataset")
  
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

escp.beginJob(btagging=btagAlgo, zmulabel=zbblabel.zmumulabel, zelelabel=zbblabel.zelelabel)
brcp.beginJob(btagPerfData, btagging=btagAlgo) 
lrcp.beginJob()             
jmcp.beginJob(btagging=btagAlgo) 

if zbbme.doMEcontrolPlots:
  mecp.beginJob(btagging=btagAlgo)
  
if muChannel[channel] : vacp.beginJob(zlabel=zbblabel.zmumulabel)
else : vacp.beginJob(zlabel=zbblabel.zelelabel)
if channel[-2:] == "MC":
  mscp.beginJob(genlabel=zbblabel.genlabel)
  prcp.beginJob(MonteCarloPUFileName, DataPUFileName, vertexlabel=zbblabel.vertexlabel, pulabel=zbblabel.pulabel)

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
      #if i > 400: break;
      if i%1000==1 :
        print "Processing... event", i, ". Last batch in ", (time.time()-t0),"s."
        t0 = time.time()
      categoryData = category(event,_muChan,ZjetFilter="bcl",checkTrigger=checkTrigger[channel],btagAlgo=btagAlgo)
      escp.setCategories(map(lambda c:isInCategory(c, categoryData),range(eventCategories())))

      escp.processEvent(event)
      brcp.processEvent(event)
      lrcp.processEvent(event)
      jmcp.processEvent(event)
      vacp.processEvent(event) 
      if zbbme.doMEcontrolPlots:
        mecp.processEvent(event)
      if channel[-2:] == "MC":
        mscp.processEvent(event)
        prcp.processEvent(event)
      
      ras_escp=escp._obsSet
      ras_lrcp=lrcp._obsSet
      ras_brcp=brcp._obsSet
      ras_jmcp=jmcp._obsSet
      ras_vacp=vacp._obsSet
      if zbbme.doMEcontrolPlots:
        ras_mecp=mecp._obsSet
      if channel[-2:] == "MC":
        ras_mscp=mscp._obsSet
        ras_prcp=prcp._obsSet

      ras_escp.add(ras_lrcp)
      ras_escp.add(ras_brcp)
      ras_escp.add(ras_jmcp)
      ras_escp.add(ras_vacp)
      if zbbme.doMEcontrolPlots:
        ras_escp.add(ras_mecp)
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
    if zbbme.doMEcontrolPlots:
      mecp.endJob()
    if channel[-2:] == "MC":
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
