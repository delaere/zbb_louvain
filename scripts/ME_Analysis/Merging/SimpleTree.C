

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

#include "rds_zbb.C"
#include "tree2.C"
#include "MLP_Higgs_vs_Zbb_EE_TIGHT.cxx"
#include "MLP_Zbb_tt_EE.cxx"
#include "MLP_Zbb_tt_Comb_EE_TIGHT.cxx"
#include "MLP_Zbb_tt_Comb_met_EE.cxx"
#include "MLP_Zbb_tt_multi_EE_TIGHT.cxx"

#include "MLP_Higgs_vs_ZZ3_EE_TIGHT.cxx"
#include "MLP_Higgs_vs_tt_EE_TIGHT.cxx"

#include "MLP_Higgs_vs_bkg_EE_TIGHT.cxx"
#include "MLP_Higgs_vs_bkg_EE_FULLL.cxx"

#include <iostream>
#include <map>


//I'm not able to compile a root macro within RooFit stuff within ROOT
//#include "RooFit.h"
//#include "RooWorkspace.h"
// use this order for safety on library loading
//using namespace RooFit ;
//using namespace RooStats ;


 
 
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
   Int_t           eventNumber;
   Int_t           runNumber;
   Double_t        Wgg;
   Double_t        Wqq;
   Double_t        Wtt;
   Double_t        Wtwb;
   Double_t        Wzz3;
   Double_t        Wzz0;
   Double_t        Whi3;
   Double_t        Whi0;
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
   
   //Here extra variables
   MLP_Higgs_vs_Zbb_EE_TIGHT *MLP_higgs_vs_zbb = 0;
   MLP_Higgs_vs_ZZ3_EE_TIGHT *MLP_higgs_vs_zz = 0;
   MLP_Higgs_vs_tt_EE_TIGHT *MLP_higgs_vs_tt = 0;

   MLP_Higgs_vs_bkg_EE_TIGHT *MLP_higgs_vs_bkg =0;
   MLP_Higgs_vs_bkg_EE_FULLL *MLP_higgs_vs_bkg_fulll =0;

   MLP_Zbb_tt_EE* MLP_zbbvstt = 0;
   MLP_Zbb_tt_Comb_EE_TIGHT* MLP_zbbvstttight = 0;
   MLP_Zbb_tt_Comb_met_EE* MLP_zbbvstt_tight_Wmet = 0;
   MLP_Zbb_tt_multi_EE_TIGHT* MLP_zbbvstt_multi_EE_tight =0;

   Double_t mlphiggsvszbb;
   Double_t mlphiggsvszz;
   Double_t mlphiggsvstt;
   Double_t mlphiggsvsbkg;
   Double_t mlphiggsvsbkg_fulll;


   Double_t mlpZbbvsTT;
   Double_t mlpZbbvsTTtight;
   Double_t mlpZbbvsTT_tight_Wmet;
   Double_t mlpzbbvstt_multi_EE_tight;


   
