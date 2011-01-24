import FWCore.ParameterSet.Config as cms

process = cms.Process("merge")

process.CombinePlots = cms.PSet(
  outputFile = cms.string('mergedPlots.root'),
  data = cms.VPSet (
   cms.PSet(
     fileName = cms.string('controlPlots_ELERun2010A.root')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_ELERun2010B.root')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_MURun2010A.root')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_MURun2010B.root')
   ) 
  ),
  mc   = cms.VPSet (
   cms.PSet(
     fileName = cms.string('controlPlots_Zbb-TuneZ2.root'),
     color = cms.uint32(2),
     scale = cms.double(0.01675), #NLO
     role = cms.string('Zbb')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_Zcc-TuneZ2_2.root'),
     color = cms.uint32(4),
     scale = cms.double(0.017625), #NLO
     role = cms.string('Zcc')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_DYJetsToLL_TuneD6T.root'),
     color = cms.uint32(3),
     scale = cms.double(0.04878), #NNLO
     role = cms.string('Z+jets')
   )
  ),
  formating = cms.VPSet (
    cms.PSet(
      name = cms.string('bestzmassMu'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Z -> #mu#mu invariant mass (GeV/c^{2})"),
      labely = cms.untracked.string("Events/GeV/c^{2}")
    )
  )
)
