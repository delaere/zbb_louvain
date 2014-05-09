#include <iostream>
#include <cmath>
#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
#include <string>
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

  //if the file contain csv, we guess that the good algo to use is CSV otherwise SSV is used by default
  std::string heWP ="SSVHEM";
  std::string hpWP ="SSVHPT";
  std::string sinputfile = inputfile;
  if(sinputfile.find("csv")!=std::string::npos){
    heWP ="CSVL";
    hpWP ="CSVM";
  }
  else if(sinputfile.find("jp")!=std::string::npos){
    heWP ="JPL";
    hpWP ="JPM";
  }
  es_->get(testRecID).get(plHandleBTAGSSVHEM_, ("MUJETSWPBTAG"+heWP).c_str());
  es_->get(testRecID).get(wpHandleBTAGSSVHEM_, ("MUJETSWPBTAG"+heWP).c_str() );
  if ( plHandleBTAGSSVHEM_.isValid() && wpHandleBTAGSSVHEM_.isValid() ) 
    perfBTAGSSVHEM_ = new BtagPerformance(*plHandleBTAGSSVHEM_, *wpHandleBTAGSSVHEM_);
  else 
    perfBTAGSSVHEM_ = NULL;

  es_->get(testRecID).get(plHandleMISTAGSSVHEM_, ("MISTAGS"+heWP).c_str() ); 
  es_->get(testRecID).get(wpHandleMISTAGSSVHEM_, ("MISTAG"+heWP).c_str() );
  if ( plHandleMISTAGSSVHEM_.isValid() && wpHandleMISTAGSSVHEM_.isValid() ) 
    perfMISTAGSSVHEM_ = new BtagPerformance(*plHandleMISTAGSSVHEM_, *wpHandleMISTAGSSVHEM_);
  else 
    perfMISTAGSSVHEM_ = NULL;

  es_->get(testRecID).get(plHandleBTAGSSVHPT_, ("MUJETSWPBTAG"+hpWP).c_str() ); 
  es_->get(testRecID).get(wpHandleBTAGSSVHPT_, ("MUJETSWPBTAG"+hpWP).c_str() );
  if ( plHandleBTAGSSVHPT_.isValid() && wpHandleBTAGSSVHPT_.isValid() ) 
    perfBTAGSSVHPT_ = new BtagPerformance(*plHandleBTAGSSVHPT_, *wpHandleBTAGSSVHPT_);
  else 
    perfBTAGSSVHPT_ = NULL;

  es_->get(testRecID).get(plHandleMISTAGSSVHPT_, ("MISTAG"+hpWP).c_str() );
  es_->get(testRecID).get(wpHandleMISTAGSSVHPT_, ("MISTAG"+hpWP).c_str() );
  if ( plHandleMISTAGSSVHPT_.isValid() && wpHandleMISTAGSSVHPT_.isValid() ) 
    perfMISTAGSSVHPT_ = new BtagPerformance(*plHandleMISTAGSSVHPT_, *wpHandleMISTAGSSVHPT_);
  else 
    perfMISTAGSSVHPT_ = NULL;
  // load data for the efficiency curves
  h_eff_ssvhem_b_brl_ = (TH1F*)esdata_->Get( (heWP+"/h_eff_bTagOverGoodJet_ptb_Barrel").c_str()  );
  h_eff_ssvhem_b_fwd_ = (TH1F*)esdata_->Get( (heWP+"/h_eff_bTagOverGoodJet_ptb_Endcaps").c_str() );
  h_eff_ssvhem_c_brl_ = (TH1F*)esdata_->Get( (heWP+"/h_eff_bTagOverGoodJet_ptc_Barrel").c_str()  );
  h_eff_ssvhem_c_fwd_ = (TH1F*)esdata_->Get( (heWP+"/h_eff_bTagOverGoodJet_ptc_Endcaps").c_str() );
  h_eff_ssvhem_l_brl_ = (TH1F*)esdata_->Get( (heWP+"/h_eff_bTagOverGoodJet_ptl_Barrel").c_str()  );
  h_eff_ssvhem_l_fwd_ = (TH1F*)esdata_->Get( (heWP+"/h_eff_bTagOverGoodJet_ptl_Endcaps").c_str() );
  h_eff_ssvhpt_b_brl_ = (TH1F*)esdata_->Get( (hpWP+"/h_eff_bTagOverGoodJet_ptb_Barrel").c_str()  );
  h_eff_ssvhpt_b_fwd_ = (TH1F*)esdata_->Get( (hpWP+"/h_eff_bTagOverGoodJet_ptb_Endcaps").c_str() );
  h_eff_ssvhpt_c_brl_ = (TH1F*)esdata_->Get( (hpWP+"/h_eff_bTagOverGoodJet_ptc_Barrel").c_str()  );
  h_eff_ssvhpt_c_fwd_ = (TH1F*)esdata_->Get( (hpWP+"/h_eff_bTagOverGoodJet_ptc_Endcaps").c_str() );
  h_eff_ssvhpt_l_brl_ = (TH1F*)esdata_->Get( (hpWP+"/h_eff_bTagOverGoodJet_ptl_Barrel").c_str()  );
  h_eff_ssvhpt_l_fwd_ = (TH1F*)esdata_->Get( (hpWP+"/h_eff_bTagOverGoodJet_ptl_Endcaps").c_str() );
}

