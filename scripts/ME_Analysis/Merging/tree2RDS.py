from ROOT import *
def tree2RDSoneSample(InputFile = "Mu_DATA"):

  print "inputfile", InputFile  
  f  = TFile("testsMergeRDSnoWS120721/Tree_rdsME_" + InputFile + ".root")
  t  = f.Get("rds_zbb")

  file_data  = TFile("File_ws_ZZ_Mu_MC.root")
  ws_data    = file_data.Get("ws")
  rdsZbb_data = ws_data.data("rds_zbb")
  myRDSRAS = rdsZbb_data.get()
#Sensible ranges
#  myWttRRV = RooRealVar("Wtt", "Wtt", 20, 30)
#  myWggRRV = RooRealVar("Wgg", "Wgg", 18, 25)
#  myWqqRRV = RooRealVar("Wqq", "Wqq", 18, 25)
#  myWtwbRRV = RooRealVar("Wtwb", "Wtwb", 20, 30)
#  myWzz3RRV = RooRealVar("Wzz3", "Wzz3", 9, 17)
#  myWzz0RRV = RooRealVar("Wzz0", "Wzz0", 16, 28)
#  myWhi3RRV = RooRealVar("Whi3", "Whi3", 10, 23)
#  myWhi0RRV = RooRealVar("Whi0", "Whi0", 18, 33)


#big range so we don't loose events out of range
  myWttRRV = RooRealVar("Wtt", "Wtt", -10, 300)
  myWggRRV = RooRealVar("Wgg", "Wgg", -10, 300)
  myWqqRRV = RooRealVar("Wqq", "Wqq", -10, 300)
  myWtwbRRV = RooRealVar("Wtwb", "Wtwb", -10, 300)
  myWzz3RRV = RooRealVar("Wzz3", "Wzz3", -10, 300)
  myWzz0RRV = RooRealVar("Wzz0", "Wzz0", -10, 300)
  myWhi3RRV = RooRealVar("Whi3", "Whi3", -10, 300)
  myWhi0RRV = RooRealVar("Whi0", "Whi0", -10, 300)
  myMeTRRV = RooRealVar("MeT", "MeT", 0, 600)#met to check the matching
  mymlphiggsvszbbRRV = RooRealVar("mlphiggsvszbb", "mlphiggsvszbb", -10000, 600)#met to check the matching
  mymlphiggsvszzRRV = RooRealVar("mlphiggsvszz", "mlphiggsvszz", -10000, 600)#met to check the matching
  mymlphiggsvsttRRV = RooRealVar("mlphiggsvstt", "mlphiggsvstt", -10000, 600)#met to check the matching
  mymlphiggsvsbkgRRV = RooRealVar("mlphiggsvsbkg", "mlphiggsvsbkg", -10000, 600)#met to check the matching
  mymlphiggsvsbkgfulllRRV = RooRealVar("mlphiggsvsbkg_fulll", "mlphiggsvsbkg_fulll", -10000, 600)#met to check the matching
  mymlpZbbvsTTRRV = RooRealVar("mlpZbbvsTT", "mlpZbbvsTT", -10000, 600)#met to check the matching
  mymlpZbbvsTTtightRRV = RooRealVar("mlpZbbvsTTtight", "mlpZbbvsTTtight", -10000, 600)#met to check the matching
  mymlpZbbvsTT_tight_Wmet_RRV = RooRealVar("mlpZbbvsTT_tight_Wmet", "mlpZbbvsTT_tight_Wmet", -10000, 600)#met to check the matching
  mymlpzbbvstt_multi_EE_tight_RRV = RooRealVar("mlpzbbvstt_multi_EE_tight", "mlpzbbvstt_multi_EE_tight", -10000, 600)#met to check the matching
  mymlpzbbttmmll_MeTtest_mll_met_RRV = RooRealVar("mlpzbbttmmll_MeTtest_mll_met","mlpzbbttmmll_MeTtest_mll_met",-10000,600)
  mymlpzbbttmlltest_mll_RRV = RooRealVar("mlpzbbttmlltest_mll","mlpzbbttmlltest_mll",-10000,600)
#
#
  myRDSRAS.add(myWttRRV)
  myRDSRAS.add(myWggRRV)
  myRDSRAS.add(myWqqRRV)
  myRDSRAS.add(myWzz3RRV)
  myRDSRAS.add(myWzz0RRV)
  myRDSRAS.add(myWhi3RRV)
  myRDSRAS.add(myWhi0RRV)
  myRDSRAS.add(myMeTRRV)
  myRDSRAS.add(mymlphiggsvszbbRRV)
  myRDSRAS.add(mymlphiggsvszzRRV)
  myRDSRAS.add(mymlphiggsvsttRRV)
  myRDSRAS.add(mymlphiggsvsbkgRRV)
  myRDSRAS.add(mymlphiggsvsbkgfulllRRV)
  myRDSRAS.add(mymlpzbbttmlltest_mll_RRV)
  myRDSRAS.add(mymlpZbbvsTTRRV)
  myRDSRAS.add(mymlpZbbvsTTtightRRV)
  myRDSRAS.add(mymlpZbbvsTT_tight_Wmet_RRV)
  myRDSRAS.add(mymlpzbbvstt_multi_EE_tight_RRV)  
  myRDSRAS.add(mymlpzbbttmmll_MeTtest_mll_met_RRV)
  if "Mu" in InputFile:
    myRDSRAS.add(myWtwbRRV)
    myRDSRAS.add(myWzz3RRV)
#  
#  

  fout = TFile("RDS_rdsME_" +InputFile + ".root", "RECREATE")
  myRDS_sum = RooDataSet("rds_zbb", "rds_zbb", t, myRDSRAS)
  
  myRDS_sum.Write()

  


tree2RDSoneSample(InputFile = "MuA_DATA")
tree2RDSoneSample(InputFile = "MuB_DATA")
tree2RDSoneSample(InputFile = "Mu_MC")
tree2RDSoneSample(InputFile = "TT_Mu_MC")
tree2RDSoneSample(InputFile = "ZZ_Mu_MC")
tree2RDSoneSample(InputFile = "ZH125_Mu_MC")

tree2RDSoneSample(InputFile = "ElA_DATA")
tree2RDSoneSample(InputFile = "ElB_DATA")
tree2RDSoneSample(InputFile = "El_MC")
tree2RDSoneSample(InputFile = "TT_El_MC")
tree2RDSoneSample(InputFile = "ZZ_El_MC")
tree2RDSoneSample(InputFile = "ZH125_El_MC")

