#include <iostream>
#include <cmath>
#include <cstdlib>
#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
#include <string>
#include "UserCode/zbb_louvain/interface/btagPerfPOGformulas.h"

// uncertainties in Pt bins 
// according POG reccom., computed for pt 20-800, for pt > 800 GeV: use the SFb value at 800 GeV with twice the quoted uncertainty 

float btagPerfPOGFormulas::SFb_error_CSVL[] = {
  0.0484285,
  0.0126178,
  0.0120027,
  0.0141137,
  0.0145441,
  0.0131145,
  0.0168479,
  0.0160836,
  0.0126209,
  0.0136017,
  0.019182,
  0.0198805,
  0.0386531,
  0.0392831,
  0.0481008,
  0.0474291,
  2*0.0474291
};

float btagPerfPOGFormulas::SFb_error_CSVM[] = {
  0.0554504,
  0.0209663,
  0.0207019,
  0.0230073,
  0.0208719,
  0.0200453,
  0.0264232,
  0.0240102,
  0.0229375,
  0.0184615,
  0.0216242,
  0.0248119,
  0.0465748,
  0.0474666,
  0.0718173,
  0.0717567,
  2*0.0717567
};

float btagPerfPOGFormulas::SFb_error_CSVT[] = {
  0.0567059,
  0.0266907,
  0.0263491,
  0.0342831,
  0.0303327,
  0.024608,
  0.0333786,
  0.0317642,
  0.031102,
  0.0295603,
  0.0474663,
  0.0503182,
  0.0580424,
  0.0575776,
  0.0769779,
  0.0898199,
  2*0.0898199
};


btagPerfPOGFormulas::btagPerfPOGFormulas() {
  // just a sigmoid. Used to parametrize the efficiencies
  eff_ = new TF1("sigmoidTimesL","[0]+([3]+[4]*x)/(1+exp([1]-x*[2]))",20,1000);
}

btagPerfPOGFormulas::~btagPerfPOGFormulas() {
  delete eff_;
}

