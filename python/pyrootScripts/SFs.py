
from ROOT import *
from time import strftime
from listForRDS import lumi

def countEvents(files={"test" : "test.root"}):
    events = {}
    #run over all the samples
    for key in files:
        print ""
        strftime("%Y-%m-%d %H:%M:%S")
        print "Run over sample:", key,
        #define stages for which we want to get the number of events
        stages = {
            "zjets" : 0,
            "zb"    : 0,
            "zbb"   : 0,
            "tt"    : 0
            }
        #special case of DY
        if key=="DYjets":
            stagesZbb =  stages = {
                "zjets" : 0,
                "zb"    : 0,
                "zbb"   : 0,
                "tt"    : 0
                }
            stagesZbx =  stages = {
                "zjets" : 0,
                "zb"    : 0,
                "zbb"   : 0,
                "tt"    : 0
                }
            stagesZxx =  stages = {
                "zjets" : 0,
                "zb"    : 0,
                "zbb"   : 0,
                "tt"    : 0
                }
        #open file and get tree
        tf = TFile.Open(files[key])
        tree = tf.Get("rds_zbb")
        #loop over the events
        entries = tree.GetEntries()
        print "Number of entries:", entries
        i = 0
        for event in tree:
            i += 1
            if i % 100000 == 0 : print 100.*i/entries, "%"
            #get the event reweightings for MC
            if key == "DATA":
                w0b = 1.
                w1b = 1.
                w2b = 1.
            else :
                w0b = event.LeptonsReweightingweight * event.lumiReweightingLumiWeight
                w1b = event.BtaggingReweightingM * event.LeptonsReweightingweight * event.lumiReweightingLumiWeight
                w2b = event.BtaggingReweightingMM * event.LeptonsReweightingweight * event.lumiReweightingLumiWeight
            #count events with sepcial case for DY
            if key!="DYjets":
                if event.rc_stage_3_idx and event.jetmetnj>1 and event.jetmetnbP==0 : stages["zjets"]+=w0b
                if event.rc_stage_9_idx and event.jetmetnbP==1 and event.jetmetnj>1 : stages["zb"]+=w1b
                if event.rc_stage_18_idx : stages["zbb"]+=w2b
                if event.rc_stage_15_idx and event.jetmetMETsignificance>10. : stages["tt"]+=w2b
            else :
                if event.rc_stage_3_idx and event.jetmetnj>1 and event.jetmetnbP==0 and abs(event.jetmetjet1Flavor)==5 and abs(event.jetmetjet2Flavor)==5 : stagesZbb["zjets"]+=w0b
                elif event.rc_stage_3_idx and event.jetmetnj>1 and event.jetmetnbP==0 and (abs(event.jetmetjet1Flavor)==5 or abs(event.jetmetjet2Flavor)==5) : stagesZbx["zjets"]+=w0b
                elif event.rc_stage_3_idx and event.jetmetnj>1 and event.jetmetnbP==0 : stagesZxx["zjets"]+=w0b
                if event.rc_stage_9_idx and event.jetmetnbP==1 and event.jetmetnj>1 and abs(event.jetmetbjet1Flavor)==5 and ( (abs(event.jetmetjet1Flavor)==5 and event.jetmetjet1CSVdisc<0.679) or (abs(event.jetmetjet2Flavor)==5 and event.jetmetjet2CSVdisc<0.679) ): stagesZbb["zb"]+=w1b
                elif event.rc_stage_9_idx and event.jetmetnbP==1 and event.jetmetnj>1 and abs(event.jetmetbjet1Flavor)==5: stagesZbx["zb"]+=w1b
                elif event.rc_stage_9_idx and event.jetmetnbP==1 and event.jetmetnj>1 : stagesZxx["zb"]+=w1b
                if abs(event.jetmetbjet1Flavor)==5 and abs(event.jetmetbjet2Flavor)==5:
                    if event.rc_stage_18_idx : stagesZbb["zbb"]+=w2b
                    if event.rc_stage_15_idx and event.jetmetMETsignificance>10. : stagesZbb["tt"]+=w2b
                elif (abs(event.jetmetbjet1Flavor)==5 or abs(event.jetmetbjet2Flavor)==5):
                    if event.rc_stage_18_idx : stagesZbx["zbb"]+=w2b
                    if event.rc_stage_15_idx and event.jetmetMETsignificance>10. : stagesZbx["tt"]+=w2b
                else :
                    if event.rc_stage_18_idx : stagesZxx["zbb"]+=w2b
                    if event.rc_stage_15_idx and event.jetmetMETsignificance>10. : stagesZxx["tt"]+=w2b
        if key=="DYjets":
            for s in stagesZbb :
                stagesZbb[s] *= lumi["DATA"]/lumi["Zbb"]
                stagesZbx[s] *= lumi["DATA"]/lumi["Zbx"]
                stagesZxx[s] *= lumi["DATA"]/lumi["Zxx"]
            events["Zbb"]=stagesZbb
            events["Zbx"]=stagesZbx
            events["Zxx"]=stagesZxx
            print stagesZbb, stagesZbx, stagesZxx
        else :
            if key != "DATA":
                for s in stages : stages[s] *= lumi["DATA"]/lumi[key]
            print stages
            events[key] = stages
    return events

