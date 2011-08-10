from ROOT import *

WP =  "HP_excl"        #"HP","HPMET","HP_excl","HE","HEMET","HE_excl"
channel = "Mu"
sel= {"Mu":"muSel",
      "El":"elSel"}

TtbarMC = "Ttbar_"+channel+"_MC"
Data    = channel+"_DATA"
DYMC    = channel+"_MC"

file = {  Data    : TFile("File_rds_zbb_"+Data+"_"+sel[channel]+"_forTtbar.root"),
          DYMC    : TFile("File_rds_zbb_"+DYMC+"_"+sel[channel]+"_forTtbar.root"),
          TtbarMC : TFile("File_rds_zbb_"+TtbarMC+"_"+sel[channel]+"_forTtbar.root")
          }
ws={}         
ws[Data]    = file[Data].Get("ws")
ws[DYMC]    = file[DYMC].Get("ws")
ws[TtbarMC] = file[TtbarMC].Get("ws")

myRDS ={}
myRDS[Data]    = ws[Data].data("rds_zbb")
myRDS[DYMC]    = ws[DYMC].data("rds_zbb")
myRDS[TtbarMC] = ws[TtbarMC].data("rds_zbb")

myRDS[DYMC]    = myRDS[DYMC].reduce("rc_"+WP+"==1")
myRDS[TtbarMC] = myRDS[TtbarMC].reduce("rc_"+WP+"==1")
DATA=myRDS[Data].reduce("rc_"+WP+"==1")

print "DATA("+WP+").numEntries() = ", DATA.numEntries()

print "myRDS[\"Ttbar_Mu_MC\"].numEntries() = ", myRDS[TtbarMC].numEntries()
print "myRDS[\"Mu_MC\"].numEntries() = ", myRDS[DYMC].numEntries()
print "myRDS[\"Mu_DATA\"].numEntries() = ", myRDS[Data].numEntries()

rrv_ll_M    = ws[Data].var("rrv_ll_M")
#rrv_HE      = ws["Mu_DATA"].var("rc_HE")
#rrv_HP      = ws["Mu_DATA"].var("rc_HP")
#rrv_HEMET   = ws["Mu_DATA"].var("rc_HEMET")
#rrv_HPMET   = ws["Mu_DATA"].var("rc_HPMET")

rrv_ll_M.setMin( 50)
rrv_ll_M.setMax(210)
rrv_ll_M.setBins(80)
rrv_ll_M.SetTitle("m(l^{+}l^{-} (GeV/c^{2}))")

myRDH = {}
myRHP = {}

myRDH[DYMC]      = RooDataHist("myRDH_DYMC",    "myRDH_DYMC",     RooArgSet(rrv_ll_M), myRDS[DYMC]  )
myRHP[DYMC]      = RooHistPdf( "myRHP_DYMC",    "myRHP_DYMC",     RooArgSet(rrv_ll_M), myRDH[DYMC]  )
myRDH[TtbarMC]   = RooDataHist("myRDH_TtbarMC", "myRDH_TtbarMC",  RooArgSet(rrv_ll_M), myRDS[TtbarMC]  )
myRHP[TtbarMC]   = RooHistPdf( "myRHP_TtbarMC", "myRHP_TtbarMC",  RooArgSet(rrv_ll_M), myRDH[TtbarMC]  )

#myRHP[DYMC]     = RooKeysPdf( "myRHP_DYMC",    "myRHP_DYMC",      rrv_ll_M, myRDS[DYMC]      )
#myRHP[TtbarMC]  = RooKeysPdf( "myRHP_TtbarMC", "myRHP_TtbarMC",  rrv_ll_M, myRDS[TtbarMC]  )

rrv_ll_M.setRange("r",60,200)
rrv_ll_M.setRange("sig",60,120)

sigArea=myRHP[TtbarMC].createIntegral(RooArgSet(rrv_ll_M),"sig") 
totArea=myRHP[TtbarMC].createIntegral(RooArgSet(rrv_ll_M),"r")

frac_in_sig_range = RooConstVar("frac_in_sig_range","frac_in_sig_range",sigArea.getVal()/totArea.getVal())

print "FRAC IN SIG RANGE", frac_in_sig_range.getVal()

frac_ttbar = RooRealVar("frac_ttbar","frac_ttbar",0.20,0,1)



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
                   RooArgList(myRHP[TtbarMC],myRHP[DYMC]),
                   RooArgList(frac_ttbar))

gROOT.SetStyle("Plain")

C=TCanvas("C","C",1000,450)
C.Divide(2)

sumPdf.fitTo(DATA,RooFit.Extended(),RooFit.Range("r"))

C.cd(1).SetLogy()
frame1 = rrv_ll_M.frame(60,200,70)
frame1.SetBarWidth(0.)
frame1.SetMarkerSize(1.3)
frame1.SetLineWidth(1)
DATA.plotOn(frame1,
            RooFit.MarkerSize(1.3),
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
sumPdf.plotOn(frame1,
              RooFit.LineWidth(1),
              RooFit.LineColor(kBlack))
sumPdf.plotOn(frame1,
              RooFit.Components("myRHP_TtbarMC"),
              RooFit.LineStyle(kDashed),
              RooFit.LineColor(kYellow),
              RooFit.LineWidth(1)
              )
sumPdf.plotOn(frame1,
              RooFit.Components("myRHP_DYMC"),      
              RooFit.LineStyle(kDashed),
              RooFit.LineColor(kBlue),
              RooFit.LineWidth(1))
DATA.plotOn(frame1,
               RooFit.MarkerSize(1.3),
               RooFit.XErrorSize(0.035),
               RooFit.DrawOption("pe2"))
sumPdf.paramOn(frame1,DATA)
frame1.SetMinimum(0.9)
frame1.Draw()

sumPdf2.fitTo(DATA,RooFit.Range("r"))

C.cd(2).SetLogy()
frame2 = rrv_ll_M.frame(60,200,70)
frame2.SetBarWidth(0.)
frame2.SetMarkerSize(1.3)
frame2.SetLineWidth(1)
DATA.plotOn(frame2,
            RooFit.MarkerSize(1.3),
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
sumPdf2.plotOn(frame2,
               RooFit.FillColor(kBlue),
               RooFit.Components("myRHP_TtbarMC,myRHP_DYMC"),
               RooFit.DrawOption("F"),
               RooFit.LineColor(kBlack),
               RooFit.LineWidth(1))
sumPdf2.plotOn(frame2,
               RooFit.Components("myRHP_TtbarMC"),
               RooFit.LineColor(kBlack),
               RooFit.FillColor(kYellow),
               RooFit.DrawOption("F"),
               RooFit.LineWidth(1))
DATA.plotOn(frame2,
            RooFit.MarkerSize(1.3),
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
frame2.SetMinimum(0.9)
frame2.Draw()

C.SaveAs("~/public/ZbbLeptonPhoton/ttbarPlots/ttbarFit_"+channel+"_"+WP+".pdf")

filename = "/afs/cern.ch/user/t/tdupree/public/ZbbLeptonPhoton/ttbarPlots/"+channel+"_"+"_"+WP+".txt"

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
print >> my_file, "--------------------> f_tt = N(tt)/[N(ll)+(tt)] = ( ", N_tt_sig/(N_ll.getVal()+N_tt_sig)*100. , " +/- ", frac_ttbar.getError()*100. , " ) % "

print "VOILA!!!"
