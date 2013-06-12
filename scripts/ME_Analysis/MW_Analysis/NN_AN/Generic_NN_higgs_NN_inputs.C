/*
 *  Neural_net.cpp
 *  
 *
 *  Created by Arnaud Pin on 30/04/12.
 *  Copyright 2010 __CP3__. All rights reserved.
 *
 */

#include "include.h"
#include "Read_input_NN_inputs.h"

void Neural_net_E(const char *dy,const char *tt,const char *zz,const char *zh,TString name, TString NNStruct,int iterations)
{
	if (!gROOT->GetClass("TMultiLayerPerceptron")) {
		gSystem->Load("libMLP");
	}

	// output file : control of the NN
        TFile file("NN_Higgs_vs_Bkg_"+name+".root","RECREATE");

	//Creation of a Tree for NN training
	TTree *simu = new TTree("Aphi","phi component of the potential");
	tree_in *sim=new tree_in();
	simu->Branch("gg_weight",&sim->gg_weight,"gg_weight/D");
	simu->Branch("qq_weight",&sim->qq_weight,"qq_weight/D");
	simu->Branch("zz_weight",&sim->zz_weight,"zz_weight/D");
        simu->Branch("zz3_weight",&sim->zz3_weight,"zz3_weight/D");
	simu->Branch("hi_weight",&sim->hi_weight,"hi_weight/D");
        simu->Branch("hi3_weight",&sim->hi3_weight,"hi3_weight/D");
	simu->Branch("type",&sim->type,"type/I");
        simu->Branch("type2",&sim->type2,"type2/I");
	simu->Branch("tt_weight",&sim->tt_weight,"tt_weight/D");
	simu->Branch("deta",&sim->deta,"deta/D");
	simu->Branch("dphi",&sim->dphi,"dphi/D");
	simu->Branch("ptZ",&sim->ptZ,"ptZ/D");
	simu->Branch("ptbb",&sim->ptbb,"ptbb/D");
	simu->Branch("Met",&sim->Met,"Met/D");
	simu->Branch("Mll",&sim->Mll,"Mll/D");
	simu->Branch("Mbb",&sim->Mbb,"Mbb/D");
        simu->Branch("Multi",&sim->Multi,"Multi/I");
        simu->Branch("metsig",&sim->metsig,"metsig/D");

        simu->Branch("HvsZbb",&sim->HvsZbb,"HvsZbb/D");
        simu->Branch("HvsTT",&sim->HvsTT,"HvsTT/D");
        simu->Branch("HvsZZ",&sim->HvsZZ,"HvsZZ/D");


	// open file to get nbres of entries
	int N1,N2, N3,N4;
	TChain *treetmp =new TChain("tree2");
	treetmp->Reset();
	treetmp->Add(dy);
	N1=treetmp->GetEntries();
	treetmp->Reset();
	treetmp->Add(tt);
	N2=treetmp->GetEntries();
	treetmp->Reset();
	treetmp->Add(zz);
	N3=treetmp->GetEntries();
	treetmp->Reset();
	treetmp->Add(zh);
	N4=treetmp->GetEntries();
	delete treetmp;

	cout<<N1<<" "<<N2<<" "<<N3<<" "<<N4<<endl;

	nn_vars *var1 = new nn_vars(N1);
	Input(dy,N1,var1,sim,simu,1,0,1);
	nn_vars *var2 = new nn_vars(N2);
	Input(tt,N2,var2,sim,simu,1,0,2);
	nn_vars *var3 = new nn_vars(N3);
	Input(zz,N3,var3,sim,simu,1,0,3);
	nn_vars *var4 = new nn_vars(N4);
	Input(zh,N4,var4,sim,simu,1,1,5);

	simu->Write();
	// Tree SIMU for NN training filled

	// Declaration of multiplayer perceptron object. input variable = branch of simu tree. Not all at the same time. To add a branch as input add @branchname. then : intermediate layer node, put : to add new layer. Ended by : @type mean that outup is 1 or 0. Then we specify the number of entries for training and test samples.
	int Dy=var1->evt_nbr[0];
	int Tt=var2->evt_nbr[0];
	int Zz=var3->evt_nbr[0];
	int Hi=var4->evt_nbr[0];
	ostringstream osdy,ostt,oszz,oszh;
	osdy << Dy;ostt << Tt;oszz << Zz;oszh << Hi;
	TString normZH= oszh.str();TString normDY= osdy.str();TString normTT= ostt.str();TString normZZ= oszz.str();

	cout<<Dy<<" "<<Tt<<" "<<Zz<<" "<<Hi<<endl;

	TMultiLayerPerceptron *mlp =new TMultiLayerPerceptron("@HvsZbb,@HvsZZ,@HvsTT:"+NNStruct+":type","(type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+")",simu,"Entry$%2!=0","Entry$%2==0");
	mlp->Train(iterations, "text,graph,update=2");
	// Function of the NN is exported in python. AND in c++ code (in NN directory) Function to use to evaluate NN
	mlp->Export("MLP_Higgs_vs_Bkg_"+name,"python");
	mlp->Export("MLP_Higgs_vs_Bkg_"+name,"c++");
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
	TH1F *zbbh = new TH1F("zbbh", "NN output", 25, -.5, 1.5);
	TH1F *zzh = new TH1F("zzh", "NN output", 25, -.5, 1.5);
	TH1F *zhh = new TH1F("zhhh", "NN output", 25, -.5, 1.5);	
	TH1F *tth = new TH1F("tth", "NN output", 25, -.5, 1.5);

	// histo of efficiency
	TH1F *bg_eff = new TH1F("bgh", "NN output", 25, -.5, 1.5);
	TH1F *sig_eff = new TH1F("sigh", "NN output", 25, -.5, 1.5);

	zbbh->SetDirectory(0);
	zzh->SetDirectory(0);
	zhh->SetDirectory(0);
	tth->SetDirectory(0);;
	Double_t params[3]; // to change according to the number of input in the NN; Order must be the same as teh one for NN training !!!
	//int zbb=0;

	//-------------------------------------------------------------------------
	// FOR Zbb
	for (int i=0;i<N1; ++i) {
	  if(var1->tagj1[i]>0.679 && var1->tagj2[i]>0.679 && var1-> Mll[i]>76. && var1-> Mll[i]<106.){
          params[0] = var1->hzbb[i];
          params[2] = var1->htt[i];
          params[1] = var1->hzz[i];
	  zbbh->Fill(mlp->Evaluate(0, params));
	  }
	}
        //-------------------------------------------------------------------------                                                            
	// FOR tt
	for (int i=0;i<N2; ++i) {
          if(var2->tagj1[i]>0.679 && var2->tagj2[i]>0.679 && var2-> Mll[i]>76. && var2-> Mll[i]<106.){
	    params[0] = var2->hzbb[i];
	    params[2] = var2->htt[i];
	    params[1] = var2->hzz[i];
	  tth->Fill(mlp->Evaluate(0, params));
	  }
	}
        //-------------------------------------------------------------------------        
	// FOR ZZ
        for (int i=0;i<N3; ++i) {
          if(var3->tagj1[i]>0.679 && var3->tagj2[i]>0.679 && var3-> Mll[i]>60. && var3-> Mll[i]<106.){
	  params[0] = var3->hzbb[i];
          params[2] = var3->htt[i];
          params[1] = var3->hzz[i];
	  zzh->Fill(mlp->Evaluate(0,params));
	  }
        }
        //-------------------------------------------------------------------------
	// FOR ZH
        for (int i=0;i<N4; ++i) {
          if(var4->tagj1[i]>0.679 && var4->tagj2[i]>0.679 && var4-> Mll[i]>60. && var4-> Mll[i]<106.){
	    params[0] = var4->hzbb[i];
	    params[2] = var4->htt[i];
	    params[1] = var4->hzz[i];
          zhh->Fill(mlp->Evaluate(0, params));
	  }
        }
//-------------------------------------------------------------------------                                                                                             



	cout<<"  Zbb  ALL "<<zbbh->Integral()<<endl;
	cout<<"  TT   ALL "<<tth->Integral()<<endl;
	cout<<"  ZZ   ALL "<<zzh->Integral()<<endl;
	cout<<"  ZH   ALL "<<zhh->Integral()<<endl;

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

	
	tth->Scale((89.+112.4)/tth->Integral());
	zbbh->Scale((762.38+137.5+138+574.2+115.1+96.9)/zbbh->Integral());
	zzh->Scale((21.5+15.8)/zzh->Integral());
	zhh->Scale((112.+137.5+138+762.38+21.5+89+15.8+574.2+115.1+96.9)/zhh->Integral());
	//zhh->Scale(higgs_norm);

	// create stack for histogram display

	THStack *hs=new THStack("hs","test stacked histograms");
	hs->Add(zbbh);
	hs->Add(tth);
	hs->Add(zzh);
	//hs->Add(twbh);
	hs->Draw();
	//tth->Draw("same");
	zhh->Draw("same");	
	//dath->Draw("same");
	TLegend *legend = new TLegend(.75, .80, .95, .95);
	legend->AddEntry(zbbh, " Zbb ");
	legend->AddEntry(tth, "t#bar{t}");
	legend->AddEntry(zzh, " ZZ ");
	legend->AddEntry(zhh, " Zhh ");
	legend->Draw();
	
	// efficiency computation signal VS background
	
	mlpa_canvas->cd(3);
	double efficiency_sig[25];
	double efficiency_bg[25];
	for(int b=1;b<26;b++){
	  bg_eff->SetBinContent(b,((zbbh->Integral(b,26)+tth->Integral(b,26)+zzh->Integral(b,26))/(zbbh->Integral()+tth->Integral()+zzh->Integral())));
	  sig_eff->SetBinContent(b,(zhh->Integral(b,26)/zhh->Integral())); // here signal is zbb
	  
	  
	  efficiency_sig[b-1]=(zhh->Integral(b,26)/zhh->Integral());
          efficiency_bg[b-1]=((zbbh->Integral(b,26)+tth->Integral(b,26)+zzh->Integral(b,26))/(zbbh->Integral()+tth->Integral()+zzh->Integral()));
	  cout<<"S/sqrt(B) "<<zhh->Integral(b,26)/sqrt(zbbh->Integral(b,26)+tth->Integral(b,26)+zzh->Integral(b,26))<<endl;
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
