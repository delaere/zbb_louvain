//inclusive MM
#include "selectedNNs/MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500.cxx"
#include "selectedNNs/MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600.cxx"
#include "selectedNNs/MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000.cxx"

//MM
#include "selectedNNs/MLP_Higgs_vs_DY_ZH125_comb-2-4_1000_Nj2_Mbb80-150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR-3-9_500_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_Higgs_vs_TT_ZH125_comb-5-10_700_Nj2_Mbb50-200_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR-2-4_500_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_Higgs_vs_ZZ_ZH125_comb-2-4_750_Nj2_Mbb80-150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR-2-4_501_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20.cxx"

//ML
#include "selectedNNs/MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2.cxx"
#include "selectedNNs/MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.cxx"

//ZZ ML
#include "selectedNNs/MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20.cxx"
#include "selectedNNs/MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20.cxx"

class nn_vars {
  public:
  int N;
  double *gg;
  double *qq;
  double *tt;
  double *hi;
  double *hi3;
  double *zz;
  double *zz3;
  int *flavour;
  double *deta;
  double *dphi;
  double *ptZ;
  double *MEptZ;
  double *ptbb;
  double *met;
  double *Mll;
  double *Mbb;
  double *regMbb;
  double *Metsig;
  double * multi;
  double *hzbb;
  double *htt;
  double *hzz;
  double *hzbb_2j;
  double *htt_2j;
  double *hzz_2j;
  double *hzbb_3j;
  double *htt_3j;
  double *hzz_3j;

  double *zzdy_2j;
  double *zztt_2j;
  double *zzdy_3j;
  double *zztt_3j;

  int *evt_nbr;
  double *tagj1;
  double *tagj2;
  double *prodNNs;
  double *prodNNs_2j;
  double *prodNNs_3j;
  double *evtWeight;
  double *trijetMdr;
  double *fsrDR;
  double *dijetdR;
  int *isMuMu;
  double *Mbb125;
  double *Mbb91;
  double *regMbb125;
  double *regMbb91;
  double *Mll91;
  nn_vars(int size) {
    N = size;
    gg = new double[size];
    qq = new double[size];
    tt = new double[size];
    hi = new double[size];
    hi3 = new double[size];
    zz = new double[size];
    zz3 = new double[size];
    flavour = new int[size];
    deta = new double[size];
    dphi = new double[size];
    ptZ = new double[size];
    MEptZ = new double[size];
    ptbb = new double[size];
    met = new double[size];
    Mll = new double[size];
    Mbb = new double[size];
    regMbb = new double[size];
    hzbb = new double[size];
    htt = new double[size];
    hzz = new double[size];
    hzbb_2j = new double[size];
    htt_2j = new double[size];
    hzz_2j = new double[size];
    hzbb_3j = new double[size];
    htt_3j = new double[size];
    hzz_3j = new double[size];
  
    zzdy_2j = new double[size];
    zztt_2j = new double[size];
    zzdy_3j = new double[size];
    zztt_3j = new double[size];

    Metsig = new double[size];
    multi = new double[size];
    evt_nbr = new int[size];
    tagj1 = new double[size];
    tagj2 = new double[size];
    prodNNs = new double[size];
    prodNNs_2j = new double[size];
    prodNNs_3j = new double[size];
    evtWeight = new double[size];
    trijetMdr = new double[size];
    fsrDR = new double[size];
    dijetdR = new double[size];
    isMuMu = new int[size];
    Mbb125 = new double[size];
    Mbb91 = new double[size];
    regMbb125 = new double[size];
    regMbb91 = new double[size];
    Mll91 = new double[size];
  }
};

class tree_in {
 public : 
  double ggweight;
  double qqweight;
  double ttweight;
  double zzweight;
  double zz3weight;
  double hiweight;
  double hi3weight;
  double Mll;
  double Mbb;
  double Mbb91;
  double Mbb125;
  double regMbb91;
  double regMbb125;
  double Mll91;
  double Met;
  double metsig;
  double deta;
  double dphi;
  double ptZ,MEptZ,ptbb;
  int type;
  double HvsZbb;
  double HvsTT;
  double HvsZZ;
  double HvsZbb2j;
  double HvsTT2j;
  double HvsZZ2j;
  double HvsZbb3j;
  double HvsTT3j;
  double HvsZZ3j;

