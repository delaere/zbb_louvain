#include <vector>
#include <iostream>
#include <iomanip>
#include <TObject.h>
#include <TCanvas.h>
#include <TList.h>
#include <TKey.h>
#include <TH1I.h>
#include <TFile.h>

void IntegralAndError(TH1* h, unsigned bin1, unsigned bin2, Double_t& integral, Double_t& error)
{
  integral=0;
  error = 0;
  for(unsigned i = bin1;i<=bin2;++i) {
    integral +=h->GetBinContent(i);
    error += h->GetBinError(i)*h->GetBinError(i);
  }
  error = sqrt(error);
}

void yield(TCanvas* categoryPlot, unsigned initialStage)
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
  // First print the title row
  std::cout << setw(10) << "stage" << setw(14) << "data"<< setw(10) << "";
  while ((obj = mc->Next())) {
    std::cout << setw(10) << obj->GetTitle() << setw(10) << "" ;
  }
  std::cout << setw(10) << "Total MC" << setw(10) << "" << std::endl;
  mc->Reset();
  // now loop over stages and print data
  for(unsigned stage=initialStage; stage<=data->GetNbinsX()-1; ++stage) {
    //all info is in bin stage+1
    std::cout << setw(10) << "stage " << stage;
    Double_t integral, error;
    Double_t totmc = 0;
    Double_t errmc = 0;
    //IntegralAndError(data,stage+1,data->GetNbinsX(),integral,error);
    //std::cout << setw(10) << setiosflags(ios::right) << integral << "+/-" << resetiosflags(ios::right);
    std::cout << setw(10) << setiosflags(ios::right) << data->GetBinContent(stage+1) << "+/-" << resetiosflags(ios::right);
    //std::cout << setw(7)  << setiosflags(ios::left) << setiosflags(ios::fixed) << setprecision(1) << error << resetiosflags(ios::left);
    std::cout << setw(7)  << setiosflags(ios::left) << setiosflags(ios::fixed) << setprecision(1) << data->GetBinError(stage+1) << resetiosflags(ios::left);
    while ((obj = mc->Next())) {
      TH1I* h = (TH1I*)obj;
      //IntegralAndError(h,stage+1,h->GetNbinsX(),integral,error);
      //std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) << integral << "+/-" << resetiosflags(ios::right);
      std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) <<h->GetBinContent(stage+1) << "+/-" << resetiosflags(ios::right);
      //std::cout << setiosflags(ios::left) << setprecision(1) << setw(7) << error << resetiosflags(ios::left);
      std::cout << setiosflags(ios::left) << setprecision(1) << setw(7) << h->GetBinError(stage+1) << resetiosflags(ios::left);
      totmc += integral;
      errmc += error*error;
    }
    std::cout << setw(10) << setiosflags(ios::right) << setiosflags(ios::fixed) << setprecision(1) << totmc << "+/-" << resetiosflags(ios::right);
    std::cout << setiosflags(ios::left) << setw(7) << sqrt(errmc) << resetiosflags(ios::left) << std::endl;
    mc->Reset();
  }
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
      for(unsigned stage = 0; stage<20; ++stage) {
        // find the lowest available category plot
	TCanvas* categoryPlot = (TCanvas*)dir->Get(Form("stage_%d/selection/category",stage));
        if(categoryPlot) {
	  yield(categoryPlot,stage);
	  break;
	}
      }
    }
  }
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

void yield(const char* filename)
{
  TFile* file = TFile::Open(filename);
  yield(file);
  file->Close();
}
