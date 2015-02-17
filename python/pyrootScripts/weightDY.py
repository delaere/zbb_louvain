
from ROOT import *

file = TFile("allDY.root")
fref = TFile("DYjets.root")

tree = file.Get("LHEinfos/LHE")

listhistos = ["ll_pt","HT","npatons","nc","nb"]
histos = {}
for key in ["raw","wpt","wht"]:
    for h in listhistos:
        histos[key+h] = TH1F(key+h, key+h, 100, 0, 2000)
        histos[key+h] = TH1F(key+h, key+h, 100, 0, 2000)
        histos[key+h] = TH1F(key+h, key+h, 100, 0, 2000)

Pt = [50, 70, 100, 180]
mapPt = {
    "50" : (2950-93.8-52.31-34.1)/29873200.,
    "70" : 93.8/6631666,
    "100" : 52.31/2915877,
    "180" : (34.1-4.56)/4079351,
    "inf": 4.56/3014942,
    }

HT = [200, 400]
mapHT = {
    "200" : 0.,
    "400" : 0.,
    "inf" : 0.
    }

mapHT2 = {
    "200" : (2950-19.73-2.826)/2776.6,
    "400" : 19.73/130.9,
    "inf" : 2.826/42.5
    }

print "entries:", tree.GetEntries()
i = 0
for event in tree:
    i += 1
    if i%1000000==0 : print i
    if i%100==0 : break
    w = 1.
    inf = True
    for pt in Pt:
        if event.ll_pt < pt:
            w = mapPt[str(pt)]
            inf = False
            break
    if inf : w = mapPt["inf"]
    wptllpt.Fill(event.ll_pt, w)

    infHT = True
    wht = 1.
    for ht in HT:
        if event.HT < ht:
            mapHT[str(ht)] += w
            wht = mapHT2[str(ht)]
            infHT = False
            break
    if infHT:
        mapHT["inf"] += w
        wht = mapHT2["inf"]
    whtllpt.Fill(event.ll_pt, w*wht)
    continue

for key in mapHT : print key, ": ", mapHT[key]

tree.Draw("ll_pt>>rawll_pt")
tref = fref.Get("LHEinfos/LHE")
tref.Draw("ll_pt>>href","","same")
rawllpt.Scale(1./rawllpt.Integral())
href.Scale(1./href.Integral())
wptllpt.Scale(1./wptllpt.Integral())
whtllpt.Scale(1./whtllpt.Integral())
rawllpt.SetLineColor(2)
wptllpt.SetLineColor(3)
whtllpt.SetLineColor(4)
rawllpt.Draw()
wptllpt.Draw("same")
whtllpt.Draw("same")
href.Draw("same")

ratio = TCanvas("ratio","ratio")
r = TH1F(whtllpt)
r.Divide(href)
r.Draw()
