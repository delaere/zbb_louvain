
// system includes
#include <vector>

// root include files
#include "TH1F.h"
#include "TFile.h"

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include <SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h>

class pileupDistInMC : public edm::EDAnalyzer {
   public:
       explicit pileupDistInMC(const edm::ParameterSet& iConfig);
       ~pileupDistInMC() {}
   private:
       virtual void beginJob();
       virtual void analyze(const edm::Event&, const edm::EventSetup&);
       TH1F* histogram;
       edm::InputTag PUIlabel;
       edm::Handle<std::vector<PileupSummaryInfo> > handle;
};

pileupDistInMC::pileupDistInMC(const edm::ParameterSet& iConfig) {
  PUIlabel = iConfig.getParameter<edm::InputTag>("PileUpSummaryLabel"); 
}

void pileupDistInMC::beginJob() {
  // create output
  edm::Service<TFileService> fileService;
  histogram = fileService->make<TH1F>("pileup","pileup",50,0,50);
}

void pileupDistInMC::analyze(const edm::Event& event, const edm::EventSetup&) {
  // get summary info
  event.getByLabel(PUIlabel,handle);
  const std::vector<PileupSummaryInfo>* pui = handle.product();
  int n = -1;
  // find the right crossing
  for(std::vector<PileupSummaryInfo>::const_iterator pu = pui->begin(); pu!=pui->end(); ++pu) {
    if(pu->getBunchCrossing()==0) {
      n = pu->getPU_NumInteractions();
      break;
    }
  }
  // fill the histogram
  if(n>=0) histogram->Fill(n);
}

