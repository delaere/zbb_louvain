from ROOT import *
gStyle.SetPalette(1)

#InputFile = "Mu_DATA"
#InputFile = "Mu_MC"
#InputFile = "Ttbar_Mu_MC"
#InputFile = "ZZ_Mu_MC"

#InputFile = "El_DATA"
#InputFile = "El_MC"
#InputFile = "Ttbar_El_MC"
#InputFile = "ZZ_El_MC"

##InputFile = "ZHbb_El_MC"
##InputFile = "ZHbb_Mu_MC"


def mergeOneSample(InputFile = "Mu_DATA"):
  MEName = "ME_zbb_" + InputFile + ".root"
  
  
  #foutput = TFile("File_rdsME_" + MEName, "new")
  
  f        = TFile(MEName) 
  
  origTree  = f.Get("tree2")
  #cutme = "sqrt((E_l1+E_l2)**2-(Pt_l1*TMath::Cos(phi_l1)+(Pt_l2*TMath::Cos(phi_l2)))**2-(Pt_l1*TMath::Sin(phi_l1)+(Pt_l2*TMath::Sin(phi_l2)))**2-(Pt_l1*sinh(Eta_l1)+(Pt_l2*sinh(Eta_l2)))**2)"
  cutme = "Inv_Mass_lept"
  
  #exclude by hand conflicting runs in mumu data to get perfect matching
  #for testing purposes
  #conflictrunsRDS = " eventSelectionrun !=172400 && eventSelectionrun != 165993 && eventSelectionrun != 173692 "
  #conflictrunsMEM = " runNumber !=172400 && runNumber != 165993 && runNumber != 173692"
  
  conflictrunsRDS = " 1==1 "
  conflictrunsMEM = " 1==1 "
  
  memTree = origTree.CopyTree(cutme+">0 && "+cutme+"< 10000000 && " + conflictrunsMEM)
  
  
  file_data  = TFile("File_rds_zbb_" + InputFile + ".root")
  ws_data    = file_data.Get("ws")
  rdsZbb_data = ws_data.data("rds_zbb")
  
  eventSelectionrun   = ws_data.var("eventSelectionrun")
  eventSelectionevent = ws_data.var("eventSelectionevent")
  #jetmetMET = ws_data.var("jetmetMET")
  
  
  runNumber   = RooFormulaVar("runNumber",  "runNumber",  "eventSelectionrun",  RooArgList(eventSelectionrun))
  eventNumber = RooFormulaVar("eventNumber","eventNumber","eventSelectionevent",RooArgList(eventSelectionevent))
  #MET = RooFormulaVar("MET","MET","jetmetMET",RooArgList(jetmetMET))
  
  
  rdsZbb_data.addColumn(runNumber)
  rdsZbb_data.addColumn(eventNumber)
  #rdsZbb_data.addColumn(MET)
 
  #eventSelectionZbbM = ws_data.var("eventSelectionZbbM")
  #MeT = RooFormulaVar("MeT","MeT","eventSelectionZbbM",RooArgList(eventSelectionZbbM))
  #rdsZbb_data.addColumn(MeT)
  #ws_data.Print()
  
  
  rdsTree  = rdsZbb_data.tree()
  
  print "rdsTree = ", rdsTree
  print "memTree = ", memTree
  
  
  isMuChannel = false
  if InputFile.find("Mu_") != -1 and InputFile.find("El_") != -1:
    print "InputFile name cannot contain both <<Mu_>> and <<El_>>"
    return
  elif InputFile.find("Mu_") != -1 :
    print "running MuMu channel"
    isMuChannel = true
    sanitycut = " eventSelectionbestzmassMu > 0.01 "
  elif InputFile.find("El_") != -1:
    print "running over ElEl channel"
    sanitycut = " eventSelectionbestzmassEl > 0.01 "
  else:
    print "InputFile name must contain <<Mu_>> or <<El_>>"
    return
  
  
  sanitycut += " && " + conflictrunsRDS
  #rds_12 = rdsZbb_data.reduce("rc_eventSelection_9==1")
  rds_12 = rdsZbb_data.reduce("rc_eventSelection_12==1 && " + sanitycut)
  


  #ws_reduced = RooWorkspace("ws","workspace")
  #getattr(ws_reduced,'import')(rds_12)
  #jetmetMET = ws_reduced.var("jetmetMET")
  #MET = RooFormulaVar("MET","MET","jetmetMET",RooArgList(jetmetMET))
  #rds_12.addColumn(MET)
  
  print "rds_12.numEntries() = ", rds_12.numEntries()
  print "memTree.GetEntries() = ", memTree.GetEntries()
  print "origTree.GetEntries() = ", origTree.GetEntries()
  
  rdsTree_12 = rds_12.tree()
  
  
  memTree.BuildIndex("runNumber","eventNumber")
  rdsTree_12.BuildIndex("runNumber","eventNumber")
  
  memTree.AddFriend(rdsTree_12)
  
  
  
  C=TCanvas()
  C.Divide(2,2)
  
  h2= TH2F("h2","h2",1000, 0, 160, 1000, 0, 160)
  
  C.cd(1)
  rdsTree_12.Draw("jetmetMET")
  #memTree.Draw("eventSelectiondijetdR")
  C.cd(2)
  memTree.Draw("MeT")
  #memTree.Draw("runNumber:eventSelectionrun","","contz")
  #C.cd(2)
  #memTree.Draw("Met")#Wtt
  C.cd(3)
  memTree.Draw("MeT:jetmetMET>>h2","","contz")#Wtt:Wtt","","contz")#Wgg_i2
  #memTree.Draw("MET")
  C.cd(4)
  memTree.Draw("jetmetMET")
  #memTree.Draw("Eta_j1:jetmetjet1eta","","contz")
  
  #print "memTreeScan"
  #memTree.Scan("runNumber:eventNumber")
  #print "\n"
  
  #print "rdsTreeScan"
  #rdsTree_12.Scan("runNumber:eventNumber")
  #print "\n"
  
  
  
  myRDSRAS = rds_12.get()
  myWttRRV = RooRealVar("Wtt", "Wtt", 20, 30)
  myMeTRRV = RooRealVar("MeT", "MeT", 0, 200)#met to check the matching
  #myMETRRV = RooRealVar("MET", "jetmetMET", 0, 200)
  myRDSRAS.add(myWttRRV)
  myRDSRAS.add(myMeTRRV)
  #myRDSRAS.add(myMETRRV)
  raw_input("Press Enter to continue...")

  myRDS_sum = RooDataSet("rds_zbb", "rds_zbb", memTree, myRDSRAS)
  
  ws_output = RooWorkspace("ws","workspace")
  getattr(ws_output,'import')(myRDS_sum)
  ws_output.writeToFile("File_rdsME_" +InputFile + ".root")
  
  #ws_data.writeToFile("File_rdsME_" + MEName)
  
  #foutput.cd()
  #memTree.Write("MEllbbTree")
  
  #reduced workspace
  #ws_reduced = RooWorkspace("ws","workspace")
  #getattr(ws_reduced,'import')(rds_12)
  #eventSelectionZbbM = ws_reduced.var("eventSelectionZbbM")
  #MeT = RooFormulaVar("MeT","MeT","eventSelectionZbbM",RooArgList(eventSelectionZbbM))
  #rds_12.addColumn(MeT)
  #ws_reduced.Print()
  
  #ws_reduced.writeToFile("File_rdsME_" + MEName) 
 
#mergeOneSample(InputFile = "Mu_DATA")
#mergeOneSample(InputFile = "Mu_MC")
mergeOneSample(InputFile = "Ttbar_Mu_MC")
#mergeOneSample(InputFile = "ZZ_Mu_MC")
