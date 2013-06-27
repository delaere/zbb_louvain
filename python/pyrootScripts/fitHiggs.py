######################################################################################
######################################################################################
###                                                                                ### 
### fitRDS.py (TdP)                                                                ### 
###                                                                                ###  
### Analyze the RooDataSet produced by makeRDS.py to perform a Higgs search        ###
###                                                                                ### 
### Functionality:                                                                 ###
### - Fit for signal peak                                                          ###
### - Estimate significance sigal peak using profile likelihood                    ###
### - CLs scan using different models as function of mH hypothesis                 ###                          
###                                                                                ###
### To do:                                                                         ###
### - get proper MC samples                                                        ###
### - allow for options to use both template and functional PDFs                   ###
### - factorize data-getting/pdf-making/fitting/plotting/etc...a bit less ugly ;-) ###
### - check CLs scan (and do the plot of the scan more elegantly)                  ###
###                                                                                ###
### more statistical methods? see http://root.cern.ch/root/html/tutorials/roostats/index.html
###                                                                                ###    
######################################################################################
######################################################################################

import ROOT
from ROOT import *

gROOT.SetStyle("Plain")


#######################
### GET DATA AND MC ###
#######################

#cutstring = "rrv_ll_pT>0"
#cutstring = "rrv_bb_dR<1.5&&rrv_ll_pT>50"
cutstring =  "jetmetMET<50&eventSelectionbestzmassEle>76&eventSelectionbestzmassEle<106"

WP =  "eventSelection_9"        #"HP","HPMET","HP_excl","HE","HEMET","HE_excl"
channel = "Mu"


sel= {"Mu":"muSel",
      "El":"elSel",
      "Sum":"sumSel"}

TtbarMC = "Ttbar_"+channel+"_MC"
Data    = channel+"_DATA"
DYMC    = channel+"_MC"

TtbarMC_mu = "Ttbar_Mu_MC"
Data_mu    = "Mu_DATA"
DYMC_mu    = "Mu_MC"

TtbarMC_el = "Ttbar_El_MC"
Data_el    = "El_DATA"
DYMC_el    = "El_MC"

if channel =="El": cutstring ="jetmetMET<50&eventSelectionbestzmassEle>76&eventSelectionbestzmassEle<106"
if channel =="Mu": cutstring ="jetmetMET<50&eventSelectionbestzmassMu>76&eventSelectionbestzmassMu<106"
if channel=="Sum":
    Data    = Data_el
    DYMC    = DYMC_el
    TtbarMC = TtbarMC_el
    cutstring ="jetmetMET<50"

file = {  Data      : TFile("File_rds_zbb_"+Data+".root"),
          DYMC       : TFile("File_rds_zbb_"+DYMC+".root"),
          TtbarMC    : TFile("File_rds_zbb_"+TtbarMC+".root"),
          Data_mu    : TFile("File_rds_zbb_"+Data_mu+".root"),
          DYMC_mu    : TFile("File_rds_zbb_"+DYMC_mu+".root"),
          TtbarMC_mu : TFile("File_rds_zbb_"+TtbarMC_mu+".root"),
          Data_el    : TFile("File_rds_zbb_"+Data_el+".root"),
          DYMC_el    : TFile("File_rds_zbb_"+DYMC_el+".root"),
          TtbarMC_el : TFile("File_rds_zbb_"+TtbarMC_el+".root")
          }

#file = {  Data    : TFile("File_rds_zbb_"+Data+"_"+sel[channel]+".root"),
#          DYMC    : TFile("File_rds_zbb_"+DYMC+"_"+sel[channel]+".root"),
#          TtbarMC : TFile("File_rds_zbb_"+TtbarMC+"_"+sel[channel]+".root")
#                    }

ws={}

myRDS ={}

