import FWCore.ParameterSet.Config as cms

def setupPatTaus (process):
    process.patDefaultSequence.replace(
        process.hpsPFTauDiscriminationByDecayModeFinding,
        process.ak5PFJetTracksAssociatorAtVertex*process.recoTauAK5PFJets08Region*process.recoTauPileUpVertices*process.pfRecoTauTagInfoProducer*process.ak5PFJetsLegacyHPSPiZeros*process.combinatoricRecoTaus*process.hpsSelectionDiscriminator*process.hpsPFTauProducerSansRefs*process.hpsPFTauProducer*process.hpsPFTauDiscriminationByDecayModeFinding
        )
