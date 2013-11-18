//Use minimal-brain-usage approach 2 merge llbb tree (frome now on
//rds_bb tree) with ME tree
// Idea is 2 create with MakeClass skeletons for rds_zbb and ME trees
//then took the list of variables and copy them 2 a), b), c) parts of the code, use some
//text editing magic to manipulate the list of variables to transform them in what you need:
// a) definition of variable (get rid of annoying vectors of chars for labels), keep
// the rest and propagate it to b) and c)
// b) throw an spell to transform the definition of variables to define branches
// c) throw an spell to transform the difinition of variables in setting the variables with
// the original values from the rds_zbb and ME trees 
//This part should be automatized if the code turns out to be useful
//
//  Author: Jesus Vizan, updated by Adrien Caudron
//  still need the update for the different mass point
      
#include "TTree.h"
#include "TFile.h"
#include "TRandom.h"
#include "TTree.h"
#include "TTree.h"
#include <algorithm>
#include "rds_zbb.C"
#include "tree2.C"
#include "TMVA/Reader.h"

using namespace TMVA;
// Include NN traine on ee
// MM: CSV Medium Medium WP
// MM_N: CSV Medium Medium WP + narrow Mll
// ML: CSV Medium Loose WP

#include "../NN/MLP_TT_vs_DY_MM_CSV_2011.cxx"
#include "MLP_TT_vs_DY_MM_N_CSV_2011.cxx"
#include "../NN/MLP_TT_vs_DY_ML_CSV_2011.cxx"

#include "../NN/MLP_TT_vs_DY_MM_CSV_2011_mm.cxx"
#include "../NN/MLP_TT_vs_DY_MM_N_CSV_2011_mm.cxx"
#include "../NN/MLP_TT_vs_DY_ML_CSV_2011_mm.cxx"

#include "../MW_Analysis/NN_AN/selectedNNs/MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20.cxx" //trained with 2012

// Include NN trained on ee-mm merged 2011
#include "MLP_Higgs_vs_DY_MM_N_CSV_2011_comb.cxx"
#include "MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb.cxx"
#include "MLP_Higgs_vs_TT_MM_N_CSV_2011_comb.cxx"
#include "MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb.cxx"
// Include NN trained on ee-mm merged 2012
#include "MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125.cxx"
#include "MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125.cxx"
#include "MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125.cxx"
#include "MLP_Higgs_vs_Bkg_ZH125_comb.cxx"
// Include NN trained on ee-mm merged 2012 : new training with Zbb and TTFullLept
#include "MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600.cxx"
#include "MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500.cxx"
#include "MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000.cxx"
#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000.cxx"

//final NN test : 1000 and 10000 it==standard bkg weights, 5000=1/3 for each bkg
#include "MLP_Higgs_vs_Bkg_ZH125_comb_1_10000.cxx"
#include "MLP_Higgs_vs_Bkg_ZH125_comb_1_5000.cxx"
#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_10000.cxx"
#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_5000.cxx"
#include "MLP_Higgs_vs_Bkg_ZH125_comb_3_5000.cxx"
#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000.cxx"
#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000.cxx"
#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000.cxx"
#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000.cxx"
#include "MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000.cxx"

//NN by jet multiplicity
//2jets
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_DY_ZH125_comb-2-4_1000_Nj2_Mbb80-150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_ZZ_ZH125_comb-2-4_750_Nj2_Mbb80-150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_TT_ZH125_comb-5-10_700_Nj2_Mbb50-200_Ptb1j40_Ptb2j25_Ptll20.cxx"
//finals
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1.cxx"

//>2jets
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR-3-9_500_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR-2-4_501_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR-2-4_500_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20.cxx"
//finals
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1.cxx"

//ML
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.cxx"

//ML ZZ
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "../MW_Analysis/NN_AN/selectedNNs/MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20.cxx"

//general include
#include <iostream>
#include <map>

//define list of NNs
int nNNs = 38+10;
std::string NNs [] = {
  //Maximum 60 chs
  "NN_Higgs125vsDY_MM_N_CSV_2011_comb",//1
  "NN_Higgs125vsZZ_MM_N_CSV_2011_comb",
  "NN_Higgs125vsTT_MM_N_CSV_2011_comb",
  "NN_Higgs125vsBKG_MM_N_CSV_2011_comb",
  "NN_Higgs125vsDY_MM_N_CSV_2012_comb_ZH125",//5
  "NN_Higgs125vsZZ_MM_N_CSV_2012_comb_ZH125",
  "NN_Higgs125vsTT_MM_N_CSV_2012_comb_ZH125",
  "NN_Higgs125vsBkgcomb",
  "NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600",
  "NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500",//10
  "NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000",
  "NN_Higgs125vsBkgcomb_2_3_2_1_1000",
  "NN_Higgs125vsBkgcomb_1_10000",
  "NN_Higgs125vsBkgcomb_1_5000",
  "NN_Higgs125vsBkgcomb_2_10000",//15
  "NN_Higgs125vsBkgcomb_2_5000",
  "NN_Higgs125vsBkgcomb_3_5000",
  "NN_Higgs125vsBkgcomb_2_3_2_10000",
  "NN_Higgs125vsBkgcomb_2_3_2_5000",
  "NN_Higgs125vsBkgcomb_2_4_10000",//20
  "NN_Higgs125vsBkgcomb_2_5_3_1_1000",
  "NN_Higgs125vsBkgcomb_3_2_10000",
  "NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520",
  "NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520",
  "NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520",//25
  "NN_Higgs125vsBkg_2jcomb_2_2_2_500_Nj2Mbb50_200Pt402520",
  "NN_Higgs125vsBkg_2jcomb_6_6_131_Nj2Mbb80_150Pt402520_3",
  "NN_Higgs125vsBkg_2jcomb_9_3_100_Nj2Mbb80_150Pt402520_8",
  "NN_Higgs125vsBkg_2jcomb_9_3_100_Nj2Mbb80_150Pt402520_21",
  "NN_Higgs125vsBkg_2jcomb_2_500_Nj2Mbb80_150Pt402520_1",//30
  "NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt",
  "NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt",
  "NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt",
  "NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_4",
  "NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_5",//35
  "NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_9",
  "NN_Higgs125vsBkg_3jcomb_9_9_300_Nj3_Mbb50_150_Pt402520_4",
  "NN_Higgs125vsBkg_3jcomb_5_600_Nj3_Mbb50_150_Pt402520_1",

  "NN_Higgs125vsDYcomb_12_120_Nj2Mbb80_150Pt402520_2",
  "NN_Higgs125vsZZcomb_2_2_1000_Nj2Mbb80_150Pt402520",//40
  "NN_Higgs125vsTTcomb_6_3_2_150_Nj2Mbb80_150Pt402520",
  "NN_Higgs125vsDYcombMbbjdRbjdRbb_12_9_6_3_210_Nj3MbbPt",
  "NN_Higgs125vsZZcombMbbjdRbjdRbb_9_100_Nj3Mbb50_150_Pt",
  "NN_Higgs125vsTTcombMbbjdRbjdRbb_2_2_600_Nj3Mbb50_150_Pt",
  "NN_Higgs125vsBkg_2jcomb_4_5000_Nj2Mbb80_150Pt402520",//45
  "NN_Higgs125vsBkg_2jcomb_4_2_500_Nj2Mbb80_150Pt402520",
  "NN_Higgs125vsBkg_3jcomb_prodCSV_5_3_1000_Nj3Mbb50_150Pt",
  "NN_Higgs125vsBkg_3jcomb_prodCSV_3_2_1000_Nj3Mbb50_150Pt",
};
int nNNsZZ = 6;
std::string NNsZZ [] = {
  "NN_ZZvsDYcomb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20",
  "NN_ZZvsDYcombMbbjdRbjdRbb_12_50_Nj3Mbb15_115Pt402520",
  "NN_ZZvsTTcomb_2_1000_Nj2Mbb45_115Pt402520",
  "NN_ZZvsTTcombMbbjdRbjdRbb_3_2_500_Nj3Mbb15_115Pt402520",
  "NN_ZZvsBkg_2jcomb_12_50_Nj2Mbb45_115Pt402520",//5
  "NN_ZZvsBkg_3jcomb_prodCSV_9_200_Nj3Mbb15_115Pt402520"
};
//------------------------------------------------------------
//Switch to turn on or of the ZbbReweight
void InitZbbReweight();
double Compute1DReweight(TH1D*, double);