def computeSFs(N1,L1,N2,L2,N3,L3,keys=[]):
    print N1, L1, N2, L2, N3, L3
    SF_A = {
        "const" : N1/L1[0],
        "SF_B" : -L1[1]/L1[0],
        "SF_C" : -L1[2]/L1[0]
        }
    print SF_A

    newL2 = [
        L2[1]+L2[0]*SF_A["SF_B"],
        L2[2]+L2[0]*SF_A["SF_C"]
        ]
    newN2 = N2-L2[0]*SF_A["const"]
    print newL2, L2
    
    SF_B = {
        "const" : newN2/newL2[0],
        "SF_C" : -newL2[1]/newL2[0]
        }

    newSF_A = {
        "const" : SF_A["const"]+SF_A["SF_B"]*SF_B["const"],
        "SF_C" : SF_A["SF_C"]+SF_A["SF_B"]*SF_B["SF_C"]
        }

    SF_C_ = (N3-L3[0]*newSF_A["const"]-L3[1]*SF_B["const"])/(L3[2]+L3[0]*newSF_A["SF_C"]+L3[1]*SF_B["SF_C"])
    SF_A_ = newSF_A["const"]+SF_C_*newSF_A["SF_C"]
    SF_B_ =SF_B["const"]+SF_C_*SF_B["SF_C"]

    print "A", SF_A_
    print "B", SF_B_
    print "C", SF_C_
    SFs = {
        keys[0] : SF_A_,
        keys[1] : SF_B_,
        keys[2] : SF_C_
        }
    return SFs

def main():
    print "Start"
    #sample definition
    dataKey = ["DATA"]
    fixSamples = [
        "ZZ",
        "WW",
        "WZ",
        "Wt",
        "Wtbar",
        "ZH125",
        ]
    fitSamples = ["DYjets"]
    checkSamples = [
        "TTFullLept",
        "TTSemiLept"
        ]
    #files
    files = {}
    path = "/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V33/ControlPlots_NAME/NAME_Summer12_final_skimed_zjets.root"
    for sample in dataKey+fixSamples+fitSamples+checkSamples : files[sample] = path.replace("NAME",sample).replace("DATA","Double2012")
    #get number of events
    print "Get number of events"
    events = countEvents(files)
    print events
    #bkg substraction
    for sample in fixSamples:
        for key in events["DATA"] : events["DATA"][key] -= events[sample][key]
    for sample in checkSamples:
        for key in events["DATA"]:
            if key == "tt" : continue
            events["DATA"][key] -= events[sample][key]
    #define equations
    N1 = events["DATA"]["zjets"]
    L1 = [events["Zbb"]["zjets"], events["Zbx"]["zjets"], events["Zxx"]["zjets"]]
    N2 = events["DATA"]["zb"]
    L2 = [events["Zbb"]["zb"], events["Zbx"]["zb"], events["Zxx"]["zb"]]
    N3 = events["DATA"]["zbb"]
    L3 = [events["Zbb"]["zbb"], events["Zbx"]["zbb"], events["Zxx"]["zbb"]]
    #get SFs
    print "Get SFs"
    SFs = computeSFs(N1,L1,N2,L2,N3,L3,["Zbb","Zbx","Zxx"])
    for sample in ["Zbb","Zbx","Zxx"] : events["DATA"]["tt"] -= events[sample]["tt"]*SFs[sample]
    #check ttbar SFs is 1.
    SFs["tt"] = events["DATA"]["tt"]/(events["TTFullLept"]["tt"]+events["TTSemiLept"]["tt"])
    for key in SFs : print key, SFs[key]

main()
