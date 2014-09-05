import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.trigTools import *
from triggerList import singleElePath, doubleElePath, MuEGPath

def setupPatElectrons (process, runOnMC, ElePt = 8.):
    process.eleIsoSequence = setupPFElectronIso(process, 'gsfElectrons', 'PFIso')
    process.patElectrons.pfElectronSource = cms.InputTag("pfSelectedElectrons")

    #Add MVA Id
    process.load('EgammaAnalysis.ElectronTools.electronIdMVAProducer_cfi')
    process.mvaID = cms.Sequence(process.mvaNonTrigV0 + process.mvaTrigV0 + process.mvaTrigNoIPV0)
    #Electron ID
    process.patElectrons.electronIDSources = cms.PSet(
        #MVA
        mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0"),
        mvaTrigV0 = cms.InputTag("mvaTrigV0"),
        mvaTrigNoIPV0 = cms.InputTag("mvaTrigNoIPV0")
        )

    #electron momentum scale
    process.load("EgammaAnalysis.ElectronTools.electronRegressionEnergyProducer_cfi")
    process.eleRegressionEnergy.inputElectronsTag = cms.InputTag('patElectrons')
    process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
                                                       calibratedPatElectrons = cms.PSet(
                                                         initialSeed = cms.untracked.uint32(975312468),
                                                         engineName = cms.untracked.string('TRandom3')
                                                         )
                                                       )
    process.load("EgammaAnalysis.ElectronTools.calibratedPatElectrons_cfi")
    if runOnMC: # For MC need to change defauls
        process.calibratedPatElectrons.isMC = runOnMC
        process.calibratedPatElectrons.inputDataset = cms.string("Summer12_LegacyPaper")
        process.calibratedPatElectrons.lumiRatio = 0.607
    process.selectedPatElectrons.src = cms.InputTag("calibratedPatElectrons")

    #what about: https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaPFBasedIsolation#Current_version_previously_known , something to do or correctedin releases
    process.load("RecoParticleFlow.PFProducer.electronPFIsolationValues_cff")
    process.selectedElectronsWithIsolationData = cms.EDProducer(
        "ElectronIsolationEmbedder",
        src = cms.InputTag("selectedPatElectrons"),
        rho = cms.InputTag("kt6PFJets:rho"),
        PFCandidateMap = cms.InputTag('particleFlow:electrons'),
        gsfElectrons = cms.InputTag('gsfElectrons'),
        conversions = cms.InputTag('allConversions'),
        beamSpot = cms.InputTag('offlineBeamSpot'),
        primaryVertex = cms.InputTag('offlinePrimaryVertices'),
        IsoValElectronNoPF = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03NoPFIdPFIso'), #use PFIdPFIso or NoPFIdPFIso: second one make more sense but no eplicit documentation about it, both producer take the same inputs then they are probably just the same
                                           cms.InputTag('elPFIsoValueGamma03NoPFIdPFIso'),
                                           cms.InputTag('elPFIsoValueNeutral03NoPFIdPFIso')),
        IsoDepElectron = cms.VInputTag(cms.InputTag('elPFIsoDepositChargedPFIso'),
                                       cms.InputTag('elPFIsoDepositGammaPFIso'),
                                       cms.InputTag('elPFIsoDepositNeutralPFIso')),
           )
    
    #process.eleTriggerMatchHLT = cms.EDProducer( "PATTriggerMatcherDRLessByR",
    #src = cms.InputTag( "selectedPatElectrons" ),
    #matched = cms.InputTag( "patTrigger"),
    #matchedCuts = cms.string('path( "HLT_*Ele*_*" )'),
    #maxDPtRel = cms.double( 0.5 ),
    #maxDeltaR = cms.double( 0.3 ),
    #resolveAmbiguities = cms.bool( True ),
    #resolveByMatchQuality = cms.bool( True )
    #)

    triggerMatchersList = []
    process.triggerMatchingSeq = cms.Sequence()
    for HLTEle in singleElePath+doubleElePath+MuEGPath :
        matcher = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                  src = cms.InputTag( "selectedPatElectrons" ),
                                  matched = cms.InputTag( "patTrigger"),
                                  matchedCuts = cms.string(HLTEle),
                                  maxDPtRel = cms.double( 0.5 ),
                                  maxDeltaR = cms.double( 0.3 ),
                                  resolveAmbiguities = cms.bool( True ),
                                  resolveByMatchQuality = cms.bool( True )
                                  )
        setattr(process,'eleTriggerMatchHLT'+HLTEle[6:-5].replace("_",""),matcher)
        triggerMatchersList.append('eleTriggerMatchHLT'+HLTEle[6:-5].replace("_",""))
        process.triggerMatchingSeq += getattr(process,'eleTriggerMatchHLT'+HLTEle[6:-5].replace("_",""))
        
    switchOnTriggerMatchEmbedding(process ,triggerMatchers = triggerMatchersList,)
    #process.eleTriggerMatchHLT.src = cms.InputTag("selectedElectronsWithIsolationData")
    for HLTEle in singleElePath+doubleElePath+MuEGPath : getattr(process,'eleTriggerMatchHLT'+HLTEle[6:-5].replace("_","")).src = cms.InputTag("selectedElectronsWithIsolationData")
        
    process.patElectronsWithTrigger = cms.EDProducer("PATTriggerMatchElectronEmbedder",
                                                     src = cms.InputTag("selectedElectronsWithIsolationData"),
                                                     matches = cms.VInputTag(triggerMatchersList)
                                                     )
    
    #switchOnTriggerMatching( process, ['eleTriggerMatchHLT' ],sequence ='patDefaultSequence', hltProcess = '*' ) #needed ?? seems not
    
    process.allElectrons = process.selectedPatElectrons.clone( cut = "pt > "+str(ElePt)+" && abs(eta) < 2.5")
    process.allElectrons.src = "patElectronsWithTrigger"

    if runOnMC:
        process.tightElectrons = process.selectedPatElectrons.clone(
            src = "allElectrons",
            cut =
            'userInt("MediumWP")==1 &' #Medium WP agreed in June 2012
            'userFloat("PFIsoPUCorrectedMC") < 0.15' # isolation for MC
            )
        process.tightMVAElectronsNonTrig = process.selectedPatElectrons.clone(
            src = "allElectrons",
            cut =
            'electronID("mvaNonTrigV0")>0.5 &' #from top analysis
            'userFloat("PFIsoPUCorrectedMC") < 0.15' # isolation for MC
            )
    else :
        process.tightElectrons = process.selectedPatElectrons.clone(
            src = "allElectrons",
            cut =
            'userInt("MediumWP")==1 &' #Medium WP agreed in June 2012
            'userFloat("PFIsoPUCorrected") < 0.15' # isolation for MC
            )
        process.tightMVAElectronsNonTrig = process.selectedPatElectrons.clone(
            src = "allElectrons",
            cut =
            'electronID("mvaNonTrigV0")>0.5 &' #from top analysis  
            'userFloat("PFIsoPUCorrected") < 0.15' # isolation for MC
            )
        
    process.preElectronSeq = cms.Sequence (
        process.eleIsoSequence *
        process.pfElectronSequence *
        process.mvaID
        )
    process.PF2PAT.replace(process.pfElectronSequence,process.preElectronSeq)

    process.patDefaultSequence.replace(
        process.selectedPatElectrons,
        process.eleRegressionEnergy*process.calibratedPatElectrons*process.selectedPatElectrons*process.selectedElectronsWithIsolationData
        )

    process.postElectronSeq = cms.Sequence (
        #process.eleTriggerMatchHLT *
        process.triggerMatchingSeq *
        process.patElectronsWithTrigger *
        process.allElectrons *
        process.tightElectrons +
        process.tightMVAElectronsNonTrig
        )
    
    
    process.zelAllelAll = cms.EDProducer('CandViewShallowCloneCombiner',
                                         decay = cms.string('allElectrons@+ allElectrons@-'),
                                         cut = cms.string('mass > 10.0'),
                                         name = cms.string('Zelallelall'),
                                         roles = cms.vstring('all1', 'all2')
                                         )
    
    process.zelTightelTight = cms.EDProducer('CandViewShallowCloneCombiner',
                                             decay = cms.string('tightElectrons@+ tightElectrons@-'),
                                             cut = cms.string('mass > 10.0'),
                                             name = cms.string('Zeltighteltight'),
                                             roles = cms.vstring('tight1', 'tight2')
                                             )
    process.zmvaelTightmvaelTight = cms.EDProducer('CandViewShallowCloneCombiner',
                                             decay = cms.string('tightMVAElectronsNonTrig@+ tightMVAElectronsNonTrig@-'),
                                             cut = cms.string('mass > 10.0'),
                                             name = cms.string('Zmvaeltightmvaeltight'),
                                             roles = cms.vstring('tight1', 'tight2')
                                             )
    process.electronComposite = cms.Sequence (
        process.zelAllelAll +
        process.zelTightelTight +
        process.zmvaelTightmvaelTight
        )
    
    
