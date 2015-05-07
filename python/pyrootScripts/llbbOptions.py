## This script centralised the core of the H to ZA analysis from the trees produced from the PATtuples ##
## Default selection, normalisation, reweighting... can be retrieved from here and updated/custumised in each scripts which makes use of it ##

### Get the normalisation map ###
from llbbNorm import lumi
### Get the SFs to normalised the TTbar and the DY ###
from llbbSF import SFlist
### Get the list of plot to be produced ###
from llbbPlotsList import *

### Class containing default options ###
class options_():
    ### list of samples ###
    samples = [
        "DATA",
        "DYjets",
        "TTFullLept",
        "TTSemiLept",
        "ZZ",
        "WZ",
        "WW",
        "Wt",
        "Wtbar",
        "ZH125",
        ]

    ### Systematics ###
    SYST = "Nominal" 
    #SYST = "JESup" 
    #SYST = "JESdown" 
    #SYST = "JERup" 
    #SYST = "JERdown" 
    #SYST = "BTAG_bc_up" 
    #SYST = "BTAG_bc_down" 
    #SYST = "BTAG_light_up" 
    #SYST = "BTAG_light_down" 
	
    ### template for file name ###
    path_data = "/nfs/user/acaudron/ControlPlots/cp5314p1/AllRDS/Nominal/RDS_Data2012/Data2012_Summer12_final_skimed_zmet.root"
    path = "/nfs/user/acaudron/ControlPlots/cp5314p1/AllRDS/SYST/RDS_NAME/NAME_Summer12_final_skimed_zmet.root"

    ### option to split or not the DY sample ###
    doDYsplit = True
    DYdiv = {
        "Zbb" : "(abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5)",
        "Zbx" : "((abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5))",
        "Zxx" : "(abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5)"
        }

    ### analysis selection ###
    stages = {
        "Mu" : "(rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10)",
        "El" : "(rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10)"
        #"Mu" : "(rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10&&boostselectionZbbM>513&&boostselectionZbbM<811&&boostselectiondijetM>446&&boostselectiondijetM<704)",
        #"El" : "(rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10&&boostselectionZbbM>513&&boostselectionZbbM<811&&boostselectiondijetM>446&&boostselectiondijetM<704)"

        #"Mu" : "(rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10&&boostselectionZbbM>222&&boostselectionZbbM<350&&boostselectiondijetM>72&&boostselectiondijetM<114)",
        #"El" : "(rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10&&boostselectionZbbM>222&&boostselectionZbbM<350&&boostselectiondijetM>72&&boostselectiondijetM<114)"

#        "Mu" : "(rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10&&boostselectionZbbM>167&&boostselectionZbbM<265&&boostselectiondijetM>18&&boostselectiondijetM<28)",
#        "El" : "(rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10&&boostselectionZbbM>167&&boostselectionZbbM<265&&boostselectiondijetM>18&&boostselectiondijetM<28)"

        #"Mu" : "(rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10&&boostselectiondijetM>18&&boostselectiondijetM<28)",
        #"El" : "(rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10&&boostselectiondijetM>18&&boostselectiondijetM<28)"

        #"Mu" : "(rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10&&boostselectionZbbM>167&&boostselectionZbbM<265)",
        #"El" : "(rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10&&boostselectionZbbM>167&&boostselectionZbbM<265)"

        #"Mu" : "(rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10&&boostselectiondijetM>72&&boostselectiondijetM<114)",
        #"El" : "(rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10&&boostselectiondijetM>72&&boostselectiondijetM<114)"

        #"Mu" : "(rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10&&boostselectionZbbM>222&&boostselectionZbbM<350)",
        #"El" : "(rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10&&boostselectionZbbM>222&&boostselectionZbbM<350)"

        #"Mu" : "(rc_stage_8_idx&&jetmetMETsignificance<10&&jetmetnj>2)",
        #"El" : "(rc_stage_19_idx&&jetmetMETsignificance<10&&jetmetnj>2)"
        }

    ### selection to the backgrounds ###
    stagesFit = {
        "Mu" : "(rc_stage_8_idx&&jetmetMETsignificance<10)",
        "El" : "(rc_stage_19_idx&&jetmetMETsignificance<10)"
        }

    ### selection to make plots ###
    Stages = {}
    Stages["Zjj"] = {
        "Mu":{"dir":"Muon","cut":"(rc_stage_2_idx&&jetmetnj>1&&jetmetMETsignificance<10&&boostselectionZbbM>0&&boostselectionZbbM<10000&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106)"},
        "El":{"dir":"Electron","cut":"(rc_stage_13_idx&&jetmetnj>1&&jetmetMETsignificance<10&&boostselectionZbbM>0&&boostselectionZbbM<10000&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106)"}
        }

    Stages["Zbb"] = {
        "Mu":{"dir":"Muon","cut":stages["Mu"]},
        "El":{"dir":"Electron","cut":stages["El"]}
        }

    ### Define 2D mapping for the search in the M(bb) - M(llbb) plane ###
    rangeMassA = []
    mbb=10
    #mbb=63
    sigma=1.0
    for i in range(1,36):
    #for i in range(1,20):
      dmbb=0.15*mbb*1.5
      step_mbb = sigma*0.15*mbb
      #step_mbb = 3
      rangeMassA.append([int(mbb-dmbb),int(mbb+dmbb),int(mbb)])
      mbb+=step_mbb

    rangeMassH = []
    mllbb=10
    #mllbb=286-80
    for i in range(1,36):
    #for i in range(1,40):
      dmllbb=0.15*mllbb*1.5
      step_mllbb = dmllbb/1.5
      #step_mllbb = 4
      rangeMassH.append([int(mllbb-dmllbb),int(mllbb+dmllbb),int(mllbb)])
      mllbb+=step_mllbb

    #rangeMassA = [[int(99*0.775),int(99*1.225),int(99)],[int(104*0.775),int(104*1.225),int(104)]]
    #rangeMassH = [[int(263*0.775),int(263*1.225),int(263)],[int(270*0.775),int(270*1.225),int(270)]]

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

    ### define a set of categories ###
    categories = {
        "Mu" : stages["Mu"],
        "El" : stages["El"],
        }

    ### BTAG weight ###
    BTAG = "*btaggingReweightingMM"
    print "BTAG:", BTAG

    ### define reweighting formula ###
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

    ### define rescaling of the backgrounds to the fitted normalisation ###
    wZbb = "( abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 )"+SFlist[SYST]["Zbb"]
    wZbx = "( (abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5) )"+SFlist[SYST]["Zbx"]
    wZxx = "( abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5 )"+SFlist[SYST]["Zxx"]
    wtt = SFlist[SYST]["TT"].replace("*","")
    wdy = "("+wZbb+"+"+wZbx+"+"+wZxx+")"

    ### Uncertainty on the bkg fit ###
    TTBKG =   [1.00, 1.02, 1.00, 0.98]
    ZbbBKG =  [1.00, 0.99, 0.97, 0.99]
    ZbbjBKG = [0.99, 0.98, 1.02, 0.98]
    ZxxBKG =  [1.08, 0.98, 1.00, 0.99]

    ### define output rootfile name for the tree used to fill the datacards ###
    #output llbbYield
    #output = "treeOnlyLoExcess_SYST.root"
    output = "treeV3_SYST.root"
    #output = "treeFineBinningLo_SYST.root"
    #output = "treeErrStat_SYST.root"
    
    ### data options to fill the datacards###
    #data="useToy" #will take data from toys
    #data="sigInj" #will consider bkg+signal as data
    data="" #will use real data
    
    ### name of the directory where the datacards for the limit computation will be written ###
    TRUEYIELDS = False # if False: consider signal yield (ee+mm)=1. ; if True: take the expected number of signal events for a given model

    dirLimits = "/nfs/user/acaudron/"
    if data=="useToy" : dirLimits+="toy"
    else : dirLimits+="unblinded"
    dirLimits+="Datacards2HDM"
    if TRUEYIELDS : dirLimits+="yieldsSignal"
    if data=="sigInj" : dirLimits+="SignalInjec"
    #dirLimits+="MCstatV2/"
    dirLimits+="/"

