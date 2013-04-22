//macro to make a Zbb reweighting. It producesdata - substracted MC (except Zbb) / MC
//  the numerator and denominator of the reweighiting histogram are also stored
//It doesn't reweight for the overall normalization
//Uses as input the THYields.root from getCP_ME_rds_CSV.py
//  doMuChannel and doElChannel switches to produce reweighting histogram for those channels
//  fileMu and fileEl point to the corresponding THYields.root files
//  the output is stored in ZbbReweightHistos.root
//  by default the reweighting is produced only for PTZ
//  Usage: root -l -q ZbbReweight_FromTHYields.C


bool doMuChannel = true;//reweighiting histogram based only on muon channel
bool doElChannel = true;//reweighiting histogram based only on electron channel
bool doBothChannel = true;//reweighiting histogram based on both the muon and electron channel
//TString fileMu = "/home/fynu/arnaudp/scratch/Zbb_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/THYields_2jets.root";
//TString fileEl = "/home/fynu/arnaudp/scratch/Zbb_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/THYields_2eejets.root";
//TString fileMu = "/home/fynu/arnaudp/scratch/Zbb_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/THYields_3jets.root";
//TString fileEl = "/home/fynu/arnaudp/scratch/Zbb_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/THYields_3eejets.root";
TString fileMu = "/home/fynu/arnaudp/scratch/Zbb_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/THYields_mm_2jets.root";
TString fileEl = "/home/fynu/arnaudp/scratch/Zbb_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/THYields_ee_2jets.root";
//TString fileMu = "/home/fynu/arnaudp/scratch/Zbb_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/THYields_mm_M2jets.root";
//TString fileEl = "/home/fynu/arnaudp/scratch/Zbb_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/THYields_ee_M2jets.root";

//*************************************************
//*************************************************
//*************************************************
//Normally no need to change any beyond this point
//*************************************************
//*************************************************
//*************************************************

TFile* fout = 0;


TFile* fMu = 0;
TFile* fEl = 0;

//Normalization factor, normally not needed
double Norm_Zb  =  1.0;
double Norm_Zc  =  1.0;
double Norm_Zl  =  1.0;
double Norm_TT  =  1.0;
double Norm_ZZ  =  1.0;

double MEnorm_TT_Mu = 1.0;

//Inputs are TH1s.root files produced by getYields

// BE CAREFUL ABOUT EXTRA MATRIX ELEMENT NORM FACTOR DUE TO NON-PROCESSED EVENTS
//Outputs are histograms to reweight on a certain variable
//The reweighting histogram is:
// (HISTOdata - SUM(HistoBkgs))/HISTOzbb, where Bkgs are all considered
// backgrounds, mainly ttbar and ZZ; Zc and Zl are also treated as background
// This is to assume that we reweight to correct for mismodeling of Zbb
// If the reweighting is done to correct for other effect the recipee should be
//changed
void ZbbReweight_FromTHYields() {

  fout = TFile::Open("ZbbReweightHistos.root", "recreate");
 
  if (doMuChannel) {
    fMu = TFile::Open(fileMu);
  }
  
  if (doElChannel) {
    fEl = TFile::Open(fileEl);
  }
  

  //ZbbReweightVar("eventSelectiondijetdR");
  
  if (doMuChannel) ZbbReweightVarChannel("eventSelectionbestzptMu", "Mu");
  if (doElChannel) ZbbReweightVarChannel("eventSelectionbestzptEle", "El");
  if (doBothChannel) ZbbReweightVarChannel("eventSelectionbestzpt", "Both", "Ele", "Mu");

  

}


