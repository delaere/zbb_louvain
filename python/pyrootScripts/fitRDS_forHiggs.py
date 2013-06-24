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

################
### GET DATA ###
################

f_Zbb = TFile("File_rds_zbb_el.root")
ws_Zbb = f_Zbb.Get("ws")
rds_zbb     = ws_Zbb.data("rds_zbb")

f_Zmmbb = TFile("File_rds_zbb_mu.root")
ws_Zmmbb = f_Zmmbb.Get("ws")
rds_zmmbb     = ws_Zmmbb.data("rds_zbb")

rds_zbb.append(rds_zmmbb)

rrv_SV_M    = ws_Zbb.var("rrv_SV_M")
rrv_bb_M    = ws_Zbb.var("rrv_bb_M")
rrv_bb_M.SetTitle("m(bb) (GeV/c^{2})")
rrv_zbb_M   = ws_Zbb.var("rrv_zbb_M")
rrv_zeebb_M = ws_Zbb.var("rrv_zeebb_M")
rrv_zmmbb_M = ws_Zbb.var("rrv_zmmbb_M")
rc_cat     = ws_Zbb.var("rc_cat")

rds_4 = rds_zbb.reduce("rc_cat>=4") #Zj
rds_5 = rds_zbb.reduce("rc_cat>=5") #ZbHE
rds_6 = rds_zbb.reduce("rc_cat>=6") #ZbHEMET
rds_7 = rds_zbb.reduce("rc_cat>=7") #ZbHPMET
rds_8 = rds_zbb.reduce("rc_cat>=8") #ZbbHPHE
rds_9 = rds_zbb.reduce("rc_cat>=9") #ZbbHPHP

print "############################"
print "#Events level 4 = ", rds_4.numEntries() 
print "#Events level 5 = ", rds_5.numEntries() 
print "#Events level 6 = ", rds_6.numEntries() 
print "#Events level 7 = ", rds_7.numEntries() 
print "#Events level 8 = ", rds_8.numEntries() 
print "#Events level 9 = ", rds_9.numEntries() 
print "############################"

#########################
### GET BACKGROUND MC ###
#########################

f_zbb_MC    = TFile("File_rds_zbb_muMC.root")
ws_zbb_MC   = f_zbb_MC.Get("ws")
rds_zbb_MC  = ws_zbb_MC.data("rds_zbb")

rds_zbb_MC_8 = rds_zbb_MC.reduce("rc_cat>=8") #ZbbHPHE
rds_zbb_MC_9 = rds_zbb_MC.reduce("rc_cat>=9") #ZbbHPHP

##############################################
### MAKE SIGNAL PDF (analytic or template) ###
##############################################

mean_bb  = RooRealVar("mean_bb", "mean_bb", 300,100,500)
sigma_bb = RooRealVar("sigma_bb","sigma_bb", 30, 10,100)

Sig_bb = RooGaussian("Sig_bb","Sig_bb",rrv_bb_M,mean_bb,sigma_bb)

##################################################
### MAKE BACKGROUND PDF (analytic or template) ###
##################################################

rdh_zbb_MC_8_SV_M = RooDataHist("rdh_zbb_MC_8_SV_M", "rdh_zbb_MC_8_SV_M", RooArgSet(rrv_SV_M), rds_zbb_MC_8)
rdh_zbb_MC_8_bb_M = RooDataHist("rdh_zbb_MC_8_bb_M", "rdh_zbb_MC_8_bb_M", RooArgSet(rrv_bb_M), rds_zbb_MC_8)
rhp_zbb_MC_8_SV_M = RooHistPdf( "rhp_zbb_MC_8_SV_M", "rhp_zbb_MC_8_SV_M", RooArgSet(rrv_SV_M), rdh_zbb_MC_8_SV_M);
rhp_zbb_MC_8_bb_M = RooHistPdf( "rhp_zbb_MC_8_bb_M", "rhp_zbb_MC_8_bb_M", RooArgSet(rrv_bb_M), rdh_zbb_MC_8_bb_M);

rhp_zbb_MC_8_bb_M = RooKeysPdf("rhp_zbb_MC_8_bb_M","rhp_zbb_MC_8_bb_M", rrv_bb_M, rds_zbb_MC_8)

#bkg_yield = RooRealVar("bkg_yield","",25,0,300);
B_8=RooRealVar("B_8","B_8",0.2*rds_8.numEntries(),0,rds_8.numEntries())
bkg_bb = RooExtendPdf("bkg_ext_pdf","",rhp_zbb_MC_8_bb_M,B_8)#,bkg_yield)
   
bkg_bb.SetName("bkg_bb")

######################
### MAKE TOTAL PDF ###
######################

S_8=RooRealVar("S_8","N_{S}",0.8*rds_8.numEntries(),0,rds_8.numEntries())

Sum_bb = RooAddPdf("Sum_bb","Sum_bb",RooArgList(Sig_bb,bkg_bb),RooArgList(S_8,B_8))

###########
### FIT ###
###########

### more statistical methods? see http://root.cern.ch/root/html/tutorials/roostats/index.html

Sum_bb.fitTo(rds_8,RooFit.Extended())

frame = rrv_bb_M.frame(0,600,12)#rrv_bb_M.getMax())
rds_8.plotOn(frame)
Sum_bb.plotOn(frame,RooFit.LineColor(kBlue))
Sum_bb.plotOn(frame,RooFit.Components("Sig_bb"),RooFit.LineColor(kGreen),RooFit.LineStyle(kDashed))
Sum_bb.plotOn(frame,RooFit.Components("bkg_bb"),RooFit.LineColor(kRed),  RooFit.LineStyle(kDashed))
Sum_bb.paramOn(frame,rds_8)

C_fit=TCanvas("C_fit","C_fit",800,700)
frame.Draw()

##########################
### PROFILE LIKELIHOOD ###
##########################

### see also http://root.cern.ch/root/html/tutorials/roostats/StandardProfileLikelihoodDemo.C.html

# can also do 2D 
# 1D (number of signal events) should be sufficient

plc_S = RooStats.ProfileLikelihoodCalculator(rds_8,Sum_bb,RooArgSet(S_8))
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
