#include "TCanvas.h"
#include "TLegend.h"
#include "TH1F.h"
#include "TMath.h"
#include "THStack.h"
#include "TObject.h"
#include "TRandom.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TPad.h"
#include "TLatex.h"
#include "TFrame.h"
#include "TF1.h"
#include "TFile.h"
#include "TGraphAsymmErrors.h"
#include "CMS_label.h"
#include <string>
#include <iostream>

const char* addLabel=NULL;

// change the number of ticks marks ... : void LabelsDeflate(Option_t* axis = "X")?
// here or in combine_.py?

void setTDRStyle() {
  // For the canvas:
  gStyle->SetCanvasBorderMode(0);
  gStyle->SetCanvasColor(kWhite);
  gStyle->SetCanvasDefH(600); //Height of canvas
  gStyle->SetCanvasDefW(600); //Width of canvas
  gStyle->SetCanvasDefX(0);   //POsition on screen
  gStyle->SetCanvasDefY(0);
  // For the Pad:
  gStyle->SetPadBorderMode(0);
  gStyle->SetPadColor(kWhite);
  gStyle->SetPadGridX(false);
  gStyle->SetPadGridY(false);
  gStyle->SetGridColor(0);
  gStyle->SetGridStyle(3);
  gStyle->SetGridWidth(1);
  // For the frame:
  gStyle->SetFrameBorderMode(0);
  gStyle->SetFrameBorderSize(1);
  gStyle->SetFrameFillColor(0);
  gStyle->SetFrameFillStyle(0);
  gStyle->SetFrameLineColor(1);
  gStyle->SetFrameLineStyle(1);
  gStyle->SetFrameLineWidth(1);
  // For the histo:
  gStyle->SetHistLineColor(1);
  gStyle->SetHistLineStyle(0);
  gStyle->SetHistLineWidth(1);
  gStyle->SetEndErrorSize(2);
  gStyle->SetErrorX(0.);
  gStyle->SetMarkerStyle(20);
  // For the fit/function:
  gStyle->SetOptFit(1);
  gStyle->SetFitFormat("5.4g");
  gStyle->SetFuncColor(2);
  gStyle->SetFuncStyle(1);
  gStyle->SetFuncWidth(1);
  // For the date:
  gStyle->SetOptDate(0);
  // For the statistics box:
  gStyle->SetOptFile(0);
  gStyle->SetOptStat(0); //gStyle->SetOptStat("mr");
  gStyle->SetStatColor(kWhite);
  gStyle->SetStatFont(42);
  gStyle->SetStatFontSize(0.025);///---> gStyle->SetStatFontSize(0.025);
  gStyle->SetStatTextColor(1);
  gStyle->SetStatFormat("6.4g");
  gStyle->SetStatBorderSize(1);
  gStyle->SetStatH(0.1);
  gStyle->SetStatW(0.15);///---> gStyle->SetStatW(0.15);
  // Margins:
  gStyle->SetPadTopMargin(0.05);
  gStyle->SetPadBottomMargin(0.13);
  gStyle->SetPadLeftMargin(0.16);
  gStyle->SetPadRightMargin(0.02);
  // For the Global title:
  gStyle->SetOptTitle(0);
  gStyle->SetTitleFont(42);
  gStyle->SetTitleColor(1);
  gStyle->SetTitleTextColor(1);
  gStyle->SetTitleFillColor(10);
  gStyle->SetTitleFontSize(0.05);
  // For the axis titles:
  gStyle->SetTitleColor(1, "XYZ");
  gStyle->SetTitleFont(42, "XYZ");
  gStyle->SetTitleSize(0.06, "XYZ");
  gStyle->SetTitleXOffset(0.9);
  gStyle->SetTitleYOffset(1.25);
  // For the axis labels:
  gStyle->SetLabelColor(1, "XYZ");
  gStyle->SetLabelFont(42, "XYZ");
  gStyle->SetLabelOffset(0.007, "XYZ");
  gStyle->SetLabelSize(0.05, "XYZ");
  // For the axis:
  gStyle->SetAxisColor(1, "XYZ");
  gStyle->SetStripDecimals(kTRUE);
  gStyle->SetTickLength(0.03, "XYZ");
  gStyle->SetNdivisions(510, "XYZ");
  gStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
  gStyle->SetPadTickY(1);
  // Change for log plots:
  gStyle->SetOptLogx(0);
  gStyle->SetOptLogy(0);
  gStyle->SetOptLogz(0);
  // Postscript options:
  gStyle->SetPaperSize(20.,20.);
  gStyle->SetHatchesLineWidth(5);
  gStyle->SetHatchesSpacing(0.05);
  gROOT->ForceStyle();
  gROOT->UseCurrentStyle();
}

