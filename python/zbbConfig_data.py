from zbbCommons import *

#configuration of the ControlPlot machinery
from collections import namedtuple
controlPlot     = namedtuple("controlPlot",    ["label","module","classname","kwargs"])
eventCollection = namedtuple("eventCollection",["label","handle","collection"])
eventProducer   = namedtuple("eventProducer",  ["label","module","function","kwargs"])
eventWeight     = namedtuple("eventWeight",    ["label","module","classname","kwargs"])

class configuration:
  # default I/O
  defaultFilename = "controlPlots"
  RDSname = "rds_zbb"
  WSname = "workspace_ras"

  # mode: plots or dataset
  runningMode = "plots"
  #runningMode = "dataset"

  # event selection class
  eventSelection = "ZbbEventSelection"

  # my variables
  btagging = "CSV" 
  muChannel = True
  eleChannel = True

  # control plot classes
  controlPlots = [ 
                   controlPlot("allmuons", "ObjectsControlPlots", "MuonsControlPlots", { "muonList":"allmuons", "muonType":"none" }),
                   controlPlot("tightmuons", "ObjectsControlPlots", "MuonsControlPlots", { "muonType":"tight" }),
                   controlPlot("allelectrons", "ObjectsControlPlots", "ElectronsControlPlots", { "electronList":"allelectrons", "electronType":"none" }),
                   controlPlot("tightelectrons", "ObjectsControlPlots", "ElectronsControlPlots", { "electronType":"tight" }),
                   controlPlot("jetmetAK5PF", "ObjectsControlPlots", "JetmetControlPlots", { "btagging":btagging }),
                   controlPlot("vertexAssociation", "VertexAssociationControlPlots", "VertexAssociationControlPlots", { }),
                   controlPlot("selection", "ZbbEventSelectionControlPlots", "ZbbEventSelectionControlPlots", { }),
#                   controlPlot("MCselection", "MonteCarloSelectionControlPlots", "MonteCarloSelectionControlPlots", { }),
                   controlPlot("matrixElements", "MatrixElementControlPlots", "MatrixElementControlPlots", { }),
#                   controlPlot("leptonsReweighting", "LeptonsReweightingControlPlots", "LeptonsReweightingControlPlots", { }),
#                   controlPlot("mcReweighting", "MonteCarloReweightingControlPlots", "MonteCarloReweightingControlPlots", { }),
#                   controlPlot("lumiReweighting", "LumiReWeightingControlPlots", "LumiReWeightingControlPlots", { }),
#                   controlPlot("btaggingReweighting", "BtaggingReWeightingControlPlots", "BtaggingReWeightingControlPlots", { })
                 ]

  # event content: lists of eventCollection, eventProducer, and eventWeight objects respectively.
  eventCollections = [ eventCollection("genParticles","vector<reco::GenParticle>",zbblabel.genlabel),
                       eventCollection("genJets","vector<reco::GenJet>",zbblabel.genjetlabel),
                       eventCollection("genInfo","GenEventInfoProduct",zbblabel.genInfolabel),
                       eventCollection("vertices","vector<reco::Vertex>",zbblabel.vertexlabel),
                       eventCollection("jets","vector<pat::Jet>",zbblabel.jetlabel),
                       eventCollection("MET","vector<pat::MET>",zbblabel.metlabel),
                       eventCollection("METNNregression","vector<pat::MET>","patMETsPF"),
                       eventCollection("Zmumu","vector<reco::CompositeCandidate>",zbblabel.zmumulabel),
                       eventCollection("Zelel","vector<reco::CompositeCandidate>",zbblabel.zelelabel),
                       eventCollection("triggerInfo","pat::TriggerEvent",zbblabel.triggerlabel),
                       eventCollection("electrons","vector<pat::Electron>",zbblabel.electronlabel),
                       eventCollection("muons","vector<pat::Muon>",zbblabel.muonlabel),
                       eventCollection("allelectrons","vector<pat::Electron>",zbblabel.allelectronslabel),
                       eventCollection("allmuons","vector<pat::Muon>",zbblabel.allmuonslabel),
                       eventCollection("PileupSummaryInfo","std::vector< PileupSummaryInfo >",zbblabel.pulabel),
                       eventCollection("rho","double",(zbblabel.rholabel,"rho"))
                     ] 

  eventProducers   = [ eventProducer("vertex", "ObjectSelection", "vertex", {}),
                       eventProducer("goodJets_mu", "ObjectSelection", "goodJets", { "muChannel":True,"eleChannel":False } ),
                       eventProducer("goodJets_ele", "ObjectSelection", "goodJets", { "muChannel":False,"eleChannel":True } ),
                       eventProducer("goodJets_all", "ObjectSelection", "goodJets", { "muChannel":True,"eleChannel":True } ),
                       eventProducer("goodJets_none", "ObjectSelection", "goodJets", { "muChannel":False,"eleChannel":False } ),
                       eventProducer("isMuTriggerOK", "ObjectSelection", "isTriggerOK", { "muChannel":True,"eleChannel":False,"perRun":True } ),
                       eventProducer("isEleTriggerOK", "ObjectSelection", "isTriggerOK", { "muChannel":False,"eleChannel":True,"perRun":True } ),
                       eventProducer("isTriggerOK", "ObjectSelection", "isTriggerOK", { "muChannel":True,"eleChannel":True,"perRun":True } ),
                       eventProducer("category", "EventSelection", "eventCategory", { "btagging":btagging, "ZjetFilter":"bcl" } ),
                       eventProducer("bestZmumuCandidate", "ObjectSelection", "findBestCandidate", { "muChannel":True,"eleChannel":False } ),
                       eventProducer("bestZelelCandidate", "ObjectSelection", "findBestCandidate", { "muChannel":False,"eleChannel":True } ),
                       eventProducer("bestZcandidate", "ObjectSelection", "findBestCandidate", { "muChannel":True,"eleChannel":True } ),
                       eventProducer("dijet_muChannel", "ObjectSelection", "findDijetPair", { "btagging":btagging,"muChannel":True,"eleChannel":False } ),
                       eventProducer("dijet_eleChannel", "ObjectSelection", "findDijetPair", { "btagging":btagging,"muChannel":False,"eleChannel":True } ),
                       eventProducer("dijet_all", "ObjectSelection", "findDijetPair", { "btagging":btagging,"muChannel":True,"eleChannel":True } ),
                       eventProducer("sortedGenJets", "MonteCarloSelection", "genjetCollectionsProducer", { "ptcut":0, "etacut":10 } )
                     ]

#  eventWeights     = [ eventWeight("Btagging","BtaggingWeight","BtaggingWeight",{"jmin1":0,"jmax1":999,"jmin2":0,"jmax2":999,"file":zbbfile.ssvperfData,"btagging":btagging}),
#                       eventWeight("Leptons","LeptonsReweighting","LeptonsReWeighting", {}),
#                       eventWeight("MonteCarlo","MonteCarloReweighting","MonteCarloReWeighting", {"shift":0, "MCmode":"none"}),
#                       eventWeight("PileUp","LumiReWeighting","LumiReWeighting", {"MonteCarloFileName":zbbfile.pileupMC, "DataFileName":zbbfile.pileupData, "systematicShift":0})
#                     ]
  eventWeights     = []

class eventDumpConfig:
  # fine-tuning of the event content for display
  productsToPrint   = [ ] # list of product to display (use the producer label)
  collectionsToHide = [ ] # collections used in the analysis but not printed (use the collection label) 

