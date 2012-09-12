TFile* fout = 0;

bool doMuChannel = true;
bool doElChannel = true;


TFile* fMu_TT = 0;
TFile* fMu_Zb = 0;
TFile* fMu_Zc = 0;
TFile* fMu_Zl = 0;
TFile* fMu_ZZ = 0;
TFile* fMu_DATA = 0;

TFile* fEl_TT = 0;
TFile* fEl_Zb = 0;
TFile* fEl_Zc = 0;
TFile* fEl_Zl = 0;
TFile* fEl_ZZ = 0;
TFile* fEl_DATA = 0;

//Normalization factor (Lumi*CrossSection/nMCentries)
double Norm_Zb  =  0.437896835114;
double Norm_Zc  =  0.437896835114;
double Norm_Zl  =  0.437896835114;
double Norm_TT  =  0.0138507491245;
double Norm_ZZ  =  0.00771484438845;

double MEnorm_TT_Mu = 42407./10000.;

//Inputs are TH1s.root files produced by getYields
// For the moment those histograms are normalized to the number of events
// after applying the reweightings (lepton, b-tag, pile-up), but do not
// include de Lumi*CrossSection/nMCentries
// for this reason this extra normalization is done by hand
// BE CAREFUL ABOUT EXTRA MATRIX ELEMENT NORM FACTOR DUE TO NON-PROCESSED EVENTS
//Outputs are histograms to reweight on a certain variable
//The reweighting histogram is:
// (HISTOdata - SUM(HistoBkgs))/HISTOzbb, where Bkgs are all considered
// backgrounds, mainly ttbar and ZZ; Zc and Zl are also treated as background
// This is to assume that we reweight to correct for mismodeling of Zbb
// If the reweighting is done to correct for other effect the recipee should be
//changed
void ZbbReweight() {

  fout = TFile::Open("ZbbReweightHistos.root", "recreate");
  TString dirMu = "~/CMSSW44btag_120711/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Muon_Plot_from_GY/";
  TString dirEl = "~/CMSSW44btag_120711/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/El_Plot_from_GY/";
  
  if (doMuChannel) {
    fMu_TT = TFile::Open(dirMu + "TH1sTT.root");
    fMu_Zb = TFile::Open(dirMu + "TH1sZb.root");
    fMu_Zc = TFile::Open(dirMu + "TH1sZc.root");
    fMu_Zl = TFile::Open(dirMu + "TH1sZl.root");
    fMu_ZZ = TFile::Open(dirMu + "TH1sZZ.root");
    fMu_DATA = TFile::Open(dirMu + "TH1sDATA.root");
  }
  
  if (doElChannel) {
    fEl_TT = TFile::Open(dirEl + "TH1sTT.root");
    fEl_Zb = TFile::Open(dirEl + "TH1sZb.root");
    fEl_Zc = TFile::Open(dirEl + "TH1sZc.root");
    fEl_Zl = TFile::Open(dirEl + "TH1sZl.root");
    fEl_ZZ = TFile::Open(dirEl + "TH1sZZ.root");
    fEl_DATA = TFile::Open(dirEl + "TH1sDATA.root");
  }
  

  ZbbReweightVar("eventSelectiondijetdR");
  ZbbReweightVar("eventSelectionbestzptMu");
  ZbbReweightVar("eventSelectionbestzptEle");
  

}

void ZbbReweightVar(TString varname) {
  //Selector to decide which channels are reweighted

  if (doMuChannel) ZbbReweightVarChannel(varname, "Mu");
  if (doElChannel) ZbbReweightVarChannel(varname, "El");
}

