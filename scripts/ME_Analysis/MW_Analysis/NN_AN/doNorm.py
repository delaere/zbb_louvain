import sys
from UserCode.zbb_louvain.listForRDS import lumi, Extra_norm

list = ["DY125","Zbb125", "TT125", "TT-FullLept125", "ZZ125", "signal125"]

channels  = [
    "EEChannel",
    "MuMuChannel",
    ]

scale = {
    "MuMuChannelDY125" : (lumi["DATA"]/lumi["Zbb"]) * (1./Extra_norm["MuMuChannelZbb"]),
    "EEChannelDY125" : (lumi["DATA"]/lumi["Zbb"]) * (1./Extra_norm["EEChannelZbb"]),
    "MuMuChannelZbb125" : (lumi["DATA"]/lumi["Zbb_Zbb"]) * (1./Extra_norm["MuMuChannelZbb_Zbb"]),
    "EEChannelZbb125" : (lumi["DATA"]/lumi["Zbb_Zbb"]) * (1./Extra_norm["EEChannelZbb_Zbb"]),
    "MuMuChannelTT125" : (lumi["DATA"]/lumi["TT"]) * (1./Extra_norm["MuMuChannelTT"]),
    "EEChannelTT125" : (lumi["DATA"]/lumi["TT"]) * (1./Extra_norm["EEChannelTT"]),
    "MuMuChannelTT-FullLept125" : (lumi["DATA"]/lumi["TT-FullLept"]) * (1./Extra_norm["MuMuChannelTT-FullLept"]),
    "EEChannelTT-FullLept125" : (lumi["DATA"]/lumi["TT-FullLept"]) * (1./Extra_norm["EEChannelTT-FullLept"]),
    "MuMuChannelZZ125" : (lumi["DATA"]/lumi["ZZ"]) * (1./Extra_norm["MuMuChannelZZ"]),
    "EEChannelZZ125" : (lumi["DATA"]/lumi["ZZ"]) * (1./Extra_norm["EEChannelZZ"]),
    "MuMuChannelsignal125" : (lumi["DATA"]/lumi["ZH125"]) * (1./Extra_norm["MuMuChannelZH125"]),
    "EEChannelsignal125" : (lumi["DATA"]/lumi["ZH125"]) * (1./Extra_norm["EEChannelZH125"]),
    }

print "scales : ", scale

from ROOT import TFile, TH1F

fName = sys.argv[1]
f = TFile(fName,"UPDATE")
f.mkdir("MuMuChannel")
f.mkdir("EEChannel")
data=TH1F("data_obs125","data_obs125",28,-0.2,1.2)
dataprod=TH1F("proddata_obs125","proddata_obs125",28,-0.2,1.2)

for c in channels :
    for l in list:
        f.cd()
        h=f.Get(c[:2]+"/"+l)
        p=f.Get(c[:2]+"/"+"prod"+l)
        h.Scale(scale[c+l])
        p.Scale(scale[c+l])
        print h.Integral()
        if l!="signal125" and l!="Zbb125" and l!="TT125":
            data.Add(h)
            dataprod.Add(p)
        f.cd(c);                
        h.Write()
        p.Write()
    f.cd(c);
    data.Write()
    dataprod.Write()
f.Close()

