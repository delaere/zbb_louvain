#include <iostream>
#include <cmath>
#include <cstdlib>
#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
#include <string>
#include "UserCode/zbb_louvain/interface/btagPerfPOGformulas_nofit.h"
#include "UserCode/zbb_louvain/interface/SFlightFuncs_EPS2013.h"

// uncertainties in Pt bins 
// according POG reccom., computed for pt 20-800, for pt > 800 GeV: use the SFb value at 800 GeV with twice the quoted uncertainty (go to 1000 GeV for light)
// according to POG, for pt < 20 GeV: use the SFb value at 20 GeV with twice the quoted uncertainty 
// https://hypernews.cern.ch/HyperNews/CMS/get/btag/1153.html
// Also since we don't have the information in our MC for pt below 20, the same approach is followed for those cases using our MC (Nadjieh)

float btagPerfPOGFormulas_nofit::SFb_error_CSVL[] = {
  0.033299,
  0.0146768,
  0.013803,
  0.0170145,
  0.0166976,
  0.0137879,
  0.0149072,
  0.0153068,
  0.0133077,
  0.0123737,
  0.0157152,
  0.0175161,
  0.0209241,
  0.0278605,
  0.0346928,
  0.0350099
};

float btagPerfPOGFormulas_nofit::SFb_error_CSVM[] = {
  0.0415707,
  0.0204209,
  0.0223227,
  0.0206655,
  0.0199325,
  0.0174121,
  0.0202332,
  0.0182446,
  0.0159777,
  0.0218531,
  0.0204688,
  0.0265191,
  0.0313175,
  0.0415417,
  0.0740446,
  0.0596716
};

float btagPerfPOGFormulas_nofit::SFb_error_CSVT[] = {
  0.0515703,
  0.0264008,
  0.0272757,
  0.0275565,
  0.0248745,
  0.0218456,
  0.0253845,
  0.0239588,
  0.0271791,
  0.0273912,
  0.0379822,
  0.0411624,
  0.0786307,
  0.0866832,
  0.0942053,
  0.102403
};


