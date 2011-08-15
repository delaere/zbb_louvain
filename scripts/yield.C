#include <vector>
#include <utility>
#include <iostream>
#include <iomanip>
#include <TObject.h>
#include <TCanvas.h>
#include <THStack.h>
#include <TList.h>
#include <TKey.h>
#include <TH1F.h>
#include <TFile.h>
#include <TMath.h>
#include <TGraphErrors.h>

//NOTE: this code grew a lot... 
//The structure is now typical of a code whose scope extended with time.
//It would be worth rewriting it as a class, using members for inter-methods communication.

const char signalName[30] = "Z+b";
unsigned int nstages = 20;

void printHeader(TCanvas* categoryPlot, bool detailedLabel=false, bool printRatio=false, bool printSig=false)
{
  //get the plots
  TIter next(categoryPlot->GetListOfPrimitives());
  TIter* mc = NULL;
  TH1F* data = NULL;
  TObject* obj = NULL;
  while ((obj = next())) {
    if(strncmp(obj->GetName(),"category",9)==0 && obj->InheritsFrom("TH1")) {
      data = (TH1F*)obj;
    }
    if(strncmp(obj->GetName(),"category",9)==0 && obj->InheritsFrom("THStack")) {
      mc = new TIter(((THStack*)obj)->GetHists());
    }
  }
  // First print the title row
  std::cout << setw(detailedLabel?30:10) << "stage" << setw(14) << "data"<< setw(10) << "";
  while ((obj = mc->Next())) {
    std::cout << setw(10) << obj->GetTitle() << setw(10) << "" ;
  }
  std::cout << setw(10) << "Total MC" << setw(10) << "";
  if(printRatio) {
    std::cout << setw(7) << "Ratio" << setw(12) << "Deviation";
  }
  if(printSig) {
    std::cout << setw(7) << "S/B" << setw(13) << "S/sqrt(B)" << setw(13) << "S/sqrt(S+B)";
  }
  std::cout << std::endl;
  mc->Reset();
}

std::vector<TGraphErrors*> initGraphs(TCanvas* categoryPlot)
{
  //get the plots
  TIter next(categoryPlot->GetListOfPrimitives());
  TIter* mc = NULL;
  TH1F* data = NULL;
  TObject* obj = NULL;
  while ((obj = next())) {
    if(strncmp(obj->GetName(),"category",9)==0 && obj->InheritsFrom("TH1")) {
      data = (TH1F*)obj;
    }
    if(strncmp(obj->GetName(),"category",9)==0 && obj->InheritsFrom("THStack")) {
      mc = new TIter(((THStack*)obj)->GetHists());
    }
  }
  // Initialize the TGraphs
  // First the data
  // Then the MC (variable) 
  // Then a fixed set of summaries
  std::vector<TGraphErrors*> output;
  TGraphErrors* g = new TGraphErrors(nstages);
  g->SetNameTitle("data", "data");
  output.push_back(g);
  while ((obj = mc->Next())) {
    g = new TGraphErrors(nstages);
    g->SetNameTitle(obj->GetName(), obj->GetTitle());
    output.push_back(g);
  }
  g = new TGraphErrors(nstages);
  g->SetNameTitle("totalMC","Total MC");
  output.push_back(g);
  g = new TGraphErrors(nstages);
  g->SetNameTitle("ratio","data/mc ratio");
  output.push_back(g);
  g = new TGraphErrors(nstages);
  g->SetNameTitle("deviation","data/mc deviation");
  output.push_back(g);
  g = new TGraphErrors(nstages);
  g->SetNameTitle("sb","S/B");
  output.push_back(g);
  g = new TGraphErrors(nstages);
  g->SetNameTitle("ssqrtb","S/sqrt(B)");
  output.push_back(g);
  g = new TGraphErrors(nstages);
  g->SetNameTitle("sosqrtsb","S/sqrt(S+B)");
  output.push_back(g);
  std::cout << std::endl;
  mc->Reset();
  return output;
}

