## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.11 $'),
    annotation = cms.untracked.string('PAT tuple for Z+b analysis'),
    name = cms.untracked.string('$Source: /cvs/CMSSW/UserCode/zbb_louvain/test/patTuple_zbb_cfg.py,v $')
)

# for the latest reprocessed samples. You can find it with:
# dbs search --query="find dataset.tag where dataset like /Mu/Run2010A-DiLeptonMu-Dec22Skim_v2/RECO"
process.GlobalTag.globaltag = cms.string('FT_R_39X_V4A::All')

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

# electron triggers are taken accroding to https://twiki.cern.ch/twiki/bin/viewauth/CMS/VbtfZeeBaselineSelection

muontriggers      = cms.vstring("HLT_Mu3","HLT_Mu5","HLT_Mu7","HLT_Mu9","HLT_Mu11","HLT_Mu15_v1")

electrontriggers  = cms.vstring("HLT_Photon10_L1R","HLT_Photon15_Cleaned_L1R","HLT_Ele15_SW_CaloEleId_L1R","HLT_Ele17_SW_CaloEleId_L1R","HLT_Ele17_SW_TightEleId_L1R")
electrontriggers += cms.vstring("HLT_Ele22_SW_TighterCaloIdIsol_L1R_v1","HLT_Ele22_SW_TighterCaloIdIsol_L1R_v2") 

alltriggers       = muontriggers + electrontriggers

process.hlt = cms.EDFilter( "TriggerResultsFilter",
                            triggerConditions = alltriggers,
                            hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
                            l1tResults = cms.InputTag( "gtDigis" ),
                            l1tIgnoreMask = cms.bool( False ),
                            l1techIgnorePrescales = cms.bool( False ),
                            daqPartitions = cms.uint32( 1 ),
                            throw = cms.bool( False )
                          )

# compute weight from prescale
process.WeightFromTrigger = cms.EDProducer('WeightFromTrigger',
    HLTLabel = cms.InputTag("TriggerResults::HLT"),
    UseCombinedPrescales = cms.bool(False),
    TriggerNames = alltriggers 
)

# add trigger information (trigTools)
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger(process)

# trigger matchers for various collections

# base matcher to define default values
defaultTriggerMatch = cms.EDProducer(
    "PATTriggerMatcherDRDPtLessByR", 
    src     = cms.InputTag( "selectedPatMuons" ),
    matched = cms.InputTag( "patTrigger" ),          
    andOr                      = cms.bool( False ),  
    filterIdsEnum              = cms.vstring( '*' ), 
    filterIds                  = cms.vint32( 0 ),    
    filterLabels               = cms.vstring( '*' ), 
    pathNames                  = cms.vstring( 'HLT_Mu9' ),
    pathLastFilterAcceptedOnly = cms.bool( True ),    
    collectionTags             = cms.vstring( '*' ), 
    maxDPtRel = cms.double( 0.5 ),
    maxDeltaR = cms.double( 0.5 ),
    resolveAmbiguities    = cms.bool( True ),     
    resolveByMatchQuality = cms.bool( True ),      
)

process.selectedMuonsTriggerMatch = defaultTriggerMatch.clone(
        src         = cms.InputTag( "selectedPatMuons" ),
        pathNames   = muontriggers
)

process.selectedElectronsTriggerMatch = defaultTriggerMatch.clone(
        src         = cms.InputTag( "selectedPatElectrons" ),
        pathNames   = electrontriggers
)

# trigger object embedders for the same collections
process.selectedMuonsMatched = cms.EDProducer( "PATTriggerMatchMuonEmbedder",
        src     = cms.InputTag(  "selectedPatMuons" ),
        matches = cms.VInputTag( cms.InputTag('selectedMuonsTriggerMatch') )
    )

