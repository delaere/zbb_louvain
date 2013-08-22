#!/usr/bin/env python

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob
### nombre total de jobs :
njobs = 70

FarmDirectory = "FARM_NoWeight_ResponseMatrix"
JobName = "Unfolding_Zbb"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1

for i in range(0,njobs):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/Matrix_RooUnfold.py -i /storage/data/cms/store/user/castello/Unfolding2012/DYJets_unfolding_noRecoBias/ -o Matrix_Unfolding/Matrix_Unfolding_NoWeight_Tot_"+str(i)+".root --Njobs "+str(njobs)+" --jobNumber "+str(i)])

LaunchOnCondor.SendCluster_Submit()
