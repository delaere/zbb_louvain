#!/usr/bin/env python

##

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob

from optparse import OptionParser

narguments = len(sys.argv)
if narguments != 4:
  print "Usage: ", sys.argv[0], " foldername njobs suffix"
  print "Examples"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/mc_DYJets/Summer11_DYJets/DYJets/ 82 _DYmumu"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/mc_DYJets/Summer11_DYJets/DYJets/ 82 _DYee"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/mc_TTJets/Summer11_TTJets/TTJets/ 31 _TTmumu"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/mc_TTJets/Summer11_TTJets/TTJets/ 31 _TTee"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/mc_ZZ/Summer11/ 11 _ZZmumu"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/mc_ZZ/Summer11/ 11 _ZZee"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/TTbar_pow/ 146 _TTpowee"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/TTbar_pow/ 146 _TTpowmumu"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/mc_Higgstobb/Summer11/ 37 _ZH125mumu"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/mc_Higgstobb/Summer11/ 37 _ZH125ee"


  print "python ", sys.argv[0], " /home/fynu/vizangarciaj/scratch/DYJets_Summer11_fewfiles/ 7 _DY7files"
  
  print "python ", sys.argv[0], " /home/fynu/vizangarciaj/scratch/DATA_2fb_Ele/ 73 _DATAee"
  print "python ", sys.argv[0], " /home/fynu/vizangarciaj/scratch/DATA_2fb_Muon/ 137 _DATAmumu"



  print "python ", sys.argv[0], " /storage/data/cms/users/arnaudp/Zbb_Prod_local/FARM_Zllbb_PAT_step/outputs/ 341 _Zbb4flvee"
  print "python ", sys.argv[0], " /storage/data/cms/users/arnaudp/Zbb_Prod_local/FARM_Zllbb_PAT_step/outputs/ 341 _Zbb4flvmumu"

  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/Prod_data_2012A/DoubleMuCert_190456-191276/ 150 _DATA12Amumu"

  print "python ", sys.argv[0], " /storage/data/cms/users/rcastello/Ele_2011A_44X_newAl/ 119 _test44"

#  /storage/data/cms/users/llbb/Prod_data_2fb/Aug05ReReco/Ele_Aug05ReReco/Ele_Aug05ReReco_Sub3
#  /storage/data/cms/users/llbb/Prod_data_2fb/Aug05ReReco/Mu_Aug05ReReco/Mu_Aug05ReReco_Sub3
#  /storage/data/cms/users/llbb/Prod_data_2fb/May10ReReco/Ele_May10ReReco/Ele_May10
#  /storage/data/cms/users/llbb/Prod_data_2fb/May10ReReco/Mu_May10ReReco/Mu_May10
#  /storage/data/cms/users/llbb/Prod_data_2fb/PromptRecoV4/Ele_PromptRecoV4/Ele_PromptRecoV4
#  /storage/data/cms/users/llbb/Prod_data_2fb/PromptRecoV4/Mu_PromptRecoV4/Mu_PromptRecoV4
#  /storage/data/cms/users/llbb/Prod_data_2fb/PromptRecoV6/Ele_PromptRecoV6/Ele_PromptRecoV6
#  /storage/data/cms/users/llbb/Prod_data_2fb/PromptRecoV6/Mu_PromptRecoV6/Mu_PromptRecoV6


  
  exit()

path=sys.argv[1]
njobs=int(sys.argv[2])
suffix=sys.argv[3]

FarmDirectory = "FARM_CMSToLHCO"+suffix

#dir with the number of rootfiles
dirList=os.listdir(path)

#number of rootfiles
nrootfile=len(dirList)
nexact=(nrootfile%njobs==0)



if njobs > nrootfile:
  print "njobs=", njobs, " should not be greater thatn nrootfile=", nrootfile
  exit()


if nexact == True:
  print "I will run ", njobs, " sections over the same number of files = ", nrootfile/njobs 
else :
  print "I will run ", njobs, "sections with ", int(nrootfile/njobs), " files and 1 section over ", nrootfile%njobs, "files"
  njobs += 1
  
print "I will run over the rootfiles in path = ", path, " which contains ", nrootfile, "rootfiles"

JobName = "outCMStoLHCO"+suffix
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1


for i in range(0,njobs):
   #command = path isection Nfilessection suffix 
   command = "/home/fynu/vizangarciaj/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/CMS_To_LHCO_usingFramework_batch.py" + " " + path + " " + str(i) + " " + str(int(nrootfile/njobs)) + " " + suffix

   #print "command = ", command
   LaunchOnCondor.SendCluster_Push(["PYTHON", command])
    
LaunchOnCondor.SendCluster_Submit()

