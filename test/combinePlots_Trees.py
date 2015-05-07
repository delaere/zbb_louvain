## Combine plots from different samples and make the comparison to the data ##
## Costumized to run on plots produced from trees ##

import FWCore.ParameterSet.Config as cms
### Get normalisation factor ###
from UserCode.zbb_louvain.pyrootScripts.llbbNorm import *

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

### read the input directory ###
f = open("input.txt","r")
DIR = f.read()
DIR = DIR.replace("\n","")
print DIR
#DIR = "ZbbMET_beforeRew_ZjjM_largerbin"

process.CombinePlots = cms.PSet(
  outputFile = cms.string(DIR+'_testRew.root'),
    
  data = cms.VPSet (
        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/Data2012.root')
            ), 
        
  ),
    
  mc   = cms.VPSet (
        
        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/ZZ.root'),
            color = cms.uint32(EColor.kMagenta+palette),
            scale = cms.double(lumi["DATA"]/lumi["ZZ"]),
            role = cms.string('ZZ')
            ),

        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/WZ.root'),
            color = cms.uint32(EColor.kCyan+palette),
            scale = cms.double(lumi["DATA"]/lumi["WZ"]), 
            role = cms.string('WZ')
            ),

        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/WW.root'),
            color = cms.uint32(EColor.kOrange+palette),
            scale = cms.double(lumi["DATA"]/lumi["WW"]),
            role = cms.string('WW')
            ),

        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/TTFullLept.root'),
            color = cms.uint32(EColor.kYellow+palette),
            scale = cms.double(lumi["DATA"]/lumi["TTFullLept"]),
            role = cms.string('t#bar{t} dilep')
            ),

        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/TTSemiLept.root'),
            color = cms.uint32(EColor.kTeal+palette),
            scale = cms.double(lumi["DATA"]/lumi["TTSemiLept"]),
            role = cms.string('t#bar{t} lept')
            ),

        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/Wt.root'),
            color = cms.uint32(EColor.kSpring+palette),
            scale = cms.double(lumi["DATA"]/lumi["Wt"]),
            role = cms.string('tW')
            ),

        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/Wtbar.root'),
            color = cms.uint32(EColor.kSpring+palette),
            scale = cms.double(lumi["DATA"]/lumi["Wtbar"]),
            role = cms.string('#bar{t}W')
            ),

        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/Zxx.root'),
            color = cms.uint32(EColor.kBlue+palette),
            scale = cms.double(lumi["DATA"]/lumi["Zxx"]),
            role = cms.string('Z+xx')
            ),

        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/Zbx.root'),     
            color = cms.uint32(EColor.kGreen+palette),
            scale = cms.double(lumi["DATA"]/lumi["Zbx"]),
            role = cms.string('Z+bx')
            ), 

        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/Zbb.root'),
            color = cms.uint32(EColor.kRed+palette),
            scale = cms.double(lumi["DATA"]/lumi["Zbb"]),
            role = cms.string('Z+bb')
            ), 

        cms.PSet(
            fileName = cms.string('../python/pyrootScripts/'+DIR+'/ZH125.root'),
            color = cms.uint32(EColor.kWhite),#EColor.kAzure+palette),
            scale = cms.double(lumi["DATA"]/lumi["ZH125"]),
            role = cms.string('Zh')
            ),
#        cms.PSet(
#            fileName = cms.string('../python/pyrootScripts/'+DIR+'/ZA_662_500.root'),
#            color = cms.uint32(EColor.kWhite),#EColor.kAzure+palette),
#            scale = cms.double(3000*4.2917282143e-03*19.7/25000), #Xs 
#            role = cms.string('3000*ZA_662_500'),
            #stacked = cms.untracked.bool(False)