if channel=="Sum":
    ws[Data_el]    = file[Data_el].Get("ws")
    ws[DYMC_el]    = file[DYMC_el].Get("ws")
    ws[TtbarMC_el] = file[TtbarMC_el].Get("ws")
    ws[Data_mu]    = file[Data_mu].Get("ws")
    ws[DYMC_mu]    = file[DYMC_mu].Get("ws")
    ws[TtbarMC_mu] = file[TtbarMC_mu].Get("ws")

    myRDS[Data]    = ws[Data_el].data("rds_zbb")
    myRDS[DYMC]    = ws[DYMC_el].data("rds_zbb")
    myRDS[TtbarMC] = ws[TtbarMC_el].data("rds_zbb")

    myRDS[Data_mu]    = ws[Data_mu].data("rds_zbb")
    myRDS[DYMC_mu]    = ws[DYMC_mu].data("rds_zbb")
    myRDS[TtbarMC_mu] = ws[TtbarMC_mu].data("rds_zbb")

    myRDS[Data].append(myRDS[Data_mu])
    myRDS[DYMC].append(myRDS[DYMC_mu])
    myRDS[TtbarMC].append(myRDS[TtbarMC_mu])
else :
    ws[Data]    = file[Data].Get("ws")
    ws[DYMC]    = file[DYMC].Get("ws")
    ws[TtbarMC] = file[TtbarMC].Get("ws")

    myRDS[Data]    = ws[Data].data("rds_zbb")
    myRDS[DYMC]    = ws[DYMC].data("rds_zbb")
    myRDS[TtbarMC] = ws[TtbarMC].data("rds_zbb")

myRDS[DYMC]    = myRDS[DYMC].reduce("rc_"+WP+"==1")
myRDS[TtbarMC] = myRDS[TtbarMC].reduce("rc_"+WP+"==1")
DATA           = myRDS[Data].reduce("rc_"+WP+"==1")

if cutstring:
    myRDS[DYMC]    = myRDS[DYMC].reduce(cutstring)
    myRDS[TtbarMC] = myRDS[TtbarMC].reduce(cutstring)
    DATA=DATA.reduce(cutstring)

print "DATA("+WP+").numEntries() = ", DATA.numEntries()

rrv_SV_M    = ws[Data].var("jetmetbjet1SVmass")

rrv_bb_M    = ws[Data].var("eventSelectiondijetM")
rrv_bb_M.setMin(0)
rrv_bb_M.setMax(750)
rrv_bb_M.setBins(25)
rrv_bb_M.SetTitle("m(bb) (GeV/c^{2})")

rrv_ll_pT    = ws[Data].var("eventSelectionbestzptMu")
rrv_ll_pT.setMin(0)
rrv_ll_pT.setMax(400)
rrv_ll_pT.setBins(20)
rrv_ll_pT.SetTitle("p_{T}(l^{+}l^{-})")

rrv_zbb_M   = ws[Data].var("eventSelectionZbbM")
rrv_zbb_M.setMin(0)
rrv_zbb_M.setMax(750)
rrv_zbb_M.setBins(15)
rrv_zbb_M.SetTitle("M(l^{+}l^{-}bb)")

rrv_bb_dR   = ws[Data].var("eventSelectiondijetdR")
rrv_bb_dR.setMin(0)
rrv_bb_dR.setMax(6)
rrv_bb_dR.setBins(12)
rrv_bb_dR.SetTitle("#Delta R(b_{1},b_{2})")

rrv_zeebb_M = ws[Data].var("rrv_zeebb_M")
rrv_zmmbb_M = ws[Data].var("rrv_zmmbb_M")
rc_cat      = ws[Data].var("rc_cat")

print "############################"
print "#Events DYMC    = ", myRDS[DYMC].numEntries() 
print "#Events TtbarMC = ", myRDS[TtbarMC].numEntries() 
print "#Events DATA    = ", DATA.numEntries() 
print "############################"

##############################################
### MAKE SIGNAL PDF (analytic or template) ###
##############################################

