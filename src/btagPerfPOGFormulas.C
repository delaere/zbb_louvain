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
  eff_ = new TF1("sigmoid","[0]+[3]/(1+exp([1]-x*[2]))",0,1000);
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

  // prescription for the first bin: use the upper bound.
  if(index==0) pt = ptmax[0];
  
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
          eff_->SetParameters(-5.51040e-02,2.23373e+00,8.77422e-02,8.08854e-01);
        } else {
          eff_->SetParameters(-7.09015e-01,6.94739e-01,6.66446e-02,1.38546e+00);
        }
      } else {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(1.34081e-01,5.44067e+00,1.47838e-01,4.44133e-01);
        } else {
          eff_->SetParameters(2.24147e-02,2.86102e+00,8.52067e-02,4.82894e-01);
        }
      }
      return std::make_pair(eff_->Eval(pt),0.);
    }
    case 4: {
      if(algo==1) {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(-6.70200e-01,-6.94898e-01,3.31213e-02,9.39803e-01);
        } else {
          eff_->SetParameters(-1.77879e-01,9.01356e-01,4.12996e-02,4.40469e-01);
        }
      } else {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(1.12619e-01,4.03054e+00,-3.16668e-02,-1.00842e+01);
        } else {
          eff_->SetParameters(1.00000e-02,5.05689e+00,1.09649e-01,7.14612e-02);
        }
      }
      return std::make_pair(eff_->Eval(pt),0.);
    }
    default: {
      if(algo==1) {
        if(fabs(eta)<0.8) {
          return std::make_pair(0.000547883+0.00023023*pt-7.317920e-07*pt*pt+1.15659e-09*pt*pt*pt-7.00641e-13*pt*pt*pt*pt,0.);
        } else if(fabs(eta)<1.6) {
          return std::make_pair(0.000615562+0.000240254*pt-7.00237e-07*pt*pt+1.25660e-09*pt*pt*pt-8.59011e-13*pt*pt*pt*pt,0.);
        } else {
          return std::make_pair(0.000372388+0.000309735*pt-4.35952e-07*pt*pt+3.63763e-10*pt*pt*pt-2.11993e-13*pt*pt*pt*pt,0.);
        }
      } else {
          return std::make_pair(-2.9605e-05+2.35624e-05*pt-1.77552e-08*pt*pt,0.);
      }
    }
  }
}

