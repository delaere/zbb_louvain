import FWCore.ParameterSet.Config as cms
#import os
process = cms.Process("ZplusJets")

#need to be implmented all what was done for 444 : leptons, jets, MET and adapt in 52X
#electron and muons recommandations : https://indico.cern.ch/conferenceDisplay.py?confId=193787
#twiki : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId and https://twiki.cern.ch/twiki/bin/view/CMS/EgammaEARhoCorrection and https://twiki.cern.ch/twiki/bin/view/CMS/EgammaCutBasedIdentification and ...
#MET : https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMetAnalysis#PAT
#packages for 52X/53X : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePATReleaseNotes53X#V08_10_00
#btag ? : don't excpect to change, just WP to be checked for CSV, and later on the JP calibration for Torino 
#Jets ? , beta/beta*, vertx ... JEC...
#444pat : https://twiki.cern.ch/twiki/bin/view/CMSPublic/LeptonSelectionVjets2011
#Trigger to be checked
#check saved outputs

#packages are OK in 525, problems in 531 then before passing to 53X need a explicit recipe for 53X

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

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('MC_summer2012.root'),
                                                              # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p1','p2') ),
                                                              # save PAT Layer 1 output; you need a '*' to
                                                              # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('drop *',
                                                                      'keep *_offlinePrimaryVertices*_*_*',
                                                                      #'keep *_offlinePrimaryVertexFromZ_*_*', ## Torino's Z vertex producer
                                                                      #'keep edmMergeableCounter_*_*_*', ## Torino's mergeable counter
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
                                                                      'keep *_combinedSecondaryVertex*BJetTags*_*_PAT',
                                                                      ### for Torino's studies on SV ############################
                                                                      #'keep recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector_*_*_*',
                                                                      #'keep recoBaseTagInfosOwned_selectedPatJets_tagInfos_PAT',
                                                                      #'keep recoBaseTagInfosOwned_patJets_tagInfos_PAT',
                                                                      #'keep recoSecondaryVertexTagInfos_secondaryVertexTagInfosAK5PFOffset__PAT',
                                                                      #'keep recoSecondaryVertexTagInfos_secondaryVertexTagInfosAOD__PAT',
                                                                      #'keep recoBaseTagInfosOwned_selectedPatJetsAK5PFOffset_tagInfos_PAT',
                                                                      #'keep recoBaseTagInfosOwned_patJetsAK5PFOffset_tagInfos_PAT',

                                                                      # MC ######################################################
                                                                      'keep GenEventInfoProduct_generator_*_*',
                                                                      'keep *_genMetTrue_*_*',
                                                                      'keep recoGenJets_ak5GenJets_*_*',
                                                                      'keep *_addPileupInfo_*_*',
                                                                      'keep LHEEventProduct_*_*_*',
                                                                      'keep *_genParticles_*_*'
                                                                      )
                               )

############LOAD PART.2####################
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger(process,sequence='patDefaultSequence',hltProcess = '*')

from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.jetTools import *
process.load('CommonTools.ParticleFlow.pfParticleSelection_cff') 

########################
## Standard Modules  ###
########################

## Load standard Reco modules
process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
## Generator informations
#process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
#process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
#process.load("Configuration.StandardSequences.Generator_cff")

from RecoJets.JetProducers.FastjetParameters_cfi import *
from RecoJets.JetProducers.ak5TrackJets_cfi import *
#from RecoJets.JetProducers.GenJetParameters_cfi import *
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

##-------------------- Import the Jet RECO modules -----------------------
#process.load('RecoJets.Configuration.RecoPFJets_cff')
#process.load("RecoJets.Configuration.GenJetParticles_cff")
#process.load("RecoJets.Configuration.RecoGenJets_cff")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

##-------------------- Turn-on the FastJet density calculation ----------------------------------------------------
process.kt6PFJets.doRhoFastjet = True

##-------------------- Turn-on the FastJet jet area calculation for your favorite algorithm -----------------------
process.kt6PFJets.doAreaFastjet = True
process.ak5PFJets.doAreaFastjet = True