mean_bb  = RooRealVar("mean_bb", "mean_bb", 250)
sigma_bb = RooRealVar("sigma_bb","sigma_bb", 30)
Sig_bb = RooGaussian("Sig_bb","Sig_bb",rrv_bb_M,mean_bb,sigma_bb)

S = RooRealVar("S","S",0.10,-30,30)

sig_pdf = RooExtendPdf("sig_pdf",
                       "sig_pdf",
                       Sig_bb,
                       S)

##################################################
### MAKE BACKGROUND PDF (analytic or template) ###
##################################################

rdh_zbb_MC_bb_M = {}
rhp_zbb_MC_bb_M = {}

B={}

###########
### FIT ###
###########

C_fit  = {}
frame  = {}  
frame2 = {}  

### more statistical methods? see http://root.cern.ch/root/html/tutorials/roostats/index.html

#Sum_bb.fitTo(DATA,RooFit.Extended())

varList = [rrv_bb_M,
           rrv_ll_pT,
           rrv_zbb_M,
           rrv_bb_dR] 

Canvas=TCanvas("Canvas","Canvas",650,650)
Canvas.Divide(2,2)

dir =0

for var in varList:
    print "var = ", var
    C_fit[var]=TCanvas("C_fit"+var.GetName(),"C_fit"+var.GetName(),800,400)
    C_fit[var].Divide(2)
    frame[var] = var.frame()#0,600,12)#rrv_bb_M.getMax())
    frame_test = var.frame()#0,600,12)#rrv_bb_M.getMax())
   
    print "var = ", var
    print "var.GetName() = ", var.GetName()
    print "var.getMax() = ", var.getMax()
    print "frame[var] = ", frame[var]
    print "frame-test = ", frame_test
  
    rdh_zbb_MC_bb_M[DYMC]    = RooDataHist("rdh_zbb_MC_bb_M"+DYMC,
                                           "rdh_zbb_MC_SV_M"+DYMC,
                                           RooArgSet(var),
                                           myRDS[DYMC])
    rdh_zbb_MC_bb_M[TtbarMC] = RooDataHist("rdh_zbb_MC_bb_M"+TtbarMC,
                                           "rdh_zbb_MC_bb_M"+TtbarMC,
                                           RooArgSet(var),
                                           myRDS[TtbarMC])
    rhp_zbb_MC_bb_M[DYMC]    = RooHistPdf( "rhp_zbb_MC_bb_M"+DYMC,
                                           "rhp_zbb_MC_bb_M"+DYMC,
                                           RooArgSet(var),
                                           rdh_zbb_MC_bb_M[DYMC])
    rhp_zbb_MC_bb_M[TtbarMC] = RooHistPdf( "rhp_zbb_MC_bb_M"+TtbarMC,
                                           "rhp_zbb_MC_bb_M"+TtbarMC,
                                           RooArgSet(var),
                                           rdh_zbb_MC_bb_M[TtbarMC])
    
    #rhp_zbb_MC_8_bb_M = RooKeysPdf("rhp_zbb_MC_8_bb_M","rhp_zbb_MC_8_bb_M", rrv_bb_M, rds_zbb_MC_8)

    #B[DYMC]    = RooRealVar("B"+DYMC,   "B"+DYMC,   myRDS[DYMC].numEntries()*(2.0/11.8)*10.)
    #B[TtbarMC] = RooRealVar("B"+TtbarMC,"B"+TtbarMC,myRDS[TtbarMC].numEntries()*(2.0/23.))

    lumi_of_TT = 3297203./158.
    lumi_of_DY = 29369902./3048.

    lumi_data = { "Mu" : 2006.8,
                  "El" : 1794.1 }
    lumi_data["Sum"] = lumi_data["Mu"]+lumi_data["El"]

    print "*** LUMI of DY = ", lumi_of_DY
    print "*** LUMI of TT = ", lumi_of_TT

    B[DYMC]    = RooRealVar("B"+DYMC,    "B"+DYMC,     myRDS[DYMC].numEntries()*lumi_data[channel]/lumi_of_DY*20./20.)
    B[TtbarMC] = RooRealVar("B"+TtbarMC, "B"+TtbarMC,  myRDS[TtbarMC].numEntries()*lumi_data[channel]/lumi_of_TT)
    
    SM_MC = B[DYMC].getVal() + B[TtbarMC].getVal()

    norm = SM_MC/DATA.numEntries()#1.

    B[DYMC].setVal(B[DYMC].getVal()/norm)
    B[TtbarMC].setVal(B[TtbarMC].getVal()/norm)
    
    B_SM = RooRealVar("B_SM","B_SM",SM_MC/norm)#,0.9*SM_MC,1.1*SM_MC)

    ext_pdf={}
    ext_pdf[DYMC] = RooExtendPdf("ext_pdf"+DYMC,
                                 "ext_pdf"+DYMC,
                                 rhp_zbb_MC_bb_M[DYMC],
                                 B[DYMC])
    ext_pdf[TtbarMC] = RooExtendPdf("ext_pdf"+TtbarMC,
                                    "ext_pdf"+TtbarMC,
                                    rhp_zbb_MC_bb_M[TtbarMC],
                                    B[TtbarMC])
    
    #bkg_bb.SetName("bkg_bb")
     
    ######################
    ### MAKE TOTAL PDF ###
    ######################

    #S_8=RooRealVar("S_8","N_{S}",0.8*rds_8.numEntries(),0,rds_8.numEntries())
     
    Sum_bb = RooAddPdf("Sum_bb","Sum_bb",
                       RooArgList(Sig_bb,rhp_zbb_MC_bb_M[DYMC],rhp_zbb_MC_bb_M[TtbarMC]),
                       RooArgList(S,     B[DYMC],              B[TtbarMC]) )
    
    print "----> FRACTIONS!!!!"
    print "#S  = ", S.getVal()
    print "#DY = ", B[DYMC].getVal()
    print "#TT = ", B[TtbarMC].getVal()
    print "frame = ", frame[var]
    
    DATA.plotOn(frame[var],
                RooFit.MarkerSize(1.3),
                RooFit.XErrorSize(0.035),
                RooFit.DrawOption("pe2"))
    Sum_bb.plotOn(frame[var],
                  RooFit.LineWidth(1),
                  RooFit.LineColor(kBlack),
                  RooFit.Normalization(norm)
                  )
    Sum_bb.plotOn(frame[var],
                  RooFit.Components("rhp_zbb_MC_bb_M"+DYMC),
                  RooFit.LineWidth(1),
                  RooFit.LineColor(kRed),
                  RooFit.LineStyle(kDashed),
                  RooFit.Normalization(norm)
                  )
    Sum_bb.plotOn(frame[var],
                  RooFit.Components("rhp_zbb_MC_bb_M"+TtbarMC),
                  RooFit.LineWidth(1),
                  RooFit.LineColor(kYellow),
                  RooFit.LineStyle(kDashed),
                  RooFit.Normalization(norm)
                  )
    DATA.plotOn(frame[var],
                RooFit.MarkerSize(1.3),
                RooFit.XErrorSize(0.035),
                RooFit.DrawOption("pe2"))
    #Sum_bb.paramOn(frame,DATA)

    C_fit[var].cd(1).SetLogy()
    frame[var].Draw()


    print "NORMALIZATION = ", norm

    frame2[var] = var.frame()#,600,12)#rrv_bb_M.getMax())
    DATA.plotOn(frame2[var],
                RooFit.MarkerSize(1.3),
                RooFit.XErrorSize(0.035),
                RooFit.DrawOption("pe2"))
    Sum_bb.plotOn(frame2[var],
                  RooFit.LineWidth(1),
                  RooFit.DrawOption("F"),
                  RooFit.FillColor(kRed),
                  RooFit.LineColor(kBlack),
                  RooFit.Normalization(norm)
                  )
    Sum_bb.plotOn(frame2[var],
                  RooFit.LineWidth(1),
                  RooFit.LineColor(kBlack),
                  RooFit.Components("rhp_zbb_MC_bb_M"+TtbarMC+",rhp_zbb_MC_bb_M"+DYMC),
                  RooFit.DrawOption("F"),
                  RooFit.FillColor(kRed),
                  RooFit.LineColor(kBlack),
                  RooFit.Normalization(norm)
                  )
    Sum_bb.plotOn(frame2[var],
                  RooFit.LineWidth(1),
                  RooFit.LineColor(kBlack),
                  RooFit.Components("rhp_zbb_MC_bb_M"+TtbarMC+",rhp_zbb_MC_bb_M"+DYMC),
                  RooFit.FillColor(kRed),
                  RooFit.LineColor(kBlack),
                  RooFit.Normalization(norm)
                  )
    Sum_bb.plotOn(frame2[var],
                  RooFit.LineWidth(1),
                  RooFit.LineColor(kBlack),
                  RooFit.Components("rhp_zbb_MC_bb_M"+TtbarMC),
                  RooFit.DrawOption("F"),
                  RooFit.FillColor(kYellow),
                  RooFit.LineColor(kBlack),
                  RooFit.Normalization(norm)
                  )
    Sum_bb.plotOn(frame2[var],
                  RooFit.LineWidth(1),
                  RooFit.LineColor(kBlack),
                  RooFit.Components("rhp_zbb_MC_bb_M"+TtbarMC),
                  RooFit.FillColor(kYellow),
                  RooFit.LineColor(kBlack),
                  RooFit.Normalization(norm)
                  )
    DATA.plotOn(frame2[var],
                RooFit.MarkerSize(1.3),
                RooFit.XErrorSize(0.035),
                RooFit.DrawOption("pe2"))
    C_fit[var].cd(2)
    frame2[var].Draw()

    dir+=1
    Canvas.cd(dir)
    frame2[var].Draw()

