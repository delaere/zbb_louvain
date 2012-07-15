import FWCore.ParameterSet.Config as cms
#import os
process = cms.Process("ZplusJets")
print "bigining"

#need to be implmented all what was done for 444 : leptons, jets, MET and adapt in 52X
#electron and muons recommandations : https://indico.cern.ch/conferenceDisplay.py?confId=193787
#twiki : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId and https://twiki.cern.ch/twiki/bin/view/CMS/EgammaEARhoCorrection and https://twiki.cern.ch/twiki/bin/view/CMS/EgammaCutBasedIdentification and ...
#MET : https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMetAnalysis#PAT
#packages for 52X/53X : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePATReleaseNotes52X
#btag : IVF ? 
#Jets ? , beta/beta*
#444pat : https://twiki.cern.ch/twiki/bin/view/CMSPublic/LeptonSelectionVjets2011
#Trigger to be checked
#check saved outputs

#packages are OK in 526, problems in 531 then before passing to 53X need a explicit recipe for 53X

#vertex ok : replace by module to match PFnoPU recommandation ?, in patSequence collection of PV replaced by goodPV
#Jets : JEC ok, PFnoPU or not ?
#bjets : ok : keep IVF infos ?
#combined objects OK


###############################
##### Loading what we need ####
###############################

process.load("PhysicsTools.PatAlgos.patSequences_cff")

######################
##      OUTPUT      ##
######################
from PhysicsTools.PatAlgos.patEventContent_cff import *

process.TotalEventCounter = cms.EDProducer("EventCountProducer")
process.TotalEventCounter = cms.EDProducer("EventCountProducer")
process.AfterPVFilterCounter = cms.EDProducer("EventCountProducer")
process.AfterNSFilterCounter = cms.EDProducer("EventCountProducer")
process.AfterPATCounter = cms.EDProducer("EventCountProducer")
process.AfterCandidatesCounter = cms.EDProducer("EventCountProducer")
process.AfterJetsCounter = cms.EDProducer("EventCountProducer")
#####################################
print "output"
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('MC_summer2012.root'),
                                                              # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p1','p2') ),
                                                              # save PAT Layer 1 output; you need a '*' to
                                                              # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('drop *',
                                                                      'keep *_offlinePrimaryVertices*_*_*',
                                                                      'keep *_offlinePrimaryVertexFromZ_*_*', ## Torino's Z vertex producer
                                                                      'keep edmMergeableCounter_*_*_*', ## Torino's mergeable counter
                                                                      'keep *_offlineBeamSpot*_*_*',
                                                                      'keep *_patMETs*_*_*',
                                                                      'keep *_patTriggerEvent_*_*',
                                                                      'keep patTriggerPaths_patTrigger_*_*',
                                                                      'keep *_*Tracks_*_*',

                                                                      ## rho corrections saved #########################
                                                                      'keep *_kt6PFJetsForIsolation_*_*',

                                                                      ### isolation deposits/ conversion information for building isolation/ID ######
                                                                      'keep *_elPFIsoValue_*_*',
                                                                      'keep *_allConversions_*_*',

                                                                      ##################################################
                                                                      'keep *_*atJets*_*_*',
                                                                      'keep reco*_z*_*_*',
                                                                      'keep *_*Muons*_*_*',
                                                                      'keep *_*Electrons*_*_*',
                                                                      #'keep *_patMETs*_*_*',

                                                                      ## b-tagger ###################################
                                                                      'keep *_bjets_*_*',
                                                                      'keep *_simpleSecondaryVertex*BJetTags*_*_PAT',
                                                                      'keep *_combinedSecondaryVertexBJetTags*_*_PAT',
                                                                      'keep *_jetProbabilityBJetTags*_*_PAT',
                                                                      ### for Torino's studies on SV ############################
                                                                      'keep recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector_*_*_*',
                                                                      'keep recoBaseTagInfosOwned_selectedPatJets_tagInfos_PAT',
                                                                      'keep recoBaseTagInfosOwned_patJets_tagInfos_PAT',
                                                                      'keep recoSecondaryVertexTagInfos_secondaryVertexTagInfosAK5PFOffset__PAT',
                                                                      'keep recoSecondaryVertexTagInfos_secondaryVertexTagInfosAOD__PAT',
                                                                      'keep recoBaseTagInfosOwned_selectedPatJetsAK5PFOffset_tagInfos_PAT',
                                                                      'keep recoBaseTagInfosOwned_patJetsAK5PFOffset_tagInfos_PAT',

                                                                      # MC ######################################################
                                                                      'keep GenEventInfoProduct_generator_*_*',
                                                                      'keep *_genMetTrue_*_*',
                                                                      'keep recoGenJets_ak5GenJets_*_*',
                                                                      'keep *_addPileupInfo_*_*',
                                                                      'keep LHEEventProduct_*_*_*',
                                                                      'keep *_genParticles_*_*'
                                                                      )
                               )


