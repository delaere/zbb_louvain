## Script to combine the datacards for the Muon and Electron channels ##

###############
### imports ###
###############

import os, sys
import math
from ROOT import *

###################
### Definitions ###
###################

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

### Directory whare to find the datacards ###
#DIR = "/nfs/user/acaudron/datacards2HDMyieldsSignal/"
#DIR = "/nfs/user/acaudron/unblindedDatacards2HDMyieldsSignal/"
#DIR = "/nfs/user/acaudron/unblindedDatacards2HDMMCstatV2/"
#DIR = "/nfs/user/acaudron/unblindedDatacards2HDMyieldsSignalSignalInjec/"
#DIR = "/nfs/user/acaudron/datacards2HDM/"
DIR = "/nfs/user/acaudron/unblindedDatacards2HDM/"
#DIR = "/nfs/user/acaudron/unblindedDatacards2HDMyieldsSignalzoomLo/"
#DIR = "/nfs/user/acaudron/toyDatacards2HDM/"

### Toy or not ###
toy = ""
if len(sys.argv)==2 : toy = "_"+sys.argv[1] 

### Create combined directory ###
mkdir_cmd = "mkdir "+DIR+"Combined"
os.system(str(mkdir_cmd))

for i in range(1,numDirs):
  dmllbb=massResol*mllbb*bin_width
  step_mllbb = dmllbb*step_fraction
  #step_mllbb = 4
  mbb=10.0
  #mbb=63

  for j in range(1,numFiles):
    dmbb=massResol*mbb*bin_width
    step_mbb = dmbb*step_fraction
    #step_mbb = 3

    print step_mbb

    ### Get the cards by channels ###
    yield_Mu = ""+DIR+"Mu/"+str(int(mbb))+"_"+str(int(mllbb))+toy+".txt"
    yield_El = ""+DIR+"El/"+str(int(mbb))+"_"+str(int(mllbb))+toy+".txt"
    yield_comb = ""+DIR+"Combined/"+str(int(mbb))+"_"+str(int(mllbb))+toy+".txt"

    ### if files exist: execute the combineCards command ###
    if os.path.isfile(yield_Mu) :
      combine_cmd = "combineCards.py "+yield_Mu+" "+yield_El+" > "+yield_comb
      os.system(str(combine_cmd))

    mbb+=step_mbb
  mllbb+=step_mllbb

###########
### FIN ###
###########