  double ZZvsDY2j;
  double ZZvsTT2j;
  double ZZvsDY3j;
  double ZZvsTT3j;

  double prodCSV;
  double regMbb;
  double dphiZbb;
  double prodNNs;
  double prodNNs2j;
  double prodNNs3j;
  double Multi;
  int type2;
  double evtWeight;
  double trijetMdr;
  double fsrDR;
  double dijetdR;

};


void Input(const string rootFile, nn_vars *var, tree_in *sim, TTree *simu, int fill, int sig, int typ2, TString totcuts)
{

  // input file : read ttree
  //TChain *chain;
  TChain *treeIn = new TChain("rds_zbb");
  treeIn->Reset();
  treeIn->Add(rootFile.c_str());
  TTree *tree = treeIn->CopyTree(totcuts);

  double Eta_j1,Eta_j2,Phi_j1,Phi_j2,MeTPhi,MeT,MeTsig;
  double Pt_lepplus,Eta_lepplus,Phi_lepplus,Pt_lepminus,Eta_lepminus,Phi_lepminus;
  double Pt_lep2plus,Eta_lep2plus,Phi_lep2plus,Pt_lep2minus,Eta_lep2minus,Phi_lep2minus;
  double Ej1,Ej2,Ptj1,Ptj2;
  double Wgg,Wqq,Wtt,Wzz,Wzz3,Whi,Whi3;
  double btagj1,btagj2;
  double Mll, Mbb, regMbb, MEptZ, zptMu, zptEle, dphiZbb;
  double multiplicity;
  double btagWeights, leptWeights, lumiWeights;
  double trijetMdr, fsrDR, dijetdR;

  tree->SetBranchAddress("jetmetnj",&multiplicity);
  tree->SetBranchAddress("jetmettrijetMdr",&trijetMdr);
  tree->SetBranchAddress("jetmetfsrDR",&fsrDR);
  tree->SetBranchAddress("eventSelectiondijetdR",&dijetdR);
  tree->SetBranchAddress("Wgg",&Wgg);
  tree->SetBranchAddress("Wqq",&Wqq);
  tree->SetBranchAddress("Wtt",&Wtt);
  tree->SetBranchAddress("Wzz0",&Wzz);
  tree->SetBranchAddress("Wzz3",&Wzz3);
  tree->SetBranchAddress("Whi0_125",&Whi);
  tree->SetBranchAddress("Whi3_125",&Whi3);
  tree->SetBranchAddress("MeTPhi",&MeTPhi);
  tree->SetBranchAddress("MeT",&MeT);
  tree->SetBranchAddress("Met_signi",&MeTsig);
  tree->SetBranchAddress("Pt_elplus",&Pt_lepplus);
  tree->SetBranchAddress("Eta_elplus",&Eta_lepplus);
  tree->SetBranchAddress("Phi_elplus",&Phi_lepplus);
  tree->SetBranchAddress("Pt_elminus",&Pt_lepminus);
  tree->SetBranchAddress("Eta_elminus",&Eta_lepminus);
  tree->SetBranchAddress("Phi_elminus",&Phi_lepminus);
  tree->SetBranchAddress("Pt_Muplus",&Pt_lep2plus);
  tree->SetBranchAddress("Eta_Muplus",&Eta_lep2plus);
  tree->SetBranchAddress("Phi_Muplus",&Phi_lep2plus);
  tree->SetBranchAddress("Pt_Muminus",&Pt_lep2minus);
  tree->SetBranchAddress("Eta_Muminus",&Eta_lep2minus);
  tree->SetBranchAddress("Phi_Muminus",&Phi_lep2minus);
  tree->SetBranchAddress("Eta_j2",&Eta_j2);
  tree->SetBranchAddress("Phi_j2",&Phi_j2);
  tree->SetBranchAddress("Eta_j1",&Eta_j1);
  tree->SetBranchAddress("Phi_j1",&Phi_j1);
  tree->SetBranchAddress("E_j2",&Ej2);
  tree->SetBranchAddress("jetmetbjet1pt",&Ptj2);
  tree->SetBranchAddress("E_j1",&Ej1);
  tree->SetBranchAddress("jetmetbjet1pt",&Ptj1);
  tree->SetBranchAddress("jetmetbjet1CSVdisc",&btagj1);
  tree->SetBranchAddress("jetmetbjet2CSVdisc",&btagj2);
  tree->SetBranchAddress("Inv_Mass_lept",&Mll);
  tree->SetBranchAddress("eventSelectiondijetM",&Mbb);
  tree->SetBranchAddress("mebbNNCorrM",&regMbb);
  tree->SetBranchAddress("eventSelectionbestzptMu",&zptMu);
  tree->SetBranchAddress("eventSelectionbestzptEle",&zptEle);
  tree->SetBranchAddress("mcSelectionllpt",&MEptZ);
  tree->SetBranchAddress("eventSelectiondphiZbb",&dphiZbb);
  tree->SetBranchAddress("BtaggingReweightingHPHP",&btagWeights);
  tree->SetBranchAddress("LeptonsReweightingweight",&leptWeights);
  tree->SetBranchAddress("lumiReweightingLumiWeight",&lumiWeights);

  // NN declaration -------------------------------------
  MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600 *HZbb=new MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600(); 
  MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500 *HTT=new MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500();    
  MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000 *HZZ=new MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000();

  MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 *HZbb_2j = new MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20();
  MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20 *HTT_2j = new MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20(); 
  MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 *HZZ_2j = new MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20();   

  MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *HZbb_3j = new MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
  MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *HTT_3j = new MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
  MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *HZZ_3j = new MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();


  MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2 *HZbb_ML_2j = new MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2();
  MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 *HTT_ML_2j = new MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20(); 
  MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20 *HZZ_ML_2j = new MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20();   

  MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *HZbb_ML_3j = new MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
  MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *HTT_ML_3j = new MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();
  MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20 *HZZ_ML_3j = new MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20();


  MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20 *ZZDY_2j = new MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20();
  MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20 *ZZDY_3j = new MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20();
  MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20 *ZZTT_2j = new MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20();
  MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20 *ZZTT_3j = new MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20();

  // ----------------------------------------------------
  
  double entry=0.0;
  for (int i=0;i<tree->GetEntries(); ++i){	
    tree->GetEntry(i); // read tree Zbb 
    double dphi1 = MeTPhi-Phi_j1;
    double dphi2 = MeTPhi-Phi_j2;
    if(dphi1>TMath::Pi()){dphi1= (2*TMath::Pi()) - dphi1;}
    if(dphi2>TMath::Pi()){dphi2= (2*TMath::Pi()) - dphi2;}
    if(fabs(dphi1)<fabs(dphi2)){sim->dphi=fabs(dphi1);}
    if(fabs(dphi2)<fabs(dphi1)){sim->dphi=fabs(dphi2);}
    TLorentzVector l1,l2,b1,b2;
    if(Pt_lepplus>0.0 && Pt_lepminus>0.0){l1.SetPtEtaPhiM(Pt_lepplus,Eta_lepplus,Phi_lepplus,0.000511);}
    if(Pt_lepplus>0.0 && Pt_lepminus>0.0){l2.SetPtEtaPhiM(Pt_lepminus,Eta_lepminus,Phi_lepminus,0.000511);}
    if(Pt_lep2plus>0.0 && Pt_lep2minus>0.0){l1.SetPtEtaPhiM(Pt_lep2plus,Eta_lep2plus,Phi_lep2plus,0.105);}
    if(Pt_lep2plus>0.0 && Pt_lep2minus>0.0){l2.SetPtEtaPhiM(Pt_lep2minus,Eta_lep2minus,Phi_lep2minus,0.105);}
    b1.SetPtEtaPhiE(Ptj1,Eta_j1,Phi_j1,Ej1);
    b2.SetPtEtaPhiE(Ptj2,Eta_j2,Phi_j2,Ej2);
    //fill
    //if(btagj2<0.679) cout<<"ERROR, cut bad"<<endl;
    sim->ggweight=Wgg;
    sim->qqweight=Wqq;
    sim->ttweight=Wtt;
    sim->zzweight=Wzz;
    sim->zz3weight=Wzz3;
    sim->hiweight=Whi;
    sim->hi3weight=Whi3;
    sim->trijetMdr=trijetMdr;
    var->trijetMdr[i]=sim->trijetMdr;
    sim->fsrDR=fsrDR;
    var->fsrDR[i]=sim->fsrDR;
    sim->dijetdR=dijetdR;
    var->dijetdR[i]=sim->dijetdR;

    sim->HvsZbb=HZbb->Value(0,Wgg,Wqq,Whi,Whi3);
    sim->HvsTT=HTT->Value(0,Wtt,Whi,Whi3);                                                                                                                                                               
    sim->HvsZZ=HZZ->Value(0,Wzz,Wzz3,Whi,Whi3);

    sim->HvsZbb2j=HZbb_2j->Value(0,Wgg,Wqq,Whi,Whi3);
    sim->HvsTT2j=HTT_2j->Value(0,Wtt,Whi,Whi3);                                                                                                                                                    
    sim->HvsZZ2j=HZZ_2j->Value(0,Wzz,Wzz3,Whi,Whi3);

    sim->HvsZbb3j=HZbb_3j->Value(0,Wgg,Wqq,Whi,Whi3,trijetMdr,fsrDR,dijetdR);
    sim->HvsTT3j=HTT_3j->Value(0,Wtt,Whi,Whi3,trijetMdr,fsrDR,dijetdR);                                                                                                                        
    sim->HvsZZ3j=HZZ_3j->Value(0,Wzz,Wzz3,Whi,Whi3,trijetMdr,fsrDR,dijetdR);

    if(!totcuts.Contains("rc_eventSelection_18_idx==1")){
      sim->HvsZbb2j=HZbb_ML_2j->Value(0,Wgg,Wqq,Whi,Whi3);
      sim->HvsTT2j=HTT_ML_2j->Value(0,Wtt,Whi,Whi3);
      sim->HvsZZ2j=HZZ_ML_2j->Value(0,Wzz,Wzz3,Whi,Whi3);

      sim->HvsZbb3j=HZbb_ML_3j->Value(0,Wgg,Wqq,Whi,Whi3,trijetMdr,fsrDR);
      sim->HvsTT3j=HTT_ML_3j->Value(0,Wtt,Whi,Whi3,trijetMdr,fsrDR);
      sim->HvsZZ3j=HZZ_ML_3j->Value(0,Wzz,Wzz3,Whi,Whi3,trijetMdr,fsrDR);
    }

    sim->ZZvsDY2j=ZZDY_2j->Value(0,Wgg,Wqq,Wzz,Wzz3);
    sim->ZZvsDY3j=ZZDY_3j->Value(0,Wgg,Wqq,Wzz,Wzz3,trijetMdr,fsrDR);
    sim->ZZvsTT2j=ZZTT_2j->Value(0,Wtt,Wzz,Wzz3);
    sim->ZZvsTT3j=ZZTT_3j->Value(0,Wtt,Wzz,Wzz3,trijetMdr,fsrDR);
    
    var->hzbb[i] = sim->HvsZbb;
    var->htt[i] = sim->HvsTT;
    var->hzz[i] = sim->HvsZZ;

    var->hzbb_2j[i] = sim->HvsZbb2j;
    var->htt_2j[i] = sim->HvsTT2j;
    var->hzz_2j[i] = sim->HvsZZ2j;

    var->hzbb_3j[i] = sim->HvsZbb3j;
    var->htt_3j[i] = sim->HvsTT3j;
    var->hzz_3j[i] = sim->HvsZZ3j;

    var->zzdy_2j[i] = sim->ZZvsDY2j;
    var->zzdy_3j[i] = sim->ZZvsDY3j;
    var->zztt_2j[i] = sim->ZZvsTT2j;
    var->zztt_3j[i] = sim->ZZvsTT3j;

    sim->prodNNs=sim->HvsZbb*sim->HvsTT*sim->HvsZZ;
    var->prodNNs[i]=sim->prodNNs;
    sim->prodNNs2j=sim->HvsZbb2j*sim->HvsTT2j*sim->HvsZZ2j;
    var->prodNNs_2j[i]=sim->prodNNs2j;
    sim->prodNNs3j=sim->HvsZbb3j*sim->HvsTT3j*sim->HvsZZ3j;
    var->prodNNs_3j[i]=sim->prodNNs3j;
    if(sim->ggweight>300.0){sim->ggweight=50;}
    if(sim->qqweight>300.0){sim->qqweight=50;}
    if(sim->ttweight>300.0){sim->ttweight=50;}
    if(sim->zzweight>300.0){sim->zzweight=50;}
    if(sim->zz3weight>300.0){sim->zz3weight=50;}
    if(sim->hiweight>300.0){sim->hiweight=50;}
    if(sim->hi3weight>300.0){sim->hi3weight=50;}
    var->gg[i]=sim->ggweight;
    var->qq[i]=sim->qqweight;
    var->zz[i]=sim->zzweight;
    var->zz3[i]=sim->zz3weight;
    var->hi[i]=sim->hiweight;
    var->hi3[i]=sim->hi3weight;
    var->tt[i]=sim->ttweight;
    var->tagj1[i]=btagj1;
    var->tagj2[i]=btagj2;
    sim->prodCSV=btagj1*btagj2;
    sim->type=sig;
    sim->type2=typ2;
    sim->deta = fabs(Eta_j1-Eta_j2);
    var->deta[i]=fabs(Eta_j1-Eta_j2);
    sim->ptZ=max(zptMu,zptEle);
    sim->MEptZ=MEptZ;
    sim->ptbb=(b1+b2).Pt();
    sim->Mll=Mll;//(l1+l2).M();
    sim->Mll91=fabs(91-Mll);//(l1+l2).M();
    sim->Mbb=Mbb;//(b1+b2).M();
    sim->Mbb91=fabs(91-Mbb);//(b1+b2).M();
    sim->Mbb125=fabs(125-Mbb);//(b1+b2).M();
    sim->regMbb=regMbb;//(b1+b2).M();
    sim->regMbb91=fabs(91-regMbb);//(b1+b2).M();
    sim->regMbb125=fabs(125-regMbb);//(b1+b2).M();
    var->Mll[i]=sim->Mll;
    var->Mll91[i]=sim->Mll91;
    var->Mbb[i]=sim->Mbb;
    var->Mbb125[i]=sim->Mbb125;
    var->Mbb91[i]=sim->Mbb91;
    var->regMbb[i]=sim->regMbb;
    var->regMbb125[i]=sim->regMbb125;
    var->regMbb91[i]=sim->regMbb91;
    var->dphi[i]=sim->dphi;
    var->ptZ[i]=sim->ptZ;
    var->MEptZ[i]=sim->MEptZ;
    var->ptbb[i]=sim->ptbb;
    var->Metsig[i]=MeTsig;
    sim->metsig=MeTsig;   
    sim->Met=MeT;
    var->met[i]=sim->Met;
    sim->Multi=multiplicity;
    var->multi[i]=sim->Multi;
    var->evtWeight[i]=btagWeights*leptWeights*lumiWeights;
    sim->evtWeight=var->evtWeight[i];
    var->isMuMu[i] = 0;
    if(zptMu>0) var->isMuMu[i] = 1;
    if(fill==1){simu->Fill();entry+=1;}     
  }
  var->evt_nbr[0]=entry;
  cout<<entry<<endl; 
}
