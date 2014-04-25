#include "UserCode/zbb_louvain/interface/btagPerfBase.h"

class TH1F;
class TF1;
class TFile;

class btagPerfPOGFormulas_nofit : public btagPerfBase {
  public:
    btagPerfPOGFormulas_nofit(const char* inputfile);
    virtual ~btagPerfPOGFormulas_nofit();
  protected:
    virtual btagPerfBase::value getbEffScaleFactor(int flavor, int algo, double pt, double eta) const;
    virtual btagPerfBase::value getbEfficiency(int flavor, int algo, double pt, double eta) const;
  private:
    TF1* eff_;
    TFile* esdata_;
    static float SFb_error_CSVL[16];
    static float SFb_error_CSVM[16];
    static float SFb_error_CSVT[16];
    TH1F *h_eff_csvl_b_brl_, *h_eff_csvl_b_fwd_, *h_eff_csvl_c_brl_, *h_eff_csvl_c_fwd_;
    TH1F *h_eff_csvm_b_brl_, *h_eff_csvm_b_fwd_, *h_eff_csvm_c_brl_, *h_eff_csvm_c_fwd_;
    TH1F *h_eff_csvt_b_brl_, *h_eff_csvt_b_fwd_, *h_eff_csvt_c_brl_, *h_eff_csvt_c_fwd_;
    TH1F *h_eff_csvl_l_brl_, *h_eff_csvl_l_fwd_, *h_eff_csvm_l_brl_, *h_eff_csvm_l_fwd_, *h_eff_csvt_l_brl_, *h_eff_csvt_l_fwd_;
};

