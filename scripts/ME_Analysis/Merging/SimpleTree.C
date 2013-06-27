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
//  Author: Jesus Vizan
      
#include "TTree.h"
#include "TFile.h"
#include "TRandom.h"
#include "TTree.h"
#include "TTree.h"
//#include "RooDataSet.h"
#include <algorithm>
#include "rds_zbb.C"
#include "tree2.C"
// Include NN traine on ee
// MM: CSV Medium Medium WP
// MM_N: CSV Medium Medium WP + narrow Mll
// ML: CSV Medium Loose WP
#include "../NN/MLP_Higgs_vs_DY_MM_CSV_2011.cxx"
#include "MLP_Higgs_vs_DY_MM_N_CSV_2011_ee.cxx"
#include "../NN/MLP_Higgs_vs_DY_ML_CSV_2011.cxx"
#include "../NN/MLP_Higgs_vs_ZZ_MM_CSV_2011.cxx"
#include "MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee.cxx"
#include "../NN/MLP_Higgs_vs_ZZ_ML_CSV_2011.cxx"
#include "../NN/MLP_Higgs_vs_TT_MM_CSV_2011.cxx"
#include "MLP_Higgs_vs_TT_MM_N_CSV_2011_ee.cxx"
#include "../NN/MLP_Higgs_vs_TT_ML_CSV_2011.cxx"
#include "../NN/MLP_Higgs_vs_BKG_MM_CSV_2011.cxx"
#include "MLP_Higgs_vs_BKG_MM_N_CSV_2011.cxx"
#include "../NN/MLP_Higgs_vs_BKG_ML_CSV_2011.cxx"
#include "../NN/MLP_TT_vs_DY_MM_CSV_2011.cxx"
#include "MLP_TT_vs_DY_MM_N_CSV_2011.cxx"
#include "../NN/MLP_TT_vs_DY_ML_CSV_2011.cxx"

// Include NN traine on mm
// MM: CSV Medium Medium WP
// MM_N: CSV Medium Medium WP + narrow Mll
// ML: CSV Medium Loose WP
#include "../NN/MLP_Higgs_vs_DY_MM_CSV_2011_mm.cxx"
#include "MLP_Higgs_vs_DY_MM_N_CSV_2011_mm.cxx"
#include "../NN/MLP_Higgs_vs_DY_ML_CSV_2011_mm.cxx"
#include "../NN/MLP_Higgs_vs_ZZ_MM_CSV_2011_mm.cxx"
#include "MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm.cxx"
#include "../NN/MLP_Higgs_vs_ZZ_ML_CSV_2011_mm.cxx"
#include "../NN/MLP_Higgs_vs_TT_MM_CSV_2011_mm.cxx"
#include "MLP_Higgs_vs_TT_MM_N_CSV_2011_mm.cxx"
#include "../NN/MLP_Higgs_vs_TT_ML_CSV_2011_mm.cxx"
#include "../NN/MLP_Higgs_vs_BKG_MM_CSV_2011_mm.cxx"
#include "MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm.cxx"
#include "../NN/MLP_Higgs_vs_BKG_ML_CSV_2011_mm.cxx"
#include "../NN/MLP_TT_vs_DY_MM_CSV_2011_mm.cxx"
#include "../NN/MLP_TT_vs_DY_MM_N_CSV_2011_mm.cxx"
#include "../NN/MLP_TT_vs_DY_ML_CSV_2011_mm.cxx"

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


//----------------------------------------------------------------

#include <iostream>
#include <map>

//I'm not able to compile a root macro within RooFit stuff within ROOT
//#include "RooFit.h"
//#include "RooWorkspace.h"
// use this order for safety on library loading
//using namespace RooFit ;
//using namespace RooStats ;

//Switch to turn on or of the ZbbReweight
void InitZbbReweight();
double Compute1DReweight(TH1D*, double);

bool useZbbReweight = true;
TFile* file_reweight = 0;
TH1D* hZbbReweight_dijetdR_Mu = 0;
TH1D* hZbbReweight_bestzpt_Mu = 0;
TH1D* hZbbReweight_dijetdR_El = 0;
TH1D* hZbbReweight_bestzpt_El = 0;

 
 
//a) Copy list of variables here:   

   //ME variables
   Double_t        Pt_elplus;
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
   Int_t           flavour;
   long int        eventNumber;
   long int        runNumber;
   Double_t        Wgg;
   Double_t        Wqq;
   Double_t        Wtt;
   Double_t        Wtwb;
   Double_t        Wzz3;
   Double_t        Wzz0;
   Double_t        Whi3_115;
   Double_t        Whi0_115;
   Double_t        Whi3_120;
   Double_t        Whi0_120;
   Double_t        Whi3_125;
   Double_t        Whi0_125;
   Double_t        Whi3_130;
   Double_t        Whi0_130;
   Double_t        Whi3_135;
   Double_t        Whi0_135;
   //Extra variables MLP's, or variables not included in tree2

   Double_t        jetmetbjetMinCSVdisc;
   Double_t        jetmetbjetMaxCSVdisc;   
   Double_t        jetmetbjetProdCSVdisc;
   MLP_Higgs_vs_DY_MM_CSV_2011 *MLP_higgs_vs_DY_MM_ee = 0;
   MLP_Higgs_vs_DY_MM_N_CSV_2011_ee *MLP_higgs_vs_DY_MM_N_ee = 0;
   MLP_Higgs_vs_DY_ML_CSV_2011 *MLP_higgs_vs_DY_ML_ee = 0;
   MLP_Higgs_vs_ZZ_MM_CSV_2011 *MLP_higgs_vs_ZZ_MM_ee = 0;
   MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee *MLP_higgs_vs_ZZ_MM_N_ee = 0;
   MLP_Higgs_vs_ZZ_ML_CSV_2011 *MLP_higgs_vs_ZZ_ML_ee = 0;
   MLP_Higgs_vs_TT_MM_CSV_2011 *MLP_higgs_vs_TT_MM_ee = 0;
   MLP_Higgs_vs_TT_MM_N_CSV_2011_ee *MLP_higgs_vs_TT_MM_N_ee = 0;
   MLP_Higgs_vs_TT_ML_CSV_2011 *MLP_higgs_vs_TT_ML_ee = 0;
   MLP_TT_vs_DY_MM_CSV_2011 *MLP_TT_vs_DY_MM_ee = 0;
   MLP_TT_vs_DY_MM_N_CSV_2011 *MLP_TT_vs_DY_MM_N_ee = 0;
   MLP_TT_vs_DY_ML_CSV_2011 *MLP_TT_vs_DY_ML_ee = 0;
   MLP_Higgs_vs_BKG_MM_CSV_2011 *MLP_higgs_vs_BKG_MM_ee = 0;
   MLP_Higgs_vs_BKG_MM_N_CSV_2011 *MLP_higgs_vs_BKG_MM_N_ee = 0;
   MLP_Higgs_vs_BKG_ML_CSV_2011 *MLP_higgs_vs_BKG_ML_ee = 0;

   MLP_Higgs_vs_DY_MM_CSV_2011_mm *MLP_higgs_vs_DY_MM_mm = 0;
   MLP_Higgs_vs_DY_MM_N_CSV_2011_mm *MLP_higgs_vs_DY_MM_N_mm = 0;
   MLP_Higgs_vs_DY_ML_CSV_2011_mm *MLP_higgs_vs_DY_ML_mm = 0;
   MLP_Higgs_vs_ZZ_MM_CSV_2011_mm *MLP_higgs_vs_ZZ_MM_mm = 0;
   MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm *MLP_higgs_vs_ZZ_MM_N_mm = 0;
   MLP_Higgs_vs_ZZ_ML_CSV_2011_mm *MLP_higgs_vs_ZZ_ML_mm = 0;
   MLP_Higgs_vs_TT_MM_CSV_2011_mm *MLP_higgs_vs_TT_MM_mm = 0;
   MLP_Higgs_vs_TT_MM_N_CSV_2011_mm *MLP_higgs_vs_TT_MM_N_mm = 0;
   MLP_Higgs_vs_TT_ML_CSV_2011_mm *MLP_higgs_vs_TT_ML_mm = 0;
   MLP_TT_vs_DY_MM_CSV_2011_mm *MLP_TT_vs_DY_MM_mm = 0;
   MLP_TT_vs_DY_MM_N_CSV_2011_mm *MLP_TT_vs_DY_MM_N_mm = 0;
   MLP_TT_vs_DY_ML_CSV_2011_mm *MLP_TT_vs_DY_ML_mm = 0;
   MLP_Higgs_vs_BKG_MM_CSV_2011_mm *MLP_higgs_vs_BKG_MM_mm = 0;
   MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm *MLP_higgs_vs_BKG_MM_N_mm = 0;
   MLP_Higgs_vs_BKG_ML_CSV_2011_mm *MLP_higgs_vs_BKG_ML_mm = 0;
   
   MLP_Higgs_vs_DY_MM_N_CSV_2011_comb *MLP_higgs_vs_DY_MM_N_comb_2011 = 0;  
   MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb *MLP_higgs_vs_ZZ_MM_N_comb_2011 = 0;  
   MLP_Higgs_vs_TT_MM_N_CSV_2011_comb *MLP_higgs_vs_TT_MM_N_comb_2011 = 0;  
   MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb *MLP_higgs_vs_BKG_MM_N_comb_2011 = 0;

   MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125 *MLP_higgs_vs_DY_MM_N_comb = 0;  
   MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125 *MLP_higgs_vs_ZZ_MM_N_comb = 0;  
   MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125 *MLP_higgs_vs_TT_MM_N_comb = 0;  
   MLP_Higgs_vs_Bkg_ZH125_comb *MLP_higgs_vs_BKG_MM_N_comb = 0;

   MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600 *NEWMLP_higgs_vs_DY_MM_N_comb = 0;  
   MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000 *NEWMLP_higgs_vs_ZZ_MM_N_comb = 0;  
   MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500 *NEWMLP_higgs_vs_TT_MM_N_comb = 0;  
   MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000 *NEWMLP_higgs_vs_BKG_MM_N_comb = 0;
//test
   MLP_Higgs_vs_Bkg_ZH125_comb_1_10000 *MLP_higgs_vs_BKG_MM_N_comb_1_10000 = 0;
   MLP_Higgs_vs_Bkg_ZH125_comb_1_5000 *MLP_higgs_vs_BKG_MM_N_comb_1_5000 = 0;
   MLP_Higgs_vs_Bkg_ZH125_comb_2_10000 *MLP_higgs_vs_BKG_MM_N_comb_2_10000 = 0;
   MLP_Higgs_vs_Bkg_ZH125_comb_2_5000 *MLP_higgs_vs_BKG_MM_N_comb_2_5000 = 0;
   MLP_Higgs_vs_Bkg_ZH125_comb_3_5000 *MLP_higgs_vs_BKG_MM_N_comb_3_5000 = 0;
   MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000 *MLP_higgs_vs_BKG_MM_N_comb_2_3_2_10000 = 0;
   MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000 *MLP_higgs_vs_BKG_MM_N_comb_2_3_2_5000 = 0; 
   MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000 *MLP_higgs_vs_BKG_MM_N_comb_2_4_10000 = 0;
   MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000 *MLP_higgs_vs_BKG_MM_N_comb_2_5_3_1_1000 = 0;
   MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000 *MLP_higgs_vs_BKG_MM_N_comb_3_2_10000 = 0;


