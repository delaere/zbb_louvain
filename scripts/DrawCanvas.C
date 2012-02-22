#include "TCanvas.h"
#include "TLegend.h"
#include "TH1F.h"
#include "THStack.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TPad.h"
#include "TLatex.h"
#include "TFrame.h"
#include "TF1.h"
#include "TGraphAsymmErrors.h"
#include <string>
#include <iostream>

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
  gStyle->SetStatFontSize(0.04);///---> gStyle->SetStatFontSize(0.025);
  gStyle->SetStatTextColor(1);
  gStyle->SetStatFormat("6.4g");
  gStyle->SetStatBorderSize(1);
  gStyle->SetStatH(0.1);
  gStyle->SetStatW(0.2);///---> gStyle->SetStatW(0.15);
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
  gStyle->SetTitleSize(0.05, "XYZ");
  gStyle->SetTitleXOffset(1.1);
  gStyle->SetTitleYOffset(1.25);
  // For the axis labels:
  gStyle->SetLabelColor(1, "XYZ");
  gStyle->SetLabelFont(42, "XYZ");
  gStyle->SetLabelOffset(0.007, "XYZ");
  gStyle->SetLabelSize(0.045, "XYZ");
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
  gROOT->ForceStyle();
  gROOT->UseCurrentStyle();
}

void DrawCanvas(TCanvas* canvas, bool SSVHE=false, bool SSVHP=false, const char* addLabel=NULL)
{
  setTDRStyle();
  // retrieve the frame
  TFrame* frame = (TFrame*) canvas->FindObject("TFrame");
  // draw the canvas
  canvas->Draw();
  // fix the size
  float borderX = canvas->GetWindowWidth()-canvas->GetWw();
  float borderY = canvas->GetWindowHeight()-canvas->GetWh();
  canvas->SetCanvasSize(500,500);
  canvas->SetWindowSize(500+borderX,500+borderY);
  // add the label
  TLatex lat;
  lat.SetTextSize(0.04);
  frame = (TFrame*) canvas->FindObject("TFrame");
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
  lat.DrawLatex(x,y,"#splitline{CMS Preliminary}{#sqrt{s} = 7 TeV, L = 2.1 fb^{-1}}");
  if(SSVHE) {
    x = frame->GetX1() + (frame->GetX2()-frame->GetX1())*0.53;
    y = frame->GetY2() - (frame->GetY2()-frame->GetY1())*0.5;
    lat.DrawLatex(x,y,"High Efficiency b-tagging");
  } else if(SSVHP) {
    x = frame->GetX1() + (frame->GetX2()-frame->GetX1())*0.53;
    y = frame->GetY2() - (frame->GetY2()-frame->GetY1())*0.5;
    lat.DrawLatex(x,y,"High Purity b-tagging");
  }
  if(addLabel) {
    x = frame->GetX1() + (frame->GetX2()-frame->GetX1())*0.53;
    y = frame->GetY2() - (frame->GetY2()-frame->GetY1())*0.5;
    lat.DrawLatex(x,y,addLabel);
  }
  // polish the legend
  TLegend* legend = ((TLegend*)canvas->FindObject("TPave"));
  if(legend) {
    legend->SetFillColor(kWhite);
    legend->SetBorderSize(0);
  }
  canvas->RedrawAxis();
  // now it is up to you to arrange things and save
}

