#include <vector>
#include <map>
#include <iostream>
#include "FWCore/ParameterSet/interface/ProcessDesc.h"
#include "FWCore/FWLite/interface/AutoLibraryLoader.h"
#include "FWCore/PythonParameterSet/interface/PythonProcessDesc.h"
#include <TDirectory.h>
#include <TFile.h>
#include <TH1.h>
#include <TROOT.h>
#include <TSystem.h>
#include <TCanvas.h>
#include <THStack.h>
#include <TList.h>
#include <TKey.h>
#include <TStyle.h>
#include <TLegend.h>

class plotCombiner {

   public:
     plotCombiner() {}
     ~plotCombiner() {}
     void run(TDirectory* output) {
       CombineDir(_filesData, _filesMC, output);
     }
     void setDatacfg(std::vector<edm::ParameterSet>& inputs) {
      _dataInputs = inputs;
      for(std::vector<edm::ParameterSet>::const_iterator input = inputs.begin();input<inputs.end();++input) {
        std::string filename = input->getParameter<std::string>("fileName");
        _filesData.push_back(TFile::Open(filename.c_str()));
      }
     }
     void setMCcfg(std::vector<edm::ParameterSet>& inputs) {
       _mcInputs = inputs;
       for(std::vector<edm::ParameterSet>::const_iterator input = inputs.begin();input<inputs.end();++input) {
         std::string filename = input->getParameter<std::string>("fileName");
         _filesMC.push_back(TFile::Open(filename.c_str()));
       }
     }
     void setStyleTweaks(std::vector<edm::ParameterSet>& tweaks) {
       for(std::vector<edm::ParameterSet>::const_iterator tweak = tweaks.begin(); tweak<tweaks.end(); ++tweak) {
         _styleTweaks[tweak->getParameter<std::string>("name")] = *tweak;
       }
     }
   private:
     void CombineHistos(const char* name, std::vector<TDirectory*> datadirs, std::vector<TDirectory*> mcdirs, TDirectory* output);
     void CombineDir(std::vector<TDirectory*> datadirs, std::vector<TDirectory*> mcdirs, TDirectory* output);
     std::vector<edm::ParameterSet> _dataInputs;
     std::vector<edm::ParameterSet> _mcInputs;
     std::vector<TDirectory*> _filesData;
     std::vector<TDirectory*> _filesMC;
     std::map<std::string, edm::ParameterSet> _styleTweaks;
};

