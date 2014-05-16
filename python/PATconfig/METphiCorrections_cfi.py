import FWCore.ParameterSet.Config as cms

# parametrization of MET x/y shift vs. Nvtx

pfMEtSysShiftCorrParameters_2011runAvsNvtx_data = cms.PSet(
    px = cms.string("+3.87339e-1 + 2.58294e-1*Nvtx"),
    py = cms.string("-7.83502e-1 - 2.88899e-1*Nvtx")
)

pfMEtSysShiftCorrParameters_2011runAvsNvtx_mc = cms.PSet(
    px = cms.string("-1.94451e-2 - 4.38986e-3*Nvtx"),
    py = cms.string("-4.31368e-1 - 1.90753e-1*Nvtx")
)

pfMEtSysShiftCorrParameters_2011runBvsNvtx_data = cms.PSet(
    px = cms.string("+6.64470e-1 + 2.71292e-1*Nvtx"),
    py = cms.string("-1.23999e0 - 3.18661e-1*Nvtx")
)

pfMEtSysShiftCorrParameters_2011runBvsNvtx_mc = cms.PSet(
    px = cms.string("-9.89706e-2 + 6.64796e-3*Nvtx"),
    py = cms.string("-5.32495e-1 - 1.82195e-1*Nvtx")
)

pfMEtSysShiftCorrParameters_2011runAplusBvsNvtx_data = cms.PSet(
    px = cms.string("+3.64118e-01 + 2.93853e-01*Nvtx"),
    py = cms.string("-7.17757e-01 - 3.57309e-01*Nvtx")
)

pfMEtSysShiftCorrParameters_2011runAplusBvsNvtx_mc = cms.PSet(
    px = cms.string("-4.79178e-02 + 8.62653e-04*Nvtx"),
    py = cms.string("-4.54408e-01 - 1.89684e-01*Nvtx")
)

pfMEtSysShiftCorrParameters_2012runAvsNvtx_data = cms.PSet(
    px = cms.string("+3.54233e-01 + 2.65299e-01*Nvtx"),
    py = cms.string("+1.88923e-01 - 1.66425e-01*Nvtx")
)

pfMEtSysShiftCorrParameters_2012runAvsNvtx_mc = cms.PSet(
    px = cms.string("-2.99576e-02 - 6.61932e-02*Nvtx"),
    py = cms.string("+3.70819e-01 - 1.48617e-01*Nvtx")
)

pfMEtSysShiftCorrParameters_2012runAplusBvsNvtx_data = cms.PSet(
    px = cms.string("+1.68804e-01 + 3.37139e-01*Nvtx"),
    py = cms.string("-1.72555e-01 - 1.79594e-01*Nvtx")
)

pfMEtSysShiftCorrParameters_2012runAplusBvsNvtx_mc = cms.PSet(
    px = cms.string("+2.22335e-02 - 6.59183e-02*Nvtx"),
    py = cms.string("+1.52720e-01 - 1.28052e-01*Nvtx")
)

pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_data = cms.PSet( # CV: ReReco data + Summer'13 JEC
    px = cms.string("+4.83642e-02 + 2.48870e-01*Nvtx"),
    py = cms.string("-1.50135e-01 - 8.27917e-02*Nvtx")
)

pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_mc = cms.PSet( # CV: Summer'12 MC + Summer'13 JEC
    px = cms.string("+1.62861e-01 - 2.38517e-02*Nvtx"),
    py = cms.string("+3.60860e-01 - 1.30335e-01*Nvtx")
)


##########################
# New Phi Correction Based on AN 13_233_v4
##########################

NewPFMEtSysShiftCorrParameters_2012runABCDvsNvtx_data = cms.PSet(
    px = cms.string("+0.0799 + 0.2393*Nvtx"),
    py = cms.string("-0.1370 - 0.0802*Nvtx")
)

NewPFMEtSysShiftCorrParameters_2012runABCDvsNvtx_mc = cms.PSet(
    px = cms.string("+0.0982 + 0.0138*Nvtx"),
    py = cms.string("-0.1802 - 0.1347*Nvtx")
)

NewNoPUMEtSysShiftCorrParameters_2012runABCDvsNvtx_data = cms.PSet(
    px = cms.string("+0.0415 + 0.1369*Nvtx"),
    py = cms.string("-0.2772 - 0.0652*Nvtx")
)

NewNoPUMEtSysShiftCorrParameters_2012runABCDvsNvtx_mc = cms.PSet(
    px = cms.string("+0.0976 + 0.0096*Nvtx"),
    py = cms.string("-0.0566 - 0.1068*Nvtx")
)

NewMVAMEtNURSysShiftCorrParameters_2012runABCDvsNvtx_data = cms.PSet(
    px = cms.string("+0.1376 + 0.0503*Nvtx"),
    py = cms.string("-0.0936 - 0.0695*Nvtx")
)

NewMVAMEtNURSysShiftCorrParameters_2012runABCDvsNvtx_mc = cms.PSet(
    px = cms.string("-0.1612 - 0.0124*Nvtx"),
    py = cms.string("+0.0139 - 0.0303*Nvtx")
)

NewMVAMEtURSysShiftCorrParameters_2012runABCDvsNvtx_data = cms.PSet(
    px = cms.string("+0.1466 + 0.0649*Nvtx"),
    py = cms.string("-0.0924 - 0.0187*Nvtx")
)

NewMVAMEtURSysShiftCorrParameters_2012runABCDvsNvtx_mc = cms.PSet(
    px = cms.string("-0.1373 - 0.0210*Nvtx"),
    py = cms.string("+0.0631 - 0.0501*Nvtx")
)

################################################################################

################################################################################

selectedVerticesForMEtCorr = cms.EDFilter("VertexSelector",
    src = cms.InputTag('offlinePrimaryVertices'),
    cut = cms.string("isValid & ndof >= 4 & chi2 > 0 & tracksSize > 0 & abs(z) < 24 & abs(position.Rho) < 2."),
    filter = cms.bool(False)
)
#--------------------------------------------------------------------------------

pfMEtSysShiftCorr = cms.EDProducer("SysShiftMETcorrInputProducer",
    src = cms.InputTag('pfMet'), # "raw"/uncorrected PFMEt, needed to access sumEt
    srcVertices = cms.InputTag('selectedVerticesForMEtCorr'),
    parameter = NewPFMEtSysShiftCorrParameters_2012runABCDvsNvtx_data
)

pfMEtSysShiftCorrSequence = cms.Sequence(selectedVerticesForMEtCorr * pfMEtSysShiftCorr)


