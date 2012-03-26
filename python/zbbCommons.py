
class zbblabel:
  """labels used in the PAT configuration"""
  allmuonslabel="allMuons"
  loosemuonslabel="looseMuons"
  muonlabel="matchedMuons"
  allelectronslabel="allElectrons"
  looseelectronslabel="allElectrons"
  electronlabel="matchedElectrons"
  jetlabel="cleanPatJets"
  zmumulabel="ZmuMatchedmuMatched"
  zelelabel="ZelMatchedelMatched"
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
  pileupData="../data/Pileup_2011_to_173692_CD111018.root"
  pileupMC="../data/Summer11_PU_S4_spikesmear.root"
  jecUncertainty="../data/Jec10V1_Uncertainty_KT4PF.txt"
  controlPlots="controlPlots.root"
  rooDataset="File_rds_zbb.root"