void setTDRStyle() {
  TStyle *tdrStyle = new TStyle("tdrStyle","Style for P-TDR");

// For the canvas:
  tdrStyle->SetCanvasBorderMode(0);
  tdrStyle->SetCanvasColor(kWhite);
  tdrStyle->SetCanvasDefH(600); //Height of canvas
  tdrStyle->SetCanvasDefW(600); //Width of canvas
  tdrStyle->SetCanvasDefX(0);   //POsition on screen
  tdrStyle->SetCanvasDefY(0);

// For the Pad:
  tdrStyle->SetPadBorderMode(0);
  // tdrStyle->SetPadBorderSize(Width_t size = 1);
  tdrStyle->SetPadColor(kWhite);
  tdrStyle->SetPadGridX(false);
  tdrStyle->SetPadGridY(false);
  tdrStyle->SetGridColor(0);
  tdrStyle->SetGridStyle(3);
  tdrStyle->SetGridWidth(1);

// For the frame:
  tdrStyle->SetFrameBorderMode(0);
  tdrStyle->SetFrameBorderSize(1);
  tdrStyle->SetFrameFillColor(0);
  tdrStyle->SetFrameFillStyle(0);
  tdrStyle->SetFrameLineColor(1);
  tdrStyle->SetFrameLineStyle(1);
  tdrStyle->SetFrameLineWidth(1);

// For the histo:
  // tdrStyle->SetHistFillColor(1);
  // tdrStyle->SetHistFillStyle(0);
  tdrStyle->SetHistLineColor(1);
  tdrStyle->SetHistLineStyle(0);
  tdrStyle->SetHistLineWidth(1);
  // tdrStyle->SetLegoInnerR(Float_t rad = 0.5);
  // tdrStyle->SetNumberContours(Int_t number = 20);

  tdrStyle->SetEndErrorSize(2);
  // tdrStyle->SetErrorMarker(20);
  tdrStyle->SetErrorX(0.);
  
  tdrStyle->SetMarkerStyle(20);

//For the fit/function:
  tdrStyle->SetOptFit(1);
  tdrStyle->SetFitFormat("5.4g");
  tdrStyle->SetFuncColor(2);
  tdrStyle->SetFuncStyle(1);
  tdrStyle->SetFuncWidth(1);

//For the date:
  tdrStyle->SetOptDate(0);
  // tdrStyle->SetDateX(Float_t x = 0.01);
  // tdrStyle->SetDateY(Float_t y = 0.01);

// For the statistics box:
  tdrStyle->SetOptFile(0);
  tdrStyle->SetOptStat(0); // To display the mean and RMS:   SetOptStat("mr");
  tdrStyle->SetStatColor(kWhite);
  tdrStyle->SetStatFont(42);
  tdrStyle->SetStatFontSize(0.025);
  tdrStyle->SetStatTextColor(1);
  tdrStyle->SetStatFormat("6.4g");
  tdrStyle->SetStatBorderSize(1);
  tdrStyle->SetStatH(0.1);
  tdrStyle->SetStatW(0.15);
  // tdrStyle->SetStatStyle(Style_t style = 1001);
  // tdrStyle->SetStatX(Float_t x = 0);
  // tdrStyle->SetStatY(Float_t y = 0);

// Margins:
  tdrStyle->SetPadTopMargin(0.05);
  tdrStyle->SetPadBottomMargin(0.13);
  tdrStyle->SetPadLeftMargin(0.16);
  tdrStyle->SetPadRightMargin(0.02);

// For the Global title:

  tdrStyle->SetOptTitle(0);
  tdrStyle->SetTitleFont(42);
  tdrStyle->SetTitleColor(1);
  tdrStyle->SetTitleTextColor(1);
  tdrStyle->SetTitleFillColor(10);
  tdrStyle->SetTitleFontSize(0.05);
  // tdrStyle->SetTitleH(0); // Set the height of the title box
  // tdrStyle->SetTitleW(0); // Set the width of the title box
  // tdrStyle->SetTitleX(0); // Set the position of the title box
  // tdrStyle->SetTitleY(0.985); // Set the position of the title box
  // tdrStyle->SetTitleStyle(Style_t style = 1001);
  // tdrStyle->SetTitleBorderSize(2);

// For the axis titles:

  tdrStyle->SetTitleColor(1, "XYZ");
  tdrStyle->SetTitleFont(42, "XYZ");
  tdrStyle->SetTitleSize(0.06, "XYZ");
  // tdrStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
  // tdrStyle->SetTitleYSize(Float_t size = 0.02);
  tdrStyle->SetTitleXOffset(0.9);
  tdrStyle->SetTitleYOffset(1.25);
  // tdrStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset

// For the axis labels:

  tdrStyle->SetLabelColor(1, "XYZ");
  tdrStyle->SetLabelFont(42, "XYZ");
  tdrStyle->SetLabelOffset(0.007, "XYZ");
  tdrStyle->SetLabelSize(0.05, "XYZ");

// For the axis:

  tdrStyle->SetAxisColor(1, "XYZ");
  tdrStyle->SetStripDecimals(kTRUE);
  tdrStyle->SetTickLength(0.03, "XYZ");
  tdrStyle->SetNdivisions(510, "XYZ");
  tdrStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
  tdrStyle->SetPadTickY(1);

// Change for log plots:
  tdrStyle->SetOptLogx(0);
  tdrStyle->SetOptLogy(0);
  tdrStyle->SetOptLogz(0);

// Postscript options:
  tdrStyle->SetPaperSize(20.,20.);
  // tdrStyle->SetLineScalePS(Float_t scale = 3);
  // tdrStyle->SetLineStyleString(Int_t i, const char* text);
  // tdrStyle->SetHeaderPS(const char* header);
  // tdrStyle->SetTitlePS(const char* pstitle);

  // tdrStyle->SetBarOffset(Float_t baroff = 0.5);
  // tdrStyle->SetBarWidth(Float_t barwidth = 0.5);
  // tdrStyle->SetPaintTextFormat(const char* format = "g");
  // tdrStyle->SetPalette(Int_t ncolors = 0, Int_t* colors = 0);
  // tdrStyle->SetTimeOffset(Double_t toffset);
  // tdrStyle->SetHistMinimumZero(kTRUE);

  tdrStyle->cd();

}

int main(int argc, char *argv[]){
  // ----------------------------------------------------------------------
  // First Part: 
  //
  //  * enable the AutoLibraryLoader 
  //  * book the histograms of interest 
  //  * open the input file
  // ----------------------------------------------------------------------

  // load framework libraries
  gSystem->Load( "libFWCoreFWLite" );
  AutoLibraryLoader::enable();
  // only allow one argument for this simple example which should be the
  // the python cfg file
  if ( argc < 2 ) {
    std::cout << "Usage : " << argv[0] << " [parameters.py]" << std::endl;
    return 0;
  }
  // Input configuration
  PythonProcessDesc builder(argv[1]);
  std::vector<TDirectory*> _filesData;
  std::vector<TDirectory*> _filesMC;
  const edm::ParameterSet& parameters = builder.processDesc()->getProcessPSet()->getParameter<edm::ParameterSet>("CombinePlots");
  std::string outputFile = parameters.getParameter<std::string>("outputFile");
  std::vector<edm::ParameterSet> dataInputs = parameters.getParameter<std::vector<edm::ParameterSet> >("data");
  std::vector<edm::ParameterSet> mcInputs = parameters.getParameter<std::vector<edm::ParameterSet> >("mc");
  std::vector<edm::ParameterSet> styleTweaks = parameters.getParameter<std::vector<edm::ParameterSet> >("formating");
  // output file
  TFile *_output = TFile::Open(outputFile.c_str(),"RECREATE");
  // set the tdr Style
  setTDRStyle();
  gROOT->SetBatch();  
  // do the job
  plotCombiner combiner;
  combiner.setDatacfg(dataInputs);
  combiner.setMCcfg(mcInputs);
  combiner.setStyleTweaks(styleTweaks);
  combiner.run(_output);
  // save and quit
  _output->Write();
  _output->Close();
  return 0;
}