//-----------------------------------------------------------------------------
   Double_t mlphiggsvszbb_115_MM,mlphiggsvszbb_120_MM,mlphiggsvszbb_125_MM,mlphiggsvszbb_130_MM,mlphiggsvszbb_135_MM;
   Double_t mlphiggsvszz_115_MM,mlphiggsvszz_120_MM,mlphiggsvszz_125_MM,mlphiggsvszz_130_MM,mlphiggsvszz_135_MM;
   Double_t mlphiggsvstt_115_MM,mlphiggsvstt_120_MM,mlphiggsvstt_125_MM,mlphiggsvstt_130_MM,mlphiggsvstt_135_MM;
   Double_t mlphiggsvsbkg_115_MM,mlphiggsvsbkg_120_MM,mlphiggsvsbkg_125_MM,mlphiggsvsbkg_130_MM,mlphiggsvsbkg_135_MM;
   Double_t mlpZbbvsTT_MM;

   Double_t mlphiggsvszbb_115_mu_MM,mlphiggsvszbb_120_mu_MM,mlphiggsvszbb_125_mu_MM,mlphiggsvszbb_130_mu_MM,mlphiggsvszbb_135_mu_MM;
   Double_t mlphiggsvszz_115_mu_MM,mlphiggsvszz_120_mu_MM,mlphiggsvszz_125_mu_MM,mlphiggsvszz_130_mu_MM,mlphiggsvszz_135_mu_MM;
   Double_t mlphiggsvstt_115_mu_MM,mlphiggsvstt_120_mu_MM,mlphiggsvstt_125_mu_MM,mlphiggsvstt_130_mu_MM,mlphiggsvstt_135_mu_MM;
   Double_t mlphiggsvsbkg_115_mu_MM,mlphiggsvsbkg_120_mu_MM,mlphiggsvsbkg_125_mu_MM,mlphiggsvsbkg_130_mu_MM,mlphiggsvsbkg_135_mu_MM;
   Double_t mlpZbbvsTT_mu_MM;
  
   Double_t mlphiggsvszbb_115_comb_MM_N_2011,mlphiggsvszbb_120_comb_MM_N_2011,mlphiggsvszbb_125_comb_MM_N_2011,mlphiggsvszbb_130_comb_MM_N_2011,mlphiggsvszbb_135_comb_MM_N_2011;
   Double_t mlphiggsvszz_115_comb_MM_N_2011,mlphiggsvszz_120_comb_MM_N_2011,mlphiggsvszz_125_comb_MM_N_2011,mlphiggsvszz_130_comb_MM_N_2011,mlphiggsvszz_135_comb_MM_N_2011;
   Double_t mlphiggsvstt_115_comb_MM_N_2011,mlphiggsvstt_120_comb_MM_N_2011,mlphiggsvstt_125_comb_MM_N_2011,mlphiggsvstt_130_comb_MM_N_2011,mlphiggsvstt_135_comb_MM_N_2011;
   Double_t mlphiggsvsbkg_115_comb_MM_N_2011,mlphiggsvsbkg_120_comb_MM_N_2011,mlphiggsvsbkg_125_comb_MM_N_2011,mlphiggsvsbkg_130_comb_MM_N_2011,mlphiggsvsbkg_135_comb_MM_N_2011;

   Double_t mlphiggsvszbb_115_comb_MM_N,mlphiggsvszbb_120_comb_MM_N,mlphiggsvszbb_125_comb_MM_N,mlphiggsvszbb_130_comb_MM_N,mlphiggsvszbb_135_comb_MM_N;
   Double_t mlphiggsvszz_115_comb_MM_N,mlphiggsvszz_120_comb_MM_N,mlphiggsvszz_125_comb_MM_N,mlphiggsvszz_130_comb_MM_N,mlphiggsvszz_135_comb_MM_N;
   Double_t mlphiggsvstt_115_comb_MM_N,mlphiggsvstt_120_comb_MM_N,mlphiggsvstt_125_comb_MM_N,mlphiggsvstt_130_comb_MM_N,mlphiggsvstt_135_comb_MM_N;
   Double_t mlphiggsvsbkg_115_comb_MM_N,mlphiggsvsbkg_120_comb_MM_N,mlphiggsvsbkg_125_comb_MM_N,mlphiggsvsbkg_130_comb_MM_N,mlphiggsvsbkg_135_comb_MM_N;

   Double_t newmlphiggsvszbb_115_comb_MM_N,newmlphiggsvszbb_120_comb_MM_N,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszbb_130_comb_MM_N,newmlphiggsvszbb_135_comb_MM_N;
   Double_t newmlphiggsvszz_115_comb_MM_N,newmlphiggsvszz_120_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvszz_130_comb_MM_N,newmlphiggsvszz_135_comb_MM_N;
   Double_t newmlphiggsvstt_115_comb_MM_N,newmlphiggsvstt_120_comb_MM_N,newmlphiggsvstt_125_comb_MM_N,newmlphiggsvstt_130_comb_MM_N,newmlphiggsvstt_135_comb_MM_N;
   Double_t newmlphiggsvsbkg_115_comb_MM_N,newmlphiggsvsbkg_120_comb_MM_N,newmlphiggsvsbkg_125_comb_MM_N,newmlphiggsvsbkg_130_comb_MM_N,newmlphiggsvsbkg_135_comb_MM_N;
   
   Double_t mlphiggsvszbb_115_MM_N_comb,mlphiggsvszbb_120_MM_N_comb,mlphiggsvszbb_125_MM_N_comb,mlphiggsvszbb_130_MM_N_comb,mlphiggsvszbb_135_MM_N_comb;
   Double_t mlphiggsvszz_115_MM_N_comb,mlphiggsvszz_120_MM_N_comb,mlphiggsvszz_125_MM_N_comb,mlphiggsvszz_130_MM_N_comb,mlphiggsvszz_135_MM_N_comb;
   Double_t mlphiggsvstt_115_MM_N_comb,mlphiggsvstt_120_MM_N_comb,mlphiggsvstt_125_MM_N_comb,mlphiggsvstt_130_MM_N_comb,mlphiggsvstt_135_MM_N_comb;
   Double_t mlphiggsvsbkg_115_MM_N_comb,mlphiggsvsbkg_120_MM_N_comb,mlphiggsvsbkg_125_MM_N_comb,mlphiggsvsbkg_130_MM_N_comb,mlphiggsvsbkg_135_MM_N_comb;

   Double_t mlphiggsvszbb_115_MM_N,mlphiggsvszbb_120_MM_N,mlphiggsvszbb_125_MM_N,mlphiggsvszbb_130_MM_N,mlphiggsvszbb_135_MM_N;
   Double_t mlphiggsvszz_115_MM_N,mlphiggsvszz_120_MM_N,mlphiggsvszz_125_MM_N,mlphiggsvszz_130_MM_N,mlphiggsvszz_135_MM_N;
   Double_t mlphiggsvstt_115_MM_N,mlphiggsvstt_120_MM_N,mlphiggsvstt_125_MM_N,mlphiggsvstt_130_MM_N,mlphiggsvstt_135_MM_N;
   Double_t mlphiggsvsbkg_115_MM_N,mlphiggsvsbkg_120_MM_N,mlphiggsvsbkg_125_MM_N,mlphiggsvsbkg_130_MM_N,mlphiggsvsbkg_135_MM_N;
   Double_t mlpZbbvsTT_MM_N;

   Double_t mlphiggsvszbb_115_mu_MM_N,mlphiggsvszbb_120_mu_MM_N,mlphiggsvszbb_125_mu_MM_N,mlphiggsvszbb_130_mu_MM_N,mlphiggsvszbb_135_mu_MM_N;
   Double_t mlphiggsvszz_115_mu_MM_N,mlphiggsvszz_120_mu_MM_N,mlphiggsvszz_125_mu_MM_N,mlphiggsvszz_130_mu_MM_N,mlphiggsvszz_135_mu_MM_N;
   Double_t mlphiggsvstt_115_mu_MM_N,mlphiggsvstt_120_mu_MM_N,mlphiggsvstt_125_mu_MM_N,mlphiggsvstt_130_mu_MM_N,mlphiggsvstt_135_mu_MM_N;
   Double_t mlphiggsvsbkg_115_mu_MM_N,mlphiggsvsbkg_120_mu_MM_N,mlphiggsvsbkg_125_mu_MM_N,mlphiggsvsbkg_130_mu_MM_N,mlphiggsvsbkg_135_mu_MM_N;
   Double_t mlpZbbvsTT_mu_MM_N;

   Double_t mlphiggsvszbb_115_ML,mlphiggsvszbb_120_ML,mlphiggsvszbb_125_ML,mlphiggsvszbb_130_ML,mlphiggsvszbb_135_ML;
   Double_t mlphiggsvszz_115_ML,mlphiggsvszz_120_ML,mlphiggsvszz_125_ML,mlphiggsvszz_130_ML,mlphiggsvszz_135_ML;
   Double_t mlphiggsvstt_115_ML,mlphiggsvstt_120_ML,mlphiggsvstt_125_ML,mlphiggsvstt_130_ML,mlphiggsvstt_135_ML;
   Double_t mlphiggsvsbkg_115_ML,mlphiggsvsbkg_120_ML,mlphiggsvsbkg_125_ML,mlphiggsvsbkg_130_ML,mlphiggsvsbkg_135_ML;
   Double_t mlpZbbvsTT_ML;

   Double_t mlphiggsvszbb_115_mu_ML,mlphiggsvszbb_120_mu_ML,mlphiggsvszbb_125_mu_ML,mlphiggsvszbb_130_mu_ML,mlphiggsvszbb_135_mu_ML;
   Double_t mlphiggsvszz_115_mu_ML,mlphiggsvszz_120_mu_ML,mlphiggsvszz_125_mu_ML,mlphiggsvszz_130_mu_ML,mlphiggsvszz_135_mu_ML;
   Double_t mlphiggsvstt_115_mu_ML,mlphiggsvstt_120_mu_ML,mlphiggsvstt_125_mu_ML,mlphiggsvstt_130_mu_ML,mlphiggsvstt_135_mu_ML;
   Double_t mlphiggsvsbkg_115_mu_ML,mlphiggsvsbkg_120_mu_ML,mlphiggsvsbkg_125_mu_ML,mlphiggsvsbkg_130_mu_ML,mlphiggsvsbkg_135_mu_ML;
   Double_t mlpZbbvsTT_mu_ML;

//test
   Double_t mlphiggsvsbkg_125_comb_MM_N_1_10000;
   Double_t mlphiggsvsbkg_125_comb_MM_N_1_5000;
   Double_t mlphiggsvsbkg_125_comb_MM_N_2_10000;
   Double_t mlphiggsvsbkg_125_comb_MM_N_2_5000;
   Double_t mlphiggsvsbkg_125_comb_MM_N_3_5000;
   Double_t mlphiggsvsbkg_125_comb_MM_N_2_3_2_10000;
   Double_t mlphiggsvsbkg_125_comb_MM_N_2_3_2_5000;
   Double_t mlphiggsvsbkg_125_comb_MM_N_2_4_10000;
   Double_t mlphiggsvsbkg_125_comb_MM_N_2_5_3_1_1000;
   Double_t mlphiggsvsbkg_125_comb_MM_N_3_2_10000;

