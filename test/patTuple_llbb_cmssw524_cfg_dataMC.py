import FWCore.ParameterSet.Config as cms
#import os
process = cms.Process("ZplusJets")

#electron and muons approvals : https://indico.cern.ch/conferenceDisplay.py?confId=193787
#Muons : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId , https://twiki.cern.ch/twiki/bin/view/CMS/MuonHLT
#electrons : https://twiki.cern.ch/twiki/bin/view/CMS/EgammaEARhoCorrection , https://twiki.cern.ch/twiki/bin/view/CMS/EgammaCutBasedIdentification , https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaPFBasedIsolation

#jet and met approvals : https://indico.cern.ch/conferenceDisplay.py?confId=172447
#MET : https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMetAnalysis , https://twiki.cern.ch/twiki/bin/view/CMS/MissingET
#Jet : https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections , https://twiki.cern.ch/twiki/bin/view/CMS/JetID , https://twiki.cern.ch/twiki/bin/view/CMS/PileupJetID 

#trigger : http://fwyzard.web.cern.ch/fwyzard/hlt/summary

#packages for 52X : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePATReleaseNotes52X
#444pat : https://twiki.cern.ch/twiki/bin/view/CMSPublic/LeptonSelectionVjets2011

#packages are for 532patch4, should work also in 533patch2 
#--- Tag ---    -------- Package --------
#V00-02-09      CMGTools/External
#V00-03-16      CommonTools/ParticleFlow
#V00-03-23      CommonTools/RecoAlgos
#V00-00-13      CommonTools/RecoUtils
#V02-06-05      DataFormats/HLTReco
#V15-03-03      DataFormats/ParticleFlowCandidate
#V00-02-14      DataFormats/StdDictionaries
#V10-02-02      DataFormats/TrackReco
#V02-00-04      DataFormats/VertexReco
#V00-00-18      EGamma/EGammaAnalysisTools
#V04-06-09      JetMETCorrections/Type1MET
#V08-09-23      PhysicsTools/PatAlgos
#V03-09-23      PhysicsTools/PatUtils
#NoTag          UserCode/zbb_louvain
#NoTag          ZbbAnalysis/AnalysisStep
#NoTag          ZbbAnalysis/Tools
#---------------------------------------

#leptons : check triggers prescaled

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
                               fileName = cms.untracked.string('pat_8TeV2012.root'),
                                                              # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p1','p2') ),
                                                              # save PAT Layer 1 output; you need a '*' to
                                                              # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('drop *',
                                                                      'keep *_offlinePrimaryVertices*_*_*',
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
                                                                      'keep *_combinedInclusiveSecondaryVertexBJetTags*_*_PAT',
                                                                      'keep *_jetProbabilityBJetTags*_*_PAT',
                                                                      ### rho corrections saved ---------------------------------------------------------------
                                                                      'keep *_kt6PFJets*_*_*',
                                                                      ### MET ---------------------------------------------------------------------------------
                                                                      'keep *_pat*METs*_*_*',
                                                                      'keep *_pf*CorrectedMet*_*_*',
                                                                      'keep *_pat*CorrectedPFMet*_*_*',
                                                                      'drop *_selectedPatJetsForMETtype1p2Corr_*_*',
                                                                      # MC ------------------------------------------------------------------------------------
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

readFiles = cms.untracked.vstring()
readFiles.extend([
       #'/store/data/Run2012A/DoubleElectron/RECO/PromptReco-v1/000/190/705/6C49578C-A083-E111-A629-5404A63886E6.root'
       #'/store/data/Run2012A/DoubleMu/RECO/PromptReco-v1/000/190/645/F0D69742-8A82-E111-ABDE-BCAEC518FF30.root'
       #'/store/data/Run2012A/DoubleMu/RECO/PromptReco-v1/000/190/645/F0D69742-8A82-E111-ABDE-BCAEC518FF30.root',
       #'/store/data/Run2012A/DoubleMu/RECO/PromptReco-v1/000/190/645/DCAE2B35-8B82-E111-A830-00215AEDFCCC.root'
      #'/store/relval/CMSSW_5_2_3_patch3/RelValTTbar/GEN-SIM-RECO/START52_V9_special_120410-v1/0122/4C156E86-1183-E111-BED9-003048FFCBF0.root'
        #'file:/storage/data/cms/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/0AE169B1-01D3-E111-9939-001E673968F1.root'
        'file:/storage/data/cms/store/data/Run2012B/SingleMu/AOD/13Jul2012-v1/0000/06FBAF11-AED3-E111-8C52-90E6BA0D09BB.root'
    ])

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport  = cms.untracked.PSet(reportEvery = cms.untracked.int32(1000))
process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32(-1) )
process.source = cms.Source("PoolSource",
                            fileNames = readFiles,
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            )

