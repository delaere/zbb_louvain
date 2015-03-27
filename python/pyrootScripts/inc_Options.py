from llbbNorm import lumi

"""
Script containing some options for python scripts
"""
#########################################################################    
######################SET PARAMETERS #####################################    
#########################################################################    
    
    
#########################################################################    
#path = "/home/fynu/bfrancois/storage/RDS/5320_BTAG_Skimmed_V5/SAMPLE_Summer12_final_skimed_ll2jetsX.root"
path = "/home/fynu/cbeluffi/storage/RDS/5320_BTAG_Skimmed_V5/llbbX/SAMPLE_Summer12_final_skimed_llbbX_withWeights_V3_BDT.root"


#########################################################################
stagesFit = {
    "Mu" : "(rc_stage_6_idx &&jetmetMETsignificance<10&& eventSelectionmu1pt_inc>20 && eventSelectionmu2pt_inc>20 &&  eventSelectiondilepM_inc > 60 &&  eventSelectiondilepM_inc < 120  && jetmetbjet1pt>30 && jetmetbjet2pt>30)",
    "El" : "(rc_stage_16_idx&&jetmetMETsignificance<10&& eventSelectionel1pt_inc>20 && eventSelectionel2pt_inc>20 &&  eventSelectiondilepM_inc > 60 &&  eventSelectiondilepM_inc < 120  && jetmetbjet1pt>30 && jetmetbjet2pt>30)"
    }
    
cat="2j" #2j or 3j or noCat
extraCutsCat=""
if cat== "2j": extraCutsCat="&&jetmetnj==2&&(eventSelectiondijetM<80||eventSelectiondijetM>150)"
elif cat== "3j": extraCutsCat="&&jetmetnj>2&&(eventSelectiondijetM<50||eventSelectiondijetM>150)"    
    
#########################################################################
#Define BTAG WP
#BTAG = ""
bTag="JP"
BTAG = "*btaggingReweightingMM"
#define reweighting formula
baseForm = "*leptonsReweightingweight*lumiReweightingLumiWeight*mcReweightingweight"

#########################################################################
doDYsplit=True
DYdiv = {
   "Zbb" : "(abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5)",
   "Zbx" : "((abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5))",
   "Zxx" : "(abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5)"
}
#########################################################################
rewForm = {}
rewForm["lljets"] = {
    "Mu":baseForm,
    "El":baseForm,
    #"MuE":baseForm
    }

rewForm["llbbX"] = {
    "Mu":baseForm+BTAG,
    "El":baseForm+BTAG, 
    #"MuE":baseForm+BTAG 
    }
#########################################################################
        
SFlist = {}

SFlist["Nominal"]={
  "Zbb" : "*((jetmetnj==2&&(eventSelectiondijetM<80||eventSelectiondijetM>150) )*1.363 + (jetmetnj>2&&(eventSelectiondijetM<50||eventSelectiondijetM>150))*1.454)",
  "Zbx" : "*1.454",
  "Zxx" : "*2.34",
  "TT" : "*1.014",
  }    
    

wZbb = "( abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 )"+SFlist["Nominal"]["Zbb"]
wZbx = "( (abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5) )"+SFlist["Nominal"]["Zbx"]
wZxx = "( abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5 )"+SFlist["Nominal"]["Zxx"]
wtt = SFlist["Nominal"]["TT"].replace("*","")
wdy = "("+wZbb+"+"+wZbx+"+"+wZxx+")"


#########################################################################