void ZbbReweightVarChannel(TString varname, TString channel, TString varSuffixEle = "", TString varSuffixMu = "") {
  TH1F* h_TT = 0;
  TH1F* h_Zb = 0;
  TH1F* h_Zc = 0;
  TH1F* h_Zl = 0;
  TH1F* h_ZZ = 0;
  TH1F* h_DATA = 0;  

  if (channel == "Mu") {
    h_TT = (TH1F*)fMu->Get("th_"+varname+"_TT");
    h_Zb = (TH1F*)fMu->Get("th_"+varname+"_Zb");
    h_Zc = (TH1F*)fMu->Get("th_"+varname+"_Zc");
    h_Zl = (TH1F*)fMu->Get("th_"+varname+"_Zl");
    h_ZZ = (TH1F*)fMu->Get("th_"+varname+"_ZZ");
    h_DATA = (TH1F*)fMu->Get("th_"+varname+"_DATA");
  }
  else if (channel == "El"){
    h_TT = (TH1F*)fEl->Get("th_"+varname+"_TT");
    h_Zb = (TH1F*)fEl->Get("th_"+varname+"_Zb");
    h_Zc = (TH1F*)fEl->Get("th_"+varname+"_Zc");
    h_Zl = (TH1F*)fEl->Get("th_"+varname+"_Zl");
    h_ZZ = (TH1F*)fEl->Get("th_"+varname+"_ZZ");
    h_DATA = (TH1F*)fEl->Get("th_"+varname+"_DATA");
  }
  else if (channel == "Both") {
    h_TT = (TH1F*)fEl->Get("th_"+varname+varSuffixEle+"_TT");
    h_Zb = (TH1F*)fEl->Get("th_"+varname+varSuffixEle+"_Zb");
    h_Zc = (TH1F*)fEl->Get("th_"+varname+varSuffixEle+"_Zc");
    h_Zl = (TH1F*)fEl->Get("th_"+varname+varSuffixEle+"_Zl");
    h_ZZ = (TH1F*)fEl->Get("th_"+varname+varSuffixEle+"_ZZ");
    h_DATA = (TH1F*)fEl->Get("th_"+varname+varSuffixEle+"_DATA");
  
    h_TT->Add((TH1F*)fMu->Get("th_"+varname+varSuffixMu+"_TT"));
    h_Zb->Add((TH1F*)fMu->Get("th_"+varname+varSuffixMu+"_Zb"));
    h_Zc->Add((TH1F*)fMu->Get("th_"+varname+varSuffixMu+"_Zc"));
    h_Zl->Add((TH1F*)fMu->Get("th_"+varname+varSuffixMu+"_Zl"));
    h_ZZ->Add((TH1F*)fMu->Get("th_"+varname+varSuffixMu+"_ZZ"));
    h_DATA->Add((TH1F*)fMu->Get("th_"+varname+varSuffixMu+"_DATA"));
  
  }
  else return;

// Not necessary since Sumw2 is already done for the .root files in THYields.root
//   h_TT->Sumw2();
//   h_Zb->Sumw2();
//   h_Zc->Sumw2();
//   h_Zl->Sumw2();
//   h_ZZ->Sumw2();
//   h_DATA->Sumw2();
      
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
  


  std::cout << "Before Rescaling" << std::endl;
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



  std::cout << "After rescaling MC samples to match data yields" << std::endl;
  std::cout << varname << " " << channel << std::endl;
  std::cout << "  h_TT->Integral() = " << h_TT->Integral() << std::endl;
  std::cout << "  h_Zb->Integral() = " << h_Zb->Integral() << std::endl;
  std::cout << "  h_Zc->Integral() = " << h_Zc->Integral() << std::endl;
  std::cout << "  h_Zl->Integral() = " << h_Zl->Integral() << std::endl;
  std::cout << "  h_ZZ->Integral() = " << h_ZZ->Integral() << std::endl;
  std::cout << "  h_DATA->Integral() = " << h_DATA->Integral() << std::endl << std::endl;
  
  //Notice that before we used to substract also the Zbx contribution
  // h_DATAminusBkg->Add(h_Zc, -1.) and h_den = h_Zb
  TH1F* h_DATAminusBkg = (TH1F*)h_DATA->Clone();
  h_DATAminusBkg->Add(h_TT, -1.);
  h_DATAminusBkg->Add(h_Zl, -1.);
  h_DATAminusBkg->Add(h_ZZ, -1.);
  TH1F* h_den = (TH1F*)h_Zb->Clone();
  h_den->Add(h_Zc);
  
  TH1F* h_Reweight = (TH1F*)h_DATAminusBkg->Clone();

  fout->cd();

  
  h_Reweight->Write(varname+"_NUM_"+channel);
  h_den->Write(varname+"_DEN_"+channel);

  
  h_Reweight->Divide(h_den);
  
   h_Reweight->Write(varname+"_"+channel);


  delete h_TT;
  delete h_Zb;
  delete h_Zc;
  delete h_Zl;
  delete h_ZZ;
  delete h_DATA;
  delete h_DATAminusBkg;
  delete h_den;
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
