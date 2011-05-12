#!/usr/bin/env python

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob

FarmDirectory = "FARM"
JobName = "ZmumubbAnalysis"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
for i in range(0,161):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"../ControlPlots_withSubJobs.py -i /home/fynu/lceard/store/Prod_AOD_2011A/Json_Golden_153pb/Mu_2011A_153pb/ -o Mu/Mu2011_153pb_"+str(i)+".root --all -n "+str(i)]) 
LaunchOnCondor.SendCluster_Submit()

