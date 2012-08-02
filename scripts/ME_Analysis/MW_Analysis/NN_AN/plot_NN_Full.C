/*
 *  Neural_net.cpp
 *  
 *
 *  Created by Arnaud Pin on 13/11/10.
 *  Copyright 2010 __CP3__. All rights reserved.
 *
 */

using namespace std;
#include "include.h"

//#include "NN_tt_aMC_1000_tight.cxx"
//#include "../NN/MLP_Zbb_vs_tt_Muon_Delphes_341_c.cxx"
//#include "../NN/MLP_Zbb_vs_tt_Muon_Delphes_5_input_weights.cxx"
#include "../NN/MLP_Zbb_vs_tt_Muon_Delphes_3_input_weights_Met.cxx"


void Control_NN(const char *DY_file,const char *tt_file,const char *ZZ_file,const char *Data_file)
{

	!gROOT->GetClass("MLP_Zbb_vs_tt_Muon_Delphes_3_input_weights_Met");
	MLP_Zbb_vs_tt_Muon_Delphes_3_input_weights_Met *mlp=new MLP_Zbb_vs_tt_Muon_Delphes_3_input_weights_Met();
	if (!gROOT->GetClass("TMultiLayerPerceptron")) {
		gSystem->Load("libMLP");
	}
	// Canvas declaration
	TCanvas* mlpa_canvas = new TCanvas("mlpa_canvas","Network analysis");
	mlpa_canvas->Divide(4,2);
	TCanvas* mlpb_canvas = new TCanvas("mlpb_canvas","Network analysis");
	mlpb_canvas->Divide(3,4);
	TCanvas* mlpc_canvas = new TCanvas("mlpc_canvas","Network analysis");
	mlpc_canvas->Divide(3,3);
	TCanvas* mlpd_canvas = new TCanvas("mlpd_canvas","Network analysis");
	mlpd_canvas->Divide(2,2);	
	TCanvas* mlpe_canvas = new TCanvas("mlpe_canvas","Network analysis");
	mlpe_canvas->Divide(2,2);
		
	// Histo init
	TH1F *bg = new TH1F("bgh", "NN output", 30, -1.0, 2.0);
	TH1F *sigb = new TH1F("sighb", "NN output", 30, -1.0, 2.0);	
	TH1F *sigc = new TH1F("sighc", "NN output", 30, -1.0, 2.0);
	TH1F *sigl = new TH1F("sighl", "NN output", 30, -1.0, 2.0);

	TH2F *higgs = new TH2F("higgs","higgs",20,20,40,20,10,30);
        TH2F *zbbbb = new TH2F("zbbbb","zbbbb",20,20,40,20,10,30);



	TH1F *sigall = new TH1F("sigall", "NN output", 30, -1.0, 2.0);

	TH1F *zz = new TH1F("zz", "NN output", 30, -1.0, 2.0);	
	TH1F *data = new TH1F("data", "NN output1", 30, -1.0, 2.0);	

	TH1F *bg2 = new TH1F("bgh2", "NN output2", 150, -.5, 1.5);
	TH1F *sigb2 = new TH1F("sigh2b", "NN output2", 150, -.5, 1.5);
	TH1F *sigl2 = new TH1F("sigh2c", "NN output2", 150, -.5, 1.5);
	TH1F *sigc2 = new TH1F("sigh2l", "NN output2", 150, -.5, 1.5);
	TH1F *zz2 = new TH1F("zz2", "NN output2", 150, -.5, 1.5);
	TH1F *data2 = new TH1F("data2", "NN output2", 150, -.5, 1.5);


	// Z_bb HISTO
	TH1F *Mll_zbb = new TH1F("Mll_zbb", "Mll_zbb", 30,76,106);			// M inv lept
 	TH1F *wqq2_zbb_b = new TH1F("wqq_zbb_b", "wqq_zbb", 24,16,30);			// WEIGHT
	TH1F *wqq2_zbb_c = new TH1F("wqq_zbb_c", "wqq_zbb", 24,16,30);                       // WEIGHT                                                         
	TH1F *wqq2_zbb_l = new TH1F("wqq_zbb_l", "wqq_zbb", 24,16,30);                       // WEIGHT     
	TH1F *wqq_zbb = new TH1F("wqq2_zbb", "wqq2_zbb", 24,16,30);
	TH1F *wgg2_zbb_b = new TH1F("wgg_zbb_b", "wgg_zbb", 24,16,30);
	TH1F *wgg2_zbb_c = new TH1F("wgg_zbb_c", "wgg_zbb", 24,16,30);
	TH1F *wgg2_zbb_l = new TH1F("wgg_zbb_l", "wgg_zbb", 24,16,30);	
	TH1F *wgg_zbb = new TH1F("wgg2_zbb", "wgg2_zbb", 24,16,30);
	TH1F *wtt2_zbb_b = new TH1F("wtt_zbb_b", "wtt_zbb", 24,16,30);	
	TH1F *wtt2_zbb_c = new TH1F("wtt_zbb_c", "wtt_zbb", 24,16,30);
	TH1F *wtt2_zbb_l = new TH1F("wtt_zbb_l", "wtt_zbb", 24,16,30);
	TH1F *wtt_zbb = new TH1F("wtt2_zbb", "wtt2_zbb", 24,16,30);

	TH1F *dwgg_zbb_b = new TH1F("dwgg_zbb", "dwgg_zbb", 20,20.0,40);
	TH1F *dwqq_zbb_b = new TH1F("dwqq_zbb", "dwqq_zbb", 20,10.0,30);
	TH1F *dwgg_zbb_c = new TH1F("dwgg_zbb", "dwgg_zbb", 20,20.0,40);
	TH1F *dwqq_zbb_c = new TH1F("dwqq_zbb", "dwqq_zbb", 20,10.0,30);
	TH1F *dwgg_zbb_l = new TH1F("dwgg_zbb", "dwgg_zbb", 20,20.0,40);
	TH1F *dwqq_zbb_l = new TH1F("dwqq_zbb", "dwqq_zbb", 20,10.0,30);	

	TH1F *dwggs_zbb_b = new TH1F("dwggs_zbb", "dwggs_zbb", 20,16.0,28);
	TH1F *dwqqs_zbb_b = new TH1F("dwqqs_zbb", "dwqqs_zbb", 20,8.0,20);
        TH1F *dwggs_zbb_c = new TH1F("dwggs_zbb", "dwggs_zbb", 20,16.0,28);
        TH1F *dwqqs_zbb_c = new TH1F("dwqqs_zbb", "dwqqs_zbb", 20,8.0,20);
        TH1F *dwggs_zbb_l = new TH1F("dwggs_zbb", "dwggs_zbb", 20,16.0,28);
        TH1F *dwqqs_zbb_l = new TH1F("dwqqs_zbb", "dwqqs_zbb", 20,8.0,20);

	// ttbar HISTO
	TH1F *Mll_tt = new TH1F("Mll_tt", "Mll_tt", 30,76,106);			// M inv lept
	TH1F *wqq_tt = new TH1F("wqq_tt", "wqq_tt", 24,16,30);			// WEIGHT
	TH1F *wqq2_tt = new TH1F("wqq2_tt", "wqq2_tt", 24,16,30);
	TH1F *wgg_tt = new TH1F("wgg_tt", "wgg_tt", 24,16,30);	
	TH1F *wgg2_tt = new TH1F("wgg2_tt", "wgg2_tt", 24,16,30);
	TH1F *wtt_tt = new TH1F("wtt_tt", "wtt_tt", 24,16,30);	
	TH1F *wtt2_tt = new TH1F("wtt2_tt", "wtt2_tt", 24,16,30);
        TH1F *dwgg_tt = new TH1F("dwgg_tt", "dwgg_tt", 20,20.0,40);
        TH1F *dwqq_tt = new TH1F("dwqq_tt", "dwqq_tt", 20,10.0,30);
        TH1F *dwggs_tt = new TH1F("dwggs_tt", "dwggs_tt", 20,16,28);
        TH1F *dwqqs_tt = new TH1F("dwqqs_tt", "dwqqs_tt", 20,8,20);



	// ZZ HISTO
	TH1F *Mll_zz = new TH1F("Mll_zz", "Mll_zz", 30,76,106);			// M inv lept
	TH1F *wqq_zz = new TH1F("wqq_zz", "wqq_zz", 24,16,30);			// WEIGHT
	TH1F *wqq2_zz = new TH1F("wqq2_zz", "wqq2_zz",24,16,30);
	TH1F *wgg_zz = new TH1F("wgg_zz", "wgg_zz", 24,16,30);	
	TH1F *wgg2_zz = new TH1F("wgg2_zz", "wgg2_zz", 24,16,30);
	TH1F *wtt_zz = new TH1F("wtt_zz", "wtt_zz", 24,16,30);	
	TH1F *wtt2_zz = new TH1F("wtt2_zz", "wtt2_zz", 24,16,30);
	TH1F *dwgg_zz = new TH1F("dwgg_zz", "dwgg_zz", 20,20.0,40);
        TH1F *dwqq_zz = new TH1F("dwqq_zz", "dwqq_zz", 20,10.0,30);
        TH1F *dwggs_zz = new TH1F("dwggs_zz", "dwggs_zz", 20,16,28);
        TH1F *dwqqs_zz = new TH1F("dwqqs_zz", "dwqqs_zz", 20,8,20);



	// DATA HISTO
	TH1F *Mll_data = new TH1F("Mll_data", "Mll_data", 30,76,106);			// M inv lept
	TH1F *wqq_data = new TH1F("wqq_data", "wqq_data", 24,16,30);			// WEIGHT
	TH1F *wqq2_data = new TH1F("wqq2_data", "wqq2_data",24,16,30);
	TH1F *wgg_data = new TH1F("wgg_data", "wgg_data", 24,16,30);	
	TH1F *wgg2_data = new TH1F("wgg2_data", "wgg2_data", 24,16,30);
	TH1F *wtt_data = new TH1F("wtt_data", "wtt_data", 24,16,30);	
	TH1F *wtt2_data = new TH1F("wtt2_data", "wtt2_data", 24,16,30);
        TH1F *dwgg_data = new TH1F("dwgg_data", "dwgg_data", 20,20.0,40);
        TH1F *dwqq_data = new TH1F("dwqq_data", "dwqq_data", 20,10.0,30);
        TH1F *dwggs_data = new TH1F("dwggs_data", "dwggs_data", 20,16,28);
        TH1F *dwqqs_data = new TH1F("dwqqs_data", "dwqqs_data", 20,8,20);

//------------------------------------------------------------------------------------------------------------------------------------
	
		
	TFile file("Control_ee_test_444_tight_selection_MetDATA.root","RECREATE");
	//-------------------------------------------------------
	//-------------------------- DY ----------------------------------------
	TChain *chain_zbb;
	TChain *tree_zbb = new TChain("tree2");
	tree_zbb->Reset();
	tree_zbb->Add(DY_file);
	double MET_zbb,MeT_zbb,MeTPhi_zbb,Inv_Mass_lept_zbb,inMass_zbb,Inv_Mass_bb_zbb,inMassbb_zbb;
	double Wqq_zbb,Wgg_zbb,Wtt_zbb, Whi3_zbb,Whi0_zbb,Wzz3_zbb,Wzz0_zbb;
	int flavour;
	double E_j1_zbb,E_j2_zbb,Eta_j1_zbb,Eta_j2_zbb,Phi_j1_zbb,Phi_j2_zbb,Pt_j1_zbb,Pt_j2_zbb;
	double Pt_elplus_zbb,Eta_elplus_zbb,Phi_elplus_zbb,Pt_elminus_zbb,Eta_elminus_zbb,Phi_elminus_zbb;
        tree_zbb->SetBranchAddress("MeT",&MeT_zbb);
	tree_zbb->SetBranchAddress("flavour",&flavour);
	tree_zbb->SetBranchAddress("Inv_Mass_lept",&Inv_Mass_lept_zbb);
	tree_zbb->SetBranchAddress("Wqq",&Wqq_zbb);
	tree_zbb->SetBranchAddress("Wgg",&Wgg_zbb);
	tree_zbb->SetBranchAddress("Wtt",&Wtt_zbb);
        tree_zbb->SetBranchAddress("Whi0",&Whi0_zbb);
        tree_zbb->SetBranchAddress("Whi3",&Whi3_zbb);
        tree_zbb->SetBranchAddress("Wzz0",&Wzz0_zbb);
        tree_zbb->SetBranchAddress("Wzz3",&Wzz3_zbb);
   sigb->SetDirectory(0);
   Double_t params[8];
   for (int i=0;i<824; ++i) {
     tree_zbb->GetEntry(i);
	 if(Inv_Mass_lept_zbb > 76 && Inv_Mass_lept_zbb <106 && MeT_zbb <50){
     MET_zbb = MeT_zbb;
     inMass_zbb=Inv_Mass_lept_zbb;
     //------------------------------------- input of NN
     params[0] = Wgg_zbb;         
     params[1] = Wqq_zbb;                                                                                                      
     params[2] = Wtt_zbb;
     params[3] = MET_zbb;
      if(params[0]>300.0){params[0]=666;}
      if(params[1]>300.0){params[1]=666;}
      if(params[2]>300.0){params[2]=666;}	
      double MLP;
      cout<<flavour<<" "<<Wgg_zbb<<" "<< Wqq_zbb<<" "<<Wtt_zbb<<" "<<MET_zbb<<endl;
      if(flavour==2){if(mlp->Value(0,params)<1.0){sigb->Fill(mlp->Value(0,params));};if(mlp->Value(0,params)>1.0){sigb->Fill(1.0);}}
      if(flavour==1){if(mlp->Value(0,params)<1.0){sigc->Fill(mlp->Value(0,params));};if(mlp->Value(0,params)>1.0){sigc->Fill(1.0);}}
      if(flavour==0){if(mlp->Value(0,params)<1.0){sigl->Fill(mlp->Value(0,params));};if(mlp->Value(0,params)>1.0){sigl->Fill(1.0);}}
      if(flavour==2){if(mlp->Value(0,params)<1.0){sigb2->Fill(mlp->Value(0,params));};if(mlp->Value(0,params)>1.0){sigb2->Fill(1.0);}}
      if(flavour==1){if(mlp->Value(0,params)<1.0){sigc2->Fill(mlp->Value(0,params));};if(mlp->Value(0,params)>1.0){sigc2->Fill(1.0);}}
      if(flavour==0){if(mlp->Value(0,params)<1.0){sigl2->Fill(mlp->Value(0,params));};if(mlp->Value(0,params)>1.0){sigl2->Fill(1.0);}}
      sigall->Fill(mlp->Value(0,params));
      double tmp_val=mlp->Value(0,params);
      //-----------------
      if(flavour==2){wgg2_zbb_b->Fill(params[0]);}
      if(flavour==1){wgg2_zbb_c->Fill(params[0]);}
      if(flavour==0){wgg2_zbb_l->Fill(params[0]);}
      if(flavour==2){wqq2_zbb_b->Fill(params[1]);}
      if(flavour==1){wqq2_zbb_c->Fill(params[1]);}
      if(flavour==0){wqq2_zbb_l->Fill(params[1]);}
      if(flavour==2){wtt2_zbb_b->Fill(params[2]);}
      if(flavour==1){wtt2_zbb_c->Fill(params[2]);}
      if(flavour==0){wtt2_zbb_l->Fill(params[2]);}

      if(flavour==2){dwgg_zbb_b->Fill(Whi0_zbb);}
      if(flavour==1){dwgg_zbb_c->Fill(Whi0_zbb);}
      if(flavour==0){dwgg_zbb_l->Fill(Whi0_zbb);}
      if(flavour==2){dwqq_zbb_b->Fill(Whi3_zbb);}
      if(flavour==1){dwqq_zbb_c->Fill(Whi3_zbb);}
      if(flavour==0){dwqq_zbb_l->Fill(Whi3_zbb);}

      if(flavour==2){dwggs_zbb_b->Fill(Wzz0_zbb);}
      if(flavour==1){dwggs_zbb_c->Fill(Wzz0_zbb);}
      if(flavour==0){dwggs_zbb_l->Fill(Wzz0_zbb);}
      if(flavour==2){dwqqs_zbb_b->Fill(Wzz3_zbb);}
      if(flavour==1){dwqqs_zbb_c->Fill(Wzz3_zbb);}
      if(flavour==0){dwqqs_zbb_l->Fill(Wzz3_zbb);}

      if(flavour==2){zbbbb->Fill(Whi0_zbb,Whi3_zbb);}
	}
   }


//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------- TT ----------------------------------------

	TChain *chain_tt;
	TChain *tree_tt = new TChain("tree2");
	tree_tt->Reset();
	tree_tt->Add(tt_file);
	double MET_tt,MeT_tt,MeTPhi_tt,Inv_Mass_lept_tt,inMass_tt,Inv_Mass_bb_tt,inMassbb_tt;
	double Wqq_tt,Wgg_tt,Wtt_tt, Whi3_tt,Whi0_tt,Wzz3_tt,Wzz0_tt;
	double E_j1_tt,E_j2_tt,Eta_j1_tt,Eta_j2_tt,Phi_j1_tt,Phi_j2_tt,Pt_j1_tt,Pt_j2_tt;
	double Pt_elplus_tt,Eta_elplus_tt,Phi_elplus_tt,Pt_elminus_tt,Eta_elminus_tt,Phi_elminus_tt;
	tree_tt->SetBranchAddress("MeT",&MeT_tt);
	tree_tt->SetBranchAddress("Inv_Mass_lept",&Inv_Mass_lept_tt);
	tree_tt->SetBranchAddress("Wqq",&Wqq_tt);
	tree_tt->SetBranchAddress("Wgg",&Wgg_tt);
	tree_tt->SetBranchAddress("Wtt",&Wtt_tt);
	tree_tt->SetBranchAddress("Whi0",&Whi0_tt);
	tree_tt->SetBranchAddress("Whi3",&Whi3_tt);
        tree_tt->SetBranchAddress("Wzz0",&Wzz0_tt);
        tree_tt->SetBranchAddress("Wzz3",&Wzz3_tt);
       	bg->SetDirectory(0);
	for (int i=0;i<31029; ++i) {
	  tree_tt->GetEntry(i);
	  if(Inv_Mass_lept_tt > 76 && Inv_Mass_lept_tt <106 && MeT_tt <50){
	  MET_tt = MeT_tt;
	  params[0] = Wgg_tt;
	  params[1] = Wqq_tt;
	  params[2] = Wtt_tt;             
	  params[3] = MET_tt;
	  if(params[0]>300.0){params[0]=666;}
	  if(params[1]>300.0){params[1]=666;
	  cout<<"Wqq ttbar To LOW5051"<<endl;
	  }	
	  if(params[2]>300.0){params[2]=666;}
		if(mlp->Value(0,params)<1.0){bg->Fill(mlp->Value(0,params));}if(mlp->Value(0,params)>1.0){bg->Fill(1.0);}
	  if(mlp->Value(0,params)<1.0){bg2->Fill(mlp->Value(0,params));}if(mlp->Value(0,params)>1.0){bg2->Fill(1.0);}
	  //-----------------
	  wgg2_tt->Fill(params[0]);
	  wqq2_tt->Fill(params[1]);
	  wtt2_tt->Fill(params[2]);
	  dwgg_tt->Fill(Whi0_tt);
	  dwqq_tt->Fill(Whi3_tt);
	  dwggs_tt->Fill(Wzz0_tt);
	  dwqqs_tt->Fill(Wzz3_tt);
	  }
	}
   
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------   
   //--------------- ZZ-----------
   TChain *chain_zz;
	TChain *tree_zz = new TChain("tree2");
	tree_zz->Reset();
	tree_zz->Add(ZZ_file);
	double MET_zz,MeT_zz,MeTPhi_zz,Inv_Mass_lept_zz,inMass_zz,Inv_Mass_bb_zz,inMassbb_zz;
	double Wqq_zz,Wgg_zz,Wtt_zz, Whi3_zz,Whi0_zz,Wzz3_zz,Wzz0_zz;
	double E_j1_zz,E_j2_zz,Eta_j1_zz,Eta_j2_zz,Phi_j1_zz,Phi_j2_zz,Pt_j1_zz,Pt_j2_zz;
	double Pt_elplus_zz,Eta_elplus_zz,Phi_elplus_zz,Pt_elminus_zz,Eta_elminus_zz,Phi_elminus_zz;
	tree_zz->SetBranchAddress("MeT",&MeT_zz);
	tree_zz->SetBranchAddress("Inv_Mass_lept",&Inv_Mass_lept_zz);
	tree_zz->SetBranchAddress("Wqq",&Wqq_zz);
	tree_zz->SetBranchAddress("Wgg",&Wgg_zz);
	tree_zz->SetBranchAddress("Wtt",&Wtt_zz);
        tree_zz->SetBranchAddress("Whi0",&Whi0_zz);
        tree_zz->SetBranchAddress("Whi3",&Whi3_zz);
        tree_zz->SetBranchAddress("Wzz0",&Wzz0_zz);
        tree_zz->SetBranchAddress("Wzz3",&Wzz3_zz);
	for (int i=0;i<1374; ++i) {
          tree_zz->GetEntry(i);
		  	 if(Inv_Mass_lept_zz > 76 && Inv_Mass_lept_zz <106 && MeT_zz <50){
          MET_zz = MeT_zz;
	    params[0] = Wgg_zz;                         
	    params[1] = Wqq_zz;                        
	    params[2] = Wtt_zz;                                                                                     
	    params[3] = MET_zz;
	  if(params[0]>300.0){params[0]=666;}
	  if(params[1]>300.0){params[1]=666;}	
	  if(params[2]>300.0){params[2]=666;}
	  if(mlp->Value(0,params)<1.0){zz->Fill(mlp->Value(0,params));}if(mlp->Value(0,params)>1.0){zz->Fill(1.0);}
	  if(mlp->Value(0,params)<1.0){zz2->Fill(mlp->Value(0,params));}if(mlp->Value(0,params)>1.0){zz2->Fill(1.0);}
	  wgg2_zz->Fill(params[0]);
	  wqq2_zz->Fill(params[1]);
	  wtt2_zz->Fill(params[2]);
          dwgg_zz->Fill(Whi0_zz);
          dwqq_zz->Fill(Whi3_zz);
          dwggs_zz->Fill(Wzz0_zz);
          dwqqs_zz->Fill(Wzz3_zz);
		  }
	}
  
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    //-------------------------- DATA ----------------------------------------
	TChain *chain_data;
	TChain *tree_data = new TChain("tree2");
	tree_data->Reset();
	tree_data->Add(Data_file);
	double MET_data,MeT_data,MeTPhi_data,Inv_Mass_lept_data,inMass_data,Inv_Mass_bb_data,inMassbb_data;
	double Wqq_data,Wgg_data,Wtt_data, Whi3_data,Whi0_data,Wzz3_data,Wzz0_data;
	double E_j1_data,E_j2_data,Eta_j1_data,Eta_j2_data,Phi_j1_data,Phi_j2_data,Pt_j1_data,Pt_j2_data;
	double Pt_elplus_data,Eta_elplus_data,Phi_elplus_data,Pt_elminus_data,Eta_elminus_data,Phi_elminus_data;
	tree_data->SetBranchAddress("MeT",&MeT_data);
	tree_data->SetBranchAddress("Inv_Mass_lept",&Inv_Mass_lept_data);
	tree_data->SetBranchAddress("Wgg",&Wgg_data);
	tree_data->SetBranchAddress("Wqq",&Wqq_data);
	tree_data->SetBranchAddress("Wtt",&Wtt_data);
        tree_data->SetBranchAddress("Whi0",&Whi0_data);
        tree_data->SetBranchAddress("Whi3",&Whi3_data);
        tree_data->SetBranchAddress("Wzz0",&Wzz0_data);
        tree_data->SetBranchAddress("Wzz3",&Wzz3_data);
	for (int i=0;i<709; ++i) {
	  tree_data->GetEntry(i);
	  if(Inv_Mass_lept_data > 76 && Inv_Mass_lept_data <106 && MeT_data <50){
	  MET_data = MeT_data;
	  params[0] = Wgg_data;                                                                                                                                                                         
	  params[1] = Wqq_data;                                                                                                                                                                         
	  params[2] = Wtt_data;                                                                                                                                                                        
	  params[3] = MET_data;
	  if(params[0]>300.0){params[0]=666;}
	  if(params[1]>300.0){params[1]=666;}	
	  if(params[2]>300.0){params[2]=666;}
	  if(mlp->Value(0,params)<1.0){data->Fill(mlp->Value(0,params));}if(mlp->Value(0,params)>1.0){data->Fill(1.0);}
	  wgg2_data->Fill(params[0]);
	  wqq2_data->Fill(params[1]);
	  wtt2_data->Fill(params[2]);
          dwgg_data->Fill(Whi0_data);
          dwqq_data->Fill(Whi3_data);
          dwggs_data->Fill(Wzz0_data);
          dwqqs_data->Fill(Wzz3_data);
	  higgs->Fill(Whi0_data,Whi3_data);
	}
	}
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
	
	cout<<"  ************************************************************* "<<endl;
	cout<<"  *															 * "<<endl;
	cout<<"  *   dddd		rrrrr      aaaaaa  wwwww            wwwww	 * "<<endl;
	cout<<"  *   dd  dd		rr  rrr    a    a    ww      w       ww		 * "<<endl;
	cout<<"  *   dd   dd	rrrrr      aaaaaa     ww    wwww    ww		 * "<<endl;
	cout<<"  *   dd  dd		rr  rr	   a    a      ww  ww  ww  ww		 * "<<endl;	
	cout<<"  *   ddddd		rr   rr    a    a       wwww    wwww		 * "<<endl;
	cout<<"  *															 * "<<endl;
	cout<<"  ************************************************************* "<<endl;

	//	TFile file2("Electron_out.root","RECREATE");
	bg->Write();

	TH1F *sigsum = new TH1F("sigsum", "NN output", 30, -1.0, 2.0);
	sigsum->Add(sigb,0.8307*824/sigb->Integral());
	sigsum->Add(sigc,0.063*824/sigc->Integral());
	sigsum->Add(sigl,0.05*824/sigl->Integral());
	//sigsum->Add(zz,0.05*2198/zz->Integral());

	sigsum->Write();
	data->Write();

	TObjArray *mc = new TObjArray(3);        // MC histograms are put in this array
	mc->Add(bg);
	mc->Add(sigsum);
	mc->Add(zz);

	TFractionFitter* fit = new TFractionFitter(data, mc); // initialise
	fit->Constrain(1,0.0,0.5);          // constrain fraction 1 to be between 0 and 1
	fit->Constrain(3,0.01,0.016);        // constrain fraction 1 to be between 0 and 1   
	fit->Constrain(2,0.7,1.0);          // constrain fraction 1 to be between 0 and 1  
	fit->SetRangeX(8,22);
	Int_t status = fit->Fit();               // perform the fit
	cout << "fit status: " << status << endl;

	TH1F* res1= (TH1F*) fit->GetPlot();
	cout<<(fit->GetPlot())->Integral()<<endl;
	res1->Write();


// First canvas DATA VS MC																					
   // NN output normalized ---------------------------	
   mlpa_canvas->cd(1);

   double tt_norm,zbb_norm,data_norm,zz_norm;
				
   //bg->Scale((1.0/1000.0));
   //bg->Scale(23.3 * (1.0/bg->Integral()));
   //   bg2->Scale(23.3 * (1.0/bg2->Integral()));
   tt_norm=157.5*5051./(59244088.);
   bg->Scale(tt_norm); 
   bg2->Scale(tt_norm);
   bg->SetLineColor(kYellow); 
   bg->SetFillColor(kYellow);
  
   //tt_norm=157.5*5051./(16352171.);

   //   sigb2->Scale(94.6*  (1.0/sigb2->Integral()));
   //   sigc2->Scale(7.9*  (1.0/sigc2->Integral()));
   //   sigl2->Scale(1.7*  (1.0/sigl2->Integral()));
   //   sigb->Scale(94.6* (1.0/sigb->Integral()));
   //   sigc->Scale(7.9*  (1.0/sigc->Integral()));
   //   sigl->Scale(1.7*  (1.0/sigl->Integral()));

   zbb_norm=3048.*5051./35907791.;
   sigb2->Scale(zbb_norm);
   sigc2->Scale(zbb_norm);
   sigl2->Scale(zbb_norm);
   sigb->Scale(zbb_norm);
   sigc->Scale(zbb_norm);
   sigl->Scale(zbb_norm);

   sigb->SetLineColor(kRed);
   sigb->SetFillColor(kRed);
   sigc->SetLineColor(kGreen);
   sigc->SetFillColor(kGreen);
   sigl->SetLineColor(kBlue);
   sigl->SetFillColor(kBlue);

   //   zz->Scale(3.1 * (1.0/zz->Integral()));
   //   zz2->Scale(3.1 * (1.0/zz2->Integral()));
   zz_norm=6.206*5051./4191045.;  
   zz->Scale(zz_norm);
   zz2->Scale(zz_norm);
   zz->SetLineColor(kCyan);
   zz->SetFillColor(kCyan);

   bg->SetStats(0);
   sigb->SetStats(0);
   sigc->SetStats(0);
   sigl->SetStats(0);
   data->SetStats(0);

   THStack *hs=new THStack("hs","test stacked histograms");
   hs->Add(zz);
   hs->Add(bg);
   hs->Add(sigb);
   hs->Add(sigc);
   hs->Add(sigl);
   hs->Draw();
   //data->Scale(18.674166*0.0189*5051./1100000.);
   //data_norm=18.674166*0.0189*5051./1100000.;
   data_norm=1.0;
   data->Draw("E1SAME");
   //data->Draw("SAME");
   TLegend *legendd = new TLegend(.75, .80, .95, .95);
   legendd->AddEntry(bg, "t #bar{t}");
   legendd->AddEntry(sigb, " z+b");
   legendd->AddEntry(sigc, " z+c");
   legendd->AddEntry(sigl, " z+l");
   legendd->AddEntry(zz, "ZZ");
   legendd->AddEntry(data, "Data 5.05fb^{-1} ");
   //legendd->AddEntry(data, " Z(ll)H(bb) ");
   legendd->Draw();
   
   //-------------------------------------------------------
   //---------  Weight Distribution

   mlpa_canvas->cd(5);
   dwgg_zbb_b->Scale(zbb_norm);
   dwgg_zbb_b->SetLineColor(kRed);
   dwgg_zbb_b->SetFillColor(kRed);
   dwgg_zbb_c->Scale(zbb_norm);
   dwgg_zbb_c->SetLineColor(kGreen);
   dwgg_zbb_c->SetFillColor(kGreen);
   dwgg_zbb_l->Scale(zbb_norm);
   dwgg_zbb_l->SetLineColor(kBlue);
   dwgg_zbb_l->SetFillColor(kBlue);
   
   dwgg_tt->Scale(tt_norm);
   dwgg_tt->SetLineColor(kYellow);
   dwgg_tt->SetFillColor(kYellow);  
   dwgg_zz->Scale(zz_norm);
   dwgg_zz->SetLineColor(kCyan);
   dwgg_zz->SetFillColor(kCyan);
   
   THStack *hs2=new THStack("hs2","Whi C0");
   hs2->Add(dwgg_zz);
   hs2->Add(dwgg_tt);
   hs2->Add(dwgg_zbb_b);
   hs2->Add(dwgg_zbb_c);
   hs2->Add(dwgg_zbb_l);
   hs2->Draw();
   dwgg_data->Scale(data_norm);
   dwgg_data->Draw("Same");
   legendd->Draw();


   mlpa_canvas->cd(7);
   dwggs_zbb_b->Scale(zbb_norm);
   dwggs_zbb_b->SetLineColor(kRed);
   dwggs_zbb_b->SetFillColor(kRed);
   dwggs_zbb_c->Scale(zbb_norm);
   dwggs_zbb_c->SetLineColor(kGreen);
   dwggs_zbb_c->SetFillColor(kGreen);
   dwggs_zbb_l->Scale(zbb_norm);
   dwggs_zbb_l->SetLineColor(kBlue);
   dwggs_zbb_l->SetFillColor(kBlue);

   dwggs_tt->Scale(tt_norm);
   dwggs_tt->SetLineColor(kYellow);
   dwggs_tt->SetFillColor(kYellow);
   dwggs_zz->Scale(zz_norm);
   dwggs_zz->SetLineColor(kCyan);
   dwggs_zz->SetFillColor(kCyan);

   THStack *hs2s=new THStack("hs2s","Wzz C0");
   hs2s->Add(dwggs_zz);
   hs2s->Add(dwggs_tt);
   hs2s->Add(dwggs_zbb_b);
   hs2s->Add(dwggs_zbb_c);
   hs2s->Add(dwggs_zbb_l);
   hs2s->Draw();
   dwggs_data->Scale(data_norm);
   dwggs_data->Draw("E1Same");
   legendd->Draw();
   
   mlpa_canvas->cd(6);   
   dwqq_zbb_b->Scale(zbb_norm);
   dwqq_zbb_b->SetLineColor(kRed);
   dwqq_zbb_b->SetFillColor(kRed);
   dwqq_zbb_c->Scale(zbb_norm);
   dwqq_zbb_c->SetLineColor(kGreen);
   dwqq_zbb_c->SetFillColor(kGreen);
   dwqq_zbb_l->Scale(zbb_norm);
   dwqq_zbb_l->SetLineColor(kBlue);
   dwqq_zbb_l->SetFillColor(kBlue);
   dwqq_tt->Scale(tt_norm);
   dwqq_tt->SetLineColor(kYellow);
   dwqq_tt->SetFillColor(kYellow);
   dwqq_zz->Scale(zz_norm);
   dwqq_zz->SetLineColor(kCyan);
   dwqq_zz->SetFillColor(kCyan);

   THStack *hs3=new THStack("hs3","Whi C3");
   hs3->Add(dwqq_zz);
   hs3->Add(dwqq_tt);
   hs3->Add(dwqq_zbb_b);
   hs3->Add(dwqq_zbb_c);
   hs3->Add(dwqq_zbb_l);
   hs3->Draw();
   dwqq_data->Scale(data_norm);
   dwqq_data->Draw("E1Same");
   legendd->Draw();

   mlpa_canvas->cd(8);
   dwqqs_zbb_b->Scale(zbb_norm);
   dwqqs_zbb_b->SetLineColor(kRed);
   dwqqs_zbb_b->SetFillColor(kRed);
   dwqqs_zbb_c->Scale(zbb_norm);
   dwqqs_zbb_c->SetLineColor(kGreen);
   dwqqs_zbb_c->SetFillColor(kGreen);
   dwqqs_zbb_l->Scale(zbb_norm);
   dwqqs_zbb_l->SetLineColor(kBlue);
   dwqqs_zbb_l->SetFillColor(kBlue);
   dwqqs_tt->Scale(tt_norm);
   dwqqs_tt->SetLineColor(kYellow);
   dwqqs_tt->SetFillColor(kYellow);
   dwqqs_zz->Scale(zz_norm);
   dwqqs_zz->SetLineColor(kCyan);
   dwqqs_zz->SetFillColor(kCyan);

   THStack *hs3s=new THStack("hs3s","Whi C3");
   hs3s->Add(dwqqs_zz);
   hs3s->Add(dwqqs_tt);
   hs3s->Add(dwqqs_zbb_b);
   hs3s->Add(dwqqs_zbb_c);
   hs3s->Add(dwqqs_zbb_l);
   hs3s->Draw();
   dwqqs_data->Scale(data_norm);
   dwqqs_data->Draw("E1Same");
   legendd->Draw();


   mlpa_canvas->cd(2);
   wqq2_zbb_b->Scale(zbb_norm);
   wqq2_zbb_b->SetLineColor(kRed);
   wqq2_zbb_b->SetFillColor(kRed);
   wqq2_zbb_c->Scale(zbb_norm);
   wqq2_zbb_c->SetLineColor(kGreen);
   wqq2_zbb_c->SetFillColor(kGreen);
   wqq2_zbb_l->Scale(zbb_norm);
   wqq2_zbb_l->SetLineColor(kBlue);
   wqq2_zbb_l->SetFillColor(kBlue);
   wqq2_tt->Scale(tt_norm);
   wqq2_tt->SetLineColor(kYellow);
   wqq2_tt->SetFillColor(kYellow);
   wqq2_zz->Scale(zz_norm);
   wqq2_zz->SetLineColor(kCyan);
   wqq2_zz->SetFillColor(kCyan);

   THStack *hs4=new THStack("hs4"," Wqq");
   hs4->Add(wqq2_zz);
   hs4->Add(wqq2_tt);
   hs4->Add(wqq2_zbb_b);
   hs4->Add(wqq2_zbb_c);
   hs4->Add(wqq2_zbb_l);
   hs4->Draw();
   wqq2_data->Scale(data_norm);
   wqq2_data->Draw("E1Same");
   legendd->Draw();

   mlpa_canvas->cd(3);
   wgg2_zbb_b->Scale(zbb_norm);
   wgg2_zbb_b->SetLineColor(kRed);
   wgg2_zbb_b->SetFillColor(kRed);
   wgg2_zbb_c->Scale(zbb_norm);
   wgg2_zbb_c->SetLineColor(kGreen);
   wgg2_zbb_c->SetFillColor(kGreen);
   wgg2_zbb_l->Scale(zbb_norm);
   wgg2_zbb_l->SetLineColor(kBlue);
   wgg2_zbb_l->SetFillColor(kBlue);
   wgg2_tt->Scale(tt_norm);
   wgg2_tt->SetLineColor(kYellow);
   wgg2_tt->SetFillColor(kYellow);
   wgg2_zz->Scale(zz_norm);
   wgg2_zz->SetLineColor(kCyan);
   wgg2_zz->SetFillColor(kCyan);


   THStack *hs5=new THStack("hs5"," Wgg");
   hs5->Add(wgg2_zz);
   hs5->Add(wgg2_tt);
   hs5->Add(wgg2_zbb_b);
   hs5->Add(wgg2_zbb_c);
   hs5->Add(wgg2_zbb_l);
   hs5->Draw();
   wgg2_data->Scale(data_norm);
   wgg2_data->Draw("E1Same");
   legendd->Draw();


   mlpa_canvas->cd(4);
   wtt2_zbb_b->Scale(zbb_norm);
   wtt2_zbb_b->SetLineColor(kRed);
   wtt2_zbb_b->SetFillColor(kRed);
   wtt2_zbb_c->Scale(zbb_norm);
   wtt2_zbb_c->SetLineColor(kGreen);
   wtt2_zbb_c->SetFillColor(kGreen);
   wtt2_zbb_l->Scale(zbb_norm);
   wtt2_zbb_l->SetLineColor(kBlue);
   wtt2_zbb_l->SetFillColor(kBlue);
   wtt2_tt->Scale(tt_norm);
   wtt2_tt->SetLineColor(kYellow);
   wtt2_tt->SetFillColor(kYellow);
   wtt2_zz->Scale(zz_norm);
   wtt2_zz->SetLineColor(kCyan);
   wtt2_zz->SetFillColor(kCyan);


   THStack *hs6=new THStack("hs6"," Wtt");
   hs6->Add(wtt2_zz);
   hs6->Add(wtt2_tt);
   hs6->Add(wtt2_zbb_b);
   hs6->Add(wtt2_zbb_c);
   hs6->Add(wtt2_zbb_l);
   hs6->Draw();
   wtt2_data->Scale(data_norm);
   wtt2_data->Draw("E1Same");
   legendd->Draw();


//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------                                                 
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
// Fourth canvas Boost correction  

   double sig2fb[150];
   double bg2fb[150];
   double sig2fb2b[150];
   double sig2fb2c[150];
   double sig2fb2l[150];
   double bg2fb2[150];
   double zz2fb[150];
   double signif[150];
   double bin[150];
   sig2fb2b[0]=0.0;
   sig2fb2l[0]=0.0;
   sig2fb2c[0]=0.0;


   bg2fb2[0]=0.0;
   zz2fb[0]=0.0;
   
   for(int j=0;j<150;j++){
     sig2fb[j]=(sigb2->Integral(j+1,151)/(sigb2->Integral()));
     bg2fb[j]=(bg2->Integral(j+1,151)/(bg2->Integral()));

     sig2fb2b[j]=sig2fb2b[j-1]+sigb2->GetBinContent(151-j);
     sig2fb2c[j]=sig2fb2c[j-1]+sigc2->GetBinContent(151-j);
     sig2fb2l[j]=sig2fb2l[j-1]+sigl2->GetBinContent(151-j);

     bg2fb2[j]=bg2fb2[j-1]+bg2->GetBinContent(151-j);
     zz2fb[j]=zz2fb[j-1]+zz2->GetBinContent(151-j);
     signif[j]=(sig2fb2b[j])/(sqrt((bg2fb2[j])+(zz2fb[j])+(sig2fb2c[j])+(sig2fb2l[j])+(sig2fb2b[j])));
     if(bg2fb2[j]==0.0 && zz2fb[j]==0.0 && sig2fb2c[j]==0.0 && (sig2fb2l[j])==0 && (sig2fb2b[j])==0){
       signif[j]=0.0;
     }
     bin[j]=sigb2->GetBinCenter(151-j);
     //cout<<j<<" "<<bg2fb2[j]<<" "<<zz2fb[j]<<" "<<sig2fb2[j]<<endl;
     cout<<j<<" "<<signif[j]<<" "<<bin[j]<<endl;                                                                                                                                            
   }
   TGraph *Eff2fb=new TGraph(150,sig2fb,bg2fb);
   TGraph *Signif2fb=new TGraph(150,bin,signif);

   mlpd_canvas->cd(1);
   Eff2fb->Draw("A*P");

   mlpd_canvas->cd(2);   
   Signif2fb->Draw("A*P");

   mlpd_canvas->cd(3);
   zbbbb->Scale(zbb_norm);
   //higgs->Scale(data_norm);
   higgs->Scale(zbbbb->Integral()/higgs->Integral());
   zbbbb->SetMarkerColor(kRed);
   zbbbb->Draw("box");
   higgs->Draw("boxSAME");


//-------------------------------------------------------------------------------------------------------------------------------------------------------------
// Fifth canvas Boost correction  
   
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//-----------------                  Write in the RootFile          -------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
   
   mlpa_canvas->Write();
   mlpb_canvas->Write();
   mlpc_canvas->Write();
   mlpd_canvas->Write();
   mlpe_canvas->Write();
   
   file.Close();
}