bool useZbbReweight = true;
TFile* file_reweight = 0;
TH1D* hZbbReweight_dijetdR_Mu = 0;
TH1D* hZbbReweight_bestzpt_Mu = 0;
TH1D* hZbbReweight_dijetdR_El = 0;
TH1D* hZbbReweight_bestzpt_El = 0;

//for the branch address
/*Double_t        Pt_elplus;
Double_t        Pt_elminus;
Double_t        Pt_Muplus;
Double_t        Pt_Muminus;
Double_t        Phi_elplus;
Double_t        Phi_elminus;
Double_t        Phi_Muplus;
Double_t        Phi_Muminus;
Double_t        Eta_elplus;
Double_t        Eta_elminus;
Double_t        Eta_Muplus;
Double_t        Eta_Muminus;
Double_t        Eta_j1;
Double_t        Phi_j1;
Double_t        Pt_j1;
Double_t        E_j1;
Double_t        Eta_j2;
Double_t        Phi_j2;
Double_t        Pt_j2;
Double_t        E_j2;
Double_t        MeTPhi;
Double_t        Met_signi;
Double_t        MeT;
Double_t        dPhiJ1Met;
Double_t        dPhiJ2Met;
Double_t        Inv_Mass_bb;
Double_t        Inv_Mass_lept;
Double_t        DR_jets;
Int_t           flavour;*/
long int        eventNumber;
long int        runNumber;
Double_t        Wgg;
Double_t        Wqq;
Double_t        Wtt;
//Double_t        Wtwb;
Double_t        Wzz3;
Double_t        Wzz0;

Float_t        wgg;
Float_t        wqq;
Float_t        wtt;
Float_t        wzz3;
Float_t        wzz0;
Float_t        wzh3;
Float_t        wzh0;
Float_t        jetmetbjetprodCSVdisc;
Double_t       bdt;

std::map< std::string , Double_t > Whi0;
std::map< std::string , Double_t > Whi3;
int nmasses = 6;//9;
string masses[] = {"110","115","120","125","130","135"};//,"140","145","150"};

Double_t        jetmetbjetMinCSVdisc;
Double_t        jetmetbjetMaxCSVdisc;   
Double_t        jetmetbjetProdCSVdisc;

Double_t mlpZbbvsTT_MM;
Double_t mlpZbbvsTT_mu_MM;
Double_t mlpZbbvsTT_MM_N;
Double_t mlpZbbvsTT_mu_MM_N;
Double_t mlpZbbvsTT_ML;
Double_t mlpZbbvsTT_mu_ML;
Double_t mlpDYvsTT_2012;

//for the NN
std::map< std::string , Double_t > NNvalue;
//for(int j = 0; j < nNNs; j++) NNvalue[NNs[j]]=-1; //not working, why ?? but not needed it looks like
std::map< std::string , Double_t > SumNN;
std::map< std::string , Double_t > ProdNN;
std::map< std::string , Double_t > SumWeightedNN;

std::map< std::string , Double_t > SumNN_2j;
std::map< std::string , Double_t > ProdNN_2j;
std::map< std::string , Double_t > SumWeightedNN_2j;

std::map< std::string , Double_t > SumNN_3j;
std::map< std::string , Double_t > ProdNN_3j;
std::map< std::string , Double_t > SumWeightedNN_3j;

std::map< std::string , Double_t > SumNN_ML_2j;
std::map< std::string , Double_t > ProdNN_ML_2j;
std::map< std::string , Double_t > SumWeightedNN_ML_2j;

std::map< std::string , Double_t > SumNN_ML_3j;
std::map< std::string , Double_t > ProdNN_ML_3j;
std::map< std::string , Double_t > SumWeightedNN_ML_3j;

//Extra variables for reweighting stuff
Double_t ZbbReweight_dijetdR;
Double_t ZbbReweight_bestzpt;

TMVA::Reader * reader;

