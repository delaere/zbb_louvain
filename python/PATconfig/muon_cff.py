import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.trigTools import *

def setupPatMuons (process, runOnMC):
     process.patMuons.pfMuonSource = cms.InputTag("pfSelectedMuons") #FIX: pfSelectedMuons is used instead of pfIsolatedMuons used in the ZH anlysis, reason no obvious need to use pre isolated muons -> isolation done after
     process.patMuons.useParticleFlow=True
     # embedding objects FIX: done in H to llqq  
     process.patMuons.embedTcMETMuonCorrs = False
     process.patMuons.embedCaloMETMuonCorrs = False
     process.patMuons.embedTrack = True
     #FIX: not done in H to llqq
     process.patMuons.embedCombinedMuon = cms.bool(True)
     process.patMuons.embedStandAloneMuon = cms.bool(False)
     process.patMuons.embedPickyMuon = cms.bool(False)
     process.patMuons.embedTpfmsMuon = cms.bool(False)
     process.patMuons.embedPFCandidate = cms.bool(True) 

     #important for MCtruth matching
     if runOnMC : process.muonMatch.src = "pfSelectedMuons"

     # use PFIsolation
     process.muIsoSequence = setupPFMuonIso(process, 'muons', 'PFIso')
     #adaptPFIsoMuons( process, applyPostfix(process,"patMuons",""), 'PFIso') #FIX: done in H to llqq
           
     # MuscleFit for muons:
          
     # identifier of the MuScleFit is Data2012_53X_ReReco for data
     # and Summer12_DR53X_smearReReco for MC (to compare with ReReco data)
     muscleid = 'Data2012_53X_ReReco'
     if runOnMC : muscleid = 'Summer12_DR53X_smearReReco'
     
     process.MuScleFit = cms.EDProducer("MuScleFitPATMuonCorrector",
                                        src = cms.InputTag("patMuons"),
                                        debug = cms.bool(False),
                                        identifier = cms.string(muscleid),
                                        applySmearing = cms.bool(runOnMC), # Must be false in data
                                        fakeSmearing = cms.bool(False),
                                        )
     process.selectedPatMuons.src = cms.InputTag("MuScleFit")
     

     process.selectedPatMuons.cut = (
         "pt > 18 && abs(eta) < 2.4"
         )

     # Classic Muons with UserData
     process.selectedMuonsWithIsolationData = cms.EDProducer("MuonIsolationEmbedder",
         src = cms.InputTag("selectedPatMuons"),
         rho = cms.InputTag("kt6PFJets:rho"),
         )

     process.muonTriggerMatchHLTMuons = cms.EDProducer("PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'selectedPatMuons' ) ,
                                                       matched = cms.InputTag( 'patTrigger' ), # selections of trigger objects ,
                                                       matchedCuts = cms.string( 'path( "HLT_*Mu*_*" )' ), # selection of matches ,
                                                       maxDPtRel = cms.double( 0.5 ),
                                                       maxDeltaR = cms.double( 0.3 ) ,
                                                       resolveAmbiguities = cms.bool( True ) ,
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )
     switchOnTriggerMatchEmbedding(process ,triggerMatchers = ['muonTriggerMatchHLTMuons'],)
     process.muonTriggerMatchHLTMuons.src = cms.InputTag( 'selectedMuonsWithIsolationData' )
     process.selectedPatMuonsTriggerMatch = cms.EDProducer(
          "PATTriggerMatchMuonEmbedder"
          , src     = cms.InputTag( 'selectedMuonsWithIsolationData' )
          , matches = cms.VInputTag('muonTriggerMatchHLTMuons')
          )

     process.allMuons = process.selectedPatMuons.clone(
          src = cms.InputTag('selectedPatMuonsTriggerMatch'),
          )
     
     process.tightMuons = process.selectedPatMuons.clone(
         src = cms.InputTag('selectedPatMuonsTriggerMatch'),
         cut = cms.string('isGlobalMuon &'
                          'isPFMuon &'
                          'innerTrack.hitPattern.trackerLayersWithMeasurement>5 &'
                          #fabs(recoMu.innerTrack()->dz(vertex->position())) < 0.5 # to be applied offline
                          'userFloat("RelativePFIsolationDBetaCorr") < 0.2 &' # PF isolation, tighter possibility: 0.12
                          'abs(dB) < 0.2 &' #not anymore 0.02? effect should be small anyway
                          'normChi2 < 10 &'
                          'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                          'numberOfMatchedStations>1 &'
                          'globalTrack.hitPattern.numberOfValidMuonHits > 0'
                          )
         )    

     process.tightNoIsoMuons = process.selectedPatMuons.clone(
         src = cms.InputTag('selectedPatMuonsTriggerMatch'),
         cut = cms.string('isGlobalMuon &'
                          'isPFMuon &'
                          'innerTrack.hitPattern.trackerLayersWithMeasurement>5 &'
                          #fabs(recoMu.innerTrack()->dz(vertex->position())) < 0.5 # to be applied offline
                          'abs(dB) < 0.2 &' #not anymore 0.02? effect should be small anyway
                          'normChi2 < 10 &'
                          'innerTrack.hitPattern.numberOfValidPixelHits > 0 &'
                          'numberOfMatchedStations>1 &'
                          'globalTrack.hitPattern.numberOfValidMuonHits > 0'
                          )
         )    
     
     # Sequence for muons:
     process.preMuonSeq = cms.Sequence (
          process.muIsoSequence *
          process.pfMuonSequence
          )
     process.PF2PAT.replace(process.pfMuonSequence,process.preMuonSeq)
     
     process.patDefaultSequence.replace(process.patMuons, process.patMuons+process.MuScleFit)
     process.patDefaultSequence.replace(process.selectedPatMuons,process.selectedPatMuons*process.selectedMuonsWithIsolationData)

     process.postMuonSeq = cms.Sequence (    
          process.muonTriggerMatchHLTMuons *
          process.selectedPatMuonsTriggerMatch *
          process.allMuons *          
          process.tightMuons +
          process.tightNoIsoMuons
          )


     process.zmuAllmuAll = cms.EDProducer('CandViewShallowCloneCombiner',
                                          decay = cms.string('allMuons@+ allMuons@-'),
                                          cut = cms.string('mass > 50.0'),
                                          name = cms.string('Zmuallmuall'),
                                          roles = cms.vstring('all1', 'all2')
                                          )

     process.zmuTightmuTight = cms.EDProducer('CandViewShallowCloneCombiner',
                                              decay = cms.string('tightMuons@+ tightMuons@-'),
                                              cut = cms.string('mass > 50.0'),
                                              name = cms.string('Zmutightmutight'),
                                              roles = cms.vstring('tight1', 'tight2')
                                              )
     process.znoisomuTightnoisomuTight = cms.EDProducer('CandViewShallowCloneCombiner',
                                              decay = cms.string('tightNoIsoMuons@+ tightNoIsoMuons@-'),
                                              cut = cms.string('mass > 50.0'),
                                              name = cms.string('Znoisomutightnoisomutight'),
                                              roles = cms.vstring('tight1', 'tight2')
                                              )
     process.muonComposite = cms.Sequence (
          process.zmuAllmuAll +
          process.zmuTightmuTight +
          process.znoisomuTightnoisomuTight
          )
     
