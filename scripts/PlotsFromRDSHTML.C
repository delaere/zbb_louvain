// Usage
// root -b -q PlotsFromRDSHTML.C+
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

//***********************************************
//Inputs is(are) the rootfile(s) from getCP_ME.py that contains the canvases for the different validation plots
//The outpus is a local folder where plots for each canvas will be created in a web format
//If 2 instead of 1 rootfile are provided the plots corresponding to the same variable will be plotted side by side for the 2 rootfiles
//If a location is specified in a remote server in the variable copyToServer02Folder, the output folder will be transferred there
//*************************************************


TString outdir = "PlotsFromRDS_re7/";
TString InputFile = "/home/fynu/arnaudp/scratch/Zbb_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Plot_mm_100H125_ptZrew_MM_N_allR.root";
//if second inputfile not empty then show the plots for the same var side by side for the 2 different rootfiles
TString InputFile2 = "";
TString copyToServer02Folder = "$USER@server02.fynu.ucl.ac.be:~/public_html/private/PlotsFromRDS_re7";//if empty do nothing
TString Suffix1 = "";//label to add to the plots for InputFile and InputFile2
TString Suffix2 = "";//  example Suffix1="_EE"; Suffix2 = "_MM", if empty _1 and _2 will be used

//******************No need to change anything below typically***************
ofstream outfile;
bool TwoFiles = false;


TFile *inputFile = 0;
TFile *inputFile2 = 0;

void printheader() {

  outfile << "<h3> Control plots from RDS (getCP_ME) </h3><br><br>" << endl;
  outfile << "<table border=\"1\" cellpadding=\"5\" cellspacing=\"5\" width=\"100%\">" << endl;
  outfile << "<tr>" << endl;
  outfile << "<td width=\"50%\">" << "Stack plots"+Suffix1+"" << "</td>" <<endl;
  outfile << "<td width=\"50%\">" << "Stack plots"+Suffix2+"" << "</td>" <<endl;
  outfile << "</tr>" << endl;
  outfile << "</center>" << endl;
}

void printtail() {
  outfile << "</table><br><br><br>" << endl;

}


void print(TString var) {

  TString var1 = var+Suffix1;
  TString var2 = var+Suffix2;
  outfile << "<tr>" << endl;

  outfile << "<td width=\"50%\">" << endl;
  outfile << "<br><IMG SRC=\""+var1+".gif"+"\" ><br>" << endl;
  outfile << "<center>" << endl;
  outfile << " <a href=\""+var1+".gif"+"\">gif</a>  <a href=\""+var1+".eps"+"\">eps</a>  <a href=\""+var1+".pdf"+"\">pdf</a>"+var1 +"</td>" << endl; 

  if (TwoFiles) {
  outfile << "<td width=\"50%\">" << endl;
  outfile << "<br><IMG SRC=\""+var2+".gif"+"\" ><br>" << endl;
  outfile << "<center>" << endl;
  outfile << " <a href=\""+var2+".gif"+"\">gif</a>  <a href=\""+var2+".eps"+"\">eps</a>  <a href=\""+var2+".pdf"+"\">pdf</a>"+var2 +"</td>" << endl; 
  
  }

  outfile << "</tr>" << endl;
  outfile << "</center>" << endl;

}


void PlotCanvas(TString var, TFile*, TString);
void PlotsFromRDSHTML();

void PlotsFromRDSHTML() {

  if (InputFile2 != "") TwoFiles = true;
  
  if (TwoFiles) {
    if (Suffix1 == "" && Suffix2 == "") {
      Suffix1 = "_1";
      Suffix2 = "_2";
    }
    if (Suffix1 == Suffix2) Suffix1 += "_";
  }
  else Suffix2 = "";



  TString makedir = ".! mkdir " + outdir;
  gROOT->ProcessLine(makedir);

  inputFile = TFile::Open(InputFile);
  if (TwoFiles) inputFile2 = TFile::Open(InputFile2);

  outfile.open(outdir+"/index.html");

  printheader();
 
  TList* listOfKeys = gDirectory->GetListOfKeys();
  TIter next(listOfKeys);
  TKey *key;
  while (key = (TKey*) next()) {
    TObject *obj = key->ReadObj(); //<-- Segmentation fault if listOfKeys is a clone.
    if (TString(obj->ClassName()).Contains("Canvas")) {
      if (TString(obj->GetName()).Contains("CANVASmlphiggsvsbkg")) continue;//do not plot final MLP's until we have blinding procedure
      
      std::cout << obj->GetName() << std::endl;
      PlotCanvas(obj->GetName(), inputFile, Suffix1);
      if (TwoFiles) PlotCanvas(obj->GetName(), inputFile2, Suffix2);
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

void PlotCanvas(TString var, TFile* f, TString suffix){
  
  TCanvas* c = (TCanvas*)f->Get(var);
  if (c != 0) {
    c->Draw();
    c->SaveAs(outdir+"/"+var+suffix+".gif");
    c->SaveAs(outdir+"/"+var+suffix+".eps");
    c->SaveAs(outdir+"/"+var+suffix+".pdf");
    c->Close();
  }
  else cout << "Not found canvas: " << var << " for file " << f->GetName() << std::endl;
}
