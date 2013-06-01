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

void Neural_net_E(const string dy, const string zbb, const string tt, const string ttfulllept, const string zz, const string zh, TString name, TString directory, TString NNStruct, int iterations, TString cuts)
{
	if (!gROOT->GetClass("TMultiLayerPerceptron")) {
		gSystem->Load("libMLP");
	}

	// output file : control of the NN
        TFile file(directory+"/NN_Higgs_vs_Bkg_"+name+".root","RECREATE");

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
	simu->Branch("dphiZbb",&sim->dphi,"dphiZbb/D");
	simu->Branch("ptZ",&sim->ptZ,"ptZ/D");
	simu->Branch("ptbb",&sim->ptbb,"ptbb/D");
	simu->Branch("prodCSV",&sim->prodCSV,"prodCSV/D");
	simu->Branch("Met",&sim->Met,"Met/D");
	simu->Branch("Mll",&sim->Mll,"Mll/D");
	simu->Branch("Mbb",&sim->Mbb,"Mbb/D");
	simu->Branch("regMbb",&sim->regMbb,"regMbb/D");
        simu->Branch("Multi",&sim->Multi,"Multi/I");
        simu->Branch("metsig",&sim->metsig,"metsig/D");

        simu->Branch("HvsZbb",&sim->HvsZbb,"HvsZbb/D");
        simu->Branch("HvsTT",&sim->HvsTT,"HvsTT/D");
        simu->Branch("HvsZZ",&sim->HvsZZ,"HvsZZ/D");
	simu->Branch("prodNNs",&sim->prodNNs,"prodNNs/D");

	simu->Branch("evtWeight",&sim->evtWeight,"evtWeight/D");

	// open file to get nbres of entries

	TString totcuts("rc_eventSelection_18_idx==1");
	totcuts+=cuts;
	cout<<"cut on : "<<totcuts<<endl;

	std::map<string,int> Ni;
	string listSample[]={dy,zbb,tt,ttfulllept,zz,zh};
	int nSamples = 6;
	std::map<string,int> sampleID;
	sampleID[dy]=0; sampleID[zbb]=1; sampleID[tt]=0; sampleID[ttfulllept]=2; sampleID[zz]=3; sampleID[zh]=5;
	std::map<string,nn_vars*> var;
	for(int s = 0; s<nSamples; s++){
	  TChain *treetmp =new TChain("rds_zbb");
	  treetmp->Reset();
	  treetmp->Add(listSample[s].c_str());
	  TTree *ttmp = treetmp->CopyTree(totcuts);
	  Ni[listSample[s]]=ttmp->GetEntries();
	  cout<<s<<" N is "<<Ni[listSample[s]]<<endl;
	  treetmp->Reset();
	  ttmp->Reset();
	  var[listSample[s]] = new nn_vars(Ni[listSample[s]]);
	  int isSignal = 0;
	  if(listSample[s]==zh) isSignal = 1;
	  int fill = 1;
	  if(listSample[s]==dy || listSample[s]==tt) fill=0;
	  Input(listSample[s], var[listSample[s]], sim, simu, fill, isSignal, sampleID[listSample[s]], totcuts);
	}
	simu->Write();
	// Tree SIMU for NN training filled

	// Declaration of multiplayer perceptron object. input variable = branch of simu tree. Not all at the same time. To add a branch as input add @branchname. then : intermediate layer node, put : to add new layer. Ended by : @type mean that outup is 1 or 0. Then we specify the number of entries for training and test samples.
	int Dy=var[zbb]->evt_nbr[0];
	int Tt=var[ttfulllept]->evt_nbr[0];
	int Zz=var[zz]->evt_nbr[0];
	int Hi=var[zh]->evt_nbr[0];
	ostringstream osdy,ostt,oszz,oszh;
	osdy << Dy;ostt << Tt;oszz << Zz;oszh << Hi;
	TString normZH= oszh.str();TString normDY= osdy.str();TString normTT= ostt.str();TString normZZ= oszz.str();

	cout<<Dy<<" "<<Tt<<" "<<Zz<<" "<<Hi<<endl;

	TMultiLayerPerceptron *mlp =new TMultiLayerPerceptron("@HvsZbb,@HvsZZ,@HvsTT"+NNStruct+":type!","evtWeight*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+"))",simu,"Entry$%2!=0","Entry$%2==0");
	mlp->Train(iterations, "text,graph,update=2");
	//
	if(tag==1){mlp =new TMultiLayerPerceptron("@gg_weight,@qq_weight,@hi_weight,@hi3_weight:"+NNStruct+":type!","(type1==1)/"+normZH+"+(type1==0)/"+normDY+"",simu,"Entry$%2!=0","Entry$%2==0");}
	if(tag==2){mlp =new TMultiLayerPerceptron("@tt_weight,@hi_weight,@hi3_weight:"+NNStruct+":type!","(type1==1)/"+normZH+"+(type1==0)/"+normTT+"",simu,"Entry$%2!=0","Entry$%2==0");}
	if(tag==3){mlp =new TMultiLayerPerceptron("@zz_weight,@zz3_weight,@hi_weight,@hi3_weight:"+NNStruct+":type!","(type1==1)/"+normZH+"+(type1==0)/"+normZZ+"",simu,"Entry$%2!=0","Entry$%2==0");}
	// Function of the NN is exported in python. AND in c++ code (in NN directory) Function to use to evaluate NN
	mlp->Export(directory+"/MLP_Higgs_vs_Bkg_"+name,"python");
	mlp->Export(directory+"/MLP_Higgs_vs_Bkg_"+name,"c++");
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

	std::map<string,TH1F*> hists;
	string channel[] = {"Mu","EE"};
	string hname[] = {"NN","prod"};
	std::map<string,string> labels;
	labels[dy]="DY"; labels[zbb]="Zbb"; labels[tt]="TT"; labels[ttfulllept]="TT-FullLept"; labels[zz]="ZZ"; labels[zh]="signal";
	for(int s = 0; s<nSamples; s++){
	  for(int c = 0; c<2; c++){
	    for(int n = 0; n<2; n++){
	      hists[labels[listSample[s]]+channel[c]+hname[n]] = new TH1F((labels[listSample[s]]+channel[c]+hname[n]).c_str(), (hname[n]+" output").c_str(), 28, -0.2, 1.2);
	      hists[labels[listSample[s]]+channel[c]+hname[n]]->SetDirectory(0);
	    }
	  }
	}

	// histo of efficiency
	TH1F *bg_eff = new TH1F("bgh", "NN output", 28, -0.2, 1.2);
	TH1F *sig_eff = new TH1F("sigh", "NN output", 28, -0.2, 1.2);

	vector<string> vNNinputs;
	if(NNStruct.BeginsWith(",")){
	  size_t first=NNStruct.Index(":");
	  string NNinputs = NNStruct.Remove(first).Data();
	  while(NNinputs.length()>0){
	    NNinputs = NNinputs.substr(2);
	    first = NNinputs.find(",@");
	    string tmp=NNinputs;
	    if(first!=string::npos) tmp=NNinputs.substr(0,first); 
	    cout<<"variables added to the NN : "<<tmp<<endl;
	    vNNinputs.push_back(tmp);
	    if(first!=string::npos) NNinputs = NNinputs.substr(first);
	    else NNinputs = "";
	    cout<<"NNinputs.length() "<<NNinputs.length()<<endl;
	  }
	  cout<<"params size "<<nIn<<endl;
	  nIn+=vNNinputs.size();
	}
	Double_t params[nIn]; // to change according to the number of input in the NN; Order must be the same as teh one for NN training !!!
	cout<<"params size "<<nIn<<endl;

	//-------------------------------------------------------------------------

	for(int s = 0; s<nSamples; s++){
	  for (int i=0;i<Ni[listSample[s]]; ++i) {
	    params[0] = var[listSample[s]]->hzbb[i];
	    params[1] = var[listSample[s]]->hzz[i];
	    params[2] = var[listSample[s]]->htt[i];
	    for(unsigned int j=0; j<vNNinputs.size(); j++){
	      if(vNNinputs[j]=="Mbb") params[3+j] = var[listSample[s]]->Mbb[i];
	      else if(vNNinputs[j]=="Multi") params[3+j] = var[listSample[s]]->multi[i];
	      else if(vNNinputs[j]=="prodCSV") params[3+j] = var[listSample[s]]->tagj1[i]*var[listSample[s]]->tagj2[i];
	      else if(vNNinputs[j]=="prodNNs") params[3+j] = var[listSample[s]]->prodNNs[i];
	      else if(vNNinputs[j]=="regMbb") params[3+j] = var[listSample[s]]->regMbb[i];
	      else cout<<"Variable added the NN not known, please add it in the code"<<endl;
	    }
	    string ch = "EE";
	    if(var[listSample[s]]->isMuMu[i]){
	      ch = "Mu";
	    }
	    hists[labels[listSample[s]]+ch+"NN"]->Fill(mlp->Evaluate(0, params),var[listSample[s]]->evtWeight[i]);
	    hists[labels[listSample[s]]+ch+"prod"]->Fill(params[0]*params[1]*params[2],var[listSample[s]]->evtWeight[i]);
	  }
	  for(int c = 0; c<2; c++){
	    cout<<labels[listSample[s]]<<" "<<channel[c]<<" "<<hists[labels[listSample[s]]+channel[c]+"NN"]->Integral()<<endl;
	  }
	}

	for(int c = 0; c<2; c++){
	  file.mkdir(channel[c].c_str());
	  file.cd(channel[c].c_str());
	  for(int s = 0; s<nSamples; s++){
	    for(int n = 0; n<2; n++){
	      string Name = "";
	      if(hname[n]=="prod") Name="prod";
	      hists[labels[listSample[s]]+channel[c]+hname[n]]->SetName((Name+labels[listSample[s]]+"125").c_str());
	      hists[labels[listSample[s]]+channel[c]+hname[n]]->Write();
	    }
	  }
	}
	file.cd();