process.selectedElectronsMatched = cms.EDProducer( "PATTriggerMatchElectronEmbedder",
        src     = cms.InputTag(  "selectedPatElectrons" ),
        matches = cms.VInputTag( cms.InputTag('selectedElectronsTriggerMatch') )
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
                 # for MC, use only L2Relative', 'L3Absolute', 'L5Flavor', 'L7Parton'
                 # jetCorrLabel = ('AK7PF',['L2Relative', 'L3Absolute','L2L3Residual', 'L5Flavor', 'L7Parton']),
                 jetCorrLabel = ('AK7PF',['L2Relative', 'L3Absolute']),  #  'L2L3Residual' working for 387 but not for 397
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
                    # for MC, use only L2Relative', 'L3Absolute', 'L5Flavor', 'L7Parton'
                    #jetCorrLabel = ('AK5PF',['L2Relative', 'L3Absolute','L2L3Residual', 'L5Flavor', 'L7Parton']),
                    jetCorrLabel = ('AK5PF',['L2Relative', 'L3Absolute']),  #  'L2L3Residual' working for 387 but not for 397
                    doType1MET   = False,
                    genJetCollection=cms.InputTag("ak5GenJets"),
                    doJetID      = True,
                    #jetIdLabel   = "ak5"
                    )

# selected Jets
process.selectedPatJets.cut      = 'pt > 25. & abs(eta) < 2.4 '
process.selectedPatJetsAK7PF.cut = 'pt > 25. & abs(eta) < 2.4 '

#---------------------------- Leptons
#------------------------------------------------------------------------------------------------------------------------------------------------

from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *
from PhysicsTools.PatAlgos.cleaningLayer1.electronCleaner_cfi import *


#*************************************** Muons
#*******************************************************
# clean pat muons should be isolated for cleaning purpose
#process.cleanPatMuons.src = "selectedMuonsMatched"
process.cleanPatMuons.preselection = ('isGlobalMuon & isTrackerMuon & (trackIso+caloIso)/pt < 0.15')

# aditional collection of muons with no cuts
process.allMuons = process.cleanPatMuons.clone( preselection = 'pt > 5' )

# clean muons for direct analysis
process.looseMuons = process.cleanPatMuons.clone(preselection =
                                                 'isGlobalMuon & isTrackerMuon &'
                                                 'innerTrack.numberOfValidHits > 10 &'
                                                 '(trackIso+caloIso)/pt < 0.15 &'  # Z+jet choice 
                                                 #' trackIso < 3 &'                # VBTF choice
                                                 'pt > 10 &'
                                                 'abs(eta) < 2.4'
                                                 )
process.looseMuons.src = "selectedMuonsMatched"

process.tightMuons = process.cleanPatMuons.clone(preselection =
                                                 'isGlobalMuon & isTrackerMuon &'
                                                 'innerTrack.numberOfValidHits > 10 &'
                                                 'abs(dB) < 0.02 &' # why not 0.2 for 2mm ???
                                                 'normChi2 < 10 &'
                                                 'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                                                 'numberOfMatches>1 &' # segments matched in at least two muon stations 
                                                 'globalTrack.hitPattern.numberOfValidMuonHits > 0 &' # one muon hit matched to the global fit
                                                 '(trackIso+caloIso)/pt < 0.15 &'  # Z+jet choice
                                                 #' trackIso < 3 &'                # VBTF choice
                                                 'pt > 20 &'
                                                 'abs(eta) < 2.1'
                                                 )
process.tightMuons.src = "selectedMuonsMatched"

process.matchedMuons = process.cleanPatMuons.clone(preselection =
                                                 'isGlobalMuon & isTrackerMuon &'
                                                 'innerTrack.numberOfValidHits > 10 &'
                                                 'abs(dB) < 0.02 &' # why not 0.2 for 2mm ???
                                                 'normChi2 < 10 &'
                                                 'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                                                 'numberOfMatches>1 &' # segments matched in at least two muon stations 
                                                 'globalTrack.hitPattern.numberOfValidMuonHits > 0 &' # one muon hit matched to the global fit
                                                 '(trackIso+caloIso)/pt < 0.15 &'  # Z+jet choice
                                                 #' trackIso < 3 &'                # VBTF choice
                                                 'pt > 20 &'
                                                 'abs(eta) < 2.1 &'
                                                 'triggerObjectMatches.size > 0' #Trigger Match DeltaR and DeltapT/pT to be really tight
                                                 )
process.matchedMuons.src = "selectedMuonsMatched"

process.Ztighttight = cms.EDProducer("CandViewShallowCloneCombiner",
                                     decay = cms.string("matchedMuons@+ tightMuons@-"),
                                     cut = cms.string("60.0 < mass < 120.0"), 
                                     name = cms.string('ztighttight'),
                                     roles = cms.vstring('matched', 'tight')
                                     )