Canvas.SaveAs(channel+"_"+str(WP)+"_"+cutstring+".pdf")

Canvas2 = TCanvas("C2","C2",1200,400)
Canvas2.Divide(3)

gStyle.SetPalette(1)

#rrv_bb_M,
#rrv_ll_pT,
#rrv_zbb_M,
#rrv_bb_dR

CorrCanvas = {}
th2_data   = {}
th2_dymc   = {}
th2_ttmc   = {}

for var1 in varList :
    for var2 in varList :
        corrVar = var1.GetName()+"__VS__"+var2.GetName()
        print "*** looking at correlation ", corrVar

for var1 in varList :
    for var2 in varList :
        corrVar = var1.GetName()+"__VS__"+var2.GetName()
        print "*** looking at correlation ", corrVar
        CorrCanvas[corrVar] = TCanvas("C"+corrVar,"C"+corrVar,1200,800)
        CorrCanvas[corrVar].Divide(3,2)
        
        th2_data[corrVar] = var1.createHistogram(corrVar,var2 )
        th2_data[corrVar].SetName("th2_data_"+corrVar)
        th2_dymc[corrVar] = var1.createHistogram(corrVar,var2 )
        th2_dymc[corrVar].SetName("th2_dymc_"+corrVar)
        th2_ttmc[corrVar] = var1.createHistogram(corrVar,var2 )
        th2_ttmc[corrVar].SetName("th2_ttmc_"+corrVar)
        
        DATA.fillHistogram(          th2_data[corrVar], RooArgList(var1,var2))
        myRDS[DYMC].fillHistogram(   th2_dymc[corrVar], RooArgList(var1,var2))
        myRDS[TtbarMC].fillHistogram(th2_ttmc[corrVar], RooArgList(var1,var2))
        
        CorrCanvas[corrVar].cd(1)
        #th2_data[corrVar].Draw("col2z")
        CorrCanvas[corrVar].cd(2)
        #th2_dymc[corrVar].Draw("col2z")
        CorrCanvas[corrVar].cd(3)
        #th2_ttmc[corrVar].Draw("col2z")
        CorrCanvas[corrVar].cd(4)
        #th2_data[corrVar].Draw("contz")
        CorrCanvas[corrVar].cd(5)
        #th2_dymc[corrVar].Draw("contz")
        CorrCanvas[corrVar].cd(6)
        #th2_ttmc[corrVar].Draw("contz")




