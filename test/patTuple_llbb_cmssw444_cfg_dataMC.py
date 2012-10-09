
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import os
import sys
process = cms.Process("ZplusJets")

###############################
##### Loading what we need ####
###############################

options = VarParsing.VarParsing ()
# setup any defaults you want
options.register('boolMC',
                 0, # default value
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.int,         # string, int, or float
                 "MC flag")

options.register('bool8Nov',
                 0, # default value
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.int,         # string, int, or float
                 "data 8Nov flag")

# Hack to be able to pass multiple arguments from multicrab.cfg
print sys.argv
if len(sys.argv) > 0:
    last = sys.argv.pop()
    sys.argv.extend(last.split(":"))
    print sys.argv
    
options.parseArguments()

isMC = bool(options.boolMC)
is8Nov = bool(options.bool8Nov)

### Torino's counters ###############
from PhysicsTools.PatAlgos.patTemplate_cfg import *
process.TotalEventCounter = cms.EDProducer("EventCountProducer")
process.AfterPVFilterCounter = cms.EDProducer("EventCountProducer")
process.AfterNSFilterCounter = cms.EDProducer("EventCountProducer")
process.AfterPATCounter = cms.EDProducer("EventCountProducer")
process.AfterCandidatesCounter = cms.EDProducer("EventCountProducer")
process.AfterJetsCounter = cms.EDProducer("EventCountProducer")
#####################################

########################
## Standard Modules  ###
########################

##----------------- Load standard PAT tools -----------------------------
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger(process,sequence='patDefaultSequence',hltProcess = '*')
from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.jetTools import *
process.load('CommonTools.ParticleFlow.pfParticleSelection_cff') 

##----------------- Load standard Reco modules --------------------------
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')

##----------------- Generator informations ------------------------------
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("Configuration.StandardSequences.Generator_cff")

##----------------- Import the Particle Flow modules  --------------------
process.load("CommonTools.ParticleFlow.pfElectrons_cff")
process.load("CommonTools.ParticleFlow.pfMuons_cff")
process.load("CommonTools.ParticleFlow.ParticleSelectors.pfSortByType_cff")
process.load("CommonTools.ParticleFlow.pfNoPileUp_cff")
process.load("CommonTools.ParticleFlow.ParticleSelectors.pfSelectedMuons_cfi")

##-------------------- Import the Jet RECO modules -----------------------
from RecoJets.JetProducers.FastjetParameters_cfi import *
from RecoJets.JetProducers.ak5TrackJets_cfi import *
from RecoJets.JetProducers.GenJetParameters_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
process.load('RecoJets.Configuration.RecoPFJets_cff')
process.load("RecoJets.Configuration.GenJetParticles_cff")
process.load("RecoJets.Configuration.RecoGenJets_cff")

##-------------------- Import the JEC services ---------------------------
process.load("JetMETCorrections.Configuration.DefaultJEC_cff")
process.load("JetMETCorrections.Configuration.JetCorrectionServices_cff")
process.load("JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff")
process.load("JetMETCorrections.Configuration.JetCorrectionProducers_cff")

##-------------------- load the PU JetID sequence ------------------------
process.load("CMGTools.External.pujetidsequence_cff")

##-------------------- Import the MET correction modules -----------------
process.load("PhysicsTools.PatUtils.patPFMETCorrections_cff")
process.load("JetMETCorrections.Type1MET.pfMETsysShiftCorrections_cfi")

##-------------------- Standard tools ------------------------------------
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

##-------------------- Working point and electron ID for 2011 ------------
process.load("RecoLocalCalo/EcalRecAlgos/EcalSeverityLevelESProducer_cfi")
process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")

##-------------------- Turn-on the FastJet density calculation ----------------------------------------------------
process.kt6PFJets.doRhoFastjet = True
##-------------------- Turn-on the FastJet jet area calculation for your favorite algorithm -----------------------
process.kt6PFJets.doAreaFastjet = True
process.ak5PFJets.doAreaFastjet = True
##-------------------- To compute FastJet rho to correct isolation (note: EtaMax restricted to 2.5) ---------------
process.kt6PFJetsForIsolation = process.kt4PFJets.clone( rParam = 0.6 ,doRhoFastjet = True)
process.kt6PFJetsForIsolation.Rho_EtaMax = cms.double(2.5)

##-------------------- Removal of MC matching ----------------------------
if isMC:
    process.muonMatch.src = "pfMuons"
else:
    removeMCMatching(process, ['All']) ## needed also on MC? very strange...
    
