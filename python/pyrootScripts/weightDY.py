## PyRoot script to compute the DY merging sample weights from LHE information and to produce some control plots. ##
 
from ROOT import *
import array

### Get the rootfiles where the LHE information is stored: see https://cp3.irmp.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/HtoZAllbbAnalysisTools#ReadingLHEinformation ###
fileAll = TFile("allDY.root") # Rootfiles with all the events from the 7 samples
file = TFile("ptDY.root") # Rootfiles with all events from the 4 exclusive pt(Z) samples and the inclusive sample
fileHT = TFile("HTDY.root") # Rootfiles with all events from the 2 exclusive HT samples
fref = TFile("DYjets.root") # Rootfiles with the inclusive sample events

### Get the trees ###
tree = file.Get("LHEinfos/LHE")
treeHT = fileHT.Get("LHEinfos/LHE")
treeAll = fileAll.Get("LHEinfos/LHE")

### Define the variable bins for each variables ###
listhistos = {
    "ll_pt" : [5, array.array( 'f', [0,50,70,100,180,2500])],
    "HT" : [3, array.array( 'f', [0, 200, 400, 3600])],
    "npartons" : [50, -0.5, 4.5],
    "nc" : [50, -0.5, 4.5],
    "nb" : [50, -0.5, 4.5]
    }

### Define the histgrams ###
histos = {}
for key in ["raw","wpt","href","xsec"]:
    for h in listhistos:
        if len(listhistos[h]) == 3 : histos[key+h] = TH1D(key+h, key+h, listhistos[h][0], listhistos[h][1], listhistos[h][2])
        else : histos[key+h] = TH1D(key+h, key+h, listhistos[h][0], listhistos[h][1])

### Number of entries in the 4 exclusive pt(Z) samples + the inclusive sample ###  
tot1 = tree.GetEntries()
print "entries:", tot1
print "*"*100

### Define the LO MG cross-sections in each pt(Z) bin ###
mapPt = {
    "ll_pt<50"              : 2950   -93.8 -52.31-34.1,
    "ll_pt>=50&&ll_pt<70"   :   93.8                  ,
    "ll_pt>=70&&ll_pt<100"  :   52.31                 ,
    "ll_pt>=100&&ll_pt<180" :   34.1 - 4.56           ,
    "ll_pt>=180"            :    4.56                 ,
    }
for x in mapPt : print x, mapPt[x]
print "*"*100

### Compute fraction of events in each bin (realPt[x]) compare to the expected fraction from MG (truePt[x]) ###
Nx = {}
truePt = {}
realPt = {}
for x in mapPt:
    Nx[x] = tree.Draw("",x)
    truePt[x] = mapPt[x]/2950.
    realPt[x] = float(Nx[x])/tot1
    print x, Nx[x], truePt[x], realPt[x]
print "*"*100

### Fill cross-section histograms with fraction of expected events ###
histos["xsecll_pt"].SetBinContent(1, mapPt["ll_pt<50"])
histos["xsecll_pt"].SetBinContent(2, mapPt["ll_pt>=50&&ll_pt<70"])
histos["xsecll_pt"].SetBinContent(3, mapPt["ll_pt>=70&&ll_pt<100"])
histos["xsecll_pt"].SetBinContent(4, mapPt["ll_pt>=100&&ll_pt<180"])
histos["xsecll_pt"].SetBinContent(5, mapPt["ll_pt>=180"])
histos["xsecll_pt"].Scale(1./histos["xsecll_pt"].Integral())

### Closure test: both test and test2 should be identical ###
test = 0
test2 = 0
for x in mapPt:
    test += Nx[x]
    test2 += (truePt[x]/realPt[x])*Nx[x]
print test, test2
print "*"*100

### Number of events in the 2 exclusive HT samples ###
tot2 = treeHT.GetEntries()
print "entries:", tot2
print "*"*100

### LO MG cross-section in each HT bin ### 
mapHT = {
    "HT<200"          : 2950    -19.73-2.826,
    "HT>=200&&HT<400" :   19.73             ,
    "HT>=400"         :    2.826           
    }
for y in mapHT : print y, mapHT[y]
print "*"*100

### Fill cross-section histograms with fraction of expected events ### 
histos["xsecHT"].SetBinContent(1, mapHT["HT<200"])
histos["xsecHT"].SetBinContent(2, mapHT["HT>=200&&HT<400"])
histos["xsecHT"].SetBinContent(3, mapHT["HT>=400"])
histos["xsecHT"].Scale(1./histos["xsecHT"].Integral())

