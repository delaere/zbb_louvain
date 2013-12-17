import FWCore.ParameterSet.Config as cms

#setup
from PhysicsTools.PatAlgos.patTemplate_cfg import *
process.load("CommonTools.ParticleFlow.PF2PAT_cff") # load PF2PAT sequence
process.setName_("llbbX")
process.options.wantSummary = False
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#options
runOnMC = False

#GT
if runOnMC : process.GlobalTag.globaltag = 'START53_V27::All'
else : process.GlobalTag.globaltag = 'FT_53_V21_AN5::All'
  
## Source
readFiles = cms.untracked.vstring()
readFiles.extend([
    #'file:/storage/data/cms/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/0AE169B1-01D3-E111-9939-001E673968F1.root'
    'file:/storage/data/cms/store/data/Run2012D/JetMon/AOD/22Jan2013-v1/10000/0CD0D545-1492-E211-97CC-782BCB67A0FA.root'
    ])
process.source = cms.Source(
    "PoolSource",
    fileNames = readFiles
    )

## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

#objects
from PhysicsTools.PatAlgos.tools.coreTools import removeMCMatching
if not runOnMC : removeMCMatching(process, ['All'])
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger(process,sequence='patDefaultSequence',hltProcess = '*')
from UserCode.zbb_louvain.PATconfig.vertex_cff import *
setupGoodVertex(process)
from UserCode.zbb_louvain.PATconfig.muon_cff import *
setupPatMuons(process, runOnMC)
from UserCode.zbb_louvain.PATconfig.electron_cff import *
setupPatElectrons(process, runOnMC)
from UserCode.zbb_louvain.PATconfig.jet_cff import *
setupPatJets(process, runOnMC)
#from UserCode.zbb_louvain.PATconfig.subjet_cff import *
#setupPatSubJets(process, runOnMC)
from UserCode.zbb_louvain.PATconfig.met_cff import *
setupPatMets(process, runOnMC)

#sequence to run before the pat default sequence
process.preSequence = cms.Sequence(
    process.goodPV+
    process.PF2PAT
    )

#clean pat default sequence
print ""
print "These modules will be removed from the pat default sequence as already produced before:"
for name in process.preSequence.moduleNames() :
    if name in process.patDefaultSequence.moduleNames() :
        print name
        process.patDefaultSequence.remove(getattr(process,name))
        if name in process.patDefaultSequence.moduleNames() : print "Error : module not removed from pat default sequence"
print "...done."
print ""

#global sequence
removeCleaningFromTriggerMatching(process)
process.llbbXSequence = cms.Sequence(process.preSequence+process.patDefaultSequence+process.postMuonSeq+process.muonComposite+process.postElectronSeq+process.electronComposite+process.metUncertaintySequence)

#adapt the collection of vertices
changeVertexCollection(process,seqName='llbbXSequence')

#path to run
process.p = cms.Path(process.llbbXSequence)

#output
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('patTuple.root'),
    SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring('drop *',
                                           #TRIGGER
                                           'keep *_patTriggerEvent_*_*',
                                           'keep patTriggerPaths_patTrigger_*_*',
                                           #PV
                                           'keep *_offlinePrimaryVertices*_*_*',
                                           'keep *_goodPV*_*_*',
                                           #MUON
                                           'keep *_*Muons*_*_llbbX',
                                           #Electron
                                           'keep *_*Electrons*_*_llbbX',
                                           #JET
                                           'keep *_*atJets*_*_*',
                                           'keep *_pfNoTau_*_*',
                                           'keep *_*5PFJets*_*_*',
                                           'keep *_puJetId_*_*',
                                           'keep *_puJetMva_*_*',
                                           'keep *_*bjets*_*_*',
                                           #'keep *_simpleSecondaryVertex*BJetTags*_*_llbbX',
                                           #'keep *_combinedSecondaryVertexBJetTags*_*_llbbX',
                                           #'keep *_combinedInclusiveSecondaryVertexBJetTags*_*_llbbX',
                                           #'keep *_jetProbabilityBJetTags*_*_llbbX',
                                           'keep *_*JetTags*_*_llbbX',
                                           'keep *_kt6PFJets*_*_*',
					   #MET
					   'keep *_*MET*_*_*',      #Do we need the correction parameters or the corrected MET is sufficient?
					   'keep *_*MEt*_*_*',
					   'keep *_*Met*_*_*',
                                           #GEN
                                           'keep GenEventInfoProduct_generator_*_*',
                                           'keep *_genMetTrue_*_*',
                                           'keep recoGenJets_ak5GenJets_*_*',
                                           'keep *_addPileupInfo_*_*',
                                           'keep LHEEventProduct_*_*_*',
                                           'keep *_genParticles_*_*'
                                           )
    )


