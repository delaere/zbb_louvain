#include <iostream>
#include <cmath>
#include <cstdlib>
#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
#include <string>
#include "UserCode/zbb_louvain/interface/btagPerfPOGformulas.h"

// uncertainties in Pt bins 
// according POG reccom., use 12% on the first bin

float btagPerfPOGFormulas::SFb_error_SSVHEM[] = {
         0.120000, 
         0.0316234, 
         0.0310149, 
         0.02381, 
         0.0223228, 
         0.023461, 
         0.0202517, 
         0.0156249, 
         0.0214799, 
         0.0399369, 
         0.0416666, 
         0.0431031, 
         0.0663209, 
         0.0687731, 
         0.0793305  
       };

float btagPerfPOGFormulas::SFb_error_SSVHPT[] = {
         0.120000, 
         0.0403485, 
         0.0396907,
         0.0291837, 
         0.0325778, 
         0.0335716, 
         0.0255023, 
         0.0300639, 
         0.0253228, 
         0.0409739, 
         0.043561, 
         0.0458427, 
         0.0763302, 
         0.0781752, 
         0.108927
       };

btagPerfPOGFormulas::btagPerfPOGFormulas() {
  // just a sigmoid. Used to parametrize the efficiencies
  eff_ = new TF1("sigmoidTimesL","[0]+([3]+[4]*x)/(1+exp([1]-x*[2]))",20,1000);
}

btagPerfPOGFormulas::~btagPerfPOGFormulas() {
  delete eff_;
}

btagPerfBase::value btagPerfPOGFormulas::getbEffScaleFactor(int flavor, int algo, double pt, double eta) const {

  // values for Moriond 2012, see: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagPOG#Recommendation_for_b_c_tagging_a
  int index=999;
  float ptmin[] = {25, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500};
  float ptmax[] = {30, 40, 50, 60, 70, 80,100, 120, 160, 210, 260, 320, 400, 500, 670};
  
  // protection against large pt (where we have no measurement).  
  if(pt>670) pt=670;

  // determine the index
  for(int ind = 0; ind < 15 ; ind++) {
    if(pt>ptmin[ind] && pt<ptmax[ind]) {
      index=ind;
    }
  }

  // prescription for the first bin: use the upper bound.if not light jets 
  if( (abs(flavor)==5||abs(flavor)==4) && index==0) pt = ptmax[0];
  
  // compute the scale factor and its uncertainty
  double SFb = 1.0;
  double SFb_unc = 1.0;
  switch(abs(flavor)) {
    case 5: {
     // b-jets
     //Tagger: SSVHEM within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
     if(algo==1) {
       SFb = 0.896462*((1.+(0.00957275*pt))/(1.+(0.00837582*pt)));   
       SFb_unc = SFb_error_SSVHEM[index];
     } else if(algo==2) {
       // Tagger: SSVHPT within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
       SFb = 0.422556*((1.+(0.437396*pt))/(1.+(0.193806*pt)));
       SFb_unc = SFb_error_SSVHPT[index];
     }
     break;
   }
   case 4: {
     // c-jets // assumes the same SF as for b-jets: THE SAME as for the b (but twice the uncertainty)   
     //Tagger: SSVHEM within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
     if(algo==1){
       SFb = 0.896462*((1.+(0.00957275*pt))/(1.+(0.00837582*pt)));
       SFb_unc = SFb_error_SSVHEM[index]*2.;
     } else if(algo==2) {
       //   Tagger: SSVHPT within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
       SFb = 0.422556*((1.+(0.437396*pt))/(1.+(0.193806*pt)));
       SFb_unc = SFb_error_SSVHPT[index]*2.;
     }
     break;
   }
   default: {
     // udsg-jets + untags (assumes these are light jets)
     if(pt>670) pt=670;
     if( algo == 1 && fabs(eta)>0.0 &&  fabs(eta)<= 0.8) {
       //   Tagger: SSVHEM within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
       SFb = 0.86318+0.000801639*pt-1.64119e-06*pt*pt+2.59121e-10*pt*pt*pt;
       SFb_unc = 0.0728159+3.38553e-04*pt-1.205256e-06*pt*pt+1.167417e-09*pt*pt*pt;
     }
     else if( algo ==1 &&  fabs(eta)> 0.8 &&  fabs(eta)<=1.6) {
       //   Tagger: SSVHEM within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
       SFb = 0.958973-0.000269555*pt+1.381e-06*pt*pt-1.87744e-09*pt*pt*pt;
       SFb_unc = 0.093202+1.0353e-05*pt+3.956e-08*pt*pt-1.2156e-10*pt*pt*pt;
     }
     else if( algo==1 &&  fabs(eta)>1.6  &&  fabs(eta)<=2.4) {
       //   Tagger: SSVHEM within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
       SFb = 0.923033-0.000898227*pt+4.74565e-06*pt*pt-6.11053e-09*pt*pt*pt;
       SFb_unc = 9.5012e-02-1.66301e-04*pt+5.4952e-07*pt*pt-2.9674e-10*pt*pt*pt;
     }
     else if( algo== 2 &&  fabs(eta)> 0.0 &&  fabs(eta)<=2.4) {
       //   Tagger: SSVHPT within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
       SFb = 0.97409+0.000646241*pt-2.86294e-06*pt*pt+2.79484e-09*pt*pt*pt;
       SFb_unc = 1.66868e-01-3.90519e-04*pt+7.6136e-07*pt*pt-3.7884e-10*pt*pt*pt;
     }
   }
  }
  return std::make_pair(SFb, SFb_unc);
}  

