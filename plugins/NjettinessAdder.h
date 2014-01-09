/* """ Imported from ExoDiBosonResonances/PATtupleProduction/plugins/ """ */

#ifndef UserCode_zbb_louvain_NjettinessAdder_h
#define UserCode_zbb_louvain_NjettinessAdder_h

#include <memory>
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

class NjettinessAdder : public edm::EDProducer { 
public:
  explicit NjettinessAdder(const edm::ParameterSet& iConfig) :
    src_(iConfig.getParameter<edm::InputTag>("src")),
    cone_(iConfig.getParameter<double>("cone"))
    {
    produces<std::vector<pat::Jet> >();
  }
  
  virtual ~NjettinessAdder() {}
  
  void produce(edm::Event & iEvent, const edm::EventSetup & iSetup) ;
  float getTau(int num,edm::Ptr<pat::Jet> object) const;

private:	
  edm::InputTag src_ ;
  double cone_ ;
};


#endif
