#include "include.h"



void ComputeGraphFromTrainTxt(TFile* outputFile, const char *inputFile1, int Nepoch) {

        //cout << "begin Comput.." << endl;

	cout<<inputFile1<<endl;
	
	ifstream infile1(inputFile1);
	double *iteration=new double[Nepoch];
	double *learn=new double[Nepoch];
	double *train=new double[Nepoch];
	//double *output=new double[Nepoch];
	Int_t line = 0;	


	//cout<<"begin readfile"<<endl;
	while(infile1 >> iteration[line] >> learn[line] >> train[line]){
	  line++;
	}
	infile1.close();
	//cout<<"end readfile"<<endl;
	

	
	//for (int i = 0; i < Nepoch; i++) {
	//  std::cout << "iteration[" << i << "]= " << iteration[i] << " learn= " << learn[i] << " train= " << train[i] << std::endl;
	//}
        //gtrain = new TGraph(Nepoch, iteration, output);
	//g->Draw();
	outputFile->cd();
	//cout<<"cd outputfile"<<endl;
	
	
	TGraph* g_learn = new TGraph(Nepoch, iteration, learn);
	TGraph* g_train = new TGraph(Nepoch, iteration, train);
	//cout<<"newing graphs"<<endl;

	g_learn->SetMarkerStyle(20);
	g_learn->SetMarkerColor(kRed);
	g_train->SetMarkerStyle(21);
	g_train->SetMarkerColor(kBlue);
	
	
	TCanvas c;
	g_learn->Draw("ALP");
	g_train->Draw("LP");
	//cout<<"drawing files"<<endl;
	
	
	g_learn->Write("g_learn");
	g_train->Write("g_train");
	c.Write("canvas_learnAndtrain");
	
	//cout<<"end Comput..."<<endl;

}
