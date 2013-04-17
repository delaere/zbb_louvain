import FWCore.ParameterSet.Config as cms

from UserCode.zbb_louvain.zbbCommons import zbbnorm
lumi=zbbnorm.lumi_tot2012*1000 #in pb-1
from UserCode.zbb_louvain.listForRDS import nev_DYjets_summer12

flow="overflow"
#flow=""
if flow=="overflow" : overflow = cms.untracked.bool(True)
else : overflow = cms.untracked.bool(False)

DIR="hist_afterFit_zptrew"
WP="18"

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
  outputFile = cms.string(DIR+'/MERGEDoverflow.root'),
  data = cms.VPSet (
   cms.PSet(
     fileName = cms.string(DIR+'/histoStage'+WP+'extraCutsDATA.root')
   ),
  ),
  mc   = cms.VPSet (
   cms.PSet(
     fileName = cms.string(DIR+'/histoStage'+WP+'extraCutsZZ.root'),
     color = cms.uint32(EColor.kMagenta+palette),
     scale = cms.double(zbbnorm.xsec_ZZ_8TeV*lumi/zbbnorm.nev_ZZ_summer12), 
     role = cms.string('ZZ')
   ),
   cms.PSet(
     fileName = cms.string(DIR+'/histoStage'+WP+'extraCutsTT.root'),
     color = cms.uint32(EColor.kYellow+palette),
     scale = cms.double(zbbnorm.xsec_TTjets_8TeV*lumi/zbbnorm.nev_TTjets_summer12), #NLO k=1.67
     role = cms.string('ttbar'),
   ),
   cms.PSet(
     fileName = cms.string(DIR+'/histoStage'+WP+'extraCutsZbb.root'),
     color = cms.uint32(EColor.kRed+palette),
     scale = cms.double(zbbnorm.xsec_DYjets_8TeV*lumi/zbbnorm.nev_DYjets_summer12), 
     role = cms.string('Z+bb')
   ),
   cms.PSet(
    fileName = cms.string(DIR+'/histoStage'+WP+'extraCutsZbx.root'),
    color = cms.uint32(EColor.kGreen+palette),
    scale = cms.double(zbbnorm.xsec_DYjets_8TeV*lumi/zbbnorm.nev_DYjets_summer12), 
    role = cms.string('Z+bx')
   ),
   cms.PSet(
    fileName = cms.string(DIR+'/histoStage'+WP+'extraCutsZxx.root'),
    color = cms.uint32(EColor.kBlue+palette),
    scale = cms.double(zbbnorm.xsec_DYjets_8TeV*lumi/zbbnorm.nev_DYjets_summer12), 
    role = cms.string('Z+xx')
   ),
   #cms.PSet(
   #  fileName = cms.string('histoStage'+WP+'extraCutsZA.root'),
   #  color = cms.uint32(1),
   #  scale = cms.double(100*0.003*5051/70000), 
   #  role = cms.string('100*ZA'),
   #  stacked = cms.untracked.bool(False)
   #),
#   cms.PSet(
#    fileName = cms.string(DIR+'/histoStage'+WP+'extraCutsZH125.root'),
#    color = cms.uint32(1),
#    scale = cms.double(100*zbbnorm.xsec_ZH125_8TeV*lumi/zbbnorm.nev_ZH125_summer12), 
#    role = cms.string('100*ZH M_H=125'),
#    stacked = cms.untracked.bool(False)
#   ),
  ),
  options = cms.PSet (
          # nostack: if set, none of the curves will be stacked. That overrides the mc set option
          nostack = cms.untracked.bool(False),
                # luminosity, in pb
          luminosity = cms.untracked.double(5051.),
                # if autoLumiScaling is set, luminosity will multiply each mc scale.
          autoLumiScaling = cms.untracked.bool(False),
                # label to be set on plots
          label = cms.untracked.string(""),
          #label = cms.untracked.string("#splitline{CMS}{#sqrt{s} = 8 TeV, L = 4.2 - 5.2 fb^{-1}}"),
          ),
  formating = cms.VPSet (
    cms.PSet(
      name = cms.string('eventSelectionbestzmass'),
      overflow=overflow,
      #rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{Z} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(60.,120.)
    ),
    cms.PSet(
      name = cms.string('eventSelectionbestzmassMu'),
      overflow=overflow,
      #rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{#mu^{+}#mu^{-}} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(60.,120.)
    ),
    cms.PSet(
      name = cms.string('eventSelectionbestzmassEle'),
      overflow=overflow,
      #rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{e^{+}e^{-}} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(60.,120.)
    ),
    cms.PSet(
      name = cms.string('jetmetbjet1pt'),
      overflow=overflow,
      begin = cms.untracked.double(25),
      end = cms.untracked.double(265),
      width = cms.untracked.double(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{b-lead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('jetmetbjet2pt'),
      overflow=overflow,
      #rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{b-sublead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('jetmetjet1pt'),
      overflow=overflow,
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{lead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('jetmetjet1etapm'),
      labelx = cms.untracked.string("#eta^{lead}"),
      labely = cms.untracked.string("Events/0.1")
    ),
    cms.PSet(
      name = cms.string('jetmetjet2pt'),
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
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("number of Reco Vertex"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('jetmetnj'),
      overflow=overflow,
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("number of jets"),
      labely = cms.untracked.string("Events ")
    ),
    cms.PSet(
      name = cms.string('el1pt'),
      overflow=overflow,
      rebin = cms.untracked.uint32(5),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{e_{1}} (GeV)"),
      labely = cms.untracked.string("Events/5GeV")
    ),
    cms.PSet(
      name = cms.string('el1eta'),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("#eta^{e_{1}}"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('el2pt'),
      overflow=overflow,
      rebin = cms.untracked.uint32(5),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{e_{2}} (GeV)"),
      labely = cms.untracked.string("Events/5GeV")
    ),
     cms.PSet(
       name = cms.string('el2eta'),
       logy = cms.untracked.bool(True),
       labelx = cms.untracked.string("#eta^{e_{2}}"),
       labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('mu1pt'),
      rebin = cms.untracked.uint32(5),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{#mu_{1}} (GeV)"),
      labely = cms.untracked.string("Events/5GeV")
    ),
     cms.PSet(
       name = cms.string('mu1eta'),
       logy = cms.untracked.bool(True),
       labelx = cms.untracked.string("#eta^{#mu_{1}}"),
       labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('mu2pt'),
      rebin = cms.untracked.uint32(5),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{#mu_{2}} (GeV)"),
      labely = cms.untracked.string("Events/5GeV")
    ),
    cms.PSet(
      name = cms.string('mu2eta'),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("#eta^{#mu_{2}}"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('jetmetMET'),
      logy = cms.untracked.bool(False),
      #rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("MET (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('jetmetMETsignificance'),
      logy = cms.untracked.bool(False),
      #rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("MET significance"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('eventSelectionvecdptZbj1'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Pt imbalance between Z and leading bjet (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('eventSelectionZbM'),
      #rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{Zb} (GeV)"),
      labely = cms.untracked.string("Events/50GeV")
    ),
    cms.PSet(
      name = cms.string('eventSelectionZbPt'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{Zb} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('eventSelectiondijetM'),
      #rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{bb} (GeV)"),
      labely = cms.untracked.string("Events/50GeV")
    ),
    cms.PSet(
      name = cms.string('eventSelectiondijetPt'),
      #rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("p_{T}^{bb} (GeV)"),
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('eventSelectiondijetdR'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Delta_R(b^{1}b^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('eventSelectiondrmumu'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Delta_R(#mu^{1}#mu^{2})"),
      labely = cms.untracked.string("Events/0.5"),
      rangex = cms.untracked.vdouble(0.,5.)
    ),
    cms.PSet(
      name = cms.string('eventSelectiondrelel'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Delta_R(e^{1}e^{2}) (GeV)"),
      labely = cms.untracked.string("Events/0.5"),
      rangex = cms.untracked.vdouble(0.,5.)
     ),
    cms.PSet(
      name = cms.string('eventSelectiondijetSVdR'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Delta_R_SV(b^{1}b^{2}) (GeV)"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('eventSelectionZbbM'),
      #rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{Zbb} (GeV)"),
      labely = cms.untracked.string("Events/50GeV")
    ),
    cms.PSet(
      name = cms.string('eventSelectionZbbPt'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{Zbb} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('eventSelectionbestzpt'),
      #rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),     
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('eventSelectionbestzptMu'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('eventSelectionbestzptEle'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('jetmetSSVHPdisc'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("SSVHP discriminant"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('jetmetjet1SSVHPdisc'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("SSVHP discriminant"),
      labely = cms.untracked.string("Events/0.2")
    ),
    cms.PSet(
      name = cms.string('jetmetSSVHPdiscDisc1'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("SSVHP discriminant"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('eventSelectiondphiZbj1'),
      #rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#Delta#phi(Z,b-lead)"),
      labely = cms.untracked.string("Events/0.2")
    ),
    cms.PSet(                                                
      name = cms.string('eventSelectiondphiZbb'),                          
      #rebin = cms.untracked.uint32(2),                       
      labelx = cms.untracked.string("#Delta#phi_{Z,bb}"),    
      labely = cms.untracked.string("Events/0.2")            
    ),
    cms.PSet(
      name = cms.string('eventSelectiondrZbj1'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#Delta R(Z,bjet_{1})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('muonChi2'),
      labelx = cms.untracked.string("#chi{^2}"),
      labely = cms.untracked.string("Muons")
    ),
    cms.PSet(
      name = cms.string('eventSelectionscaldptZbj1'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#Delta Pt(Z,bjet_{1})"),
      labely = cms.untracked.string("Events/10 GeV")
    ),
    cms.PSet(
      name = cms.string('eventSelectiondrZbb'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#Delta R(Z,bb)"),
      labely = cms.untracked.string("Events/5")
    ), 
   cms.PSet(
      name = cms.string('eventSelectionscaldptZbb'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#Delta Pt(Z,bb)"),
      labely = cms.untracked.string("Events/10 GeV")
    ),
  )
)
