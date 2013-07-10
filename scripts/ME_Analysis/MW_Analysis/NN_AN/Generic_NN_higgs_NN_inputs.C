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

void Neural_net_E(const string dy, const string zbb, const string tt, const string ttfulllept, const string zz, const string zh, TString name, TString directory, TString NNchoice, TString NNStruct, int iterations, TString cuts)
{
	if (!gROOT->GetClass("TMultiLayerPerceptron")) {
		gSystem->Load("libMLP");
	}

	// output file : control of the NN
        TFile file(directory+"/NN_"+NNchoice+"_"+name+".root","RECREATE");

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

        simu->Branch("HvsZbb_2j",&sim->HvsZbb_2j,"HvsZbb_2j/D");
        simu->Branch("HvsTT_2j",&sim->HvsTT_2j,"HvsTT_2j/D");
        simu->Branch("HvsZZ_2j",&sim->HvsZZ_2j,"HvsZZ_2j/D");
	simu->Branch("prodNNs_2j",&sim->prodNNs_2j,"prodNNs_2j/D");

        simu->Branch("HvsZbb_3j",&sim->HvsZbb_3j,"HvsZbb_3j/D");
        simu->Branch("HvsTT_3j",&sim->HvsTT_3j,"HvsTT_3j/D");
        simu->Branch("HvsZZ_3j",&sim->HvsZZ_3j,"HvsZZ_3j/D");
	simu->Branch("prodNNs_3j",&sim->prodNNs_3j,"prodNNs_3j/D");

	simu->Branch("evtWeight",&sim->evtWeight,"evtWeight/D");
	simu->Branch("trijetMdr",&sim->trijetMdr,"trijetMdr/D");
	simu->Branch("fsrDR",&sim->fsrDR,"fsrDR/D");
	simu->Branch("dijetdR",&sim->dijetdR,"dijetdR/D");

	// open file to get nbres of entries

	TString totcuts("rc_eventSelection_18_idx==1");
	totcuts+=cuts;
	cout<<"cut on : "<<totcuts<<endl;

	std::map<string,int> Ni;
	string listSample[]={dy,zbb,tt,ttfulllept,zz,zh};
	int nSamples = 6;
	std::map<string,int> sampleID;
	sampleID[dy]=1; sampleID[zbb]=1; sampleID[tt]=2; sampleID[ttfulllept]=2; sampleID[zz]=3; sampleID[zh]=5;
	std::map<string,int> fill;
	if(NNchoice.Contains("Higgs_vs_Bkg")) {fill[dy]=1; fill[zbb]=1; fill[tt]=1; fill[ttfulllept]=1; fill[zz]=1; fill[zh]=1;}
	if(NNchoice=="Higgs_vs_DY") {fill[dy]=1; fill[zbb]=1; fill[tt]=0; fill[ttfulllept]=0; fill[zz]=0; fill[zh]=1;}
	if(NNchoice=="Higgs_vs_TT") {fill[dy]=0; fill[zbb]=0; fill[tt]=1; fill[ttfulllept]=1; fill[zz]=0; fill[zh]=1;}
	if(NNchoice=="Higgs_vs_ZZ") {fill[dy]=0; fill[zbb]=0; fill[tt]=0; fill[ttfulllept]=0; fill[zz]=1; fill[zh]=1;}
	if(NNchoice=="DY_vs_TT") {fill[dy]=1; fill[zbb]=1; fill[tt]=1; fill[ttfulllept]=1; fill[zz]=0; fill[zh]=0;}
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
	  else if((listSample[s]==dy||listSample[s]==zbb) && NNchoice=="DY_vs_TT") isSignal = 1;
	  Input(listSample[s], var[listSample[s]], sim, simu, fill[listSample[s]], isSignal, sampleID[listSample[s]], totcuts);
	}
	simu->Write();
	// Tree SIMU for NN training filled

	// Declaration of multiplayer perceptron object. input variable = branch of simu tree. Not all at the same time. To add a branch as input add @branchname. then : intermediate layer node, put : to add new layer. Ended by : @type mean that outup is 1 or 0. Then we specify the number of entries for training and test samples.
	int Dy=var[zbb]->evt_nbr[0]+var[dy]->evt_nbr[0];
	int Tt=var[ttfulllept]->evt_nbr[0]+var[tt]->evt_nbr[0];
	int Zz=var[zz]->evt_nbr[0];
	int Hi=var[zh]->evt_nbr[0];
	ostringstream osdy,ostt,oszz,oszh;
	osdy << Dy;ostt << Tt;oszz << Zz;oszh << Hi;
	TString normZH= oszh.str();TString normDY= osdy.str();TString normTT= ostt.str();TString normZZ= oszz.str();

	cout<<Dy<<" "<<Tt<<" "<<Zz<<" "<<Hi<<endl;

	TMultiLayerPerceptron *mlp = new TMultiLayerPerceptron();
	if(NNchoice=="Higgs_vs_Bkg") mlp = new TMultiLayerPerceptron("@HvsZbb,@HvsZZ,@HvsTT"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+"))",simu,"Entry$%2!=0","Entry$%2==0");
	if(NNchoice=="Higgs_vs_Bkg_2j") mlp = new TMultiLayerPerceptron("@HvsZbb_2j,@HvsZZ_2j,@HvsTT_2j"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+"))",simu,"Entry$%2!=0","Entry$%2==0");
	if(NNchoice=="Higgs_vs_Bkg_3j") mlp = new TMultiLayerPerceptron("@HvsZbb_3j,@HvsZZ_3j,@HvsTT_3j"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+"))",simu,"Entry$%2!=0","Entry$%2==0");
	if(NNchoice=="Higgs_vs_DY"){mlp = new TMultiLayerPerceptron("@gg_weight,@qq_weight,@hi_weight,@hi3_weight"+NNStruct+":type!","(type2==5)/"+normZH+"+(type2==1)/"+normDY+"",simu,"Entry$%2!=0","Entry$%2==0");}
	if(NNchoice=="Higgs_vs_TT"){mlp = new TMultiLayerPerceptron("@tt_weight,@hi_weight,@hi3_weight"+NNStruct+":type!","(type2==5)/"+normZH+"+(type2==2)/"+normTT+"",simu,"Entry$%2!=0","Entry$%2==0");}
	if(NNchoice=="Higgs_vs_ZZ"){mlp = new TMultiLayerPerceptron("@zz_weight,@zz3_weight,@hi_weight,@hi3_weight"+NNStruct+":type!","(type2==5)/"+normZH+"+(type2==3)/"+normZZ+"",simu,"Entry$%2!=0","Entry$%2==0");}
	if(NNchoice=="DY_vs_TT"){mlp = new TMultiLayerPerceptron("@gg_weight,@qq_weight,@tt_weight"+NNStruct+":type!","(type2==1)/"+normDY+"+(type2==2)/"+normTT+"",simu,"Entry$%2!=0","Entry$%2==0");}

	if(NNchoice=="Higgs_vs_Bkg_7w") mlp = new TMultiLayerPerceptron("@gg_weight,@qq_weight,@hi_weight,@hi3_weight,@tt_weight,@zz_weight,@zz3_weight"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+"))",simu,"Entry$%2!=0","Entry$%2==0");

	if(NNchoice=="Higgs_vs_Bkg_5w") mlp = new TMultiLayerPerceptron("@gg_weight,@qq_weight,@tt_weight,@zz_weight,@zz3_weight"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+"))",simu,"Entry$%2!=0","Entry$%2==0");

	// Function of the NN is exported in python. AND in c++ code (in NN directory) Function to use to evaluate NN
	mlp->Train(iterations, "text,graph,update=2");
	mlp->Export((directory+"/MLP_"+NNchoice+"_"+name).ReplaceAll("-","_"),"python");
	mlp->Export((directory+"/MLP_"+NNchoice+"_"+name).ReplaceAll("-","_"),"c++");
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

	int nIn = 3;
	if(NNchoice=="Higgs_vs_DY" || NNchoice=="Higgs_vs_ZZ") nIn=4;
	if(NNchoice=="Higgs_vs_Bkg_7w") nIn=7;
	if(NNchoice=="Higgs_vs_Bkg_5w") nIn=5;
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
	  //nIn+=vNNinputs.size();
	}
	Double_t params[nIn+vNNinputs.size()]; // to change according to the number of input in the NN; Order must be the same as teh one for NN training !!!
	cout<<"params size "<<nIn+vNNinputs.size()<<endl;

	//-------------------------------------------------------------------------

	for(int s = 0; s<nSamples; s++){
	  for (int i=0;i<Ni[listSample[s]]; ++i) {
	    if(NNchoice=="Higgs_vs_Bkg") {params[0] = var[listSample[s]]->hzbb[i]; params[1] = var[listSample[s]]->hzz[i]; params[2] = var[listSample[s]]->htt[i];}
	    if(NNchoice=="Higgs_vs_Bkg_2j") {params[0] = var[listSample[s]]->hzbb_2j[i]; params[1] = var[listSample[s]]->hzz_2j[i]; params[2] = var[listSample[s]]->htt_2j[i];}
	    if(NNchoice=="Higgs_vs_Bkg_3j") {params[0] = var[listSample[s]]->hzbb_3j[i]; params[1] = var[listSample[s]]->hzz_3j[i]; params[2] = var[listSample[s]]->htt_3j[i];}
	    if(NNchoice=="Higgs_vs_DY") {params[0] = var[listSample[s]]->gg[i]; params[1] = var[listSample[s]]->qq[i]; params[2] = var[listSample[s]]->hi[i]; params[3] = var[listSample[s]]->hi3[i];}
	    if(NNchoice=="Higgs_vs_TT") {params[0] = var[listSample[s]]->tt[i]; params[1] = var[listSample[s]]->hi[i]; params[2] = var[listSample[s]]->hi3[i];}
	    if(NNchoice=="Higgs_vs_ZZ") {params[0] = var[listSample[s]]->zz[i]; params[1] = var[listSample[s]]->zz3[i]; params[2] = var[listSample[s]]->hi[i]; params[3] = var[listSample[s]]->hi3[i];}
	    if(NNchoice=="DY_vs_TT") {params[0] = var[listSample[s]]->gg[i]; params[1] = var[listSample[s]]->qq[i]; params[2] = var[listSample[s]]->tt[i];}

	    if(NNchoice=="Higgs_vs_Bkg_7w") {params[0] = var[listSample[s]]->gg[i]; params[1] = var[listSample[s]]->qq[i]; params[2] = var[listSample[s]]->hi[i]; params[3] = var[listSample[s]]->hi3[i]; params[4] = var[listSample[s]]->tt[i]; params[5] = var[listSample[s]]->zz[i]; params[6] = var[listSample[s]]->zz3[i];}
	    if(NNchoice=="Higgs_vs_Bkg_5w") {params[0] = var[listSample[s]]->gg[i]; params[1] = var[listSample[s]]->qq[i]; params[2] = var[listSample[s]]->tt[i]; params[3] = var[listSample[s]]->zz[i]; params[4] = var[listSample[s]]->zz3[i];}

	    for(unsigned int j=0; j<vNNinputs.size(); j++){
	      if(vNNinputs[j]=="Mbb") params[nIn+j] = var[listSample[s]]->Mbb[i];
	      else if(vNNinputs[j]=="Multi") params[nIn+j] = var[listSample[s]]->multi[i];
	      else if(vNNinputs[j]=="prodCSV") params[nIn+j] = var[listSample[s]]->tagj1[i]*var[listSample[s]]->tagj2[i];
	      else if(vNNinputs[j]=="prodNNs") params[nIn+j] = var[listSample[s]]->prodNNs[i];
	      else if(vNNinputs[j]=="regMbb") params[nIn+j] = var[listSample[s]]->regMbb[i];
	      else if(vNNinputs[j]=="trijetMdr") params[nIn+j] = var[listSample[s]]->trijetMdr[i];
	      else if(vNNinputs[j]=="fsrDR") params[nIn+j] = var[listSample[s]]->fsrDR[i];
	      else if(vNNinputs[j]=="dijetdR") params[nIn+j] = var[listSample[s]]->dijetdR[i];
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
	for(int s = 0; s<nSamples; s++){
	  hists[labels[listSample[s]]+"MuNN"]->Add(hists[labels[listSample[s]]+"EENN"]);
	}

	hists["TTMuNN"]->Add(hists["TT-FullLeptMuNN"]);
	hists["DYMuNN"]->Add(hists["ZbbMuNN"]);

	hists["TTMuNN"]->SetLineColor(kBlue); hists["TTMuNN"]->SetFillColor(kBlue);
	hists["ZZMuNN"]->SetLineColor(kGreen); hists["ZZMuNN"]->SetFillColor(kGreen);
	hists["DYMuNN"]->SetLineColor(kRed); hists["DYMuNN"]->SetFillColor(kRed);

	hists["TTMuNN"]->SetStats(0);
	hists["ZZMuNN"]->SetStats(0);
	hists["DYMuNN"]->SetStats(0);

	// normalisation
	if(NNchoice.Contains("Higgs_vs_Bkg")){
	  hists["TTMuNN"]->Scale(0.15/hists["TTMuNN"]->Integral());
	  hists["DYMuNN"]->Scale(0.80/hists["DYMuNN"]->Integral());
	  hists["ZZMuNN"]->Scale(0.05/hists["ZZMuNN"]->Integral());
	  hists["signalMuNN"]->Scale(1.0/hists["signalMuNN"]->Integral());
	}
	else{
	  for(int s = 0; s<nSamples; s++){
	    hists[labels[listSample[s]]+"MuNN"]->Scale(1.0/hists[labels[listSample[s]]+"MuNN"]->Integral());
	  }
	}
	// create stack for histogram display

	THStack *hs=new THStack("hs","test stacked histograms");
	if(fill[zbb]&&NNchoice!="DY_vs_TT") hs->Add(hists["DYMuNN"]);
	if(fill[tt]) hs->Add(hists["TTMuNN"]);
	if(fill[zz]) hs->Add(hists["ZZMuNN"]);

	hs->Draw();
	if(NNchoice!="DY_vs_TT") hists["signalMuNN"]->Draw("same");	
	else hists["DYMuNN"]->Draw("same");

	TLegend *legend = new TLegend(.75, .80, .95, .95);
	if(fill[zbb]&&NNchoice!="DY_vs_TT") legend->AddEntry(hists["DYMuNN"], " DY ");
	if(fill[tt]) legend->AddEntry(hists["TTMuNN"], "t#bar{t}");
	if(fill[zz]) legend->AddEntry(hists["ZZMuNN"], " ZZ ");
	legend->AddEntry(hists["signalMuNN"], " signal ");
	legend->Draw();
	
	// efficiency computation signal VS background
	
	mlpa_canvas->cd(3);
	double efficiency_sig[28];
	double efficiency_bg[28];

	for(int b=1;b<29;b++){
	  string namesig="signalMuNN";
	  if(NNchoice=="DY_vs_TT") namesig="DYMuNN";
	  double seff = hists[namesig]->Integral(b,29)/hists[namesig]->Integral();
	  double beff = 0;
	  for(int s = 0; s<nSamples; s++){
	    if(fill[listSample[s]]&&((listSample[s]==dy&&NNchoice!="DY_vs_TT")||listSample[s]==tt||listSample[s]==zz)) beff+=hists[labels[listSample[s]]+"MuNN"]->Integral(b,29);
	  }

	  bg_eff->SetBinContent(b,beff);
	  sig_eff->SetBinContent(b,seff); 
	  	  
	  efficiency_sig[b-1]=seff;
          efficiency_bg[b-1]=beff;
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