void DrawCanvas(TCanvas* canvas, int labelCMS=11)
{
  setTDRStyle();
  // retrieve the frame
  //TFrame* frame = (TFrame*) canvas->FindObject("TFrame");
  // draw the canvas
  canvas->Draw();
  // fix the size
  float borderX = canvas->GetWindowWidth()-canvas->GetWw();
  float borderY = canvas->GetWindowHeight()-canvas->GetWh();
  canvas->SetCanvasSize(500,500);
  canvas->SetWindowSize(500+borderX,500+borderY);
  // move the legend to the place it should be
  TLegend* legend = ((TLegend*)canvas->FindObject("TPave"));
  TIter next(canvas->GetListOfPrimitives());
  TLatex* label = NULL;
  TH1F* data = NULL;
  TObject* obj = NULL;
  while((obj = next())) {
    if(obj->InheritsFrom("TLatex")) {
      label = (TLatex*)obj;
      break;
    }
    if(std::string(canvas->GetName()).find(std::string(obj->GetName()))<2 && obj->InheritsFrom("TH1")) {
      data = (TH1F*)obj;
    }
  }
  if(label != NULL) {
    //legend->SetX1NDC(label->GetX());
    //legend->SetX2NDC(label->GetX()+0.3);
    legend->SetY1NDC(0.65 - 0.04);
    legend->SetY2NDC(0.95 - 0.04);
    //legend->Draw();
  }
  // add the label
  TLatex lat;
  //TFrame frame;
  lat.SetTextSize(0.04);
  TFrame* frame = (TFrame*) canvas->FindObject("TFrame");
  bool logx = canvas->GetLogx();
  bool logy = canvas->GetLogy();
  canvas->SetLogx(false);
  canvas->SetLogy(false);
  canvas->Modified();
  canvas->Update();
  float x = frame->GetX1() + (frame->GetX2()-frame->GetX1())*0.03;
  float y = frame->GetY2() - (frame->GetY2()-frame->GetY1())*0.1;
  canvas->UseCurrentStyle();
  canvas->SetLogx(logx);
  canvas->SetLogy(logy);
  //lat.DrawLatex(x,y,"#splitline{CMS}{#sqrt{s} = 7 TeV, L = 5.0 fb^{-1}}");
  if(addLabel) {
    x = frame->GetX1() + (frame->GetX2()-frame->GetX1())*0.53;
    y = frame->GetY2() - (frame->GetY2()-frame->GetY1())*0.5;
    lat.DrawLatex(x,y,addLabel);
  }
  CMS_lumi(canvas, 2, labelCMS );
  //data->GetXaxis()->SetNdivisions(12, 2, 0, true); //for MET significance 
  data->GetXaxis()->SetNdivisions(10, 4, 3, true);
  //data->GetXaxis()->SetRange(0,10); 
  data->Draw("sameaxis");
  // redraw the axis on top of everything
  //canvas->RedrawAxis();
  // now it is up to you to arrange things and save
}

