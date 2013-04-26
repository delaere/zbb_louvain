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
};

float btagPerfPOGFormulas::SFb_error_CSVT[] = {
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
  float ptmin[] = {20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600};
  float ptmax[] = {30, 40, 50, 60, 70, 80,100, 120, 160, 210, 260, 320, 400, 500, 600, 800};

  if(pt>800) pt=800;

  // determine the index
  for(int ind = 0; ind < 16 ; ind++) {
    if(pt>ptmin[ind] && pt<ptmax[ind]) {
      index=ind;
    }
  }

  // prescription for the first bin: use the upper bound.
  //if(index==0) pt = ptmax[0];
  
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
     // udsg-jets + untags (assumes these are light jets), recommandation give SFb, SFb+ and SFb- for 2012 ABCD combined, for SFb_unc we take (SFb+ -SFb-)/2
     if(pt>700 && fabs(eta)>1.5) pt=700;
     else if(pt>800) pt=800;
     double x = pt;

     if( algo == 1 && fabs(eta)>0.0 &&  fabs(eta)<= 0.5) {
       //   Tagger: CSVL within 20 < pt GeV, abs(eta) < 0.5, x = pt
       SFb = ((1.04901+(0.00152181*x))+(-3.43568e-06*(x*x)))+(2.17219e-09*(x*(x*x)));
       SFb_unc = ( ((0.973773+(0.00103049*x))+(-2.2277e-06*(x*x)))+(1.37208e-09*(x*(x*x))) - ((1.12424+(0.00201136*x))+(-4.64021e-06*(x*x)))+(2.97219e-09*(x*(x*x))) )/-2;
     } else if ( algo == 1 && fabs(eta)>0.5 &&  fabs(eta)<= 1.0) {
       //   Tagger: CSVL within 20 < pt GeV, 0.5 < abs(eta) < 1.0, x = pt
       SFb = ((0.991915+(0.00172552*x))+(-3.92652e-06*(x*x)))+(2.56816e-09*(x*(x*x)));
       SFb_unc = ( ((0.921518+(0.00129098*x))+(-2.86488e-06*(x*x)))+(1.86022e-09*(x*(x*x))) - ((1.06231+(0.00215815*x))+(-4.9844e-06*(x*x)))+(3.27623e-09*(x*(x*x))) )/-2;
     } else if ( algo == 1 && fabs(eta)>1.0 &&  fabs(eta)<= 1.5) {
       //   Tagger: CSVL within 20 < pt GeV, 1.0 < abs(eta) < 1.5, x = pt
       SFb = ((0.962127+(0.00192796*x))+(-4.53385e-06*(x*x)))+(3.0605e-09*(x*(x*x)));
       SFb_unc = ( ((0.895419+(0.00153387*x))+(-3.48409e-06*(x*x)))+(2.30899e-09*(x*(x*x))) - ((1.02883+(0.00231985*x))+(-5.57924e-06*(x*x)))+(3.81235e-09*(x*(x*x))) )/-2;
     } else if ( algo == 1 && fabs(eta)>1.5 &&  fabs(eta)<= 2.4) {
       //   Tagger: CSVL within 20 < pt GeV, 1.5 < abs(eta) < 2.0, x = pt
       SFb = ((1.06121+(0.000332747*x))+(-8.81201e-07*(x*x)))+(7.43896e-10*(x*(x*x)));
       SFb_unc = ( ((0.983607+(0.000196747*x))+(-3.98327e-07*(x*x)))+(2.95764e-10*(x*(x*x))) - ((1.1388+(0.000468418*x))+(-1.36341e-06*(x*x)))+(1.19256e-09*(x*(x*x))) )/-2;
     } else if ( algo == 2 && fabs(eta)>0.0 &&  fabs(eta)<= 0.8) {
       //   Tagger: CSVM within 20 < pt GeV, 0.0 < abs(eta) < 0.8, x = pt
       SFb = ((1.06238+(0.00198635*x))+(-4.89082e-06*(x*x)))+(3.29312e-09*(x*(x*x)));
       SFb_unc = ( ((0.972746+(0.00104424*x))+(-2.36081e-06*(x*x)))+(1.53438e-09*(x*(x*x))) - ((1.15201+(0.00292575*x))+(-7.41497e-06*(x*x)))+(5.0512e-09*(x*(x*x))) )/-2;
     } else if ( algo == 2 && fabs(eta)>0.8 &&  fabs(eta)<= 1.6) {
       //   Tagger: CSVM within 20 < pt GeV, 0.8 < abs(eta) < 1.6, x = pt
       SFb = ((1.08048+(0.00110831*x))+(-2.96189e-06*(x*x)))+(2.16266e-09*(x*(x*x)));
       SFb_unc = ( ((0.9836+(0.000649761*x))+(-1.59773e-06*(x*x)))+(1.14324e-09*(x*(x*x))) - ((1.17735+(0.00156533*x))+(-4.32257e-06*(x*x)))+(3.18197e-09*(x*(x*x))) )/-2;
     } else if ( algo == 2 && fabs(eta)>1.6 &&  fabs(eta)<= 2.4) {
       //   Tagger: CSVM within 20 < pt GeV, 1.6 < abs(eta) < 2.4, x = pt
       SFb = ((1.09145+(0.000687171*x))+(-2.45054e-06*(x*x)))+(1.7844e-09*(x*(x*x)));
       SFb_unc = ( ((1.00616+(0.000358884*x))+(-1.23768e-06*(x*x)))+(6.86678e-10*(x*(x*x))) - ((1.17671+(0.0010147*x))+(-3.66269e-06*(x*x)))+(2.88425e-09*(x*(x*x))) )/-2;  
     } else if ( algo == 3 && fabs(eta)>0.0 &&  fabs(eta)<= 2.4) {
       //   Tagger: CSVT within 20 < pt GeV, 0.0 < abs(eta) < 2.4, x = pt
       SFb = ((1.01739+(0.00283619*x))+(-7.93013e-06*(x*x)))+(5.97491e-09*(x*(x*x)));
       SFb_unc = ( ((0.953587+(0.00124872*x))+(-3.97277e-06*(x*x)))+(3.23466e-09*(x*(x*x))) - ((1.08119+(0.00441909*x))+(-1.18764e-05*(x*x)))+(8.71372e-09*(x*(x*x))) )/-2;
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

