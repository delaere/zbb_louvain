import os

theZfilter = os.getenv("ZjetFilter")
if not theZfilter : theZfilter = "none"

weightmode = os.getenv("weightmode")
if not weightmode : weightmode = "none"

#configuration of the ControlPlot machinery
from collections import namedtuple
controlPlot     = namedtuple("controlPlot",    ["label","module","classname","kwargs"])
eventCollection = namedtuple("eventCollection",["label","handle","collection"])
eventProducer   = namedtuple("eventProducer",  ["label","module","function","kwargs"])
eventWeight     = namedtuple("eventWeight",    ["label","module","classname","kwargs"])

#default configuration: can be used like this on data
class configuration:
  # default I/O
  pythonpath = "UserCode.zbb_louvain."
  defaultFilename = "controlPlots"
  RDSname = "rds_zbb"
  WSname = "workspace_ras"

  # mode: plots or dataset
  #runningMode = "plots"
  runningMode = "dataset"
  RDSasCP = False #put to True if you want the variables in the RDS to start with the same name as the CP directories for the CP for which this option is implemented, if False the default purpose name will be used
  
  # Event selection class
  eventSelection = pythonpath+"ZbbEventSelection"

  # my variables: files, systematics and other options
  ptjet = 30.
  leadMuPt = 18.
  secMuPt = 8.
  btagging = "CSV"
  WP = ["M","L"] # to be ordered from tighter to looser ones: ["M","L"], ["T","L"], ["T","M"]
  muChannel = True
  eleChannel = True
  doMEcontrolPlots = True
  doNNJetRegression = False
  JERfactor = 0. # don't change it, should be 0 on data
  JESfactor = 0. # don't change it, should be 0 on data
  dataDirectory = str(os.environ["CMSSW_BASE"])+"/src/UserCode/zbb_louvain/data/"
  jecUncertaintyAK5=dataDirectory+"Summer13_V5_DATA_UncertaintySources_AK5PFchs.txt"
  jecUncertaintyAK7=dataDirectory+"Summer13_V5_DATA_UncertaintySources_AK7PFchs.txt"

  #parameter you want to print
  toprint = ['runningMode', 'eventSelection', 'ptjet', 'btagging', 'WP', 'muChannel', 'eleChannel', 'doMEcontrolPlots', 'doNNJetRegression']

  # control plot classes
  controlPlots = [
    controlPlot("jetmet", "ObjectsControlPlots", "JetmetControlPlots", { "btagging":btagging, "WP":WP, "postjetsall":"muChannel", "postjetsgood":"mu" }),
    controlPlot( "jetmetmatched", "ObjectsControlPlots", "JetmetControlPlots", { "btagging":btagging, "WP":WP, "postjetsall":"matchedJetWithB", "postjetsgood":"muMatched" }),
    controlPlot("allMets", "ObjectsControlPlots", "MetControlPlots", { }),
    controlPlot("vertexAssociation", "VertexAssociationControlPlots", "VertexAssociationControlPlots", { }),
    controlPlot("me", "MatrixElementControlPlots", "MatrixElementControlPlots", { }),
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
                       eventCollection("rawjets","vector<pat::Jet>","selectedPatJetsWithBeta"),
                       eventCollection("rawsubjets","vector<pat::Jet>","selectedPatJetsCA8PrunedSubjetsPF"),
                       eventCollection("rawfatjets","vector<pat::Jet>","selectedPatJetsCA8CHSwithNsub"),
                       eventCollection("rawprunedjets","vector<pat::Jet>","selectedPatJetsCA8CHSPrunedPacked"),
                       eventCollection("rawprunedjets2","vector<pat::Jet>","selectedPatJetsCA8CHSpruned"),
                       eventCollection("MET","vector<pat::MET>","patType1CorrectedPFMet"),
                       eventCollection("METNNregression","vector<pat::MET>","patPFMet"),
		       eventCollection("PFMETNoCorr","vector<pat::MET>","patPFMet"),
                       eventCollection("PFMET01Phi","vector<pat::MET>","patType01SCorrectedPFMet"),
                       eventCollection("PFMET01","vector<pat::MET>","patType01CorrectedPFMet"),
                       eventCollection("PFMET1","vector<pat::MET>","patTypeOnly1CorrectedPFMet"),
                       eventCollection("PFMETPhi","vector<pat::MET>","patTypeSysCorrectedPFMet"),
                       eventCollection("PFMET1Phi","vector<pat::MET>","patType1sysCorrectedPFMet"),
                       eventCollection("MVAMET","vector<pat::MET>","patPFMetMVA"),
                       eventCollection("NoPUMET","vector<pat::MET>","patPFMetNoPileUp"),
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
                       eventProducer("goodJets_mu", "ObjectSelection", "goodJets", { "muChannel":True,"eleChannel":False,"pt":ptjet } ),
                       eventProducer("goodJets_ele", "ObjectSelection", "goodJets", { "muChannel":False,"eleChannel":True,"pt":ptjet } ),
                       eventProducer("goodJets_all", "ObjectSelection", "goodJets", { "muChannel":True,"eleChannel":True,"pt":ptjet } ),
                       eventProducer("goodJets_none", "ObjectSelection", "goodJets", { "muChannel":False,"eleChannel":False,"pt":ptjet } ),
                       eventProducer("jets", "ObjectSelection", "allJets", {"jets":"rawjets" } ),
                       eventProducer("subjets", "ObjectSelection", "subjets", { } ),
                       eventProducer("fatjets", "ObjectSelection", "fatjets", { "pt":ptjet } ),
                       eventProducer("isMuTriggerOK", "ObjectSelection", "isTriggerOK", { "muChannel":True,"eleChannel":False,"perRun":True } ),
                       eventProducer("isEleTriggerOK", "ObjectSelection", "isTriggerOK", { "muChannel":False,"eleChannel":True,"perRun":True } ),
                       eventProducer("isINCTriggerOK", "ObjectSelection", "isTriggerIncOK", {"perRun":True } ),
                       eventProducer("isTriggerOK", "ObjectSelection", "isTriggerOK", { "muChannel":True,"eleChannel":True,"perRun":True } ),
		       eventProducer("isHambDiMuTriggerOK", "ObjectSelection", "isTriggerHambOK", {"perRun":True } ),
		       eventProducer("isDiMuTriggerNoMatchOK", "ObjectSelection", "passDiMuTrigger", {"perRun":True } ),
                       eventProducer("category", "PatAnalysis.EventSelection", "eventCategory", { "btagging":btagging, "WP":WP, "ZjetFilter":theZfilter } ),
                       eventProducer("bestZmumuCandidate", "ObjectSelection", "findBestCandidate", { "muChannel":True,"eleChannel":False } ),
                       eventProducer("bestZelelCandidate", "ObjectSelection", "findBestCandidate", { "muChannel":False,"eleChannel":True } ),
                       eventProducer("bestZcandidate", "ObjectSelection", "findBestCandidate", { "muChannel":True,"eleChannel":True } ),
                       eventProducer("bestDiLeptCandidate", "ObjectSelection", "findBestDiLeptCandidate", { "muChannel":True,"eleChannel":True } ),
                       eventProducer("bestHambDiMuCandidate", "ObjectSelection", "findBestHambDiMuCandidate", { "muChannel":True} ),
		       eventProducer("muonsPair", "ObjectSelection", "diLeptonsPair", { "bestLeptonCand":"bestZmumucandidate" } ),
                       eventProducer("electronsPair", "ObjectSelection", "diLeptonsPair", { "bestLeptonCand":"bestZelelcandidate" } ),
                       eventProducer("leptonsPair", "ObjectSelection", "diLeptonsPair", { "bestLeptonCand":"bestZcandidate" } ),
                       eventProducer("dijet_muChannel", "ObjectSelection", "findDijetPair", { "btagging":btagging,"WP":WP,"muChannel":True,"eleChannel":False } ),
                       eventProducer("dijet_eleChannel", "ObjectSelection", "findDijetPair", { "btagging":btagging,"WP":WP,"muChannel":False,"eleChannel":True } ),
                       eventProducer("dijet_all", "ObjectSelection", "findDijetPair", { "btagging":btagging,"WP":WP,"muChannel":True,"eleChannel":True } ),
                       eventProducer("sortedGenJets", "MonteCarloSelection", "genjetCollectionsProducer", { "ptcut":0, "etacut":10 } ),
		       eventProducer("dijet_matchedJetWithB", "ObjectSelection", "findJetsMatchedWithB", {}),
		       eventProducer("goodJets_muMatched","ObjectSelection","goodJetMatchedWithB",{}),
                       eventProducer("ptSortedLeptons", "ObjectSelection","leptonsFromPV_ptSorted",{}),
                       eventProducer("ptSortedLeptons_DRll", "ObjectSelection", "leptonsFromPV_ptSorted_DRllVetoOnFirstTwo", {"DRll_cut":0.3, "ptLeadLep":17.0, "ptSubLeadLep":8.0} )
                     ]

  eventWeights     = []

  #list of objects to update if you plan to chenge the b-tag WP and/or algo (see: "changeBTAG" below)
  toupdateForBtag = {
    "controlPlots" : ["jetmet","jetmetmatched"],
#    "controlPlots" : ["jetmet"],
    "eventProducers" : ["category", "dijet_muChannel", "dijet_eleChannel", "dijet_all"]
    }

