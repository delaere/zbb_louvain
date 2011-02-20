import FWCore.ParameterSet.Config as cms

process = cms.Process("merge")

process.CombinePlots = cms.PSet(
  outputFile = cms.string('mergedPlots_ZjZcZb_MCFM_test.root'),
  data = cms.VPSet (
   cms.PSet(
     fileName = cms.string('controlPlots_El_2010A_Dec22.root'),
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_El_2010B_Dec22.root'),
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_Mu_2010A_Dec22.root'),
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_Mu_2010B_Dec22.root'),
   ) 
  ),
  mc   = cms.VPSet (
   cms.PSet(
     fileName = cms.string('controlPlots_Zbb-TuneZ2_2.root'),
     color = cms.uint32(2),
     scale = cms.double(0.0358024), #NLO MCFM
     role = cms.string('Zb')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_Zcc-TuneZ2_2.root'),
     color = cms.uint32(4),
     scale = cms.double(0.0368016), #NLO MCFM
     role = cms.string('Zc')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_TTJets_TuneZ2_387.root'),
     color = cms.uint32(5),
     scale = cms.double(0.0044184), #NLO k=1.67
     role = cms.string('ttbar')
   ),
   cms.PSet(
     fileName = cms.string('controlPlots_DYJets_TuneZ2_noZbbZcc.root'),
     color = cms.uint32(3),
     scale = cms.double(0.0432474), #NNLO
     role = cms.string('Z+jets')
   )
  ),
  options = cms.PSet (
      nostack = cms.untracked.bool(False)
  ),
  formating = cms.VPSet (
    cms.PSet(
      name = cms.string('bestzmassMu'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Z -> #mu#mu invariant mass (GeV/c^{2})"),
      labely = cms.untracked.string("Events/2GeV/c^{2}"),
      rangex = cms.untracked.vdouble(60.,120.)
    ),
    cms.PSet(
      name = cms.string('bestzmassEle'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Z -> ee invariant mass (GeV/c^{2})"),
      labely = cms.untracked.string("Events/2GeV/c^{2}"),
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
    cms.PSet(
      name = cms.string('bestzpt'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Z Pt (GeV/c)"),
      labely = cms.untracked.string("Events/10GeV/c")
    ),
    cms.PSet(
      name = cms.string('bestzptMu'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Z Pt (GeV/c)"),
      labely = cms.untracked.string("Events/10GeV/c")
    ),
    cms.PSet(
      name = cms.string('bestzptEle'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Z Pt (GeV/c)"),
      labely = cms.untracked.string("Events/10GeV/c")
    ),
  )
)