##########################
#### INPUT files #########
##########################
print "input"
readFiles = cms.untracked.vstring()
readFiles.extend([
       #'/store/data/Run2012A/DoubleElectron/RECO/PromptReco-v1/000/190/705/6C49578C-A083-E111-A629-5404A63886E6.root'
       #'/store/data/Run2012A/DoubleMu/RECO/PromptReco-v1/000/190/645/F0D69742-8A82-E111-ABDE-BCAEC518FF30.root'
       #'/store/data/Run2012A/DoubleMu/RECO/PromptReco-v1/000/190/645/F0D69742-8A82-E111-ABDE-BCAEC518FF30.root',
       #'/store/data/Run2012A/DoubleMu/RECO/PromptReco-v1/000/190/645/DCAE2B35-8B82-E111-A830-00215AEDFCCC.root'
      #'/store/relval/CMSSW_5_2_3_patch3/RelValTTbar/GEN-SIM-RECO/START52_V9_special_120410-v1/0122/4C156E86-1183-E111-BED9-003048FFCBF0.root'
        'file:/storage/data/cms/store/mc/Summer12/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S7_START52_V9-v2/0000/ACEB2F43-F396-E111-A7E3-002481E150DA.root'
    ])

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport  = cms.untracked.PSet(reportEvery = cms.untracked.int32(15))
process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32(1000) )
process.source = cms.Source("PoolSource",
                            fileNames = readFiles,
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            )




############LOAD PART.2####################
print "pat tools"
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger(process,sequence='patDefaultSequence',hltProcess = '*')

#from PhysicsTools.PatAlgos.tools.coreTools import * #dead
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.jetTools import *
process.load('CommonTools.ParticleFlow.pfParticleSelection_cff') 

########################
## Standard Modules  ###
########################
print "load"
## Load standard Reco modules
process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')

from RecoJets.JetProducers.FastjetParameters_cfi import *
from RecoJets.JetProducers.ak5TrackJets_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *

##----------------- Import the Particle Flow modules  --------------------
process.load("CommonTools.ParticleFlow.pfElectrons_cff")
process.load("CommonTools.ParticleFlow.pfMuons_cff")
process.load("CommonTools.ParticleFlow.ParticleSelectors.pfSortByType_cff")
process.load("CommonTools.ParticleFlow.pfNoPileUp_cff")
process.load("CommonTools.ParticleFlow.ParticleSelectors.pfSelectedMuons_cfi")
##-------------------- Import the JEC services ---------------------------
process.load("JetMETCorrections.Configuration.DefaultJEC_cff")
process.load("JetMETCorrections.Configuration.JetCorrectionServices_cff")
process.load("JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff")
process.load("JetMETCorrections.Configuration.JetCorrectionProducers_cff")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

############ WARNING! to be run on data only!
############  need to be adapted for MC 
print "remove matching"
MC = True
if not MC : removeMCMatching(process, ['All'])

process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(False),
                                     makeTriggerResults=cms.untracked.bool(False),
                                     )
