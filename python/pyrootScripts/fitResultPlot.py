## Script to add several plot on the same canvas and also add the fit uncertainty ##

from ROOT import *
import math

### function to add a text in a canvas ###
def addtex(c, cat, jet):
    c.cd()
    tex = TLatex();
    tex.SetNDC(); # Important for fixing the coordinate in the canvas between 0 and 1
    tex.SetTextAlign(13);
    tex.SetTextFont(42);
    tex.SetTextSize(0.05);
    tex.SetLineWidth(2);
    
    ### where and which text to add ###
    tex.DrawLatex(0.15,0.955,"category: "+cat+" - "+jet);
    tex.Draw();
    c.Modified()
    return c

### function to add the uncertainty from the background fit ###
def addunc(c,jet):
    c.cd()
    ### Get all objects in the canvas ###
    prim = c.GetListOfPrimitives()
    stack = None
    for p in prim:
        ### Get the stack of MC ###
        if p.InheritsFrom("THStack"):
            stack = p
            break
    ### Get the MC histograms ###
    H = stack.GetHists()
    unc=[]
    ### compute the sum squared of the uncertainty from the different MC ###
    for h in H:
        for b in range(1,h.GetNbinsX()+1):
            if len(unc)<b : unc.append(0)
            if h.GetTitle()=="Z+bb" and jet=="2jets" : unc[b-1]+=h.GetBinContent(b)*0.04/1.16*h.GetBinContent(b)*0.04/1.16
            elif "Z+b" in h.GetTitle() : unc[b-1]+=h.GetBinContent(b)*0.05/1.27*h.GetBinContent(b)*0.05/1.27
            elif h.GetTitle()=="Z+xx" : unc[b-1]+=h.GetBinContent(b)*0.10/1.27*h.GetBinContent(b)*0.10/1.27
            elif "t#bar{t}" in h.GetTitle() : unc[b-1]+=h.GetBinContent(b)*0.03/1.04*h.GetBinContent(b)*0.03/1.04
    g = TGraphErrors(h.GetNbinsX())
    ### Get sum of the MC ###
    mc = stack.GetStack().Last()
    ### a graph with point with mean value=sum MC and unc.=unc. from the fit computed above ###
    for b in range(1,mc.GetNbinsX()+1):
        g.SetPoint(b-1,mc.GetBinCenter(b),mc.GetBinContent(b))
        g.SetPointError(b-1,mc.GetBinWidth(b)/2.,math.sqrt(unc[b-1]))
    g.SetFillColor(1)
    g.SetFillStyle(3001)
    ### Add the unc. band ###
    g.Draw("E2,same")
    return (c,g)
f = {}

### Get files ###
f["2j"] = TFile("Zbb_Rew_ZbblowMET_largeMll_RewFormformulaPol3_nj2_NotNorm_testRew.root")
f["3j"] = TFile("Zbb_Rew_ZbblowMET_largeMll_RewFormformulaPol3_nj3_NotNorm_testRew.root")

c = {}
### load DrawCanvas for the style ###
gSystem.Load("DrawCanvas_C.so")

it = 0
for fkey in f:
    for ckey in ["Electron","Muon"]:
        for pkey in ["CSVprod","boostselectionbestzmass"+ckey.replace("ctron","").replace("on","")]:
            ### choice of the strings specific to each categories ###
            if "El" in ckey : cat = "ee"
            else : cat = "#mu#mu"
            if "2" in fkey : jet = "2jets"
            else : jet = ">2jets" 
            ### Get the canvas ###
            ctmp = f[fkey].Get(ckey+"/"+pkey)
            ### remake it with proper style ###
            DrawCanvas(ctmp,11)
            ### Add additional text ###
            ctmp=addtex(ctmp, cat, jet)
            ### Add unc. band ###
            (ctmp,g)=addunc(ctmp, jet)
            c[fkey+ckey+pkey] = ctmp.Clone()
            for obj in c[fkey+ckey+pkey].GetListOfPrimitives():
                if obj.InheritsFrom("THStack"):
                    H = obj.GetHists()
                    if not H : continue
                    print H
                    for h in H : 
                        h.SetName(pkey+ckey+fkey+str(it))
                        it +=1
                if obj.GetName()==ctmp.GetName() : obj.SetName(pkey+ckey+fkey+str(it))
                it+=1
            c[fkey+ckey+pkey].SetName(pkey+ckey+fkey)

### Make final canvas ###
can = TCanvas("fitResult", "CANVAS",243,68,1580,972)
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
can.Divide(4,2)
i = 1

### canvas in the order to be plotted ##
lc = [
    "2jElectronboostselectionbestzmassEle",
    "2jElectronCSVprod",
    "3jElectronboostselectionbestzmassEle",
    "3jElectronCSVprod",
    "2jMuonboostselectionbestzmassMu",
    "2jMuonCSVprod",
    "3jMuonboostselectionbestzmassMu",
    "3jMuonCSVprod",
]

### Draw individual canvases in the big one ###
for key in lc:
    print key
    can.cd(i)
    c[key].DrawClonePad()
    i+=1

