#include "TFile.h"
#include "TString.h"
#include "TF1.h"
#include <string>
#include "DataFormats/FWLite/interface/EventSetup.h"
#include "DataFormats/FWLite/interface/ESHandle.h"
#include "RecoBTag/PerformanceDB/interface/BtagPerformance.h"

class TH1F;

class btagPerfFWLiteInterface {
  public:
    btagPerfFWLiteInterface(const char* inputfile);
    ~btagPerfFWLiteInterface();
    double getbEffScaleFactor(std::string mode, std::string meanminmax ,int flavor, int algo, double pt, double eta) const;
    double getbEfficiency(int flavor, int algo, double pt, double eta) const;
  private:
    TFile* esdata_;
    fwlite::EventSetup* es_;
    fwlite::ESHandle< PerformancePayload > plHandleBTAGSSVHEM_;
    fwlite::ESHandle< PerformanceWorkingPoint > wpHandleBTAGSSVHEM_;
    BtagPerformance* perfBTAGSSVHEM_;
    fwlite::ESHandle< PerformancePayload > plHandleMISTAGSSVHEM_;
    fwlite::ESHandle< PerformanceWorkingPoint > wpHandleMISTAGSSVHEM_;
    BtagPerformance* perfMISTAGSSVHEM_;
    fwlite::ESHandle< PerformancePayload > plHandleBTAGSSVHPT_;
    fwlite::ESHandle< PerformanceWorkingPoint > wpHandleBTAGSSVHPT_;
    BtagPerformance* perfBTAGSSVHPT_;
    fwlite::ESHandle< PerformancePayload > plHandleMISTAGSSVHPT_;
    fwlite::ESHandle< PerformanceWorkingPoint > wpHandleMISTAGSSVHPT_;
    BtagPerformance* perfMISTAGSSVHPT_;
    TH1F *h_eff_ssvhem_b_brl_, *h_eff_ssvhem_b_fwd_, *h_eff_ssvhem_c_brl_, *h_eff_ssvhem_c_fwd_;
    TH1F *h_eff_ssvhpt_b_brl_, *h_eff_ssvhpt_b_fwd_, *h_eff_ssvhpt_c_brl_, *h_eff_ssvhpt_c_fwd_;
    TF1 *tmpSFl_1, *tmpSFl_2, *tmpSFl_3, *tmpSFl_4, *tmpSFl_5, *tmpSFl_6, *tmpSFl_7, *tmpSFl_8, *tmpSFl_9, *tmpSFl_10, *tmpSFl_11, *tmpSFl_12;
};

