#include "UserCode/zbb_louvain/interface/btagPerfBase.h"

class TH1F;
class TF1;

class btagPerfPOGFormulas : public btagPerfBase {
  public:
    btagPerfPOGFormulas();
    virtual ~btagPerfPOGFormulas();
  protected:
    virtual btagPerfBase::value getbEffScaleFactor(int flavor, int algo, double pt, double eta) const;
    virtual btagPerfBase::value getbEfficiency(int flavor, int algo, double pt, double eta) const;
  private:
    TF1* eff_;
    static float SFb_error_SSVHEM[15];
    static float SFb_error_SSVHPT[15];
};

