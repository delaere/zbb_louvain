#!/usr/bin/env python
#run as 'python Launch_pat.py TT' to run over TT sample, number of jobs to be changed below
import urllib
import string
import os
import sys
import LaunchOnCondor
import glob

#first to last jobs
start = 1
njobs = 250

#sample name
sample="ZA_875_761"
if len(sys.argv)>1:
    sample=sys.argv[1]

#output directory
OUTDIR = '/nfs/user/'+str(os.environ["USER"])+'/'+sample+'_PAT2014'
os.system('if [[ -d '+OUTDIR+' ]]; then echo "Directory '+OUTDIR+' exists";  else mkdir '+OUTDIR+'; fi;')

#LaunchOnCondor
#FarmDirectory = "FARM_"+sample+"_"+str(start)+"to"+str(start+njobs-1)
FarmDirectory = "FARM_"+sample
JobName = sample+"pat"
LaunchOnCondor.Jobs_FinalCmds = ['mv pat53_*.root '+OUTDIR+'/ \n']
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)

for i in range(start,start+njobs):
    command = "../../test/patTuple_llbbX_cfg_dataMC.py"  
    option  = " option=Condor slice="+str(i)+" sample="+sample  
    print "command = ", command
    print "option  = ", option
    LaunchOnCondor.SendCluster_Push(["CMSSW", command, option ])
LaunchOnCondor.SendCluster_Submit()

