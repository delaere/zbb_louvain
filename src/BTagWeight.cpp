#include <math.h>
#include <iostream>
#include <vector>
#include <map>
#include <utility>

using namespace std; 

// jet info class
class JetInfo {
  public:
    JetInfo(float mceff=1.,float datasf=1., int mcflavor=5, int balgo=1) : eff(mceff), sf(datasf), flavor(mcflavor), algo(balgo) {}
    ~JetInfo() {}
    float eff;
    float sf;
    int flavor;
    int algo;
};

// a vector of jetsets, easily handled in python
class JetSet {
  public:
    explicit JetSet(int year):year_(year) {}
    ~JetSet() {}
    void add(int flavor, int algo, double pt, double eta) { 
      jets_.push_back(JetInfo(getbEfficiency(flavor,algo,pt,eta),getbEffScaleFactor(flavor,algo,pt,eta),flavor,algo)); 
    }
    vector<JetInfo>& getJets() { return jets_; }
  private:
    int year_;
    vector<JetInfo> jets_;
    double getbEffScaleFactor(int flavor, int algo, double pt, double eta);
    double getbEfficiency(int flavor, int algo, double pt, double eta);
    // associative maps
    static std::map<std::pair<double, double>,double> theAssociativeMapSFbHEM2010_;
    static std::map<std::pair<double, double>,double> theAssociativeMapSFbHPT2010_;
    static std::map<std::pair<double, double>,double> theAssociativeMapSFbHEM2011_;
    static std::map<std::pair<double, double>,double> theAssociativeMapSFbHPT2011_;
    static bool __init;
    static bool initializeMaps();
};

std::map<std::pair<double, double>,double> JetSet::theAssociativeMapSFbHEM2010_;
std::map<std::pair<double, double>,double> JetSet::theAssociativeMapSFbHPT2010_;
std::map<std::pair<double, double>,double> JetSet::theAssociativeMapSFbHEM2011_;
std::map<std::pair<double, double>,double> JetSet::theAssociativeMapSFbHPT2011_;

//intialize the associative maps
bool JetSet::initializeMaps() {
  // SFb for Fall10 (Winter10?) and 2010 data                                           #
  // based on http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2011_114_v2.pdf #
  //SSVHEM
  theAssociativeMapSFbHEM2010_[std::make_pair<double,double>(40,50)] = 0.909;
  theAssociativeMapSFbHEM2010_[std::make_pair<double,double>(50,60)] = 0.841;
  theAssociativeMapSFbHEM2010_[std::make_pair<double,double>(60,80)] = 0.857;
  theAssociativeMapSFbHEM2010_[std::make_pair<double,double>(80,140)] = 0.753;
  theAssociativeMapSFbHEM2010_[std::make_pair<double,double>(140,999999)] = 0.617;
  //SSVHPT
  theAssociativeMapSFbHPT2010_[std::make_pair<double,double>(40,50)] = 0.956;
  theAssociativeMapSFbHPT2010_[std::make_pair<double,double>(50,60)] = 0.927;
  theAssociativeMapSFbHPT2010_[std::make_pair<double,double>(60,80)] = 0.854;
  theAssociativeMapSFbHPT2010_[std::make_pair<double,double>(80,140)] = 0.824;
  theAssociativeMapSFbHPT2010_[std::make_pair<double,double>(140,999999)] = 0.713;
  // SFb for Spring11 (+DA patch) or Summer11 MC and 2011 data                                             #
  // based on https://indico.cern.ch/getFile.py/access?contribId=2&resId=1&materialId=slides&confId=130982 #
  //SSVHEM
  theAssociativeMapSFbHEM2011_[std::make_pair<double,double>(15,20)] = 0.873;
  theAssociativeMapSFbHEM2011_[std::make_pair<double,double>(20,30)] = 1.069;
  theAssociativeMapSFbHEM2011_[std::make_pair<double,double>(30,40)] = 1.014;
  theAssociativeMapSFbHEM2011_[std::make_pair<double,double>(40,50)] = 0.981;
  theAssociativeMapSFbHEM2011_[std::make_pair<double,double>(50,60)] = 0.977;
  theAssociativeMapSFbHEM2011_[std::make_pair<double,double>(60,70)] = 0.892;
  theAssociativeMapSFbHEM2011_[std::make_pair<double,double>(70,80)] = 0.982;
  theAssociativeMapSFbHEM2011_[std::make_pair<double,double>(80,100)] = 0.966;
  theAssociativeMapSFbHEM2011_[std::make_pair<double,double>(100,120)] = 0.947;
  theAssociativeMapSFbHEM2011_[std::make_pair<double,double>(120,999999)] = 0.795;
  //SSVHPT
  theAssociativeMapSFbHPT2011_[std::make_pair<double,double>(15,20)] = 0.802;
  theAssociativeMapSFbHPT2011_[std::make_pair<double,double>(20,30)] = 1.000;
  theAssociativeMapSFbHPT2011_[std::make_pair<double,double>(30,40)] = 0.995;
  theAssociativeMapSFbHPT2011_[std::make_pair<double,double>(40,50)] = 0.948;
  theAssociativeMapSFbHPT2011_[std::make_pair<double,double>(50,60)] = 0.912;
  theAssociativeMapSFbHPT2011_[std::make_pair<double,double>(60,70)] = 0.829;
  theAssociativeMapSFbHPT2011_[std::make_pair<double,double>(70,80)] = 0.948;
  theAssociativeMapSFbHPT2011_[std::make_pair<double,double>(80,100)] = 0.900;
  theAssociativeMapSFbHPT2011_[std::make_pair<double,double>(100,120)] = 0.863;
  theAssociativeMapSFbHPT2011_[std::make_pair<double,double>(120,999999)] = 0.794;
  // confirm initialization
  return true;
}

