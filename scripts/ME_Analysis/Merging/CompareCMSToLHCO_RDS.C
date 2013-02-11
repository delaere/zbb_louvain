/*
Macro to check if results from CMSToLHCO, and RDS (from makRDS) are compatible
cutRDS is the string of the selection step that matches the selection implemented in CMSToLHCO
It currently checks the number of events after the selection plus several variables:
ptj1,j2 CSVdiscj1j,2, etaj1,j2, bbM, llM, MET, METphi. To add more variables add 1 line calling to Compare2Histos following as for the already implemented samples
If all the checks are successful it will print in the end allOK=1. If not allOK=WR. Previous lines give you hints about which check failed
Currently the checks for jet and lepton variables fail for ZZ samples. I believe the reason is that is the following:
-mumu channel searchs for Z->mumu candidates, and elel for Z->elel candidates
-if 1 candidate is found the event passes the CMSToLHCO/RDS selection.
-However if the best candidate in the mumu (elel) channel is a Z->elel (Z->mumu) then that event will be removed afterwards. This seems to happen only for ~1/1000 ZZ events.
-For CMSToLHCO those events are keep the kinematics of the Z candidate of the considered channel, while for RDS the corresponding variables are set to zero causing the mismatch
On a different matter notice also that if the jetmetMETsignificance variables is EXACTLY zero. It means that the event doesn't pass the jetmetMETsignificance < x requirement
Usage:
First argument "tree1" from CMSToLHCO, second argument RDS
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ElA_DATA_CSV2011Sel_0.root", "File_rds_zbb_ElA_DATA.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ElB_DATA_CSV2011Sel_0.root", "File_rds_zbb_ElB_DATA.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_El_MC_CSV2011Sel_0.root", "File_rds_zbb_El_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_MuA_DATA_CSV2011Sel_0.root", "File_rds_zbb_MuA_DATA.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_MuB_DATA_CSV2011Sel_0.root", "File_rds_zbb_MuB_DATA.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_Mu_MC_CSV2011Sel_0.root", "File_rds_zbb_Mu_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_TT_El_MC_CSV2011Sel_0.root", "File_rds_zbb_TT_El_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_TT_Mu_MC_CSV2011Sel_0.root", "File_rds_zbb_TT_Mu_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZH115_El_MC_CSV2011Sel_0.root", "File_rds_zbb_ZH115_El_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZH115_Mu_MC_CSV2011Sel_0.root", "File_rds_zbb_ZH115_Mu_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZH120_El_MC_CSV2011Sel_0.root", "File_rds_zbb_ZH120_El_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZH120_Mu_MC_CSV2011Sel_0.root", "File_rds_zbb_ZH120_Mu_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZH125_El_MC_CSV2011Sel_0.root", "File_rds_zbb_ZH125_El_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZH125_Mu_MC_CSV2011Sel_0.root", "File_rds_zbb_ZH125_Mu_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZH130_El_MC_CSV2011Sel_0.root", "File_rds_zbb_ZH130_El_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZH130_Mu_MC_CSV2011Sel_0.root", "File_rds_zbb_ZH130_Mu_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZH135_El_MC_CSV2011Sel_0.root", "File_rds_zbb_ZH135_El_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZH135_Mu_MC_CSV2011Sel_0.root", "File_rds_zbb_ZH135_Mu_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZZ_El_MC_CSV2011Sel_0.root", "File_rds_zbb_ZZ_El_MC.root")'
root -q -b CompareCMSToLHCO_RDS.C'("outCMStoLHCO_ZZ_Mu_MC_CSV2011Sel_0.root", "File_rds_zbb_ZZ_Mu_MC.root")'

*/


TFile* fileRDS = 0;
TFile* fileCMStoLHCO = 0;

TTree* treeRDS = 0;
TTree* treeCMStoLHCO = 0;
TString cutRDS = "rc_eventSelection_10_idx == 1 && jetmetMETsignificance < 10 && jetmetMETsignificance != 0";