//---------------------------
   //Extra variables for reweighting stuff
   Double_t ZbbReweight_dijetdR;
   Double_t ZbbReweight_bestzpt;
   
   Double_t SumNN;
   Double_t ProdNN;
   Double_t SumWeightedNN;
   
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
  
   //sanitycut += " && " + conflictrunsRDS;
   
   MLP_higgs_vs_DY_MM_ee = new MLP_Higgs_vs_DY_MM_CSV_2011();
   MLP_higgs_vs_DY_MM_N_ee = new MLP_Higgs_vs_DY_MM_N_CSV_2011_ee();
   MLP_higgs_vs_DY_ML_ee = new MLP_Higgs_vs_DY_ML_CSV_2011();
   MLP_higgs_vs_ZZ_MM_ee = new MLP_Higgs_vs_ZZ_MM_CSV_2011();
   MLP_higgs_vs_ZZ_MM_N_ee = new MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee();
   MLP_higgs_vs_ZZ_ML_ee = new MLP_Higgs_vs_ZZ_ML_CSV_2011();
   MLP_higgs_vs_TT_MM_ee = new MLP_Higgs_vs_TT_MM_CSV_2011();
   MLP_higgs_vs_TT_MM_N_ee = new MLP_Higgs_vs_TT_MM_N_CSV_2011_ee();
   MLP_higgs_vs_TT_ML_ee = new MLP_Higgs_vs_TT_ML_CSV_2011();
   MLP_TT_vs_DY_MM_ee = new MLP_TT_vs_DY_MM_CSV_2011();
   MLP_TT_vs_DY_MM_N_ee = new MLP_TT_vs_DY_MM_N_CSV_2011();
   MLP_TT_vs_DY_ML_ee = new MLP_TT_vs_DY_ML_CSV_2011();
   MLP_higgs_vs_BKG_MM_ee = new MLP_Higgs_vs_BKG_MM_CSV_2011();
   MLP_higgs_vs_BKG_MM_N_ee = new MLP_Higgs_vs_BKG_MM_N_CSV_2011();
   MLP_higgs_vs_BKG_ML_ee = new MLP_Higgs_vs_BKG_ML_CSV_2011();

   MLP_higgs_vs_DY_MM_mm = new MLP_Higgs_vs_DY_MM_CSV_2011_mm();
   MLP_higgs_vs_DY_MM_N_mm = new MLP_Higgs_vs_DY_MM_N_CSV_2011_mm();
   MLP_higgs_vs_DY_ML_mm = new MLP_Higgs_vs_DY_ML_CSV_2011_mm();
   MLP_higgs_vs_ZZ_MM_mm = new MLP_Higgs_vs_ZZ_MM_CSV_2011_mm();
   MLP_higgs_vs_ZZ_MM_N_mm = new MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm();
   MLP_higgs_vs_ZZ_ML_mm = new MLP_Higgs_vs_ZZ_ML_CSV_2011_mm();
   MLP_higgs_vs_TT_MM_mm = new MLP_Higgs_vs_TT_MM_CSV_2011_mm();
   MLP_higgs_vs_TT_MM_N_mm = new MLP_Higgs_vs_TT_MM_N_CSV_2011_mm();
   MLP_higgs_vs_TT_ML_mm = new MLP_Higgs_vs_TT_ML_CSV_2011_mm();
   MLP_TT_vs_DY_MM_mm = new MLP_TT_vs_DY_MM_CSV_2011_mm();
   MLP_TT_vs_DY_MM_N_mm = new MLP_TT_vs_DY_MM_N_CSV_2011_mm();
   MLP_TT_vs_DY_ML_mm = new MLP_TT_vs_DY_ML_CSV_2011_mm();
   MLP_higgs_vs_BKG_MM_mm = new MLP_Higgs_vs_BKG_MM_CSV_2011_mm();
   MLP_higgs_vs_BKG_MM_N_mm = new MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm();
   MLP_higgs_vs_BKG_ML_mm = new MLP_Higgs_vs_BKG_ML_CSV_2011_mm();

   MLP_higgs_vs_DY_MM_N_comb_2011 = new MLP_Higgs_vs_DY_MM_N_CSV_2011_comb();
   MLP_higgs_vs_ZZ_MM_N_comb_2011 = new MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb();
   MLP_higgs_vs_TT_MM_N_comb_2011 = new MLP_Higgs_vs_TT_MM_N_CSV_2011_comb();
   MLP_higgs_vs_BKG_MM_N_comb_2011 = new MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb();

   MLP_higgs_vs_DY_MM_N_comb = new MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125();
   MLP_higgs_vs_ZZ_MM_N_comb = new MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125();
   MLP_higgs_vs_TT_MM_N_comb = new MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125();
   MLP_higgs_vs_BKG_MM_N_comb = new MLP_Higgs_vs_Bkg_ZH125_comb();

   NEWMLP_higgs_vs_DY_MM_N_comb = new MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600();
   NEWMLP_higgs_vs_ZZ_MM_N_comb = new MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000();
   NEWMLP_higgs_vs_TT_MM_N_comb = new MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500();
   NEWMLP_higgs_vs_BKG_MM_N_comb = new MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000();
   //test
   MLP_higgs_vs_BKG_MM_N_comb_1_10000 = new MLP_Higgs_vs_Bkg_ZH125_comb_1_10000();
   MLP_higgs_vs_BKG_MM_N_comb_1_5000 = new MLP_Higgs_vs_Bkg_ZH125_comb_1_5000();
   MLP_higgs_vs_BKG_MM_N_comb_2_10000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_10000();
   MLP_higgs_vs_BKG_MM_N_comb_2_5000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_5000();
   MLP_higgs_vs_BKG_MM_N_comb_3_5000 = new MLP_Higgs_vs_Bkg_ZH125_comb_3_5000();
   MLP_higgs_vs_BKG_MM_N_comb_2_3_2_10000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000();
   MLP_higgs_vs_BKG_MM_N_comb_2_3_2_5000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000();
   MLP_higgs_vs_BKG_MM_N_comb_2_4_10000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000();
   MLP_higgs_vs_BKG_MM_N_comb_2_5_3_1_1000 = new MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000();
   MLP_higgs_vs_BKG_MM_N_comb_3_2_10000 = new MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000();   
   
   
   //-----------------------------------------------------------------------
   // Input files location
   TString folder = "/nfs/user/acaudron/Tree2_537/";
   TString folderB = "/nfs/user/acaudron/Tree2_537/";
   //RDS location
   TString folder2 = "/nfs/user/acaudron/RDS537/";

   TFile* f_RDS  = new TFile(folder2+"File_rds_zbb_"+InputFile+".root");
   TTree* t_RDS  = (TTree*) f_RDS->Get("rds_zbb");  
   
   TString mename = folder+"ME_zbb_" + InputFile + ".root";
   //mename.ReplaceAll("A_DATA", "_DATA");
   //mename.ReplaceAll("B_DATA", "_DATA");

   TFile* f_ME  = new TFile(mename);
   TTree* t_ME    = (TTree*)f_ME->Get("tree2");  
   
   TFile *f_RDSME = new TFile(folderB+"Tree_rdsME_"+InputFile +".root", "RECREATE");
   TTree *t_RDSME = t_RDS->CloneTree(0);
   t_RDSME->SetTitle("merged zbb-ME tree");

   cout<<"read file : "<<f_RDS->GetName()<<endl;
   //-----------------------------------------------------------------------

   //Initialize histograms for reweighting
   if (useZbbReweight){
     InitZbbReweight();
   }

