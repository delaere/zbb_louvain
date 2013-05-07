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

void Neural_net_E(const char *dy,const char *tt,const char *zz,const char *zh, TString name, TString NNStruct,int iterations, int multiplicity)
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
        simu->Branch("btagprod",&sim->btagprod,"btagprod/D");

        simu->Branch("HvsZbb",&sim->HvsZbb,"HvsZbb/D");
        simu->Branch("HvsTT",&sim->HvsTT,"HvsTT/D");
        simu->Branch("HvsZZ",&sim->HvsZZ,"HvsZZ/D");
        simu->Branch("bbDR",&sim->bbDR,"bbDR/D");                                                  
        simu->Branch("Mbbj",&sim->Mbbj,"Mbbj/D");                                                  
        simu->Branch("DRFSR",&sim->DRFSR,"DRFSR/D");                                               
        simu->Branch("Mbbjdr",&sim->Mbbjdr,"Mbbjdr/D");                                            
        simu->Branch("FSRDR",&sim->FSRDR,"FSRDR/D");                                               
        simu->Branch("leadingb",&sim->leadingb,"leadingb/D");                                      
        simu->Branch("Fj1",&sim->Fj1,"Fj1/I");                                                     
        simu->Branch("Fj2",&sim->Fj2,"Fj2/I");                                                     
        simu->Branch("dyflag",&sim->dyflag,"dyflag/I");
	
	
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

	nn_vars *var1 = new nn_vars(N1);
	Input(dy,N1,var1,sim,simu,0,1,multiplicity);
	nn_vars *var2 = new nn_vars(N2);
	Input(tt,N2,var2,sim,simu,0,2,multiplicity);
	nn_vars *var3 = new nn_vars(N3);
	Input(zz,N3,var3,sim,simu,0,3,multiplicity);
	nn_vars *var4 = new nn_vars(N4);
	Input(zh,N4,var4,sim,simu,1,4,multiplicity);


	simu->Write();
	// Tree SIMU for NN training filled

	// Declaration of multiplayer perceptron object. input variable = branch of simu tree. Not all at the same time. To add a branch as input add @branchname. then : intermediate layer node, put : to add new layer. Ended by : @type mean that outup is 1 or 0. Then we specify the number of entries for training and test samples.
	int Dy=var1->evt_nbr[0];
	int Dy0=var1->evt_nbr[1];                                                                  
	int Dy1=var1->evt_nbr[2];                                                                  
	int Dy2=var1->evt_nbr[3];
	
	int Tt=var2->evt_nbr[0];          
	int Zz=var3->evt_nbr[0];
	int Hi=var4->evt_nbr[0];
	ostringstream osdy,ostt,oszz,oszh,osdy0,osdy1,osdy2;
	osdy << Dy;ostt << Tt;oszz << Zz;oszh << Hi;osdy0<<Dy0;osdy1<<Dy1;osdy2<<Dy2;
	TString normZH= oszh.str();TString normDY= osdy.str();TString normTT= ostt.str();TString normZZ= oszz.str();TString normdyflag0= osdy0.str();TString normdyflag1= osdy1.str();TString normdyflag2= osdy2.str();

	cout<<"DY="<<Dy<<" TT="<<Tt<<" ZZ="<<Zz<<" Higgs="<<Hi<<endl;
	
	TMultiLayerPerceptron *mlp =new TMultiLayerPerceptron("@HvsZbb,@HvsZZ,@HvsTT,@btagprod:"+NNStruct+":type!","(0.9*(type2==1)/3*((dyflag==0)/"+normdyflag0+"+(dyflag==1)/"+normdyflag1+" + (dyflag==2)/"+normdyflag2+"))+(type2==2)*(0.085/"+normTT+")+(type2==3)*(0.015/"+normZZ+")+(type2==4)*(1.05/"+normZH+")",simu,"Entry$%2!=0","Entry$%2==0");

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
	
	//we used to use 25 bins between -0.5 and 1.5 for the non-constrained (in [0-1]) performance plots
	TH1F *zbbh = new TH1F("zbbh", "NN output", 28, -.2, 1.2);
	TH1F *zzh = new TH1F("zzh", "NN output", 28, -.2, 1.2);
	TH1F *zhh = new TH1F("zhhh", "NN output", 28, -.2, 1.2);	
	TH1F *tth = new TH1F("tth", "NN output", 28, -.2, 1.2);

	// histo of efficiency
	TH1F *bg_eff = new TH1F("bgh", "NN output", 28, -.2, 1.2);
	TH1F *sig_eff = new TH1F("sigh", "NN output", 28, -.2, 1.2);

	zbbh->SetDirectory(0);
	zzh->SetDirectory(0);
	zhh->SetDirectory(0);
	tth->SetDirectory(0);

	Double_t params[4]; // to change according to the number of input in the NN; Order must be the same as teh one for NN training !!!
	int zbb=0;

	//-------------------------------------------------------------------------
	// FOR Zbb
	bool evt_DY[N1];
	for (int i=0;i<N1; ++i) {
	  evt_DY[i]=false;
	  if(var1->DY_flag[i]==1&&var1->Leading_b[i]>20&&var1->subLeading_b[i]>20&&var1->Mll[i]>76.&&var1->Mll[i]<106.&&var1->Mbb[i]<150.){
	    if (multiplicity==1 && var1->multi[i]==1&&var1->Mbb[i]>50.)evt_DY[i]=true;
	    else if (multiplicity==0 && var1->multi[i]==0&&var1->Mbb[i]>80.)evt_DY[i]=true;
	  }
	  if(evt_DY[i]==true){
	    zbb=zbb+1;
            params[0] = var1->hzbb[i];
            params[2] = var1->htt[i];
            params[1] = var1->hzz[i];
	    params[3] = var1->tagj1[i]*var1->tagj2[i];
	    zbbh->Fill(mlp->Evaluate(0, params)); 
	  }
	}
        //-------------------------------------------------------------------------                                                            
	// FOR tt
	bool evt_TT[N2];
	for (int i=0;i<N2; ++i) {
	  evt_TT[i]==false;
	  if(var2->Leading_b[i]>20&&var2->subLeading_b[i]>20&&var2->Mll[i]>76.&&var2->Mll[i]<106.&&var2->Mbb[i]<150.){
	    if (multiplicity==1 && var2->multi[i]==1&&var2->Mbb[i]>50.)evt_TT[i]=true;
	    else if (multiplicity==0 && var2->multi[i]==0&&var2->Mbb[i]>80.)evt_TT[i]=true;
	  }
	  if(evt_TT[i]==true){ 
	    params[0] = var2->hzbb[i];
	    params[2] = var2->htt[i];
	    params[1] = var2->hzz[i];
            params[3] = var2->tagj1[i]*var2->tagj2[i];
	  tth->Fill(mlp->Evaluate(0, params));
	  }
	}
        //-------------------------------------------------------------------------        
	// FOR ZZ
	bool evt_ZZ[N3];
        for (int i=0;i<N3; ++i) {
	  evt_ZZ[i]=false;
	  if(var3->Leading_b[i]>20&&var3->subLeading_b[i]>20&&var3->Mll[i]>76.&&var3->Mll[i]<106.&&var3->Mbb[i]<150.){
	    if (multiplicity==1 && var3->multi[i]==1&&var3->Mbb[i]>50.)evt_ZZ[i]=true;
	    else if (multiplicity==0 && var3->multi[i]==0&&var3->Mbb[i]>80.)evt_ZZ[i]=true;
	  }	
	  if(evt_ZZ[i]==true){
	    params[0] = var3->hzbb[i];
            params[2] = var3->htt[i];
            params[1] = var3->hzz[i];
            params[3] = var3->tagj1[i]*var3->tagj2[i];                               
	    zzh->Fill(mlp->Evaluate(0,params));
	  }
        }
        //-------------------------------------------------------------------------
	// FOR ZH
	bool evt_ZH[N4];
        for (int i=0;i<N4; ++i) {
	  evt_ZH[i]=false;
	  if(var4->Leading_b[i]>20&&var4->subLeading_b[i]>20&&var4->Mll[i]>76.&&var4->Mll[i]<106.&&var4->Mbb[i]<150.){
	    if (multiplicity==1 && var4->multi[i]==1&&var4->Mbb[i]>50.)evt_ZH[i]=true;
	    else if (multiplicity==0 && var4->multi[i]==0&&var4->Mbb[i]>80.)evt_ZH[i]=true;
	  }	
	  if(evt_ZH[i]==true){
 	    params[0] = var4->hzbb[i];
	    params[2] = var4->htt[i];
	    params[1] = var4->hzz[i];
            params[3] = var4->tagj1[i]*var4->tagj2[i];
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


	double tt_norm=157.5*5051./(59244088.);
	//double tt_norm=1./31029.;
	double zz_norm=6.206*5051./4191045.;  
	//double zz_norm=1.0/1374;
	//double zbb_norm=1.0/824;
	double zbb_norm=3048.*5051./35907791.;
	//double higgs_norm=0.0189*5051.*(30579./1200.)/30579.;
	double higgs_norm = 100.*2.13 / zhh->Integral();
	
	tth->Scale(tt_norm);
	zbbh->Scale(zbb_norm);
	zzh->Scale(zz_norm);
	zhh->Scale(higgs_norm);

	tth->SetLineColor(kBlue);
	zzh->SetLineColor(kGreen);
	tth->SetFillColor(kBlue);
	zzh->SetFillColor(kGreen);
	zbbh->SetLineColor(kRed);
	zbbh->SetFillColor(kRed);
	tth->SetStats(0);
	zzh->SetStats(0);
	zbbh->SetStats(0);


	// create stack for histogram display

	THStack *hs=new THStack("hs","test stacked histograms");
	hs->Add(zbbh);
	hs->Add(tth);
	hs->Add(zzh);
	hs->Draw();
	zhh->Draw("same");	
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
	  
	}
	bg_eff->SetLineColor(kBlue);
	sig_eff->SetLineColor(kRed);
	bg_eff->SetStats(0);
	sig_eff->SetStats(0);
	bg_eff->Draw();
	sig_eff->Draw("same");
	mlpa_canvas->cd(4);
	TGraph *Eff = new TGraph(25,efficiency_sig,efficiency_bg);
	Eff->Draw("AP");
	Eff->Write();
	mlpa_canvas->Write();


	file.Close();
}
