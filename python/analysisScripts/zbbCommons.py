# this class is named zbbCommons for backward compatibility.
# scripts should be based on AnalysisEvent and its configuration mechanism
# and should therefore not need the labels directly.
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
