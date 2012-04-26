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

#print "isMC", isMC
#print "is8Nov", is8Nov

#isMC=False
#is8Nov=False

### Torino's counter ################

from PhysicsTools.PatAlgos.patTemplate_cfg import *

process.TotalEventCounter = cms.EDProducer("EventCountProducer")
process.TotalEventCounter = cms.EDProducer("EventCountProducer")
process.AfterPVFilterCounter = cms.EDProducer("EventCountProducer")
process.AfterNSFilterCounter = cms.EDProducer("EventCountProducer")
process.AfterPATCounter = cms.EDProducer("EventCountProducer")
process.AfterCandidatesCounter = cms.EDProducer("EventCountProducer")
process.AfterJetsCounter = cms.EDProducer("EventCountProducer")
#####################################

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
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
## Generator informations
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("Configuration.StandardSequences.Generator_cff")

from RecoJets.JetProducers.FastjetParameters_cfi import *
from RecoJets.JetProducers.ak5TrackJets_cfi import *
from RecoJets.JetProducers.GenJetParameters_cfi import *
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
process.load('RecoJets.Configuration.RecoPFJets_cff')
process.load("RecoJets.Configuration.GenJetParticles_cff")
process.load("RecoJets.Configuration.RecoGenJets_cff")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

##-------------------- Turn-on the FastJet density calculation ----------------------------------------------------
process.kt6PFJets.doRhoFastjet = True
##-------------------- Turn-on the FastJet jet area calculation for your favorite algorithm -----------------------
process.kt6PFJets.doAreaFastjet = True
process.ak5PFJets.doAreaFastjet = True

# to compute FastJet rho to correct isolation (note: EtaMax restricted to 2.5)
process.kt6PFJetsForIsolation = process.kt4PFJets.clone( rParam = 0.6 ,doRhoFastjet = True)
process.kt6PFJetsForIsolation.Rho_EtaMax = cms.double(2.5)


######### REMOVAL OF MC MATCHING

#if not isMC:
removeMCMatching(process, ['All']) ## needed also on MC? very strange...
    
process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(True),
                                         makeTriggerResults=cms.untracked.bool(True),
                                     )

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
    "file:/tmp/castello/Run2011A_DoubleElectron_AOD_08Nov2011-v1_0000_001ED292-B51B-E111-A231-001BFCDBD130.root" ### test file for electrons
    #"file:/tmp/castello/Run2011A_DoubleMu_AOD_08Nov2011-v1_0000_00011B62-381B-E111-8425-002618943810.root" ## test file for muons
    #"file:/tmp/castello/Fall11_DYJetsToLL_TuneZ2_M-50_7TeV-madgraph_PU_S6-START44_V5-v1_FE772459-D80A-E111-ABBE-E0CB4E1A1186.root" ## test file for MC Drell-Yan
    ])

process.MessageLogger.cerr.FwkReport  = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(100),  )
process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32(1000) )
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
                              ' position.Rho <2 '
                              )

###########################
#### PRE-SEQUENCES #######
##########################
if isMC:
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
#### ELECTRON ISOLATION ###
###########################

### from PF2PAT sequence...
process.pfPileUp.PFCandidates = cms.InputTag("particleFlow")
process.pfNoPileUp.bottomCollection = cms.InputTag("particleFlow")

### create the particle-based isolation values for gsfElectrons and muons
from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFElectronIso, setupPFMuonIso
process.eleIsoSequence = setupPFElectronIso(process, 'gsfElectrons')
process.muIsoSequence = setupPFMuonIso(process, 'muons')

#process.patElectrons.useParticleFlow=True
#process.load("CommonTools.ParticleFlow.Isolation.pfElectronIsolationFromDeposits_cff")
#process.isoValElectronWithNeutral.deposits[0].deltaR = 0.3  
#process.isoValElectronWithCharged.deposits[0].deltaR = 0.3  
#process.isoValElectronWithPhotons.deposits[0].deltaR = 0.3  

process.pfIsolatedElectrons.isolationCut = 0.5 ### VERY loose, true isolation done later, exploiting deposits...

### VETOs for 0.3 cone: is there an existing backporting in 44X? #######################
#process.load("RecoParticleFlow.PFProducer.electronPFIsolationValues_cff")
#process.elPFIsoValueCharged03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.015)')
#process.elPFIsoValueChargedAll03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.015)')
#process.elPFIsoValuePU03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.015)')
#process.elPFIsoValueGamma03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.08)')

