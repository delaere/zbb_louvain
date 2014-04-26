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
    TFile* esdata_;
    static float SFb_error_CSVL[16];
    static float SFb_error_CSVM[16];
    static float SFb_error_CSVT[16];
    TH1F *h_eff_csvl_b_brl_, *h_eff_csvl_b_fwd_, *h_eff_csvl_c_brl_, *h_eff_csvl_c_fwd_;
    TH1F *h_eff_csvm_b_brl_, *h_eff_csvm_b_fwd_, *h_eff_csvm_c_brl_, *h_eff_csvm_c_fwd_;
    TH1F *h_eff_csvt_b_brl_, *h_eff_csvt_b_fwd_, *h_eff_csvt_c_brl_, *h_eff_csvt_c_fwd_;
    TH1F *h_eff_csvl_l_brl_, *h_eff_csvl_l_fwd_, *h_eff_csvm_l_brl_, *h_eff_csvm_l_fwd_, *h_eff_csvt_l_brl_, *h_eff_csvt_l_fwd_;

    TF1 *GetSFlmeanCSVL00, *GetSFlminCSVL00, *GetSFlmaxCSVL00;
    TF1 *GetSFlmeanCSVL05, *GetSFlminCSVL05, *GetSFlmaxCSVL05;
    TF1 *GetSFlmeanCSVL10, *GetSFlminCSVL10, *GetSFlmaxCSVL10;
    TF1 *GetSFlmeanCSVL15, *GetSFlminCSVL15, *GetSFlmaxCSVL15;

    TF1 *GetSFlmeanCSVM00, *GetSFlminCSVM00, *GetSFlmaxCSVM00;
    TF1 *GetSFlmeanCSVM08, *GetSFlminCSVM08, *GetSFlmaxCSVM08;
    TF1 *GetSFlmeanCSVM16, *GetSFlminCSVM16, *GetSFlmaxCSVM16;

    TF1 *GetSFlmeanCSVT00, *GetSFlminCSVT00, *GetSFlmaxCSVT00;
};