##########################
### PROFILE LIKELIHOOD ###
##########################

### see also http://root.cern.ch/root/html/tutorials/roostats/StandardProfileLikelihoodDemo.C.html

# can also do 2D 
# 1D (number of signal events) should be sufficient

plc_S = RooStats.ProfileLikelihoodCalculator(DATA,Sum_bb,RooArgSet(S))
plot_S = RooStats.LikelihoodIntervalPlot(plc_S.GetInterval())

print "plotting likelihood of S alone"

C_profLik=TCanvas("C_profLik","C_profLik",400,350)
plot_S.Draw()

###############
###   CLs   ###
###############

ntoys = 1000

data = {}
myHybridCalc = {}
myHybridResult={}
myHybridPlot={}
sum_bb = {}
clsb_data={}
clb_data={}
cls_data={}
cls_error={}
data_significance={}
min2lnQ_data={}
mean_sb_toys_test_stat={}
myHybridResult={}
toys_significance={}
sig_bb = {}

mList = (300,350,400)

for m in mList :
    sig_bb[m] = RooGaussian("sig_bb_"+str(m),"sig_bb_"+str(m),rrv_bb_M,RooFit.RooConst(m),RooFit.RooConst(25))
    sum_bb[m] = RooAddPdf("sum_bb_"+str(m),"sum_bb_"+str(m),RooArgList(sig_bb[m],Sum_bb),RooArgList(S,RooFit.RooConst(DATA.numEntries())))
    ### generate a data sample
    data[m] = sum_bb[m].generate(RooArgSet(rrv_bb_M),RooFit.Extended())
    ### run HybridCalculator on those inputs
    ### use interface from HypoTest calculator by default
    myHybridCalc[m] = RooStats.HybridCalculatorOriginal(data[m], sum_bb[m], Sum_bb ,RooArgSet())
    #&nuisance_parameters, &bkg_yield_prior);
    ## here I use the default test statistics: 2*lnQ (optional)
    myHybridCalc[m].SetTestStatistic(1);
    ###//myHybridCalc.SetTestStatistic(3); // profile likelihood ratio
    myHybridCalc[m].SetNumberOfToys(ntoys)
    ##
    myHybridCalc[m].UseNuisance(false)
    ### for speed up generation (do binned data)
    myHybridCalc[m].SetGenerateBinned(false);
    ### calculate by running ntoys for the S+B and B hypothesis and retrieve the result
    myHybridResult[m] = myHybridCalc[m].GetHypoTest()
    if not myHybridResult[m] :
        print "***Error returned from Hypothesis test" 
    ### run 1000 toys without gaussian prior on the background yield
    ### HybridResult* myHybridResult = myHybridCalc.Calculate(*data,1000,false);
    ## nice plot of the results
    myHybridPlot[m] = myHybridResult[m].GetPlot("myHybridPlot","Plot of results with HybridCalculatorOriginal",100)

    ### recover and display the results
    clsb_data[m] = myHybridResult[m].CLsplusb()
    clb_data[m] = myHybridResult[m].CLb()
    cls_data[m] = myHybridResult[m].CLs()
    cls_error[m] = myHybridResult[m].CLsError()
    
    data_significance[m] = myHybridResult[m].Significance()
    min2lnQ_data[m] = myHybridResult[m].GetTestStat_data()

    ### compute the mean expected significance from toys
    mean_sb_toys_test_stat[m] = myHybridPlot[m].GetSBmean()
    myHybridResult[m].SetDataTestStatistics(mean_sb_toys_test_stat[m])
    toys_significance[m] = myHybridResult[m].Significance()

    print "==> m(Higgs) = ", m ," <==="
    print " - -2lnQ = " , min2lnQ_data[m] 
    print " - CL_sb = " , clsb_data[m]
    print " - CL_b  = " , clb_data[m]
    print " - CL_s  = " , cls_data[m]
    print " - CL_s 'error' = " , cls_error[m]
    print " - significance of data  = " , data_significance[m]
    print " - mean significance of toys  = " , toys_significance[m]

    bla