############LOAD PART.2####################
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger(process,sequence='patDefaultSequence',hltProcess = '*')

from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.jetTools import *
process.load('CommonTools.ParticleFlow.pfParticleSelection_cff') 

########################
## Standard Modules  ###
########################
## Load standard Reco modules
process.load("Configuration.Geometry.GeometryIdeal_cff")
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
##-------------------- Working point and electron ID for 2011 ------------
process.load("RecoLocalCalo/EcalRecAlgos/EcalSeverityLevelESProducer_cfi")
process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff") ##somthing to change ?
##-------------------- Import the JEC services ---------------------------
process.load("JetMETCorrections.Configuration.DefaultJEC_cff")
process.load("JetMETCorrections.Configuration.JetCorrectionServices_cff")
process.load("JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff")
process.load("JetMETCorrections.Configuration.JetCorrectionProducers_cff")
##-------------------- load the PU JetID sequence ------------------------
process.load("CMGTools.External.pujetidsequence_cff")
##-------------------- load MET sequences --------------------------------
process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")
process.load("JetMETCorrections.Type1MET.pfMETCorrectionType0_cfi")
process.load("JetMETCorrections.Type1MET.pfMETsysShiftCorrections_cfi")
process.load("PhysicsTools.PatUtils.patPFMETCorrections_cff")
##------------------------------------------------------------------------
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

#######Option MC or DATA
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ()
# setup any defaults you want
options.register('boolMC',
                 0, # default value
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.int,         # string, int, or float
                 "MC flag")

options.parseArguments()
isMC = bool(options.boolMC)

###remove MC matching for DATA and use the good collection for muons for MC
if not isMC : removeMCMatching(process, ['All'])
else : process.muonMatch.src = "pfIsolatedMuons"

process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(False),
                                     makeTriggerResults=cms.untracked.bool(False),
                                     )

if isMC :
    process.GlobalTag.globaltag = 'START53_V7A::All'
else :    
    process.GlobalTag.globaltag = 'FT_53_V6_AN1::All'

#import FWCore.PythonUtilities.LumiList as LumiList
#import FWCore.ParameterSet.Types as CfgTypes
#myLumis = LumiList.LumiList(filename = 'Cert_190456-190688_8TeV_PromptReco_Collisions12_JSON.txt').getCMSSWString().split(',')
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#process.source.lumisToProcess.extend(myLumis)

##########################
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

######################
#### VERTEX FILTER ###
######################

#from https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#JetEnCor2012V2
from PhysicsTools.SelectorUtils.pvSelector_cfi import pvSelector
process.goodPV = cms.EDFilter(
    "PrimaryVertexObjectFilter",
    filterParams = pvSelector.clone( minNdof = cms.double(4.0), maxZ = cms.double(24.0) ),
    src=cms.InputTag('offlinePrimaryVertices')
    )
#replace the PV sequence
process.patPF2PATSequence = cms.Sequence( process.patDefaultSequence )
adaptPVs(process, pvCollection="goodPV")

process.pfPileUp.PFCandidates = cms.InputTag("particleFlow")
process.pfNoPileUp.bottomCollection = cms.InputTag("particleFlow")

from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFElectronIso, setupPFMuonIso
process.eleIsoSequence = setupPFElectronIso(process, 'gsfElectrons')
process.muIsoSequence = setupPFMuonIso(process, 'muons')

###########################
#### ELECTRON selection ###
###########################
#cvs co -r V00-00-18 -d EGamma/EGammaAnalysisTools UserCode/EGamma/EGammaAnalysisTools

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

process.pfIsolatedElectrons.isolationCut = 0.5 ### TBC

#https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaPFBasedIsolation#Recommended_electron_vetoes_Upda
process.load("RecoParticleFlow.PFProducer.electronPFIsolationValues_cff")
process.elPFIsoValueCharged03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.015)')
process.elPFIsoValueChargedAll03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.015)')
process.elPFIsoValuePU03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.015)')
process.elPFIsoValueGamma03NoPFId.deposits[0].vetos =cms.vstring('EcalEndcaps:ConeVeto(0.08)')

