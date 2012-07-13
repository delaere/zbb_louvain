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