##########################
#### GLOBAL TAG  #########
##########################

if isMC:
    process.GlobalTag.globaltag = 'START44_V13::All' # for Fall11    
    print "isMC=True"
else:
    if is8Nov: 
        process.GlobalTag.globaltag = 'GR_R_44_V15::All' ##'FT_R_44_V9::All' # 44X -- Nov8
        print "is8Nov=True"
        print "isMC=False"
    else:
        process.GlobalTag.globaltag = 'GR_R_44_V15::All' ##'FT_R_44_V11::All' # 44X -- Nov19
        print "is8Nov=False"
        print "isMC=False"

##########################
#### INPUT files #########
##########################

readFiles = cms.untracked.vstring()
readFiles.extend([
    #"file:/tmp/castello/Run2011A_DoubleElectron_AOD_08Nov2011-v1_0000_001ED292-B51B-E111-A231-001BFCDBD130.root" ### test file for electrons
    #"file:/tmp/castello/Run2011A_DoubleMu_AOD_08Nov2011-v1_0000_00011B62-381B-E111-8425-002618943810.root" ## test file for muons
    #"file:/tmp/castello/Fall11_DYJetsToLL_TuneZ2_M-50_7TeV-madgraph_PU_S6-START44_V5-v1_FE772459-D80A-E111-ABBE-E0CB4E1A1186.root" ## test file for MC Drell-Yan
    "file:/storage/data/cms/store/mc/Fall11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S6_START44_V9B-v1/0001/7A64B1BE-CE36-E111-BE8E-003048FFD7D4.root",
    #"file:/storage/data/cms/store/mc/Fall11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S6_START44_V9B-v1/0001/4A8BD06C-CE36-E111-B940-00304867D446.root",
    #"file:/storage/data/cms/store/mc/Fall11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S6_START44_V9B-v1/0001/A4CE0883-D336-E111-AD3A-003048FFD740.root"
    #"file:/storage/data/cms/store/mc/Fall11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S6_START44_V9B-v1/0000/A06A3717-C52B-E111-BFFA-00304867BEC0.root",
    #"file:/storage/data/cms/store/mc/Fall11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S6_START44_V9B-v1/0000/A2A2AAA2-AA2B-E111-9DA6-002618943951.root",
    #"file:/storage/data/cms/store/mc/Fall11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S6_START44_V9B-v1/0000/A41BD3D4-A22B-E111-B6D9-003048678AE2.root"
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_1.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_10.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_11.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_12.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_13.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_14.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_15.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_16.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_17.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_18.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_19.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_2.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_20.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_21.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_22.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_23.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_24.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_25.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_26.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_27.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_28.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_29.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_3.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_30.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_31.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_32.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_33.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_34.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_35.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_36.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_37.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_38.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_39.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_4.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_40.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_5.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_6.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_7.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_8.root",
  "file:/storage/data/cms/store/user/acaudron/ZAsamples/A125_H0475/RECO_9.root",

    ])

process.MessageLogger.cerr.FwkReport  = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(100),  )
# Example of how to debug a specific module
#process.MessageLogger.debugModules = cms.untracked.vstring('selectedElectronsWithIsolationData')
#process.MessageLogger.cerr = cms.untracked.PSet( threshold  = cms.untracked.string('DEBUG') )
process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(True),
                                      makeTriggerResults=cms.untracked.bool(True),
                                    )

process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32(30000) )
process.source = cms.Source("PoolSource",
                            fileNames = readFiles,
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            )

######################
#### VERTEX FILTER ###
######################

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
process.goodPV= offlinePrimaryVertices.clone()
process.goodPV.cut=cms.string('ndof > 4&'
                              'abs(z) <24&'
                              '!isFake &'
                              'position.Rho <2'
                              )

##########################
#### PRE-SEQUENCES #######
##########################

if isMC:
    process.electronMatch.matched = "genParticles"
    process.muonMatch.matched = "genParticles"
    process.preMuonSequence = cms.Sequence(
             process.muonMatch+
             process.patTrigger
    ) 
    
    process.preElectronSequence = cms.Sequence(
             process.electronMatch+
             process.patTrigger
    ) 
else:
    process.preMuonSequence = cms.Sequence(process.patTrigger) 
    process.preElectronSequence = cms.Sequence(process.patTrigger) 

################################
#### ELECTRON IDENTIFICATION ###
################################

process.patElectrons.addElectronID = cms.bool(True)
process.patElectrons.electronIDSources = cms.PSet(
    simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
    simpleEleId85relIso= cms.InputTag("simpleEleId85relIso"),
    simpleEleId80relIso= cms.InputTag("simpleEleId80relIso")
    )