TCanvas* DrawCanvasWithRatio(TCanvas* canvas)
{
  // get data and total MC from the canvas
  TIter next(canvas->GetListOfPrimitives());
  TIter* mc = NULL;
  TH1F* data = NULL;
  TObject* obj = NULL;
  while ((obj = next())) {
    if(std::string(obj->GetName())==std::string(canvas->GetName()) && obj->InheritsFrom("TH1")) {
      data = (TH1F*)obj;
    }
    if(std::string(obj->GetName())==std::string(canvas->GetName()) && obj->InheritsFrom("THStack")) {
      mc = new TIter(((THStack*)obj)->GetHists());
    }
  }
  TH1F* histo_ratio = (TH1F*)(data ? data->Clone() : NULL);
  TH1F* totmc = NULL;
  if(mc) {
    while ((obj = mc->Next())) {
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
  // set ratio to 1 for empty bins
  //for(int i=0;i<=histo_ratio->GetNbinsX();++i) {
  //  if(histo_ratio->GetBinContent(i)==0) {
  //    histo_ratio->SetBinContent(i,1);
  //    histo_ratio->SetBinError(i,0);
  //  }
  //}
  // create the uncertainty histogram
  TH1F* mc_uncertainty = (TH1F*)totmc->Clone();
  //for(unsigned bin = 0; bin<=mc_uncertainty->GetNbinsx(); ++bin) mc_uncertainty->SetBinContent(mc_uncertainty->GetBinError());
  mc_uncertainty->Divide(totmc);
  // set uncertainty to 0 for empty bins
  for(int i=0;i<=mc_uncertainty->GetNbinsX();++i) {
    if(mc_uncertainty->GetBinContent(i)==0) {
      mc_uncertainty->SetBinContent(i,1);
      mc_uncertainty->SetBinError(i,0);
    }
  }
  // set the color
  mc_uncertainty->SetFillColor(kYellow);
  // create a new canvas with two pads
  TCanvas* c = new TCanvas(Form("%s_withRatio",canvas->GetName()),Form("%s with ratio",canvas->GetTitle()),500,640);
  TPad *canvas_1 = new TPad("canvas_1", canvas->GetTitle(),0,0.22,1.0,1.0);
  canvas_1->Draw();
  TPad *canvas_2 = new TPad("canvas_2", Form("%s ratio",canvas->GetTitle()),0,0.,1.0,0.22);
  canvas_2->Draw();
  // in pad 1, put a copy of the input
  canvas_1->cd();
  canvas->DrawClonePad();
  // in pad 2, put the ratio plot and the relative uncertainty from MC
  canvas_2->cd();
  gPad->SetBottomMargin(0.375);
  gPad->SetGridy();
  gPad->SetGridx();
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
  mc_uncertainty->SetMinimum(0.);
  mc_uncertainty->SetMaximum(2.);
  histo_ratio->SetMarkerStyle(20);
  histo_ratio->SetMarkerSize(0.7);
  histo_ratio->Draw("E1X0 same");
  // return the new canvas
  return c;
}

void addErrorBand(TF1* errorFunction=NULL) {
  // finds the stack
  TIter next(gPad->GetListOfPrimitives());
  THStack* stack = NULL;
  TObject* obj = NULL;
  while(obj = next()) {
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
      err = sqrt(err2);
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
}

// Extension for JES + Btag efficiency uncertainty
void addErrorBandFromTH1(TH1* minusHistoJES=NULL, TH1* plusHistoJES=NULL, TH1* minusHistoBtag=NULL, TH1* plusHistoBtag=NULL) {
  // finds the stack
  TIter next(gPad->GetListOfPrimitives());
  THStack* stack = NULL;
  TObject* obj = NULL;
  while(obj = next()) {
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
  TGraphAsymmErrors* TG_systematics = NULL;
  TG_systematics = new TGraphAsymmErrors(systematics);

  if(minusHistoJES && plusHistoJES &&  TG_systematics) {
    for(int i=1; i<=systematics->GetNbinsX(); ++i) {
      
      // extracting the errors ---------------------------------------
      
      double minusErrorJES = minusHistoJES->GetBinContent(i)- systematics->GetBinContent(i); 
      double plusErrorJES  = plusHistoJES->GetBinContent(i)- systematics->GetBinContent(i);
      //std::cout<< "bin content "<<i<< " is "<< systematics->GetBinContent(i) << std::endl;

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
      TG_systematics ->SetPointEXhigh(i-1,(systematics->GetBinWidth(i)/2)*0.75);   
      TG_systematics ->SetPointEXlow(i-1,(systematics->GetBinWidth(i)/2)*0.75);  
      
      // Errors along y-axis ----------------------------------------
      TG_systematics ->SetPointEYhigh(i-1,plusErrorTot);
      TG_systematics ->SetPointEYlow(i-1,minusErrorTot);
    }
  }
  // draw the uncertainty on top of everything.
  // Note: we have to change the ErrorX, which impacts the data as well.
  TG_systematics->SetFillColor(1);
  TG_systematics->SetFillStyle(3001); 
  gStyle->SetErrorX(0.4); 
  TG_systematics->Draw("E2,same");
}

