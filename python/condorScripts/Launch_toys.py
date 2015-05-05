#!/usr/bin/env python
#run as 'python Launch_pat.py TT' to run over TT sample, number of jobs to be changed below
import urllib
import string
import os
import sys
import LaunchOnCondor
import glob

#script = "llbbDC"
script = "combineElMuCards"

#LaunchOnCondor
#FarmDirectory = "FARM_"+sample+"_"+str(start)+"to"+str(start+njobs-1)
FarmDirectory = "FARM_"+script+"toys"
JobName = script+"toys"
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)

for i in range(0,1000):
    command = "cd /nfs/user/acaudron/final53Xreleases/CMSSW_5_3_14_patch1/src/UserCode/zbb_louvain/python/pyrootScripts/; python "+script+".py "+str(i)  
    LaunchOnCondor.SendCluster_Push(["BASH", command])
LaunchOnCondor.SendCluster_Submit()