// do the initialization !
bool JetSet::__init = JetSet::initializeMaps();

// scale factor as a funtion of (pt,eta) for a given algo and year.
double JetSet::getbEffScaleFactor(int flavor,int algo,double pt, double /*eta*/){
  //we only have SF for b-jets... or do we use mistag SF for light and c ? 
  if(flavor!=5) return 1.;
  // select the proper maps
  std::map<std::pair<double, double>,double>& theAssociativeMapSFb_ = theAssociativeMapSFbHEM2010_;
  if(year_==2010 && algo==1) theAssociativeMapSFb_ = theAssociativeMapSFbHEM2010_;
  if(year_==2010 && algo==2) theAssociativeMapSFb_ = theAssociativeMapSFbHPT2010_;
  if(year_==2011 && algo==1) theAssociativeMapSFb_ = theAssociativeMapSFbHEM2011_;
  if(year_==2011 && algo==2) theAssociativeMapSFb_ = theAssociativeMapSFbHPT2011_;
  //loop over the map
  for(std::map<std::pair<double, double>,double>::const_iterator it = theAssociativeMapSFb_.begin(); 
      it !=theAssociativeMapSFb_.end(); ++it ){
    // if pT in the range
    if( pt >= it->first.first && pt <= it->first.second){
      return it->second;
    }// ends if on pT range
  }// ends loop over map
  return 1;
}

// efficiency as a funtion of (pt,eta) for a given algo and year.
// TODO: these numbers are just fake for now. Could also be tabulated.
double JetSet::getbEfficiency(int flavor, int algo, double /*pt*/, double /*eta*/) {
  if(flavor==5) { //Bjets
    if(algo==1) return 0.70; //SSVHEM
    else return 0.40; //SSVHPT
  } else if(flavor==4) { //Cjets
    if(algo==1) return 0.2; //SSVHEM
    else return 0.02; //SSVHPT
  } else { // light jets (UDSG) and pileup (no id)
    if(algo==1) return 0.1; //SSVHEM
    else return 0.01; //SSVHPT
  }
}

// the algorithm.
// TODO: that version only works for one or two jets of the same kind.
class BTagWeight 
{
 public:
   BTagWeight(int jmin, int jmax): maxTags(jmax), minTags(jmin) {}
   virtual ~BTagWeight() {}
   bool filter(int t);
   float weight(vector<JetInfo> jets, int tags);
   float weight(JetSet jets, int tags) { return weight(jets.getJets(),tags); }
 private:
   int maxTags;
   int minTags;
};

// filter events passing the selection
bool BTagWeight::filter(int t)
{
 return (t >= minTags && t <= maxTags);
}

// compute the weight
float BTagWeight::weight(vector<JetInfo> jets, int tags)
{
 if(!filter(tags)) return 0;
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
      if(tagged) 
        {
           ntagged++;
           mc*=jets[j].eff;
           data*=jets[j].eff*jets[j].sf;
        }
      else
        {
           mc*=(1.-jets[j].eff);
           data*=(1.-jets[j].eff*jets[j].sf);
        }
    }       
   
   if(filter(ntagged))
   {
    std::cout << mc << " " << data << endl;
    pMC+=mc;
    pData+=data;
   }
  }

  if(pMC==0) return 0; 
  return pData/pMC;
}