TCanvas* DrawCanvasWithRatio(TCanvas* canvas, bool emptyBinsNoUnc = true)
{
  // get data and total MC from the canvas
  TIter next(canvas->GetListOfPrimitives());
  TIter* mc = NULL;
  TH1F* data = NULL;
  TObject* obj = NULL;
  bool isMCfound = false;
  while ((obj = next())) {
    if(std::string(canvas->GetName()).find(std::string(obj->GetName()))<2 && obj->InheritsFrom("TH1")) {
      data = (TH1F*)obj;
    }
    if(std::string(canvas->GetName()).find(std::string(obj->GetName()))<2 && obj->InheritsFrom("THStack") && !isMCfound) {
      mc = new TIter(((THStack*)obj)->GetHists());  
      isMCfound = true;          
    }
  }
  TH1F* histo_ratio = (TH1F*)(data ? data->Clone() : NULL);
  TH1F* totmc = NULL;
  if(mc) {
    while (((obj = mc->Next()))) {
      if(totmc) {
        totmc->Add((TH1*)obj);
      } else {
        totmc = (TH1F*)((TH1*)obj)->Clone();
      }
    }
  }
  // if data or MC is missing, simply return the input
  if(totmc == NULL || histo_ratio == NULL) {
    return (TCanvas*) canvas->DrawClone();
  }
  // create the ratio histogram
  histo_ratio->SetName("histo_ratio");
  histo_ratio->SetTitle("");
  histo_ratio->Sumw2();
  histo_ratio->Divide(totmc);
  // create the uncertainty histogram
  TH1F* mc_uncertainty = (TH1F*)totmc->Clone();
  mc_uncertainty->Divide(totmc);
  // set uncertainty to 0 or 1 for empty bins
  for(int i=0;i<=mc_uncertainty->GetNbinsX();++i) {
    if(mc_uncertainty->GetBinContent(i)==0) {
      mc_uncertainty->SetBinContent(i,1);
      mc_uncertainty->SetBinError(i,emptyBinsNoUnc? 0. : 1.);
    }
  }
  // set the color
  mc_uncertainty->SetFillColor(kYellow); 
  // create a new canvas with two pads
  TCanvas* c = new TCanvas(Form("%s_withRatio",canvas->GetName()),Form("%s with ratio",canvas->GetTitle()),500,640);
  TPad *canvas_1 = new TPad("canvas_1", canvas->GetTitle(),0,0.22,1.0,1.0);
  canvas_1->SetNumber(1);
  canvas_1->Draw();
  TPad *canvas_2 = new TPad("canvas_2", Form("%s ratio",canvas->GetTitle()),0,0.,1.0,0.22);
  canvas_2->SetNumber(2);
  canvas_2->Draw();
  // in pad 1, put a copy of the input
  canvas_1->cd();
  canvas->DrawClonePad();
  // in pad 2, put the ratio plot and the relative uncertainty from MC
  canvas_2->cd();
  gPad->SetBottomMargin(0.375);
  gPad->SetGridy();
  gPad->SetGridx();
  mc_uncertainty->GetYaxis()->SetRangeUser(0.5,1.5);
  mc_uncertainty->Draw("E3");
  mc_uncertainty->GetYaxis()->SetTitle("Data/MC");
  mc_uncertainty->GetYaxis()->SetTitleFont(42);
  mc_uncertainty->GetYaxis()->SetTitleOffset( 0.4 );
  mc_uncertainty->GetYaxis()->SetTitleSize( 0.17 );
  mc_uncertainty->GetYaxis()->SetLabelFont(42);
  mc_uncertainty->GetYaxis()->SetLabelSize(0.16);
  mc_uncertainty->GetYaxis()->SetNdivisions( 505 );
  mc_uncertainty->GetXaxis()->SetTitle(data->GetXaxis()->GetTitle());
  mc_uncertainty->GetXaxis()->SetTitleFont(42);
  mc_uncertainty->GetXaxis()->SetTitleSize( 0.17 );
  mc_uncertainty->GetXaxis()->SetLabelSize(0.16);
  mc_uncertainty->GetXaxis()->SetLabelFont(42);
  mc_uncertainty->GetXaxis()->SetRange(data->GetXaxis()->GetFirst(), data->GetXaxis()->GetLast());
  //mc_uncertainty->SetMinimum(0.);
  //mc_uncertainty->SetMaximum(2.8);
  mc_uncertainty->GetXaxis()->SetNdivisions(10, 2, 0, true);
  histo_ratio->SetMarkerStyle(20);
  histo_ratio->SetMarkerSize(0.7);
  histo_ratio->Draw("E1X0 same");
  //histo_ratio->Draw("E0X0 same");
  mc_uncertainty->Draw("AXIG same");
  // return the new canvas
  return c;
}

