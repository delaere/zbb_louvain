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

FarmDirectory = "FARM_RDSmaker_V4"

from globalLists import listToProcessEMu
processesToRun = listToProcessEMu

print "I will run over ", len(processesToRun), "processes"

JobName = "File_rds"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1

for x in processesToRun[:]:

  command = "./makeRDS_usingFramework.py" + " " + x

  print "command  = ", command
 
  LaunchOnCondor.SendCluster_Push(["PYTHON", command])

LaunchOnCondor.SendCluster_Submit()