void CreateParentTree(TString InputFile) {
   std::cout << "Running over sample: " << InputFile << std::endl;
   TString sanitycut = "";
   bool isMuChannel = false;
   if (InputFile.Contains("Mu_") && InputFile.Contains("El_")) {
     std::cout << "InputFile name cannot contain both <<Mu_>> and <<El_>>" << std::endl;
     return;
   }
   
   else if (InputFile.Contains("Mu_") || InputFile.Contains("Mu_") || InputFile.Contains("Mu_")) {
     std::cout << "  running MuMu channel" << std::endl;
     isMuChannel = true;
     sanitycut = " && eventSelectionbestzmassMu > 0.01 ";
   }
   
   else if (InputFile.Contains("El_") || InputFile.Contains("Ele_") || InputFile.Contains("Ele_")) {
     std::cout << "  running over ElEl channel" << std::endl;
     sanitycut = " && eventSelectionbestzmassEl > 0.01 ";
   }
   
   else {
     std::cout << "InputFile name must contain <<Mu_>> or <<El_>>" << std::endl;
     return;
   }
  
   reader = new TMVA::Reader("!Color:!Silent");
   reader->AddVariable("ggweight", &wgg);
   reader->AddVariable("qqweight", &wqq);
   reader->AddVariable("ttweight", &wtt);
   reader->AddVariable("zzweight", &wzz0);
   reader->AddVariable("zz3weight", &wzz3);
   reader->AddVariable("hiweight", &wzh0);
   reader->AddVariable("hi3weight", &wzh3);
   reader->AddVariable("prodCSV", &jetmetbjetprodCSVdisc);
   reader->BookMVA("BDT", "../MW_Analysis/NN_AN/selectedBDT/higgs_BDT.weights.xml");


   MLP_TT_vs_DY_MM_CSV_2011 *MLP_TT_vs_DY_MM_ee = new MLP_TT_vs_DY_MM_CSV_2011();
   MLP_TT_vs_DY_MM_N_CSV_2011 *MLP_TT_vs_DY_MM_N_ee = new MLP_TT_vs_DY_MM_N_CSV_2011();
   MLP_TT_vs_DY_ML_CSV_2011 *MLP_TT_vs_DY_ML_ee = new MLP_TT_vs_DY_ML_CSV_2011();
   MLP_TT_vs_DY_MM_CSV_2011_mm *MLP_TT_vs_DY_MM_mm = new MLP_TT_vs_DY_MM_CSV_2011_mm();
   MLP_TT_vs_DY_MM_N_CSV_2011_mm *MLP_TT_vs_DY_MM_N_mm = new MLP_TT_vs_DY_MM_N_CSV_2011_mm();
   MLP_TT_vs_DY_ML_CSV_2011_mm *MLP_TT_vs_DY_ML_mm = new MLP_TT_vs_DY_ML_CSV_2011_mm();
   MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20 *MLP_TT_vs_DY_2012 = new MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20();
   
   MLP_Higgs_vs_DY_MM_N_CSV_2011_comb *MLP_higgs_vs_DY_MM_N_CSV_2011_comb = new MLP_Higgs_vs_DY_MM_N_CSV_2011_comb();  
   MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb *MLP_higgs_vs_ZZ_MM_N_CSV_2011_comb = new MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb();  
   MLP_Higgs_vs_TT_MM_N_CSV_2011_comb *MLP_higgs_vs_TT_MM_N_CSV_2011_comb = new MLP_Higgs_vs_TT_MM_N_CSV_2011_comb();  
   MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb *MLP_higgs_vs_BKG_MM_N_CSV_2011_comb = new MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb();
   
   MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125 *MLP_higgs_vs_DY_MM_N_CSV_2012_comb_ZH125 = new MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125();  
   MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125 *MLP_higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125 = new MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125();
   MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125 *MLP_higgs_vs_TT_MM_N_CSV_2012_comb_ZH125 = new MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125();
   MLP_Higgs_vs_Bkg_ZH125_comb *MLP_higgs_vs_Bkg_ZH125_comb = new MLP_Higgs_vs_Bkg_ZH125_comb();
   
   MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600 *MLP_higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600 = new MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600();  
   MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000 *MLP_higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000 = new MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000();  
   MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500 *MLP_higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500 = new MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500();
   MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000 *MLP_higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000();
   //test
   MLP_Higgs_vs_Bkg_ZH125_comb_1_10000 *MLP_higgs_vs_Bkg_ZH125_comb_1_10000 = new MLP_Higgs_vs_Bkg_ZH125_comb_1_10000();
   MLP_Higgs_vs_Bkg_ZH125_comb_1_5000 *MLP_higgs_vs_Bkg_ZH125_comb_1_5000 = new MLP_Higgs_vs_Bkg_ZH125_comb_1_5000();
   MLP_Higgs_vs_Bkg_ZH125_comb_2_10000 *MLP_higgs_vs_Bkg_ZH125_comb_2_10000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_10000();
   MLP_Higgs_vs_Bkg_ZH125_comb_2_5000 *MLP_higgs_vs_Bkg_ZH125_comb_2_5000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_5000();
   MLP_Higgs_vs_Bkg_ZH125_comb_3_5000 *MLP_higgs_vs_Bkg_ZH125_comb_3_5000 = new MLP_Higgs_vs_Bkg_ZH125_comb_3_5000();
   MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000 *MLP_higgs_vs_Bkg_ZH125_comb_2_3_2_10000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000();
   MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000 *MLP_higgs_vs_Bkg_ZH125_comb_2_3_2_5000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000(); 
   MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000 *MLP_higgs_vs_Bkg_ZH125_comb_2_4_10000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000();
   MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000 *MLP_higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000();
   MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000 *MLP_higgs_vs_Bkg_ZH125_comb_3_2_10000 = new MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000();
   //jet cat.
   MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20(); 
   
   MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3 *MLP_higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3 = new MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3();
   MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8 *MLP_higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8 = new MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8();
   MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21 *MLP_higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21 = new MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21();
   MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1 *MLP_higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1 = new MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1();
   
   MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
   
   MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4 *MLP_higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4 = new MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4();
   MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5 *MLP_higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5 = new MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5();
   MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9 *MLP_higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9 = new MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9();
   MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4 *MLP_higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4 =new MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4();
   MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1 *MLP_higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1 = new MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1();

   MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2 *MLP_higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2 = new MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2();
   MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *MLP_higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 = new MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
   MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20 *MLP_zz_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20 = new MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20();
   MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20 *MLP_zz_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20 = new MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20();
   MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20 *MLP_zz_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20 = new MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20();
   MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20 *MLP_zz_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20 = new MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20();
   MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20 *MLP_zz_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20 = new MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20();
   MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20 *MLP_zz_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20 = new MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20();

   //-----------------------------------------------------------------------
   // Input files location

   //RDS location
   TString folderRDS = "/nfs/user/acaudron/RDS537/";
   TFile* f_RDS  = new TFile(folderRDS+"File_rds_zbb_"+InputFile+".root");
   TTree* t_RDS  = (TTree*) f_RDS->Get("rds_zbb");  
   //tree2 input
   TString folderIn = "/nfs/user/acaudron/Tree2_537/";   
   TString mename = folderIn+"ME_zbb_" + InputFile + ".root";
   TFile* f_ME  = new TFile(mename);
   TTree* t_ME    = (TTree*)f_ME->Get("tree2");  
   //out file
   TString folderOut = "/nfs/user/acaudron/Tree2_537/";   
   TFile *f_RDSME = new TFile(folderOut+"Tree_rdsME_"+InputFile +".root", "RECREATE");
   TTree *t_RDSME = t_RDS->CloneTree(0);
   t_RDSME->SetTitle("merged zbb-ME tree");

   std::cout<<"read file : "<<f_RDS->GetName()<<std::endl;
   //-----------------------------------------------------------------------

   //Initialize histograms for reweighting
   if (useZbbReweight){
     InitZbbReweight();
   }

//b) Define branches
/*   t_RDSME->Branch("Pt_elplus", &Pt_elplus, "Pt_elplus/D");
   t_RDSME->Branch("Pt_elminus", &Pt_elminus, "Pt_elminus/D");
   t_RDSME->Branch("Pt_Muplus", &Pt_Muplus, "Pt_Muplus/D");
   t_RDSME->Branch("Pt_Muminus", &Pt_Muminus, "Pt_Muminus/D");
   t_RDSME->Branch("Phi_elplus", &Phi_elplus, "Phi_elplus/D");
   t_RDSME->Branch("Phi_elminus", &Phi_elminus, "Phi_elminus/D");
   t_RDSME->Branch("Phi_Muplus", &Phi_Muplus, "Phi_Muplus/D");
   t_RDSME->Branch("Phi_Muminus", &Phi_Muminus, "Phi_Muminus/D");
   t_RDSME->Branch("Eta_elplus", &Eta_elplus, "Eta_elplus/D");
   t_RDSME->Branch("Eta_elminus", &Eta_elminus, "Eta_elminus/D");
   t_RDSME->Branch("Eta_Muplus", &Eta_Muplus, "Eta_Muplus/D");
   t_RDSME->Branch("Eta_Muminus", &Eta_Muminus, "Eta_Muminus/D");
   t_RDSME->Branch("Eta_j1", &Eta_j1, "Eta_j1/D");
   t_RDSME->Branch("Phi_j1", &Phi_j1, "Phi_j1/D");
   t_RDSME->Branch("Pt_j1", &Pt_j1, "Pt_j1/D");
   t_RDSME->Branch("E_j1", &E_j1, "E_j1/D");
   t_RDSME->Branch("Eta_j2", &Eta_j2, "Eta_j2/D");
   t_RDSME->Branch("Phi_j2", &Phi_j2, "Phi_j2/D");
   t_RDSME->Branch("Pt_j2", &Pt_j2, "Pt_j2/D");
   t_RDSME->Branch("E_j2", &E_j2, "E_j2/D");
   t_RDSME->Branch("MeTPhi", &MeTPhi, "MeTPhi/D");
   t_RDSME->Branch("Met_signi", &Met_signi, "Met_signi/D");
   t_RDSME->Branch("MeT", &MeT, "MeT/D");
   t_RDSME->Branch("dPhiJ1Met", &dPhiJ1Met, "dPhiJ1Met/D");
   t_RDSME->Branch("dPhiJ2Met", &dPhiJ2Met, "dPhiJ2Met/D");
   t_RDSME->Branch("Inv_Mass_bb", &Inv_Mass_bb, "Inv_Mass_bb/D");
   t_RDSME->Branch("Inv_Mass_lept", &Inv_Mass_lept, "Inv_Mass_lept/D");
   t_RDSME->Branch("Inv_Mass_bb", &Inv_Mass_bb, "Inv_Mass_bb/D");
   t_RDSME->Branch("Inv_Mass_lept", &Inv_Mass_lept, "Inv_Mass_lept/D");
   t_RDSME->Branch("DR_jets", &DR_jets, "DR_jets/D");
   t_RDSME->Branch("flavour", &flavour, "flavour/I");*/
   t_RDSME->Branch("eventNumber", &eventNumber, "eventNumber/l");
   t_RDSME->Branch("runNumber", &runNumber, "runNumber/l");
   t_RDSME->Branch("bdt", &bdt, "bdt/D");
   t_RDSME->Branch("Wgg", &Wgg, "Wgg/D");
   t_RDSME->Branch("Wqq", &Wqq, "Wqq/D");
   t_RDSME->Branch("Wtt", &Wtt, "Wtt/D");
   //   t_RDSME->Branch("Wtwb", &Wtwb, "Wtwb/D");
   t_RDSME->Branch("Wzz3", &Wzz3, "Wzz3/D");
   t_RDSME->Branch("Wzz0", &Wzz0, "Wzz0/D");
   for(int m=0; m < (nmasses) ; m++){
     t_RDSME->Branch(("Whi3_"+masses[m]).c_str(), &Whi3[masses[m]], ("Whi3_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("Whi0_"+masses[m]).c_str(), &Whi0[masses[m]], ("Whi0_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("SumNN_"+masses[m]).c_str() , &SumNN[masses[m]],("SumNN_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("ProdNN_"+masses[m]).c_str() , &ProdNN[masses[m]],("ProdNN_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("SumWeightedNN_"+masses[m]).c_str() , &SumWeightedNN[masses[m]],("SumWeightedNN_"+masses[m]+"/D").c_str());
     
     t_RDSME->Branch(("SumNN_2j_"+masses[m]).c_str() , &SumNN_2j[masses[m]],("SumNN_2j_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("ProdNN_2j_"+masses[m]).c_str() , &ProdNN_2j[masses[m]],("ProdNN_2j_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("SumWeightedNN_2j_"+masses[m]).c_str() , &SumWeightedNN_2j[masses[m]],("SumWeightedNN_2j_"+masses[m]+"/D").c_str());
     
     t_RDSME->Branch(("SumNN_3j_"+masses[m]).c_str() , &SumNN_3j[masses[m]],("SumNN_3j_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("ProdNN_3j_"+masses[m]).c_str() , &ProdNN_3j[masses[m]],("ProdNN_3j_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("SumWeightedNN_3j_"+masses[m]).c_str() , &SumWeightedNN_3j[masses[m]],("SumWeightedNN_3j_"+masses[m]+"/D").c_str());

     t_RDSME->Branch(("SumNN_ML_2j_"+masses[m]).c_str() , &SumNN_ML_2j[masses[m]],("SumNN_ML_2j_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("ProdNN_ML_2j_"+masses[m]).c_str() , &ProdNN_ML_2j[masses[m]],("ProdNN_ML_2j_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("SumWeightedNN_ML_2j_"+masses[m]).c_str() , &SumWeightedNN_ML_2j[masses[m]],("SumWeightedNN_ML_2j_"+masses[m]+"/D").c_str());
     
     t_RDSME->Branch(("SumNN_ML_3j_"+masses[m]).c_str() , &SumNN_ML_3j[masses[m]],("SumNN_ML_3j_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("ProdNN_ML_3j_"+masses[m]).c_str() , &ProdNN_ML_3j[masses[m]],("ProdNN_ML_3j_"+masses[m]+"/D").c_str());
     t_RDSME->Branch(("SumWeightedNN_ML_3j_"+masses[m]).c_str() , &SumWeightedNN_ML_3j[masses[m]],("SumWeightedNN_ML_3j_"+masses[m]+"/D").c_str());

     for(int n=0; n<nNNs; n++) {
       t_RDSME->Branch((NNs[n]+"_"+masses[m]).c_str(), &NNvalue[NNs[n]+"_"+masses[m]],(NNs[n]+"_"+masses[m]+"/D").c_str());
     }
   }
   for(int n=0; n<nNNsZZ; n++) {
     t_RDSME->Branch((NNsZZ[n]).c_str(), &NNvalue[NNsZZ[n]],(NNsZZ[n]+"/D").c_str());
   }

   //Extra variables MLP's or variables not included in tree2
   t_RDSME->Branch("jetmetbjetMinCSVdisc",&jetmetbjetMinCSVdisc,"jetmetbjetMinCSVdisc/D");
   t_RDSME->Branch("jetmetbjetMaxCSVdisc",&jetmetbjetMaxCSVdisc,"jetmetbjetMaxCSVdisc/D");
   t_RDSME->Branch("jetmetbjetProdCSVdisc",&jetmetbjetProdCSVdisc,"jetmetbjetProdCSVdisc/D");     

   t_RDSME->Branch("mlpZbbvsTT_MM" , &mlpZbbvsTT_MM,"mlpZbbvsTT_MM/D");
   t_RDSME->Branch("mlpZbbvsTT_MM_N" , &mlpZbbvsTT_MM_N,"mlpZbbvsTT_MM_N/D");
   t_RDSME->Branch("mlpZbbvsTT_ML" , &mlpZbbvsTT_ML,"mlpZbbvsTT_ML/D");

   t_RDSME->Branch("mlpZbbvsTT_mu_MM" , &mlpZbbvsTT_mu_MM,"mlpZbbvsTT_mu_MM/D");
   t_RDSME->Branch("mlpZbbvsTT_mu_MM_N" , &mlpZbbvsTT_mu_MM_N,"mlpZbbvsTT_mu_MM_N/D");
   t_RDSME->Branch("mlpZbbvsTT_mu_ML" , &mlpZbbvsTT_mu_ML,"mlpZbbvsTT_mu_ML/D");

   t_RDSME->Branch("mlpDYvsTT_2012" , &mlpDYvsTT_2012,"mlpDYvsTT_2012/D");

   //Extra variables reweighting                                                                                                                                                 
   t_RDSME->Branch("ZbbReweight_dijetdR",&ZbbReweight_dijetdR,"ZbbReweight_dijetdR/D");
   t_RDSME->Branch("ZbbReweight_bestzpt",&ZbbReweight_bestzpt,"ZbbReweight_bestzpt/D");

   rds_zbb* mc_RDS = new rds_zbb(t_RDS);
   tree2* mc_ME = new tree2(t_ME);

   bool IsDATA = InputFile.Contains("DATA");

   //First loop to relatively short ME ntuple to create the index (for some reason BuildIndex-GetEntryWithIndex doesn't work)
   std::map<std::pair<long int, long int>, long int> map_runevent;
   Long64_t nbytesME = 0, nbME = 0;
   for (Int_t iME=0;iME<t_ME->GetEntries();iME++) {
      //if (iME > 5000) break;

      Long64_t ientry = mc_ME->LoadTree(iME);
      if (ientry < 0) break;
      //std::cout << "iME = " << iME << std::endl;
      nbME = mc_ME->GetEntry(iME);   nbytesME += nbME;     
      //std::cout << "iME=" << iME << " run= " << mc_ME->runNumber << " event= "<< mc_ME->eventNumber << std::endl;
      //I sum 1 to the entry because 0 is the code when the entry is not found but it is also a valid index
      if (IsDATA)
        map_runevent[std::pair<Long64_t, Long64_t>(Long64_t(mc_ME->runNumber), Long64_t(mc_ME->eventNumber))] = iME + 1;
      else
        map_runevent[std::pair<Long64_t, Long64_t>(1, Long64_t(mc_ME->eventNumber))] = iME + 1;

      //std::cout << map_runevent.size() << std::endl;
   }
   

   //Second loop to larger RDS sample, break right away if not selected step fulfilled
   Long64_t nbytesRDS = 0, nbRDS = 0;
   for (Int_t iRDS=0;iRDS<t_RDS->GetEntries();iRDS++) {

      Long64_t ientry = mc_RDS->LoadTree(iRDS);
      if (ientry < 0 ) break;
      nbRDS = mc_RDS->GetEntry(iRDS);   nbytesRDS += nbRDS;
      //if (mc_RDS->rc_eventSelection_12_idx == 0) continue;
      //if (mc_RDS->rc_eventSelection_9_idx == 0) continue;
      if (isMuChannel && mc_RDS->eventSelectionbestzmassMu < 0.01 ) continue;
      if (!isMuChannel && mc_RDS->eventSelectionbestzmassEle < 0.01 ) continue;
      
 
      
      int MEentry = -1; 
      if (IsDATA) MEentry = map_runevent[std::pair<Long64_t, Long64_t>(Long64_t(mc_RDS->eventSelectionrun), Long64_t(mc_RDS->eventSelectionevent))];
      else  MEentry = map_runevent[std::pair<long int, long int>(1, int(mc_RDS->eventSelectionevent))];
      //std::cout << "RDSeventNumber=" << mc_RDS->eventSelectionevent << std::endl;
      if (MEentry==0) {
        //printf("Not Found [%i, %i]\n", int(mc_RDS->eventSelectionrun), int(mc_RDS->eventSelectionevent));
        //std::cout << "Not Found [" << mc_RDS->eventSelectionrun << ":" << mc_RDS->eventSelectionevent << "]" << std::endl; 
      }
      //else printf("Found [%i, %i]\n", int(mc_RDS->eventSelectionrun), int(mc_RDS->eventSelectionevent));
      //std::cout << "MEentry = " << MEentry << " for event=" << mc_RDS->eventSelectionevent<< std::endl;
      if (MEentry > 0) {//std::cout << "MEentry = " << MEentry << std::endl;
        //std:: cout << "MEentry for " << mc_RDS->eventSelectionrun << ", " << mc_RDS->eventSelectionevent << "]= " << MEentry << std::endl;
        MEentry -= 1; //I substract the unity I added when creating the map 
	
        //MeT = 0;
	Wtt = 0;
	Wqq = 0;
	Wgg = 0;
	//        Wtwb = 0;
        Wzz3 = 0;
        Wzz0 = 0;
	for (int m = 0; m<nmasses; m++) {
	  Whi0[masses[m]]=0;
	  Whi3[masses[m]]=0;
	}

        //Inv_Mass_bb = 0;
        //Inv_Mass_lept = 0;
       
        mc_ME->LoadTree(MEentry);
        mc_ME->GetEntry(MEentry);
      
	//        MeT = mc_ME->MeT;
	Wtt = mc_ME->Wtt;
	Wqq = mc_ME->Wqq;
 	Wgg = mc_ME->Wgg;
	//        Wtwb = mc_ME->Wtwb;
        Wzz3 = mc_ME->Wzz3;
        Wzz0 = mc_ME->Wzz0;
        Whi3["110"] = mc_ME->Whi3_110;
        Whi0["110"] = mc_ME->Whi0_110;
        Whi3["115"] = mc_ME->Whi3_115;
        Whi0["115"] = mc_ME->Whi0_115;
        Whi3["120"] = mc_ME->Whi3_120;
        Whi0["120"] = mc_ME->Whi0_120;
        Whi3["125"] = mc_ME->Whi3_125;
        Whi0["125"] = mc_ME->Whi0_125;
        Whi3["130"] = mc_ME->Whi3_130;
        Whi0["130"] = mc_ME->Whi0_130;
        Whi3["135"] = mc_ME->Whi3_135;
        Whi0["135"] = mc_ME->Whi0_135;
        Whi3["140"] = mc_ME->Whi3_140;
        Whi0["140"] = mc_ME->Whi0_140;
        Whi3["145"] = mc_ME->Whi3_145;
        Whi0["145"] = mc_ME->Whi0_145;
        Whi3["150"] = mc_ME->Whi3_150;
        Whi0["150"] = mc_ME->Whi0_150;

	jetmetbjetMinCSVdisc=std::min(mc_RDS->jetmetbjet1CSVdisc,mc_RDS->jetmetbjet2CSVdisc);
	jetmetbjetMaxCSVdisc=std::max(mc_RDS->jetmetbjet1CSVdisc,mc_RDS->jetmetbjet2CSVdisc);
	jetmetbjetProdCSVdisc=mc_RDS->jetmetbjet1CSVdisc*mc_RDS->jetmetbjet2CSVdisc;


	wtt = Wtt;
	wqq = Wqq;
 	wgg = Wgg;
        wzz3 = Wzz3;
        Wzz0 = Wzz0;
        wzh3 = Whi3["125"];
        wzh0 = Whi0["125"];
	jetmetbjetprodCSVdisc=jetmetbjetProdCSVdisc;
        bdt = reader->EvaluateMVA("BDT");

	//        Inv_Mass_bb = mc_ME->Inv_Mass_bb;
        //Inv_Mass_lept = mc_ME->Inv_Mass_lept;
	
//---------------------- NN  output here ---------------------------------
        // For DY vs TT
	mlpZbbvsTT_MM = std::max(0.0,std::min(1.0,MLP_TT_vs_DY_MM_ee->Value(0, Wgg, Wqq, Wtt)));
        mlpZbbvsTT_MM_N = std::max(0.0,std::min(1.0,MLP_TT_vs_DY_MM_N_ee->Value(0, Wgg,Wqq, mc_RDS->jetmetbjet2CSVdisc*mc_RDS->jetmetbjet1CSVdisc)));
        mlpZbbvsTT_ML = std::max(0.0,std::min(1.0,MLP_TT_vs_DY_ML_ee->Value(0, Wgg, Wqq, Wtt)));
	mlpZbbvsTT_mu_MM = std::max(0.0,std::min(1.0,MLP_TT_vs_DY_MM_mm->Value(0, Wgg, Wqq, Wtt)));
        mlpZbbvsTT_mu_MM_N = std::max(0.0,std::min(1.0,MLP_TT_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Wtt)));
	mlpZbbvsTT_mu_ML = std::max(0.0,std::min(1.0,MLP_TT_vs_DY_ML_mm->Value(0, Wgg, Wqq, Wtt)));
	mlpDYvsTT_2012 = std::max(0.0,std::min(1.0,MLP_TT_vs_DY_2012->Value(0, Wgg, Wqq, Wtt)));

	for(int m=0; m<nmasses; m++){
	  NNvalue["NN_Higgs125vsDY_MM_N_CSV_2011_comb_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_DY_MM_N_CSV_2011_comb->Value(0, Wgg, Wqq, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2011_comb_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_ZZ_MM_N_CSV_2011_comb->Value(0, Wzz0 , Wzz3, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsTT_MM_N_CSV_2011_comb_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_TT_MM_N_CSV_2011_comb->Value(0, Wtt, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsBKG_MM_N_CSV_2011_comb_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_BKG_MM_N_CSV_2011_comb->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2011_comb_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2011_comb_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2011_comb_"+masses[m]])));
	  
	  NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb_ZH125_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_DY_MM_N_CSV_2012_comb_ZH125->Value(0, Wgg, Wqq, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb_ZH125_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125->Value(0, Wzz0 , Wzz3, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb_ZH125_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_TT_MM_N_CSV_2012_comb_ZH125->Value(0, Wtt, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsBkgcomb_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb_ZH125_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb_ZH125_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb_ZH125_"+masses[m]])));
	  
	  NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600->Value(0, Wgg, Wqq, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000->Value(0, Wzz0 , Wzz3, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500->Value(0, Wtt, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsBkgcomb_2_3_2_1_1000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])));
	  
	  NNvalue["NN_Higgs125vsBkgcomb_1_10000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb_1_10000->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkgcomb_1_5000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb_1_5000->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkgcomb_2_10000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb_2_10000->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkgcomb_2_5000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb_2_5000->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkgcomb_3_5000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb_3_5000->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkgcomb_2_3_2_10000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb_2_3_2_10000->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkgcomb_2_3_2_5000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb_2_3_2_5000->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkgcomb_2_4_10000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb_2_4_10000->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkgcomb_2_5_3_1_1000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkgcomb_3_2_10000_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_ZH125_comb_3_2_10000->Value(0,NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]],NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]],NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])));
	  
	  SumNN[masses[m]] = (NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]]+NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]]+NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]])/3;
	  ProdNN[masses[m]] = NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]]*NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]]*NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]];
	  SumWeightedNN[masses[m]] = NNvalue["NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600_"+masses[m]]*0.8+NNvalue["NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000_"+masses[m]]*0.05+NNvalue["NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500_"+masses[m]]*0.15;
	  
	  
	  NNvalue["NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wgg, Wqq, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wzz0 , Wzz3, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wtt, Whi0[masses[m]] , Whi3[masses[m]])));
	  SumNN_2j[masses[m]] = (NNvalue["NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520_"+masses[m]]+NNvalue["NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520_"+masses[m]]+NNvalue["NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520_"+masses[m]])/3;
	  ProdNN_2j[masses[m]] = NNvalue["NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520_"+masses[m]]*NNvalue["NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520_"+masses[m]]*NNvalue["NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520_"+masses[m]];
	  SumWeightedNN_2j[masses[m]] = NNvalue["NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520_"+masses[m]]*0.8+NNvalue["NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520_"+masses[m]]*0.05+NNvalue["NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520_"+masses[m]]*0.15;
	  
	  
	  NNvalue["NN_Higgs125vsBkg_2jcomb_2_2_2_500_Nj2Mbb50_200Pt402520_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20->Value(0,NNvalue["NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkg_2jcomb_6_6_131_Nj2Mbb80_150Pt402520_3_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3->Value(0,NNvalue["NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkg_2jcomb_9_3_100_Nj2Mbb80_150Pt402520_8_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8->Value(0,NNvalue["NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkg_2jcomb_9_3_100_Nj2Mbb80_150Pt402520_21_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21->Value(0,NNvalue["NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkg_2jcomb_2_500_Nj2Mbb80_150Pt402520_1_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1->Value(0,NNvalue["NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520_"+masses[m]])));
	  
	  
	  NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wgg, Wqq, Whi0[masses[m]] , Whi3[masses[m]],mc_RDS->jetmettrijetMdr,mc_RDS->jetmetfsrDR,mc_RDS->eventSelectiondijetdR)));
	  NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wzz0 , Wzz3, Whi0[masses[m]] , Whi3[masses[m]],mc_RDS->jetmettrijetMdr,mc_RDS->jetmetfsrDR,mc_RDS->eventSelectiondijetdR)));
	  NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wtt, Whi0[masses[m]] , Whi3[masses[m]],mc_RDS->jetmettrijetMdr,mc_RDS->jetmetfsrDR,mc_RDS->eventSelectiondijetdR)));
	  SumNN_3j[masses[m]] = (NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt_"+masses[m]]+NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt_"+masses[m]]+NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt_"+masses[m]])/3;
	  ProdNN_3j[masses[m]] = NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt_"+masses[m]]*NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt_"+masses[m]]*NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt_"+masses[m]];
	  SumWeightedNN_3j[masses[m]] = NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt_"+masses[m]]*0.8+NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt_"+masses[m]]*0.05+NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt_"+masses[m]]*0.15;
	  
	  NNvalue["NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_4_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4->Value(0,NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt_"+masses[m]],NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt_"+masses[m]],NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_5_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5->Value(0,NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt_"+masses[m]],NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt_"+masses[m]],NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_9_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9->Value(0,NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt_"+masses[m]],NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt_"+masses[m]],NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkg_3jcomb_9_9_300_Nj3_Mbb50_150_Pt402520_4_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4->Value(0,NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt_"+masses[m]],NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt_"+masses[m]],NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkg_3jcomb_5_600_Nj3_Mbb50_150_Pt402520_1_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1->Value(0,NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt_"+masses[m]],NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt_"+masses[m]],NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt_"+masses[m]])));



	  NNvalue["NN_Higgs125vsDYcomb_12_120_Nj2Mbb80_150Pt402520_2_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2->Value(0, Wgg, Wqq, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsZZcomb_2_2_1000_Nj2Mbb80_150Pt402520_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wzz0, Wzz3, Whi0[masses[m]] , Whi3[masses[m]])));
	  NNvalue["NN_Higgs125vsTTcomb_6_3_2_150_Nj2Mbb80_150Pt402520_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wtt, Whi0[masses[m]] , Whi3[masses[m]])));
	  SumNN_ML_2j[masses[m]] = (NNvalue["NN_Higgs125vsDYcomb_12_120_Nj2Mbb80_150Pt402520_2_"+masses[m]]+NNvalue["NN_Higgs125vsZZcomb_2_2_1000_Nj2Mbb80_150Pt402520_"+masses[m]]+NNvalue["NN_Higgs125vsTTcomb_6_3_2_150_Nj2Mbb80_150Pt402520_"+masses[m]])/3;
	  ProdNN_ML_2j[masses[m]] = NNvalue["NN_Higgs125vsDYcomb_12_120_Nj2Mbb80_150Pt402520_2_"+masses[m]]*NNvalue["NN_Higgs125vsZZcomb_2_2_1000_Nj2Mbb80_150Pt402520_"+masses[m]]*NNvalue["NN_Higgs125vsTTcomb_6_3_2_150_Nj2Mbb80_150Pt402520_"+masses[m]];
	  SumWeightedNN_ML_2j[masses[m]] = NNvalue["NN_Higgs125vsDYcomb_12_120_Nj2Mbb80_150Pt402520_2_"+masses[m]]*0.8+NNvalue["NN_Higgs125vsZZcomb_2_2_1000_Nj2Mbb80_150Pt402520_"+masses[m]]*0.05+NNvalue["NN_Higgs125vsTTcomb_6_3_2_150_Nj2Mbb80_150Pt402520_"+masses[m]]*0.15;


	  NNvalue["NN_Higgs125vsBkg_2jcomb_4_5000_Nj2Mbb80_150Pt402520_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20->Value(0,NNvalue["NN_Higgs125vsDYcomb_12_120_Nj2Mbb80_150Pt402520_2_"+masses[m]],NNvalue["NN_Higgs125vsZZcomb_2_2_1000_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsTTcomb_6_3_2_150_Nj2Mbb80_150Pt402520_"+masses[m]])));
	  NNvalue["NN_Higgs125vsBkg_2jcomb_4_2_500_Nj2Mbb80_150Pt402520_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20->Value(0,NNvalue["NN_Higgs125vsDYcomb_12_120_Nj2Mbb80_150Pt402520_2_"+masses[m]],NNvalue["NN_Higgs125vsZZcomb_2_2_1000_Nj2Mbb80_150Pt402520_"+masses[m]],NNvalue["NN_Higgs125vsTTcomb_6_3_2_150_Nj2Mbb80_150Pt402520_"+masses[m]])));
	  

	  NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_12_9_6_3_210_Nj3MbbPt_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wgg, Wqq, Whi0[masses[m]] , Whi3[masses[m]],mc_RDS->jetmettrijetMdr,mc_RDS->jetmetfsrDR)));
	  NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_9_100_Nj3Mbb50_150_Pt_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wzz0, Wzz3, Whi0[masses[m]] , Whi3[masses[m]],mc_RDS->jetmettrijetMdr,mc_RDS->jetmetfsrDR)));
	  NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_2_600_Nj3Mbb50_150_Pt_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wtt, Whi0[masses[m]] , Whi3[masses[m]],mc_RDS->jetmettrijetMdr,mc_RDS->jetmetfsrDR)));
	  SumNN_ML_3j[masses[m]] = (NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_12_9_6_3_210_Nj3MbbPt_"+masses[m]]+NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_9_100_Nj3Mbb50_150_Pt_"+masses[m]]+NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_2_600_Nj3Mbb50_150_Pt_"+masses[m]])/3;
	  ProdNN_ML_3j[masses[m]] = NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_12_9_6_3_210_Nj3MbbPt_"+masses[m]]*NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_9_100_Nj3Mbb50_150_Pt_"+masses[m]]*NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_2_600_Nj3Mbb50_150_Pt_"+masses[m]];
	  SumWeightedNN_ML_3j[masses[m]] = NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_12_9_6_3_210_Nj3MbbPt_"+masses[m]]*0.8+NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_9_100_Nj3Mbb50_150_Pt_"+masses[m]]*0.05+NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_2_600_Nj3Mbb50_150_Pt_"+masses[m]]*0.15;

	  NNvalue["NN_Higgs125vsBkg_3jcomb_prodCSV_5_3_1000_Nj3Mbb50_150Pt_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20->Value(0,NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_12_9_6_3_210_Nj3MbbPt_"+masses[m]],NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_9_100_Nj3Mbb50_150_Pt_"+masses[m]],NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_2_600_Nj3Mbb50_150_Pt_"+masses[m]],mc_RDS->jetmetbjet2CSVdisc*mc_RDS->jetmetbjet1CSVdisc)));
	  NNvalue["NN_Higgs125vsBkg_3jcomb_prodCSV_3_2_1000_Nj3Mbb50_150Pt_"+masses[m]] = std::max(0.0,std::min(1.0,MLP_higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20->Value(0,NNvalue["NN_Higgs125vsDYcombMbbjdRbjdRbb_12_9_6_3_210_Nj3MbbPt_"+masses[m]],NNvalue["NN_Higgs125vsZZcombMbbjdRbjdRbb_9_100_Nj3Mbb50_150_Pt_"+masses[m]],NNvalue["NN_Higgs125vsTTcombMbbjdRbjdRbb_2_2_600_Nj3Mbb50_150_Pt_"+masses[m]],mc_RDS->jetmetbjet2CSVdisc*mc_RDS->jetmetbjet1CSVdisc)));

	  
	}



	NNvalue["NN_ZZvsDYcomb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20"] = std::max(0.0,std::min(1.0,MLP_zz_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wgg, Wqq, Wzz0 , Wzz3)));
	NNvalue["NN_ZZvsTTcomb_2_1000_Nj2Mbb45_115Pt402520"] = std::max(0.0,std::min(1.0,MLP_zz_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wtt, Wzz0 , Wzz3)));
	
	NNvalue["NN_ZZvsBkg_2jcomb_12_50_Nj2Mbb45_115Pt402520"] = std::max(0.0,std::min(1.0,MLP_zz_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20->Value(0,NNvalue["NN_ZZvsDYcomb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20"],NNvalue["NN_ZZvsTTcomb_2_1000_Nj2Mbb45_115Pt402520"])));
	
	
	NNvalue["NN_ZZvsDYcombMbbjdRbjdRbb_12_50_Nj3Mbb15_115Pt402520"] = std::max(0.0,std::min(1.0,MLP_zz_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wgg, Wqq, Wzz0 , Wzz3,mc_RDS->jetmettrijetMdr,mc_RDS->jetmetfsrDR)));
	NNvalue["NN_ZZvsTTcombMbbjdRbjdRbb_3_2_500_Nj3Mbb15_115Pt402520"] = std::max(0.0,std::min(1.0,MLP_zz_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20->Value(0, Wtt, Wzz0 , Wzz3,mc_RDS->jetmettrijetMdr,mc_RDS->jetmetfsrDR)));
	
	NNvalue["NN_ZZvsBkg_3jcomb_prodCSV_9_200_Nj3Mbb15_115Pt402520"] = std::max(0.0,std::min(1.0,MLP_zz_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20->Value(0,NNvalue["NN_ZZvsDYcombMbbjdRbjdRbb_12_50_Nj3Mbb15_115Pt402520"],NNvalue["NN_ZZvsTTcombMbbjdRbjdRbb_3_2_500_Nj3Mbb15_115Pt402520"],mc_RDS->jetmetbjet2CSVdisc*mc_RDS->jetmetbjet1CSVdisc)));


	//Reweighting stuff here:
	ZbbReweight_dijetdR = 1.;
	ZbbReweight_bestzpt = 1.;
	
	//std::cout << "hZbbReweight_dijetdR_Mu_>Integral()=" << hZbbReweight_dijetdR_Mu->Integral() << std::endl;
        if (useZbbReweight && (InputFile == "Mu_MC" || InputFile == "El_MC")){
          if (InputFile == "Mu_MC") {
	    ZbbReweight_dijetdR = Compute1DReweight(hZbbReweight_dijetdR_Mu, mc_RDS->eventSelectiondijetdR);
	    ZbbReweight_bestzpt = Compute1DReweight(hZbbReweight_bestzpt_Mu, mc_RDS->eventSelectionbestzptMu);
	  }
        
          if (InputFile == "El_MC") {
	    ZbbReweight_dijetdR = Compute1DReweight(hZbbReweight_dijetdR_El, mc_RDS->eventSelectiondijetdR);
	    ZbbReweight_bestzpt = Compute1DReweight(hZbbReweight_bestzpt_El, mc_RDS->eventSelectionbestzptEle);
	  }
        }
	//mc_RDS->eventSelectionbestzptEle
	
	t_RDSME->Fill();
     } //else std:: cout << "MEentry not found for " << mc_RDS->eventSelectionrun << ", " << mc_RDS->eventSelectionevent << "]= " << MEentry << std::endl;
      }


      f_RDSME->cd();
      t_RDSME->Write();
   
      delete mc_RDS;
      delete mc_ME;

      //delete f_RDSME;
      //delete t_RDSME;
 
      //delete f_ME;
      //delete t_ME;
 
      //delete f_RDS;
      //delete t_RDS;

}


