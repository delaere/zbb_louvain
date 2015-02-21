from llbbOptions import *
from ROOT import *
gROOT.SetBatch()

Options = options_()

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

Systs = [
    #"JES",
    #"JER",
    "BTAG_bc_",
    #"BTAG_light_",
    #"LEP"
    ]

for s in Systs:
    print s
    print ""
    for sig in signals:
        nev = {}
        mA = int(sig.split("_")[2])
        mH = int(sig.split("_")[1])
        for cat in Options.categories:
            for i in ["Nominal",s+"up",s+"down"]:
                f = TFile(Options.path.replace("SYST",i).replace("NAME",sig))
                t = f.Get("rds_zbb")
                h = TH1D('MET','MET',100,0,1000)
                t.Draw("jetmetMET>>MET","(boostselectiondijetM>="+str(0.775*mA)+"&&boostselectiondijetM<"+str(1.225*mA)+"&&boostselectionZbbM>="+str(0.775*mH)+"&&boostselectionZbbM<"+str(1.225*mH)+"&&"+Options.Stages["Zbb"][cat]["cut"]+")"+Options.rewForm["Zbb"][cat])
                nev[i] = h.Integral()
                h.Delete()
            unc = 0.5*(nev[s+"up"]-nev[s+"down"])/nev["Nominal"]
            print sig, cat, nev["Nominal"], 100*unc
    print ""
    print ""
    print ""