btagPerfPOGFormulas_nofit::btagPerfPOGFormulas_nofit(const char* inputfile) {
  // just a sigmoid. Used to parametrize the efficiencies
  std::cout<<"I'm using the hardcoded CSV b-tag SFs"<<std::endl;
  esdata_ = TFile::Open(inputfile);
  h_eff_csvl_b_brl_ = (TH1F*)esdata_->Get( "CSVL/h_eff_bTagOverGoodJet_ptb_Barrel"  );
  h_eff_csvl_b_fwd_ = (TH1F*)esdata_->Get( "CSVL/h_eff_bTagOverGoodJet_ptb_Endcaps" );
  h_eff_csvl_c_brl_ = (TH1F*)esdata_->Get( "CSVL/h_eff_bTagOverGoodJet_ptc_Barrel"  );
  h_eff_csvl_c_fwd_ = (TH1F*)esdata_->Get( "CSVL/h_eff_bTagOverGoodJet_ptc_Endcaps" );
  h_eff_csvl_l_brl_ = (TH1F*)esdata_->Get( "CSVL/h_eff_bTagOverGoodJet_ptl_Barrel"  );
  h_eff_csvl_l_fwd_ = (TH1F*)esdata_->Get( "CSVL/h_eff_bTagOverGoodJet_ptl_Endcaps" );
  h_eff_csvm_b_brl_ = (TH1F*)esdata_->Get( "CSVM/h_eff_bTagOverGoodJet_ptb_Barrel"  );
  h_eff_csvm_b_fwd_ = (TH1F*)esdata_->Get( "CSVM/h_eff_bTagOverGoodJet_ptb_Endcaps" );
  h_eff_csvm_c_brl_ = (TH1F*)esdata_->Get( "CSVM/h_eff_bTagOverGoodJet_ptc_Barrel"  );
  h_eff_csvm_c_fwd_ = (TH1F*)esdata_->Get( "CSVM/h_eff_bTagOverGoodJet_ptc_Endcaps" );
  h_eff_csvm_l_brl_ = (TH1F*)esdata_->Get( "CSVM/h_eff_bTagOverGoodJet_ptl_Barrel"  );
  h_eff_csvm_l_fwd_ = (TH1F*)esdata_->Get( "CSVM/h_eff_bTagOverGoodJet_ptl_Endcaps" );
  h_eff_csvt_b_brl_ = (TH1F*)esdata_->Get( "CSVT/h_eff_bTagOverGoodJet_ptb_Barrel"  );
  h_eff_csvt_b_fwd_ = (TH1F*)esdata_->Get( "CSVT/h_eff_bTagOverGoodJet_ptb_Endcaps" );
  h_eff_csvt_c_brl_ = (TH1F*)esdata_->Get( "CSVT/h_eff_bTagOverGoodJet_ptc_Barrel"  );
  h_eff_csvt_c_fwd_ = (TH1F*)esdata_->Get( "CSVT/h_eff_bTagOverGoodJet_ptc_Endcaps" );
  h_eff_csvt_l_brl_ = (TH1F*)esdata_->Get( "CSVT/h_eff_bTagOverGoodJet_ptl_Barrel"  );
  h_eff_csvt_l_fwd_ = (TH1F*)esdata_->Get( "CSVT/h_eff_bTagOverGoodJet_ptl_Endcaps" );

  GetSFlmeanCSVL00 = GetSFlmean("CSV", "L", 0.0, 0.5, "ABCD");  
  GetSFlminCSVL00  = GetSFlmin("CSV", "L", 0.0, 0.5, "ABCD");
  GetSFlmaxCSVL00 = GetSFlmax("CSV", "L", 0.0, 0.5, "ABCD");

  GetSFlmeanCSVL05 = GetSFlmean("CSV", "L", 0.5, 1.0, "ABCD");
  GetSFlminCSVL05 = GetSFlmin("CSV", "L", 0.5, 1.0, "ABCD");
  GetSFlmaxCSVL05 = GetSFlmax("CSV", "L", 0.5, 1.0, "ABCD");

  GetSFlmeanCSVL10 = GetSFlmean("CSV", "L", 1.0, 1.5, "ABCD");
  GetSFlminCSVL10 = GetSFlmin("CSV", "L", 1.0, 1.5, "ABCD");
  GetSFlmaxCSVL10 = GetSFlmax("CSV", "L", 1.0, 1.5, "ABCD");

  GetSFlmeanCSVL15 = GetSFlmean("CSV", "L", 1.5, 2.4, "ABCD");
  GetSFlminCSVL15 = GetSFlmin("CSV", "L", 1.5, 2.4, "ABCD");
  GetSFlmaxCSVL15 = GetSFlmax("CSV", "L", 1.5, 2.4, "ABCD");

  GetSFlmeanCSVM00 = GetSFlmean("CSV", "M", 0.0, 0.8, "ABCD");
  GetSFlminCSVM00 = GetSFlmin("CSV", "M", 0.0, 0.8, "ABCD");
  GetSFlmaxCSVM00 = GetSFlmax("CSV", "M", 0.0, 0.8, "ABCD");

  GetSFlmeanCSVM08 = GetSFlmean("CSV", "M", 0.8, 1.6, "ABCD");
  GetSFlminCSVM08 = GetSFlmin("CSV", "M", 0.8, 1.6, "ABCD");
  GetSFlmaxCSVM08 = GetSFlmax("CSV", "M", 0.8, 1.6, "ABCD");

  GetSFlmeanCSVM16 = GetSFlmean("CSV", "M", 1.6, 2.4, "ABCD");
  GetSFlminCSVM16 = GetSFlmin("CSV", "M", 1.6, 2.4, "ABCD");
  GetSFlmaxCSVM16 = GetSFlmax("CSV", "M", 1.6, 2.4, "ABCD");

  GetSFlmeanCSVT00 = GetSFlmean("CSV", "T", 0.0, 2.4, "ABCD");
  GetSFlminCSVT00 = GetSFlmin("CSV", "T", 0.0, 2.4, "ABCD");
  GetSFlmaxCSVT00 = GetSFlmax("CSV", "T", 0.0, 2.4, "ABCD");
}

