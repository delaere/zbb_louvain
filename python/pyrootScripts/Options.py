"""
Script containing some options for python scripts
"""

#Define a list of intersting plots
Vars = {}
Vars["Zbb"] = {
    #"boostselectionbestzmassMu":{"name":"boostselectionbestzmassMu","title":"boostselectionbestzmassMu","bin":30,"xmin":76,"xmax":106},
    #"boostselectionbestzmassEle":{"name":"boostselectionbestzmassEle","title":"boostselectionbestzmassEle","bin":30,"xmin":76,"xmax":106},
    #"boostselectionbestzptMu":{"name":"boostselectionbestzptMu","title":"boostselectionbestzptMu","bin":30,"xmin":0,"xmax":300},
    #"boostselectionbestzptEle":{"name":"boostselectionbestzptEle","title":"boostselectionbestzptEle","bin":30,"xmin":0,"xmax":300},
    #"boostselectiondphiZbb":{"name":"boostselectiondphiZbb","title":"boostselectiondphiZbb","bin":20,"xmin":0,"xmax":3.15},
    #"boostselectiondrZbb":{"name":"boostselectiondrZbb","title":"boostselectiondrZbb","bin":50,"xmin":0,"xmax":10},
    "boostselectionZbbM":{"name":"boostselectionZbbM","title":"boostselectionZbbM","bin":1000/20,"xmin":0,"xmax":1000},
    #"boostselectionZbbPt":{"name":"boostselectionZbbPt","title":"boostselectionZbbPt","bin":1000/20,"xmin":0,"xmax":1000},
    #"boostselectiondetab1l2":{"name":"boostselectiondetab1l2","title":"boostselectiondetab1l2","bin":20,"xmin":0,"xmax":5},
    #"boostselectiondetab2l1":{"name":"boostselectiondetab2l1","title":"boostselectiondetab2l1","bin":20,"xmin":0,"xmax":5},
    #"jetmetMET":{"name":"jetmetMET","title":"jetmetMET","bin":100/5,"xmin":0,"xmax":100},
    #"jetmetMETphi":{"name":"jetmetMETphi","title":"jetmetMETphi","bin":30,"xmin":-3.15,"xmax":3.15},
    #"jetmetMETsignificance":{"name":"jetmetMETsignificance","title":"jetmetMETsignificance","bin":20,"xmin":0,"xmax":20},
    #"jetmetnj":{"name":"jetmetnj","title":"jetmetnj","bin":10,"xmin":-0.5,"xmax":9.5},
    #"matrixElementsbjet1pt":{"name":"matrixElementsbjet1pt","title":"matrixElementsbjet1pt","bin":25,"xmin":0,"xmax":250},
    #"matrixElementsbjet2pt":{"name":"matrixElementsbjet2pt","title":"matrixElementsbjet2pt","bin":15,"xmin":0,"xmax":150},
    #"matrixElementsbjet1etapm":{"name":"matrixElementsbjet1etapm","title":"matrixElementsbjet1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsbjet2etapm":{"name":"matrixElementsbjet2etapm","title":"matrixElementsbjet2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsmu1pt":{"name":"matrixElementsmu1pt","title":"matrixElementsmu1pt","bin":25,"xmin":0,"xmax":250},
    #"matrixElementsmu2pt":{"name":"matrixElementsmu2pt","title":"matrixElementsmu2pt","bin":15,"xmin":0,"xmax":150},
    #"matrixElementsmu1etapm":{"name":"matrixElementsmu1etapm","title":"matrixElementsmu1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsmu2etapm":{"name":"matrixElementsmu2etapm","title":"matrixElementsmu2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsel1pt":{"name":"matrixElementsel1pt","title":"matrixElementsel1pt","bin":25,"xmin":0,"xmax":250},
    #"matrixElementsel2pt":{"name":"matrixElementsel2pt","title":"matrixElementsel2pt","bin":15,"xmin":0,"xmax":150},
    #"matrixElementsel1etapm":{"name":"matrixElementsel1etapm","title":"matrixElementsel1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsel2etapm":{"name":"matrixElementsel2etapm","title":"matrixElementsel2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"boostselectionCentrality":{"name":"boostselectionCentrality","title":"boostselectionCentrality","bin":20,"xmin":0,"xmax":1},
    #"boostselectionCentralityBoost":{"name":"boostselectionCentralityBoost","title":"boostselectionCentralityBoost","bin":20,"xmin":0,"xmax":1},
    #"boostselectiondijetM":{"name":"boostselectiondijetM","title":"boostselectiondijetM","bin":50,"xmin":0,"xmax":500},
    #"boostselectiondijetPt":{"name":"boostselectiondijetPt","title":"boostselectiondijetPt","bin":30,"xmin":0,"xmax":300},
    #"boostselectiondijetdR":{"name":"boostselectiondijetdR","title":"boostselectiondijetdR","bin":25,"xmin":0,"xmax":5},
    #"boostselectiondrllMu":{"name":"boostselectiondrllMu","title":"boostselectiondrllMu","bin":25,"xmin":0,"xmax":5},
    #"boostselectiondrllEle":{"name":"boostselectiondrllEle","title":"boostselectiondrllEle","bin":25,"xmin":0,"xmax":5},
    #"":{"name":"","title":"","bin":30,"xmin":76,"xmax":106},
}

