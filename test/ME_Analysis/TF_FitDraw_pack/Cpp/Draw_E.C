/*
 *  Draw.c
 *  
 *
 *  Created by Arnaud Pin on 18/02/09.
 *  Copyright 2009 __CP3__. All rights reserved.
 *
 */

#include "classes.C"
#include "TFile.h"

//using namespace std;

TChain *chain;
TChain *tree1 = new TChain("tree1");
double Eta_mu, phi_mu ;
double Eta_antimu, phi_antimu;
double E_mu_reco,DeltaE_mu_reco,E_mu;
double E_antimu_reco,DeltaE_antimu_reco,E_antimu;

TH1F **TF=new TH1F*[4];
TH1F **MC=new TH1F*[4];

//---------------------------------------------------------------------------
void Printplot(){

  TCanvas  *c1 = new TCanvas("c1","the fit canvas",1000,800);
  const Font_t kExRootFont = 42;
  const Float_t kExRootFontSize = 0.06;
  gStyle->SetCanvasColor(10);
  gStyle->SetPadColor(10);
  gStyle->SetFillColor(-1);
  gStyle->SetPaperSize(20, 24);
  gStyle->SetStatFont(kExRootFont);
  gStyle->SetTextFont(kExRootFont);
  gStyle->SetTextSize(kExRootFontSize);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(1);
  gStyle->SetLegendBorderSize(0);
  gStyle->SetPadBorderSize(0);
  c1->Divide(2,2);

  for(int i=0;i<4;i++){
    c1->cd(i+1);
    if(MC[i]->Integral()>0){MC[i]->Scale(1.0/(MC[i]->Integral()));}
    MC[i]->SetLineWidth(3);
    MC[i]->Draw();
    if(TF[i]->Integral()>0){TF[i]->Scale(1.0/(TF[i]->Integral()));}
    TF[i]->SetLineColor(kBlue);
    TF[i]->SetLineWidth(3);
    TF[i]->Draw("SAME");
  }
  c1->Update();                                                                                                                                                                                           

  //ostringstream tag;
  //tag<<"File/plot/"<<val_min<<"_"<<val_max<<".C";                                                                                                                                                             
  //c1->Print(tag.str().c_str());                                                                                                                                                                               
  c1->Print("File/plot_test.C");                                                                                                                                                                                        
}

//---------------------------------------------------------------------------
int Range(int val_min, int val_max, TH1F *value_TH, TH1F *delta,TH1F *value_eta ){
		// read root file
		chain=tree1;

                chain->SetBranchAddress("phi_jb",&phi_mu);
                chain->SetBranchAddress("phi_jab",&phi_antimu);
                chain->SetBranchAddress("Eta_jb",&Eta_mu);
                chain->SetBranchAddress("Eta_jab",&Eta_antimu);
		
		chain->SetBranchAddress("DeltaE_jet",&DeltaE_mu_reco);
		chain->SetBranchAddress("E_jb",&E_mu_reco);
		chain->SetBranchAddress("E_b",&E_mu);
		chain->SetBranchAddress("DeltaE_ajet",&DeltaE_antimu_reco);
		chain->SetBranchAddress("E_jb",&E_antimu_reco);
		chain->SetBranchAddress("E_jab",&E_antimu);

		long L=0.0;

		double a1=0.0;
		double c1=0.0;
		double b1=0.0;
		double a2=0.0;
		double c2=0.0;
		double b2=0.0;
                double DR=0.0;
		
                double dphi=0.0;
                double phimu=0.0;
                double phiantimu=0.0;
                double etamu=0.0;
                double etaantimu=0.0;		
		
		double Emuon=0.0;
		double Eantimuon=0.0;
		double Emuon_reco=0.0;
		double Eantimuon_reco=0.0;
		double DeltaEmu_reco=0.0;
		double DeltaEantimu_reco=0.0;

		int number_of_entries = chain->GetEntries();
		for (Int_t i=0; i<number_of_entries; ++i){
			chain->GetEntry(i);
			//fill histogram			  
			
			Emuon = E_mu;
			Eantimuon= E_antimu;
			Emuon_reco = E_mu_reco;
			Eantimuon_reco= E_antimu_reco;
 			DeltaEmu_reco= DeltaE_mu_reco;
			DeltaEantimu_reco= DeltaE_antimu_reco;

                        phimu=phi_mu;
                        phiantimu=phi_antimu;
                        etamu=Eta_mu;
                        etaantimu= Eta_antimu ;

                        dphi=phimu-phiantimu;
                        if(dphi>TMath::Pi()){
                          dphi= (2*TMath::Pi()) - dphi;			
			
			}


			if(Emuon>val_min && Emuon<val_max){
				value_TH->Fill(Emuon);			
				delta->Fill(DeltaEmu_reco);
				value_eta->Fill(etamu);

			}// end if
		        if(Eantimuon>val_min && Eantimuon<val_max){// && DR>0.006){
				value_TH->Fill(Eantimuon);				
				delta->Fill(DeltaEantimu_reco);
				value_eta->Fill(etaantimu);
				
			}// end if

		}
return 0;		
		
}

