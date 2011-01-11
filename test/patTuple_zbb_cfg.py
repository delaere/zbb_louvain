## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

# for the latest reprocessed samples
#dbs search --query="find dataset.tag where dataset like /Mu/Run2010A-DiLeptonMu-Dec22Skim_v2/RECO"
# dbs search --query="find dataset.tag where dataset like /Mu/Run2010B-DiLeptonMu-Dec22Skim_v2/RECO"
process.GlobalTag.globaltag = cms.string('FT_R_39X_V4A::All')

#dbs search --query="find dataset.tag where dataset like /TTJets_TuneD6T_7TeV-madgraph-tauola/Fall10-START38_V12-v2/GEN-SIM-RECO"
#process.GlobalTag.globaltag = cms.string('START38_V13::All')

# for the local cp3 samples
#process.GlobalTag.globaltag = cms.string('GR_R_38X_V15::All')

# running on data, remove genparticle references in objects
from PhysicsTools.PatAlgos.tools.coreTools import *
removeMCMatching(process, ['All'])

# scrapingveto:
process.scrapingVeto = cms.EDFilter("FilterOutScraping",
                                    applyfilter = cms.untracked.bool(True),
                                    debugOn = cms.untracked.bool(False),
                                    numtrack = cms.untracked.uint32(10),
                                    thresh = cms.untracked.double(0.2)
                                    )


#---------------------------- Trigger
#------------------------------------------------------------------------------------------------------------------------------------------------

process.hlt = cms.EDFilter( "TriggerResultsFilter",
                            triggerConditions = cms.vstring("HLT_Mu3","HLT_Mu5","HLT_Mu7","HLT_Mu9","HLT_Mu11","HLT_Mu15_v1",
                                                            "HLT_Ele10_LW_L1R","HLT_Ele10_SW_L1R","HLT_Ele15_LW_L1R","HLT_Ele15_SW_L1R"
                                                            ),    #HLT_Ele10_SW_L1R for TTJets sample           #changer HLT pour 2010B "HLT_Mu15_v1"
                            hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
                            l1tResults = cms.InputTag( "gtDigis" ),
                            l1tIgnoreMask = cms.bool( False ),
                            l1techIgnorePrescales = cms.bool( False ),
                            daqPartitions = cms.uint32( 1 ),
                            throw = cms.bool( False )
                            )

# add trigger information (trigTools)
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger(process)

process.cleanMuonTriggerMatchHLTMuAll = cms.EDProducer(
    "PATTriggerMatcherDRDPtLessByR", 
    src     = cms.InputTag( "cleanPatMuons" ), 
    matched = cms.InputTag( "patTrigger" ), 
    andOr                      = cms.bool( False ), 
    filterIdsEnum              = cms.vstring( '*' ), 
    filterIds                  = cms.vint32( 0 ), 
    filterLabels               = cms.vstring( '*' ), 
    pathNames                  = cms.vstring(
        'HLT_Mu3','HLT_Mu5','HLT_Mu7','HLT_Mu9','HLT_Mu11','HLT_Mu15_v1'
    ), 
    pathLastFilterAcceptedOnly = cms.bool( True ), 
    collectionTags             = cms.vstring( '*' ), 
    maxDPtRel = cms.double( 0.5 ), 
    maxDeltaR = cms.double( 0.5 ), 
    resolveAmbiguities    = cms.bool( True ), 
    resolveByMatchQuality = cms.bool( True )
)

process.cleanElectronTriggerMatchHLTEleAll = cms.EDProducer(
    "PATTriggerMatcherDRDPtLessByR", 
    src     = cms.InputTag( "cleanPatElectrons" ), 
    matched = cms.InputTag( "patTrigger" ), 
    andOr                      = cms.bool( False ), 
    filterIdsEnum              = cms.vstring( '*' ), 
    filterIds                  = cms.vint32( 0 ), 
    filterLabels               = cms.vstring( '*' ), 
    pathNames                  = cms.vstring(
       'HLT_Ele10_LW_L1R','HLT_Ele10_SW_L1R','HLT_Ele15_LW_L1R','HLT_Ele15_SW_L1R' 
    ), 
    pathLastFilterAcceptedOnly = cms.bool( True ), 
    collectionTags             = cms.vstring( '*' ), 
    maxDPtRel = cms.double( 0.5 ), 
    maxDeltaR = cms.double( 0.5 ), 
    resolveAmbiguities    = cms.bool( True ), 
    resolveByMatchQuality = cms.bool( True )
)