process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)

###########################
#### ELECTRON ISOLATION ###
###########################

### from PF2PAT sequence...
process.pfPileUp.PFCandidates = cms.InputTag("particleFlow")
process.pfNoPileUp.bottomCollection = cms.InputTag("particleFlow")

### create the particle-based isolation values for gsfElectrons and muons
from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFElectronIso
process.eleIsoSequence = setupPFElectronIso(process, 'gsfElectrons')
process.pfIsolatedElectrons.isolationCut = 0.5 ### VERY loose, true isolation done later, exploiting deposits...
process.pfAllElectrons.src = "particleFlow" # default = pfNoMuons

### Electrons with UserData for isolation
process.selectedElectronsWithIsolationData = cms.EDProducer(
   "ElectronIsolationEmbedder",
   src = cms.InputTag("selectedPatElectrons"),
   rho = cms.InputTag("kt6PFJetsForIsolation:rho"),
   PFCandidateMap = cms.InputTag('particleFlow:electrons'),
   gsfElectrons = cms.InputTag('gsfElectrons'),
   conversions = cms.InputTag('allConversions'),
   beamSpot = cms.InputTag('offlineBeamSpot'),
   primaryVertex = cms.InputTag('offlinePrimaryVertices'),
   # NOT yet backported in 44X and 42X
   #IsoValElectronNoPF = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03NoPFIdPFIso'),
   #                                   cms.InputTag('elPFIsoValueGamma03NoPFIdPFIso'),
   #                                   cms.InputTag('elPFIsoValueNeutral03NoPFIdPFIso')),
   IsoValElectronNoPF = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03PFIso'),
                                      cms.InputTag('elPFIsoValueGamma03PFIso'),
                                      cms.InputTag('elPFIsoValueNeutral03PFIso')),
   IsoDepElectron = cms.VInputTag(cms.InputTag('elPFIsoDepositChargedPFIso'),
                                  cms.InputTag('elPFIsoDepositGammaPFIso'),
                                  cms.InputTag('elPFIsoDepositNeutralPFIso')),
)

#################################
### ELECTRON trigger matching ###
#################################

pathTriggerEle ='(path("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",0,0) && filter("hltEle17CaloIdIsoEle8CaloIdIsoPixelMatchDoubleFilter")) || (path("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,0) && filter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter"))'

process.eleTriggerMatchHLT = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                             src     = cms.InputTag( "selectedElectronsWithIsolationData" ),
                                             matched = cms.InputTag( "patTrigger"),
                                             matchedCuts = cms.string(pathTriggerEle),
                                             maxDPtRel = cms.double( 0.5 ),
                                             maxDeltaR = cms.double( 0.3 ),
                                             resolveAmbiguities    = cms.bool( True ),
                                             resolveByMatchQuality = cms.bool( True )
                                           )

process.patElectronsWithTrigger = cms.EDProducer( "PATTriggerMatchElectronEmbedder",
                                                  src     = cms.InputTag("selectedElectronsWithIsolationData"),
                                                  matches = cms.VInputTag(cms.InputTag('eleTriggerMatchHLT'))
                                                )

switchOnTriggerMatching( process, ['eleTriggerMatchHLT' ],sequence ='patDefaultSequence', hltProcess = '*' )

### Our electron collections: all, tight, matched
process.allElectrons = process.selectedPatElectrons.clone( cut = 'pt > 20 && abs(eta) < 2.5' ) 
process.allElectrons.src = "patElectronsWithTrigger"

if isMC:
  process.tightElectrons = process.selectedPatElectrons.clone( cut = 
                                                  'userInt("MediumWP")==1 &' #Medium WP agreed in June 2012
                                                  'userFloat("PFIsoPUCorrectedMC") < 0.15 &' # isolation for MC
                                                  '((abs(superCluster.eta)< 1.442)||((1.566<(abs(superCluster.eta)))&&((abs(superCluster.eta))<2.50))) &' # fiducial cut
                                                  'abs(dB) < 0.02 &'
                                                  'pt>20 &'
                                                  'abs(eta) < 2.5'
                                                  )
  process.matchedElectrons = process.cleanPatElectrons.clone( preselection =
                                                  'userInt("MediumWP")==1 &' #Medium WP agreed in June 2012
                                                  'userFloat("PFIsoPUCorrectedMC") < 0.15 &' # isolation for MC
                                                  '((abs(superCluster.eta)< 1.442)||((1.566<(abs(superCluster.eta)))&&((abs(superCluster.eta))<2.50))) &' # fiducial cut
                                                  'abs(dB) < 0.02 &'
                                                  'pt>20 &'
                                                  'abs(eta) < 2.5'
                                                  )
