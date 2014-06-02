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

using namespace std;

TChain *chain;
TChain *tree2 = new TChain("tree2");
double E_mu_reco,DeltaE_mu_reco,E_mu,Pt_antimu,DeltaPt_antimu_reco,DeltaPt_mu_reco,unsurPt_mu, unsurPt_antimu, unsurPt_mu_reco, unsurPt_antimu_reco  ;
double E_antimu_reco,DeltaE_antimu_reco,E_antimu,Pt_antimu_reco,Pt_mu_reco ,Pt_mu;

double DeltaPtInv_lm,DeltaPtInv_lp,PtInv_lrm,PtInv_lrp,PtInv_lgm,PtInv_lgp,E_lgm,E_lgp;

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
  gStyle->SetOptStat(1111111);
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
  c1->Print("File/plot_test_muon.C");                                                                                                                                                                                        
}

//---------------------------------------------------------------------------
void Range(double val_min, double val_max, TH1F *value_TH, TH1F *delta){
		// read root file
		chain=tree2;
		chain->SetBranchAddress("DeltaPtInv_lm",&DeltaPtInv_lm);
		chain->SetBranchAddress("PtInv_lrm",&PtInv_lrm);
		chain->SetBranchAddress("PtInv_lgm",&PtInv_lgm);
                chain->SetBranchAddress("E_lgm",&E_lgm);                                                                                                                                                

		chain->SetBranchAddress("DeltaPtInv_lp",&DeltaPtInv_lp);
		chain->SetBranchAddress("PtInv_lrp",&PtInv_lrp);
                chain->SetBranchAddress("PtInv_lgp",&PtInv_lgp);
                chain->SetBranchAddress("E_lgp",&E_lgp);                                                          
		
		long L=0.0;
		double a1=0.0;
		double c1=0.0;
		double b1=0.0;
		double a2=0.0;
		double c2=0.0;
		double b2=0.0; 
		//working with 1/pt

		int number_of_entries = chain->GetEntries();
		for (Int_t i=0; i<number_of_entries; i++){
			chain->GetEntry(i);
			//fill histogram
			cout<<PtInv_lgm<<" "<<DeltaPtInv_lm<<endl;
			if(PtInv_lgm> 1/val_max&& PtInv_lgm<1/val_min){
			  value_TH->Fill(PtInv_lgm);
			  delta->Fill(DeltaPtInv_lm);
			}
                        if(PtInv_lgp> 1/val_max&& PtInv_lgp<1/val_min){
			  value_TH->Fill(PtInv_lgp);
			  delta->Fill(DeltaPtInv_lp);
			}
		}

}// end of range fct

//-----------------------------------------------------------------------------

void Draw(const char *inputFile,const char *paramFile,double val_min, double val_max, double binning, double bin_min, double bin_max, int window)
{
	
	cout<<inputFile<<endl;
	cout<<paramFile<<endl;
	tree2->Reset();
	tree2->Add(inputFile);    // Loading Input File
	
	ifstream infile1(paramFile);
	Double_t param[15];
	Int_t line = 0;
        while(infile1 >> param[line]){
          line++;
		}
        infile1.close();
	
	ostringstream title;
	title<<val_max<<" < pt < "<<val_min;
	
	int nbre_bin=10*(TMath::Abs(1000*bin_min)+(1000*bin_max));
	nbre_bin=10*(TMath::Abs(1000*bin_min)+(1000*bin_max))/binning;
	
	cout<<" nbre bin "<<nbre_bin<<endl;
	
	TH1F *value_TH = new TH1F("value_TH","Energy of parton",500,0,0.5);
	TF[window] = new TH1F("transfert_fun",title.str().c_str(),nbre_bin,bin_min,bin_max);
	MC[window] = new TH1F("delta",title.str().c_str(),nbre_bin,bin_min,bin_max);


double a=0.0,b=0.0,c=0.0,aprime=0.0,d=0.0;
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
//double lim_inf = 1/val_max;
//double lim_sup = 1/val_min;



Range(val_min,val_max,value_TH,MC[window]);

for(int i=1;i<(nbre_bin+1);i++){
  double bin_size=fabs((bin_max-bin_min)/nbre_bin);
  cout<<"bin_size "<<bin_size<<endl;
double sum=0.0;
 for(int j=1;j<501;j++){
		a=0.0;
		b=0.0;
		c=0.0;
		d=0.0;
		double Eb_entry = value_TH->GetBinContent(j);
		double Eb=0.0;
		//Eb=j*0.001;
		Eb=value_TH->GetBinCenter(j);
		//diff = binning*((bin_min/binning) +(i-1));
		diff = bin_min+(bin_size*(i-1))+((bin_size/2.));
		cout<<"diff "<<diff<<endl;		
		double p1 = a0 + a1 * Eb + a2 * sqrt(Eb);
		double p2 = a3 + a4 * Eb + a5 * sqrt(Eb)  ;
		double p3 = a6 + a7 * Eb + a8 * sqrt(Eb);
		double p4 = a9 + a10 * Eb + a11 * sqrt(Eb);
		double p5 = a12 + a13 * Eb + a14 * sqrt(Eb);
			
		a= (1.0/(sqrt(2.0* TMath::Pi())*(p2 + p3 * p5)));
		b= (exp((-1.0/2.0)*(pow((diff - p1),2)/(pow(p2,2)))));
		c= (p3)* (exp((-1.0/2.0)*(pow((diff - p4),2)/(pow(p5,2)))));
		sum = sum + Eb_entry * (a*(b + c));

		}
	TF[window]->SetBinContent(i,sum);
	}
		
		
//-----------------------

 if (window==3){
   Printplot();
 }
		
}
