from listForRDS import lumi
from llbbSF import SFlist
from llbbPlotsList import *

class options_():
    #list of samples
    samples = [
        "DATA",
        #"DYjets",
        "TTFullLept",
        #"TTSemiLept",
        #"ZZ",
        #"WZ",
        #"WW",
        #"Wt",
        #"Wtbar",
        #"ZH125",
        ]
    print samples

    #Systematics
    #SYST = "Nominal" 
    #SYST = "JESup" 
    #SYST = "JESdown" 
    #SYST = "JERup" 
    #SYST = "JERdown" 
    #SYST = "BTAG_bc_up" 
    #SYST = "BTAG_bc_down" 
    #SYST = "BTAG_light_up" 
    #SYST = "BTAG_light_down" 
    #print SYST
	
    #template for file name
    path_data = "/nfs/user/acaudron/ControlPlots/cp5314p1/AllRDS/Nominal/RDS_Data2012/Data2012_Summer12_final_skimed_zmet.root"
    path = "/nfs/user/acaudron/ControlPlots/cp5314p1/AllRDS/SYST/RDS_NAME/NAME_Summer12_final_skimed_zmet.root"

    #option to split or not the DY sample
    doDYsplit = True
    DYdiv = {
        "Zbb" : "(abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5)",
        "Zbx" : "((abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5))",
        "Zxx" : "(abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5)"
        }

    #stages
    stages = {
        "Mu" : "(rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10)",
        "El" : "(rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10)"
        #"Mu" : "(rc_stage_8_idx&&jetmetMETsignificance<10)",
        #"El" : "(rc_stage_19_idx&&jetmetMETsignificance<10)"
        }
    
    stagesFit = {
        "Mu" : "(rc_stage_8_idx&&jetmetMETsignificance<10)",
        "El" : "(rc_stage_19_idx&&jetmetMETsignificance<10)"
        }

    print "stages:", stages

    Stages = {}
    Stages["Zjj"] = {
        "Mu":{"dir":"Muon","cut":"(rc_stage_2_idx&&jetmetnj>1&&jetmetMETsignificance<10&&boostselectionZbbM>0&&boostselectionZbbM<1500&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106)"},
        "El":{"dir":"Electron","cut":"(rc_stage_13_idx&&jetmetnj>1&&jetmetMETsignificance<10&&boostselectionZbbM>0&&boostselectionZbbM<1500&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106)"}
        }

    Stages["Zbb"] = {
        "Mu":{"dir":"Muon","cut":stages["Mu"]},
        "El":{"dir":"Electron","cut":stages["El"]}
        }

    #define cuts
    presel = "("+stages["El"]+"_idx || "+stages["Mu"]+"_idx)"
    
    rangeMassA = []
    mbb=10
    for i in range(1,36):
      dmbb=0.15*mbb*1.5
      step_mbb = dmbb/1.5
      rangeMassA.append([int(mbb-dmbb),int(mbb+dmbb),int(mbb)])
      mbb+=step_mbb

    rangeMassH = []
    mllbb=10
    for i in range(1,36):
      dmllbb=0.15*mllbb*1.5
      step_mllbb = dmllbb/1.5
      rangeMassH.append([int(mllbb-dmllbb),int(mllbb+dmllbb),int(mllbb)])
      mllbb+=step_mllbb

    cut = {}
    mA_list = {}
    mA_list_down = {}
    mA_list_up = {}
    mH_list = {}
    mH_list_down = {}
    mH_list_up = {}

    for mA in rangeMassA:
        for mH in rangeMassH:
            key = "mA"+str(mA[0])+"to"+str(mA[1])+"_mH"+str(mH[0])+"to"+str(mH[1])
            cut[key] = "boostselectiondijetM>="+str(mA[0])+"&&boostselectiondijetM<"+str(mA[1])+"&&boostselectionZbbM>="+str(mH[0])+"&&boostselectionZbbM<"+str(mH[1])
            mA_list[key] = mA[2]
            mA_list_down[key] = mA[0]
            mA_list_up[key] = mA[1]
            mH_list[key] = mH[2]
            mH_list_down[key] = mH[0]
            mH_list_up[key] = mH[1]

    #categories
    categories = {
        "Mu" : stages["Mu"],
        "El" : stages["El"],
        }

    #BTAG weight
    BTAG = "*btaggingReweightingMM"
    print "BTAG:", BTAG

    #define reweighting formula              
    baseForm = "*leptonsReweightingweight*lumiReweightingLumiWeight*mcReweightingweight"

    rewForm = {}
    rewForm["Zjj"] = {
        "Mu":baseForm,
        "El":baseForm
        }
    
    rewForm["Zbb"] = {
        "Mu":baseForm+BTAG,
        "El":baseForm+BTAG
    }
    
    wZbb = "( abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 )"+SFlist["Nominal"]["Zbb"]
    wZbx = "( (abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5) )"+SFlist["Nominal"]["Zbx"]
    wZxx = "( abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5 )"+SFlist["Nominal"]["Zxx"]
    wtt = SFlist["Nominal"]["TT"].replace("*","")
    wdy = "("+wZbb+"+"+wZbx+"+"+wZxx+")"

    #Uncertainty on the bkg fit
    TTBKG =   [1.00, 1.02, 1.00, 0.98]
    ZbbBKG =  [1.00, 0.99, 0.97, 0.99]
    ZbbjBKG = [0.99, 0.98, 1.02, 0.98]
    ZxxBKG =  [1.08, 0.98, 1.00, 0.99]

    print "categories:", categories

    #output llbbYield
    output = "treeV3_SYST.root"
    #name of the directory where the txt for the limit will be written
    TRUEYIELDS = True
    if not TRUEYIELDS : dirLimits = "/nfs/user/acaudron/datacards2HDM/"
    else : dirLimits = "/nfs/user/acaudron/datacards2HDMyieldsSignal/"


