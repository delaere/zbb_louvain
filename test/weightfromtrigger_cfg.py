import FWCore.ParameterSet.Config as cms

process = cms.Process("Analysis")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/data/Run2010B/Mu/RECO/DiLeptonMu-Dec22Skim_v2/0040/88B29906-EB11-E011-B75A-90E6BA442F32.root'
    )
)

# Conditions (Global Tag is used here):
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'FT_R_39X_V4A::All'

process.triggerSelection = cms.EDFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring(
      "HLT_Mu5","HLT_Mu7","HLT_Mu9","HLT_Mu11","HLT_Mu25"
    ),
    hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
    l1tResults = cms.InputTag( "gtDigis" ),
    l1tIgnoreMask = cms.bool( False ),
    l1techIgnorePrescales = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( False )
)

process.WeightFromTrigger = cms.EDProducer('WeightFromTrigger',
    HLTLabel = cms.InputTag("TriggerResults::HLT"),
    UseCombinedPrescales = cms.bool(False),
    TriggerNames = cms.vstring("HLT_Mu5","HLT_Mu7","HLT_Mu9","HLT_Mu11","HLT_Mu25"),
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root'),
    outputCommands = cms.untracked.vstring(
       'drop *',
       'keep *_*_*_Analysis',
    )
)
  
process.p = cms.Path(process.triggerSelection*process.WeightFromTrigger)
process.out.SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') )

process.e = cms.EndPath(process.out)