//-----------------------------------------------------------------------------

void Draw(const char *inputFile,const char *paramFile,int val_min, int val_max, int binning, int bin_min, int bin_max, int window)
{

	cout<<inputFile<<endl;
	cout<<paramFile<<endl;
	tree1->Reset();
	tree1->Add(inputFile);    // Loading Input File
	
	ifstream infile1(paramFile);
	Double_t param[15];
	Int_t line = 0;
        while(infile1 >> param[line]){
          line++;
		}
        infile1.close();
	
	ostringstream title;
	title<<val_min<<" < Ejet < "<<val_max;
	
	int nbre_bin=(abs(bin_min)+bin_max);
	nbre_bin=(abs(bin_min)+bin_max)/binning;
	TH1F *value_TH = new TH1F("value_TH","Energy of parton",500,0,500);	
	TH1F *value_eta = new TH1F("value_eta","eta of parton",42,-2.1,2.1);
	TF[window] = new TH1F("transfert_fun",title.str().c_str(),nbre_bin,bin_min,bin_max);
	MC[window] = new TH1F("delta",title.str().c_str(),nbre_bin,bin_min,bin_max);


	
double a=0.0,b=0.0,c=0.0,d=0.0;
double a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14;
//initialization of the parameters
a0=param[0];
a1=param[1];
a2=param[2];
a3=param[3];
a4=param[4];
a5=param[5];
a6=param[6];
a7=param[7];
a8=param[8];
a9=param[9];
a10=param[10];
a11=param[11];
a12=param[12];
a13=param[13];
a14=param[14];

Double_t diff=0.0;
Double_t diff2=0.0;
Range(val_min,val_max,value_TH,MC[window], value_eta);
double sum;
double sum2;
		
  for(int i=1;i<(nbre_bin+1);i++){
    a=0.0;
    b=0.0;
    c=0.0;
    d=0.0;
    sum=0;

	for(int j=1;j<501;j++){		
	  double Eb_entry = value_TH->GetBinContent(j);
	  double Eb=0.0;
	  Eb=j;
	  sum2=0.0;

	  for(int e=1; e<43 ; e++){
	  //cout <<"--------------------------------------------------------------------------------------------"<<endl;
                
		double eta_entry = value_eta->GetBinContent(e);
		double eta=0.0;
		eta=-2.1 +(e-1)*0.1;
		//cout <<"eta vaut "<<eta<<endl;		
		double s= (2*exp(-eta))/(1+exp(-2*eta));
		//cout << "s vaut "<<s<<endl;
		
		diff = binning*((bin_min/binning) +(i-1));
		diff2 = ((1/Eb)-1/(Eb-diff))*(1/s);
		if (Eb-diff>0){	
		//cout << "diff2 vaut "<<diff2<<endl;
					
		double p1 = a0 + a1 * 1/(Eb*s) + a2 * sqrt(1/(Eb*s));
		double p2 = a3 + a4 * 1/(Eb*s) + a5 * sqrt(1/(Eb*s))  ;
		double p3 = a6 + a7 * 1/(Eb*s) + a8 * sqrt(1/(Eb*s));
		double p4 = a9 + a10 * 1/(Eb*s) + a11 * sqrt(1/(Eb*s));
		double p5 = a12 + a13 * 1/(Eb*s) + a14 * sqrt(1/(Eb*s));
		
			
		a= (1/(s*pow((Eb-diff),2)))*(1.0/(sqrt(2.0* TMath::Pi())*(p2 + p3 * p5)));
		b= exp((-1.0/2.0)*(pow((diff2 - p1),2)/pow(p2,2)));
		c= (p3)* (exp((-1.0/2.0)*(pow((diff2 - p4),2)/(pow(p5,2)))));
		
		sum2 = sum2 + (eta_entry) * (a*(b + c));
		}
		
//		if (a==0 || b==0 || c==0) cout  << "a vaut "<<a<<" et b vaut "<<b<< " et c vaut "<<c<< "et diif2 vaut "<<diff2<<endl;
		//cout <<" et sum 2 vaut "<<sum2<<endl;
                }
	      //cout <<"--------------------------------------------------------------------------------------------"<<endl;
	      sum = sum + Eb_entry*sum2;
	      //cout << "sum vaut "<<sum<<endl;
	      }
	      //cout<<sum<<endl;
	TF[window]->SetBinContent(i,sum);
	}
	
	
		
//-----------------------

 if (window==3){
   Printplot();
}
		
}
