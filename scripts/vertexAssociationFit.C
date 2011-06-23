#include <iostream>
#include <TH1.h>
#include <TGraph.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TDirectory.h>
#include <TF1.h>
#include <TFitResult.h>
#include <TROOT.h>
#include <cmath> 

// constants
double xminfit[11] = {0.0,0.1,0.1,0.1,0.2,0.2,0.2,0.3,0.3,0.3,0.3};
double xmaxfit[11] = {1.0,0.95,0.9,0.9,0.85,0.85,0.8,0.8,0.75,0.75,0.75};
unsigned int nbins = 11;
unsigned int nSteps = 20;
float cutmin = 0.;
float cutmax = 0.5;
float defaultCut = 0.1;
float defaultPur = 0.995;
float defaultEff = 0.98;
bool constrainSlope = false;
double contrainedSlopeParameters[2] = { 4.443, -0.1367 };

void findWorkingPoint(TGraph* graph, unsigned int& n, double& x, double& y, unsigned int known){
  switch(known) {
    // known 1 : fixed n
    case 1: {
      graph->GetPoint(n,x,y);
      break;
    }
    // known 2 : fixed x
    case 2: {
      /*
      double dist = 1000.;
      int best = n;
      double target = x;
      for(int i=0;i<graph->GetN();++i) {
        graph->GetPoint(i,x,y);
        if (fabs(target-x)<dist) {
          dist = fabs(target-x);
          best = i;
        }
      }
      n = best;
      graph->GetPoint(n,x,y);
      */
      double target = x;
      for(n=0;n<graph->GetN();++n) {
        graph->GetPoint(n,x,y);
	if(x>target) break;
      }
      break;
    }
    // known 3 : fixed y
    case 3: {
      /*
      double dist = 1000.;
      int best = n;
      double target = y;
      for(int i=0;i<graph->GetN();++i) {
        graph->GetPoint(i,x,y);
        if (fabs(target-y)<dist) {
          dist = fabs(target-y);
          best = i;
        }
      }
      n = best;
      graph->GetPoint(n,x,y);
      */
      double target = y;
      for(n=0;n<graph->GetN();++n) {
        graph->GetPoint(n,x,y);
	if(y<target) break;
      }
      break;
    }
  }
}

void estimateEfficiencyAndPurity(TH1* fraction,double cut,double& efficiency, double& purity) {
  // efficiency loss is defined as the estimated signal below the cut over the estimated total signal
  double rangeLow, rangeHigh;
  TF1* expo = fraction->GetFunction("expo");
  expo->GetRange(rangeLow, rangeHigh);
  double signalLoss = expo->Integral(0,cut)/fraction->GetBinWidth(1);
  double signal_expopart = expo->Integral(cut,rangeHigh)/fraction->GetBinWidth(1);
  double signal_toppoart = fraction->Integral(fraction->FindBin(rangeHigh),fraction->FindBin(1.)+1);
  efficiency = (signal_expopart+signal_toppoart)/(signal_expopart+signal_toppoart+signalLoss);
  // purity is defined as the signal above the cut (signal_expopart+signal_toppoart) 
  // over the total data above that cut
  double data_kept = fraction->Integral(fraction->FindBin(cut),fraction->FindBin(1.)+1);
  purity = (signal_expopart+signal_toppoart)/data_kept;
  std::cout << "estimateEfficiencyAndPurity for cut=" << cut << std::endl;
  std::cout << "signal: " << signalLoss << " " << signal_expopart << " " << signal_toppoart << std::endl;
  std::cout << "data kept: " << data_kept << std::endl;
  std::cout << "eff, pur: " << efficiency << " " << purity << std::endl;
}

void vertexAssociationAnalysis(TH1* fraction, unsigned int index, double& slope, TGraph*& graph) {
  // do the fit
  if(constrainSlope) {
    fraction->Fit("expo","LS","",xminfit[index],xmaxfit[index]);
    TF1* expo = (TF1*)gROOT->FindObjectAny("expo");
    expo->FixParameter(1,contrainedSlopeParameters[0]+contrainedSlopeParameters[1]*(index+1));
    fraction->Fit("expo","LSB","",xminfit[index],xmaxfit[index]);
    expo->SetParLimits(1,-10000,10000);
  } else {
    fraction->Fit("expo","LS","",xminfit[index],xmaxfit[index]);
  }
  //TFitResultPtr result = fraction->Fit("expo","LS","",xminfit[index],xmaxfit[index]);
  // estimate efficiency and purity as a function of the cut
  double *efficiency, *purity;
  efficiency = new double[nSteps];
  purity = new double[nSteps];
  unsigned int step = 0;
  for(float cut=cutmin; cut<cutmax; cut += (cutmax-cutmin)/float(nSteps), ++step) {
    estimateEfficiencyAndPurity(fraction,cut,efficiency[step],purity[step]);
  }
  // output: the graph with efficiency and purity vs cut and the expo slope
  slope = fraction->GetFunction("expo")->GetParameter(1);
  //slope = result->Parameter(1);
  graph = new TGraph(nSteps,purity,efficiency);
  delete[] efficiency;
  delete[] purity;
}

