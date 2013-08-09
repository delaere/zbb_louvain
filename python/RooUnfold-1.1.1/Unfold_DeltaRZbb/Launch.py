#!/usr/bin/env python

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob
### nombre total de jobs :
njobs = 300

FarmDirectory = "FARM_ResponseMatrix_DrZbb_bin"
JobName = "Unfolding_Zbb"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1

for i in range(0,njobs):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/Unfold_DeltaRZbb/Matrix_RooUnfold.py -i /storage/data/cms/store/user/castello/Unfolding2012/DYJets_unfolding_noRecoBias/ -o Matrix_Unfolding_bin/Matrix_Unfolding_Tot_"+str(i)+".root --Njobs "+str(njobs)+" --jobNumber "+str(i)])

LaunchOnCondor.SendCluster_Submit()
