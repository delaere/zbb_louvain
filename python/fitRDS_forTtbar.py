from ROOT import *

file = {  "Mu_DATA"     : TFile("File_rds_zbb_Mu_diLepM_DATA.root"),
          "Mu_MC"       : TFile("File_rds_zbb_Mu_diLepM_Mu_MC.root"),
          "Ttbar_Mu_MC" : TFile("File_rds_zbb_Mu_diLepM_Ttbar_MC.root")
          }
ws={}         
ws["Mu_DATA"]     = file["Mu_DATA"].Get("ws")
ws["Mu_MC"]       = file["Mu_MC"].Get("ws")
ws["Ttbar_Mu_MC"] = file["Ttbar_Mu_MC"].Get("ws")

myRDS ={}
myRDS["Mu_DATA"]     = ws["Mu_DATA"].data("rds_zbb")
myRDS["Mu_MC"]       = ws["Mu_MC"].data("rds_zbb")
myRDS["Ttbar_Mu_MC"] = ws["Ttbar_Mu_MC"].data("rds_zbb")

print "myRDS[\"Ttbar_Mu_MC\"].numEntries() = ", myRDS["Ttbar_Mu_MC"].numEntries()
print "myRDS[\"Mu_MC\"].numEntries() = ", myRDS["Mu_MC"].numEntries()
print "myRDS[\"Mu_DATA\"].numEntries() = ", myRDS["Mu_DATA"].numEntries()

rrv_ll_M    = ws["Mu_DATA"].var("rrv_ll_M")
#rrv_HE      = ws["Mu_DATA"].var("rc_HE")
#rrv_HP      = ws["Mu_DATA"].var("rc_HP")
#rrv_HEMET   = ws["Mu_DATA"].var("rc_HEMET")
#rrv_HPMET   = ws["Mu_DATA"].var("rc_HPMET")

rrv_ll_M.setMin( 50)
rrv_ll_M.setMax(150)

myRDH = {}
myRHP = {}

#myRDH["Mu_MC"]       = RooDataHist("myRDH_Mu_MC",       "myRDH_Mu_MC",        RooArgSet(rrv_ll_M), myRDS["Mu_MC"]  )
#myRHP["Mu_MC"]       = RooHistPdf( "myRHP_Mu_MC",       "myRHP_Mu_MC",        RooArgSet(rrv_ll_M), myRDH["Mu_MC"]  )
#myRDH["Ttbar_Mu_MC"] = RooDataHist("myRDH_Ttbar_Mu_MC", "myRDH_Ttbar_Mu_MC",  RooArgSet(rrv_ll_M), myRDS["Mu_MC"]  )
#myRHP["Ttbar_Mu_MC"] = RooHistPdf( "myRHP_Ttbar_Mu_MC", "myRHP_Ttbar_Mu_MC",  RooArgSet(rrv_ll_M), myRDH["Mu_MC"]  )

myRHP["Mu_MC"]       = RooKeysPdf( "myRHP_Mu_MC",       "myRHP_Mu_MC",        rrv_ll_M, myRDS["Mu_MC"]  )
myRHP["Ttbar_Mu_MC"] = RooKeysPdf( "myRHP_Ttbar_Mu_MC", "myRHP_Ttbar_Mu_MC",  rrv_ll_M, myRDS["Ttbar_Mu_MC"]  )

rrv_ll_M.setRange("r",50,150)
rrv_ll_M.setRange("sig",60,120)

sigArea=myRHP["Ttbar_Mu_MC"].createIntegral(RooArgSet(rrv_ll_M),"sig") 
totArea=myRHP["Ttbar_Mu_MC"].createIntegral(RooArgSet(rrv_ll_M),"r")

frac_in_sig_range = RooConstVar("frac_in_sig_range","frac_in_sig_range",sigArea.getVal()/totArea.getVal())

print "FRAC IN SIG RANGE", frac_in_sig_range.getVal()

frac_ttbar = RooRealVar("frac_ttbar","frac_ttbar",0.20,0,1)


