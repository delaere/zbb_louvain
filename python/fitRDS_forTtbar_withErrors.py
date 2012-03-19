from ROOT import *

WP       = "HEHE"        #"HP","HPMET","HP_excl","HE","HEMET","HE_excl"
channel  = "El"
PVreduce = 0

sel= {"Mu":"muSel",
      "El":"elSel"}

TtbarMC = "Ttbar_"+channel+"_MC"
Data    = channel+"_DATA"
DYMC    = channel+"_MC"

keys = False

file = {}

if   channel == "El" :
    file[DYMC]    = TFile("File_rds_zbb_El_MC.root")
    file[Data]    = TFile("File_rds_zbb_El_DATA.root")
    file[TtbarMC] = TFile("File_rds_zbb_Ttbar_El_MC.root")
elif channel == "Mu" :
    file[DYMC] = TFile("File_rds_zbb_Mu_MC.root")
    file[Data] = TFile("File_rds_zbb_Mu_DATA.root")
    file[TtbarMC] = TFile("File_rds_zbb_Ttbar_El_MC.root")

#file = {  Data    : TFile("File_rds_zbb_"+Data+"_"+sel[channel]+"_forTtbar.root"),
#          DYMC    : TFile("File_rds_zbb_"+DYMC+"_"+sel[channel]+"_forTtbar.root"),
#          TtbarMC : TFile("File_rds_zbb_"+TtbarMC+"_"+sel[channel]+"_forTtbar.root")
#          }

ws={}         
ws[Data]    = file[Data].Get("ws")
ws[DYMC]    = file[DYMC].Get("ws")
ws[TtbarMC] = file[TtbarMC].Get("ws")

myRDS ={}
myRDS[Data]    = ws[Data].data("rds_zbb")
myRDS[DYMC]    = ws[DYMC].data("rds_zbb")
myRDS[TtbarMC] = ws[TtbarMC].data("rds_zbb")

#myRDS[DYMC]    = myRDS[DYMC].reduce("rc_"+WP+"==1")
#myRDS[TtbarMC] = myRDS[TtbarMC].reduce("rc_"+WP+"==1")
#DATA=myRDS[Data].reduce("rc_"+WP+"==1")

if channel == "Mu" :
    myRDS[TtbarMC] = myRDS[TtbarMC].reduce("eventSelectionbestzmassMu<120&eventSelectionbestzmassMu>60")
    myRDS[DYMC]    = myRDS[DYMC].reduce("eventSelectionbestzmassMu<120&eventSelectionbestzmassMu>60")
    myRDS[Data]    = myRDS[Data].reduce("eventSelectionbestzmassMu<120&eventSelectionbestzmassMu>60")
elif channel == "El" :
    myRDS[TtbarMC] = myRDS[TtbarMC].reduce("eventSelectionbestzmassEle<120&eventSelectionbestzmassEle>60")
    myRDS[DYMC]    = myRDS[DYMC].reduce("eventSelectionbestzmassEle<120&eventSelectionbestzmassEle>60")
    myRDS[Data]    = myRDS[Data].reduce("eventSelectionbestzmassEle<120&eventSelectionbestzmassEle>60")


if PVreduce == 1: DATA = DATA.reduce("rrv_nPV<4.5")
if PVreduce == 2:
    DATA = DATA.reduce("rrv_nPV>4.5")
    DATA = DATA.reduce("rrv_nPV<7.5")
if PVreduce == 3: DATA = DATA.reduce("rrv_nPV>7.5")

if WP == "HEHE":
    myRDS[TtbarMC] = myRDS[TtbarMC].reduce("rc_eventSelection_9==1&jetmetMET<50")
    myRDS[DYMC] = myRDS[DYMC].reduce("rc_eventSelection_9==1&jetmetMET<50")
    DATA   = myRDS[Data].reduce("rc_eventSelection_9==1&jetmetMET<50")
elif WP == "HPHP":
    myRDS[TtbarMC] = myRDS[TtbarMC].reduce("rc_eventSelection_11==1&jetmetMET<50")
    myRDS[DYMC] = myRDS[DYMC].reduce("rc_eventSelection_11==1&jetmetMET<50")
    DATA   = myRDS[Data].reduce("rc_eventSelection_11==1&jetmetMET<50")
                                

print "DATA("+WP+").numEntries() = ", DATA.numEntries()

print "myRDS[\"Ttbar_Mu_MC\"].numEntries() = ", myRDS[TtbarMC].numEntries()
print "myRDS[\"Mu_MC\"].numEntries() = ", myRDS[DYMC].numEntries()
print "myRDS[\"Mu_DATA\"].numEntries() = ", myRDS[Data].numEntries()

