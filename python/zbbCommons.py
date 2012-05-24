 
class zbblabel:
  """labels used in the PAT configuration"""
  allmuonslabel="allMuons"
  muonlabel="matchedMuons"
  allelectronslabel="allElectrons"
  electronlabel="matchedElectrons"
  jetlabel="cleanPatJets"

  #zmumulabel="zmuMatchedmuMatched"
  zmumulabel="zmuAllmuAll"
  #zelelabel="zelMatchedelMatched"
  zelelabel="zelAllelAll"
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
  ssvperfData="reweighting_files/performance_ssv_witheff.root"
  pileupData="reweighting_files/Pileup_2011_to_173692_CD111018_data.root"
  pileupMC="reweighting_files/Summer11_PU_S4_spikesmear.root"
  jecUncertainty="reweighting_files/Jec11_V2_Uncertainty_AK5PF.txt"

  controlPlots="controlPlots.root"
  rooDataset="File_rds_zbb.root"

