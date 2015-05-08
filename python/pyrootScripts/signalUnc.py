## This script allow to check the systematic unc. for different signal hypotheses ##

from llbbOptions import *
from ROOT import *
gROOT.SetBatch()

Options = options_()

### List of available signal ###
signals = [
    "ZA_142_35",
    "ZA_200_50",
    "ZA_200_90",
    "ZA_329_30",
    "ZA_329_70",
    "ZA_329_142",
    "ZA_575_70",
    "ZA_575_142",
    "ZA_575_378",
    "ZA_875_70",
    "ZA_875_142",
    "ZA_875_378",
    "ZA_875_575",
    "ZA_875_761",]

### List of systematics to test ###
Systs = [
    "JES",
    "JER",
    "BTAG_bc_",
    "BTAG_light_",
    "LEP"
    ]

### run over the syst. ###
for s in Systs:
    print s
    print ""
    for sig in signals:
        nev = {}
        ### Get M(bb) and M(llbb)
        mA = int(sig.split("_")[2])
        mH = int(sig.split("_")[1])
        for cat in Options.categories:
            ### Get Nominal and +-1 deviations ###
            for i in ["Nominal",s+"up",s+"down"]:
                f = TFile(Options.path.replace("SYST",i).replace("NAME",sig))
                t = f.Get("rds_zbb")
                h = TH1D('MET','MET',100,0,1000)
                ### got in a window defined in the same way as the bin used for the limit: +-1.5 s.d. with 1.s.d.=15% ###
                t.Draw("jetmetMET>>MET","(boostselectiondijetM>="+str(0.775*mA)+"&&boostselectiondijetM<"+str(1.225*mA)+"&&boostselectionZbbM>="+str(0.775*mH)+"&&boostselectionZbbM<"+str(1.225*mH)+"&&"+Options.Stages["Zbb"][cat]["cut"]+")"+Options.rewForm["Zbb"][cat])
                nev[i] = h.Integral()
                h.Delete()
            ### Compute the unc. and print it ###
            unc = 0.5*(nev[s+"up"]-nev[s+"down"])/nev["Nominal"]
            print sig, cat, nev["Nominal"], 100*unc
    print ""
    print ""
    print ""
