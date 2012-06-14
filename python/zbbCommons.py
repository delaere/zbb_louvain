 
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

