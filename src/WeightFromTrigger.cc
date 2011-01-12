// -*- C++ -*-
//
// Package:    WeightFromTrigger
// Class:      WeightFromTrigger
// 
/**\class WeightFromTrigger WeightFromTrigger.cc UserCode/zbb_louvain/src/WeightFromTrigger.cc

 Description: Simple code to extract the event weight from the trigger prescales

 Implementation:
     The weight is obtained by looping on the triggers and is added to the event.
*/
//
// Original Author:  Christophe Delaere,354 2-003,+41227674739,
//         Created:  Sat Nov 20 15:25:22 CET 2010
// $Id: WeightFromTrigger.cc,v 1.1 2011/01/11 15:57:42 delaer Exp $
//
//


// system include files
#include <memory>
#include <vector>
#include <algorithm>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <FWCore/MessageLogger/interface/MessageLogger.h>

#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/Common/interface/TriggerResults.h"


//
// class declaration
//

class WeightFromTrigger : public edm::EDProducer {
   public:
      explicit WeightFromTrigger(const edm::ParameterSet&);
      ~WeightFromTrigger();

   private:
      virtual void beginJob() ;
      virtual void beginRun(edm::Run&, const edm::EventSetup&);
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
      edm::InputTag HLTLabel_;
      std::vector<std::string> triggerNames_; // name of the algorithms selected by our analysis
      std::vector<unsigned int> triggerIndices_; // index of the algorithms selected by our analysis
      HLTConfigProvider hltConfig_;        // to get configuration for L1s/Pre
      bool useCombinedPrescales_; // switch between HLT only and L1*HLT prescales
      bool useAllTriggers_; // if no trigger names are provided, use all triggers to find event weight

};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
WeightFromTrigger::WeightFromTrigger(const edm::ParameterSet& iConfig):hltConfig_()
{
  // initialization
  HLTLabel_             = iConfig.getParameter<edm::InputTag>("HLTLabel");
  useCombinedPrescales_ = iConfig.getParameter<bool>("UseCombinedPrescales");
  triggerNames_         = iConfig.getParameter< std::vector<std::string> > ("TriggerNames");
  useAllTriggers_       = (triggerNames_.size()==0);
  
  // registration of the product: weight and subset of trigger bits
  produces<float>("WeightFromTrigger");
  produces<std::vector<bool> >("SelectedTriggers");

}


WeightFromTrigger::~WeightFromTrigger()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
WeightFromTrigger::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   // load trigger information
   edm::Handle<edm::TriggerResults> hltTriggerResultHandle;
   iEvent.getByLabel(HLTLabel_, hltTriggerResultHandle);
   unsigned int hltCount(0);
   if(hltTriggerResultHandle.isValid()) {
     hltCount = hltTriggerResultHandle->size();
   } else {
     edm::LogError("MyAnalyzer") << "invalid handle for HLT TriggerResults" << std::endl;
   }

   // loop over the triggers and record prescale
   unsigned int minimalPrescale(10000);
   unsigned int prescale(0);
   bool bit(true);
   std::pair<int,int> prescalepair;
   std::vector<bool>  triggerSubset;
   for(unsigned int itrig = 0; itrig < triggerNames_.size(); ++itrig) {
    if(triggerIndices_[itrig]!=2048) {
     // check trigger response
     bit = hltTriggerResultHandle->accept(triggerIndices_[itrig]);
     triggerSubset.push_back(bit);
     if(bit) {
       // look at the prescale
       int prescaleset = hltConfig_.prescaleSet(iEvent,iSetup);
       if(prescaleset!=-1) {
         prescalepair = hltConfig_.prescaleValues(iEvent,iSetup,triggerNames_[itrig]);
	 if((useCombinedPrescales_ && prescalepair.first<0) || prescalepair.second<0) {
	   edm::LogWarning("MyAnalyzer") << " Unable to get prescale from event for trigger " << triggerNames_[itrig] << " :" 
	                               << prescalepair.first << ", " << prescalepair.second;
	 }
	 prescale = useCombinedPrescales_ ? prescalepair.first*prescalepair.second : prescalepair.second;
	 minimalPrescale = minimalPrescale <  prescale ? minimalPrescale : prescale;
       } else {
         edm::LogError("MyAnalyzer") << " Unable to get prescale set from event. Check that L1 data products are present.";
       }
     }
    } else {
     // that trigger is presently not in the menu
     triggerSubset.push_back(false);
    }
   }

   // put the result in the event
   std::auto_ptr<float> pOut(new float(minimalPrescale));
   iEvent.put(pOut, "WeightFromTrigger");
   std::auto_ptr<std::vector<bool> > pOut2(new std::vector<bool> (triggerSubset));
   iEvent.put(pOut2, "SelectedTriggers");

}

// ------------ method called once each run just before starting event loop  ------------
void 
WeightFromTrigger::beginRun(edm::Run& iRun, edm::EventSetup const& iSetup)
{
   //HLT names
   std::vector<std::string>  hlNames;
   bool changed (true);
   if (hltConfig_.init(iRun,iSetup,HLTLabel_.process(),changed)) {
     if (changed) {
       hlNames = hltConfig_.triggerNames();
     }
   } else {
     edm::LogError("MyAnalyzer") << " HLT config extraction failure with process name " << HLTLabel_.process();
   }
   if(useAllTriggers_) triggerNames_ = hlNames;

   //HLT indices
   triggerIndices_.clear();
   for(unsigned int itrig = 0; itrig < triggerNames_.size(); ++itrig) {
     if(find(hlNames.begin(),hlNames.end(),triggerNames_[itrig])!=hlNames.end())
       triggerIndices_.push_back(hltConfig_.triggerIndex(triggerNames_[itrig]));
     else
       triggerIndices_.push_back(2048);
   }

   // text (debug) output
   int i=0;
   for(std::vector<std::string>::const_iterator it = hlNames.begin(); it<hlNames.end();++it) {
     std::cout << (i++) << " = " << (*it) << std::endl;
   } 

}

// ------------ method called once each job just before starting event loop  ------------
void 
WeightFromTrigger::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
WeightFromTrigger::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(WeightFromTrigger);
