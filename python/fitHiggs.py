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

WP =  "HEHE"        #"HP","HPMET","HP_excl","HE","HEMET","HE_excl"
channel = "Mu"
sel= {"Mu":"muSel",
      "El":"elSel"}

TtbarMC = "Ttbar_"+channel+"_MC"
Data    = channel+"_DATA"
DYMC    = channel+"_MC"

file = {  Data    : TFile("File_rds_zbb_"+Data+".root"),
          DYMC    : TFile("File_rds_zbb_"+DYMC+".root"),
          TtbarMC : TFile("File_rds_zbb_"+TtbarMC+".root")
          }
                    
#file = {  Data    : TFile("File_rds_zbb_"+Data+"_"+sel[channel]+".root"),
#          DYMC    : TFile("File_rds_zbb_"+DYMC+"_"+sel[channel]+".root"),
#          TtbarMC : TFile("File_rds_zbb_"+TtbarMC+"_"+sel[channel]+".root")
#                    }

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

rrv_SV_M    = ws[Data].var("rrv_SV_M")
rrv_bb_M    = ws[Data].var("rrv_bb_M")
rrv_bb_M.SetTitle("m(bb) (GeV/c^{2})")
rrv_zbb_M   = ws[Data].var("rrv_zbb_M")
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

mean_bb  = RooRealVar("mean_bb", "mean_bb", 300,100,500)
sigma_bb = RooRealVar("sigma_bb","sigma_bb", 30, 10,100)
Sig_bb = RooGaussian("Sig_bb","Sig_bb",rrv_bb_M,mean_bb,sigma_bb)

S = RooRealVar("S","S",10,0,30)

sig_pdf = RooExtendPdf("sig_pdf",
                       "sig_pdf",
                       Sig_bb,
                       S)

##################################################
### MAKE BACKGROUND PDF (analytic or template) ###
##################################################

rdh_zbb_MC_bb_M = {}
rhp_zbb_MC_bb_M = {}

rdh_zbb_MC_bb_M[DYMC]    = RooDataHist("rdh_zbb_MC_bb_M"+DYMC,
                                       "rdh_zbb_MC_SV_M"+DYMC,
                                       RooArgSet(rrv_bb_M),
                                       myRDS[DYMC])
rdh_zbb_MC_bb_M[TtbarMC] = RooDataHist("rdh_zbb_MC_bb_M"+TtbarMC,
                                       "rdh_zbb_MC_bb_M"+TtbarMC,
                                        RooArgSet(rrv_bb_M),
                                        myRDS[TtbarMC])
rhp_zbb_MC_bb_M[DYMC]    = RooHistPdf( "rhp_zbb_MC_bb_M"+DYMC,
                                       "rhp_zbb_MC_bb_M"+DYMC,
                                        RooArgSet(rrv_bb_M),
                                        rdh_zbb_MC_bb_M[DYMC])
rhp_zbb_MC_bb_M[TtbarMC] = RooHistPdf( "rhp_zbb_MC_bb_M"+TtbarMC,
                                       "rhp_zbb_MC_bb_M"+TtbarMC,
                                        RooArgSet(rrv_bb_M),
                                        rdh_zbb_MC_bb_M[TtbarMC])

#rhp_zbb_MC_8_bb_M = RooKeysPdf("rhp_zbb_MC_8_bb_M","rhp_zbb_MC_8_bb_M", rrv_bb_M, rds_zbb_MC_8)

B={}

B[DYMC]    = RooRealVar("B"+DYMC,   "B"+DYMC,   myRDS[DYMC].numEntries()*2/11.8)
B[TtbarMC] = RooRealVar("B"+TtbarMC,"B"+TtbarMC,myRDS[TtbarMC].numEntries()*(2/23)/10)

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

###########
### FIT ###
###########

### more statistical methods? see http://root.cern.ch/root/html/tutorials/roostats/index.html

Sum_bb.fitTo(DATA,RooFit.Extended())

frame = rrv_bb_M.frame(0,600,12)#rrv_bb_M.getMax())
DATA.plotOn(frame)
Sum_bb.plotOn(frame,RooFit.LineColor(kBlue))
Sum_bb.plotOn(frame,RooFit.Components("Sig_bb"),RooFit.LineColor(kGreen),RooFit.LineStyle(kDashed))
Sum_bb.plotOn(frame,RooFit.Components("bkg_bb"),RooFit.LineColor(kRed),  RooFit.LineStyle(kDashed))
Sum_bb.paramOn(frame,DATA)

C_fit=TCanvas("C_fit","C_fit",800,700)
frame.Draw()

##########################
### PROFILE LIKELIHOOD ###
##########################

### see also http://root.cern.ch/root/html/tutorials/roostats/StandardProfileLikelihoodDemo.C.html

# can also do 2D 
# 1D (number of signal events) should be sufficient

plc_S = RooStats.ProfileLikelihoodCalculator(DATA,Sum_bb,RooArgSet(S_8))
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

mList = (200,250,300,350,400)

for m in mList :
    sig_bb[m] = RooGaussian("sig_bb_"+str(m),"sig_bb_"+str(m),rrv_bb_M,RooFit.RooConst(m),RooFit.RooConst(25))
    sum_bb[m] = RooAddPdf("sum_bb_"+str(m),"sum_bb_"+str(m),RooArgList(sig_bb[m],bkg_bb),RooArgList(S_8,B_8))
    ### generate a data sample
    data[m] = sum_bb[m].generate(RooArgSet(rrv_bb_M),RooFit.Extended())
    ### run HybridCalculator on those inputs
    ### use interface from HypoTest calculator by default
    myHybridCalc[m] = RooStats.HybridCalculatorOriginal(data[m], sum_bb[m], bkg_bb ,RooArgSet())
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
