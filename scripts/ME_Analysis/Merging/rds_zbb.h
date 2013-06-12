//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Tue Apr  9 23:01:21 2013 by ROOT version 5.32/00
// from TTree rds_zbb/rds_zbb
// found on file: /nfs/user/acaudron/RDS537/File_rds_zbb_DY_Mu_MC.root
//////////////////////////////////////////////////////////

#ifndef rds_zbb_h
#define rds_zbb_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class rds_zbb {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Double_t        eventSelectionrun;
   Double_t        eventSelectionevent;
   Double_t        eventSelectionls;
   Double_t        eventSelectiontriggerSelection;
   Double_t        eventSelectiontriggerBits;
   Double_t        eventSelectiontriggerDouble;
   Double_t        eventSelectiontriggerSingle;
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
   Double_t        eventSelectionZbM;
   Double_t        eventSelectionZbPt;
   Double_t        eventSelectionZbbM;
   Double_t        eventSelectionZbbPt;
   Double_t        eventSelectioncategory;
   Double_t        eventSelectionmu1pt;
   Double_t        eventSelectionmu2pt;
   Double_t        eventSelectionmu1eta;
   Double_t        eventSelectionmu2eta;
   Double_t        eventSelectionmu1etapm;
   Double_t        eventSelectionmu2etapm;
   Double_t        eventSelectiondrllMu;
   Double_t        eventSelectionel1pt;
   Double_t        eventSelectionel2pt;
   Double_t        eventSelectionel1eta;
   Double_t        eventSelectionel2eta;
   Double_t        eventSelectionel1etapm;
   Double_t        eventSelectionel2etapm;
   Double_t        eventSelectiondrllEle;
   Double_t        jetmetSSVHEdisc;
   Double_t        jetmetnVertHE;
   Double_t        jetmetSSVHPdisc;
   Double_t        jetmetnVertHP;
   Double_t        jetmetSVmass;
   Double_t        jetmetSVpT;
   Double_t        jetmetCSVdisc;
   Double_t        jetmetJPdisc;
   Double_t        jetmetSSVHEdiscDisc1;
   Double_t        jetmetSSVHPdiscDisc1;
   Double_t        jetmetCSVdiscDisc1;
   Double_t        jetmetJPdiscDisc1;
   Double_t        jetmetMET;
   Double_t        jetmetMETphi;
   Double_t        jetmetMETsignificance;
   Double_t        jetmetMETphiNNregression;
   Double_t        jetmetMETNNregression;
   Double_t        jetmetjetpt;
   Double_t        jetmetjetpt_totunc;
   Double_t        jetmetjetFlavor;
   Double_t        jetmetjeteta;
   Double_t        jetmetjetetapm;
   Double_t        jetmetjetphi;
   Double_t        jetmetjetoverlapmu;
   Double_t        jetmetjetoverlapele;
   Double_t        jetmetjetbeta;
   Double_t        jetmetjetbetaStar;
   Double_t        jetmetjet1pt;
   Double_t        jetmetjet1pt_totunc;
   Double_t        jetmetjet1Flavor;
   Double_t        jetmetjet1eta;
   Double_t        jetmetjet1etapm;
   Double_t        jetmetjet1phi;
   Double_t        jetmetjet1energy;
   Double_t        jetmetjet1mass;
   Double_t        jetmetjet1Chf;
   Double_t        jetmetjet1Nhf;
   Double_t        jetmetjet1Phf;
   Double_t        jetmetjet1Elf;
   Double_t        jetmetjet1Muf;
   Double_t        jetmetjet1Vtx3dL;
   Double_t        jetmetjet1Vtx3deL;
   Double_t        jetmetjet1VtxPt;
   Double_t        jetmetjet1PtD;
   Double_t        jetmetjet1SSVHEdisc;
   Double_t        jetmetjet1nVertHE;
   Double_t        jetmetjet1SSVHPdisc;
   Double_t        jetmetjet1nVertHP;
   Double_t        jetmetjet1SVmass;
   Double_t        jetmetjet1SVpT;
   Double_t        jetmetjet1CSVdisc;
   Double_t        jetmetjet1JPdisc;
   Double_t        jetmetjet1beta;
   Double_t        jetmetjet1betaStar;
   Double_t        jetmetjet2pt;
   Double_t        jetmetjet2pt_totunc;
   Double_t        jetmetjet2Flavor;
   Double_t        jetmetjet2eta;
   Double_t        jetmetjet2etapm;
   Double_t        jetmetjet2phi;
   Double_t        jetmetjet2energy;
   Double_t        jetmetjet2mass;
   Double_t        jetmetjet2Chf;
   Double_t        jetmetjet2Nhf;
   Double_t        jetmetjet2Phf;
   Double_t        jetmetjet2Elf;
   Double_t        jetmetjet2Muf;
   Double_t        jetmetjet2Vtx3dL;
   Double_t        jetmetjet2Vtx3deL;
   Double_t        jetmetjet2VtxPt;
   Double_t        jetmetjet2PtD;
   Double_t        jetmetjet2SSVHEdisc;
   Double_t        jetmetjet2nVertHE;
   Double_t        jetmetjet2SSVHPdisc;
   Double_t        jetmetjet2nVertHP;
   Double_t        jetmetjet2SVmass;
   Double_t        jetmetjet2SVpT;
   Double_t        jetmetjet2CSVdisc;
   Double_t        jetmetjet2JPdisc;
   Double_t        jetmetjet2beta;
   Double_t        jetmetjet2betaStar;
   Double_t        jetmetbjet1pt;
   Double_t        jetmetbjet1pt_totunc;
   Double_t        jetmetbjet1Flavor;
   Double_t        jetmetbjet1eta;
   Double_t        jetmetbjet1etapm;
   Double_t        jetmetbjet1phi;
   Double_t        jetmetbjet1energy;
   Double_t        jetmetbjet1mass;
   Double_t        jetmetbjet1Chf;
   Double_t        jetmetbjet1Nhf;
   Double_t        jetmetbjet1Phf;
   Double_t        jetmetbjet1Elf;
   Double_t        jetmetbjet1Muf;
   Double_t        jetmetbjet1Vtx3dL;
   Double_t        jetmetbjet1Vtx3deL;
   Double_t        jetmetbjet1VtxPt;
   Double_t        jetmetbjet1PtD;
   Double_t        jetmetbjet1SSVHEdisc;
   Double_t        jetmetbjet1nVertHE;
   Double_t        jetmetbjet1SSVHPdisc;
   Double_t        jetmetbjet1nVertHP;
   Double_t        jetmetbjet1SVmass;
   Double_t        jetmetbjet1SVpT;
   Double_t        jetmetbjet1CSVdisc;
   Double_t        jetmetbjet1JPdisc;
   Double_t        jetmetbjet1beta;
   Double_t        jetmetbjet1betaStar;
   Double_t        jetmetbjet2pt;
   Double_t        jetmetbjet2pt_totunc;
   Double_t        jetmetbjet2Flavor;
   Double_t        jetmetbjet2eta;
   Double_t        jetmetbjet2etapm;
   Double_t        jetmetbjet2phi;
   Double_t        jetmetbjet2energy;
   Double_t        jetmetbjet2mass;
   Double_t        jetmetbjet2Chf;
   Double_t        jetmetbjet2Nhf;
   Double_t        jetmetbjet2Phf;
   Double_t        jetmetbjet2Elf;
   Double_t        jetmetbjet2Muf;
   Double_t        jetmetbjet2Vtx3dL;
   Double_t        jetmetbjet2Vtx3deL;
   Double_t        jetmetbjet2VtxPt;
   Double_t        jetmetbjet2PtD;
   Double_t        jetmetbjet2SSVHEdisc;
   Double_t        jetmetbjet2nVertHE;
   Double_t        jetmetbjet2SSVHPdisc;
   Double_t        jetmetbjet2nVertHP;
   Double_t        jetmetbjet2SVmass;
   Double_t        jetmetbjet2SVpT;
   Double_t        jetmetbjet2CSVdisc;
   Double_t        jetmetbjet2JPdisc;
   Double_t        jetmetbjet2beta;
   Double_t        jetmetbjet2betaStar;
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
   Double_t        jetmetrho;
   Double_t        vertexAssociationnvertices;
   Double_t        vertexAssociationvx;
   Double_t        vertexAssociationvy;
   Double_t        vertexAssociationvz;
   Double_t        vertexAssociationvxerr;
   Double_t        vertexAssociationvyerr;
   Double_t        vertexAssociationvzerr;
   Double_t        vertexAssociationlepton_dz;
   Double_t        vertexAssociationl1v_dz;
   Double_t        vertexAssociationl2v_dz;
   Double_t        vertexAssociationlvertex;
   Double_t        mebjet1pt;
   Double_t        mebjet1ptNNCorr;
   Double_t        mebjet1etapm;
   Double_t        mebjet1phi;
   Double_t        mebjet1mass;
   Double_t        mebjet1massNNCorr;
   Double_t        mebjet2pt;
   Double_t        mebjet2ptNNCorr;
   Double_t        mebjet2etapm;
   Double_t        mebjet2phi;
   Double_t        mebjet2mass;
   Double_t        mebjet2massNNCorr;
   Double_t        memu1pt;
   Double_t        memu1etapm;
   Double_t        memu1phi;
   Double_t        memu1mass;
   Double_t        memu1charge;
   Double_t        memu2pt;
   Double_t        memu2etapm;
   Double_t        memu2phi;
   Double_t        memu2mass;
   Double_t        memu2charge;
   Double_t        meel1pt;
   Double_t        meel1etapm;
   Double_t        meel1phi;
   Double_t        meel1mass;
   Double_t        meel1charge;
   Double_t        meel2pt;
   Double_t        meel2etapm;
   Double_t        meel2phi;
   Double_t        meel2mass;
   Double_t        meel2charge;
   Double_t        meMET;
   Double_t        meMETphi;
   Double_t        mebbM;
   Double_t        mebbNNCorrM;
   Double_t        meFilledJetTF;
   Double_t        meFilledLepTF;
   Double_t        meE_b;
   Double_t        meE_jb;
   Double_t        meDeltaE_jet;
   Double_t        meE_ab;
   Double_t        meE_jab;
   Double_t        meDeltaE_ajet;
   Double_t        meNNCorrE_jb;
   Double_t        meDeltaNNCorrE_jet;
   Double_t        meNNCorrE_jab;
   Double_t        meDeltaNNCorrE_ajet;
   Double_t        mephi_b;
   Double_t        mephi_ab;
   Double_t        mephi_jb;
   Double_t        mephi_jab;
   Double_t        meDeltaphi_jet;
   Double_t        meDeltaphi_ajet;
   Double_t        meEta_b;
   Double_t        meEta_ab;
   Double_t        meEta_jb;
   Double_t        meEta_jab;
   Double_t        meDeltaEta_jet;
   Double_t        meDeltaEta_ajet;
   Double_t        meE_lgm;
   Double_t        meE_lrm;
   Double_t        meDeltaE_lm;
   Double_t        meE_lgp;
   Double_t        meE_lrp;
   Double_t        meDeltaE_lp;
   Double_t        mephi_lgm;
   Double_t        mephi_lgp;
   Double_t        mephi_lrm;
   Double_t        mephi_lrp;
   Double_t        meDeltaphi_lm;
   Double_t        meDeltaphi_lp;
   Double_t        meEta_lgm;
   Double_t        meEta_lgp;
   Double_t        meEta_lrm;
   Double_t        meEta_lrp;
   Double_t        meDeltaEta_lm;
   Double_t        meDeltaEta_lp;
   Double_t        mePtInv_lgp;
   Double_t        mePtInv_lgm;
   Double_t        mePtInv_lrp;
   Double_t        mePtInv_lrm;
   Double_t        meDeltaPtInv_lp;
   Double_t        meDeltaPtInv_lm;
   Double_t        BtaggingReweightingHE;
   Double_t        BtaggingReweightingHP;
   Double_t        BtaggingReweightingHEexcl;
   Double_t        BtaggingReweightingHPexcl;
   Double_t        BtaggingReweightingHEHE;
   Double_t        BtaggingReweightingHEHP;
   Double_t        BtaggingReweightingHPHP;
   Double_t        LeptonsReweightingweight;
   Double_t        mcSelectioneventType;
   Double_t        mcSelectionLepPosPx;
   Double_t        mcSelectionLepPosPy;
   Double_t        mcSelectionLepPosPz;
   Double_t        mcSelectionLepPosEn;
   Double_t        mcSelectionLepNegPx;
   Double_t        mcSelectionLepNegPy;
   Double_t        mcSelectionLepNegPz;
   Double_t        mcSelectionLepNegEn;
   Double_t        mcSelectionBottomPx;
   Double_t        mcSelectionBottomPy;
   Double_t        mcSelectionBottomPz;
   Double_t        mcSelectionBottomEn;
   Double_t        mcSelectionAntibottomPx;
   Double_t        mcSelectionAntibottomPy;
   Double_t        mcSelectionAntibottomPz;
   Double_t        mcSelectionAntibottomEn;
   Double_t        mcSelectionFlavLepPos;
   Double_t        mcSelectionFlavLepNeg;
   Double_t        mcSelectionNLepPos;
   Double_t        mcSelectionNLepNeg;
   Double_t        mcSelectionNBottom;
   Double_t        mcSelectionNAntibottom;
   Double_t        lumiReweightingLumiWeight;
   Double_t        lumiReweightingpu;
   Double_t        lumiReweightingpv;
   Int_t           rc_eventSelection_0_idx;
   Char_t          rc_eventSelection_0_lbl;
   Int_t           rc_eventSelection_1_idx;
   Char_t          rc_eventSelection_1_lbl;
   Int_t           rc_eventSelection_2_idx;
   Char_t          rc_eventSelection_2_lbl;
   Int_t           rc_eventSelection_3_idx;
   Char_t          rc_eventSelection_3_lbl;
   Int_t           rc_eventSelection_4_idx;
   Char_t          rc_eventSelection_4_lbl;
   Int_t           rc_eventSelection_5_idx;
   Char_t          rc_eventSelection_5_lbl;
   Int_t           rc_eventSelection_6_idx;
   Char_t          rc_eventSelection_6_lbl;
   Int_t           rc_eventSelection_7_idx;
   Char_t          rc_eventSelection_7_lbl;
   Int_t           rc_eventSelection_8_idx;
   Char_t          rc_eventSelection_8_lbl;
   Int_t           rc_eventSelection_9_idx;
   Char_t          rc_eventSelection_9_lbl;
   Int_t           rc_eventSelection_10_idx;
   Char_t          rc_eventSelection_10_lbl;
   Int_t           rc_eventSelection_11_idx;
   Char_t          rc_eventSelection_11_lbl;
   Int_t           rc_eventSelection_12_idx;
   Char_t          rc_eventSelection_12_lbl;
   Int_t           rc_eventSelection_13_idx;
   Char_t          rc_eventSelection_13_lbl;
   Int_t           rc_eventSelection_14_idx;
   Char_t          rc_eventSelection_14_lbl;
   Int_t           rc_eventSelection_15_idx;
   Char_t          rc_eventSelection_15_lbl;
   Int_t           rc_eventSelection_16_idx;
   Char_t          rc_eventSelection_16_lbl;
   Int_t           rc_eventSelection_17_idx;
   Char_t          rc_eventSelection_17_lbl;
   Int_t           rc_eventSelection_18_idx;
   Char_t          rc_eventSelection_18_lbl;

   // List of branches
   TBranch        *b_eventSelectionrun;   //!
   TBranch        *b_eventSelectionevent;   //!
   TBranch        *b_eventSelectionls;   //!
   TBranch        *b_eventSelectiontriggerSelection;   //!
   TBranch        *b_eventSelectiontriggerBits;   //!
   TBranch        *b_eventSelectiontriggerDouble;   //!
   TBranch        *b_eventSelectiontriggerSingle;   //!
   TBranch        *b_eventSelectionzmassMu;   //!
   TBranch        *b_eventSelectionbestzmassMu;   //!
   TBranch        *b_eventSelectionzmassEle;   //!
   TBranch        *b_eventSelectionbestzmassEle;   //!
   TBranch        *b_eventSelectionzptMu;   //!
   TBranch        *b_eventSelectionbestzptMu;   //!
   TBranch        *b_eventSelectionzptEle;   //!
   TBranch        *b_eventSelectionbestzptEle;   //!
   TBranch        *b_eventSelectionscaldptZbj1;   //!
   TBranch        *b_eventSelectiondrZbj1;   //!
   TBranch        *b_eventSelectiondphiZbj1;   //!
   TBranch        *b_eventSelectionscaldptZbb;   //!
   TBranch        *b_eventSelectiondphiZbb;   //!
   TBranch        *b_eventSelectiondrZbb;   //!
   TBranch        *b_eventSelectiondijetM;   //!
   TBranch        *b_eventSelectiondijetPt;   //!
   TBranch        *b_eventSelectiondijetdR;   //!
   TBranch        *b_eventSelectiondijetSVdR;   //!
   TBranch        *b_eventSelectiondphidijetMET;   //!
   TBranch        *b_eventSelectionZbM;   //!
   TBranch        *b_eventSelectionZbPt;   //!
   TBranch        *b_eventSelectionZbbM;   //!
   TBranch        *b_eventSelectionZbbPt;   //!
   TBranch        *b_eventSelectioncategory;   //!
   TBranch        *b_eventSelectionmu1pt;   //!
   TBranch        *b_eventSelectionmu2pt;   //!
   TBranch        *b_eventSelectionmu1eta;   //!
   TBranch        *b_eventSelectionmu2eta;   //!
   TBranch        *b_eventSelectionmu1etapm;   //!
   TBranch        *b_eventSelectionmu2etapm;   //!
   TBranch        *b_eventSelectiondrllMu;   //!
   TBranch        *b_eventSelectionel1pt;   //!
   TBranch        *b_eventSelectionel2pt;   //!
   TBranch        *b_eventSelectionel1eta;   //!
   TBranch        *b_eventSelectionel2eta;   //!
   TBranch        *b_eventSelectionel1etapm;   //!
   TBranch        *b_eventSelectionel2etapm;   //!
   TBranch        *b_eventSelectiondrllEle;   //!
   TBranch        *b_jetmetSSVHEdisc;   //!
   TBranch        *b_jetmetnVertHE;   //!
   TBranch        *b_jetmetSSVHPdisc;   //!
   TBranch        *b_jetmetnVertHP;   //!
   TBranch        *b_jetmetSVmass;   //!
   TBranch        *b_jetmetSVpT;   //!
   TBranch        *b_jetmetCSVdisc;   //!
   TBranch        *b_jetmetJPdisc;   //!
   TBranch        *b_jetmetSSVHEdiscDisc1;   //!
   TBranch        *b_jetmetSSVHPdiscDisc1;   //!
   TBranch        *b_jetmetCSVdiscDisc1;   //!
   TBranch        *b_jetmetJPdiscDisc1;   //!
   TBranch        *b_jetmetMET;   //!
   TBranch        *b_jetmetMETphi;   //!
   TBranch        *b_jetmetMETsignificance;   //!
   TBranch        *b_jetmetMETphiNNregression;   //!
   TBranch        *b_jetmetMETNNregression;   //!
   TBranch        *b_jetmetjetpt;   //!
   TBranch        *b_jetmetjetpt_totunc;   //!
   TBranch        *b_jetmetjetFlavor;   //!
   TBranch        *b_jetmetjeteta;   //!
   TBranch        *b_jetmetjetetapm;   //!
   TBranch        *b_jetmetjetphi;   //!
   TBranch        *b_jetmetjetoverlapmu;   //!
   TBranch        *b_jetmetjetoverlapele;   //!
   TBranch        *b_jetmetjetbeta;   //!
   TBranch        *b_jetmetjetbetaStar;   //!
   TBranch        *b_jetmetjet1pt;   //!
   TBranch        *b_jetmetjet1pt_totunc;   //!
   TBranch        *b_jetmetjet1Flavor;   //!
   TBranch        *b_jetmetjet1eta;   //!
   TBranch        *b_jetmetjet1etapm;   //!
   TBranch        *b_jetmetjet1phi;   //!
   TBranch        *b_jetmetjet1energy;   //!
   TBranch        *b_jetmetjet1mass;   //!
   TBranch        *b_jetmetjet1Chf;   //!
   TBranch        *b_jetmetjet1Nhf;   //!
   TBranch        *b_jetmetjet1Phf;   //!
   TBranch        *b_jetmetjet1Elf;   //!
   TBranch        *b_jetmetjet1Muf;   //!
   TBranch        *b_jetmetjet1Vtx3dL;   //!
   TBranch        *b_jetmetjet1Vtx3deL;   //!
   TBranch        *b_jetmetjet1VtxPt;   //!
   TBranch        *b_jetmetjet1PtD;   //!
   TBranch        *b_jetmetjet1SSVHEdisc;   //!
   TBranch        *b_jetmetjet1nVertHE;   //!
   TBranch        *b_jetmetjet1SSVHPdisc;   //!
   TBranch        *b_jetmetjet1nVertHP;   //!
   TBranch        *b_jetmetjet1SVmass;   //!
   TBranch        *b_jetmetjet1SVpT;   //!
   TBranch        *b_jetmetjet1CSVdisc;   //!
   TBranch        *b_jetmetjet1JPdisc;   //!
   TBranch        *b_jetmetjet1beta;   //!
   TBranch        *b_jetmetjet1betaStar;   //!
   TBranch        *b_jetmetjet2pt;   //!
   TBranch        *b_jetmetjet2pt_totunc;   //!
   TBranch        *b_jetmetjet2Flavor;   //!
   TBranch        *b_jetmetjet2eta;   //!
   TBranch        *b_jetmetjet2etapm;   //!
   TBranch        *b_jetmetjet2phi;   //!
   TBranch        *b_jetmetjet2energy;   //!
   TBranch        *b_jetmetjet2mass;   //!
   TBranch        *b_jetmetjet2Chf;   //!
   TBranch        *b_jetmetjet2Nhf;   //!
   TBranch        *b_jetmetjet2Phf;   //!
   TBranch        *b_jetmetjet2Elf;   //!
   TBranch        *b_jetmetjet2Muf;   //!
   TBranch        *b_jetmetjet2Vtx3dL;   //!
   TBranch        *b_jetmetjet2Vtx3deL;   //!
   TBranch        *b_jetmetjet2VtxPt;   //!
   TBranch        *b_jetmetjet2PtD;   //!
   TBranch        *b_jetmetjet2SSVHEdisc;   //!
   TBranch        *b_jetmetjet2nVertHE;   //!
   TBranch        *b_jetmetjet2SSVHPdisc;   //!
   TBranch        *b_jetmetjet2nVertHP;   //!
   TBranch        *b_jetmetjet2SVmass;   //!
   TBranch        *b_jetmetjet2SVpT;   //!
   TBranch        *b_jetmetjet2CSVdisc;   //!
   TBranch        *b_jetmetjet2JPdisc;   //!
   TBranch        *b_jetmetjet2beta;   //!
   TBranch        *b_jetmetjet2betaStar;   //!
   TBranch        *b_jetmetbjet1pt;   //!
   TBranch        *b_jetmetbjet1pt_totunc;   //!
   TBranch        *b_jetmetbjet1Flavor;   //!
   TBranch        *b_jetmetbjet1eta;   //!
   TBranch        *b_jetmetbjet1etapm;   //!
   TBranch        *b_jetmetbjet1phi;   //!
   TBranch        *b_jetmetbjet1energy;   //!
   TBranch        *b_jetmetbjet1mass;   //!
   TBranch        *b_jetmetbjet1Chf;   //!
   TBranch        *b_jetmetbjet1Nhf;   //!
   TBranch        *b_jetmetbjet1Phf;   //!
   TBranch        *b_jetmetbjet1Elf;   //!
   TBranch        *b_jetmetbjet1Muf;   //!
   TBranch        *b_jetmetbjet1Vtx3dL;   //!
   TBranch        *b_jetmetbjet1Vtx3deL;   //!
   TBranch        *b_jetmetbjet1VtxPt;   //!
   TBranch        *b_jetmetbjet1PtD;   //!
   TBranch        *b_jetmetbjet1SSVHEdisc;   //!
   TBranch        *b_jetmetbjet1nVertHE;   //!
   TBranch        *b_jetmetbjet1SSVHPdisc;   //!
   TBranch        *b_jetmetbjet1nVertHP;   //!
   TBranch        *b_jetmetbjet1SVmass;   //!
   TBranch        *b_jetmetbjet1SVpT;   //!
   TBranch        *b_jetmetbjet1CSVdisc;   //!
   TBranch        *b_jetmetbjet1JPdisc;   //!
   TBranch        *b_jetmetbjet1beta;   //!
   TBranch        *b_jetmetbjet1betaStar;   //!
   TBranch        *b_jetmetbjet2pt;   //!
   TBranch        *b_jetmetbjet2pt_totunc;   //!
   TBranch        *b_jetmetbjet2Flavor;   //!
   TBranch        *b_jetmetbjet2eta;   //!
   TBranch        *b_jetmetbjet2etapm;   //!
   TBranch        *b_jetmetbjet2phi;   //!
   TBranch        *b_jetmetbjet2energy;   //!
   TBranch        *b_jetmetbjet2mass;   //!
   TBranch        *b_jetmetbjet2Chf;   //!
   TBranch        *b_jetmetbjet2Nhf;   //!
   TBranch        *b_jetmetbjet2Phf;   //!
   TBranch        *b_jetmetbjet2Elf;   //!
   TBranch        *b_jetmetbjet2Muf;   //!
   TBranch        *b_jetmetbjet2Vtx3dL;   //!
   TBranch        *b_jetmetbjet2Vtx3deL;   //!
   TBranch        *b_jetmetbjet2VtxPt;   //!
   TBranch        *b_jetmetbjet2PtD;   //!
   TBranch        *b_jetmetbjet2SSVHEdisc;   //!
   TBranch        *b_jetmetbjet2nVertHE;   //!
   TBranch        *b_jetmetbjet2SSVHPdisc;   //!
   TBranch        *b_jetmetbjet2nVertHP;   //!
   TBranch        *b_jetmetbjet2SVmass;   //!
   TBranch        *b_jetmetbjet2SVpT;   //!
   TBranch        *b_jetmetbjet2CSVdisc;   //!
   TBranch        *b_jetmetbjet2JPdisc;   //!
   TBranch        *b_jetmetbjet2beta;   //!
   TBranch        *b_jetmetbjet2betaStar;   //!
   TBranch        *b_jetmetdptj1b1;   //!
   TBranch        *b_jetmetnj;   //!
   TBranch        *b_jetmetnb;   //!
   TBranch        *b_jetmetnbP;   //!
   TBranch        *b_jetmetnhf;   //!
   TBranch        *b_jetmetnef;   //!
   TBranch        *b_jetmetnpf;   //!
   TBranch        *b_jetmetchf;   //!
   TBranch        *b_jetmetnch;   //!
   TBranch        *b_jetmetcef;   //!
   TBranch        *b_jetmetjetid;   //!
   TBranch        *b_jetmetrho;   //!
   TBranch        *b_vertexAssociationnvertices;   //!
   TBranch        *b_vertexAssociationvx;   //!
   TBranch        *b_vertexAssociationvy;   //!
   TBranch        *b_vertexAssociationvz;   //!
   TBranch        *b_vertexAssociationvxerr;   //!
   TBranch        *b_vertexAssociationvyerr;   //!
   TBranch        *b_vertexAssociationvzerr;   //!
   TBranch        *b_vertexAssociationlepton_dz;   //!
   TBranch        *b_vertexAssociationl1v_dz;   //!
   TBranch        *b_vertexAssociationl2v_dz;   //!
   TBranch        *b_vertexAssociationlvertex;   //!
   TBranch        *b_mebjet1pt;   //!
   TBranch        *b_mebjet1ptNNCorr;   //!
   TBranch        *b_mebjet1etapm;   //!
   TBranch        *b_mebjet1phi;   //!
   TBranch        *b_mebjet1mass;   //!
   TBranch        *b_mebjet1massNNCorr;   //!
   TBranch        *b_mebjet2pt;   //!
   TBranch        *b_mebjet2ptNNCorr;   //!
   TBranch        *b_mebjet2etapm;   //!
   TBranch        *b_mebjet2phi;   //!
   TBranch        *b_mebjet2mass;   //!
   TBranch        *b_mebjet2massNNCorr;   //!
   TBranch        *b_memu1pt;   //!
   TBranch        *b_memu1etapm;   //!
   TBranch        *b_memu1phi;   //!
   TBranch        *b_memu1mass;   //!
   TBranch        *b_memu1charge;   //!
   TBranch        *b_memu2pt;   //!
   TBranch        *b_memu2etapm;   //!
   TBranch        *b_memu2phi;   //!
   TBranch        *b_memu2mass;   //!
   TBranch        *b_memu2charge;   //!
   TBranch        *b_meel1pt;   //!
   TBranch        *b_meel1etapm;   //!
   TBranch        *b_meel1phi;   //!
   TBranch        *b_meel1mass;   //!
   TBranch        *b_meel1charge;   //!
   TBranch        *b_meel2pt;   //!
   TBranch        *b_meel2etapm;   //!
   TBranch        *b_meel2phi;   //!
   TBranch        *b_meel2mass;   //!
   TBranch        *b_meel2charge;   //!
   TBranch        *b_meMET;   //!
   TBranch        *b_meMETphi;   //!
   TBranch        *b_mebbM;   //!
   TBranch        *b_mebbNNCorrM;   //!
   TBranch        *b_meFilledJetTF;   //!
   TBranch        *b_meFilledLepTF;   //!
   TBranch        *b_meE_b;   //!
   TBranch        *b_meE_jb;   //!
   TBranch        *b_meDeltaE_jet;   //!
   TBranch        *b_meE_ab;   //!
   TBranch        *b_meE_jab;   //!
   TBranch        *b_meDeltaE_ajet;   //!
   TBranch        *b_meNNCorrE_jb;   //!
   TBranch        *b_meDeltaNNCorrE_jet;   //!
   TBranch        *b_meNNCorrE_jab;   //!
   TBranch        *b_meDeltaNNCorrE_ajet;   //!
   TBranch        *b_mephi_b;   //!
   TBranch        *b_mephi_ab;   //!
   TBranch        *b_mephi_jb;   //!
   TBranch        *b_mephi_jab;   //!
   TBranch        *b_meDeltaphi_jet;   //!
   TBranch        *b_meDeltaphi_ajet;   //!
   TBranch        *b_meEta_b;   //!
   TBranch        *b_meEta_ab;   //!
   TBranch        *b_meEta_jb;   //!
   TBranch        *b_meEta_jab;   //!
   TBranch        *b_meDeltaEta_jet;   //!
   TBranch        *b_meDeltaEta_ajet;   //!
   TBranch        *b_meE_lgm;   //!
   TBranch        *b_meE_lrm;   //!
   TBranch        *b_meDeltaE_lm;   //!
   TBranch        *b_meE_lgp;   //!
   TBranch        *b_meE_lrp;   //!
   TBranch        *b_meDeltaE_lp;   //!
   TBranch        *b_mephi_lgm;   //!
   TBranch        *b_mephi_lgp;   //!
   TBranch        *b_mephi_lrm;   //!
   TBranch        *b_mephi_lrp;   //!
   TBranch        *b_meDeltaphi_lm;   //!
   TBranch        *b_meDeltaphi_lp;   //!
   TBranch        *b_meEta_lgm;   //!
   TBranch        *b_meEta_lgp;   //!
   TBranch        *b_meEta_lrm;   //!
   TBranch        *b_meEta_lrp;   //!
   TBranch        *b_meDeltaEta_lm;   //!
   TBranch        *b_meDeltaEta_lp;   //!
   TBranch        *b_mePtInv_lgp;   //!
   TBranch        *b_mePtInv_lgm;   //!
   TBranch        *b_mePtInv_lrp;   //!
   TBranch        *b_mePtInv_lrm;   //!
   TBranch        *b_meDeltaPtInv_lp;   //!
   TBranch        *b_meDeltaPtInv_lm;   //!
   TBranch        *b_BtaggingReweightingHE;   //!
   TBranch        *b_BtaggingReweightingHP;   //!
   TBranch        *b_BtaggingReweightingHEexcl;   //!
   TBranch        *b_BtaggingReweightingHPexcl;   //!
   TBranch        *b_BtaggingReweightingHEHE;   //!
   TBranch        *b_BtaggingReweightingHEHP;   //!
   TBranch        *b_BtaggingReweightingHPHP;   //!
   TBranch        *b_LeptonsReweightingweight;   //!
   TBranch        *b_mcSelectioneventType;   //!
   TBranch        *b_mcSelectionLepPosPx;   //!
   TBranch        *b_mcSelectionLepPosPy;   //!
   TBranch        *b_mcSelectionLepPosPz;   //!
   TBranch        *b_mcSelectionLepPosEn;   //!
   TBranch        *b_mcSelectionLepNegPx;   //!
   TBranch        *b_mcSelectionLepNegPy;   //!
   TBranch        *b_mcSelectionLepNegPz;   //!
   TBranch        *b_mcSelectionLepNegEn;   //!
   TBranch        *b_mcSelectionBottomPx;   //!
   TBranch        *b_mcSelectionBottomPy;   //!
   TBranch        *b_mcSelectionBottomPz;   //!
   TBranch        *b_mcSelectionBottomEn;   //!
   TBranch        *b_mcSelectionAntibottomPx;   //!
   TBranch        *b_mcSelectionAntibottomPy;   //!
   TBranch        *b_mcSelectionAntibottomPz;   //!
   TBranch        *b_mcSelectionAntibottomEn;   //!
   TBranch        *b_mcSelectionFlavLepPos;   //!
   TBranch        *b_mcSelectionFlavLepNeg;   //!
   TBranch        *b_mcSelectionNLepPos;   //!
   TBranch        *b_mcSelectionNLepNeg;   //!
   TBranch        *b_mcSelectionNBottom;   //!
   TBranch        *b_mcSelectionNAntibottom;   //!
   TBranch        *b_lumiReweightingLumiWeight;   //!
   TBranch        *b_lumiReweightingpu;   //!
   TBranch        *b_lumiReweightingpv;   //!
   TBranch        *b_rc_eventSelection_0_idx;   //!
   TBranch        *b_rc_eventSelection_0_lbl;   //!
   TBranch        *b_rc_eventSelection_1_idx;   //!
   TBranch        *b_rc_eventSelection_1_lbl;   //!
   TBranch        *b_rc_eventSelection_2_idx;   //!
   TBranch        *b_rc_eventSelection_2_lbl;   //!
   TBranch        *b_rc_eventSelection_3_idx;   //!
   TBranch        *b_rc_eventSelection_3_lbl;   //!
   TBranch        *b_rc_eventSelection_4_idx;   //!
   TBranch        *b_rc_eventSelection_4_lbl;   //!
   TBranch        *b_rc_eventSelection_5_idx;   //!
   TBranch        *b_rc_eventSelection_5_lbl;   //!
   TBranch        *b_rc_eventSelection_6_idx;   //!
   TBranch        *b_rc_eventSelection_6_lbl;   //!
   TBranch        *b_rc_eventSelection_7_idx;   //!
   TBranch        *b_rc_eventSelection_7_lbl;   //!
   TBranch        *b_rc_eventSelection_8_idx;   //!
   TBranch        *b_rc_eventSelection_8_lbl;   //!
   TBranch        *b_rc_eventSelection_9_idx;   //!
   TBranch        *b_rc_eventSelection_9_lbl;   //!
   TBranch        *b_rc_eventSelection_10_idx;   //!
   TBranch        *b_rc_eventSelection_10_lbl;   //!
   TBranch        *b_rc_eventSelection_11_idx;   //!
   TBranch        *b_rc_eventSelection_11_lbl;   //!
   TBranch        *b_rc_eventSelection_12_idx;   //!
   TBranch        *b_rc_eventSelection_12_lbl;   //!
   TBranch        *b_rc_eventSelection_13_idx;   //!
   TBranch        *b_rc_eventSelection_13_lbl;   //!
   TBranch        *b_rc_eventSelection_14_idx;   //!
   TBranch        *b_rc_eventSelection_14_lbl;   //!
   TBranch        *b_rc_eventSelection_15_idx;   //!
   TBranch        *b_rc_eventSelection_15_lbl;   //!
   TBranch        *b_rc_eventSelection_16_idx;   //!
   TBranch        *b_rc_eventSelection_16_lbl;   //!
   TBranch        *b_rc_eventSelection_17_idx;   //!
   TBranch        *b_rc_eventSelection_17_lbl;   //!
   TBranch        *b_rc_eventSelection_18_idx;   //!
   TBranch        *b_rc_eventSelection_18_lbl;   //!

   rds_zbb(TTree *tree=0);
   virtual ~rds_zbb();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef rds_zbb_cxx
