#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaCutBasedEleId.h"
#include <vector>
#include <TMath.h>

using namespace edm;
using namespace std;
using namespace reco;

class ElectronIsolationEmbedder : public edm::EDProducer {
public:
  ElectronIsolationEmbedder( const edm::ParameterSet & );   

private:
  void produce( edm::Event &, const edm::EventSetup & );
  InputTag src_, rho_;
  InputTag inputTagPFCandidateMap_;
  InputTag electronsInputTag_, conversionsInputTag_, beamSpotInputTag_, primaryVertexInputTag_;
  std::vector<edm::InputTag> inputTagIsoDepElectrons_;
  std::vector<edm::InputTag> inputTagIsoValElectronsNoPFId_;
  typedef std::vector< edm::Handle< edm::ValueMap<reco::IsoDeposit> > > IsoDepositMaps;
  typedef std::vector< edm::Handle< edm::ValueMap<double> > > IsoDepositVals;
};

ElectronIsolationEmbedder::ElectronIsolationEmbedder( const ParameterSet & cfg ):
  src_( cfg.getParameter<edm::InputTag>("src")),    
  rho_( cfg.getParameter<edm::InputTag>("rho")),   
  inputTagPFCandidateMap_( cfg.getParameter< edm::InputTag>("PFCandidateMap")),
  electronsInputTag_(cfg.getParameter< edm::InputTag>("gsfElectrons")),
  conversionsInputTag_(cfg.getParameter< edm::InputTag>("conversions")),
  beamSpotInputTag_(cfg.getParameter< edm::InputTag>("beamSpot")),
  primaryVertexInputTag_(cfg.getParameter< edm::InputTag>("primaryVertex")),
  inputTagIsoDepElectrons_ (cfg.getParameter< std::vector<edm::InputTag> >("IsoDepElectron")),
  inputTagIsoValElectronsNoPFId_ (cfg.getParameter< std::vector<edm::InputTag> >("IsoValElectronNoPF"))
{
  produces<std::vector<pat::Electron> >();
}

