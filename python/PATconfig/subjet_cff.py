import FWCore.ParameterSet.Config as cms
from CommonTools.ParticleFlow.pfPileUp_cfi import *
from CommonTools.ParticleFlow.TopProjectors.pfNoPileUp_cfi import *
#from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets
#from RecoJets.JetAssociationProducers.ak5JTA_cff import *
#from RecoBTag.Configuration.RecoBTag_cff import * # btagging sequence
    
def setupPatSubJets (process, runOnMC):
    process.jetSubstructuresSequence = cms.Sequence() #??
    process.goodOfflinePrimaryVerticesForSubJets = process.goodPV.clone()

    #??
    process.pfPileUpForSubJets = pfPileUp.clone(
        checkClosestZVertex = False,
        PFCandidates = 'particleFlow',
        Vertices = 'goodOfflinePrimaryVerticesForSubJets'
        )
    #??
    process.pfNoPileUpForSubJets = pfNoPileUp.clone(
        topCollection = 'pfPileUpForSubJets',
        bottomCollection = 'particleFlow'
        )
    
    process.jetSubstructuresSequence += process.goodOfflinePrimaryVerticesForSubJets
    process.jetSubstructuresSequence += process.pfPileUpForSubJets
    process.jetSubstructuresSequence += process.pfNoPileUpForSubJets

    #??
    pfNoPileUpSrc = 'pfNoPileUpForSubJets'
    #### Adding CA8 jets and CA8 pruned jets
    # load("ExoDiBosonResonances.PATtupleProduction.PAT_ca8jets_cff")
    process.ca8PFJetsCHS.src = pfNoPileUpSrc
    process.ca8PFJetsCHSpruned.src = pfNoPileUpSrc
    
    process.selectedPatJetsCA8CHS.cut = cms.string('pt > 25.0 && abs(eta) < 2.4 && getPFConstituents().size > 1') #to change???
