import FWCore.ParameterSet.Config as cms
#from ROOT import EColor

#from UserCode.zbb_louvain.zbbCommons import zbbnorm
import os, sys
lib_path = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/storm-0.20-py2.7-linux-x86_64.egg/')
lib_path2 = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/MySQL_python-1.2.3-py2.7-linux-x86_64.egg')
lib_path3 = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg/')
sys.path.append(lib_path)
sys.path.append(lib_path2)
sys.path.append(lib_path3)
from UserCode.zbb_louvain.zbbSamples import *
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
  outputFile = cms.string('mergedPlots_2012ABCD_V1_higgs_allMC_30GeV_stage18_database.root'),
    
  data = cms.VPSet (
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_DoubleEle2012A/DoubleEle2012A_Summer12_final.root')
            ), 
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_DoubleEle2012B/DoubleEle2012B_Summer12_final.root')
            ), 
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_DoubleEle2012C/DoubleEle2012C_Summer12_final.root')
            ), 
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_DoubleEle2012D/DoubleEle2012D_Summer12_final.root')
            ), 

        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_DoubleMu2012A/DoubleMu2012A_Summer12_final.root') 
            ),
        cms.PSet(
           fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_DoubleMu2012B/DoubleMu2012B_Summer12_final.root') 
            ),
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_DoubleMu2012C/DoubleMu2012C_Summer12_final.root') 
            ),
        cms.PSet(
           fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_DoubleMu2012D/DoubleMu2012D_Summer12_final.root') 
            ),
        
  ),
    
    
  mc   = cms.VPSet (
        
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_ZZ/ZZ_Summer12_final.root'),
            color = cms.uint32(EColor.kMagenta+palette),
            scale = cms.double(getSample(name="ZZ_2014").source_dataset.xsection*lumi/getSample(name="ZZ_2014").nevents_processed),#6.206*5051./(4191045.)), #Xs 
            role = cms.string('ZZ')
            ),

        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_WZ/WZ_Summer12_final.root'),
            color = cms.uint32(EColor.kCyan+palette),
            scale = cms.double(getSample(name="WZ_2014").source_dataset.xsection*lumi/getSample(name="WZ_2014").nevents_processed),#6.206*5051./(4191045.)), #Xs 
            role = cms.string('WZ')
            ),

        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_WW/WW_Summer12_final.root'),
            color = cms.uint32(EColor.kOrange+palette),
            scale = cms.double(getSample(name="WW_2014").source_dataset.xsection*lumi/getSample(name="WW_2014").nevents_processed),#6.206*5051./(4191045.)), #Xs 
            role = cms.string('WW')
            ),

        cms.PSet(
            #fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp537/ControlPlots_V12/ControlPlots_TTjets/TTjets_Summer12_final.root'),
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_TTFullLept/TTFullLept_Summer12_final.root'),
            color = cms.uint32(EColor.kYellow+palette),
            #scale = cms.double(getSample(name="_2014").source_dataset.xsectionTTjets_8TeV*lumi/getSample(name="_2014").nevents_processedTTjets_summer12),#157.5*5051./(3701947.)), #NLO MCFM proper Xs
            scale = cms.double(getSample(name="TTFullLept_2014").source_dataset.xsection*lumi/getSample(name="TTFullLept_2014").nevents_processed),#157.5*5051./(3701947.)), #NLO MCFM proper Xs
            role = cms.string('t#bar{t} dilep')
            ),

        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_TTSemiLept/TTSemiLept_Summer12_final.root'),
            color = cms.uint32(EColor.kTeal+palette),
            scale = cms.double(getSample(name="TTSemiLept_2014").source_dataset.xsection*lumi/getSample(name="TTSemiLept_2014").nevents_processed),#157.5*5051./(3701947.)), #NLO MCFM proper Xs
            role = cms.string('t#bar{t} lept')
            ),

        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_Wt/Wt_Summer12_final.root'),
            color = cms.uint32(EColor.kSpring+palette),
            scale = cms.double(getSample(name="Wt_2014").source_dataset.xsection*lumi/getSample(name="Wt_2014").nevents_processed),#157.5*5051./(3701947.)), #NLO MCFM proper Xs
            role = cms.string('tW')
            ),

        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_Wtbar/Wtbar_Summer12_final.root'),
            color = cms.uint32(EColor.kSpring+palette),
            scale = cms.double(getSample(name="Wtbar_2014").source_dataset.xsection*lumi/getSample(name="Wtbar_2014").nevents_processed),#157.5*5051./(3701947.)), #NLO MCFM proper Xs
            role = cms.string('#bar{t}W')
            ),

        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_DYjets_0b/DYjets_0b_Summer12_final.root'),
            color = cms.uint32(EColor.kBlue+palette),
            scale = cms.double(getSample(name="DY_2014").source_dataset.xsection*lumi/getSample(name="DY_2014").nevents_processed),#3048.*5051./35907791.), #NLO MCFM
            role = cms.string('Z+xx')
            ),
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_DYjets_1b/DYjets_1b_Summer12_final.root'),     
            color = cms.uint32(EColor.kGreen+palette),
            scale = cms.double(getSample(name="DY_2014").source_dataset.xsection*lumi/getSample(name="DY_2014").nevents_processed),#3048.*5051./35907791.), #NLO MCFM
            role = cms.string('Z+bx')
            ), 
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_DYjets_2b/DYjets_2b_Summer12_final.root'),
            #fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp537/ControlPlots_V40/ControlPlots_Zbb_Zb/Zbb_Zb_Summer12_final.root'),
            color = cms.uint32(EColor.kRed+palette),
            scale = cms.double(getSample(name="DY_2014").source_dataset.xsection*lumi/getSample(name="DY_2014").nevents_processed),#3048.*5051./35907791.), #NLO MCFM
            #scale = cms.double(getSample(name="_2014").source_dataset.xsectionZbb_8TeV*lumi/getSample(name="_2014").nevents_processedZbb_summer12),
            role = cms.string('Z+bb')
            ), 
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_ZH125/ZH125_Summer12_final.root'),
            color = cms.uint32(EColor.kWhite),#EColor.kAzure+palette),
            scale = cms.double(getSample(name="ZH125_2014").source_dataset.xsection*lumi/getSample(name="DY_2014").nevents_processed), #Xs 
            role = cms.string('ZH_125')
            ),
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_ZA_350_15/ZA_350_15_Summer12_final.root'),
            color = cms.uint32(1),#EColor.kAzure+palette),
            scale = cms.double(50*getSample(name="ZH125_2014").source_dataset.xsection*lumi/getSample(name="ZH125_2014").nevents_processed), #Xs 
            role = cms.string('50*ZA_350_15'),
            stacked = cms.untracked.bool(False)
            ),
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_ZA_350_30/ZA_350_30_Summer12_final.root'),
            color = cms.uint32(3),#EColor.kAzure+palette),
            scale = cms.double(50*getSample(name="ZH125_2014").source_dataset.xsection*lumi/getSample(name="ZH125_2014").nevents_processed), #Xs 
            role = cms.string('50*ZA_350_30'),
            stacked = cms.untracked.bool(False)
            ),
        cms.PSet(
            fileName = cms.string('/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V40/ControlPlots_ZA_350_70/ZA_350_70_Summer12_final.root'),
            color = cms.uint32(4),#EColor.kAzure+palette),
            scale = cms.double(50*getSample(name="ZH125_2014").source_dataset.xsection*lumi/getSample(name="ZH125_2014").nevents_processed), #Xs 
            role = cms.string('50*ZA_350_70'),
            stacked = cms.untracked.bool(False)
            ),
  ),

  options = cms.PSet (
      nostack = cms.untracked.bool(False),
  ),
  formating = cms.VPSet (
    cms.PSet(
      name = cms.string('bestzmass'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{Z} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(76.,106.)
    ),
    cms.PSet(
      name = cms.string('bestzmassMu'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{#mu^{+}#mu^{-}} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(76.,106.)
    ),
    cms.PSet(
      name = cms.string('bestzmassEle'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{e^{+}e^{-}} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(76.,106.)
    ),
    cms.PSet(
      name = cms.string('bjet1pt'),
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
    cms.PSet(
          name = cms.string('el1pt'),
	  #rebin = cms.untracked.uint32(10),
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
	  #rebin = cms.untracked.uint32(5),
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
	  #rebin = cms.untracked.uint32(5),
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
	  #rebin = cms.untracked.uint32(5),
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
      logy = cms.untracked.bool(True),
      #rebin = cms.untracked.uint32(5),
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
      rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{Zb} (GeV)"),
      labely = cms.untracked.string("Events/50GeV")
    ),
    cms.PSet(
      name = cms.string('ZbPt'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{Zb} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('dijetM'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("M_{bb} (GeV)"),
      labely = cms.untracked.string("Events/5GeV")
    ),
    cms.PSet(
      name = cms.string('dijetPt'),
      rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("p_{T}^{bb} (GeV)"),
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('dijetdR'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#DeltaR(b^{1}b^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('dijetSVdR'),
      #rebin = cms.untracked.uint32(10),
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
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#DeltaR(e^{1}e^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('drllMu'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#DeltaR(#mu^{1}#mu^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('drll'),
      #rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#DeltaR(l^{1}l^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('ZbbM'),
      rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{Zbb} (GeV)"),
      labely = cms.untracked.string("Events/50GeV")
    ),
    cms.PSet(
      name = cms.string('ZbbPt'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{Zbb} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('bestzpt'),
      rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),          ####### /2 rebining
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('bestzptMu'),
      rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('bestzptEle'),
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
      #rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("Secondary vertex pT (GeV)"),
      labely = cms.untracked.string("Events/2")
    ),
    cms.PSet(
      name = cms.string('SSVHPdisc'),
      #rebin = cms.untracked.uint32(5),
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
      #rebin = cms.untracked.uint32(5),
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
      overflow = cms.untracked.bool(True),
      #rebin = cms.untracked.uint32(5),
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
      #rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#Delta Pt(Z,bjet_{1})"),
      labely = cms.untracked.string("Events/10 GeV"),
      rangex = cms.untracked.vdouble(-250.,250.)
    ),
    
    ### Zbb quantities
   cms.PSet(
      name = cms.string('drZbb'),
      #rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#Delta R(Z,bb)"),
      labely = cms.untracked.string("Events/0.5")
    ), 
   cms.PSet(
      name = cms.string('scaldptZbb'),
      #rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#Delta Pt(Z,bb)"),
      labely = cms.untracked.string("Events/10 GeV"),
      rangex = cms.untracked.vdouble(-250.,250.)
    ),

    
  )
)
