#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
//#include "FWCore/Utilities/interface/EDMException.h"
#include <vector>
#include <TMath.h>

using namespace edm;
using namespace std;
using namespace reco;

class MuonIsolationEmbedder : public edm::EDProducer {
public:
  MuonIsolationEmbedder( const edm::ParameterSet & );   

private:
  void produce( edm::Event &, const edm::EventSetup & );
  InputTag src_, rho_;
  const float R04;
};

MuonIsolationEmbedder::MuonIsolationEmbedder( const ParameterSet & cfg ):
  src_( cfg.getParameter<InputTag>("src") ),
  rho_( cfg.getParameter<edm::InputTag>("rho")),
  R04(0.4)
{
  produces<std::vector<pat::Muon> >();
}

void MuonIsolationEmbedder::produce( Event & evt, const EventSetup & ) {

  Handle<vector<pat::Muon>  > muons;
  evt.getByLabel(src_,muons);

  Handle<double> rhoHandle;
  evt.getByLabel(rho_,rhoHandle);
  double rho = *rhoHandle; 
  float PUEnergyInCone = (TMath::Pi()) * R04 * R04 * rho;  

  auto_ptr<vector<pat::Muon> > muonColl( new vector<pat::Muon> (*muons) );
  
  for (unsigned int i = 0; i< muonColl->size();++i){
    pat::Muon & m = (*muonColl)[i];

    // pf Isolation variables
    double chargedHadronIso = m.pfIsolationR04().sumChargedHadronPt;
    double chargedHadronIsoPU = m.pfIsolationR04().sumPUPt;  
    double neutralHadronIso  = m.pfIsolationR04().sumNeutralHadronEt;
    double photonIso  = m.pfIsolationR04().sumPhotonEt;

    // OPTION 1: DeltaBeta corrections for iosolation
    float RelativeIsolationDBetaCorr = (chargedHadronIso + std::max(photonIso+neutralHadronIso - 0.5*chargedHadronIsoPU,0.))
                                        /std::max(0.5, m.pt());   
    m.addUserFloat("RelativePFIsolationDBetaCorr",RelativeIsolationDBetaCorr);

    // OPTION 2: rho correctios BUT without Effective area.
    neutralHadronIso =std::max(0., neutralHadronIso-PUEnergyInCone);
    photonIso =std::max(0., photonIso-PUEnergyInCone);
    float RelativeIsolationRhoCorr   = (chargedHadronIso+neutralHadronIso+photonIso)/std::max(0.5, m.pt());
    m.addUserFloat("RelativeIsolationRhoCorr",RelativeIsolationRhoCorr);

  }
  evt.put( muonColl);
}

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE( MuonIsolationEmbedder );