btagPerfFWLiteInterface::~btagPerfFWLiteInterface() {
  if(perfMISTAGSSVHPT_) delete perfMISTAGSSVHPT_;
  if(perfBTAGSSVHPT_) delete perfBTAGSSVHPT_;
  if(perfMISTAGSSVHEM_) delete perfMISTAGSSVHEM_;
  if(perfBTAGSSVHEM_) delete perfBTAGSSVHEM_;
  delete es_;
  esdata_->Close();
}

btagPerfBase::value btagPerfFWLiteInterface::getbEffScaleFactor(int flavor, int algo, double pt, double eta) const {
  BinningPointByMap p;
  p.insert(BinningVariables::JetEta,fabs(eta));
  p.insert(BinningVariables::JetEt,pt<30. ? 30. : pt);
  switch(abs(flavor)) {
    case 5: {
      // b-jets
      BtagPerformance* perf_ = algo==1 ? perfBTAGSSVHEM_ : perfBTAGSSVHPT_ ;
      if(!perf_) return std::make_pair(1.,1.);
      return std::make_pair(perf_->getResult(PerformanceResult::BTAGBEFFCORR,p), 
                            pt<30. ? 0.12 : perf_->getResult(PerformanceResult::BTAGBERRCORR,p));
    }
    case 4: {
      // c-jets // assumes the same SF as for b-jets
      BtagPerformance* perf_ = algo==1 ? perfBTAGSSVHEM_ : perfBTAGSSVHPT_ ;
      if(!perf_) return std::make_pair(1.,1.);
      return std::make_pair(perf_->getResult(PerformanceResult::BTAGBEFFCORR,p), 
                            pt<30. ? 0.24 : perf_->getResult(PerformanceResult::BTAGBERRCORR,p)*2.);
    }
    default: {
      // udsg-jets + untags (assumes these are light jets from PU)
      BtagPerformance* perf_ = algo==1 ? perfMISTAGSSVHEM_ : perfMISTAGSSVHPT_ ;
      if(!perf_) return std::make_pair(1.,1.);
      return std::make_pair(perf_->getResult(PerformanceResult::BTAGLEFFCORR,p), perf_->getResult(PerformanceResult::BTAGBERRCORR,p));
    }
  }
}  

