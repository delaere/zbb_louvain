
from basicConfig import *

changeJetCollection(conf = configuration, jetcoll = "rawjets")
#changeJetCollection(conf = configuration, jetcoll = "subjets")
#changeJetCollection(conf = configuration, jetcoll = "rawsubjets")

changeJetPt(conf = configuration, ptjet=30.)
#changeJetPt(conf = configuration, ptjet=20.)

class configuration(configuration):
  # mode: plots or dataset
  runningMode = "plots"
  # my variables: files, systematics and other options
  btagging = "CSV"
  WP = ["M","L"] # to be ordered from tighter to looser ones: ["M","L"], ["T","L"], ["T","M"]
  #Add zbb selection plots
  controlPlots = configuration.controlPlots
  controlPlots.extend([
    controlPlot("selection", "ZbbEventSelectionControlPlots", "ZbbEventSelectionControlPlots", { })
    ])
