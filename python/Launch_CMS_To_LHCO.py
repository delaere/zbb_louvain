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

  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/production2012_44X/Fall11_TTbar/ 363 _TTtest44"

  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/production2012_44X/Fall11_ZZ/ 841 _1fileperjobZZTest44"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/production2012_44X/Fall11_ZZ/ 29 _ZZTest44"

  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/productionJune2012_444/Fall11_Hbb/ 55 _ZHbb125"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/productionJune2012_444/Fall11_T_tW/ 17 _tW"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/productionJune2012_444/Fall11_Tbar_tW/ 18 _tbarW"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/productionJune2012_444/Fall11_TT_powheg/ 47 _TTpow"

  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/productionJune2012_444/Fall11_ZZ/ 421 _ZZ"


  print "python ", sys.argv[0], " /storage/data/cms/store/user/acaudron/Fall11MC_444/Fall11_DYjets_v4/acaudron/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/production5fb_June2012_Fall11_DYjets_v4/918089973f5ad18b0c79d580ed9142aa/ 1451 _DY"


  print "python ", sys.argv[0], " /home/fynu/vizangarciaj/scratch/DY444secondProdMissingFile/ 1 _DY1missingfileEE"
  print "python ", sys.argv[0], " /home/fynu/vizangarciaj/scratch/DY444secondProdMissingFile/ 1 _DY1missingfileMM"

  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/zbbProd/ 3 _Zbb4Flavee"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/zbbProd/ 3 _Zbb4Flavmumu"


  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/zbbProd/ 3 _Zbb4Flavmumu"

  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_TTbar_v3/ 54 _TTmumu"
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_TTbar_v3/ 54 _TTee"

  print "python ", sys.argv[0], " /home/fynu/vizangarciaj/scratch/DATA_5fb_EleA/ 499 _DataEleA"
  print "python ", sys.argv[0], " /home/fynu/vizangarciaj/scratch/DATA_5fb_EleB/ 353 _DataEleB"

  print "python ", sys.argv[0], " /home/fynu/vizangarciaj/scratch/DATA_5fb_Mu/ 183 _DataMu"
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
   command = "./CMS_To_LHCO_usingFramework_batch.py" + " " + path + " " + str(i) + " " + str(int(nrootfile/njobs)) + " " + suffix

   #print "command = ", command
   LaunchOnCondor.SendCluster_Push(["PYTHON", command])
    
LaunchOnCondor.SendCluster_Submit()

