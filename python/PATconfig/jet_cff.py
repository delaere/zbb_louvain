import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.jetTools import *

def setupPatJets (process, runOnMC):
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
     #jets
     inputJetCorrLabel = ('AK5PFchs',['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual']) #data
     if runOnMC : inputJetCorrLabel = ('AK5PFchs',['L1FastJet', 'L2Relative', 'L3Absolute'])
     switchJetCollection(process,cms.InputTag('pfNoTau'), #==ak5PFJetsCHS
                         doJTA = True,
                         doBTagging = True,
                         jetCorrLabel = inputJetCorrLabel,
                         doType1MET = False,
                         genJetCollection=cms.InputTag("ak5GenJets"),
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
     process.load("CMGTools.External.pujetidsequence_cff")
     process.puJetIdChs.jets = cms.InputTag("patJets")
     process.puJetMvaChs.jets = cms.InputTag("patJets")
     process.puJetMvaChs.algos[0].tmvaWeights = cms.string('CMGTools/External/data/TMVAClassificationCategory_JetID_53X_chs_Dec2012.weights.xml')

     process.patJetsWithBeta = cms.EDProducer('JetBetaProducer',
                                              src = cms.InputTag("patJets"),
                                              primaryVertices = cms.InputTag("goodPV"),
                                              puJetIdMVA = cms.InputTag("puJetMvaChs","fullDiscriminant"),
                                              puJetIdFlag = cms.InputTag("puJetMvaChs","fullId"),
                                              puJetIdentifier = cms.InputTag("puJetIdChs"),
                                              )

     #jet selection
     process.selectedPatJets.src = cms.InputTag("patJetsWithBeta")
     process.selectedPatJets.cut = 'pt > 15. & abs(eta) < 2.5 '

     #add everything to the sequence
     process.patDefaultSequence.replace(process.patJets,cms.Sequence(process.patJets+process.puJetIdSqeuenceChs+process.patJetsWithBeta))
