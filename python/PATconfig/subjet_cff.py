import FWCore.ParameterSet.Config as cms
from RecoJets.JetProducers.ak5PFJets_cfi import ak5PFJets
from RecoJets.JetProducers.ak5PFJetsPruned_cfi import ak5PFJetsPruned
from PhysicsTools.PatAlgos.tools.jetTools import *
#from RecoJets.Configuration.RecoGenJets_cff import ak7GenJetsNoNu, ak7GenJets
from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters
from UserCode.zbb_louvain.PATconfig.jet_cff import btagInfo, btagdiscriminators

def setupPatSubJets (process, runOnMC):
    #CA8 jets
    process.ca8PFJetsCHS = ak5PFJets.clone(
        src = 'pfNoPileUp',
        jetPtMin = cms.double(10.0),
        doAreaFastjet = cms.bool(True),
        rParam = cms.double(0.8),
        jetAlgorithm = cms.string("CambridgeAachen"),
        )

    process.ca8PFJetsCHSpruned = ak5PFJetsPruned.clone( #Pruned CA8 jets
        src = 'pfNoPileUp',
        jetPtMin = cms.double(10.0),
        doAreaFastjet = cms.bool(True),
        rParam = cms.double(0.8),
        jetAlgorithm = cms.string("CambridgeAachen"),
        )

    #Add to PAT
    inputJetCorrLabel = ('AK7PFchs',['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual']) #data
    if runOnMC : inputJetCorrLabel = ('AK7PFchs',['L1FastJet', 'L2Relative', 'L3Absolute'])

    addJetCollection(process,
                     cms.InputTag('ca8PFJetsCHS'),
                     'CA8', 'CHS',
                     doJTA=True,
                     doBTagging=True,
                     jetCorrLabel=inputJetCorrLabel,
                     doType1MET=False,
                     genJetCollection = cms.InputTag("ca8GenJetsNoNu"), #Why NoNu
                     doJetID = True,
                     btagInfo = btagInfo,
                     btagdiscriminators = btagdiscriminators
                     )
    process.patJetsCA8CHS.embedCaloTowers = False
    process.patJetsCA8CHS.embedPFCandidates = False
    process.selectedPatJetsCA8CHS.cut = 'pt > 15. & abs(eta) < 2.5' #harder cut?
    
    process.puJetIdChsCA8 = process.puJetIdChs.clone() #configure beta/beta* for CA8 jets
    process.puJetMvaChsCA8 = process.puJetMvaChs.clone()
    
    process.puJetIdChsCA8.jets = cms.InputTag("patJetsCA8CHS")
    process.puJetMvaChsCA8.jets = cms.InputTag("patJetsCA8CHS")
    process.puJetMvaChsCA8.jetids = cms.InputTag("puJetIdChsCA8")
    
    process.patJetsCA8CHSWithBeta = cms.EDProducer('JetBetaProducer',
                                                               src = cms.InputTag("patJetsCA8CHS"),
                                                               primaryVertices = cms.InputTag("goodPV"),
                                                               puJetIdMVA = cms.InputTag("puJetMvaChsCA8","fullDiscriminant"),
                                                               puJetIdFlag = cms.InputTag("puJetMvaChsCA8","fullId"),
                                                               puJetIdentifier = cms.InputTag("puJetIdChsCA8"),
                                                               )
    process.selectedPatJetsCA8CHS.src = cms.InputTag("patJetsCA8CHSWithBeta")

                            
    addJetCollection(process, #pruned CA8 jets to PAT
                     cms.InputTag('ca8PFJetsCHSpruned'),
                     'CA8', 'CHSpruned',
                     doJTA=True,
                     doBTagging=True,
                     jetCorrLabel=inputJetCorrLabel,
                     doType1MET=False,
                     genJetCollection = cms.InputTag("ca8GenJetsNoNu"),
                     doJetID = True,
                     btagInfo = btagInfo,
                     btagdiscriminators = btagdiscriminators
                     )
    process.patJetsCA8CHSpruned.embedCaloTowers = False
    process.patJetsCA8CHSpruned.embedPFCandidates = False
    process.selectedPatJetsCA8CHSpruned.cut = 'pt > 15. & abs(eta) < 2.5' #harder cut?

    #subjets
    inputJetCorrLabel = ('AK5PFchs',['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual']) #data
    if runOnMC : inputJetCorrLabel = ('AK5PFchs',['L1FastJet', 'L2Relative', 'L3Absolute'])
    addJetCollection(process,
                     cms.InputTag('ca8PFJetsCHSpruned','SubJets'),
                     'CA8PrunedSubjets', 'PF',
                     doJTA=True,
                     doBTagging=True,
                     jetCorrLabel=inputJetCorrLabel,
                     doType1MET=False,
                     genJetCollection=cms.InputTag('ca8GenJetsNoNuPruned','SubJets'),
                     doJetID=True,
                     btagInfo = btagInfo,
                     btagdiscriminators = btagdiscriminators
                     )
    process.patJetsCA8PrunedSubjetsPF.addJetCharge = False
    process.patJetsCA8PrunedSubjetsPF.embedCaloTowers = False
    process.patJetsCA8PrunedSubjetsPF.embedPFCandidates = False

    #CA8 genJets
    process.ca8GenJetsNoNu = process.ak7GenJetsNoNu.clone()
    process.ca8GenJetsNoNu.rParam = 0.8
    process.ca8GenJetsNoNu.jetAlgorithm = "CambridgeAachen"

    process.ca8GenJets = process.ak7GenJets.clone()
    process.ca8GenJets.rParam = 0.8
    process.ca8GenJets.jetAlgorithm = "CambridgeAachen"

    process.ca8GenJetsNoNuPruned = process.ca8GenJetsNoNu.clone( #Pruned gen jets
        SubJetParameters,
        usePruning = cms.bool(True),
        useExplicitGhosts = cms.bool(True),
        writeCompound = cms.bool(True),
        jetCollInstanceName=cms.string("SubJets")
        )

    process.ca8GenJetsPruned = process.ca8GenJets.clone( #Pruned gen jets
        SubJetParameters,
        usePruning = cms.bool(True),
        useExplicitGhosts = cms.bool(True),
        writeCompound = cms.bool(True),
        jetCollInstanceName=cms.string("SubJets")
        )

    #Nsubjettiness
    process.selectedPatJetsCA8CHSwithNsub = cms.EDProducer("NjettinessAdder",
                                                           src=cms.InputTag("selectedPatJetsCA8CHS"),
                                                           cone=cms.double(0.8)
                                                           )

    #BoostedJetMerger: map properly pat fat jets and pat subjets
    process.selectedPatJetsCA8CHSPrunedPacked = cms.EDProducer("BoostedJetMerger",
                                                          jetSrc=cms.InputTag("selectedPatJetsCA8CHSpruned"),
                                                          subjetSrc=cms.InputTag("selectedPatJetsCA8PrunedSubjetsPF")
                                                          )

    #Sequences
    process.jetMCSequenceCA8CHS = cms.Sequence(
        process.ca8GenJetsNoNu *
        process.ca8GenJets *
        process.ca8GenJetsNoNuPruned *
        process.ca8GenJetsPruned
        )

    process.preSequenceCA8CHS = cms.Sequence(
        process.ca8PFJetsCHS +
        process.ca8PFJetsCHSpruned
        )
    if runOnMC : process.preSequenceCA8CHS += cms.Sequence(process.jetMCSequenceCA8CHS)

    process.patDefaultSequence.replace(
        process.selectedPatJetsCA8CHS,
        cms.Sequence(process.puJetIdChsCA8 * process.puJetMvaChsCA8 * process.patJetsCA8CHSWithBeta * process.selectedPatJetsCA8CHS * process.selectedPatJetsCA8CHSwithNsub)
        )
     

