#include <vector>
#include <map>
#include <iostream>
#include <string>
#include "FWCore/ParameterSet/interface/ProcessDesc.h"
#include "FWCore/FWLite/interface/AutoLibraryLoader.h"
#include "FWCore/PythonParameterSet/interface/PythonProcessDesc.h"
#include <TDirectory.h>
#include <TFile.h>
#include <TH1.h>
#include <TROOT.h>
#include <TMath.h>
#include <TSystem.h>
#include <TCanvas.h>
#include <THStack.h>
#include <TList.h>
#include <TKey.h>
#include <TStyle.h>
#include <TLegend.h>
#include <TLatex.h>
#include <TFrame.h>

class plotCombiner {

   public:
     plotCombiner(edm::ParameterSet& options) {
       _nostack = options.getUntrackedParameter("nostack",false);
       _lumi = options.getUntrackedParameter("luminosity",1.);
       _rescaleMu = options.getUntrackedParameter("lumiMuCor",1.);
       _autoLumiScaling = options.getUntrackedParameter("autoLumiScaling",false);
       _lat = new TLatex(0.2,0.87,options.getUntrackedParameter("label",std::string("")).c_str());
       _leg = new TLegend(0.6,0.7,0.9,0.9);
       _legendCompleted = false;
     }
     ~plotCombiner() { 
       delete _lat;
       delete _leg;
     }
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
     void resetLegend() {
       delete _leg;
       _leg = new TLegend(0.6,0.7,0.9,0.9);
       _legendCompleted = false;
     }
   private:
     void CombineHistos(const char* name, std::vector<TDirectory*> datadirs, std::vector<TDirectory*> mcdirs, TDirectory* output, std::string channel, std::string stage);
     void CombineDir(std::vector<TDirectory*> datadirs, std::vector<TDirectory*> mcdirs, TDirectory* output);
     TH1* Rebin(TH1* h,std::map<std::string, edm::ParameterSet>::iterator& style);
     void showOverflow(TH1* h);
     std::vector<edm::ParameterSet> _dataInputs;
     std::vector<edm::ParameterSet> _mcInputs;
     std::vector<TDirectory*> _filesData;
     std::vector<TDirectory*> _filesMC;
     std::map<std::string, edm::ParameterSet> _styleTweaks;
     bool _nostack, _autoLumiScaling, _legendCompleted;
     double _lumi;
     TLegend* _leg;
     TLatex* _lat;
     double _rescaleMu;
     std::string channel;
     std::string stage;

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
  tdrStyle->SetHistLineColor(1);
  tdrStyle->SetHistLineStyle(0);
  tdrStyle->SetHistLineWidth(1);
  tdrStyle->SetEndErrorSize(2);
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
  // For the axis titles:
  tdrStyle->SetTitleColor(1, "XYZ");
  tdrStyle->SetTitleFont(42, "XYZ");
  tdrStyle->SetTitleSize(0.06, "XYZ");
  tdrStyle->SetTitleXOffset(0.9);
  tdrStyle->SetTitleYOffset(1.5);
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
  // make active
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
  edm::ParameterSet options = parameters.getParameter<edm::ParameterSet>("options");
  std::vector<edm::ParameterSet> dataInputs = parameters.getParameter<std::vector<edm::ParameterSet> >("data");
  std::vector<edm::ParameterSet> mcInputs = parameters.getParameter<std::vector<edm::ParameterSet> >("mc");
  std::vector<edm::ParameterSet> styleTweaks = parameters.getParameter<std::vector<edm::ParameterSet> >("formating");
  // output file
  TFile *_output = TFile::Open(outputFile.c_str(),"RECREATE");
  // set the tdr Style
  setTDRStyle();
  gROOT->SetBatch();  
  gROOT->SetStyle("tdrStyle");
  // do the job
  plotCombiner combiner(options);
  combiner.setDatacfg(dataInputs);
  combiner.setMCcfg(mcInputs);
  combiner.setStyleTweaks(styleTweaks);
  combiner.run(_output);
  // save and quit
  _output->Write();
  _output->Close();
  std::cout << "Done." << std::endl;
  return 0;
}

