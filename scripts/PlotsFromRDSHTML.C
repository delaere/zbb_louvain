// Usage
// .L Shapes.C
// allshapes()
#define NProcesses 2
#include <iostream>
#include <fstream>
#include <TH1F.h>
#include <TKey.h>
#include <TFile.h>
#include <TCanvas.h>
#include <TFrame.h>
#include <TROOT.h>
#include <TSystem.h>
#include <TRandom.h>
#include <TBenchmark.h>
#include <TInterpreter.h>

TString outdir = "PlotsFromRDS/";
TString InputFile = "/home/fynu/arnaudp/scratch/Zbb_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Plot_mm_100H125_ptZrew_MM_N_allR.root";
TString copyToServer02Folder = "$USER@server02.fynu.ucl.ac.be:~/public_html/private/PlotsFromRDS_re";//if empty do nothing

//******************No need to change anything below typically***************
ofstream outfile;



TFile *inputFile = 0;
void printheader() {

  outfile << "<h3> Control plots from RDS (getCP_ME) </h3><br><br>" << endl;
  outfile << "<table border=\"1\" cellpadding=\"5\" cellspacing=\"5\" width=\"100%\">" << endl;
  outfile << "<tr>" << endl;
  outfile << "<th>Stack plots</th>" << endl;
  outfile << "</tr>" << endl;

}

void printtail() {
  outfile << "</table><br><br><br>" << endl;

}


void print(TString var) {

  outfile << "<tr>" << endl;

  outfile << "<td width=\"50%\">" << endl;
  outfile << "<br><IMG SRC=\""+var+".gif"+"\" ><br>" << endl;
  outfile << "<center>" << endl;
  outfile << " <a href=\""+var+".gif"+"\">gif</a>  <a href=\""+var+".eps"+"\">eps</a>  <a href=\""+var+".pdf"+"\">pdf</a>"+var +"</td>" << endl; 

//   outfile << "<td width=\"50%\">" << endl;
//   outfile << "<br><IMG SRC=\""+var+"_log.gif"+"\" ><br>" << endl;
//   outfile << "<center>" << endl;
//   outfile << " <a href=\""+var+"_log.gif"+"\">gif</a>  <a href=\""+var+"_log.eps"+"\">eps</a>  <a href=\""+var+"_log.pdf"+"\">pdf</a> </td>" << endl; 

  outfile << "</tr>" << endl;
  outfile << "</center>" << endl;

}


void PlotCanvas(TString var = "th1_jetmetMETsignificance");
void  PlotsFromRDSHTML();

void  PlotsFromRDSHTML() {
  outfile.open(outdir+"/index.html");


  printheader();


  TString makedir = ".! mkdir " + outdir;
  gROOT->ProcessLine(makedir);


  inputFile = TFile::Open(InputFile);
 
  TList* listOfKeys = gDirectory->GetListOfKeys();
  TIter next(listOfKeys);
  TKey *key;
  while (key = (TKey*) next()) {
    TObject *obj = key->ReadObj(); //<-- Segmentation fault if listOfKeys is a clone.
    if (TString(obj->ClassName()).Contains("Canvas")) {
      if (TString(obj->GetName()).Contains("CANVASmlphiggsvsbkg")) continue;//do not plot final MLP's until we have blinding procedure
      
      std::cout << obj->GetName() << std::endl;
      PlotCanvas(obj->GetName());
      print(obj->GetName());
    }
    
  }

  printtail();
  
  if (copyToServer02Folder != "") {
    TString copytoweb = ".! scp  -r " + outdir + "/ " + copyToServer02Folder;
    std::cout << copytoweb << std::endl;
    gROOT->ProcessLine(copytoweb);
  
  }
}

void PlotCanvas(TString var){
  
  TCanvas* c = (TCanvas*)inputFile->Get(var);
  c->Draw();
//   c->cd();
//   //TVirtualPad* gg = c->GetSelectedPad();
//   //TPad* gg = (TPad*)c->GetSelectedPad();
//   TPad* gg = (TPad*)c->GetPadPointer();
//   std::cout << "gg=" << gg << std::endl;
//   //gg = c->GetSelectedPad();
//   gg->SetLogy(0);
  c->SaveAs(outdir+"/"+var+".gif");
  c->SaveAs(outdir+"/"+var+".eps");
  c->SaveAs(outdir+"/"+var+".pdf");
//   gg->SetLogy(1);
//   c->SaveAs(outdir+"/"+var+"_log.gif");
//   c->SaveAs(outdir+"/"+var+"_log.eps");
//   c->SaveAs(outdir+"/"+var+"_log.pdf");
  c->Close();
  //delete gg;
  //delete c;
}
