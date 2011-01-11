import FWCore.ParameterSet.Config as cms

process = cms.Process("Analysis")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/data/Run2010B/Mu/RECO/PromptReco-v2/000/149/442/F4CBBFB8-40E6-DF11-9FAD-0030487C2B86.root',
'/store/data/Run2010B/Mu/RECO/PromptReco-v2/000/149/442/E282E48F-4AE6-DF11-BDA4-00304879FA4A.root',
#'/store/data/Run2010B/Mu/RECO/PromptReco-v2/000/149/442/B0642007-47E6-DF11-ACC0-0030487CD16E.root',
'/store/data/Run2010B/Mu/RECO/PromptReco-v2/000/149/442/A080AD3E-44E6-DF11-8C79-0030487C7828.root',
'/store/data/Run2010B/Mu/RECO/PromptReco-v2/000/149/442/98D8AFD9-42E6-DF11-BAC4-0030487CD6B4.root',
#'/store/data/Run2010B/Mu/RECO/PromptReco-v2/000/149/442/8E396AD5-49E6-DF11-BDEF-000423D94908.root',
#'/store/data/Run2010B/Mu/RECO/PromptReco-v2/000/149/442/46420456-46E6-DF11-9957-0030487CD716.root',
'/store/data/Run2010B/Mu/RECO/PromptReco-v2/000/149/442/2ED860B8-40E6-DF11-A060-0030487CD718.root',
'/store/data/Run2010B/Mu/RECO/PromptReco-v2/000/149/442/0C9D8607-47E6-DF11-996C-0030487C7392.root',
    )
)

# Conditions (Global Tag is used here):
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR_R_39X_V2::All'

process.triggerSelection = cms.EDFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring(
      "HLT_Mu5","HLT_Mu7","HLT_Mu9","HLT_Mu11"
    ),
    hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
    l1tResults = cms.InputTag( "gtDigis" ),
    l1tIgnoreMask = cms.bool( False ),
    l1techIgnorePrescales = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True )
)

process.WeightFromTrigger = cms.EDProducer('WeightFromTrigger',
    HLTLabel = cms.InputTag("TriggerResults::HLT"),
    UseCombinedPrescales = cms.bool(False),
    TriggerNames = cms.vstring("HLT_Mu5","HLT_Mu7","HLT_Mu9","HLT_Mu11"),
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root'),
    outputCommands = cms.untracked.vstring(
       'drop *',
       'keep *_*_*_Analysis',
    )
)
  
process.p = cms.Path(process.triggerSelection*process.WeightFromTrigger)

process.e = cms.EndPath(process.out)

tracer = cms.Service("Tracer")