#            ),
#        cms.PSet(
#            fileName = cms.string('../python/pyrootScripts/'+DIR+'/ZA_286_93.root'),
#            color = cms.uint32(EColor.kWhite),#EColor.kAzure+palette),
#            scale = cms.double(1000*0.0941904290405*19.7/25000), #Xs 
#            role = cms.string('ZA_286_93'),
            #stacked = cms.untracked.bool(False)
#            ),
#        cms.PSet(
#            fileName = cms.string('../python/pyrootScripts/'+DIR+'/ZA_660_450.root'),
#            color = cms.uint32(EColor.kWhite),#EColor.kAzure+palette),
#            scale = cms.double(3000*8.272e-03*19.7/25000), #Xs 
#            role = cms.string('3000*ZA_660_450'),
            #stacked = cms.untracked.bool(False)
#            ),
#        cms.PSet(
#            fileName = cms.string('../python/pyrootScripts/'+DIR+'/ZA_262_99.root'),
#            color = cms.uint32(EColor.kWhite),#EColor.kAzure+palette),
#            scale = cms.double(1000*0.1112*19.7/25000), #Xs 
#            role = cms.string('ZA_262_99'),
            #stacked = cms.untracked.bool(False)
#            ),
        #cms.PSet(
            #fileName = cms.string('../python/pyrootScripts/'+DIR+'/ControlPlots_ZA_350_30/ZA_350_30_Summer12_final.root'),
            #color = cms.uint32(3),#EColor.kAzure+palette),
            #scale = cms.double(50*getSample(name="ZH125_2014").source_dataset.xsection*lumi/getSample(name="ZH125_2014").nevents_processed), #Xs 
            #role = cms.string('50*ZA_350_30'),
            #stacked = cms.untracked.bool(False)
            #),
        #cms.PSet(
            #fileName = cms.string('../python/pyrootScripts/'+DIR+'/ControlPlots_ZA_350_70/ZA_350_70_Summer12_final.root'),
            #color = cms.uint32(4),#EColor.kAzure+palette),
            #scale = cms.double(50*getSample(name="ZH125_2014").source_dataset.xsection*lumi/getSample(name="ZH125_2014").nevents_processed), #Xs 
            #role = cms.string('50*ZA_350_70'),
            #stacked = cms.untracked.bool(False)
            #),
  ),

  options = cms.PSet (
      nostack = cms.untracked.bool(False),
  ),
  formating = cms.VPSet (
    
    cms.PSet(
      name = cms.string('boostselectionbestzmass'),
      rebin = cms.untracked.uint32(2),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("M_{ll} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      #rangex = cms.untracked.vdouble(76.,106.)
    ),
    cms.PSet(
      name = cms.string('boostselectionbestzmassMu'),
      rebin = cms.untracked.uint32(2),
      logx = cms.untracked.bool(False),
      #logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{#mu^{+}#mu^{-}} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      #rangex = cms.untracked.vdouble(76.,106.)
    ),
    cms.PSet(
      name = cms.string('boostselectionbestzmassEle'),
      rebin = cms.untracked.uint32(2),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("M_{e^{+}e^{-}} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      #rangex = cms.untracked.vdouble(76.,106.)
    ),

    cms.PSet(
      name = cms.string('boostselectionbestzpt'),
      rebin = cms.untracked.uint32(6),
      #rangex = cms.untracked.vdouble(0.,500.),
      labelx = cms.untracked.string("p_{T}^{ll} (GeV)"),          ####### /2 #rebining
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('boostselectionbestzptMu'),
      rebin = cms.untracked.uint32(6),
      #rangex = cms.untracked.vdouble(0.,500.),
      labelx = cms.untracked.string("p_{T}^{ll} (GeV)"),
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('boostselectionbestzptEle'),
      rebin = cms.untracked.uint32(6),
      #rangex = cms.untracked.vdouble(0.,500.),
      labelx = cms.untracked.string("p_{T}^{ll} (GeV)"),
      labely = cms.untracked.string("Events/20GeV")
    ),

    cms.PSet(
      name = cms.string('boostselectionbestzeta'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("#eta_{ll}"),
      labely = cms.untracked.string("Events/0.4"),
    ),
    cms.PSet(
      name = cms.string('boostselectionbestzetaMu'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("#eta_{#mu^{+}#mu^{-}}"),
      labely = cms.untracked.string("Events/0.4"),
    ),
    cms.PSet(
      name = cms.string('boostselectionbestzetaEle'),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("#eta_{e^{+}e^{-}}"),
      labely = cms.untracked.string("Events/0.4"),
    ),

    cms.PSet(
      name = cms.string('boostselectionbestzphi'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("#phi_{ll}"),
      labely = cms.untracked.string("Events/0.365"),
    ),
    cms.PSet(
      name = cms.string('boostselectionbestzphiMu'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("#phi_{#mu^{+}#mu^{-}}"),
      labely = cms.untracked.string("Events/0.365"),
    ),
    cms.PSet(
      name = cms.string('boostselectionbestzphiEle'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("#phi_{e^{+}e^{-}}"),
      labely = cms.untracked.string("Events/0.365"),
    ),

   cms.PSet(
      name = cms.string('boostselectiondrllEle'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#DeltaR(e^{1}e^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('boostselectiondrllMu'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#DeltaR(#mu^{1}#mu^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('boostselectiondrll'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#DeltaR(l^{1}l^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),

    cms.PSet(
      name = cms.string('boostselectiondijetM'),
      begin = cms.untracked.double(0),
      end = cms.untracked.double(630),
      width = cms.untracked.double(30),
      #rebin = cms.untracked.uint32(30),
      rangex = cms.untracked.vdouble(0.,600.),
      overflow = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{bb} (GeV)"),
      labely = cms.untracked.string("Events/30GeV")
    ),
    cms.PSet(
      name = cms.string('boostselectiondijetPt'),
      rebin = cms.untracked.uint32(20),
      #rangex = cms.untracked.vdouble(0.,500.),
      labelx = cms.untracked.string("p_{T}^{bb} (GeV)"),
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('boostselectiondijetdR'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#DeltaR(b^{1}b^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('detab1b2'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#Delta#eta(b^{1}b^{2})"),
      labely = cms.untracked.string("Events/0.8")
    ),
    cms.PSet(
      name = cms.string('boostselectiondijetEta'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#eta(bb)"),
      labely = cms.untracked.string("Events/0.4")
    ),
    cms.PSet(
      name = cms.string('boostselectiondijetPhi'),
      rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("#phi(bb)"),
      labely = cms.untracked.string("Events/0.365")
    ),
    cms.PSet(
      name = cms.string('detab1b2'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#Delta#eta(b^{1}b^{2})"),
      labely = cms.untracked.string("Events/0.5")
    ),

    cms.PSet(
      name = cms.string('boostselectionZbbM'),
      begin = cms.untracked.double(0),
      end = cms.untracked.double(1050),
      width = cms.untracked.double(50),
      #rebin = cms.untracked.uint32(50),
      overflow = cms.untracked.bool(True),
      rangex = cms.untracked.vdouble(0.,1000.),
      labelx = cms.untracked.string("M_{llbb} (GeV)"),
      labely = cms.untracked.string("Events/50GeV")
    ),
    cms.PSet(
      name = cms.string('boostselectionZbbPt'),
      rebin = cms.untracked.uint32(20),
      #rangex = cms.untracked.vdouble(0.,500.),
      labelx = cms.untracked.string("p_{T}^{llbb} (GeV)"),
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(                                                #
      name = cms.string('boostselectiondphiZbb'),                          #
      rebin = cms.untracked.uint32(40),                       #
      labelx = cms.untracked.string("#Delta#phi_{ll,bb}"),    #
      labely = cms.untracked.string("Events/0.315")            #
    ),
    cms.PSet(                                                #
      name = cms.string('detaZbb'),                          #
      rebin = cms.untracked.uint32(10),                       #
      labelx = cms.untracked.string("#Delta#eta_{ll,bb}"),    #
      labely = cms.untracked.string("Events/0.4")            #
    ),
   cms.PSet(
      name = cms.string('boostselectiondrZbb'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#Delta R(ll,bb)"),
      labely = cms.untracked.string("Events/0.5")
    ), 
    cms.PSet(
      name = cms.string('boostselectionZbbEta'),
      rebin = cms.untracked.uint32(10),
      ##rangex = cms.untracked.vdouble(0.,1000.),
      labelx = cms.untracked.string("#eta_{llbb}"),
      labely = cms.untracked.string("Events/0.4")
    ),
    cms.PSet(
      name = cms.string('boostselectionZbbPhi'),
      rebin = cms.untracked.uint32(20),
      ##rangex = cms.untracked.vdouble(0.,1000.),
      labelx = cms.untracked.string("#phi_{llbb}"),
      labely = cms.untracked.string("Events/0.365")
    ),
   cms.PSet(
      name = cms.string('boostselectionCentrality'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("Centrality"),
      labely = cms.untracked.string("Events/1.0"),
    ),
   cms.PSet(
      name = cms.string('boostselectionCentralityBoost'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("Centrality in rest frame"),
      labely = cms.untracked.string("Events/1.0"),
    ),

    cms.PSet(
      name = cms.string('jetmetbjet1pt'),
      #begin = cms.untracked.double(0),
      #end = cms.untracked.double(990),
      #width = cms.untracked.double(15),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("p_{T}^{b-lead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('jetmetbjet2pt'),
      #begin = cms.untracked.double(0),
      #end = cms.untracked.double(990),
      #width = cms.untracked.double(15),
      rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("p_{T}^{b-sublead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('jetmetbjet1eta'),
      #begin = cms.untracked.double(0),
      #end = cms.untracked.double(990),
      #width = cms.untracked.double(15),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("|#eta^{b-lead}|"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('jetmetbjet2eta'),
      #begin = cms.untracked.double(0),
      #end = cms.untracked.double(990),
      #width = cms.untracked.double(15),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("|#eta^{b-sublead}|"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('jetmetjet1pt'),
      #rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
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
      #rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("p_{T}^{sublead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('vertexAssociationnvertices'),
      ##rebin = cms.untracked.uint32(10),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("number of Reco Vertex"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('jetmetnj'),
      logx = cms.untracked.bool(False),
      labelx = cms.untracked.string("number of jets"),
      labely = cms.untracked.string("Events ")
    ),
    cms.PSet(
      name = cms.string('boostselectionel1pt'),
      #rebin = cms.untracked.uint32(5),
      #logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{e_{1}} (GeV)"),
      labely = cms.untracked.string("Events/5GeV"),
      #rangex = cms.untracked.vdouble(0.,250.)
    ),
    cms.PSet(
      name = cms.string('boostselectionel1eta'),
      #rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#eta^{e_{1}}"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('boostselectionel1etapm'),
      #rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#eta^{e_{1}}"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('boostselectionel2pt'),
      #rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("p_{T}^{e_{2}} (GeV)"),
      labely = cms.untracked.string("Events/5GeV"),
      #rangex = cms.untracked.vdouble(0.,150.)
    ),
     cms.PSet(
      name = cms.string('boostselectionel2eta'),
      ##rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#eta^{e_{2}}"),
      labely = cms.untracked.string("Events")
    ),
     cms.PSet(
      name = cms.string('boostselectionel2etapm'),
      ##rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#eta^{e_{2}}"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('boostselectionmu1pt'),
      #rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("p_{T}^{#mu_{1}} (GeV)"),
      labely = cms.untracked.string("Events/5GeV"),
      #rangex = cms.untracked.vdouble(0.,250.)
    ),
    cms.PSet(
      name = cms.string('boostselectionmu1eta'),
      ##rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#eta^{#mu_{1}}"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('boostselectionmu1etapm'),
      #rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#eta^{#mu_{1}}"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('boostselectionmu2pt'),
      #rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("p_{T}^{#mu_{2}} (GeV)"),
      labely = cms.untracked.string("Events/5GeV"),
      #rangex = cms.untracked.vdouble(0.,150.)
    ),
    cms.PSet(
      name = cms.string('boostselectionmu2eta'),
      ##rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#eta^{#mu_{2}}"),
      labely = cms.untracked.string("Events")
    ),
    cms.PSet(
      name = cms.string('boostselectionmu2etapm'),
      #rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#eta^{#mu_{2}}"),
      labely = cms.untracked.string("Events")
    ),

    cms.PSet(
      name = cms.string('matrixElementsel1pt'),
      rebin = cms.untracked.uint32(10),
      #logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{e_{1}} (GeV)"),
      labely = cms.untracked.string("Events/10GeV"),
      #rangex = cms.untracked.vdouble(0.,250.)
    ),
    cms.PSet(
      name = cms.string('matrixElementsel1etapm'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#eta^{e_{1}}"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('matrixElementsel2pt'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{e_{2}} (GeV)"),
      labely = cms.untracked.string("Events/10GeV"),
      #rangex = cms.untracked.vdouble(0.,150.)
    ),
     cms.PSet(
      name = cms.string('matrixElementsel2etapm'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#eta^{e_{2}}"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('matrixElementsmu1pt'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{#mu_{1}} (GeV)"),
      labely = cms.untracked.string("Events/10GeV"),
      #rangex = cms.untracked.vdouble(0.,250.)
    ),
    cms.PSet(
      name = cms.string('matrixElementsmu1etapm'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#eta^{#mu_{1}}"),
      labely = cms.untracked.string("Events/0.5")
    ),
    cms.PSet(
      name = cms.string('matrixElementsmu2pt'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{#mu_{2}} (GeV)"),
      labely = cms.untracked.string("Events/10GeV"),
      #rangex = cms.untracked.vdouble(0.,150.)
    ),
    cms.PSet(
      name = cms.string('matrixElementsmu2etapm'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#eta^{#mu_{2}}"),
      labely = cms.untracked.string("Events/0.5")
    ),

    cms.PSet(
      name = cms.string('boostselectionZbM'),
      rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{llb} (GeV)"),
      labely = cms.untracked.string("Events/50GeV")
    ),
    cms.PSet(
      name = cms.string('boostselectionZbPt'),
      rebin = cms.untracked.uint32(40),
      labelx = cms.untracked.string("p_{T}^{llb} (GeV)"),
      labely = cms.untracked.string("Events/40GeV")
    ),
    cms.PSet(
      name = cms.string('dphidijetMET'),
      #rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#Delta#phi(b#bar{b},MET)"),
      labely = cms.untracked.string("Events/0.2")
    ),
    cms.PSet(
      name = cms.string('jetmetbjet1CSVdisc'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("CSV leading b-tagged jet"),
      labely = cms.untracked.string("Events/0.0321")
    ),
    cms.PSet(
      name = cms.string('jetmetbjet2CSVdisc'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("CSV sub-leading b-tagged jet"),
      labely = cms.untracked.string("Events/0.0321")
    ),
    cms.PSet(
      name = cms.string('CSVprod'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("CSV product"),
      labely = cms.untracked.string("Events/0.05")
    ),

    cms.PSet(
      name = cms.string('jetmetMET'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("MEt (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('jetmetMETphi'),
      rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("#phi_{MEt}"),
      labely = cms.untracked.string("Events/0.365")
    ),
    cms.PSet(
      name = cms.string('jetmetMETsignificance'),
      overflow = cms.untracked.bool(True),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("METsignificance"),
      labely = cms.untracked.string("Events/1.0")
    ),
  )
)
