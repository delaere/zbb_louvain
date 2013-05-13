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

//These are the default cuts
//If you want to change the cuts DO NOT MODIFY THEM HERE, but change the arguments used in the NN.sh script
double ptj1_cut = 20;
double ptj2_cut = 20;
double ptz_cut = -1.0;

void setPtJ1Cut(double x) {ptj1_cut = x;}
void setPtJ2Cut(double x) {ptj2_cut = x;}
void setPtZCut(double x) {ptz_cut = x;}


void Neural_net_E(const char *dy,const char *tt,const char *zz,const char *zh,TString name,int tag,TString NNStruct,int iterations, int multiplicity)
{
	if (!gROOT->GetClass("TMultiLayerPerceptron")) {
		gSystem->Load("libMLP");
	}
	
	std::cout << "[Neural_net_E] tag=" << tag << " NNStruct=" << NNStruct << " iterations=" << iterations << " multiplicity=" << multiplicity << std::endl;

	// output file : control of the NN
        TFile file("NN_Higgs_vs_"+name+".root","RECREATE");

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
	simu->Branch("bbDR",&sim->bbDR,"bbDR/D");
	simu->Branch("Mbbj",&sim->Mbbj,"Mbbj/D");
	simu->Branch("DRFSR",&sim->DRFSR,"DRFSR/D");
	simu->Branch("Mbbjdr",&sim->Mbbjdr,"Mbbjdr/D");
	simu->Branch("FSRDR",&sim->FSRDR,"FSRDR/D");	
	simu->Branch("leadingb",&sim->leadingb,"leadingb/D");
	simu->Branch("Fj1",&sim->Fj1,"Fj1/I");
	simu->Branch("Fj2",&sim->Fj2,"Fj2/I");
	simu->Branch("dyflag",&sim->dyflag,"dyflag/I");	
	
	// open file to get nbres of entries
	int N1,N2,N3,N4;
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
	

	//Apply ptj1, ptj2, and ptz cuts
	kinematical_cuts* kin_cut = new kinematical_cuts(ptj1_cut, ptj2_cut, ptz_cut);
	

	nn_vars *var1 = new nn_vars(N1);
	if(tag==1){Input(dy,N1,var1,sim,simu,1,0,0,multiplicity,kin_cut);}
	nn_vars *var2 = new nn_vars(N2);
	if(tag==2){Input(tt,N2,var2,sim,simu,1,0,0,multiplicity,kin_cut);}
	nn_vars *var3 = new nn_vars(N3);
	if(tag==3){Input(zz,N3,var3,sim,simu,1,0,0,multiplicity,kin_cut);}
	nn_vars *var4 = new nn_vars(N4);
	Input(zh,N4,var4,sim,simu,1,1,0,multiplicity,kin_cut);

	simu->Write();
	// Tree SIMU for NN training filled

	// Declaration of multiplayer perceptron object. input variable = branch of simu tree. Not all at the same time. To add a branch as input add @branchname. then : intermediate layer node, put : to add new layer. Ended by : @type mean that outup is 1 or 0. Then we specify the number of entries for training and test samples.
	TMultiLayerPerceptron *mlp;
	int Dy=var1->evt_nbr[0];
	int Dy0=var1->evt_nbr[1];
	int Dy1=var1->evt_nbr[2];
	int Dy2=var1->evt_nbr[3];
	cout<<Dy<<endl;
        int Tt=var2->evt_nbr[0];
	int Zz=var3->evt_nbr[0];
	int Hi=var4->evt_nbr[0];
	ostringstream osdy,ostt,oszz,oszh,osdy0,osdy1,osdy2;
	osdy << Dy;ostt << Tt;oszz << Zz;oszh << Hi;osdy0<<Dy0;osdy1<<Dy1;osdy2<<Dy2;
	TString normZH= oszh.str();TString normDY= osdy.str();TString normTT= ostt.str();TString normZZ= oszz.str();TString normdyflag0= osdy0.str();TString normdyflag1= osdy1.str();TString normdyflag2= osdy2.str();

        cout << "(1.0*(type1==1))/"+normZH+"+((type1==0)/3 *((dyflag==0)/"+normdyflag0+" + (dyflag==1)/"+normdyflag1+" + (dyflag==2)/"+normdyflag2+"))"<<endl;

	if(tag==1){
	  if (multiplicity==0)mlp =new TMultiLayerPerceptron("@gg_weight,@qq_weight,@hi_weight,@hi3_weight:"+NNStruct+":type1!","(1.0*(type1==1))/"+normZH+"+((type1==0)/4 *(2*(dyflag==0)/"+normdyflag0+"+(dyflag==1)/"+normdyflag1+" + (dyflag==2)/"+normdyflag2+"))",simu,"Entry$%2!=0","Entry$%2==0");	// mean taht we train with 1000 iteration and we update the test and training curve with a step of 100 iterations.
	  if (multiplicity==1)mlp =new TMultiLayerPerceptron("@gg_weight,@qq_weight,@hi_weight,@hi3_weight,@Mbbjdr,@bbDR,@FSRDR:"+NNStruct+":type1!","(1.0*(type1==1))/"+normZH+"+((type1==0)/4 *(2*(dyflag==0)/"+normdyflag0+"+(dyflag==1)/"+normdyflag1+" + (dyflag==2)/"+normdyflag2+"))",simu,"Entry$%2!=0","Entry$%2==0");	
	}
	if(tag==2){
	  if (multiplicity==0)mlp =new TMultiLayerPerceptron("@tt_weight,@hi_weight,@hi3_weight:"+NNStruct+":type1!","(type1==1)/"+normZH+"+(type1==0)/"+normTT+"",simu,"Entry$%2!=0","Entry$%2==0");
	  if (multiplicity==1)mlp =new TMultiLayerPerceptron("@tt_weight,@hi_weight,@hi3_weight,@Mbbjdr,@bbDR,@FSRDR:"+NNStruct+":type1!","(type1==1)/"+normZH+"+(type1==0)/"+normTT+"",simu,"Entry$%2!=0","Entry$%2==0");
	}
	if(tag==3){mlp =new TMultiLayerPerceptron("@zz_weight,@zz3_weight,@hi_weight,@hi3_weight:"+NNStruct+":type1!","(type1==1)/"+normZH+"+(type1==0)/"+normZZ+"",simu,"Entry$%2!=0","Entry$%2==0");}	// mean taht we train with 1000 iteration and we update the test and training curve with a step of 100 iterations.
	
	mlp->Train(iterations, "text,graph,update=2");
	
	//TGraph *train = train_train_residual_plot;
	//TGraph *test = train_residual_plot;
	
	// Function of the NN is exported in python. AND in c++ code (in NN directory) Function to use to evaluate NN
	mlp->Export("MLP_Higgs_vs_"+name,"python");
	mlp->Export("MLP_Higgs_vs_"+name,"c++");
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
	tth->SetDirectory(0);
	Double_t params[7];
	//if(tag==2){Double_t params[3];}// to change according to the number of input in the NN; Order must be the same as teh one for NN training !!!

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
	    if (multiplicity==0)params[0] = var1->gg[i];params[1]=var1->qq[i];params[2]=var1->hi[i];params[3]=var1->hi3[i];
	    if (multiplicity==1)params[0] = var1->gg[i];params[1]=var1->qq[i];params[2]=var1->hi[i];params[3]=var1->hi3[i];params[4]=var1->trijetMdr[i];params[5]=var1->bb_dr[i];params[6]=var1->fsr_DR[i];

	    zbbh->Fill(mlp->Evaluate(0, params));

	  }
