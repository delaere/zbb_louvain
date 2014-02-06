import FWCore.ParameterSet.Config as cms

#Options

#"""""""" Use as 'cmsRun patTuple_llbbX_cfg_dataMC.py option' to run locally or with crab, where option is a string containing 'Data' or/and 'AllEv' """"""""
#"""""""" Use as 'cmsRun patTuple_llbbX_cfg_dataMC.py option=Condor slice=X sample=NAME' where slice is an integer, sample is a string 'DY' ot 'TT' for example, other condor options are defined in runPATcondor.py """"""""""

runOnMC = True
runOnCondor = False
nevents = 100
makeNoPUMet = True

import sys

if (len(sys.argv)>1 and sys.argv[0]!="cmsRun") or (sys.argv[0]=="cmsRun" and len(sys.argv)>2):
    if sys.argv[0]=="cmsRun" : option = sys.argv[2]
    else : option = sys.argv[1]
    if "Condor" in option :
        runOnCondor = True
        print "Run on condor"
    if "Data" in option : runOnMC = False
    if "AllEv" in option : nevents = -1

if runOnCondor:
    from UserCode.zbb_louvain.condorScripts.runPATcondor import *
    files = cms.untracked.vstring(files)
else :
    readFiles = cms.untracked.vstring()
    if runOnMC:
        readFiles.extend([
            'file:/storage/data/cms/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/0AE169B1-01D3-E111-9939-001E673968F1.root'
            ])
    else :
        readFiles.extend([
            'file:/storage/data/cms/store/data/Run2012D/JetMon/AOD/22Jan2013-v1/10000/0CD0D545-1492-E211-97CC-782BCB67A0FA.root'
            ])
    files=readFiles
    out_fileName = "test.root"

#setup
from PhysicsTools.PatAlgos.patTemplate_cfg import *
process.load("CommonTools.ParticleFlow.PF2PAT_cff") # load PF2PAT sequence
process.pfPileUp.checkClosestZVertex = cms.bool(False)
process.pfNoElectron.enable = cms.bool(False)
process.pfNoMuon.enable = cms.bool(False)
process.pfJets.srcPVs = cms.InputTag("goodPV")
process.pfNoTau.enable = cms.bool(False)

process.setName_("llbbX")
process.options.wantSummary = False
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
if nevents > 0 : process.MessageLogger.cerr.FwkReport.reportEvery = nevents/10 

#GT
if runOnMC : process.GlobalTag.globaltag = 'START53_V27::All'
else : process.GlobalTag.globaltag = 'FT_53_V21_AN6::All'
  
## Source
process.source = cms.Source(
    "PoolSource",
    fileNames = files
    )

## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(nevents) )

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
from UserCode.zbb_louvain.PATconfig.tau_cff import *
setupPatTaus(process)
from UserCode.zbb_louvain.PATconfig.jet_cff import *
setupPatJets(process, runOnMC)
from UserCode.zbb_louvain.PATconfig.subjet_cff import *
setupPatSubJets(process, runOnMC)
from UserCode.zbb_louvain.PATconfig.met_cff import *
setupPatMets(process, runOnMC, makeNoPUMet)

#sequence to run before the pat default sequence
process.preSequence = cms.Sequence(
    process.goodPV *
    process.PF2PAT *
    process.preJetSequence *
    process.preSequenceCA8CHS +
    process.preMetSequence
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
process.llbbXSequence = cms.Sequence(
    process.preSequence*
    process.patDefaultSequence*
    process.postMuonSeq*
    process.muonComposite+
    process.postElectronSeq*
    process.electronComposite+
    process.selectedPatJetsCA8CHSPrunedPacked
    )
#adapt the collection of vertices
changeVertexCollection(process,seqName='llbbXSequence')

#path to run
process.LeptMerger = cms.EDProducer("CandViewMerger",
                                    src = cms.VInputTag( "allMuons","allElectrons")
                                    )

process.LeptFilter = cms.EDFilter("CandViewCountFilter",
                                  src = cms.InputTag("LeptMerger"),
                                  minNumber = cms.uint32(2),
                                  )

process.AllMerger = cms.EDProducer("CandViewMerger",
                                    src = cms.VInputTag("LeptMerger","cleanPatJets","cleanPatJetsCA8CHS","cleanPatJetsCA8CHSpruned")
                                    )

process.AllFilter = cms.EDFilter("CandViewCountFilter",
                                  src = cms.InputTag("AllMerger"),
                                  minNumber = cms.uint32(3),
                                  )

process.zMerger = cms.EDProducer("CandViewMerger",
                                 src = cms.VInputTag("zmuAllmuAll","zelAllelAll")
                                 )

process.zFilter = cms.EDFilter("CandViewCountFilter",
                                 src = cms.InputTag("zMerger"),
                                 minNumber = cms.uint32(1),
                                 )

process.p1 = cms.Path(process.llbbXSequence*process.LeptMerger*process.LeptFilter*process.AllMerger*process.AllFilter*process.metUncertaintySequence)

#output
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string(out_fileName),
    SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p1') ),
    outputCommands = cms.untracked.vstring('drop *',
                                           #TRIGGER
                                           'keep *_patTriggerEvent_*_*',
                                           'keep patTriggerPaths_patTrigger_*_*',
                                           #Tracks
                                           #'keep *_*Tracks_*_*', #needed?
                                           #PV
                                           'keep *_offlinePrimaryVertices*_*_*',
                                           'keep *_goodPV*_*_*',
                                           'keep edmMergeableCounter_*_*_*', #???
                                           'keep *_offlineBeamSpot*_*_*',
                                           #MUON
                                           'keep *_*Muons*_*_*',
                                           'keep *_MuScleFit_*_*',
                                           #Electron
                                           'keep *_*Electrons*_*_*',
                                           'keep *_elPFIso*_*_*',
                                           'keep *_allConversions_*_*',
                                           #Taus
                                           'keep *_*atTaus*_*_*',
                                           'keep *_hpsPFTauProducer_*_*',
                                           #Z candidates
                                           'keep *_z*_*_*',
                                           #JET
                                           'keep *_*atJets*_*_*',
                                           'keep *_pfNoTau_*_*',
                                           'keep *_*5PFJets*_*_*',
                                           'keep *_*ca8PFJets*_*_*',
                                           'keep *_pileupJetIdProducerChs*_*_*',
                                           #'keep *_puJetId*_*_*',
                                           #'keep *_puJetMva*_*_*',
                                           'keep *_*bjets*_*_*',
                                           #'keep *_*JetTags*_*_*',
                                           #'keep *_*TagInfos*_*_*',
                                           'keep *_kt6PFJets*_*_*',
					   #MET
					   'keep patMETs_*_*_*',
                                           #GEN
                                           'keep GenEventInfoProduct_generator_*_*',
                                           'keep *_genMetTrue_*_*',
                                           'keep recoGenJets_ak5GenJets*_*_*',
                                           'keep *_addPileupInfo_*_*',
                                           'keep LHEEventProduct_*_*_*',
                                           'keep *_genParticles_*_*',
                                           'keep recoGenJets_ca8GenJets*_*_*'
                                           )
    )