#make the best choice for the eta max.
#process.kt6PFJets.Rho_EtaMax = cms.double(5.0)
#process.ak5PFJets.Rho_EtaMax = cms.double(5.0)

# to compute FastJet rho to correct isolation (note: EtaMax restricted to 2.5)
process.kt6PFJetsForIsolation = process.kt4PFJets.clone( rParam = 0.6, doRhoFastjet = True)
process.kt6PFJetsForIsolation.Rho_EtaMax = cms.double(2.5)


############ WARNING! to be run on data only!
############  need to be adapted for MC 
removeMCMatching(process, ['All'])

process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(True),
                                     makeTriggerResults=cms.untracked.bool(True),
                                     )

MC = True

if MC :
    process.GlobalTag.globaltag = 'START52_V9::All'
else :    
    process.GlobalTag.globaltag = 'GR_R_52_V7::All'

process.pfPileUp.PFCandidates = cms.InputTag("particleFlow")
process.pfNoPileUp.bottomCollection = cms.InputTag("particleFlow")

from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFElectronIso, setupPFMuonIso
process.eleIsoSequence = setupPFElectronIso(process, 'gsfElectrons')
process.muIsoSequence = setupPFMuonIso(process, 'muons')


##########################
#### INPUT files #########
##########################

readFiles = cms.untracked.vstring()
readFiles.extend([
           #'/store/relval/CMSSW_5_2_2/DoubleMu/RECO/GR_R_52_V4_RelVal_zMu2011A-v2/0252/ECB07DA5-9274-E111-83D5-0018F3D09652.root'
       #'/store/relval/CMSSW_5_2_2/DoubleElectron/RECO/GR_R_52_V4_RelVal_zEl2011A-v1/0004/04A3F83B-B473-E111-9233-003048F118AC.root'
       #'/store/data/Run2012A/DoubleElectron/RECO/PromptReco-v1/000/190/705/6C49578C-A083-E111-A629-5404A63886E6.root'
       #'/store/data/Run2012A/DoubleMu/RECO/PromptReco-v1/000/190/645/F0D69742-8A82-E111-ABDE-BCAEC518FF30.root'
       #'/store/data/Run2012A/DoubleMu/RECO/PromptReco-v1/000/190/645/F0D69742-8A82-E111-ABDE-BCAEC518FF30.root',
       #'/store/data/Run2012A/DoubleMu/RECO/PromptReco-v1/000/190/645/DCAE2B35-8B82-E111-A830-00215AEDFCCC.root'
      '/store/relval/CMSSW_5_2_3_patch3/RelValTTbar/GEN-SIM-RECO/START52_V9_special_120410-v1/0122/4C156E86-1183-E111-BED9-003048FFCBF0.root'
    ])

process.MessageLogger.cerr.FwkReport  = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(150),  )
process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32(1000) )
process.source = cms.Source("PoolSource",
                            fileNames = readFiles,
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            )

#import FWCore.PythonUtilities.LumiList as LumiList
#import FWCore.ParameterSet.Types as CfgTypes
#myLumis = LumiList.LumiList(filename = 'Cert_190456-190688_8TeV_PromptReco_Collisions12_JSON.txt').getCMSSWString().split(',')
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#process.source.lumisToProcess.extend(myLumis)

######################
#### VERTEX FILTER ###
######################

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
process.goodPV= offlinePrimaryVertices.clone()
process.goodPV.cut=cms.string('ndof > 4&'
                              'abs(z) <24&'
                              '!isFake &'
                              ' position.Rho <2 '
                             )


###########################
#### PRE-SEQUENCES #######
##########################
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
                                  cut   = cms.string('mass > 12.0'),
                                  name  = cms.string('zelallelall'),
                                  roles = cms.vstring('all1', 'all2')
                                  )