// 	  cout << "zbbh: " << mlp->Evaluate(0, params)
// 	                   << " for var1->DY_flag[i]= " << var1->DY_flag[i]
// 	                   << " for var1->Leading_b[i]= " << var1->Leading_b[i]
// 	                   << " for var1->subLeading_b[i]= " << var1->subLeading_b[i]
// 	                   << " for var1->Mll[i]= " << var1->Mll[i]
// 	                   << " for var1->Mbb[i]= " << var1->Mbb[i] << endl;
	  
	  
	  //if(var1->ptZ[i]<100){zbbh->Fill(mlp->Evaluate(0, params));}
	  //if(var1->ptZ[i]>100){zbbh->Fill(mlp->Evaluate(0, params),(15.85/50));}	  
	  
	}
        //-------------------------------------------------------------------------                                                            
	// FOR tt
	bool evt_TT[N2];
	for (int i=0;i<N2; ++i) {
	evt_TT[i]=false;
	  if(var2->Leading_b[i]>20&&var2->subLeading_b[i]>20&&var2->Mll[i]>76.&&var2->Mll[i]<106.&&var2->Mbb[i]<150.){
	    if (multiplicity==1 && var2->multi[i]==1&&var2->Mbb[i]>50.)evt_TT[i]=true;
	    else if (multiplicity==0 && var2->multi[i]==0&&var2->Mbb[i]>80.)evt_TT[i]=true;
	  }
	  if(evt_TT[i]==true){ 
	    if (multiplicity==0)params[0] = var2->tt[i];params[1]=var2->hi[i];params[2]=var2->hi3[i];
	    if (multiplicity==1)params[0] = var2->tt[i];params[1]=var2->hi[i];params[2]=var2->hi3[i];params[3]=var2->trijetMdr[i];params[4]=var2->bb_dr[i];params[5]=var2->fsr_DR[i];
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
	    params[0] = var3->zz[i];params[1] = var3->zz3[i];params[2] = var3->hi[i];params[3] = var3->hi3[i];
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
            if(tag==3)params[0] = var4->zz[i];params[1] = var4->zz3[i];params[2] = var4->hi[i];params[3] = var4->hi3[i];
            if(tag==2){
	      if (multiplicity==0)params[0] = var4->tt[i];params[1] = var4->hi[i];params[2] = var4->hi3[i];
	      if (multiplicity==1)params[0] = var4->tt[i];params[1] = var4->hi[i];params[2] = var4->hi3[i];params[3]=var4->trijetMdr[i];params[4]=var4->bb_dr[i];params[5]=var4->fsr_DR[i];
            } 
	    if(tag==1){
	      if (multiplicity==0)params[0] = var4->gg[i];params[1] =var4->qq[i];params[2]=var4->hi[i];params[3]=var4->hi3[i];
	      if (multiplicity==1)params[0] = var4->gg[i];params[1] =var4->qq[i];params[2]=var4->hi[i];params[3]=var4->hi3[i];params[4]=var4->trijetMdr[i];params[5]=var4->bb_dr[i];params[6]=var4->fsr_DR[i];
	    }
	    zhh->Fill(mlp->Evaluate(0, params));
	  }
	}