void addErrorBand(TF1* errorFunction=NULL) {
  // finds the stack
  TIter next(gPad->GetListOfPrimitives());
  THStack* stack = NULL;
  TObject* obj = NULL;
  while((obj = next())) {
    if(obj->InheritsFrom("THStack")) {
      stack = (THStack*)obj;
      break;
    }
  }
  if(stack==NULL) {
   std::cerr << "ERROR: MC histogram not found" << std::endl;
   return;
  }
  // get the total histogram, clone it
  TH1* systematics = (TH1*)stack->GetStack()->Last()->Clone("systematics");
  // add the syst uncertainty in quadrature to the stat uncertainty
  if(errorFunction) {
    for(int i=1; i<=systematics->GetNbinsX(); ++i) {
      // errorFunction is the relative uncertainty at the center of the bin
      double err = errorFunction->Eval(systematics->GetBinCenter(i))*systematics->GetBinContent(i);
      // we add it in quadrature to the stat uncertainty
      double err2 = err*err + systematics->GetBinError(i)*systematics->GetBinError(i);
      err = TMath::Sqrt(err2);
      // set it
      systematics->SetBinError(i,err);
    }
  }
  
  // draw the uncertainty on top of everything.
  // Note: we have to change the ErrorX, which impacts the data as well.
  systematics->SetFillColor(1);
  systematics->SetFillStyle(3001);
  gStyle->SetErrorX(0.4);
  systematics->Draw("E2,same");

  // add a legend
  TLegend* legend = new TLegend(0.1,0.7,0.48,0.9);
  if(legend) {
    legend->AddEntry(systematics,"JES","f");
    legend->SetFillColor(kWhite);
    legend->SetBorderSize(0);
    legend->Draw();
    
  }
}

// Extension for JES + Btag efficiency uncertainty
//Here are my files for systematics :
//file_JES = /home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/combined_Plots_JES_final_V_SaveHisto_Combined.root
//file_B = /home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/combined_Plots_BMMM_harcoded_RDS_V_HistoSaved_Combined.root