DATA_HE=myRDS["Mu_DATA"].reduce("rc_HE==1")
DATA_HP=myRDS["Mu_DATA"].reduce("rc_HP==1")
DATA_HEMET=myRDS["Mu_DATA"].reduce("rc_HEMET==1")
DATA_HPMET=myRDS["Mu_DATA"].reduce("rc_HPMET==1")

DATA_HE.SetName("DATA_HE")
DATA_HP.SetName("DATA_HP")
DATA_HEMET.SetName("DATA_HEMET")
DATA_HPMET.SetName("DATA_HPMET")

print "DATA_HE.numEntries() = ", DATA_HE.numEntries()
print "DATA_HP.numEntries() = ", DATA_HP.numEntries()
print "DATA_HEMET.numEntries() = ", DATA_HEMET.numEntries()
print "DATA_HPMET.numEntries() = ", DATA_HPMET.numEntries()



N_ttbar_in_sig_range = RooRealVar("N_ttbar_in_sig_range","N_ttbar_in_sig_range",
                                  0.80*DATA_HE.numEntries(),
                                  0.00*DATA_HE.numEntries(),
                                  1.10*DATA_HE.numEntries())
#N_ttbar = RooFormulaVar("N_ttbar","N_ttbar","@0/@1",RooArgList(N_ttbar_in_sig_range,frac_in_sig_range))
N_ttbar = RooRealVar("N_ttbar","N_ttbar",
                     0.80*DATA_HE.numEntries(),
                     0.00*DATA_HE.numEntries(),
                     1.10*DATA_HE.numEntries())
N_ll = RooRealVar("N_ll","N_ll",
                     0.21*DATA_HE.numEntries(),
                     0.00*DATA_HE.numEntries(),
                     1.20*DATA_HE.numEntries())

sumPdf = RooAddPdf("sumPdf","sumPdf",
                   RooArgList(myRHP["Ttbar_Mu_MC"],myRHP["Mu_MC"]),
                   RooArgList(N_ttbar,N_ll))

sumPdf2 = RooAddPdf("sumPdf2","sumPdf2",
                   RooArgList(myRHP["Ttbar_Mu_MC"],myRHP["Mu_MC"]),
                   RooArgList(frac_ttbar))

gROOT.SetStyle("Plain")

C=TCanvas("C","C",400,700)
C.Divide(2,4)


sumPdf.fitTo(DATA_HE,RooFit.Extended(),RooFit.Range("r"))

C.cd(1).SetLogy()
frame1 = rrv_ll_M.frame(50,150,25)
DATA_HE.plotOn(frame1,
               RooFit.MarkerSize(1.3),
               RooFit.XErrorSize(0.035),
               RooFit.DrawOption("pe2"))
sumPdf.plotOn(frame1,
              RooFit.LineWidth(1),
              RooFit.LineColor(kBlack))
sumPdf.plotOn(frame1,
              RooFit.Components("myRHP_Ttbar_Mu_MC"),
              RooFit.LineStyle(kDashed),
              RooFit.LineColor(kYellow),
              RooFit.LineWidth(1)
              )
sumPdf.plotOn(frame1,
              RooFit.Components("myRHP_Mu_MC"),      
              RooFit.LineStyle(kDashed),
              RooFit.LineColor(kBlue),
              RooFit.LineWidth(1))
DATA_HE.plotOn(frame1,
               RooFit.MarkerSize(1.3),
               RooFit.XErrorSize(0.035),
               RooFit.DrawOption("pe2"))
sumPdf.paramOn(frame1,DATA_HE)
frame1.Draw()

sumPdf2.fitTo(DATA_HE,RooFit.Range("r"))

C.cd(2).SetLogy()
frame2 = rrv_ll_M.frame(50,150,25)
DATA_HE.plotOn(frame2,
               RooFit.MarkerSize(1.3),
               RooFit.XErrorSize(0.035),
               RooFit.DrawOption("pe2"))
sumPdf2.plotOn(frame2,
               RooFit.FillColor(kBlue),
               RooFit.Components("myRHP_Ttbar_Mu_MC,myRHP_Mu_MC"),
               RooFit.DrawOption("F"),
               RooFit.LineColor(kBlack),
               RooFit.LineWidth(1))
