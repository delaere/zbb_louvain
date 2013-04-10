#include <iostream>
#include <cmath>
#include <cstdlib>
#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
#include <string>
#include "UserCode/zbb_louvain/interface/btagPerfPOGformulas_CSV.h"

// uncertainties in Pt bins 
// according POG reccom., computed for pt 20-800, for pt > 800 GeV: use the SFb value at 800 GeV with twice the quoted uncertainty 

float btagPerfPOGFormulas_CSV::SFb_error_CSVL[] = {
  0.0188743,
  0.0161816,
  0.0139824,
  0.0152644,
  0.0161226,
  0.0157396,
  0.0161619,
  0.0168747,
  0.0257175,
  0.026424,
  0.0264928,
  0.0315127,
  0.030734,
  0.0438259,
  2*0.0438259
};

float btagPerfPOGFormulas_CSV::SFb_error_CSVM[] = {
  0.0295675,
  0.0295095,
  0.0210867,
  0.0219349,
  0.0227033,
  0.0204062,
  0.0185857,
  0.0256242,
  0.0383341,
  0.0409675,
  0.0420284,
  0.0541299,
  0.0578761,
  0.0655432,
  2*0.0655432
};

float btagPerfPOGFormulas_CSV::SFb_error_CSVT[] = {
  0.0364717,
  0.0362281,
  0.0232876,
  0.0249618,
  0.0261482,
  0.0290466,
  0.0300033,
  0.0453252,
  0.0685143,
  0.0653621,
  0.0712586,
  0.094589,
  0.0777011,
  0.0866563,
  2*0.0866563
};


btagPerfPOGFormulas_CSV::btagPerfPOGFormulas_CSV(const char* inputfile) {
  // just a sigmoid. Used to parametrize the efficiencies
  eff_ = new TF1("sigmoidTimesL","[0]+([3]+[4]*x)/(1+exp([1]-x*[2]))",20,1000);
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
}

btagPerfPOGFormulas_CSV::~btagPerfPOGFormulas_CSV() {
  delete eff_;
}