process.Ztightloose = cms.EDProducer("CandViewShallowCloneCombiner", 
                                     decay = cms.string("matchedMuons@+ looseMuons@-"), 
                                     cut = cms.string("60.0 < mass < 120.0"), 
                                     name = cms.string('ztightloose'),
                                     roles = cms.vstring('matched', 'loose')
                                     )

process.Zcleanclean = cms.EDProducer("CandViewShallowCloneCombiner", 
                                     decay = cms.string("cleanPatMuons@+ cleanPatMuons@-"), 
                                     cut = cms.string("60.0 < mass < 120.0"), 
                                     name = cms.string('zcleanclean'),
                                     roles = cms.vstring('clean1', 'clean2')
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

# clean pat Electrons should be isolated for cleaning purpose
#process.cleanPatElectrons.src = "selectedElectronsMatched"
process.cleanPatElectrons.preselection = 'electronID("simpleEleId85relIso") == 7'

# aditional collection of electrons with no cuts 
process.allElectrons = process.cleanPatElectrons.clone( preselection = 'pt > 5' ) 

# clean electrons for direct analysis
process.tightElectrons = cleanPatElectrons.clone( preselection =
                                                 'electronID("simpleEleId85relIso") == 7 &' 
                                                 # abs(eta)< 1.442 || 1.566 <abs(eta)<2.50 & included in WP85
                                                 'pt > 10. &'
                                                 'abs(eta) < 2.5 &'
                                                 #'abs(superCluster.energy * sin(2 * atan(exp(-1 *abs(superCluster.eta))))) > 20 &'
                                                 'abs(dB) < 0.02'
                                                 )
process.tightElectrons.src = "selectedElectronsMatched"

process.matchedElectrons = cleanPatElectrons.clone(preselection =
                                                   'electronID("simpleEleId85relIso") == 7 &' 
                                                   # abs(eta)< 1.442 || 1.566 <abs(eta)<2.50 & included in WP85
                                                   'pt > 25. &'
                                                   'abs(eta) < 2.5 &'
                                                   #'abs(superCluster.energy * sin(2 * atan(exp(-1 *abs(superCluster.eta))))) > 20 &'
                                                   'abs(dB) < 0.02 &'
                                                   'triggerObjectMatches.size > 0' #Trigger Match DeltaR and DeltapT/pT to be really tight
                                                   )
process.matchedElectrons.src = "selectedElectronsMatched"

process.Zelel = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("tightElectrons@+ matchedElectrons@-"),
                               cut = cms.string("60.0 < mass < 120.0"),
                               name = cms.string('zelel'), 
                               roles = cms.vstring('tight', 'matched')
                              )

#-----------------tracks
process.patMuons.embedTrack = True
process.patElectrons.embedTrack = True

#------------------------------ Vertices 
#------------------------------------------------------------------------------------------------------------------------------------------------		
# vertex filter

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
process.goodPV= offlinePrimaryVertices.clone()
process.goodPV.cut=cms.string('ndof > 4&'
                              'abs(z) <24&'
                              '!isFake &'
                              ' position.Rho <2 '
                              )

#------------------------------ Sequence
#------------------------------------------------------------------------------------------------------------------------------------------------		
# new definitions for special events

# bjets
process.bjets = process.cleanPatJets.clone( preselection = 'bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 1.74' )


# boosted Zs
process.boostedZelel = process.Zelel.clone( cut = cms.string("60.0 < mass < 120.0 & pt > 150.0")  )
process.boostedZmumu = process.Ztightloose.clone( cut = cms.string("60.0 < mass < 120.0 & pt > 150.0")  )

# counters
process.defaultcounter = cms.EDFilter("PATCandViewCountFilter",
    minNumber = cms.uint32(0),
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("cleanPatJets")
)

process.countZelel        = process.defaultcounter.clone( minNumber = cms.uint32(1), src = cms.InputTag("Zelel") )
process.countBoostedZelel = process.defaultcounter.clone( minNumber = cms.uint32(1), src = cms.InputTag("boostedZelel") )
process.countZmumu        = process.defaultcounter.clone( minNumber = cms.uint32(1), src = cms.InputTag("Ztightloose") )
process.countBoostedZmumu = process.defaultcounter.clone( minNumber = cms.uint32(1), src = cms.InputTag("boostedZmumu") )
process.countTwobjets     = process.defaultcounter.clone( minNumber = cms.uint32(2), src = cms.InputTag("bjets") )
process.countOnebjet      = process.defaultcounter.clone( minNumber = cms.uint32(1), src = cms.InputTag("bjets") )


