import sys
import ROOT
import os
import glob
from ROOT import *
gROOT.Macro("~/rootlogon.C")

from DataFormats.FWLite import Events, Handle

from ROOT import RooUnfoldResponse
from ROOT import RooUnfold
#from ROOT import RooUnfoldBayes
from ROOT import RooUnfoldSvd
# from ROOT import RooUnfoldTUnfold

print "=========== getting response matrix ============="
### get only root files in the current directory ###
##dirList = os.listdir(os.getcwd())
list = open('list','r')
dirList=[]

for line in list:
    dirList.append(line.replace("\n",""))
    
print "dirList", dirList,

response= RooUnfoldResponse(25,0,500);
hTrue= TH1D ("true", "Test Truth", 25 , 0., 500.)
hMeas= TH1D ("meas", "Test Measured", 25 , 0., 500.)

#### loop on files ####
for fileList in dirList :
    print "fileList", fileList
    file = TFile(fileList)
    print "file", file
    response.Add(file.Get("response_pT_Z"))

    hTrue.Add(file.Get("true"))
    hMeas.Add(file.Get("meas"))

output_file= TFile('merged.root','RECREATE')
output_file.WriteTObject(hMeas)
output_file.WriteTObject(hTrue)
output_file.WriteTObject(response, "response_pT_Z")
