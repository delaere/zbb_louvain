## Script to mae data-MC from CPs ##

from ROOT import *

### Get file with the CPs ###
f = TFile("Zbb_Rew_ZbblowMET_smallMll_RewFormformulaPol3_MA93_NotNorm_testRew_signalH262A99.root")

### Get plot ###
canvas = f.Get("Combined/boostselectionZbbM")

data = None
mc = None
for p in canvas.GetListOfPrimitives():
    if p.GetName()==canvas.GetName():
        ### get bkg=MC-signal ###
        if mc is None and p.InheritsFrom("THStack") : 
            mc = p.GetStack().Last()
            sig = p.GetStack().Before(mc)
            sig.Add(mc,-1)
            sig.Scale(-1)
            mc.Add(sig,-1)
            print sig.Integral(), mc.Integral()
         ### get data ###   
        if data is None and p.InheritsFrom("TH1") : data = p
    if data is not None and mc is not None : break

### data-bkg
data.Add(mc, -1)
c = TCanvas()
data.Draw()
sig.Draw("same HIST")