void plotCombiner::CombineHistos(const char* name, std::vector<TDirectory*> datadirs, std::vector<TDirectory*> mcdirs, TDirectory* output, std::string channel, std::string stage)
{
   // we need something called data to initialize the canvas and stack.
   // if no data is provided, copy first MC.
   bool drawData = true;
   if(!datadirs.size()) {
     datadirs = mcdirs;
     drawData = false;
   }
   // create everything, using also first data histo
   gROOT->SetStyle("tdrStyle");
   TH1* data;
   (*datadirs.begin())->cd();
   (*datadirs.begin())->GetObject(name,data);
   data = (TH1*) data->Clone();
   TCanvas* c = new TCanvas(data->GetName(),data->GetTitle(),500,500);
   THStack* stack = new THStack(data->GetName(),"MC stack");
   THStack* nostack = new THStack(data->GetName(),"MC stack - not stacked");
   // DATA
   std::map<std::string, edm::ParameterSet>::iterator style = _styleTweaks.find(data->GetName());
   for(std::vector<TDirectory*>::const_iterator it = datadirs.begin()+1;it<datadirs.end();++it) {
     TH1* h;
     (*it)->GetObject(data->GetName(),h);
     data->Add(h);
   }
   if(style!=_styleTweaks.end()) data = Rebin(data,style);
   data->SetTitle("data");
   if(!_legendCompleted) _leg->AddEntry(data,"Data","LEP");
   // now to the MC
   int nf = 0;
   std::vector<edm::ParameterSet>::const_iterator mcConf = _mcInputs.begin();
   for(std::vector<TDirectory*>::const_iterator it = mcdirs.begin();it<mcdirs.end();++it, ++mcConf) {
     TH1* h;
     (*it)->GetObject(data->GetName(),h);
     if(!h) {delete c; return;}

     double rescaleCombined = 1;
     if(channel=="Combined"){
       //std::cout<<data->GetName()<<std::endl;
       //std::string MM = (*it)->GetName();
       //std::string MM2 = data->GetName();
       MM = "MuMuChannel/"+stage+"/"+MM+"/"+MM2;
       //std::cout<<MM<<std::endl;
       TH1F *mumu;
       _filesMC[nf]->GetObject(MM.c_str(),mumu);
       if(mumu==NULL) mumu = (TH1F*) _filesMC[nf]->Get(MM.c_str());
       if(mumu==NULL) _filesMC[nf]->GetObject((MM+"Mu").c_str(),mumu);
       if(mumu==NULL) mumu = (TH1F*) _filesMC[nf]->Get((MM+"Mu").c_str());
       if(mumu==NULL) std::cout<<"ERROR : "<<_filesMC[nf]->GetName()<<std::endl;
       int nentries = mumu->GetEntries();
       //std::cout<<data->GetName()<<std::endl;
       int Centries = h->GetEntries();
       if(Centries>0) rescaleCombined = double(Centries-nentries+nentries*_rescaleMu)/double(Centries);
       //std::cout<<rescaleCombined<<std::endl;
       nf++;
     }

     // title
     h->SetTitle(mcConf->getParameter<std::string>("role").c_str());
     // color and style
     if(mcConf->getUntrackedParameter<bool>("stacked",true) && !_nostack)
       // for stacked histograms, just set the fill color
       h->SetFillColor(mcConf->getParameter<unsigned int>("color"));
     else {
       // non-stacked histograms are drawn as a thicker line
       h->SetLineColor(mcConf->getParameter<unsigned int>("color"));
       h->SetFillStyle(0);
       h->SetLineWidth(3);
     }
     // scale
     h->Sumw2();
     double scale = mcConf->getParameter<double>("scale");
     if(channel=="MuMu") scale *= _rescaleMu;
     if(channel=="Combined") scale *= rescaleCombined;
     //if(channel=="EE") std::cout<<scale<<std::endl;
     h->Scale(scale);
     if(_autoLumiScaling)
       h->Scale(_lumi);
     // rebin
     if(style!=_styleTweaks.end()) h = Rebin(h,style);
     // add
     if(mcConf->getUntrackedParameter<bool>("stacked",true) && !_nostack) 
       stack->Add(h);
     else
       nostack->Add(h);
   }
   std::vector<edm::ParameterSet>::const_reverse_iterator mcrConf = _mcInputs.rbegin();
   // another loop on MC, in reverse order, to create the legend.
   if(!_legendCompleted) {
     for(std::vector<TDirectory*>::const_reverse_iterator it = mcdirs.rbegin();it<mcdirs.rend();++it, ++mcrConf) {
       TH1* h;
       (*it)->GetObject(data->GetName(),h);
       // legend
       if(mcrConf->getUntrackedParameter<bool>("stacked",true) && !_nostack)
         _leg->AddEntry(h,mcrConf->getParameter<std::string>("role").c_str(),"f");
       else
         _leg->AddEntry(h,mcrConf->getParameter<std::string>("role").c_str(),"l");
     }
     _legendCompleted = true;
   }
   if(drawData) {
     data->Draw("e");         // first draw data... that fixes the scale
     stack->Draw("hist, same");   // then the stack on top
     nostack->Draw("nostack, hist, same");     // then the unstacked histograms on top
     data->Draw("e, same");   // and again data to see all points
   } else {
     stack->Draw();         // draw the mc alone
     nostack->Draw("nostack, same");// draw the mc alone
   }
   // add the label from options
   float fontsize = 0.04;
   _lat->SetNDC();
   _lat->SetTextSize(fontsize);
   float datamax = data->GetBinCenter(data->GetMaximumBin());
   float xmin = data->GetXaxis()->GetXmin();
   float xmax = data->GetXaxis()->GetXmax();
   float x1 = xmin + (xmax-xmin)*0.03; // left
   float x2 = xmax - (xmax-xmin)*(0.03 + _lat->GetXsize()); // right
   bool justifyRight = true; // default
   if (datamax>x1+_lat->GetXsize() && datamax<x2) { // both are ok
     justifyRight = (x2-datamax) > (datamax-x1-_lat->GetXsize());
   } else if (datamax>x1+_lat->GetXsize()) { // left works
     justifyRight = false;
   } else if (datamax<x2) { // right works
     justifyRight = true;
   }
   _lat->SetX(justifyRight?0.925-_lat->GetXsize():0.2);
   _lat->Draw();
   // put the legend accordingly
   _leg->SetFillColor(kWhite);
   _leg->SetBorderSize(0);
   _leg->SetX1NDC(justifyRight?0.925-_lat->GetXsize():0.2);
   _leg->SetX2NDC(_leg->GetX1NDC()+0.3);
   _leg->SetY1NDC(0.65 - fontsize);
   _leg->SetY2NDC(0.85 - fontsize);
   _leg->Draw();               // draw the legend
   c->UseCurrentStyle();
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
   // cleanup
   delete c;
   // this is needed, in principle, but slows things down a lot.
   /*
   delete data;
   delete stack;
   delete nostack;
   */
}