process.pfAllElectrons.src = "particleFlow" # default = pfNoMuons

## Electrons with UserData ###############################
process.selectedElectronsWithIsolationData = cms.EDProducer(
   "ElectronIsolationEmbedder",
   src = cms.InputTag("selectedPatElectrons"),
   rho = cms.InputTag("kt6PFJets:rho"),
   PFCandidateMap = cms.InputTag('particleFlow:electrons'),
   gsfElectrons = cms.InputTag('gsfElectrons'),
   conversions = cms.InputTag('allConversions'),
   beamSpot = cms.InputTag('offlineBeamSpot'),
   primaryVertex = cms.InputTag('offlinePrimaryVertices'),
   IsoValElectronNoPF = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03NoPFIdPFIso'),
                                      cms.InputTag('elPFIsoValueGamma03NoPFIdPFIso'),
                                      cms.InputTag('elPFIsoValueNeutral03NoPFIdPFIso')),
   IsoDepElectron = cms.VInputTag(cms.InputTag('elPFIsoDepositChargedPFIso'),
                                  cms.InputTag('elPFIsoDepositGammaPFIso'),
                                  cms.InputTag('elPFIsoDepositNeutralPFIso')),
)


#################################
### ELECTRON trigger matching ###
#################################
#check trigger for 2012 : still ok, used by H->ZZ->4l : https://twiki.cern.ch/twiki/bin/view/CMS/HZZTriggers2012
pathTriggerEle ='path("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,0) && filter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter")'

process.eleTriggerMatchHLT = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                             src     = cms.InputTag( "selectedElectronsWithIsolationData" ),
                                             matched = cms.InputTag( "patTrigger"),
                                             matchedCuts = cms.string(pathTriggerEle),
                                             maxDPtRel = cms.double( 0.5 ),
                                             maxDeltaR = cms.double( 0.3 ),
                                             resolveAmbiguities    = cms.bool( True ),
                                             resolveByMatchQuality = cms.bool( True )
                                             )

process.patElectronsWithTrigger = cms.EDProducer("PATTriggerMatchElectronEmbedder",
                                                 src     = cms.InputTag("selectedElectronsWithIsolationData"),
                                                 matches = cms.VInputTag(cms.InputTag('eleTriggerMatchHLT'))
                                                 )

switchOnTriggerMatching( process, ['eleTriggerMatchHLT' ],sequence ='patDefaultSequence', hltProcess = '*' )

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
#The patDefaultSequence takes the pfIsolatedMuons as default input collection. To change the input collection one can use:
#process.patMuons.pfMuonSource = cms.InputTag("pfMuons")  
#Then one can use the selectedPatMuons as collection and it will have the trigger matching embedded and it can also be used to build the Z candidate. 

process.patMuons.pfMuonSource = cms.InputTag("pfIsolatedMuons")
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

### Muons with isolation data embedded
process.selectedMuonsWithIsolationData = cms.EDProducer(
   "MuonIsolationEmbedder",
   src = cms.InputTag("selectedPatMuons"),
   rho = cms.InputTag("kt6PFJets:rho")
)

#add muon cuts
#check here for values: CommonTools/ParticleFlow/python/Isolation/pfIsolatedMuons_cfi.py
#check here for values of the isolation deposits:  RecoMuon/MuonIsolation/python/muonPFIsolationValues_cff.py
# DEFAULT ones are: muPFIsoValueCharged04/muPFIsoValueNeutral04/muPFIsoValueGamma04...

process.pfIsolatedMuons.isolationCut = 0.5

#################################
### MUON Trigger matching #######
#################################
#https://twiki.cern.ch/twiki/bin/view/CMS/MuonHLT#2012_Runs
#Selection OK : need only to check if trigger became prescaled
pathTriggerMu = 'path("HLT_Mu17_Mu8_v*",0,1)'# || path("HLT_Mu17_TkMu8_v*",0,1)'

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

process.allMuons = selectedPatMuons.clone(
    src = cms.InputTag('selectedPatMuonsTriggerMatch'),
    cut = cms.string("pt>20  & abs(eta) < 2.4")    
    )


