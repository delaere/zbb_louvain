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

samples = [
            "DY_MC",
            "TT_MC",
            "Mu_DataA",
            "El_DataA",
            "Mu_DataB",
            "El_DataB",
            "ZZ_MC",
            #"ZH115_MC",
            #"ZH120_MC",
            "ZH125_MC",
            #"ZH130_MC",
            #"ZH135_MC"
            ]

FarmDirectory = "FARM_skim"
JobName = "Skim_pats"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1

for s in samples :
    whichSample = s #options.which
    os.system('mkdir /nfs/user/acaudron/skim53X/'+whichSample)
            
    for i in range(1,11):
        command = "/nfs/user/acaudron/CMSSW_5_3_2_patch4/src/UserCode/zbb_louvain/test/skimDY_423_cfg.py"  
        option  = " sample="+whichSample+" slice="+str(i)  
        print "command = ", command
        print "option  = ", option
        LaunchOnCondor.SendCluster_Push(["CMSSW", command, option ])
LaunchOnCondor.SendCluster_Submit()