std::vector<std::pair<float,float> > yieldData(TCanvas* categoryPlot, unsigned stage)
{
  //get the plots
  TIter next(categoryPlot->GetListOfPrimitives());
  TIter* mc = NULL;
  TH1F* data = NULL;
  TObject* obj = NULL;
  while ((obj = next())) {
    if(strncmp(obj->GetName(),"category",9)==0 && obj->InheritsFrom("TH1")) {
      data = (TH1F*)obj;
    }
    if(strncmp(obj->GetName(),"category",9)==0 && obj->InheritsFrom("THStack")) {
      mc = new TIter(((THStack*)obj)->GetHists());
    }
  }
  // now select the proper stage and retrieve data. all info is in bin stage+1
  Double_t signal = 0;
  Double_t totmc = 0;
  Double_t errmc = 0;
  std::vector<std::pair<float,float> > output;
  output.reserve(10);
  output.push_back(std::make_pair(data->GetBinContent(stage+1),data->GetBinError(stage+1)));
  while ((obj = mc->Next())) {
    TH1F* h = (TH1F*)obj;
    output.push_back(std::make_pair(h->GetBinContent(stage+1),h->GetBinError(stage+1)));
    totmc += h->GetBinContent(stage+1);
    if(string(h->GetTitle())==signalName) signal+= h->GetBinContent(stage+1);
    errmc += h->GetBinError(stage+1)*h->GetBinError(stage+1);
  }
  output.push_back(std::make_pair(totmc,sqrt(errmc)));
  float ratio = data->GetBinContent(stage+1)/totmc;
  output.push_back(std::make_pair(ratio,ratio*sqrt(pow(data->GetBinError(stage+1)/data->GetBinContent(stage+1),2)+pow(sqrt(errmc)/totmc,2))));
  float deviation = (data->GetBinContent(stage+1)-totmc)/sqrt(errmc+data->GetBinError(stage+1)*data->GetBinError(stage+1));
  output.push_back(std::make_pair(deviation,0));
  float sb = signal/(totmc-signal);
  output.push_back(std::make_pair(sb,0));
  float ssqrtb = signal/sqrt(totmc-signal);
  output.push_back(std::make_pair(ssqrtb,0));
  float ssqrtsb = signal/sqrt(totmc);
  output.push_back(std::make_pair(ssqrtsb,0));
  if(mc) delete mc;
  return output;
}

void printYield(const std::vector<std::pair<float,float> >& data, unsigned stage, const char* label="", bool printRatio=false, bool printSig=false)
{
  bool detailedLabel = (string(label)!="");
  // title column
  if(!detailedLabel) {
    std::cout << setw(10) << "stage " << stage;
  } else {
    std::cout << setw(30) <<  label;
  }
  // data
  std::cout << setw(10) << setiosflags(ios::right) << data[0].first << "+/-" << resetiosflags(ios::right);
  std::cout << setw(7)  << setiosflags(ios::left) << setiosflags(ios::fixed) << setprecision(1) << data[0].second << resetiosflags(ios::left);
  // mc
  unsigned int i = 1;
  for(; i< data.size()-6 ; ++i) {
    std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) << data[i].first << "+/-";
    std::cout << resetiosflags(ios::right) << setiosflags(ios::left) << setprecision(1) << setw(7) << data[i].second << resetiosflags(ios::left);
  }
  // Tot MC 
  std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) << data[i].first << "+/-";
  std::cout << resetiosflags(ios::right) << setiosflags(ios::left) << setw(7) << data[i++].second << resetiosflags(ios::left);
  // Fixed content: ratio, significance
  if(printRatio) {
    std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) << data[i++].first;
    std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) << data[i++].first << resetiosflags(ios::left);
  }
  if(printSig) {
    std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) << data[i++].first;
    std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) << data[i++].first;
    std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) << data[i++].first;
  }
  std::cout << std::endl;
}