//------------------------------------------------------------------------- 
//-------------------Normalisation and plot ------------------------------------------------------
//-------------------------------------------------------------------------                                                               
	hists["TT-FullLeptMuNN"]->Add(hists["TT-FullLeptEENN"]);
	hists["DYMuNN"]->Add(hists["DYEENN"]);
	hists["ZZMuNN"]->Add(hists["ZZEENN"]);
	hists["signalMuNN"]->Add(hists["signalEENN"]);

	hists["TT-FullLeptMuNN"]->SetLineColor(kBlue); hists["TT-FullLeptMuNN"]->SetFillColor(kBlue);
	hists["ZZMuNN"]->SetLineColor(kGreen); hists["ZZMuNN"]->SetFillColor(kGreen);
	hists["DYMuNN"]->SetLineColor(kRed); hists["DYMuNN"]->SetFillColor(kRed);

	hists["TT-FullLeptMuNN"]->SetStats(0);
	hists["ZZMuNN"]->SetStats(0);
	hists["DYMuNN"]->SetStats(0);

	// normalisation
	
	hists["TT-FullLeptMuNN"]->Scale((89.+112.4)/hists["TT-FullLeptMuNN"]->Integral());
	hists["DYMuNN"]->Scale((762.38+137.5+138+574.2+115.1+96.9)/hists["DYMuNN"]->Integral());
	hists["ZZMuNN"]->Scale((21.5+15.8)/hists["ZZMuNN"]->Integral());
	hists["signalMuNN"]->Scale((112.+137.5+138+762.38+21.5+89+15.8+574.2+115.1+96.9)/hists["signalMuNN"]->Integral());
	//zhh->Scale(higgs_norm);

	// create stack for histogram display

	THStack *hs=new THStack("hs","test stacked histograms");
	hs->Add(hists["DYMuNN"]);
	hs->Add(hists["TT-FullLeptMuNN"]);
	hs->Add(hists["ZZMuNN"]);
	//hs->Add(twbh);
	hs->Draw();
	//tth->Draw("same");
	hists["signalMuNN"]->Draw("same");	
	//dath->Draw("same");
	TLegend *legend = new TLegend(.75, .80, .95, .95);
	legend->AddEntry(hists["DYMuNN"], " Zbb ");
	legend->AddEntry(hists["TT-FullLeptMuNN"], "t#bar{t}");
	legend->AddEntry(hists["ZZMuNN"], " ZZ ");
	legend->AddEntry(hists["signalMuNN"], " Zhh ");
	legend->Draw();
	
	// efficiency computation signal VS background
	
	mlpa_canvas->cd(3);
	double efficiency_sig[28];
	double efficiency_bg[28];
	for(int b=1;b<29;b++){
	  bg_eff->SetBinContent(b,((hists["DYMuNN"]->Integral(b,29)+hists["TT-FullLeptMuNN"]->Integral(b,29)+hists["ZZMuNN"]->Integral(b,29))/(hists["DYMuNN"]->Integral()+hists["TT-FullLeptMuNN"]->Integral()+hists["ZZMuNN"]->Integral())));
	  sig_eff->SetBinContent(b,(hists["signalMuNN"]->Integral(b,29)/hists["signalMuNN"]->Integral())); // here signal is zbb
	  	  
	  efficiency_sig[b-1]=(hists["signalMuNN"]->Integral(b,29)/hists["signalMuNN"]->Integral());
          efficiency_bg[b-1]=((hists["DYMuNN"]->Integral(b,29)+hists["TT-FullLeptMuNN"]->Integral(b,29)+hists["ZZMuNN"]->Integral(b,29))/(hists["DYMuNN"]->Integral()+hists["TT-FullLeptMuNN"]->Integral()+hists["ZZMuNN"]->Integral()));
	  cout<<"S/sqrt(B) "<<hists["signalMuNN"]->Integral(b,29)/sqrt(hists["DYMuNN"]->Integral(b,29)+hists["TT-FullLeptMuNN"]->Integral(b,29)+hists["ZZMuNN"]->Integral(b,29))<<endl;
	}
	bg_eff->SetLineColor(kBlue);
	sig_eff->SetLineColor(kRed);
	bg_eff->SetStats(0);
	sig_eff->SetStats(0);
	bg_eff->Draw();
	sig_eff->Draw("same");
	TLegend *legend2 = new TLegend(.75, .80, .95, .95);
	legend2->AddEntry(bg_eff, "bkg");
	legend2->AddEntry(sig_eff, "higgs");
	legend2->Draw();
	mlpa_canvas->cd(4);
	TGraph *Eff = new TGraph(28,efficiency_sig,efficiency_bg);
	Eff->Draw("AP");
	Eff->Write();

	mlpa_canvas->Write();

	file.Close();
}
