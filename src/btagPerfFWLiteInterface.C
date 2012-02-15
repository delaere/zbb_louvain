#include <iostream>
#include <cmath>
#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
//#include "TString.h"
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
  // load data for the efficiency curves
  h_eff_ssvhem_b_brl_ = (TH1F*)esdata_->Get("SSVHEM/h_eff_bTagOverGoodJet_ptb1_brl");
  h_eff_ssvhem_b_fwd_ = (TH1F*)esdata_->Get("SSVHEM/h_eff_bTagOverGoodJet_ptb1_fwd");
  h_eff_ssvhem_c_brl_ = (TH1F*)esdata_->Get("SSVHEM/h_eff_bTagOverGoodJet_ptc1_brl");
  h_eff_ssvhem_c_fwd_ = (TH1F*)esdata_->Get("SSVHEM/h_eff_bTagOverGoodJet_ptc1_fwd");
  h_eff_ssvhpt_b_brl_ = (TH1F*)esdata_->Get("SSVHPT/h_eff_bTagOverGoodJet_ptb1_brl");
  h_eff_ssvhpt_b_fwd_ = (TH1F*)esdata_->Get("SSVHPT/h_eff_bTagOverGoodJet_ptb1_fwd");
  h_eff_ssvhpt_c_brl_ = (TH1F*)esdata_->Get("SSVHPT/h_eff_bTagOverGoodJet_ptc1_brl");
  h_eff_ssvhpt_c_fwd_ = (TH1F*)esdata_->Get("SSVHPT/h_eff_bTagOverGoodJet_ptc1_fwd");
}

btagPerfFWLiteInterface::~btagPerfFWLiteInterface() {
  if(perfMISTAGSSVHPT_) delete perfMISTAGSSVHPT_;
  if(perfBTAGSSVHPT_) delete perfBTAGSSVHPT_;
  if(perfMISTAGSSVHEM_) delete perfMISTAGSSVHEM_;
  if(perfBTAGSSVHEM_) delete perfBTAGSSVHEM_;
  delete es_;
  esdata_->Close();
}