from PhysicsTools.PatAlgos.triggerLayer1.triggerMatcher_cfi import *
switchOnTriggerMatching( process ,
                         triggerMatchers = ['cleanMuonTriggerMatchHLTMuAll',
                                            'cleanElectronTriggerMatchHLTEleAll'
                                           ]
                       )


#---------------------------- MET
#------------------------------------------------------------------------------------------------------------------------------------------------

# add MET (for PF objects)
from PhysicsTools.PatAlgos.tools.metTools import *
addPfMET(process, 'PF')

#---------------------------- JET
#------------------------------------------------------------------------------------------------------------------------------------------------
#
from PhysicsTools.PatAlgos.tools.jetTools import *
# add kt4calo for comparison (should switch to some cone thing)
addJetCollection(process,cms.InputTag('ak7PFJets'),
                 'AK7', 'PF',
                 doJTA        = True,
                 doBTagging   = True,
                 jetCorrLabel = ('AK7PF',['L2Relative', 'L3Absolute']),
                 doType1MET   = False,
                 doL1Cleaning = True,                 
                 doL1Counters = False,
                 genJetCollection=cms.InputTag("ak7GenJets"),
                 doJetID      = True,
                 jetIdLabel   = "ak7"
                 )

# Use ak5PF instead of ak5Calo
switchJetCollection(process,cms.InputTag('ak5PFJets'),
                    doJTA  = True,
                    doBTagging   = True,
                    jetCorrLabel = ('AK5PF',['L2Relative', 'L3Absolute']),  #  , 'L2L3Residual' working for 387 but not for 397
                    doType1MET   = False,
                    genJetCollection=cms.InputTag("ak5GenJets"),
                    doJetID      = True,
                    #jetIdLabel   = "ak5"
                    )

#selected Jets
process.selectedJetsAK5PF = process.cleanPatJets.clone(preselection =                                # cleanPatJets are the ak5PFJets
                                                   'pt > 25. &'
                                                   'abs(eta) < 2.4 '
                                                   )


from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
process.jet1 = countPatJets.clone(src = 'selectedJetsAK5PF', minNumber = 1)
process.jets2 = countPatJets.clone(src = 'selectedJetsAK5PF', minNumber = 2)



#---------------------------- Leptons
#------------------------------------------------------------------------------------------------------------------------------------------------

from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *
from PhysicsTools.PatAlgos.cleaningLayer1.electronCleaner_cfi import *


#*************************************** Muons
#*******************************************************
# clean muons for direct analysis
process.looseMuons = process.cleanPatMuons.clone(preselection =
                                                 'isGlobalMuon & isTrackerMuon &'
                                                 'pt > 10 &'
                                                 'abs(eta) < 2.4 &'
                                                 #'(trackIso+caloIso)/pt < 0.15 &'  # in the talk
                                                 ' trackIso < 3 &'
                                                 'abs(dB) < 0.02 &'
                                                 'innerTrack.hitPattern.numberOfValidStripHits > 10'
                                                 #'innerTrack.numberOfValidHits > 10 &'

                                                 )

process.tightMuons = process.cleanPatMuons.clone(preselection =
                                                 'isGlobalMuon & isTrackerMuon &'
                                                 'pt > 10 &'
                                                 'abs(eta) < 2.4 &'
                                                 #'(trackIso+caloIso)/pt < 0.15 &'   # in the talk
                                                 ' trackIso < 3 &'
                                                 'abs(dB) < 0.02 &'
                                                 'innerTrack.hitPattern.numberOfValidStripHits > 10 &'
                                                 #'innerTrack.numberOfValidHits > 10 &'
                                                 'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                                                 #'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                                                 'normChi2 < 10 &'
                                                 'abs(eta) < 2.1'
                                                 #Trigger Match DeltaR and DeltapT/pT to be really tight
                                                 #number of muon station >1 in the PAS
                                                 )

