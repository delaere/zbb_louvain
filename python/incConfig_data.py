
from basicConfig import *

#update dilepton selection
changeDiLeptCand(conf = configuration, names = {"leptonsPair" : "bestDiLeptCandidate"})

class configuration(configuration):

  #config file used
  eventSelection = configuration.pythonpath+"IncEventSelection"
  
  # mode: plots or dataset
  runningMode = "plots"
  
  #produce EMU or LL CP:
  run_on_emu = False
  
  # my variables: files, systematics and other options
  btagging = "CSV"
  WP = ["M","L"] # to be ordered from tighter to looser ones: ["M","L"], ["T","L"], ["T","M"]
  #Add zbb selection plots
  controlPlots = configuration.controlPlots
  controlPlots.extend([
    controlPlot("selection", "IncEventSelectionControlPlots", "IncEventSelectionControlPlots", { })
    ])