print "global tag"

if MC :
    process.GlobalTag.globaltag = 'START52_V9::All'
else :    
    process.GlobalTag.globaltag = 'GR_R_52_V7::All'

#import FWCore.PythonUtilities.LumiList as LumiList
#import FWCore.ParameterSet.Types as CfgTypes
#myLumis = LumiList.LumiList(filename = 'Cert_190456-190688_8TeV_PromptReco_Collisions12_JSON.txt').getCMSSWString().split(',')
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#process.source.lumisToProcess.extend(myLumis)

##########################
#### PRE-SEQUENCES #######
##########################
print "pre-sequences"
#This should not change from 444
if MC:
    process.electronMatch.matched = "genParticles"
    process.muonMatch.matched = "genParticles"

    process.preMuonSequence = cms.Sequence(
                                           process.muonMatch+
                                           process.patTrigger)

    process.preElectronSequence = cms.Sequence(
                                               process.electronMatch+
                                               process.patTrigger
                                               )

else:
    process.preMuonSequence = cms.Sequence(process.patTrigger)

    process.preElectronSequence = cms.Sequence(process.patTrigger)

######################
#### VERTEX FILTER ###
######################

#from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
#process.goodPV= offlinePrimaryVertices.clone()
#process.goodPV.cut=cms.string('ndof > 4&'
#                              'abs(z) <24&'
#                              '!isFake &'
#                              ' position.Rho <2 '
#                             )

#from https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#JetEnCor2012V2
from PhysicsTools.SelectorUtils.pvSelector_cfi import pvSelector
process.goodPV = cms.EDFilter(
    "PrimaryVertexObjectFilter",
    filterParams = pvSelector.clone( minNdof = cms.double(4.0), maxZ = cms.double(24.0) ),
    src=cms.InputTag('offlinePrimaryVertices')
    )

process.patPF2PATSequence = cms.Sequence( process.patDefaultSequence )
adaptPVs(process, pvCollection="goodPV")


#Do we need this ?
process.load('RecoJets.Configuration.RecoPFJets_cff')
process.ak5PFJets.doAreaFastjet = True
##

process.pfPileUp.PFCandidates = cms.InputTag("particleFlow")
process.pfNoPileUp.bottomCollection = cms.InputTag("particleFlow")

from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFElectronIso, setupPFMuonIso
process.eleIsoSequence = setupPFElectronIso(process, 'gsfElectrons')
process.muIsoSequence = setupPFMuonIso(process, 'muons')

###########################
#### ELECTRON selection ###
###########################

#process.patElectrons.useParticleFlow=True

process.pfIsolatedElectrons.isolationCut = 0.5 ### TBC

process.load("RecoParticleFlow.PFProducer.electronPFIsolationValues_cff")
process.elPFIsoValueCharged03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.015)')
process.elPFIsoValueChargedAll03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.015)')
process.elPFIsoValuePU03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.015)')
process.elPFIsoValueGamma03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.08)')

process.pfAllElectrons.src = "particleFlow" # default = pfNoMuons
#process.pfAllElectrons.src = "pfNoPileUp"

# pfIsolated electrons are input for PATelectron producer (when usePF==True)



#################################
### ELECTRON trigger matching ###
#################################

pathTriggerEle ='path("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,0) && filter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter")'

process.eleTriggerMatchHLT = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                             src     = cms.InputTag( "selectedPatElectrons" ),
                                             matched = cms.InputTag( "patTrigger"),
                                             matchedCuts = cms.string(pathTriggerEle),
                                             maxDPtRel = cms.double( 0.5 ),
                                             maxDeltaR = cms.double( 0.3 ),
                                             resolveAmbiguities    = cms.bool( True ),
                                             resolveByMatchQuality = cms.bool( True )
                                             )

process.patElectronsWithTrigger = cms.EDProducer("PATTriggerMatchElectronEmbedder",
                                                 src     = cms.InputTag("selectedPatElectrons"),
                                                 matches = cms.VInputTag(cms.InputTag('eleTriggerMatchHLT'))
                                                 )