//b) Define branches
   t_RDSME->Branch("Pt_elplus", &Pt_elplus, "Pt_elplus/D");
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
   t_RDSME->Branch("flavour", &flavour, "flavour/I");
   t_RDSME->Branch("eventNumber", &eventNumber, "eventNumber/l");
   t_RDSME->Branch("runNumber", &runNumber, "runNumber/l");
   t_RDSME->Branch("Wgg", &Wgg, "Wgg/D");
   t_RDSME->Branch("Wqq", &Wqq, "Wqq/D");
   t_RDSME->Branch("Wtt", &Wtt, "Wtt/D");
   t_RDSME->Branch("Wtwb", &Wtwb, "Wtwb/D");
   t_RDSME->Branch("Wzz3", &Wzz3, "Wzz3/D");
   t_RDSME->Branch("Wzz0", &Wzz0, "Wzz0/D");
   t_RDSME->Branch("Whi3_115", &Whi3_115, "Whi3_115/D");
   t_RDSME->Branch("Whi0_115", &Whi0_115, "Whi0_115/D");
   t_RDSME->Branch("Whi3_120", &Whi3_120, "Whi3_120/D");
   t_RDSME->Branch("Whi0_120", &Whi0_120, "Whi0_120/D");
   t_RDSME->Branch("Whi3_125", &Whi3_125, "Whi3_125/D");
   t_RDSME->Branch("Whi0_125", &Whi0_125, "Whi0_125/D");
   t_RDSME->Branch("Whi3_130", &Whi3_130, "Whi3_130/D");
   t_RDSME->Branch("Whi0_130", &Whi0_130, "Whi0_130/D");
   t_RDSME->Branch("Whi3_135", &Whi3_135, "Whi3_135/D");
   t_RDSME->Branch("Whi0_135", &Whi0_135, "Whi0_135/D");

   //Extra variables MLP's or variables not included in tree2
   t_RDSME->Branch("jetmetbjetMinCSVdisc",&jetmetbjetMinCSVdisc,"jetmetbjetMinCSVdisc/D");
   t_RDSME->Branch("jetmetbjetMaxCSVdisc",&jetmetbjetMaxCSVdisc,"jetmetbjetMaxCSVdisc/D");
   t_RDSME->Branch("jetmetbjetProdCSVdisc",&jetmetbjetProdCSVdisc,"jetmetbjetProdCSVdisc/D");     

   t_RDSME->Branch("mlphiggsvszbb_125_MM" , &mlphiggsvszbb_125_MM,"mlphiggsvszbb_125_MM/D");
   t_RDSME->Branch("mlphiggsvstt_125_MM" , &mlphiggsvstt_125_MM,"mlphiggsvstt_125_MM/D");
   t_RDSME->Branch("mlphiggsvszz_125_MM" , &mlphiggsvszz_125_MM,"mlphiggsvszz_125_MM/D");
   t_RDSME->Branch("mlphiggsvszbb_125_MM_N" , &mlphiggsvszbb_125_MM_N,"mlphiggsvszbb_125_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_125_MM_N" , &mlphiggsvstt_125_MM_N,"mlphiggsvstt_125_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_125_MM_N" , &mlphiggsvszz_125_MM_N,"mlphiggsvszz_125_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_125_ML" , &mlphiggsvszbb_125_ML,"mlphiggsvszbb_125_ML/D");
   t_RDSME->Branch("mlphiggsvstt_125_ML" , &mlphiggsvstt_125_ML,"mlphiggsvstt_125_ML/D");
   t_RDSME->Branch("mlphiggsvszz_125_ML" , &mlphiggsvszz_125_ML,"mlphiggsvszz_125_ML/D");
   t_RDSME->Branch("mlphiggsvszbb_115_MM" , &mlphiggsvszbb_115_MM,"mlphiggsvszbb_115_MM/D");
   t_RDSME->Branch("mlphiggsvstt_115_MM" , &mlphiggsvstt_115_MM,"mlphiggsvstt_115_MM/D");
   t_RDSME->Branch("mlphiggsvszz_115_MM" , &mlphiggsvszz_115_MM,"mlphiggsvszz_115_MM/D");
   t_RDSME->Branch("mlphiggsvszbb_115_MM_N" , &mlphiggsvszbb_115_MM_N,"mlphiggsvszbb_115_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_115_MM_N" , &mlphiggsvstt_115_MM_N,"mlphiggsvstt_115_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_115_MM_N" , &mlphiggsvszz_115_MM_N,"mlphiggsvszz_115_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_115_ML" , &mlphiggsvszbb_115_ML,"mlphiggsvszbb_115_ML/D");
   t_RDSME->Branch("mlphiggsvstt_115_ML" , &mlphiggsvstt_115_ML,"mlphiggsvstt_115_ML/D");
   t_RDSME->Branch("mlphiggsvszz_115_ML" , &mlphiggsvszz_115_ML,"mlphiggsvszz_115_ML/D");
   t_RDSME->Branch("mlphiggsvszbb_120_MM" , &mlphiggsvszbb_120_MM,"mlphiggsvszbb_120_MM/D");
   t_RDSME->Branch("mlphiggsvstt_120_MM" , &mlphiggsvstt_120_MM,"mlphiggsvstt_120_MM/D");
   t_RDSME->Branch("mlphiggsvszz_120_MM" , &mlphiggsvszz_120_MM,"mlphiggsvszz_120_MM/D");
   t_RDSME->Branch("mlphiggsvszbb_120_MM_N" , &mlphiggsvszbb_120_MM_N,"mlphiggsvszbb_120_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_120_MM_N" , &mlphiggsvstt_120_MM_N,"mlphiggsvstt_120_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_120_MM_N" , &mlphiggsvszz_120_MM_N,"mlphiggsvszz_120_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_120_ML" , &mlphiggsvszbb_120_ML,"mlphiggsvszbb_120_ML/D");
   t_RDSME->Branch("mlphiggsvstt_120_ML" , &mlphiggsvstt_120_ML,"mlphiggsvstt_120_ML/D");
   t_RDSME->Branch("mlphiggsvszz_120_ML" , &mlphiggsvszz_120_ML,"mlphiggsvszz_120_ML/D");
   t_RDSME->Branch("mlphiggsvszbb_130_MM" , &mlphiggsvszbb_130_MM,"mlphiggsvszbb_130_MM/D");
   t_RDSME->Branch("mlphiggsvstt_130_MM" , &mlphiggsvstt_130_MM,"mlphiggsvstt_130_MM/D");
   t_RDSME->Branch("mlphiggsvszz_130_MM" , &mlphiggsvszz_130_MM,"mlphiggsvszz_130_MM/D");
   t_RDSME->Branch("mlphiggsvszbb_130_MM_N" , &mlphiggsvszbb_130_MM_N,"mlphiggsvszbb_130_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_130_MM_N" , &mlphiggsvstt_130_MM_N,"mlphiggsvstt_130_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_130_MM_N" , &mlphiggsvszz_130_MM_N,"mlphiggsvszz_130_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_130_ML" , &mlphiggsvszbb_130_ML,"mlphiggsvszbb_130_ML/D");
   t_RDSME->Branch("mlphiggsvstt_130_ML" , &mlphiggsvstt_130_ML,"mlphiggsvstt_130_ML/D");
   t_RDSME->Branch("mlphiggsvszz_130_ML" , &mlphiggsvszz_130_ML,"mlphiggsvszz_130_ML/D");
   t_RDSME->Branch("mlphiggsvszbb_135_MM" , &mlphiggsvszbb_135_MM,"mlphiggsvszbb_135_MM/D");
   t_RDSME->Branch("mlphiggsvstt_135_MM" , &mlphiggsvstt_135_MM,"mlphiggsvstt_135_MM/D");
   t_RDSME->Branch("mlphiggsvszz_135_MM" , &mlphiggsvszz_135_MM,"mlphiggsvszz_135_MM/D");
   t_RDSME->Branch("mlphiggsvszbb_135_MM_N" , &mlphiggsvszbb_135_MM_N,"mlphiggsvszbb_135_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_135_MM_N" , &mlphiggsvstt_135_MM_N,"mlphiggsvstt_135_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_135_MM_N" , &mlphiggsvszz_135_MM_N,"mlphiggsvszz_135_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_135_ML" , &mlphiggsvszbb_135_ML,"mlphiggsvszbb_135_ML/D");
   t_RDSME->Branch("mlphiggsvstt_135_ML" , &mlphiggsvstt_135_ML,"mlphiggsvstt_135_ML/D");
   t_RDSME->Branch("mlphiggsvszz_135_ML" , &mlphiggsvszz_135_ML,"mlphiggsvszz_135_ML/D");


   t_RDSME->Branch("mlphiggsvszbb_125_comb_MM_N_2011" , &mlphiggsvszbb_125_comb_MM_N_2011,"mlphiggsvszbb_125_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvszz_125_comb_MM_N_2011" , &mlphiggsvszz_125_comb_MM_N_2011,"mlphiggsvszz_125_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvstt_125_comb_MM_N_2011" , &mlphiggsvstt_125_comb_MM_N_2011,"mlphiggsvstt_125_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N_2011" , &mlphiggsvsbkg_125_comb_MM_N_2011,"mlphiggsvsbkg_125_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvszbb_115_comb_MM_N_2011" , &mlphiggsvszbb_115_comb_MM_N_2011,"mlphiggsvszbb_115_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvszz_115_comb_MM_N_2011" , &mlphiggsvszz_115_comb_MM_N_2011,"mlphiggsvszz_115_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvstt_115_comb_MM_N_2011" , &mlphiggsvstt_115_comb_MM_N_2011,"mlphiggsvstt_115_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvsbkg_115_comb_MM_N_2011" , &mlphiggsvsbkg_115_comb_MM_N_2011,"mlphiggsvsbkg_115_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvszbb_135_comb_MM_N_2011" , &mlphiggsvszbb_135_comb_MM_N_2011,"mlphiggsvszbb_135_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvszz_135_comb_MM_N_2011" , &mlphiggsvszz_135_comb_MM_N_2011,"mlphiggsvszz_135_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvstt_135_comb_MM_N_2011" , &mlphiggsvstt_135_comb_MM_N_2011,"mlphiggsvstt_135_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvsbkg_135_comb_MM_N_2011" , &mlphiggsvsbkg_135_comb_MM_N_2011,"mlphiggsvsbkg_135_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvszbb_130_comb_MM_N_2011" , &mlphiggsvszbb_130_comb_MM_N_2011,"mlphiggsvszbb_130_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvszz_130_comb_MM_N_2011" , &mlphiggsvszz_130_comb_MM_N_2011,"mlphiggsvszz_130_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvstt_130_comb_MM_N_2011" , &mlphiggsvstt_130_comb_MM_N_2011,"mlphiggsvstt_130_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvsbkg_130_comb_MM_N_2011" , &mlphiggsvsbkg_130_comb_MM_N_2011,"mlphiggsvsbkg_130_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvszbb_120_comb_MM_N_2011" , &mlphiggsvszbb_120_comb_MM_N_2011,"mlphiggsvszbb_120_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvszz_120_comb_MM_N_2011" , &mlphiggsvszz_120_comb_MM_N_2011,"mlphiggsvszz_120_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvstt_120_comb_MM_N_2011" , &mlphiggsvstt_120_comb_MM_N_2011,"mlphiggsvstt_120_comb_MM_N_2011/D");
   t_RDSME->Branch("mlphiggsvsbkg_120_comb_MM_N_2011" , &mlphiggsvsbkg_120_comb_MM_N_2011,"mlphiggsvsbkg_120_comb_MM_N_2011/D");


   t_RDSME->Branch("mlphiggsvszbb_125_comb_MM_N" , &mlphiggsvszbb_125_comb_MM_N,"mlphiggsvszbb_125_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_125_comb_MM_N" , &mlphiggsvszz_125_comb_MM_N,"mlphiggsvszz_125_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_125_comb_MM_N" , &mlphiggsvstt_125_comb_MM_N,"mlphiggsvstt_125_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N" , &mlphiggsvsbkg_125_comb_MM_N,"mlphiggsvsbkg_125_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_115_comb_MM_N" , &mlphiggsvszbb_115_comb_MM_N,"mlphiggsvszbb_115_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_115_comb_MM_N" , &mlphiggsvszz_115_comb_MM_N,"mlphiggsvszz_115_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_115_comb_MM_N" , &mlphiggsvstt_115_comb_MM_N,"mlphiggsvstt_115_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_115_comb_MM_N" , &mlphiggsvsbkg_115_comb_MM_N,"mlphiggsvsbkg_115_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_135_comb_MM_N" , &mlphiggsvszbb_135_comb_MM_N,"mlphiggsvszbb_135_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_135_comb_MM_N" , &mlphiggsvszz_135_comb_MM_N,"mlphiggsvszz_135_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_135_comb_MM_N" , &mlphiggsvstt_135_comb_MM_N,"mlphiggsvstt_135_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_135_comb_MM_N" , &mlphiggsvsbkg_135_comb_MM_N,"mlphiggsvsbkg_135_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_130_comb_MM_N" , &mlphiggsvszbb_130_comb_MM_N,"mlphiggsvszbb_130_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_130_comb_MM_N" , &mlphiggsvszz_130_comb_MM_N,"mlphiggsvszz_130_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_130_comb_MM_N" , &mlphiggsvstt_130_comb_MM_N,"mlphiggsvstt_130_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_130_comb_MM_N" , &mlphiggsvsbkg_130_comb_MM_N,"mlphiggsvsbkg_130_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_120_comb_MM_N" , &mlphiggsvszbb_120_comb_MM_N,"mlphiggsvszbb_120_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_120_comb_MM_N" , &mlphiggsvszz_120_comb_MM_N,"mlphiggsvszz_120_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_120_comb_MM_N" , &mlphiggsvstt_120_comb_MM_N,"mlphiggsvstt_120_comb_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_120_comb_MM_N" , &mlphiggsvsbkg_120_comb_MM_N,"mlphiggsvsbkg_120_comb_MM_N/D");

   t_RDSME->Branch("newmlphiggsvszbb_125_comb_MM_N" , &newmlphiggsvszbb_125_comb_MM_N,"newmlphiggsvszbb_125_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvszz_125_comb_MM_N" , &newmlphiggsvszz_125_comb_MM_N,"newmlphiggsvszz_125_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvstt_125_comb_MM_N" , &newmlphiggsvstt_125_comb_MM_N,"newmlphiggsvstt_125_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvsbkg_125_comb_MM_N" , &newmlphiggsvsbkg_125_comb_MM_N,"newmlphiggsvsbkg_125_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvszbb_115_comb_MM_N" , &newmlphiggsvszbb_115_comb_MM_N,"newmlphiggsvszbb_115_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvszz_115_comb_MM_N" , &newmlphiggsvszz_115_comb_MM_N,"newmlphiggsvszz_115_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvstt_115_comb_MM_N" , &newmlphiggsvstt_115_comb_MM_N,"newmlphiggsvstt_115_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvsbkg_115_comb_MM_N" , &newmlphiggsvsbkg_115_comb_MM_N,"newmlphiggsvsbkg_115_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvszbb_135_comb_MM_N" , &newmlphiggsvszbb_135_comb_MM_N,"newmlphiggsvszbb_135_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvszz_135_comb_MM_N" , &newmlphiggsvszz_135_comb_MM_N,"newmlphiggsvszz_135_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvstt_135_comb_MM_N" , &newmlphiggsvstt_135_comb_MM_N,"newmlphiggsvstt_135_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvsbkg_135_comb_MM_N" , &newmlphiggsvsbkg_135_comb_MM_N,"newmlphiggsvsbkg_135_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvszbb_130_comb_MM_N" , &newmlphiggsvszbb_130_comb_MM_N,"newmlphiggsvszbb_130_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvszz_130_comb_MM_N" , &newmlphiggsvszz_130_comb_MM_N,"newmlphiggsvszz_130_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvstt_130_comb_MM_N" , &newmlphiggsvstt_130_comb_MM_N,"newmlphiggsvstt_130_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvsbkg_130_comb_MM_N" , &newmlphiggsvsbkg_130_comb_MM_N,"newmlphiggsvsbkg_130_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvszbb_120_comb_MM_N" , &newmlphiggsvszbb_120_comb_MM_N,"newmlphiggsvszbb_120_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvszz_120_comb_MM_N" , &newmlphiggsvszz_120_comb_MM_N,"newmlphiggsvszz_120_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvstt_120_comb_MM_N" , &newmlphiggsvstt_120_comb_MM_N,"newmlphiggsvstt_120_comb_MM_N/D");
   t_RDSME->Branch("newmlphiggsvsbkg_120_comb_MM_N" , &newmlphiggsvsbkg_120_comb_MM_N,"newmlphiggsvsbkg_120_comb_MM_N/D");
   

   t_RDSME->Branch("mlphiggsvszbb_125_mu_MM" , &mlphiggsvszbb_125_mu_MM,"mlphiggsvszbb_125_mu_MM/D");
   t_RDSME->Branch("mlphiggsvstt_125_mu_MM" , &mlphiggsvstt_125_mu_MM,"mlphiggsvstt_125_mu_MM/D");
   t_RDSME->Branch("mlphiggsvszz_125_mu_MM" , &mlphiggsvszz_125_mu_MM,"mlphiggsvszz_125_mu_MM/D");
   t_RDSME->Branch("mlphiggsvszbb_125_mu_MM_N" , &mlphiggsvszbb_125_mu_MM_N,"mlphiggsvszbb_125_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_125_mu_MM_N" , &mlphiggsvstt_125_mu_MM_N,"mlphiggsvstt_125_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_125_mu_MM_N" , &mlphiggsvszz_125_mu_MM_N,"mlphiggsvszz_125_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_125_mu_ML" , &mlphiggsvszbb_125_mu_ML,"mlphiggsvszbb_125_mu_ML/D");
   t_RDSME->Branch("mlphiggsvstt_125_mu_ML" , &mlphiggsvstt_125_mu_ML,"mlphiggsvstt_125_mu_ML/D");
   t_RDSME->Branch("mlphiggsvszz_125_mu_ML" , &mlphiggsvszz_125_mu_ML,"mlphiggsvszz_125_mu_ML/D");
   t_RDSME->Branch("mlphiggsvszbb_115_mu_MM" , &mlphiggsvszbb_115_mu_MM,"mlphiggsvszbb_115_mu_MM/D");
   t_RDSME->Branch("mlphiggsvstt_115_mu_MM" , &mlphiggsvstt_115_mu_MM,"mlphiggsvstt_115_mu_MM/D");
   t_RDSME->Branch("mlphiggsvszz_115_mu_MM" , &mlphiggsvszz_115_mu_MM,"mlphiggsvszz_115_mu_MM/D");
   t_RDSME->Branch("mlphiggsvszbb_115_mu_MM_N" , &mlphiggsvszbb_115_mu_MM_N,"mlphiggsvszbb_115_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_115_mu_MM_N" , &mlphiggsvstt_115_mu_MM_N,"mlphiggsvstt_115_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_115_mu_MM_N" , &mlphiggsvszz_115_mu_MM_N,"mlphiggsvszz_115_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_115_mu_ML" , &mlphiggsvszbb_115_mu_ML,"mlphiggsvszbb_115_mu_ML/D");
   t_RDSME->Branch("mlphiggsvstt_115_mu_ML" , &mlphiggsvstt_115_mu_ML,"mlphiggsvstt_115_mu_ML/D");
   t_RDSME->Branch("mlphiggsvszz_115_mu_ML" , &mlphiggsvszz_115_mu_ML,"mlphiggsvszz_115_mu_ML/D");
   t_RDSME->Branch("mlphiggsvszbb_120_mu_MM" , &mlphiggsvszbb_120_mu_MM,"mlphiggsvszbb_120_mu_MM/D");
   t_RDSME->Branch("mlphiggsvstt_120_mu_MM" , &mlphiggsvstt_120_mu_MM,"mlphiggsvstt_120_mu_MM/D");
   t_RDSME->Branch("mlphiggsvszz_120_mu_MM" , &mlphiggsvszz_120_mu_MM,"mlphiggsvszz_120_mu_MM/D");
   t_RDSME->Branch("mlphiggsvszbb_120_mu_MM_N" , &mlphiggsvszbb_120_mu_MM_N,"mlphiggsvszbb_120_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_120_mu_MM_N" , &mlphiggsvstt_120_mu_MM_N,"mlphiggsvstt_120_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_120_mu_MM_N" , &mlphiggsvszz_120_mu_MM_N,"mlphiggsvszz_120_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_120_mu_ML" , &mlphiggsvszbb_120_mu_ML,"mlphiggsvszbb_120_mu_ML/D");
   t_RDSME->Branch("mlphiggsvstt_120_mu_ML" , &mlphiggsvstt_120_mu_ML,"mlphiggsvstt_120_mu_ML/D");
   t_RDSME->Branch("mlphiggsvszz_120_mu_ML" , &mlphiggsvszz_120_mu_ML,"mlphiggsvszz_120_mu_ML/D");
   t_RDSME->Branch("mlphiggsvszbb_130_mu_MM" , &mlphiggsvszbb_130_mu_MM,"mlphiggsvszbb_130_mu_MM/D");
   t_RDSME->Branch("mlphiggsvstt_130_mu_MM" , &mlphiggsvstt_130_mu_MM,"mlphiggsvstt_130_mu_MM/D");
   t_RDSME->Branch("mlphiggsvszz_130_mu_MM" , &mlphiggsvszz_130_mu_MM,"mlphiggsvszz_130_mu_MM/D");
   t_RDSME->Branch("mlphiggsvszbb_130_mu_MM_N" , &mlphiggsvszbb_130_mu_MM_N,"mlphiggsvszbb_130_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_130_mu_MM_N" , &mlphiggsvstt_130_mu_MM_N,"mlphiggsvstt_130_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_130_mu_MM_N" , &mlphiggsvszz_130_mu_MM_N,"mlphiggsvszz_130_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_130_mu_ML" , &mlphiggsvszbb_130_mu_ML,"mlphiggsvszbb_130_mu_ML/D");
   t_RDSME->Branch("mlphiggsvstt_130_mu_ML" , &mlphiggsvstt_130_mu_ML,"mlphiggsvstt_130_mu_ML/D");
   t_RDSME->Branch("mlphiggsvszz_130_mu_ML" , &mlphiggsvszz_130_mu_ML,"mlphiggsvszz_130_mu_ML/D");
   t_RDSME->Branch("mlphiggsvszbb_135_mu_MM" , &mlphiggsvszbb_135_mu_MM,"mlphiggsvszbb_135_mu_MM/D");
   t_RDSME->Branch("mlphiggsvstt_135_mu_MM" , &mlphiggsvstt_135_mu_MM,"mlphiggsvstt_135_mu_MM/D");
   t_RDSME->Branch("mlphiggsvszz_135_mu_MM" , &mlphiggsvszz_135_mu_MM,"mlphiggsvszz_135_mu_MM/D");
   t_RDSME->Branch("mlphiggsvszbb_135_mu_MM_N" , &mlphiggsvszbb_135_mu_MM_N,"mlphiggsvszbb_135_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvstt_135_mu_MM_N" , &mlphiggsvstt_135_mu_MM_N,"mlphiggsvstt_135_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvszz_135_mu_MM_N" , &mlphiggsvszz_135_mu_MM_N,"mlphiggsvszz_135_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvszbb_135_mu_ML" , &mlphiggsvszbb_135_mu_ML,"mlphiggsvszbb_135_mu_ML/D");
   t_RDSME->Branch("mlphiggsvstt_135_mu_ML" , &mlphiggsvstt_135_mu_ML,"mlphiggsvstt_135_mu_ML/D");
   t_RDSME->Branch("mlphiggsvszz_135_mu_ML" , &mlphiggsvszz_135_mu_ML,"mlphiggsvszz_135_mu_ML/D");

   t_RDSME->Branch("mlphiggsvsbkg_115_mu_ML" , &mlphiggsvsbkg_115_mu_ML,"mlphiggsvsbkg_115_mu_ML/D");
   t_RDSME->Branch("mlphiggsvsbkg_115_mu_MM" , &mlphiggsvsbkg_115_mu_MM,"mlphiggsvsbkg_115_mu_MM/D");
   t_RDSME->Branch("mlphiggsvsbkg_115_mu_MM_N" , &mlphiggsvsbkg_115_mu_MM_N,"mlphiggsvsbkg_115_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_120_mu_ML" , &mlphiggsvsbkg_120_mu_ML,"mlphiggsvsbkg_120_mu_ML/D");
   t_RDSME->Branch("mlphiggsvsbkg_120_mu_MM" , &mlphiggsvsbkg_120_mu_MM,"mlphiggsvsbkg_120_mu_MM/D");
   t_RDSME->Branch("mlphiggsvsbkg_120_mu_MM_N" , &mlphiggsvsbkg_120_mu_MM_N,"mlphiggsvsbkg_120_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_mu_ML" , &mlphiggsvsbkg_125_mu_ML,"mlphiggsvsbkg_125_mu_ML/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_mu_MM" , &mlphiggsvsbkg_125_mu_MM,"mlphiggsvsbkg_125_mu_MM/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_mu_MM_N" , &mlphiggsvsbkg_125_mu_MM_N,"mlphiggsvsbkg_125_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_130_mu_ML" , &mlphiggsvsbkg_130_mu_ML,"mlphiggsvsbkg_130_mu_ML/D");
   t_RDSME->Branch("mlphiggsvsbkg_130_mu_MM" , &mlphiggsvsbkg_130_mu_MM,"mlphiggsvsbkg_130_mu_MM/D");
   t_RDSME->Branch("mlphiggsvsbkg_130_mu_MM_N" , &mlphiggsvsbkg_130_mu_MM_N,"mlphiggsvsbkg_130_mu_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_135_mu_ML" , &mlphiggsvsbkg_135_mu_ML,"mlphiggsvsbkg_135_mu_ML/D");
   t_RDSME->Branch("mlphiggsvsbkg_135_mu_MM" , &mlphiggsvsbkg_135_mu_MM,"mlphiggsvsbkg_135_mu_MM/D");
   t_RDSME->Branch("mlphiggsvsbkg_135_mu_MM_N" , &mlphiggsvsbkg_135_mu_MM_N,"mlphiggsvsbkg_135_mu_MM_N/D");


   t_RDSME->Branch("mlphiggsvsbkg_115_ML" , &mlphiggsvsbkg_115_ML,"mlphiggsvsbkg_115_ML/D");
   t_RDSME->Branch("mlphiggsvsbkg_115_MM" , &mlphiggsvsbkg_115_MM,"mlphiggsvsbkg_115_MM/D");
   t_RDSME->Branch("mlphiggsvsbkg_115_MM_N" , &mlphiggsvsbkg_115_MM_N,"mlphiggsvsbkg_115_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_120_ML" , &mlphiggsvsbkg_120_ML,"mlphiggsvsbkg_120_ML/D");
   t_RDSME->Branch("mlphiggsvsbkg_120_MM" , &mlphiggsvsbkg_120_MM,"mlphiggsvsbkg_120_MM/D");
   t_RDSME->Branch("mlphiggsvsbkg_120_MM_N" , &mlphiggsvsbkg_120_MM_N,"mlphiggsvsbkg_120_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_ML" , &mlphiggsvsbkg_125_ML,"mlphiggsvsbkg_125_ML/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_MM" , &mlphiggsvsbkg_125_MM,"mlphiggsvsbkg_125_MM/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_MM_N" , &mlphiggsvsbkg_125_MM_N,"mlphiggsvsbkg_125_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_130_ML" , &mlphiggsvsbkg_130_ML,"mlphiggsvsbkg_130_ML/D");
   t_RDSME->Branch("mlphiggsvsbkg_130_MM" , &mlphiggsvsbkg_130_MM,"mlphiggsvsbkg_130_MM/D");
   t_RDSME->Branch("mlphiggsvsbkg_130_MM_N" , &mlphiggsvsbkg_130_MM_N,"mlphiggsvsbkg_130_MM_N/D");
   t_RDSME->Branch("mlphiggsvsbkg_135_ML" , &mlphiggsvsbkg_135_ML,"mlphiggsvsbkg_135_ML/D");
   t_RDSME->Branch("mlphiggsvsbkg_135_MM" , &mlphiggsvsbkg_135_MM,"mlphiggsvsbkg_135_MM/D");
   t_RDSME->Branch("mlphiggsvsbkg_135_MM_N" , &mlphiggsvsbkg_135_MM_N,"mlphiggsvsbkg_135_MM_N/D");

