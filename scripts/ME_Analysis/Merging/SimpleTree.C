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
#include "RooDataSet.h"
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
#include "../NN/MLP_TT_vs_DY_MM_N_CSV_2011.cxx"
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

// Include NN trained on ee-mm merged
#include "MLP_Higgs_vs_DY_MM_N_CSV_2011_comb.cxx"
#include "MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb.cxx"
#include "MLP_Higgs_vs_TT_MM_N_CSV_2011_comb.cxx"
#include "MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb.cxx"



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
   Double_t        ProdEstimator;
   Double_t        eventSelectionrun;
   Double_t        eventSelectionevent;
   Double_t        eventSelectionls;
   Double_t        eventSelectiontriggerSelection;
   Double_t        eventSelectiontriggerBits;
   Double_t        eventSelectionzmassMu;
   Double_t        eventSelectionbestzmassMu;
   Double_t        eventSelectionzmassEle;
   Double_t        eventSelectionbestzmassEle;
   Double_t        eventSelectionzptMu;
   Double_t        eventSelectionbestzptMu;
   Double_t        eventSelectionzptEle;
   Double_t        eventSelectionbestzptEle;
   Double_t        eventSelectionscaldptZbj1;
   Double_t        eventSelectiondrZbj1;
   Double_t        eventSelectiondphiZbj1;
   Double_t        eventSelectionscaldptZbb;
   Double_t        eventSelectiondphiZbb;
   Double_t        eventSelectiondrZbb;
   Double_t        eventSelectiondijetM;
   Double_t        eventSelectiondijetPt;
   Double_t        eventSelectiondijetdR;
   Double_t        eventSelectiondijetSVdR;
   Double_t        eventSelectiondphidijetMET;
   Double_t        eventSelectionmindphijetMET;
   Double_t        eventSelectionnJets;
   Double_t        eventSelectionZbM;
   Double_t        eventSelectionZbPt;
   Double_t        eventSelectionZbbM;
   Double_t        eventSelectionZbbPt;
   Double_t        eventSelectioncategory;
   Double_t        eventSelectionmu1pt;
   Double_t        eventSelectionmu2pt;
   Double_t        eventSelectionmu1eta;
   Double_t        eventSelectionmu2eta;
   Double_t        eventSelectiondummy;
   Double_t        eventSelectionmu1etapm;
   Double_t        eventSelectionmu2etapm;
   Double_t        eventSelectionel1pt;
   Double_t        eventSelectionel2pt;
   Double_t        eventSelectionel1eta;
   Double_t        eventSelectionel2eta;
   Double_t        eventSelectionel1etapm;
   Double_t        eventSelectionel2etapm;
   Double_t        eventSelectiondijetdEta;
   Double_t        eventSelectionSSVHE1;
   Double_t        eventSelectionSSVHE2;
   Double_t        eventSelectionSSVHP1;
   Double_t        eventSelectionSSVHP2;
   Double_t        eventSelectionCSV1;
   Double_t        eventSelectionCSV2;
   Double_t        eventSelectiondilepdR;
   Double_t        BtaggingReweightingHE;
   Double_t        BtaggingReweightingHP;
   Double_t        BtaggingReweightingHEexcl;
   Double_t        BtaggingReweightingHPexcl;
   Double_t        BtaggingReweightingHEHE;
   Double_t        BtaggingReweightingHEHP;
   Double_t        BtaggingReweightingHPHP;
   Double_t        LeptonsReweightingweight;
   Double_t        jetmetSSVHEdisc;
   Double_t        jetmetnVertHE;
   Double_t        jetmetSSVHPdisc;
   Double_t        jetmetnVertHP;
   Double_t        jetmetSVmass;
   Double_t        jetmetTCHEdisc;
   Double_t        jetmetTCHPdisc;
   Double_t        jetmetSSVHEdiscDisc1;
   Double_t        jetmetSSVHPdiscDisc1;
   Double_t        jetmetTCHEdiscDisc1;
   Double_t        jetmetTCHPdiscDisc1;
   Double_t        jetmetbjet1CSVdisc;
   Double_t        jetmetbjet2CSVdisc;
   Double_t        jetmetMET;
   Double_t        jetmetMETphi;
   Double_t        jetmetMETsignificance;
   Double_t        jetmetjetpt;
   Double_t        jetmetjetpt_totunc;
   Double_t        jetmetjetFlavor;
   Double_t        jetmetjeteta;
   Double_t        jetmetjetetapm;
   Double_t        jetmetjetphi;
   Double_t        jetmetjetoverlapmu;
   Double_t        jetmetjetoverlapele;
   Double_t        jetmetjet1pt;
   Double_t        jetmetjet1pt_totunc;
   Double_t        jetmetjet1Flavor;
   Double_t        jetmetjet1eta;
   Double_t        jetmetjet1etapm;
   Double_t        jetmetjet1SSVHEdisc;
   Double_t        jetmetjet1nVertHE;
   Double_t        jetmetjet1SSVHPdisc;
   Double_t        jetmetjet1nVertHP;
   Double_t        jetmetjet1SVmass;
   Double_t        jetmetjet1TCHEdisc;
   Double_t        jetmetjet1TCHPdisc;
   Double_t        jetmetjet2pt;
   Double_t        jetmetjet2pt_totunc;
   Double_t        jetmetjet2Flavor;
   Double_t        jetmetjet2eta;
   Double_t        jetmetjet2etapm;
   Double_t        jetmetjet2SSVHEdisc;
   Double_t        jetmetjet2nVertHE;
   Double_t        jetmetjet2SSVHPdisc;
   Double_t        jetmetjet2nVertHP;
   Double_t        jetmetjet2SVmass;
   Double_t        jetmetjet2TCHEdisc;
   Double_t        jetmetjet2TCHPdisc;
   Double_t        jetmetbjet1pt;
   Double_t        jetmetbjet1pt_totunc;
   Double_t        jetmetbjet1Flavor;
   Double_t        jetmetbjet1eta;
   Double_t        jetmetbjet1etapm;
   Double_t        jetmetbjet1SSVHEdisc;
   Double_t        jetmetbjet1nVertHE;
   Double_t        jetmetbjet1SSVHPdisc;
   Double_t        jetmetbjet1nVertHP;
   Double_t        jetmetbjet1SVmass;
   Double_t        jetmetbjet1TCHEdisc;
   Double_t        jetmetbjet1TCHPdisc;
   Double_t	   jetmetjet1CSVdisc;
   Double_t        jetmetjet2CSVdisc;
   Double_t        jetmetbjet2pt;
   Double_t        jetmetbjet2pt_totunc;
   Double_t        jetmetbjet2Flavor;
   Double_t        jetmetbjet2eta;
   Double_t        jetmetbjet2etapm;
   Double_t        jetmetbjet2SSVHEdisc;
   Double_t        jetmetbjet2nVertHE;
   Double_t        jetmetbjet2SSVHPdisc;
   Double_t        jetmetbjet2nVertHP;
   Double_t        jetmetbjet2SVmass;
   Double_t        jetmetbjet2TCHEdisc;
   Double_t        jetmetbjet2TCHPdisc;
   Double_t        jetmetdptj1b1;
   Double_t        jetmetnj;
   Double_t        jetmetnb;
   Double_t        jetmetnbP;
   Double_t        jetmetnhf;
   Double_t        jetmetnef;
   Double_t        jetmetnpf;
   Double_t        jetmetchf;
   Double_t        jetmetnch;
   Double_t        jetmetcef;
   Double_t        jetmetjetid;
   Double_t        mcSelectioneventType;
   Double_t        lumiReweightingLumiWeight;
   Double_t        lumiReweightingLumiWeightUp;
   Double_t        lumiReweightingLumiWeightDown;
   Double_t        lumiReweightingpu;
   Double_t        lumiReweightingpv;
   Int_t           rc_eventSelection_0_idx;
   Int_t           rc_eventSelection_1_idx;
   Int_t           rc_eventSelection_2_idx;
   Int_t           rc_eventSelection_3_idx;
   Int_t           rc_eventSelection_4_idx;
   Int_t           rc_eventSelection_5_idx;
   Int_t           rc_eventSelection_6_idx;
   Int_t           rc_eventSelection_7_idx;
   Int_t           rc_eventSelection_8_idx;
   Int_t           rc_eventSelection_9_idx;
   Int_t           rc_eventSelection_10_idx;
   Int_t           rc_eventSelection_11_idx;
   Int_t           rc_eventSelection_12_idx;
   Int_t           rc_eventSelection_13_idx;
   Int_t           rc_eventSelection_14_idx;
   Int_t           rc_eventSelection_15_idx;
   Int_t           rc_eventSelection_16_idx;
   Int_t           rc_eventSelection_17_idx;
   Int_t           rc_eventSelection_18_idx;
   Int_t           rc_eventSelection_19_idx;
   Int_t           rc_eventSelection_20_idx;
   Int_t           rc_eventSelection_21_idx;
   Int_t           rc_eventSelection_22_idx;
   Double_t mcSelectionnLepPos;
   Double_t mcSelectionnLepNeg;
   Double_t mcSelectionnBottom;
   Double_t mcSelectionnAntibottom;
   Double_t mcSelectionflavLepPos;
   Double_t mcSelectionflavLepNeg;
   Double_t mcSelectionlepPosPx;
   Double_t mcSelectionlepPosPy;
   Double_t mcSelectionlepPosPz;
   Double_t mcSelectionlepPosEn;
   Double_t mcSelectionlepNegPx;
   Double_t mcSelectionlepNegPy;
   Double_t mcSelectionlepNegPz;
   Double_t mcSelectionlepNegEn;
   Double_t mcSelectionbottomPx;
   Double_t mcSelectionbottomPy;
   Double_t mcSelectionbottomPz;
   Double_t mcSelectionbottomEn;
   Double_t mcSelectionantibottomPx;
   Double_t mcSelectionantibottomPy;
   Double_t mcSelectionantibottomPz;
   Double_t mcSelectionantibottomEn;
   
   //Extra variables MLP's

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
   
    MLP_Higgs_vs_DY_MM_N_CSV_2011_comb *MLP_higgs_vs_DY_MM_N_comb = 0;  
    MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb *MLP_higgs_vs_ZZ_MM_N_comb = 0;  
    MLP_Higgs_vs_TT_MM_N_CSV_2011_comb *MLP_higgs_vs_TT_MM_N_comb = 0;  
    MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb *MLP_higgs_vs_BKG_MM_N_comb = 0;
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
  
   Double_t mlphiggsvszbb_115_comb_MM_N,mlphiggsvszbb_120_comb_MM_N,mlphiggsvszbb_125_comb_MM_N,mlphiggsvszbb_130_comb_MM_N,mlphiggsvszbb_135_comb_MM_N;
   Double_t mlphiggsvszz_115_comb_MM_N,mlphiggsvszz_120_comb_MM_N,mlphiggsvszz_125_comb_MM_N,mlphiggsvszz_130_comb_MM_N,mlphiggsvszz_135_comb_MM_N;
   Double_t mlphiggsvstt_115_comb_MM_N,mlphiggsvstt_120_comb_MM_N,mlphiggsvstt_125_comb_MM_N,mlphiggsvstt_130_comb_MM_N,mlphiggsvstt_135_comb_MM_N;
   Double_t mlphiggsvsbkg_115_comb_MM_N,mlphiggsvsbkg_120_comb_MM_N,mlphiggsvsbkg_125_comb_MM_N,mlphiggsvsbkg_130_comb_MM_N,mlphiggsvsbkg_135_comb_MM_N;
   
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