//Functions for reweighting
void InitZbbReweight() {
  
  //return if reweighting histograms already filled
  if (file_reweight != 0) return;
  if (hZbbReweight_dijetdR_Mu  != 0 && 
      hZbbReweight_bestzpt_Mu  != 0 && 
      hZbbReweight_dijetdR_El  != 0 && 
      hZbbReweight_bestzpt_El  != 0) {return;}

  file_reweight = TFile::Open("./ZbbReweightHistos.root");
  hZbbReweight_dijetdR_Mu = (TH1D*)file_reweight->Get("eventSelectiondijetdR_Mu");
  hZbbReweight_bestzpt_Mu = (TH1D*)file_reweight->Get("eventSelectionbestzptMu_Mu");

  hZbbReweight_dijetdR_El = (TH1D*)file_reweight->Get("eventSelectiondijetdR_El");
  hZbbReweight_bestzpt_El = (TH1D*)file_reweight->Get("eventSelectionbestzptEle_El");
  
  if (hZbbReweight_dijetdR_Mu  == 0) {std::cout << " hZbbReweight_dijetdR_Mu==0" << std::endl; exit(1);} 
  if (hZbbReweight_bestzpt_Mu  == 0) {std::cout << " hZbbReweight_bestzpt_Mu==0" << std::endl; exit(1);} 
  if (hZbbReweight_dijetdR_El  == 0) {std::cout << " hZbbReweight_dijetdR_El==0" << std::endl; exit(1);} 
  if (hZbbReweight_bestzpt_El  == 0) {std::cout << " hZbbReweight_bestzpt_El==0" << std::endl; exit(1);}
  
  std::cout << "hZbbReweight_dijetdR_Mu->GetName()=" << hZbbReweight_dijetdR_Mu->GetName() << std::endl;
  std::cout << "hZbbReweight_dijetdR_Mu->Integral()=" << hZbbReweight_dijetdR_Mu->Integral() << std::endl;
  std::cout << "hZbbReweight_dijetdR_Mu->FindBin(3.)=" << hZbbReweight_dijetdR_Mu->FindBin(3.)<< std::endl;  
  
 }