//-------------------------------------------------------------------------                                                                                             

	cout<<"  DY   ALL "<<zbbh->Integral()<<endl;
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
	
	tth->Scale(1.0/tth->Integral());
	zbbh->Scale(1.0/zbbh->Integral());
	zzh->Scale(1.0/zzh->Integral());
	zhh->Scale(1.0/zhh->Integral());

	// create stack for histogram display

	THStack *hs=new THStack("hs","test stacked histograms");
	if(tag==1){hs->Add(zbbh);}
	if(tag==2){hs->Add(tth);}
	if(tag==3){hs->Add(zzh);}
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
	  if(tag==1){bg_eff->SetBinContent(b,((zbbh->Integral(b,26))/(zbbh->Integral())));}
	  if(tag==2){bg_eff->SetBinContent(b,((tth->Integral(b,26))/(tth->Integral())));}
	  if(tag==3){bg_eff->SetBinContent(b,((zzh->Integral(b,26))/(zzh->Integral())));}
	  sig_eff->SetBinContent(b,(zhh->Integral(b,26)/zhh->Integral())); // here signal is zbb
	  
	  efficiency_sig[b-1]=(zhh->Integral(b,26)/zhh->Integral());
	  if(tag==1){efficiency_bg[b-1]=(zbbh->Integral(b,26)/zbbh->Integral());}
	  if(tag==2){efficiency_bg[b-1]=(tth->Integral(b,26)/tth->Integral());}
	  if(tag==3){efficiency_bg[b-1]=(zzh->Integral(b,26)/zzh->Integral());}	  
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


