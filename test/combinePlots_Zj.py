import FWCore.ParameterSet.Config as cms

process = cms.Process("merge")

process.CombinePlots = cms.PSet(
  outputFile = cms.string('mergedPlots_Zj_all.root'),
  data = cms.VPSet (
   cms.PSet(
     fileName = cms.string('controlPlots_Ele_2010A_Dec22_all.root')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_Ele_2010B_Dec22_all.root')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_Mu_2010A_Dec22_all.root')
   ), 
   cms.PSet(
     fileName = cms.string('controlPlots_Mu_2010B_Dec22_all.root')
   ) 
  ),
  mc   = cms.VPSet (
   cms.PSet(
     fileName = cms.string('controlPlots_TTJets_TuneZ2_v3_all.root'),
     color = cms.uint32(5),
     scale = cms.double(0.00463), #NLO MCFM
     role = cms.string('t#bar{t}')
   ),
   cms.PSet(
     fileName = cms.string('controlPlots_DYJetsToLL_TuneZ2_Zj_all.root'),
     color = cms.uint32(4),
     scale = cms.double(0.0209305), #NNLO
     role = cms.string('Z+jets')
   ),
  ),
  options = cms.PSet (
      nostack = cms.untracked.bool(False)
  ),
  formating = cms.VPSet (
    cms.PSet(
      name = cms.string('bestzmass'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{l^{+}l^{-}} (GeV/c^{2})"),
      labely = cms.untracked.string("Events/2GeV/c^{2}"),
      rangex = cms.untracked.vdouble(60.,120.)
    ),
    cms.PSet(
      name = cms.string('bestzmassMu'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{#mu^{+}#mu^{-}} (GeV/c^{2})"),
      labely = cms.untracked.string("Events/2GeV/c^{2}"),
      rangex = cms.untracked.vdouble(60.,120.)
    ),
    cms.PSet(
      name = cms.string('bestzmassEle'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{e^{+}e^{-}} invariant mass (GeV/c^{2})"),
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
      name = cms.string('jet1pt'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Pt_{Leading jet} (GeV/c)"),
      labely = cms.untracked.string("Events/10GeV/c")
    ),
    cms.PSet(
      name = cms.string('jet1etapm'),
      labelx = cms.untracked.string("#eta_{Leading jet} (GeV/c)"),
      labely = cms.untracked.string("Events/0.1")
    ),
    cms.PSet(
      name = cms.string('jet2pt'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Pt_{Second jet} (GeV/c)"),
      labely = cms.untracked.string("Events/10GeV/c")
    ),
    cms.PSet(
          name = cms.string('el1pt'),
	  rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("Pt_{e_{1}} (GeV/c)"),
	  labely = cms.untracked.string("Events/5GeV/c")
    ),
    cms.PSet(
          name = cms.string('el2pt'),
	  rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("Pt_{e_{2}} (GeV/c)"),
	  labely = cms.untracked.string("Events/5GeV/c")
    ),
    cms.PSet(
          name = cms.string('mu1pt'),
	  rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("Pt_{#mu_{1}} (GeV/c)"),
	  labely = cms.untracked.string("Events/5GeV/c")
    ),
    cms.PSet(
          name = cms.string('mu2pt'),
	  rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("Pt_{#mu_{2}} (GeV/c)"),
	  labely = cms.untracked.string("Events/5GeV/c")
    ),
    cms.PSet(
      name = cms.string('MET'),
      logy = cms.untracked.bool(True),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("MEt (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
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
      rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{Zb} (GeV/c^{2})"),
      labely = cms.untracked.string("Events/50GeV/c^{2}")
    ),
    cms.PSet(
      name = cms.string('ZbPt'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Pt_{Zb} (GeV/c)"),
      labely = cms.untracked.string("Events/10GeV/c")
    ),
    cms.PSet(
      name = cms.string('ZbbM'),
      rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{Zbb} (GeV/c^{2})"),
      labely = cms.untracked.string("Events/50GeV/c^{2}")
    ),
    cms.PSet(
      name = cms.string('ZbbPt'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Pt_{Zbb} (GeV/c)"),
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
    cms.PSet(
      name = cms.string('SSVHEdisc'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("SSVHE discriminant"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('SSVHPdisc'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("SSVHP discriminant"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('SSVHEdiscDisc1'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("SSVHE discriminant"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('SSVHPdiscDisc1'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("SSVHP discriminant"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('dphiZbj1'),
      labelx = cms.untracked.string("#Delta#phi(Z,bjet_{1})"),
      labely = cms.untracked.string("Events/0.1")
    ),
    cms.PSet(
      name = cms.string('drZbj1'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#Delta R(Z,bjet_{1})"),
      labely = cms.untracked.string("Events/0.5")
    ),



  )
)