sumPdf2.plotOn(frame2,
               RooFit.Components("myRHP_Ttbar_Mu_MC"),
               RooFit.LineColor(kBlack),
               RooFit.DrawOption("F"),
               RooFit.FillColor(kYellow),
               RooFit.LineWidth(1))
DATA_HE.plotOn(frame2,
               RooFit.MarkerSize(1.3),
               RooFit.XErrorSize(0.035),
               RooFit.DrawOption("pe2"))
frame2.Draw()

sumPdf3=sumPdf

sumPdf3.fitTo(DATA_HP,RooFit.Extended(),RooFit.Range("r"))

C.cd(3).SetLogy()
frame3 = rrv_ll_M.frame(50,150,25)
DATA_HP.plotOn(frame3,
               RooFit.MarkerSize(1.3),
               RooFit.XErrorSize(0.035),
               RooFit.DrawOption("pe2"))
sumPdf3.plotOn(frame3,
               RooFit.LineWidth(1),
               RooFit.LineColor(kBlack))
sumPdf3.plotOn(frame3,
               RooFit.Components("myRHP_Ttbar_Mu_MC"),
               RooFit.LineWidth(1),
               RooFit.LineStyle(kDashed),
               RooFit.LineColor(kYellow))
sumPdf3.plotOn(frame3,
               RooFit.Components("myRHP_Mu_MC"),      
               RooFit.LineWidth(1),
               RooFit.LineStyle(kDashed),
               RooFit.LineColor(kBlue))
DATA_HP.plotOn(frame3,
               RooFit.MarkerSize(1.3),
               RooFit.XErrorSize(0.035),
               RooFit.DrawOption("pe2"))
frame3.Draw()

sumPdf4=sumPdf2
sumPdf4.fitTo(DATA_HP,RooFit.Range("r"))

C.cd(4).SetLogy()
frame4 = rrv_ll_M.frame(50,150,25)
DATA_HP.plotOn(frame4,
               RooFit.MarkerSize(1.3),
               RooFit.XErrorSize(0.035),
               RooFit.DrawOption("pe2"))
sumPdf4.plotOn(frame4,
               RooFit.Components("myRHP_Ttbar_Mu_MC,myRHP_Mu_MC"),      
               RooFit.DrawOption("F"),
               RooFit.FillColor(kBlue),
               RooFit.LineColor(kBlack),
               RooFit.LineWidth(1))
sumPdf4.plotOn(frame4,RooFit.Components("myRHP_Ttbar_Mu_MC"),
               RooFit.DrawOption("F"),
               RooFit.FillColor(kYellow),
               RooFit.LineColor(kBlack),
               RooFit.LineWidth(1))
DATA_HP.plotOn(frame4,
               RooFit.MarkerSize(1.3),
               RooFit.XErrorSize(0.035),
               RooFit.DrawOption("pe2"))
frame4.Draw()

sumPdf5=sumPdf
sumPdf5.fitTo(DATA_HEMET,RooFit.Extended(),RooFit.Range("r"))

C.cd(5).SetLogy()
frame5 = rrv_ll_M.frame(50,150,25)
DATA_HEMET.plotOn(frame5,
                  RooFit.MarkerSize(1.3),
                  RooFit.XErrorSize(0.035),
                  RooFit.DrawOption("pe2"))
sumPdf5.plotOn(frame5,
               RooFit.LineWidth(1),
               RooFit.LineColor(kBlack))
sumPdf5.plotOn(frame5,
               RooFit.Components("myRHP_Ttbar_Mu_MC"),
               RooFit.LineStyle(kDashed),
               RooFit.LineWidth(1),
               RooFit.LineColor(kYellow))
sumPdf5.plotOn(frame5,
               RooFit.Components("myRHP_Mu_MC"),      
               RooFit.LineStyle(kDashed),
               RooFit.LineWidth(1),
               RooFit.LineColor(kBlue))
