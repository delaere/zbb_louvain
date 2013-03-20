import FWCore.ParameterSet.Config as cms
#from ROOT import EColor

from UserCode.zbb_louvain.zbbCommons import zbbnorm
lumi=zbbnorm.lumi_totEle2011*1000 #in pb-1

flow="overflow"
#flow=""
if flow=="overflow" : overflow = cms.untracked.bool(True)
else : overflow = cms.untracked.bool(False)

class EColor:
 """ROOT colors taken from RTypes.h"""
 kWhite  = 0
 kBlack  = 1
 kGray   = 920
 kRed    = 632
 kGreen  = 416
 kBlue   = 600
 kYellow = 400
 kMagenta= 616
 kCyan   = 432
 kOrange = 800
 kSpring = 820
 kTeal   = 840
 kAzure  = 860
 kViolet = 880
 kPink   = 900 
 
palette=-7
print "ok"
process = cms.Process("merge")

process.CombinePlots = cms.PSet(
    outputFile = cms.string('mergedPlots_5050pb_2011AB_V2_overflow.root'),
    
  data = cms.VPSet (
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp444/ControlPlots_V4/ControlPlots_Ele2011A/Ele2011A_Fall11_final.root')
            ), 
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp444/ControlPlots_V4/ControlPlots_Ele2011B/Ele2011B_Fall11_final.root')
            ), 
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp444/ControlPlots_V4/ControlPlots_Mu2011A/Mu2011A_Fall11_final.root') 
                                          ),
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp444/ControlPlots_V4/ControlPlots_Mu2011B/Mu2011B_Fall11_final.root')    
            ),   
        
  ),
    
  mc   = cms.VPSet (
        
        cms.PSet(
            fileName = cms.string('/home/fynu/rcastello/Physics/Zbb/Aug2012_full2011/upgrade_version/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/ControlPlots_V5/ControlPlots_ZZ/CP_ZZ_v5_combined.root'),
            color = cms.uint32(EColor.kMagenta+palette),
            scale = cms.double(zbbnorm.xsec_ZZ_7TeV*lumi/zbbnorm.nev_ZZ_fall11),#6.206*5051./(4191045.)), #Xs 
            role = cms.string('ZZ')
            ),

        cms.PSet(
            fileName = cms.string('/home/fynu/rcastello/Physics/Zbb/Aug2012_full2011/upgrade_version/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/ControlPlots_V5/ControlPlots_TT/CP_TTbar_v5_combined.root'),
            color = cms.uint32(EColor.kYellow+palette),
            scale = cms.double(zbbnorm.xsec_TTjets_7TeV*lumi/zbbnorm.nev_TTjets_fall11),#157.5*5051./(3701947.)), #NLO MCFM proper Xs
            role = cms.string('t#bar{t}')
            ),

        cms.PSet(
            fileName = cms.string('/home/fynu/rcastello/Physics/Zbb/Aug2012_full2011/upgrade_version/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/ControlPlots_V5/ControlPlots_Zb/CP_Zb_v5_combined.root'),
            color = cms.uint32(EColor.kRed+palette),
            scale = cms.double(zbbnorm.xsec_DYjets_7TeV*lumi/zbbnorm.nev_DYjets_fall11),#3048.*5051./35907791.), #NLO MCFM
            role = cms.string('Z+b')
            ), 
        cms.PSet(
            fileName = cms.string('/home/fynu/rcastello/Physics/Zbb/Aug2012_full2011/upgrade_version/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/ControlPlots_V5/ControlPlots_Zc/CP_Zc_v5_combined.root'),
            color = cms.uint32(EColor.kGreen+palette),
            scale = cms.double(zbbnorm.xsec_DYjets_7TeV*lumi/zbbnorm.nev_DYjets_fall11),#3048.*5051./35907791.), #NLO MCFM
            role = cms.string('Z+c')
            ), 
        cms.PSet(
            fileName = cms.string('/home/fynu/rcastello/Physics/Zbb/Aug2012_full2011/upgrade_version/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/ControlPlots_V5/ControlPlots_Zl/CP_Zl_v5_combined.root'),
            color = cms.uint32(EColor.kBlue+palette),
            scale = cms.double(zbbnorm.xsec_DYjets_7TeV*lumi/zbbnorm.nev_DYjets_fall11),#3048.*5051./35907791.), #NLO MCFM
            role = cms.string('Z+l')
            ),
        #cms.PSet(
        #    fileName = cms.string('/home/fynu/rcastello/Physics/Zbb/Aug2012_full2011/upgrade_version/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/ControlPlots_ZH_125/ZH125_Fall11_all.root'),
        #    color = cms.uint32(EColor.kWhite),#EColor.kAzure+palette),
        #    scale = cms.double(50*zbbnorm.xsec_ZH125_7TeV*lumi/zbbnorm.nev_ZH125_fall11), #Xs 
        #    role = cms.string('50*ZH_125')
        #    ),
  ),

  options = cms.PSet (
      nostack = cms.untracked.bool(False),
      lumiMuCor = cms.untracked.double(zbbnorm.lumi_totMu2011/zbbnorm.lumi_totEle2011)
  ),
  formating = cms.VPSet (
    cms.PSet(
      name = cms.string('bestzmass'),
      overflow=overflow,
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{Z} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(76.,106.)
    ),
    cms.PSet(
      name = cms.string('bestzmassMu'),
      overflow=overflow,
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{#mu^{+}#mu^{-}} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(76.,106.)
    ),
    cms.PSet(
      name = cms.string('bestzmassEle'),
      overflow=overflow,
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{e^{+}e^{-}} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(76.,106.)
    ),
    cms.PSet(
      name = cms.string('bjet1pt'),
      overflow=overflow,
      begin = cms.untracked.double(0),
      end = cms.untracked.double(265),
      width = cms.untracked.double(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{b-lead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('bjet2pt'),
      overflow=overflow,
      begin = cms.untracked.double(0),
      end = cms.untracked.double(265),
      width = cms.untracked.double(10),
      #rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{b-sublead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('jet1pt'),
      overflow=overflow,
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{lead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('jet1etapm'),
      labelx = cms.untracked.string("#eta^{lead}"),
      labely = cms.untracked.string("Events/0.1")
    ),
    cms.PSet(
      name = cms.string('jet2pt'),
      overflow=overflow,
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{sublead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('nvertices'),
      overflow=overflow,
      #rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("number of Reco Vertex"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('nj'),
      overflow=overflow,
      #rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("number of jets"),
      labely = cms.untracked.string("Events ")
    ),
    cms.PSet(
          name = cms.string('el1pt'),
          overflow=overflow,
	  rebin = cms.untracked.uint32(5),
	  #logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("p_{T}^{e_{1}} (GeV)"),
	  labely = cms.untracked.string("Events/5GeV"),
          rangex = cms.untracked.vdouble(0.,250.)
    ),
    cms.PSet(
          name = cms.string('el1eta'),
	  #rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("#eta^{e_{1}}"),
	  labely = cms.untracked.string("Events")
    ),
    cms.PSet(
          name = cms.string('el1etapm'),
	  rebin = cms.untracked.uint32(2),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("#eta^{e_{1}}"),
	  labely = cms.untracked.string("Events")
    ),
    cms.PSet(
          name = cms.string('el2pt'),
          overflow=overflow,
	  rebin = cms.untracked.uint32(5),
	  #logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("p_{T}^{e_{2}} (GeV)"),
	  labely = cms.untracked.string("Events/5GeV"),
          rangex = cms.untracked.vdouble(0.,150.)
    ),
     cms.PSet(
          name = cms.string('el2eta'),
	  #rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("#eta^{e_{2}}"),
	  labely = cms.untracked.string("Events")
    ),
     cms.PSet(
          name = cms.string('el2etapm'),
	  rebin = cms.untracked.uint32(2),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("#eta^{e_{2}}"),
	  labely = cms.untracked.string("Events")
    ),
    cms.PSet(
          name = cms.string('mu1pt'),
          overflow=overflow,
	  rebin = cms.untracked.uint32(5),
	  #logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("p_{T}^{#mu_{1}} (GeV)"),
	  labely = cms.untracked.string("Events/5GeV"),
          rangex = cms.untracked.vdouble(0.,250.)
    ),
     cms.PSet(
          name = cms.string('mu1eta'),
	  #rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("#eta^{#mu_{1}}"),
	  labely = cms.untracked.string("Events")
    ),
     cms.PSet(
          name = cms.string('mu1etapm'),
	  rebin = cms.untracked.uint32(2),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("#eta^{#mu_{1}}"),
	  labely = cms.untracked.string("Events")
    ),
    cms.PSet(
          name = cms.string('mu2pt'),
          overflow=overflow,
	  rebin = cms.untracked.uint32(5),
	  #logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("p_{T}^{#mu_{2}} (GeV)"),
	  labely = cms.untracked.string("Events/5GeV"),
          rangex = cms.untracked.vdouble(0.,150.)
    ),
    cms.PSet(
          name = cms.string('mu2eta'),
	  #rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("#eta^{#mu_{2}}"),
	  labely = cms.untracked.string("Events")
    ),
    cms.PSet(
          name = cms.string('mu2etapm'),
	  rebin = cms.untracked.uint32(2),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("#eta^{#mu_{2}}"),
	  labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('MET'),
      overflow=overflow,
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
      labelx = cms.untracked.string("Pt imbalance between Z and leading bjet (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('ZbM'),
      overflow=overflow,
      rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{Zb} (GeV)"),
      labely = cms.untracked.string("Events/50GeV")
    ),
    cms.PSet(
      name = cms.string('ZbPt'),
      overflow=overflow,
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{Zb} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('dijetM'),
      overflow=overflow,
      rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{bb} (GeV)"),
      labely = cms.untracked.string("Events/50GeV")
    ),
    cms.PSet(
      name = cms.string('dijetPt'),
      overflow=overflow,
      rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("p_{T}^{bb} (GeV)"),
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('dijetdR'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#DeltaR(b^{1}b^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('dijetSVdR'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#DeltaR_{SV}(b^{1}b^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('dphidijetMET'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#Delta#phi(b#bar{b},MET)"),
      labely = cms.untracked.string("Events/0.2")
    ),
   cms.PSet(
      name = cms.string('drllEle'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#DeltaR(e^{1}e^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('drllMu'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#DeltaR(#mu^{1}#mu^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('drll'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#DeltaR(l^{1}l^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('ZbbM'),
      overflow=overflow,
      rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{Zbb} (GeV)"),
      labely = cms.untracked.string("Events/50GeV")
    ),
    cms.PSet(
      name = cms.string('ZbbPt'),
      overflow=overflow,
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{Zbb} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('bestzpt'),
      overflow=overflow,
      rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),          ####### /2 rebining
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('bestzptMu'),
      overflow=overflow,
      rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('bestzptEle'),
      overflow=overflow,
      rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),
      labely = cms.untracked.string("Events/20GeV")
    ),
#    cms.PSet(
#      name = cms.string('SSVHEdisc'),
#      rebin = cms.untracked.uint32(5),
#      labelx = cms.untracked.string("SSVHE discriminant"),
#      labely = cms.untracked.string("Events/0.5")
#    ),
    cms.PSet(
      name = cms.string('SVpT'),
      overflow=overflow,
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("Secondary vertex pT (GeV)"),
      labely = cms.untracked.string("Events/2")
    ),
    cms.PSet(
      name = cms.string('SSVHPdisc'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("SSVHP discriminant"),
      labely = cms.untracked.string("Events/0.5")
    ),
#    cms.PSet(
#      name = cms.string('jet1SSVHEdisc'),
#      rebin = cms.untracked.uint32(5),
#      labelx = cms.untracked.string("SSVHE discriminant"),
#      labely = cms.untracked.string("Events/0.5")
#    ),
#    cms.PSet(
#      name = cms.string('bjet1SSVHEdisc'),
#      rebin = cms.untracked.uint32(5),
#      labelx = cms.untracked.string("SSVHE discriminant b-lead jet"),
#      labely = cms.untracked.string("Events/0.5")
#    ),
    cms.PSet(
      name = cms.string('jet1SSVHPdisc'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("SSVHP discriminant"),
      labely = cms.untracked.string("Events/0.2")
    ),
#    cms.PSet(
#      name = cms.string('SSVHEdiscDisc1'),
#      rebin = cms.untracked.uint32(5),
#      labelx = cms.untracked.string("SSVHE discriminant"),
#      labely = cms.untracked.string("Events/0.5")
#    ),
    cms.PSet(
      name = cms.string('SSVHPdiscDisc1'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("SSVHP discriminant"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('dphiZbj1'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#Delta#phi(Z,b-lead)"),
      labely = cms.untracked.string("Events/0.2")
    ),
    cms.PSet(
      name = cms.string('METsignificance'),
      overflow=overflow,
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("METsignificance"),
      labely = cms.untracked.string("Events/0.5")
    ),

    ####### ATTENTION              
    cms.PSet(                                                #
      name = cms.string('dphiZbb'),                          #
      #setRangeUser = cms.
      rebin = cms.untracked.uint32(2),                       #
      labelx = cms.untracked.string("#Delta#phi_{Z,bb}"),    #
      labely = cms.untracked.string("Events/0.2")            #
    ),
    ##########################################################
    cms.PSet(
      name = cms.string('drZbj1'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#Delta R(Z,bjet_{1})"),
      labely = cms.untracked.string("Events/0.5")
    ),

    ### muons and electrons selection plots
    cms.PSet(
      name = cms.string('muonChi2'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#chi{^2}"),
      labely = cms.untracked.string("Muons")
    ),
    ###Zb quantities
    cms.PSet(
      name = cms.string('scaldptZbj1'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#Delta Pt(Z,bjet_{1})"),
      labely = cms.untracked.string("Events/10 GeV"),
      rangex = cms.untracked.vdouble(-250.,250.)
    ),
    
    ### Zbb quantities
   cms.PSet(
      name = cms.string('drZbb'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#Delta R(Z,bb)"),
      labely = cms.untracked.string("Events/0.5")
    ), 
   cms.PSet(
      name = cms.string('scaldptZbb'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#Delta Pt(Z,bb)"),
      labely = cms.untracked.string("Events/10 GeV"),
      rangex = cms.untracked.vdouble(-250.,250.)
    ),

    
  )
)