process.tightMuons = selectedPatMuons.clone(
   src = cms.InputTag('selectedPatMuonsTriggerMatch'),
   cut = cms.string('isGlobalMuon &'
                    'isPFMuon &'
                    'innerTrack.hitPattern.trackerLayersWithMeasurement>5 &'
                    #fabs(recoMu.innerTrack()->dz(vertex->position())) < 0.5  # to be applied offline ?
                    'userFloat("RelativePFIsolationDBetaCorr") < 0.2 &' # PF isolation
                    'abs(dB) < 0.02 &' 
                    'normChi2 < 10 &'
                    'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                    'numberOfMatchedStations>1 &'                                 
                    'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                    'pt>20 &'
                    'abs(eta) < 2.4')
   )

if not isMC:
    process.matchedMuons = process.tightMuons.clone(
        src = cms.InputTag('selectedPatMuonsTriggerMatch'),
        cut = cms.string('triggerObjectMatches.size > 0')
        )
else:
    process.matchedMuons = process.tightMuons.clone(
        src = cms.InputTag('selectedPatMuonsTriggerMatch'),
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

process.zmuMatchedTrigmuMatchedTrig = cms.EDProducer('CandViewShallowCloneCombiner',
                                  decay = cms.string('matchedMuonsTrig@+ matchedMuonsTrig@-'),
                                  cut   = cms.string('mass >12.0'),
                                  name  = cms.string('Zmumatchedtrigmumatchedtrig'),
                                  roles = cms.vstring('matchedtrig1', 'matchedtrig2')
                                  )


#################################################
#### JETS #######################################
#################################################

process.load('RecoJets.Configuration.RecoPFJets_cff')
process.ak5PFJets.doAreaFastjet = True

inputJetCorrLabel = ('AK5PF',['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual'])
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

# official PU JetID sequence (approved on 28.05.2012)
process.puJetId.rho  = cms.InputTag("kt6PFJets:rho")
process.puJetId.jets = cms.InputTag("patJets")
process.puJetMva.rho = cms.InputTag("kt6PFJets:rho")
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
from PhysicsTools.PatAlgos.tools.metTools import *
addPfMET(process, 'PF')

# for MET systematics: adds ~10 variants of type1-corrected MET
from PhysicsTools.PatUtils.tools.metUncertaintyTools import runMEtUncertainties
if isMC : runMEtUncertainties(process)
else : process.patPFMet.addGenMET = cms.bool(False)

process.selectedPatJetsForMETtype1p2Corr.src = cms.InputTag('selectedPatJets')
process.patPFJetMETtype1p2Corr.type1JetPtThreshold = cms.double(10.0)
process.patPFJetMETtype1p2Corr.skipEM = cms.bool(False)
process.patPFJetMETtype1p2Corr.skipMuons = cms.bool(False)
process.patType1p2CorrectedPFMet.srcType1Corrections = cms.VInputTag(    
    cms.InputTag('patPFJetMETtype1p2Corr', 'type1'),
    cms.InputTag('patPFMETtype0Corr')             
)

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
##    SEQUENCES     ##
######################

process.patDefaultSequence.replace(process.selectedPatMuons,cms.Sequence(process.selectedPatMuons+process.selectedMuonsWithIsolationData))
process.patDefaultSequence.replace(process.selectedPatElectrons,cms.Sequence(process.selectedPatElectrons+process.selectedElectronsWithIsolationData))
process.patDefaultSequence.replace(process.patJets,cms.Sequence(process.patJets+process.puJetIdSqeuence+process.patJetsWithBeta))
if not isMC : process.patDefaultSequence.replace(process.patTrigger,process.patTrigger*process.producePatPFMETobjectWithCorrections)
else : process.patDefaultSequence.replace(process.patPFMet,process.producePatPFMETobjectWithCorrections)

process.PFLeptons = cms.Sequence(
    process.TotalEventCounter*
    process.goodPV *
    process.ak5PFJets *
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
    (process.preMuonSequence * process.preElectronSequence)*
    process.patPF2PATSequence *
    # this is to add the various corrections to the MET that we use.
    #process.producePatPFMETobjectWithCorrections *
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
    (process.zmmj+process.zeej+process.zmmb+process.zeeb)      ## the Z+j and Z+b candidates
    )

process.p1 = cms.Path(process.PFLeptons*process.ZMMFilter)
process.p2 = cms.Path(process.PFLeptons*process.ZEEFilter)

#####################
###  OUTPATH    #####
#####################

process.outpath = cms.EndPath(
    process.out
    )
