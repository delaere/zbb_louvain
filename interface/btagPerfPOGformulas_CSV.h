#include "UserCode/zbb_louvain/interface/btagPerfBase.h"

class TFile;
class TH1F;
class TF1;

class btagPerfPOGFormulas_CSV : public btagPerfBase {
  public:
    btagPerfPOGFormulas_CSV(const char* inputfile);
    virtual ~btagPerfPOGFormulas_CSV();
  protected:
    virtual btagPerfBase::value getbEffScaleFactor(int flavor, int algo, double pt, double eta) const;
    virtual btagPerfBase::value getbEfficiency(int flavor, int algo, double pt, double eta) const;
  private:
    TF1* eff_;
    TFile* esdata_;
    static float SFb_error_CSVL[15];
    static float SFb_error_CSVM[15];
    static float SFb_error_CSVT[15];
    TH1F *h_eff_csvl_b_brl_, *h_eff_csvl_b_fwd_, *h_eff_csvl_c_brl_, *h_eff_csvl_c_fwd_;
    TH1F *h_eff_csvm_b_brl_, *h_eff_csvm_b_fwd_, *h_eff_csvm_c_brl_, *h_eff_csvm_c_fwd_;
    TH1F *h_eff_csvl_l_brl_, *h_eff_csvl_l_fwd_, *h_eff_csvm_l_brl_, *h_eff_csvm_l_fwd_;
};

