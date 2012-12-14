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
  print "python ", sys.argv[0], " /storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/zbbProd/ 3 _Zbb4Flavee"


  print "python ", sys.argv[0], "MuA_DATA 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ElA_DATA 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "MuB_DATA 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ElB_DATA 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "Mu_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "El_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "TT_Mu_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "TT_El_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZZ_Mu_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZZ_El_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZH115_Mu_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZH115_El_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZH120_Mu_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZH120_El_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZH125_Mu_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZH125_El_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZH130_Mu_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZH130_El_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZH135_Mu_MC 9999 _CSV2011Sel"
  print "python ", sys.argv[0], "ZH135_El_MC 9999 _CSV2011Sel"

  exit()
  
mappath = { 
  "MuA_DATA"     : "/nfs/user/acaudron/skim444/Mu_DataA/" ,
  "ElA_DATA"     : "/nfs/user/acaudron/skim444/El_DataA/" ,
  "MuB_DATA"     : "/nfs/user/acaudron/skim444/Mu_DataB/" ,
  "ElB_DATA"     : "/nfs/user/acaudron/skim444/El_DataB/" ,
  "Mu_MC"        : "/nfs/user/acaudron/skim444/DY_MC/"    ,
  "El_MC"        : "/nfs/user/acaudron/skim444/DY_MC/"    ,
  #"Mu_MC"        : "/storage/data/cms/store/user/acaudron/Torino/DYJets_MCMatched_00.root"    , 
  #"El_MC"        : "/storage/data/cms/store/user/acaudron/Torino/DYJets_MCMatched_00.root"    , 
  "Zbb_Mu_MC"    : "/storage/data/cms/store/user/acaudron/Fall11MC_444/zbbProd/"   ,
  "Zbb_El_MC"    : "/storage/data/cms/store/user/acaudron/Fall11MC_444/zbbProd/"   ,
  "TT_Mu_MC"     : "/nfs/user/acaudron/skim444/TT_MC/"    ,
  "TT_El_MC"     : "/nfs/user/acaudron/skim444/TT_MC/"    ,
  "ZZ_Mu_MC"     : "/nfs/user/acaudron/skim444/ZZ_MC/"    ,
  "ZZ_El_MC"     : "/nfs/user/acaudron/skim444/ZZ_MC/"    ,
  "ZH115_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH115_MC/" ,
  "ZH115_El_MC"  : "/nfs/user/acaudron/skim444/ZH115_MC/" ,
  "ZH120_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH120_MC/" ,
  "ZH120_El_MC"  : "/nfs/user/acaudron/skim444/ZH120_MC/" ,
  "ZH125_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH125_MC/" ,
  "ZH125_El_MC"  : "/nfs/user/acaudron/skim444/ZH125_MC/" ,
  "ZH130_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH130_MC/" ,
  "ZH130_El_MC"  : "/nfs/user/acaudron/skim444/ZH130_MC/" ,
  "ZH135_Mu_MC"  : "/nfs/user/acaudron/skim444/ZH135_MC/" ,
  "ZH135_El_MC"  : "/nfs/user/acaudron/skim444/ZH135_MC/" ,
  "tW_Mu_MC"     : "/nfs/user/acaudron/skim444/tW_MC/"    ,
  "tW_El_MC"     : "/nfs/user/acaudron/skim444/tW_MC/"    ,
  "tbarW_Mu_MC"  : "/nfs/user/acaudron/skim444/tbarW_MC/" ,
  "tbarW_El_MC"  : "/nfs/user/acaudron/skim444/tbarW_MC/" ,
  "evtgen_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/evtgen/",
  "herwig_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/herwig/",
  "pythia_MC"    : "/storage/data/cms/users/tdupree/zbb_2011/pythia/",
  "ZA_Mu_MC" : "/nfs/user/acaudron/ZApat/",
  "ZA_El_MC" : "/nfs/user/acaudron/ZApat/"
  }


channel = sys.argv[1]
suffix=sys.argv[3]
nfilespersection=int(sys.argv[2])

path=mappath[channel]

FarmDirectory = "FARM_CMSToLHCO_"+channel+suffix

#dir with the number of rootfiles
dirList=os.listdir(path)


#number of rootfiles
nrootfile=len(dirList)
njobs = int(nrootfile)/nfilespersection
if  nfilespersection > nrootfile: njobs = 1

#print "dirList=", dirList, " nrootfile=",nrootfile, " nfilespersection = ", nfilespersection, " njobs=",njobs

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

JobName = "outCMStoLHCO_"+channel+suffix
LaunchOnCondor.Jobs_RunHere = 1
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
LaunchOnCondor.Jobs_RunHere= 1


for i in range(0,njobs):
   #command = path isection Nfilessection suffix 
   command = "./CMS_To_LHCO_usingFramework_batch.py" + " " + channel + " " + str(i) + " " + str(int(nfilespersection)) + " " + suffix

   #print "command = ", command
   LaunchOnCondor.SendCluster_Push(["PYTHON", command])
    
LaunchOnCondor.SendCluster_Submit()

