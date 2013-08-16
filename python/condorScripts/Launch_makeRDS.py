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
from zbbSamples import getSamples, samples_PAT

FarmDirectory = "FARM_RDSmaker_TEST"
print "I will run over ", len(processesToRun), "processes"

JobName = "File_rds"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1

for sample in getSamples(processList=samples_PAT,typeList=["PAT"]):

  print "for proc. = ", key[0], "nevents to process : ", sample.nevents

  n=250000
  if sample.nevents>n :
    print "jobs will be splited as the number of events to process exceed "+str(n)
    for i in range(0,((sample.nevents/n)+1)) :
      command = "./makeRDS_usingFramework.py" + " " + sample.path + " " + str(i+1)
      print "command  = ", command
      print "jobs will run from event", i*n, "to event",(i+1)*n 
      LaunchOnCondor.SendCluster_Push(["PYTHON", command])
  else :
    command = "./makeRDS_usingFramework.py" + " " + sample.path
    print "command  = ", command
    LaunchOnCondor.SendCluster_Push(["PYTHON", command])

LaunchOnCondor.SendCluster_Submit()