process.zelTightelTight = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("tightElectrons@+ tightElectrons@-"),
                               cut = cms.string("mass > 12.0"),
                               name = cms.string('zeltighteltight'), 
                               roles = cms.vstring('tight1', 'tight2')
                              )

process.zelMatchedelMatched = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("matchedElectrons@+ matchedElectrons@-"),
                               cut = cms.string("mass > 12.0"),
                               name = cms.string('zelmatchedelmatched'), 
                               roles = cms.vstring('matched1', 'matched2')
                              )

process.zelMatchedTrigelMatchedTrig = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("matchedElectronsTrig@+ matchedElectronsTrig@-"),
                               cut = cms.string("mass > 12.0"),
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

process.patMuons.useParticleFlow=True

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
process.userDataSelectedMuons = cms.EDProducer(
       "Higgs2l2bMuonUserData",
          src = cms.InputTag("selectedPatMuons"),
          rho = cms.InputTag("kt6PFJetsForIsolation:rho")
       )
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

#from PhysicsTools.PatAlgos.tools.jetTools import *
# Use ak5PF instead of ak5Calo
##-------------------- Import the JEC services -----------------------
#process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
##-------------------- Import the Jet RECO modules -----------------------
#process.load('RecoJets.Configuration.RecoPFJets_cff')
##-------------------- Turn-on the FastJet density calculation -----------------------
#process.kt6PFJets.doRhoFastjet = True
##-------------------- Turn-on the FastJet jet area calculation for your favorite algorithm -----------------------
#process.ak5PFJets.doAreaFastjet = True

inputJetCorrLabel = ('AK5PF',['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual']) # ,'L5Flavor','L7Parton' OUTDATED: do not use them!
if MC:
     inputJetCorrLabel = ('AK5PF',['L1FastJet', 'L2Relative', 'L3Absolute'])
        

switchJetCollection(process,cms.InputTag('ak5PFJets'),
                    doJTA  = True,
                    doBTagging   = True,
                    # for MC, use only  ['L1FastJet','L2Relative','L3Absolute', 'L5Flavor', 'L7Parton']
                    jetCorrLabel = inputJetCorrLabel,#('AK5PF',['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual']),    #,'L5Flavor','L7Parton']),  
                    doType1MET   = False,
                    genJetCollection=cms.InputTag("ak5GenJets"),
                    doJetID      = True,
                    jetIdLabel   = "ak5"
                    )

process.selectedPatJets.cut      = 'pt > 10. & abs(eta) < 2.4 '
process.patJets.addTagInfos = cms.bool( True )


#process.cleanPatJets.checkOverlaps = cms.PSet(
#                       muons = cms.PSet(
#                              src       = cms.InputTag("cleanPatMuons"),
#                                                        algorithm = cms.string("byDeltaR"),
#                                                        preselection        = cms.string(""),
#                                                        deltaR              = cms.double(0.5),
#                                                        checkRecoComponents = cms.bool(False), # don't check if they share some AOD object ref
#                                                        pairCut             = cms.string(""),
#                                                        requireNoOverlaps   = cms.bool(True), # overlaps don't cause the jet to be discared
#                                                     ),
#                       electrons = cms.PSet(
#                              src       = cms.InputTag("cleanPatElectrons"),
#                                                        algorithm = cms.string("byDeltaR"),
#                                                        preselection        = cms.string(""),
#                                                        deltaR              = cms.double(0.5),
#                                                        checkRecoComponents = cms.bool(False), # don't check if they share some AOD object ref
#                                                        pairCut             = cms.string(""),
#                                                        requireNoOverlaps   = cms.bool(True), # overlaps don't cause the jet to be discared
#                                                     )
#                                   )


#clean 
process.bjets = process.cleanPatJets.clone( preselection = 'bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 1.74' ) ## FIXME:change the TAGGER!

#process.bbbar = cms.EDProducer("CandViewShallowCloneCombiner",
#                               decay = cms.string("bjets bjets"),
#                               cut = cms.string("mass > 0"),
#                               name = cms.string('bbbar'),
#                               roles = cms.vstring('b1', 'b2'),
#                               checkCharge = cms.bool(False)
#                              )