### Compute weights for the merging ###
Ny = {}
trueHT = {}
realHT = {}
Nall = {}
Nreal = {}
### Run over the HT bins ###
for y in mapHT:
    ### Reading the number of events in this HT bin for the HT samples ###
    Ny[y] = treeHT.Draw("",y)
    ### Run over the pt(Z) bins ###
    for x in mapPt:
        ### Read number of events in this HT and pt(Z) bin reweighted to fit the expected number of events from the LO MG cross-section ###
        Ny[y] += (truePt[x]/realPt[x])*tree.Draw("",x+"&&"+y)
    ### Compute the expected and real fraction of events in this HT and pt(Z) bin for the 7 samples together ###
    trueHT[y] = mapHT[y]/2950.
    realHT[y] = Ny[y]/(tot1+tot2)
    print y, Ny[y], trueHT[y], realHT[y]
    ### Compute final weight ###
    for x in mapPt:
        Nall[x+"&&"+y] = (truePt[x]/realPt[x])*(trueHT[y]/realHT[y])*tree.Draw("",x+"&&"+y) + (trueHT[y]/realHT[y])*treeHT.Draw("",x+"&&"+y) # Number of events after weighting
        Nreal[x+"&&"+y] = tree.Draw("",x+"&&"+y)+treeHT.Draw("",x+"&&"+y) # Pure number of events
        print x+"&&"+y, Nall[x+"&&"+y], Nreal[x+"&&"+y]
print "*"*100

### Print final weights ###
tot = 0
tot_ = 0
for k in Nall:
    tot += Nall[k]
    tot_ += Nreal[k]
    print k, " "*(100-len(k)), Nall[k]/Nreal[k]
print "*"*100

### Closure test ###
print tot1+tot2, tot, tot_
print "*"*100

### Histograms production (quite slow) ###
for h in listhistos:
    c1 = TCanvas("c1","c1")
    int1 = 0
    int2 = 0
    for k in Nall:
        if len(listhistos[h]) == 3 : tmp = TH1D("tmp", "tmp", listhistos[h][0], listhistos[h][1], listhistos[h][2])
        else : tmp = TH1D("tmp", "tmp", listhistos[h][0], listhistos[h][1])        
        treeAll.Draw(h+">>tmp", k)
        tmp.Sumw2()
        int1 += tmp.Integral()
        int2 += tmp.Integral()*(Nall[k]/Nreal[k])
        histos["wpt"+h].Add(tmp, Nall[k]/Nreal[k])
        print Nall[k], Nreal[k], tmp.Integral(), tmp.Integral()*(Nall[k]/Nreal[k])
    print histos["wpt"+h].Integral(), int1, int2
print "*"*100

### Make comparisons ###
c = {}
r = {}
tref = fref.Get("LHEinfos/LHE")
for h in listhistos:
    print h
    c[h] = TCanvas(h,h)

    tmp = TH1D(histos["raw"+h])
    tmp.SetName("tmp")
    tmp.SetTitle("tmp")
    treeAll.Draw(h+">>tmp")
    histos["raw"+h].Add(tmp)

    tmp = TH1D(histos["href"+h])
    tmp.SetName("tmp")
    tmp.SetTitle("tmp")
    tref.Draw(h+">>tmp","","same")
    histos["href"+h].Add(tmp)

    histos["href"+h].Sumw2()
    histos["raw"+h].Sumw2()

    r[h+"DYinc"] = TH1D(histos["href"+h])
    r[h+"DYinc"].SetName(h+"DYinc")
    r[h+"DYinc"].Divide(histos["raw"+h])

    histos["raw"+h].Scale(1./histos["raw"+h].Integral())
    histos["href"+h].Scale(1./histos["href"+h].Integral())
    histos["wpt"+h].Scale(1./histos["wpt"+h].Integral())

    histos["raw"+h].SetLineColor(2)
    histos["wpt"+h].SetLineColor(3)

    histos["raw"+h].Draw()
    histos["wpt"+h].Draw("same")
    histos["href"+h].Draw("same")

    c["ratio"+h] = TCanvas("ratio"+h,"ratio"+h)
    r[h] = TH1D(histos["wpt"+h])
    r[h].SetName(h+"ratio")
    r[h].Divide(histos["xsec"+h])

    r[h+"VsInc"] = TH1D(histos["wpt"+h])
    r[h+"VsInc"].Divide(histos["href"+h])
    r[h+"VsInc"].SetLineColor(4)    

    r[h].Draw("e")
    r[h+"VsInc"].Draw("e,same")
    r[h+"DYinc"].Draw("e,same")
