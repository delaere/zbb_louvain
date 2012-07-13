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

FarmDirectory = "FARM"

processesToRun = ["Mu_DATA", "El_DATA", "Mu_MC", "El_MC", "Ttbar_Mu_MC", "Ttbar_El_MC", "ZZ_Mu_MC", "ZZ_El_MC", "ZHbb_Mu_MC", "ZHbb_El_MC"]


print "I will run over ", len(processesToRun), "processes"


JobName = "File_rds"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1



for x in processesToRun[:]:

  #
  #option  = " " + x

  command = "./makeRDS_usingFramework.py" + " " + x

  print "command  = ", command
 
  #When using SendCluster_Push using PYTHON as a first argument, only command is taking into account (the argument option is trashed)
  #LaunchOnCondor.SendCluster_Push(["PYTHON", command, option ])
  LaunchOnCondor.SendCluster_Push(["PYTHON", command])

LaunchOnCondor.SendCluster_Submit()