process.Ztightloose = cms.EDProducer("CandViewShallowCloneCombiner", 
                                     decay = cms.string("tightMuons@+ looseMuons@-"), 
                                     cut = cms.string("60.0 < mass < 120.0"), 
                                     name = cms.string('ztightloose'),
                                     roles = cms.vstring('muon1', 'muon2')
                                     )

process.Zcleanclean = cms.EDProducer("CandViewShallowCloneCombiner", 
                                     decay = cms.string("cleanPatMuons@+ cleanPatMuons@-"), 
                                     cut = cms.string("60.0 < mass < 120.0"), 
                                     name = cms.string('zcleanclean'),
                                     roles = cms.vstring('muon1', 'muon2')
                                     )


#*************************************** Electrons
#*******************************************************
# Working point   and     electron id
process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")
process.patElectrons.addElectronID = cms.bool(True)
process.patElectrons.electronIDSources = cms.PSet(
    simpleEleId95relIso= cms.InputTag("simpleEleId95relIso"),
    simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
    simpleEleId85relIso= cms.InputTag("simpleEleId85relIso")
    )
process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
process.makePatElectrons = cms.Sequence(process.patElectronIDs*process.patElectronIsolation*process.patElectrons)


# clean electrons for direct analysis
process.isolatedElectrons = cleanPatElectrons.clone(preselection =
                                                    'electronID("simpleEleId95relIso") == 7 &' ## abs(eta)< 1.442 || 1.566 <abs(eta)<2.50 & included in WP95
                                                    'pt > 20. &'
                                                    'abs(eta) < 2.5 &'
                                                    'abs(superCluster.energy * sin(2 * atan(exp(-1 *abs(superCluster.eta))))) > 20 &'
                                                    'abs(dB) < 0.02'
                                                    #'sqrt(pow(gsfTrack.innerPosition.x,2) + pow(gsfTrack.innerPosition.y,2))< 0.02 '  #supposed to be same than above
                                                    #'ecalDriven &'
                                                    #'(((dr03TkSumPt+max(0,dr03EcalRecHitSumEt-1)+dr03HcalTowerSumEt)/max(20,et)< 0.15 && abs(eta)<=1.4442)  ||'                                                                       '((dr03TkSumPt+max(0,dr03EcalRecHitSumEt)+dr03HcalTowerSumEt)/max(20,et)< 0.15 && abs(eta)>1.566))' #user defined isolation independantly from WP90/95
                                                    )

process.Zelel = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("isolatedElectrons@+ isolatedElectrons@-"),
                               cut = cms.string("60.0 < mass < 120.0")
                               )


#-----------------tracks
process.patMuons.embedTrack = True
process.patElectrons.embedTrack = True

#------------------------------ Vertices 
#------------------------------------------------------------------------------------------------------------------------------------------------		
# vertex filter
process.vertexselect = cms.EDFilter("VertexSelector",
                                    src = cms.InputTag("offlinePrimaryVertices"),
                                    cut = cms.string("!isFake && ndof > 4 && abs(z) < 24 && position.Rho < 2"),
                                    filter = cms.bool(True),
                                    )

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
process.goodPV= offlinePrimaryVertices.clone()
process.goodPV.cut=cms.string('ndof > 4&'
                              'abs(z) <24&'
                              '!isFake &'
                              ' position.Rho <2 '
                              )




# triggers based on loose leptons for skimming #in the talk
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
process.mutrigger = countPatMuons.clone(src = 'cleanPatMuons', minNumber = 2)
process.eltrigger = countPatElectrons.clone(src = 'cleanPatElectrons', minNumber = 2)

# add user objects to patDefault
process.patDefaultSequence *= process.looseMuons
process.patDefaultSequence *= process.tightMuons
process.patDefaultSequence *= process.Ztightloose
process.patDefaultSequence *= process.Zcleanclean
process.patDefaultSequence *= process.isolatedElectrons
process.patDefaultSequence *= process.Zelel
process.patDefaultSequence *= process.selectedJetsAK5PF
#process.patDefaultSequence *= process.jet1
#process.patDefaultSequence *= process.jets2
process.patDefaultSequence *= process.goodPV