else:
  process.tightElectrons = process.selectedPatElectrons.clone( cut = 
                                                  'userInt("MediumWP")==1 &' #Medium WP agreed in June 2012
                                                  'userFloat("PFIsoPUCorrected") < 0.15 &' # isolation for data
                                                  '((abs(superCluster.eta)< 1.442)||((1.566<(abs(superCluster.eta)))&&((abs(superCluster.eta))<2.50))) &' #fiducial cut
                                                  'abs(dB) < 0.02 &'
                                                  'pt>20 &'
                                                  'abs(eta) < 2.5'
                                                  )
  process.matchedElectrons = process.cleanPatElectrons.clone( preselection =
                                                  'userInt("MediumWP")==1 &' #Medium WP agreed in June 2012
                                                  'userFloat("PFIsoPUCorrected") < 0.15 &' # isolation for data
                                                  '((abs(superCluster.eta)< 1.442)||((1.566<(abs(superCluster.eta)))&&((abs(superCluster.eta))<2.50))) &' #fiducial cut
                                                  'abs(dB) < 0.02 &'
                                                  'pt>20 &'
                                                  'abs(eta) < 2.5 &'
                                                  'triggerObjectMatches.size > 0' # trigger match
                                                   )

process.tightElectrons.src = "patElectronsWithTrigger"
process.matchedElectrons.src = "patElectronsWithTrigger"

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

###########################
#### MUON selection #######
###########################

#Use PF for PAT muons. Then one can run the patDefaultSequence after the pfNoPU stuff.
#The patDefaultSequence takes the pfIsolatedMuons as default input collection. 
#To change the input collection one can use: process.patMuons.pfMuonSource = cms.InputTag("pfMuons")  
#Then one can use the selectedPatMuons as collection and it will have the trigger matching embedded 
#and it can also be used to build the Z candidate. 

process.patMuons.pfMuonSource = cms.InputTag("pfMuons")
process.patMuons.useParticleFlow=True

### embedding objects
process.patMuons.embedCombinedMuon = cms.bool(True)
process.patMuons.embedStandAloneMuon = cms.bool(False)
process.patMuons.embedPickyMuon = cms.bool(False)
process.patMuons.embedTpfmsMuon = cms.bool(False)
process.patMuons.embedPFCandidate = cms.bool(True)  # embedding of track info process.patMuons.embedTrack = cms.bool(True)

###########################
#### MUON Isolation #######
###########################

### create the particle-based isolation values for gsfElectrons and muons
from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFMuonIso
process.muIsoSequence = setupPFMuonIso(process, 'muons')

#check here for values: CommonTools/ParticleFlow/python/Isolation/pfIsolatedMuons_cfi.py
#check here for values of the isolation deposits:  RecoMuon/MuonIsolation/python/muonPFIsolationValues_cff.py
# DEFAULT ones are: muPFIsoValueCharged04/muPFIsoValueNeutral04/muPFIsoValueGamma04...
process.pfIsolatedMuons.isolationCut = 0.5 ## very loose, true isolation done later, exploiting deposits...
## default cone is 0.4, as recommended at: https://twiki.cern.ch/twiki/bin/view/CMS/TWikiSMP-MUO#MuORecommendations

### Muons with isolation data embedded
process.selectedMuonsWithIsolationData = cms.EDProducer(
   "MuonIsolationEmbedder",
   src = cms.InputTag("selectedPatMuons"),
   rho = cms.InputTag("kt6PFJetsForIsolation:rho")
)

#################################
#### MUON Trigger matching ######
#################################

pathTriggerMu = 'path("HLT_DoubleMu6_v*",0,0) || path("HLT_DoubleMu7_v*",0,0) || path("HLT_Mu13_Mu8_v*",0,1) || path("HLT_Mu17_Mu8_v*",0,1)'

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
#Switch to selected PAT objects in the trigger matching removeCleaningFromTriggerMatching( process )
#match the trigger object to the reconstructed muon (no cuts on id iso...) 
from CommonTools.ParticleFlow.ParticleSelectors.pfSelectedMuons_cfi import pfSelectedMuons 
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *                       
process.muonTriggerMatchHLTMuons.src = cms.InputTag( 'selectedMuonsWithIsolationData' )
process.selectedPatMuonsTriggerMatch.src = cms.InputTag( 'selectedMuonsWithIsolationData' )
process.selectedPatMuonsTriggerMatch.matches = cms.VInputTag('muonTriggerMatchHLTMuons')