void ZbbReweightVarChannel(TString varname, TString channel) {
  TH1F* h_TT = 0;
  TH1F* h_Zb = 0;
  TH1F* h_Zc = 0;
  TH1F* h_Zl = 0;
  TH1F* h_ZZ = 0;
  TH1F* h_DATA = 0;  

  if (channel == "Mu") {
    h_TT = (TH1F*)fMu_TT->Get(varname);
    h_Zb = (TH1F*)fMu_Zb->Get(varname);
    h_Zc = (TH1F*)fMu_Zc->Get(varname);
    h_Zl = (TH1F*)fMu_Zl->Get(varname);
    h_ZZ = (TH1F*)fMu_ZZ->Get(varname);
    h_DATA = (TH1F*)fMu_DATA->Get(varname);
  }
  else if (channel == "El"){
    h_TT = (TH1F*)fEl_TT->Get(varname);
    h_Zb = (TH1F*)fEl_Zb->Get(varname);
    h_Zc = (TH1F*)fEl_Zc->Get(varname);
    h_Zl = (TH1F*)fEl_Zl->Get(varname);
    h_ZZ = (TH1F*)fEl_ZZ->Get(varname);
    h_DATA = (TH1F*)fEl_DATA->Get(varname);  
  }
  else return;
  
  int nbins = h_DATA->GetNbinsX()+1;
  //h_DATA->Draw();
  
  std::cout << "TotalData = " << h_DATA->Integral(0, nbins+1) << std::endl;


  //Rescale MC to proper lumi:
  // the treatment of the errors doesn't really matter
  //std::cout << "Before Rescaling" << std::endl;
  //std::cout << varname << " " << channel << std::endl;
  //std::cout << "  h_TT->Integral() = " << h_TT->Integral() << std::endl;
  //std::cout << "  h_Zb->Integral() = " << h_Zb->Integral() << std::endl;
  //std::cout << "  h_Zc->Integral() = " << h_Zc->Integral() << std::endl;
  //std::cout << "  h_Zl->Integral() = " << h_Zl->Integral() << std::endl;
  //std::cout << "  h_ZZ->Integral() = " << h_ZZ->Integral() << std::endl;
  //std::cout << "  h_DATA->Integral() = " << h_DATA->Integral() << std::endl;  

  if (channel == "Mu")	{h_TT->Scale(Norm_TT*MEnorm_TT_Mu);}
  else 			{h_TT->Scale(Norm_TT);}
  h_Zb->Scale(Norm_Zb);
  h_Zc->Scale(Norm_Zc);
  h_Zl->Scale(Norm_Zl);
  h_ZZ->Scale(Norm_ZZ);
  


  std::cout << "After Rescaling" << std::endl;
  std::cout << varname << " " << channel << std::endl;
  std::cout << "  h_TT->Integral() = " << h_TT->Integral() << std::endl;
  std::cout << "  h_Zb->Integral() = " << h_Zb->Integral() << std::endl;
  std::cout << "  h_Zc->Integral() = " << h_Zc->Integral() << std::endl;
  std::cout << "  h_Zl->Integral() = " << h_Zl->Integral() << std::endl;
  std::cout << "  h_ZZ->Integral() = " << h_ZZ->Integral() << std::endl;
  std::cout << "  h_DATA->Integral() = " << h_DATA->Integral() << std::endl;
  

  //First rescale MC histograms so the total MC matches the data
  //We want the rescaling to affect only the shapes
  double TotalMC = double(h_TT->Integral(0, nbins+1))+
    double(h_Zb->Integral(0, nbins+1))+
    double(h_Zc->Integral(0, nbins+1))+
    double(h_Zl->Integral(0, nbins+1))+
    double(h_ZZ->Integral(0, nbins+1));

  NormalizeIntegralPlusUandOToX(h_TT, double(h_TT->Integral(0, nbins+1))/TotalMC*double(h_DATA->Integral(0, nbins+1)));
  NormalizeIntegralPlusUandOToX(h_Zb, double(h_Zb->Integral(0, nbins+1))/TotalMC*double(h_DATA->Integral(0, nbins+1)));
  NormalizeIntegralPlusUandOToX(h_Zc, double(h_Zc->Integral(0, nbins+1))/TotalMC*double(h_DATA->Integral(0, nbins+1)));
  NormalizeIntegralPlusUandOToX(h_Zl, double(h_Zl->Integral(0, nbins+1))/TotalMC*double(h_DATA->Integral(0, nbins+1)));
  NormalizeIntegralPlusUandOToX(h_ZZ, double(h_ZZ->Integral(0, nbins+1))/TotalMC*double(h_DATA->Integral(0, nbins+1)));



  std::cout << "After Rescaling2" << std::endl;
  std::cout << varname << " " << channel << std::endl;
  std::cout << "  h_TT->Integral() = " << h_TT->Integral() << std::endl;
  std::cout << "  h_Zb->Integral() = " << h_Zb->Integral() << std::endl;
  std::cout << "  h_Zc->Integral() = " << h_Zc->Integral() << std::endl;
  std::cout << "  h_Zl->Integral() = " << h_Zl->Integral() << std::endl;
  std::cout << "  h_ZZ->Integral() = " << h_ZZ->Integral() << std::endl;
  std::cout << "  h_DATA->Integral() = " << h_DATA->Integral() << std::endl;
  

  TH1F* h_DATAminusBkg = (TH1F*)h_DATA->Clone();
  h_DATAminusBkg->Add(h_TT, -1.);
  h_DATAminusBkg->Add(h_Zc, -1.);
  h_DATAminusBkg->Add(h_Zl, -1.);
  h_DATAminusBkg->Add(h_ZZ, -1.);
  
  TH1F* h_Reweight = (TH1F*)h_DATAminusBkg->Clone();

  fout->cd();

  
  h_Reweight->Write(varname+"_NUM_"+channel);
  h_Zb->Write(varname+"_DEN_"+channel);

  
  h_Reweight->Divide(h_Zb);
  
   h_Reweight->Write(varname+"_"+channel);


  delete h_TT;
  delete h_Zb;
  delete h_Zc;
  delete h_Zl;
  delete h_ZZ;
  delete h_DATA;
  delete h_DATAminusBkg;
  delete h_Reweight;
  
}

void NormalizeIntegralPlusUandO(TH1* h, Int_t color = 1) {
  int nbins = h->GetNbinsX() + 1;
  double integ = h->Integral(0, nbins);
  if (integ != 0) {
    Double_t sc = 1.0/integ;
    h->Scale(sc);
    h->SetLineColor(color);
  }
}

void NormalizeIntegralPlusUandOToX(TH1* h, Double_t X, Int_t color = 1) {
  int nbins = h->GetNbinsX() + 1;
  double integ = h->Integral(0, nbins);
  if (integ != 0) {
    Double_t sc = X/integ;
    h->Scale(sc);
    h->SetLineColor(color);
  }
}
