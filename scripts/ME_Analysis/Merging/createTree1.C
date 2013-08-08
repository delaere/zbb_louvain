#include "TTree.h"
#include "TFile.h"
#include "TRandom.h"
#include "TTree.h"
#include "TLorentzVector.h"
#include "rds_zbb.C"

#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

TString inputFolder = "/nfs/user/acaudron/RDS537_JESdown/";
TString outputFolder = "/nfs/user/acaudron/LHCO537_JESdown/";

void CreateTree(TString InputFile){ 
 
  int runNumber;
  int eventNumber;

  double E_j1;
  double E_j2;
  double Eta_j1;
  double Eta_j2;
  double phi_j1;
  double phi_j2;
  double Pt_j1;
  double Pt_j2;
  double btag_j1;
  double btag_j2;
  double Mass_j1;
  double Mass_j2;
  
  double deltaE_ajet;
  double deltaE_jet;
  double deltaEta_ajet;
  double deltaEta_jet;  
  double deltaPhi_ajet;
  double deltaPhi_jet;    

  double llM;
  double bbM;

  double E_l1;
  double E_l2;
  double Eta_l1;
  double Eta_l2;
  double phi_l1;
  double phi_l2;
  double Pt_l1;
  double Pt_l2;
  double Mass_l1;
  double Mass_l2; 
  int charge_l1;
  int charge_l2; 
    
  double deltaElp;
  double deltaElm;
  double deltaEtalp;
  double deltaEtalm;  
  double deltaPhilp;
  double deltaPhilm;
  double deltaPtInvlp;
  double deltaPtInvlm;  
       
  double DR_jet;

  double Met;
  double Met_phi;
  double Met_sig;

  int isZb;
  int isZc;
  int isZl;
  double Pile_up;

  int nbr_PV;

  int nJets;
  int nBjetsHE;
  int nBjetsHP;
  int nBjetsHEHP;
  
  int category;

  std::cout << "Running over sample: " << InputFile << std::endl;
  bool isMuChannel = false;
  if (InputFile.Contains("Mu_") && InputFile.Contains("El_")) {
    std::cout << "InputFile name cannot contain both <<Mu>> and <<El>>" << std::endl;
    return;
  }
  else if (InputFile.Contains("Mu")) {
    std::cout << "  running MuMu channel" << std::endl;
    isMuChannel = true;
  }
  else if (InputFile.Contains("El")) {
    std::cout << "  running over ElEl channel" << std::endl;
  }
  else {
    std::cout << "InputFile name must contain <<Mu>> or <<El>>" << std::endl;
    return;  
  }
  
  bool IsDATA = InputFile.Contains("Data");
  
  TFile* f_RDS  = new TFile(inputFolder+"File_rds_zbb_"+InputFile+".root");
  TTree* t_RDS    = (TTree*)f_RDS->Get("rds_zbb");  
  
  rds_zbb* mc_RDS = new rds_zbb(t_RDS);
  
  TFile *f_RDSME = new TFile(outputFolder+"outRDStoLHCO_"+InputFile+".root", "RECREATE");
  TTree *t_RDSME = new TTree("tree1", "tree 1");   
  
  t_RDSME->Branch("runNumber", &runNumber, "runNumber/l");
  t_RDSME->Branch("eventNumber", &eventNumber, "eventNumber/l");
  
  t_RDSME->Branch("E_j1",&E_j1,"E_j1/D");
  t_RDSME->Branch("E_j2",&E_j2,"E_j2/D");
  t_RDSME->Branch("Eta_j1",&Eta_j1,"Eta_j1/D");
  t_RDSME->Branch("Eta_j2",&Eta_j2,"Eta_j2/D");
  t_RDSME->Branch("phi_j1",&phi_j1,"phi_j1/D");
  t_RDSME->Branch("phi_j2",&phi_j2,"phi_j2/D");
  t_RDSME->Branch("Pt_j1",&Pt_j1,"Pt_j1/D");
  t_RDSME->Branch("Pt_j2",&Pt_j2,"Pt_j2/D");
  t_RDSME->Branch("btag_j1",&btag_j1,"btag_j1/D");
  t_RDSME->Branch("btag_j2",&btag_j2,"btag_j2/D");
  t_RDSME->Branch("Mass_j1",&Mass_j1,"Mass_j1/D");
  t_RDSME->Branch("Mass_j2",&Mass_j2,"Mass_j2/D");   
  
  t_RDSME->Branch("deltaE_ajet",&deltaE_ajet,"deltaE_ajet/D");       
  t_RDSME->Branch("deltaE_jet",&deltaE_jet,"deltaE_jet/D");          
  t_RDSME->Branch("deltaEta_ajet",&deltaEta_ajet,"deltaEta_ajet/D"); 
  t_RDSME->Branch("deltaEta_jet",&deltaEta_jet,"deltaEta_jet/D");    
  t_RDSME->Branch("deltaPhi_ajet",&deltaPhi_ajet,"deltaPhi_ajet/D"); 
  t_RDSME->Branch("deltaPhi_jet",&deltaPhi_jet,"deltaPhi_jet/D");    
 
  t_RDSME->Branch("llM",&llM,"llM/D");
  t_RDSME->Branch("bbM",&bbM,"bbM/D");
  
  t_RDSME->Branch("E_l1",&E_l1,"E_l1/D");
  t_RDSME->Branch("E_l2",&E_l2,"E_l2/D");
  t_RDSME->Branch("Eta_l1",&Eta_l1,"Eta_l1/D");
  t_RDSME->Branch("Eta_l2",&Eta_l2,"Eta_l2/D");
  t_RDSME->Branch("phi_l1",&phi_l1,"phi_l1/D");
  t_RDSME->Branch("phi_l2",&phi_l2,"phi_l2/D");
  t_RDSME->Branch("Pt_l1",&Pt_l1,"Pt_l1/D");
  t_RDSME->Branch("Pt_l2",&Pt_l2,"Pt_l2/D");
  t_RDSME->Branch("Mass_l1",&Mass_l1,"Mass_l1/D");
  t_RDSME->Branch("Mass_l2",&Mass_l2,"Mass_l2/D");  
  t_RDSME->Branch("charge_l1",&charge_l1,"charge_l1/I");
  t_RDSME->Branch("charge_l2",&charge_l2,"charge_l2/I");
  
  t_RDSME->Branch("deltaElp",&deltaElp,"deltaElp/D");      
  t_RDSME->Branch("deltaElm",&deltaElm,"deltaElm/D");      
  t_RDSME->Branch("deltaEtalp",&deltaEtalp,"deltaEtalp/D");
  t_RDSME->Branch("deltaEtalm",&deltaEtalm,"deltaEtalm/D"); 
  t_RDSME->Branch("deltaPhilp",&deltaPhilp,"deltaPhilp/D");
  t_RDSME->Branch("deltaPhilm",&deltaPhilm,"deltaPhilm/D");
  t_RDSME->Branch("deltaPtInvlp",&deltaPtInvlp,"deltaPtInvlp/D");
  t_RDSME->Branch("deltaPtInvlm",&deltaPtInvlm,"deltaPtInvlm/D");
  
  t_RDSME->Branch("DR_jet",&DR_jet,"DR_jet/D");
  
  t_RDSME->Branch("Met", &Met, "Met/D");
  t_RDSME->Branch("Met_phi", &Met_phi, "Met_phi/D");
  t_RDSME->Branch("Met_sig", &Met_sig, "Met_sig/D");
  
  t_RDSME->Branch("isZb", &isZb, "isZb/I");
  t_RDSME->Branch("isZc", &isZc, "isZc/I");
  t_RDSME->Branch("isZl", &isZl, "isZl/I");
  t_RDSME->Branch("Pile_up", &Pile_up, "Pile_up/D");
  
  t_RDSME->Branch("nbr_PV", &nbr_PV, "nbr_PV/I");

  t_RDSME->Branch("nJets", &nJets, "nJets/I");
  //t_RDSME->Branch("nBjetsHE", &nBjetsHE, "nBjetsHE/I");
  //t_RDSME->Branch("nBjetsHP", &nBjetsHP, "nBjetsHP/I");
  //t_RDSME->Branch("nBjetsHEHP", &nBjetsHEHP, "nBjetsHEHP/I"); 
  
  //t_RDSME->Branch("category", &category, "category/I"); 
  
  ofstream myfile2; 
  myfile2.open (outputFolder+"outRDStoLHCO_"+InputFile+".lhco",ios::out); 
  
  Long64_t nbytesRDS = 0, nbRDS = 0;
  for (Int_t iRDS=0;iRDS<t_RDS->GetEntries();iRDS++) {
    
    Long64_t ientry = mc_RDS->LoadTree(iRDS);
    if (ientry < 0 ) break;
    nbRDS = mc_RDS->GetEntry(iRDS);   nbytesRDS += nbRDS;
    
    runNumber   = mc_RDS->eventSelectionrun;
    eventNumber = mc_RDS->eventSelectionevent;
    TLorentzVector tlj1(0,0,0,0);
    TLorentzVector tlj2(0,0,0,0);
    tlj1.SetPtEtaPhiM(mc_RDS->mebjet1pt, mc_RDS->mebjet1etapm, mc_RDS->mebjet1phi, mc_RDS->mebjet1mass);
    tlj2.SetPtEtaPhiM(mc_RDS->mebjet2pt, mc_RDS->mebjet2etapm, mc_RDS->mebjet2phi, mc_RDS->mebjet2mass);
    
    E_j1          = tlj1.E();
    E_j2          = tlj2.E();
    Eta_j1        = mc_RDS->mebjet1etapm;
    Eta_j2        = mc_RDS->mebjet2etapm;
    phi_j1        = mc_RDS->mebjet1phi;
    phi_j2        = mc_RDS->mebjet2phi;
    Pt_j1         = mc_RDS->mebjet1pt;
    Pt_j2         = mc_RDS->mebjet2pt;
    Mass_j1       = mc_RDS->mebjet1mass;
    Mass_j2       = mc_RDS->mebjet2mass;	
    
    deltaE_ajet   = mc_RDS->meDeltaE_ajet;
    deltaE_jet    = mc_RDS->meDeltaE_jet;
    deltaEta_ajet = mc_RDS->meDeltaEta_ajet;
    deltaEta_jet  = mc_RDS->meDeltaEta_jet;
    deltaPhi_ajet = mc_RDS->meDeltaphi_ajet;
    deltaPhi_jet  = mc_RDS->meDeltaphi_jet;
    
    btag_j1       = mc_RDS->jetmetbjet1CSVdisc;
    btag_j2       = mc_RDS->jetmetbjet2CSVdisc;
    
    if (isMuChannel)llM= mc_RDS->eventSelectionbestzmassMu;
    else            llM= mc_RDS->eventSelectionbestzmassEle;
    
    bbM           = mc_RDS->eventSelectiondijetM;

    if (isMuChannel){
      TLorentzVector tlm1(0,0,0,0);
      TLorentzVector tlm2(0,0,0,0);
      tlm1.SetPtEtaPhiM(mc_RDS->memu1pt, mc_RDS->memu1etapm, mc_RDS->memu1phi, mc_RDS->memu1mass);
      tlm2.SetPtEtaPhiM(mc_RDS->memu2pt, mc_RDS->memu2etapm, mc_RDS->memu2phi, mc_RDS->memu2mass);
      E_l1         = tlm1.E();
      E_l2         = tlm2.E();
      Eta_l1       = mc_RDS->memu1etapm;
      Eta_l2       = mc_RDS->memu2etapm;
      phi_l1       = mc_RDS->memu1phi;
      phi_l2       = mc_RDS->memu2phi;
      Pt_l1        = mc_RDS->memu1pt;
      Pt_l2        = mc_RDS->memu2pt;
      Mass_l1      = mc_RDS->memu1mass;
      Mass_l2      = mc_RDS->memu2mass;
      charge_l1    = mc_RDS->memu1charge;
      charge_l2    = mc_RDS->memu2charge;	
    }
    else {
      TLorentzVector tle1(0,0,0,0);
      TLorentzVector tle2(0,0,0,0);
      tle1.SetPtEtaPhiM(mc_RDS->meel1pt, mc_RDS->meel1etapm, mc_RDS->meel1phi, mc_RDS->meel1mass);
      tle2.SetPtEtaPhiM(mc_RDS->meel2pt, mc_RDS->meel2etapm, mc_RDS->meel2phi, mc_RDS->meel2mass);
      
      E_l1         = tle1.E();
      E_l2         = tle2.E();
      Eta_l1       = mc_RDS->meel1etapm;
      Eta_l2       = mc_RDS->meel2etapm;
      phi_l1       = mc_RDS->meel1phi;
      phi_l2       = mc_RDS->meel2phi;
      Pt_l1        = mc_RDS->meel1pt;
      Pt_l2        = mc_RDS->meel2pt;
      Mass_l1      = mc_RDS->meel1mass;
      Mass_l2      = mc_RDS->meel2mass;
      charge_l1    = mc_RDS->meel1charge;
      charge_l2    = mc_RDS->meel2charge;		
    }
			
    deltaElp      = mc_RDS->meDeltaE_lp;
    deltaElm      = mc_RDS->meDeltaE_lm;
    deltaEtalp    = mc_RDS->meDeltaEta_lp;
    deltaEtalm    = mc_RDS->meDeltaEta_lm; 
    deltaPhilp    = mc_RDS->meDeltaphi_lp;
    deltaPhilm    = mc_RDS->meDeltaphi_lm;
    deltaPtInvlp  = mc_RDS->meDeltaPtInv_lp;
    deltaPtInvlm  = mc_RDS->meDeltaPtInv_lm;
  
    DR_jet        = mc_RDS->eventSelectiondijetdR;
    
    Met           = mc_RDS->jetmetMET;
    Met_phi       = mc_RDS->jetmetMETphi;
    Met_sig       = mc_RDS->jetmetMETsignificance;
    
    
    int type      = mc_RDS->mcSelectioneventType;
    if (!IsDATA){
      if( type==3) {
	isZb= 1;
	isZc= 0;
	isZl= 0;
      }
      else if( type==2){
	isZb= 0;
	isZc= 1;
	isZl= 0;	
      }
      else if( type==1){
	isZb= 0;
	isZc= 0;
	isZl= 1;	
      }
      else {
	isZb= 0;
	isZc= 0;
	isZl= 0;	
      }
    }
    else {
      isZb= 0;
      isZc= 0;
      isZl= 0;	
    }                       

    if (!IsDATA)Pile_up       = mc_RDS->lumiReweightingpu;
    else        Pile_up       =0;
    
    nbr_PV        = mc_RDS->vertexAssociationnvertices;

    nJets         = mc_RDS->jetmetnj;
    nBjetsHE      = mc_RDS->jetmetnb;
    nBjetsHP      = mc_RDS->jetmetnj;
    nBjetsHEHP    = mc_RDS->jetmetnj;
	
    category      = mc_RDS->rc_eventSelection_10_idx;
	
    if (category == 1 && Met_sig < 10 &&  Met_sig!= 0){

      myfile2 <<"0 "<<eventNumber << " " <<runNumber << endl;
      if (isMuChannel){
	myfile2 <<"1  2 " <<setprecision(9) <<Eta_l1<<" " <<phi_l1<<" " <<Pt_l1<< " " <<Mass_l1<< " " <<charge_l1<<" 0 0 0 0" <<endl;
	myfile2 <<"2  2 " <<setprecision(9) <<Eta_l2<<" " <<phi_l2<<" " <<Pt_l2<< " " <<Mass_l2<< " " <<charge_l2<<" 0 0 0 0" <<endl;	 
      }
      else{
	myfile2 <<"1  1 " <<setprecision(9) <<Eta_l1<<" " <<phi_l1<<" " <<Pt_l1<< " " <<Mass_l1<< " " <<charge_l1<<" 0 0 0 0" <<endl;
	myfile2 <<"2  1 " <<setprecision(9) <<Eta_l2<<" " <<phi_l2<<" " <<Pt_l2<< " " <<Mass_l2<< " " <<charge_l2<<" 0 0 0 0" <<endl;	
      }
      myfile2 <<"3  4 " <<setprecision(9) <<Eta_j1<<" " <<phi_j1 <<" " <<Pt_j1<< " " <<Mass_j1<< " " <<"0"<<" 2 0 0 0" <<endl;
      myfile2 <<"4  4 " <<setprecision(9) <<Eta_j2<<" " <<phi_j2 <<" " <<Pt_j2<< " " <<Mass_j2<< " " <<"0"<<" 2 0 0 0" <<endl;
      myfile2 <<"5  6 " <<"0"   <<" " <<Met_phi<<" " <<Met  << " " <<"0 0 0 0 0 0" <<endl;
      
      t_RDSME->Fill();
    }
  }
  
  myfile2.close();
  f_RDSME->cd();
  t_RDSME->Write();
  
  delete mc_RDS;    
}

