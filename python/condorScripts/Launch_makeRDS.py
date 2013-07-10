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

FarmDirectory = "FARM_RDSmaker_TEST"

lib_path = os.path.abspath('../analysisScripts/')
sys.path.append(lib_path)
from globalLists import listToProcessEMu, pathSkimEMu
processesToRun = listToProcessEMu
path = pathSkimEMu

print "I will run over ", len(processesToRun), "processes"

lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from AnalysisEvent import AnalysisEvent
import glob

JobName = "File_rds"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1

for x in processesToRun[:]:

  files=glob.glob(path[x]+"*") 
  events = AnalysisEvent (files)
  print "for proc. = ", x, "nevents to process : ", events.size()

  n=250000
  if events.size()>n :
    print "jobs will be splited as the number of events to process exceed "+str(n)
    for i in range(0,((events.size()/n)+1)) :
      command = "./makeRDS_usingFramework.py" + " " + x + " " + str(i+1)
      print "command  = ", command
      print "jobs will run from event", i*n, "to event",(i+1)*n 
      LaunchOnCondor.SendCluster_Push(["PYTHON", command])
  else :
    command = "./makeRDS_usingFramework.py" + " " + x
    print "command  = ", command
    LaunchOnCondor.SendCluster_Push(["PYTHON", command])

LaunchOnCondor.SendCluster_Submit()