//test
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N_1_10000", &mlphiggsvsbkg_125_comb_MM_N_1_10000,"mlphiggsvsbkg_125_comb_MM_N_1_10000/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N_1_5000", &mlphiggsvsbkg_125_comb_MM_N_1_5000,"mlphiggsvsbkg_125_comb_MM_N_1_5000/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N_2_10000", &mlphiggsvsbkg_125_comb_MM_N_2_10000,"mlphiggsvsbkg_125_comb_MM_N_2_10000/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N_2_5000", &mlphiggsvsbkg_125_comb_MM_N_2_5000,"mlphiggsvsbkg_125_comb_MM_N_2_5000/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N_3_5000", &mlphiggsvsbkg_125_comb_MM_N_3_5000,"mlphiggsvsbkg_125_comb_MM_N_3_5000/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N_2_3_2_10000", &mlphiggsvsbkg_125_comb_MM_N_2_3_2_10000,"mlphiggsvsbkg_125_comb_MM_N_2_3_2_10000/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N_2_3_2_5000", &mlphiggsvsbkg_125_comb_MM_N_2_3_2_5000,"mlphiggsvsbkg_125_comb_MM_N_2_3_2_5000/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N_2_4_10000", &mlphiggsvsbkg_125_comb_MM_N_2_4_10000,"mlphiggsvsbkg_125_comb_MM_N_2_4_10000/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N_2_5_3_1_1000", &mlphiggsvsbkg_125_comb_MM_N_2_5_3_1_1000,"mlphiggsvsbkg_125_comb_MM_N_2_5_3_1_1000/D");
   t_RDSME->Branch("mlphiggsvsbkg_125_comb_MM_N_3_2_10000", &mlphiggsvsbkg_125_comb_MM_N_3_2_10000,"mlphiggsvsbkg_125_comb_MM_N_3_2_10000/D");



   t_RDSME->Branch("mlpZbbvsTT_MM" , &mlpZbbvsTT_MM,"mlpZbbvsTT_MM/D");
   t_RDSME->Branch("mlpZbbvsTT_MM_N" , &mlpZbbvsTT_MM_N,"mlpZbbvsTT_MM_N/D");
   t_RDSME->Branch("mlpZbbvsTT_ML" , &mlpZbbvsTT_ML,"mlpZbbvsTT_ML/D");

   t_RDSME->Branch("mlpZbbvsTT_mu_MM" , &mlpZbbvsTT_mu_MM,"mlpZbbvsTT_mu_MM/D");
   t_RDSME->Branch("mlpZbbvsTT_mu_MM_N" , &mlpZbbvsTT_mu_MM_N,"mlpZbbvsTT_mu_MM_N/D");
   t_RDSME->Branch("mlpZbbvsTT_mu_ML" , &mlpZbbvsTT_mu_ML,"mlpZbbvsTT_mu_ML/D");

   t_RDSME->Branch("SumNN" , &SumNN,"SumNN/D");
   t_RDSME->Branch("ProdNN" , &ProdNN,"ProdNN/D");
   t_RDSME->Branch("SumWeightedNN" , &SumWeightedNN,"SumWeightedNN/D");


   //Extra variables reweighting                                                                                                                                                                                  
   t_RDSME->Branch("ZbbReweight_dijetdR",&ZbbReweight_dijetdR,"ZbbReweight_dijetdR/D");
   t_RDSME->Branch("ZbbReweight_bestzpt",&ZbbReweight_bestzpt,"ZbbReweight_bestzpt/D");

   //$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

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
        map_runevent[pair<Long64_t, Long64_t>(Long64_t(mc_ME->runNumber), Long64_t(mc_ME->eventNumber))] = iME + 1;
      else
        map_runevent[pair<Long64_t, Long64_t>(1, Long64_t(mc_ME->eventNumber))] = iME + 1;

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
      if (IsDATA) MEentry = map_runevent[pair<Long64_t, Long64_t>(Long64_t(mc_RDS->eventSelectionrun), Long64_t(mc_RDS->eventSelectionevent))];
      else  MEentry = map_runevent[pair<long int, long int>(1, int(mc_RDS->eventSelectionevent))];
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
	
        MeT = 0;
	Wtt = 0;
	Wqq = 0;
	Wgg = 0;
        Wtwb = 0;
        Wzz3 = 0;
        Wzz0 = 0;
        Whi3_115 = 0;
        Whi0_115 = 0;
        Whi3_120 = 0;
        Whi0_120 = 0;
        Whi3_125 = 0;
        Whi0_125 = 0;
        Whi3_130 = 0;
        Whi0_130 = 0;
        Whi3_135 = 0;
        Whi0_135 = 0;

        Inv_Mass_bb = 0;
        Inv_Mass_lept = 0;
       
        mc_ME->LoadTree(MEentry);
        mc_ME->GetEntry(MEentry);
      
        MeT = mc_ME->MeT;
	Wtt = mc_ME->Wtt;
	Wqq = mc_ME->Wqq;
 	Wgg = mc_ME->Wgg;
        Wtwb = mc_ME->Wtwb;
        Wzz3 = mc_ME->Wzz3;
        Wzz0 = mc_ME->Wzz0;
        Whi3_115 = mc_ME->Whi3_115;
        Whi0_115 = mc_ME->Whi0_115;
	Whi3_120 = mc_ME->Whi3_120;
        Whi0_120 = mc_ME->Whi0_120;
	Whi3_125 = mc_ME->Whi3_125;
        Whi0_125 = mc_ME->Whi0_125;
	Whi3_130 = mc_ME->Whi3_130;
        Whi0_130 = mc_ME->Whi0_130;
	Whi3_135 = mc_ME->Whi3_135;
        Whi0_135 = mc_ME->Whi0_135;
	jetmetbjetMinCSVdisc=min(mc_RDS->jetmetbjet1CSVdisc,mc_RDS->jetmetbjet2CSVdisc);
	jetmetbjetMaxCSVdisc=max(mc_RDS->jetmetbjet1CSVdisc,mc_RDS->jetmetbjet2CSVdisc);
	jetmetbjetProdCSVdisc=mc_RDS->jetmetbjet1CSVdisc*mc_RDS->jetmetbjet2CSVdisc;

        Inv_Mass_bb = mc_ME->Inv_Mass_bb;
        Inv_Mass_lept = mc_ME->Inv_Mass_lept;
	
