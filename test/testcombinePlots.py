import FWCore.ParameterSet.Config as cms

process = cms.Process("merge")

process.CombinePlots = cms.PSet(
  outputFile = cms.string('mergedPlots.root'),
  data = cms.VPSet (
   cms.PSet(
     fileName = cms.string('controlPlots_El_2010A_Dec22.root')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_El_2010B_Dec22.root')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_Mu_2010A_Dec22.root')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_Mu_2010B_Dec22.root')
   ) 
  ),
  mc   = cms.VPSet (
   cms.PSet(
     fileName = cms.string('controlPlots_Zbb-TuneZ2_2.root'),
     color = cms.uint32(2),
     scale = cms.double(0.017978), #NLO k=1.25
     role = cms.string('Zbb')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_Zcc-TuneZ2_2.root'),
     color = cms.uint32(4),
     scale = cms.double(0.0189175), #NLO k=1.25
     role = cms.string('Zcc')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_TTJets_TuneZ2_387.root'),
     color = cms.uint32(5),
     scale = cms.double(0.003),
     role = cms.string('ttbar')
   ),
   cms.PSet(
     #fileName = cms.string('controlPlots_DYJetsToLL_TuneD6T.root'),
     fileName = cms.string('controlPlots_DYJetsToLL_TuneZ2_387.root'),
     color = cms.uint32(3),
     scale = cms.double(0.03595), #NNLO
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
      labely = cms.untracked.string("Events/GeV/c^{2}"),
      rangex = cms.untracked.vdouble(60.,120.)
    ),
    cms.PSet(
      name = cms.string('bestzmassEle'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Z -> ee invariant mass (GeV/c^{2})"),
      labely = cms.untracked.string("Events/GeV/c^{2}"),
      rangex = cms.untracked.vdouble(60.,120.)
    ),
    cms.PSet(
      name = cms.string('bjet1pt'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Leading bjet Pt (GeV/c)"),
      labely = cms.untracked.string("Events/10GeV/c")
    ),
    cms.PSet(
      name = cms.string('bjet2pt'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Second bjet Pt (GeV/c)"),
      labely = cms.untracked.string("Events/10GeV/c")
    ),
    cms.PSet(
      name = cms.string('MET'),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Missing Et (GeV)"),
      labely = cms.untracked.string("Events/2GeV")
    ),
    cms.PSet(
      name = cms.string('vecdptZbj1'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Pt imbalance between Z and leading bjet (GeV/c)"),
      labely = cms.untracked.string("Events/10GeV/c")
    ),
    cms.PSet(
      name = cms.string('ZbM'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Zb invariant mass (GeV/c^{2})"),
      labely = cms.untracked.string("Events/10GeV/c^{2}")
    ),
    cms.PSet(
      name = cms.string('ZbPt'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Zb Pt (GeV/c)"),
      labely = cms.untracked.string("Events/10GeV/c")
    ),
    cms.PSet(
      name = cms.string('ZbbM'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Zbb invariant mass (GeV/c^{2})"),
      labely = cms.untracked.string("Events/10GeV/c^{2}")
    ),
    cms.PSet(
      name = cms.string('ZbbPt'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Zbb Pt (GeV/c)"),
      labely = cms.untracked.string("Events/10GeV/c")
    ),
  )
)