//---------------------------
   //Extra variables for reweighting stuff
   Double_t ZbbReweight_dijetdR;
   Double_t ZbbReweight_bestzpt;
   

   
void CreateParentTree(TString InputFile) {
   std::cout << "Running over sample: " << InputFile << std::endl;
   TString sanitycut = "";
   bool isMuChannel = false;
   if (InputFile.Contains("Mu_") && InputFile.Contains("El_")) {
     std::cout << "InputFile name cannot contain both <<Mu_>> and <<El_>>" << std::endl;
     return;
   }
   
   else if (InputFile.Contains("Mu_") || InputFile.Contains("MuA_") || InputFile.Contains("MuB_")) {
     std::cout << "  running MuMu channel" << std::endl;
     isMuChannel = true;
     sanitycut = " && eventSelectionbestzmassMu > 0.01 ";
   }
   
   else if (InputFile.Contains("El_") || InputFile.Contains("ElA_") || InputFile.Contains("ElB_")) {
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

   MLP_higgs_vs_DY_MM_N_comb = new MLP_Higgs_vs_DY_MM_N_CSV_2011_comb();
   MLP_higgs_vs_ZZ_MM_N_comb = new MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb();
   MLP_higgs_vs_TT_MM_N_comb = new MLP_Higgs_vs_TT_MM_N_CSV_2011_comb();
   MLP_higgs_vs_BKG_MM_N_comb = new MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb();

   
   
   
   //-----------------------------------------------------------------------
   // Input files location
   TString folder = "MergeRDS_CSV/";
   //RDS location
   TString folder2 = "/home/fynu/vizangarciaj/storage/CMSSW444_121207_forCSV2011Branch/CMSSW_4_4_4/src/UserCode/zbb_louvain/scripts/ME_Analysis/Merging/testCSV2011_130110/";
   //TString folder2 = "/storage/data/cms/users/vizangarciaj/RDS/SMP-12-003_v0_121114/PlainTrees/";
   //TString folder2 = "/storage/data/cms/users/vizangarciaj/RDS/SMP-12-003_v0_121114_JER0/JESMinus/";
   //TString folder2 = "/storage/data/cms/users/vizangarciaj/RDS/SMP-12-003_v0_121114_JER0/JESPlus/";
   //TString folder2 = "testsMergeRDS_jesM/";
   //TFile* f_RDS  = new TFile(folder2+"Tree_File_rds_zbb_" + InputFile + ".root");
   TFile* f_RDS  = new TFile(folder2+"Tree_File_rds_zbb_" + InputFile + ".root");
   TTree* t_RDS    = (TTree*)f_RDS->Get("rds_zbb");  
   
   //RooDataSet* R_RDS = (RooDataSet*)f_RDS->Get("rds_zbb");
   //TTree* t_RDS    = (TTree*)R_RDS->tree();

   TString mename = folder+"ME_zbb_" + InputFile + ".root";
   mename.ReplaceAll("A_DATA", "_DATA");
   mename.ReplaceAll("B_DATA", "_DATA");

   TFile* f_ME  = new TFile(mename);
   TTree* t_ME    = (TTree*)f_ME->Get("tree2");  
   
   TFile *f_RDSME = new TFile(folder+"Tree_rdsME_" +InputFile + ".root", "RECREATE");
   TTree *t_RDSME = new TTree("rds_zbb", "merged zbb-ME tree");

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
   t_RDSME->Branch("eventSelectionrun", &eventSelectionrun, "eventSelectionrun/D");
   t_RDSME->Branch("eventSelectionevent", &eventSelectionevent, "eventSelectionevent/D");
   t_RDSME->Branch("eventSelectionls", &eventSelectionls, "eventSelectionls/D");
   t_RDSME->Branch("eventSelectiontriggerSelection", &eventSelectiontriggerSelection, "eventSelectiontriggerSelection/D");
   t_RDSME->Branch("eventSelectiontriggerBits", &eventSelectiontriggerBits, "eventSelectiontriggerBits/D");
   t_RDSME->Branch("eventSelectionzmassMu", &eventSelectionzmassMu, "eventSelectionzmassMu/D");
   t_RDSME->Branch("eventSelectionbestzmassMu", &eventSelectionbestzmassMu, "eventSelectionbestzmassMu/D");
   t_RDSME->Branch("eventSelectionzmassEle", &eventSelectionzmassEle, "eventSelectionzmassEle/D");
   t_RDSME->Branch("eventSelectionbestzmassEle", &eventSelectionbestzmassEle, "eventSelectionbestzmassEle/D");
   t_RDSME->Branch("eventSelectionzptMu", &eventSelectionzptMu, "eventSelectionzptMu/D");
   t_RDSME->Branch("eventSelectionbestzptMu", &eventSelectionbestzptMu, "eventSelectionbestzptMu/D");
   t_RDSME->Branch("eventSelectionzptEle", &eventSelectionzptEle, "eventSelectionzptEle/D");
   t_RDSME->Branch("eventSelectionbestzptEle", &eventSelectionbestzptEle, "eventSelectionbestzptEle/D");
   t_RDSME->Branch("eventSelectionscaldptZbj1", &eventSelectionscaldptZbj1, "eventSelectionscaldptZbj1/D");
   t_RDSME->Branch("eventSelectiondrZbj1", &eventSelectiondrZbj1, "eventSelectiondrZbj1/D");
   t_RDSME->Branch("eventSelectiondphiZbj1", &eventSelectiondphiZbj1, "eventSelectiondphiZbj1/D");
   t_RDSME->Branch("eventSelectionscaldptZbb", &eventSelectionscaldptZbb, "eventSelectionscaldptZbb/D");
   t_RDSME->Branch("eventSelectiondphiZbb", &eventSelectiondphiZbb, "eventSelectiondphiZbb/D");
   t_RDSME->Branch("eventSelectiondrZbb", &eventSelectiondrZbb, "eventSelectiondrZbb/D");
   t_RDSME->Branch("eventSelectiondijetM", &eventSelectiondijetM, "eventSelectiondijetM/D");
   t_RDSME->Branch("eventSelectiondijetPt", &eventSelectiondijetPt, "eventSelectiondijetPt/D");
   t_RDSME->Branch("eventSelectiondijetdR", &eventSelectiondijetdR, "eventSelectiondijetdR/D");
   t_RDSME->Branch("eventSelectiondijetSVdR", &eventSelectiondijetSVdR, "eventSelectiondijetSVdR/D");
   t_RDSME->Branch("eventSelectiondphidijetMET", &eventSelectiondphidijetMET, "eventSelectiondphidijetMET/D");
   t_RDSME->Branch("eventSelectionmindphijetMET", &eventSelectionmindphijetMET, "eventSelectionmindphijetMET/D");
   t_RDSME->Branch("eventSelectionnJets", &eventSelectionnJets, "eventSelectionnJets/D");
   t_RDSME->Branch("eventSelectionZbM", &eventSelectionZbM, "eventSelectionZbM/D");
   t_RDSME->Branch("eventSelectionZbPt", &eventSelectionZbPt, "eventSelectionZbPt/D");
   t_RDSME->Branch("eventSelectionZbbM", &eventSelectionZbbM, "eventSelectionZbbM/D");
   t_RDSME->Branch("eventSelectionZbbPt", &eventSelectionZbbPt, "eventSelectionZbbPt/D");
   t_RDSME->Branch("eventSelectioncategory", &eventSelectioncategory, "eventSelectioncategory/D");
   t_RDSME->Branch("eventSelectionmu1pt", &eventSelectionmu1pt, "eventSelectionmu1pt/D");
   t_RDSME->Branch("eventSelectionmu2pt", &eventSelectionmu2pt, "eventSelectionmu2pt/D");
   t_RDSME->Branch("eventSelectionmu1eta", &eventSelectionmu1eta, "eventSelectionmu1eta/D");
   t_RDSME->Branch("eventSelectionmu2eta", &eventSelectionmu2eta, "eventSelectionmu2eta/D");
   t_RDSME->Branch("eventSelectiondummy", &eventSelectiondummy, "eventSelectiondummy/D");
   t_RDSME->Branch("eventSelectionmu1etapm", &eventSelectionmu1etapm, "eventSelectionmu1etapm/D");
   t_RDSME->Branch("eventSelectionmu2etapm", &eventSelectionmu2etapm, "eventSelectionmu2etapm/D");
   t_RDSME->Branch("eventSelectionel1pt", &eventSelectionel1pt, "eventSelectionel1pt/D");
   t_RDSME->Branch("eventSelectionel2pt", &eventSelectionel2pt, "eventSelectionel2pt/D");
   t_RDSME->Branch("eventSelectionel1eta", &eventSelectionel1eta, "eventSelectionel1eta/D");
   t_RDSME->Branch("eventSelectionel2eta", &eventSelectionel2eta, "eventSelectionel2eta/D");
   t_RDSME->Branch("eventSelectionel1etapm", &eventSelectionel1etapm, "eventSelectionel1etapm/D");
   t_RDSME->Branch("eventSelectionel2etapm", &eventSelectionel2etapm, "eventSelectionel2etapm/D");
   t_RDSME->Branch("eventSelectiondijetdEta", &eventSelectiondijetdEta, "eventSelectiondijetdEta/D");
   t_RDSME->Branch("eventSelectionSSVHE1", &eventSelectionSSVHE1, "eventSelectionSSVHE1/D");
   t_RDSME->Branch("eventSelectionSSVHE2", &eventSelectionSSVHE2, "eventSelectionSSVHE2/D");
   t_RDSME->Branch("eventSelectionSSVHP1", &eventSelectionSSVHP1, "eventSelectionSSVHP1/D");
   t_RDSME->Branch("eventSelectionSSVHP2", &eventSelectionSSVHP2, "eventSelectionSSVHP2/D");
   t_RDSME->Branch("eventSelectionCSV1", &eventSelectionCSV1, "eventSelectionCSV1/D");
   t_RDSME->Branch("eventSelectionCSV2", &eventSelectionCSV2, "eventSelectionCSV2/D");
   t_RDSME->Branch("eventSelectiondilepdR", &eventSelectiondilepdR, "eventSelectiondilepdR/D");
   t_RDSME->Branch("BtaggingReweightingHE", &BtaggingReweightingHE, "BtaggingReweightingHE/D");
   t_RDSME->Branch("BtaggingReweightingHP", &BtaggingReweightingHP, "BtaggingReweightingHP/D");
   t_RDSME->Branch("BtaggingReweightingHEexcl", &BtaggingReweightingHEexcl, "BtaggingReweightingHEexcl/D");
   t_RDSME->Branch("BtaggingReweightingHPexcl", &BtaggingReweightingHPexcl, "BtaggingReweightingHPexcl/D");
   t_RDSME->Branch("BtaggingReweightingHEHE", &BtaggingReweightingHEHE, "BtaggingReweightingHEHE/D");
   t_RDSME->Branch("BtaggingReweightingHEHP", &BtaggingReweightingHEHP, "BtaggingReweightingHEHP/D");
   t_RDSME->Branch("BtaggingReweightingHPHP", &BtaggingReweightingHPHP, "BtaggingReweightingHPHP/D");
   t_RDSME->Branch("LeptonsReweightingweight", &LeptonsReweightingweight, "LeptonsReweightingweight/D");
   t_RDSME->Branch("jetmetSSVHEdisc", &jetmetSSVHEdisc, "jetmetSSVHEdisc/D");
   t_RDSME->Branch("jetmetnVertHE", &jetmetnVertHE, "jetmetnVertHE/D");
   t_RDSME->Branch("jetmetSSVHPdisc", &jetmetSSVHPdisc, "jetmetSSVHPdisc/D");
   t_RDSME->Branch("jetmetnVertHP", &jetmetnVertHP, "jetmetnVertHP/D");
   t_RDSME->Branch("jetmetSVmass", &jetmetSVmass, "jetmetSVmass/D");
   t_RDSME->Branch("jetmetTCHEdisc", &jetmetTCHEdisc, "jetmetTCHEdisc/D");
   t_RDSME->Branch("jetmetTCHPdisc", &jetmetTCHPdisc, "jetmetTCHPdisc/D");
   t_RDSME->Branch("jetmetSSVHEdiscDisc1", &jetmetSSVHEdiscDisc1, "jetmetSSVHEdiscDisc1/D");
   t_RDSME->Branch("jetmetSSVHPdiscDisc1", &jetmetSSVHPdiscDisc1, "jetmetSSVHPdiscDisc1/D");
   t_RDSME->Branch("jetmetTCHEdiscDisc1", &jetmetTCHEdiscDisc1, "jetmetTCHEdiscDisc1/D");
   t_RDSME->Branch("jetmetTCHPdiscDisc1", &jetmetTCHPdiscDisc1, "jetmetTCHPdiscDisc1/D");
   t_RDSME->Branch("jetmetMET", &jetmetMET, "jetmetMET/D");
   t_RDSME->Branch("jetmetMETphi", &jetmetMETphi, "jetmetMETphi/D");
   t_RDSME->Branch("jetmetMETsignificance", &jetmetMETsignificance, "jetmetMETsignificance/D");
   t_RDSME->Branch("jetmetjetpt", &jetmetjetpt, "jetmetjetpt/D");
   t_RDSME->Branch("jetmetjetpt_totunc", &jetmetjetpt_totunc, "jetmetjetpt_totunc/D");
   t_RDSME->Branch("jetmetjetFlavor", &jetmetjetFlavor, "jetmetjetFlavor/D");
   t_RDSME->Branch("jetmetjeteta", &jetmetjeteta, "jetmetjeteta/D");
   t_RDSME->Branch("jetmetjetetapm", &jetmetjetetapm, "jetmetjetetapm/D");
   t_RDSME->Branch("jetmetjetphi", &jetmetjetphi, "jetmetjetphi/D");
   t_RDSME->Branch("jetmetjetoverlapmu", &jetmetjetoverlapmu, "jetmetjetoverlapmu/D");
   t_RDSME->Branch("jetmetjetoverlapele", &jetmetjetoverlapele, "jetmetjetoverlapele/D");
   t_RDSME->Branch("jetmetjet1pt", &jetmetjet1pt, "jetmetjet1pt/D");
   t_RDSME->Branch("jetmetjet1pt_totunc", &jetmetjet1pt_totunc, "jetmetjet1pt_totunc/D");
   t_RDSME->Branch("jetmetjet1Flavor", &jetmetjet1Flavor, "jetmetjet1Flavor/D");
   t_RDSME->Branch("jetmetjet1eta", &jetmetjet1eta, "jetmetjet1eta/D");
   t_RDSME->Branch("jetmetjet1etapm", &jetmetjet1etapm, "jetmetjet1etapm/D");
   t_RDSME->Branch("jetmetjet1SSVHEdisc", &jetmetjet1SSVHEdisc, "jetmetjet1SSVHEdisc/D");
   t_RDSME->Branch("jetmetjet1nVertHE", &jetmetjet1nVertHE, "jetmetjet1nVertHE/D");
   t_RDSME->Branch("jetmetjet1SSVHPdisc", &jetmetjet1SSVHPdisc, "jetmetjet1SSVHPdisc/D");
   t_RDSME->Branch("jetmetjet1nVertHP", &jetmetjet1nVertHP, "jetmetjet1nVertHP/D");
   t_RDSME->Branch("jetmetjet1SVmass", &jetmetjet1SVmass, "jetmetjet1SVmass/D");
   t_RDSME->Branch("jetmetjet1TCHEdisc", &jetmetjet1TCHEdisc, "jetmetjet1TCHEdisc/D");
   t_RDSME->Branch("jetmetjet1TCHPdisc", &jetmetjet1TCHPdisc, "jetmetjet1TCHPdisc/D");
   t_RDSME->Branch("jetmetjet2pt", &jetmetjet2pt, "jetmetjet2pt/D");
   t_RDSME->Branch("jetmetjet2pt_totunc", &jetmetjet2pt_totunc, "jetmetjet2pt_totunc/D");
   t_RDSME->Branch("jetmetjet2Flavor", &jetmetjet2Flavor, "jetmetjet2Flavor/D");
   t_RDSME->Branch("jetmetjet2eta", &jetmetjet2eta, "jetmetjet2eta/D");
   t_RDSME->Branch("jetmetjet2etapm", &jetmetjet2etapm, "jetmetjet2etapm/D");
   t_RDSME->Branch("jetmetjet2SSVHEdisc", &jetmetjet2SSVHEdisc, "jetmetjet2SSVHEdisc/D");
   t_RDSME->Branch("jetmetjet2nVertHE", &jetmetjet2nVertHE, "jetmetjet2nVertHE/D");
   t_RDSME->Branch("jetmetjet2SSVHPdisc", &jetmetjet2SSVHPdisc, "jetmetjet2SSVHPdisc/D");
   t_RDSME->Branch("jetmetjet2nVertHP", &jetmetjet2nVertHP, "jetmetjet2nVertHP/D");
   t_RDSME->Branch("jetmetjet2SVmass", &jetmetjet2SVmass, "jetmetjet2SVmass/D");
   t_RDSME->Branch("jetmetjet2TCHEdisc", &jetmetjet2TCHEdisc, "jetmetjet2TCHEdisc/D");
   t_RDSME->Branch("jetmetjet2TCHPdisc", &jetmetjet2TCHPdisc, "jetmetjet2TCHPdisc/D");
   t_RDSME->Branch("jetmetbjet1pt", &jetmetbjet1pt, "jetmetbjet1pt/D");
   t_RDSME->Branch("jetmetbjet1pt_totunc", &jetmetbjet1pt_totunc, "jetmetbjet1pt_totunc/D");
   t_RDSME->Branch("jetmetbjet1Flavor", &jetmetbjet1Flavor, "jetmetbjet1Flavor/D");
   t_RDSME->Branch("jetmetbjet1eta", &jetmetbjet1eta, "jetmetbjet1eta/D");
   t_RDSME->Branch("jetmetbjet1etapm", &jetmetbjet1etapm, "jetmetbjet1etapm/D");
   t_RDSME->Branch("jetmetbjet1SSVHEdisc", &jetmetbjet1SSVHEdisc, "jetmetbjet1SSVHEdisc/D");
   t_RDSME->Branch("jetmetbjet1nVertHE", &jetmetbjet1nVertHE, "jetmetbjet1nVertHE/D");
   t_RDSME->Branch("jetmetbjet1SSVHPdisc", &jetmetbjet1SSVHPdisc, "jetmetbjet1SSVHPdisc/D");
   t_RDSME->Branch("jetmetbjet1nVertHP", &jetmetbjet1nVertHP, "jetmetbjet1nVertHP/D");
   t_RDSME->Branch("jetmetbjet1SVmass", &jetmetbjet1SVmass, "jetmetbjet1SVmass/D");
   t_RDSME->Branch("jetmetbjet1TCHEdisc", &jetmetbjet1TCHEdisc, "jetmetbjet1TCHEdisc/D");
   t_RDSME->Branch("jetmetbjet1TCHPdisc", &jetmetbjet1TCHPdisc, "jetmetbjet1TCHPdisc/D");
   t_RDSME->Branch("jetmetbjet1pt", &jetmetbjet1pt, "jetmetbjet1pt/D");
   t_RDSME->Branch("jetmetbjet2CSVdisc", &jetmetbjet2CSVdisc, "jetmetbjet2CSVdisc/D");
   t_RDSME->Branch("jetmetbjet1CSVdisc", &jetmetbjet1CSVdisc, "jetmetbjet1CSVdisc/D");
   t_RDSME->Branch("jetmetbjet2pt_totunc", &jetmetbjet2pt_totunc, "jetmetbjet2pt_totunc/D");
   t_RDSME->Branch("jetmetbjet2Flavor", &jetmetbjet2Flavor, "jetmetbjet2Flavor/D");
   t_RDSME->Branch("jetmetbjet2eta", &jetmetbjet2eta, "jetmetbjet2eta/D");
   t_RDSME->Branch("jetmetbjet2etapm", &jetmetbjet2etapm, "jetmetbjet2etapm/D");
   t_RDSME->Branch("jetmetbjet2SSVHEdisc", &jetmetbjet2SSVHEdisc, "jetmetbjet2SSVHEdisc/D");
   t_RDSME->Branch("jetmetbjet2nVertHE", &jetmetbjet2nVertHE, "jetmetbjet2nVertHE/D");
   t_RDSME->Branch("jetmetbjet2SSVHPdisc", &jetmetbjet2SSVHPdisc, "jetmetbjet2SSVHPdisc/D");
   t_RDSME->Branch("jetmetbjet2nVertHP", &jetmetbjet2nVertHP, "jetmetbjet2nVertHP/D");
   t_RDSME->Branch("jetmetbjet2SVmass", &jetmetbjet2SVmass, "jetmetbjet2SVmass/D");
   t_RDSME->Branch("jetmetbjet2TCHEdisc", &jetmetbjet2TCHEdisc, "jetmetbjet2TCHEdisc/D");
   t_RDSME->Branch("jetmetbjet2TCHPdisc", &jetmetbjet2TCHPdisc, "jetmetbjet2TCHPdisc/D");
   t_RDSME->Branch("jetmetdptj1b1", &jetmetdptj1b1, "jetmetdptj1b1/D");
   t_RDSME->Branch("jetmetnj", &jetmetnj, "jetmetnj/D");
   t_RDSME->Branch("jetmetnb", &jetmetnb, "jetmetnb/D");
   t_RDSME->Branch("jetmetnbP", &jetmetnbP, "jetmetnbP/D");
   t_RDSME->Branch("jetmetnhf", &jetmetnhf, "jetmetnhf/D");
   t_RDSME->Branch("jetmetnef", &jetmetnef, "jetmetnef/D");
   t_RDSME->Branch("jetmetnpf", &jetmetnpf, "jetmetnpf/D");
   t_RDSME->Branch("jetmetchf", &jetmetchf, "jetmetchf/D");
   t_RDSME->Branch("jetmetnch", &jetmetnch, "jetmetnch/D");
   t_RDSME->Branch("jetmetcef", &jetmetcef, "jetmetcef/D");
   t_RDSME->Branch("jetmetjetid", &jetmetjetid, "jetmetjetid/D");
   t_RDSME->Branch("mcSelectioneventType", &mcSelectioneventType, "mcSelectioneventType/D");
   t_RDSME->Branch("lumiReweightingLumiWeight", &lumiReweightingLumiWeight, "lumiReweightingLumiWeight/D");
   t_RDSME->Branch("lumiReweightingLumiWeightUp", &lumiReweightingLumiWeightUp, "lumiReweightingLumiWeightUp/D");
   t_RDSME->Branch("lumiReweightingLumiWeightDown", &lumiReweightingLumiWeightDown, "lumiReweightingLumiWeightDown/D");
   t_RDSME->Branch("lumiReweightingpu", &lumiReweightingpu, "lumiReweightingpu/D");
   t_RDSME->Branch("lumiReweightingpv", &lumiReweightingpv, "lumiReweightingpv/D");
   t_RDSME->Branch("rc_eventSelection_0_idx", &rc_eventSelection_0_idx, "rc_eventSelection_0_idx/I");
   t_RDSME->Branch("rc_eventSelection_1_idx", &rc_eventSelection_1_idx, "rc_eventSelection_1_idx/I");
   t_RDSME->Branch("rc_eventSelection_2_idx", &rc_eventSelection_2_idx, "rc_eventSelection_2_idx/I");
   t_RDSME->Branch("rc_eventSelection_3_idx", &rc_eventSelection_3_idx, "rc_eventSelection_3_idx/I");
   t_RDSME->Branch("rc_eventSelection_4_idx", &rc_eventSelection_4_idx, "rc_eventSelection_4_idx/I");
   t_RDSME->Branch("rc_eventSelection_5_idx", &rc_eventSelection_5_idx, "rc_eventSelection_5_idx/I");
   t_RDSME->Branch("rc_eventSelection_6_idx", &rc_eventSelection_6_idx, "rc_eventSelection_6_idx/I");
   t_RDSME->Branch("rc_eventSelection_7_idx", &rc_eventSelection_7_idx, "rc_eventSelection_7_idx/I");
   t_RDSME->Branch("rc_eventSelection_8_idx", &rc_eventSelection_8_idx, "rc_eventSelection_8_idx/I");
   t_RDSME->Branch("rc_eventSelection_9_idx", &rc_eventSelection_9_idx, "rc_eventSelection_9_idx/I");
   t_RDSME->Branch("rc_eventSelection_10_idx", &rc_eventSelection_10_idx, "rc_eventSelection_10_idx/I");
   t_RDSME->Branch("rc_eventSelection_11_idx", &rc_eventSelection_11_idx, "rc_eventSelection_11_idx/I");
   t_RDSME->Branch("rc_eventSelection_12_idx", &rc_eventSelection_12_idx, "rc_eventSelection_12_idx/I");
   t_RDSME->Branch("rc_eventSelection_13_idx", &rc_eventSelection_13_idx, "rc_eventSelection_13_idx/I");
   t_RDSME->Branch("rc_eventSelection_14_idx", &rc_eventSelection_14_idx, "rc_eventSelection_14_idx/I");
   t_RDSME->Branch("rc_eventSelection_15_idx", &rc_eventSelection_15_idx, "rc_eventSelection_15_idx/I");
   t_RDSME->Branch("rc_eventSelection_16_idx", &rc_eventSelection_16_idx, "rc_eventSelection_16_idx/I");
   t_RDSME->Branch("rc_eventSelection_17_idx", &rc_eventSelection_17_idx, "rc_eventSelection_17_idx/I");
   t_RDSME->Branch("rc_eventSelection_18_idx", &rc_eventSelection_18_idx, "rc_eventSelection_18_idx/I");
   t_RDSME->Branch("rc_eventSelection_19_idx", &rc_eventSelection_19_idx, "rc_eventSelection_19_idx/I");
   t_RDSME->Branch("rc_eventSelection_20_idx", &rc_eventSelection_20_idx, "rc_eventSelection_20_idx/I");
   t_RDSME->Branch("rc_eventSelection_21_idx", &rc_eventSelection_21_idx, "rc_eventSelection_21_idx/I");
   t_RDSME->Branch("rc_eventSelection_22_idx", &rc_eventSelection_22_idx, "rc_eventSelection_22_idx/I");

   t_RDSME->Branch("mcSelectionnLepPos" , &mcSelectionnLepPos,"mcSelectionnLepPos/D");
   t_RDSME->Branch("mcSelectionnLepNeg" , &mcSelectionnLepNeg,"mcSelectionnLepNeg/D");
   t_RDSME->Branch("mcSelectionnBottom" , &mcSelectionnBottom,"mcSelectionnBottom/D");
   t_RDSME->Branch("mcSelectionnAntibottom" , &mcSelectionnAntibottom,"mcSelectionnAntibottom/D");
   t_RDSME->Branch("mcSelectionflavLepPos" , &mcSelectionflavLepPos,"mcSelectionflavLepPos/D");
   t_RDSME->Branch("mcSelectionflavLepNeg" , &mcSelectionflavLepNeg,"mcSelectionflavLepNeg/D");
   t_RDSME->Branch("mcSelectionlepPosPx" , &mcSelectionlepPosPx,"mcSelectionlepPosPx/D");
   t_RDSME->Branch("mcSelectionlepPosPy" , &mcSelectionlepPosPy,"mcSelectionlepPosPy/D");
   t_RDSME->Branch("mcSelectionlepPosPz" , &mcSelectionlepPosPz,"mcSelectionlepPosPz/D");
   t_RDSME->Branch("mcSelectionlepPosEn" , &mcSelectionlepPosEn,"mcSelectionlepPosEn/D");
   t_RDSME->Branch("mcSelectionlepNegPx" , &mcSelectionlepNegPx,"mcSelectionlepNegPx/D");
   t_RDSME->Branch("mcSelectionlepNegPy" , &mcSelectionlepNegPy,"mcSelectionlepNegPy/D");
   t_RDSME->Branch("mcSelectionlepNegPz" , &mcSelectionlepNegPz,"mcSelectionlepNegPz/D");
   t_RDSME->Branch("mcSelectionlepNegEn" , &mcSelectionlepNegEn,"mcSelectionlepNegEn/D");
   t_RDSME->Branch("mcSelectionbottomPx" , &mcSelectionbottomPx,"mcSelectionbottomPx/D");
   t_RDSME->Branch("mcSelectionbottomPy" , &mcSelectionbottomPy,"mcSelectionbottomPy/D");
   t_RDSME->Branch("mcSelectionbottomPz" , &mcSelectionbottomPz,"mcSelectionbottomPz/D");
   t_RDSME->Branch("mcSelectionbottomEn" , &mcSelectionbottomEn,"mcSelectionbottomEn/D");
   t_RDSME->Branch("mcSelectionantibottomPx" , &mcSelectionantibottomPx,"mcSelectionantibottomPx/D");
   t_RDSME->Branch("mcSelectionantibottomPy" , &mcSelectionantibottomPy,"mcSelectionantibottomPy/D");
   t_RDSME->Branch("mcSelectionantibottomPz" , &mcSelectionantibottomPz,"mcSelectionantibottomPz/D");
   t_RDSME->Branch("mcSelectionantibottomEn" , &mcSelectionantibottomEn,"mcSelectionantibottomEn/D");

   //Extra variables MLP's
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
   t_RDSME->Branch("mlphiggsvsbkg_1305_mu_ML" , &mlphiggsvsbkg_130_mu_ML,"mlphiggsvsbkg_130_mu_ML/D");
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

   t_RDSME->Branch("mlpZbbvsTT_MM" , &mlpZbbvsTT_MM,"mlpZbbvsTT_MM/D");
   t_RDSME->Branch("mlpZbbvsTT_MM_N" , &mlpZbbvsTT_MM_N,"mlpZbbvsTT_MM_N/D");
   t_RDSME->Branch("mlpZbbvsTT_ML" , &mlpZbbvsTT_ML,"mlpZbbvsTT_ML/D");

   t_RDSME->Branch("mlpZbbvsTT_mu_MM" , &mlpZbbvsTT_mu_MM,"mlpZbbvsTT_mu_MM/D");
   t_RDSME->Branch("mlpZbbvsTT_mu_MM_N" , &mlpZbbvsTT_mu_MM_N,"mlpZbbvsTT_mu_MM_N/D");
   t_RDSME->Branch("mlpZbbvsTT_mu_ML" , &mlpZbbvsTT_mu_ML,"mlpZbbvsTT_mu_ML/D");

   t_RDSME->Branch("ProdEstimator" , &ProdEstimator,"ProdEstimator/D");




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
      
      rc_eventSelection_1_idx = mc_RDS->rc_eventSelection_1_idx;
      rc_eventSelection_2_idx = mc_RDS->rc_eventSelection_2_idx;
      rc_eventSelection_3_idx = mc_RDS->rc_eventSelection_3_idx;
      rc_eventSelection_4_idx = mc_RDS->rc_eventSelection_4_idx;
      rc_eventSelection_5_idx = mc_RDS->rc_eventSelection_5_idx;
      rc_eventSelection_6_idx = mc_RDS->rc_eventSelection_6_idx;
      rc_eventSelection_7_idx = mc_RDS->rc_eventSelection_7_idx;
      rc_eventSelection_8_idx = mc_RDS->rc_eventSelection_8_idx; 
      rc_eventSelection_9_idx = mc_RDS->rc_eventSelection_9_idx;
      rc_eventSelection_10_idx = mc_RDS->rc_eventSelection_10_idx;
      rc_eventSelection_11_idx = mc_RDS->rc_eventSelection_11_idx;
      rc_eventSelection_12_idx = mc_RDS->rc_eventSelection_12_idx;
      rc_eventSelection_13_idx = mc_RDS->rc_eventSelection_13_idx;
      rc_eventSelection_14_idx = mc_RDS->rc_eventSelection_14_idx;
      rc_eventSelection_15_idx = mc_RDS->rc_eventSelection_15_idx;
      rc_eventSelection_16_idx = mc_RDS->rc_eventSelection_16_idx;
      rc_eventSelection_17_idx = mc_RDS->rc_eventSelection_17_idx;
      rc_eventSelection_18_idx = mc_RDS->rc_eventSelection_18_idx;
      rc_eventSelection_19_idx = mc_RDS->rc_eventSelection_19_idx;
      
      eventSelectionrun = mc_RDS->eventSelectionrun;
      eventSelectionevent = mc_RDS->eventSelectionevent;
      eventSelectionls = mc_RDS->eventSelectionls;
      eventSelectiontriggerSelection = mc_RDS->eventSelectiontriggerSelection;
      eventSelectiontriggerBits = mc_RDS->eventSelectiontriggerBits;
      eventSelectionzmassMu = mc_RDS->eventSelectionzmassMu;
      eventSelectionbestzmassMu = mc_RDS->eventSelectionbestzmassMu;
      eventSelectionzmassEle = mc_RDS->eventSelectionzmassEle;
      eventSelectionbestzmassEle = mc_RDS->eventSelectionbestzmassEle;
      eventSelectionzptMu = mc_RDS->eventSelectionzptMu;
      eventSelectionbestzptMu = mc_RDS->eventSelectionbestzptMu;
      eventSelectionzptEle = mc_RDS->eventSelectionzptEle;
      eventSelectionbestzptEle = mc_RDS->eventSelectionbestzptEle;
      eventSelectionscaldptZbj1 = mc_RDS->eventSelectionscaldptZbj1;
      eventSelectiondrZbj1 = mc_RDS->eventSelectiondrZbj1;
      eventSelectiondphiZbj1 = mc_RDS->eventSelectiondphiZbj1;
      eventSelectionscaldptZbb = mc_RDS->eventSelectionscaldptZbb;
      eventSelectiondphiZbb = mc_RDS->eventSelectiondphiZbb;
      eventSelectiondrZbb = mc_RDS->eventSelectiondrZbb;
      eventSelectiondijetM = mc_RDS->eventSelectiondijetM;
      eventSelectiondijetPt = mc_RDS->eventSelectiondijetPt;
      eventSelectiondijetdR = mc_RDS->eventSelectiondijetdR;
      eventSelectiondijetSVdR = mc_RDS->eventSelectiondijetSVdR;
      eventSelectiondphidijetMET = mc_RDS->eventSelectiondphidijetMET;
      eventSelectionZbM = mc_RDS->eventSelectionZbM;
      eventSelectionZbPt = mc_RDS->eventSelectionZbPt;
      eventSelectionZbbM = mc_RDS->eventSelectionZbbM;
      eventSelectionZbbPt = mc_RDS->eventSelectionZbbPt;
      eventSelectioncategory = mc_RDS->eventSelectioncategory;
      eventSelectionmu1pt = mc_RDS->eventSelectionmu1pt;
      eventSelectionmu2pt = mc_RDS->eventSelectionmu2pt;
      eventSelectionmu1eta = mc_RDS->eventSelectionmu1eta;
      eventSelectionmu2eta = mc_RDS->eventSelectionmu2eta;
      eventSelectionmu1etapm = mc_RDS->eventSelectionmu1etapm;
      eventSelectionmu2etapm = mc_RDS->eventSelectionmu2etapm;
      eventSelectionel1pt = mc_RDS->eventSelectionel1pt;
      eventSelectionel2pt = mc_RDS->eventSelectionel2pt;
      eventSelectionel1eta = mc_RDS->eventSelectionel1eta;
      eventSelectionel2eta = mc_RDS->eventSelectionel2eta;
      eventSelectionel1etapm = mc_RDS->eventSelectionel1etapm;
      eventSelectionel2etapm = mc_RDS->eventSelectionel2etapm;

      jetmetSSVHEdisc = mc_RDS->jetmetSSVHEdisc;
      jetmetnVertHE = mc_RDS->jetmetnVertHE;
      jetmetSSVHPdisc = mc_RDS->jetmetSSVHPdisc;
      jetmetnVertHP = mc_RDS->jetmetnVertHP;
      jetmetSVmass = mc_RDS->jetmetSVmass;
      jetmetSSVHEdiscDisc1 = mc_RDS->jetmetSSVHEdiscDisc1;
      jetmetSSVHPdiscDisc1 = mc_RDS->jetmetSSVHPdiscDisc1;
      jetmetMET = mc_RDS->jetmetMET;
      jetmetMETphi = mc_RDS->jetmetMETphi;
      jetmetMETsignificance = mc_RDS->jetmetMETsignificance;
      jetmetjetpt = mc_RDS->jetmetjetpt;
      jetmetjetpt_totunc = mc_RDS->jetmetjetpt_totunc;
      jetmetjetFlavor = mc_RDS->jetmetjetFlavor;
      jetmetjeteta = mc_RDS->jetmetjeteta;
      jetmetjetetapm = mc_RDS->jetmetjetetapm;
      jetmetjetphi = mc_RDS->jetmetjetphi;
      jetmetjetoverlapmu = mc_RDS->jetmetjetoverlapmu;
      jetmetjetoverlapele = mc_RDS->jetmetjetoverlapele;
      jetmetjet1pt = mc_RDS->jetmetjet1pt;
      jetmetjet1pt_totunc = mc_RDS->jetmetjet1pt_totunc;
      jetmetjet1Flavor = mc_RDS->jetmetjet1Flavor;
      jetmetjet1eta = mc_RDS->jetmetjet1eta;
      jetmetjet1etapm = mc_RDS->jetmetjet1etapm;
      jetmetjet1SSVHEdisc = mc_RDS->jetmetjet1SSVHEdisc;
      jetmetjet1nVertHE = mc_RDS->jetmetjet1nVertHE;
      jetmetjet1SSVHPdisc = mc_RDS->jetmetjet1SSVHPdisc;
      jetmetjet1nVertHP = mc_RDS->jetmetjet1nVertHP;
      jetmetjet1SVmass = mc_RDS->jetmetjet1SVmass;
      jetmetjet2pt = mc_RDS->jetmetjet2pt;
      jetmetjet2pt_totunc = mc_RDS->jetmetjet2pt_totunc;
      jetmetjet2Flavor = mc_RDS->jetmetjet2Flavor;
      jetmetjet2eta = mc_RDS->jetmetjet2eta;
      jetmetjet2etapm = mc_RDS->jetmetjet2etapm;
      jetmetjet2SSVHEdisc = mc_RDS->jetmetjet2SSVHEdisc;
      jetmetjet2nVertHE = mc_RDS->jetmetjet2nVertHE;
      jetmetjet2SSVHPdisc = mc_RDS->jetmetjet2SSVHPdisc;
      jetmetjet2nVertHP = mc_RDS->jetmetjet2nVertHP;
      jetmetjet2SVmass = mc_RDS->jetmetjet2SVmass;
      jetmetbjet1pt = mc_RDS->jetmetbjet1pt;
      jetmetbjet1pt_totunc = mc_RDS->jetmetbjet1pt_totunc;
      jetmetbjet1CSVdisc = mc_RDS->jetmetbjet1CSVdisc;
      jetmetbjet2CSVdisc = mc_RDS->jetmetbjet2CSVdisc;
      jetmetbjet1Flavor = mc_RDS->jetmetbjet1Flavor;
      jetmetbjet1eta = mc_RDS->jetmetbjet1eta;
      jetmetbjet1etapm = mc_RDS->jetmetbjet1etapm;
      jetmetbjet1SSVHEdisc = mc_RDS->jetmetbjet1SSVHEdisc;
      jetmetbjet1nVertHE = mc_RDS->jetmetbjet1nVertHE;
      jetmetbjet1SSVHPdisc = mc_RDS->jetmetbjet1SSVHPdisc;
      jetmetbjet1nVertHP = mc_RDS->jetmetbjet1nVertHP;
      jetmetbjet1SVmass = mc_RDS->jetmetbjet1SVmass;
      jetmetbjet2pt = mc_RDS->jetmetbjet2pt;
      jetmetbjet2pt_totunc = mc_RDS->jetmetbjet2pt_totunc;
      jetmetbjet2Flavor = mc_RDS->jetmetbjet2Flavor;
      jetmetbjet2eta = mc_RDS->jetmetbjet2eta;
      jetmetbjet2etapm = mc_RDS->jetmetbjet2etapm;
      jetmetbjet2SSVHEdisc = mc_RDS->jetmetbjet2SSVHEdisc;
      jetmetbjet2nVertHE = mc_RDS->jetmetbjet2nVertHE;
      jetmetbjet2SSVHPdisc = mc_RDS->jetmetbjet2SSVHPdisc;
      jetmetbjet2nVertHP = mc_RDS->jetmetbjet2nVertHP;
      jetmetbjet2SVmass = mc_RDS->jetmetbjet2SVmass;
      jetmetdptj1b1 = mc_RDS->jetmetdptj1b1;
      jetmetnj = mc_RDS->jetmetnj;
      jetmetnb = mc_RDS->jetmetnb;
      jetmetnbP = mc_RDS->jetmetnbP;
      jetmetnhf = mc_RDS->jetmetnhf;
      jetmetnef = mc_RDS->jetmetnef;
      jetmetnpf = mc_RDS->jetmetnpf;
      jetmetchf = mc_RDS->jetmetchf;
      jetmetnch = mc_RDS->jetmetnch;
      jetmetcef = mc_RDS->jetmetcef;
      jetmetjetid = mc_RDS->jetmetjetid;


      BtaggingReweightingHE = mc_RDS->BtaggingReweightingHE;
      BtaggingReweightingHP = mc_RDS->BtaggingReweightingHP;
      BtaggingReweightingHEexcl = mc_RDS->BtaggingReweightingHEexcl;
      BtaggingReweightingHPexcl = mc_RDS->BtaggingReweightingHPexcl;
      BtaggingReweightingHEHE = mc_RDS->BtaggingReweightingHEHE;
      BtaggingReweightingHEHP = mc_RDS->BtaggingReweightingHEHP;
      BtaggingReweightingHPHP = mc_RDS->BtaggingReweightingHPHP;
      LeptonsReweightingweight = mc_RDS->LeptonsReweightingweight;
      lumiReweightingLumiWeight = mc_RDS->lumiReweightingLumiWeight;
      lumiReweightingLumiWeightUp = mc_RDS->lumiReweightingLumiWeightUp;
      lumiReweightingLumiWeightDown = mc_RDS->lumiReweightingLumiWeightDown;

      mcSelectioneventType = mc_RDS->mcSelectioneventType;
      mcSelectionnLepPos = mc_RDS->mcSelectionNLepPos;
      mcSelectionnLepNeg = mc_RDS->mcSelectionNLepNeg;
      mcSelectionnBottom = mc_RDS->mcSelectionNBottom;
      mcSelectionnAntibottom = mc_RDS->mcSelectionNAntibottom;
      mcSelectionflavLepPos = mc_RDS->mcSelectionFlavLepPos;
      mcSelectionflavLepNeg = mc_RDS->mcSelectionFlavLepNeg;
      mcSelectionlepPosPx = mc_RDS->mcSelectionLepPosPx;
      mcSelectionlepPosPy = mc_RDS->mcSelectionLepPosPy;
      mcSelectionlepPosPz = mc_RDS->mcSelectionLepPosPz;
      mcSelectionlepPosEn = mc_RDS->mcSelectionLepPosEn;
      mcSelectionlepNegPx = mc_RDS->mcSelectionLepNegPx;
      mcSelectionlepNegPy = mc_RDS->mcSelectionLepNegPy;
      mcSelectionlepNegPz = mc_RDS->mcSelectionLepNegPz;
      mcSelectionlepNegEn = mc_RDS->mcSelectionLepNegEn;
      mcSelectionbottomPx = mc_RDS->mcSelectionBottomPx;
      mcSelectionbottomPy = mc_RDS->mcSelectionBottomPy;
      mcSelectionbottomPz = mc_RDS->mcSelectionBottomPz;
      mcSelectionbottomEn = mc_RDS->mcSelectionBottomEn;
      mcSelectionantibottomPx = mc_RDS->mcSelectionAntibottomPx;
      mcSelectionantibottomPy = mc_RDS->mcSelectionAntibottomPy;
      mcSelectionantibottomPz = mc_RDS->mcSelectionAntibottomPz;
      mcSelectionantibottomEn = mc_RDS->mcSelectionAntibottomEn;
      
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


        Inv_Mass_bb = mc_ME->Inv_Mass_bb;
        Inv_Mass_lept = mc_ME->Inv_Mass_lept;
	
//---------------------- NN  output here ---------------------------------
        // For DY vs TT
	mlpZbbvsTT_MM = MLP_TT_vs_DY_MM_ee->Value(0, Wgg, Wqq, Wtt);
        mlpZbbvsTT_MM_N = MLP_TT_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Wtt);
        mlpZbbvsTT_ML = MLP_TT_vs_DY_ML_ee->Value(0, Wgg, Wqq, Wtt);
	mlpZbbvsTT_mu_MM = MLP_TT_vs_DY_MM_mm->Value(0, Wgg, Wqq, Wtt);
        mlpZbbvsTT_mu_MM_N = MLP_TT_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Wtt);
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
        mlphiggsvszbb_115_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)));
        mlphiggsvszz_115_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_115 , Whi3_115)));
        mlphiggsvstt_115_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_115 , Whi3_115)));
        mlphiggsvsbkg_115_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb->Value(0,mlphiggsvszbb_115_comb_MM_N,mlphiggsvszz_115_comb_MM_N,mlphiggsvstt_115_comb_MM_N )));
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
        mlphiggsvszbb_120_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)));
        mlphiggsvszz_120_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_120 , Whi3_120)));
        mlphiggsvstt_120_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_120 , Whi3_120)));
        mlphiggsvsbkg_120_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb->Value(0,mlphiggsvszbb_120_comb_MM_N,mlphiggsvszz_120_comb_MM_N,mlphiggsvstt_120_comb_MM_N ))); 
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
        mlphiggsvszbb_130_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)));
        mlphiggsvszz_130_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_130 , Whi3_130)));
        mlphiggsvstt_130_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_130 , Whi3_130)));
        mlphiggsvsbkg_130_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb->Value(0,mlphiggsvszbb_130_comb_MM_N,mlphiggsvszz_130_comb_MM_N,mlphiggsvstt_130_comb_MM_N )));
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
        mlphiggsvszbb_135_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)));
        mlphiggsvszz_135_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3, Whi0_135 , Whi3_135)));
        mlphiggsvstt_135_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_135 , Whi3_135)));
        mlphiggsvsbkg_135_comb_MM_N = max(0.0,min(1.0,MLP_higgs_vs_BKG_MM_N_comb->Value(0,mlphiggsvszbb_135_comb_MM_N,mlphiggsvszz_135_comb_MM_N,mlphiggsvstt_135_comb_MM_N )));
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
	if (InputFile.Contains("DATA")){
	  if( MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_MM=-999.;}
	  if( MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_MM=-999.;}
	  if( MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_MM=-999.;}
	  if( MLP_higgs_vs_BKG_MM_ee->Value(0, MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_125 , Whi3_125)) > 0.5 ){mlphiggsvsbkg_125_MM=-999.;}
	  if( MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_mu_MM=-999.;}
	  if( MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_mu_MM=-999.;}
	  if( MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_mu_MM=-999.;}
	  if( MLP_higgs_vs_BKG_MM_mm->Value(0, MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_125 , Whi3_125) ) > 0.5 ){mlphiggsvsbkg_125_mu_MM=-999.;}
          if( MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_ee->Value(0, MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_125 , Whi3_125)) > 0.5 ){mlphiggsvsbkg_125_MM_N=-999.;}
          if( MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_mu_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_mu_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_mu_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_mm->Value(0, MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_125 , Whi3_125) ) > 0.5 ){mlphiggsvsbkg_125_mu_MM_N=-999.;}
          if( MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_ML=-999.;}
          if( MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_ML=-999.;}
          if( MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_ML=-999.;}
          if( MLP_higgs_vs_BKG_ML_ee->Value(0, MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_125 , Whi3_125)) > 0.5 ){mlphiggsvsbkg_125_ML=-999.;}
          if( MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_mu_ML=-999.;}
          if( MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_mu_ML=-999.;}
          if( MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_mu_ML=-999.;}
          if( MLP_higgs_vs_BKG_ML_mm->Value(0, MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_125 , Whi3_125) ) > 0.5 ){mlphiggsvsbkg_125_mu_ML=-999.;}
	  if( MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125)>0.5){mlphiggsvszbb_125_comb_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_125 , Whi3_125)>0.5){mlphiggsvstt_125_comb_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125)>0.5){mlphiggsvszz_125_comb_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_comb->Value(0, MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_125 , Whi3_125), MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_125 , Whi3_125) ,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_125 , Whi3_125) ) > 0.5 ){mlphiggsvsbkg_125_comb_MM_N=-999.;}
	}
        // For H 115
        if (InputFile.Contains("DATA")){
          if( MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_MM=-999.;}
          if( MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_MM=-999.;}
          if( MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_MM=-999.;}
          if( MLP_higgs_vs_BKG_MM_ee->Value(0, MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_115 , Whi3_115)) > 0.5 ){mlphiggsvsbkg_115_MM=-999.;}
          if( MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_mu_MM=-999.;}
          if( MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_mu_MM=-999.;}
          if( MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_mu_MM=-999.;}
          if( MLP_higgs_vs_BKG_MM_mm->Value(0, MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_115 , Whi3_115) ) > 0.5 ){mlphiggsvsbkg_115_mu_MM=-999.;}
          if( MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_ee->Value(0, MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_115 , Whi3_115)) > 0.5 ){mlphiggsvsbkg_115_MM_N=-999.;}
          if( MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_mu_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_mu_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_mu_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_mm->Value(0, MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_115 , Whi3_115) ) > 0.5 ){mlphiggsvsbkg_115_mu_MM_N=-999.;}
          if( MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_ML=-999.;}
          if( MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_ML=-999.;}
          if( MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_ML=-999.;}
          if( MLP_higgs_vs_BKG_ML_ee->Value(0, MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_115 , Whi3_115)) > 0.5 ){mlphiggsvsbkg_115_ML=-999.;}
          if( MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_mu_ML=-999.;}
          if( MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_mu_ML=-999.;}
          if( MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_mu_ML=-999.;}
          if( MLP_higgs_vs_BKG_ML_mm->Value(0, MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_115 , Whi3_115) ) > 0.5 ){mlphiggsvsbkg_115_mu_ML=-999.;}
          if( MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115)>0.5){mlphiggsvszbb_115_comb_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_115 , Whi3_115)>0.5){mlphiggsvstt_115_comb_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115)>0.5){mlphiggsvszz_115_comb_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_comb->Value(0, MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_115 , Whi3_115), MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_115 , Whi3_115) ,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_115 , Whi3_115) ) > 0.5 ){mlphiggsvsbkg_115_comb_MM_N=-999.;}	
		
		}
	// For H 120
        if (InputFile.Contains("DATA")){
          if( MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_MM=-999.;}
          if( MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_MM=-999.;}
          if( MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_MM=-999.;}
          if( MLP_higgs_vs_BKG_MM_ee->Value(0, MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_120 , Whi3_120)) > 0.5 ){mlphiggsvsbkg_120_MM=-999.;}
          if( MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_mu_MM=-999.;}
          if( MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_mu_MM=-999.;}
          if( MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_mu_MM=-999.;}
          if( MLP_higgs_vs_BKG_MM_mm->Value(0, MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_120 , Whi3_120) ) > 0.5 ){mlphiggsvsbkg_120_mu_MM=-999.;}
          if( MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_ee->Value(0, MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_120 , Whi3_120)) > 0.5 ){mlphiggsvsbkg_120_MM_N=-999.;}
          if( MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_mu_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_mu_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_mu_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_mm->Value(0, MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_120 , Whi3_120) ) > 0.5 ){mlphiggsvsbkg_120_mu_MM_N=-999.;}
          if( MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_ML=-999.;}
          if( MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_ML=-999.;}
          if( MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_ML=-999.;}
          if( MLP_higgs_vs_BKG_ML_ee->Value(0, MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_120 , Whi3_120)) > 0.5 ){mlphiggsvsbkg_120_ML=-999.;}
          if( MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_mu_ML=-999.;}
          if( MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_mu_ML=-999.;}
          if( MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_mu_ML=-999.;}
          if( MLP_higgs_vs_BKG_ML_mm->Value(0, MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_120 , Whi3_120) ) > 0.5 ){mlphiggsvsbkg_120_mu_ML=-999.;}
	  if( MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120)>0.5){mlphiggsvszbb_120_comb_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_120 , Whi3_120)>0.5){mlphiggsvstt_120_comb_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120)>0.5){mlphiggsvszz_120_comb_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_comb->Value(0, MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_120 , Whi3_120), MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_120 , Whi3_120) ,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_120 , Whi3_120) ) > 0.5 ){mlphiggsvsbkg_120_comb_MM_N=-999.;}

	
	}
        // For H 130
        if (InputFile.Contains("DATA")){
	  if( MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_MM=-999.;}
          if( MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_MM=-999.;}
          if( MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_MM=-999.;}
          if( MLP_higgs_vs_BKG_MM_ee->Value(0, MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_130 , Whi3_130)) > 0.5 ){mlphiggsvsbkg_130_MM=-999.;}
          if( MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_mu_MM=-999.;}
          if( MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_mu_MM=-999.;}
          if( MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_mu_MM=-999.;}
          if( MLP_higgs_vs_BKG_MM_mm->Value(0, MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_130 , Whi3_130) ) > 0.5 ){mlphiggsvsbkg_130_mu_MM=-999.;}
          if( MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_ee->Value(0, MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_130 , Whi3_130)) > 0.5 ){mlphiggsvsbkg_130_MM_N=-999.;}
          if( MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_mu_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_mu_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_mu_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_mm->Value(0, MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_130 , Whi3_130) ) > 0.5 ){mlphiggsvsbkg_130_mu_MM_N=-999.;}
          if( MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_ML=-999.;}
          if( MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_ML=-999.;}
          if( MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_ML=-999.;}
          if( MLP_higgs_vs_BKG_ML_ee->Value(0, MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_130 , Whi3_130)) > 0.5 ){mlphiggsvsbkg_130_ML=-999.;}
          if( MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_mu_ML=-999.;}
          if( MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_mu_ML=-999.;}
          if( MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_mu_ML=-999.;}
          if( MLP_higgs_vs_BKG_ML_mm->Value(0, MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_130 , Whi3_130) ) > 0.5 ){mlphiggsvsbkg_130_mu_ML=-999.;}
	  if( MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130)>0.5){mlphiggsvszbb_130_comb_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_130 , Whi3_130)>0.5){mlphiggsvstt_130_comb_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130)>0.5){mlphiggsvszz_130_comb_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_comb->Value(0, MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_130 , Whi3_130), MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_130 , Whi3_130) ,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_130 , Whi3_130) ) > 0.5 ){mlphiggsvsbkg_130_comb_MM_N=-999.;}
	
	}
	// For H 135
        if (InputFile.Contains("DATA")){
	  if( MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_MM=-999.;}
          if( MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_MM=-999.;}
          if( MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_MM=-999.;}
          if( MLP_higgs_vs_BKG_MM_ee->Value(0, MLP_higgs_vs_DY_MM_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_MM_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_MM_ee->Value(0, Wtt,Whi0_135 , Whi3_135)) > 0.5 ){mlphiggsvsbkg_135_MM=-999.;}
          if( MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_mu_MM=-999.;}
          if( MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_mu_MM=-999.;}
          if( MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_mu_MM=-999.;}
          if( MLP_higgs_vs_BKG_MM_mm->Value(0, MLP_higgs_vs_DY_MM_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_MM_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_MM_mm->Value(0, Wtt, Whi0_135 , Whi3_135) ) > 0.5 ){mlphiggsvsbkg_135_mu_MM=-999.;}
          if( MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_ee->Value(0, MLP_higgs_vs_DY_MM_N_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_MM_N_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_MM_N_ee->Value(0, Wtt,Whi0_135 , Whi3_135)) > 0.5 ){mlphiggsvsbkg_135_MM_N=-999.;}
          if( MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_mu_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_mu_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_mu_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_mm->Value(0, MLP_higgs_vs_DY_MM_N_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_MM_N_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_MM_N_mm->Value(0, Wtt, Whi0_135 , Whi3_135) ) > 0.5 ){mlphiggsvsbkg_135_mu_MM_N=-999.;}
          if( MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_ML=-999.;}
          if( MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_ML=-999.;}
          if( MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_ML=-999.;}
          if( MLP_higgs_vs_BKG_ML_ee->Value(0, MLP_higgs_vs_DY_ML_ee->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_ML_ee->Value(0, Wzz0 , Wzz3 ,Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_ML_ee->Value(0, Wtt,Whi0_135 , Whi3_135)) > 0.5 ){mlphiggsvsbkg_135_ML=-999.;}
          if( MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_mu_ML=-999.;}
          if( MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_mu_ML=-999.;}
          if( MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_mu_ML=-999.;}
          if( MLP_higgs_vs_BKG_ML_mm->Value(0, MLP_higgs_vs_DY_ML_mm->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_ML_mm->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_ML_mm->Value(0, Wtt, Whi0_135 , Whi3_135) ) > 0.5 ){mlphiggsvsbkg_135_mu_ML=-999.;}	
	  if( MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135)>0.5){mlphiggsvszbb_135_comb_MM_N=-999.;}
          if( MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_135 , Whi3_135)>0.5){mlphiggsvstt_135_comb_MM_N=-999.;}
          if( MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135)>0.5){mlphiggsvszz_135_comb_MM_N=-999.;}
          if( MLP_higgs_vs_BKG_MM_N_comb->Value(0, MLP_higgs_vs_DY_MM_N_comb->Value(0, Wgg, Wqq, Whi0_135 , Whi3_135), MLP_higgs_vs_ZZ_MM_N_comb->Value(0, Wzz0 , Wzz3 , Whi0_135 , Whi3_135) ,MLP_higgs_vs_TT_MM_N_comb->Value(0, Wtt, Whi0_135 , Whi3_135) ) > 0.5 ){mlphiggsvsbkg_135_comb_MM_N=-999.;}

	}


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
   //CreateParentTree("MuA_DATA");
   //CreateParentTree("ElA_DATA");
   //CreateParentTree("MuB_DATA");
   //CreateParentTree("ElB_DATA");
   //CreateParentTree("Mu_MC");
   //CreateParentTree("El_MC");
   CreateParentTree("DY_Pt100_El_MC");
   //CreateParentTree("TT_Mu_MC");
   //CreateParentTree("TT_El_MC");
   //CreateParentTree("ZZ_Mu_MC");
   //CreateParentTree("ZZ_El_MC");
   //CreateParentTree("ZH125_Mu_MC");
   //CreateParentTree("ZH125_El_MC");
   //CreateParentTree("ZH115_Mu_MC");
   //CreateParentTree("ZH115_El_MC");
   //CreateParentTree("ZH120_Mu_MC");
   //CreateParentTree("ZH120_El_MC");
   //CreateParentTree("ZH130_Mu_MC");
   //CreateParentTree("ZH130_El_MC");
   //CreateParentTree("ZH135_Mu_MC");
   //CreateParentTree("ZH135_El_MC");
}

//mergeOneSample(InputFile = "Mu_DATA")
//mergeOneSample(InputFile = "Mu_MC")
//mergeOneSample(InputFile = "Ttbar_Mu_MC")
//mergeOneSample(InputFile = "ZZ_Mu_MC")