double btagPerfFWLiteInterface::getbEffScaleFactor(std::string mode, std::string meanminmax, int flavor, int algo, double pt, double eta) const {
  
  //double btagPerfFWLiteInterface::getbEffScaleFactor(int flavor, int algo, double pt, double eta) const {  // R.C. 2012: previous version

  if (mode=="hardcoded")
    {
      // values for Moriond 2012, see: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagPOG#Recommendation_for_b_c_tagging_a
      int index=999;
      float ptmin[] = {25, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500};
      float ptmax[] = {30, 40, 50, 60, 70, 80,100, 120, 160, 210, 260, 320, 400, 500, 670};
      float SFb=1.0;
      
      // protection against large pt (where we have no measurement).  
      if(pt>670) pt=670;
      
      for(int ind = 0; ind < 15 ; ind++){
	if(pt>ptmin[ind] && pt<ptmax[ind]){
	  index=ind;
	}
      }
      //std::cout << "index " << index <<std::endl;  
      
      switch(abs(flavor)){
      case 5: {
	// b-jets
	//Tagger: SSVHEM within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
	if(algo==1){
	  //FIXME:temporary solution
	  if(index==0) {
	    SFb = 0.896462*((1.+(0.00957275*35))/(1.+(0.00837582*35)));
	  }
	  else{
	    SFb = 0.896462*((1.+(0.00957275*pt))/(1.+(0.00837582*pt)));   
	  }
	  
	  float SFb_error[] = {
	    /// 12% uncertainties assigned according POG reccom. on the first bin
	    0.120000, 
	    0.0316234, 
	    0.0310149, 
	    0.02381, 
	    0.0223228, 
	    0.023461, 
	    0.0202517, 
	    0.0156249, 
	    0.0214799, 
	    0.0399369, 
	    0.0416666, 
	    0.0431031, 
	    0.0663209, 
	    0.0687731, 
	    0.0793305  
	  };     
	  
	  if(meanminmax=="mean"){
	    return SFb;
	  }
	  else if(meanminmax=="min"){
	    return SFb-(SFb*SFb_error[index]);
	    
	  }
	  else if(meanminmax=="max"){
	    return SFb+(SFb*SFb_error[index]);
	  }
	  else{
	    std::cerr << "WARNING: unrecognize specification: no weight assigned, please check!" << std::endl;
	    return 1.0;
	  }
	}
	
	else if(algo==2){
	  //   Tagger: SSVHPT within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
	  //FIXME:temporary solution
	  if(index==0){
	    SFb = 0.422556*((1.+(0.437396*35))/(1.+(0.193806*35)));
	  }
	  else {
	    SFb = 0.422556*((1.+(0.437396*pt))/(1.+(0.193806*pt)));
	  }
	  
	  float SFb_error[] = {
	    0.120000, 
	    0.0403485, 
	    0.0396907,
	    0.0291837, 
	    0.0325778, 
	    0.0335716, 
	    0.0255023, 
	    0.0300639, 
	    0.0253228, 
	    0.0409739, 
	    0.043561, 
	    0.0458427, 
	    0.0763302, 
	    0.0781752, 
	    0.108927
	  };
	  
	  if(meanminmax=="mean"){
	    return SFb;
	  }
	  else if(meanminmax=="min"){
	    return SFb-(SFb*SFb_error[index]);
	  }
	  else if(meanminmax=="max"){
	    return SFb+(SFb*SFb_error[index]);
	  }
	  else{
	    std::cerr << "WARNING: unrecognize specification: no weight assigned, please check!" << std::endl;
	    return 1.0;
	  }    
	}
	else{
	  std::cerr << "WARNING: unrecognized tagger: no weight assigned, please check!" << std::endl;
	  return 1.0;  
	}
      }
	
      case 4: {
	// c-jets // assumes the same SF as for b-jets: THE SAME as for the b (but twice the uncertainty)   
	//Tagger: SSVHEM within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
	if(algo==1){
	  //FIXME:temporary solution
	  if(index==0){
	    SFb = 0.896462*((1.+(0.00957275*35))/(1.+(0.00837582*35)));
	  }
	  else {
	    SFb = 0.896462*((1.+(0.00957275*pt))/(1.+(0.00837582*pt)));
	  }
	  float SFb_error[] = {
	    /// 12% uncertainties assigned according POG reccom. on the first bin
	    0.120000, 
	    0.0316234, 
	    0.0310149, 
	    0.02381, 
	    0.0223228, 
	    0.023461, 
	    0.0202517, 
	    0.0156249, 
	    0.0214799, 
	    0.0399369, 
	    0.0416666, 
	    0.0431031, 
	    0.0663209, 
	    0.0687731, 
	    0.0793305  
	  };
	  
	  if(meanminmax=="mean"){
	    return SFb;
	  }
	  else if(meanminmax=="min"){
	    return SFb-(SFb*2*SFb_error[index]);
	  }
	  else if(meanminmax=="max"){
	    return SFb+(SFb*2*SFb_error[index]);
	  }
	  else{
	    std::cerr << "WARNING: unrecognized specification : no weight assigned, please check!" << std::endl;
	    return 1.0;	
	  }
	}
	
	else if(algo==2){
	  //   Tagger: SSVHPT within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
	  //FIXME:temporary solution
	  if(index==0){
	    SFb = 0.422556*((1.+(0.437396*35))/(1.+(0.193806*35)));
	  }
	  else {
	    SFb = 0.422556*((1.+(0.437396*pt))/(1.+(0.193806*pt)));
	  }
	  
	  float SFb_error[] = {
	    0.120000, 
	    0.0403485, 
	    0.0396907,
	    0.0291837, 
	    0.0325778, 
	    0.0335716, 
	    0.0255023, 
	    0.0300639, 
	    0.0253228, 
	    0.0409739, 
	    0.043561, 
	    0.0458427, 
	    0.0763302, 
	    0.0781752, 
	    0.108927
	  };
	  
	  
	  if(meanminmax=="mean"){
	    return SFb;
	  }
	  else if(meanminmax=="min"){
	    return SFb-(SFb*2*SFb_error[index]);
	  }
	  else if(meanminmax=="max"){
	    return SFb+(SFb*2*SFb_error[index]);
	  }
	  else{
	    std::cerr << "WARNING: unrecognize specification: no weight assigned, please check!" << std::endl;
	    return 1.0;
	  }    
	}
	else{
	  std::cerr << "WARNING: unrecognize tagger: no weight assigned, please check!" << std::endl;
	  return 1.0;  
	}
      }
	
      default: {
	// udsg-jets + untags (assumes these are light jets)
	// FIXME....
	TF1 *tmpSFl = NULL;
	if(pt>670) pt=670;
	if( algo == 1 && fabs(eta)>0.0 &&  fabs(eta)<= 0.8)
	  {
	    //   Tagger: SSVHEM within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
	    if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.86318+(0.000801639*x))+(-1.64119e-06*(x*x)))+(2.59121e-10*(x*(x*x)))", 20.,670.);
	    if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.790364+(0.000463086*x))+(-4.35934e-07*(x*x)))+(-9.08296e-10*(x*(x*x)))", 20.,670.);
	    if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((0.935969+(0.0011402*x))+(-2.84645e-06*(x*x)))+(1.42654e-09*(x*(x*x)))", 20.,670.);
	  }
	if( algo ==1 &&  fabs(eta)> 0.8 &&  fabs(eta)<=1.6)
	  {
	    //   Tagger: SSVHEM within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
	    if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.958973+(-0.000269555*x))+(1.381e-06*(x*x)))+(-1.87744e-09*(x*(x*x)))", 20.,670.);
	    if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.865771+(-0.000279908*x))+(1.34144e-06*(x*x)))+(-1.75588e-09*(x*(x*x)))", 20.,670.);
	    if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.0522+(-0.000259296*x))+(1.42056e-06*(x*x)))+(-1.999e-09*(x*(x*x)))", 20.,670.);
	  }
	if( algo==1 &&  fabs(eta)>1.6  &&  fabs(eta)<=2.4)
	  {
	    //   Tagger: SSVHEM within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
	    if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.923033+(-0.000898227*x))+(4.74565e-06*(x*x)))+(-6.11053e-09*(x*(x*x)))", 20.,670.);
	    if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.828021+(-0.000731926*x))+(4.19613e-06*(x*x)))+(-5.81379e-09*(x*(x*x)))", 20.,670.);
	    if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.01812+(-0.00106483*x))+(5.29518e-06*(x*x)))+(-6.40728e-09*(x*(x*x)))", 20.,670.);
	  }
	
	if( algo== 2 &&  fabs(eta)> 0.0 &&  fabs(eta)<=2.4)
	  {
	    //   Tagger: SSVHPT within 30 < pt < 670 GeV, abs(eta) < 2.4, x = pt
	    if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.97409+(0.000646241*x))+(-2.86294e-06*(x*x)))+(2.79484e-09*(x*(x*x)))", 20.,670.);
	    if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.807222+(0.00103676*x))+(-3.6243e-06*(x*x)))+(3.17368e-09*(x*(x*x)))", 20.,670.);
	    if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.14091+(0.00025586*x))+(-2.10157e-06*(x*x)))+(2.41599e-09*(x*(x*x)))", 20.,670.);
	  }
	
	if( tmpSFl == NULL ){
	  std::cout << "NULL pointer returned... Function seems not to exist" << std::endl;
	  return 1.0;
	}
	else{
	  return tmpSFl->Eval(pt);
	}  
      }
      }
    }
  else if(mode=="database"){
    BinningPointByMap p;
    p.insert(BinningVariables::JetAbsEta,fabs(eta));
    p.insert(BinningVariables::JetEt,pt);
    switch(abs(flavor)) {
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
  else{
    std::cout << "Warning: UNKNOWN MODE: please check the spelling, 'database' or 'hardcoded' "<< std::endl;      ;
    return 0;
  }
}  



double btagPerfFWLiteInterface::getbEfficiency(int flavor, int algo, double pt, double eta) const {
  // small protection against large pt (shere we have no measurement).
  // the subject is a bit delicate, but I think it is better to use 
  // the efficiency for the last bin than to set it to 0.
  if(pt>249) pt=249;
  switch(abs(flavor)) {
    case 5:
      // this is not in the db and must be parametrized from OUR mc
      if(fabs(eta)<1.2 && algo==1) 
        return h_eff_ssvhem_b_brl_->GetBinContent(h_eff_ssvhem_b_brl_->FindBin(pt));
      else if(fabs(eta)>1.2 && algo==1)
        return h_eff_ssvhem_b_fwd_->GetBinContent(h_eff_ssvhem_b_fwd_->FindBin(pt));
      else if(fabs(eta)<1.2 && algo==2)
        return h_eff_ssvhpt_b_brl_->GetBinContent(h_eff_ssvhpt_b_brl_->FindBin(pt));
      else if(fabs(eta)>1.2 && algo==2)
        return h_eff_ssvhpt_b_fwd_->GetBinContent(h_eff_ssvhpt_b_fwd_->FindBin(pt));
      else 
        return 0.;
    case 4:
      // this is not in the db and must be parametrized from OUR mc
      if(fabs(eta)<1.2 && algo==1) 
        return h_eff_ssvhem_c_brl_->GetBinContent(h_eff_ssvhem_c_brl_->FindBin(pt));
      else if(fabs(eta)>1.2 && algo==1)
        return h_eff_ssvhem_c_fwd_->GetBinContent(h_eff_ssvhem_c_fwd_->FindBin(pt));
      else if(fabs(eta)<1.2 && algo==2)
        return h_eff_ssvhpt_c_brl_->GetBinContent(h_eff_ssvhpt_c_brl_->FindBin(pt));
      else if(fabs(eta)>1.2 && algo==2)
        return h_eff_ssvhpt_c_fwd_->GetBinContent(h_eff_ssvhpt_c_fwd_->FindBin(pt));
      else 
        return 0.;
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

