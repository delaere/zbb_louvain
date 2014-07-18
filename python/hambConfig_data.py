from basicConfig import *

#update dilepton selection
changeDiLeptCand(conf = configuration, names = {"leptonsPair" : "bestHambDiMuCandidate"})
changeDiLeptCand(conf = configuration, names = {"muonsPair" : "bestHambDiMuCandidate"})
#changeJetPt(conf = configuration, ptjet=20.)
class configuration(configuration):

  #config file used
  eventSelection = configuration.pythonpath+"HambEventSelection"
  
  # mode: plots or dataset
  runningMode = "plots"
    
  #information about the MET cut
  #NB : the choice to cut on MET or on MET significance is done in eventSelection
  MetCut = 50   # Define the value of the met threshold
  MetSigCut = 10   # Define the value of the met significance threshold
  MetType = "PF" # Define the type of MET you want to use. Can be PF, MVA or NoPU
  mHblind = True
  mH = 125
  mHwindow = 20
  # my variables: files, systematics and other options
  btagging = "CSV"
  WP = ["M","L"] # to be ordered from tighter to looser ones: ["M","L"], ["T","L"], ["T","M"]
  #Add inclusive selection plots
  controlPlots = configuration.controlPlots
  controlPlots.extend([
    controlPlot("selection", "HambEventSelectionControlPlots", "HambEventSelectionControlPlots", { })
    ])