//---------------------- NN  output here ---------------------------------
        // For DY vs TT
	mlpZbbvsTT_MM = MLP_TT_vs_DY_MM_ee->Value(0, Wgg, Wqq, Wtt);
        mlpZbbvsTT_MM_N = max(0.0,min(1.0,MLP_TT_vs_DY_MM_N_ee->Value(0, Wgg,Wqq, mc_RDS->jetmetbjet2CSVdisc*mc_RDS->jetmetbjet1CSVdisc)));
        mlpZbbvsTT_ML = MLP_TT_vs_DY_ML_ee->Value(0, Wgg, Wqq, Wtt);
	mlpZbbvsTT_mu_MM = MLP_TT_vs_DY_MM_mm->Value(0, Wgg, Wqq, Wtt);
        mlpZbbvsTT_mu_MM_N = max(0.0,min(1.0,MLP_TT_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Wtt)));
	mlpZbbvsTT_mu_ML = MLP_TT_vs_DY_ML_mm->Value(0, Wgg, Wqq, Wtt);

	// For H 125
	mlphiggsvszbb_125_MM = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)));
	mlphiggsvstt_125_MM = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt, Whi0_125 , Whi3_125)));
        mlphiggsvszz_125_MM = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3, Whi0_125 , Whi3_125)));   
        mlphiggsvsbkg_125_MM = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_ee->Value(0, mlphiggsvszbb_125_MM  , mlphiggsvszz_125_MM , mlphiggsvstt_125_MM)));
        mlphiggsvszbb_125_ML = max(0.0,min(1.0,MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)));
        mlphiggsvstt_125_ML = max(0.0,min(1.0,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt, Whi0_125 , Whi3_125)));
        mlphiggsvszz_125_ML = max(0.0,min(1.0,MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3, Whi0_125 , Whi3_125)));
        mlphiggsvsbkg_125_ML = max(0.0,min(1.0,MLP_higgs_vs_BKG_ML_ee->Value(0, mlphiggsvszbb_125_ML  , mlphiggsvszz_125_ML , mlphiggsvstt_125_ML)));
        mlphiggsvszbb_125_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)));
        mlphiggsvstt_125_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt, Whi0_125 , Whi3_125)));
        mlphiggsvszz_125_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3, Whi0_125 , Whi3_125)));
        mlphiggsvsbkg_125_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_ee->Value(0, mlphiggsvszbb_125_MM_N  , mlphiggsvszz_125_MM_N , mlphiggsvstt_125_MM_N)));
	// For H 125
	mlphiggsvszbb_125_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb_2011->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)));
	mlphiggsvszz_125_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb_2011->Value(0, Wzz0 , Wzz3, Whi0_125 , Whi3_125)));
	mlphiggsvstt_125_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb_2011->Value(0, Wtt, Whi0_125 , Whi3_125)));
	mlphiggsvsbkg_125_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_2011->Value(0,mlphiggsvszbb_125_comb_MM_N_2011,mlphiggsvszz_125_comb_MM_N_2011,mlphiggsvstt_125_comb_MM_N_2011 )));
	// For H 125
	newmlphiggsvszbb_125_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)));
	newmlphiggsvszz_125_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_125 , Whi3_125)));
	newmlphiggsvstt_125_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_125 , Whi3_125)));
	newmlphiggsvsbkg_125_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_BKG_MM_N_comb->Value(0,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvstt_125_comb_MM_N )));
	SumNN = (newmlphiggsvszbb_125_comb_MM_N+newmlphiggsvszz_125_comb_MM_N+newmlphiggsvstt_125_comb_MM_N)/3;
	ProdNN = newmlphiggsvszbb_125_comb_MM_N*newmlphiggsvszz_125_comb_MM_N*newmlphiggsvstt_125_comb_MM_N;
	SumWeightedNN = newmlphiggsvszbb_125_comb_MM_N*0.8+newmlphiggsvszz_125_comb_MM_N*0.05+newmlphiggsvstt_125_comb_MM_N*0.15;
	//test
	mlphiggsvsbkg_125_comb_MM_N_1_10000 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_1_10000->Value(0,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvstt_125_comb_MM_N )));
	mlphiggsvsbkg_125_comb_MM_N_1_5000 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_1_5000->Value(0,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvstt_125_comb_MM_N )));
	mlphiggsvsbkg_125_comb_MM_N_2_10000 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_2_10000->Value(0,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvstt_125_comb_MM_N )));
	mlphiggsvsbkg_125_comb_MM_N_2_5000 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_2_5000->Value(0,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvstt_125_comb_MM_N )));
	mlphiggsvsbkg_125_comb_MM_N_3_5000 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_3_5000->Value(0,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvstt_125_comb_MM_N )));
	mlphiggsvsbkg_125_comb_MM_N_2_3_2_10000 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_2_3_2_10000->Value(0,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvstt_125_comb_MM_N )));
	mlphiggsvsbkg_125_comb_MM_N_2_3_2_5000 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_2_3_2_5000->Value(0,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvstt_125_comb_MM_N )));
	mlphiggsvsbkg_125_comb_MM_N_2_4_10000 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_2_4_10000->Value(0,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvstt_125_comb_MM_N )));
	mlphiggsvsbkg_125_comb_MM_N_2_5_3_1_1000 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_2_5_3_1_1000->Value(0,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvstt_125_comb_MM_N )));
	mlphiggsvsbkg_125_comb_MM_N_3_2_10000 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_3_2_10000->Value(0,newmlphiggsvszbb_125_comb_MM_N,newmlphiggsvszz_125_comb_MM_N,newmlphiggsvstt_125_comb_MM_N )));


	// For H 125
	mlphiggsvszbb_125_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)));
	mlphiggsvszz_125_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_125 , Whi3_125)));
	mlphiggsvstt_125_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_125 , Whi3_125)));
	mlphiggsvsbkg_125_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb->Value(0,mlphiggsvszbb_125_comb_MM_N,mlphiggsvszz_125_comb_MM_N,mlphiggsvstt_125_comb_MM_N )));
	// For H 125
        mlphiggsvszbb_125_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)));
        mlphiggsvstt_125_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt , Whi0_125 , Whi3_125)));
        mlphiggsvszz_125_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)));
        mlphiggsvsbkg_125_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_mm->Value(0, mlphiggsvszbb_125_mu_MM  , mlphiggsvszz_125_mu_MM , mlphiggsvstt_125_mu_MM)));
        mlphiggsvszbb_125_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)));
        mlphiggsvstt_125_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt , Whi0_125 , Whi3_125)));
        mlphiggsvszz_125_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)));
        mlphiggsvsbkg_125_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_BKG_ML_mm->Value(0, mlphiggsvszbb_125_mu_ML  , mlphiggsvszz_125_mu_ML , mlphiggsvstt_125_mu_ML)));
        mlphiggsvszbb_125_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)));
        mlphiggsvstt_125_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt , Whi0_125 , Whi3_125)));
        mlphiggsvszz_125_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)));
        mlphiggsvsbkg_125_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_mm->Value(0, mlphiggsvszbb_125_mu_MM_N  , mlphiggsvszz_125_mu_MM_N , mlphiggsvstt_125_mu_MM_N)));
	//cout<<MLP_higgs_vs_BKG_MM_N_mm->Value(0, mlphiggsvszbb_125_mu_MM_N  , mlphiggsvszz_125_mu_MM_N , mlphiggsvstt_125_mu_MM_N)<<endl;
  
      // For H 115
        mlphiggsvszbb_115_MM = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)));
        mlphiggsvstt_115_MM = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt, Whi0_115 , Whi3_115)));
        mlphiggsvszz_115_MM = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3, Whi0_115 , Whi3_115)));
        mlphiggsvsbkg_115_MM = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_ee->Value(0, mlphiggsvszbb_115_MM  , mlphiggsvszz_115_MM , mlphiggsvstt_115_MM)));
        mlphiggsvszbb_115_ML = max(0.0,min(1.0,MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)));
        mlphiggsvstt_115_ML = max(0.0,min(1.0,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt, Whi0_115 , Whi3_115)));
        mlphiggsvszz_115_ML = max(0.0,min(1.0,MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3, Whi0_115 , Whi3_115)));
        mlphiggsvsbkg_115_ML = max(0.0,min(1.0,MLP_higgs_vs_BKG_ML_ee->Value(0, mlphiggsvszbb_115_ML  , mlphiggsvszz_115_ML , mlphiggsvstt_115_ML)));
        mlphiggsvszbb_115_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)));
        mlphiggsvstt_115_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt, Whi0_115 , Whi3_115)));
        mlphiggsvszz_115_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3, Whi0_115 , Whi3_115)));
        mlphiggsvsbkg_115_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_ee->Value(0, mlphiggsvszbb_115_MM_N  , mlphiggsvszz_115_MM_N , mlphiggsvstt_115_MM_N)));
        // For H 115
        mlphiggsvszbb_115_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb_2011->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)));
        mlphiggsvszz_115_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb_2011->Value(0, Wzz0 , Wzz3, Whi0_115 , Whi3_115)));
        mlphiggsvstt_115_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb_2011->Value(0, Wtt, Whi0_115 , Whi3_115)));
        mlphiggsvsbkg_115_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_2011->Value(0,mlphiggsvszbb_115_comb_MM_N_2011,mlphiggsvszz_115_comb_MM_N_2011,mlphiggsvstt_115_comb_MM_N_2011 )));
        // For H 115
        mlphiggsvszbb_115_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)));
        mlphiggsvszz_115_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_115 , Whi3_115)));
        mlphiggsvstt_115_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_115 , Whi3_115)));
        mlphiggsvsbkg_115_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb->Value(0,mlphiggsvszbb_115_comb_MM_N,mlphiggsvszz_115_comb_MM_N,mlphiggsvstt_115_comb_MM_N )));
        // %For H 115
        newmlphiggsvszbb_115_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)));
        newmlphiggsvszz_115_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_115 , Whi3_115)));
        newmlphiggsvstt_115_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_115 , Whi3_115)));
        newmlphiggsvsbkg_115_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_BKG_MM_N_comb->Value(0,newmlphiggsvszbb_115_comb_MM_N,newmlphiggsvszz_115_comb_MM_N,newmlphiggsvstt_115_comb_MM_N )));
        // For H 115
        mlphiggsvszbb_115_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)));
        mlphiggsvstt_115_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt , Whi0_115 , Whi3_115)));
        mlphiggsvszz_115_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115)));
        mlphiggsvsbkg_115_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_mm->Value(0, mlphiggsvszbb_115_mu_MM  , mlphiggsvszz_115_mu_MM , mlphiggsvstt_115_mu_MM)));
        mlphiggsvszbb_115_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)));
        mlphiggsvstt_115_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt , Whi0_115 , Whi3_115)));
        mlphiggsvszz_115_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115)));
        mlphiggsvsbkg_115_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_BKG_ML_mm->Value(0, mlphiggsvszbb_115_mu_ML  , mlphiggsvszz_115_mu_ML , mlphiggsvstt_115_mu_ML)));
        mlphiggsvszbb_115_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)));
        mlphiggsvstt_115_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt , Whi0_115 , Whi3_115)));
        mlphiggsvszz_115_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115)));
        mlphiggsvsbkg_115_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_mm->Value(0, mlphiggsvszbb_115_mu_MM_N  , mlphiggsvszz_115_mu_MM_N , mlphiggsvstt_115_mu_MM_N)));

        // For H 120
        mlphiggsvszbb_120_MM = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)));
        mlphiggsvstt_120_MM = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt, Whi0_120 , Whi3_120)));
        mlphiggsvszz_120_MM = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3, Whi0_120 , Whi3_120)));
        mlphiggsvsbkg_120_MM = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_ee->Value(0, mlphiggsvszbb_120_MM  , mlphiggsvszz_120_MM , mlphiggsvstt_120_MM)));
        mlphiggsvszbb_120_ML = max(0.0,min(1.0,MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)));
        mlphiggsvstt_120_ML = max(0.0,min(1.0,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt, Whi0_120 , Whi3_120)));
        mlphiggsvszz_120_ML = max(0.0,min(1.0,MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3, Whi0_120 , Whi3_120)));
        mlphiggsvsbkg_120_ML = max(0.0,min(1.0,MLP_higgs_vs_BKG_ML_ee->Value(0, mlphiggsvszbb_120_ML  , mlphiggsvszz_120_ML , mlphiggsvstt_120_ML)));
        mlphiggsvszbb_120_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)));
        mlphiggsvstt_120_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt, Whi0_120 , Whi3_120)));
        mlphiggsvszz_120_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3, Whi0_120 , Whi3_120)));
        mlphiggsvsbkg_120_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_ee->Value(0, mlphiggsvszbb_120_MM_N  , mlphiggsvszz_120_MM_N , mlphiggsvstt_120_MM_N)));
        // For H 120
        mlphiggsvszbb_120_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb_2011->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)));
        mlphiggsvszz_120_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb_2011->Value(0, Wzz0 , Wzz3, Whi0_120 , Whi3_120)));
        mlphiggsvstt_120_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb_2011->Value(0, Wtt, Whi0_120 , Whi3_120)));
        mlphiggsvsbkg_120_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_2011->Value(0,mlphiggsvszbb_120_comb_MM_N_2011,mlphiggsvszz_120_comb_MM_N_2011,mlphiggsvstt_120_comb_MM_N_2011 ))); 
        // For H 120
        mlphiggsvszbb_120_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)));
        mlphiggsvszz_120_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_120 , Whi3_120)));
        mlphiggsvstt_120_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_120 , Whi3_120)));
        mlphiggsvsbkg_120_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb->Value(0,mlphiggsvszbb_120_comb_MM_N,mlphiggsvszz_120_comb_MM_N,mlphiggsvstt_120_comb_MM_N ))); 
        // For H 120
        newmlphiggsvszbb_120_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)));
        newmlphiggsvszz_120_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_120 , Whi3_120)));
        newmlphiggsvstt_120_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_120 , Whi3_120)));
        newmlphiggsvsbkg_120_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_BKG_MM_N_comb->Value(0,newmlphiggsvszbb_120_comb_MM_N,newmlphiggsvszz_120_comb_MM_N,newmlphiggsvstt_120_comb_MM_N ))); 
        // For H 120
        mlphiggsvszbb_120_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)));
        mlphiggsvstt_120_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt , Whi0_120 , Whi3_120)));
        mlphiggsvszz_120_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120)));
        mlphiggsvsbkg_120_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_mm->Value(0, mlphiggsvszbb_120_mu_MM  , mlphiggsvszz_120_mu_MM , mlphiggsvstt_120_mu_MM)));
        mlphiggsvszbb_120_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)));
        mlphiggsvstt_120_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt , Whi0_120 , Whi3_120)));
        mlphiggsvszz_120_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120)));
        mlphiggsvsbkg_120_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_BKG_ML_mm->Value(0, mlphiggsvszbb_120_mu_ML  , mlphiggsvszz_120_mu_ML , mlphiggsvstt_120_mu_ML)));
        mlphiggsvszbb_120_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)));
        mlphiggsvstt_120_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt , Whi0_120 , Whi3_120)));
        mlphiggsvszz_120_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120)));
        mlphiggsvsbkg_120_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_mm->Value(0, mlphiggsvszbb_120_mu_MM_N  , mlphiggsvszz_120_mu_MM_N , mlphiggsvstt_120_mu_MM_N)));

        // For H 130
        mlphiggsvszbb_130_MM = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)));
        mlphiggsvstt_130_MM = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt, Whi0_130 , Whi3_130)));
        mlphiggsvszz_130_MM = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3, Whi0_130 , Whi3_130)));
        mlphiggsvsbkg_130_MM = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_ee->Value(0, mlphiggsvszbb_130_MM  , mlphiggsvszz_130_MM , mlphiggsvstt_130_MM)));
        mlphiggsvszbb_130_ML = max(0.0,min(1.0,MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)));
        mlphiggsvstt_130_ML = max(0.0,min(1.0,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt, Whi0_130 , Whi3_130)));
        mlphiggsvszz_130_ML = max(0.0,min(1.0,MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3, Whi0_130 , Whi3_130)));
        mlphiggsvsbkg_130_ML = max(0.0,min(1.0,MLP_higgs_vs_BKG_ML_ee->Value(0, mlphiggsvszbb_130_ML  , mlphiggsvszz_130_ML , mlphiggsvstt_130_ML)));
        mlphiggsvszbb_130_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)));
        mlphiggsvstt_130_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt, Whi0_130 , Whi3_130)));
        mlphiggsvszz_130_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3, Whi0_130 , Whi3_130)));
        mlphiggsvsbkg_130_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_ee->Value(0, mlphiggsvszbb_130_MM_N  , mlphiggsvszz_130_MM_N , mlphiggsvstt_130_MM_N)));
        // For H 130
        mlphiggsvszbb_130_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb_2011->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)));
        mlphiggsvszz_130_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb_2011->Value(0, Wzz0 , Wzz3, Whi0_130 , Whi3_130)));
        mlphiggsvstt_130_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb_2011->Value(0, Wtt, Whi0_130 , Whi3_130)));
        mlphiggsvsbkg_130_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_2011->Value(0,mlphiggsvszbb_130_comb_MM_N_2011,mlphiggsvszz_130_comb_MM_N_2011,mlphiggsvstt_130_comb_MM_N_2011 )));
        // For H 130
        mlphiggsvszbb_130_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)));
        mlphiggsvszz_130_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_130 , Whi3_130)));
        mlphiggsvstt_130_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_130 , Whi3_130)));
        mlphiggsvsbkg_130_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb->Value(0,mlphiggsvszbb_130_comb_MM_N,mlphiggsvszz_130_comb_MM_N,mlphiggsvstt_130_comb_MM_N )));
        // For H 130
        newmlphiggsvszbb_130_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)));
        newmlphiggsvszz_130_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_130 , Whi3_130)));
        newmlphiggsvstt_130_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_130 , Whi3_130)));
        newmlphiggsvsbkg_130_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_BKG_MM_N_comb->Value(0,newmlphiggsvszbb_130_comb_MM_N,newmlphiggsvszz_130_comb_MM_N,newmlphiggsvstt_130_comb_MM_N )));
	// For H 130
        mlphiggsvszbb_130_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)));
        mlphiggsvstt_130_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt , Whi0_130 , Whi3_130)));
        mlphiggsvszz_130_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130)));
        mlphiggsvsbkg_130_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_mm->Value(0, mlphiggsvszbb_130_mu_MM  , mlphiggsvszz_130_mu_MM , mlphiggsvstt_130_mu_MM)));
        mlphiggsvszbb_130_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)));
        mlphiggsvstt_130_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt , Whi0_130 , Whi3_130)));
        mlphiggsvszz_130_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130)));
        mlphiggsvsbkg_130_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_BKG_ML_mm->Value(0, mlphiggsvszbb_130_mu_ML  , mlphiggsvszz_130_mu_ML , mlphiggsvstt_130_mu_ML)));
        mlphiggsvszbb_130_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)));
        mlphiggsvstt_130_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt , Whi0_130 , Whi3_130)));
        mlphiggsvszz_130_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130)));
        mlphiggsvsbkg_130_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_mm->Value(0, mlphiggsvszbb_130_mu_MM_N  , mlphiggsvszz_130_mu_MM_N , mlphiggsvstt_130_mu_MM_N)));

        // For H 135
        mlphiggsvszbb_135_MM = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)));
        mlphiggsvstt_135_MM = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt, Whi0_135 , Whi3_135)));
        mlphiggsvszz_135_MM = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3, Whi0_135 , Whi3_135)));
        mlphiggsvsbkg_135_MM = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_ee->Value(0, mlphiggsvszbb_135_MM  , mlphiggsvszz_135_MM , mlphiggsvstt_135_MM)));
        mlphiggsvszbb_135_ML = max(0.0,min(1.0,MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)));
        mlphiggsvstt_135_ML = max(0.0,min(1.0,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt, Whi0_135 , Whi3_135)));
        mlphiggsvszz_135_ML = max(0.0,min(1.0,MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3, Whi0_135 , Whi3_135)));
        mlphiggsvsbkg_135_ML = max(0.0,min(1.0,MLP_higgs_vs_BKG_ML_ee->Value(0, mlphiggsvszbb_135_ML  , mlphiggsvszz_135_ML , mlphiggsvstt_135_ML)));
        mlphiggsvszbb_135_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)));
        mlphiggsvstt_135_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt, Whi0_135 , Whi3_135)));
        mlphiggsvszz_135_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3, Whi0_135 , Whi3_135)));
        mlphiggsvsbkg_135_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_ee->Value(0, mlphiggsvszbb_135_MM_N  , mlphiggsvszz_135_MM_N , mlphiggsvstt_135_MM_N)));
         // For H 135
        mlphiggsvszbb_135_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb_2011->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)));
        mlphiggsvszz_135_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb_2011->Value(0, Wzz0 , Wzz3, Whi0_135 , Whi3_135)));
        mlphiggsvstt_135_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb_2011->Value(0, Wtt, Whi0_135 , Whi3_135)));
        mlphiggsvsbkg_135_comb_MM_N_2011 = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb_2011->Value(0,mlphiggsvszbb_135_comb_MM_N_2011,mlphiggsvszz_135_comb_MM_N_2011,mlphiggsvstt_135_comb_MM_N_2011 )));
         // For H 135
        mlphiggsvszbb_135_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)));
        mlphiggsvszz_135_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_135 , Whi3_135)));
        mlphiggsvstt_135_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_135 , Whi3_135)));
        mlphiggsvsbkg_135_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb->Value(0,mlphiggsvszbb_135_comb_MM_N,mlphiggsvszz_135_comb_MM_N,mlphiggsvstt_135_comb_MM_N )));
         // For H 135
        newmlphiggsvszbb_135_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)));
        newmlphiggsvszz_135_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_135 , Whi3_135)));
        newmlphiggsvstt_135_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_135 , Whi3_135)));
        newmlphiggsvsbkg_135_comb_MM_N = max(0.0,min(1.0,NEWMLP_higgs_vs_BKG_MM_N_comb->Value(0,newmlphiggsvszbb_135_comb_MM_N,newmlphiggsvszz_135_comb_MM_N,newmlphiggsvstt_135_comb_MM_N )));
	// For H 135
        mlphiggsvszbb_135_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)));
        mlphiggsvstt_135_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt , Whi0_135 , Whi3_135)));
        mlphiggsvszz_135_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135)));
        mlphiggsvsbkg_135_mu_MM = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_mm->Value(0, mlphiggsvszbb_135_mu_MM  , mlphiggsvszz_135_mu_MM , mlphiggsvstt_135_mu_MM)));
        mlphiggsvszbb_135_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)));
        mlphiggsvstt_135_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt , Whi0_135 , Whi3_135)));
        mlphiggsvszz_135_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135)));
        mlphiggsvsbkg_135_mu_ML = max(0.0,min(1.0,MLP_higgs_vs_BKG_ML_mm->Value(0, mlphiggsvszbb_135_mu_ML  , mlphiggsvszz_135_mu_ML , mlphiggsvstt_135_mu_ML)));
        mlphiggsvszbb_135_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)));
        mlphiggsvstt_135_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt , Whi0_135 , Whi3_135)));
        mlphiggsvszz_135_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135)));
        mlphiggsvsbkg_135_mu_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_mm->Value(0, mlphiggsvszbb_135_mu_MM_N  , mlphiggsvszz_135_mu_MM_N , mlphiggsvstt_135_mu_MM_N)));





