#include <vector>
#include <iostream>
#include <iomanip>
#include <TObject.h>
#include <TCanvas.h>
#include <THStack.h>
#include <TList.h>
#include <TKey.h>
#include <TH1I.h>
#include <TFile.h>

void yield(TCanvas* categoryPlot, unsigned stage, bool doheader)
{
  //get the plots
  TIter next(categoryPlot->GetListOfPrimitives());
  TIter* mc = NULL;
  TH1I* data = NULL;
  TObject* obj = NULL;
  while ((obj = next())) {
    if(strncmp(obj->GetName(),"category",9)==0 && obj->InheritsFrom("TH1")) {
      data = (TH1I*)obj;
    }
    if(strncmp(obj->GetName(),"category",9)==0 && obj->InheritsFrom("THStack")) {
      mc = new TIter(((THStack*)obj)->GetHists());
    }
  }
  // now that we have everything, go on.
  if(doheader) {
    // First print the title row
    std::cout << setw(10) << "stage" << setw(14) << "data"<< setw(10) << "";
    while ((obj = mc->Next())) {
      std::cout << setw(10) << obj->GetTitle() << setw(10) << "" ;
    }
    std::cout << setw(10) << "Total MC" << setw(10) << "" << std::endl;
    mc->Reset();
  }
  // now select the proper stage and print data. all info is in bin stage+1
  std::cout << setw(10) << "stage " << stage;
  Double_t totmc = 0;
  Double_t errmc = 0;
  std::cout << setw(10) << setiosflags(ios::right) << data->GetBinContent(stage+1) << "+/-" << resetiosflags(ios::right);
  std::cout << setw(7)  << setiosflags(ios::left) << setiosflags(ios::fixed) << setprecision(1) << data->GetBinError(stage+1) << resetiosflags(ios::left);
  while ((obj = mc->Next())) {
    TH1I* h = (TH1I*)obj;
    std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) <<h->GetBinContent(stage+1) << "+/-" << resetiosflags(ios::right);
    std::cout << setiosflags(ios::left) << setprecision(1) << setw(7) << h->GetBinError(stage+1) << resetiosflags(ios::left);
    totmc += h->GetBinContent(stage+1);
    errmc += h->GetBinError(stage+1)*h->GetBinError(stage+1);
  }
  std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) << totmc << "+/-" << resetiosflags(ios::right);
  std::cout << setiosflags(ios::left) << setw(7) << sqrt(errmc) << resetiosflags(ios::left) << std::endl;
  if(mc) delete mc;
}

void yield(TFile* file)
{
  TList* keys = file->GetListOfKeys();
  TIter next(keys);
  TKey *key;
  // loop over the folders = analysis channels
  while ((key = (TKey*) next())) {
    if(key->IsFolder()) {
      std::cout << "Selection details for channel " << key->GetName() << std::endl;
      TDirectory* dir = (TDirectory*) key->ReadObj();
      // loop over stages
      bool doheader = true;
      for(unsigned stage = 0; stage<20; ++stage) {
	TCanvas* categoryPlot = (TCanvas*)dir->Get(Form("stage_%d/selection/category",stage));
        if(categoryPlot) {
	  if(categoryPlot->InheritsFrom("TCanvas")) {
  	    yield(categoryPlot,stage, doheader);
	    doheader = false;
	  } else {
	    std::cout << "Error: input file doesn't look like a combined file with canvas" << std::endl;
	  }
	}
      }
    }
  }
}

void yield(const char* filename)
{
  TFile* file = TFile::Open(filename);
  yield(file);
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

