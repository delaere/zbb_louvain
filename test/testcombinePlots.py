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
     scale = cms.double(0.0134),
     role = cms.string('Zbb')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_DYJetsToLL_TuneD6T.root'),
     color = cms.uint32(3),
     scale = cms.double(0.13734),
     role = cms.string('Z+jets')
   )
  )
)