btagPerfBase::value btagPerfFWLiteInterface::getbEfficiency(int flavor, int algo, double pt, double eta) const {
  // small protection against large et (shere we have no measurement).
  // the subject is a bit delicate, but I think it is better to use 
  // the efficiency for the last bin than to set it to 0.
  if(pt>900) pt=900;
  switch(abs(flavor)) {
    case 5:
      // this is not in the db and must be parametrized from OUR mc
      if(fabs(eta)<1.2 && algo==1) 
        return std::make_pair(h_eff_ssvhem_b_brl_->GetBinContent(h_eff_ssvhem_b_brl_->FindBin(pt)),
                              h_eff_ssvhem_b_brl_->GetBinError(h_eff_ssvhem_b_brl_->FindBin(pt)));
      else if(fabs(eta)>1.2 && algo==1)
        return std::make_pair(h_eff_ssvhem_b_fwd_->GetBinContent(h_eff_ssvhem_b_fwd_->FindBin(pt)),
                              h_eff_ssvhem_b_fwd_->GetBinError(h_eff_ssvhem_b_fwd_->FindBin(pt)));
      else if(fabs(eta)<1.2 && algo==2)
        return std::make_pair(h_eff_ssvhpt_b_brl_->GetBinContent(h_eff_ssvhpt_b_brl_->FindBin(pt)),
                              h_eff_ssvhpt_b_brl_->GetBinError(h_eff_ssvhpt_b_brl_->FindBin(pt)));
      else if(fabs(eta)>1.2 && algo==2)
        return std::make_pair(h_eff_ssvhpt_b_fwd_->GetBinContent(h_eff_ssvhpt_b_fwd_->FindBin(pt)),
                              h_eff_ssvhpt_b_fwd_->GetBinError(h_eff_ssvhpt_b_fwd_->FindBin(pt)));
      else 
        return std::make_pair(0.,0.);
    case 4:
      // this is not in the db and must be parametrized from OUR mc
      if(fabs(eta)<1.2 && algo==1) 
        return std::make_pair(h_eff_ssvhem_c_brl_->GetBinContent(h_eff_ssvhem_c_brl_->FindBin(pt)),
                              h_eff_ssvhem_c_brl_->GetBinError(h_eff_ssvhem_c_brl_->FindBin(pt)));
      else if(fabs(eta)>1.2 && algo==1)
        return std::make_pair(h_eff_ssvhem_c_fwd_->GetBinContent(h_eff_ssvhem_c_fwd_->FindBin(pt)),
                              h_eff_ssvhem_c_fwd_->GetBinError(h_eff_ssvhem_c_fwd_->FindBin(pt)));
      else if(fabs(eta)<1.2 && algo==2)
        return std::make_pair(h_eff_ssvhpt_c_brl_->GetBinContent(h_eff_ssvhpt_c_brl_->FindBin(pt)),
                              h_eff_ssvhpt_c_brl_->GetBinError(h_eff_ssvhpt_c_brl_->FindBin(pt)));
      else if(fabs(eta)>1.2 && algo==2)
        return std::make_pair(h_eff_ssvhpt_c_fwd_->GetBinContent(h_eff_ssvhpt_c_fwd_->FindBin(pt)),
                              h_eff_ssvhpt_c_fwd_->GetBinError(h_eff_ssvhpt_c_fwd_->FindBin(pt)));
      else 
        return std::make_pair(0.,0.);
    default: {
      // this better parametrized from OUR mc
      if(fabs(eta)<1.2 && algo==1) 
        return std::make_pair(h_eff_ssvhem_l_brl_->GetBinContent(h_eff_ssvhem_l_brl_->FindBin(pt)),
                              h_eff_ssvhem_l_brl_->GetBinError(h_eff_ssvhem_l_brl_->FindBin(pt)));
      else if(fabs(eta)>1.2 && algo==1)
        return std::make_pair(h_eff_ssvhem_l_fwd_->GetBinContent(h_eff_ssvhem_l_fwd_->FindBin(pt)),
                              h_eff_ssvhem_l_fwd_->GetBinError(h_eff_ssvhem_l_fwd_->FindBin(pt)));
      else if(fabs(eta)<1.2 && algo==2)
        return std::make_pair(h_eff_ssvhpt_l_brl_->GetBinContent(h_eff_ssvhpt_l_brl_->FindBin(pt)),
                              h_eff_ssvhpt_l_brl_->GetBinError(h_eff_ssvhpt_l_brl_->FindBin(pt)));
      else if(fabs(eta)>1.2 && algo==2)
        return std::make_pair(h_eff_ssvhpt_l_fwd_->GetBinContent(h_eff_ssvhpt_l_fwd_->FindBin(pt)),
                              h_eff_ssvhpt_l_fwd_->GetBinError(h_eff_ssvhpt_l_fwd_->FindBin(pt)));
      else 
        return std::make_pair(0.,0.);
    }
  }
}

