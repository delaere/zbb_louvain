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
  "MuA_DATA"     : "/nfs/user/llbb/Pat_8TeV_532p4/Mu2012A_V3/" ,
  "ElA_DATA"     : "/nfs/user/llbb/Pat_8TeV_532p4/Mu2012B_V3/" ,
  "MuB_DATA"     : "/nfs/user/llbb/Pat_8TeV_532p4/Ele2012A_V4/" ,
  "ElB_DATA"     : "/nfs/user/llbb/Pat_8TeV_532p4/Ele2012B_V4/" ,
  "Mu_MC"        : "/nfs/user/llbb/Pat_8TeV_532p4/DYjets_Summer12_V2/"    ,
  "El_MC"        : "/nfs/user/llbb/Pat_8TeV_532p4/DYjets_Summer12_V2/"    ,
  "TT_Mu_MC"     : "/nfs/user/llbb/Pat_8TeV_532p4/TTjets_Summer12/"    ,
  "TT_El_MC"     : "/nfs/user/llbb/Pat_8TeV_532p4/TTjets_Summer12/"    ,
  "ZZ_Mu_MC"     : "/nfs/user/llbb/Pat_8TeV_532p4/ZZ_Summer12_V2/"    ,
  "ZZ_El_MC"     : "/nfs/user/llbb/Pat_8TeV_532p4/ZZ_Summer12_V2/"    ,
  #"ZH115_Mu_MC"  : "/nfs/user/llbb/Pat_8TeV_532p4/ZH115_MC/" ,
  #"ZH115_El_MC"  : "/nfs/user/llbb/Pat_8TeV_532p4/ZH115_MC/" ,
  #"ZH120_Mu_MC"  : "/nfs/user/llbb/Pat_8TeV_532p4/ZH120_MC/" ,
  #"ZH120_El_MC"  : "/nfs/user/llbb/Pat_8TeV_532p4/ZH120_MC/" ,
  "ZH125_Mu_MC"  : "/nfs/user/llbb/Pat_8TeV_532p4/ZH125_Summer12_V2/" ,
  "ZH125_El_MC"  : "/nfs/user/llbb/Pat_8TeV_532p4/ZH125_Summer12_V2/" ,
  #"ZH130_Mu_MC"  : "/nfs/user/llbb/Pat_8TeV_532p4/ZH130_MC/" ,
  #"ZH130_El_MC"  : "/nfs/user/llbb/Pat_8TeV_532p4/ZH130_MC/" ,
  #"ZH135_Mu_MC"  : "/nfs/user/llbb/Pat_8TeV_532p4/ZH135_MC/" ,
  #"ZH135_El_MC"  : "/nfs/user/llbb/Pat_8TeV_532p4/ZH135_MC/" ,
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
