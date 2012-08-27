#!/usr/bin/env python

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob

FarmDirectory = "FARM_All"
JobName = "ZbbAnalysis_All"
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1
for i in range(0,300):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_TTbar_v3/ -o ControlPlots_TT/TT_Fall11_"+str(i)+".root --all -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs 300 --jobNumber "+str(i)])

for i in range(0,400):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_DYjets_v4/ -o ControlPlots_ZlfromDY/Zl_fromDYJets_Summer11_"+str(i)+".root --all -j l -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs 400 --jobNumber "+str(i)])

for i in range(0,400):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_DYjets_v4/ -o ControlPlots_ZbfromDY/Zb_fromDYJets_Summer11_"+str(i)+".root --all -j b -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs 400 --jobNumber "+str(i)])

for i in range(0,400):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_DYjets_v4/ -o ControlPlots_ZcfromDY/Zc_fromDYJets_Summer11_"+str(i)+".root --all -j c -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs 400 --jobNumber "+str(i)])

for i in range(0,50):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_ZZ_v2/ -o ControlPlots_ZZ/ZZ_Fall11_"+str(i)+".root --all -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs 50 --jobNumber "+str(i)])

for i in range(0,400):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/Production_5fb/Data/Ele2011A/files/ -o ControlPlots_Ele2011A/Ele2011A_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyEle --Njobs 400 --jobNumber "+str(i)])

for i in range(0,400):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/Production_5fb/Data/Ele2011B/files/ -o ControlPlots_Ele2011B/Ele2011B_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyEle --Njobs 300 --jobNumber "+str(i)])

for i in range(0,400):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/Production_5fb/Data/Mu2011A/files/ -o ControlPlots_Mu2011A/Mu2011A_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyMu --Njobs 400 --jobNumber "+str(i)])

for i in range(0,400):
    LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/Production_5fb/Data/Mu2011B/files/ -o ControlPlots_Mu2011B/Mu2011B_"+str(i)+".root --all --noPUweight --noBweight --noLweight --trigger --onlyMu --Njobs 400 --jobNumber "+str(i)])

#mass = [115,120,125,130,135]
#for m in mass:
#    for i in range(0,40):
#        LaunchOnCondor.SendCluster_Push(["PYTHON", os.getcwd()+"/ControlPlots.py -i /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_ZHbb_"+str(m)+"/ -o ControlPlots_ZH_"+str(m)+"/ZH"+str(m)+"_Fall11_"+str(i)+".root --all -p ../data/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2_pileupTruth.root -P ../data/Fall11_PU_MC.root -w ../data/performance_ssv_witheff_062012.root --Njobs 40 --jobNumber "+str(i)])

LaunchOnCondor.SendCluster_Submit()
