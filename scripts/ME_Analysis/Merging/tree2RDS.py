
from ROOT import *
from UserCode.zbb_louvain.globalLists import dirTree2, dirRDS, PlotForCLsRaw
RooAbsData.setDefaultStorageType(RooAbsData.Tree)

listNNs = PlotForCLsRaw
RAS = {}

def tree2RDSoneSample(InputFile = "Mu_DATA"):

  print "inputfile", InputFile

  file_data = TFile("/nfs/user/acaudron/RDS537/File_rds_zbb_ZZ_Mu_MC.root")
  ws_zbb = file_data.Get("ws_ras")
  myRDSRAS = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())

  #big range so we don't loose events out of range
  myWttRRV = RooRealVar("Wtt", "Wtt", -10, 300)
  myWggRRV = RooRealVar("Wgg", "Wgg", -10, 300)
  myWqqRRV = RooRealVar("Wqq", "Wqq", -10, 300)
  myWtwbRRV = RooRealVar("Wtwb", "Wtwb", -10, 3300)
  myWzz3RRV = RooRealVar("Wzz3", "Wzz3", -10, 300)
  myWzz0RRV = RooRealVar("Wzz0", "Wzz0", -10, 300)
  mybdtRRV = RooRealVar("bdt", "bdt", -10, 300)
  for m in ["110","115","120","125","130","135","140","145","150"] :
    RAS["hi0"+m]=RooRealVar("Whi0_"+m, "Whi0_"+m, -10, 300)
    RAS["hi3"+m]=RooRealVar("Whi3_"+m, "Whi3_"+m, -10, 300)
    for nn in listNNs : RAS[nn+m] = RooRealVar(nn+"_"+m, nn+"_"+m, -10000, 600)
  myjetmetbjetMinCSVdiscRRV = RooRealVar("jetmetbjetMinCSVdisc","jetmetbjetMinCSVdisc",-10, 10)
  myjetmetbjetMaxCSVdiscRRV = RooRealVar("jetmetbjetMaxCSVdisc","jetmetbjetMaxCSVdisc",-10, 10)
  myjetmetbjetProdCSVdiscRRV = RooRealVar("jetmetbjetProdCSVdisc","jetmetbjetProdCSVdisc",-10, 10)

  myMeTRRV = RooRealVar("MeT", "MeT", 0, 600)#met to check the matching

  mymlpZbbvsTT_MM = RooRealVar("mlpZbbvsTT_MM", "mlpZbbvsTT_MM", -10000, 600)
  mymlpZbbvsTT_MM_N = RooRealVar("mlpZbbvsTT_MM_N", "mlpZbbvsTT_MM_N", -10000, 600)
  mymlpZbbvsTT_ML = RooRealVar("mlpZbbvsTT_ML", "mlpZbbvsTT_ML", -10000, 600)
  mymlpZbbvsTT_mu_MM = RooRealVar("mlpZbbvsTT_mu_MM", "mlpZbbvsTT_mu_MM", -10000, 600)
  mymlpZbbvsTT_mu_MM_N = RooRealVar("mlpZbbvsTT_mu_MM_N", "mlpZbbvsTT_mu_MM_N", -10000, 600)
  mymlpZbbvsTT_mu_ML = RooRealVar("mlpZbbvsTT_mu_ML", "mlpZbbvsTT_mu_ML", -10000, 600)
  mymlpDYvsTT_2012 = RooRealVar("mlpDYvsTT_2012", "mlpDYvsTT_2012", -10000, 600)
  

  myRDSRAS.add(myWttRRV)
  myRDSRAS.add(myWggRRV)
  myRDSRAS.add(myWqqRRV)
  myRDSRAS.add(myWzz3RRV)
  myRDSRAS.add(myWzz0RRV)
  myRDSRAS.add(myMeTRRV)
  myRDSRAS.add(mybdtRRV)
  myRDSRAS.add(myjetmetbjetMinCSVdiscRRV)
  myRDSRAS.add(myjetmetbjetMaxCSVdiscRRV)
  myRDSRAS.add(myjetmetbjetProdCSVdiscRRV)
     
  myRDSRAS.add(mymlpZbbvsTT_MM)
  myRDSRAS.add(mymlpZbbvsTT_MM_N)
  myRDSRAS.add(mymlpZbbvsTT_ML)
  myRDSRAS.add(mymlpZbbvsTT_mu_MM)
  myRDSRAS.add(mymlpZbbvsTT_mu_MM_N)
  myRDSRAS.add(mymlpZbbvsTT_mu_ML)
  myRDSRAS.add(mymlpDYvsTT_2012)

  for n in RAS : myRDSRAS.add(RAS[n])
  
  f  = TFile(dirTree2+"Tree_rdsME_"+InputFile+".root","READ")
  t  = f.Get("rds_zbb")
  myRDS_sum = RooDataSet("rds_zbb", "rds_zbb", t, myRDSRAS)

  ras_zbb = myRDS_sum.get()
  ws_ras = RooWorkspace("ws_ras","workspace_ras")
  getattr(ws_ras,'import')(ras_zbb)

  ws_ras.writeToFile(dirTree2+"RDS_rdsME_"+InputFile+".root")
  gDirectory.Add(ws_ras)

  fout=TFile(dirTree2+"RDS_rdsME_"+InputFile+".root","UPDATE")
  tree_zbb = myRDS_sum.tree()
  tree_zbb.Write()
  fout.Close()


list=[
      "DoubleEle_DataA",
      "DoubleEle_DataA06aug",
      "DoubleEle_DataB",
      "DoubleEle_DataC-v1",
      "DoubleEle_DataC-v2",
      "DoubleEle_DataD",
      "DoubleMu_DataA",
      "DoubleMu_DataA06aug",
      "DoubleMu_DataB",
      "DoubleMu_DataC-v1",
      "DoubleMu_DataC-v2",
      "DoubleMu_DataD",
      "DY_Mu_MC",
      "DY_El_MC",
      "TT_Mu_MC",
      "TT_El_MC",
      "ZZ_Mu_MC",
      "ZZ_El_MC",
      "ZH110_Mu_MC",
      "ZH110_El_MC",
      "ZH115_Mu_MC",
      "ZH115_El_MC",
      "ZH120_Mu_MC",
      "ZH120_El_MC",
      "ZH125_Mu_MC",
      "ZH125_El_MC",
      "ZH130_Mu_MC",
      "ZH130_El_MC",
      "ZH135_Mu_MC",
      "ZH135_El_MC",
      "ZH140_Mu_MC",
      "ZH140_El_MC",
      "ZH145_Mu_MC",
      "ZH145_El_MC",
      "ZH150_Mu_MC",
      "ZH150_El_MC",
      "TT-FullLept_Mu_MC",
      "TT-FullLept_El_MC",
      "Zbb_Mu_MC",
      "Zbb_El_MC",
      "DY1j_Mu_MC",
      "DY1j_El_MC",
      "DY2j_Mu_MC",
      "DY2j_El_MC",
      "DY3j_Mu_MC",
      "DY3j_El_MC",
      #"DY4j_Mu_MC",
      #"DY4j_El_MC",
      "DY50-70_Mu_MC",
      "DY50-70_El_MC",
      "DY70-100_Mu_MC",
      "DY70-100_El_MC",
      "DY100_Mu_MC",
      "DY100_El_MC",
      "DY180_Mu_MC",
      "DY180_El_MC",
      ]


for s in list : 
  tree2RDSoneSample(InputFile = s)

