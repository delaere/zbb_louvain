#!/usr/bin/env python
#Usage: python Launch_allCP ConfigFile
#example: python Launch_allCP zbbConfig

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob

theConfig = "UserCode.zbb_louvain."+sys.argv[1]
if theConfig is not None:
  configImplementation = __import__(theConfig)
  atts=theConfig.split(".")[1:]
  for att in atts : configImplementation = getattr(configImplementation,att)
  configuration = configImplementation.configuration


mode = configuration.runningMode

dir_plot = {
  "abdollah": "/home/fynu/acaudron/scratch/",
  "acaudron": "/home/fynu/acaudron/scratch/",
  "bfrancois": "/home/fynu/bfrancois/storage/ControlPlots/",
  "cbeluffi": "/home/fynu/cbeluffi/storage/ControlPlots/",
  "vizangarciaj": "/home/fynu/vizangarciaj/storage/CP/testJune2014/",
}

dir_rds = {
  "abdollah": "/home/fynu/acaudron/scratch/",
  "acaudron": "/home/fynu/acaudron/scratch/",
  "bfrancois": "/home/fynu/bfrancois/storage/RDS/",
  "cbeluffi": "/home/fynu/cbeluffi/storage/ControlPlots/",
  "vizangarciaj": "/home/fynu/vizangarciaj/storage/RDS/testJune2014/",
}



samples = [
#    "DATA",
"DY",
"TT",
"ZZ",
"ZH",
    ]

DYsamples = [
    "DYjets",
#"DY1jets",
#"DY2jets",
#"DY3jets",
#"DY4jets",
#"DYjets_Pt50to70",
#"DYjets_Pt70to100",
#"DYjets_Pt100",
#"DYjets_Pt180",
#"Zbb",
"DYjets_M10to50",
    ]

DYbcl = [
    #"Zb",
    #"Zc",
    #"Zl",
    "Zbb",
    "Zbx",
    "Zxx",
    ]

TTsamples = [
    #"TTjets",
    "TTFullLept",
    "TTSemiLept",
    #"TTHadronic"
    ]

mass = [125] #[110,115,120,125,130,135]

MC = "Summer12"
DATA = "2012"
cpVersion = "CSV_EMU_afterSF_MC"
README = "Corrected SF recipe for inclusive search \n"

listdata=[
        "A",
        "B",
        "C",
        "D",
        ]

DataChannel = [
    "Ele",
    "Mu",
    ]

DataSample = [
    #"Single",
    #"Double",
    "MuEG",
    ]

jobs = {
    "A" : 50,
    "B" : 250,
    "C" : 300,
    "D" : 400,  
    "TTjets" : 150,
    "TTFullLept" : 400,
    "TTSemiLept" : 200,
    "TTHadronic" : 100,
    "ZZ" : 50,
    "ZH" : 50,
    "DYjets" : 400,
    "DY1jets" : 300,
    "DY2jets" : 200,
    "DY3jets" : 150,
    "DY4jets" : 100,
    "DYjets_Pt50to70" : 250,
    "DYjets_Pt70to100" : 250,
    "DYjets_Pt100" : 50,
    "DYjets_Pt180" : 50,
    "Zbb" : 400,
    "DYjets_M10to50" : 100,
    }

if mode == "plots":
  dir = dir_plot[os.environ["USER"]]
  string_mode='ControlPlots_'
elif mode == "dataset":
  dir = dir_rds[os.environ["USER"]]
  string_mode='RDS_'

os.system('mkdir '+dir+string_mode+cpVersion)
f = open(dir+string_mode+cpVersion+'/README.txt', 'w')
f.write(README)
f.close()
for sample in samples :
    if sample=="ZH":
        for m in mass:
            os.system('mkdir '+dir+string_mode+cpVersion+'/'+string_mode+sample+str(m))
            LaunchOnCondor.Jobs_FinalCmds.append('mv ZH'+str(m)+'_'+MC+'_*.root '+dir+string_mode+cpVersion+'/'+string_mode+sample+str(m)+'/ \n')
    elif sample=="DY":
        for dy in DYsamples :
            #for fl in DYbcl :
                #os.system('mkdir '+dir+string_mode+cpVersion+'/'+string_mode+dy+'_'+fl)
                #LaunchOnCondor.Jobs_FinalCmds.append('mv '+dy+'_'+fl+'_'+MC+'_*.root '+dir+string_mode+cpVersion+'/'+string_mode+dy+'_'+fl+'/ \n')
            os.system('mkdir '+dir+string_mode+cpVersion+'/'+string_mode+dy)
            LaunchOnCondor.Jobs_FinalCmds.append('mv '+dy+'_'+MC+'_*.root '+dir+string_mode+cpVersion+'/'+string_mode+dy+'/ \n')
    elif sample=="TT":
        for tt in TTsamples :
            os.system('mkdir '+dir+string_mode+cpVersion+'/'+string_mode+tt)
            LaunchOnCondor.Jobs_FinalCmds.append('mv '+tt+'_'+MC+'_*.root '+dir+string_mode+cpVersion+'/'+string_mode+tt+'/ \n')
    elif sample=="DATA":
          for samp in DataSample :
	    if samp == "MuEG" :
              for period in listdata :
                  os.system('mkdir '+dir+string_mode+cpVersion+'/'+string_mode+samp+DATA+period)
                  LaunchOnCondor.Jobs_FinalCmds.append('mv '+samp+DATA+period+'_*.root '+dir+string_mode+cpVersion+'/'+string_mode+samp+DATA+period+'/ \n')
	    else:
	      for ch in DataChannel :	      
                for period in listdata :
                    os.system('mkdir '+dir+string_mode+cpVersion+'/'+string_mode+samp+ch+DATA+period)
                    LaunchOnCondor.Jobs_FinalCmds.append('mv '+samp+ch+DATA+period+'_*.root '+dir+string_mode+cpVersion+'/'+string_mode+samp+ch+DATA+period+'/ \n')
    else :
        os.system('mkdir '+dir+string_mode+cpVersion+'/'+string_mode+sample)
        LaunchOnCondor.Jobs_FinalCmds.append('mv '+sample+'_*.root '+dir+string_mode+cpVersion+'/'+string_mode+sample+'/ \n')
        
