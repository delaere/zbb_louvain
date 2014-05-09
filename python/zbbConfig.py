import os

#configuration of the ControlPlot machinery
from collections import namedtuple
controlPlot     = namedtuple("controlPlot",    ["label","module","classname","kwargs"])
eventCollection = namedtuple("eventCollection",["label","handle","collection"])
eventProducer   = namedtuple("eventProducer",  ["label","module","function","kwargs"])
eventWeight     = namedtuple("eventWeight",    ["label","module","classname","kwargs"])

class configuration:
  # default I/O
  pythonpath = "UserCode.zbb_louvain."
  defaultFilename = "controlPlots"
  RDSname = "rds_zbb"
  WSname = "workspace_ras"

  # mode: plots or dataset
  runningMode = "plots"
  #runningMode = "dataset"

  # event selection class
  eventSelection = pythonpath+"ZbbEventSelection"

  # my variables: files, systematics and other options
  btagging = "CSV" #CSV or JP 
  WP = ["M","L"] #2 WP, the tightest one first
  muChannel = True
  eleChannel = True
  SF_uncert="mean" #btagging reweighting:  choose among min/max/mean
  if btagging == "CSV":
    SF_running_mode= "hardcoded_nofit" #btagging reweighting: choose between hardcoded_nofit/hardcoded/database
  elif btagging == "JP":
    SF_running_mode= "database" #btagging reweighting: choose between hardcoded_nofit/hardcoded/database
    
  JERfactor = 1. # 1 = recommended smearing for MC, use 0 for MadWeight
  JESfactor = 0. # 1 = +1sigma
  LeptonTnPfactor = 0 # Lepton reweighting uncertainty
  doMEcontrolPlots = True
  doNNJetRegression = False
  dataDirectory = str(os.environ["CMSSW_BASE"])+"/src/UserCode/zbb_louvain/data/"
  if btagging == "CSV":
    ssvperfData=dataDirectory+"btag_allalgos_witheff.root"
  elif btagging == "JP":
    ssvperfData=dataDirectory+"performance_jp_witheff.root"
  pileupData=dataDirectory+"Cert_190456-208686_8TeV_22Jan2013ReReco_pileupTruth.root"
  pileupMC=dataDirectory+"MCpileup_Summer12_S10.root"
  jecUncertainty=dataDirectory+"Summer13_V5_DATA_UncertaintySources_AK5PFchs.txt"

  # control plot classes
  controlPlots = [ 
    controlPlot("jetmetAK5PF", "ObjectsControlPlots", "JetmetControlPlots", { "btagging":btagging ,"WP":WP }),
    controlPlot("vertexAssociation", "VertexAssociationControlPlots", "VertexAssociationControlPlots", { }),
    controlPlot("selection", "ZbbEventSelectionControlPlots", "ZbbEventSelectionControlPlots", { }),
    controlPlot("MCselection", "MonteCarloSelectionControlPlots", "MonteCarloSelectionControlPlots", { }),
    controlPlot("matrixElements", "MatrixElementControlPlots", "MatrixElementControlPlots", { }),
    controlPlot("leptonsReweighting", "LeptonsReweightingControlPlots", "LeptonsReweightingControlPlots", { }),
    controlPlot("mcReweighting", "MonteCarloReweightingControlPlots", "MonteCarloReweightingControlPlots", { }),
    controlPlot("lumiReweighting", "LumiReWeightingControlPlots", "LumiReWeightingControlPlots", { }),
    controlPlot("btaggingReweighting", "BtaggingReWeightingControlPlots", "BtaggingReWeightingControlPlots", { "btagging":btagging ,"WP":WP })
    ]

  if runningMode == "plots" :
    plotCP = [
      controlPlot("allmuons", "ObjectsControlPlots", "MuonsControlPlots", { "muonList":"allmuons", "muonType":"none" }),
      controlPlot("tightmuons", "ObjectsControlPlots", "MuonsControlPlots", { "muonType":"tight" }),
      controlPlot("allelectrons", "ObjectsControlPlots", "ElectronsControlPlots", { "electronList":"allelectrons", "electronType":"none" }),
      controlPlot("tightelectrons", "ObjectsControlPlots", "ElectronsControlPlots", { "electronType":"tight" }),
      ]
    for cp in plotCP : controlPlots.append(cp)
    
  # event content: lists of eventCollection, eventProducer, and eventWeight objects respectively.
  eventCollections = [ eventCollection("genParticles","vector<reco::GenParticle>","genParticles"),
                       eventCollection("lheParticles","LHEEventProduct","source"),
                       eventCollection("genJets","vector<reco::GenJet>","ak5GenJets"),
                       eventCollection("genInfo","GenEventInfoProduct","generator"),
                       eventCollection("vertices","vector<reco::Vertex>","goodPV"),
                       eventCollection("jets","vector<pat::Jet>","selectedPatJetsWithBeta"),
                       #eventCollection("jets","vector<pat::Jet>","selectedPatJetsCA8PrunedSubjetsPF"),
                       #eventCollection("jets","vector<pat::Jet>","selectedPatJetsCA8CHSWithBeta"),
                       eventCollection("MET","vector<pat::MET>","patType01SCorrectedPFMet"),
                       eventCollection("METNNregression","vector<pat::MET>","patPFMet"),
                       eventCollection("Zmumu","vector<reco::CompositeCandidate>","zmuTightmuTight"),
                       eventCollection("Zelel","vector<reco::CompositeCandidate>","zelTightelTight"),
                       eventCollection("triggerInfo","pat::TriggerEvent","patTriggerEvent"),
                       eventCollection("electrons","vector<pat::Electron>","tightElectrons"),
                       eventCollection("muons","vector<pat::Muon>","tightMuons"),
                       eventCollection("allelectrons","vector<pat::Electron>","allElectrons"),
                       eventCollection("allmuons","vector<pat::Muon>","allMuons"),
                       eventCollection("PileupSummaryInfo","std::vector< PileupSummaryInfo >","addPileupInfo"),
                       eventCollection("rho","double",("kt6PFJets","rho")),
                     ] 

  eventProducers   = [ eventProducer("vertex", "ObjectSelection", "vertex", {}),
                       eventProducer("goodJets_mu", "ObjectSelection", "goodJets", { "muChannel":True,"eleChannel":False } ),
                       eventProducer("goodJets_ele", "ObjectSelection", "goodJets", { "muChannel":False,"eleChannel":True } ),
                       eventProducer("goodJets_all", "ObjectSelection", "goodJets", { "muChannel":True,"eleChannel":True } ),
                       eventProducer("goodJets_none", "ObjectSelection", "goodJets", { "muChannel":False,"eleChannel":False } ),
                       eventProducer("isMuTriggerOK", "ObjectSelection", "isTriggerOK", { "muChannel":True,"eleChannel":False,"perRun":True } ),
                       eventProducer("isEleTriggerOK", "ObjectSelection", "isTriggerOK", { "muChannel":False,"eleChannel":True,"perRun":True } ),
                       eventProducer("isTriggerOK", "ObjectSelection", "isTriggerOK", { "muChannel":True,"eleChannel":True,"perRun":True } ),
                       eventProducer("category", "PatAnalysis.EventSelection", "eventCategory", { "btagging":btagging, "WP":WP, "ZjetFilter":"bcl" } ),
                       eventProducer("bestZmumuCandidate", "ObjectSelection", "findBestCandidate", { "muChannel":True,"eleChannel":False } ),
                       eventProducer("bestZelelCandidate", "ObjectSelection", "findBestCandidate", { "muChannel":False,"eleChannel":True } ),
                       #eventProducer("bestDiLeptCandidate", "ObjectSelection", "findBestDiLeptCandidate", { "muChannel":True,"eleChannel":True } ),
		       eventProducer("bestZcandidate", "ObjectSelection", "findBestCandidate", { "muChannel":True,"eleChannel":True } ),
		       eventProducer("dijet_muChannel", "ObjectSelection", "findDijetPair",{ "btagging":btagging,"WP":WP,"muChannel":True,"eleChannel":False } ),
                       eventProducer("dijet_eleChannel", "ObjectSelection", "findDijetPair", { "btagging":btagging,"WP":WP,"muChannel":False,"eleChannel":True } ),
                       eventProducer("dijet_all", "ObjectSelection", "findDijetPair", { "btagging":btagging,"WP":WP,"muChannel":True,"eleChannel":True } ),
                       eventProducer("sortedGenJets", "MonteCarloSelection", "genjetCollectionsProducer", { "ptcut":0, "etacut":10 } ),
#                       eventProducer("genZparticle", "MonteCarloSelection", "getGenZparticle", { "muons":True, "electrons":True, "leptonPtCut":20, "leptonEtaCut":2.4 } )
                       eventProducer("genZparticle", "MonteCarloSelection", "getGenZleptonPair", { "muons":True, "electrons":True, "leptonPtCut":20, "leptonEtaCut":2.4 } )
                     ]

  eventWeights     = [ eventWeight("Btagging","BtaggingWeight","BtaggingWeight",{"jmin1":0,"jmax1":999,"jmin2":0,"jmax2":999,"file":ssvperfData,"btagging":btagging}),
                       eventWeight("Leptons","LeptonsReweighting","LeptonsReWeighting", {}),
                       eventWeight("MonteCarlo","MonteCarloReweighting","MonteCarloReWeighting", {"shift":0, "MCmode":"none"}),
                       eventWeight("PileUp","LumiReWeighting","LumiReWeighting", {"MonteCarloFileName":pileupMC, "DataFileName":pileupData, "systematicShift":0})
                     ]

class eventDumpConfig:
  # fine-tuning of the event content for display
  productsToPrint   = [ ] # list of product to display (use the producer label)
  collectionsToHide = [ "genParticles" ] # collections used in the analysis but not printed (use the collection label) 