void Loop(){
  //CreateTree("DoubleMu_DataA");
  //CreateTree("DoubleEle_DataA");
  CreateTree("DY_El_MC");
  CreateTree("DY_Mu_MC");

  CreateTree("DY1j_El_MC");
  CreateTree("DY1j_Mu_MC");
  CreateTree("DY2j_El_MC");
  CreateTree("DY2j_Mu_MC");
  CreateTree("DY3j_El_MC");
  CreateTree("DY3j_Mu_MC");
  CreateTree("DY4j_El_MC");
  CreateTree("DY4j_Mu_MC");
  CreateTree("DY50-70_El_MC");
  CreateTree("DY50-70_Mu_MC");
  CreateTree("DY70-100_El_MC");
  CreateTree("DY70-100_Mu_MC");
  CreateTree("DY100_El_MC");
  CreateTree("DY100_Mu_MC");
  CreateTree("DY180_El_MC");
  CreateTree("DY180_Mu_MC");

  CreateTree("TT-FullLept_El_MC");
  CreateTree("TT-FullLept_Mu_MC");

  //CreateTree("TT_El_MC");
  //CreateTree("TT_Mu_MC");
  CreateTree("ZZ_El_MC");
  CreateTree("ZZ_Mu_MC");
  CreateTree("ZH110_El_MC");
  CreateTree("ZH110_Mu_MC");
  CreateTree("ZH115_El_MC");
  CreateTree("ZH115_Mu_MC");
  CreateTree("ZH120_El_MC");
  CreateTree("ZH120_Mu_MC");
  CreateTree("ZH125_El_MC");
  CreateTree("ZH125_Mu_MC");
  CreateTree("ZH130_El_MC");
  CreateTree("ZH130_Mu_MC");
  CreateTree("ZH135_El_MC");
  CreateTree("ZH135_Mu_MC");
  CreateTree("ZH140_El_MC");
  CreateTree("ZH140_Mu_MC");
  CreateTree("ZH145_El_MC");
  CreateTree("ZH145_Mu_MC");
  CreateTree("ZH150_El_MC");
  CreateTree("ZH150_Mu_MC");
}
