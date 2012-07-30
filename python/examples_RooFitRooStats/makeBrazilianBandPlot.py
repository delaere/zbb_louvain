from ROOT import *

f=TFile("higgsCombineTest.Asymptotic.root")

tree = f.Get("limit")
entries = tree.GetEntriesFast()

print "number of entries = ", entries

myTH1_cls = {}
expectedList = {}
g_cls={}

mhHypoList = [115,120,125,130,135]
expectList = [-1,
              0.975,
              0.84,
              0.5,
              0.16,
              0.025]

mhBin = {115:1,
         120:2,
         125:3,
         130:4,
         135:5}

for expects in expectList:
    myTH1_cls[str(expects)] = TH1F("TH1_"+str(expects),"TH1_"+str(expects),
                                   len(mhHypoList),
                                   min(mhHypoList)-3.,
                                   max(mhHypoList)+3.)
    
for jentry in xrange(entries) :
    # get the next tree in the chain and verify
    ientry = tree.LoadTree( jentry )
    if ientry < 0: bla
    
    # copy next entry into memory and verify
    nb = tree.GetEntry( jentry )
    if nb <= 0: continue

    #print "going to loop over jets"
    for expects in expectList:
        if 0.99*abs(expects) < abs(tree.quantileExpected) < 1.01*abs(expects) :
            print "BIN = ", mhBin[tree.mh]
            myTH1_cls[str(expects)].SetBinContent(mhBin[tree.mh], tree.limit)
            print "limit saved, limit = ", tree.limit
            print "            expect = ", tree.quantileExpected
            print "                mh = ", tree.mh

for expects in expectList:
    g_cls[expects] = TGraph(myTH1_cls[str(expects)])
    
    g_cls[expects].GetYaxis().SetTitle("#sigma(Z[ll]+H[bb])_{95%CL}/#sigma(Z[ll]+H[bb])_{SM}, l=e,#mu")
    g_cls[expects].GetXaxis().SetTitle("m_{H} (GeV/c^{2})")
    g_cls[expects].SetMaximum(30.)
    g_cls[expects].SetMinimum(0.00001)
    
    g_cls[expects].GetXaxis().SetRange(min(mhHypoList),max(mhHypoList))
    
C = TCanvas("C","C",1200,500)

g_cls[-1].Draw("AC")

for expects in expectList: myTH1_cls[str(expects)].Draw("AC,same")

myTH1_cls["0.975"].SetFillColor(kYellow)
myTH1_cls["0.84"].SetFillColor(kGreen)
myTH1_cls["0.16"].SetFillColor(kYellow)
myTH1_cls["0.025"].SetFillColor(1001)

myTH1_cls["-1"].SetLineWidth(3)
myTH1_cls["-1"].Draw("AC*,same")

##################
### THE END :( ###
##################
                                                                  