removeCleaningFromTriggerMatching(process)

### Our muon collections: all, tight, matched
process.allMuons = selectedPatMuons.clone(
    src = cms.InputTag('selectedPatMuonsTriggerMatch'),
    cut = cms.string("pt>20  & abs(eta) < 2.4")    
    )

process.tightMuons = selectedPatMuons.clone(
   src = cms.InputTag('selectedPatMuonsTriggerMatch'),
   cut = cms.string('isGlobalMuon & isTrackerMuon &'
                    'innerTrack.hitPattern.trackerLayersWithMeasurement>8 &'  ## new requirement in 44X due to changes in tracking
                    'userFloat("RelativePFIsolationDBetaCorr") < 0.2 &' # PF isolation
                    'abs(dB) < 0.02 &' 
                    'normChi2 < 10 &'
                    'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                    'numberOfMatchedStations>1 &'                                 
                    'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                    'pt>20 &'
                    'abs(eta) < 2.4')
   )

if isMC :
    process.matchedMuons = selectedPatMuons.clone(
        src = cms.InputTag('selectedPatMuonsTriggerMatch'),
        cut = cms.string('isGlobalMuon & isTrackerMuon &'
                         'innerTrack.hitPattern.trackerLayersWithMeasurement>8 &'  ## new requirement in 44X due to changes in tracking
                         'userFloat("RelativePFIsolationDBetaCorr") < 0.2 &' # PF isolation   
                         'abs(dB) < 0.02 &' 
                         'normChi2 < 10 &'
                         'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                         'numberOfMatchedStations>1 &'                                   # segments matched in at least two muon stations 
                         'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'    # one muon hit matched to the global fit
                         'pt>20 &'
                         'abs(eta) < 2.4 &'
                         #'(trackIso+caloIso)/pt < 0.15 &'                       # Z+jet choice
                         #' trackIso < 3 &'                                      # VBTF choice
                         )
        )
else :
    process.matchedMuons = selectedPatMuons.clone(
        src = cms.InputTag('selectedPatMuonsTriggerMatch'),
        cut = cms.string('isGlobalMuon & isTrackerMuon &'
                         'innerTrack.hitPattern.trackerLayersWithMeasurement>8 &'  ## new requirement in 44X due to changes in tracking
                         'userFloat("RelativePFIsolationDBetaCorr") < 0.2 &' # PF isolation   
                         'abs(dB) < 0.02 &' 
                         'normChi2 < 10 &'
                         'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                         'numberOfMatchedStations>1 &'                                   # segments matched in at least two muon stations 
                         'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'    # one muon hit matched to the global fit
                         'pt>20 &'
                         'abs(eta) < 2.4 &'
                         #'(trackIso+caloIso)/pt < 0.15 &'                       # Z+jet choice
                         #' trackIso < 3 &'                                      # VBTF choice
                         'triggerObjectMatches.size > 0')
        )


#################################
### Z muon candidates ###########
#################################

process.zmuAllmuAll = cms.EDProducer('CandViewShallowCloneCombiner',
                                  decay = cms.string('allMuons@+ allMuons@-'),
                                  cut   = cms.string('mass > 50.0'),
                                  name  = cms.string('Zmuallmuall'),
                                  roles = cms.vstring('all1', 'all2')
                                  )

process.zmuTightmuTight = cms.EDProducer('CandViewShallowCloneCombiner',
                                  decay = cms.string('tightMuons@+ tightMuons@-'),
                                  cut   = cms.string('mass > 50.0'),
                                  name  = cms.string('Zmutightmutight'),
                                  roles = cms.vstring('tight1', 'tight2')
                                  )