### old stuff #########################################################################
#process.pfIsolatedElectrons.isolationValueMapsCharged  = cms.VInputTag(cms.InputTag("elPFIsoValueCharged03"))
#process.pfIsolatedElectrons.isolationValueMapsNeutral  = cms.VInputTag(cms.InputTag("elPFIsoValueNeutral03"),cms.InputTag("elPFIsoValueGamma03"))
##process.pfIsolatedElectrons.doDeltaBetaCorrection      = cms.bool(False)
#process.pfIsolatedElectrons.deltaBetaIsolationValueMap = cms.InputTag("elPFIsoValuePU03")

process.pfAllElectrons.src = "particleFlow" # default = pfNoMuons
# process.pfAllElectrons.src = "pfNoPileUp"
# pfIsolated electrons are input for PATelectron producer (when usePF==True)

#################################
### ELECTRON trigger matching ###
#################################

pathTriggerEle ='(path("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",0,0) && filter("hltEle17CaloIdIsoEle8CaloIdIsoPixelMatchDoubleFilter")) || (path("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,0) && filter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter"))'

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

## Working point and electron ID for 2011 ---> values updated w.r.t. 2010
process.load("RecoLocalCalo/EcalRecAlgos/EcalSeverityLevelESProducer_cfi")
process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")

#########################################################################

process.patElectrons.addElectronID = cms.bool(True)
process.patElectrons.electronIDSources = cms.PSet(
   
    simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
    simpleEleId85relIso= cms.InputTag("simpleEleId85relIso"),
    simpleEleId80relIso= cms.InputTag("simpleEleId80relIso")
    )

process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)


## Electrons with UserData for isolation ###############################
process.userDataSelectedElectrons = cms.EDProducer(
   "Higgs2l2bElectronUserData",
   src = cms.InputTag("patElectrons"),
   rho = cms.InputTag("kt6PFJetsForIsolation:rho"),
   #Electrons = cms.InputTag("gsfElectrons"),
   PFCandidateMap = cms.InputTag('particleFlow:electrons'),

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

########################################################################################

process.allElectrons = process.selectedPatElectrons.clone( cut = 'pt > 20 && abs(eta) < 2.5' ) 
process.allElectrons.src = "patElectronsWithTrigger"

process.tightElectrons = process.selectedPatElectrons.clone( cut = 
                                                  ##  WP85 2011, same as 2010+ H/E cut: https://twiki.cern.ch/twiki/bin/view/CMS/VbtfEleID2011#Basic_Cuts
                                                  'electronID("simpleEleId85relIso") == 5 &' ## passing conversion rejection and ID 
                                                  'userFloat("PFIsoPUCorrected") < 0.15 &'
                                                  '((abs(superCluster.eta)< 1.442)||((1.566<(abs(superCluster.eta)))&&((abs(superCluster.eta))<2.50))) &'
                                                  'abs(dB) < 0.02 &'
                                                  'pt>20 &'
                                                  'abs(eta) < 2.5'
                                                  )
process.tightElectrons.src = "patElectronsWithTrigger"

process.matchedElectrons = process.cleanPatElectrons.clone( preselection =
                                                   'electronID("simpleEleId85relIso") == 5 &'
                                                   'userFloat("PFIsoPUCorrected") < 0.15 &'
                                                   '((abs(superCluster.eta)< 1.442)||((1.566<(abs(superCluster.eta)))&&((abs(superCluster.eta))<2.50))) &'
                                                   'abs(dB) < 0.02 & '
                                                   'pt>20 &'
                                                   'abs(eta) < 2.5 &'
                                                   'triggerObjectMatches.size > 0'                           
                                                   )
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
#The patDefaultSequence takes the pfIsolatedMuons as default input collection. To change the input collection one can use:
#process.patMuons.pfMuonSource = cms.InputTag("pfMuons")  
#Then one can use the selectedPatMuons as collection and it will have the trigger matching embedded and it can also be used to build the Z candidate. 

process.patMuons.useParticleFlow=True


#################################
### MUON Trigger matching #######
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
    cut = cms.string("pt>20  & abs(eta) < 2.4")    
    )

