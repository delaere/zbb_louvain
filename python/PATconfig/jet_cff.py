import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.jetTools import *

#b-tagging algo and tag infos
btagInfo = [
     'impactParameterTagInfos'
     ,'secondaryVertexTagInfos'
     ,'softPFMuonsTagInfos'
     ,'softPFElectronsTagInfos'
     ,'inclusiveSecondaryVertexFinderTagInfos'
     ,'inclusiveSecondaryVertexFinderFilteredTagInfos'
     ]

btagdiscriminators = [
     'jetBProbabilityBJetTags'
     ,'jetProbabilityBJetTags'
     ,'trackCountingHighPurBJetTags'
     ,'trackCountingHighEffBJetTags'
     ,'simpleSecondaryVertexHighEffBJetTags'
     ,'simpleSecondaryVertexHighPurBJetTags'
     ,'combinedSecondaryVertexBJetTags'
     ,'combinedSecondaryVertexV1BJetTags'
     ,'softPFMuonBJetTags'
     ,'softPFElectronBJetTags'
     ,'simpleInclusiveSecondaryVertexHighEffBJetTags'
     ,'simpleInclusiveSecondaryVertexHighPurBJetTags'
     ,'doubleSecondaryVertexHighEffBJetTags'
     ,'combinedInclusiveSecondaryVertexBJetTags'
     ,'combinedInclusiveSecondaryVertexPositiveBJetTags'
     ,'combinedSecondaryVertexSoftPFLeptonV1BJetTags'
     ]

def setupPatJets (process, runOnMC):
     #genJets
     process.load('RecoJets.Configuration.RecoGenJets_cff')
     process.preJetSequence = cms.Sequence(process.genParticlesForJets * process.genParticlesForJetsNoNu * process.ak5GenJetsNoNu)
     #jets
     inputJetCorrLabel = ('AK5PFchs',['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual']) #data
     if runOnMC : inputJetCorrLabel = ('AK5PFchs',['L1FastJet', 'L2Relative', 'L3Absolute'])
     switchJetCollection(process,cms.InputTag('pfNoTau'), #==ak5PFJetsCHS
                         doJTA = True,
                         doBTagging = True,
                         jetCorrLabel = inputJetCorrLabel,
                         doType1MET = False,
                         genJetCollection=cms.InputTag("ak5GenJetsNoNu"),
                         doJetID = True,
                         jetIdLabel = "ak5",
                         btagInfo = btagInfo,
                         btagdiscriminators = btagdiscriminators
                         )
     #b-tagging mva
     process.load('CondCore.DBCommon.CondDBSetup_cfi')
     process.BTauMVAJetTagComputerRecord = cms.ESSource(
          'PoolDBESSource',
          process.CondDBSetup,
          timetype = cms.string('runnumber'),
          toGet = cms.VPSet(
            cms.PSet(
              record = cms.string('BTauGenericMVAJetTagComputerRcd'),
              tag = cms.string('MVAComputerContainer_Retrained53X_JetTags_v2')
            )
          ),
          connect = cms.string('frontier://FrontierProd/CMS_COND_PAT_000'),
          BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService')
     )
     process.es_prefer_BTauMVAJetTagComputerRecord = cms.ESPrefer('PoolDBESSource','BTauMVAJetTagComputerRecord')
     
     #PU JetID
     process.load("RecoJets.JetProducers.PileupJetID_cfi")
     process.pileupJetIdProducerChs.jets = cms.InputTag("patJets")
     process.pileupJetIdProducerChs.vertexes = cms.InputTag("goodPV")
     process.pileupJetIdProducerChs.residualsTxt = cms.FileInPath("RecoJets/JetProducers/data/mva_JetID_v1.weights.xml")
     process.puJetIdChs = process.pileupJetIdProducerChs.clone(
          produceJetIds = cms.bool(True),
          jetids = cms.InputTag(""),
          runMvas = cms.bool(False),
          algos = cms.VPSet(process.cutbased),
          )
     
     process.puJetMvaChs = process.pileupJetIdProducerChs.clone(
          produceJetIds = cms.bool(False),
          jetids = cms.InputTag("puJetIdChs"),
          runMvas = cms.bool(True),
          )

     process.puJetIdSqeuenceChs = cms.Sequence(process.puJetIdChs*process.puJetMvaChs)

     process.patJetsWithBeta = cms.EDProducer('JetBetaProducer',
                                              src = cms.InputTag("patJets"),
                                              primaryVertices = cms.InputTag("goodPV"),
                                              #puJetIdMVA = cms.InputTag("puJetMvaChs","fullDiscriminant"),
                                              #puJetIdFlag = cms.InputTag("puJetMvaChs","fullId"),
                                              #puJetIdentifier = cms.InputTag("puJetIdChs"),
                                              puJetIdMVA = cms.InputTag("pileupJetIdProducerChs","fullDiscriminant"),
                                              puJetIdFlag = cms.InputTag("pileupJetIdProducerChs","fullId"),
                                              puJetIdentifier = cms.InputTag("pileupJetIdProducerChs"),
                                              )

     #jet selection
     process.selectedPatJets.src = cms.InputTag("patJetsWithBeta")
     process.selectedPatJets.cut = 'pt > 15. & abs(eta) < 2.5 '

     #add everything to the sequence
     process.patDefaultSequence.replace(process.patJets,cms.Sequence(process.patJets*process.pileupJetIdProducerChs*process.patJetsWithBeta))
     #process.patDefaultSequence.replace(process.patJets,cms.Sequence(process.patJets*process.pileupJetIdProducerChs*process.puJetIdSqeuenceChs*process.patJetsWithBeta))
     