btagPerfBase::value btagPerfPOGFormulas::getbEffScaleFactor(int flavor, int algo, double pt, double eta) const {

  // values for Moriond 2013, see: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagPOG#Recommendation_for_b_c_tagging_a
  int index=999;
  float ptmin[] = {20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600, 800};
  float ptmax[] = {30, 40, 50, 60, 70, 80,100, 120, 160, 210, 260, 320, 400, 500, 600, 800, 1000};

  if(pt>1000) pt=1000;

  // determine the index
  for(int ind = 0; ind < 17 ; ind++) {
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
     //Tagger: CSVL within 20 < pt GeV, abs(eta) < 2.4, x = pt
     if(algo==1) {
       SFb = 0.981149*((1.+(-0.000713295*pt))/(1.+(-0.000703264*pt)));   
       SFb_unc = SFb_error_CSVL[index];
     } else if(algo==2) {
       // Tagger: CSVM within 20 < pt GeV, abs(eta) < 2.4, x = pt
       SFb = 0.726981*((1.+(0.253238*pt))/(1.+(0.188389*pt)));
       SFb_unc = SFb_error_CSVM[index];
     } else if(algo==3) {
       // Tagger: CSVT within 20 < pt GeV, abs(eta) < 2.4, x = pt
       SFb = 0.869965*((1.+(0.0335062*pt))/(1.+(0.0304598*pt)));
       SFb_unc = SFb_error_CSVT[index];
     }

     break;
   }
   case 4: {
     // c-jets // assumes the same SF as for b-jets: THE SAME as for the b (but twice the uncertainty)   
     //Tagger: SSVHEM within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
     //Tagger: CSVL within 20 < pt GeV, abs(eta) < 2.4, x = pt
     if(algo==1) {
       SFb = 0.981149*((1.+(-0.000713295*pt))/(1.+(-0.000703264*pt)));   
       SFb_unc = SFb_error_CSVL[index]*2;
     } else if(algo==2) {
       // Tagger: CSVM within 20 < pt GeV, abs(eta) < 2.4, x = pt
       SFb = 0.726981*((1.+(0.253238*pt))/(1.+(0.188389*pt)));
       SFb_unc = SFb_error_CSVM[index]*2;
     } else if(algo==3) {
       // Tagger: CSVT within 20 < pt GeV, abs(eta) < 2.4, x = pt
       SFb = 0.869965*((1.+(0.0335062*pt))/(1.+(0.0304598*pt)));
       SFb_unc = SFb_error_CSVT[index]*2;
     }

     break;
   }
   default: {
     // udsg-jets + untags (assumes these are light jets), recommandation give SFb, SFb+ and SFb- but still for 2011, for SFb_unc we take (SFb+ -SFb-)/2
     if(pt>800) pt=800;
     if( algo == 1 && fabs(eta)>0.0 &&  fabs(eta)<= 0.5) {
       //   Tagger: CSVL within 20 < pt GeV, abs(eta) < 0.5, x = pt
       SFb = ((1.07536+(0.000175506*pt))+(-8.63317e-07*(pt*pt)))+(3.27516e-10*(pt*(pt*pt)));
       SFb_unc = ( ((0.994425+(-8.66392e-05*pt))+(-3.03813e-08*(pt*pt)))+(-3.52151e-10*(pt*(pt*pt))) - ((1.15628+(0.000437668*pt))+(-1.69625e-06*(pt*pt)))+(1.00718e-09*(pt*(pt*pt))) )/-2;
     } else if ( algo == 1 && fabs(eta)>0.5 &&  fabs(eta)<= 1.0) {
       //   Tagger: CSVL within 20 < pt GeV, 0.5 < abs(eta) < 1.0, x = pt
       SFb = ((1.07846+(0.00032458*pt))+(-1.30258e-06*(pt*pt)))+(8.50608e-10*(pt*(pt*pt)));
       SFb_unc = ( ((0.998088+(6.94916e-05*pt))+(-4.82731e-07*(pt*pt)))+(1.63506e-10*(pt*(pt*pt))) - ((1.15882+(0.000579711*pt))+(-2.12243e-06*(pt*pt)))+(1.53771e-09*(pt*(pt*pt))) )/-2;
     } else if ( algo == 1 && fabs(eta)>1.0 &&  fabs(eta)<= 1.5) {
       //   Tagger: CSVL within 20 < pt GeV, 1.0 < abs(eta) < 1.5, x = pt
       SFb = ((1.08294+(0.000474818*pt))+(-1.43857e-06*(pt*pt)))+(1.13308e-09*(pt*(pt*pt)));
       SFb_unc = ( ((1.00294+(0.000289844*pt))+(-7.9845e-07*(pt*pt)))+(5.38525e-10*(pt*(pt*pt))) - ((1.16292+(0.000659848*pt))+(-2.07868e-06*(pt*pt)))+(1.72763e-09*(pt*(pt*pt))) )/-2;
     } else if ( algo == 1 && fabs(eta)>1.5 &&  fabs(eta)<= 2.0) {
       //   Tagger: CSVL within 20 < pt GeV, 1.5 < abs(eta) < 2.0, x = pt
       SFb = ((1.0617+(0.000173654*pt))+(-5.29009e-07*(pt*pt)))+(5.55931e-10*(pt*(pt*pt)));
       SFb_unc = ( ((0.979816+(0.000138797*pt))+(-3.14503e-07*(pt*pt)))+(2.38124e-10*(pt*(pt*pt))) - ((1.14357+(0.00020854*pt))+(-7.43519e-07*(pt*pt)))+(8.73742e-10*(pt*(pt*pt))) )/-2;
     } else if ( algo == 1 && fabs(eta)>2.0 &&  fabs(eta)<= 2.4) {
       //   Tagger: CSVL within 20 < pt GeV, 2.0 < abs(eta) < 2.4, x = pt
       if(pt>700) pt=700;
       SFb = ((1.0617+(0.000173654*pt))+(-5.29009e-07*(pt*pt)))+(5.55931e-10*(pt*(pt*pt)));
       SFb_unc = ( ((0.979816+(0.000138797*pt))+(-3.14503e-07*(pt*pt)))+(2.38124e-10*(pt*(pt*pt))) - ((1.14357+(0.00020854*pt))+(-7.43519e-07*(pt*pt)))+(8.73742e-10*(pt*(pt*pt))) )/-2;
       
     } else if ( algo == 2 && fabs(eta)>0.0 &&  fabs(eta)<= 0.8) {
       //   Tagger: CSVM within 20 < pt GeV, 0.0 < abs(eta) < 0.8, x = pt
       SFb = ((1.06182+(0.000617034*pt))+(-1.5732e-06*(pt*pt)))+(3.02909e-10*(pt*(pt*pt)));
       SFb_unc = ( ((0.972455+(7.51396e-06*pt))+(4.91857e-07*(pt*pt)))+(-1.47661e-09*(pt*(pt*pt))))- fabs(SFb-((1.15116+(0.00122657*pt))+(-3.63826e-06*(pt*pt)))+(2.08242e-09*(pt*(pt*pt))) )/-2;
     } else if ( algo == 2 && fabs(eta)>0.8 &&  fabs(eta)<= 1.6) {
       //   Tagger: CSVM within 20 < pt GeV, 0.8 < abs(eta) < 1.6, x = pt
       SFb = ((1.111+(-9.64191e-06*pt))+(1.80811e-07*(pt*pt)))+(-5.44868e-10*(pt*(pt*pt)));
       SFb_unc = ( ((1.02055+(-0.000378856*pt))+(1.49029e-06*(pt*pt)))+(-1.74966e-09*(pt*(pt*pt))) - ((1.20146+(0.000359543*pt))+(-1.12866e-06*(pt*pt)))+(6.59918e-10*(pt*(pt*pt))) )/-2;
     } else if ( algo == 2 && fabs(eta)>1.6 &&  fabs(eta)<= 2.4) {
       //   Tagger: CSVM within 20 < pt GeV, 1.6 < abs(eta) < 2.4, x = pt
       SFb = ((1.08498+(-0.000701422*pt))+(3.43612e-06*(pt*pt)))+(-4.11794e-09*(pt*(pt*pt)));
       SFb_unc = ( ((0.983476+(-0.000607242*pt))+(3.17997e-06*(pt*pt)))+(-4.01242e-09*(pt*(pt*pt))) - ((1.18654+(-0.000795808*pt))+(3.69226e-06*(pt*pt)))+(-4.22347e-09*(pt*(pt*pt))) )/-2;
       
     } else if ( algo == 3 && fabs(eta)>0.0 &&  fabs(eta)<= 2.4) {
       //   Tagger: CSVT within 20 < pt GeV, 0.0 < abs(eta) < 2.4, x = pt
       SFb = ((0.948463+(0.00288102*pt))+(-7.98091e-06*(pt*pt)))+(5.50157e-09*(pt*(pt*pt)));
       SFb_unc = ( ((0.899715+(0.00102278*pt))+(-2.46335e-06*(pt*pt)))+(9.71143e-10*(pt*(pt*pt))) - ((0.997077+(0.00473953*pt))+(-1.34985e-05*(pt*pt)))+(1.0032e-08*(pt*(pt*pt))) )/-2;
     }
   }
  }
  if(SFb_unc<0) {/*std::cout<<"Warning : SFb_unc is negative = "<<SFb_unc<<" the absolute value will be taken"<<std::endl;*/ SFb_unc=fabs(SFb_unc);}
  return std::make_pair(SFb, SFb_unc);
}  