void plotCombiner::CombineHistos(const char* name, std::vector<TDirectory*> datadirs, std::vector<TDirectory*> mcdirs, TDirectory* output)
{
   TH1* data;
   (*datadirs.begin())->GetObject(name,data);
   data = (TH1*) data->Clone();
   TCanvas* c = new TCanvas(data->GetName(),data->GetTitle());
   THStack* stack = new THStack(data->GetName(),"MC stack");
   TLegend* leg = new TLegend(0.6,0.7,0.9,0.9);
   std::map<std::string, edm::ParameterSet>::iterator style = _styleTweaks.find(data->GetName());
   for(std::vector<TDirectory*>::const_iterator it = datadirs.begin()+1;it<datadirs.end();++it) {
     TH1* h;
     (*it)->GetObject(data->GetName(),h);
     data->Add(h);
   }
   if(style!=_styleTweaks.end()) data->Rebin(style->second.getUntrackedParameter<unsigned>("rebin",1));
   data->SetTitle("data");
   leg->AddEntry(data,"Data","LE");
   std::vector<edm::ParameterSet>::const_iterator mcConf = _mcInputs.begin();
   for(std::vector<TDirectory*>::const_iterator it = mcdirs.begin();it<mcdirs.end();++it, ++mcConf) {
     TH1* h;
     (*it)->GetObject(data->GetName(),h);
     // title
     h->SetTitle(mcConf->getParameter<std::string>("role").c_str());
     // color
     h->SetFillColor(mcConf->getParameter<unsigned int>("color"));
     // scale
     h->Scale(mcConf->getParameter<double>("scale"));
     // rebin
     if(style!=_styleTweaks.end()) h->Rebin(style->second.getUntrackedParameter<unsigned>("rebin",1));
     // add
     stack->Add(h);
     // legend
     leg->AddEntry(h,mcConf->getParameter<std::string>("role").c_str(),"f");
   }
   data->Draw("e");         // first draw data... that fixes the scale
   stack->Draw("same");     // then the stack on top
   data->Draw("e, same");   // and again data to see all points
   leg->Draw();
   if(style!=_styleTweaks.end()) {
     // we might add in the config file a set of entries to set labels, axis, etc.
     // everything is done using untracked parameters, so it is easy and quick to add things.
     data->SetXTitle(style->second.getUntrackedParameter("labelx",std::string("")).c_str());
     data->SetYTitle(style->second.getUntrackedParameter("labely",std::string("")).c_str());
     if(style->second.getUntrackedParameter("logx",false)) c->SetLogx();
     if(style->second.getUntrackedParameter("logy",false)) c->SetLogy();
     std::vector<double> xrange = style->second.getUntrackedParameter("rangex",std::vector<double>());
     if(xrange.size()==2) data->GetXaxis()->SetRangeUser(xrange[0],xrange[1]);
   }
   output->WriteObject(c,c->GetName());
   delete c;
}

void plotCombiner::CombineDir(std::vector<TDirectory*> datadirs, std::vector<TDirectory*> mcdirs, TDirectory* output)
{
   TDirectory* datadir = datadirs[0];
   TList* keys = datadir->GetListOfKeys();
   TIter next(keys);
   TKey *key;
   while ((key = (TKey*) next())) {
     if(key->IsFolder()) {
        std::vector<TDirectory*> dataitems;
        for(std::vector<TDirectory*>::const_iterator it = datadirs.begin();it<datadirs.end();++it) {
          TDirectory* dir;
          (*it)->GetObject(key->GetName(),dir);
          dataitems.push_back(dir);
        }
        std::vector<TDirectory*> mcitems;
        for(std::vector<TDirectory*>::const_iterator it = mcdirs.begin();it<mcdirs.end();++it) {
          TDirectory* dir;
          (*it)->GetObject(key->GetName(),dir);
          mcitems.push_back(dir);
        }
        CombineDir(dataitems, mcitems, output->mkdir(key->GetName()));
     } else if (key->ReadObj()->InheritsFrom("TH1")) {
        CombineHistos(key->GetName(),datadirs,mcdirs,output);
     }
   }
}

