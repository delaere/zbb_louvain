from basicConfig import *

#update dilepton selection
changeDiLeptCand(conf = configuration, names = {"leptonsPair" : "ptSortedLeptons_DRll"})
changeBTAG(conf = configuration,btagging="JP")
changeJetPt(conf = configuration, ptjet=20)

class configuration(configuration):

  #config file used
  eventSelection = configuration.pythonpath+"IncEventSelection"

  # mode: plots or dataset
  runningMode = "plots"

  #produce EMU or LL CP:

  #information about the MET cut
  #NB : the choice to cut on MET or on MET significance is done in eventSelection
  MetCut = 50   # Define the value of the met threshold
  MetSigCut = 10   # Define the value of the met significance threshold
  MetRegion = "Low"  #Can be Low or High (the cut applied in the eventSelection will then be MetSig<MetSigCut if you chose the Low MetRegion)
  MetType = "PF" # Define the type of MET you want to use. Can be PF, MVA or NoPU

  # my variables: files, systematics and other options
  btagging = "JP"
  WP = ["M","L"] # to be ordered from tighter to looser ones: ["M","L"], ["T","L"], ["T","M"]    NB : only the first one will be read for the IncJets
  #Add inclusive selection plots
  controlPlots = configuration.controlPlots
  controlPlots.extend([
    controlPlot("IncJets", "IncEventSelectionControlPlots", "IncJetControlPlots", { "btagging":btagging, "WP":WP }),
    controlPlot("IncLeps", "IncEventSelectionControlPlots", "IncLepControlPlots", {}),
    controlPlot("FwdJets", "IncEventSelectionControlPlots", "IncForwardJetControlPlots", {}),
    controlPlot("selection", "IncEventSelectionControlPlots", "IncEventSelectionControlPlots", { })
    
    ])
  eventProducers = configuration.eventProducers
  eventProducers.extend([
    eventProducer("jetInfo", "ObjectSelection", "jetMult", { "btagging":btagging,"WP":WP } ),
    eventProducer("goodJets_fwd", "ObjectSelection", "goodJets_fwd", { "muChannel":True,"eleChannel":True,"pt":20 } ),
    
    ])
    