btagPerfPOGFormulas_nofit::~btagPerfPOGFormulas_nofit() {

  delete GetSFlmeanCSVL00; delete GetSFlminCSVL00; delete GetSFlmaxCSVL00;
  delete GetSFlmeanCSVL05; delete GetSFlminCSVL05; delete GetSFlmaxCSVL05;
  delete GetSFlmeanCSVL10; delete GetSFlminCSVL10; delete GetSFlmaxCSVL10;
  delete GetSFlmeanCSVL15; delete GetSFlminCSVL15; delete GetSFlmaxCSVL15;

  delete GetSFlmeanCSVM00; delete GetSFlminCSVM00; delete GetSFlmaxCSVM00;
  delete GetSFlmeanCSVM08; delete GetSFlminCSVM08; delete GetSFlmaxCSVM08;
  delete GetSFlmeanCSVM16; delete GetSFlminCSVM16; delete GetSFlmaxCSVM16;

  delete GetSFlmeanCSVT00; delete GetSFlminCSVT00; delete GetSFlmaxCSVT00;

}

btagPerfBase::value btagPerfPOGFormulas_nofit::getbEffScaleFactor(int flavor, int algo, double pt, double eta) const {
  // values for Moriond 2013, see: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagPOG#Recommendation_for_b_c_tagging_a
  int index=999;
  float ptmin[] = {20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600};
  float ptmax[] = {30, 40, 50, 60, 70, 80,100, 120, 160, 210, 260, 320, 400, 500, 600, 800};

  //to handle low pt jets and keep their information
  double ptstore = pt;

  if(pt>800) pt=800;  

  if(pt<20) pt=20;

  // determine the index
  for(int ind = 0; ind < 16 ; ind++) {
    if(pt>ptmin[ind] && pt<ptmax[ind]) {
      index=ind;
    }
  }
  pt = ptstore;
  // prescription for the first bin: use the upper bound.
  //if(index==0) pt = ptmax[0];
  
  // compute the scale factor and its uncertainty
  double SFb = 1.0;
  double SFb_unc = 1.0;
  switch(abs(flavor)) {
    case 5: {
     // b-jets
     int ERR = 1;
     if(pt>800) {pt=800; ERR=2;}
     if(pt<20.) {pt=20.; ERR=2;}
     //Tagger: CSVL within 20 < pt GeV, abs(eta) < 2.4, x = pt
     if(algo==1) {
       SFb = 0.997942*((1.+(0.00923753*pt))/(1.+(0.0096119*pt)));   
       SFb_unc = ERR*SFb_error_CSVL[index];
     } else if(algo==2) {
       // Tagger: CSVM within 20 < pt GeV, abs(eta) < 2.4, x = pt
       SFb = (0.938887+(0.00017124*pt))+(-2.76366e-07*(pt*pt));
       SFb_unc = ERR*SFb_error_CSVM[index];
     } else if(algo==3) {
       // Tagger: CSVT within 20 < pt GeV, abs(eta) < 2.4, x = pt
       SFb = (0.927563+(1.55479e-05*pt))+(-1.90666e-07*(pt*pt));
       SFb_unc = ERR*SFb_error_CSVT[index];
     }

     break;
   }
   case 4: {
     // c-jets // assumes the same SF as for b-jets: THE SAME as for the b (but twice the uncertainty)   
     int ERR = 1;
     if(pt>800) {pt=800; ERR=2;}
     if(pt<20) {pt=20; ERR=2;}
     //Tagger: CSVL within 20 < pt GeV, abs(eta) < 2.4, x = pt
     if(algo==1) {
       SFb = 0.997942*((1.+(0.00923753*pt))/(1.+(0.0096119*pt)));   
       SFb_unc = ERR*SFb_error_CSVL[index]*2;
     } else if(algo==2) {
       // Tagger: CSVM within 20 < pt GeV, abs(eta) < 2.4, x = pt
       SFb = (0.938887+(0.00017124*pt))+(-2.76366e-07*(pt*pt));
       SFb_unc = ERR*SFb_error_CSVM[index]*2;
     } else if(algo==3) {
       // Tagger: CSVT within 20 < pt GeV, abs(eta) < 2.4, x = pt
       SFb = (0.927563+(1.55479e-05*pt))+(-1.90666e-07*(pt*pt));
       SFb_unc = ERR*SFb_error_CSVT[index]*2;
     }
     break;
   }
   default: {
     // udsg-jets + untags (assumes these are light jets), recommandation give SFb, SFb+ and SFb- for 2012 ABCD combined, for SFb_unc we take (SFb+ -SFb-)/2
     int ERR = 1;
     if(pt>850 && fabs(eta)>1.5 && algo == 1) {pt=850; ERR=2;}
     else if(pt>850 && fabs(eta)>1.6 && algo == 2) {pt=850; ERR=2;}
     else if(pt>1000) {pt=1000; ERR=2;}
     else if(pt<20) {pt=20.; ERR = 2;}
     if( algo == 1 && fabs(eta)>0.0 &&  fabs(eta)<= 0.5) {
       //   Tagger: CSVL within 20 < pt GeV, abs(eta) < 0.5, x = pt
       SFb = GetSFlmeanCSVL00->Eval(pt);
       SFb_unc = ERR*(GetSFlmaxCSVL00->Eval(pt)-GetSFlminCSVL00->Eval(pt))/2;
     } else if ( algo == 1 && fabs(eta)>0.5 &&  fabs(eta)<= 1.0) {
       //   Tagger: CSVL within 20 < pt GeV, 0.5 < abs(eta) < 1.0, x = pt
       SFb = GetSFlmeanCSVL05->Eval(pt);
       SFb_unc = ERR*(GetSFlmaxCSVL05->Eval(pt)-GetSFlminCSVL05->Eval(pt))/2;
     } else if ( algo == 1 && fabs(eta)>1.0 &&  fabs(eta)<= 1.5) {
       //   Tagger: CSVL within 20 < pt GeV, 1.0 < abs(eta) < 1.5, x = pt
       SFb = GetSFlmeanCSVL10->Eval(pt);
       SFb_unc = ERR*(GetSFlmaxCSVL10->Eval(pt)-GetSFlminCSVL10->Eval(pt))/2;
     } else if ( algo == 1 && fabs(eta)>1.5) {
       //   Tagger: CSVL within 20 < pt GeV, 1.5 < abs(eta) < 2.4, x = pt
       SFb = GetSFlmeanCSVL15->Eval(pt);
       SFb_unc = ERR*(GetSFlmaxCSVL15->Eval(pt)-GetSFlminCSVL15->Eval(pt))/2;
     } else if ( algo == 2 && fabs(eta)>0.0 &&  fabs(eta)<= 0.8) {
       //   Tagger: CSVM within 20 < pt GeV, 0.0 < abs(eta) < 0.8, x = pt
       SFb = GetSFlmeanCSVM00->Eval(pt);
       SFb_unc = ERR*(GetSFlmaxCSVM00->Eval(pt)-GetSFlminCSVM00->Eval(pt))/2;
     } else if ( algo == 2 && fabs(eta)>0.8 &&  fabs(eta)<= 1.6) {
       //   Tagger: CSVM within 20 < pt GeV, 0.8 < abs(eta) < 1.6, x = pt
       SFb = GetSFlmeanCSVM08->Eval(pt);
       SFb_unc = ERR*(GetSFlmaxCSVM08->Eval(pt)-GetSFlminCSVM08->Eval(pt))/2;
     } else if ( algo == 2 && fabs(eta)>1.6) {
       //   Tagger: CSVM within 20 < pt GeV, 1.6 < abs(eta) < 2.4, x = pt
       SFb = GetSFlmeanCSVM16->Eval(pt);
       SFb_unc = ERR*(GetSFlmaxCSVM16->Eval(pt)-GetSFlminCSVM16->Eval(pt))/2;
     } else if ( algo == 3 ) {
       //   Tagger: CSVT within 20 < pt GeV, 0.0 < abs(eta) < 2.4, x = pt
       SFb = GetSFlmeanCSVT00->Eval(pt);
       SFb_unc = ERR*(GetSFlmaxCSVT00->Eval(pt)-GetSFlminCSVT00->Eval(pt))/2;
     }
   }
  }
  if(SFb_unc<0) {/*std::cout<<"Warning : SFb_unc is negative = "<<SFb_unc<<" the absolute value will be taken"<<std::endl;*/ SFb_unc=fabs(SFb_unc);}
  return std::make_pair(SFb, SFb_unc);
}  

