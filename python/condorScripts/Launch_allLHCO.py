#!/usr/bin/env python

import os
import LaunchOnCondor

from globalLists import listToProcessEMu
version = "V2"

FarmDirectory = "FARM_CMSToLHCO_"+version

JobName = "LHCO_"+version
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1
  
for sample in listToProcessEMu:
  command = "./CMS_To_LHCO_usingFramework_batch.py "+sample+" "+version
  #print "command = ", command
  LaunchOnCondor.SendCluster_Push(["PYTHON", command])
    
LaunchOnCondor.SendCluster_Submit()
