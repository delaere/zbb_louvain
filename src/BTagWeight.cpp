#include <math.h>
#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include "UserCode/zbb_louvain/interface/btagPerfFWLiteInterface.h"
#include "UserCode/zbb_louvain/interface/BTagWeight.h"

using namespace std; 

JetSet::JetSet(const char* infile) { interface_ = new btagPerfFWLiteInterface(infile); }

JetSet::~JetSet() { delete interface_; }

void JetSet::addJet(int flavor, double et, double eta) { 
   jets_.push_back(JetInfo(interface_->getbEfficiency(flavor,1,et,eta),
                           interface_->getbEffScaleFactor(flavor,1,et,eta),
			   interface_->getbEfficiency(flavor,2,et,eta),
			   interface_->getbEffScaleFactor(flavor,2,et,eta),
                           flavor)
                  );
}

void JetSet::addJet(JetInfo jet) {
  jets_.push_back(jet);
}

// filter events passing the selection
bool BTagWeight::filter(int t)
{
 return (t >= minTags && t <= maxTags);
}

// compute the weight
float BTagWeight::weight(vector<JetInfo> jets, int algo, int ntags)
{
 if(!filter(ntags)) return 0;
 int njets=jets.size();
 int comb= 1 << njets;
 float pMC=0;
 float pData=0;
 for(int i=0;i < comb; i++)
  {
   float mc=1.;
   float data=1.;
   int ntagged=0;
   for(int j=0;j<njets;j++)
    {
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
   
   if(filter(ntagged))
   {
    //std::cout << mc << " " << data << endl;
    pMC+=mc;
    pData+=data;
   }
  }

  if(pMC==0) return 0; 
  return pData/pMC;
}