void CreateParentTree(TString InputFile) {
   // create a simple TTree with 5 branches
   // Two branches ("Run" and "Event") will be used to index the Tree


// 
//    Int_t Run, Event;
//    Float_t x,y,z;
//    TFile *f = new TFile("treeparent.root","recreate");
//    TTree *T = new TTree("T","test friend trees");
//    T->Branch("Run",&Run,"Run/I");
//    T->Branch("Event",&Event,"Event/I");
//    T->Branch("x",&x,"x/F");
//    T->Branch("y",&y,"y/F");
//    T->Branch("z",&z,"z/F");
//    TRandom r;
//    for (Int_t i=0;i<10000;i++) {
//       if (i < 5000) Run = 1;
//       else          Run = 2;
//       Event = i;
//       x = r.Gaus(10,1);
//       y = r.Gaus(20,2);
//       z = r.Landau(2,1);
//       T->Fill();
//    }
//    T->Print();
//    T->Write();
//    delete f;
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
   
   MLP_higgs_vs_zbb = new MLP_Higgs_vs_Zbb_EE_TIGHT();
   MLP_higgs_vs_zz = new MLP_Higgs_vs_ZZ3_EE_TIGHT();
   MLP_higgs_vs_tt = new MLP_Higgs_vs_tt_EE_TIGHT();
   MLP_higgs_vs_bkg = new MLP_Higgs_vs_bkg_EE_TIGHT();
   MLP_higgs_vs_bkg_fulll = new MLP_Higgs_vs_bkg_EE_FULLL();


   MLP_zbbvstt = new MLP_Zbb_tt_EE();
   MLP_zbbvstttight = new MLP_Zbb_tt_Comb_EE_TIGHT();
   MLP_zbbvstt_tight_Wmet = new MLP_Zbb_tt_Comb_met_EE();
   MLP_zbbvstt_multi_EE_tight = new MLP_Zbb_tt_multi_EE_TIGHT();

   TFile* f_RDS  = new TFile("testsMergeRDSnoWS120721/Tree_File_rds_zbb_" + InputFile + ".root");
   TTree* t_RDS    = (TTree*)f_RDS->Get("rds_zbb");  

   TString mename = "testsMergeRDSnoWS120721/ME_zbb_" + InputFile + ".root";
   mename.ReplaceAll("A_DATA", "_DATA");
   mename.ReplaceAll("B_DATA", "_DATA");

   TFile* f_ME  = new TFile(mename);
   TTree* t_ME    = (TTree*)f_ME->Get("tree2");  




   
   TFile *f_RDSME = new TFile("testsMergeRDSnoWS120721/Tree_rdsME_" +InputFile + ".root", "RECREATE");
   TTree *t_RDSME = new TTree("rds_zbb", "merged zbb-ME tree");




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
   t_RDSME->Branch("eventNumber", &eventNumber, "eventNumber/I");
   t_RDSME->Branch("runNumber", &runNumber, "runNumber/I");
   t_RDSME->Branch("Wgg", &Wgg, "Wgg/D");
   t_RDSME->Branch("Wqq", &Wqq, "Wqq/D");
   t_RDSME->Branch("Wtt", &Wtt, "Wtt/D");
   t_RDSME->Branch("Wtwb", &Wtwb, "Wtwb/D");
   t_RDSME->Branch("Wzz3", &Wzz3, "Wzz3/D");
   t_RDSME->Branch("Wzz0", &Wzz0, "Wzz0/D");
   t_RDSME->Branch("Whi3", &Whi3, "Whi3/D");
   t_RDSME->Branch("Whi0", &Whi0, "Whi0/D");
   t_RDSME->Branch("eventSelectionrun", &eventSelectionrun, "eventSelectionrun/I");
   t_RDSME->Branch("eventSelectionevent", &eventSelectionevent, "eventSelectionevent/I");
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
   t_RDSME->Branch("jetmetbjet2pt", &jetmetbjet2pt, "jetmetbjet2pt/D");
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

   //Here extra variables
   t_RDSME->Branch("mlphiggsvszbb" , &mlphiggsvszbb,"mlphiggsvszbb/D");
   t_RDSME->Branch("mlphiggsvstt" , &mlphiggsvstt,"mlphiggsvstt/D");
   t_RDSME->Branch("mlphiggsvszz" , &mlphiggsvszz,"mlphiggsvszz/D");
   t_RDSME->Branch("mlphiggsvsbkg" , &mlphiggsvsbkg,"mlphiggsvsbkg/D");
   t_RDSME->Branch("mlphiggsvsbkg_fulll" , &mlphiggsvsbkg_fulll,"mlphiggsvsbkg_fulll/D");
   t_RDSME->Branch("mlpZbbvsTT" , &mlpZbbvsTT,"mlpZbbvsTT/D");
   t_RDSME->Branch("mlpZbbvsTTtight" , &mlpZbbvsTTtight,"mlpZbbvsTTtight/D");
   t_RDSME->Branch("mlpZbbvsTT_tight_Wmet" , &mlpZbbvsTT_tight_Wmet,"mlpZbbvsTT_tight_Wmet/D");
   t_RDSME->Branch("mlpzbbvstt_multi_EE_tight",&mlpzbbvstt_multi_EE_tight,"mlpzbbvstt_multi_EE_tight/D");

   //t_RDS->BuildIndex("eventSelectionrun","eventSelectionevent");
   //t_RDS->AddFriend(t_ME);

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
        map_runevent[pair<long int, long int>(long(mc_ME->runNumber), int(mc_ME->eventNumber))] = iME + 1;
      else
        map_runevent[pair<long int, long int>(1, int(mc_ME->eventNumber))] = iME + 1;

      //std::cout << map_runevent.size() << std::endl;
   }
   

   //Second loop to larger RDS sample, break right away if not selected step fulfilled
   Long64_t nbytesRDS = 0, nbRDS = 0;
   for (Int_t iRDS=0;iRDS<t_RDS->GetEntries();iRDS++) {

      Long64_t ientry = mc_RDS->LoadTree(iRDS);
      if (ientry < 0 ) break;
      nbRDS = mc_RDS->GetEntry(iRDS);   nbytesRDS += nbRDS;
      //if (mc_RDS->rc_eventSelection_12_idx == 0) continue;
      if (mc_RDS->rc_eventSelection_9_idx == 0) continue;
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
      eventSelectiondrZbb = mc_RDS->eventSelectiondrZbb;
      eventSelectiondijetM = mc_RDS->eventSelectiondijetM;

      eventSelectionbestzmassEle = mc_RDS->eventSelectionbestzmassEle;
      eventSelectionbestzmassMu = mc_RDS->eventSelectionbestzmassMu;
      eventSelectiondijetdR = mc_RDS->eventSelectiondijetdR;
      eventSelectionZbM = mc_RDS->eventSelectionZbM;
      jetmetMETsignificance = mc_RDS->jetmetMETsignificance;
      jetmetMET = mc_RDS->jetmetMET;
      jetmetnj = mc_RDS->jetmetnj;


      BtaggingReweightingHE = mc_RDS->BtaggingReweightingHE;
      BtaggingReweightingHP = mc_RDS->BtaggingReweightingHP;
      BtaggingReweightingHEexcl = mc_RDS->BtaggingReweightingHEexcl;
      BtaggingReweightingHPexcl = mc_RDS->BtaggingReweightingHPexcl;
      BtaggingReweightingHEHE = mc_RDS->BtaggingReweightingHEHE;
      BtaggingReweightingHEHP = mc_RDS->BtaggingReweightingHEHP;
      BtaggingReweightingHPHP = mc_RDS->BtaggingReweightingHPHP;
      LeptonsReweightingweight = mc_RDS->LeptonsReweightingweight;
      lumiReweightingLumiWeight = mc_RDS->lumiReweightingLumiWeight;

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
      if (IsDATA) MEentry = map_runevent[pair<long int, long int>(int(mc_RDS->eventSelectionrun), int(mc_RDS->eventSelectionevent))];
      else  MEentry = map_runevent[pair<long int, long int>(1, int(mc_RDS->eventSelectionevent))];
      
      if (MEentry==0) {
        printf("Not Found [%i, %i]\n", int(mc_RDS->eventSelectionrun), int(mc_RDS->eventSelectionevent));
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
        Whi3 = 0;
        Whi0 = 0;

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
        Whi3 = mc_ME->Whi3;
        Whi0 = mc_ME->Whi0;
        Inv_Mass_bb = mc_ME->Inv_Mass_bb;
        Inv_Mass_lept = mc_ME->Inv_Mass_lept;
	
	//NN  output here
	mlpZbbvsTT = MLP_zbbvstt->Value(0, Wgg, Wqq, Wtt, MeT);
	mlpZbbvsTTtight = MLP_zbbvstttight->Value(0, Wgg, Wqq, Wtt);
        mlpZbbvsTT_tight_Wmet = MLP_zbbvstt_tight_Wmet->Value(0, Wgg, Wqq, Wtt,MeT);
	if(jetmetnj > 2){mlpzbbvstt_multi_EE_tight = MLP_zbbvstt_multi_EE_tight->Value(0, Wgg, Wqq, Wtt,1);}
	if(jetmetnj < 3){mlpzbbvstt_multi_EE_tight = MLP_zbbvstt_multi_EE_tight->Value(0, Wgg, Wqq, Wtt,0);}

	mlphiggsvszbb = MLP_higgs_vs_zbb->Value(0, Wgg, Wqq, Whi0 , Whi3);
	mlphiggsvstt = MLP_higgs_vs_tt->Value(0, Whi0 , Whi3 , Wtt);
        mlphiggsvszz = MLP_higgs_vs_zz->Value(0, Whi0 , Whi3 , Wzz0 , Wzz3);   
        mlphiggsvsbkg = MLP_higgs_vs_bkg->Value(0, mlphiggsvszbb  , mlphiggsvszz , mlphiggsvstt);
        mlphiggsvsbkg_fulll = MLP_higgs_vs_bkg_fulll->Value(0, Wgg,Wqq,Wtt,Wzz0,Wzz3,Whi0,Whi3);


	if (InputFile.Contains("DATA")){
	      if( MLP_higgs_vs_zbb->Value(0, Wgg, Wqq, Whi0 , Whi3)>0.5){mlphiggsvszbb=-999.;}
	      if( MLP_higgs_vs_tt->Value(0, Whi0 , Whi3 , Wtt)>0.5){mlphiggsvstt=-999.;}
	      if( MLP_higgs_vs_zz->Value(0, Whi0 , Whi3 , Wzz0 , Wzz3)>0.5){mlphiggsvszz=-999.;}
	      if( MLP_higgs_vs_bkg->Value(0, MLP_higgs_vs_zbb->Value(0, Wgg, Wqq, Whi0 , Whi3), MLP_higgs_vs_zz->Value(0, Whi0 , Whi3 , Wzz0 , Wzz3) ,MLP_higgs_vs_tt->Value(0, Whi0 , Whi3 , Wtt) ) > 0.5 ){mlphiggsvsbkg=-999.;}
	}
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


//void SimpleTree(TString InputFile = "Mu_DATA") {
//   CreateParentTree(InputFile);

void SimpleTree() {
   CreateParentTree("MuA_DATA");
   CreateParentTree("ElA_DATA");
   CreateParentTree("MuB_DATA");
   CreateParentTree("ElB_DATA");
   CreateParentTree("Mu_MC");
   CreateParentTree("El_MC");
   CreateParentTree("TT_Mu_MC");
   CreateParentTree("TT_El_MC");
   CreateParentTree("ZZ_Mu_MC");
   CreateParentTree("ZZ_El_MC");
   CreateParentTree("ZH125_Mu_MC");
   CreateParentTree("ZH125_El_MC");

}

//mergeOneSample(InputFile = "Mu_DATA")
//mergeOneSample(InputFile = "Mu_MC")
//mergeOneSample(InputFile = "Ttbar_Mu_MC")
//mergeOneSample(InputFile = "ZZ_Mu_MC")