void addErrorBandFromTH1(TH1* minusHistoJES=NULL, TH1* plusHistoJES=NULL, TH1* minusHistoBtag=NULL, TH1* plusHistoBtag=NULL) {
  // finds the stack
  TPad* histoPad = (TPad*)gPad->GetCanvas()->cd(1); 
  //TPad* ratioPad = (TPad*)gPad->GetCanvas()->cd(2); 
  histoPad->cd();

  TIter next(histoPad->GetListOfPrimitives());
  histoPad->ls();
  THStack* stack = NULL;
  TH1F* data = NULL;
  TLegend* legend = NULL; 
  TObject* obj = NULL;
  while((obj = next())) {
    if(obj->InheritsFrom("THStack") && !stack) {
      stack = (THStack*)obj;
    }
    if(obj->InheritsFrom("TH1") && !data) {
      data = (TH1F*)obj;
    }
    if(obj->InheritsFrom("TLegend") && !legend) {
      legend = (TLegend*)obj;
    }
    if(stack && data && legend) break;
  }
  if(stack==NULL) {
   std::cerr << "ERROR: MC histogram not found" << std::endl;
   return;
  }
  if(data==NULL) {
   std::cerr << "ERROR: data histogram not found" << std::endl;
   return;
  }
  if(legend==NULL) {
   std::cerr << "ERROR: Legend not found" << std::endl;
   return;
  }

  // get the total histogram, clone it
  TH1* systematics = (TH1*)stack->GetStack()->Last()->Clone("systematics");
  // add the syst uncertainty in quadrature to the stat uncertainty
  TGraphAsymmErrors* TG_systematics = NULL;
  TG_systematics = new TGraphAsymmErrors(systematics);

  if(minusHistoJES && plusHistoJES &&  TG_systematics) {
    for(int i=1; i<=systematics->GetNbinsX(); ++i) {
      
      // extracting the errors ---------------------------------------
      
      double minusErrorJES = minusHistoJES->GetBinContent(i)- systematics->GetBinContent(i); 
      double plusErrorJES  = plusHistoJES->GetBinContent(i)- systematics->GetBinContent(i);
      std::cout<< "bin content "<<i<< " is "<< systematics->GetBinError(i) << std::endl;

      // combining with statistical ---------------------------------------      

      double minusErrorTot = sqrt(minusErrorJES*minusErrorJES + systematics->GetBinError(i)*systematics->GetBinError(i));
    double plusErrorTot = sqrt(plusErrorJES*plusErrorJES + systematics->GetBinError(i)*systematics->GetBinError(i));
        
      if(minusHistoBtag && plusHistoBtag){	
	double minusErrorBtag = minusHistoBtag->GetBinContent(i)- systematics->GetBinContent(i); 
	double plusErrorBtag  = plusHistoBtag->GetBinContent(i)- systematics->GetBinContent(i);
       
	minusErrorTot = sqrt(minusErrorJES*minusErrorJES + minusErrorBtag*minusErrorBtag + systematics->GetBinError(i)*systematics->GetBinError(i));
	plusErrorTot = sqrt(plusErrorJES*plusErrorJES + plusErrorBtag*plusErrorBtag + systematics->GetBinError(i)*systematics->GetBinError(i));
      }

      //setting the errors and the mean value --------------------------------
      // Errors along x-axis, just for aesthetics  ----------------------------
      //TG_systematics ->SetPointEXhigh(i-1,(systematics->GetBinWidth(i)/2)*0.75);   
      TG_systematics ->SetPointEXhigh(i-1,(systematics->GetBinWidth(i)/2)*1.05);   
      TG_systematics ->SetPointEXlow(i-1,(systematics->GetBinWidth(i)/2)*0.95);  
      
      // Errors along y-axis ----------------------------------------
      TG_systematics ->SetPointEYhigh(i-1,plusErrorTot);
      TG_systematics ->SetPointEYlow(i-1,minusErrorTot);
    }
  }
  // draw the uncertainty on top of everything.
  // Note: we have to change the ErrorX, which impacts the data as well.
  // 2012 Style for uncertainties band
  //  TG_systematics->SetFillColor(1);
  //TG_systematics->SetFillStyle(3001); 
  
  // 2013 "Wbb" Style for uncertainties band
  //gStyle->SetHatchesSpacing(1.0);
  //gStyle->SetHatchesLineWidth(2);
  TG_systematics->SetLineColor(0);
  TG_systematics->SetFillColor(kBlack);
  TG_systematics->SetFillStyle(3004); 
  gStyle->SetErrorX(0.4);
  TG_systematics->Draw("E2,same");
  data->Draw("p,same");

  legend->SetX1NDC(0.65 - 0.04);
  //legend->SetX2NDC(0.75 - 0.04);
  legend->SetX2NDC(1.05 - 0.04);
  legend->SetX2NDC(1.05 - 0.04);
  legend->SetY1NDC(0.65 - 0.04);
  legend->SetY2NDC(1.05 - 0.04);
  legend->AddEntry(TG_systematics,"JES + b-tag","f");
  //legend->AddEntry(TG_systematics,"JES + b-tag + stat.","f");
  TGraphAsymmErrors* for_style= (TGraphAsymmErrors*) TG_systematics->Clone();
  for_style->SetLineColor(kWhite);
  for_style->SetFillColor(kWhite);
  //legend->AddEntry(TG_systematics,"#splitline{JES}{#splitline{+ b-tag}{+ stat.}}","f");*/
  legend->AddEntry(for_style,"+ stat. unc. ","f");
  legend->Draw();    
}

