#!/usr/bin/env python

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob
import os

samples = [
    "TT",
    "Zl",
    "Zc",
    "Zb",
    "ZZ",
    "ZH",
    "Ele",
    "Mu"
    ]

MC = "Summer12"
DATA = "2012"
cpVersion = "V14"

listdata=[
        "A",
        "B"
        ]

os.system('mkdir ControlPlots_'+cpVersion)
for sample in samples :
    if sample=="ZH":
        mass = [125] #[115,120,125,130,135]
        for m in mass:
            os.system('mkdir ControlPlots_'+cpVersion+'/ControlPlots_'+sample+str(m))
    elif sample=="Ele" or sample=="Mu":
        for l in listdata:
            os.system('mkdir ControlPlots_'+cpVersion+'/ControlPlots_'+sample+DATA+l)
    else: os.system('mkdir ControlPlots_'+cpVersion+'/ControlPlots_'+sample)

FarmDirectory = "FARM_CP_"+cpVersion
JobName = "ZbbAnalysis_All"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1
if "TT" in samples :
    njobs = 350
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /nfs/user/acaudron/TTjetsMassiveB_Summer12_S10/ -o ControlPlots_"+cpVersion+"/ControlPlots_TT/TT_"+MC+"_"+str(i)+".root --all -p ../data/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_pileupTruth.root -P ../data/MCpileup_Summer12_S10.root -w ../data/performance_csv_witheff.root  --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "Zl" in samples :
    njobs = 400
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/store/user/acaudron/Sept2012production8TeV/Summer12_DYjets_S10_V2/acaudron/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Sept2012production8TeV_Summer12_DYjets_S10_V2/d5186fd016990c766c736d42e5dce079/ -o ControlPlots_"+cpVersion+"/ControlPlots_Zl/Zl_"+MC+"_"+str(i)+".root --all -j l -p ../data/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_pileupTruth.root -P ../data/MCpileup_Summer12_S10.root -w ../data/performance_csv_witheff.root  --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "Zc" in samples :
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/store/user/acaudron/Sept2012production8TeV/Summer12_DYjets_S10_V2/acaudron/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Sept2012production8TeV_Summer12_DYjets_S10_V2/d5186fd016990c766c736d42e5dce079/ -o ControlPlots_"+cpVersion+"/ControlPlots_Zc/Zc_"+MC+"_"+str(i)+".root --all -j c -p ../data/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_pileupTruth.root -P ../data/MCpileup_Summer12_S10.root -w ../data/performance_csv_witheff.root  --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "Zb" in samples :
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/store/user/acaudron/Sept2012production8TeV/Summer12_DYjets_S10_V2/acaudron/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Sept2012production8TeV_Summer12_DYjets_S10_V2/d5186fd016990c766c736d42e5dce079/ -o ControlPlots_"+cpVersion+"/ControlPlots_Zb/Zb_"+MC+"_"+str(i)+".root --all -j b -p ../data/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_pileupTruth.root -P ../data/MCpileup_Summer12_S10.root -w ../data/performance_csv_witheff.root  --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "ZZ" in samples :
    njobs = 50
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/store/user/acaudron/Sept2012production8TeV/Summer12_ZZ_S10_V2/acaudron/ZZ_TuneZ2star_8TeV_pythia6_tauola/Sept2012production8TeV_Summer12_ZZ_S10_V2/d5186fd016990c766c736d42e5dce079/ -o ControlPlots_"+cpVersion+"/ControlPlots_ZZ/ZZ_"+MC+"_"+str(i)+".root --all -p ../data/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_pileupTruth.root -P ../data/MCpileup_Summer12_S10.root -w ../data/performance_csv_witheff.root  --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "Ele" in samples :
    njobs = 50
    if "A" in listdata :
        for i in range(0,njobs):
            LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/store/user/acaudron/Sept2012production8TeV/Ele2012A_V4/acaudron/DoubleElectron/Sept2012production8TeV_Ele2012A_V4/ee8b79c5bec180099e91bf02c7018cc0/ -o ControlPlots_"+cpVersion+"/ControlPlots_Ele"+DATA+"A/Ele"+DATA+"A_"+MC+"_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyEle --Njobs "+str(njobs)+" --jobNumber "+str(i)])

    njobs = 300
    if "B" in listdata :
        for i in range(0,njobs):
            LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/store/user/acaudron/Sept2012production8TeV/Ele2012B_V4/acaudron/DoubleElectron/Sept2012production8TeV_Ele2012B_V4/ee8b79c5bec180099e91bf02c7018cc0/ -o ControlPlots_"+cpVersion+"/ControlPlots_Ele"+DATA+"B/Ele"+DATA+"B_"+MC+"_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyEle --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "Mu" in samples :
    njobs = 50
    if "A" in listdata :
        for i in range(0,njobs):
            LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/store/user/acaudron/Sept2012production8TeV/Mu2012A_V3/acaudron/DoubleMu/Sept2012production8TeV_Mu2012A_V3/18ff4149fdd30a1229c72782767e6503/ -o ControlPlots_"+cpVersion+"/ControlPlots_Mu"+DATA+"A/Mu"+DATA+"A_"+MC+"_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyMu --Njobs "+str(njobs)+" --jobNumber "+str(i)])

    njobs = 300
    if "B" in listdata :
        for i in range(0,njobs):
            LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/store/user/acaudron/Sept2012production8TeV/Mu2012B_V3/acaudron/DoubleMu/Sept2012production8TeV_Mu2012B_V3/18ff4149fdd30a1229c72782767e6503/ -o ControlPlots_"+cpVersion+"/ControlPlots_Mu"+DATA+"B/Mu"+DATA+"B_"+MC+"_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyMu --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "ZH" in samples :
    mass = [125]#[115,120,125,130,135]
    for m in mass:
        njobs = 40
        for i in range(0,njobs):
            LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/store/user/acaudron/Sept2012production8TeV/Summer12_ZH125_S10_V2/acaudron/ZH_ZToLL_HToBB_M-125_8TeV-powheg-herwigpp/Sept2012production8TeV_Summer12_ZH125_S10_V2/d5186fd016990c766c736d42e5dce079/ -o ControlPlots_"+cpVersion+"/ControlPlots_ZH"+str(m)+"/ZH"+str(m)+"_"+MC+"_"+str(i)+".root --all -p ../data/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_pileupTruth.root -P ../data/MCpileup_Summer12_S10.root -w ../data/performance_csv_witheff.root  --Njobs "+str(njobs)+" --jobNumber "+str(i)])

LaunchOnCondor.SendCluster_Submit()