Vars["Zjj"] = {
    "boostselectionbestzmassMu":{"name":"boostselectionbestzmassMu","title":"boostselectionbestzmassMu","bin":30,"xmin":76,"xmax":106},
    "boostselectionbestzmassEle":{"name":"boostselectionbestzmassEle","title":"boostselectionbestzmassEle","bin":30,"xmin":76,"xmax":106},
    "boostselectionbestzptMu":{"name":"boostselectionbestzptMu","title":"boostselectionbestzptMu","bin":30,"xmin":0,"xmax":300},
    "boostselectionbestzptEle":{"name":"boostselectionbestzptEle","title":"boostselectionbestzptEle","bin":30,"xmin":0,"xmax":300},
    "boostselectiondphiZbb":{"name":"boostselectiondphiZbb","title":"boostselectiondphiZbb","bin":20,"xmin":0,"xmax":3.15},
    "boostselectiondrZbb":{"name":"boostselectiondrZbb","title":"boostselectiondrZbb","bin":50,"xmin":0,"xmax":10},
    "boostselectionZbbM":{"name":"boostselectionZbbM","title":"boostselectionZbbM","bin":1000/20,"xmin":0,"xmax":1000},
    "boostselectionZbbPt":{"name":"boostselectionZbbPt","title":"boostselectionZbbPt","bin":1000/20,"xmin":0,"xmax":1000},
    "boostselectiondetab1l2":{"name":"boostselectiondetab1l2","title":"boostselectiondetab1l2","bin":20,"xmin":0,"xmax":5},
    "boostselectiondetab2l1":{"name":"boostselectiondetab2l1","title":"boostselectiondetab2l1","bin":20,"xmin":0,"xmax":5},
    "jetmetMET":{"name":"jetmetMET","title":"jetmetMET","bin":100/5,"xmin":0,"xmax":100},
    "jetmetMETphi":{"name":"jetmetMETphi","title":"jetmetMETphi","bin":30,"xmin":-3.15,"xmax":3.15},
    "jetmetMETsignificance":{"name":"jetmetMETsignificance","title":"jetmetMETsignificance","bin":20,"xmin":0,"xmax":20},
    "jetmetnj":{"name":"jetmetnj","title":"jetmetnj","bin":10,"xmin":-0.5,"xmax":9.5},
    "matrixElementsbjet1pt":{"name":"matrixElementsbjet1pt","title":"matrixElementsbjet1pt","bin":25,"xmin":0,"xmax":250},
    "matrixElementsbjet2pt":{"name":"matrixElementsbjet2pt","title":"matrixElementsbjet2pt","bin":15,"xmin":0,"xmax":150},
    "matrixElementsbjet1etapm":{"name":"matrixElementsbjet1etapm","title":"matrixElementsbjet1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "matrixElementsbjet2etapm":{"name":"matrixElementsbjet2etapm","title":"matrixElementsbjet2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "matrixElementsmu1pt":{"name":"matrixElementsmu1pt","title":"matrixElementsmu1pt","bin":25,"xmin":0,"xmax":250},
    "matrixElementsmu2pt":{"name":"matrixElementsmu2pt","title":"matrixElementsmu2pt","bin":15,"xmin":0,"xmax":150},
    "matrixElementsmu1etapm":{"name":"matrixElementsmu1etapm","title":"matrixElementsmu1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "matrixElementsmu2etapm":{"name":"matrixElementsmu2etapm","title":"matrixElementsmu2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "matrixElementsel1pt":{"name":"matrixElementsel1pt","title":"matrixElementsel1pt","bin":25,"xmin":0,"xmax":250},
    "matrixElementsel2pt":{"name":"matrixElementsel2pt","title":"matrixElementsel2pt","bin":15,"xmin":0,"xmax":150},
    "matrixElementsel1etapm":{"name":"matrixElementsel1etapm","title":"matrixElementsel1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "matrixElementsel2etapm":{"name":"matrixElementsel2etapm","title":"matrixElementsel2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "boostselectionCentrality":{"name":"boostselectionCentrality","title":"boostselectionCentrality","bin":20,"xmin":0,"xmax":1},
    "boostselectionCentralityBoost":{"name":"boostselectionCentralityBoost","title":"boostselectionCentralityBoost","bin":20,"xmin":0,"xmax":1},
    "boostselectiondijetM":{"name":"boostselectiondijetM","title":"boostselectiondijetM","bin":50,"xmin":0,"xmax":500},
    "boostselectiondijetPt":{"name":"boostselectiondijetPt","title":"boostselectiondijetPt","bin":30,"xmin":0,"xmax":300},
    "boostselectiondijetdR":{"name":"boostselectiondijetdR","title":"boostselectiondijetdR","bin":25,"xmin":0,"xmax":5},
    "boostselectiondrllMu":{"name":"boostselectiondrllMu","title":"boostselectiondrllMu","bin":25,"xmin":0,"xmax":5},
    "boostselectiondrllEle":{"name":"boostselectiondrllEle","title":"boostselectiondrllEle","bin":25,"xmin":0,"xmax":5},
    #"":{"name":"","title":"","bin":30,"xmin":76,"xmax":106},
}

#define a template for the rootfile name
fileName = "/nfs/user/acaudron/ControlPlots/cp5314p1/RDS_V67/RDS_SAMPLE/SAMPLE_Summer12_final_skimed_zmet.root"

#selection to compute rewweighting
Stages = {}
Stages["Zjj"] = {
    #"Mu":{"dir":"Muon","cut":"(rc_stage_3_idx&&jetmetnj>1&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_14_idx&&jetmetnj>1&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10)"}
    #"Mu":{"dir":"Muon","cut":"(rc_stage_2_idx&&jetmetnj>1&&jetmetMETsignificance>10&&boostselectionZbbM>450&&boostselectionZbbM<600&&matrixElementsbjet1etapm>-1.5&&matrixElementsbjet1etapm<1.5)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_13_idx&&jetmetnj>1&&jetmetMETsignificance>10&&boostselectionZbbM>450&&boostselectionZbbM<600&&matrixElementsbjet1etapm>-1.5&&matrixElementsbjet1etapm<1.5)"}
    "Mu":{"dir":"Muon","cut":"(rc_stage_2_idx&&jetmetnj>1&&jetmetMETsignificance<10&&matrixElementsbjet1etapm>-1.5&&matrixElementsbjet1etapm<1.5&&matrixElementsbjet2etapm>-1.5&&matrixElementsbjet2etapm<1.5)"},
    "Ele":{"dir":"Electron","cut":"(rc_stage_13_idx&&jetmetnj>1&&jetmetMETsignificance<10&&matrixElementsbjet1etapm>-1.5&&matrixElementsbjet1etapm<1.5&&matrixElementsbjet2etapm>-1.5&&matrixElementsbjet2etapm<1.5)"}
    #"Mu":{"dir":"Muon","cut":"(rc_stage_2_idx&&jetmetnj>1&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetnj>1)"},#&&jetmetMETsignificance>10)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_13_idx&&jetmetnj>1&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetnj>1)"}#&&jetmetMETsignificance>10)"}
    }

Stages["Zbb"] = {
    #"Mu":{"dir":"Muon","cut":"(rc_stage_8_idx&&jetmetMETsignificance<10&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_19_idx&&jetmetMETsignificance<10&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10)"}
    #"Mu":{"dir":"Muon","cut":"(rc_stage_8_idx&&jetmetMETsignificance>10)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_19_idx&&jetmetMETsignificance>10)"}
    "Mu":{"dir":"Muon","cut":"(rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetnj>1&&jetmetMETsignificance<10)"},
    "Ele":{"dir":"Electron","cut":"(rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetnj>1&&jetmetMETsignificance<10)"}
    }

#Define BTAG WP
#BTAG = ""
BTAG = "*btaggingReweightingMM"
#define reweighting formula
baseFrom = "*leptonsReweightingweight*lumiReweightingLumiWeight*mcReweightingweight"
rewFrom = {}
rewFrom["Zjj"] = {
    "Mu":baseFrom,
    "Ele":baseFrom
    }

rewFrom["Zbb"] = {
    "Mu":baseFrom+BTAG,
    "Ele":baseFrom+BTAG 
    }

wZbb = "( abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 && jetmetnj==2 )*1.15"
wZbbj = "( abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 && jetmetnj>2 )*1.30"
wZbx = "( (abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5) )*1.30"
wZxx = "( abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5 )*1.28"
wtt = "1.05"
wdy = "("+wZbb+"+"+wZbbj+"+"+wZbx+"+"+wZxx+")"
