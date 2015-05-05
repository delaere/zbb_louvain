from ROOT import *

f = TFile("../../test/Zbb_Rew_ZbblowMET_smallMll_RewFormformulaPol3_MH662_NotNorm_testRew.root")

#canvas = f.Get("Combined/boostselectionZbbM")
canvas = f.Get("Combined/boostselectiondijetM")

data = None
mc = None
for p in canvas.GetListOfPrimitives():
    if p.GetName()==canvas.GetName():
        if mc is None and p.InheritsFrom("THStack") : mc = p.GetStack().Last()
        if data is None and p.InheritsFrom("TH1") : data = p
    if data is not None and mc is not None : break

data.Add(mc, -1)
data.Rebin(2)
c = TCanvas()
data.Draw()



        