print "***Completed HybridCalculatorOriginal example"
print "*** varying Higgs mass hypothesis and estimating confidence level ***"
for m in mList :
    print "==> m(Higgs) = ", m ," <==="
    print " - -2lnQ = " , min2lnQ_data[m] 
    print " - CL_sb = " , clsb_data[m]
    print " - CL_b  = " , clb_data[m]
    print " - CL_s  = " , cls_data[m]
    print " - CL_s 'error' = " , cls_error[m]
    print " - significance of data  = " , data_significance[m]
    print " - mean significance of toys  = " , toys_significance[m]

myTH1_cls       = TH1F("",   "",len(mList),min(mList)-25,max(mList)+25)
myTH1_cls_plus  = TH1F("xxx","",len(mList),min(mList)-25,max(mList)+25)
myTH1_cls_2plus = TH1F("22x","",len(mList),min(mList)-25,max(mList)+25)
myTH1_cls_min   = TH1F("yyy","",len(mList),min(mList)-25,max(mList)+25)
myTH1_cls_2min  = TH1F("22y","",len(mList),min(mList)-25,max(mList)+25)
for x in range(1,len(mList)+1):
    myTH1_cls.SetBinContent(     x, 1-cls_data[mList[x-1]])
    myTH1_cls_plus.SetBinContent(x, 1-(cls_data[mList[x-1]]-cls_error[mList[x-1]]))
    myTH1_cls_min.SetBinContent( x, 1-(cls_data[mList[x-1]]+cls_error[mList[x-1]]))
    myTH1_cls_2plus.SetBinContent(x, 1-(cls_data[mList[x-1]]-2*cls_error[mList[x-1]]))
    myTH1_cls_2min.SetBinContent( x, 1-(cls_data[mList[x-1]]+2*cls_error[mList[x-1]]))