#function to change the jet collection
def changeJetCollection(conf = None, jetcoll = "rawjets"):
  next((x for x in conf.eventProducers if x.label == "jets"), None).kwargs["jets"] = jetcoll
  return

#function to change jet pt cut
def changeJetPt(conf = None, ptjet=30.):
  if conf is None : return
  conf.ptjet = ptjet
  iter = (x for x in conf.eventProducers if x.function == "goodJets")
  while True:
    try: next(iter).kwargs["pt"] = ptjet
    except StopIteration : break  
  return
#function to change muon pt cut
def changeHambMuPt(conf = configuration, leadPt=17., secPt = 8.):
  if conf is None: return
  conf.leadMuPt = leadPt
  conf.secMuPt = secPt
  iter = (x for x in conf.eventProducers if x.function == "findBestHambDiMuCandidate")
  while True:
    try: next(iter).kwargs["leadPt"] = leadPt
    except StopIteration : break
  iter = (x for x in conf.eventProducers if x.function == "findBestHambDiMuCandidate")
  while True:
    try: next(iter).kwargs["secPt"] = secPt
    except StopIteration : break
  return

#function to switch b-tagging or WP
def changeBTAG(conf = None, btagging="CSV", WP=["M","L"]):
  if conf is None : return
  conf.btagging = btagging
  conf.WP = WP
  for up in conf.toupdateForBtag:
    for sub in conf.toupdateForBtag[up]:
      next((x for x in getattr(conf, up) if x.label == sub), None).kwargs["btagging"] = btagging
      next((x for x in getattr(conf, up) if x.label == sub), None).kwargs["WP"] = WP
  return

