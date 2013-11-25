import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.patTemplate_cfg import *
process.setName_("llbbX")
process.options.wantSummary = False
process.MessageLogger.cerr.FwkReport.reportEvery = 100

## Source
readFiles = cms.untracked.vstring()
readFiles.extend([
    'file:/storage/data/cms/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/0AE169B1-01D3-E111-9939-001E673968F1.root'
    ])

process.source = cms.Source(
    "PoolSource",
    fileNames = readFiles
    )

## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

runOnMC = True

#muons
from UserCode.zbb_louvain.PATconfig.muon_cff import *
setupPatMuons(process, runOnMC)

process.preSequence = cms.Sequence(
    process.pfNoPileUpSequence+
    process.pfParticleSelectionSequence+
    process.pfParticleSelectionSequence +
    process.preMuonSeq
    )

print "These modules will be removed from the pat defualt sequence as already produced before:"
for name in process.preSequence.moduleNames() :
    if name in process.patDefaultSequence.moduleNames() :
        print name
        process.patDefaultSequence.remove(getattr(process,name))
        if name in process.patDefaultSequence.moduleNames() : print "Error : module not removed from pat default sequence"
print "...done."

process.p = cms.Path(process.preSequence+process.patDefaultSequence+process.postMuonSeq)

## Output Module Configuration (expects a path 'p')
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('patTuple.root'),
    SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring('drop *',
                                           'keep *_*Muons*_*_llbbX',
                                           )
    )