process.zmuMatchedmuMatched = cms.EDProducer('CandViewShallowCloneCombiner',
                                  decay = cms.string('matchedMuons@+ matchedMuons@-'),
                                  cut   = cms.string('mass >50.0'),
                                  name  = cms.string('Zmumatchedmumatched'),
                                  roles = cms.vstring('matched1', 'matched2')
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
#### JETS #######################################
#################################################

# Jet Correction label. 'L5Flavor' and 'L7Parton' are OUTDATED: do not use them!
if isMC:
    inputJetCorrLabel = ('AK5PF',['L1FastJet', 'L2Relative', 'L3Absolute'])
else:
    inputJetCorrLabel = ('AK5PF',['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual'])

# Use ak5PFJets
switchJetCollection(process,cms.InputTag('ak5PFJets'),
                    doJTA  = True,
                    doBTagging   = True,
                    jetCorrLabel = inputJetCorrLabel,
                    doType1MET   = False, # that doesn't work (yet in 44X)
                    genJetCollection=cms.InputTag("ak5GenJets"),
                    doJetID      = True,
                    jetIdLabel   = "ak5"
                    )

# official PU JetID sequence (approved on 28.05.2012)
process.puJetId.rho  = cms.InputTag("kt6PFJetsForIsolation:rho")
process.puJetId.jets = cms.InputTag("patJets")
process.puJetMva.rho = cms.InputTag("kt6PFJetsForIsolation:rho")
process.puJetMva.jets = cms.InputTag("patJets")

# beta and beta*, added as UserFloats (private definition, just in case)
# that producer also puts the official values as userFloats
process.patJetsWithBeta = cms.EDProducer('JetBetaProducer',
   src = cms.InputTag("patJets"),
   primaryVertices = cms.InputTag("goodPV"),
   puJetIdMVA = cms.InputTag("puJetMva","fullDiscriminant"),
   puJetIdFlag = cms.InputTag("puJetMva","fullId"),
   puJetIdentifier = cms.InputTag("puJetId"),
)
process.selectedPatJets.src      = cms.InputTag("patJetsWithBeta")
process.selectedPatJets.cut      = 'pt > 20. & abs(eta) < 2.4 '
process.patJets.addTagInfos = cms.bool( True )

# b-jets
#Let the possibility to skim the PAT with either CSV, JP or SSV
#WP : SSVHEM, JPL, CSVL for 44X
#more info at : https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagPerformanceOP and https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookBTagging
process.bjets =    process.cleanPatJets.clone( preselection = 'bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 1.74' )
process.CSVbjets = process.cleanPatJets.clone( preselection = 'bDiscriminator("combinedSecondaryVertexBJetTags") > 0.244' )
process.JPbjets =  process.cleanPatJets.clone( preselection = 'bDiscriminator("jetProbabilityBJetTags") > 0.275' )

process.filterbjets = process.countPatJets.clone(src= "bjets", minNumber = 2)
    
# combined objects
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

#################################################
###### MET ######################################
#################################################

process.selectedPatJetsForMETtype1p2Corr.src = cms.InputTag('selectedPatJets')
process.patPFJetMETtype1p2Corr.type1JetPtThreshold = cms.double(10.0)
process.patPFJetMETtype1p2Corr.skipEM = cms.bool(False)
process.patPFJetMETtype1p2Corr.skipMuons = cms.bool(False)

# this is to add the various corrections to the MET that we use.
process.patType1CorrectedPFMet.srcType1Corrections = cms.VInputTag(
   cms.InputTag('patPFJetMETtype1p2Corr', 'type1'), #type1
)

process.patType01CorrectedPFMet = process.patType1CorrectedPFMet.clone(
   srcType1Corrections = cms.VInputTag(
     cms.InputTag('patPFJetMETtype1p2Corr', 'type1'), #type1
     cms.InputTag('patPFMETtype0Corr'),               #type0
   )
)

process.patType1SCorrectedPFMet = process.patType1CorrectedPFMet.clone(
   srcType1Corrections = cms.VInputTag(
     cms.InputTag('patPFJetMETtype1p2Corr', 'type1'), #type1
     cms.InputTag('pfMEtSysShiftCorr')                #sysShift
   )
)

process.patType01SCorrectedPFMet = process.patType1CorrectedPFMet.clone(
   srcType1Corrections = cms.VInputTag(
     cms.InputTag('patPFJetMETtype1p2Corr', 'type1'), #type1
     cms.InputTag('patPFMETtype0Corr'),               #type0
     cms.InputTag('pfMEtSysShiftCorr')                #sysShift
   )
)

# for data, add residual correctionand disable GetMET
if not isMC:
  process.patPFJetMETtype1p2Corr.jetCorrLabel = 'L2L3Residual'
  process.patPFMet.addGenMET = cms.bool(False)

# select the proper SysShift correction
if isMC:
  process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2011runAplusBvsNvtx_mc
else:
  process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2011runAplusBvsNvtx_data

# standard (raw) MET
from PhysicsTools.PatAlgos.tools.metTools import *
addPfMET(process, 'PF')

# for MET systematics: adds ~10 variants of type1-corrected MET
#from PhysicsTools.PatUtils.tools.metUncertaintyTools import runMEtUncertainties
#runMEtUncertainties(process)
     
# MET sequence
process.producePatPFMETobjectWithCorrections = cms.Sequence(
    process.patPFMet
    * process.type0PFMEtCorrection
    * process.patPFMETtype0Corr
    * process.pfMEtSysShiftCorrSequence
    * process.selectedPatJetsForMETtype1p2Corr
    * process.patPFJetMETtype1p2Corr
    * process.patType1CorrectedPFMet
    * process.patType01CorrectedPFMet
    * process.patType1SCorrectedPFMet
    * process.patType01SCorrectedPFMet
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
##      OUTPUT      ##
######################

process.out.fileName = cms.untracked.string('/storage/data/cms/store/user/acaudron/ZAsamples/pat2_A125_H0475/PATprod-MC.root')

process.out.outputCommands = cms.untracked.vstring( 'drop *' )
                                   ### vertex, incl. Torino's Z vertex producer and mergeable counter ----------------------
process.out.outputCommands.extend(['keep *_offlinePrimaryVertices*_*_*',
                                   'keep *_goodPV*_*_*',
                                   'keep *_offlinePrimaryVertexFromZ_*_*',
                                   'keep edmMergeableCounter_*_*_*',
                                   'keep *_offlineBeamSpot*_*_*',
                                   ### for Torino's studies on SV ----------------------------------------------------------
                                   'keep recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector_*_*_*',
                                   'keep recoBaseTagInfosOwned_selectedPatJets_tagInfos_PAT',
                                   'keep recoBaseTagInfosOwned_patJets_tagInfos_PAT',
                                   'keep recoSecondaryVertexTagInfos_secondaryVertexTagInfosAK5PFOffset__PAT',
                                   'keep recoSecondaryVertexTagInfos_secondaryVertexTagInfosAOD__PAT',
                                   'keep recoBaseTagInfosOwned_selectedPatJetsAK5PFOffset_tagInfos_PAT',
                                   'keep recoBaseTagInfosOwned_patJetsAK5PFOffset_tagInfos_PAT',
                                   ### Trigger -----------------------------------------------------------------------------
                                   'keep *_patTriggerEvent_*_*',
                                   'keep patTriggerPaths_patTrigger_*_*',
                                   ### Tracks ------------------------------------------------------------------------------
                                   'keep *_*Tracks_*_*',
                                   ### muons -------------------------------------------------------------------------------
                                   'keep *_*Muons*_*_*',
                                   ### electrons, incl. isolation deposits/ conversions for isolation/ID -------------------
                                   'keep *_*Electrons*_*_*',
                                   'keep *_elPFIso*_*_*',
                                   'keep *_allConversions_*_*',  ## maybe useless?
                                   ### Z candidates ------------------------------------------------------------------------
                                   'keep *_z*_*_*',
                                   ### Jets and b-jets ---------------------------------------------------------------------
                                   'keep *_*atJets*_*_*',
                                   'keep *_*5PFJets*_*_*',
                                   'keep *_puJetId_*_*',
                                   'keep *_puJetMva_*_*',
                                   'keep *_*bjets*_*_*',
                                   'keep *_simpleSecondaryVertex*BJetTags*_*_PAT',
                                   'keep *_combinedSecondaryVertexBJetTags*_*_PAT',
                                   'keep *_jetProbabilityBJetTags*_*_PAT',
                                   ### rho corrections saved ---------------------------------------------------------------
                                   'keep *_kt6PFJetsForIsolation_*_*',
                                   ### MET ---------------------------------------------------------------------------------
                                   'keep *_pat*METs*_*_*',
                                   'keep *_patMETs*_*_*',
                                   'keep *_patType1CorrectedPFMet*_*_*',
                                   'keep *_patType01CorrectedPFMet*_*_*',
                                   'keep *_patType1SCorrectedPFMet*_*_*',
                                   'keep *_patType01SCorrectedPFMet*_*_*',
                                   'drop *_selectedPatJetsForMETtype1p2Corr_*_*',
                                   # MC ------------------------------------------------------------------------------------
                                   'keep GenEventInfoProduct_generator_*_*',
                                   'keep *_genMetTrue_*_*',
                                   'keep recoGenJets_ak5GenJets_*_*',
                                   'keep *_addPileupInfo_*_*',
                                   'keep LHEEventProduct_*_*_*',
                                   'keep *_genParticles_*_*'
                                   ])
process.out.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('PFmuon','PFelectron'))

######################
##    SEQUENCES     ##
######################

process.patDefaultSequence.replace(process.selectedPatMuons,cms.Sequence(process.selectedPatMuons+process.selectedMuonsWithIsolationData))
process.patDefaultSequence.replace(process.selectedPatElectrons,cms.Sequence(process.selectedPatElectrons+process.selectedElectronsWithIsolationData))
process.patDefaultSequence.replace(process.patJets,cms.Sequence(process.patJets+process.puJetIdSqeuence+process.patJetsWithBeta))

process.PFmuon = cms.Path(
    process.TotalEventCounter*
    process.goodPV*                                            ## Primary vertex
    process.simpleEleIdSequence*
    process.pfNoPileUpSequence*
    process.pfParticleSelectionSequence*
    process.eleIsoSequence*
    process.muIsoSequence*
    process.pfAllNeutralHadrons*
    process.pfAllChargedHadrons*
    process.pfAllPhotons*
    process.pfMuonSequence* 
    process.pfElectronSequence*
    (process.kt4PFJets+process.kt6PFJets+process.ak5PFJets)*   ## reco jets
    process.kt6PFJetsForIsolation*                             ##
    (process.preMuonSequence * process.preElectronSequence)*
    process.patDefaultSequence*
    process.producePatPFMETobjectWithCorrections*              ## MET with various corrections
    process.bjets*                                             ## our b jets
    process.CSVbjets*
    process.JPbjets* 
    process.patElectronsWithTrigger *                          ## Include trigger matching
    process.allElectrons*                                      ## our final electron collection: all electrons
    process.tightElectrons*                                    ## our final electron collection: tight electrons
    process.matchedElectrons*                                  ## our final electron collection: matched electrons
    process.allMuons*                                          ## our final muon collection: all muons
    process.tightMuons*                                        ## our final muon collection: tight muons
    process.matchedMuons*                                      ## our final muon collection: matched muons
    (process.zelAllelAll+                                      ## the Z candidates
     process.zelTightelTight+                                  ##
     process.zelMatchedelMatched+                              ##
     process.zmuAllmuAll+                                      ##
     process.zmuTightmuTight+                                  ##
     process.zmuMatchedmuMatched)*                             ##
    process.offlinePrimaryVertexFromZ*                         ## Offline PV from Z for Torino's analysis
    (process.zmmj+process.zeej+process.zmmb+process.zeeb)*     ## the Z+j and Z+b candidates
    process.ZMMFilter                                          ## Final filter on the presence of Z->mm
    )

process.PFelectron = cms.Path(
    process.TotalEventCounter*
    process.goodPV*                                            ## Primary vertex
    process.simpleEleIdSequence*
    process.pfNoPileUpSequence*
    process.pfParticleSelectionSequence*
    process.eleIsoSequence*
    process.muIsoSequence*
    process.pfAllNeutralHadrons*
    process.pfAllChargedHadrons*
    process.pfAllPhotons*
    process.pfMuonSequence* 
    process.pfElectronSequence*
    (process.kt4PFJets+process.kt6PFJets+process.ak5PFJets)*   ## reco jets
    process.kt6PFJetsForIsolation*                             ##
    (process.preMuonSequence * process.preElectronSequence)*
    process.patDefaultSequence*
    process.producePatPFMETobjectWithCorrections*              ## MET with various corrections
    process.bjets*                                             ## our b jets
    process.CSVbjets*
    process.JPbjets*
    process.patElectronsWithTrigger *                          ## Include trigger matching
    process.allElectrons*                                      ## our final electron collection: all electrons
    process.tightElectrons*                                    ## our final electron collection: tight electrons
    process.matchedElectrons*                                  ## our final electron collection: matched electrons
    process.allMuons*                                          ## our final muon collection: all muons
    process.tightMuons*                                        ## our final muon collection: tight muons
    process.matchedMuons*                                      ## our final muon collection: matched muons
    (process.zelAllelAll+                                      ## the Z candidates
     process.zelTightelTight+                                  ##
     process.zelMatchedelMatched+                              ##
     process.zmuAllmuAll+                                      ##
     process.zmuTightmuTight+                                  ##
     process.zmuMatchedmuMatched)*                             ##
    process.offlinePrimaryVertexFromZ*                         ## Offline PV from Z for Torino's analysis
    (process.zmmj+process.zeej+process.zmmb+process.zeeb)*     ## the Z+j and Z+b candidates
    process.ZEEFilter                                          ## Final filter on the presence of Z->mm
    )

#####################
###  OUTPATH    #####
#####################

process.outpath = cms.EndPath(process.out)

