import FWCore.ParameterSet.Config as cms
#from ROOT import EColor

from UserCode.zbb_louvain.zbbCommons import zbbnorm
#lumi=zbbnorm.lumi_tot2012*1000 #in pb-1
lumi=(19.7)*1000

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
  outputFile = cms.string('mergedPlots_2012ABCD_V1_hamb_allMC_btagSFs.root'),
    
  data = cms.VPSet (
        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_DoubleMu2012A/DoubleMu2012A_Summer12_final.root') 
            ),
        cms.PSet(
           fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_DoubleMu2012B/DoubleMu2012B_Summer12_final.root') 
            ),
        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_DoubleMu2012C/DoubleMu2012C_Summer12_final.root') 
            ),
        cms.PSet(
           fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_DoubleMu2012D/DoubleMu2012D_Summer12_final.root') 
            ),
        
  ),
    
    
  mc   = cms.VPSet (
        
        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_ZZ/ZZ_Summer12_final.root'),
            color = cms.uint32(EColor.kMagenta+palette),
            scale = cms.double(zbbnorm.xsec_ZZ_8TeV*lumi/zbbnorm.nev_ZZ_summer12),#6.206*5051./(4191045.)), #Xs 
            role = cms.string('ZZ')
            ),

        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_WZ/WZ_Summer12_final.root'),
            color = cms.uint32(EColor.kCyan+palette),
            scale = cms.double(zbbnorm.xsec_WZ_8TeV*lumi/zbbnorm.nev_WZ_summer12),#6.206*5051./(4191045.)), #Xs 
            role = cms.string('WZ')
            ),

        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_WW/WW_Summer12_final.root'),
            color = cms.uint32(EColor.kOrange+palette),
            scale = cms.double(zbbnorm.xsec_WW_8TeV*lumi/zbbnorm.nev_WW_summer12),#6.206*5051./(4191045.)), #Xs 
            role = cms.string('WW')
            ),

        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_TTFullLept/TTFullLept_Summer12_final.root'),
            color = cms.uint32(EColor.kYellow+palette),
            scale = cms.double(zbbnorm.xsec_TTFullLept_8TeV*lumi/zbbnorm.nev_TTFullLept_summer12),#157.5*5051./(3701947.)), #NLO MCFM proper Xs
            role = cms.string('t#bar{t} dilep')
            ),

        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_TTSemiLept/TTSemiLept_Summer12_final.root'),
            color = cms.uint32(EColor.kTeal+palette),
            scale = cms.double(zbbnorm.xsec_TTSemiLept_8TeV*lumi/zbbnorm.nev_TTSemiLept_summer12),#157.5*5051./(3701947.)), #NLO MCFM proper Xs
            role = cms.string('t#bar{t} lept')
            ),

        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_Wt/Wt_Summer12_final.root'),
            color = cms.uint32(EColor.kSpring+palette),
            scale = cms.double(zbbnorm.xsec_tW_8TeV*lumi/zbbnorm.nev_tW_summer12),#157.5*5051./(3701947.)), #NLO MCFM proper Xs
            role = cms.string('tW')
            ),

        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_Wtbar/Wtbar_Summer12_final.root'),
            color = cms.uint32(EColor.kSpring+palette),
            scale = cms.double(zbbnorm.xsec_tbarW_8TeV*lumi/zbbnorm.nev_tbarW_summer12),#157.5*5051./(3701947.)), #NLO MCFM proper Xs
            role = cms.string('#bar{t}W')
            ),

        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_DYjets/DYjets_Summer12_final.root'),
            color = cms.uint32(EColor.kRed+palette),
            scale = cms.double(zbbnorm.xsec_DYjets_8TeV*lumi/zbbnorm.nev_DYjets_summer12),#3048.*5051./35907791.), #NLO MCFM
            role = cms.string('Z+j')
            ), 
        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_DYjets_M10to50/DYjets_M10to50_Summer12_final.root'),
            color = cms.uint32(EColor.kRed+palette),
            scale = cms.double(zbbnorm.xsec_DYjets_M10to50_8TeV*lumi/zbbnorm.nev_DYjets_M10to50_summer12),#3048.*5051./35907791.), #NLO MCFM
            role = cms.string('Z+j')
            ), 
        cms.PSet(
            fileName = cms.string('/home/fynu/ajafari/storage/CP/V4/ControlPlots_CSV_EMU_afterSF_MC/ControlPlots_ZH125/ZH125_Summer12_final.root'),
            color = cms.uint32(EColor.kWhite),#EColor.kAzure+palette),
            scale = cms.double(zbbnorm.xsec_ZH125_8TeV*lumi/zbbnorm.nev_ZH125_summer12), #Xs 
            role = cms.string('ZH_125')
            ),
  ),

  options = cms.PSet (
      nostack = cms.untracked.bool(False),
      ratioPlot = cms.untracked.bool(True),
  ),
  formating = cms.VPSet (
    cms.PSet(
      name = cms.string('diffMassaa'),
      rebin = cms.untracked.uint32(5),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("#Delta m(a,a) (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(0.,100.)
    ),
    cms.PSet(
      name = cms.string('hMass'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Higgs mass (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(40.,940.)
    ),
    cms.PSet(
      name = cms.string('hPt'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Higgs p_{T} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(0.,700.)
    ),
    cms.PSet(
      name = cms.string('dphiHiggsMET'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#Delta #phi (H, MET)"),
      labely = cms.untracked.string("Events/0.2")
    ),
    cms.PSet(
      name = cms.string('aadR'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("#Delta R (a,a)"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('dphiaa'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#Delta #phi (a,a)"),
      labely = cms.untracked.string("Events/0.2")
    ),
    ################################################
    cms.PSet(
      name = cms.string('amassMu'),
      rebin = cms.untracked.uint32(50),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("di-#mu mass (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(0.,1000.)
    ),
    cms.PSet(
      name = cms.string('aptMu'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("di-#mu p_{T}"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(0.,700.)
    ),
    cms.PSet(
      name = cms.string('dphiaMuMET'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#Delta #phi (a_{#mu}, MET)"),
      labely = cms.untracked.string("Events/0.2")
    ),
    cms.PSet(
      name = cms.string('diMudR'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("#Delta R (#mu,#mu)"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('dphidiMu'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#Delta #phi (#mu,#mu)"),
      labely = cms.untracked.string("Events/0.2")
    ),
    ################################################
    cms.PSet(
      name = cms.string('amassBjet'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("di-b-jet mass (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(0.,1000.)
    ),
    cms.PSet(
      name = cms.string('aptBjet'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("di-b-jet p_{T} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(0.,700.)
    ),
    cms.PSet(
      name = cms.string('dphiaBjetMET'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#Delta #phi (a_{b}, MET)"),
      labely = cms.untracked.string("Events/0.2")
    ),
    cms.PSet(
      name = cms.string('diBjetdR'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("#Delta R (b,b)"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('diBjetSVdR'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("#Delta R_{SV} (b,b)"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('dphidiBjet'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#Delta #phi (b,b)"),
      labely = cms.untracked.string("Events/0.2")
    ),
    ################################################   
    cms.PSet(
      name = cms.string('mu1pt'),
	    labelx = cms.untracked.string("p_{T}^{#mu_{1}} (GeV)"),
	    labely = cms.untracked.string("Events/5GeV"),
      rangex = cms.untracked.vdouble(0.,250.)
    ),
    cms.PSet(
      name = cms.string('mu1eta'),
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
      labelx = cms.untracked.string("p_{T}^{#mu_{2}} (GeV)"),
      labely = cms.untracked.string("Events/5GeV"),
      rangex = cms.untracked.vdouble(0.,150.)
    ),
    cms.PSet(
      name = cms.string('mu2eta'),
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
      name = cms.string('METsignificance_hamb'),
      overflow = cms.untracked.bool(True),
      labelx = cms.untracked.string("Missing transverse energy significance"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('MET_hamb'),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("Missing transverse energy (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    ################################################       
    
    cms.PSet(
      name = cms.string('jet2pt'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{sublead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('nvertices'),
      #rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("number of Reco Vertex"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('nj'),
      #rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("number of jets"),
      labely = cms.untracked.string("Events ")
    ),   
  )
)

