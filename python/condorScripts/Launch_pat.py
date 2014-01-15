#!/usr/bin/env python
#run as 'python Launch_pat.py TT' to run over TT sample, number of jobs to be changed below
import urllib
import string
import os
import sys
import LaunchOnCondor
import glob

njobs=100

sample="DY"
if len(sys.argv)>1:
    sample=sys.argv[1]

FarmDirectory = "FARM_"+sample+"_V2"
JobName = sample+"pat"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1
for i in range(1,njobs+1):
    command = "../../test/patTuple_llbbX_cfg_dataMC.py"  
    option  = " option=Condor slice="+str(i)+" sample="+sample  
    print "command = ", command
    print "option  = ", option
    LaunchOnCondor.SendCluster_Push(["CMSSW", command, option ])
LaunchOnCondor.SendCluster_Submit()

