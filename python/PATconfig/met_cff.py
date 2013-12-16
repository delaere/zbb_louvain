from PhysicsTools.PatAlgos.tools.metTools import *
from PhysicsTools.PatUtils.tools.metUncertaintyTools import runMEtUncertainties

def setupPatMets (process, runOnMC):
	addPfMET(process, 'PF')		
	process.MetSequence = cms.Sequence()
	
	##Filters
	
	process.load("RecoMET.METFilters.metFilters_cff")  
	if not runOnMC : MetSequence += process.metFilters
	
	##Corrections

	process.load("PhysicsTools.PatUtils.patPFMETCorrections_cff")
	#Type 0 Corrections
	process.patPFMETtype0Corr.src = cms.InputTag('goodPV')
	#Type 1 correction
	if runOnMC :
        	process.patPFJetMETtype1p2Corr.jetCorrLabel = cms.string("L3Absolute")
	else :
        	process.patPFJetMETtype1p2Corr.jetCorrLabel = cms.string("L2L3Residual")
        	process.patPFMet.addGenMET = cms.bool(False)
	process.patPFJetMETtype1p2Corr.skipEM = cms.bool(False)
	process.patPFJetMETtype1p2Corr.skipMuons = cms.bool(False)
	#SysShift correction (to turn the MET flat with respect to Phi)
	process.load("JetMETCorrections.Type1MET.pfMETsysShiftCorrections_cfi")
	process.selectedVerticesForMEtCorr.src = cms.InputTag('goodPV')
	if runOnMC : process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_mc	
	process.patType01CorrectedPFMet = cms.EDProducer("CorrectedPATMETProducer",
    		src = cms.InputTag('patPFMet'),
    		applyType1Corrections = cms.bool(True),
    		srcType1Corrections = cms.VInputTag(
        	cms.InputTag('patPFJetMETtype1p2Corr', 'type1'),
        	cms.InputTag('patPFMETtype0Corr')
    		),
    		applyType2Corrections = cms.bool(False)
	)
	process.patType01SysCorrectedPFMet = cms.EDProducer("CorrectedPATMETProducer",
          	src = cms.InputTag('patPFMet'),
          	applyType1Corrections = cms.bool(True),
          	srcType1Corrections = cms.VInputTag(
              	cms.InputTag('patPFJetMETtype1p2Corr', 'type1'),
              	cms.InputTag('patPFMETtype0Corr'),
              	cms.InputTag('pfMEtSysShiftCorr'),
          	),
          	applyType2Corrections = cms.bool(False)
      	)      		
	process.MetSequence *= cms.Sequence(
                  process.patPFMet
                  *process.pfMEtSysShiftCorrSequence
                  *process.pfCandsNotInJet
                  *process.selectedPatJetsForMETtype1p2Corr
                  *process.patPFJetMETtype1p2Corr
                  *process.type0PFMEtCorrection
                  *process.patPFMETtype0Corr
                  *process.pfCandMETcorr
                  *process.patType1CorrectedPFMet
                  *process.patType01CorrectedPFMet
                  *process.patType01SysCorrectedPFMet
              )
	process.patDefaultSequence.replace(process.patMETsPF,process.MetSequence)
	#Suggested Modules to remove :
	#process.patDefaultSequence.remove(process.pfType1p2CorrectedMet)
	#process.patDefaultSequence.remove(process.pfType1CorrectedMet)
	#process.patDefaultSequence.remove(process.patMETs)
	#process.patDefaultSequence.remove(process.caloType1p2CorrectedMet)
	#process.patDefaultSequence.remove(process.caloType1CorrectedMet)
	#process.patDefaultSequence.remove(process.muonCaloMETcorr)
	
	##Uncertainties      Does not work for now

	#if runOnMC :
	#       runMEtUncertainties(process,doApplyType0corr=True,makeType1p2corrPFMEt=False,sysShiftCorrParameter=process.pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_mc,doApplySysShiftCorr=True,addToPatDefaultSequence=True)

 











 