btagPerfBase::value btagPerfPOGFormulas::getbEfficiency(int flavor, int algo, double pt, double eta) const {
  switch(abs(flavor)) {
    case 5: {
      if(algo==1) {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(-1.48976e+01,-2.33468e+00,5.63766e-02,1.54646e+01,-1.76495e-04);
        } else {
          eff_->SetParameters(-1.49449e+01,-2.48731e+00,5.10619e-02,1.54167e+01,-9.20870e-05);
        }
      } else {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(-2.22397e+01,-2.73586e+00,5.61474e-02,2.28068e+01,-1.76713e-04);
        } else {
          eff_->SetParameters(-4.46156e+01,-3.58358e+00,5.06866e-02,4.50875e+01,-9.21825e-05);
        }
      }
      return std::make_pair(eff_->Eval(pt),0.);
    }
    case 4: {
      if(algo==1) {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(-2.35646e+00,-2.23076e+00,5.30713e-02,2.44600e+00,-4.10810e-05);
        } else {
          eff_->SetParameters(-2.36127e+00,-2.39206e+00,4.54041e-02,2.44112e+00,-6.91750e-05);
        }
      } else {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(-1.31439e+01,-3.95421e+00,5.24966e-02,1.32335e+01,-4.11156e-05);
        } else {
          eff_->SetParameters(-1.31488e+01,-4.11692e+00,4.49178e-02,1.32286e+01,-6.91372e-05);
        }
      }
      return std::make_pair(eff_->Eval(pt),0.);
    }
    default: {
      if(algo==1) {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(1.69103e-04,5.09983e+00,6.26066e-02,9.38001e-04,2.13956e-06);
        } else {
          eff_->SetParameters(1.86636e-04,4.41344e+00,4.72039e-02,3.77524e-03,-1.22904e-06);
        }
      } else {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(-1.31642e+01,-8.03625e+00,3.84933e-03,1.31682e+01,-1.84878e-06);
        } else {
          eff_->SetParameters(-1.31639e+01,-7.84069e+00,8.51549e-03,1.31682e+01,0.00000e+00);
        }
      }
      return std::make_pair(eff_->Eval(pt),0.);
    }
  }
}

