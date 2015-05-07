import FWCore.ParameterSet.Config as cms

process = cms.Process("copy")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
      'file:testfileaMCatNLO.root'
    )
)


process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string("test.root"),
    SelectEvents = cms.untracked.PSet(),
    outputCommands = cms.untracked.vstring('drop *',
                                           'keep *_gen*_*_*',
                                           'keep *_*LHE*_*_*',
                                           'keep *_ak5GenJets_*_*',
                                           )
    )

process.end = cms.EndPath(process.out)
