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
        outputFile = cms.string('mergedPlots_ZlZcZb_Zbb_V2_all_and_Xs.root'),
        #outputFile = cms.string('mergedPlots_ZlZcZb_Zbb_V2_all_FinalLumi_and_Xs_SSVHEbining.root'),
        #outputFile = cms.string('mergedPlots_ZlZcZb_Zbb_V2_all_FinalLumi_and_Xs.root'),
        #outputFile = cms.string('mergedPlots_ZlZcZb_Zbb_V2_BFIX_all_Rebin.root'),
        #outputFile = cms.string('mergedPlots_ZlZcZb_Zbb_V2_BFIX_all.root'),
        #outputFile = cms.string('mergedPlots_ZlZcZb_Zbb_V2_level_memoryleak.root'),
        #outputFile = cms.string('mergedPlots_ZlZcZb_Zbb_REBIN1.root'),
        #outputFile = cms.string('mergedPlots_ZlZcZb_24112011_ApprovalPlots_V2012_AGAIN.root'),
        #outputFile = cms.string('mergedPlots_ZlZcZb_24112011_+_MCatNLO_AllWeightSignOnly.root'),
        #outputFile = cms.string('mergedPlots_ZlZcZb_24112011_+_MCatNLO_RAW.root'),

  data = cms.VPSet (
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2/May10ReReco/MU/Mu_ReRecoMay10_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/May10ReReco/MU/Mu_ReRecoMay10_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/May10ReReco/MU/Mu_ReRecoMay10_ControlPlots_all.root')
   ), 
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2/PromptRecoV4/MU/Mu_PromptV4_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/PromptRecoV4/MU/Mu_PromptV4_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/PromptRecoV4/MU/Mu_PromptV4_ControlPlots_all.root')
   ), 
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2/Aug05ReReco/MU/Mu_Aug05ReReco_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/Aug05ReReco/MU/Mu_Aug05ReReco_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/Aug05ReReco/MU/Mu_Aug05ReReco_ControlPlots_all.root')
   ),
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2/PromptRecoV6/MU/Mu_PromptV6_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/PromptRecoV6/MU/Mu_PromptV6_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/PromptRecoV6/MU/Mu_PromptV6_ControlPlots_all.root')
   ),

   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2/May10ReReco/ELE/Ele_ReRecoMay10_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/May10ReReco/ELE/Ele_ReRecoMay10_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/May10ReReco/ELE/Ele_ReRecoMay10_ControlPlots_all.root')
   ), 
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2/PromptRecoV4/ELE/Ele_PromptV4_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/PromptRecoV4/ELE/Ele_PromptV4_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/PromptRecoV4/ELE/Ele_PromptV4_ControlPlots_all.root')
   ), 
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2/Aug05ReReco/ELE/Ele_Aug05ReReco_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/Aug05ReReco/ELE/Ele_Aug05ReReco_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/Aug05ReReco/ELE/Ele_Aug05ReReco_ControlPlots_all.root')
   ),
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2/PromptRecoV6/ELE/Ele_PromptV6_ControlPlots_all.root')
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/PromptRecoV6/ELE/Ele_PromptV6_ControlPlots_all.root')
     #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/PromptRecoV6/ELE/Ele_PromptV6_ControlPlots_all.root')
   )   
  ),

        
  mc   = cms.VPSet (

   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2_FIX/ZZ/ZZ_Summer11_ControlPlots_all.root'),
    color = cms.uint32(EColor.kMagenta+palette),
    ##scale = cms.double(6.206*2200./(4187885.)), #New Xs to use!   
    scale = cms.double(6.206*2130./(4187885.)), #Xs ??????
    ##scale = cms.double(6.258*2130./(4187885.)), #Xs ??????
    role = cms.string('ZZ')
   ),

   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2_FIX/TT/TTJets_Summer11_ControlPlots_all.root'),
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/TTJets/TTJets_ControlPlots_all.root'),
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/TTJets/TTJets_ControlPlots_all.root'),
     #color = cms.uint32(5),
    color = cms.uint32(EColor.kYellow+palette),
    ##scale = cms.double(157.5*2200./(3701947.)), #NLO MCFM proper Xs
    scale = cms.double(157.5*2130./(3701947.)), #NLO MCFM proper Xs
     #scale = cms.double(168.*1090./((21./25.)*3701947.)), #NLO MCFM
     #scale = cms.double(0.0045916), #NLO MCFM
     role = cms.string('t#bar{t}')
   ),

   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2_FIX/Zb/Zb_fromDYJets_Summer11_ControlPlots_all.root'),
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/Zb/Zb_fromDYJets_Summer11_ControlPlots_all.root'),
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/Zb/Zb_fromDYJets_Summer11_ControlPlots_all.root'),
     #color = cms.uint32(2),
     color = cms.uint32(EColor.kRed+palette),
     #scale = cms.double(3048.*2200./36257961.), #NLO MCFM
     scale = cms.double(3048.*2130./36257961.), #NLO MCFM
     #scale = cms.double(3048.*1090./30008836.), #NLO MCFM
     #scale = cms.double(0.0355249), #NLO MCFM
     role = cms.string('Z+b')
   ), 
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2_FIX/Zc/Zc_fromDYJets_Summer11_ControlPlots_all.root'),     
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/Zc/Zc_fromDYJets_Summer11_ControlPlots_all.root'),     
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/Zc/Zc_fromDYJets_Summer11_ControlPlots_all.root'),     
    #color = cms.uint32(3),
     color = cms.uint32(EColor.kGreen+palette),
     #scale = cms.double(3048.*2200./36257961.), #NLO MCFM
     scale = cms.double(3048.*2130./36257961.), #NLO MCFM
    #scale = cms.double(3048.*1090./30008836.), #NLO MCFM
     #scale = cms.double(0.0365163), #NLO MCFM
     role = cms.string('Z+c')
   ), 
   cms.PSet(
    fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_Zbb_V2_FIX/Zl/Zl_fromDYJets_Summer11_ControlPlots_all.root'),
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/Control_Plots_2fb_V2_Approval/Zl/Zl_fromDYJets_Summer11_ControlPlots_all.root'),
    #fileName = cms.string('/home/fynu/lceard/scratch/CMSSW_4_2_7/src/UserCode/zbb_louvain/python/ControlPlots_19112011_2fb/Zl/Zl_fromDYJets_Summer11_ControlPlots_all.root'),
     #color = cms.uint32(4),
     color = cms.uint32(EColor.kBlue+palette),
     scale = cms.double(3048.*2130./36257961.), #NLO MCFM
#     #scale = cms.double(3048.*1090./30008836.), #NNLO
#     #scale = cms.double(0.0207567), #NNLO
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
      labelx = cms.untracked.string("M_{Z} (GeV)"),
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
	  rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("p_{T}^{e_{1}} (GeV)"),
	  labely = cms.untracked.string("Events/5GeV")
    ),
    cms.PSet(
          name = cms.string('el1eta'),
	  #rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("#eta^{e_{1}}"),
	  labely = cms.untracked.string("Events")
    ),
    cms.PSet(
          name = cms.string('el2pt'),
	  rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("p_{T}^{e_{2}} (GeV)"),
	  labely = cms.untracked.string("Events/5GeV")
    ),
     cms.PSet(
          name = cms.string('el2eta'),
	  #rebin = cms.untracked.uint32(5),
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
	  #rebin = cms.untracked.uint32(5),
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
	  #rebin = cms.untracked.uint32(5),
	  logy = cms.untracked.bool(True),
	  labelx = cms.untracked.string("#eta^{#mu_{2}}"),
	  labely = cms.untracked.string("Events")
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
      rebin = cms.untracked.uint32(20),
      labelx = cms.untracked.string("p_{T}^{Z} (GeV)"),          ####### /2 rebining
      labely = cms.untracked.string("Events/20GeV")
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
#    cms.PSet(
#      name = cms.string('SSVHEdisc'),
#      rebin = cms.untracked.uint32(5),
#      labelx = cms.untracked.string("SSVHE discriminant"),
#      labely = cms.untracked.string("Events/0.5")
#    ),
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
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#Delta Pt(Z,bjet_{1})"),
      labely = cms.untracked.string("Events/10 GeV")
    ),
    
    ### Zbb quantities
   cms.PSet(
      name = cms.string('drZbb'),
      rebin = cms.untracked.uint32(5),
      labelx = cms.untracked.string("#Delta R(Z,bb)"),
      labely = cms.untracked.string("Events/5")
    ), 
   cms.PSet(
      name = cms.string('scaldptZbb'),
      rebin = cms.untracked.uint32(10),
      labelx = cms.untracked.string("#Delta Pt(Z,bb)"),
      labely = cms.untracked.string("Events/10 GeV")
    ),

    
  )
)
