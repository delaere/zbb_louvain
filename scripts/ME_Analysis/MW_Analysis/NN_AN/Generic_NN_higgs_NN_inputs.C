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

void Neural_net_E(string dy, string zbb, string tt, string ttfulllept, string zz, string zh, TString name, TString directory, TString NNchoice, TString NNStruct, int iterations, TString cuts)
{
	if (!gROOT->GetClass("TMultiLayerPerceptron")) {
		gSystem->Load("libMLP");
	}

	// output file : control of the NN
        TFile file(directory+"/NN_"+NNchoice+"_"+name+".root","RECREATE");

	//Creation of a Tree for NN training
	TTree *simu = new TTree("Aphi","phi component of the potential");
	tree_in *sim=new tree_in();
	simu->Branch("ggweight",&sim->ggweight,"ggweight/D");
	simu->Branch("qqweight",&sim->qqweight,"qqweight/D");
	simu->Branch("zzweight",&sim->zzweight,"zzweight/D");
        simu->Branch("zz3weight",&sim->zz3weight,"zz3weight/D");
	simu->Branch("hiweight",&sim->hiweight,"hiweight/D");
        simu->Branch("hi3weight",&sim->hi3weight,"hi3weight/D");
	simu->Branch("type",&sim->type,"type/I");
        simu->Branch("type2",&sim->type2,"type2/I");
	simu->Branch("ttweight",&sim->ttweight,"ttweight/D");
	simu->Branch("deta",&sim->deta,"deta/D");
	simu->Branch("dphiZbb",&sim->dphi,"dphiZbb/D");
	simu->Branch("ptZ",&sim->ptZ,"ptZ/D");
	simu->Branch("MEptZ",&sim->MEptZ,"MEptZ/D");
	simu->Branch("ptbb",&sim->ptbb,"ptbb/D");
	simu->Branch("prodCSV",&sim->prodCSV,"prodCSV/D");
	simu->Branch("Met",&sim->Met,"Met/D");
	simu->Branch("Mll",&sim->Mll,"Mll/D");
	simu->Branch("Mbb",&sim->Mbb,"Mbb/D");

	simu->Branch("Mbb125",&sim->Mbb125,"Mbb125/D");
	simu->Branch("Mbb91",&sim->Mbb91,"Mbb91/D");
	simu->Branch("regMbb125",&sim->regMbb125,"regMbb125/D");
	simu->Branch("regMbb91",&sim->regMbb91,"regMbb91/D");
	simu->Branch("Mll91",&sim->Mll91,"Mll91/D");

	simu->Branch("regMbb",&sim->regMbb,"regMbb/D");
        simu->Branch("Multi",&sim->Multi,"Multi/I");
        simu->Branch("metsig",&sim->metsig,"metsig/D");

        simu->Branch("HvsZbb",&sim->HvsZbb,"HvsZbb/D");
        simu->Branch("HvsTT",&sim->HvsTT,"HvsTT/D");
        simu->Branch("HvsZZ",&sim->HvsZZ,"HvsZZ/D");
	simu->Branch("prodNNs",&sim->prodNNs,"prodNNs/D");

        simu->Branch("HvsZbb2j",&sim->HvsZbb2j,"HvsZbb2j/D");
        simu->Branch("HvsTT2j",&sim->HvsTT2j,"HvsTT2j/D");
        simu->Branch("HvsZZ2j",&sim->HvsZZ2j,"HvsZZ2j/D");
	simu->Branch("prodNNs2j",&sim->prodNNs2j,"prodNNs2j/D");

        simu->Branch("HvsZbb3j",&sim->HvsZbb3j,"HvsZbb3j/D");
        simu->Branch("HvsTT3j",&sim->HvsTT3j,"HvsTT3j/D");
        simu->Branch("HvsZZ3j",&sim->HvsZZ3j,"HvsZZ3j/D");
	simu->Branch("prodNNs3j",&sim->prodNNs3j,"prodNNs3j/D");

        simu->Branch("ZZvsDY2j",&sim->ZZvsDY2j,"ZZvsDY2j/D");
        simu->Branch("ZZvsDY3j",&sim->ZZvsDY3j,"ZZvsDY3j/D");
        simu->Branch("ZZvsTT2j",&sim->ZZvsTT2j,"ZZvsTT2j/D");
        simu->Branch("ZZvsTT3j",&sim->ZZvsTT3j,"ZZvsTT3j/D");

	simu->Branch("evtWeight",&sim->evtWeight,"evtWeight/D");
	simu->Branch("trijetMdr",&sim->trijetMdr,"trijetMdr/D");
	simu->Branch("fsrDR",&sim->fsrDR,"fsrDR/D");
	simu->Branch("dijetdR",&sim->dijetdR,"dijetdR/D");

	// open file to get nbres of entries

	TString totcuts("rc_eventSelection_17_idx==1");
	totcuts+=cuts;
	cout<<"cut on : "<<totcuts<<endl;
        
	std::map<string,int> Ni;
	size_t pos = dy.find("DY");
	string stmp = dy;
	string dy50to70 = stmp.replace(pos,2,"DY50-70"); stmp = dy; string dy70to100 = stmp.replace(pos,2,"DY70-100"); stmp = dy; string dy100 = stmp.replace(pos,2,"DY100"); stmp = dy; string dy180 = stmp.replace(pos,2,"DY180");
	stmp = dy; string dy1j = stmp.replace(pos,2,"DY1j"); stmp = dy; string dy2j = stmp.replace(pos,2,"DY2j"); stmp = dy; string dy3j = stmp.replace(pos,2,"DY3j"); //stmp = dy; string dy4j = stmp.replace(pos,2,"DY4j");
	string listSample[]={dy,zbb,tt,ttfulllept,zz,zh,dy50to70,dy70to100,dy100,dy180,dy1j,dy2j,dy3j};
	int nSamples = 6+4+3;
	std::map<string,int> sampleID;
	sampleID[dy]=1; sampleID[zbb]=1; sampleID[tt]=2; sampleID[ttfulllept]=2; sampleID[zz]=3; sampleID[zh]=5;
	sampleID[dy50to70]=1; sampleID[dy70to100]=1; sampleID[dy100]=1; sampleID[dy180]=1;
	sampleID[dy1j]=1; sampleID[dy2j]=1; sampleID[dy3j]=1; //sampleID[dy4j]=1; 
	std::map<string,int> fill;
	fill[dy50to70]=0; fill[dy70to100]=0; fill[dy100]=0; fill[dy180]=0;
	fill[dy1j]=0; fill[dy2j]=0; fill[dy3j]=0; //fill[dy4j]=0;
	if(NNchoice.Contains("Higgs_vs_Bkg") || NNchoice.Contains("ZHAll")) {fill[dy]=1; fill[zbb]=1; fill[tt]=1; fill[ttfulllept]=1; fill[zz]=1; fill[zh]=1;}
	if(NNchoice=="Higgs_vs_DY" || NNchoice.Contains("ZHDY")) {fill[dy]=1; fill[zbb]=1; fill[tt]=0; fill[ttfulllept]=0; fill[zz]=0; fill[zh]=1;}
	if(NNchoice=="Higgs_vs_TT" || NNchoice.Contains("ZHTT")) {fill[dy]=0; fill[zbb]=0; fill[tt]=1; fill[ttfulllept]=1; fill[zz]=0; fill[zh]=1;}
	if(NNchoice=="Higgs_vs_ZZ" || NNchoice.Contains("ZHZZ")) {fill[dy]=0; fill[zbb]=0; fill[tt]=0; fill[ttfulllept]=0; fill[zz]=1; fill[zh]=1;}
	if(NNchoice=="DY_vs_TT" || NNchoice.Contains("DYTT")) {fill[dy]=1; fill[zbb]=1; fill[tt]=1; fill[ttfulllept]=1; fill[zz]=0; fill[zh]=0;}
	if(NNchoice=="ZZ_vs_DY" || NNchoice.Contains("ZZDY")) {fill[dy]=1; fill[zbb]=1; fill[tt]=0; fill[ttfulllept]=0; fill[zz]=1; fill[zh]=0;}
	if(NNchoice=="ZZ_vs_TT" || NNchoice.Contains("ZZTT")) {fill[dy]=0; fill[zbb]=0; fill[tt]=1; fill[ttfulllept]=1; fill[zz]=1; fill[zh]=0;}
	if(NNchoice.Contains("ZZ_vs_Bkg") || NNchoice.Contains("ZZAll")) {fill[dy]=1; fill[zbb]=1; fill[tt]=1; fill[ttfulllept]=1; fill[zz]=1; fill[zh]=0;}
	//if(NNchoice.Contains("BDT")) {fill[dy]=1; fill[zbb]=1; fill[tt]=1; fill[ttfulllept]=1; fill[zz]=1; fill[zh]=1;}
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
	  else if((listSample[s]==dy||listSample[s]==zbb) && (NNchoice=="DY_vs_TT" || NNchoice.Contains("DYTT"))) isSignal = 1;
	  else if(listSample[s]==zz && (NNchoice.Contains("ZZ_vs_") || NNchoice.Contains("BDTZZ") || NNchoice.Contains("BDTZZAll"))) isSignal = 1;
	  Input(listSample[s], var[listSample[s]], sim, simu, fill[listSample[s]], isSignal, sampleID[listSample[s]], totcuts);
	}
	simu->Write();
	// Tree SIMU for NN training filled

	// Declaration of multiplayer perceptron object. input variable = branch of simu tree. Not all at the same time. To add a branch as input add @branchname. then : intermediate layer node, put : to add new layer. Ended by : @type mean that outup is 1 or 0. Then we specify the number of entries for training and test samples.
	int Dy=var[zbb]->evt_nbr[0]+var[dy]->evt_nbr[0];//+var[dy1j]->evt_nbr[0]+var[dy2j]->evt_nbr[0]+var[dy3j]->evt_nbr[0];
	int Tt=var[ttfulllept]->evt_nbr[0]+var[tt]->evt_nbr[0];
	int Zz=var[zz]->evt_nbr[0];
	int Hi=var[zh]->evt_nbr[0];
	ostringstream osdy,ostt,oszz,oszh;
	osdy << Dy;ostt << Tt;oszz << Zz;oszh << Hi;
	TString normZH= oszh.str();TString normDY= osdy.str();TString normTT= ostt.str();TString normZZ= oszz.str();

	cout<<Dy<<" "<<Tt<<" "<<Zz<<" "<<Hi<<endl;

	TMultiLayerPerceptron *mlp = new TMultiLayerPerceptron();
	//ZH vs Bkg
	if(NNchoice=="Higgs_vs_Bkg") mlp = new TMultiLayerPerceptron("@HvsZbb,@HvsZZ,@HvsTT"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+"))",simu,"Entry$%2!=0","Entry$%2==0");
	if(NNchoice=="Higgs_vs_Bkg_2j") mlp = new TMultiLayerPerceptron("@HvsZbb2j,@HvsZZ2j,@HvsTT2j"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+"))",simu,"Entry$%2!=0","Entry$%2==0");
	if(NNchoice=="Higgs_vs_Bkg_3j") mlp = new TMultiLayerPerceptron("@HvsZbb3j,@HvsZZ3j,@HvsTT3j"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+"))",simu,"Entry$%2!=0","Entry$%2==0");
	//ZH vs ...
	if(NNchoice=="Higgs_vs_DY"){mlp = new TMultiLayerPerceptron("@ggweight,@qqweight,@hiweight,@hi3weight"+NNStruct+":type!","(type2==5)/"+normZH+"+(type2==1)/"+normDY+"",simu,"Entry$%2!=0","Entry$%2==0");}
	if(NNchoice=="Higgs_vs_TT"){mlp = new TMultiLayerPerceptron("@ttweight,@hiweight,@hi3weight"+NNStruct+":type!","(type2==5)/"+normZH+"+(type2==2)/"+normTT+"",simu,"Entry$%2!=0","Entry$%2==0");}
	if(NNchoice=="Higgs_vs_ZZ"){mlp = new TMultiLayerPerceptron("@zzweight,@zz3weight,@hiweight,@hi3weight"+NNStruct+":type!","(type2==5)/"+normZH+"+(type2==3)/"+normZZ+"",simu,"Entry$%2!=0","Entry$%2==0");}
	if(NNchoice=="DY_vs_TT"){mlp = new TMultiLayerPerceptron("@ggweight,@qqweight,@ttweight"+NNStruct+":type!","(type2==1)/"+normDY+"+(type2==2)/"+normTT+"",simu,"Entry$%2!=0","Entry$%2==0");}
	//ZZ vs ...
	if(NNchoice=="ZZ_vs_DY"){mlp = new TMultiLayerPerceptron("@ggweight,@qqweight,@zzweight,@zz3weight"+NNStruct+":type!","(type2==3)/"+normZZ+"+(type2==1)/"+normDY+"",simu,"Entry$%2!=0","Entry$%2==0");}
	if(NNchoice=="ZZ_vs_TT"){mlp = new TMultiLayerPerceptron("@ttweight,@zzweight,@zz3weight"+NNStruct+":type!","(type2==3)/"+normZZ+"+(type2==2)/"+normTT+"",simu,"Entry$%2!=0","Entry$%2==0");}
	if(NNchoice=="ZZ_vs_Bkg_2j") mlp = new TMultiLayerPerceptron("@ZZvsDY2j,@ZZvsTT2j"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(1.1/"+normZZ+"))",simu,"Entry$%2!=0","Entry$%2==0");
	if(NNchoice=="ZZ_vs_Bkg_3j") mlp = new TMultiLayerPerceptron("@ZZvsDY3j,@ZZvsTT3j"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(1.1/"+normZZ+"))",simu,"Entry$%2!=0","Entry$%2==0");
	//ZH vs Bkg only weights
	if(NNchoice=="Higgs_vs_Bkg_7w") mlp = new TMultiLayerPerceptron("@ggweight,@qqweight,@hiweight,@hi3weight,@ttweight,@zzweight,@zz3weight"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+"))",simu,"Entry$%2!=0","Entry$%2==0");

	if(NNchoice=="Higgs_vs_Bkg_5w") mlp = new TMultiLayerPerceptron("@ggweight,@qqweight,@ttweight,@zzweight,@zz3weight"+NNStruct+":type!","1.0*((type2==1)*(0.887/"+normDY+")+(type2==2)*(0.095/"+normTT+")+(type2==3)*(0.018/"+normZZ+")+(type2==5)*(1.2/"+normZH+"))",simu,"Entry$%2!=0","Entry$%2==0");



	int nIn = 3;
	if(NNchoice=="Higgs_vs_DY" || NNchoice=="Higgs_vs_ZZ" || NNchoice=="ZZ_vs_DY") nIn=4;
	if(NNchoice=="Higgs_vs_Bkg_7w") nIn=7;
	if(NNchoice=="Higgs_vs_Bkg_5w") nIn=5;
	if(NNchoice.Contains("ZZ_vs_Bkg")) nIn=2;
	if(NNchoice.Contains("BDT")) nIn=0;
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
	}
	Double_t params[nIn+vNNinputs.size()]; // to change according to the number of input in the NN; Order must be the same as teh one for NN training !!!
	Float_t fparams[nIn+vNNinputs.size()]; // to change according to the number of input in the NN; Order must be the same as teh one for NN training !!!
	cout<<"params size "<<nIn+vNNinputs.size()<<endl;

	TCanvas* mlpa_canvas = new TCanvas("mlpa_canvas","Network analysis"); // For NN output
	mlpa_canvas->Divide(2,2);

	// http://tmva.sourceforge.net/optionRef.html
	//TMVA::Factory * bdt = new TMVA::Factory("higgs", &file,"!V:Transformations=I;N;D"); //D means decorrelation
	TMVA::Factory * tmva; 
	TMVA::Reader * reader; 
	if(NNchoice.Contains("BDT")){
	  tmva = new TMVA::Factory("higgs", &file,"!V");
	  //tmva = new TMVA::Factory("higgs", &file,"!V:Transformations=I;N;D"); //D means decorrelation

	  for (unsigned int i=0; i<vNNinputs.size(); i++){
	    tmva->AddVariable(vNNinputs[i].c_str(), 'D');
	  }

	  if(NNchoice.Contains("ZHAll")) {tmva->AddSignalTree(simu->CopyTree("type2==5"),1.2/Hi); tmva->AddBackgroundTree(simu->CopyTree("type2==1"),0.887/Dy); tmva->AddBackgroundTree(simu->CopyTree("type2==2"),0.095/Tt); tmva->AddBackgroundTree(simu->CopyTree("type2==3"),0.018/Zz);}
	  else if(NNchoice.Contains("ZZAll")) {tmva->AddBackgroundTree(simu->CopyTree("type2==1"),0.9/Dy); tmva->AddBackgroundTree(simu->CopyTree("type2==2"),0.1/Tt); tmva->AddSignalTree(simu->CopyTree("type2==3"),1.2/Zz);}
	  else if(NNchoice.Contains("DYTT")) {tmva->AddSignalTree(simu->CopyTree("type2==1"),1./Dy); tmva->AddBackgroundTree(simu->CopyTree("type2==2"),1./Tt);}
	  else if(NNchoice.Contains("ZZDY")) {tmva->AddSignalTree(simu->CopyTree("type2==3"),1./Zz); tmva->AddBackgroundTree(simu->CopyTree("type2==1"),1./Dy);}
	  else if(NNchoice.Contains("ZZTT")) {tmva->AddSignalTree(simu->CopyTree("type2==3"),1./Zz); tmva->AddBackgroundTree(simu->CopyTree("type2==2"),1./Tt);}
	  else if(NNchoice.Contains("ZHDY")) {tmva->AddSignalTree(simu->CopyTree("type2==5"),1./Hi); tmva->AddBackgroundTree(simu->CopyTree("type2==1"),1./Dy);}
	  else if(NNchoice.Contains("ZHTT")) {tmva->AddSignalTree(simu->CopyTree("type2==5"),1./Hi); tmva->AddBackgroundTree(simu->CopyTree("type2==2"),1./Tt);}
	  else if(NNchoice.Contains("ZHZZ")) {tmva->AddSignalTree(simu->CopyTree("type2==5"),1./Hi); tmva->AddBackgroundTree(simu->CopyTree("type2==3"),1./Zz);}
	  
	  //tmva->PrepareTrainingAndTestTree(TCut("type2==5"), TCut("type2!=5"), "nTrain_Signal=350:nTest_Signal=350:nTrain_Background=350:nTest_Background=350:!V");
	  //tmva->PrepareTrainingAndTestTree(TCut("type2==5"), TCut("type2!=5"), "nTrain_Signal=0:nTest_Signal=0:nTrain_Background=0:nTest_Background=0:SplitMode=Random:NormMode=NumEvents:!V");
	  //tmva->PrepareTrainingAndTestTree(TCut("type2==5"), TCut("type2!=5"), "nTrain_Signal=0:nTest_Signal=0:nTrain_Background=0:nTest_Background=0:SplitMode=Random:NormMode=None:!V");
	  tmva->PrepareTrainingAndTestTree(TCut("type==1"), TCut("type!=1"), "nTrain_Signal=0:nTest_Signal=0:nTrain_Background=0:nTest_Background=0:SplitMode=Random:NormMode=None:!V");
	  ostringstream iter;
	  TString Iter= iter.str();	  
	  tmva->BookMethod(TMVA::Types::kBDT, NNchoice+"_"+name, "!V:BoostType=AdaBoost:NTrees="+Iter+":nEventsMin=50:nCuts=20");
	  //tmva->BookMethod(TMVA::Types::kBDT, "BDT2", "!V:BoostType=AdaBoost:NTrees=50:nEventsMin=50:nCuts=20");
	  //tmva->BookMethod(TMVA::Types::kBDT, "BDT3", "!V:BoostType=AdaBoost:NTrees=100:nEventsMin=50:nCuts=20");
	  //tmva->BookMethod(TMVA::Types::kBDT, "BDT4", "!V:BoostType=AdaBoost:NTrees=150:nEventsMin=50:nCuts=20");
	  //tmva->BookMethod(TMVA::Types::kBDT, "BDT5", "!V:BoostType=AdaBoost:NTrees=400:nEventsMin=50:nCuts=20");

	  //tmva->BookMethod(TMVA::Types::kMLP, "BDT", "!H:!V:VarTransform=N:HiddenLayers=N-1:NCycles=500:TrainingMethod=BFGS");
	  //tmva->BookMethod(TMVA::Types::kMlpANN, "TMLP", "!H:!V:VarTransform=N:HiddenLayers=3:NCycles=500:TrainingMethod=BFGS");
	  
	  tmva->TrainAllMethods();
	  tmva->TestAllMethods();
	  tmva->EvaluateAllMethods();

	  reader = new TMVA::Reader("!Color:!Silent");
	  mlpa_canvas->cd(1);
	  // shows the network structure
	  mlpa_canvas->cd(2);

	  //file.Close();
	  //return;
	}
	else{
	  // Function of the NN is exported in python. AND in c++ code (in NN directory) Function to use to evaluate NN
	  mlp->Train(iterations, "text,graph,update=2");
	  mlp->Export((directory+"/MLP_"+NNchoice+"_"+name).ReplaceAll("-","_"),"python");
	  mlp->Export((directory+"/MLP_"+NNchoice+"_"+name).ReplaceAll("-","_"),"c++");
	  mlp->Write();
	  
	  // Use TMLPAnalyzer to see what it looks for. INFO will be in the contro root file
	  TCanvas* kin = new TCanvas("kin","kin"); // for kin Variable
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
	}

	std::map<string,TH1F*> hists;
	string channel[] = {"Mu","EE"};
	string hname[] = {"NN","prod"};
	int nDYbins = 5;
	string DYbins[] = {"0to50","50to70","70to100","100to180","180toInf"};
	std::map<string,int> limDYbins;
	limDYbins["0to50"]=50; limDYbins["50to70"]=70; limDYbins["70to100"]=100; limDYbins["100to180"]=180; limDYbins["180toInf"]=99999;
	std::map<string,string> labels;
	labels[dy]="DY"; labels[zbb]="Zbb"; labels[tt]="TT"; labels[ttfulllept]="TT-FullLept"; labels[zz]="ZZ"; labels[zh]="signal";
	labels[dy50to70]="DY50-70"; labels[dy70to100]="DY70-100"; labels[dy100]="DY100"; labels[dy180]="DY180";
	labels[dy1j]="DY1j"; labels[dy2j]="DY2j"; labels[dy3j]="DY3j"; //labels[dy4j]="DY4j";
	int nbins = 28;
	if(NNchoice.Contains("BDT")) nbins = 40;
	for(int s = 0; s<nSamples; s++){
	  for(int c = 0; c<2; c++){
	    for(int n = 0; n<2; n++){
	      if(!(NNchoice.Contains("BDT"))) hists[labels[listSample[s]]+channel[c]+hname[n]] = new TH1F((labels[listSample[s]]+channel[c]+hname[n]).c_str(), (hname[n]+" output").c_str(), nbins, -0.2, 1.2);
	      else hists[labels[listSample[s]]+channel[c]+hname[n]] = new TH1F((labels[listSample[s]]+channel[c]+hname[n]).c_str(), (hname[n]+" output").c_str(), nbins, -1, 1);
	      hists[labels[listSample[s]]+channel[c]+hname[n]]->SetDirectory(0);
	      for(int iDY = 0; iDY<nDYbins; iDY++){
		if(listSample[s].find("DY")!=dy.find("DY")) break;
		if(!(NNchoice.Contains("BDT"))) hists[labels[listSample[s]]+DYbins[iDY]+channel[c]+hname[n]] = new TH1F((labels[listSample[s]]+DYbins[iDY]+channel[c]+hname[n]).c_str(), (hname[n]+" output").c_str(), nbins, -0.2, 1.2);
		else hists[labels[listSample[s]]+DYbins[iDY]+channel[c]+hname[n]] = new TH1F((labels[listSample[s]]+DYbins[iDY]+channel[c]+hname[n]).c_str(), (hname[n]+" output").c_str(), nbins, -1, 1);
		hists[labels[listSample[s]]+DYbins[iDY]+channel[c]+hname[n]]->SetDirectory(0);
	      }
	    }
	  }
	}

	// histo of efficiency
	TH1F *bg_eff = new TH1F("bgh", "NN output", nbins, -0.2, 1.2);
	TH1F *sig_eff = new TH1F("sigh", "NN output", nbins, -0.2, 1.2);	

	//-------------------------------------------------------------------------

	if(NNchoice.Contains("BDT")){
	  bg_eff = new TH1F("bgh", "NN output", nbins, -1, 1);
	  sig_eff = new TH1F("sigh", "NN output", nbins, -1, 1);
	  for (unsigned int i=0; i<vNNinputs.size(); i++){
            reader->AddVariable(vNNinputs[i].c_str(), &fparams[i]);
          }
	  reader->BookMVA("BDT", "weights/higgs_"+NNchoice+"_"+name+".weights.xml");
	}

	for(int s = 0; s<nSamples; s++){
	  for (int i=0;i<Ni[listSample[s]]; ++i) {
	    if(NNchoice=="Higgs_vs_Bkg") {params[0] = var[listSample[s]]->hzbb[i]; params[1] = var[listSample[s]]->hzz[i]; params[2] = var[listSample[s]]->htt[i];}
	    if(NNchoice=="Higgs_vs_Bkg_2j") {params[0] = var[listSample[s]]->hzbb_2j[i]; params[1] = var[listSample[s]]->hzz_2j[i]; params[2] = var[listSample[s]]->htt_2j[i];}
	    if(NNchoice=="Higgs_vs_Bkg_3j") {params[0] = var[listSample[s]]->hzbb_3j[i]; params[1] = var[listSample[s]]->hzz_3j[i]; params[2] = var[listSample[s]]->htt_3j[i];}
	    if(NNchoice=="Higgs_vs_DY") {params[0] = var[listSample[s]]->gg[i]; params[1] = var[listSample[s]]->qq[i]; params[2] = var[listSample[s]]->hi[i]; params[3] = var[listSample[s]]->hi3[i];}
	    if(NNchoice=="Higgs_vs_TT") {params[0] = var[listSample[s]]->tt[i]; params[1] = var[listSample[s]]->hi[i]; params[2] = var[listSample[s]]->hi3[i];}
	    if(NNchoice=="Higgs_vs_ZZ") {params[0] = var[listSample[s]]->zz[i]; params[1] = var[listSample[s]]->zz3[i]; params[2] = var[listSample[s]]->hi[i]; params[3] = var[listSample[s]]->hi3[i];}
	    if(NNchoice=="DY_vs_TT") {params[0] = var[listSample[s]]->gg[i]; params[1] = var[listSample[s]]->qq[i]; params[2] = var[listSample[s]]->tt[i];}


	    if(NNchoice=="ZZ_vs_DY") {params[0] = var[listSample[s]]->gg[i]; params[1] = var[listSample[s]]->qq[i]; params[2] = var[listSample[s]]->zz[i]; params[3] = var[listSample[s]]->zz3[i];}
	    if(NNchoice=="ZZ_vs_TT") {params[0] = var[listSample[s]]->tt[i]; params[1] = var[listSample[s]]->zz[i]; params[2] = var[listSample[s]]->zz3[i];}
	    if(NNchoice=="ZZ_vs_Bkg_2j") {params[0] = var[listSample[s]]->zzdy_2j[i]; params[1] = var[listSample[s]]->zztt_2j[i];}
	    if(NNchoice=="ZZ_vs_Bkg_3j") {params[0] = var[listSample[s]]->zzdy_3j[i]; params[1] = var[listSample[s]]->zztt_3j[i];}


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
	      else if(vNNinputs[j]=="ggweight") params[nIn+j] = var[listSample[s]]->gg[i];
	      else if(vNNinputs[j]=="qqweight") params[nIn+j] = var[listSample[s]]->qq[i];
	      else if(vNNinputs[j]=="ttweight") params[nIn+j] = var[listSample[s]]->tt[i];
	      else if(vNNinputs[j]=="zzweight") params[nIn+j] = var[listSample[s]]->zz[i];
	      else if(vNNinputs[j]=="zz3weight") params[nIn+j] = var[listSample[s]]->zz3[i];
	      else if(vNNinputs[j]=="hiweight") params[nIn+j] = var[listSample[s]]->hi[i];
	      else if(vNNinputs[j]=="hi3weight") params[nIn+j] = var[listSample[s]]->hi3[i];

	      else if(vNNinputs[j]=="HvsZbb2j") params[nIn+j] = var[listSample[s]]->hzbb_2j[i];
	      else if(vNNinputs[j]=="HvsTT2j") params[nIn+j] = var[listSample[s]]->htt_2j[i];
	      else if(vNNinputs[j]=="HvsZZ2j") params[nIn+j] = var[listSample[s]]->hzz_2j[i];
	      else if(vNNinputs[j]=="HvsZbb3j") params[nIn+j] = var[listSample[s]]->hzbb_3j[i];
	      else if(vNNinputs[j]=="HvsTT3j") params[nIn+j] = var[listSample[s]]->htt_3j[i];
	      else if(vNNinputs[j]=="HvsZZ3j") params[nIn+j] = var[listSample[s]]->hzz_3j[i];

	      else if(vNNinputs[j]=="ZZvsDY2j") params[nIn+j] = var[listSample[s]]->zzdy_2j[i];
	      else if(vNNinputs[j]=="ZZvsDY3j") params[nIn+j] = var[listSample[s]]->zzdy_3j[i];
	      else if(vNNinputs[j]=="ZZvsTT2j") params[nIn+j] = var[listSample[s]]->zztt_2j[i];
	      else if(vNNinputs[j]=="ZZvsTT3j") params[nIn+j] = var[listSample[s]]->zztt_3j[i];

	      else if(vNNinputs[j]=="prodNNs2j") params[nIn+j] = var[listSample[s]]->prodNNs_2j[i];
	      else if(vNNinputs[j]=="prodNNs3j") params[nIn+j] = var[listSample[s]]->prodNNs_3j[i];
	      else if(vNNinputs[j]=="ptZ") params[nIn+j] = var[listSample[s]]->ptZ[i];
	      else if(vNNinputs[j]=="ptbb") params[nIn+j] = var[listSample[s]]->ptbb[i];
	      else if(vNNinputs[j]=="Mll") params[nIn+j] = var[listSample[s]]->Mll[i];
	      else if(vNNinputs[j]=="Mbb125") params[nIn+j] = var[listSample[s]]->Mbb125[i];
	      else if(vNNinputs[j]=="Mbb91") params[nIn+j] = var[listSample[s]]->Mbb91[i];
	      else if(vNNinputs[j]=="regMbb125") params[nIn+j] = var[listSample[s]]->regMbb125[i];
	      else if(vNNinputs[j]=="regMbb91") params[nIn+j] = var[listSample[s]]->regMbb91[i];
	      else if(vNNinputs[j]=="Mll91") params[nIn+j] = var[listSample[s]]->Mll91[i];

	      else cout<<"Variable added the NN not known, please add it in the code"<<endl;
	      fparams[nIn+j] = float(params[nIn+j]);
	    }
	    string ch = "EE";
	    if(var[listSample[s]]->isMuMu[i]){
	      ch = "Mu";
	    }	 
	    if(!(NNchoice.Contains("BDT"))) hists[labels[listSample[s]]+ch+"NN"]->Fill(mlp->Evaluate(0, params),var[listSample[s]]->evtWeight[i]);
	    else hists[labels[listSample[s]]+ch+"NN"]->Fill(reader->EvaluateMVA("BDT"),var[listSample[s]]->evtWeight[i]);
	    if(nIn>2) hists[labels[listSample[s]]+ch+"prod"]->Fill(params[0]*params[1]*params[2],var[listSample[s]]->evtWeight[i]);
	    else hists[labels[listSample[s]]+ch+"prod"]->Fill(params[0]*params[1],var[listSample[s]]->evtWeight[i]);
	    for(int iDY = 0; iDY<nDYbins; iDY++){
	      if(listSample[s].find("DY")!=dy.find("DY")) break;
	      if(var[listSample[s]]->MEptZ[i]>=limDYbins[DYbins[iDY]]) continue;
	      if(!(NNchoice.Contains("BDT"))) hists[labels[listSample[s]]+DYbins[iDY]+ch+"NN"]->Fill(mlp->Evaluate(0, params),var[listSample[s]]->evtWeight[i]);
	      else hists[labels[listSample[s]]+DYbins[iDY]+ch+"NN"]->Fill(reader->EvaluateMVA("BDT"),var[listSample[s]]->evtWeight[i]);
	      hists[labels[listSample[s]]+DYbins[iDY]+ch+"prod"]->Fill(params[0]*params[1]*params[2],var[listSample[s]]->evtWeight[i]);
	      break;
	    }
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
	      for(int iDY = 0; iDY<nDYbins; iDY++){
		if(listSample[s].find("DY")!=dy.find("DY")) break;
		hists[labels[listSample[s]]+DYbins[iDY]+channel[c]+hname[n]]->SetName((Name+labels[listSample[s]]+DYbins[iDY]+"125").c_str());
		hists[labels[listSample[s]]+DYbins[iDY]+channel[c]+hname[n]]->Write();
	      }
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
	if(NNchoice.Contains("Higgs_vs_Bkg") || NNchoice.Contains("BDT")){
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
	if(fill[zz]&&!NNchoice.Contains("ZZ_vs_")) hs->Add(hists["ZZMuNN"]);

	hs->Draw();
	if(NNchoice!="DY_vs_TT" && (!NNchoice.Contains("ZZ_vs_")) && (!NNchoice.Contains("BDTZZ"))) hists["signalMuNN"]->Draw("same");	
	else if(NNchoice=="DY_vs_TT") {hists["DYMuNN"]->SetFillColor(0); hists["DYMuNN"]->Draw("same");}
	else {hists["ZZMuNN"]->SetFillColor(0); hists["ZZMuNN"]->Draw("same");}

	TLegend *legend = new TLegend(.75, .80, .95, .95);
	if(fill[zbb]&&NNchoice!="DY_vs_TT") legend->AddEntry(hists["DYMuNN"], " DY ");
	if(fill[tt]) legend->AddEntry(hists["TTMuNN"], "t#bar{t}");
	if(fill[zz]&&!NNchoice.Contains("ZZ_vs_")) legend->AddEntry(hists["ZZMuNN"], " ZZ ");
	legend->AddEntry(hists["signalMuNN"], " signal ");
	legend->Draw();
	
	// efficiency computation signal VS background
	
	mlpa_canvas->cd(3);
	double efficiency_sig[nbins];
	double efficiency_bg[nbins];

	for(int b=1;b<nbins+1;b++){
	  string namesig="signalMuNN";
	  if(NNchoice=="DY_vs_TT") namesig="DYMuNN";
	  if(NNchoice.Contains("ZZ_vs_")) namesig="ZZMuNN";
	  double seff = hists[namesig]->Integral(b,nbins+1)/hists[namesig]->Integral();
	  double beff = 0;
	  for(int s = 0; s<nSamples; s++){
	    if(fill[listSample[s]]&&((listSample[s]==dy&&NNchoice!="DY_vs_TT")||listSample[s]==tt||(listSample[s]==zz&&!NNchoice.Contains("ZZ_vs_")))) beff+=hists[labels[listSample[s]]+"MuNN"]->Integral(b,nbins+1);
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
	TGraph *Eff = new TGraph(nbins,efficiency_sig,efficiency_bg);
	Eff->Draw("AP");
	Eff->Write();

	mlpa_canvas->Write();

	file.Close();
}
