
from ROOT import *
from time import strftime
from listForRDS import lumi

class options_:
    histos = {
        "jetmetbjet1SVmass" : [20, 0., 5.],
        "jetmetbjet2SVmass" : [20, 0., 5.],
        "jetmetbjet1CSVdisc" : [20, 0.244, 1.],
        "jetmetbjet2CSVdisc" : [20, 0.244, 1.],
        }

    stage = "rc_stage_36_idx"
    BTAG = {
        "rc_stage_10_idx" : "LL",
        "rc_stage_11_idx" : "LM",
        "rc_stage_12_idx" : "MM",
        "rc_stage_13_idx" : "LL",
        "rc_stage_14_idx" : "LM",
        "rc_stage_15_idx" : "MM",
        "rc_stage_16_idx" : "LL",
        "rc_stage_36_idx" : "LM",
        "rc_stage_18_idx" : "MM",
        }
    SFs = {
        "LL" : {"Zbb" : 1.00, "Zbx" : 1.23, "Zxx" : 1.31, "TT" : 1.02},
        #"LM" : {"Zbb" : 0.97, "Zbx" : 1.08, "Zxx" : 1.44, "TT" : 1.16},
        "LM" : {"Zbb" : 0.96, "Zbx" : 1.08, "Zxx" : 1.46, "TT" : 1.13},
        "MM" : {"Zbb" : 1.08, "Zbx" : 1.14, "Zxx" : 1.24, "TT" : 1.09}
        }

def fillHistos(files={"test" : "test.root"}, options=None):
    if options is None : return
    hists = {}
    #run over all the samples
    for key in files:
        print ""
        strftime("%Y-%m-%d %H:%M:%S")
        print "Run over sample:", key,
        #define stages for which we want to get the number of events
        if key!="DYjets":
            for hname in options.histos : hists[key+hname] = TH1F(key+hname, hname, options.histos[hname][0], options.histos[hname][1], options.histos[hname][2])
        #special case of DY
        else :
            for dy in ["Zbb","Zbx","Zxx"]:
                for hname in options.histos : hists[dy+hname] = TH1F(dy+hname, hname, options.histos[hname][0], options.histos[hname][1], options.histos[hname][2])
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
            passStage = getattr(event, options.stage)
            if not passStage : continue
            if key == "DATA":
                w = 1.
            else :
                wLepPU = event.LeptonsReweightingweight * event.lumiReweightingLumiWeight
                w2b = getattr(event, "BtaggingReweighting"+options.BTAG[options.stage])
                w = w2b*wLepPU
            #count events with sepcial case for DY
            if key!="DYjets":
                if "TT" in key : w *= options.SFs[options.BTAG[options.stage]]["TT"]
                for h in options.histos : hists[key+h].Fill(getattr(event,h),w) 
            else :
                if abs(event.jetmetbjet1Flavor)==5 and abs(event.jetmetbjet2Flavor)==5:
                    if event.jetmetnj>2:
                        w *= options.SFs[options.BTAG[options.stage]]["Zbx"]
                        for h in options.histos : hists["Zbb"+h].Fill(getattr(event,h),w*1.14) 
                    else :
                        w *= options.SFs[options.BTAG[options.stage]]["Zbb"]
                        for h in options.histos : hists["Zbb"+h].Fill(getattr(event,h),w*1.08) 
                elif (abs(event.jetmetbjet1Flavor)==5 or abs(event.jetmetbjet2Flavor)==5):
                    w *= options.SFs[options.BTAG[options.stage]]["Zbx"]
                    for h in options.histos : hists["Zbx"+h].Fill(getattr(event,h),w*1.14) 
                else :
                    w *= options.SFs[options.BTAG[options.stage]]["Zxx"]
                    for h in options.histos : hists["Zxx"+h].Fill(getattr(event,h),w*1.24) 
        if key=="DYjets":
            for dy in ["Zbb","Zbx","Zxx"]:
                for h in options.histos : hists[dy+h].Scale(lumi["DATA"]/lumi[dy])
        else :
            if key != "DATA":
                for h in options.histos : hists[key+h].Scale(lumi["DATA"]/lumi[key])
    return hists


def main():
    print "Start"
    options = options_()
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
    path = "/nfs/user/acaudron/ControlPlots/cp5314p1/ControlPlots_V33/ControlPlots_NAME/NAME_Summer12_final_skimed.root"
    for sample in dataKey+fixSamples+fitSamples+checkSamples : files[sample] = path.replace("NAME",sample).replace("DATA","Double2012")
    #get number of events
    print "Get number of events"
    hists = fillHistos(files, options)
    c_ = {}
    stack = {}
    for hname in options.histos:
        print hname
        c_[hname] = TCanvas(hname,hname,600,600)
        hists["DATA"+hname].Draw("e")
        stack[hname] = THStack(hname,hname)
        for key in hists:
            if not hname in key or "DATA" in key : continue
            print key, hists[key].Integral()
            stack[hname].Add(hists[key])
        stack[hname].Draw("same, hist")
        hists["DATA"+hname].Draw("same,e")
    return (c_, hists, stack)

C = main()
