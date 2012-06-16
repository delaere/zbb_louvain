 
class zbblabel:
  """labels used in the PAT configuration"""
  allmuonslabel="allMuons"
  muonlabel="matchedMuons"
  allelectronslabel="allElectrons"
  electronlabel="matchedElectrons"
  jetlabel="cleanPatJets"

  zmumulabel="zmuMatchedmuMatched"
  #zmumulabel="zmuAllmuAll"
  zelelabel="zelMatchedelMatched"
  #zelelabel="zelAllelAll"
  vertexlabel="goodPV"
  pulabel="addPileupInfo"
  triggerlabel="patTriggerEvent"
  metlabel="patMETsPF"
  zmmbblabel="Zmmbb"
  zeebblabel="Zeebb"
  bblabel ="bbbar"
  genlabel="genParticles"
  SF_uncert="mean" ## choose among min/max/mean
  SF_running_mode= "hardcoded" ## choose between hardcoded/database

class zbbfile:
  """files containing calibrations and other data"""
  ssvperfData="../data/performance_ssv_witheff.root"
  pileupData="../data/Cert_160404-180252_7TeV_ALL_Collisions11_JSON.pileupTruth.root"
  pileupMC="../data/Fall11_PU_MC.root"
  jecUncertainty="../data/Jec11_V2_Uncertainty_AK5PF.txt"

  controlPlots="controlPlots.root"
  rooDataset="File_rds_zbb.root"


class zbbnorm:
  """information to be used for the MC sample normalization"""
  lumi_tot2011=5.051 #in fb-1
  
  #x_section 7 TeV in pb
  #https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSections
  xsec_DYjets_7TeV=3048.  #Ml+l->50, NNLO for Z->ll
  xsec_TTjets_7TeV=157.5  #NLO inclusive
  xsec_ZZ_7TeV=6.206      #cms measurement EWK-11-010 (2011)
  xsec_ZH_125_7TeV=0.0123 #ZHxsec"0.3158"*BR(H->bb)"0.577"*BR(Z->ll)"0.06729" , here l=e or mu : https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CrossSections#Higgs_cross_sections_at_7_8_and
  xsec_tW_7TeV=5.3        #NLO inclusive
  xsec_tbarW_7TeV=5.3     #NLO inclusive
  
  #x_section 8 TeV in pb, yet under construction, to be checked later
  #https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat8TeV
  xsec_DYjets_8TeV=3503.71. #Ml+l->50, NNLO for Z->ll
  xsec_TTjets_8TeV=225.197  #NLO inclusive
  xsec_ZZ_8TeV= 8.25561     #NLO inclusive Ml+l->12
  xsec_ZH_125_8TeV=0.0153   #ZHxsec"0.3943 "*BR(H->bb)"0.577"*BR(Z->ll)"0.06729" , here l=e or mu
  xsec_tW_8TeV=11.1         #approx. NNLO inclusive
  xsec_tbarW_8TeV=11.1      #approx. NNLO inclusive

  #number of events processed for the PATtuple production
  nev_DY_fall11=35907791.       #1st prod. to be updated when new DY will be available
  nev_TT_fall1=37710785         #to be updated with matching
  nev_ZZ_fall11=4191045.        #if needed to be updated with matching
  nev_ZH_125_fall11=1100000.    #if needed to be updated with matching
  nev_TTpowheg_fall11=16352171. #if needed to be updated with matching
  nev_tW_fall11=814390.         #if needed to be updated with matching
  nev_tbarW_fall11=809984.      #if needed to be updated with matching
  
