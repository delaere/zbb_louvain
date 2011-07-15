#include "TFile.h"
#include "DataFormats/FWLite/interface/EventSetup.h"
#include "DataFormats/FWLite/interface/ESHandle.h"
#include "RecoBTag/PerformanceDB/interface/BtagPerformance.h"

class btagPerfFWLiteInterface {
  public:
    btagPerfFWLiteInterface(const char* inputfile);
    ~btagPerfFWLiteInterface();
    double getbEffScaleFactor(int flavor, int algo, double pt, double eta);
    double getbEfficiency(int flavor, int algo, double pt, double eta);
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
};

