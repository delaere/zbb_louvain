#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
// #include "DataFormats/Math/interface/deltaPhi.h"
// #include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
// #include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
// #include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
 #include "FWCore/Framework/interface/Frameworkfwd.h"
// #include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
 #include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
// #include "CommonTools/UtilAlgos/interface/TFileService.h"
// #include "FWCore/ServiceRegistry/interface/Service.h"
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
  std::vector<edm::InputTag> inputTagIsoDepElectrons_;
  std::vector<edm::InputTag> inputTagIsoValElectronsNoPFId_;
  const float R03;
  typedef std::vector< edm::Handle< edm::ValueMap<reco::IsoDeposit> > > IsoDepositMaps;
  typedef std::vector< edm::Handle< edm::ValueMap<double> > > IsoDepositVals;
};

ElectronIsolationEmbedder::ElectronIsolationEmbedder( const ParameterSet & cfg ):
  src_( cfg.getParameter<edm::InputTag>("src")),    
  rho_( cfg.getParameter<edm::InputTag>("rho")),   
  inputTagPFCandidateMap_( cfg.getParameter< edm::InputTag>("PFCandidateMap")),   
  inputTagIsoDepElectrons_ (cfg.getParameter< std::vector<edm::InputTag> >("IsoDepElectron")),
  inputTagIsoValElectronsNoPFId_ (cfg.getParameter< std::vector<edm::InputTag> >("IsoValElectronNoPF")),
  R03(0.3)
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
    pat::Electron & el = (*electronColl)[i];
    const IsoDepositVals * electronIsoVals = &electronIsoValPFId;

    // use the reference to the original gsfElectron from PAT::electron
    double charged =  (*(*electronIsoVals)[0])[el.originalObjectRef()];
    double photon = (*(*electronIsoVals)[1])[el.originalObjectRef()];
    double neutral = (*(*electronIsoVals)[2])[el.originalObjectRef()];

    // Effective area for 2011 data (Delta_R=0.3) (taken from https://twiki.cern.ch/twiki/bin/view/Main/HVVElectronId2012 )
    double A_eff_PH, A_eff_NH;
    if(abs(el.eta())<=1.0){A_eff_PH=0.081; A_eff_NH=0.024;}
    else if(abs(el.eta())>1.0 && abs(el.eta())<=1.479){A_eff_PH=0.084 ; A_eff_NH=0.037;}
    else if(abs(el.eta())>1.479 && abs(el.eta())<=2.0){A_eff_PH=0.048 ; A_eff_NH=0.037;}
    else if(abs(el.eta())>2.0 && abs(el.eta())<=2.2){A_eff_PH=0.089 ; A_eff_NH=0.023;}
    else if(abs(el.eta())>2.2 && abs(el.eta())<=2.3){A_eff_PH=0.092 ; A_eff_NH=0.023;}
    else if(abs(el.eta())>2.3 && abs(el.eta())<=2.4){A_eff_PH=0.097 ; A_eff_NH=0.021;}   
    else {A_eff_PH=0.11 ; A_eff_NH=0.021;}

    float PFIsoPUCorrected =(charged + max(photon - rho*A_eff_PH  , 0.) +  max(neutral - rho * A_eff_NH, 0.))/std::max(0.5, el.pt());
    el.addUserFloat("PFIsoPUCorrected", PFIsoPUCorrected);  
  }
  evt.put(electronColl);
}

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE( ElectronIsolationEmbedder );

