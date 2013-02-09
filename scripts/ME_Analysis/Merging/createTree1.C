#include "TTree.h"
#include "TFile.h"
#include "TRandom.h"
#include "TTree.h"
//#include "RooDataSet.h"
#include "rds_zbb.C"


#include <iostream>
#include <fstream>

using namespace std;

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

  double llM;
  double bbM;


  double E_mu1;
  double E_mu2;
  double Eta_mu1;
  double Eta_mu2;
  double phi_mu1;
  double phi_mu2;
  double Pt_mu1;
  double Pt_mu2;
  double Mass_mu1;
  double Mass_mu2; 
  double charge_mu1;
  double charge_mu2; 
    
  double E_el1;
  double E_el2;
  double Eta_el1;
  double Eta_el2;
  double phi_el1;
  double phi_el2;
  double Pt_el1;
  double Pt_el2;  
  double Mass_el1;
  double Mass_el2; 
  double charge_el1;
  double charge_el2;
     
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
     std::cout << "InputFile name cannot contain both <<Mu_>> and <<El_>>" << std::endl;
     return;
   }
   
   else if (InputFile.Contains("Mu_") || InputFile.Contains("MuA_") || InputFile.Contains("MuB_")) {
     std::cout << "  running MuMu channel" << std::endl;
     isMuChannel = true;
   }
   
   else if (InputFile.Contains("El_") || InputFile.Contains("ElA_") || InputFile.Contains("ElB_")) {
     std::cout << "  running over ElEl channel" << std::endl;
   }
   
   else {
     std::cout << "InputFile name must contain <<Mu_>> or <<El_>>" << std::endl;
     return;

   }
   
   bool IsDATA = InputFile.Contains("DATA");
      
   TFile* f_RDS  = new TFile(InputFile);
   TTree* t_RDS    = (TTree*)f_RDS->Get("rds_zbb");  


   rds_zbb* mc_RDS = new rds_zbb(t_RDS);
   
   TFile *f_RDSME = new TFile("test.root", "RECREATE");
   TTree *t_RDSME = new TTree("rds_zbb", "tree 1");   
   
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

   t_RDSME->Branch("llM",&llM,"llM/D");
   t_RDSME->Branch("bbM",&bbM,"bbM/D");
  

   t_RDSME->Branch("E_mu1",&E_mu1,"E_mu1/D");
   t_RDSME->Branch("E_mu2",&E_mu2,"E_mu2/D");
   t_RDSME->Branch("Eta_mu1",&Eta_mu1,"Eta_mu1/D");
   t_RDSME->Branch("Eta_mu2",&Eta_mu2,"Eta_mu2/D");
   t_RDSME->Branch("phi_mu1",&phi_mu1,"phi_mu1/D");
   t_RDSME->Branch("phi_mu2",&phi_mu2,"phi_mu2/D");
   t_RDSME->Branch("Pt_mu1",&Pt_mu1,"Pt_mu1/D");
   t_RDSME->Branch("Pt_mu2",&Pt_mu2,"Pt_mu2/D");
   t_RDSME->Branch("Mass_mu1",&Mass_mu1,"Mass_mu1/D");
   t_RDSME->Branch("Mass_mu2",&Mass_mu2,"Mass_mu2/D");  
   t_RDSME->Branch("charge_mu1",&charge_mu1,"charge_mu1/D");
   t_RDSME->Branch("charge_mu2",&charge_mu2,"charge_mu2/D");
        
   t_RDSME->Branch("E_el1",&E_el1,"E_el1/D");
   t_RDSME->Branch("E_el2",&E_el2,"E_el2/D");
   t_RDSME->Branch("Eta_el1",&Eta_el1,"Eta_el1/D");
   t_RDSME->Branch("Eta_el2",&Eta_el2,"Eta_el2/D");
   t_RDSME->Branch("phi_el1",&phi_el1,"phi_el1/D");
   t_RDSME->Branch("phi_el2",&phi_el2,"phi_el2/D");
   t_RDSME->Branch("Pt_el1",&Pt_el1,"Pt_el1/D");
   t_RDSME->Branch("Pt_el2",&Pt_el2,"Pt_el2/D");   
   t_RDSME->Branch("Mass_el1",&Mass_el1,"Mass_el1/D");
   t_RDSME->Branch("Mass_el2",&Mass_el2,"Mass_el2/D"); 
   t_RDSME->Branch("charge_el1",&charge_el1,"charge_el1/D");
   t_RDSME->Branch("charge_el2",&charge_el2,"charge_el2/D");
         
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
   t_RDSME->Branch("nBjetsHE", &nBjetsHE, "nBjetsHE/I");
   t_RDSME->Branch("nBjetsHP", &nBjetsHP, "nBjetsHP/I");
   t_RDSME->Branch("nBjetsHEHP", &nBjetsHEHP, "nBjetsHEHP/I"); 
   
   t_RDSME->Branch("category", &category, "category/I"); 
   
   Long64_t nbytesRDS = 0, nbRDS = 0;
   for (Int_t iRDS=0;iRDS<t_RDS->GetEntries();iRDS++) {

      Long64_t ientry = mc_RDS->LoadTree(iRDS);
      if (ientry < 0 ) break;
      nbRDS = mc_RDS->GetEntry(iRDS);   nbytesRDS += nbRDS;
      
      
        runNumber   = mc_RDS->eventSelectionrun;
        eventNumber = mc_RDS->eventSelectionevent;

        E_j1          = mc_RDS->jetmetjet1energy;
        E_j2          = mc_RDS->jetmetjet1energy;
        Eta_j1        = mc_RDS->jetmetjet1eta;
        Eta_j2        = mc_RDS->jetmetjet2eta;
        phi_j1        = mc_RDS->jetmetjet1phi;
        phi_j2        = mc_RDS->jetmetjet2phi;
        Pt_j1         = mc_RDS->jetmetjet1pt;
	Pt_j2         = mc_RDS->jetmetjet2pt;
        Mass_j1       = mc_RDS->jetmetjet1mass;
	Mass_j2       = mc_RDS->jetmetjet2mass;	
	
        btag_j1       = mc_RDS->jetmetbjet1CSVdisc;
        btag_j2       = mc_RDS->jetmetbjet2CSVdisc;

        if (isMuChannel)llM= mc_RDS->eventSelectionbestzmassMu;
	else            llM= mc_RDS->eventSelectionbestzmassEle;
	
        bbM           = mc_RDS->eventSelectiondijetM;


        E_el1         =0;
        E_el2         =0;
        Eta_el1       = mc_RDS->eventSelectionel1eta;
        Eta_el2       = mc_RDS->eventSelectionel2eta;
        phi_el1       = mc_RDS->eventSelectionel1phi;
        phi_el2       = mc_RDS->eventSelectionel1phi;
        Pt_el1        = mc_RDS->eventSelectionel1ptME;
        Pt_el2        = mc_RDS->eventSelectionel2ptME;
        Mass_el1      = mc_RDS->eventSelectionel1mass;
        Mass_el2      = mc_RDS->eventSelectionel2mass;
        charge_el1    = mc_RDS->eventSelectionel1charge;
        charge_el2    = mc_RDS->eventSelectionel2charge;		
	
        E_mu1         = 0;
        E_mu2         = 0;
        Eta_mu1       = mc_RDS->eventSelectionmu1eta;
        Eta_mu2       = mc_RDS->eventSelectionmu2eta;
        phi_mu1       = mc_RDS->eventSelectionmu1phi;
        phi_mu2       = mc_RDS->eventSelectionmu1phi;
        Pt_mu1        = mc_RDS->eventSelectionmu1ptME;
        Pt_mu2        = mc_RDS->eventSelectionmu2ptME;
        Mass_mu1      = mc_RDS->eventSelectionmu1mass;
        Mass_mu2      = mc_RDS->eventSelectionmu2mass;
        charge_mu1    = mc_RDS->eventSelectionmu1charge;
        charge_mu2    = mc_RDS->eventSelectionmu2charge;	
			
	
        DR_jet        = mc_RDS->eventSelectiondijetdR;

        Met           = mc_RDS->jetmetMET_ME;
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
	
	
        category      = mc_RDS->rc_eventSelection_11_idx;
	
	ofstream myfile2;
	
	if (category == 1 && Met_sig < 10 &&  Met_sig!= 0){
	
	  myfile2.open ("dumpEvents.txt",ios::app);
	  myfile2 <<"0 "<<runNumber << " " <<eventNumber << endl;
	  if (isMuChannel){
	    myfile2 <<"1  2 " <<Eta_mu1<<" " <<phi_mu1<<" " <<Pt_mu1<< " " <<Mass_mu1<< " " <<charge_mu1<<" 0 0 0 0" <<endl;
	    myfile2 <<"2  2 " <<Eta_mu2<<" " <<phi_mu2<<" " <<Pt_mu2<< " " <<Mass_mu2<< " " <<charge_mu2<<" 0 0 0 0" <<endl;	 
	  }
	  else{
	    myfile2 <<cout <<"1  1 " <<Eta_el1<<" " <<phi_el1<<" " <<Pt_el1<< " " <<Mass_el1<< " " <<charge_el1<<" 0 0 0 0" <<endl;
	    myfile2 <<cout <<"2  1 " <<Eta_el2<<" " <<phi_el2<<" " <<Pt_el2<< " " <<Mass_el2<< " " <<charge_el2<<" 0 0 0 0" <<endl;	
	  }
	  myfile2 <<"3  4 " <<Eta_j1<<" " <<phi_j1 <<" " <<Pt_j1<< " " <<Mass_j1<< " " <<"0"<<" 2 0 0 0" <<endl;
	  myfile2 <<"4  4 " <<Eta_j2<<" " <<phi_j2 <<" " <<Pt_j2<< " " <<Mass_j2<< " " <<"0"<<" 2 0 0 0" <<endl;
	  myfile2 <<"5  6 " <<"0"   <<" " <<Met_phi<<" " <<Met  << " " <<"0 0 0 0 0 0" <<endl;
	  
	  myfile2.close();
	}
	
	
        t_RDSME->Fill();
	
	}

      f_RDSME->cd();
      t_RDSME->Write();
   
      delete mc_RDS;
      
      
}
