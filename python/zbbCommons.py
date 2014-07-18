import os

useJP=True

if useJP :
  tagger="jp"
else:
  tagger="csv"

rmPixelMisAligRuns = False

class zbblabel:
  """labels used in the PAT configuration"""
  allmuonslabel="allMuons"
  muonlabel="tightMuons"
  allelectronslabel="allElectrons"
  electronlabel="tightElectrons"
  #jetlabel="smearedPatJetsResDown"
  jetlabel="cleanPatJets"
  zmumulabel="zmuTightmuTight"
  zelelabel="zelTightelTight"
  vertexlabel="goodPV"
  pulabel="addPileupInfo"
  triggerlabel="patTriggerEvent"
  metlabel="patType01SCorrectedPFMet"
  rholabel="kt6PFJets"
  genlabel="genParticles" #genlabel="prunedGen"
  genjetlabel="ak5GenJets"
  genInfolabel="generator"

class zbbsystematics:
  # btagging reweighting
  SF_uncert="mean" ## choose among min/max/mean/min_bc/max_bc/min_l/max_l 
  #SF_running_mode= "hardcoded_nofit" ## choose between hardcoded/database
  SF_running_mode= "database" ## choose between "hardcoded" and "database"
  # Jet Energy corrections for MC. For data, these factors must be (forced to) zero!
  JERfactor = 0. # 1 = recommended smearing for MC, use 0 for MadWeight
  JESfactor = 0. # 1 = +1sigma
  # Lepton reweighting uncertainty
  LeptonTnPfactor = 0

class zbbfile:
  """files containing calibrations and other data"""
  ssvperfData=str(os.environ["CMSSW_BASE"])+"/src/UserCode/zbb_louvain/data/performance_"+tagger+"_witheff.root" ## in order to use the csv efficiencies and SFs
  pileupData=str(os.environ["CMSSW_BASE"])+"/src/UserCode/zbb_louvain/data/Cert_190456-208686_8TeV_PromptPlusReReco_pileupTruth.root"
  pileupMC=str(os.environ["CMSSW_BASE"])+"/src/UserCode/zbb_louvain/data/MCpileup_Summer12_S10.root"
  jecUncertainty=str(os.environ["CMSSW_BASE"])+"/src/UserCode/zbb_louvain/data/Fall12_V7_DATA_UncertaintySources_AK5PF.txt"
  controlPlots="controlPlots.root"
  rooDataset="File_rds_zbb.root"

class zbbnorm:
  """information to be used for the MC sample normalization"""
  lumi_totEle2011 = 4.99 #in fb-1
  lumi_totMu2011  = 5.05

  lumi_tot2012 = 19.45 #A+B+C+D
  if rmPixelMisAligRuns : lumi_tot2012-=0.58
  #lumi_tot2012= 19.45-7.27 #ABC
  
  #x_section 7 TeV in pb
  #https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSections
  xsec_DYjets_7TeV= 3048.     #Ml+l->50, NNLO for Z->ll
  xsec_TTjets_7TeV=  157.5    #NLO inclusive
  xsec_TTlept_7TeV=   16.7    #ttbar->llvvbb_
  xsec_ZZ_7TeV    =    6.206  #cms measurement EWK-11-010 (2011)
  xsec_ZH110_7TeV =    0.0385 #ZHxsec"0.4978", BR(H->bb)"0.744"
  xsec_ZH115_7TeV =    0.0318 #ZHxsec"0.4345", BR(H->bb)"0.703"
  xsec_ZH120_7TeV =    0.0257 #ZHxsec"0.3808", BR(H->bb)"0.648" 
  xsec_ZH125_7TeV =    0.0201 #ZHxsec"0.3351"*BR(H->bb)"0.577"*BR(Z->ll)"0.10399" , here l=e, mu or tau : https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CrossSections#Higgs_cross_sections_at_7_8_and
  xsec_ZH130_7TeV =    0.0152 #ZHxsec"0.2957", BR(H->bb)"0.494" 
  xsec_ZH135_7TeV =    0.0110 #ZHxsec"0.2616", BR(H->bb)"0.404" 
  xsec_tW_7TeV    =    5.3    #NLO inclusive
  xsec_tbarW_7TeV =    5.3    #NLO inclusive
  
  #x_section 8 TeV in pb, yet under construction, to be checked later
  #https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat8TeV
  xsec_DYjets_8TeV=3503.71  #Ml+l->50, NNLO for Z->ll
  xsec_DYjets_M10to50_8TeV= 13229.7# based on AN 2013/302
  #xsec_TTjets_8TeV=225.197  #NLO inclusive
  xsec_TTjets_8TeV=245.8    #NNLO inclusive 
  xsec_TTFullLept_8TeV = xsec_TTjets_8TeV*(1/3.)*(1/3.) #0.308 is W to lnu with l = e, mu, tau from PDG
  xsec_TTSemiLept_8TeV = xsec_TTjets_8TeV*(1/3.)*(2/3.)*2
  xsec_ZZ_8TeV = 8.258     #NLO inclusive Ml+l->40 NNPDF
  xsec_WW_8TeV = 56. 	   #NLO inclusive Ml+l->40 NNPDF
  xsec_WZ_8TeV = 33.6  	   #NLO inclusive Ml+l->40 NNPDF
  xsec_Zbb_8TeV = 76.75     #LO form MCFM : Ml+l->50, massive b-quark
  xsec_ZH110_8TeV=0.0474    #xsec=0.6125
  xsec_ZH115_8TeV=0.0392    #xsec=0.5358
  xsec_ZH120_8TeV=0.0317    #xsec=0.4710
  xsec_ZH125_8TeV=0.0249    #ZHxsec"0.4153 "*BR(H->bb)"0.577"*BR(Z->ll)"0.10399" , here l=e, mu or tau
  xsec_ZH130_8TeV=0.0189    #xsec=0.3671
  xsec_ZH135_8TeV=0.0137    #xsec=0.3259
  xsec_ZH140_8TeV=0.0095    #xsec=0.2898 BR=0.315
  xsec_ZH145_8TeV=0.0062    #xsec=0.2583 BR=0.232
  xsec_ZH150_8TeV=0.0038    #xsec=0.2308 BR=0.157
