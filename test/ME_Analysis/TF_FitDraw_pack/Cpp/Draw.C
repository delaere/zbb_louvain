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
double E_jb,DeltaE_jet,E_b,phi_jb ,Eta_jb ;
double E_jab,DeltaE_ajet,E_ab,phi_jab , Eta_jab;


TH1F **TF=new TH1F*[4];
TH1F **MC=new TH1F*[4];

//---------------------------------------------------------------------------
void Printplot(){

  TCanvas  *c1 = new TCanvas("c1","the fit canvas",1000,800);
  const Font_t kExRootFont = 42;
  const Float_t kExRootFontSize = 0.06;
  gStyle->SetCanvasColor(0);
  gStyle->SetPadColor(10);
  gStyle->SetFillColor(-1);
  gStyle->SetPaperSize(20, 24);
  gStyle->SetStatFont(kExRootFont);
  gStyle->SetTextFont(kExRootFont);
  gStyle->SetTextSize(kExRootFontSize);
  //gStyle->SetBorderSize(0);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(1);
  gStyle->SetLegendBorderSize(0);
  gStyle->SetPadBorderSize(0);
  c1->Divide(2,2);

  for(int i=0;i<4;i++){
    c1->cd(i+1);
    if(MC[i]->Integral()>0){MC[i]->Scale(1.0/(MC[i]->Integral()));}
    MC[i]->SetLineWidth(3);
    MC[i]->SetXTitle("E eGEN - E eRECO [GeV]");
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
  c1->Print("File/plot_del_test.C");                                                                                                                                                                                        
}

//---------------------------------------------------------------------------
void Range(int val_min, int val_max, TH1F *value_TH, TH1F *delta){
		// read root file
		chain=tree1;
		
		chain->SetBranchAddress("DeltaE_jet",&DeltaE_jet);
		chain->SetBranchAddress("E_jb",&E_jb);
		chain->SetBranchAddress("E_b",&E_b);
		chain->SetBranchAddress("DeltaE_ajet",&DeltaE_ajet);
		chain->SetBranchAddress("E_jab",&E_jab);
		chain->SetBranchAddress("E_ab",&E_ab);
                chain->SetBranchAddress("phi_jb",&phi_jb);
                chain->SetBranchAddress("phi_jab",&phi_jab);
                chain->SetBranchAddress("Eta_jb",&Eta_jb);
                chain->SetBranchAddress("Eta_jab",&Eta_jab);
		/*
		chain->SetBranchAddress("DeltaE_mu_reco",&DeltaE_jet);                                                                    
                chain->SetBranchAddress("E_mu_reco",&E_jb);                                                                                       
                chain->SetBranchAddress("E_mu",&E_b);                                                                                              
                chain->SetBranchAddress("DeltaE_antimu_reco",&DeltaE_ajet);                                                                    
                chain->SetBranchAddress("E_antimu_reco",&E_jab);                                                                                  
                chain->SetBranchAddress("E_antimu",&E_ab);                                                                                       
                chain->SetBranchAddress("phi_mu_reco",&phi_jb);                                                                                   
                chain->SetBranchAddress("phi_antimu_reco",&phi_jab);                                                                              
                chain->SetBranchAddress("Eta_mu_reco",&Eta_jb);                                                                                   
                chain->SetBranchAddress("Eta_antimu_reco",&Eta_jab);
		*/
		long L=0.0;
		double Eb=0.0;
		double Eab=0.0;
		double Ejb=0.0;
		double Ejab=0.0;
		double diffb=0.0;
		double diffab=0.0;
		double a1=0.0;
		double c1=0.0;
		double b1=0.0;
		double a2=0.0;
		double c2=0.0;
		double b2=0.0;
                double DR=0.0;
                double dphi=0.0;
                double phijb=0.0;
                double phijab=0.0;
                double etajb=0.0;
                double etajab=0.0;

		
		int number_of_entries = chain->GetEntries();
		for (Int_t i=0; i<number_of_entries; ++i){
			chain->GetEntry(i);
			//fill histogram
			Eb = E_b;
			Eab= E_ab;
			Ejb = 1.0*E_jb;
			Ejab= 1.0*E_jab;
			diffb =  DeltaE_jet;
			diffab= DeltaE_ajet;
                        phijb=phi_jb;
                        phijab=phi_jab;
                        etajb=Eta_jb;
                        etajab= Eta_jab ;

                        dphi=phijb-phijab;
                        if(dphi>TMath::Pi()){
                          dphi= (2*TMath::Pi()) - dphi;
			}

                        DR=sqrt(pow(etajb-etajab,2)+pow(dphi,2));

			if(E_b>val_min && E_b<val_max && fabs(etajb)>1.6 && Ejb>0){
				value_TH->Fill(E_b);			
				delta->Fill(diffb);
				}// end if
			if(E_ab>val_min && E_ab<val_max && fabs(etajab)>1.6 && Ejb>0){
				value_TH->Fill(E_ab);				
				delta->Fill(diffab);
			}// end if

		}
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
	title<<val_min<<" < E eGEN < "<<val_max;
	
	int nbre_bin=(abs(bin_min)+bin_max);
	nbre_bin=(abs(bin_min)+bin_max)/binning;
	
	TH1F *value_TH = new TH1F("value_TH","Energy of parton",1000,0,1000);
	TF[window] = new TH1F("transfert_fun",title.str().c_str(),nbre_bin,bin_min,bin_max);
	MC[window] = new TH1F("delta",title.str().c_str(),nbre_bin,bin_min,bin_max);


double a=0.0,b=0.0,c=0.0,aprime=0.0,d=0.0;
double a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14;
//initialization of the parameters
a0=param[0];//*(1.);
a1=param[1];//*(1.6);
a2=param[2];//*(1.3);
a3=param[3];//*(1.0);
a4=param[4];//*(1.0);
a5=param[5];
a6=param[6];//*(1.1);
a7=param[7];//*(1.5);
a8=param[8];//*(1.6);
a9=param[9];
a10=param[10];
a11=param[11];
a12=param[12]*(1.0);
a13=param[13]*(1.0);
a14=param[14]*(1.0);

Double_t diff=0.0;
Range(val_min,val_max,value_TH,MC[window]);
		
for(int i=1;i<(nbre_bin+1);i++){
double sum=0.0;
	for(int j=15;j<1001;j++){
		a=0.0;
		b=0.0;
		c=0.0;
		d=0.0;
		double Eb_entry = value_TH->GetBinContent(j);
		double Eb=0.0;
		Eb=j;
		diff = binning*((bin_min/binning) +(i-1));	
					
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