TH1* plotCombiner::Rebin(TH1* h,std::map<std::string, edm::ParameterSet>::iterator& style)
{
       // simple rebin
       unsigned ngroup = style->second.getUntrackedParameter<unsigned>("rebin",1);
       // rebin using an explicit binning
       std::vector<double> bins = style->second.getUntrackedParameter<std::vector<double> >("bins",std::vector<double>() );
       // rebin using begin, end, width
       double begin = style->second.getUntrackedParameter<double>("begin",0);
       double end   = style->second.getUntrackedParameter<double>("end",-1);
       double width = style->second.getUntrackedParameter<double>("width",1);
       // option to show the overflow bin
       bool showOverflowbin = style->second.getUntrackedParameter<bool>("overflow",0);
       // now, prepare the array of bins
       if(end>begin && bins.size()==0) {
         width = width>h->GetBinWidth(h->GetNbinsX()/2) ? width : h->GetBinWidth(h->GetNbinsX()/2) ;
         for(double x=begin;x<end;x+=width)
	   bins.push_back(x);
         bins.push_back(end);
       }
       // actually do the rebinning
       if(bins.size()) {
         double* xbins = new double[bins.size()];
	 for(unsigned i=0;i<bins.size();++i) {
	   xbins[i] = bins[i];
	 }
	 ngroup = bins.size()-1;
         TH1* hnew = h->Rebin(ngroup,h->GetName(),xbins); 
	 h=hnew;
	 delete[] xbins;
	 if(showOverflowbin) showOverflow(hnew);
	 return hnew;
       } else {
         h->Rebin(ngroup);
	 if(showOverflowbin) showOverflow(h);
         return h;
       }
       return h;
}

void plotCombiner::showOverflow(TH1* h)
{
	// add last bin and overflow
	int nbins = h->GetNbinsX();
	double newContent = h->GetBinContent(nbins) + h->GetBinContent(nbins+1);
	double newError = TMath::Hypot(h->GetBinError(nbins), h->GetBinError(nbins+1));
	// overwrite the content of the last bin by including the content of the overflow bin
	h->SetBinContent(nbins,newContent);
	h->SetBinError(nbins,newError);
	// set the overflow to 0.
	h->SetBinContent(nbins+1,0);
	h->SetBinError(nbins+1,0);
}

void plotCombiner::CombineDir(std::vector<TDirectory*> datadirs, std::vector<TDirectory*> mcdirs, TDirectory* output)
{
   TDirectory* refdir = NULL;
   if(datadirs.size()) refdir = datadirs[0];
   else if(mcdirs.size()) refdir = mcdirs[0];
   else return;
   TList* keys = refdir->GetListOfKeys();
   TIter next(keys);
   TKey *key;
   while ((key = (TKey*) next())) {
     if(key->IsFolder()) {
	std::string k = key->GetName();
	if(k.find("MuMu")==0 || k.find("EE")==0 || k.find("Combined")==0){
	  if(k.find("MuMu")==0) channel="MuMu";
	  else if(k.find("EE")==0) channel="EE";
	  else if(k.find("Combined")==0) channel="Combined";
	  std::cout<<key->GetName()<<" , "<<channel<<std::endl;
	}
	if(k.find("stage")==0){
	  stage=k;
	}
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
        CombineDir(dataitems, mcitems, output->mkdir(key->GetName(),key->GetTitle()));
     } else if (key->ReadObj()->InheritsFrom("TH1")) {
       CombineHistos(key->GetName(),datadirs,mcdirs,output,channel,stage);
     }
   }
}