rrv_ll_M    = ws[Data].var("rrv_ll_M")

if channel=="El": rrv_ll_M    = ws[Data].var("eventSelectionbestzmassEle")
if channel=="Mu": rrv_ll_M    = ws[Data].var("eventSelectionbestzmassMu")

#rrv_HE      = ws["Mu_DATA"].var("rc_HE")
#rrv_HP      = ws["Mu_DATA"].var("rc_HP")
#rrv_HEMET   = ws["Mu_DATA"].var("rc_HEMET")
#rrv_HPMET   = ws["Mu_DATA"].var("rc_HPMET")


myRDH = {}
myRHP = {}

rrv_ll_M.setMin( 60)
rrv_ll_M.setMax(120)
rrv_ll_M.setBins(15)
rrv_ll_M.SetTitle("m(l^{+}l^{-})")
if channel=="Mu": rrv_ll_M.SetTitle("m(#mu^{+}#mu^{-})")
if channel=="El": rrv_ll_M.SetTitle("m(e^{+}e^{-})")
rrv_ll_M.setUnit("GeV/c^{2}")


if keys:
    myRHP[DYMC]     = RooKeysPdf( "myRHP_DYMC",    "myRHP_DYMC",      rrv_ll_M, myRDS[DYMC]    , kFALSE, 0.3 )
    #myRHP[TtbarMC]  = RooKeysPdf( "myRHP_TtbarMC", "myRHP_TtbarMC",  rrv_ll_M, myRDS[TtbarMC]   )
    c = RooRealVar("c","c",-1.,1)
    myRHP[TtbarMC]  = RooExponential( "myRHP_TtbarMC", "myRHP_TtbarMC", rrv_ll_M, c  )
else:
    myRDH[DYMC]      = RooDataHist("myRDH_DYMC",    "myRDH_DYMC",     RooArgSet(rrv_ll_M), myRDS[DYMC]  )
    myRHP[DYMC]      = RooHistPdf( "myRHP_DYMC",    "myRHP_DYMC",     RooArgSet(rrv_ll_M), myRDH[DYMC]  )
    myRDH[TtbarMC]   = RooDataHist("myRDH_TtbarMC", "myRDH_TtbarMC",  RooArgSet(rrv_ll_M), myRDS[TtbarMC]  )
    myRHP[TtbarMC]   = RooHistPdf( "myRHP_TtbarMC", "myRHP_TtbarMC",  RooArgSet(rrv_ll_M), myRDH[TtbarMC]  )


################# with error

nbins  = rrv_ll_M.getBins()
xMin   = rrv_ll_M.getMin()
xMax   = rrv_ll_M.getMax()
xRange = xMax-xMin

limitsArray = TArrayD(nbins+1)

for i in range(0,nbins+1):
    limit_i = xMin+i*xRange/nbins
    print "limit_i = ", limit_i
    limitsArray.SetAt(limit_i,i)
    
list = RooArgList("list")
binHeight = {}

for i in range(0,nbins-1):
    rrv_ll_M.setVal(xMin+i*(xRange/nbins))
    binH = myRHP[TtbarMC].getVal(RooArgSet(rrv_ll_M))
    print "bin height = ", binH

    binHeight[i] = RooRealVar("binHeight_"+str(i),"bin "+str(i)+" value",
                              binH, binH*0.7, binH*1.1 )
    print "adding binheight number ", i
    list.add(binHeight[i]) # up to binHeight8, ie. 9 parameters

myRHP[TtbarMC] = RooParametricStepFunction(myRHP[TtbarMC].GetName(),myRHP[TtbarMC].GetTitle(),
                                           rrv_ll_M,
                                           list,
                                           limitsArray,
                                           nbins)

cat = RooCategory("cat","cat")
cat.defineType("MC")
cat.defineType("data")

cat.setLabel("MC")
myRDS[TtbarMC].addColumn(cat)
cat.setLabel("data")
DATA.addColumn(cat)

frac_DY = RooRealVar("frac_DY","frac_DY",0.80,0,1)

totPdf = RooAddPdf("totPdf","totPdf",RooArgList(myRHP[DYMC],myRHP[TtbarMC]),RooArgList(frac_DY))

simPdf = RooSimultaneous("sim","sim",cat)
simPdf.addPdf(myRHP[TtbarMC],"MC")
simPdf.addPdf(totPdf,"data")

dataPlusMC = RooDataSet("dataPlusMC","dataPlusMC",DATA,RooArgSet(rrv_ll_M,cat))

