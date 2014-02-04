from PhysicsTools.PatAlgos.tools.metTools import *
from PhysicsTools.PatUtils.tools.metUncertaintyTools import runMEtUncertainties

def setupPatMets (process, runOnMC, makeNoPUMet):
	process.preMetSequence = cms.Sequence()
	
	##Filters
	process.load("RecoMET.METFilters.metFilters_cff")  
 	process.preMetSequence += process.metFilters

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
	#SysShift correction to turn the MET flat(ter) with respect to Phi
	process.load("JetMETCorrections.Type1MET.pfMETsysShiftCorrections_cfi")
	process.selectedVerticesForMEtCorr.src = cms.InputTag('goodPV')
        
	#MVA MET                        !!! Based on AK5PFJets and not on AK5PFchsJets (the same holds for noPUMET)
	process.load("RecoMET.METPUSubtraction.mvaPFMET_cff")
        process.pfMEtMVA.srcVertices = cms.InputTag('goodPV')
        process.pfMEtMVA.srcLeptons = cms.VInputTag("tightMuons","tightElectrons")

	
	##Uncertainties
	if makeNoPUMet : 
		process.load("RecoMET.METPUSubtraction.noPileUpPFMET_cff")
                process.noPileUpPFMEt.srcLeptons = cms.VInputTag("tightMuons","tightElectrons")
		if runOnMC :
                        process.calibratedAK5PFJetsForNoPileUpPFMEt.correctors = cms.vstring("ak5PFL1FastL2L3")
			process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3")
			runMEtUncertainties(process,
					makeType1p2corrPFMEt=False,
					doApplyType0corr=True,
				    	sysShiftCorrParameter=process.pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_mc,
				    	doApplySysShiftCorr=True,
				    	jetCorrPayloadName='AK5PFchs',
                                    	makePFMEtByMVA=True,
				    	makeNoPileUpPFMEt=True,
				    	addToPatDefaultSequence=False,
				   	postfix='')
		else :
                        process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3Residual")
                        process.calibratedAK5PFJetsForNoPileUpPFMEt.correctors = cms.vstring("ak5PFL1FastL2L3Residual")
			runMEtUncertainties(process,
				    	makeType1p2corrPFMEt=False,
				    	doApplyType0corr=True,
				    	sysShiftCorrParameter=process.pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_data,
				    	doApplySysShiftCorr=True,
				    	jetCorrPayloadName='AK5PFchs',
                                    	makePFMEtByMVA=True,
					makeNoPileUpPFMEt=True,
				    	addToPatDefaultSequence=False,
				    	doSmearJets=False,
				    	postfix='')

	else : 
		if runOnMC :
                        process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3")
                        runMEtUncertainties(process,
                                        makeType1p2corrPFMEt=False,
                                        doApplyType0corr=True,
                                        sysShiftCorrParameter=process.pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_mc,
                                        doApplySysShiftCorr=True,
                                        jetCorrPayloadName='AK5PFchs',
                                        makePFMEtByMVA=True,
                                        addToPatDefaultSequence=False,
                                        postfix='')
                else :
                        process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3Residual")
                        runMEtUncertainties(process,
                                        makeType1p2corrPFMEt=False,
                                        doApplyType0corr=True,
                                        sysShiftCorrParameter=process.pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_data,
                                        doApplySysShiftCorr=True,
                                        jetCorrPayloadName='AK5PFchs',
                                        makePFMEtByMVA=True,
                                        addToPatDefaultSequence=False,
                                        doSmearJets=False,
                                        postfix='')

	


	process.patType01SCorrectedPFMet = process.patType1CorrectedPFMet.clone()
	process.metUncertaintySequence.replace(process.patType1CorrectedPFMet,
					       cms.Sequence(process.type0PFMEtCorrection*process.patPFMETtype0Corr*process.patType1CorrectedPFMet*process.patType01SCorrectedPFMet)
					       )

	process.pfCandsNotInJet.topCollection = cms.InputTag("pfNoTau")
	
	#Add Met with different corrections
	process.patType01CorrectedPFMet = cms.EDProducer("CorrectedPATMETProducer",
                src = cms.InputTag('patPFMet'),
                applyType1Corrections = cms.bool(True),
                srcType1Corrections = cms.VInputTag(
                    cms.InputTag('patPFJetMETtype1p2Corr', 'type1'),
                    cms.InputTag('patPFMETtype0Corr')
                ),
                applyType2Corrections = cms.bool(False)
        )       
  
	process.patTypeOnly1CorrectedPFMet = cms.EDProducer("CorrectedPATMETProducer",
        	src = cms.InputTag('patPFMet'),
        	applyType1Corrections = cms.bool(True),
        	srcType1Corrections = cms.VInputTag(
          	    cms.InputTag('patPFJetMETtype1p2Corr', 'type1'),
        	),
        	applyType2Corrections = cms.bool(False)
	)

	process.patType0CorrectedPFMet = cms.EDProducer("CorrectedPATMETProducer",
                src = cms.InputTag('patPFMet'),
                applyType1Corrections = cms.bool(True),
                srcType1Corrections = cms.VInputTag(
                    cms.InputTag('patPFMETtype0Corr')
                ),
                applyType2Corrections = cms.bool(False)
        )       
	
	process.patTypeSysCorrectedPFMet = cms.EDProducer("CorrectedPATMETProducer",
                src = cms.InputTag('patPFMet'),
                applyType1Corrections = cms.bool(True),
                srcType1Corrections = cms.VInputTag(
                    cms.InputTag('pfMEtSysShiftCorr')
		),
                applyType2Corrections = cms.bool(False)
        )


 	
	process.patType0sysCorrectedPFMet = cms.EDProducer("CorrectedPATMETProducer",
                src = cms.InputTag('patPFMet'),
                applyType1Corrections = cms.bool(True),
                srcType1Corrections = cms.VInputTag(
                    cms.InputTag('patPFMETtype0Corr'),
		    cms.InputTag('pfMEtSysShiftCorr')
                ),
                applyType2Corrections = cms.bool(False)
        )       
	
	process.patType1sysCorrectedPFMet = cms.EDProducer("CorrectedPATMETProducer",
                src = cms.InputTag('patPFMet'),
                applyType1Corrections = cms.bool(True),
                srcType1Corrections = cms.VInputTag(
		    cms.InputTag('patPFJetMETtype1p2Corr', 'type1'),
                    cms.InputTag('pfMEtSysShiftCorr')
                ),
                applyType2Corrections = cms.bool(False)
        )  
	

	process.metUncertaintySequence += cms.Sequence(process.patTypeOnly1CorrectedPFMet+process.patType0CorrectedPFMet+process.patTypeSysCorrectedPFMet+process.patType01CorrectedPFMet+process.patType1sysCorrectedPFMet+process.patType0sysCorrectedPFMet)
 

	#clean metUncertaintySequence
	print ""
	print "These modules will be removed from the metUncertaintySequence as already produced before:"
	for name in process.patDefaultSequence.moduleNames() :
		if name in process.metUncertaintySequence.moduleNames() :
			print name
			process.metUncertaintySequence.remove(getattr(process,name))
			if name in process.metUncertaintySequence.moduleNames() : print "Error : module not removed from metUncertaintySequence"
	print "...done."
	print ""
					
	#clean metUncertaintySequence for data
	if not runOnMC:
		print ""
		print "These modules will be removed from the metUncertaintySequence as useless for data:"
		for name in process.metUncertaintySequence.moduleNames() :
			if name[-2:]=="Up" or name[-4:]=="Down" :
				print "Run on data: remove uncertainty variation,", name
				process.metUncertaintySequence.remove(getattr(process,name))
				if name in process.metUncertaintySequence.moduleNames() :
					process.metUncertaintySequence.remove(getattr(process,name))
				if name in process.metUncertaintySequence.moduleNames() :
					print "Error : module not removed from metUncertaintySequence"
		print "...done."
		print ""







 
