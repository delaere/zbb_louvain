###############
### imports ###
###############

import math
import os
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
massResol=0.15
bin_width = 1.5
step_fraction = 2.0/3.0

run_combine = 0

myTGraph = TGraph2D(100)
myTGraph.SetNpx(100)
myTGraph.SetNpy(100)


mllbb=10
n=0
for i in range(1,numDirs):
  dmllbb=massResol*mllbb*bin_width
  step_mllbb = dmllbb*step_fraction

  MH_dir = "MH_"+str(int(mllbb))
  if run_combine == 1:
    mkdir_cmd = "mkdir "+MH_dir
    print mkdir_cmd
    rmdir_cmd = "rm -rf "+MH_dir
    os.system(rmdir_cmd)
    os.system(str(mkdir_cmd))
  mbb=10.0
  for j in range(1,numFiles):
    dmbb=massResol*mbb*bin_width
    step_mbb = dmbb*step_fraction
    print step_mbb
    yield_path = "/home/fynu/amertens/scratch/CMSSW/CMSSW_6_1_1/src/2HDM/mH"+str(int(mllbb-dmllbb))+"to"+str(int(mllbb+dmllbb))+"/Combined/testmA"+str(int(mbb-dmbb))+"to"+str(int(mbb+dmbb))+".txt"
    #combine_cmd = "combine -M ProfileLikelihood --significance --pvalue --backgroundPdfNames='*WZ*,*ZZ*,*Zb*,*ZH*,*WW*,*TT*,*Wt* --signalPdfNames=*ZA* -m "+str(int(mbb))+" "+yield_path+" -t -1 --expectSignal=1"
    combine_cmd = "combine -M ProfileLikelihood --significance --pvalue -m "+str(int(mbb))+" "+yield_path+" -t -1 --expectSignal=1"
    print combine_cmd
    n+=1
    try:
      file_path = MH_dir+"/higgsCombineTest.ProfileLikelihood.mA"+str(int(mbb))+".root"
      if run_combine == 1:
        os.system(str(combine_cmd))
        cp_cmd = "cp higgsCombineTest.ProfileLikelihood.mH"+str(int(mbb))+".root "+file_path
        os.system(str(cp_cmd))

      fList = TFile(str(file_path)) 
      mytree  = fList.Get("limit")
      for entry in mytree:
        print "p-value(",(i-1)*numDirs+(j-1) , ", " , int(mbb) , ", " , int(mllbb),") = ", mytree.limit
        j+=1
        myTGraph.SetPoint(n, mbb, mllbb, mytree.limit)
    except:
      print 'no background events'
      myTGraph.SetPoint(n, mbb, mllbb, 0)
    mbb+=step_mbb

    print '##############################################'
    print 'mbb:', mbb, 'myTGraph size', myTGraph.GetN()
    print '##############################################'

  mllbb+=step_mllbb

'''
  hadd_cmd = "hadd "+MH_dir+"/higgsCombineTest.ProfileLikelihood.root "+MH_dir+"/higgsCombineTest.ProfileLikelihood.mA*.root"
  os.system(str(hadd_cmd))
  fList = TFile(MH_dir+"/higgsCombineTest.ProfileLikelihood.root")
  mytree  = fList.Get("limit")
  j=0
  for entry in mytree:
    print "p-value(",(i-1)*5+(j-1) , ", " , mbb , ", " , mllbb,") = ", entry.limit
    j+=1
    myTGraph.SetPoint((i-1)*5+(j-1), mbb, mllbb,entry.limit)
'''
'''
C=TCanvas("C","C",2000,1000)
C.Divide(2)
C.cd(1)
myTGraph.Draw("CONT")
C.cd(2)
myTGraph.Draw("surf1")
C.Print("Limits_data.png","png")
C.Print("Limits_data.C","cxx")
'''

C=TCanvas("C","C",1000,1000)
ROOT.gStyle.SetPalette(52)
C.SetRightMargin(0.2)
C.SetLogz()
myTGraph.Draw("colz")
myTGraph.GetXaxis().SetTitle("m_{bb}")
myTGraph.GetYaxis().SetTitle("m_{llbb}")
myTGraph.GetZaxis().SetTitle("Expected Exclusion (Events / GeV^{2})")
#myTGraph.GetZaxis().SetLimits(0.0001,10.0)
C.Update();
C.Modified();
C.Print("Exp_Lim_BW_allBkg_colz.png","png")


C2=TCanvas("C2","C2",1200,1000)
ROOT.gStyle.SetPalette(52)
C2.SetRightMargin(0.2)
C2.SetLeftMargin(0.2)
C2.SetLogz()
myTGraph.SetTitle("p-value (signal injected)")
myTGraph.GetXaxis().SetRangeUser(0,700)
myTGraph.GetYaxis().SetRangeUser(0,700)
myTGraph.GetXaxis().SetTitle("M_{bb} (GeV)")
myTGraph.GetXaxis().SetTitleSize(0.07)
myTGraph.GetXaxis().SetTitleOffset(0.6)
myTGraph.GetYaxis().SetTitle("M_{Zbb} (GeV)")
myTGraph.GetYaxis().SetTitleSize(0.07)
myTGraph.GetYaxis().SetTitleOffset(0.8)
myTGraph.GetZaxis().SetTitle("p-value")
myTGraph.GetZaxis().SetTitleSize(0.07)
myTGraph.GetZaxis().SetTitleOffset(0.6)
#myTGraph.GetZaxis().SetLimits(0.0001,10.0)
myTGraph.SetMarkerStyle(20); 
myTGraph.Draw("PCOL")
#myTGraph.GetZaxis().SetRangeUser(0.00000000001,0.5)

C2.Print("pvalue_BW.png","png")
C2.Print("pvalue_BW.C","cxx")


'''
fList={}
treeList={}

binx=0
biny=0

###########
### Run ###
###########

for MH in mHHypoList:

    print "======= MH=", MH
    MHmin = str(MH-25)
    MHmax = str(MH+25)

    for MA in mAHypoList:

        print "MA=", MA
        filename = "MH_"+MHmin+"-"+MHmax+"/Mu/higgsCombineTest.ProfileLikelihood.mH"+str(MA)+".root"
        print "filename = ", filename

        fList[MH] = TFile(filename)
        mytree  = fList[MH].Get("limit")

        for entry in mytree:
            
            print "p-value = ", entry.limit
            myTH2D.SetBinContent(mABin[MA], #[tree.mh],
                                 mHBin[MH],
                                 entry.limit
                                 )

####################
### Colored plot ###
####################

C=TCanvas("C","C",1000,500)
C.Divide(2)
C.cd(1)
myTH2D.Draw("colz")
C.cd(2).SetLogz()
myTH2D.Draw("colz")
C.Draw()

################
### B&W plot ###
################

C2=TCanvas("C2","C2",1000,500)
C2.Divide(2)
ROOT.gStyle.SetPalette(52)
C2.cd(1)
myTH2D.Draw("colz")
C2.cd(2).SetLogz()
myTH2D.Draw("colz")
'''
print "==> Now you have your 2D p-value scans of MH vs MA :-)"

###########
### FIN ###
###########