btagPerfBase::value btagPerfPOGFormulas_CSV::getbEffScaleFactor(int flavor, int algo, double pt, double eta) const {

  // values for Moriond 2013, see: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagPOG#Recommendation_for_b_c_tagging_a
  int index=999;
  float ptmin[] = {20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500};
  float ptmax[] = {30, 40, 50, 60, 70, 80,100, 120, 160, 210, 260, 320, 400, 500, 670};

  if(pt>670) pt=670;

  // determine the index
  for(int ind = 0; ind < 15 ; ind++) {
    if(pt>ptmin[ind] && pt<ptmax[ind]) {
      index=ind;
    }
  }

  // prescription for the first bin: use the upper bound if not light jets
  if( (abs(flavor)==5||abs(flavor)==4) && index==0) pt = ptmax[0];
  
  // compute the scale factor and its uncertainty
  double SFb = 1.0;
  double SFb_unc = 1.0;
  double x = pt;
  switch(abs(flavor)) {
    case 5: {
     // b-jets
     //Tagger: CSVL within 30 < pt GeV < 670 GeV, abs(eta) < 2.4, x = pt
     if(algo==1) {
       SFb = 1.02658*((1.+(0.0195388*x))/(1.+(0.0209145*x)));   
       SFb_unc = SFb_error_CSVL[index];
     } else if(algo==2) {
       // Tagger: CSVM within 30 < pt GeV < 670 GeV, abs(eta) < 2.4, x = pt
       SFb = 0.6981*((1.+(0.414063*x))/(1.+(0.300155*x)));
       SFb_unc = SFb_error_CSVM[index];
     } else if(algo==3) {
       // Tagger: CSVT within 30 < pt GeV < 670 GeV, abs(eta) < 2.4, x = pt
       SFb = 0.901615*((1.+(0.552628*x))/(1.+(0.547195*x)));
       SFb_unc = SFb_error_CSVT[index];
     }
     break;
   }
   case 4: {
     // c-jets // assumes the same SF as for b-jets: THE SAME as for the b (but twice the uncertainty)   
     //Tagger: CSVL within 30 < pt GeV < 670 GeV, abs(eta) < 2.4, x = pt
     if(algo==1) {
       SFb = 1.02658*((1.+(0.0195388*x))/(1.+(0.0209145*x)));   
       SFb_unc = SFb_error_CSVL[index]*2;
     } else if(algo==2) {
       // Tagger: CSVM within 30 < pt GeV < 670 GeV, abs(eta) < 2.4, x = pt
       SFb = 0.6981*((1.+(0.414063*x))/(1.+(0.300155*x)));
       SFb_unc = SFb_error_CSVM[index]*2;
     } else if(algo==3) {
       // Tagger: CSVT within 30 < pt GeV < 670 GeV, abs(eta) < 2.4, x = pt
       SFb = 0.901615*((1.+(0.552628*x))/(1.+(0.547195*x)));
       SFb_unc = SFb_error_CSVT[index]*2;
     }
     break;
   }
   default: {
     // udsg-jets + untags (assumes these are light jets), recommandation give SFb, SFb+ and SFb-, for SFb_unc we take (SFb+ -SFb-)/2, computed from 20 GeV as precise in the twiki
     if( algo == 1 && fabs(eta)>0.0 &&  fabs(eta)<= 0.5) {
       //   Tagger: CSVL within 20 < pt GeV, abs(eta) < 0.5, x = pt
       SFb = ((1.07536+(0.000175506*x))+(-8.63317e-07*(x*x)))+(3.27516e-10*(x*(x*x)));
       SFb_unc = ( ((0.994425+(-8.66392e-05*x))+(-3.03813e-08*(x*x)))+(-3.52151e-10*(x*(x*x))) - ((1.15628+(0.000437668*x))+(-1.69625e-06*(x*x)))+(1.00718e-09*(x*(x*x))) )/-2;
     } else if ( algo == 1 && fabs(eta)>0.5 &&  fabs(eta)<= 1.0) {
       //   Tagger: CSVL within 20 < pt GeV, 0.5 < abs(eta) < 1.0, x = pt
       SFb = ((1.07846+(0.00032458*x))+(-1.30258e-06*(x*x)))+(8.50608e-10*(x*(x*x)));
       SFb_unc = ( ((0.998088+(6.94916e-05*x))+(-4.82731e-07*(x*x)))+(1.63506e-10*(x*(x*x))) - ((1.15882+(0.000579711*x))+(-2.12243e-06*(x*x)))+(1.53771e-09*(x*(x*x))) )/-2;
     } else if ( algo == 1 && fabs(eta)>1.0 &&  fabs(eta)<= 1.5) {
       //   Tagger: CSVL within 20 < pt GeV, 1.0 < abs(eta) < 1.5, x = pt
       SFb = ((1.08294+(0.000474818*x))+(-1.43857e-06*(x*x)))+(1.13308e-09*(x*(x*x)));
       SFb_unc = ( ((1.00294+(0.000289844*x))+(-7.9845e-07*(x*x)))+(5.38525e-10*(x*(x*x))) - ((1.16292+(0.000659848*x))+(-2.07868e-06*(x*x)))+(1.72763e-09*(x*(x*x))) )/-2;
     } else if ( algo == 1 && fabs(eta)>1.5 &&  fabs(eta)<= 2.4) {
       //   Tagger: CSVL within 20 < pt GeV, 1.5 < abs(eta) < 2.4, x = pt
       SFb = ((1.0617+(0.000173654*x))+(-5.29009e-07*(x*x)))+(5.55931e-10*(x*(x*x)));
       SFb_unc = ( ((0.979816+(0.000138797*x))+(-3.14503e-07*(x*x)))+(2.38124e-10*(x*(x*x))) - ((1.14357+(0.00020854*x))+(-7.43519e-07*(x*x)))+(8.73742e-10*(x*(x*x))) )/-2;
     } else if ( algo == 2 && fabs(eta)>0.0 &&  fabs(eta)<= 0.8) {
       //   Tagger: CSVM within 20 < pt GeV, 0.0 < abs(eta) < 0.8, x = pt
       SFb = ((1.06182+(0.000617034*x))+(-1.5732e-06*(x*x)))+(3.02909e-10*(x*(x*x)));
       SFb_unc = ( ((0.972455+(7.51396e-06*x))+(4.91857e-07*(x*x)))+(-1.47661e-09*(x*(x*x))) - ((1.15116+(0.00122657*x))+(-3.63826e-06*(x*x)))+(2.08242e-09*(x*(x*x))) )/-2;
     } else if ( algo == 2 && fabs(eta)>0.8 &&  fabs(eta)<= 1.6) {
       //   Tagger: CSVM within 20 < pt GeV, 0.8 < abs(eta) < 1.6, x = pt
       SFb = ((1.111+(-9.64191e-06*x))+(1.80811e-07*(x*x)))+(-5.44868e-10*(x*(x*x)));
       SFb_unc = ( ((1.02055+(-0.000378856*x))+(1.49029e-06*(x*x)))+(-1.74966e-09*(x*(x*x))) - ((1.20146+(0.000359543*x))+(-1.12866e-06*(x*x)))+(6.59918e-10*(x*(x*x))) )/-2;
     } else if ( algo == 2 && fabs(eta)>1.6 &&  fabs(eta)<= 2.4) {
       //   Tagger: CSVM within 20 < pt GeV, 1.6 < abs(eta) < 2.4, x = pt
       SFb = ((1.08498+(-0.000701422*x))+(3.43612e-06*(x*x)))+(-4.11794e-09*(x*(x*x)));
       SFb_unc = ( ((0.983476+(-0.000607242*x))+(3.17997e-06*(x*x)))+(-4.01242e-09*(x*(x*x))) - ((1.18654+(-0.000795808*x))+(3.69226e-06*(x*x)))+(-4.22347e-09*(x*(x*x))) )/-2;  
     } else if ( algo == 3 && fabs(eta)>0.0 &&  fabs(eta)<= 2.4) {
       //   Tagger: CSVT within 20 < pt GeV, 0.0 < abs(eta) < 2.4, x = pt
       SFb = ((0.948463+(0.00288102*x))+(-7.98091e-06*(x*x)))+(5.50157e-09*(x*(x*x)));
       SFb_unc = ( ((0.899715+(0.00102278*x))+(-2.46335e-06*(x*x)))+(9.71143e-10*(x*(x*x))) - ((0.997077+(0.00473953*x))+(-1.34985e-05*(x*x)))+(1.0032e-08*(x*(x*x))) )/-2;
     }
   }
  }
  if(SFb_unc<0) {/*std::cout<<"Warning : SFb_unc is negative = "<<SFb_unc<<" the absolute value will be taken"<<std::endl;*/ SFb_unc=fabs(SFb_unc);}
  return std::make_pair(SFb, SFb_unc);
}  

btagPerfBase::value btagPerfPOGFormulas_CSV::getbEfficiency(int flavor, int algo, double pt, double eta) const {
  // small protection against large et (shere we have no measurement).
  // the subject is a bit delicate, but I think it is better to use 
  // the efficiency for the last bin than to set it to 0.
  if(pt>670) pt=670;
  switch(abs(flavor)) {
    case 5:
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
      else 
	return std::make_pair(0.,0.);
    case 4:
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
      else 
      return std::make_pair(0.,0.);
    default: {
      // this better parametrized from OUR mc
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
      else 
	return std::make_pair(0.,0.);
    }
  }
}

