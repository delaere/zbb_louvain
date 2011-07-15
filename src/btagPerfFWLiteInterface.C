#include <iostream>
#include <cmath>
#include "TFile.h"
#include "DataFormats/FWLite/interface/Record.h"
#include "DataFormats/FWLite/interface/EventSetup.h"
#include "DataFormats/FWLite/interface/ESHandle.h"
#include "CondFormats/PhysicsToolsObjects/interface/BinningPointByMap.h"
#include "RecoBTag/PerformanceDB/interface/BtagPerformance.h"
#include "UserCode/zbb_louvain/interface/btagPerfFWLiteInterface.h"

btagPerfFWLiteInterface::btagPerfFWLiteInterface(const char* inputfile) {
  //std::cout << "btagPerfFWLiteInterface: Initializing..." << std::endl;
  esdata_ = TFile::Open(inputfile);
  es_ = esdata_ ? new fwlite::EventSetup(esdata_) : NULL;
  if ( es_ && es_->exists("BTagPerformanceRecord") ) {
    //std::cout << "btagPerfFWLiteInterface: Got the performance tree" << std::endl;
  } else {
    std::cerr << "btagPerfFWLiteInterface: Can't find performance tree" << std::endl;
    perfBTAGSSVHEM_ = NULL;
    perfMISTAGSSVHEM_ = NULL;
    perfBTAGSSVHPT_ = NULL;
    perfMISTAGSSVHPT_ = NULL;
    return;
  }
  fwlite::RecordID testRecID = es_->recordID("BTagPerformanceRecord");
  es_->syncTo(edm::EventID(1001,0,0),edm::Timestamp());
  //std::cout << "btagPerfFWLiteInterface: Got record ID " << testRecID << es_->get(testRecID).startSyncValue().eventID()<<std::endl;

  es_->get(testRecID).get(plHandleBTAGSSVHEM_,"BTAGSSVHEM"); 
  es_->get(testRecID).get(wpHandleBTAGSSVHEM_,"BTAGSSVHEM");
  if ( plHandleBTAGSSVHEM_.isValid() && wpHandleBTAGSSVHEM_.isValid() ) 
    perfBTAGSSVHEM_ = new BtagPerformance(*plHandleBTAGSSVHEM_, *wpHandleBTAGSSVHEM_);
  else 
    perfBTAGSSVHEM_ = NULL;

  es_->get(testRecID).get(plHandleMISTAGSSVHEM_,"MISTAGSSVHEM"); 
  es_->get(testRecID).get(wpHandleMISTAGSSVHEM_,"MISTAGSSVHEM");
  if ( plHandleMISTAGSSVHEM_.isValid() && wpHandleMISTAGSSVHEM_.isValid() ) 
    perfMISTAGSSVHEM_ = new BtagPerformance(*plHandleMISTAGSSVHEM_, *wpHandleMISTAGSSVHEM_);
  else 
    perfMISTAGSSVHEM_ = NULL;

  es_->get(testRecID).get(plHandleBTAGSSVHPT_,"BTAGSSVHPT"); 
  es_->get(testRecID).get(wpHandleBTAGSSVHPT_,"BTAGSSVHPT");
  if ( plHandleBTAGSSVHPT_.isValid() && wpHandleBTAGSSVHPT_.isValid() ) 
    perfBTAGSSVHPT_ = new BtagPerformance(*plHandleBTAGSSVHPT_, *wpHandleBTAGSSVHPT_);
  else 
    perfBTAGSSVHPT_ = NULL;

  es_->get(testRecID).get(plHandleMISTAGSSVHPT_,"MISTAGSSVHPT"); 
  es_->get(testRecID).get(wpHandleMISTAGSSVHPT_,"MISTAGSSVHPT");
  if ( plHandleMISTAGSSVHPT_.isValid() && wpHandleMISTAGSSVHPT_.isValid() ) 
    perfMISTAGSSVHPT_ = new BtagPerformance(*plHandleMISTAGSSVHPT_, *wpHandleMISTAGSSVHPT_);
  else 
    perfMISTAGSSVHPT_ = NULL;
}

btagPerfFWLiteInterface::~btagPerfFWLiteInterface() {
  if(perfMISTAGSSVHPT_) delete perfMISTAGSSVHPT_;
  if(perfBTAGSSVHPT_) delete perfBTAGSSVHPT_;
  if(perfMISTAGSSVHEM_) delete perfMISTAGSSVHEM_;
  if(perfBTAGSSVHEM_) delete perfBTAGSSVHEM_;
  delete es_;
  esdata_->Close();
}

double btagPerfFWLiteInterface::getbEffScaleFactor(int flavor, int algo, double pt, double eta) {
  BinningPointByMap p;
  p.insert(BinningVariables::JetAbsEta,fabs(eta));
  p.insert(BinningVariables::JetEt,pt);
  switch(flavor) {
    case 5: {
      // b-jets
      BtagPerformance* perf_ = algo==1 ? perfBTAGSSVHEM_ : perfBTAGSSVHPT_ ;
      if(!perf_) return 1.;
      return perf_->getResult(PerformanceResult::BTAGBEFFCORR,p);
    }
    case 4: {
      // c-jets // assumes the same SF as for b-jets
      BtagPerformance* perf_ = algo==1 ? perfBTAGSSVHEM_ : perfBTAGSSVHPT_ ;
      if(!perf_) return 1.;
      return perf_->getResult(PerformanceResult::BTAGBEFFCORR,p);
    }
    default: {
      // udsg-jets + untags (assumes these are light jets from PU)
      BtagPerformance* perf_ = algo==1 ? perfMISTAGSSVHEM_ : perfMISTAGSSVHPT_ ;
      if(!perf_) return 1.;
      return perf_->getResult(PerformanceResult::BTAGLEFFCORR,p);
    }
  }
}

double btagPerfFWLiteInterface::getbEfficiency(int flavor, int algo, double pt, double eta) {
  switch(flavor) {
    case 5:
      // this is not in the db and must be parametrized from OUR mc
      return algo==1 ? 0.6 : 0.4 ; // FAKE !!!
    case 4:
      // this is not in the db and must be parametrized from OUR mc
      return algo==1 ? 0.08 : 0.008; // FAKE !!!
    default: {
      // difficult to measure the fake rate in our sample... use official mistag.
      BtagPerformance* perf_ = algo==1 ? perfMISTAGSSVHEM_ : perfMISTAGSSVHPT_ ;
      if(!perf_) return 0.;
      BinningPointByMap p;
      p.insert(BinningVariables::JetAbsEta,fabs(eta));
      p.insert(BinningVariables::JetEt,pt);
      return perf_->getResult(PerformanceResult::BTAGLEFF,p);
    }
  }
}