void CompareCMSToLHCO_RDS(TString nameCMStoLHCO, TString nameRDS) {
  bool verbose = true;

  fileRDS = TFile::Open(nameRDS);
  RooAbsData* rad = (RooDataSet*)fileRDS->Get("rds_zbb");
  treeRDS = rad->tree();
  //treeRDS->Draw("eventSelectionevent");
  
  fileCMStoLHCO = TFile::Open(nameCMStoLHCO);
  treeCMStoLHCO = (TTree*)fileCMStoLHCO->Get("tree1");
  //treeCMStoLHCO->Draw("Met");

  TString channel = "";
  if (TString(fileRDS->GetName()).Contains("_El")) channel = "Ele";
  else if (TString(fileRDS->GetName()).Contains("_Mu")) channel = "Mu";
  else {std::cout << "could not determine channel (Ele or Mu)" << std::endl; return;}
  std::cout << "channel=" << channel << std::endl;
  
  TString muORel = (channel == "Ele")? "el": "mu";

  //First check number of entries both selections
  TH1F* hCMSevent = new TH1F("hCMSevent", "", 1, 0, 1);
  TH1F* hRDSevent = new TH1F("hRDSevent", "", 1, 0, 1);
  treeCMStoLHCO->Draw("eventNumber>>hCMSevent");
  treeRDS->Draw("eventSelectionevent>>hRDSevent", cutRDS);

  int nEventsCMS = hCMSevent->GetEntries();
  int nEventsRDS = hRDSevent->GetEntries();
  std::cout << "nEventsCMS=" << nEventsCMS << " nEventsRDS=" << nEventsRDS << std::endl;
  if (nEventsCMS == nEventsRDS) std::cout << "entriescheck =OK" << std::endl;
  else std::cout << "entriescheck =WRONG!!!" << std::endl;

  delete hCMSevent;
  delete hRDSevent;

  bool iseq = false;
  bool allOK = true;
  TString id = "";

  id="ptj1"; iseq=Compare2Histos(300, 0, 300, "Pt_j1*(Pt_j1>Pt_j2)+Pt_j2*(Pt_j2>Pt_j1)", "jetmetbjet1pt", verbose, id); if (!iseq) allOK=false; cout<<"id="<<id<<":"<<iseq<<endl;

  id="etaj1"; iseq=Compare2Histos(100, -3.0, 3.0, "Eta_j1*(Pt_j1>Pt_j2)+Eta_j2*(Pt_j2>Pt_j1)", "jetmetbjet1etapm", verbose, id); if (!iseq) allOK=false; cout<<"id="<<id<<":"<<iseq<<endl;

  id="CSVj1"; iseq=Compare2Histos(100, -0.1, 1.1, "btag_j1*(Pt_j1>Pt_j2)+btag_j2*(Pt_j2>Pt_j1)", "jetmetbjet1CSVdisc", verbose, id); if (!iseq) allOK=false; cout<<"id="<<id<<":"<<iseq<<endl;

  id="ptj2"; iseq=Compare2Histos(300, 0, 300, "Pt_j2*(Pt_j1>Pt_j2)+Pt_j1*(Pt_j2>Pt_j1)", "jetmetbjet2pt", verbose, id); if (!iseq) allOK=false; cout<<"id="<<id<<":"<<iseq<<endl;

  id="etaj2"; iseq=Compare2Histos(100, -3.0, 3.0, "Eta_j2*(Pt_j1>Pt_j2)+Eta_j1*(Pt_j2>Pt_j1)", "jetmetbjet2etapm", verbose, id); if (!iseq) allOK=false; cout<<"id="<<id<<":"<<iseq<<endl;

  id="CSVj2"; iseq=Compare2Histos(100, -0.1, 0.1, "btag_j2*(Pt_j1>Pt_j2)+btag_j1*(Pt_j2>Pt_j1)", "jetmetbjet2CSVdisc", verbose, id); if (!iseq) allOK=false; cout<<"id="<<id<<":"<<iseq<<endl;
  
  id="bbM"; iseq=Compare2Histos(400, 0, 400, "bbM", "eventSelectiondijetM", verbose, id); if (!iseq) allOK=false; cout<<"id="<<id<<":"<<iseq<<endl;

  id="MET"; iseq=Compare2Histos(200, 0, 200, "Met", "jetmetMET", verbose, id); if (!iseq) allOK=false; cout<<"id="<<id<<":"<<iseq<<endl;

  id="METphi"; iseq=Compare2Histos(150, -3.2, 3.2, "Met_phi", "jetmetMETphi", verbose, id); if (!iseq) allOK=false; cout<<"id="<<id<<":"<<iseq<<endl;

  id="llM"; iseq=Compare2Histos(250, 0, 250, "llM", "eventSelectionbestzmass"+channel, verbose, id); if (!iseq) allOK=false; cout<<"id="<<id<<":"<<iseq<<endl;
  
  id="Pt_l1"; iseq=Compare2Histos(250, 0, 250, "Pt_l1", "eventSelection"+muORel+"1pt", verbose, id); if (!iseq) allOK=false; cout<<"id="<<id<<":"<<iseq<<endl;
  
  std::cout << "allOK=" << allOK << std::endl;
  
  
  
  
}