switchOnTriggerMatching( process, ['eleTriggerMatchHLT' ],sequence ='patDefaultSequence', hltProcess = '*' )

#from CommonTools.ParticleFlow.ParticleSelectors.pfSelectedElectrons_cfi import pfSelectedElectrons
#process.selectedPatElectronsTriggerMatch.src = cms.InputTag( 'selectedPatElectrons' )
#process.selectedPatElectronsTriggerMatch.matches = cms.VInputTag('eleTriggerMatchHLT')

################################
#### ELECTRON IDENTIFICATION ###
################################

## Working point and electron ID
process.load("RecoLocalCalo/EcalRecAlgos/EcalSeverityLevelESProducer_cfi")
process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")

process.patElectrons.addElectronID = cms.bool(True)
process.patElectrons.electronIDSources = cms.PSet(
    simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
    simpleEleId85relIso= cms.InputTag("simpleEleId85relIso"),
    simpleEleId80relIso= cms.InputTag("simpleEleId80relIso")
    )

process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)

#process.load("RecoParticleFlow.PFProducer.electronPFIsolationValues_cff")
## Electrons with UserData ###############################
process.userDataSelectedElectrons = cms.EDProducer(
       "Higgs2l2bElectronUserData",
          src = cms.InputTag("patElectrons"),
          rho = cms.InputTag("kt6PFJetsForIsolation:rho"),
          #Electrons = cms.InputTag("gsfElectrons"),
          PFCandidateMap = cms.InputTag('particleFlow:electrons'),

          ## NOT yet backported in 44X and 42X
          IsoValElectronNoPF = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03NoPFIdPFIso'),
                                             cms.InputTag('elPFIsoValueGamma03NoPFIdPFIso'),
                                             cms.InputTag('elPFIsoValueNeutral03NoPFIdPFIso')),
          IsoDepElectron = cms.VInputTag(cms.InputTag('elPFIsoDepositChargedPFIso'),
                                         cms.InputTag('elPFIsoDepositGammaPFIso'),
                                         cms.InputTag('elPFIsoDepositNeutralPFIso')),
       )

process.allElectrons = process.selectedPatElectrons.clone( cut = 'pt > 10 && abs(eta) < 2.5' ) 
process.allElectrons.src = "patElectronsWithTrigger"


process.tightElectrons = process.selectedPatElectrons.clone( cut = 
                                                  'electronID("simpleEleId80relIso") == 5 &' ## passing conversion rejection and ID
                                                  'userFloat("PFIsoPUCorrected") < 0.15 &'           
                                                  '((abs(superCluster.eta)< 1.442)||((1.566<(abs(superCluster.eta)))&&((abs(superCluster.eta))<2.50))) &'
                                                  'abs(dB) < 0.02 &'
                                                  'pt>10 &'
                                                  'abs(eta) < 2.5'
                                                  )
process.tightElectrons.src = "patElectronsWithTrigger"

process.matchedElectrons = process.tightElectrons.clone()

process.matchedElectronsTrig = process.cleanPatElectrons.clone( preselection =
                                                   'electronID("simpleEleId80relIso") == 5 &'
                                                   'userFloat("PFIsoPUCorrected") < 0.15 &'         
                                                   '((abs(superCluster.eta)< 1.442)||((1.566<(abs(superCluster.eta)))&&((abs(superCluster.eta))<2.50))) &'
                                                   'abs(dB) < 0.02 & '
                                                   'pt>10 &'
                                                   'abs(eta) < 2.5 &'
                                                   'triggerObjectMatches.size > 0'                           

                                                   )
process.matchedElectronsTrig.src = "patElectronsWithTrigger"

#################################
### Z electron candidates #######
#################################

process.zelAllelAll = cms.EDProducer('CandViewShallowCloneCombiner',
                                  decay = cms.string('allElectrons@+ allElectrons@-'),
                                  cut   = cms.string('mass > 50.0'),
                                  name  = cms.string('zelallelall'),
                                  roles = cms.vstring('all1', 'all2')
                                  )