dataPlusMC.append(myRDS[TtbarMC])

rrv_ll_M.setRange("r",60,120)
r=simPdf.fitTo(dataPlusMC,RooFit.Save())

rrv_ll_M.setRange("r",60,120)
rrv_ll_M.setRange("sig",60,120)

sigArea=myRHP[TtbarMC].createIntegral(RooArgSet(rrv_ll_M),"sig") 
totArea=myRHP[TtbarMC].createIntegral(RooArgSet(rrv_ll_M),"r")

frac_in_sig_range = RooConstVar("frac_in_sig_range","frac_in_sig_range",sigArea.getVal()/totArea.getVal())

print "FRAC IN SIG RANGE", frac_in_sig_range.getVal()




#N_ttbar_in_sig_range = RooRealVar("N_{tt} (60-120)","N_{tt} (60-120)",
#                                  0.20*DATA.numEntries(),
#                                  0.00*DATA.numEntries(),
#                                  1.10*DATA.numEntries())
#N_ttbar = RooFormulaVar("N_ttbar","N_ttbar","@0/@1",RooArgList(N_ttbar_in_sig_range,frac_in_sig_range))
N_ttbar = RooRealVar("N_{tt} (60-200)","N_{tt} (60-200)",
                                  0.20*DATA.numEntries(),
                                  0.00*DATA.numEntries(),
                                  1.10*DATA.numEntries())
N_ll = RooRealVar("N_{ll}","N_{ll}",
                     0.81*DATA.numEntries(),
                     0.00*DATA.numEntries(),
                     1.20*DATA.numEntries())

sumPdf = RooAddPdf("sumPdf","sumPdf",
                   RooArgList(myRHP[TtbarMC],myRHP[DYMC]),
                   RooArgList(N_ttbar,N_ll))

sumPdf2 = RooAddPdf("sumPdf2","sumPdf2",
                   RooArgList(myRHP[DYMC],myRHP[TtbarMC]),
                   RooArgList(frac_DY))

gROOT.SetStyle("Plain")
gStyle.SetErrorX(0)

C=TCanvas("C","C",1200,400)
C.Divide(3)

#sumPdf.fitTo(DATA,RooFit.Extended(),RooFit.Range("r"))

