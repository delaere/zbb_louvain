import FWCore.ParameterSet.Config as cms
#from ROOT import EColor

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
  outputFile = cms.string('mergedPlots_ZlZcZb_24112011_+_MCatNLO_15.20pb.root'),

  data = cms.VPSet (
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/May10ReReco/MU/Mu_ReRecoMay10_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/May10ReReco/MU/Mu_ReRecoMay10_ControlPlots_all.root')
   ), 
   cms.PSet(
     fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/PromptRecoV4/MU/Mu_PromptV4_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/PromptRecoV4/MU/Mu_PromptV4_ControlPlots_all.root')
   ), 
   cms.PSet(
     fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/Aug05ReReco/MU/Mu_Aug05ReReco_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/Aug05ReReco/MU/Mu_Aug05ReReco_ControlPlots_all.root')
   ),
   cms.PSet(
     fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/PromptRecoV6/MU/Mu_PromptV6_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/PromptRecoV6/MU/Mu_PromptV6_ControlPlots_all.root')
   ),

   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/May10ReReco/ELE/Ele_ReRecoMay10_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/May10ReReco/ELE/Ele_ReRecoMay10_ControlPlots_all.root')
   ), 
   cms.PSet(
     fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/PromptRecoV4/ELE/Ele_PromptV4_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/PromptRecoV4/ELE/Ele_PromptV4_ControlPlots_all.root')
   ), 
   cms.PSet(
     fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/Aug05ReReco/ELE/Ele_Aug05ReReco_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/Aug05ReReco/ELE/Ele_Aug05ReReco_ControlPlots_all.root')
   ),
   cms.PSet(
     fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/PromptRecoV6/ELE/Ele_PromptV6_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/PromptRecoV6/ELE/Ele_PromptV6_ControlPlots_all.root')
   )   
  ),
  mc   = cms.VPSet (
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/TTJets/TTJets_ControlPlots_all.root'),
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/TTJets/TTJets_ControlPlots_all.root'),
     #color = cms.uint32(5),
     color = cms.uint32(EColor.kYellow+palette),
     scale = cms.double(157.5*2130./(3701947.)), #NLO MCFM proper Xs
     #scale = cms.double(168.*1090./((21./25.)*3701947.)), #NLO MCFM
     #scale = cms.double(0.0045916), #NLO MCFM
     role = cms.string('t#bar{t}')
   ),
   cms.PSet(
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb/TTJets/TTJets_ControlPlots_all.root'),
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V3/MC@NLO/MCatNLO_ControlPlots_all.root'),
    #color = cms.uint32(7),
    color = cms.uint32(EColor.kPink),
    scale = cms.double(2130.), #with weight already apllied event per event
    #scale = cms.double(16.10*2130./96772.), #wrong
    #scale = cms.double(16.10*2130./955602.), #wrong
    role = cms.string('aMC@NLO')
   ), 
#   cms.PSet(
#    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/Zb/Zb_fromDYJets_Summer11_ControlPlots_all.root'),
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/Zb/Zb_fromDYJets_Summer11_ControlPlots_all.root'),
     #color = cms.uint32(2),
#     color = cms.uint32(EColor.kRed+palette),
#     scale = cms.double(3048.*2130./36257961.), #NLO MCFM
     #scale = cms.double(3048.*1090./30008836.), #NLO MCFM
     #scale = cms.double(0.0355249), #NLO MCFM
#     role = cms.string('Z+b')
#   ), 
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/Zc/Zc_fromDYJets_Summer11_ControlPlots_all.root'),     
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/Zc/Zc_fromDYJets_Summer11_ControlPlots_all.root'),     
    #color = cms.uint32(3),
     color = cms.uint32(EColor.kGreen+palette),
     scale = cms.double(3048.*2130./36257961.), #NLO MCFM
     #scale = cms.double(3048.*1090./30008836.), #NLO MCFM
     #scale = cms.double(0.0365163), #NLO MCFM
     role = cms.string('Z+c')
   ), 
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/Zl/Zl_fromDYJets_Summer11_ControlPlots_all.root'),
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/Zl/Zl_fromDYJets_Summer11_ControlPlots_all.root'),
     #color = cms.uint32(4),
     color = cms.uint32(EColor.kBlue+palette),
     scale = cms.double(3048.*2130./36257961.), #NLO MCFM
     #scale = cms.double(3048.*1090./30008836.), #NNLO
     #scale = cms.double(0.0207567), #NNLO
     role = cms.string('Z+l')
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
      labelx = cms.untracked.string("M_{l^{+}l^{-}} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(60.,120.)
    ),
    cms.PSet(
      name = cms.string('bestzmassMu'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{#mu^{+}#mu^{-}} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(60.,120.)
    ),
    cms.PSet(
      name = cms.string('bestzmassEle'),
      rebin = cms.untracked.uint32(20),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("M_{e^{+}e^{-}} (GeV)"),
      labely = cms.untracked.string("Events/2GeV"),
      rangex = cms.untracked.vdouble(60.,120.)
    ),
    cms.PSet(
      name = cms.string('bjet1pt'),
      begin = cms.untracked.double(25),
      end = cms.untracked.double(265),
      width = cms.untracked.double(10),
      logx = cms.untracked.bool(False),
      logy = cms.untracked.bool(True),
      labelx = cms.untracked.string("p_{T}^{b-lead} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('bjet2pt'),
      rebin = cms.untracked.uint32(10),
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
          name = cms.string('el1pt'),
	  rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("p_{T}^{e_{1}} (GeV)"),
	  labely = cms.untracked.string("Events/5GeV")
    ),
    cms.PSet(
          name = cms.string('el2pt'),
	  rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("p_{T}^{e_{2}} (GeV)"),
	  labely = cms.untracked.string("Events/5GeV")
    ),
    cms.PSet(
          name = cms.string('mu1pt'),
	  rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("p_{T}^{#mu_{1}} (GeV)"),
	  labely = cms.untracked.string("Events/5GeV")
    ),
    cms.PSet(
          name = cms.string('mu2pt'),
	  rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("p_{T}^{#mu_{2}} (GeV)"),
	  labely = cms.untracked.string("Events/5GeV")
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
      rebin = cms.untracked.uint32(50),
      labelx = cms.untracked.string("M_{bb} (GeV)"),
      labely = cms.untracked.string("Events/50GeV")
    ),
    cms.PSet(
      name = cms.string('dijetPt'),
      rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("p_{T}^{bb} (GeV)"),
      labely = cms.untracked.string("Events/20GeV")
    ),
    cms.PSet(
      name = cms.string('dijetdR'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Delta_R(b^{1}b^{2}) (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('dijetSVdR'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("Delta_R_SV(b^{1}b^{2}) (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
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
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('bestzptMu'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
    ),
    cms.PSet(
      name = cms.string('bestzptEle'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),
      labely = cms.untracked.string("Events/10GeV")
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
      name = cms.string('jet1SSVHEdisc'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("SSVHE discriminant"),
      labely = cms.untracked.string("Events/0.2")
    ),
    cms.PSet(
      name = cms.string('jet1SSVHPdisc'),
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("SSVHP discriminant"),
      labely = cms.untracked.string("Events/0.2")
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
      rebin = cms.untracked.uint32(2),
      labelx = cms.untracked.string("#Delta#phi(Z,b-lead)"),
      labely = cms.untracked.string("Events/0.2")
    ),
    cms.PSet(
      name = cms.string('drZbj1'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#Delta R(Z,bjet_{1})"),
      labely = cms.untracked.string("Events/0.5")
    ),



  )
)