#  xsec_t_8TeV=11.1         #approx. NNLO inclusive
#  xsec_tbar_8TeV=11.1         #approx. NNLO inclusive
  xsec_tW_8TeV=11.1         #approx. NNLO inclusive
  xsec_tbarW_8TeV=11.1      #approx. NNLO inclusive
#  xsec_s_8TeV=11.1      #approx. NNLO inclusive
#  xsec_sbar_8TeV=11.1      #approx. NNLO inclusive

  # fall 11 number of events processed for the PATtuple production
  nev_DYjets_fall11   = 36264432 # updated
  nev_TTjets_fall11   = 59244088 # updated
  nev_ZZ_fall11       =  4191045 # updated
  nev_ZH115_fall11    =  1090000 # updated
  nev_ZH120_fall11    =  1090000 # updated
  nev_ZH125_fall11    =  1100000 # updated
  nev_ZH130_fall11    =  1100000 # updated
  nev_ZH135_fall11    =  1096956 # updated
  nev_TTpowheg_fall11 = 16352171 # if needed to be updated with matching
  nev_tW_fall11       =   814390 # updated
  nev_tbarW_fall11    =   809984 # updated
  
  #summer 12 number of events processed for the PATtuple production
  nev_DYjets_M10to50_summer12= 37835275 # according to https://cmsweb.cern.ch/das/request?input=dataset%3D%2FDYJetsToLL_M-10To50_TuneZ2Star_8TeV-madgraph%2FSummer12_DR53X-PU_S10_START53_V7A-v1%2FAODSIM&instance=prod%2Fglobal
  nev_DYjets_summer12     = 30459503 # OK, inclusive sample
  nev_TTjets_summer12     =  6923750 # MassiveBinDecay S10, OK
  nev_TTFullLept_summer12 = 12119013 # Full leptonic decay, OK
  nev_TTSemiLept_summer12 = 10997349 # Semi leptonic decay, OK
  nev_ZZ_summer12         = 9799908 # OK
  nev_WW_summer12         = 10000431  # OK
  nev_WZ_summer12         = 10000283  # OK
  nev_Zbb_summer12        = 14129304 # OK 
  nev_ZH110_summer12      =   998514 # OK
  nev_ZH115_summer12      =   999699 # OK
  nev_ZH120_summer12      =  1000215 # OK
  nev_ZH125_summer12      =   999462 # OK
  nev_ZH130_summer12      =  1000000 # OK
  nev_ZH135_summer12      =  1000000 # OK
  nev_t_summer12	  =  497658  # OK                
#  nev_tbar_summer12	  =  497658  # OK                
  nev_tbarW_summer12	  =  493460  # OK                
  nev_tW_summer12	  =  497658  # OK                
#  nev_s_summer12	  =  497658  # OK                
#  nev_sbar_summer12	  =  497658  # OK                
class zbbme:
  doMEcontrolPlots = False # if false nobody else of this class matters
  doNNJetRegression = False
