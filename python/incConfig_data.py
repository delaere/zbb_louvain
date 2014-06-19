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
  
  #information about the MET (cut)
  MetThreshold = "Upper"  #Can be Upper or Lower (applies an upper/lower threshold on MET or MET_significance in the eventSelection)
  MetCut = 50   # Define the value of the met threshold
  MetSigCut = 10   # Define the value of the met significance threshold
  MetType = "PF" # Define the type of MET you want to use. Can be PF, MVA or NoPU

  # my variables: files, systematics and other options
  btagging = "CSV"
  WP = ["M","L"] # to be ordered from tighter to looser ones: ["M","L"], ["T","L"], ["T","M"]
  #Add inclusive selection plots
  controlPlots = configuration.controlPlots
  controlPlots.extend([
    controlPlot("selection", "IncEventSelectionControlPlots", "IncEventSelectionControlPlots", { })
    ])
