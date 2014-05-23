/*
 *  Likelihood_minmisation.C
 *  
 *
 *  Created by Arnaud Pin on 18/02/09.
 *  Copyright 2009 __MyCompanyName__. All rights reserved.
 *
 */

#include "classes.C"
#include "TMath.h"
//-----------------------------------------------------------
// -------------------- Function to minimise ----------------------
TChain *chain; //= new TChain("DATA");

TChain *tree1 = new TChain("tree1");
double E_jb,DeltaE_jet,E_b,phi_jb ,Eta_jb ;
double E_jab,DeltaE_ajet,E_ab,phi_jab , Eta_jab;

void fcn(Int_t &npar, Double_t *gin, Double_t &f, Double_t *p, Int_t iflag)
{
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
			Eb = E_b;
			Eab= E_ab;
			Ejb = E_jb;
			Ejab= E_jab;
			diffb = DeltaE_jet;
			diffab= DeltaE_ajet;
                        phijb=phi_jb;
                        phijab=phi_jab;
                        etajb=Eta_jb;
                        etajab=	Eta_jab	;	
			
			dphi=phijb-phijab;
                        if(dphi>TMath::Pi()){
                          dphi= (2*TMath::Pi()) - dphi;
                        }
                        DR=sqrt(pow(etajb-etajab,2)+pow(dphi,2));

			if(Eb>30 && Eb<1000 && fabs(etajb)<1.6 && DR>0.006){	
		//     Double gaussian	for jets
			double p1 = p[0] + p[1] * Eb + p[2] * sqrt(Eb);
			double p2 = p[3] + p[4] * Eb + p[5] * sqrt(Eb);
			double p3 = p[6] + p[7] * Eb + p[8] * sqrt(Eb);
			double p4 = p[9] + p[10] * Eb + p[11] * sqrt(Eb);
			double p5 = p[12] + p[13] * Eb  + p[14] * sqrt(Eb);					
			a1=  (1.0/(sqrt(2.0* TMath::Pi())*(p2+ p3 * p5)));
			b1= (exp((-1.0/2.0)*(pow((diffb - p1),2)/(pow(p2,2)))));
			c1=(p3)* (exp((-1.0/2.0)*(pow((diffb - p4),2)/(pow(p5,2)))));
			L= L + log(a1*(b1 + c1));
			}
			if(Eab>30 && Eab<1000 && fabs(etajab)<1.6 && DR>0.006){	
		//     Double gaussian	for jets bar
			double p1 = p[0] + p[1] * Eab + p[2] * sqrt(Eab);
			double p2 = p[3] + p[4] * Eab + p[5] * sqrt(Eab);
			double p3 = p[6] + p[7] * Eab + p[8] * sqrt(Eab);
			double p4 = p[9] + p[10] * Eab + p[11] * sqrt(Eab);
			double p5 = p[12] + p[13] * Eab  + p[14] * sqrt(Eab);					
			a2=  (1.0/(sqrt(2.0* TMath::Pi())*(p2+ p3 * p5)));
			b2= (exp((-1.0/2.0)*(pow((diffab - p1),2)/(pow(p2,2)))));
			c2=(p3)* (exp((-1.0/2.0)*(pow((diffab - p4),2)/(pow(p5,2)))));
			L= L + log(a2*(b2 + c2));
			//cout<<" l Value "<<L<<endl;
			}
		}
		f = -L;
}

//---------------------------------------------------------------------------------
// ------------------ Main code -------------------------- 

void Likelihood_minmisation(const char *inputFile)
{
	tree1->Reset();
	tree1->Add(inputFile);    // Loading Input File
    //---------------------------------------------------------
	TMinuit *gMinuit = new TMinuit(10);        // initialize TMinuit with 15 params
	gMinuit->SetFCN(fcn);			   // Launch Minuit on  the fcn function
	
	Double_t arglist[10];
	Int_t ierflg = 0;
	arglist[0] = 1;
	gMinuit->mnexcm("SET ERR", arglist ,1,ierflg);
	
// Set starting values and step sizes for parameters
// Initialisation of 15 parameters.
   //------------------------------------------------Start----Step --- range-------
   gMinuit->mnparm(0, "mean gauss 1 constant     ", 1.05 , 0.01  , 1.03,1.07,ierflg);
   gMinuit->mnparm(1, "mean gauss 1 E deps       ", -0.021,0.0002,-0.022,-0.02,ierflg);
   gMinuit->mnparm(2, "mean gauss 1 sqrt(E) deps ", 0.0,0.0,0.0,0.0,ierflg);
   
   gMinuit->mnparm(3, "width gauss 1 constant    ", 0.0 , 0.0 , 0.0,0.0,ierflg);
   gMinuit->mnparm(4, "width gauss 1 E deps      ", 0.037 , 0.0005 , 0.036,0.038,ierflg);
   gMinuit->mnparm(5, "width gauss 1 sqrt(E) deps", 0.83 ,0.005,0.82,0.84,ierflg);

   gMinuit->mnparm(6, "ratio constant            ", 0.0 , 0.0 , 0.0,0.0,ierflg);
   gMinuit->mnparm(7, "ratio E deps              ", 0.00122392, 0.00002 , 0.0012,0.0013,ierflg);
   gMinuit->mnparm(8, "ratio sqrt(E) deps        ", 0.001 ,0.0001,0.0007,0.0013,ierflg);
   
   gMinuit->mnparm(9, "mean gauss 2 constant     ", 5.0, 0.1 , 4.7,5.3,ierflg); 
   gMinuit->mnparm(10,"mean gauss 2 E deps       ", 0.0 , 0.0 , 0.0,0.0,ierflg);
   gMinuit->mnparm(11,"mean gauss 2 sqrt(E) deps ", 2.4, 0.02,2.3,2.5,ierflg);
   
   gMinuit->mnparm(12,"width gauss 2 constant    ", 0.0 , 0.0 , 0.0,0.0,ierflg);
   gMinuit->mnparm(13,"width gauss 2 E deps      ", 0.05,0.02,0.0,0.1,ierflg);
   gMinuit->mnparm(14,"width gauss 2 sqrt(E) deps", 0.9,0.01,0.8,1.0,ierflg);
	

// Now ready for minimization step
   arglist[0] = 1000;
   arglist[1] = 0.1;
   //gMinuit->mnexcm("MINIMIZE", arglist ,2,ierflg);
   gMinuit->mnexcm("MIGRAD", arglist ,2,ierflg);

// Print results
   Double_t amin,edm,errdef;
   Int_t nvpar,nparx,icstat;
   gMinuit->mnstat(amin,edm,errdef,nvpar,nparx,icstat);
   gMinuit->mnprin(3,amin);
   
// Print parameters in text file
   ofstream output ("File/parameters.txt");
   double p[15];
   double error[15];
   for(int u=0;u<15;u++){
	gMinuit->GetParameter(u,p[u],error[u]);
	output<<p[u]<<endl;
	}
}