DATA_HEMET.plotOn(frame5,
                  RooFit.MarkerSize(1.3),
                  RooFit.XErrorSize(0.035),
                  RooFit.DrawOption("pe2"))
sumPdf5.paramOn(frame5,DATA_HEMET)
frame5.Draw()

sumPdf6=sumPdf2
sumPdf6.fitTo(DATA_HEMET,RooFit.Range("r"))

C.cd(6).SetLogy()
frame6 = rrv_ll_M.frame(50,150,25)
DATA_HEMET.plotOn(frame6,
                  RooFit.MarkerSize(1.3),
                  RooFit.XErrorSize(0.035),
                  RooFit.DrawOption("pe2"))
sumPdf6.plotOn(frame6,RooFit.Components("myRHP_Ttbar_Mu_MC,myRHP_Mu_MC"),      
               RooFit.DrawOption("F"),
               RooFit.FillColor(kBlue),
               RooFit.LineColor(kBlack),
               RooFit.LineWidth(1))
sumPdf6.plotOn(frame6,RooFit.Components("myRHP_Ttbar_Mu_MC"),
               RooFit.DrawOption("F"),
               RooFit.FillColor(kYellow),
               RooFit.LineColor(kBlack),
               RooFit.LineWidth(1))
DATA_HEMET.plotOn(frame6,
                  RooFit.MarkerSize(1.3),
                  RooFit.XErrorSize(0.035),
                  RooFit.DrawOption("pe2"))
frame6.Draw()

sumPdf7=sumPdf
sumPdf7.fitTo(DATA_HPMET,RooFit.Extended(),RooFit.Range("r"))

C.cd(7).SetLogy()
frame7 = rrv_ll_M.frame(50,150,25)
DATA_HPMET.plotOn(frame7,
                  RooFit.MarkerSize(1.3),
                  RooFit.XErrorSize(0.035),
                  RooFit.DrawOption("pe2"))
sumPdf7.plotOn(frame7,
               RooFit.LineWidth(1),
               RooFit.LineColor(kBlack))
sumPdf7.plotOn(frame7,
              RooFit.Components("myRHP_Ttbar_Mu_MC"),
              RooFit.LineStyle(kDashed),
              RooFit.LineColor(kYellow),
               RooFit.LineWidth(1))
sumPdf7.plotOn(frame7,
              RooFit.Components("myRHP_Mu_MC"),      
              RooFit.LineStyle(kDashed),
              RooFit.LineColor(kBlue),
               RooFit.LineWidth(1))
DATA_HPMET.plotOn(frame7,
                  RooFit.MarkerSize(1.3),
                  RooFit.XErrorSize(0.035),
                  RooFit.DrawOption("pe2"))
sumPdf7.paramOn(frame7,DATA_HPMET)
frame7.Draw()

sumPdf8=sumPdf2
sumPdf8.fitTo(DATA_HPMET,RooFit.Range("r"))

C.cd(8).SetLogy()
frame8 = rrv_ll_M.frame(50,150,25)
DATA_HPMET.plotOn(frame8,
                  RooFit.MarkerSize(1.3),
                  RooFit.XErrorSize(0.035),
                  RooFit.DrawOption("pe2"))
sumPdf8.plotOn(frame8,
               RooFit.Components("myRHP_Ttbar_Mu_MC,myRHP_Mu_MC"),      
               RooFit.DrawOption("F"),
               RooFit.FillColor(kBlue),
               RooFit.LineColor(kBlack),
               RooFit.LineWidth(1))
sumPdf8.plotOn(frame8,
               RooFit.Components("myRHP_Ttbar_Mu_MC"),
               RooFit.DrawOption("F"),
               RooFit.FillColor(kYellow),
               RooFit.LineColor(kBlack),
               RooFit.LineWidth(1))
DATA_HPMET.plotOn(frame8,
                  RooFit.MarkerSize(1.3),
                  RooFit.XErrorSize(0.035),
                  RooFit.DrawOption("pe2"))
frame8.Draw()

print "FRAC IN SIG RANGE", frac_in_sig_range.getVal()