process.tightMuons = selectedPatMuons.clone(
   src = cms.InputTag('selectedPatMuonsTriggerMatch'),
   cut = cms.string('isGlobalMuon & isTrackerMuon &'
                    'innerTrack.hitPattern.trackerLayersWithMeasurement>8 &'  ## new requirement in 44X due to changes in tracking
                    'userFloat("RelativePFIsolationDBetaCorr") < 0.2 &' # PF isolation
                    'abs(dB) < 0.2 &' 
                    'normChi2 < 10 &'
                    'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                    'numberOfMatchedStations>1 &'                                 
                    'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                    'pt>20 &'
                    'abs(eta) < 2.4')
   )

process.matchedMuons = selectedPatMuons.clone(
    src = cms.InputTag('selectedPatMuonsTriggerMatch'),
    cut = cms.string('isGlobalMuon & isTrackerMuon &'
                     'innerTrack.hitPattern.trackerLayersWithMeasurement>8 &'  ## new requirement in 44X due to changes in tracking
                     'userFloat("RelativePFIsolationDBetaCorr") < 0.2 &' # PF isolation   
                     'abs(dB) < 0.2 &' 
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


#add muon cuts
#check here for values: CommonTools/ParticleFlow/python/Isolation/pfIsolatedMuons_cfi.py
#check here for values of the isolation deposits:  RecoMuon/MuonIsolation/python/muonPFIsolationValues_cff.py
# DEFAULT ones are: muPFIsoValueCharged04/muPFIsoValueNeutral04/muPFIsoValueGamma04...

process.pfIsolatedMuons.isolationCut = 0.5 ## very loose, true isolation done later, exploiting deposits...
## default cone is 0.4, as recommended at: https://twiki.cern.ch/twiki/bin/view/CMS/TWikiSMP-MUO#MuORecommendations

## embedding objects

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


inputJetCorrLabel = ('AK5PF',['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual']) #  ,'L5Flavor','L7Parton'OUTDATED: do not use them!
if isMC:
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

process.selectedPatJets.cut      = 'pt > 20. & abs(eta) < 2.4 '
process.patJets.addTagInfos = cms.bool( True )

process.bjets = process.cleanPatJets.clone( preselection = 'bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 1.74' )

process.filterbjets = process.countPatJets.clone(src= "bjets", minNumber = 2)
    
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

#add MET (for PF objects)
from PhysicsTools.PatAlgos.tools.metTools import *
addPfMET(process, 'PF')

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

process.out.fileName = cms.untracked.string('PATskim-Zjets.root')

process.out.outputCommands =  cms.untracked.vstring(
    'drop *',
    )
process.out.outputCommands.extend(['keep *_offlinePrimaryVertices*_*_*',
                                   'keep *_goodPV*_*_*',
                                   'keep *_offlinePrimaryVertexFromZ_*_*', ## Torino's Z vertex producer
                                   'keep edmMergeableCounter_*_*_*', ## Torino's mergeable counter
                                   'keep *_offlineBeamSpot*_*_*',
                                   'keep *_pat*METs*_*_*',
                                   'keep *_patTriggerEvent_*_*',
                                   'keep patTriggerPaths_patTrigger_*_*',
                                   'keep *_*Tracks_*_*',

                                   ## rho corrections saved #########################
                                   
                                   'keep *_kt6PFJetsForIsolation_*_*',

                                   ### isolation deposits/ conversion information for building isolation/ID ######
                                   
                                   'keep *_elPFIso*_*_*',
                                   'keep *_allConversions_*_*',  ## maybe useless?

                                   ##################################################                                   
                                
                                   'keep *_*atJets*_*_*',
                                   #### keep candidates based on b jets
                                   'keep *_bjets*_*_*',
                                   ####################################
                                   'keep *_*5PFJets*_*_*',
                                   'keep *_z*_*_*',
                                   'keep *_*Muons*_*_*',
                                   'keep *_*Electrons*_*_*',
                                   'keep *_patMETs*_*_*',
                                   
                                   ## b-tagger ###################################
                                   
                                   'keep *_simpleSecondaryVertex*BJetTags*_*_PAT',
                                   'keep *_combinedSecondaryVertex*BJetTags*_*_PAT',

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
                                   
                                   #'keep *_*_*_PAT',
                                   #'keep *_trackCounting*BJetTags*_*_PAT'
                                   
                                   ])

process.out.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('PFmuon','PFelectron'))


######################
##    SEQUENCES     ##
######################

process.PFmuon = cms.Path(
    process.goodPV*
    process.TotalEventCounter*
    process.simpleEleIdSequence*

    ##to create the collection pfNoPileUp
    process.pfNoPileUpSequence*
    ## to create the isoVariables with pfNoPileUp
    process.pfParticleSelectionSequence*
    process.eleIsoSequence* ### check if they are alrady in the PAT default sequence
    process.muIsoSequence*

    #process.pfElectronIsolationFromDepositsSequence+
    
    process.pfAllNeutralHadrons*
    process.pfAllChargedHadrons*
    process.pfAllPhotons*

 
    process.pfMuonSequence* 
    process.pfElectronSequence*

    (process.kt4PFJets+
     process.kt6PFJets+
     process.ak5PFJets)*
    process.kt6PFJetsForIsolation*

    #process.patTrigger*
    (process.preMuonSequence * process.preElectronSequence)*
    process.patDefaultSequence*

    #### b-jets candidates #####
    process.bjets*
    ##process.filterbjets*
    
    process.userDataSelectedMuons*
    process.userDataSelectedElectrons*

    ###### electron candidates #####
    process.eleTriggerMatchHLT *
    process.patElectronsWithTrigger *
    process.allElectrons*
    process.tightElectrons*
    process.matchedElectrons*
    
    ###### muon candidates #####
    process.muonTriggerMatchHLTMuons*
    process.selectedPatMuonsTriggerMatch*
    process.allMuons*
    process.tightMuons*
    process.matchedMuons*
       
    
    #### Z candidates ##########
    (process.zelAllelAll+
     process.zelTightelTight+
     process.zelMatchedelMatched+   
     process.zmuAllmuAll+
     process.zmuTightmuTight+
     process.zmuMatchedmuMatched)*


    process.offlinePrimaryVertexFromZ*

    #### Z+jets candidates ##########
    (process.zmmj+
     process.zeej+
     process.zmmb+
     process.zeeb)*
     #process.filterbjets*
     #(process.bbbar+
     # process.zmmbb+
     # process.zeebb))*
    process.ZMMFilter
     
    )

process.PFelectron = cms.Path(
    process.goodPV*
    process.TotalEventCounter*
    process.simpleEleIdSequence*

    ##to create the collection pfNoPileUp
    process.pfNoPileUpSequence*
    ## to create the isoVariables with pfNoPileUp
    process.pfParticleSelectionSequence*
    process.eleIsoSequence* ### check if they are alrady in the PAT default sequence
    process.muIsoSequence*

    #process.pfElectronIsolationFromDepositsSequence+
    
    process.pfAllNeutralHadrons*
    process.pfAllChargedHadrons*
    process.pfAllPhotons*
 
    process.pfMuonSequence* 
    process.pfElectronSequence*

    (process.kt4PFJets+
     process.kt6PFJets+
     process.ak5PFJets)*
    process.kt6PFJetsForIsolation*

    (process.preMuonSequence * process.preElectronSequence)*
    # process.patTrigger*
    process.patDefaultSequence*

    #### b-jets candidates #####
    process.bjets*
    #process.bbbar+
    
    process.userDataSelectedMuons*
    process.userDataSelectedElectrons*

    ###### electron candidates #####
    process.eleTriggerMatchHLT *
    process.patElectronsWithTrigger *
    process.allElectrons*
    process.tightElectrons*
    process.matchedElectrons*
    
    ###### muon candidates #####
    process.muonTriggerMatchHLTMuons*
    process.selectedPatMuonsTriggerMatch*
    process.allMuons*
    process.tightMuons*
    process.matchedMuons*
    
    #### Z candidates ##########

    (process.zelAllelAll+
     process.zelTightelTight+
     process.zelMatchedelMatched+   
     process.zmuAllmuAll+
     process.zmuTightmuTight+
     process.zmuMatchedmuMatched)*

    process.offlinePrimaryVertexFromZ*

    #### Z+jets candidates ##########
    (process.zmmj+
     process.zeej+
     process.zmmb+
     process.zeeb)*
     #process.filterbjets*
     #(process.bbbar+
     # process.zmmbb+
     # process.zeebb))*
    process.ZEEFilter
    )
    

#####################
###  OUTPATH    #####
#####################

process.outpath = cms.EndPath(
    process.out
    )
