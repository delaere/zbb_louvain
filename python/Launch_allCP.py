#!/usr/bin/env python

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob
import os

samples = [
    #"TT",
    #"Zl",
    "Zc",
    "Zb",
    "ZZ",
    "ZH",
    #"Ele",
    #"Mu"
    ]

MC = "Fall11"
DATA = "2011"
cpVersion = "V3"

os.system('mkdir ControlPlots_'+cpVersion)
for sample in samples :
    os.system('mkdir ControlPlots_'+cpVersion+'/ControlPlots_'+sample)

FarmDirectory = "FARM_CP_"+cpVersion
JobName = "ZbbAnalysis_All"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1
if "TT" in samples :
    njobs = 300
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_TTbar_v3/ -o ControlPlots_"+cpVersion+"/ControlPlots_TT/TT_"+MC+"_"+str(i)+".root --all -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "Zl" in samples :
    njobs = 400
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_DYjets_v4/ -o ControlPlots_"+cpVersion+"/ControlPlots_Zl/Zl_"+MC+"_"+str(i)+".root --all -j l -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "Zc" in samples :
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_DYjets_v4/ -o ControlPlots_"+cpVersion+"/ControlPlots_Zc/Zc_"+MC+"_"+str(i)+".root --all -j c -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "Zb" in samples :
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_DYjets_v4/ -o ControlPlots_"+cpVersion+"/ControlPlots_Zb/Zb_"+MC+"_"+str(i)+".root --all -j b -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "ZZ" in samples :
    njobs = 50
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_ZZ_v2/ -o ControlPlots_"+cpVersion+"/ControlPlots_ZZ/ZZ_"+MC+"_"+str(i)+".root --all -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "Ele" in samples :
    njobs = 400
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/Production_5fb/Data/Ele2011A/files/ -o ControlPlots_"+cpVersion+"/ControlPlots_Ele"+DATA+"A/Ele"+DATA+"A_"+MC+"_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyEle --Njobs "+str(njobs)+" --jobNumber "+str(i)])

    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/Production_5fb/Data/Ele2011B/files/ -o ControlPlots_"+cpVersion+"/ControlPlots_Ele"+DATA+"B/Ele"+DATA+"B_"+MC+"_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyEle --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "Mu" in samples :
    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/Production_5fb/Data/Mu2011A/files/ -o ControlPlots_"+cpVersion+"/ControlPlots_Mu"+DATA+"A/Mu"+DATA+"A_"+MC+"_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyMu --Njobs "+str(njobs)+" --jobNumber "+str(i)])

    for i in range(0,njobs):
        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/Production_5fb/Data/Mu2011B/files/ -o ControlPlots_"+cpVersion+"/ControlPlots_Mu"+DATA+"B/Mu"+DATA+"B_"+MC+"_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyMu --Njobs "+str(njobs)+" --jobNumber "+str(i)])

if "ZH" in samples :
    mass = [115,120,125,130,135]
    for m in mass:
        njobs = 40
        for i in range(0,njobs):
            LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_ZHbb_"+str(m)+"/ -o ControlPlots_"+cpVersion+"/ControlPlots_ZH"+str(m)+"/ZH"+str(m)+"_"+MC+"_"+str(i)+".root --all -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs "+str(njobs)+" --jobNumber "+str(i)])

LaunchOnCondor.SendCluster_Submit()
