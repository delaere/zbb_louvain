#include <math.h>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <boost/shared_ptr.hpp>
#include "UserCode/zbb_louvain/interface/BTagWeight.h"
#include "UserCode/zbb_louvain/interface/btagPerfPOGformulas.h"
#include "UserCode/zbb_louvain/interface/btagPerfPOGformulas_nofit.h"
#include "UserCode/zbb_louvain/interface/btagPerfFWLiteInterface.h"

using namespace std; 

JetSet::JetSet(std::string themode, const char* infile) {
  if(themode=="hardcoded")
    interface_ = boost::shared_ptr<btagPerfBase>(new btagPerfPOGFormulas());
  else if(themode=="hardcoded_nofit")
    interface_ = boost::shared_ptr<btagPerfBase>(new btagPerfPOGFormulas_nofit(infile)); 
  else if(themode=="database")
    interface_ = boost::shared_ptr<btagPerfBase>(new btagPerfFWLiteInterface(infile)); 
  else {
    std::cout << "Warning: UNKNOWN MODE: please check the spelling, 'database' or 'hardcoded' "<< std::endl;
    if(std::string(infile)=="") {
      std::cout << "  using hardcoded values." << std::endl;
      interface_ = boost::shared_ptr<btagPerfBase>(new btagPerfPOGFormulas());
    } else {
      std::cout << "  using database." << std::endl;
      interface_ = boost::shared_ptr<btagPerfBase>(new btagPerfFWLiteInterface(infile));
    }
  }
}

JetSet::~JetSet() { }

// add a jet to the set. 
// Efficiencies and scale factors are automatically extracted from the db,
// and the jet is added to the set only if meaningful data can be obtained.
void JetSet::addJet(std::string uncert, int flavor, double et, double eta, int algo1, int algo2) { 
  btagPerfBase::SystematicVariation mode = btagPerfBase::MEAN;
  if(uncert=="min") mode = btagPerfBase::MIN;
  if(uncert=="max") mode = btagPerfBase::MAX;
  if(uncert=="min_bc") mode = btagPerfBase::MIN_BC;
  if(uncert=="max_bc") mode = btagPerfBase::MAX_BC;
  if(uncert=="min_l") mode = btagPerfBase::MIN_L;
  if(uncert=="max_l") mode = btagPerfBase::MAX_L;
  addJet(JetInfo(interface_->getbEfficiency(mode,flavor,algo1,et,eta),
                 interface_->getbEffScaleFactor(mode,flavor,algo1,et,eta),
                 interface_->getbEfficiency(mode,flavor,algo2,et,eta),
                 interface_->getbEffScaleFactor(mode,flavor,algo2,et,eta),
                 flavor)
        );
}

// add a jet to the set, checking that the efficiencies and scale factors are well defined.
void JetSet::addJet(const JetInfo& jet) {
  //jet.print(); // for debugging
  if(jet.isValid()) jets_.push_back(jet);
  else {
    std::cerr << "Error: attempt to use a ill-defined jet for btagging." << std::endl;
    jet.print(true);
  }
  if(jet.flavor==0 && (jet.eff_SSVHEM>0.5 || jet.eff_SSVHPT>0.5)) { //true if jets not matched with a parton are not considered like a light jet 
    std::cerr << "Warning : attempt to use a ill-defined jet for btagging. with high eficiency" << std::endl;
    jet.print(true);
  }
}

// filter events passing the selection
bool BTagWeight::filter(int t) const {
  return (t >= minTags1 && t <= maxTags1);
}

// compute the weight for jets of one kind (algo1 = HE, algo2 = HP)
float BTagWeight::weight(vector<JetInfo> jets, int algo, int ntags) const {
  if(!filter(ntags)) return 0; //shouldn't be 1 ? No, we are safe, with the event selection.
  int njets=jets.size();
  int comb= 1 << njets;
  float pMC=0;
  float pData=0;
  for(int i=0;i < comb; i++) {
    float mc=1.;
    float data=1.;
    int ntagged=0;
    for(int j=0;j<njets;j++) {
      bool tagged = ((i >> j) & 0x1);
      switch(algo) {
        case 1: {
          if(tagged) {
            ntagged++;
            mc*=jets[j].eff_SSVHEM;
            data*=jets[j].eff_SSVHEM*jets[j].sf_SSVHEM;
          } else {
            mc*=(1.-jets[j].eff_SSVHEM);
	    data*=(1.-jets[j].eff_SSVHEM*jets[j].sf_SSVHEM);
          }
	}
 	case 2: {
          if(tagged) {
            ntagged++;
            mc*=jets[j].eff_SSVHPT;
            data*=jets[j].eff_SSVHPT*jets[j].sf_SSVHPT;
          } else {
            mc*=(1.-jets[j].eff_SSVHPT);
            data*=(1.-jets[j].eff_SSVHPT*jets[j].sf_SSVHPT);
          }
 	}
      }
    }       
    if(filter(ntagged)) {
      pMC+=mc;
      pData+=data;
    }
  }
  if(pMC==0) return 0; 
  return pData/pMC;
}

// filter events passing the selection
bool BTagWeight::filter(int t1, int t2) const {
 return (t1>=minTags1 && t1<=maxTags1 && t2>=minTags2 && t2<=maxTags2);
}

// compute the weight for jets of two kinds, one including the othe (e.g. SSV HE and HP)
float BTagWeight::weight2(vector<JetInfo> jets, int ntags1, int ntags2) const {
  // check that the event passes the selection
  if(!filter(ntags1,ntags2)) return 0; //shouldn't be 1 ? No, we are safe, with the event selection.
  int njets=jets.size();
  int comb = pow(3,njets);
  float pMC=0;
  float pData=0;
  for(int i=0;i < comb; i++) {
    float mc=1.;
    float data=1.;
    int ntagged1=0;
    int ntagged2=0;
    for(int j=0;j<njets;j++) {
      int tagged = int(i/pow(3,j)+0.5)%3;
      switch(tagged) {
        case 0: { // no tag
          mc*=(1.-jets[j].eff_SSVHEM);
          data*=(1.-jets[j].eff_SSVHEM*jets[j].sf_SSVHEM);
          break;
        }
        case 1: { // HE tag (and not HP)
          ntagged1++;
	  //if(jets[j].flavor<4||jets[j].flavor>5) std::cout<<"efficiency on Mc for Loose is "<<jets[j].eff_SSVHEM<<std::endl;
          mc*=(jets[j].eff_SSVHEM-jets[j].eff_SSVHPT);
          data*=(jets[j].eff_SSVHEM*jets[j].sf_SSVHEM-jets[j].eff_SSVHPT*jets[j].sf_SSVHPT);
          break;
        }
        case 2: { // HP tag (and HE)
          ntagged1++;
          ntagged2++;
          mc*=jets[j].eff_SSVHPT;
          data*=jets[j].eff_SSVHPT*jets[j].sf_SSVHPT;
          break;
        }
      }
    }       
    if(filter(ntagged1,ntagged2)) {
      pMC+=mc;
      pData+=data;
    }
  }
  if(pMC==0) return 0; 
  return pData/pMC;
}