void ElectronIsolationEmbedder::produce( Event & evt, const EventSetup & ) {

  Handle<double> rhoHandle;
  evt.getByLabel(rho_,rhoHandle);
  double rho = *rhoHandle; 

  Handle<vector<pat::Electron>  > electrons;
  evt.getByLabel(src_, electrons);
  auto_ptr<vector<pat::Electron> > electronColl( new vector<pat::Electron> (*electrons) );

  edm::Handle<reco::GsfElectronCollection> els_h;
  evt.getByLabel(electronsInputTag_, els_h);

  edm::Handle<reco::ConversionCollection> conversions_h;
  evt.getByLabel(conversionsInputTag_, conversions_h);

  edm ::Handle<reco::BeamSpot> beamspot_h;
  evt.getByLabel(beamSpotInputTag_, beamspot_h);
  const reco::BeamSpot &beamSpot = *(beamspot_h.product());

  edm ::Handle<reco::VertexCollection> vtx_h;
  evt.getByLabel(primaryVertexInputTag_, vtx_h);

  // get the iso deposits. 3 (charged hadrons, photons, neutral hadrons)
  unsigned nTypes=3;
  IsoDepositMaps electronIsoDep(nTypes);
  for (size_t j = 0; j<inputTagIsoDepElectrons_.size(); ++j) {
    evt.getByLabel(inputTagIsoDepElectrons_[j], electronIsoDep[j]);
  }

  IsoDepositVals electronIsoValPFId(nTypes);
  for (size_t j = 0; j<inputTagIsoValElectronsNoPFId_.size(); ++j) {
    evt.getByLabel(inputTagIsoValElectronsNoPFId_[j], electronIsoValPFId[j]);
  }

  for (unsigned int i = 0; i< electronColl->size();++i){      
    // get the electron and iso deposits
    pat::Electron & el = (*electronColl)[i];
    float eta = el.superCluster()->eta();
    reco::GsfElectronRef gsfele(els_h, el.originalObjectRef().key());
    const IsoDepositVals * electronIsoVals = &electronIsoValPFId;

    // use the reference to the original gsfElectron from PAT::electron
    double charged = (*(*electronIsoVals)[0])[el.originalObjectRef()];
    double photon  = (*(*electronIsoVals)[1])[el.originalObjectRef()];
    double neutral = (*(*electronIsoVals)[2])[el.originalObjectRef()];

    // introduce the new definition of the medium WP, approved on June 1st.
    LogDebug("ElectronIsolationEmbedder") << "WP inputs: " << charged << " " << photon << " " << neutral << " " << rho;
    bool medium = EgammaCutBasedEleId::PassWP(EgammaCutBasedEleId::MEDIUM, gsfele, conversions_h, beamSpot, vtx_h, charged, photon, neutral, rho);
    el.addUserInt("MediumWP", medium);
    LogDebug("ElectronIsolationEmbedder") << "MediumWP: " << medium;

    // Effective area for 2012 data (Delta_R=0.3) (taken from https://twiki.cern.ch/twiki/bin/view/CMS/EgammaEARhoCorrection#Isolation_cone_R_0_3)
    double  A_eff_PHNH;
    if     (abs(eta)<=1.0)                   { A_eff_PHNH=0.13; }
    else if(abs(eta)>1.0 && abs(eta)<=1.479) { A_eff_PHNH=0.14; }
    else if(abs(eta)>1.479 && abs(eta)<=2.0) { A_eff_PHNH=0.07; }
    else if(abs(eta)>2.0 && abs(eta)<=2.2)   { A_eff_PHNH=0.09; }
    else if(abs(eta)>2.2 && abs(eta)<=2.3)   { A_eff_PHNH=0.11; }
    else if(abs(eta)>2.3 && abs(eta)<=2.4)   { A_eff_PHNH=0.11; }   
    else                                     { A_eff_PHNH=0.14; }

    LogDebug("ElectronIsolationEmbedder") << "Effective area, PH+NH: " << A_eff_PHNH ;
    float PFIsoPUCorrected =(charged + max(photon+neutral - rho*A_eff_PHNH  , 0.))/std::max(0.5, el.pt());
    el.addUserFloat("PFIsoPUCorrected", PFIsoPUCorrected);  
    LogDebug("ElectronIsolationEmbedder") << "PFIsoPUCorrected=" << PFIsoPUCorrected;

    // Effective area for 2012 MC (as in data). (taken from https://twiki.cern.ch/twiki/bin/view/CMS/EgammaEARhoCorrection#Isolation_cone_R_0_3)
    if     (abs(eta)<=1.0)                   { A_eff_PHNH=0.13; }
    else if(abs(eta)>1.0 && abs(eta)<=1.479) { A_eff_PHNH=0.14; }
    else if(abs(eta)>1.479 && abs(eta)<=2.0) { A_eff_PHNH=0.07; }
    else if(abs(eta)>2.0 && abs(eta)<=2.2)   { A_eff_PHNH=0.09; }
    else if(abs(eta)>2.2 && abs(eta)<=2.3)   { A_eff_PHNH=0.11; }
    else if(abs(eta)>2.3 && abs(eta)<=2.4)   { A_eff_PHNH=0.11; }   
    else                                     { A_eff_PHNH=0.14; }

    LogDebug("ElectronIsolationEmbedder") << "Effective area for MC, PH and NH: " << A_eff_PHNH ;
    float PFIsoPUCorrectedMC = (charged + max(photon+neutral - rho*A_eff_PHNH  , 0.))/std::max(0.5, el.pt());
    el.addUserFloat("PFIsoPUCorrectedMC", PFIsoPUCorrectedMC);
    LogDebug("ElectronIsolationEmbedder") << "PFIsoPUCorrectedMC=" << PFIsoPUCorrectedMC;  
  
  }
  evt.put(electronColl);
}

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE( ElectronIsolationEmbedder );

