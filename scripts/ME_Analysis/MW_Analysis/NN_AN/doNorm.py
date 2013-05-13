import sys
from UserCode.zbb_louvain.listForRDS import lumi, Extra_norm

list = ["DY125", "TT125", "ZZ125", "signal125"]

scale = {
    #"DY125" : lumi["DATA"]/lumi["Zbb"],
    "DY125" : (lumi["DATA"]/lumi["Zbb_Zbb"]) * (0.5/Extra_norm["MuMuChannelZbb_Zbb"]+0.5/Extra_norm["EEChannelZbb_Zbb"]),
    "TT125" : (lumi["DATA"]/lumi["TT-FullLept"]) * (0.5/Extra_norm["MuMuChannelTT-FullLept"]+0.5/Extra_norm["EEChannelTT-FullLept"]),
    "ZZ125" : (lumi["DATA"]/lumi["ZZ"]) * (0.5/Extra_norm["MuMuChannelZZ"]+0.5/Extra_norm["EEChannelZZ"]),
    "signal125" : (lumi["DATA"]/lumi["ZH125"]) * (0.5/Extra_norm["MuMuChannelZH125"]+0.5/Extra_norm["EEChannelZH125"]),
    }

print "scales : ", scale

from ROOT import TFile, TH1F

fName = sys.argv[1]
f = TFile(fName,"UPDATE")
f.mkdir("Combined")
data=TH1F("data_obs125","data_obs125",28,-0.2,1.2)
dataprod=TH1F("proddata_obs125","proddata_obs125",28,-0.2,1.2)
for l in list:
    f.cd()
    h=f.Get(l)
    p=f.Get("prod"+l)
    h.Scale(scale[l])
    p.Scale(scale[l])
    print h.Integral()
    data.Add(h)
    dataprod.Add(p)
    f.cd("Combined");                
    h.Write()
    p.Write()
f.cd("Combined");
data.Write()
dataprod.Write()
f.Close()

