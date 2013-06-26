from ROOT import *
from zbbCommons import zbbnorm

channels  = [
    "EEChannel",
    "MuMuChannel",
    ]

var = {
    "EEChannel"   : "EEChannel/Cut1/eventSelectionbestzptEle",
    "MuMuChannel" : "MuMuChannel/Cut1/eventSelectionbestzptMu",
    }

list = [
    "DATA",
    "Zb",
    "Zc",
    "Zl",
    "TT",
    "ZZ",
    ]

lumi = { "DATAEEChannel"   : zbbnorm.lumi_totEle2011,
         "DATAMuMuChannel"   : zbbnorm.lumi_totMu2011,
         "TT"     : zbbnorm.nev_TTjets_fall11/zbbnorm.xsec_TTjets_7TeV/1000.,
         "Zb"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "Zc"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "Zl"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "ZZ"     : zbbnorm.nev_ZZ_fall11/zbbnorm.xsec_ZZ_7TeV/1000.,
         }

DataZbRatio = {}
zptRew = {}

for c in channels :
    files = {}
    histos = {}
    
    for l in list :
        files[l]=TFile("ZptNoRew/histoStage16extraCuts"+l+".root","READ")
        histos[l]=files[l].Get(var[c])

    nbins = histos["DATA"].GetNbinsX()
    
    zptRew[c]="("

    for i in range(1,nbins+1):
        x1=histos["DATA"].GetBinLowEdge(i)
        x2=x1+histos["DATA"].GetBinWidth(i)
        DataZbRatio[c]=histos["DATA"].GetBinContent(i)
        for l in list :
            if l=="Zb" or l=="DATA" : continue
            DataZbRatio[c]=DataZbRatio[c]-histos[l].GetBinContent(i)*(lumi["DATA"+c]/lumi[l])
        if histos["Zb"].GetBinContent(i) : DataZbRatio[c]=float(DataZbRatio[c])/(histos["Zb"].GetBinContent(i)*(lumi["DATA"+c]/lumi["Zb"]))
        else : DataZbRatio[c]=0
        if DataZbRatio[c]<0 : DataZbRatio[c]=1.0
        print DataZbRatio[c]
        zptRew[c]+="(@3>="+str(x1)+")*(@3<"+str(x2)+")*"+str(DataZbRatio[c])
        zptRew[c]+="+"
    zptRew[c]+="(@3>="+str(x2)+"))"
    print c, zptRew[c]