g_cls      = TGraph(myTH1_cls)
g_cls_plus = TGraph(myTH1_cls_plus)
g_cls_min  = TGraph(myTH1_cls_min)

g_cls.GetYaxis().SetTitle("1-CL_{S}")
g_cls.GetXaxis().SetTitle("m_{H} (GeV/c^{2})")
g_cls.SetMaximum(1.)
g_cls.SetMinimum(0.)

#g_cls.GetXaxis().SetRange(min(mList),max(mList))
#myTH1_cls_2plus.GetXaxis().SetRange(min(mList),max(mList))
#myTH1_cls_plus.GetXaxis().SetRange(min(mList),max(mList))
#myTH1_cls.GetXaxis().SetRange(min(mList),max(mList))
#myTH1_cls_min.GetXaxis().SetRange(min(mList),max(mList))
#myTH1_cls_2min.GetXaxis().SetRange(min(mList),max(mList))

Ccls = TCanvas("Ccls","Ccls",500,400)

g_cls.Draw("AC")
myTH1_cls_2plus.Draw("AC,same")
myTH1_cls_plus.Draw("AC,same")
myTH1_cls.Draw("AC,same")
myTH1_cls_min.Draw("AC,same")
myTH1_cls_2min.Draw("AC,same")

myTH1_cls_2plus.SetFillColor(kGreen)
myTH1_cls_plus.SetFillColor(kYellow)
myTH1_cls_min.SetFillColor(kGreen)
myTH1_cls_2min.SetFillColor(1001)

##################
### THE END :( ###
##################

### more statistical methods? see http://root.cern.ch/root/html/tutorials/roostats/index.html