C.cd(1)
frame1 = rrv_ll_M.frame()
frame1.SetBarWidth(0.)
frame1.SetMarkerSize(1.3)
frame1.SetLineWidth(1)
myRDS[TtbarMC].plotOn(frame1,
            RooFit.MarkerSize(1.3),
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
myRHP[TtbarMC].plotOn(frame1,
                      RooFit.LineWidth(1),
                      RooFit.LineColor(kBlack))

myRHP[TtbarMC].plotOn(frame1,RooFit.VisualizeError(r,2),RooFit.FillColor(kGray+1))
myRHP[TtbarMC].plotOn(frame1,RooFit.VisualizeError(r,1),RooFit.FillColor(kGray))
myRHP[TtbarMC].plotOn(frame1,RooFit.LineColor(kBlack))
myRDS[TtbarMC].plotOn(frame1,RooFit.MarkerSize(1.3),
                      RooFit.XErrorSize(0.035),
                      RooFit.DrawOption("pe2"))
#myRHP[TtbarMC].paramOn(frame1,myRDS[TtbarMC])
frame1.Draw()

#sumPdf2.fitTo(DATA,RooFit.Range("r"))

C.cd(2)
frame2 = rrv_ll_M.frame()
frame2.SetBarWidth(0.)
frame2.SetMarkerSize(1.3)
frame2.SetLineWidth(1)
DATA.plotOn(frame2,
            RooFit.MarkerSize(1.3),
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
totPdf.plotOn(frame2,
              RooFit.FillColor(kBlue-7),
              RooFit.Components("myRHP_TtbarMC,myRHP_DYMC"),
              RooFit.DrawOption("F"),
              RooFit.LineColor(kBlack),
              RooFit.LineWidth(1))
totPdf.plotOn(frame2,
              RooFit.FillColor(kBlue-7),
              RooFit.Components("myRHP_TtbarMC,myRHP_DYMC"),
              RooFit.LineColor(kBlack),
              RooFit.LineWidth(1))
totPdf.plotOn(frame2,
              RooFit.Components("myRHP_TtbarMC"),
              RooFit.LineColor(kBlack),
              RooFit.FillColor(kYellow-7),
              RooFit.DrawOption("F"),
              RooFit.LineWidth(1))
totPdf.plotOn(frame2,
              RooFit.Components("myRHP_TtbarMC"),
              RooFit.LineColor(kBlack),
              RooFit.FillColor(kYellow-7),
              RooFit.LineWidth(1))
DATA.plotOn(frame2,
            RooFit.MarkerSize(1.3),
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
frame2.Draw()

C.cd(3)
frame3 = rrv_ll_M.frame()
totPdf.paramOn(frame3,DATA)
frame3.Draw()

bla

pvString=""
if PVreduce : pvString+="_"+"PVregion"+str(PVreduce)


#######################################################

from drawStyle import *

setStyle()

#######################################################

CANVAS = TCanvas("CANVAS","CANVAS",600,600)

borderX = CANVAS.GetWindowWidth()-CANVAS.GetWw()
borderY = CANVAS.GetWindowHeight()-CANVAS.GetWh()
CANVAS.SetCanvasSize(500,500)
CANVAS.SetWindowSize(500+borderX,500+borderY)

CANVAS.Modified()
CANVAS.Update()
#float x = frame->GetX1() + (frame->GetX2()-frame->GetX1())*0.03;
#float y = frame->GetY2() - (frame->GetY2()-frame->GetY1())*0.1;

CANVAS.UseCurrentStyle()

#######################################################

FRAME = rrv_ll_M.frame(30)

DATA.plotOn(FRAME,
            RooFit.MarkerSize(1.0),#0.7
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
sumPdf2.plotOn(FRAME,
               RooFit.FillColor(kBlue-7),
               RooFit.Components("myRHP_TtbarMC,myRHP_DYMC"),
               RooFit.DrawOption("F"),
               RooFit.LineColor(kBlack),
               RooFit.LineWidth(1))
sumPdf2.plotOn(FRAME,
               RooFit.FillColor(kBlue-7),
               RooFit.Components("myRHP_TtbarMC,myRHP_DYMC"),
               RooFit.LineColor(kBlack),
               RooFit.LineWidth(1))
sumPdf2.plotOn(FRAME,
               RooFit.Components("myRHP_TtbarMC"),
               RooFit.LineColor(kBlack),
               RooFit.FillColor(kYellow-7),
               RooFit.DrawOption("F"),
               RooFit.LineWidth(1))
sumPdf2.plotOn(FRAME,
               RooFit.FillColor(kYellow-7),
               RooFit.Components("myRHP_TtbarMC"),
               RooFit.LineColor(kBlack),
               RooFit.LineWidth(1))
DATA.plotOn(FRAME,
            RooFit.MarkerSize(1.0),
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
FRAME.Draw()

leg1 = TLegend(0.72, 0.55, 0.92, 0.95-0.15, "", "NDC")
leg1.AddEntry( FRAME.getObject(0), "Data ",   "PLE")
leg1.AddEntry( FRAME.getObject(1), "DY+jets"  ,"F")
leg1.AddEntry( FRAME.getObject(3), "tt"       ,"F")

leg1.SetTextSize(0.04)
leg1.SetFillColor(0)
leg1.SetShadowColor(0)
leg1.SetBorderSize(0)

leg1.Draw()

lat=TLatex()
lat.SetTextSize(0.04)
lat.DrawLatex(2.4,0.88*FRAME.GetMaximum(),"#splitline{CMS Preliminary}{#sqrt{s} = 7 TeV, L = 2.1 fb^{-1}}")

CANVAS.Draw()

CANVAS.SaveAs("~/public/Z2b/ttbar/ttbarFit_"+channel+"_"+WP+".pdf")

filename = "/home/fynu/tdupree/public/Z2b/ttbar/ttbarFit_"+channel+"_"+WP+".txt"

my_file = open(filename,"w")
print "filename = ", filename
print >> my_file, "##############################################################"
print >> my_file, "WP = ", WP
print >> my_file, "channel = ", channel
print >> my_file, "fraction of background model in signal range", frac_in_sig_range.getVal()

print >> my_file, "N(ll) = ", N_ll.getVal()
print >> my_file, "N(tt) [60-200]= ", N_ttbar.getVal()
N_tt_sig = N_ttbar.getVal()*frac_in_sig_range.getVal()
print >> my_file, "=> N(tt) [60-120]= ", N_tt_sig

print >> my_file, "--------------------> for di-", channel, "sample at selection step ", WP
print >> my_file, "--------------------> "
print >> my_file, "--------------------> f_tt = N(tt)/[N(ll)+(tt)] = ( ", str(N_tt_sig/(N_ll.getVal()+N_tt_sig)*100.)[:4] , " +/- ", str(frac_DY.getError()*100.)[:4] , " ) % "

print "VOILA!!!"
