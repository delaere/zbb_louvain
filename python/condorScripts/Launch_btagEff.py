#!/usr/bin/env python

### to be run as
#python Launch_makeRDS.py
#it runs 1 job per each process specified in the variable processesToRun

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob
from optparse import OptionParser
#from zbbSamples import getSamples, samples_PAT

FarmDirectory = "FARM_btagEff"

lib_path = os.path.abspath('../')
sys.path.append(lib_path)

JobName = "btageff"
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)

#for sample in getSamples(processList=samples_PAT,typeList=["PAT"]):
for sample in ["/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_DYjets/","/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_DYjets_HT200to400/","/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_DYjets_HT400/","/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_DYjets_Pt100/","/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_DYjets_Pt180/","/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_DYjets_Pt50to70/","/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_DYjets_Pt50to70_ext/","/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_DYjets_Pt70to100/","/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_DY3jets/","/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_DY4jets/","/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_ZH125/","/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_TTFullLept/"]:

  command = "/home/fynu/acaudron/scratch/final53Xreleases/CMSSW_5_3_14_patch1/src/UserCode/zbb_louvain/python/analysisScripts/btagEfficiencyStudy.py "+sample.split("/")[-2]+".root "+sample
  print "command  = ", command
  LaunchOnCondor.SendCluster_Push(["PYTHON", command])

LaunchOnCondor.SendCluster_Submit()