process.zelTightelTight = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("tightElectrons@+ tightElectrons@-"),
                               cut = cms.string("mass > 50.0"),
                               name = cms.string('zeltighteltight'), 
                               roles = cms.vstring('tight1', 'tight2')
                              )

process.zelMatchedelMatched = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("matchedElectrons@+ matchedElectrons@-"),
                               cut = cms.string("mass > 50.0"),
                               name = cms.string('zelmatchedelmatched'), 
                               roles = cms.vstring('matched1', 'matched2')
                              )

process.zelMatchedTrigelMatchedTrig = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("matchedElectronsTrig@+ matchedElectronsTrig@-"),
                               cut = cms.string("mass > 50.0"),
                               name = cms.string('zelmatchedtrigelmatchedtrig'), 
                               roles = cms.vstring('matchedtrig1', 'matchedtrig2')
                              )


###########################
#### MUON selection #######
###########################


#Use PF for PAT muons. Then one can run the patDefaultSequence after the pfNoPU stuff.
#The patDefaultSequence takes the pfIsolatedMuons as default input collection. To change the input collection one can use:
#process.patMuons.pfMuonSource = cms.InputTag("pfMuons")  
#Then one can use the selectedPatMuons as collection and it will have the trigger matching embedded and it can also be used to build the Z candidate. 

#process.patMuons.useParticleFlow=True

#################################
### MUON Trigger matching #######
#################################

pathTriggerMu = 'path("HLT_Mu13_Mu8_v*",0,1) || path("HLT_Mu17_Mu8_v*",0,1) || path("HLT_Mu17_TkMu8_v*",0,1)'

process.muonTriggerMatchHLTMuons = cms.EDProducer("PATTriggerMatcherDRLessByR",
                                                  src     = cms.InputTag( 'selectedPatMuons' ) ,
                                                  matched = cms.InputTag( 'patTrigger' ),    # selections of trigger objects ,
                                                  matchedCuts = cms.string( pathTriggerMu ),    # selection of matches ,
                                                  maxDPtRel   = cms.double( 0.5 ), 
                                                  maxDeltaR   = cms.double( 0.3 ) ,
                                                  resolveAmbiguities    = cms.bool( True ) ,
                                                  resolveByMatchQuality = cms.bool( True )
                                                  )

switchOnTriggerMatchEmbedding(process ,triggerMatchers = ['muonTriggerMatchHLTMuons'],)
removeCleaningFromTriggerMatching(process)

#Switch to selected PAT objects in the trigger matching removeCleaningFromTriggerMatching( process )
#match the trigger object to the reconstructed muon (no cuts on id iso...) 
from CommonTools.ParticleFlow.ParticleSelectors.pfSelectedMuons_cfi import pfSelectedMuons

#process.muonTriggerMatchHLTMuons.src     = cms.InputTag( 'selectedPatMuons' )
#process.selectedPatMuonsTriggerMatch.src = cms.InputTag( 'pfSelectedMuons' ) 
#process.muonTriggerMatchHLTMuons.src     = cms.InputTag( 'pfSelectedMuons' )

from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
process.selectedPatMuonsTriggerMatch.src = cms.InputTag( 'selectedPatMuons' )
process.selectedPatMuonsTriggerMatch.matches = cms.VInputTag('muonTriggerMatchHLTMuons')

#the selectedMuons are created with the trigger matched muons as input collection.

# Muons with UserData ###############################
#process.userDataSelectedMuons = cms.EDProducer(
#       "Higgs2l2bMuonUserData",
#          src = cms.InputTag("selectedPatMuons"),
#          rho = cms.InputTag("kt6PFJetsForIsolation:rho")
#       )
###################################################

process.allMuons = selectedPatMuons.clone(
    src = cms.InputTag('selectedPatMuonsTriggerMatch'),
    cut = cms.string("pt>10  & abs(eta) < 2.4")    
    )