//------------------------------------ FOR BLINDING ----------------------------------------------------------------------------------
	// For H 125
	/*	if (InputFile.Contains("Data")){
	  if( MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_MM=1.5;}
	  if( MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_MM=1.5;}
	  if( MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_MM=1.5;}
	  if( MLP_higgs_vs_BKG_MM_ee->Value(0, MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_125 , Whi3_125)) > 0.5 ){mlphiggsvsbkg_125_MM=1.5;}
	  if( MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_mu_MM=1.5;}
	  if( MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_mu_MM=1.5;}
	  if( MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_mu_MM=1.5;}
	  if( MLP_higgs_vs_BKG_MM_mm->Value(0, MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_125 , Whi3_125) ) > 0.5 ){mlphiggsvsbkg_125_mu_MM=1.5;}
          if( MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_ee->Value(0, MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_125 , Whi3_125)) > 0.5 ){mlphiggsvsbkg_125_MM_N=1.5;}
          if( MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_mu_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_mu_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_mu_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_mm->Value(0, MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_125 , Whi3_125) ) > 0.5 ){mlphiggsvsbkg_125_mu_MM_N=1.5;}
          if( MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_ML=1.5;}
          if( MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_ML=1.5;}
          if( MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_ML=1.5;}
          if( MLP_higgs_vs_BKG_ML_ee->Value(0, MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_125 , Whi3_125)) > 0.5 ){mlphiggsvsbkg_125_ML=1.5;}
          if( MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_mu_ML=1.5;}
          if( MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_mu_ML=1.5;}
          if( MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_mu_ML=1.5;}
          if( MLP_higgs_vs_BKG_ML_mm->Value(0, MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_125 , Whi3_125) ) > 0.5 ){mlphiggsvsbkg_125_mu_ML=1.5;}
	  if( MLP_higgs_vs_DY_MM_N_comb_2011->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_comb_MM_N_2011=1.5;}
          if( MLP_higgs_vs_TT_MM_N_comb_2011->Value(0, Wtt, Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_comb_MM_N_2011=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_comb_2011->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_comb_MM_N_2011=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_comb_2011->Value(0, MLP_higgs_vs_DY_MM_N_comb_2011->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_MM_N_comb_2011->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_MM_N_comb_2011->Value(0, Wtt, Whi0_125 , Whi3_125) ) > 0.5 ){mlphiggsvsbkg_125_comb_MM_N=1.5;}
	  if( MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_comb_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_comb_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_comb_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_comb->Value(0, MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_125 , Whi3_125) ) > 0.5 ){mlphiggsvsbkg_125_comb_MM_N=1.5;}
	  if( NEWMLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){newmlphiggsvszbb_125_comb_MM_N=1.5;}
          if( NEWMLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_125 , Whi3_125)>0.5){newmlphiggsvstt_125_comb_MM_N=1.5;}
          if( NEWMLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)>0.5){newmlphiggsvszz_125_comb_MM_N=1.5;}
          if( NEWMLP_higgs_vs_BKG_MM_N_comb->Value(0, NEWMLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), NEWMLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125) ,NEWMLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_125 , Whi3_125) ) > 0.5 ){newmlphiggsvsbkg_125_comb_MM_N=1.5;}

	}
        // For H 115
        if (InputFile.Contains("Data")){
          if( MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_MM=1.5;}
          if( MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_MM=1.5;}
          if( MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_MM=1.5;}
          if( MLP_higgs_vs_BKG_MM_ee->Value(0, MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_115 , Whi3_115)) > 0.5 ){mlphiggsvsbkg_115_MM=1.5;}
          if( MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_mu_MM=1.5;}
          if( MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_mu_MM=1.5;}
          if( MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_mu_MM=1.5;}
          if( MLP_higgs_vs_BKG_MM_mm->Value(0, MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_115 , Whi3_115) ) > 0.5 ){mlphiggsvsbkg_115_mu_MM=1.5;}
          if( MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_ee->Value(0, MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_115 , Whi3_115)) > 0.5 ){mlphiggsvsbkg_115_MM_N=1.5;}
          if( MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_mu_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_mu_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_mu_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_mm->Value(0, MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_115 , Whi3_115) ) > 0.5 ){mlphiggsvsbkg_115_mu_MM_N=1.5;}
          if( MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_ML=1.5;}
          if( MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_ML=1.5;}
          if( MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_ML=1.5;}
          if( MLP_higgs_vs_BKG_ML_ee->Value(0, MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_115 , Whi3_115)) > 0.5 ){mlphiggsvsbkg_115_ML=1.5;}
          if( MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_mu_ML=1.5;}
          if( MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_mu_ML=1.5;}
          if( MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_mu_ML=1.5;}
          if( MLP_higgs_vs_BKG_ML_mm->Value(0, MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_115 , Whi3_115) ) > 0.5 ){mlphiggsvsbkg_115_mu_ML=1.5;}
          if( MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_comb_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_comb_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_comb_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_comb->Value(0, MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_115 , Whi3_115) ) > 0.5 ){mlphiggsvsbkg_115_comb_MM_N=1.5;}	
		
		}
	// For H 120
        if (InputFile.Contains("Data")){
          if( MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_MM=1.5;}
          if( MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_MM=1.5;}
          if( MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_MM=1.5;}
          if( MLP_higgs_vs_BKG_MM_ee->Value(0, MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_120 , Whi3_120)) > 0.5 ){mlphiggsvsbkg_120_MM=1.5;}
          if( MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_mu_MM=1.5;}
          if( MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_mu_MM=1.5;}
          if( MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_mu_MM=1.5;}
          if( MLP_higgs_vs_BKG_MM_mm->Value(0, MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_120 , Whi3_120) ) > 0.5 ){mlphiggsvsbkg_120_mu_MM=1.5;}
          if( MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_ee->Value(0, MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_120 , Whi3_120)) > 0.5 ){mlphiggsvsbkg_120_MM_N=1.5;}
          if( MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_mu_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_mu_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_mu_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_mm->Value(0, MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_120 , Whi3_120) ) > 0.5 ){mlphiggsvsbkg_120_mu_MM_N=1.5;}
          if( MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_ML=1.5;}
          if( MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_ML=1.5;}
          if( MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_ML=1.5;}
          if( MLP_higgs_vs_BKG_ML_ee->Value(0, MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_120 , Whi3_120)) > 0.5 ){mlphiggsvsbkg_120_ML=1.5;}
          if( MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_mu_ML=1.5;}
          if( MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_mu_ML=1.5;}
          if( MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_mu_ML=1.5;}
          if( MLP_higgs_vs_BKG_ML_mm->Value(0, MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_120 , Whi3_120) ) > 0.5 ){mlphiggsvsbkg_120_mu_ML=1.5;}
	  if( MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_comb_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_comb_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_comb_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_comb->Value(0, MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_120 , Whi3_120) ) > 0.5 ){mlphiggsvsbkg_120_comb_MM_N=1.5;}

	
	}
        // For H 130
        if (InputFile.Contains("Data")){
	  if( MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_MM=1.5;}
          if( MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_MM=1.5;}
          if( MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_MM=1.5;}
          if( MLP_higgs_vs_BKG_MM_ee->Value(0, MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_130 , Whi3_130)) > 0.5 ){mlphiggsvsbkg_130_MM=1.5;}
          if( MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_mu_MM=1.5;}
          if( MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_mu_MM=1.5;}
          if( MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_mu_MM=1.5;}
          if( MLP_higgs_vs_BKG_MM_mm->Value(0, MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_130 , Whi3_130) ) > 0.5 ){mlphiggsvsbkg_130_mu_MM=1.5;}
          if( MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_ee->Value(0, MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_130 , Whi3_130)) > 0.5 ){mlphiggsvsbkg_130_MM_N=1.5;}
          if( MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_mu_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_mu_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_mu_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_mm->Value(0, MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_130 , Whi3_130) ) > 0.5 ){mlphiggsvsbkg_130_mu_MM_N=1.5;}
          if( MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_ML=1.5;}
          if( MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_ML=1.5;}
          if( MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_ML=1.5;}
          if( MLP_higgs_vs_BKG_ML_ee->Value(0, MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_130 , Whi3_130)) > 0.5 ){mlphiggsvsbkg_130_ML=1.5;}
          if( MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_mu_ML=1.5;}
          if( MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_mu_ML=1.5;}
          if( MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_mu_ML=1.5;}
          if( MLP_higgs_vs_BKG_ML_mm->Value(0, MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_130 , Whi3_130) ) > 0.5 ){mlphiggsvsbkg_130_mu_ML=1.5;}
	  if( MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_comb_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_comb_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_comb_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_comb->Value(0, MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_130 , Whi3_130) ) > 0.5 ){mlphiggsvsbkg_130_comb_MM_N=1.5;}
	
	}
	// For H 135
        if (InputFile.Contains("Data")){
	  if( MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_MM=1.5;}
          if( MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_MM=1.5;}
          if( MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_MM=1.5;}
          if( MLP_higgs_vs_BKG_MM_ee->Value(0, MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_135 , Whi3_135)) > 0.5 ){mlphiggsvsbkg_135_MM=1.5;}
          if( MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_mu_MM=1.5;}
          if( MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_mu_MM=1.5;}
          if( MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_mu_MM=1.5;}
          if( MLP_higgs_vs_BKG_MM_mm->Value(0, MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_135 , Whi3_135) ) > 0.5 ){mlphiggsvsbkg_135_mu_MM=1.5;}
          if( MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_ee->Value(0, MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_135 , Whi3_135)) > 0.5 ){mlphiggsvsbkg_135_MM_N=1.5;}
          if( MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_mu_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_mu_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_mu_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_mm->Value(0, MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_135 , Whi3_135) ) > 0.5 ){mlphiggsvsbkg_135_mu_MM_N=1.5;}
          if( MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_ML=1.5;}
          if( MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_ML=1.5;}
          if( MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_ML=1.5;}
          if( MLP_higgs_vs_BKG_ML_ee->Value(0, MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_135 , Whi3_135)) > 0.5 ){mlphiggsvsbkg_135_ML=1.5;}
          if( MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_mu_ML=1.5;}
          if( MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_mu_ML=1.5;}
          if( MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_mu_ML=1.5;}
          if( MLP_higgs_vs_BKG_ML_mm->Value(0, MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_135 , Whi3_135) ) > 0.5 ){mlphiggsvsbkg_135_mu_ML=1.5;}	
	  if( MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_comb_MM_N=1.5;}
          if( MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_comb_MM_N=1.5;}
          if( MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_comb_MM_N=1.5;}
          if( MLP_higgs_vs_BKG_MM_N_comb->Value(0, MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_135 , Whi3_135) ) > 0.5 ){mlphiggsvsbkg_135_comb_MM_N=1.5;}

	}
	*/
	
	//Reweighting stuff here:
	ZbbReweight_dijetdR = 1.;
	ZbbReweight_bestzpt = 1.;
	
	//std::cout << "hZbbReweight_dijetdR_Mu->Integral()=" << hZbbReweight_dijetdR_Mu->Integral() << std::endl;
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
  //cout << "after FindBin, bin=" << bin << endl;
  
  //reweighting hRWs not correct for under/overflow
  if(bin<=0 || bin==hRW->GetNbinsX()+1) return 1.; 
  const float content = hRW->GetBinContent(bin);
  if(content <=0.) return 1.;
  if (content > 5.)//prevent huge weights
    return 5.;

  return content;
}