void addErrorBandFromTF1(TF1* errorFunctionMinus=NULL, TF1* errorFunctionPlus=NULL) {
  //define functions
  //TFile *file1  = new TFile("JES_pTlead.root"); 
  //TFile *file1  = new TFile("JES_pTsublead.root"); 
  //TFile *file1  = new TFile("JES_pTbb.root"); 
  
  //TFile *file1  = new TFile("pTZJES.root"); 
  
  TFile *file1  = new TFile("pTZBtag.root");
  
  //TFile *file1  = new TFile("pTbbJESBtag.root"); 
  //TFile *file1  = new TFile("pTZJESBtag.root"); 
  //TFile *file1  = new TFile("pTbbJESBtagSq.root"); 
  //TFile *file1  = new TFile("pTbbJESBtagSq.root"); 

  
  errorFunctionMinus =(TF1*)file1->Get("funcminus");
  errorFunctionPlus =(TF1*)file1->Get("funcplus");


  // finds the stack
  TIter next(gPad->GetListOfPrimitives());
  THStack* stack = NULL;
  TObject* obj = NULL;
  while((obj = next())) {
    if(obj->InheritsFrom("THStack")) {
      stack = (THStack*)obj;
      break;
    }
  }
  if(stack==NULL) {
   std::cerr << "ERROR: MC histogram not found" << std::endl;
   return;
  }
  // get the total histogram, clone it
  TH1* systematics = (TH1*)stack->GetStack()->Last()->Clone("systematics");
  TGraphAsymmErrors* TG_systematics = NULL;
  TG_systematics = new TGraphAsymmErrors(systematics);


  // add the syst uncertainty in quadrature to the stat uncertainty
  if(errorFunctionMinus && errorFunctionPlus &&  TG_systematics) {
    for(int i=1; i<=systematics->GetNbinsX(); ++i) {
      // errorFunction is the relative uncertainty at the center of the bin
      double errPlus  = errorFunctionPlus->Eval(systematics->GetBinCenter(i))*systematics->GetBinContent(i);
      double errMinus = errorFunctionMinus->Eval(systematics->GetBinCenter(i))*systematics->GetBinContent(i);      
      // we add it in quadrature to the stat uncertainty
      // set it
      TG_systematics ->SetPointEXhigh(i-1,(systematics->GetBinWidth(i)/2)*0.75);   
      TG_systematics ->SetPointEXlow(i-1,(systematics->GetBinWidth(i)/2)*0.75);  
    
      // Errors along y-axis ----------------------------------------
      TG_systematics ->SetPointEYhigh(i-1,errPlus);
      TG_systematics ->SetPointEYlow(i-1,errMinus);
 
    }
  }
  // draw the uncertainty on top of everything.
  // Note: we have to change the ErrorX, which impacts the data as well.
  TG_systematics->SetFillColor(1);
  TG_systematics->SetFillStyle(3001); 
  gStyle->SetErrorX(0.4); 
  TG_systematics->Draw("E2,same");

  TLegend* legend = new TLegend(0.1,0.7,0.48,0.9);
  if(legend) {
    //legend->AddEntry(TG_systematics," JES Uncertainty","f");
    legend->SetY1NDC(0.65 - 0.04);
    legend->SetY2NDC(1.05 - 0.04);
    legend->AddEntry(TG_systematics," B Uncertainty","f");
    //legend->AddEntry(TG_systematics," JES + B-Tag Uncertainties","f");
    legend->SetFillColor(kWhite);
    legend->SetBorderSize(0);
    legend->Draw();    
  }
}

