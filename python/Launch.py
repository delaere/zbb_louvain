#!/usr/bin/env python

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob

FarmDirectory = "FARM"
JobName = "ZmumubbAnalysis_MC_TTJets_Spring11"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1
for i in range(0,50):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /home/fynu/lceard/store/MC_Spring11/TTJets/ -o Control_Plots/MC_Spring11/TTJets_Spring11_Condor/TTJets_Spring11_"+str(i)+".root --all --noPU --Njobs 50 --jobNumber "+str(i)])
LaunchOnCondor.SendCluster_Submit()