FarmDirectory = dir+"FARM_"+string_mode+cpVersion
JobName = "CoPl_list_"+cpVersion

LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)

if "TT" in samples :
    for tt in TTsamples :
        njobs = jobs[tt]
        for i in range(0,njobs):
            LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/../PatAnalysis/ControlPlots.py -c " + theConfig + " -i /nfs/user/llbb/Pat_8TeV_ReReco/Summer12_"+tt+"/ -o "+tt+"_"+MC+"_"+str(i)+".root --all --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "ZZ" in samples :
    njobs = jobs["ZZ"]
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/../PatAnalysis/ControlPlots.py -c " + theConfig + " -i /nfs/user/llbb/Pat_8TeV_ReReco/Summer12_ZZ/ -o ZZ_"+MC+"_"+str(i)+".root --all --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "DATA" in samples :
	if samp=="MuEG" :
          for period in listdata :
              njobs = jobs[period]
              for i in range(0,njobs):
                  print "/nfs/user/llbb/Pat_8TeV_ReReco/"+samp+DATA+period
                  LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/../PatAnalysis/ControlPlots.py -c " + theConfig + "_data -i /nfs/user/llbb/Pat_8TeV_ReReco/"+samp+DATA+period+"/ -o "+samp+DATA+period+"_"+str(i)+".root --all --Njobs "+str(njobs)+" --jobNumber "+str(i)])
                  #LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/../PatAnalysis/ControlPlots.py -c " + theConfig + "_data -i /nfs/user/llbb/Pat_8TeV_ReReco/"+samp+ch+DATA+period+"/ -o "+samp+ch+DATA+period+"_"+str(i)+".root --all --Njobs "+str(njobs)+" --jobNumber "+str(i)])
	else:
	  for ch in DataChannel :
            for period in listdata :
                njobs = jobs[period]
                for i in range(0,njobs):
                    print "/nfs/user/llbb/Pat_8TeV_ReReco/"+samp+ch+DATA+period
                    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/../PatAnalysis/ControlPlots.py -c " + theConfig + "_data -i /nfs/user/llbb/Pat_8TeV_ReReco/"+samp+ch+DATA+period+"/ -o "+samp+ch+DATA+period+"_"+str(i)+".root --all --Njobs "+str(njobs)+" --jobNumber "+str(i)])
                    #LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/../PatAnalysis/ControlPlots.py -c " + theConfig + "_data -i /nfs/user/llbb/Pat_8TeV_ReReco/"+samp+ch+DATA+period+"/ -o "+samp+ch+DATA+period+"_"+str(i)+".root --all --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "DY" in samples :
    for dy in DYsamples :
        njobs = jobs[dy]        
        #for fl in DYbcl :
            #for i in range(0,njobs):
                #LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/../PatAnalysis/ControlPlots.py -c " + theConfig + " -i /nfs/user/llbb/Pat_8TeV_ReReco/Summer12_"+dy+"/ -o "+dy+"_"+fl+"_"+MC+"_"+str(i)+".root --all -j "+fl+"  --Njobs "+str(njobs)+" --jobNumber "+str(i)])
        for i in range(0,njobs):
            LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/../PatAnalysis/ControlPlots.py -c " + theConfig + " -i /nfs/user/llbb/Pat_8TeV_ReReco/Summer12_"+dy+"/ -o "+dy+"_"+MC+"_"+str(i)+".root --all --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "ZH" in samples :
    mass = [125]#[115,120,125,130,135]
    for m in mass:
        njobs = jobs["ZH"]
        for i in range(0,njobs):
            LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/../PatAnalysis/ControlPlots.py -c " + theConfig + " -i /nfs/user/llbb/Pat_8TeV_ReReco/Summer12_ZH"+str(m)+"/ -o ZH"+str(m)+"_"+MC+"_"+str(i)+".root --all --Njobs "+str(njobs)+" --jobNumber "+str(i)])

LaunchOnCondor.SendCluster_Submit()
