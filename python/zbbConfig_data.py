## Configuration file used by the H to Z(ll)A(bb) analysis ##

from basicConfig import *

### You can change here the main jet collection but is not really relevant here as now we run on ak5, CA8 and subjets jets. ###
changeJetCollection(conf = configuration, jetcoll = "rawjets")
#changeJetCollection(conf = configuration, jetcoll = "subjets")
#changeJetCollection(conf = configuration, jetcoll = "rawsubjets")

### Here you update the basis configuration with what is specific to this analysis###
class configuration(configuration):
  ### Choose the python file where the selection stages are defined.###
  ### BoostEventSelection=allow to run on several jets collection ; ZbbEventSelection is older and based on Z+bb analysis ###
  eventSelection = configuration.pythonpath+"BoostEventSelection"
  #eventSelection = configuration.pythonpath+"ZbbEventSelection"

  ### Put this to True to avoid confusion name beetween CP and RDS naming conventions. ###
  RDSasCP = True 

  ### Choice of b-tagging algorithm and WPs, if you want to change them you have to use the function 'changeBTAG' defined in basicConfig.py ###
  btagging = "CSV"
  WP = ["M","L"] # to be ordered from tighter to looser ones: ["M","L"], ["T","L"], ["T","M"]

  ### Add control plots for fat and subjets and for the selction. ###
  controlPlots = configuration.controlPlots
  controlPlots.extend([
    controlPlot("subjetmet", "ObjectsControlPlots", "JetmetControlPlots", { "btagging":btagging, "WP":WP, "prejets":"sub" }), 
    controlPlot("fatjetmet", "ObjectsControlPlots", "JetmetControlPlots", { "btagging":btagging, "WP":WP, "prejets":"fat" }), 
    controlPlot("boostselection", "BoostEventSelectionControlPlots", "BoostEventSelectionControlPlots", { })
    ])

  ### Add the functions to select the fat and subjets + the jet information used in the stages selection ###
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

  ### Add the defintions which need an update in case we changed the btagging or the WPs ### 
  toupdateForBtag = configuration.toupdateForBtag
  toupdateForBtag["controlPlots"].extend(["subjetmet","fatjetmet"])
  
### Change the jet pt to 30 GeV ###
changeJetPt(conf = configuration, ptjet=30.)
