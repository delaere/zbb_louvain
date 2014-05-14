from zbbConfig_data import *

# my variables: files, systematics and other options
configuration.JERfactor = 1.
configuration.JESfactor = 0.
configuration.LeptonTnPfactor = 0 # Lepton reweighting uncertainty
configuration.SF_uncert="mean" #btagging reweighting:  choose among min/max/mean
if configuration.btagging == "CSV":
    configuration.SF_running_mode= "hardcoded_nofit" #btagging reweighting: choose between hardcoded_nofit/hardcoded/database
    configuration.btagperfData=configuration.dataDirectory+"btag_allalgos_witheff.root"
elif configuration.btagging == "JP":
    configuration.SF_running_mode= "database" #btagging reweighting: choose between hardcoded_nofit/hardcoded/database 
    configuration.btagperfData=configuration.dataDirectory+"performance_jp_witheff.root"
configuration.pileupData=configuration.dataDirectory+"Cert_190456-208686_8TeV_22Jan2013ReReco_pileupTruth.root"
configuration.pileupMC=configuration.dataDirectory+"MCpileup_Summer12_S10.root"

configuration.toprint = ["JERfactor", "JESfactor", "LeptonTnPfactor", "SF_uncert", "SF_running_mode", "btagperfData", "pileupData", "pileupMC"]

# control plot classes
updateControlPlots = [
    controlPlot("MCselection", "MonteCarloSelectionControlPlots", "MonteCarloSelectionControlPlots", { }),
    controlPlot("genMets","MonteCarloSelectionControlPlots","genMetsControlPlots",{}),
    controlPlot("leptonsReweighting", "LeptonsReweightingControlPlots", "LeptonsReweightingControlPlots", { }),
    controlPlot("mcReweighting", "MonteCarloReweightingControlPlots", "MonteCarloReweightingControlPlots", { }),
    controlPlot("lumiReweighting", "LumiReWeightingControlPlots", "LumiReWeightingControlPlots", { }),
    controlPlot("btaggingReweighting", "BtaggingReWeightingControlPlots", "BtaggingReWeightingControlPlots", { "btagging":configuration.btagging ,"WP":configuration.WP })
    ]
for cp in updateControlPlots : configuration.controlPlots.append(cp)

# event content: lists of eventCollection, eventProducer, and eventWeight objects respectively.
updateEventCollections = [
    eventCollection("genMET","vector<reco::GenMET>","genMetTrue"),
    ]
for ec in updateEventCollections : configuration.eventCollections.append(ec)

updateEventProducers = [
    #eventProducer("genZparticle", "MonteCarloSelection", "getGenZparticle", { "muons":True, "electrons":True, "leptonPtCut":20, "leptonEtaCut":2.4 } )
    eventProducer("genZparticle", "MonteCarloSelection", "getGenZleptonPair", { "muons":True, "electrons":True, "leptonPtCut":20, "leptonEtaCut":2.4 } ),
    eventProducer("MEMET_4v", "MonteCarloSelection", "getMEMET_4v", {} ),
    eventProducer("NumberOfNeutrinos", "MonteCarloSelection", "getNumberOfStatus3Neutrinos", {} ),
    ]
for ep in updateEventProducers : configuration.eventProducers.append(ep)

configuration.eventWeights = [
    eventWeight("Btagging","BtaggingWeight","BtaggingWeight",{"jmin1":0,"jmax1":999,"jmin2":0,"jmax2":999,"file":configuration.btagperfData,"btagging":configuration.btagging}),
    eventWeight("Leptons","LeptonsReweighting","LeptonsReWeighting", {}),
    eventWeight("MonteCarlo","MonteCarloReweighting","MonteCarloReWeighting", {"shift":0, "MCmode":"none"}),
    eventWeight("PileUp","LumiReWeighting","LumiReWeighting", {"MonteCarloFileName":configuration.pileupMC, "DataFileName":configuration.pileupData, "systematicShift":0})
    ]

# fine-tuning of the event content for display
eventDumpConfig.collectionsToHide.append("genParticles")

printConfig(configuration)
                                                                             