btagPerfBase::value btagPerfPOGFormulas_nofit::getbEfficiency(int flavor, int algo, double pt, double eta) const {
  // small protection against large et (shere we have no measurement).
  // the subject is a bit delicate, but I think it is better to use
  // the efficiency for the last bin than to set it to 0.
  if(pt>=1000) pt=999;
  switch(abs(flavor)) {
  case 5: {
    
    if(pt>800) pt=800;
    if(pt<20) pt=20;
    // this is not in the db and must be parametrized from OUR mc
    if(fabs(eta)<1.2 && algo==1)
      return std::make_pair(h_eff_csvl_b_brl_->GetBinContent(h_eff_csvl_b_brl_->FindBin(pt)),
			    h_eff_csvl_b_brl_->GetBinError(h_eff_csvl_b_brl_->FindBin(pt)));
    else if(fabs(eta)>1.2 && algo==1)
      return std::make_pair(h_eff_csvl_b_fwd_->GetBinContent(h_eff_csvl_b_fwd_->FindBin(pt)),
			    h_eff_csvl_b_fwd_->GetBinError(h_eff_csvl_b_fwd_->FindBin(pt)));
    else if(fabs(eta)<1.2 && algo==2)
      return std::make_pair(h_eff_csvm_b_brl_->GetBinContent(h_eff_csvm_b_brl_->FindBin(pt)),
			    h_eff_csvm_b_brl_->GetBinError(h_eff_csvm_b_brl_->FindBin(pt)));
    else if(fabs(eta)>1.2 && algo==2)
      return std::make_pair(h_eff_csvm_b_fwd_->GetBinContent(h_eff_csvm_b_fwd_->FindBin(pt)),
			    h_eff_csvm_b_fwd_->GetBinError(h_eff_csvm_b_fwd_->FindBin(pt)));
    else if(fabs(eta)<1.2 && algo==3)
      return std::make_pair(h_eff_csvt_b_brl_->GetBinContent(h_eff_csvt_b_brl_->FindBin(pt)),
			    h_eff_csvt_b_brl_->GetBinError(h_eff_csvt_b_brl_->FindBin(pt)));
    else if(fabs(eta)>1.2 && algo==3)
      return std::make_pair(h_eff_csvt_b_fwd_->GetBinContent(h_eff_csvt_b_fwd_->FindBin(pt)),
			    h_eff_csvt_b_fwd_->GetBinError(h_eff_csvt_b_fwd_->FindBin(pt)));
    else
      return std::make_pair(0.,0.);
  }
  case 4: {
    if(pt>800) pt=800;
    if(pt<20) pt=20;
    // this is not in the db and must be parametrized from OUR mc
    if(fabs(eta)<1.2 && algo==1)
      return std::make_pair(h_eff_csvl_c_brl_->GetBinContent(h_eff_csvl_c_brl_->FindBin(pt)),
			    h_eff_csvl_c_brl_->GetBinError(h_eff_csvl_c_brl_->FindBin(pt)));
    else if(fabs(eta)>1.2 && algo==1)
      return std::make_pair(h_eff_csvl_c_fwd_->GetBinContent(h_eff_csvl_c_fwd_->FindBin(pt)),
			    h_eff_csvl_c_fwd_->GetBinError(h_eff_csvl_c_fwd_->FindBin(pt)));
    else if(fabs(eta)<1.2 && algo==2)
      return std::make_pair(h_eff_csvm_c_brl_->GetBinContent(h_eff_csvm_c_brl_->FindBin(pt)),
			    h_eff_csvm_c_brl_->GetBinError(h_eff_csvm_c_brl_->FindBin(pt)));
    else if(fabs(eta)>1.2 && algo==2)
      return std::make_pair(h_eff_csvm_c_fwd_->GetBinContent(h_eff_csvm_c_fwd_->FindBin(pt)),
			    h_eff_csvm_c_fwd_->GetBinError(h_eff_csvm_c_fwd_->FindBin(pt)));
    else if(fabs(eta)<1.2 && algo==3)
      return std::make_pair(h_eff_csvt_c_brl_->GetBinContent(h_eff_csvt_c_brl_->FindBin(pt)),
			    h_eff_csvt_c_brl_->GetBinError(h_eff_csvt_c_brl_->FindBin(pt)));
    else if(fabs(eta)>1.2 && algo==3)
      return std::make_pair(h_eff_csvt_c_fwd_->GetBinContent(h_eff_csvt_c_fwd_->FindBin(pt)),
			    h_eff_csvt_c_fwd_->GetBinError(h_eff_csvt_c_fwd_->FindBin(pt)));
    else
      return std::make_pair(0.,0.);
  }
  default: {
    // this better parametrized from OUR mc
    if(pt>850 && fabs(eta)>1.5 && algo == 1) pt=850;
    else if(pt>850 && fabs(eta)>1.6 && algo == 2) pt=850;
    if(pt<20) pt=20.; 
    if(fabs(eta)<1.2 && algo==1)
      return std::make_pair(h_eff_csvl_l_brl_->GetBinContent(h_eff_csvl_l_brl_->FindBin(pt)),
			    h_eff_csvl_l_brl_->GetBinError(h_eff_csvl_l_brl_->FindBin(pt)));
    else if(fabs(eta)>1.2 && algo==1)
      return std::make_pair(h_eff_csvl_l_fwd_->GetBinContent(h_eff_csvl_l_fwd_->FindBin(pt)),
			    h_eff_csvl_l_fwd_->GetBinError(h_eff_csvl_l_fwd_->FindBin(pt)));
    else if(fabs(eta)<1.2 && algo==2)
      return std::make_pair(h_eff_csvm_l_brl_->GetBinContent(h_eff_csvm_l_brl_->FindBin(pt)),
                            h_eff_csvm_l_brl_->GetBinError(h_eff_csvm_l_brl_->FindBin(pt)));
    else if(fabs(eta)>1.2 && algo==2)
      return std::make_pair(h_eff_csvm_l_fwd_->GetBinContent(h_eff_csvm_l_fwd_->FindBin(pt)),
			    h_eff_csvm_l_fwd_->GetBinError(h_eff_csvm_l_fwd_->FindBin(pt)));
    else if(fabs(eta)<1.2 && algo==3)
      return std::make_pair(h_eff_csvt_l_brl_->GetBinContent(h_eff_csvt_l_brl_->FindBin(pt)),
                            h_eff_csvt_l_brl_->GetBinError(h_eff_csvt_l_brl_->FindBin(pt)));
    else if(fabs(eta)>1.2 && algo==3)
      return std::make_pair(h_eff_csvt_l_fwd_->GetBinContent(h_eff_csvt_l_fwd_->FindBin(pt)),
			    h_eff_csvt_l_fwd_->GetBinError(h_eff_csvt_l_fwd_->FindBin(pt)));
    else
      return std::make_pair(0.,0.);
  }
  }
}