# trigger matching and embedding should be done at the end of the sequence
process.patDefaultSequence *= process.selectedMuonsTriggerMatch
process.patDefaultSequence *= process.selectedMuonsMatched
process.patDefaultSequence *= process.selectedElectronsTriggerMatch
process.patDefaultSequence *= process.selectedElectronsMatched

# add user objects to patDefault
process.patDefaultSequence *= process.looseMuons
process.patDefaultSequence *= process.tightMuons
process.patDefaultSequence *= process.matchedMuons
process.patDefaultSequence *= process.allMuons
process.patDefaultSequence *= process.tightElectrons
process.patDefaultSequence *= process.matchedElectrons
process.patDefaultSequence *= process.allElectrons
process.patDefaultSequence *= process.goodPV

# special events section
process.patDefaultSequence *= process.bjets
process.patDefaultSequence *= process.boostedZelel
process.patDefaultSequence *= process.boostedZmumu

# compute weight from trigger presscale
process.patDefaultSequence *= process.WeightFromTrigger

# combine leptons to get Z candidates
process.patDefaultSequence *= process.Ztighttight
process.patDefaultSequence *= process.Ztightloose
process.patDefaultSequence *= process.Zcleanclean
process.patDefaultSequence *= process.Zelel

# Run it
# Zmumu, 2 bjets
process.p1 = cms.Path(process.hlt * process.scrapingVeto * process.patDefaultSequence * process.countZmumu * process.countTwobjets )
# Zelel, 2 bjets
process.p2 = cms.Path(process.hlt * process.scrapingVeto * process.patDefaultSequence * process.countZelel * process.countTwobjets )
# boosted Zmumu
process.p3 = cms.Path(process.hlt * process.scrapingVeto * process.patDefaultSequence * process.countOnebjet * process.countBoostedZmumu)
# boosted Zelel
process.p4 = cms.Path(process.hlt * process.scrapingVeto * process.patDefaultSequence * process.countOnebjet * process.countBoostedZelel)

process.out.SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p1', 'p2', 'p3', 'p4') )

#process.out.outputCommands = cms.untracked.vstring('keep *')
tokeep_clean  = [ 
                  # keep all types of pat and Pat Jets, to access embedded PF candidates
                  'keep *_*atJets*_*_*',

                  # keep all tracks (not tracksextra)
                  'keep recoTracks_generalTracks_*_*',

                  'keep *_patMETs*_*_*',
                  'keep *_patTrigger*_*_*' ]

tokeep_clean += [
                 'keep *_tightElectrons_*_*',
                 'keep *_matchedElectrons_*_*',
                 'keep *_allElectrons*_*_*',
                 
                 'keep *_looseMuons_*_*',
                 'keep *_tightMuons_*_*',
                 'keep *_matchedMuons_*_*',
                 'keep *_allMuons*_*_*',

                 # keep the weight from trigger info
                 'keep *_WeightFromTrigger_*_*',
                 'keep *_bjets_*_*',

                 'keep *_Z*_*_*',

                 'keep *_goodPV*_*_*' ]

# B-Tagging: is this needed ?
tokeep_clean += ['keep *_simpleSecondaryVertex*BJetTags*_*_PAT', 'keep *_trackCounting*BJetTags*_*_PAT']


process.out.outputCommands = cms.untracked.vstring('drop *', *tokeep_clean )
# process.out.outputCommands = cms.untracked.vstring( 'keep *' )

from glob import glob

files = glob('/storage/data/cms/store/data/Run2010A/Mu/RECO/DiLeptonMu-Dec22Skim_v2/*/*.root')
files = ["file:%s"  % (file) for file in files]

process.source.fileNames = files
    # [
    #"file:/storage/data/cms/store/data/Run2010A/Mu/RECO/DiLeptonMu-Dec22Skim_v2/0029/142EFD78-F010-E011-933A-003048D15D04.root"
    #"file:/home/fynu/arnaudp/scratch/Early_top_Analysis/101206/CMSSW_3_8_6_patch1/src/TopAnalysis/TopAnalysis/test/test_tt.root"
    # ]                                     

process.maxEvents.input = -1

process.out.fileName = 'Z_data.root'

process.options.wantSummary = True
