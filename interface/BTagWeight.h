#include <vector>
#include "TString.h"
#include <string>
#include <iostream>
#include "UserCode/zbb_louvain/interface/btagPerfBase.h"

// jet info class
class JetInfo {
  public:
    JetInfo(float mceffSSVHE=1.,float datasfSSVHE=1., float mceffSSVHP=1.,float datasfSSVHP=1., int mcflavor=5): 
      eff_SSVHEM(mceffSSVHE), sf_SSVHEM(datasfSSVHE), eff_SSVHPT(mceffSSVHP), sf_SSVHPT(datasfSSVHP),flavor(mcflavor) {}
    ~JetInfo() {}
    float eff_SSVHEM;
    float sf_SSVHEM;
    float eff_SSVHPT;
    float sf_SSVHPT;
    int   flavor;
    bool isValid() const {
      return eff_SSVHEM>=0 && eff_SSVHEM<=1 && eff_SSVHPT>=0 && eff_SSVHPT<=1 && sf_SSVHEM>=0 && sf_SSVHEM<=10 && sf_SSVHPT>=0 && sf_SSVHPT<=10;
    }
    void print(bool usecerr = false) const {
      if(usecerr) {
        std::cerr << "Jet info (flavor " << flavor << ") :" 
                  << " eff_SSVHEM=" << eff_SSVHEM
                  << " sf_SSVHEM=" << sf_SSVHEM
                  << " eff_SSVHPT=" << eff_SSVHPT
                  << " sf_SSVHPT=" << sf_SSVHPT
                  << ". Validity: " << isValid() << std::endl;
      } else {
        std::cout << "Jet info (flavor " << flavor << ") :" 
                  << " eff_SSVHEM=" << eff_SSVHEM
                  << " sf_SSVHEM=" << sf_SSVHEM
                  << " eff_SSVHPT=" << eff_SSVHPT
                  << " sf_SSVHPT=" << sf_SSVHPT
                  << ". Validity: " << isValid() << std::endl;
      }
    }
};

// a vector of jetsets, easily handled in python
class JetSet {
  public:
    JetSet(std::string themode, const char* infile = "");
    ~JetSet();
    void addJet(std::string uncert, int flavor, double et, double eta);
    void addJet(const JetInfo& jet);
    const std::vector<JetInfo>& getJets() const { return jets_; }
    void reset() { jets_.clear(); }
  private:
    std::vector<JetInfo> jets_;
    boost::shared_ptr<btagPerfBase> interface_;
};

// the algorithm.
class BTagWeight 
{
 public:
   BTagWeight(int jmin1, int jmax1, int jmin2, int jmax2): maxTags1(jmax1), minTags1(jmin1), maxTags2(jmax2), minTags2(jmin2) {}
   virtual ~BTagWeight() {}
   void setLimits(int jmin1, int jmax1, int jmin2, int jmax2) { maxTags1=jmax1; minTags1=jmin1; maxTags2=jmax2; minTags2=jmin2; }
   // check that the selection is fulfiled (one algo case)
   bool filter(int t) const;
   // check that the selection is fulfiled (two algos case)
   bool filter(int t1, int t2) const;
   // compute the weight in the 1 algo case
   float weight(std::vector<JetInfo> jets, int algo, int ntags) const;
   float weight(JetSet& jets, int algo, int ntags) const { return weight(jets.getJets(),algo,ntags); }
   // compute the weight in the 2 algos case
   float weight2(std::vector<JetInfo> jets, int ntags1, int ntags2) const;
   float weight2(JetSet& jets, int ntags1, int ntags2) const { return weight2(jets.getJets(),ntags1,ntags2); }
 private:
   int maxTags1;
   int minTags1;
   int maxTags2;
   int minTags2;
};