#function to switch to different dileptons selection: names is a map between the dilepton pair names and the dilepton candidate names
def changeDiLeptCand(conf = None, names = {"muonsPair" : "bestZmumucandidate", "electronsPair" : "bestZelelcandidate", "muelPair" : "bestZmuelcandidate", "leptonsPair" : "bestZcandidate"}):
  if conf is None : return
  for name in names:
    next((x for x in conf.eventProducers if x.label == name), None).kwargs["bestLeptonCand"] = names[name]
  return

class eventDumpConfig:
  # fine-tuning of the event content for display
  productsToPrint   = [ ] # list of product to display (use the producer label)
  collectionsToHide = [ ] # collections used in the analysis but not printed (use the collection label)

def updateConfMC(c=configuration):
    # my variables: files, systematics and other options
    c.JERfactor = 1.
    c.JESfactor = 0.
    c.LeptonTnPfactor = 0 # Lepton reweighting uncertainty
    if c.btagging == "CSV":
        c.SF_running_mode= "hardcoded_nofit" #btagging reweighting: choose between hardcoded_nofit/hardcoded/database
        c.btagperfData=c.dataDirectory+"btag_allalgos_witheff.root"
    elif c.btagging == "JP":
        c.SF_running_mode= "database" #btagging reweighting: choose between hardcoded_nofit/hardcoded/database
        c.btagperfData=c.dataDirectory+"performance_jp_witheff.root"
    c.SF_uncert="mean" #btagging reweighting:  choose among min/max/mean
    c.pileupData=c.dataDirectory+"Cert_190456-208686_8TeV_22Jan2013ReReco_pileupTruth.root"
    c.pileupMC=c.dataDirectory+"MCpileup_Summer12_S10.root"
    c.DYmerging=c.dataDirectory+"DYmergingWeights.txt"

    #toprint = configuration.toprint
    c.toprint.extend(["JERfactor", "JESfactor", "LeptonTnPfactor", "SF_uncert", "SF_running_mode", "btagperfData", "pileupData", "pileupMC"])

    # control plot classes
    updateControlPlots = [
        controlPlot("mcSelection", "MonteCarloSelectionControlPlots", "MonteCarloSelectionControlPlots", { }),
        controlPlot("genMets","MonteCarloSelectionControlPlots","genMetsControlPlots",{}),
        controlPlot("leptonsReweighting", "LeptonsReweightingControlPlots", "LeptonsReweightingControlPlots", { }),
        controlPlot("mcReweighting", "MonteCarloReweightingControlPlots", "MonteCarloReweightingControlPlots", { }),
        controlPlot("lumiReweighting", "LumiReWeightingControlPlots", "LumiReWeightingControlPlots", { }),
        controlPlot("btaggingReweighting", "BtaggingReWeightingControlPlots", "BtaggingReWeightingControlPlots", { "btagging":c.btagging ,"WP":c.WP })
        ]
    #controlPlots = configuration.controlPlots
    c.controlPlots.extend(updateControlPlots)

    # event content: lists of eventCollection, eventProducer, and eventWeight objects respectively.
    updateEventCollections = [
        eventCollection("genMET","vector<reco::GenMET>","genMetTrue"),
        ]
    #eventCollections = configuration.eventCollections
    c.eventCollections.extend(updateEventCollections)

    updateEventProducers = [
        #eventProducer("genZparticle", "MonteCarloSelection", "getGenZparticle", { "muons":True, "electrons":True, "leptonPtCut":20, "leptonEtaCut":2.4 } )
        eventProducer("genZparticle", "MonteCarloSelection", "getGenZleptonPair", { "muons":True, "electrons":True, "leptonPtCut":20, "leptonEtaCut":2.4 } ),
        eventProducer("MEMET_4v", "MonteCarloSelection", "getMEMET_4v", {} ),
        eventProducer("NumberOfNeutrinos", "MonteCarloSelection", "getNumberOfStatus3Neutrinos", {} ),
        ]
    #eventProducers = configuration.eventProducers
    c.eventProducers.extend(updateEventProducers)

    c.eventWeights = [
        eventWeight("Btagging","BtaggingWeight","BtaggingWeight", {"jmin1":0,"jmax1":999,"jmin2":0,"jmax2":999,"file":c.btagperfData,"btagging":c.btagging,"WP":c.WP}),
        eventWeight("Leptons","LeptonsReweighting","LeptonsReWeighting", {}),
        eventWeight("MonteCarlo","MonteCarloReweighting","MonteCarloReWeighting", {"shift":0, "MCmode":weightmode}),
        eventWeight("PileUp","LumiReWeighting","LumiReWeighting", {"MonteCarloFileName":c.pileupMC, "DataFileName":c.pileupData, "systematicShift":0})
        ]