btagPerfBase::value btagPerfPOGFormulas::getbEfficiency(int flavor, int algo, double pt, double eta) const {
  switch(abs(flavor)) {
    case 5: {
      if(algo==1) {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(0.840321,4.81788,-0.076856,-82.2072,0.018272);
        } else {
          eff_->SetParameters(0.836553,4.07004,-0.0759033,-35.2138,-0.00014107);
        }
      } else {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(0.676632,2.78089,-0.0254405,-14.5089,0.294153);
        } else {
          eff_->SetParameters(0.671256,2.2391,-0.0369153,-10.4821,0.112888);
        }
      }
      return std::make_pair(eff_->Eval(pt),0.);
    }
    case 4: {
      if(algo==1) {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(0.359646,2.82075,-0.111542,-60.3113,3.0002);
        } else {
          eff_->SetParameters(0.385027,1.35562,-0.105426,-20.9092,1.11364);
        }
      } else {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(0.200776,1.17113,-0.0683021,-1.6036,0.0033813);
        } else {
          eff_->SetParameters(0.157195,2.3917,-0.0854877,-5.08071,-0.0221911);
        }
      }
      return std::make_pair(eff_->Eval(pt),0.);
    }
    default: {
      if(algo==1) {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(0.0807507,-4.94873,-0.0494754,0.0467574,-0.000975562);
        } else {
          eff_->SetParameters(0.129643,-2.59915,-0.119248,-0.420888,0.0245026);
        }
      } else {
        if(fabs(eta)<1.2) {
          eff_->SetParameters(0.0145932,-3.96123,-0.0337904,-0.00135054,-8.38501e-05);
        } else {
          eff_->SetParameters(0.0163065,-328.366,-4.24081,0.00713713,-0.000172221);
        }
      }
      return std::make_pair(eff_->Eval(pt),0.);
    }
  }
}

