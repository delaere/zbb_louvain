from ROOT import *
from zbbCommons import zbbnorm

channels  = [
    "EEChannel",
    "MuMuChannel",
    ]

var = {
    "EEChannel"   : "EEChannel/Cut2/eventSelectionbestzptEle",
    "MuMuChannel" : "MuMuChannel/Cut2/eventSelectionbestzptMu",
    }

list = [
        "DATA",
        "Zbb",
        "Zbx",
        "Zxx",
        "TT-FullLept",
        "ZZ",
        ]

from listForRDS import lumi

DataZbRatio = {}
zptRew = {}

for c in channels :
    files = {}
    histos = {}
    
    for l in list :
        files[l]=TFile("~acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/python/hist_cuts_fullleptTTbar_norm_zpt2/histoStage18extraCuts"+l+".root","READ")
        histos[l]=files[l].Get(var[c])

    nbins = histos["DATA"].GetNbinsX()
    
    zptRew[c]="("

    for i in range(1,nbins+1):
        x1=histos["DATA"].GetBinLowEdge(i)
        x2=x1+histos["DATA"].GetBinWidth(i)
        DataZbRatio[c]=histos["DATA"].GetBinContent(i)
        for l in list :
            if l=="Zbx" or l=="Zbb" or l=="DATA" : continue
            DataZbRatio[c]=DataZbRatio[c]-histos[l].GetBinContent(i)*(lumi["DATA"]/lumi[l])
        if (histos["Zbb"].GetBinContent(i)+histos["Zbx"].GetBinContent(i))>0 : DataZbRatio[c]=float(DataZbRatio[c])/(histos["Zbb"].GetBinContent(i)*(lumi["DATA"]/lumi["Zbb"])+histos["Zbx"].GetBinContent(i)*(lumi["DATA"]/lumi["Zbx"]))
        else : DataZbRatio[c]=0
        if DataZbRatio[c]<0 : DataZbRatio[c]=1.0
        print DataZbRatio[c]
        zptRew[c]+="(@3>="+str(x1)+")*(@3<"+str(x2)+")*"+str(DataZbRatio[c])
        zptRew[c]+="+"
    zptRew[c]+="(@3>="+str(x2)+"))"
    print c, zptRew[c]
