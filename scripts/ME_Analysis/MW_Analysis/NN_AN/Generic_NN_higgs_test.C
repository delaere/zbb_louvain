/*
 *  Neural_net.cpp
 *  
 *
 *  Created by Arnaud Pin on 30/04/12.
 *  Copyright 2010 __CP3__. All rights reserved.
 *
 */

#include "include.h"
#include "Read_input.h"

void Neural_net_E(const char *dy,const char *tt,const char *zz,const char *twb,const char *zh,const char *dat,int N1,int N2,int N3,int N4,int N5,int N6,TString name)
{
	if (!gROOT->GetClass("TMultiLayerPerceptron")) {
		gSystem->Load("libMLP");
	}

	// output file : control of the NN
        TFile file("../NN/NN_Higgs_vs_Zbb_Merge"+name+".root","RECREATE");

	//Creation of a Tree for NN training
	TTree *simu = new TTree("Aphi","phi component of the potential");
	tree_in *sim=new tree_in();
	simu->Branch("gg_weight",&sim->gg_weight,"gg_weight/D");
	simu->Branch("qq_weight",&sim->qq_weight,"qq_weight/D");
	simu->Branch("zz_weight",&sim->zz_weight,"zz_weight/D");
        simu->Branch("zz3_weight",&sim->zz3_weight,"zz3_weight/D");
	simu->Branch("hi_weight",&sim->hi_weight,"hi_weight/D");
        simu->Branch("hi3_weight",&sim->hi3_weight,"hi3_weight/D");
	simu->Branch("type1",&sim->type1,"type1/I");
        simu->Branch("type2",&sim->type2,"type2/I");
	simu->Branch("tt_weight",&sim->tt_weight,"tt_weight/D");
	simu->Branch("deta",&sim->deta,"deta/D");
	simu->Branch("dphi",&sim->dphi,"dphi/D");
	simu->Branch("ptZ",&sim->ptZ,"ptZ/D");
	simu->Branch("ptbb",&sim->ptZ,"ptbb/D");
	simu->Branch("Met",&sim->Met,"Met/D");
	simu->Branch("Mll",&sim->Mll,"Mll/D");
	simu->Branch("Mbb",&sim->Mbb,"Mbb/D");

	nn_vars *var1 = new nn_vars(N1);
	Input(dy,N1,var1,sim,simu,1,0,0);
	nn_vars *var2 = new nn_vars(N2);
	Input(tt,N2,var2,sim,simu,0,0,0);
	nn_vars *var3 = new nn_vars(N3);
	Input(zz,N3,var3,sim,simu,0,0,0);

	nn_vars *var4 = new nn_vars(N4);
	Input(twb,N4,var4,sim,simu,0,0,0);
	nn_vars *var5 = new nn_vars(N5);
	Input(zh,N5,var5,sim,simu,1,1,0);
	nn_vars *var6 = new nn_vars(N6);
	Input(dat,N6,var6,sim,simu,0,0,0);

	simu->Write();
	// Tree SIMU for NN training filled

	// Declaration of multiplayer perceptron object. input variable = branch of simu tree. Not all at the same time. To add a branch as input add @branchname. then : intermediate layer node, put : to add new layer. Ended by : @type mean that outup is 1 or 0. Then we specify the number of entries for training and test samples.

	TMultiLayerPerceptron *mlp =new TMultiLayerPerceptron("@gg_weight,@qq_weight,@hi_weight,@hi3_weight:5:2:type1","(type1==0)/1901.+(type1==1)/2259.",simu,"Entry$%2!=0","Entry$%2==0");	// mean taht we train with 1000 iteration and we update the test and training curve with a step of 100 iterations.
	mlp->Train(2000, "text,graph,update=100");
	// Function of the NN is exported in python. AND in c++ code (in NN directory) Function to use to evaluate NN
	mlp->Export("../NN/MLP_Higgs_vs_Zbb_Merge"+name,"python");
	mlp->Export("../NN/MLP_Higgs_vs_Zbb_Merge"+name,"c++");
	mlp->Write();


	// Use TMLPAnalyzer to see what it looks for. INFO will be in the contro root file
	TCanvas* mlpa_canvas = new TCanvas("mlpa_canvas","Network analysis"); // For NN output
	TCanvas* kin = new TCanvas("kin","kin"); // for kin Variable
	mlpa_canvas->Divide(2,2);
	kin->Divide(2,2);
	TMLPAnalyzer ana(mlp);
	ana.GatherInformations();
	ana.CheckNetwork();
	mlpa_canvas->cd(1);
	// shows the network structure
	mlp->Draw();
	mlpa_canvas->cd(2);
	// Use the NN to plot the results for each sample
	// This will give approx. the same result as DrawNetwork.
	// All entries are used, while DrawNetwork focuses on 
	// the test sample. Also the xaxis range is manually set.
	TH1F *zbbh = new TH1F("zbbh", "NN output", 20, -.5, 1.5);
	TH1F *zzh = new TH1F("zzh", "NN output", 20, -.5, 1.5);
	TH1F *zhh = new TH1F("zhhh", "NN output", 20, -.5, 1.5);	
	TH1F *tth = new TH1F("tth", "NN output", 20, -.5, 1.5);
	TH1F *twbh = new TH1F("twbh", "NN output", 20, -.5, 1.5);
	TH1F *dath = new TH1F("dath", "NN output", 20, -.5, 1.5);

	// histo of efficiency
	TH1F *bg_eff = new TH1F("bgh", "NN output", 25, -.5, 1.5);
	TH1F *sig_eff = new TH1F("sigh", "NN output", 25, -.5, 1.5);

	zbbh->SetDirectory(0);
	zzh->SetDirectory(0);
	zhh->SetDirectory(0);
	tth->SetDirectory(0);
	twbh->SetDirectory(0);
	dath->SetDirectory(0);
	Double_t params[4]; // to change according to the number of input in the NN; Order must be the same as teh one for NN training !!!
	int zbb=0;

	//-------------------------------------------------------------------------
	// FOR Zbb
	for (int i=0;i<N1; ++i) {
	  if(var1-> Mll[i]>76. && var1-> Mll[i]<106.){
	  zbb=zbb+1;
	  //params[0] =var1-> Mll[i];
	  //params[1] = var1->Mbb[i];
	  //params[2] = var1->dphi[i];
	  params[0] = var1->gg[i];
	  params[1] = var1->qq[i];
	  //params[2] = var1->zz[i];
          //params[3] = var1->zz3[i];
	  params[2] = var1->hi[i];
	  params[3] = var1->hi3[i];
	  //params[5] = var1->met[i];
	  //params[2] = var1->hi[i];
	  //params[3] = var1->ptZ[i];
	  //params[4] = var1->deta[i];
	  //params[4] = var1->ptbb[i];
	  zbbh->Fill(mlp->Evaluate(0, params));
	  }
	}
        //-------------------------------------------------------------------------                                                            
	// FOR tt
	for (int i=0;i<N2; ++i) {
          if(var2-> Mll[i]>76. && var2-> Mll[i]<106.){
	  //params[0] =var2-> Mll[i];
	  //params[1] = var2->Mbb[i];
	  //params[2] = var2->dphi[i];
	  params[0] = var2->gg[i];
	  params[1] = var2->qq[i];
	  //params[2] = var2->zz[i];
          //params[3] = var2->zz3[i];
	  params[2] = var2->hi[i];
	  params[3] = var2->hi3[i];
	  //params[5] = var2->met[i];
	  //params[3] = var2->ptZ[i];
          //params[4] = var2->deta[i];
          //params[4] = var2->ptbb[i];
	  tth->Fill(mlp->Evaluate(0, params));
	  }
	}
        //-------------------------------------------------------------------------        
	// FOR ZZ
        for (int i=0;i<N3; ++i) {
          if(var3-> Mll[i]>76. && var3-> Mll[i]<106.){
	  //params[0] =var2-> Mll[i];
	  //params[1] = var3->Mbb[i];
	  //params[2] = var3->dphi[i];
	  params[0] = var3->gg[i];
	  params[1] = var3->qq[i];
	  //params[2] = var3->zz[i];
          //params[3] = var3->zz3[i];
	  params[2] = var3->hi[i];
	  params[3] = var3->hi3[i];
	  //params[5] = var3->met[i];
	  //params[3] = var3->ptZ[i];
	  //params[4] = var3->deta[i];
	  //params[4] = var3->ptbb[i];                                          
	  zzh->Fill(mlp->Evaluate(0,params));
	  }
        }
        //-------------------------------------------------------------------------
	// FOR ZH
        for (int i=0;i<N5; ++i) {
          if(var5-> Mll[i]>76. && var5-> Mll[i]<106.){
          //params[0] =var5-> Mll[i];                                                                                                                                                                           
          //params[1] = var5->Mbb[i];                                                                                                                                                                 
          //params[2] = var5->dphi[i];                                                                                                                                                                   
          params[0] = var5->gg[i];
          params[1] = var5->qq[i];
          //params[2] = var5->zz[i];
          //params[3] = var5->zz3[i];
	  params[2] = var5->hi[i];
          params[3] = var5->hi3[i];                                                                                                                                                              
          //params[5] = var5->met[i];
          //params[3] = var5->ptZ[i];                                                                                                                                                               
          //params[4] = var5->deta[i];                                                                                                                                  
          //params[4] = var5->ptbb[i];
          zhh->Fill(mlp->Evaluate(0, params));
        }
	}


        //-------------------------------------------------------------------------
        // FOR TWb
        for (int i=0;i<N4; ++i) {
          if(var4-> Mll[i]>76. && var4-> Mll[i]<106.){
          //params[0] =var4-> Mll[i];                                                                                                          
          //params[1] = var4->Mbb[i];                                                                                                                                     
          //params[2] = var4->dphi[i];                                                                                                                                  
          params[0] = var4->gg[i];
          params[1] = var4->qq[i];
          //params[2] = var4->zz[i];
	  params[2] = var4->hi[i];
          params[3] = var4->hi3[i];                                                                                                                   
          //params[5] = var4->met[i];
          //params[3] = var4->ptZ[i];                                                                                                              
          //params[4] = var4->deta[i];                                                                                                               
          //params[4] = var4->ptbb[i];                                                                                                                         
          twbh->Fill(mlp->Evaluate(0, params));
	  }
        }

        //------------------------------------------------------------------------- 
        // FOR dat
        for (int i=0;i<N6; ++i) {
          if(var6-> Mll[i]>76. && var6-> Mll[i]<106.){
          //params[0] =var6-> Mll[i];   
          //params[1] = var6->Mbb[i];    
          //params[2] = var6->dphi[i];      
          params[0] = var6->gg[i];
          params[1] = var6->qq[i];
          //params[2] = var6->zz[i];                                                                              
          //params[3] = var6->zz3[i];
          params[2] = var6->hi[i];
          params[3] = var6->hi3[i];
          //params[5] = var6->met[i];
          //params[3] = var6->ptZ[i];                                  
          //params[4] = var6->deta[i];                                                                                          
          //params[4] = var6->ptbb[i]; 
          dath->Fill(mlp->Evaluate(0, params));
	  }
        }
//-------------------------------------------------------------------------                                                                                             



	cout<<"  Zbb  ALL "<<zbbh->Integral()<<endl;
	cout<<"  TT   ALL "<<tth->Integral()<<endl;
	cout<<"  ZZ   ALL "<<zzh->Integral()<<endl;
	cout<<"  Twb  ALL "<<twbh->Integral()<<endl;
	cout<<"  ZH   ALL "<<zhh->Integral()<<endl;
	cout<<"  data ALL "<<dath->Integral()<<endl;

//------------------------------------------------------------------------- 
//-------------------Normalisation and plot ------------------------------------------------------
//-------------------------------------------------------------------------                                                                                                                                       


	tth->SetLineColor(kBlue);
	zzh->SetLineColor(kGreen);
	tth->SetFillColor(kBlue);
	zzh->SetFillColor(kGreen);
	zbbh->SetLineColor(kRed);
	zbbh->SetFillColor(kRed);
	tth->SetStats(0);
	zzh->SetStats(0);
	zbbh->SetStats(0);

	// normalisation
	
	//double tt_norm=157.5*5051./(59244088.);
	double tt_norm=1./31029.;
	//double zz_norm=6.206*5051./4191045.;  
	double zz_norm=1.0/1374;
	double zbb_norm=1.0/824;
	//zbb_norm=3048.*5051./35907791.;
	double higgs_norm=1.0/1200;
	double twb_norm=0.0;
	
	tth->Scale(1.0/tth->Integral());
	zbbh->Scale(1.0/zbbh->Integral());
	twbh->Scale(1.0/twbh->Integral());
	zzh->Scale(1.0/zzh->Integral());
	zhh->Scale(1.0/zhh->Integral());

	// create stack for histogram display

	THStack *hs=new THStack("hs","test stacked histograms");
	hs->Add(zbbh);
	//hs->Add(tth);
	//hs->Add(zzh);
	//hs->Add(twbh);
	hs->Draw();
	//tth->Draw("same");
	zhh->Draw("same");	
	//dath->Draw("same");
	TLegend *legend = new TLegend(.75, .80, .95, .95);
	legend->AddEntry(zbbh, " Zbb ");
	legend->AddEntry(tth, "t#bar{t}");
	legend->AddEntry(zzh, " ZZ ");
	legend->AddEntry(twbh, "twb");
	legend->AddEntry(zhh, " Zhh ");
	legend->AddEntry(dath, "data");
	legend->Draw();
	
	// efficiency computation signal VS background
	
	mlpa_canvas->cd(3);
	double efficiency_sig[25];
	double efficiency_bg[25];
	for(int b=1;b<26;b++){
	  //bg_eff->SetBinContent(b,(bg->Integral(b,26)/bg->Integral())); // Old line
	  bg_eff->SetBinContent(b,((tth->Integral(b,26))/(tth->Integral())));
	  //bg_eff->SetBinContent(b,((zbbh->Integral(b,26))/(zbbh->Integral())));
//	  bg_eff->SetBinContent(b,((zbbh->Integral(b,26)+tth->Integral(b,26)+twbh->Integral(b,26)+zzh->Integral(b,26))/(zbbh->Integral()+tth->Integral()+twbh->Integral()+zzh->Integral())));
	  sig_eff->SetBinContent(b,(zhh->Integral(b,26)/zhh->Integral())); // here signal is zbb
	  
	  
	  efficiency_sig[b-1]=(zhh->Integral(b,26)/zhh->Integral());
          efficiency_bg[b-1]=(tth->Integral(b,26)/tth->Integral());
	  //efficiency_bg[b-1]=(zbbh->Integral(b,26)/zbbh->Integral());
	  cout<<"S/sqrt(B) "<<zbbh->Integral(b,26)/sqrt(tth->Integral(b,26))<<endl;
	}
	bg_eff->SetLineColor(kBlue);
	sig_eff->SetLineColor(kRed);
	bg_eff->SetStats(0);
	sig_eff->SetStats(0);
	bg_eff->Draw();
	sig_eff->Draw("same");
	TLegend *legend2 = new TLegend(.75, .80, .95, .95);
	legend2->AddEntry(bg_eff, "t#bar{t}");
	legend2->AddEntry(sig_eff, "Zbb");
	legend2->Draw();
	mlpa_canvas->cd(4);
	TGraph *Eff = new TGraph(25,efficiency_sig,efficiency_bg);
	Eff->Draw("AP");
	Eff->Write();

	mlpa_canvas->Write();




	file.Close();
}
