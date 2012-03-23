import FWCore.ParameterSet.Config as cms

process = cms.Process("merge")

process.CombinePlots = cms.PSet(
  outputFile = cms.string('mergedPlots.root'),
  data = cms.VPSet (
   cms.PSet(
     fileName = cms.string('TH1sDATA.root')
   ) 
  ),
  mc   = cms.VPSet (
   cms.PSet(
     fileName = cms.string('TH1sDY.root'),
     color = cms.uint32(2),
     scale = cms.double(0.176535023577), 
     role = cms.string('Z+j')
   ), 
   cms.PSet(
     fileName = cms.string('TH1sTT.root'),
     color = cms.uint32(5),
     scale = cms.double(0.0893448771687), #NLO k=1.67
     role = cms.string('ttbar'),
   ),
   cms.PSet(
     fileName = cms.string('TH1sZZ.root'),
     color = cms.uint32(3),
     scale = cms.double(0.00315), 
     role = cms.string('ZZ')
   ),
   cms.PSet(
     fileName = cms.string('TH1sZHbb.root'),
     color = cms.uint32(4),
     scale = cms.double(0.000175), 
     role = cms.string('ZH'),
     stacked = cms.untracked.bool(False)
   )
  ),
  options = cms.PSet (
          # nostack: if set, none of the curves will be stacked. That overrides the mc set option
          nostack = cms.untracked.bool(False),
                # luminosity, in pb
                luminosity = cms.untracked.double(2130.),
                # if autoLumiScaling is set, luminosity will multiply each mc scale.
                autoLumiScaling = cms.untracked.bool(False),
                # label to be set on plots
                label = cms.untracked.string("#splitline{CMS}{#sqrt{s} = 7 TeV, L = 2.2 fb^{-1}}"),
            ),
  formating = cms.VPSet (
    cms.PSet(
     name = cms.string('th1_eventSelectiondijetdR'),
    #   rebin = cms.untracked.uint32(20),
    #   logx = cms.untracked.bool(False),
    #   logy = cms.untracked.bool(True),
    #   labelx = cms.untracked.string("M_{l^{+}l^{-}} (GeV/c^{2})"),
    #   labely = cms.untracked.string("Events/2GeV/c^{2}"),
    #   rangex = cms.untracked.vdouble(60.,120.)
       ),
  )
)