double Compute1DReweight(TH1D* hRW, double value) {
 
  //cout << "before FindBin(" << value << ")" << endl;
  const int bin = hRW->FindBin(value);
  //std::cout << "after FindBin, bin=" << bin << endl;
  
  //reweighting hRWs not correct for under/overflow
  if(bin<=0 || bin==hRW->GetNbinsX()+1) return 1.; 
  const float content = hRW->GetBinContent(bin);
  if(content <=0.) return 1.;
  if (content > 5.)//prevent huge weights
    return 5.;

  return content;
}

void SimpleTree() {
  CreateParentTree("DoubleMu_DataA");
  CreateParentTree("DoubleEle_DataA");
  CreateParentTree("DoubleMu_DataA06aug");
  CreateParentTree("DoubleEle_DataA06aug");
  CreateParentTree("DoubleMu_DataB");
  CreateParentTree("DoubleEle_DataB");
  CreateParentTree("DoubleMu_DataC-v1");
  CreateParentTree("DoubleEle_DataC-v1");
  CreateParentTree("DoubleMu_DataC-v2");
  CreateParentTree("DoubleEle_DataC-v2");
  CreateParentTree("DoubleMu_DataD");
  CreateParentTree("DoubleEle_DataD");
  CreateParentTree("DY_Mu_MC");
  CreateParentTree("DY_El_MC");
  
  CreateParentTree("DY1j_Mu_MC");
  CreateParentTree("DY1j_El_MC");
  CreateParentTree("DY2j_Mu_MC");
  CreateParentTree("DY2j_El_MC");
  CreateParentTree("DY3j_Mu_MC");
  CreateParentTree("DY3j_El_MC");
  //CreateParentTree("DY4j_Mu_MC");
  //CreateParentTree("DY4j_El_MC");
  CreateParentTree("DY50-70_Mu_MC");
  CreateParentTree("DY50-70_El_MC");
  CreateParentTree("DY70-100_Mu_MC");
  CreateParentTree("DY70-100_El_MC");
  CreateParentTree("DY100_Mu_MC");
  CreateParentTree("DY100_El_MC");
  CreateParentTree("DY180_Mu_MC");
  CreateParentTree("DY180_El_MC");
  
  //CreateParentTree("TT_Mu_MC");
  //CreateParentTree("TT_El_MC");
  CreateParentTree("TT-FullLept_Mu_MC");
  CreateParentTree("TT-FullLept_El_MC");
  CreateParentTree("TT-SemiLept_Mu_MC");
  CreateParentTree("TT-SemiLept_El_MC");
  CreateParentTree("Zbb_Mu_MC");
  CreateParentTree("Zbb_El_MC");
  CreateParentTree("ZZ_Mu_MC");
  CreateParentTree("ZZ_El_MC");
  CreateParentTree("ZH125_Mu_MC");
  CreateParentTree("ZH125_El_MC");
  
  CreateParentTree("ZH110_Mu_MC");
  CreateParentTree("ZH110_El_MC");
  CreateParentTree("ZH115_Mu_MC");
  CreateParentTree("ZH115_El_MC");
  CreateParentTree("ZH120_Mu_MC");
  CreateParentTree("ZH120_El_MC");
  CreateParentTree("ZH130_Mu_MC");
  CreateParentTree("ZH130_El_MC");
  CreateParentTree("ZH135_Mu_MC");
  CreateParentTree("ZH135_El_MC");
  CreateParentTree("ZH140_Mu_MC");
  CreateParentTree("ZH140_El_MC");
  CreateParentTree("ZH145_Mu_MC");
  CreateParentTree("ZH145_El_MC");
  CreateParentTree("ZH150_Mu_MC");
  CreateParentTree("ZH150_El_MC");
}
