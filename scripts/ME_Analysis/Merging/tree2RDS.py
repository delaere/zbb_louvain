from ROOT import *
def tree2RDSoneSample(InputFile = "Mu_DATA"):

  
  f  = TFile("Tree_rdsME_" + InputFile + ".root")
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
  myWttRRV = RooRealVar("Wtt", "Wtt", 0, 300)
  myWggRRV = RooRealVar("Wgg", "Wgg", 0, 300)
  myWqqRRV = RooRealVar("Wqq", "Wqq", 0, 300)
  myWtwbRRV = RooRealVar("Wtwb", "Wtwb", 0, 300)
  myWzz3RRV = RooRealVar("Wzz3", "Wzz3", 0, 300)
  myWzz0RRV = RooRealVar("Wzz0", "Wzz0", 0, 300)
  myWhi3RRV = RooRealVar("Whi3", "Whi3", 0, 300)
  myWhi0RRV = RooRealVar("Whi0", "Whi0", 0, 300)
  myMeTRRV = RooRealVar("MeT", "MeT", 0, 600)#met to check the matching
  mymlpZH125vsZbbRRV = RooRealVar("mlpZH125vsZbb", "mlpZH125vsZbb", -10000, 600)#met to check the matching
  mymlpZbbvsTTRRV = RooRealVar("mlpZbbvsTT", "mlpZbbvsTT", -10000, 600)#met to check the matching
  mymlpZbbvsTTtightRRV = RooRealVar("mlpZbbvsTTtight", "mlpZbbvsTTtight", -10000, 600)#met to check the matching

#
#
  myRDSRAS.add(myWttRRV)
  myRDSRAS.add(myWggRRV)
  myRDSRAS.add(myWqqRRV)
  myRDSRAS.add(myWzz0RRV)
  myRDSRAS.add(myWhi3RRV)
  myRDSRAS.add(myWhi0RRV)
  myRDSRAS.add(myMeTRRV)
  myRDSRAS.add(mymlpZH125vsZbbRRV)
  myRDSRAS.add(mymlpZbbvsTTRRV)
  myRDSRAS.add(mymlpZbbvsTTtightRRV)
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