process.Zeej = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("zelMatchedelMatched selectedPatJets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zeej'),
                               roles = cms.vstring('Z', 'j'),
                               checkCharge = cms.bool(False)
                              )

process.Zmmj = cms.EDProducer("CandViewShallowCloneCombiner",
                               decay = cms.string("zmuMatchedmuMatched selectedPatJets"),
                               cut = cms.string("mass > 0"),
                               name = cms.string('Zmmj'),
                               roles = cms.vstring('Z', 'j'),
                               checkCharge = cms.bool(False)
                              )

#process.Zeeb = cms.EDProducer("CandViewShallowCloneCombiner",
#                              decay = cms.string("ZelMatchedelMatched bjets"),
#                              cut = cms.string("mass > 0"),
#                              name = cms.string('Zb'),
#                              roles = cms.vstring('Z', 'b'),
#                              checkCharge = cms.bool(False)
#                             )

#process.Zmmb = cms.EDProducer("CandViewShallowCloneCombiner",
#                              decay = cms.string("ZmuMatchedmuMatched bjets"),
#                              cut = cms.string("mass > 0"),
#                              name = cms.string('Zbb'),
#                              roles = cms.vstring('Z', 'b'),
#                              checkCharge = cms.bool(False)
#                             )

#process.Zeebb = cms.EDProducer("CandViewShallowCloneCombiner",
#                               decay = cms.string("ZelMatchedelMatched bbbar"),
#                               cut = cms.string("mass > 0"),
#                               name = cms.string('Zbb'),
#                               roles = cms.vstring('Z', 'b'),
#                               checkCharge = cms.bool(False)
#                              )

#process.Zmmbb = cms.EDProducer("CandViewShallowCloneCombiner",
#                               decay = cms.string("ZmuMatchedmuMatched bbbar"),
#                               cut = cms.string("mass > 0"),
#                               name = cms.string('Zbb'),
#                               roles = cms.vstring('Z', 'b'),
#                               checkCharge = cms.bool(False)
#                              )


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

# add MET (for PF objects)
from PhysicsTools.PatAlgos.tools.metTools import *
addPfMET(process, 'PF')


#####################Filter########################
process.ZMuMuFilter = cms.EDFilter("CandViewCountFilter",
                                   src = cms.InputTag("zmuAllmuAll"),
                                   minNumber = cms.uint32(1),
                                   )

process.ZEEFilter = cms.EDFilter("CandViewCountFilter",
                                 src = cms.InputTag("zelAllelAll"),
                                 minNumber = cms.uint32(1),
                                 )
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
process.mutrigger = countPatMuons.clone(src = 'allMuons', minNumber = 2)
process.eltrigger = countPatElectrons.clone(src = 'allElectrons', minNumber = 2)

######################
##    SEQUENCES     ##
######################
process.PFLepton = cms.Sequence(
    process.goodPV +
    process.TotalEventCounter +
        
    process.kt6PFJetsForIsolation+
    process.kt6PFJets+
    process.ak5PFJets+
    process.simpleEleIdSequence+

    ##to create the collection pfNoPileUp
    process.pfNoPileUpSequence+
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
    process.patDefaultSequence+

    process.userDataSelectedMuons+
    process.userDataSelectedElectrons+
        
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

    process.bjets+
    #process.bbbar+

    #process.offlinePrimaryVertexFromZ +
    
    #### Z+jets candidates ##########
    (process.Zmmj+
     process.Zeej)

    #(process.Zeeb+
     #process.Zmmb)
    
    #(process.Zeebb+
    # process.Zmmbb)

    
    )

process.p1 = cms.Path(process.PFLepton*process.mutrigger *process.ZMuMuFilter)
process.p2 = cms.Path(process.PFLepton*process.eltrigger *process.ZEEFilter)
    

#####################
###  OUTPATH    #####
#####################

process.outpath = cms.EndPath(
    process.out
    )