# Run it
#process.p1 = cms.Path(process.scrapingVeto * process.patDefaultSequence* process.mutrigger)
process.p1 = cms.Path(process.hlt * process.scrapingVeto * process.patDefaultSequence * process.mutrigger)
#process.p2 = cms.Path(process.scrapingVeto * process.patDefaultSequence* process.eltrigger )
process.p2 = cms.Path(process.hlt * process.scrapingVeto * process.patDefaultSequence *process.eltrigger)

process.out.SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p1', 'p2') )

# decide what collections to keep. keep * is fun, try it :)
#process.out.outputCommands = cms.untracked.vstring('keep *')
#from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning
#patEventContentNoCleaning += ['keep *_isolatedMuons*_*_*', 'keep *_isolatedElectrons*_*_*']

tokeep_clean  = [ #'keep *']
                  'keep *_cleanPatElectrons*_*_*',
                  'keep *_cleanPatMuons*_*_*',
                  
                  # keep all types of pat and Pat Jets
                  'keep *_*atJets*_*_*',

                  # keep all tracks (not tracksextra)
                  'keep recoTracks_generalTracks_*_*',

                  'keep *_patMETs*_*_*',
                  'keep *_patTrigger*_*_*' ]

tokeep_clean += ['keep *_isolatedMuons*_*_*',
                 'keep *_isolatedElectrons*_*_*',
                 
                 'keep *_looseMuons*_*_*',
                 'keep *_tightMuons*_*_*',
                 'keep *_Z*_*_*',
                 'keep *_isolatedElectrons010*_*_*',
                 'keep *_jet1*_*_*',
                 'keep *_jets2*_*_*',
                 'keep *_goodPV*_*_*']

#B-Tagging!!!!!
tokeep_clean += ['keep *_simpleSecondaryVertex*BJetTags*_*_PAT', 'keep *_trackCounting*BJetTags*_*_PAT']


# process.out.outputCommands = cms.untracked.vstring('drop *', *patEventContentNoCleaning )
process.out.outputCommands = cms.untracked.vstring('drop *', *tokeep_clean )
#process.out.outputCommands = cms.untracked.vstring('drop *', 'keep *' )


process.source.fileNames = [
    "file:/storage/data/cms/store/data/Run2010A/Mu/RECO/DiLeptonMu-Dec22Skim_v2/0029/142EFD78-F010-E011-933A-003048D15D04.root"
    #"file:/home/fynu/arnaudp/scratch/Early_top_Analysis/101206/CMSSW_3_8_6_patch1/src/TopAnalysis/TopAnalysis/test/test_tt.root"
    ]                                     

process.maxEvents.input = 1

#for local submission                                       
# process.out.fileName = 'pat_leptons_cuts.root'
#process.out.fileName = 'tttttttttt_test.root'
#process.out.fileName = '2011_01_07_local_MURun2010A-DiLeptonMu-Dec22Skim.root'
#process.out.fileName = '2011_01_08_MURun2010A-DiLeptonMu-Dec22Skim.root'

#for CRAB submission
#process.out.fileName = 'MuRun2010A-DiLeptonMu-Nov4Skim_v1.root'  
#process.out.fileName = 'MuRun2010A-WZMu-Nov4Skim_v1.root'  
#process.out.fileName = 'TTJets_TuneD6T_7TeV-madgraph.root'  
#process.out.fileName = 'MuRun2010B-DiLeptonMu-Nov4Skim_v1.root'  
#process.out.fileName = 'MuRun2010A-DiLeptonMu-Nov4Skim_20101220.root'
#process.out.fileName = 'MURun2010A-DiLeptonMu-Dec22Skim.root'
process.out.fileName = 'MURun2010B-DiLeptonMu-Dec22Skim.root'
#process.out.fileName = 'ELERun2010A-DiLeptonEle-Dec22Skim.root'
#process.out.fileName = 'ELERun2010B-DiLeptonEle-Dec22Skim.root'

process.options.wantSummary = True