rds_zbb::rds_zbb(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/nfs/user/acaudron/RDS537/File_rds_zbb_DY_Mu_MC.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/nfs/user/acaudron/RDS537/File_rds_zbb_DY_Mu_MC.root");
      }
      f->GetObject("rds_zbb",tree);

   }
   Init(tree);
}

rds_zbb::~rds_zbb()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t rds_zbb::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t rds_zbb::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void rds_zbb::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("eventSelectionrun", &eventSelectionrun, &b_eventSelectionrun);
   fChain->SetBranchAddress("eventSelectionevent", &eventSelectionevent, &b_eventSelectionevent);
   fChain->SetBranchAddress("eventSelectionls", &eventSelectionls, &b_eventSelectionls);
   fChain->SetBranchAddress("eventSelectiontriggerSelection", &eventSelectiontriggerSelection, &b_eventSelectiontriggerSelection);
   fChain->SetBranchAddress("eventSelectiontriggerBits", &eventSelectiontriggerBits, &b_eventSelectiontriggerBits);
   fChain->SetBranchAddress("eventSelectiontriggerDouble", &eventSelectiontriggerDouble, &b_eventSelectiontriggerDouble);
   fChain->SetBranchAddress("eventSelectiontriggerSingle", &eventSelectiontriggerSingle, &b_eventSelectiontriggerSingle);
   fChain->SetBranchAddress("eventSelectionzmassMu", &eventSelectionzmassMu, &b_eventSelectionzmassMu);
   fChain->SetBranchAddress("eventSelectionbestzmassMu", &eventSelectionbestzmassMu, &b_eventSelectionbestzmassMu);
   fChain->SetBranchAddress("eventSelectionzmassEle", &eventSelectionzmassEle, &b_eventSelectionzmassEle);
   fChain->SetBranchAddress("eventSelectionbestzmassEle", &eventSelectionbestzmassEle, &b_eventSelectionbestzmassEle);
   fChain->SetBranchAddress("eventSelectionzptMu", &eventSelectionzptMu, &b_eventSelectionzptMu);
   fChain->SetBranchAddress("eventSelectionbestzptMu", &eventSelectionbestzptMu, &b_eventSelectionbestzptMu);
   fChain->SetBranchAddress("eventSelectionzptEle", &eventSelectionzptEle, &b_eventSelectionzptEle);
   fChain->SetBranchAddress("eventSelectionbestzptEle", &eventSelectionbestzptEle, &b_eventSelectionbestzptEle);
   fChain->SetBranchAddress("eventSelectionscaldptZbj1", &eventSelectionscaldptZbj1, &b_eventSelectionscaldptZbj1);
   fChain->SetBranchAddress("eventSelectiondrZbj1", &eventSelectiondrZbj1, &b_eventSelectiondrZbj1);
   fChain->SetBranchAddress("eventSelectiondphiZbj1", &eventSelectiondphiZbj1, &b_eventSelectiondphiZbj1);
   fChain->SetBranchAddress("eventSelectionscaldptZbb", &eventSelectionscaldptZbb, &b_eventSelectionscaldptZbb);
   fChain->SetBranchAddress("eventSelectiondphiZbb", &eventSelectiondphiZbb, &b_eventSelectiondphiZbb);
   fChain->SetBranchAddress("eventSelectiondrZbb", &eventSelectiondrZbb, &b_eventSelectiondrZbb);
   fChain->SetBranchAddress("eventSelectiondijetM", &eventSelectiondijetM, &b_eventSelectiondijetM);
   fChain->SetBranchAddress("eventSelectiondijetPt", &eventSelectiondijetPt, &b_eventSelectiondijetPt);
   fChain->SetBranchAddress("eventSelectiondijetdR", &eventSelectiondijetdR, &b_eventSelectiondijetdR);
   fChain->SetBranchAddress("eventSelectiondijetSVdR", &eventSelectiondijetSVdR, &b_eventSelectiondijetSVdR);
   fChain->SetBranchAddress("eventSelectiondphidijetMET", &eventSelectiondphidijetMET, &b_eventSelectiondphidijetMET);
   fChain->SetBranchAddress("eventSelectionZbM", &eventSelectionZbM, &b_eventSelectionZbM);
   fChain->SetBranchAddress("eventSelectionZbPt", &eventSelectionZbPt, &b_eventSelectionZbPt);
   fChain->SetBranchAddress("eventSelectionZbbM", &eventSelectionZbbM, &b_eventSelectionZbbM);
   fChain->SetBranchAddress("eventSelectionZbbPt", &eventSelectionZbbPt, &b_eventSelectionZbbPt);
   fChain->SetBranchAddress("eventSelectioncategory", &eventSelectioncategory, &b_eventSelectioncategory);
   fChain->SetBranchAddress("eventSelectionmu1pt", &eventSelectionmu1pt, &b_eventSelectionmu1pt);
   fChain->SetBranchAddress("eventSelectionmu2pt", &eventSelectionmu2pt, &b_eventSelectionmu2pt);
   fChain->SetBranchAddress("eventSelectionmu1eta", &eventSelectionmu1eta, &b_eventSelectionmu1eta);
   fChain->SetBranchAddress("eventSelectionmu2eta", &eventSelectionmu2eta, &b_eventSelectionmu2eta);
   fChain->SetBranchAddress("eventSelectionmu1etapm", &eventSelectionmu1etapm, &b_eventSelectionmu1etapm);
   fChain->SetBranchAddress("eventSelectionmu2etapm", &eventSelectionmu2etapm, &b_eventSelectionmu2etapm);
   fChain->SetBranchAddress("eventSelectiondrllMu", &eventSelectiondrllMu, &b_eventSelectiondrllMu);
   fChain->SetBranchAddress("eventSelectionel1pt", &eventSelectionel1pt, &b_eventSelectionel1pt);
   fChain->SetBranchAddress("eventSelectionel2pt", &eventSelectionel2pt, &b_eventSelectionel2pt);
   fChain->SetBranchAddress("eventSelectionel1eta", &eventSelectionel1eta, &b_eventSelectionel1eta);
   fChain->SetBranchAddress("eventSelectionel2eta", &eventSelectionel2eta, &b_eventSelectionel2eta);
   fChain->SetBranchAddress("eventSelectionel1etapm", &eventSelectionel1etapm, &b_eventSelectionel1etapm);
   fChain->SetBranchAddress("eventSelectionel2etapm", &eventSelectionel2etapm, &b_eventSelectionel2etapm);
   fChain->SetBranchAddress("eventSelectiondrllEle", &eventSelectiondrllEle, &b_eventSelectiondrllEle);
   fChain->SetBranchAddress("jetmetSSVHEdisc", &jetmetSSVHEdisc, &b_jetmetSSVHEdisc);
   fChain->SetBranchAddress("jetmetnVertHE", &jetmetnVertHE, &b_jetmetnVertHE);
   fChain->SetBranchAddress("jetmetSSVHPdisc", &jetmetSSVHPdisc, &b_jetmetSSVHPdisc);
   fChain->SetBranchAddress("jetmetnVertHP", &jetmetnVertHP, &b_jetmetnVertHP);
   fChain->SetBranchAddress("jetmetSVmass", &jetmetSVmass, &b_jetmetSVmass);
   fChain->SetBranchAddress("jetmetSVpT", &jetmetSVpT, &b_jetmetSVpT);
   fChain->SetBranchAddress("jetmetCSVdisc", &jetmetCSVdisc, &b_jetmetCSVdisc);
   fChain->SetBranchAddress("jetmetJPdisc", &jetmetJPdisc, &b_jetmetJPdisc);
   fChain->SetBranchAddress("jetmetSSVHEdiscDisc1", &jetmetSSVHEdiscDisc1, &b_jetmetSSVHEdiscDisc1);
   fChain->SetBranchAddress("jetmetSSVHPdiscDisc1", &jetmetSSVHPdiscDisc1, &b_jetmetSSVHPdiscDisc1);
   fChain->SetBranchAddress("jetmetCSVdiscDisc1", &jetmetCSVdiscDisc1, &b_jetmetCSVdiscDisc1);
   fChain->SetBranchAddress("jetmetJPdiscDisc1", &jetmetJPdiscDisc1, &b_jetmetJPdiscDisc1);
   fChain->SetBranchAddress("jetmetMET", &jetmetMET, &b_jetmetMET);
   fChain->SetBranchAddress("jetmetMETphi", &jetmetMETphi, &b_jetmetMETphi);
   fChain->SetBranchAddress("jetmetMETsignificance", &jetmetMETsignificance, &b_jetmetMETsignificance);
   fChain->SetBranchAddress("jetmetMETphiNNregression", &jetmetMETphiNNregression, &b_jetmetMETphiNNregression);
   fChain->SetBranchAddress("jetmetMETNNregression", &jetmetMETNNregression, &b_jetmetMETNNregression);
   fChain->SetBranchAddress("jetmetjetpt", &jetmetjetpt, &b_jetmetjetpt);
   fChain->SetBranchAddress("jetmetjetpt_totunc", &jetmetjetpt_totunc, &b_jetmetjetpt_totunc);
   fChain->SetBranchAddress("jetmetjetFlavor", &jetmetjetFlavor, &b_jetmetjetFlavor);
   fChain->SetBranchAddress("jetmetjeteta", &jetmetjeteta, &b_jetmetjeteta);
   fChain->SetBranchAddress("jetmetjetetapm", &jetmetjetetapm, &b_jetmetjetetapm);
   fChain->SetBranchAddress("jetmetjetphi", &jetmetjetphi, &b_jetmetjetphi);
   fChain->SetBranchAddress("jetmetjetoverlapmu", &jetmetjetoverlapmu, &b_jetmetjetoverlapmu);
   fChain->SetBranchAddress("jetmetjetoverlapele", &jetmetjetoverlapele, &b_jetmetjetoverlapele);
   fChain->SetBranchAddress("jetmetjetbeta", &jetmetjetbeta, &b_jetmetjetbeta);
   fChain->SetBranchAddress("jetmetjetbetaStar", &jetmetjetbetaStar, &b_jetmetjetbetaStar);
   fChain->SetBranchAddress("jetmetjet1pt", &jetmetjet1pt, &b_jetmetjet1pt);
   fChain->SetBranchAddress("jetmetjet1pt_totunc", &jetmetjet1pt_totunc, &b_jetmetjet1pt_totunc);
   fChain->SetBranchAddress("jetmetjet1Flavor", &jetmetjet1Flavor, &b_jetmetjet1Flavor);
   fChain->SetBranchAddress("jetmetjet1eta", &jetmetjet1eta, &b_jetmetjet1eta);
   fChain->SetBranchAddress("jetmetjet1etapm", &jetmetjet1etapm, &b_jetmetjet1etapm);
   fChain->SetBranchAddress("jetmetjet1phi", &jetmetjet1phi, &b_jetmetjet1phi);
   fChain->SetBranchAddress("jetmetjet1energy", &jetmetjet1energy, &b_jetmetjet1energy);
   fChain->SetBranchAddress("jetmetjet1mass", &jetmetjet1mass, &b_jetmetjet1mass);
   fChain->SetBranchAddress("jetmetjet1Chf", &jetmetjet1Chf, &b_jetmetjet1Chf);
   fChain->SetBranchAddress("jetmetjet1Nhf", &jetmetjet1Nhf, &b_jetmetjet1Nhf);
   fChain->SetBranchAddress("jetmetjet1Phf", &jetmetjet1Phf, &b_jetmetjet1Phf);
   fChain->SetBranchAddress("jetmetjet1Elf", &jetmetjet1Elf, &b_jetmetjet1Elf);
   fChain->SetBranchAddress("jetmetjet1Muf", &jetmetjet1Muf, &b_jetmetjet1Muf);
   fChain->SetBranchAddress("jetmetjet1Vtx3dL", &jetmetjet1Vtx3dL, &b_jetmetjet1Vtx3dL);
   fChain->SetBranchAddress("jetmetjet1Vtx3deL", &jetmetjet1Vtx3deL, &b_jetmetjet1Vtx3deL);
   fChain->SetBranchAddress("jetmetjet1VtxPt", &jetmetjet1VtxPt, &b_jetmetjet1VtxPt);
   fChain->SetBranchAddress("jetmetjet1PtD", &jetmetjet1PtD, &b_jetmetjet1PtD);
   fChain->SetBranchAddress("jetmetjet1SSVHEdisc", &jetmetjet1SSVHEdisc, &b_jetmetjet1SSVHEdisc);
   fChain->SetBranchAddress("jetmetjet1nVertHE", &jetmetjet1nVertHE, &b_jetmetjet1nVertHE);
   fChain->SetBranchAddress("jetmetjet1SSVHPdisc", &jetmetjet1SSVHPdisc, &b_jetmetjet1SSVHPdisc);
   fChain->SetBranchAddress("jetmetjet1nVertHP", &jetmetjet1nVertHP, &b_jetmetjet1nVertHP);
   fChain->SetBranchAddress("jetmetjet1SVmass", &jetmetjet1SVmass, &b_jetmetjet1SVmass);
   fChain->SetBranchAddress("jetmetjet1SVpT", &jetmetjet1SVpT, &b_jetmetjet1SVpT);
   fChain->SetBranchAddress("jetmetjet1CSVdisc", &jetmetjet1CSVdisc, &b_jetmetjet1CSVdisc);
   fChain->SetBranchAddress("jetmetjet1JPdisc", &jetmetjet1JPdisc, &b_jetmetjet1JPdisc);
   fChain->SetBranchAddress("jetmetjet1beta", &jetmetjet1beta, &b_jetmetjet1beta);
   fChain->SetBranchAddress("jetmetjet1betaStar", &jetmetjet1betaStar, &b_jetmetjet1betaStar);
   fChain->SetBranchAddress("jetmetjet2pt", &jetmetjet2pt, &b_jetmetjet2pt);
   fChain->SetBranchAddress("jetmetjet2pt_totunc", &jetmetjet2pt_totunc, &b_jetmetjet2pt_totunc);
   fChain->SetBranchAddress("jetmetjet2Flavor", &jetmetjet2Flavor, &b_jetmetjet2Flavor);
   fChain->SetBranchAddress("jetmetjet2eta", &jetmetjet2eta, &b_jetmetjet2eta);
   fChain->SetBranchAddress("jetmetjet2etapm", &jetmetjet2etapm, &b_jetmetjet2etapm);
   fChain->SetBranchAddress("jetmetjet2phi", &jetmetjet2phi, &b_jetmetjet2phi);
   fChain->SetBranchAddress("jetmetjet2energy", &jetmetjet2energy, &b_jetmetjet2energy);
   fChain->SetBranchAddress("jetmetjet2mass", &jetmetjet2mass, &b_jetmetjet2mass);
   fChain->SetBranchAddress("jetmetjet2Chf", &jetmetjet2Chf, &b_jetmetjet2Chf);
   fChain->SetBranchAddress("jetmetjet2Nhf", &jetmetjet2Nhf, &b_jetmetjet2Nhf);
   fChain->SetBranchAddress("jetmetjet2Phf", &jetmetjet2Phf, &b_jetmetjet2Phf);
   fChain->SetBranchAddress("jetmetjet2Elf", &jetmetjet2Elf, &b_jetmetjet2Elf);
   fChain->SetBranchAddress("jetmetjet2Muf", &jetmetjet2Muf, &b_jetmetjet2Muf);
   fChain->SetBranchAddress("jetmetjet2Vtx3dL", &jetmetjet2Vtx3dL, &b_jetmetjet2Vtx3dL);
   fChain->SetBranchAddress("jetmetjet2Vtx3deL", &jetmetjet2Vtx3deL, &b_jetmetjet2Vtx3deL);
   fChain->SetBranchAddress("jetmetjet2VtxPt", &jetmetjet2VtxPt, &b_jetmetjet2VtxPt);
   fChain->SetBranchAddress("jetmetjet2PtD", &jetmetjet2PtD, &b_jetmetjet2PtD);
   fChain->SetBranchAddress("jetmetjet2SSVHEdisc", &jetmetjet2SSVHEdisc, &b_jetmetjet2SSVHEdisc);
   fChain->SetBranchAddress("jetmetjet2nVertHE", &jetmetjet2nVertHE, &b_jetmetjet2nVertHE);
   fChain->SetBranchAddress("jetmetjet2SSVHPdisc", &jetmetjet2SSVHPdisc, &b_jetmetjet2SSVHPdisc);
   fChain->SetBranchAddress("jetmetjet2nVertHP", &jetmetjet2nVertHP, &b_jetmetjet2nVertHP);
   fChain->SetBranchAddress("jetmetjet2SVmass", &jetmetjet2SVmass, &b_jetmetjet2SVmass);
   fChain->SetBranchAddress("jetmetjet2SVpT", &jetmetjet2SVpT, &b_jetmetjet2SVpT);
   fChain->SetBranchAddress("jetmetjet2CSVdisc", &jetmetjet2CSVdisc, &b_jetmetjet2CSVdisc);
   fChain->SetBranchAddress("jetmetjet2JPdisc", &jetmetjet2JPdisc, &b_jetmetjet2JPdisc);
   fChain->SetBranchAddress("jetmetjet2beta", &jetmetjet2beta, &b_jetmetjet2beta);
   fChain->SetBranchAddress("jetmetjet2betaStar", &jetmetjet2betaStar, &b_jetmetjet2betaStar);
   fChain->SetBranchAddress("jetmetbjet1pt", &jetmetbjet1pt, &b_jetmetbjet1pt);
   fChain->SetBranchAddress("jetmetbjet1pt_totunc", &jetmetbjet1pt_totunc, &b_jetmetbjet1pt_totunc);
   fChain->SetBranchAddress("jetmetbjet1Flavor", &jetmetbjet1Flavor, &b_jetmetbjet1Flavor);
   fChain->SetBranchAddress("jetmetbjet1eta", &jetmetbjet1eta, &b_jetmetbjet1eta);
   fChain->SetBranchAddress("jetmetbjet1etapm", &jetmetbjet1etapm, &b_jetmetbjet1etapm);
   fChain->SetBranchAddress("jetmetbjet1phi", &jetmetbjet1phi, &b_jetmetbjet1phi);
   fChain->SetBranchAddress("jetmetbjet1energy", &jetmetbjet1energy, &b_jetmetbjet1energy);
   fChain->SetBranchAddress("jetmetbjet1mass", &jetmetbjet1mass, &b_jetmetbjet1mass);
   fChain->SetBranchAddress("jetmetbjet1Chf", &jetmetbjet1Chf, &b_jetmetbjet1Chf);
   fChain->SetBranchAddress("jetmetbjet1Nhf", &jetmetbjet1Nhf, &b_jetmetbjet1Nhf);
   fChain->SetBranchAddress("jetmetbjet1Phf", &jetmetbjet1Phf, &b_jetmetbjet1Phf);
   fChain->SetBranchAddress("jetmetbjet1Elf", &jetmetbjet1Elf, &b_jetmetbjet1Elf);
   fChain->SetBranchAddress("jetmetbjet1Muf", &jetmetbjet1Muf, &b_jetmetbjet1Muf);
   fChain->SetBranchAddress("jetmetbjet1Vtx3dL", &jetmetbjet1Vtx3dL, &b_jetmetbjet1Vtx3dL);
   fChain->SetBranchAddress("jetmetbjet1Vtx3deL", &jetmetbjet1Vtx3deL, &b_jetmetbjet1Vtx3deL);
   fChain->SetBranchAddress("jetmetbjet1VtxPt", &jetmetbjet1VtxPt, &b_jetmetbjet1VtxPt);
   fChain->SetBranchAddress("jetmetbjet1PtD", &jetmetbjet1PtD, &b_jetmetbjet1PtD);
   fChain->SetBranchAddress("jetmetbjet1SSVHEdisc", &jetmetbjet1SSVHEdisc, &b_jetmetbjet1SSVHEdisc);
   fChain->SetBranchAddress("jetmetbjet1nVertHE", &jetmetbjet1nVertHE, &b_jetmetbjet1nVertHE);
   fChain->SetBranchAddress("jetmetbjet1SSVHPdisc", &jetmetbjet1SSVHPdisc, &b_jetmetbjet1SSVHPdisc);
   fChain->SetBranchAddress("jetmetbjet1nVertHP", &jetmetbjet1nVertHP, &b_jetmetbjet1nVertHP);
   fChain->SetBranchAddress("jetmetbjet1SVmass", &jetmetbjet1SVmass, &b_jetmetbjet1SVmass);
   fChain->SetBranchAddress("jetmetbjet1SVpT", &jetmetbjet1SVpT, &b_jetmetbjet1SVpT);
   fChain->SetBranchAddress("jetmetbjet1CSVdisc", &jetmetbjet1CSVdisc, &b_jetmetbjet1CSVdisc);
   fChain->SetBranchAddress("jetmetbjet1JPdisc", &jetmetbjet1JPdisc, &b_jetmetbjet1JPdisc);
   fChain->SetBranchAddress("jetmetbjet1beta", &jetmetbjet1beta, &b_jetmetbjet1beta);
   fChain->SetBranchAddress("jetmetbjet1betaStar", &jetmetbjet1betaStar, &b_jetmetbjet1betaStar);
   fChain->SetBranchAddress("jetmetbjet2pt", &jetmetbjet2pt, &b_jetmetbjet2pt);
   fChain->SetBranchAddress("jetmetbjet2pt_totunc", &jetmetbjet2pt_totunc, &b_jetmetbjet2pt_totunc);
   fChain->SetBranchAddress("jetmetbjet2Flavor", &jetmetbjet2Flavor, &b_jetmetbjet2Flavor);
   fChain->SetBranchAddress("jetmetbjet2eta", &jetmetbjet2eta, &b_jetmetbjet2eta);
   fChain->SetBranchAddress("jetmetbjet2etapm", &jetmetbjet2etapm, &b_jetmetbjet2etapm);
   fChain->SetBranchAddress("jetmetbjet2phi", &jetmetbjet2phi, &b_jetmetbjet2phi);
   fChain->SetBranchAddress("jetmetbjet2energy", &jetmetbjet2energy, &b_jetmetbjet2energy);
   fChain->SetBranchAddress("jetmetbjet2mass", &jetmetbjet2mass, &b_jetmetbjet2mass);
   fChain->SetBranchAddress("jetmetbjet2Chf", &jetmetbjet2Chf, &b_jetmetbjet2Chf);
   fChain->SetBranchAddress("jetmetbjet2Nhf", &jetmetbjet2Nhf, &b_jetmetbjet2Nhf);
   fChain->SetBranchAddress("jetmetbjet2Phf", &jetmetbjet2Phf, &b_jetmetbjet2Phf);
   fChain->SetBranchAddress("jetmetbjet2Elf", &jetmetbjet2Elf, &b_jetmetbjet2Elf);
   fChain->SetBranchAddress("jetmetbjet2Muf", &jetmetbjet2Muf, &b_jetmetbjet2Muf);
   fChain->SetBranchAddress("jetmetbjet2Vtx3dL", &jetmetbjet2Vtx3dL, &b_jetmetbjet2Vtx3dL);
   fChain->SetBranchAddress("jetmetbjet2Vtx3deL", &jetmetbjet2Vtx3deL, &b_jetmetbjet2Vtx3deL);
   fChain->SetBranchAddress("jetmetbjet2VtxPt", &jetmetbjet2VtxPt, &b_jetmetbjet2VtxPt);
   fChain->SetBranchAddress("jetmetbjet2PtD", &jetmetbjet2PtD, &b_jetmetbjet2PtD);
   fChain->SetBranchAddress("jetmetbjet2SSVHEdisc", &jetmetbjet2SSVHEdisc, &b_jetmetbjet2SSVHEdisc);
   fChain->SetBranchAddress("jetmetbjet2nVertHE", &jetmetbjet2nVertHE, &b_jetmetbjet2nVertHE);
   fChain->SetBranchAddress("jetmetbjet2SSVHPdisc", &jetmetbjet2SSVHPdisc, &b_jetmetbjet2SSVHPdisc);
   fChain->SetBranchAddress("jetmetbjet2nVertHP", &jetmetbjet2nVertHP, &b_jetmetbjet2nVertHP);
   fChain->SetBranchAddress("jetmetbjet2SVmass", &jetmetbjet2SVmass, &b_jetmetbjet2SVmass);
   fChain->SetBranchAddress("jetmetbjet2SVpT", &jetmetbjet2SVpT, &b_jetmetbjet2SVpT);
   fChain->SetBranchAddress("jetmetbjet2CSVdisc", &jetmetbjet2CSVdisc, &b_jetmetbjet2CSVdisc);
   fChain->SetBranchAddress("jetmetbjet2JPdisc", &jetmetbjet2JPdisc, &b_jetmetbjet2JPdisc);
   fChain->SetBranchAddress("jetmetbjet2beta", &jetmetbjet2beta, &b_jetmetbjet2beta);
   fChain->SetBranchAddress("jetmetbjet2betaStar", &jetmetbjet2betaStar, &b_jetmetbjet2betaStar);
   fChain->SetBranchAddress("jetmetdptj1b1", &jetmetdptj1b1, &b_jetmetdptj1b1);
   fChain->SetBranchAddress("jetmetnj", &jetmetnj, &b_jetmetnj);
   fChain->SetBranchAddress("jetmetnb", &jetmetnb, &b_jetmetnb);
   fChain->SetBranchAddress("jetmetnbP", &jetmetnbP, &b_jetmetnbP);
   fChain->SetBranchAddress("jetmetnhf", &jetmetnhf, &b_jetmetnhf);
   fChain->SetBranchAddress("jetmetnef", &jetmetnef, &b_jetmetnef);
   fChain->SetBranchAddress("jetmetnpf", &jetmetnpf, &b_jetmetnpf);
   fChain->SetBranchAddress("jetmetchf", &jetmetchf, &b_jetmetchf);
   fChain->SetBranchAddress("jetmetnch", &jetmetnch, &b_jetmetnch);
   fChain->SetBranchAddress("jetmetcef", &jetmetcef, &b_jetmetcef);
   fChain->SetBranchAddress("jetmetjetid", &jetmetjetid, &b_jetmetjetid);
   fChain->SetBranchAddress("jetmetrho", &jetmetrho, &b_jetmetrho);
   fChain->SetBranchAddress("vertexAssociationnvertices", &vertexAssociationnvertices, &b_vertexAssociationnvertices);
   fChain->SetBranchAddress("vertexAssociationvx", &vertexAssociationvx, &b_vertexAssociationvx);
   fChain->SetBranchAddress("vertexAssociationvy", &vertexAssociationvy, &b_vertexAssociationvy);
   fChain->SetBranchAddress("vertexAssociationvz", &vertexAssociationvz, &b_vertexAssociationvz);
   fChain->SetBranchAddress("vertexAssociationvxerr", &vertexAssociationvxerr, &b_vertexAssociationvxerr);
   fChain->SetBranchAddress("vertexAssociationvyerr", &vertexAssociationvyerr, &b_vertexAssociationvyerr);
   fChain->SetBranchAddress("vertexAssociationvzerr", &vertexAssociationvzerr, &b_vertexAssociationvzerr);
   fChain->SetBranchAddress("vertexAssociationlepton_dz", &vertexAssociationlepton_dz, &b_vertexAssociationlepton_dz);
   fChain->SetBranchAddress("vertexAssociationl1v_dz", &vertexAssociationl1v_dz, &b_vertexAssociationl1v_dz);
   fChain->SetBranchAddress("vertexAssociationl2v_dz", &vertexAssociationl2v_dz, &b_vertexAssociationl2v_dz);
   fChain->SetBranchAddress("vertexAssociationlvertex", &vertexAssociationlvertex, &b_vertexAssociationlvertex);
   fChain->SetBranchAddress("mebjet1pt", &mebjet1pt, &b_mebjet1pt);
   fChain->SetBranchAddress("mebjet1ptNNCorr", &mebjet1ptNNCorr, &b_mebjet1ptNNCorr);
   fChain->SetBranchAddress("mebjet1etapm", &mebjet1etapm, &b_mebjet1etapm);
   fChain->SetBranchAddress("mebjet1phi", &mebjet1phi, &b_mebjet1phi);
   fChain->SetBranchAddress("mebjet1mass", &mebjet1mass, &b_mebjet1mass);
   fChain->SetBranchAddress("mebjet1massNNCorr", &mebjet1massNNCorr, &b_mebjet1massNNCorr);
   fChain->SetBranchAddress("mebjet2pt", &mebjet2pt, &b_mebjet2pt);
   fChain->SetBranchAddress("mebjet2ptNNCorr", &mebjet2ptNNCorr, &b_mebjet2ptNNCorr);
   fChain->SetBranchAddress("mebjet2etapm", &mebjet2etapm, &b_mebjet2etapm);
   fChain->SetBranchAddress("mebjet2phi", &mebjet2phi, &b_mebjet2phi);
   fChain->SetBranchAddress("mebjet2mass", &mebjet2mass, &b_mebjet2mass);
   fChain->SetBranchAddress("mebjet2massNNCorr", &mebjet2massNNCorr, &b_mebjet2massNNCorr);
   fChain->SetBranchAddress("memu1pt", &memu1pt, &b_memu1pt);
   fChain->SetBranchAddress("memu1etapm", &memu1etapm, &b_memu1etapm);
   fChain->SetBranchAddress("memu1phi", &memu1phi, &b_memu1phi);
   fChain->SetBranchAddress("memu1mass", &memu1mass, &b_memu1mass);
   fChain->SetBranchAddress("memu1charge", &memu1charge, &b_memu1charge);
   fChain->SetBranchAddress("memu2pt", &memu2pt, &b_memu2pt);
   fChain->SetBranchAddress("memu2etapm", &memu2etapm, &b_memu2etapm);
   fChain->SetBranchAddress("memu2phi", &memu2phi, &b_memu2phi);
   fChain->SetBranchAddress("memu2mass", &memu2mass, &b_memu2mass);
   fChain->SetBranchAddress("memu2charge", &memu2charge, &b_memu2charge);
   fChain->SetBranchAddress("meel1pt", &meel1pt, &b_meel1pt);
   fChain->SetBranchAddress("meel1etapm", &meel1etapm, &b_meel1etapm);
   fChain->SetBranchAddress("meel1phi", &meel1phi, &b_meel1phi);
   fChain->SetBranchAddress("meel1mass", &meel1mass, &b_meel1mass);
   fChain->SetBranchAddress("meel1charge", &meel1charge, &b_meel1charge);
   fChain->SetBranchAddress("meel2pt", &meel2pt, &b_meel2pt);
   fChain->SetBranchAddress("meel2etapm", &meel2etapm, &b_meel2etapm);
   fChain->SetBranchAddress("meel2phi", &meel2phi, &b_meel2phi);
   fChain->SetBranchAddress("meel2mass", &meel2mass, &b_meel2mass);
   fChain->SetBranchAddress("meel2charge", &meel2charge, &b_meel2charge);
   fChain->SetBranchAddress("meMET", &meMET, &b_meMET);
   fChain->SetBranchAddress("meMETphi", &meMETphi, &b_meMETphi);
   fChain->SetBranchAddress("mebbM", &mebbM, &b_mebbM);
   fChain->SetBranchAddress("mebbNNCorrM", &mebbNNCorrM, &b_mebbNNCorrM);
   fChain->SetBranchAddress("meFilledJetTF", &meFilledJetTF, &b_meFilledJetTF);
   fChain->SetBranchAddress("meFilledLepTF", &meFilledLepTF, &b_meFilledLepTF);
   fChain->SetBranchAddress("meE_b", &meE_b, &b_meE_b);
   fChain->SetBranchAddress("meE_jb", &meE_jb, &b_meE_jb);
   fChain->SetBranchAddress("meDeltaE_jet", &meDeltaE_jet, &b_meDeltaE_jet);
   fChain->SetBranchAddress("meE_ab", &meE_ab, &b_meE_ab);
   fChain->SetBranchAddress("meE_jab", &meE_jab, &b_meE_jab);
   fChain->SetBranchAddress("meDeltaE_ajet", &meDeltaE_ajet, &b_meDeltaE_ajet);
   fChain->SetBranchAddress("meNNCorrE_jb", &meNNCorrE_jb, &b_meNNCorrE_jb);
   fChain->SetBranchAddress("meDeltaNNCorrE_jet", &meDeltaNNCorrE_jet, &b_meDeltaNNCorrE_jet);
   fChain->SetBranchAddress("meNNCorrE_jab", &meNNCorrE_jab, &b_meNNCorrE_jab);
   fChain->SetBranchAddress("meDeltaNNCorrE_ajet", &meDeltaNNCorrE_ajet, &b_meDeltaNNCorrE_ajet);
   fChain->SetBranchAddress("mephi_b", &mephi_b, &b_mephi_b);
   fChain->SetBranchAddress("mephi_ab", &mephi_ab, &b_mephi_ab);
   fChain->SetBranchAddress("mephi_jb", &mephi_jb, &b_mephi_jb);
   fChain->SetBranchAddress("mephi_jab", &mephi_jab, &b_mephi_jab);
   fChain->SetBranchAddress("meDeltaphi_jet", &meDeltaphi_jet, &b_meDeltaphi_jet);
   fChain->SetBranchAddress("meDeltaphi_ajet", &meDeltaphi_ajet, &b_meDeltaphi_ajet);
   fChain->SetBranchAddress("meEta_b", &meEta_b, &b_meEta_b);
   fChain->SetBranchAddress("meEta_ab", &meEta_ab, &b_meEta_ab);
   fChain->SetBranchAddress("meEta_jb", &meEta_jb, &b_meEta_jb);
   fChain->SetBranchAddress("meEta_jab", &meEta_jab, &b_meEta_jab);
   fChain->SetBranchAddress("meDeltaEta_jet", &meDeltaEta_jet, &b_meDeltaEta_jet);
   fChain->SetBranchAddress("meDeltaEta_ajet", &meDeltaEta_ajet, &b_meDeltaEta_ajet);
   fChain->SetBranchAddress("meE_lgm", &meE_lgm, &b_meE_lgm);
   fChain->SetBranchAddress("meE_lrm", &meE_lrm, &b_meE_lrm);
   fChain->SetBranchAddress("meDeltaE_lm", &meDeltaE_lm, &b_meDeltaE_lm);
   fChain->SetBranchAddress("meE_lgp", &meE_lgp, &b_meE_lgp);
   fChain->SetBranchAddress("meE_lrp", &meE_lrp, &b_meE_lrp);
   fChain->SetBranchAddress("meDeltaE_lp", &meDeltaE_lp, &b_meDeltaE_lp);
   fChain->SetBranchAddress("mephi_lgm", &mephi_lgm, &b_mephi_lgm);
   fChain->SetBranchAddress("mephi_lgp", &mephi_lgp, &b_mephi_lgp);
   fChain->SetBranchAddress("mephi_lrm", &mephi_lrm, &b_mephi_lrm);
   fChain->SetBranchAddress("mephi_lrp", &mephi_lrp, &b_mephi_lrp);
   fChain->SetBranchAddress("meDeltaphi_lm", &meDeltaphi_lm, &b_meDeltaphi_lm);
   fChain->SetBranchAddress("meDeltaphi_lp", &meDeltaphi_lp, &b_meDeltaphi_lp);
   fChain->SetBranchAddress("meEta_lgm", &meEta_lgm, &b_meEta_lgm);
   fChain->SetBranchAddress("meEta_lgp", &meEta_lgp, &b_meEta_lgp);
   fChain->SetBranchAddress("meEta_lrm", &meEta_lrm, &b_meEta_lrm);
   fChain->SetBranchAddress("meEta_lrp", &meEta_lrp, &b_meEta_lrp);
   fChain->SetBranchAddress("meDeltaEta_lm", &meDeltaEta_lm, &b_meDeltaEta_lm);
   fChain->SetBranchAddress("meDeltaEta_lp", &meDeltaEta_lp, &b_meDeltaEta_lp);
   fChain->SetBranchAddress("mePtInv_lgp", &mePtInv_lgp, &b_mePtInv_lgp);
   fChain->SetBranchAddress("mePtInv_lgm", &mePtInv_lgm, &b_mePtInv_lgm);
   fChain->SetBranchAddress("mePtInv_lrp", &mePtInv_lrp, &b_mePtInv_lrp);
   fChain->SetBranchAddress("mePtInv_lrm", &mePtInv_lrm, &b_mePtInv_lrm);
   fChain->SetBranchAddress("meDeltaPtInv_lp", &meDeltaPtInv_lp, &b_meDeltaPtInv_lp);
   fChain->SetBranchAddress("meDeltaPtInv_lm", &meDeltaPtInv_lm, &b_meDeltaPtInv_lm);
   fChain->SetBranchAddress("BtaggingReweightingHE", &BtaggingReweightingHE, &b_BtaggingReweightingHE);
   fChain->SetBranchAddress("BtaggingReweightingHP", &BtaggingReweightingHP, &b_BtaggingReweightingHP);
   fChain->SetBranchAddress("BtaggingReweightingHEexcl", &BtaggingReweightingHEexcl, &b_BtaggingReweightingHEexcl);
   fChain->SetBranchAddress("BtaggingReweightingHPexcl", &BtaggingReweightingHPexcl, &b_BtaggingReweightingHPexcl);
   fChain->SetBranchAddress("BtaggingReweightingHEHE", &BtaggingReweightingHEHE, &b_BtaggingReweightingHEHE);
   fChain->SetBranchAddress("BtaggingReweightingHEHP", &BtaggingReweightingHEHP, &b_BtaggingReweightingHEHP);
   fChain->SetBranchAddress("BtaggingReweightingHPHP", &BtaggingReweightingHPHP, &b_BtaggingReweightingHPHP);
   fChain->SetBranchAddress("LeptonsReweightingweight", &LeptonsReweightingweight, &b_LeptonsReweightingweight);
   fChain->SetBranchAddress("mcSelectioneventType", &mcSelectioneventType, &b_mcSelectioneventType);
   fChain->SetBranchAddress("mcSelectionLepPosPx", &mcSelectionLepPosPx, &b_mcSelectionLepPosPx);
   fChain->SetBranchAddress("mcSelectionLepPosPy", &mcSelectionLepPosPy, &b_mcSelectionLepPosPy);
   fChain->SetBranchAddress("mcSelectionLepPosPz", &mcSelectionLepPosPz, &b_mcSelectionLepPosPz);
   fChain->SetBranchAddress("mcSelectionLepPosEn", &mcSelectionLepPosEn, &b_mcSelectionLepPosEn);
   fChain->SetBranchAddress("mcSelectionLepNegPx", &mcSelectionLepNegPx, &b_mcSelectionLepNegPx);
   fChain->SetBranchAddress("mcSelectionLepNegPy", &mcSelectionLepNegPy, &b_mcSelectionLepNegPy);
   fChain->SetBranchAddress("mcSelectionLepNegPz", &mcSelectionLepNegPz, &b_mcSelectionLepNegPz);
   fChain->SetBranchAddress("mcSelectionLepNegEn", &mcSelectionLepNegEn, &b_mcSelectionLepNegEn);
   fChain->SetBranchAddress("mcSelectionBottomPx", &mcSelectionBottomPx, &b_mcSelectionBottomPx);
   fChain->SetBranchAddress("mcSelectionBottomPy", &mcSelectionBottomPy, &b_mcSelectionBottomPy);
   fChain->SetBranchAddress("mcSelectionBottomPz", &mcSelectionBottomPz, &b_mcSelectionBottomPz);
   fChain->SetBranchAddress("mcSelectionBottomEn", &mcSelectionBottomEn, &b_mcSelectionBottomEn);
   fChain->SetBranchAddress("mcSelectionAntibottomPx", &mcSelectionAntibottomPx, &b_mcSelectionAntibottomPx);
   fChain->SetBranchAddress("mcSelectionAntibottomPy", &mcSelectionAntibottomPy, &b_mcSelectionAntibottomPy);
   fChain->SetBranchAddress("mcSelectionAntibottomPz", &mcSelectionAntibottomPz, &b_mcSelectionAntibottomPz);
   fChain->SetBranchAddress("mcSelectionAntibottomEn", &mcSelectionAntibottomEn, &b_mcSelectionAntibottomEn);
   fChain->SetBranchAddress("mcSelectionFlavLepPos", &mcSelectionFlavLepPos, &b_mcSelectionFlavLepPos);
   fChain->SetBranchAddress("mcSelectionFlavLepNeg", &mcSelectionFlavLepNeg, &b_mcSelectionFlavLepNeg);
   fChain->SetBranchAddress("mcSelectionNLepPos", &mcSelectionNLepPos, &b_mcSelectionNLepPos);
   fChain->SetBranchAddress("mcSelectionNLepNeg", &mcSelectionNLepNeg, &b_mcSelectionNLepNeg);
   fChain->SetBranchAddress("mcSelectionNBottom", &mcSelectionNBottom, &b_mcSelectionNBottom);
   fChain->SetBranchAddress("mcSelectionNAntibottom", &mcSelectionNAntibottom, &b_mcSelectionNAntibottom);
   fChain->SetBranchAddress("lumiReweightingLumiWeight", &lumiReweightingLumiWeight, &b_lumiReweightingLumiWeight);
   fChain->SetBranchAddress("lumiReweightingpu", &lumiReweightingpu, &b_lumiReweightingpu);
   fChain->SetBranchAddress("lumiReweightingpv", &lumiReweightingpv, &b_lumiReweightingpv);
   fChain->SetBranchAddress("rc_eventSelection_0_idx", &rc_eventSelection_0_idx, &b_rc_eventSelection_0_idx);
   fChain->SetBranchAddress("rc_eventSelection_0_lbl", &rc_eventSelection_0_lbl, &b_rc_eventSelection_0_lbl);
   fChain->SetBranchAddress("rc_eventSelection_1_idx", &rc_eventSelection_1_idx, &b_rc_eventSelection_1_idx);
   fChain->SetBranchAddress("rc_eventSelection_1_lbl", &rc_eventSelection_1_lbl, &b_rc_eventSelection_1_lbl);
   fChain->SetBranchAddress("rc_eventSelection_2_idx", &rc_eventSelection_2_idx, &b_rc_eventSelection_2_idx);
   fChain->SetBranchAddress("rc_eventSelection_2_lbl", &rc_eventSelection_2_lbl, &b_rc_eventSelection_2_lbl);
   fChain->SetBranchAddress("rc_eventSelection_3_idx", &rc_eventSelection_3_idx, &b_rc_eventSelection_3_idx);
   fChain->SetBranchAddress("rc_eventSelection_3_lbl", &rc_eventSelection_3_lbl, &b_rc_eventSelection_3_lbl);
   fChain->SetBranchAddress("rc_eventSelection_4_idx", &rc_eventSelection_4_idx, &b_rc_eventSelection_4_idx);
   fChain->SetBranchAddress("rc_eventSelection_4_lbl", &rc_eventSelection_4_lbl, &b_rc_eventSelection_4_lbl);
   fChain->SetBranchAddress("rc_eventSelection_5_idx", &rc_eventSelection_5_idx, &b_rc_eventSelection_5_idx);
   fChain->SetBranchAddress("rc_eventSelection_5_lbl", &rc_eventSelection_5_lbl, &b_rc_eventSelection_5_lbl);
   fChain->SetBranchAddress("rc_eventSelection_6_idx", &rc_eventSelection_6_idx, &b_rc_eventSelection_6_idx);
   fChain->SetBranchAddress("rc_eventSelection_6_lbl", &rc_eventSelection_6_lbl, &b_rc_eventSelection_6_lbl);
   fChain->SetBranchAddress("rc_eventSelection_7_idx", &rc_eventSelection_7_idx, &b_rc_eventSelection_7_idx);
   fChain->SetBranchAddress("rc_eventSelection_7_lbl", &rc_eventSelection_7_lbl, &b_rc_eventSelection_7_lbl);
   fChain->SetBranchAddress("rc_eventSelection_8_idx", &rc_eventSelection_8_idx, &b_rc_eventSelection_8_idx);
   fChain->SetBranchAddress("rc_eventSelection_8_lbl", &rc_eventSelection_8_lbl, &b_rc_eventSelection_8_lbl);
   fChain->SetBranchAddress("rc_eventSelection_9_idx", &rc_eventSelection_9_idx, &b_rc_eventSelection_9_idx);
   fChain->SetBranchAddress("rc_eventSelection_9_lbl", &rc_eventSelection_9_lbl, &b_rc_eventSelection_9_lbl);
   fChain->SetBranchAddress("rc_eventSelection_10_idx", &rc_eventSelection_10_idx, &b_rc_eventSelection_10_idx);
   fChain->SetBranchAddress("rc_eventSelection_10_lbl", &rc_eventSelection_10_lbl, &b_rc_eventSelection_10_lbl);
   fChain->SetBranchAddress("rc_eventSelection_11_idx", &rc_eventSelection_11_idx, &b_rc_eventSelection_11_idx);
   fChain->SetBranchAddress("rc_eventSelection_11_lbl", &rc_eventSelection_11_lbl, &b_rc_eventSelection_11_lbl);
   fChain->SetBranchAddress("rc_eventSelection_12_idx", &rc_eventSelection_12_idx, &b_rc_eventSelection_12_idx);
   fChain->SetBranchAddress("rc_eventSelection_12_lbl", &rc_eventSelection_12_lbl, &b_rc_eventSelection_12_lbl);
   fChain->SetBranchAddress("rc_eventSelection_13_idx", &rc_eventSelection_13_idx, &b_rc_eventSelection_13_idx);
   fChain->SetBranchAddress("rc_eventSelection_13_lbl", &rc_eventSelection_13_lbl, &b_rc_eventSelection_13_lbl);
   fChain->SetBranchAddress("rc_eventSelection_14_idx", &rc_eventSelection_14_idx, &b_rc_eventSelection_14_idx);
   fChain->SetBranchAddress("rc_eventSelection_14_lbl", &rc_eventSelection_14_lbl, &b_rc_eventSelection_14_lbl);
   fChain->SetBranchAddress("rc_eventSelection_15_idx", &rc_eventSelection_15_idx, &b_rc_eventSelection_15_idx);
   fChain->SetBranchAddress("rc_eventSelection_15_lbl", &rc_eventSelection_15_lbl, &b_rc_eventSelection_15_lbl);
   fChain->SetBranchAddress("rc_eventSelection_16_idx", &rc_eventSelection_16_idx, &b_rc_eventSelection_16_idx);
   fChain->SetBranchAddress("rc_eventSelection_16_lbl", &rc_eventSelection_16_lbl, &b_rc_eventSelection_16_lbl);
   fChain->SetBranchAddress("rc_eventSelection_17_idx", &rc_eventSelection_17_idx, &b_rc_eventSelection_17_idx);
   fChain->SetBranchAddress("rc_eventSelection_17_lbl", &rc_eventSelection_17_lbl, &b_rc_eventSelection_17_lbl);
   fChain->SetBranchAddress("rc_eventSelection_18_idx", &rc_eventSelection_18_idx, &b_rc_eventSelection_18_idx);
   fChain->SetBranchAddress("rc_eventSelection_18_lbl", &rc_eventSelection_18_lbl, &b_rc_eventSelection_18_lbl);
   Notify();
}

Bool_t rds_zbb::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void rds_zbb::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t rds_zbb::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef rds_zbb_cxx
