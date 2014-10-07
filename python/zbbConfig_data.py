
from basicConfig import *

changeJetCollection(conf = configuration, jetcoll = "rawjets")
#changeJetCollection(conf = configuration, jetcoll = "subjets")
#changeJetCollection(conf = configuration, jetcoll = "rawsubjets")

#changeJetPt(conf = configuration, ptjet=20.)

class configuration(configuration):
  eventSelection = configuration.pythonpath+"BoostEventSelection"
  # mode: plots or dataset
  runningMode = "plots"
  #runningMode = "dataset"
  # my variables: files, systematics and other options
  btagging = "CSV"
  WP = ["M","L"] # to be ordered from tighter to looser ones: ["M","L"], ["T","L"], ["T","M"]
  #Add zbb selection plots
  controlPlots = configuration.controlPlots
  controlPlots.extend([
    controlPlot("subjetmet", "ObjectsControlPlots", "JetmetControlPlots", { "btagging":btagging, "WP":WP, "prejets":"sub" }), #SPE
    controlPlot("fatjetmet", "ObjectsControlPlots", "JetmetControlPlots", { "btagging":btagging, "WP":WP, "prejets":"fat" }), #SPE
    controlPlot("boostselection", "BoostEventSelectionControlPlots", "BoostEventSelectionControlPlots", { })
    ])

  #SPE
  eventProducers = configuration.eventProducers
  eventProducers.extend([
    eventProducer("goodsubJets_all", "ObjectSelection", "goodJets", { "muChannel":True,"eleChannel":True,"pt":configuration.ptjet, "jets":"subjets" } ),
    eventProducer("goodfatJets_all", "ObjectSelection", "goodJets", { "muChannel":True,"eleChannel":True,"pt":configuration.ptjet, "jets":"fatjets" } ),
    eventProducer("disubjet_all", "ObjectSelection", "findDijetPair", { "btagging":btagging,"WP":WP,"muChannel":True,"eleChannel":True,"prejets":"sub" } ),
    eventProducer("difatjet_all", "ObjectSelection", "findDijetPair", { "btagging":btagging,"WP":WP,"muChannel":True,"eleChannel":True,"prejets":"fat" } ),

    eventProducer("jetInfo", "ObjectSelection", "jetMult", { "btagging":btagging,"WP":WP } ),
    eventProducer("fatjetInfo", "ObjectSelection", "jetMult", { "btagging":btagging,"WP":WP,"prejets":"fat" } ),
    eventProducer("subjetInfo", "ObjectSelection", "jetMult", { "btagging":btagging,"WP":WP,"prejets":"sub" } ),
    ])
  #end SPE

changeJetPt(conf = configuration, ptjet=30.)