void yield(TFile* file, bool verbose = false, bool graphOutput = false)
{
  TList* keys = file->GetListOfKeys();
  TIter next(keys);
  TKey *key;
  // in case an output file is desired, create it
  TFile* output = graphOutput ? TFile::Open("yield.root","recreate"): NULL;
  // loop over the folders = analysis channels
  while ((key = (TKey*) next())) {
    if(key->IsFolder()) {
      std::cout << "Selection details for channel " << key->GetName() << std::endl;
      TDirectory* dir = (TDirectory*) key->ReadObj();
      // loop over stages
      bool doheader = true;
      std::vector<int> stages;
      std::vector<TGraphErrors*> graphs;
      std::vector<std::vector<std::pair<float,float> > > data;
      for(unsigned stage = 0; stage<nstages; ++stage) {
	TCanvas* categoryPlot = (TCanvas*)dir->Get(Form("stage_%d/selection/category",stage));
        if(categoryPlot) {
	  if(categoryPlot->InheritsFrom("TCanvas")) {
	    if(doheader) { 
	      printHeader(categoryPlot, verbose, verbose, verbose);
	      graphs = initGraphs(categoryPlot);
	    }
	    doheader = false;
	    stages.push_back(stage);
	    data.push_back(yieldData(categoryPlot, stage));
	    printYield(data.back(), stage, verbose ? ((TDirectory*)(dir->Get(Form("stage_%d",stage))))->GetTitle(): "", verbose, verbose);
	  } else {
	    std::cout << "Error: input file doesn't look like a combined file with canvas" << std::endl;
	  }
	}
      }
      // in case an output file is desired, create it
      if(graphOutput) {
        // fill graphs
        // loop on the lines (stages)
        for(std::vector<std::vector<std::pair<float,float> > >::iterator it = data.begin(); it<data.end(); ++it) {
          // loop on the columns (graphs)
          for(unsigned int i=0; i<it->size(); ++i) {
            graphs[i]->SetPoint(it-data.begin(),stages[it-data.begin()],TMath::IsNaN((*it)[i].first) ? 0. : (*it)[i].first );
            graphs[i]->SetPointError(it-data.begin(),0,TMath::IsNaN((*it)[i].second) ? 0. : (*it)[i].second );
          }
        }
      }
      // write the graphs
      if(output) { 
        output->mkdir(key->GetName()); output->cd(key->GetName()); 
        for(std::vector<TGraphErrors*>::iterator g = graphs.begin(); g != graphs.end(); ++g) { 
          (*g)->Write();
	  delete (*g);
        }
      }
    }
  }
  // close the output
  if(output) output->Close();
}

void yield(const char* filename,bool verbose = false, bool graphOutput = false)
{
  TFile* file = TFile::Open(filename);
  yield(file,verbose,graphOutput);
  file->Close();
}

void ratioData(double DataZb, double DataZj, double MCttbar, double purity, double efficiency, 
               double purityErr = 0.15, double efficiencyErr = 0.2, double MCttbarError = 0.0, double JESError = 0.03)
{
  // first compute the ratio
  double ratio = ((DataZb*purity)-MCttbar)/DataZj/efficiency;
  // now, compute the statistical error
  double stat = sqrt((purity*purity*DataZb+MCttbarError*MCttbarError)/((DataZb*purity-MCttbar)*(DataZb*purity-MCttbar))+1/DataZj);
  stat *= ratio;
  // and finally the systematic error
  double syst = sqrt(purityErr*purityErr+efficiencyErr*efficiencyErr+JESError*JESError);
  syst *= ratio;

  // print
  std::cout << "ratio = " << ratio << " +/- " << stat << " (stat) +/- " << syst << " (syst)" << std::endl;
}

void ratioMC(double MCZb, double MCZj, double MCZbError, double MCZjError, double MCZbErrorTh, double MCZjErrorTh,
             double JESError = 0.03)
{
  // first compute the ratio
  double ratio = MCZb/MCZj;
  // now, compute the statistical error
  MCZbError/=MCZb;
  MCZjError/=MCZj;
  double stat = sqrt(MCZbError*MCZbError+MCZjError*MCZjError);
  stat*=ratio;
  // now, compute thesystematic error
  double syst = ratio*JESError;
  // and finally the theoretical error
  double theo = sqrt(MCZbErrorTh*MCZbErrorTh+MCZjErrorTh*MCZjErrorTh);
  theo*=ratio;

  // print
  std::cout << "ratio = " << ratio << " +/- " << stat << " (stat) +/- " << syst << " (syst) +/- " << theo << " (theo)" << std::endl;
}