#Define a list of intersting plots
Vars = {}
Vars["llbbX"] = {
    "IncLepslep1pt":{"name":"IncLepslep1pt","title":"IncLepslep1pt","bin":50,"xmin":0,"xmax":225},
    "IncLepslep1etapm":{"name":"IncLepslep1etapm","title":"IncLepslep1etapm","bin":20,"xmin":-2.6,"xmax":2.6},
    "IncLepslep1phi":{"name":"IncLepslep1phi","title":"IncLepslep1phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "IncLepslep2pt":{"name":"IncLepslep2pt","title":"IncLepslep2pt","bin":50,"xmin":0,"xmax":200},
    "IncLepslep2etapm":{"name":"IncLepslep2etapm","title":"IncLepslep2etapm","bin":20,"xmin":-2.6,"xmax":2.6},
    "IncLepslep2phi":{"name":"IncLepslep2phi","title":"IncLepslep2phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "Mll":{"name":"eventSelectiondilepM_inc","title":"Mll","bin":5,"xmin":60,"xmax":120},
    "DRll":{"name":"eventSelectiondrll_inc","title":"DRll","bin":50,"xmin":0,"xmax":5},
    "PTll":{"name":"eventSelectiondilepPt_inc","title":"PTll","bin":50,"xmin":0,"xmax":250},
    "dEtall":{"name":"abs(IncLepslep1etapm-IncLepslep2etapm)","title":"dEtall","bin":50,"xmin":0,"xmax":5},
    "dPhill":{"name":"abs(abs(abs(IncLepslep1phi-IncLepslep2phi)-3.14159)-3.14159)","title":"dPhill","bin":50,"xmin":0,"xmax":3.2},
    "Nlep":{"name":"eventSelectionnlept_inc","title":"Nlep","bin":5,"xmin":0,"xmax":5},
    "jetmetnj":{"name":"jetmetnj","title":"jetmetnj","bin":9,"xmin":0,"xmax":9},
    "IncJetsNlightJets":{"name":"IncJetsNlightJets","title":"IncJetsNlightJets","bin":6,"xmin":0,"xmax":6},
    "IncJetsNbJets":{"name":"IncJetsNbJets","title":"IncJetsNbJets","bin":6,"xmin":0,"xmax":6},
    "IncJetsbjet1pt":{"name":"IncJetsbjet1pt","title":"IncJetsbjet1pt","bin":50,"xmin":0,"xmax":275},
    "IncJetsbjet1etapm":{"name":"IncJetsbjet1etapm","title":"IncJetsbjet1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "IncJetsbjet1phi":{"name":"IncJetsbjet1phi","title":"IncJetsbjet1phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "IncJetsbjet1JPdisc":{"name":"IncJetsbjet1JPdisc","title":"IncJetsbjet1JPdisc","bin":50,"xmin":0,"xmax":2.5},
    "IncJetsbjet1CSVdisc":{"name":"IncJetsbjet1CSVdisc","title":"IncJetsbjet1CSVdisc","bin":50,"xmin":0,"xmax":1},
    "IncJetsbjet2pt":{"name":"IncJetsbjet2pt","title":"IncJetsbjet2pt","bin":50,"xmin":0,"xmax":150},
    "IncJetsbjet2etapm":{"name":"IncJetsbjet2etapm","title":"IncJetsbjet2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "IncJetsbjet2phi":{"name":"IncJetsbjet2phi","title":"IncJetsbjet2phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "IncJetsbjet2JPdisc":{"name":"IncJetsbjet2JPdisc","title":"IncJetsbjet2JPdisc","bin":50,"xmin":0,"xmax":2.5},
    "IncJetsbjet2CSVdisc":{"name":"IncJetsbjet2CSVdisc","title":"IncJetsbjet2CSVdisc","bin":50,"xmin":0,"xmax":1},
    "IncJetsjet1pt":{"name":"IncJetsjet1pt","title":"IncJetsjet1pt","bin":50,"xmin":0,"xmax":350},
    "IncJetsjet1eta":{"name":"IncJetsjet1eta","title":"IncJetsjet1eta","bin":15,"xmin":0,"xmax":2.5},
    "IncJetsjet1phi":{"name":"IncJetsjet1phi","title":"IncJetsjet1phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "IncJetsjet1JPdisc":{"name":"IncJetsjet1JPdisc","title":"IncJetsjet1JPdisc","bin":50,"xmin":0,"xmax":1},
    "IncJetsjet1CSVdisc":{"name":"IncJetsjet1CSVdisc","title":"IncJetsjet1CSVdisc","bin":50,"xmin":0,"xmax":1},
    "DRjj":{"name":"eventSelectiondijetdR_inc","title":"DRjj","bin":50,"xmin":0,"xmax":5},
    "Mjj":{"name":"eventSelectiondijetM_inc","title":"Mjj","bin":25,"xmin":0,"xmax":550},
    "PTjj":{"name":"eventSelectiondijetPt_inc","title":"PTjj","bin":50,"xmin":0,"xmax":400},
    "dEtajj":{"name":"abs(IncJetsbjet1etapm-IncJetsbjet2etapm)","title":"dEtajj","bin":50,"xmin":0,"xmax":5},
    "dPhijj":{"name":"abs(abs(abs(IncJetsbjet1phi-IncJetsbjet2phi)-3.14159)-3.14159)","title":"dPhijj","bin":50,"xmin":0,"xmax":3.3},
    "jetmetMET":{"name":"jetmetMET","title":"jetmetMET","bin":50,"xmin":0,"xmax":300},
    "jetmetMETphi":{"name":"jetmetMETphi","title":"jetmetMETphi","bin":25,"xmin":-3.2,"xmax":3.2},
    "jetmetMETsignificance":{"name":"jetmetMETsignificance","title":"jetmetMETsignificance","bin":50,"xmin":0,"xmax":75},
    "MVAMET_Pt":{"name":"allMetsMVAMET_Pt","title":"MVAMET_Pt","bin":50,"xmin":0,"xmax":300},
    "MVAMET_Phi":{"name":"allMetsMVAMET_Phi","title":"MVAMET_Phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "MVAMET_Significance":{"name":"allMetsMVAMET_Significance","title":"MVAMET_Significance","bin":50,"xmin":0,"xmax":150},
    "NoPUMET_Pt":{"name":"allMetsNoPUMET_Pt","title":"NoPUMET_Pt","bin":50,"xmin":0,"xmax":300},
    "NoPUMET_Phi":{"name":"allMetsNoPUMET_Phi","title":"NoPUMET_Phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "NoPUMET_Significance":{"name":"allMetsNoPUMET_Significance","title":"NoPUMET_Significance","bin":50,"xmin":0,"xmax":150},
    "Mlljj":{"name":"eventSelectionllbbM_inc","title":"Mlljj","bin":50,"xmin":0,"xmax":800},
    "PT_lljj":{"name":"eventSelectionllbbPt_inc","title":"PT_lljj","bin":50,"xmin":0,"xmax":400},
    "HT_lljj":{"name":"IncJetsbjet1pt+IncJetsbjet2pt+IncLepslep1pt+IncLepslep2pt","title":"HT_lljj","bin":50,"xmin":0,"xmax":700},
    "HT_met_lljj":{"name":"IncJetsbjet1pt+IncJetsbjet2pt+IncLepslep1pt+IncLepslep2pt+jetmetMET","title":"HT_met_lljj","bin":50,"xmin":0,"xmax":700},

    "MinusLogW_ZH_cor3":{"name":"MinusLogW_ZH_cor3","title":"-logW ZH correction 3","bin":100,"xmin":-5,"xmax":100},
    "MinusLogW_ZH_cor0":{"name":"MinusLogW_ZH_cor0","title":"-logW ZH correction 0","bin":100,"xmin":-5,"xmax":100},
    "MinusLogW_ZZ_cor3":{"name":"MinusLogW_ZZ_cor3","title":"-logW ZZ correction 3","bin":100,"xmin":-5,"xmax":100},
    "MinusLogW_ZZ_cor0":{"name":"MinusLogW_ZZ_cor0","title":"-logW ZZ correction 0","bin":100,"xmin":-5,"xmax":100},
    "MinusLogW_TT":{"name":"MinusLogW_TT","title":"-logW TT","bin":100,"xmin":-5,"xmax":100},
    "MinusLogW_gg_Zbb":{"name":"MinusLogW_gg_Zbb","title":"-logW Zbbgg","bin":100,"xmin":-5,"xmax":100},
    "MinusLogW_qq_Zbb":{"name":"MinusLogW_qq_Zbb","title":"-logW Zbbqq","bin":100,"xmin":-5,"xmax":100},

    "MLPTTDY_El_noCat":{"name":"MLPTTDY_El_noCat","title":"MLPTTDY_El_noCat","bin":4,"xmin":-0.1,"xmax":1.1}, 
    "MLPTTDY_Mu_noCat":{"name":"MLPTTDY_Mu_noCat","title":"MLPTTDY_Mu_noCat","bin":4,"xmin":-0.1,"xmax":1.1}, 
    "bdtTTDY_El_noCat":{"name":"bdtTTDY_El_noCat","title":"bdtTTDY_El_noCat","bin":100,"xmin":-1.2,"xmax":1.2}, 
    "bdtTTDY_Mu_noCat":{"name":"bdtTTDY_Mu_noCat","title":"bdtTTDY_Mu_noCat","bin":100,"xmin":-1.2,"xmax":1.2},    
    
     
    "leptonsReweightingweight":{"name":"leptonsReweightingweight","title":"leptonsReweightingweight","bin":100,"xmin":0.5,"xmax":1.1},
    "lumiReweightingLumiWeight":{"name":"lumiReweightingLumiWeight","title":"lumiReweightingLumiWeight","bin":100,"xmin":0.0,"xmax":2.0},
    "mcReweightingweight":{"name":"mcReweightingweight","title":"mcReweightingweight","bin":100,"xmin":-1,"xmax":1.0},
    "btaggingReweightingMM":{"name":"btaggingReweightingMM","title":"btaggingReweightingMM","bin":100,"xmin":0.8,"xmax":1.1},

}

Vars["lljets"] = {
    "IncLepslep1pt":{"name":"IncLepslep1pt","title":"IncLepslep1pt","bin":50,"xmin":0,"xmax":200},
    "IncLepslep1etapm":{"name":"IncLepslep1etapm","title":"IncLepslep1etapm","bin":20,"xmin":-2.6,"xmax":2.6},
    "IncLepslep1phi":{"name":"IncLepslep1phi","title":"IncLepslep1phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "IncLepslep2pt":{"name":"IncLepslep2pt","title":"IncLepslep2pt","bin":50,"xmin":0,"xmax":120},
    "IncLepslep2etapm":{"name":"IncLepslep2etapm","title":"IncLepslep2etapm","bin":20,"xmin":-2.6,"xmax":2.6},
    "IncLepslep2phi":{"name":"IncLepslep2phi","title":"IncLepslep2phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "Mll":{"name":"eventSelectiondilepM_inc","title":"Mll","bin":100,"xmin":10,"xmax":140},
    "DRll":{"name":"eventSelectiondrll_inc","title":"DRll","bin":50,"xmin":0,"xmax":5},
    "PTll":{"name":"eventSelectiondilepPt_inc","title":"PTll","bin":50,"xmin":0,"xmax":300},
    "dEtall":{"name":"abs(IncLepslep1etapm-IncLepslep2etapm)","title":"dEtall","bin":50,"xmin":0,"xmax":5},
    "dPhill":{"name":"abs(abs(abs(IncLepslep1phi-IncLepslep2phi)-3.14159)-3.14159)","title":"dPhill","bin":50,"xmin":0,"xmax":3.2},
    "Nlep":{"name":"eventSelectionnlept_inc","title":"Nlep","bin":5,"xmin":0,"xmax":5},
    "jetmetnj":{"name":"jetmetnj","title":"jetmetnj","bin":9,"xmin":0,"xmax":9},
    "IncJetsNlightJets":{"name":"IncJetsNlightJets","title":"IncJetsNlightJets","bin":6,"xmin":0,"xmax":6},
    "IncJetsNbJets":{"name":"IncJetsNbJets","title":"IncJetsNbJets","bin":6,"xmin":0,"xmax":6},
    "jetmetjet1pt":{"name":"jetmetjet1pt","title":"jetmetjet1pt","bin":50,"xmin":0,"xmax":250},
    "jetmetjet1etapm":{"name":"jetmetjet1etapm","title":"jetmetjet1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "jetmetjet1phi":{"name":"jetmetjet1phi","title":"jetmetjet1phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "jetmetjet1JPdisc":{"name":"jetmetjet1JPdisc","title":"jetmetjet1JPdisc","bin":50,"xmin":0,"xmax":2.5},
    "jetmetjet1CSVdisc":{"name":"jetmetjet1CSVdisc","title":"jetmetjet1CSVdisc","bin":50,"xmin":0,"xmax":1},
    "jetmetjet2pt":{"name":"jetmetjet2pt","title":"jetmetjet2pt","bin":50,"xmin":0,"xmax":150},
    "jetmetjet2etapm":{"name":"jetmetjet2etapm","title":"jetmetjet2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "jetmetjet2phi":{"name":"jetmetjet2phi","title":"jetmetjet2phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "jetmetjet2JPdisc":{"name":"jetmetjet2JPdisc","title":"jetmetjet2JPdisc","bin":50,"xmin":0,"xmax":2.5},
    "jetmetjet2CSVdisc":{"name":"jetmetjet2CSVdisc","title":"jetmetjet2CSVdisc","bin":50,"xmin":0,"xmax":1},
    "DRjj":{"name":"eventSelectiondijetdR_inc","title":"DRjj","bin":50,"xmin":0,"xmax":6},
    "Mjj":{"name":"eventSelectiondijetM_inc","title":"Mjj","bin":25,"xmin":0,"xmax":550},
    "PTjj":{"name":"eventSelectiondijetPt_inc","title":"PTjj","bin":50,"xmin":0,"xmax":400},
    "dEtajj":{"name":"abs(jetmetjet1etapm-jetmetjet2etapm)","title":"dEtajj","bin":50,"xmin":0,"xmax":5},
    "dPhijj":{"name":"abs(abs(abs(jetmetjet1phi-jetmetjet2phi)-3.14159)-3.14159)","title":"dPhijj","bin":50,"xmin":0,"xmax":3.3},
    "jetmetMET":{"name":"jetmetMET","title":"jetmetMET","bin":50,"xmin":0,"xmax":150},
    "jetmetMETphi":{"name":"jetmetMETphi","title":"jetmetMETphi","bin":25,"xmin":-3.2,"xmax":3.2},
    "jetmetMETsignificance":{"name":"jetmetMETsignificance","title":"jetmetMETsignificance","bin":50,"xmin":0,"xmax":20},
    "MVAMET_Pt":{"name":"allMetsMVAMET_Pt","title":"MVAMET_Pt","bin":50,"xmin":0,"xmax":150},
    "MVAMET_Phi":{"name":"allMetsMVAMET_Phi","title":"MVAMET_Phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "MVAMET_Significance":{"name":"allMetsMVAMET_Significance","title":"MVAMET_Significance","bin":50,"xmin":0,"xmax":60},
    "NoPUMET_Pt":{"name":"allMetsNoPUMET_Pt","title":"NoPUMET_Pt","bin":50,"xmin":0,"xmax":100},
    "NoPUMET_Phi":{"name":"allMetsNoPUMET_Phi","title":"NoPUMET_Phi","bin":25,"xmin":-3.2,"xmax":3.2},
    "NoPUMET_Significance":{"name":"allMetsNoPUMET_Significance","title":"NoPUMET_Significance","bin":50,"xmin":0,"xmax":40},
    "Mlljj":{"name":"eventSelectionllbbM_inc","title":"Mlljj","bin":50,"xmin":0,"xmax":800},
    "PT_lljj":{"name":"eventSelectionllbbPt_inc","title":"PT_lljj","bin":50,"xmin":0,"xmax":200},
    "HT_lljj":{"name":"jetmetjet1pt+jetmetjet2pt+IncLepslep1pt+IncLepslep2pt","title":"HT_lljj","bin":50,"xmin":0,"xmax":700},
    "HT_met_lljj":{"name":"jetmetjet1pt+jetmetjet2pt+IncLepslep1pt+IncLepslep2pt+jetmetMET","title":"HT_met_lljj","bin":50,"xmin":0,"xmax":700},
}

#selection to compute rewweighting
Stages = {}
Stages["lljets"] = {
    ######################
    # No Selection
    ######################
    #"Mu":{"dir":"Muon","cut":"rc_stage_2_idx"},
    #"Ele":{"dir":"Electron","cut":"rc_stage_12_idx"},
    #"MuE":{"dir":"MuE","cut":"rc_stage_22_idx"},
    ######################
    # Inclusive Selection
    ######################
    "Mu":{"dir":"Muon","cut":"(rc_stage_2_idx && eventSelectionmu1pt_inc>20 && eventSelectionmu2pt_inc>10 &&  eventSelectiondilepM_inc > 15 &&  eventSelectiondilepM_inc < 45 && jetmetMETsignificance<10000 && jetmetjet1pt>20 && jetmetjet2pt>20)"},
    "El":{"dir":"Electron","cut":"(rc_stage_12_idx && eventSelectionel1pt_inc>20 && eventSelectionel2pt_inc>10 && eventSelectiondilepM_inc > 15 &&  eventSelectiondilepM_inc < 45 && jetmetMETsignificance<10000 && jetmetjet1pt>20 && jetmetjet2pt>20)"},
    "MuE":{"dir":"MuE","cut":"(rc_stage_22_idx && (eventSelectionel1pt_inc >20 && eventSelectionmu2pt_inc >10 || eventSelectionel2pt_inc >10 && eventSelectionmu1pt_inc >20) && eventSelectiondilepM_inc > 0 &&  eventSelectiondilepM_inc < 45 && jetmetMETsignificance<10000 && jetmetjet1pt>20 && jetmetjet2pt>20)"}
    ######################
    # Inclusive Selection Mll>45 Mll<55  
    ######################
    #"Mu":{"dir":"Muon","cut":"(rc_stage_2_idx && eventSelectionmu1pt_inc>20 && eventSelectionmu2pt_inc>10 &&  eventSelectiondilepM_inc > 45 &&  eventSelectiondilepM_inc < 55 && jetmetMETsignificance<10000 && jetmetjet1pt>20 && jetmetjet2pt>20)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_12_idx && eventSelectionel1pt_inc>20 && eventSelectionel2pt_inc>10 && eventSelectiondilepM_inc > 45 &&  eventSelectiondilepM_inc < 55 && jetmetMETsignificance<10000 && jetmetjet1pt>20 && jetmetjet2pt>20)"},
    #"MuE":{"dir":"MuE","cut":"(rc_stage_22_idx && (eventSelectionel1pt_inc >20 && eventSelectionmu2pt_inc >10 || eventSelectionel2pt_inc >10 && eventSelectionmu1pt_inc >20) && eventSelectiondilepM_inc > 0 &&  eventSelectiondilepM_inc < 10000 && jetmetMETsignificance<10000 && jetmetjet1pt>20 && jetmetjet2pt>20)"}
    ######################
    # Inclusive Selection Mll<45 Safe 
    ######################
    #"Mu":{"dir":"Muon","cut":"(rc_stage_2_idx && eventSelectionmu1pt_inc>20 && eventSelectionmu2pt_inc>20 &&  eventSelectiondilepM_inc > 20 &&  eventSelectiondilepM_inc < 45 && jetmetMETsignificance<10000 && jetmetjet1pt>30 && jetmetjet2pt>30)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_12_idx && eventSelectionel1pt_inc>20 && eventSelectionel2pt_inc>20 && eventSelectiondilepM_inc > 20 &&  eventSelectiondilepM_inc < 45 && jetmetMETsignificance<10000 && jetmetjet1pt>30 && jetmetjet2pt>30)"},
    #"MuE":{"dir":"MuE","cut":"(rc_stage_22_idx && (eventSelectionel1pt_inc >20 && eventSelectionmu2pt_inc >20 || eventSelectionel2pt_inc >20 && eventSelectionmu1pt_inc >20) && eventSelectiondilepM_inc > 0 &&  eventSelectiondilepM_inc < 10000 && jetmetMETsignificance<10000 && jetmetjet1pt>30 && jetmetjet2pt>30)"}
    }

Stages["llbbX"] = {
    ######################
    # No Selection
    ######################
    #"Mu":{"dir":"Muon","cut":"rc_stage_6_idx"},
    #"Ele":{"dir":"Electron","cut":"rc_stage_16_idx"},
    #"MuE":{"dir":"MuE","cut":"rc_stage_26_idx"},
    ######################
    # Inclusive Selection
    ######################
    "Mu":{"dir":"Muon","cut":"(rc_stage_6_idx&&jetmetMETsignificance<10&& eventSelectionmu1pt_inc>20 && eventSelectionmu2pt_inc>20 &&  eventSelectiondilepM_inc > 60 &&  eventSelectiondilepM_inc < 120  && jetmetbjet1pt>30 && jetmetbjet2pt>30"+extraCutsCat+")"},
    "El":{"dir":"Electron","cut":"(rc_stage_16_idx&&jetmetMETsignificance<10&& eventSelectionel1pt_inc>20 && eventSelectionel2pt_inc>20 &&  eventSelectiondilepM_inc > 60 &&  eventSelectiondilepM_inc < 120  && jetmetbjet1pt>30 && jetmetbjet2pt>30"+extraCutsCat+")"},
    #"MuE":{"dir":"MuE","cut":"(rc_stage_26_idx && ((eventSelectionel1pt_inc >20 && eventSelectionmu2pt_inc >20) || (eventSelectionel2pt_inc >20 && eventSelectionmu1pt_inc >20)) && eventSelectiondilepM_inc > 60 &&  eventSelectiondilepM_inc < 120 && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30&&jetmetnj==2&&(eventSelectiondijetM<80||eventSelectiondijetM>150))"}
    }
