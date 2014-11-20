from ROOT import *
import array

file = "/home/fynu/mvidal/scratch/Limits_HH/CMSSW_6_1_1/src/HiggsAnalysis/CombinedLimit/data/hh-bbww/NO-systematics/higgsCombineHHbbWW.Asymptotic.NoSys.root"

f=TFile(file)

tree = f.Get("limit")

entries = tree.GetEntriesFast()


print "number of entries = ", entries

TG = {}
TGAS = {}
expectedList = {}


expectList = [-1,
              0.975,
              0.84,
              0.5,
              0.16,
              0.025]

LambdaBin = { -1:1,
  0:2,
  1:3,
  2:4,
  10:5,
}
LambdaHypoList = [-1,0,1,2,10]

limits = [0,0,0,0,0]

TG = TGraph(0)    
for sigmas in ["1sigma","2sigma"]:
    TGAS[sigmas] = TGraphAsymmErrors(0)
    
for jentry in xrange(entries) :
    # get the next tree in the chain and verify
    ientry = tree.LoadTree( jentry )
    if ientry < 0: bla
    
    # copy next entry into memory and verify
    nb = tree.GetEntry( jentry )
    if nb <= 0: continue

    bin=LambdaBin[tree.mh]

    #print "going to loop over jets"

    print "limit saved, limit = ", tree.limit
    print "            expect = ", tree.quantileExpected
    print "                mh = ", tree.mh

    if abs(tree.quantileExpected - 0.5) < 0.01:
	TGAS["1sigma"].SetPoint(bin-1,tree.mh,tree.limit)
        TGAS["2sigma"].SetPoint(bin-1,tree.mh,tree.limit)
	TG.SetPoint(bin-1,tree.mh,tree.limit)
	print "0.5 filled"
        limits[bin-1] = tree.limit

for jentry in xrange(entries) :
    # get the next tree in the chain and verify
    ientry = tree.LoadTree( jentry )
    if ientry < 0: bla

    # copy next entry into memory and verify
    nb = tree.GetEntry( jentry )
    if nb <= 0: continue

    bin=LambdaBin[tree.mh]

    if abs(tree.quantileExpected - 0.975) < 0.01:
	TGAS["2sigma"].SetPointEYhigh(bin-1,abs(limits[bin-1]-tree.limit))
        print "0.975 filled"


    elif abs(tree.quantileExpected - 0.025) < 0.01:
        TGAS["2sigma"].SetPointEYlow(bin-1,abs(limits[bin-1]-tree.limit))
        print "0.025 filled"

    elif abs(tree.quantileExpected - 0.84) < 0.01:
        TGAS["1sigma"].SetPointEYhigh(bin-1,abs(limits[bin-1]-tree.limit))
        print "0.84 filled"


    elif abs(tree.quantileExpected - 0.16) < 0.01:
        TGAS["1sigma"].SetPointEYlow(bin-1,abs(limits[bin-1]-tree.limit))
        print "0.16 filled"


gStyle.SetOptTitle(0)

TGAS["2sigma"].SetFillColor(kYellow)
TGAS["2sigma"].SetFillStyle(1001)
TGAS["2sigma"].GetYaxis().SetTitle("95% Asymptotic CL Limit on ???")
TGAS["2sigma"].GetYaxis().SetTitleSize(0.045)
TGAS["2sigma"].GetYaxis().SetTitleOffset(0.7)
#TGAS["2sigma"].GetYaxis().SetRangeUser(0,(myTH1_cls[str(0.5)].GetBinContent(5)+TGAS["2sigma"].GetErrorYhigh(4))*1.5)
#TGAS["2sigma"].GetYaxis().SetRangeUser(0,40)
TGAS["2sigma"].GetXaxis().SetTitle("#Lambda")
TGAS["2sigma"].GetXaxis().SetTitleSize(0.045)
TGAS["2sigma"].GetXaxis().SetTitleOffset(0.8)
TGAS["2sigma"].Draw('A E3')
TGAS["1sigma"].SetFillColor(kGreen)
TGAS["1sigma"].SetFillStyle(1001)
TGAS["1sigma"].Draw('E3 SAME')


TG.Draw("L*")

#C = TCanvas("C","C",1200,500)




'''
#lat = TLatex(0.12,0.75,"#splitline{#splitline{#splitline{CMS internal}{#sqrt{s} = 7 TeV, L = 5.0 fb^{-1}} }{#sqrt{s} = 8 TeV, L = 19.6 fb^{-1}} }{Z(ll)H(bb), l=e, #mu}")
lat = TLatex(0.12,0.75,"#splitline{#splitline{CMS internal}{#sqrt{s} = 8 TeV, L = 19.6 fb^{-1}} }{Z(ll)H(bb), "+cat+"}")
lat.SetNDC()
lat.Draw()
'''

leg = TLegend(0.59,0.68,0.89,0.88)
leg.SetLineColor(0)
leg.SetFillColor(0)
leg.AddEntry(TGAS["1sigma"],"CL_{s} Expected #pm 1 #sigma","F")
leg.AddEntry(TGAS["2sigma"],"CL_{s} Expected #pm 2 #sigma","F")
leg.AddEntry(TG,"CL_{s} Expected","L")
leg.Draw()

##################
### The END :( ###
##################
                                                                  