process.tightMuons = selectedPatMuons.clone(
   src = cms.InputTag('selectedPatMuonsTriggerMatch'),
   cut = cms.string('isGlobalMuon & isTrackerMuon &'
                    'innerTrack.hitPattern.trackerLayersWithMeasurement()>8 &'  ## new requirement in 44X due to changes in tracking
                    'userFloat("RelativePFIsolationRhoCorr") < 0.2 &' # PF isolation
                    #'innerTrack.numberOfValidHits > 10 &'  
                    'abs(dB) < 0.02 &' 
                    'normChi2 < 10 &'
                    'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                    'numberOfMatches>1 &'                                 
                    'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                    'pt>10 &'
                    'abs(eta) < 2.4')
   )

process.matchedMuons = process.tightMuons.clone()

process.matchedMuonsTrig = selectedPatMuons.clone(
    src = cms.InputTag('selectedPatMuonsTriggerMatch'),
    cut = cms.string('isGlobalMuon & isTrackerMuon &'
                     'innerTrack.hitPattern.trackerLayersWithMeasurement()>8 &'  ## new requirement in 44X due to changes in tracking
                     'userFloat("RelativePFIsolationRhoCorr") < 0.2 &' # PF isolation
                     #'innerTrack.numberOfValidHits > 10 &'    
                     'abs(dB) < 0.02 &' 
                     'normChi2 < 10 &'
                     'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                     'numberOfMatches>1 &'                                   # segments matched in at least two muon stations 
                     'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'    # one muon hit matched to the global fit
                     'pt>10 &'
                     'abs(eta) < 2.4 &'
                     #'(trackIso+caloIso)/pt < 0.15 &'                       # Z+jet choice
                     #' trackIso < 3 &'                                      # VBTF choice
                     'triggerObjectMatches.size > 0')
    )


#add muon cuts
#check here for values: CommonTools/ParticleFlow/python/Isolation/pfIsolatedMuons_cfi.py
#check here for values of the isolation deposits:  RecoMuon/MuonIsolation/python/muonPFIsolationValues_cff.py
# DEFAULT ones are: muPFIsoValueCharged04/muPFIsoValueNeutral04/muPFIsoValueGamma04...

process.pfIsolatedMuons.isolationCut = 0.2

#embedding objects
process.patMuons.embedCombinedMuon = cms.bool(True)
process.patMuons.embedStandAloneMuon = cms.bool(False)
process.patMuons.embedPickyMuon = cms.bool(False)
process.patMuons.embedTpfmsMuon = cms.bool(False)
process.patMuons.embedPFCandidate = cms.bool(True)  # embedding of track info process.patMuons.embedTrack = cms.bool(True)


#build the Z candidates taking 2 muons with opposite charge and a loose pT, eta cut (pfSelectedMuons).
#from CommonTools.ParticleFlow.ParticleSelectors.pfSelectedMuons_cfi import pfSelectedMuons
#process.selectedMuons = pfSelectedMuons.clone()
#process.selectedMuons.src = cms.InputTag("pfSelectedMuons")
#process.selectedMuons.cut = cms.string("pt > 15. & abs(eta) < 3. ")

#uncomment to select the two mouns with highest pT
## process.selectedMuonsForZ = cms.EDFilter("LargestPtCandViewSelector",
##                                          src = cms.InputTag("selectedMuonsAll"),
##                                          maxNumber = cms.uint32(2)
##                                          )


#################################
### Z muon candidates ###########
#################################

process.zmuAllmuAll = cms.EDProducer('CandViewShallowCloneCombiner',
                                  decay = cms.string('allMuons@+ allMuons@-'),
                                  cut   = cms.string('mass > 12.0'),
                                  name  = cms.string('Zmuallmuall'),
                                  roles = cms.vstring('all1', 'all2')
                                  )

