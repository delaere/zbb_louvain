###############
### imports ###
###############

import math
import os
from ROOT import *



#numDirs=36
#numFiles=36

numDirs=36
numFiles=36

massResol=0.15
bin_width = 1.5
step_fraction = 2.0/3.0

run_combine = 1

DataCards_path = "/home/fynu/amertens/storage/THDM/DataCards/Mu/"

myTGraph = TGraph2D(100)
myTGraph.SetName("Limit")
h0 = TH2D("h1","Expected Exclusion (Events / (GeV^{2}))",500,0,1200,500,0,1200)
myTGraph.SetHistogram(h0)



myTGraph_sigma = TGraph2D(100)
myTGraph_sigma.SetName("Efficiency + Acceptance")
h1 = TH2D("h1","Efficiency + Acceptance",500,0,1200,500,0,1200)
myTGraph_sigma.SetHistogram(h1)


myTGraph_limit = TGraph2D(10)
myTGraph_limit.SetName("limit_on_sigma")
#myTGraph_limit.SetNpx(500)
#myTGraph_limit.SetNpy(500)

h2 = TH2D("h2","Expected Exclusion on #sigma(fb)",500,0,1200,500,0,1200)
myTGraph_limit.SetHistogram(h2)
#myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)
#myTGraph_limit.GetHistogram().GetXaxis().SetLimits(0,1000)

myTGraph2 = TGraph2D(100)
myTGraph2.SetName("Expected Exclusion (Events)")
h3 = TH2D("h3","Expected Exclusion (Events)",500,0,1200,500,0,1200)
myTGraph2.SetHistogram(h3)


mllbb=10
n=-1
m=-1
for i in range(1,numDirs):
  dmllbb=massResol*mllbb*bin_width
  step_mllbb = dmllbb*step_fraction

  MH_dir_NOSYST = "MH_"+str(int(mllbb))+"_Asymptotic_NOSYST_"
  MH_dir_SYST = "MH_"+str(int(mllbb))+"_Asymptotic_SYST_"
  if run_combine == 1:
    mkdir_cmd = "mkdir "+MH_dir_SYST
    print mkdir_cmd
    rmdir_cmd = "rm -rf "+MH_dir_SYST
    os.system(rmdir_cmd)
    os.system(str(mkdir_cmd))
    mkdir_cmd = "mkdir "+MH_dir_NOSYST
    print mkdir_cmd
    rmdir_cmd = "rm -rf "+MH_dir_NOSYST
    os.system(rmdir_cmd)
    os.system(str(mkdir_cmd))
  mbb=10.0
  for j in range(1,numFiles):
    dmbb=massResol*mbb*bin_width
    step_mbb = dmbb*step_fraction
    if (mbb < mllbb) and (mllbb > 200) and (mbb > 100):
      yield_path = DataCards_path+str(int(mbb))+"_"+str(int(mllbb))+".txt"
      combine_cmd_nosys = "combine -M Asymptotic -m "+str(int(mbb))+" -S 0 --run=blind "+yield_path
      combine_cmd_sys = "combine -M Asymptotic -m "+str(int(mbb))+" --run=blind "+yield_path
      #combine_cmd = "combine -M ProfileLikelihood --significance --pvalue -m "+str(int(mbb))+" "+yield_path+" -t -1 --expectSignal=1"

      try:
        file_path_syst = MH_dir_SYST+"/higgsCombineTest.Asymptotic.mA"+str(int(mbb))+".root"
	file_path_nosyst = MH_dir_NOSYST+"/higgsCombineTest.Asymptotic.mA"+str(int(mbb))+".root"
        if run_combine == 1:
	  # combine with Systematics
          os.system(str(combine_cmd_sys))
          cp_cmd_sys = "mv higgsCombineTest.Asymptotic.mH"+str(int(mbb))+".root "+file_path_syst
          os.system(str(cp_cmd_sys))

	  # combine without systematics
	  os.system(str(combine_cmd_nosys))
          cp_cmd_nosys = "mv higgsCombineTest.Asymptotic.mH"+str(int(mbb))+".root "+file_path_nosyst
          os.system(str(cp_cmd_nosys))

        fList_sys = TFile(str(file_path_syst)) 
        mytree_sys  = fList_sys.Get("limit")
        #for entry in mytree:
        mytree_sys.GetEntry(2);

	print "Expected Limit with syst (",(i-1)*numDirs+(j-1) , ", " , int(mbb) , ", " , int(mllbb),") = ", mytree_sys.limit
	limit=mytree_sys.limit
        limitGev2_sys=mytree_sys.limit/(2*dmbb*2*dmllbb)

	fList_sys.Close()


        fList_nosys = TFile(str(file_path_nosyst))
        mytree_nosys  = fList_nosys.Get("limit")
        #for entry in mytree:
        mytree_nosys.GetEntry(2);

        print "Expected Limit no syst (",(i-1)*numDirs+(j-1) , ", " , int(mbb) , ", " , int(mllbb),") = ", mytree_nosys.limit
        limit_nosys=mytree_nosys.limit
        limitGev2_nosys=mytree_nosys.limit/(2*dmbb*2*dmllbb)

	fList_nosys.Close()

	n+=1
        myTGraph_limit.SetPoint(n, mbb, mllbb, limitGev2_sys/limitGev2_nosys)
	print "ppppppppp",limitGev2_sys/limitGev2_nosys,"ppppppppp"
      except:
        print 'no background events'
    mbb+=step_mbb

    print '#############################################################'
    print 'mllbb:', mllbb, 'mbb:', mbb, 'myTGraph size', myTGraph.GetN()
    print '#############################################################'

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

#C=TCanvas("C","C",2000,1000)
#C.Divide(2)
#C.cd(1)
#myTGraph.Draw("CONT")
#C.cd(2)
#myTGraph.Draw("surf1")
#C.Print("Exp_Limit_allBkg.png","png")
#C.Print("Exp_Limit_allBkg.C","cxx")

#myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)

print 'M value :', m

C=TCanvas("C","C",1800,1000)
ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetOptStat(0)


gPad.SetLogz()
gPad.SetRightMargin(0.2)
gPad.SetLeftMargin(0.2)
gPad.SetBottomMargin(0.2)
myTGraph_limit.GetHistogram().Draw("colz")
#gPad.Update()

#myTGraph_limit.GetHistogram().GetXaxis().SetLimits(0,1000)
#myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)

#myTGraph_limit.GetHistogram().SetMargin(0.0)
myTGraph_limit.GetHistogram().GetXaxis().SetTitle("M_{bb} (GeV)")
myTGraph_limit.GetHistogram().GetXaxis().SetTitleSize(0.07)
myTGraph_limit.GetHistogram().GetXaxis().SetTitleOffset(1.1)
myTGraph_limit.GetHistogram().GetYaxis().SetTitle("M_{Zbb} (GeV)")
myTGraph_limit.GetHistogram().GetYaxis().SetTitleSize(0.07)
myTGraph_limit.GetHistogram().GetYaxis().SetTitleOffset(1.1)
myTGraph_limit.GetHistogram().SetMinimum(10)
#myTGraph_limit.GetHistogram().GetXaxis().SetRangeUser(0,1000)
#myTGraph_limit.GetHistogram().GetYaxis().SetRangeUser(0,1000)
myTGraph_limit.GetHistogram().SetTitle("Expected Exclusion on #sigma")

gPad.Modified()
gPad.Update()

C.Print("Exp_Eff_BW_allBkg_colz_final.png","png")

### FIN ###
###########
