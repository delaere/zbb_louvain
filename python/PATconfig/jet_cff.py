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
     
