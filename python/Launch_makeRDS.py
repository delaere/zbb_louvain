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

FarmDirectory = "condorRDSmaker"

processesToRun = ["MuA_DATA"   ,
                  "ElA_DATA"   ,
                  "MuB_DATA"   ,
                  "ElB_DATA"   ,
                  "Mu_MC"      ,
                  "El_MC"      ,
                  "DY_Pt100_Mu_MC"      ,
                  "DY_Pt100_El_MC"      ,
                  "Zbb_Mu_MC"  ,
                  "Zbb_El_MC"  ,
                  "TT_Mu_MC"   ,
                  "TT_El_MC"   ,
                  "TT_1of10_Mu_MC"	,
                  "TT_1of10_El_MC"	,
                  "TT_2of10_Mu_MC"	,
                  "TT_2of10_El_MC"	,
                  "TT_3of10_Mu_MC"	,
                  "TT_3of10_El_MC"	,
                  "TT_4of10_Mu_MC"	,
                  "TT_4of10_El_MC"	,
                  "TT_5of10_Mu_MC"	,
                  "TT_5of10_El_MC"	,
                  "TT_6of10_Mu_MC"	,
                  "TT_6of10_El_MC"	,
                  "TT_7of10_Mu_MC"	,
                  "TT_7of10_El_MC"	,
                  "TT_8of10_Mu_MC"	,
                  "TT_8of10_El_MC"	,
                  "TT_9of10_Mu_MC"	,
                  "TT_9of10_El_MC"	,
                  "TT_10of10_Mu_MC"	,
                  "TT_10of10_El_MC"	,
                  "ZZ_Mu_MC"   ,
                  "ZZ_El_MC"   ,
                  "ZH110_Mu_MC",
                  "ZH110_El_MC",
                  "ZH115_Mu_MC",
                  "ZH115_El_MC",
                  "ZH120_Mu_MC",
                  "ZH120_El_MC",
                  "ZH125_Mu_MC",
                  "ZH125_El_MC",
                  "ZH130_Mu_MC",
                  "ZH130_El_MC",
                  "ZH135_Mu_MC",
                  "ZH135_El_MC",
                  "tW_Mu_MC"   ,
                  "tW_El_MC"   ,
                  "tbarW_Mu_MC",
                  "tbarW_El_MC"
                  ]


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


