
from zbbConfig_data import *

def updateConfiguration(c=configuration):
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

    #toprint = configuration.toprint
    c.toprint.extend(["JERfactor", "JESfactor", "LeptonTnPfactor", "SF_uncert", "SF_running_mode", "btagperfData", "pileupData", "pileupMC"])

    # control plot classes
    updateControlPlots = [
        controlPlot("MCselection", "MonteCarloSelectionControlPlots", "MonteCarloSelectionControlPlots", { }),
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
        eventWeight("MonteCarlo","MonteCarloReweighting","MonteCarloReWeighting", {"shift":0, "MCmode":"none"}),
        eventWeight("PileUp","LumiReWeighting","LumiReWeighting", {"MonteCarloFileName":c.pileupMC, "DataFileName":c.pileupData, "systematicShift":0})
        ]

updateConfiguration(c=configuration)

# fine-tuning of the event content for display
eventDumpConfig.collectionsToHide.append("genParticles")

