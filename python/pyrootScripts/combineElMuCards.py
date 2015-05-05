###############
### imports ###
###############

import math
import os, sys
from ROOT import *

###################
### Definitions ###
###################
'''
mAHypoList = [30,50,70,90,110,130,150]
mHHypoList = [325,375,425,475]

mHBin = {325:1,
         375:2,
         425:3,
         475:4}

mABin = {  30:1,
           50:2,
           70:3,
           90:4,
          110:5,
          130:6,
          150:7 }
'''

numDirs=36
numFiles=36
#numDirs=40
#numFiles=20
massResol=0.15
bin_width = 1.5
step_fraction = 2.0/3.0

run_combine = 0

myTGraph = TGraph2D(100)
myTGraph.SetNpx(500)
myTGraph.SetNpy(500)


mllbb=10
#mllbb=206

#DIR = "/nfs/user/acaudron/datacards2HDMyieldsSignal/"
#DIR = "/nfs/user/acaudron/unblindedDatacards2HDMyieldsSignal/"
DIR = "/nfs/user/acaudron/unblindedDatacards2HDMMCstatV2/"
#DIR = "/nfs/user/acaudron/unblindedDatacards2HDMyieldsSignalSignalInjec/"
#DIR = "/nfs/user/acaudron/datacards2HDM/"
#DIR = "/nfs/user/acaudron/unblindedDatacards2HDM/"
#DIR = "/nfs/user/acaudron/unblindedDatacards2HDMyieldsSignalzoomLo/"
#DIR = "/nfs/user/acaudron/toyDatacards2HDM/"
toy = ""
if len(sys.argv)==2 : toy = "_"+sys.argv[1] 

mkdir_cmd = "mkdir "+DIR+"Combined"
os.system(str(mkdir_cmd))

for i in range(1,numDirs):
  dmllbb=massResol*mllbb*bin_width
  step_mllbb = dmllbb*step_fraction
  #step_mllbb = 4
  mbb=10.0
  #mbb=63

#  mkdir_cmd = "mkdir /home/fynu/amertens/scratch/CMSSW/CMSSW_6_1_1/src/2HDM/mH"+str(int(mllbb-dmllbb))+"to"+str(int(mllbb+dmllbb))+"/Combined"
#  os.system(str(mkdir_cmd))

  for j in range(1,numFiles):
    dmbb=massResol*mbb*bin_width
    step_mbb = dmbb*step_fraction
    #step_mbb = 3

    print step_mbb
#    yield_Mu = "/home/fynu/amertens/scratch/CMSSW/CMSSW_6_1_1/src/2HDM/mH"+str(int(mllbb-dmllbb))+"to"+str(int(mllbb+dmllbb))+"/Mu/testmA"+str(int(mbb-dmbb))+"to"+str(int(mbb+dmbb))+".txt"
#    yield_El = "/home/fynu/amertens/scratch/CMSSW/CMSSW_6_1_1/src/2HDM/mH"+str(int(mllbb-dmllbb))+"to"+str(int(mllbb+dmllbb))+"/El/testmA"+str(int(mbb-dmbb))+"to"+str(int(mbb+dmbb))+".txt"

    yield_Mu = ""+DIR+"Mu/"+str(int(mbb))+"_"+str(int(mllbb))+toy+".txt"
    yield_El = ""+DIR+"El/"+str(int(mbb))+"_"+str(int(mllbb))+toy+".txt"
#    yield_comb = "/home/fynu/amertens/scratch/CMSSW/CMSSW_6_1_1/src/2HDM/mH"+str(int(mllbb-dmllbb))+"to"+str(int(mllbb+dmllbb))+"/Combined/testmA"+str(int(mbb-dmbb))+"to"+str(int(mbb+dmbb))+".txt"
    yield_comb = ""+DIR+"Combined/"+str(int(mbb))+"_"+str(int(mllbb))+toy+".txt"

    if os.path.isfile(yield_Mu) :
      combine_cmd = "combineCards.py "+yield_Mu+" "+yield_El+" > "+yield_comb

      os.system(str(combine_cmd))
    #combine_cmd = "combine -M ProfileLikelihood --significance --pvalue -m "+str(int(mbb))+" "+yield_path+" -t -1 --expectSignal=1"

    mbb+=step_mbb

  mllbb+=step_mllbb

###########
### FIN ###
###########