process.zmuTightmuTight = cms.EDProducer('CandViewShallowCloneCombiner',
                                  decay = cms.string('tightMuons@+ tightMuons@-'),
                                  cut   = cms.string('mass > 12.0'),
                                  name  = cms.string('Zmutightmutight'),
                                  roles = cms.vstring('tight1', 'tight2')
                                  )

process.zmuMatchedmuMatched = cms.EDProducer('CandViewShallowCloneCombiner',
                                  decay = cms.string('matchedMuons@+ matchedMuons@-'),
                                  cut   = cms.string('mass >12.0'),
                                  name  = cms.string('Zmumatchedmumatched'),
                                  roles = cms.vstring('matched1', 'matched2')
                                  )

process.zmuMatchedTrigmuMatchedTrig = cms.EDProducer('CandViewShallowCloneCombiner',
                                  decay = cms.string('matchedMuonsTrig@+ matchedMuonsTrig@-'),
                                  cut   = cms.string('mass >12.0'),
                                  name  = cms.string('Zmumatchedtrigmumatchedtrig'),
                                  roles = cms.vstring('matchedtrig1', 'matchedtrig2')
                                  )


#################################################
#### JETS #######################################
#################################################

inputJetCorrLabel = ('AK5PF',['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual'])
if MC:
     inputJetCorrLabel = ('AK5PF',['L1FastJet', 'L2Relative', 'L3Absolute'])

switchJetCollection(process,cms.InputTag('ak5PFJets'),
                    doJTA  = True,
                    doBTagging   = True,
                    jetCorrLabel = inputJetCorrLabel,  
                    doType1MET   = False,
                    genJetCollection=cms.InputTag("ak5GenJets"),
                    doJetID      = True,
                    jetIdLabel   = "ak5"
                    )

process.selectedPatJets.cut      = 'pt > 15. & abs(eta) < 2.4 '
process.patJets.addTagInfos = cms.bool( True )

#bjets collections 
process.bjets = process.cleanPatJets.clone( preselection = 'bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 1.74' )
process.CSVbjets = process.cleanPatJets.clone( preselection = 'bDiscriminator("combinedSecondaryVertexBJetTags") > 0.679' )
process.JPbjets =  process.cleanPatJets.clone( preselection = 'bDiscriminator("jetProbabilityBJetTags") > 0.545' )

##################################
####### combined objects #########
##################################

process.bbbar = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("bjets bjets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('bbar'),
                               roles = cms.vstring('b1', 'b2'),
                               checkCharge = cms.bool(False)
                              )

process.zeej = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("zelMatchedelMatched selectedPatJets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zeej'),
                               roles = cms.vstring('Z', 'j'),
                               checkCharge = cms.bool(False)
                              )

process.zmmj = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("zmuMatchedmuMatched selectedPatJets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zmmj'),
                               roles = cms.vstring('Z', 'j'),
                               checkCharge = cms.bool(False)
                              )


process.zeeb = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("zelMatchedelMatched bjets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zeeb'),
                               roles = cms.vstring('Z', 'b'),
                               checkCharge = cms.bool(False)
                              )

process.zmmb = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("zmuMatchedmuMatched bjets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zmmbb'),
                               roles = cms.vstring('Z', 'b'),
                               checkCharge = cms.bool(False)
                              )

process.zeebb = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("zelMatchedelMatched bbbar"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zbb'),
                               roles = cms.vstring('Z', 'b'),
                               checkCharge = cms.bool(False)
                              )

process.zmmbb = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("zmuMatchedmuMatched bbbar"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zbb'),
                               roles = cms.vstring('Z', 'b'),
                               checkCharge = cms.bool(False)
                              )


##################################
### Torino's Z vertex producer ###
##################################

from ZbbAnalysis.Tools.zvertexproducer_cfi import zvertexproducer
process.offlinePrimaryVertexFromZ =  zvertexproducer.clone(
          VertexSrc   = cms.untracked.InputTag("offlinePrimaryVertices"),
          ZmmSrc      = cms.untracked.InputTag("zmuAllmuAll"),
          ZeeSrc      = cms.untracked.InputTag("zelAllelAll")
          )