bool Compare2Histos(int nbins, double xmin, double xmax, TString varCMS, TString varRDS, bool verbose=false, TString varid = "") {
  TH1F* hCMS = new TH1F("hCMS"+varid, "", nbins, xmin, xmax);
  TH1F* hRDS = new TH1F("hRDS"+varid, "", nbins, xmin, xmax);
  
  treeCMStoLHCO->Draw(varCMS+">>hCMS"+varid);
  treeRDS->Draw(varRDS+">>hRDS"+varid, cutRDS);
  
  bool out=IsHistoEqual(hCMS, hRDS, verbose);
 
  delete hCMS;
  delete hRDS;
 
  return out;  
  
}


bool IsHistoEqual(TH1F* a, TH1F* b, bool verbose = false) {
  if (!a) {
    std::cout << "isHistoEqual: first histo doesn't exist" << std::endl;
    return false;
  }

  if (!b) {
    std::cout << "isHistoEqual: second histo doesn't exist" << std::endl;
    return false;
  }
 
  if (a->GetNbinsX() != b->GetNbinsX()) {
    if (verbose) {
      std::cout << "GetNbins(" << a->GetName() << ")=" << a->GetNbinsX() << " != "
                << "GetNbins(" << b->GetName() << ")=" << b->GetNbinsX()
                << std::endl;
    }
    return false;
  }
  TAxis* xa = a->GetXaxis();
  TAxis* xb = b->GetXaxis();
  
  if (xa->GetXmin() != xb->GetXmin()) {
    if (verbose) {
      std::cout << "GetXmin(" << a->GetName() << ")=" << xa->GetXmin() << " != "
                << "GetXmin(" << b->GetName() << ")=" << xb->GetXmin()
                << std::endl;
    }
    return false;
  }

  if (xa->GetXmax() != xb->GetXmax()) {
    if (verbose) {
      std::cout << "GetXmax(" << a->GetName() << ")=" << xa->GetXmax() << " != "
                << "GetXmax(" << b->GetName() << ")=" << xb->GetXmax()
                << std::endl;
    }
    return false;
  }
  
  for (unsigned int i = 0; i <= a->GetNbinsX() + 1; i++) {
    if (a->GetBinContent(i) != b->GetBinContent(i)) {
      if (verbose) {
        std::cout << "GetBinContent(" << a->GetName() << ", " << i << ")=" << a->GetBinContent(i) << " != "
                  << "GetBinContent(" << b->GetName() << ", " << i << ")=" << b->GetBinContent(i)
                  << std::endl;
      }
      return false;
    }
  }
  
  return true;
}