//void SimpleTree(TString InputFile = "Mu_DATA") {
//   CreateParentTree(InputFile);

void SimpleTree() {
  /*  CreateParentTree("DoubleMu_DataA");
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
  CreateParentTree("DoubleEle_DataD");*/
  CreateParentTree("DY_Mu_MC");
  CreateParentTree("DY_El_MC");
   //CreateParentTree("DY_Pt100_El_MC");
  CreateParentTree("TT_Mu_MC");
  CreateParentTree("TT_El_MC");
  CreateParentTree("TT-FullLept_Mu_MC");
  CreateParentTree("TT-FullLept_El_MC");
  CreateParentTree("ZZ_Mu_MC");
  CreateParentTree("ZZ_El_MC");
  CreateParentTree("ZH125_Mu_MC");
  CreateParentTree("ZH125_El_MC");/*
   CreateParentTree("ZH115_Mu_MC");
   CreateParentTree("ZH115_El_MC");
   CreateParentTree("ZH120_Mu_MC");
   CreateParentTree("ZH120_El_MC");
   CreateParentTree("ZH130_Mu_MC");
   CreateParentTree("ZH130_El_MC");
   CreateParentTree("ZH135_Mu_MC");
   CreateParentTree("ZH135_El_MC");*/
}

//mergeOneSample(InputFile = "Mu_DATA")
//mergeOneSample(InputFile = "Mu_MC")
//mergeOneSample(InputFile = "Ttbar_Mu_MC")
//mergeOneSample(InputFile = "ZZ_Mu_MC")