#################################################
###### MET ######################################
#################################################

process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")
process.load("JetMETCorrections.Type1MET.pfMETCorrectionType0_cfi")
process.pfType1CorrectedMet.applyType0Corrections = cms.bool(False)
process.pfType1CorrectedMet.srcType1Corrections = cms.VInputTag(
#    cms.InputTag('pfMETcorrType0'),
    cms.InputTag('pfJetMETcorr', 'type1')        
)

process.load("JetMETCorrections.Type1MET.pfMETsysShiftCorrections_cfi")
if not MC : process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2012runAvsNvtx_data

process.pfType1p2CorrectedMet.srcType1Corrections = cms.VInputTag(
    cms.InputTag('pfJetMETcorr', 'type1') ,
    #cms.InputTag('pfMEtSysShiftCorr')       
)

######################
##      FILTER      ##
######################

process.ZMMFilter = cms.EDFilter("CandViewCountFilter",
                                 src = cms.InputTag("zmuAllmuAll"),
                                 minNumber = cms.uint32(1),
                                 )

process.ZEEFilter = cms.EDFilter("CandViewCountFilter",
                                 src = cms.InputTag("zelAllelAll"),
                                 minNumber = cms.uint32(1),
                                 )

######################
##    SEQUENCES     ##
######################
process.PFLepton = cms.Sequence(
    process.goodPV *
    process.TotalEventCounter *
        
    #process.kt6PFJetsForIsolation+
    #process.kt6PFJets+
    process.ak5PFJets *

    process.simpleEleIdSequence *

    ##to create the collection pfNoPileUp
    process.pfNoPileUpSequence *
    ## to create the isoVariables with pfNoPileUp
    ##and the values in the cfg
    
    process.pfParticleSelectionSequence+ 
    process.eleIsoSequence + ### check if they are alrady in the PAT default sequence
    process.muIsoSequence +
    #process.electronPFIsolationValuesSequence+
    
    process.pfAllNeutralHadrons+
    process.pfAllChargedHadrons+
    process.pfAllPhotons+
 
    process.pfMuonSequence+ 
    process.pfElectronSequence+
 
    (process.preMuonSequence + process.preElectronSequence)+

    #process.patDefaultSequence*
    process.patPF2PATSequence *

    #process.type0PFMEtCorrection * #missing class, seems not yet tagged : edm::Wrapper<edm::AssociationMap<edm::OneToManyWithQuality<std::vector<reco::Vertex>,std::vector<reco::Track>,float,unsigned int> > >
    process.pfType1CorrectedMet *
    process.pfMEtSysShiftCorrSequence * 
    process.pfType1p2CorrectedMet * #producePFMETCorrections *


    #process.userDataSelectedMuons+
    #process.userDataSelectedElectrons+
        
    ###### electron candidates #####
    process.eleTriggerMatchHLT+
    process.patElectronsWithTrigger+
 
    (process.allElectrons +
     process.tightElectrons +
     process.matchedElectrons +
     process.matchedElectronsTrig )+
    
    ###### muon candidates #####
    process.muonTriggerMatchHLTMuons+
    process.selectedPatMuonsTriggerMatch+
  
    (process.allMuons+
     process.tightMuons+
     process.matchedMuons+
     process.matchedMuonsTrig)+

    #### Z candidates ##########

    (process.zelAllelAll+
     process.zelTightelTight+
     process.zelMatchedelMatched +
     process.zelMatchedTrigelMatchedTrig)+

    (process.zmuAllmuAll+
     process.zmuTightmuTight+
     process.zmuMatchedmuMatched+
     process.zmuMatchedTrigmuMatchedTrig)+

    process.bjets
    )

process.p1 = cms.Path(process.PFLepton*process.ZMMFilter)
process.p2 = cms.Path(process.PFLepton*process.ZEEFilter)
    

#####################
###  OUTPATH    #####
#####################

process.outpath = cms.EndPath(
    process.out
    )
