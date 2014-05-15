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
	process.patPFJetMETtype1p2Corr.skipEM = cms.bool(False)
	process.patPFJetMETtype1p2Corr.skipMuons = cms.bool(False)
	#SysShift correction to turn the MET flat(ter) with respect to Phi
	process.load("UserCode.zbb_louvain.PATconfig.METphiCorrections_cfi")
	process.selectedVerticesForMEtCorr.src = cms.InputTag('goodPV')

	if runOnMC :
                process.PFMETSysShiftCorr = process.pfMEtSysShiftCorr.clone(parameter=process.NewPFMEtSysShiftCorrParameters_2012runABCDvsNvtx_mc,
                                                                            )

                process.MVAMETNURSysShiftCorr = process.pfMEtSysShiftCorr.clone(parameter=process.NewMVAMEtNURSysShiftCorrParameters_2012runABCDvsNvtx_mc,
                                                                             src = cms.InputTag('pfMEtMVA')  # I think this is not mandatory for Nvtx based correction but to be safe...
                                                                            )

                process.MVAMETURSysShiftCorr = process.pfMEtSysShiftCorr.clone(parameter=process.NewMVAMEtURSysShiftCorrParameters_2012runABCDvsNvtx_mc,
                                                                             src = cms.InputTag('pfMEtMVA') 
                                                                            )

                process.NoPUMETSysShiftCorr = process.pfMEtSysShiftCorr.clone(parameter=process.NewNoPUMEtSysShiftCorrParameters_2012runABCDvsNvtx_mc,
                                                                             src = cms.InputTag('noPileUpPFMEt') 
                                                                            )
        else :

                process.PFMETSysShiftCorr = process.pfMEtSysShiftCorr.clone(parameter=process.NewPFMEtSysShiftCorrParameters_2012runABCDvsNvtx_data,
                                                                            )

                process.MVAMETNURSysShiftCorr = process.pfMEtSysShiftCorr.clone(parameter=process.NewMVAMEtNURSysShiftCorrParameters_2012runABCDvsNvtx_data,
                                                                             src = cms.InputTag('pfMEtMVA')
                                                                            )

                process.MVAMETURSysShiftCorr = process.pfMEtSysShiftCorr.clone(parameter=process.NewMVAMEtURSysShiftCorrParameters_2012runABCDvsNvtx_data,
                                                                             src = cms.InputTag('pfMEtMVA')
                                                                            )

                process.NoPUMETSysShiftCorr = process.pfMEtSysShiftCorr.clone(parameter=process.NewNoPUMEtSysShiftCorrParameters_2012runABCDvsNvtx_data,
                                                                             src = cms.InputTag('noPileUpPFMEt')
                                                                            )
        
	#MVA MET                        !!! Based on AK5PFJets and not on AK5PFchsJets (the same holds for noPUMET)
	process.load("RecoMET.METPUSubtraction.mvaPFMET_cff")
        process.pfMEtMVA.srcVertices = cms.InputTag('goodPV')
        process.pfMEtMVA.srcLeptons = cms.VInputTag("tightMuons","tightElectrons")

	#noPUMET
	if makeNoPUMet :
		process.load("RecoMET.METPUSubtraction.noPileUpPFMET_cff")
		process.noPileUpPFMEt.srcLeptons = cms.VInputTag("tightMuons","tightElectrons")
		if not runOnMC : process.calibratedAK5PFJetsForNoPileUpPFMEt.correctors = cms.vstring("ak5PFL1FastL2L3")

	##Uncertainties
	if runOnMC :
		runMEtUncertainties(process,
				    makeType1p2corrPFMEt=False,
				    doApplyType0corr=True,
				    jetCorrLabel = "L3Absolute",
				    sysShiftCorrParameter=process.pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_mc,  #old phi correction for PFMET
				    doApplySysShiftCorr=True,
				    jetCorrPayloadName='AK5PFchs',
				    makePFMEtByMVA=True,
				    makeNoPileUpPFMEt=makeNoPUMet,    
				    addToPatDefaultSequence=False,
				    postfix='')
	else :
		process.patPFMet.addGenMET = cms.bool(False)
		process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3Residual")
		runMEtUncertainties(process,
				    makeType1p2corrPFMEt=False,
				    doApplyType0corr=True,
				    jetCorrLabel = "L2L3Residual",
				    sysShiftCorrParameter=process.pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_data,
				    doApplySysShiftCorr=True,
				    jetCorrPayloadName='AK5PFchs',
				    makePFMEtByMVA=True,
				    makeNoPileUpPFMEt=makeNoPUMet,    
				    addToPatDefaultSequence=False,
				    doSmearJets=False,
				    postfix='')

	
	process.metUncertaintySequence.replace(process.patType1CorrectedPFMet,
					       cms.Sequence(process.type0PFMEtCorrection*process.patPFMETtype0Corr*process.patType1CorrectedPFMet)
					       )

	process.pfCandsNotInJet.topCollection = cms.InputTag("pfNoTau")
	
	#Add Met with different corrections
	process.patType01SCorrectedPFMet = process.patType1CorrectedPFMet.clone(
						srcType1Corrections = cms.VInputTag(
                    						cms.InputTag('patPFJetMETtype1p2Corr', 'type1'),
                    						cms.InputTag('patPFMETtype0Corr'),
								cms.InputTag('PFMETSysShiftCorr')
                						),
 	)

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
                    cms.InputTag('PFMETSysShiftCorr')
		),
                applyType2Corrections = cms.bool(False)
        )
	
	process.patType0sysCorrectedPFMet = cms.EDProducer("CorrectedPATMETProducer",
                src = cms.InputTag('patPFMet'),
                applyType1Corrections = cms.bool(True),
                srcType1Corrections = cms.VInputTag(
                    cms.InputTag('patPFMETtype0Corr'),
		    cms.InputTag('PFMETSysShiftCorr')
                ),
                applyType2Corrections = cms.bool(False)
        )       
	
	process.patType1sysCorrectedPFMet = cms.EDProducer("CorrectedPATMETProducer",
                src = cms.InputTag('patPFMet'),
                applyType1Corrections = cms.bool(True),
                srcType1Corrections = cms.VInputTag(
		    cms.InputTag('patPFJetMETtype1p2Corr', 'type1'),
                    cms.InputTag('PFMETSysShiftCorr')
                ),
                applyType2Corrections = cms.bool(False)
        ) 
	
	process.patMVAMETNURphiCorrected = cms.EDProducer("CorrectedPATMETProducer",
                src = cms.InputTag('patPFMetMVA'),
                applyType1Corrections = cms.bool(True),
                srcType1Corrections = cms.VInputTag(
                    cms.InputTag('MVAMETNURSysShiftCorr')
                ),
                applyType2Corrections = cms.bool(False)
        )

        process.patMVAMETURphiCorrected = cms.EDProducer("CorrectedPATMETProducer",
                src = cms.InputTag('patPFMetMVA'),
                applyType1Corrections = cms.bool(True),
                srcType1Corrections = cms.VInputTag(
                    cms.InputTag('MVAMETURSysShiftCorr')
                ),
                applyType2Corrections = cms.bool(False)
        )

        process.patNoPUMETphiCorrected = cms.EDProducer("CorrectedPATMETProducer",
                src = cms.InputTag('patPFMetNoPileUp'),
                applyType1Corrections = cms.bool(True),
                srcType1Corrections = cms.VInputTag(
                    cms.InputTag('NoPUMETSysShiftCorr')
                ),
                applyType2Corrections = cms.bool(False)
        )	

	process.metUncertaintySequence += cms.Sequence(process.PFMETSysShiftCorr+process.MVAMETNURSysShiftCorr+process.MVAMETURSysShiftCorr+process.NoPUMETSysShiftCorr+process.patType01SCorrectedPFMet+process.patTypeOnly1CorrectedPFMet+process.patType0CorrectedPFMet+process.patTypeSysCorrectedPFMet+process.patType01CorrectedPFMet+process.patType1sysCorrectedPFMet+process.patType0sysCorrectedPFMet+process.patMVAMETNURphiCorrected+process.patMVAMETURphiCorrected+process.patMVAMETURphiCorrected+process.patNoPUMETphiCorrected)
 

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
			#if name[-4:]=="EnUp" or name[-6:]=="EnDown" :
			if "EnUp" in name or "EnDown" in name:
				print "Run on data: remove uncertainty variation,", name
				process.metUncertaintySequence.remove(getattr(process,name))
				if name in process.metUncertaintySequence.moduleNames() :
					process.metUncertaintySequence.remove(getattr(process,name))
				if name in process.metUncertaintySequence.moduleNames() :
					print "Error : module not removed from metUncertaintySequence"
		print "...done."
		print ""



