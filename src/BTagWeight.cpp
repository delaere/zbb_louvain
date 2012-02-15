#include <math.h>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include "UserCode/zbb_louvain/interface/btagPerfFWLiteInterface.h"
#include "UserCode/zbb_louvain/interface/BTagWeight.h"

using namespace std; 

JetSet::JetSet(const char* infile) { interface_ = boost::shared_ptr<btagPerfFWLiteInterface>(new btagPerfFWLiteInterface(infile)); }

JetSet::~JetSet() { }

// add a jet to the set. 
// Efficiencies and scale factors are automatically extracted from the db,
// and the jet is added to the set only if meaningful data can be obtained.
void JetSet::addJet(std::string themode, std::string uncert, int flavor, double et, double eta) { 
  addJet(JetInfo(interface_->getbEfficiency(flavor,1,et,eta),
                 interface_->getbEffScaleFactor(themode,uncert,flavor,1,et,eta),
                 interface_->getbEfficiency(flavor,2,et,eta),
                 interface_->getbEffScaleFactor(themode,uncert,flavor,2,et,eta),
                 flavor)
        );
}

// add a jet to the set, checking that the efficiencies and scale factors are well defined.
void JetSet::addJet(const JetInfo& jet) {
  if(jet.isValid()) jets_.push_back(jet);
  else std::cerr << "Error: attempt to use a ill-defined jet for btagging." << std::endl
                 << jet.eff_SSVHEM << " " << jet.sf_SSVHEM << " " 
                 << jet.eff_SSVHPT << " " << jet.sf_SSVHPT << " "
                 << jet.flavor << std::endl; 
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
