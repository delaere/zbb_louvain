#!/usr/bin/env python

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob
import os

samples = [
    #"DATA",
    "DY",
    #"TT",
    #"ZZ",
    #"ZH",
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
    "Zbb",
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
    "TTjets",
    "TTbarFullLept",
    "TTbarSemiLept",
    #"TTbarHadronic"
    ]

mass = [125] #[110,115,120,125,130,135]

MC = "Summer12"
DATA = "2012"
cpVersion = "V13"
README = "corect bug for DY\n"

listdata=[
        "A",
        "A06aug",
        "B",
        "C-v1",
        "C-v2",
        "D",
        ]

DataChannel = [
    "Ele",
    #"Mu",
    ]

DataSample = [
    #"Single",
    "Double",
    ]

jobs = {
    "A" : 50,
    "A06aug" : 10,
    "B" : 250,
    "C-v1" : 25,
    "C-v2" : 300,
    "D" : 400,  
    "TTjets" : 150,
    "TTbarFullLept" : 400,
    "TTbarSemiLept" : 200,
    "TTbarHadronic" : 100,
    "ZZ" : 50,
    "ZH" : 50,
    "DYjets" : 400,
    "DY1jets" : 300,
    "DY2jets" : 200,
    "DY3jets" : 150,
    "DY4jets" : 100,
    "DYjets_Pt50to70" : 250,
    "DYjets_Pt70to100" : 250,
    "DYjets_Pt180" : 50,
    "Zbb" : 400,
    }

dir = "/nfs/user/acaudron/ControlPlots/cp537/"

os.system('mkdir '+dir+'ControlPlots_'+cpVersion)
f = open(dir+'ControlPlots_'+cpVersion+'/README.txt', 'w')
f.write(README)
f.close()
for sample in samples :
    if sample=="ZH":
        for m in mass:
            os.system('mkdir '+dir+'ControlPlots_'+cpVersion+'/ControlPlots_'+sample+str(m))
    elif sample=="DY":
        for dy in DYsamples :
            for fl in DYbcl :
                os.system('mkdir '+dir+'ControlPlots_'+cpVersion+'/ControlPlots_'+dy+'_'+fl)
    elif sample=="TT":
        for tt in TTsamples :
            os.system('mkdir '+dir+'ControlPlots_'+cpVersion+'/ControlPlots_'+tt)
    elif sample=="DATA":
        for ch in DataChannel :
            for samp in DataSample :
                for period in listdata :
                    os.system('mkdir '+dir+'ControlPlots_'+cpVersion+'/ControlPlots_'+samp+ch+DATA+period)
    else: os.system('mkdir '+dir+'ControlPlots_'+cpVersion+'/ControlPlots_'+sample)

FarmDirectory = dir+"FARM_CP_"+cpVersion
JobName = "CoPl_list_"+cpVersion
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1

if "TT" in samples :
    for tt in TTsamples :
        njobs = jobs[tt]
        for i in range(0,njobs):
            LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /nfs/user/llbb/Pat_8TeV_537/Summer12_"+tt+"_S10/ -o "+dir+"ControlPlots_"+cpVersion+"/ControlPlots_"+tt+"/"+tt+"_"+MC+"_"+str(i)+".root --all -p ../data/Cert_190456-208686_8TeV_PromptPlusReReco_pileupTruth.root -P ../data/MCpileup_Summer12_S10.root -w ../data/performance_csv_witheff.root  --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "ZZ" in samples :
    njobs = jobs["ZZ"]
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /nfs/user/llbb/Pat_8TeV_537/Summer12_ZZ_S10/ -o "+dir+"ControlPlots_"+cpVersion+"/ControlPlots_ZZ/ZZ_"+MC+"_"+str(i)+".root --all -p ../data/Cert_190456-208686_8TeV_PromptPlusReReco_pileupTruth.root -P ../data/MCpileup_Summer12_S10.root -w ../data/performance_csv_witheff.root  --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "DATA" in samples :
    for ch in DataChannel :
        for samp in DataSample :
            for period in listdata :
                njobs = jobs[period]
                for i in range(0,njobs):
                    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /nfs/user/llbb/Pat_8TeV_537/"+samp+ch+DATA+period+"/ -o "+dir+"ControlPlots_"+cpVersion+"/ControlPlots_"+samp+ch+DATA+period+"/"+samp+ch+DATA+period+"_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --only"+ch+" --Njobs "+str(njobs)+" --jobNumber "+str(i)])
                    #LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /nfs/user/llbb/Pat_8TeV_537/"+samp+ch+DATA+period+"/ -o "+dir+"ControlPlots_"+cpVersion+"/ControlPlots_"+samp+ch+DATA+period+"/"+samp+ch+DATA+period+"_"+str(i)+".root --all --noPUweight --noBweight --noLweight --only"+ch+" --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "DY" in samples :
    for dy in DYsamples :
        njobs = jobs[dy]        
        for fl in DYbcl :
            for i in range(0,njobs):
                LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /nfs/user/llbb/Pat_8TeV_537/Summer12_"+dy+"_S10/ -o "+dir+"ControlPlots_"+cpVersion+"/ControlPlots_"+dy+"_"+fl+"/"+dy+"_"+fl+"_"+MC+"_"+str(i)+".root --all -j "+fl+" -p ../data/Cert_190456-208686_8TeV_PromptPlusReReco_pileupTruth.root -P ../data/MCpileup_Summer12_S10.root -w ../data/performance_csv_witheff.root  --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "ZH" in samples :
    mass = [125]#[115,120,125,130,135]
    for m in mass:
        njobs = jobs["ZH"]
        for i in range(0,njobs):
            LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /nfs/user/llbb/Pat_8TeV_537/Summer12_ZH"+str(m)+"_S10/ -o "+dir+"ControlPlots_"+cpVersion+"/ControlPlots_ZH"+str(m)+"/ZH"+str(m)+"_"+MC+"_"+str(i)+".root --all -p ../data/Cert_190456-208686_8TeV_PromptPlusReReco_pileupTruth.root -P ../data/MCpileup_Summer12_S10.root -w ../data/performance_csv_witheff.root  --Njobs "+str(njobs)+" --jobNumber "+str(i)])

LaunchOnCondor.SendCluster_Submit()
