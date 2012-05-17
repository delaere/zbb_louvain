// -*- C++ -*-
//
// Package:    JetBetaProducer
// Class:      JetBetaProducer
// 
/**\class JetBetaProducer JetBetaProducer.cc UserCode/JetBetaProducer/src/JetBetaProducer.cc

 Description: add beta and beta* to the pat::jet (pflow)

 Implementation:
     Computes the beta and beta* for pflow jets and add the information as UserFloat to the pat::jet.
     The input MUST be a particle flow jet.
     The output is a clone of the input collection, with additional data added.
*/
//
// Original Author:  Christophe Delaere
//         Created:  Wed May 16 21:12:25 CEST 2012
// $Id: JetBetaProducer.cc,v 1.1 2012/05/16 22:33:05 delaer Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/Framework/interface/Event.h"

#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "FWCore/Utilities/interface/EDMException.h"


//
// class declaration
//

class JetBetaProducer : public edm::EDProducer {
   public:
      explicit JetBetaProducer(const edm::ParameterSet&);
      ~JetBetaProducer() {}

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() {}
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() {}
      
      float beta(pat::Jet const&, edm::Handle<reco::VertexCollection> const&) const;
      float betaStar(pat::Jet const&, edm::Handle<reco::VertexCollection> const&) const;

      // ----------member data ---------------------------
      edm::InputTag src_, primaryVertices_;
};

JetBetaProducer::JetBetaProducer(const edm::ParameterSet& iConfig):
   src_( iConfig.getParameter<edm::InputTag>( "src" ) ),
   primaryVertices_(iConfig.getParameter<edm::InputTag>( "primaryVertices" ) )
{
   produces<std::vector<pat::Jet> >();
}

//
// member functions
//
using namespace edm;
using namespace std;
using namespace reco;

// ------------ method called to produce the beta  ------------
float
JetBetaProducer::beta(pat::Jet const& jet, Handle<VertexCollection> const& vertices) const
{
  // definition of beta: ratio of charged pT from first vertex over the sum of all the charged pT in jet. 

  LogDebug("JetBetaProducer") << "Computing beta for jet with Pt " << jet.pt()
                              << " in an event with " << vertices->size() << " vertices."; 

  // by definition, 0 if there is no primary vertex.
  if(vertices->size()<1) return 0.;
  // loop over the tracks making the PV, and store the keys
  list<int> trackrefs;
  const reco::Vertex pv = vertices.product()->operator[](0);
  for( reco::Vertex::trackRef_iterator tk = pv.tracks_begin(); tk < pv.tracks_end(); ++tk) {
    trackrefs.push_back(tk->key());
    LogDebug("JetBetaProducer") << "Key from PV: " << trackrefs.back();
  }
  // now loop over the jet charged constituents, and count pt
  float ptsum = 0.;
  float ptsumall = 0.;
  const std::vector< reco::PFCandidatePtr > constituents = jet.getPFConstituents();
  for(std::vector< reco::PFCandidatePtr >::const_iterator jetconst = constituents.begin(); jetconst < constituents.end(); ++jetconst) {
    if((*jetconst)->trackRef().isNull()) continue;
    list<int>::iterator found = find(trackrefs.begin(), trackrefs.end(), (*jetconst)->trackRef().key());
    LogDebug("JetBetaProducer") << "found charged component in jet with key " << (*jetconst)->trackRef().key() << ". Found = " << (found!=trackrefs.end());
    if(found!=trackrefs.end()) {
      ptsum += (*jetconst)->pt();
    }
    ptsumall += (*jetconst)->pt();
    LogDebug("JetBetaProducer") << "ptsum= " << ptsum << " ptsumall= " << ptsumall << " ratio= " << ptsum/ptsumall;
  }
  if(ptsumall<0.001) // non-null: 0.001 is much lower than any pt cut at reco level.
    return -1.;
  return ptsum/ptsumall;
  
}

// ------------ method called to produce the beta*  -----------
float
JetBetaProducer::betaStar(pat::Jet const& jet, Handle<VertexCollection> const& vertices) const
{
  // defined as the ratio of charged pT coming from good PU vertices over the sum of all charged pT in jet. 

  LogDebug("JetBetaProducer") << "Computing beta* for jet with Pt " << jet.pt()
                              << " in an event with " << vertices->size() << " vertices."; 

  // by definition, 0 if there is no PU vertex.
  if(vertices->size()<2) return 0.;
  // loop over the tracks making the PU vertices, and store the keys
  list<int> trackrefs;
  for(VertexCollection::const_iterator PUvertex = vertices->begin()+1; PUvertex<vertices->end(); ++PUvertex) {
    for( reco::Vertex::trackRef_iterator tk = PUvertex->tracks_begin(); tk < PUvertex->tracks_end(); ++tk) {
      trackrefs.push_back(tk->key());
      LogDebug("JetBetaProducer") << "Key from PU: " << trackrefs.back();
    }
  }
  // now loop over the jet charged constituents, and count pt
  float ptsum = 0.;
  float ptsumall = 0.;
  const std::vector< reco::PFCandidatePtr > constituents = jet.getPFConstituents();
  for(std::vector< reco::PFCandidatePtr >::const_iterator jetconst = constituents.begin(); jetconst < constituents.end(); ++jetconst) {
    if((*jetconst)->trackRef().isNull()) continue;
    list<int>::iterator found = find(trackrefs.begin(), trackrefs.end(), (*jetconst)->trackRef().key());
    LogDebug("JetBetaProducer") << "found charged component in jet with key " << (*jetconst)->trackRef().key() << ". Found = " << (found!=trackrefs.end());
    if(found!=trackrefs.end()) ptsum += (*jetconst)->pt();
    ptsumall += (*jetconst)->pt();
    LogDebug("JetBetaProducer") << "ptsum= " << ptsum << " ptsumall= " << ptsumall << " ratio= " << ptsum/ptsumall;
  }
  if(ptsumall<0.001) // non-null: 0.001 is much lower than any pt cut at reco level.
    return -1.;
  return ptsum/ptsumall;

}

// ------------ method called to produce the data  ------------
void
JetBetaProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;

  Handle<vector<pat::Jet>  > jets;
  iEvent.getByLabel(src_,jets);

  Handle<VertexCollection> primaryVertices;  // Collection of primary Vertices
  iEvent.getByLabel(primaryVertices_, primaryVertices);

  auto_ptr<vector<pat::Jet> > jetColl( new vector<pat::Jet> (*jets) );
  for (unsigned int i = 0; i< jetColl->size();++i){
    pat::Jet & j = (*jetColl)[i];
    if ( !j.isPFJet() )
      throw cms::Exception("InvalidInput") 
         << "Input pat::Jet is not of PF-type !!\n";
    j.addUserFloat("beta",beta(j,primaryVertices));
    j.addUserFloat("betaStar",betaStar(j,primaryVertices));
    LogDebug("JetBetaProducerSummary") << "jet Pt = " << j.pt() << " beta= " << j.userFloat("beta") << " beta*= " << j.userFloat("betaStar");
  }
  iEvent.put(jetColl);
 
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetBetaProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetBetaProducer);