void vertexAssociationFit(TFile* input, TFile* output) {
  // prepare the output
  // * canvas to put the fit per bin
  TCanvas* canvas_0 = new TCanvas("FitPerBin","Fit for each vertex bin");
  canvas_0->Divide(3,4);
  // * canvas to put the plots per bin
  TCanvas* canvas_1 = new TCanvas("EffPerBin","Efficiency vs purity for each vertex bin");
  canvas_1->Divide(3,4);
  // * canvas with other plots: slope vs nvertices, efficiency and purity for fixed cut, etc.
  TCanvas* canvas_2 = new TCanvas("jvAssociation","Efficiency vs purity summary plots");
  canvas_2->Divide(3,3);
  // summary graphs
  TGraph* slopeGraph  = new TGraph(nbins);
  slopeGraph->SetNameTitle("slopeGraph","expo slope in each #vertex bin");
  TGraph* cuteffGraph = new TGraph(nbins);
  cuteffGraph->SetNameTitle("cuteffGraph","Efficiency in each #vertex bin");
  TGraph* cutpurGraph = new TGraph(nbins);
  cutpurGraph->SetNameTitle("cutpurGraph","Purity in each #vertex bin");
  TGraph* effcutGraph = new TGraph(nbins);
  effcutGraph->SetNameTitle("effcutGraph","Cut for fixed efficiency in each #vertex bin");
  TGraph* effpurGraph = new TGraph(nbins);
  effpurGraph->SetNameTitle("effpurGraph","Purity for fixed efficiency in each #vertex bin");
  TGraph* purcutGraph = new TGraph(nbins);
  purcutGraph->SetNameTitle("purcutGraph","Cut for fixed purity in each #vertex bin");
  TGraph* pureffGraph = new TGraph(nbins);
  pureffGraph->SetNameTitle("pureffGraph","Efficiency for fixed purity in each #vertex bin");
  // loop over the directories
  double slope = 0.;
  TGraph* result = NULL;
  double x,y;
  unsigned int index;
  for(unsigned int i=1; i<=nbins; ++i) {
    // get the histogram
    TH1* fraction = (TH1*)input->Get(Form("v%d/j1_ratio2b",i));
    // do it
    canvas_0->cd(i);
    if(fraction) vertexAssociationAnalysis(fraction,i-1,slope,result);
    gPad->SetLogy();
    // plot
    canvas_1->cd(i);
    result->Draw("al");
    result->GetXaxis()->SetRangeUser(0.8,1.2);
    result->GetYaxis()->SetRangeUser(0.85,1.0);
    // extract other quantities
    slopeGraph->SetPoint(i-1,i,slope);
    index = unsigned(((defaultCut-cutmin)/(cutmax-cutmin)*nSteps)+0.5);
    findWorkingPoint(result,index,x,y,1);
    cuteffGraph->SetPoint(i-1,i,y);
    cutpurGraph->SetPoint(i-1,i,x);
    x = defaultPur;
    findWorkingPoint(result,index,x,y,2);
    purcutGraph->SetPoint(i-1,i,cutmin+(cutmax-cutmin)/nSteps*index);
    pureffGraph->SetPoint(i-1,i,y);
    y = defaultEff;
    findWorkingPoint(result,index,x,y,3);
    effcutGraph->SetPoint(i-1,i,cutmin+(cutmax-cutmin)/nSteps*index);
    effpurGraph->SetPoint(i-1,i,x);
  }
  // plot summary graphs
  TF1* f=NULL;
  canvas_2->cd(1);
  slopeGraph->Draw("al");
  slopeGraph->Fit("pol1");
  f = slopeGraph->GetFunction("pol1");
  if(f->GetParError(1)>fabs(f->GetParameter(1))) slopeGraph->Fit("pol0");
  canvas_2->cd(2);
  cuteffGraph->Draw("al");
  cuteffGraph->Fit("pol1");
  f = cuteffGraph->GetFunction("pol1");
  if(f->GetParError(1)>fabs(f->GetParameter(1))) cuteffGraph->Fit("pol0");
  canvas_2->cd(3);
  cutpurGraph->Draw("al");
  cutpurGraph->Fit("pol1");
  f = cutpurGraph->GetFunction("pol1");
  if(f->GetParError(1)>fabs(f->GetParameter(1))) cutpurGraph->Fit("pol0");
  canvas_2->cd(4);
  effcutGraph->Draw("al");
  effcutGraph->Fit("expo");
  canvas_2->cd(5);
  effpurGraph->Draw("al");
  effpurGraph->Fit("pol1");
  f = effpurGraph->GetFunction("pol1");
  if(f->GetParError(1)>fabs(f->GetParameter(1))) effpurGraph->Fit("pol0");
  canvas_2->cd(6);
  purcutGraph->Draw("al");
  purcutGraph->Fit("expo");
  canvas_2->cd(7);
  pureffGraph->Draw("al");
  pureffGraph->Fit("pol1");
  f = pureffGraph->GetFunction("pol1");
  if(f->GetParError(1)>fabs(f->GetParameter(1))) pureffGraph->Fit("pol0");
  // save
  output->cd();
  canvas_0->Write();
  canvas_1->Write();
  canvas_2->Write();
}

void vertexAssociationFit(const char* filename, const char* output="output.root") {
  TFile* file = TFile::Open(filename);
  TFile* fileOut = TFile::Open(output,"recreate");
  vertexAssociationFit(file,fileOut);
  //file->Close();
  //fileOut->Close();
}