// Extension for generic uncertainty in the ratio plot
void addErrorBandToRatioFromTH1(TH1* minusHisto=NULL, TH1* plusHisto=NULL, int color=kBlue, int linestyle=0) {
  // find each of the two pads
  TPad* histoPad = (TPad*)gPad->GetCanvas()->cd(1); 
  TPad* ratioPad = (TPad*)gPad->GetCanvas()->cd(2); 
  // find the stack 
  TIter next(histoPad->GetListOfPrimitives());
  THStack* stack = NULL;
  TObject* obj = NULL;
  while((obj = next())) {
    if(obj->InheritsFrom("THStack")) {
      stack = (THStack*)obj;
      break;
    }
  }
  if(stack==NULL) {
   std::cerr << "ERROR: MC histogram not found" << std::endl;
   return;
  }
  
  TH1D* data = NULL;
  TIter nextratio(ratioPad->GetListOfPrimitives());
  while((obj = nextratio())) {
    cout << "obj get name = " << obj->GetName() <<endl;
    string js = obj->GetName();
    if(js.find("ratio")<10) {
      data = (TH1D*)obj;
    }
  }
  // get the total histogram, clone it
  TH1* systematics = (TH1*)stack->GetStack()->Last()->Clone("systematics");
  // histograms with the systematics up and down
  TH1* H_systematicsP = (TH1*)systematics->Clone("systematicsPlus");
  H_systematicsP->Reset();
  H_systematicsP->SetLineColor(color);
  H_systematicsP->SetFillStyle(0);
  H_systematicsP->SetLineStyle(linestyle);

  TH1* H_systematicsM = (TH1*)systematics->Clone("systematicsMinus");
  H_systematicsM->Reset();
  H_systematicsM->SetLineColor(color);
  H_systematicsM->SetFillStyle(0);
  H_systematicsM->SetLineStyle(linestyle);
  for(int i=1; i<=systematics->GetNbinsX(); ++i) {
    // extracting the errors ---------------------------------------
    double minusError = minusHisto->GetBinContent(i)/systematics->GetBinContent(i);
    double plusError  = plusHisto->GetBinContent(i)/systematics->GetBinContent(i);
    if (TMath::IsNaN(minusError)) minusError = 1.;
    if (TMath::IsNaN(plusError)) plusError = 1.;
    //setting the errors and the mean value --------------------------------
    H_systematicsP->SetBinContent(i,plusError);
    H_systematicsM->SetBinContent(i,minusError);
  }
  // draw the uncertainty on top of everything in the ratio pad.
  ratioPad->cd();
  H_systematicsP->Draw("same");
  H_systematicsM->Draw("same");

  data->Draw("E1X0 same");

}

// function to extract the total MC from a file+path
TH1* getHisto(TFile* file, TString& path) {
  // save current pad and directory
  TVirtualPad* pad = gPad;
  TDirectory* dir = gDirectory;
  // go to the TCanvas
  TCanvas* thePad = (TCanvas*)file->Get(path);
  // find the stack
  TIter next(thePad->GetListOfPrimitives());
  THStack* stack = NULL;
  TObject* obj = NULL;
  while((obj = next())) {
    if(obj->InheritsFrom("THStack")) {
      stack = (THStack*)obj;
      break;
    }
  }
  if(stack==NULL) {
   std::cerr << "ERROR: MC histogram not found" << std::endl;
   return NULL;
  }
  // get the total histogram, clone it
  TH1* systematics = (TH1*)stack->GetStack()->Last()->Clone("systematics");
  // return to original location
  dir->cd();
  pad->cd();
  // return result
  return systematics;
}

// function to get the current path, including canvas name
TString mypath()
{
  // path name
  TString pathString(gDirectory->GetPath());
  pathString.Replace(0,pathString.First(":")+1,"");
  // canvas name
  TString canvasName(gPad->GetCanvas()->GetName());
  if (canvasName.Index("_withRatio")!=-1)
    canvasName.Remove(canvasName.Index("_withRatio"));
  else
    std::cout << "Warning: this doesn't seem to be a canvas drawn with Ratio" << std::endl;
  // all together
  pathString.Append("/");
  pathString.Append(canvasName);
  return pathString;
}

// Extension for generic uncertainty in the MAIN plot, directly from files
void addErrorBandFromFiles(TFile* file_minusJES, TFile* file_plusJES,TFile* file_minusBtag, TFile* file_plusBtag) {
  // get the path
  TString path = mypath();
  // get the histograms for systematics
  TH1* h_minusJES = getHisto(file_minusJES, path);
  TH1* h_plusJES  = getHisto(file_plusJES, path);
  TH1* h_minusBtag = getHisto(file_minusBtag, path);
  TH1* h_plusBtag  = getHisto(file_plusBtag, path);

  addErrorBandFromTH1(h_minusJES,h_plusJES,h_minusBtag,h_plusBtag);
}


// Extension for generic uncertainty in the ratio plot, directly from files
void addErrorBandToRatioFromFiles(TFile* file_minus, TFile* file_plus, int color, int linestyle) {
  // get the path
  TString path = mypath();
  // get the histograms for systematics
  TH1* h_minus = getHisto(file_minus, path);
  TH1* h_plus  = getHisto(file_plus, path);
  // add to plot
  addErrorBandToRatioFromTH1(h_minus, h_plus, color, linestyle);
}

