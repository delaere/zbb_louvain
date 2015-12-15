from basicConfig import *

#update dilepton selection
changeDiLeptCand(conf = configuration, names = {"leptonsPair" : "bestHambDiMuCandidate"})
changeDiLeptCand(conf = configuration, names = {"muonsPair" : "bestHambDiMuCandidate"})
changeJetPt(conf = configuration, ptjet=15.)
changeHambMuPt(conf = configuration, leadPt=17., secPt = 8.) #asymmetric muon pt cut
changeBTAG(conf = configuration, btagging="CSV", WP=["T","L"])
#changeHambMuEta(conf = configuration, muEta = 2.1) #asymmetric muon pt cut
class configuration(configuration):

  #config file used
  eventSelection = configuration.pythonpath+"HambEventSelection"
  
  # mode: plots or dataset
  #runningMode = "plots"
  runningMode = "dataset"
    
  #information about the MET cut
  #NB : the choice to cut on MET or on MET significance is done in eventSelection
  MetCut = 50   # Define the value of the met threshold
  MetSigCut = 6.   # Define the value of the met significance threshold
  MetType = "PF" # Define the type of MET you want to use. Can be PF, MVA or NoPU

  #blinding options:
  #0: no blinding
  #1: data blind
  #2: data & MC blind
  #3: data & MC in Higgs window 
  
  blindingOpt = 0
  if runningMode == "plots":
     blindingOpt = 1 
  isRealData = False
  lowmassMu = 20 #default 20
  highmassMu = 70 #default 70
  
  mH = 125
  mHwindow = 20
  # my variables: files, systematics and other options
  btagging = "CSV"
  WP = ["T","L"] # to be ordered from tighter to looser ones: ["M","L"], ["T","L"], ["T","M"]
  mHOpt = [18., 20., 20., 15., 16., 18., 18., 20.]
  mu1ptOpt = [24., 24., 24., 35., 30., 30., 23., 17.]
  mu2ptOpt = [8., 8., 15., 10., 16., 17., 10., 10.]
  jet1ptOpt = [20., 18., 15., 27., 25., 20., 23., 25.]
  jet2ptOpt = [15., 15., 15., 15., 19., 15., 20., 20.]
  #Add inclusive selection plots
  controlPlots = configuration.controlPlots
  controlPlots.extend([
    controlPlot("selection", "HambEventSelectionControlPlots", "HambEventSelectionControlPlots", { })
    ])
  eventProducers = configuration.eventProducers
  eventProducers.extend([
    eventProducer("jetInfo", "ObjectSelection", "jetMult", { "btagging":btagging,"WP":WP } ),
    ])
  toupdateForBtag = configuration.toupdateForBtag
  toupdateForBtag = {
    "eventProducers" : ["jetInfo"]
    }

  configuration.toprint.extend(["leadMuPt", "secMuPt","blindingOpt"])
