#!/usr/bin/env python

### to be run as
#python Launch.py --which=TT_MC
#python Launch.py --which=DY_MC
#python Launch.py --which=El_Data
#python Launch.py --which=Mu_Data
###

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob

from globalLists import listToProcess, dirSkim
samples = listToProcess

FarmDirectory = "FARM_skim_V5"
JobName = "Skim_pats"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1

j=0
for s in samples :
    whichSample = s 
    os.system('mkdir '+dirSkim+whichSample)
            
    for i in range(1,11):
        command = "../test/skimDY_423_cfg.py"  
        option  = " sample="+whichSample+" slice="+str(i)  
        print "command = ", command
        print "option  = ", option
        LaunchOnCondor.SendCluster_Push(["CMSSW", command, option ])
LaunchOnCondor.SendCluster_Submit()

