######################################################################################
######################################################################################
###                                                                                ### 
### fitRDS.py (TdP)                                                                ### 
###                                                                                ###  
### Analyze the RooDataSet produced by makeRDS.py to perform a Higgs search        ###
###                                                                                ###
### To do:                                                                         ###
### - check difference reco composite candidates (e.g. zbb vs home-brewn)          ###
### - get proper MC sample                                                         ###
### - allow for options to use both template and functional PDFs                   ###
### - factorize data-getting/pdf-making/fitting/plotting/etc...a bit less ugly ;-) ###
### - make profile likelihoods etc (using RooStats)                                ### 
###                                                                                ### 
######################################################################################
######################################################################################

import ROOT
from ROOT import *

gROOT.SetStyle("Plain")

### GET DATA ###

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

#########################
### MAKE SIGNAL PDF ### (analytic or template)
#########################

mean_bb  = RooRealVar("mean_bb", "mean_bb", 300,100,500)
sigma_bb = RooRealVar("sigma_bb","sigma_bb", 30, 10,100)

Sig_bb = RooGaussian("Sig_bb","Sig_bb",rrv_bb_M,mean_bb,sigma_bb)

#sig_bb_300 = RooGaussian("sig_bb_300","sig_bb_300",rrv_bb_M,RooFit.RooConst(300),RooFit.RooConst(25))
#sig_bb_400 = RooGaussian("sig_bb_400","sig_bb_400",rrv_bb_M,RooFit.RooConst(400),RooFit.RooConst(25))

#########################
### MAKE BACKGROUND PDF ### (analytic or template)
#########################

# RooKeysPdf* myRHP_b = new RooKeysPdf("myRHP_b","myRHP_b",*SV_m,*RDS_Zbb);
# RooKeysPdf* myRHP_c = new RooKeysPdf("myRHP_c","myRHP_c",*SV_m,*RDS_Zcc);
# RooKeysPdf* myRHP_l = new RooKeysPdf("myRHP_l","myRHP_l",*SV_m,*RDS_Zll);

rdh_zbb_MC_8_SV_M = RooDataHist("rdh_zbb_MC_8_SV_M", "rdh_zbb_MC_8_SV_M", RooArgSet(rrv_SV_M), rds_zbb_MC_8)
rdh_zbb_MC_8_bb_M = RooDataHist("rdh_zbb_MC_8_bb_M", "rdh_zbb_MC_8_bb_M", RooArgSet(rrv_bb_M), rds_zbb_MC_8)
rhp_zbb_MC_8_SV_M = RooHistPdf( "rhp_zbb_MC_8_SV_M", "rhp_zbb_MC_8_SV_M", RooArgSet(rrv_SV_M), rdh_zbb_MC_8_SV_M);
rhp_zbb_MC_8_bb_M = RooHistPdf( "rhp_zbb_MC_8_bb_M", "rhp_zbb_MC_8_bb_M", RooArgSet(rrv_bb_M), rdh_zbb_MC_8_bb_M);

rhp_zbb_MC_8_bb_M = RooKeysPdf("rhp_zbb_MC_8_bb_M","rhp_zbb_MC_8_bb_M", rrv_bb_M, rds_zbb_MC_8)

#RooDataHist* myRDH_c = new RooDataHist("myZc", "myRDH_Zc", RooArgSet(*SV_m), *RDS_Zcc);
#RooDataHist* myRDH_l = new RooDataHist("myZl", "myRDH_Zl", RooArgSet(*SV_m), *RDS_Zll);
#RooHistPdf* myRHP_c = new RooHistPdf("myRHP_c","myRHP_c",RooArgSet(*SV_m),*myRDH_c);
#RooHistPdf* myRHP_l = new RooHistPdf("myRHP_l","myRHP_l",RooArgSet(*SV_m),*myRDH_l);

#rhp_zbb_MC_8_bb_M

#bkg_yield = RooRealVar("bkg_yield","",25,0,300);
B_8=RooRealVar("B_8","B_8",0.2*rds_8.numEntries(),0,rds_8.numEntries())
bkg_bb = RooExtendPdf("bkg_ext_pdf","",rhp_zbb_MC_8_bb_M,B_8)#,bkg_yield)
   
bkg_bb.SetName("bkg_bb")

######################
### MAKE TOTAL PDF ###
######################

S_8=RooRealVar("S_8","N_{S}",0.8*rds_8.numEntries(),0,rds_8.numEntries())

Sum_bb = RooAddPdf("Sum_bb","Sum_bb",RooArgList(Sig_bb,bkg_bb),RooArgList(S_8,B_8))


#sum_bb_200 = RooAddPdf("sum_bb_200","sum_bb_200",RooArgList(sig_bb_200,bkg_bb),RooArgList(S_8,B_8))
#sum_bb_300 = RooAddPdf("sum_bb_300","sum_bb_300",RooArgList(sig_bb_300,bkg_bb),RooArgList(S_8,B_8))
#sum_bb_400 = RooAddPdf("sum_bb_400","sum_bb_400",RooArgList(sig_bb_400,bkg_bb),RooArgList(S_8,B_8))

Sum_bb.fitTo(rds_8,RooFit.Extended())

frame = rrv_bb_M.frame(0,600,12)#rrv_bb_M.getMax())
rds_8.plotOn(frame)
Sum_bb.plotOn(frame,RooFit.LineColor(kBlue))
Sum_bb.plotOn(frame,RooFit.Components("Sig_bb"),RooFit.LineColor(kGreen),RooFit.LineStyle(kDashed))
Sum_bb.plotOn(frame,RooFit.Components("bkg_bb"),RooFit.LineColor(kRed),  RooFit.LineStyle(kDashed))
Sum_bb.paramOn(frame,rds_8)
frame.Draw()


###########
### FIT ###
###########

#sum_bb.fitTo(rds_8,RooFit.Extended())

### more statistical methods? see http://root.cern.ch/root/html/tutorials/roostats/index.html

##########################
### PROFILE LIKELIHOOD ###
##########################

### see also http://root.cern.ch/root/html/tutorials/roostats/StandardProfileLikelihoodDemo.C.html

################################
### Make likelihood profiles ###
################################

# can do 2D (see below)
# 1D (number of signal events) should be sufficient

plc_S = RooStats.ProfileLikelihoodCalculator(rds_8,Sum_bb,RooArgSet(S_8))
plot_S = RooStats.LikelihoodIntervalPlot(plc_S.GetInterval())

C=TCanvas("C","C",400,350)

print "plotting likelihood of S alone"
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

for m in mList :
    print "Completed HybridCalculatorOriginal example"
    print "*** floating Higgs mass ***"
    print "*** m(Higgs)= ", m , " ***"
    print " - -2lnQ = " , min2lnQ_data[m] 
    print " - CL_sb = " , clsb_data[m]
    print " - CL_b  = " , clb_data[m]
    print " - CL_s  = " , cls_data[m]
    print " - CL_s 'error' = " , cls_error[m]
    print " - significance of data  = " , data_significance[m]
    print " - mean significance of toys  = " , toys_significance[m]

myTH1_cls      = TH1F("",   "",len(mList),min(mList)-25,max(mList)+25)
myTH1_cls_plus = TH1F("xxx","",len(mList),min(mList)-25,max(mList)+25)
myTH1_cls_min  = TH1F("yyy","",len(mList),min(mList)-25,max(mList)+25)
for x in range(1,len(mList)+1):
    myTH1_cls.SetBinContent(     x, 1-cls_data[mList[x-1]])
    myTH1_cls_plus.SetBinContent(x, 1-(cls_data[mList[x-1]]+cls_error[mList[x-1]]))
    myTH1_cls_min.SetBinContent( x, 1-(cls_data[mList[x-1]]-cls_error[mList[x-1]]))

g_cls      = TGraph(myTH1_cls)
g_cls_plus = TGraph(myTH1_cls_plus)
g_cls_min  = TGraph(myTH1_cls_min)

g_cls.GetYaxis().SetTitle("1-CL_{S}")
g_cls.GetXaxis().SetTitle("m_{H} (GeV/c^{2})")

g_cls.SetMaximum(1.)
g_cls_min.SetMaximum(1.)
g_cls_plus.SetMaximum(1.)
g_cls.SetMinimum(0.)
g_cls_min.SetMinimum(0.)
g_cls_plus.SetMinimum(0.)

Ccls = TCanvas("Ccls","Ccls",500,400)

g_cls.Draw("AC")
myTH1_cls.Draw("AC,same")
myTH1_cls_min.Draw("AC,same")
myTH1_cls_plus.Draw("AC,same")

bla

### save the toy-MC results to file, this way splitting into sub-batch jobs is possible
###TFile fileOut("some_hybridresult.root","RECREATE");
###fileOut.cd();
###myHybridResult.Write();
##fileOut.Close();

### read the results from a file
##TFile fileIn("some_hybridresult.root");
##HybridResult* myOtherHybridResult = (HybridResult*) fileIn.Get("myHybridCalc");

### example on how to merge with toy-MC results obtained in another job
##HybridResult* mergedHybridResult = new HybridResult("mergedHybridResult","this object holds merged results");
##mergedHybridResult->Add(myHybridResult);
##mergedHybridResult->Add(myOtherHybridResult);
## or
##myHybridResult->Add(myOtherHybridResult);



print "likelihood of dGG_s alone"

plc_dGG_s = RooStats.ProfileLikelihoodCalculator(data,myJpsiphiPdf,RooArgSet(dGG_s))
plot_dGG_s = RooStats.LikelihoodIntervalPlot(plc_dGG_s.GetInterval())

print "plotting likelihood of (dGG_s,Phi_s)"

print " ***************"
print " *** 3 sigma ***"
print " ***************"
plc_2D_99 = RooStats.ProfileLikelihoodCalculator(data,myJpsiphiPdf,RooArgSet(Phi_s,dGG_s))
plc_2D_99.SetTestSize(0.01)
plot_2D_99 = RooStats.LikelihoodIntervalPlot(plc_2D_99.GetInterval())
print " ***************"
print " *** 2 sigma ***"
print " ***************"
plc_2D_95 = RooStats.ProfileLikelihoodCalculator(data,myJpsiphiPdf,RooArgSet(Phi_s,dGG_s))
plc_2D_95.SetTestSize(0.05)
plot_2D_95 = RooStats.LikelihoodIntervalPlot(plc_2D_95.GetInterval())
print " ***************"
print " *** 1 sigma ***"
print " ***************"
plc_2D_68 = RooStats.ProfileLikelihoodCalculator(data,myJpsiphiPdf,RooArgSet(Phi_s,dGG_s))
plc_2D_68.SetTestSize(0.32)
plot_2D_68 = RooStats.LikelihoodIntervalPlot(plc_2D_68.GetInterval())

#"nominuit" option avoids:
#(1) possible problems in minimization using minuit: instead of looking for contour it scans whole 2D space
#(2) bug in axis labelling

C=TCanvas("C","C",1200,350)
C.Divide(3)

print "plotting likelihood of Phi_s alone"
C.cd(1)
#plot_Phi_s.Draw()
print "plotting likelihood of dGG_s alone"
C.cd(2)
#plot_dGG_s.Draw()

print "plotting likelihood of (dGG_s,Phi_s)"
C.cd(3)
print " ***************"
print " *** 3 sigma ***"
print " ***************"
plot_2D_99.SetContourColor(RooFit.kYellow)
#plot_2D_99.SetPrecision(0.001)# I don't understand this option
plot_2D_99.SetNPoints(10)
plot_2D_99.Draw("nominuit")
print " ***************"
print " *** 2 sigma ***"
print " ***************"
plot_2D_95.SetContourColor(RooFit.kOrange)
plot_2D_95.SetNPoints(10)
plot_2D_95.Draw("nominuit,same")
print " ***************"
print " *** 1 sigma ***"
print " ***************"
#plot_2D_68.SetContourColor(RooFit.kRed)
#plot_2D_68.SetNPoints(10)
#plot_2D_68.Draw("nominuit,same")



C.SaveAs("profLikelihood.eps")

print "Finished plotting"



################
### CLs SCAN ###
################

### http://root.cern.ch/root/html/tutorials/roostats/HybridInstructional.C.html

############
### PLOT ###
############


C4=TCanvas("C4","C4",900,900)
C4.Divide(2,2)

C4.cd(1)
frame_SV_M_4 = rrv_SV_M.frame(0,rrv_SV_M.getMax())
rds_4.plotOn(frame_SV_M_4)
frame_SV_M_4.Draw()

C4.cd(2)
frame_bb_M_4 = rrv_bb_M.frame(0,rrv_bb_M.getMax())
rds_4.plotOn(frame_bb_M_4)
frame_bb_M_4.Draw()

C4.cd(3)
frame_zeebb_M_4 = rrv_zeebb_M.frame(0,rrv_zeebb_M.getMax())
rds_4.plotOn(frame_zeebb_M_4)
frame_zeebb_M_4.Draw()

C4.cd(4)
frame_zmmbb_M_4 = rrv_zmmbb_M.frame(0,rrv_zmmbb_M.getMax())
rds_4.plotOn(frame_zmmbb_M_4)
frame_zmmbb_M_4.Draw()


C5=TCanvas("C5","C5",900,900)
C5.Divide(2,2)

C5.cd(1)
frame_SV_M_5 = rrv_SV_M.frame(0,rrv_SV_M.getMax())
rds_5.plotOn(frame_SV_M_5)
frame_SV_M_5.Draw()

C5.cd(2)
frame_bb_M_5 = rrv_bb_M.frame(0,rrv_bb_M.getMax())
rds_5.plotOn(frame_bb_M_5)
frame_bb_M_5.Draw()

C4.cd(3)
frame_zeebb_M_5 = rrv_zeebb_M.frame(0,rrv_zeebb_M.getMax())
rds_5.plotOn(frame_zeebb_M_5)
frame_zeebb_M_5.Draw()

C4.cd(4)
frame_zmmbb_M_5 = rrv_zmmbb_M.frame(0,rrv_zmmbb_M.getMax())
rds_5.plotOn(frame_zmmbb_M_5)
frame_zmmbb_M_5.Draw()


C8=TCanvas("C8","C8",900,900)
C8.Divide(2,2)

C8.cd(1)
frame_SV_M_8 = rrv_SV_M.frame(0,rrv_SV_M.getMax())
rds_8.plotOn(frame_SV_M_8)
frame_SV_M_8.Draw()

C8.cd(2)
frame_bb_M_8 = rrv_bb_M.frame(0,rrv_bb_M.getMax())
rds_8.plotOn(frame_bb_M_8)
frame_bb_M_8.Draw()

C8.cd(3)
frame_zeebb_M_8 = rrv_zeebb_M.frame(0,rrv_zeebb_M.getMax())
rds_8.plotOn(frame_zeebb_M_8)
frame_zeebb_M_8.Draw()

C8.cd(4)
frame_zmmbb_M_8 = rrv_zmmbb_M.frame(0,rrv_zmmbb_M.getMax())
rds_8.plotOn(frame_zmmbb_M_8)
frame_zmmbb_M_8.Draw()


C9=TCanvas("C9","C9",900,900)
C9.Divide(3)

C9.cd(1)
frame_SV_M_9 = rrv_SV_M.frame(0,rrv_SV_M.getMax())
rds_9.plotOn(frame_SV_M_9)
frame_SV_M_9.Draw()

C9.cd(2)
frame_bb_M_9 = rrv_bb_M.frame(0,rrv_bb_M.getMax())
rds_9.plotOn(frame_bb_M_9)
frame_bb_M_9.Draw()

C9.cd(3)
frame_zeebb_M_9 = rrv_zeebb_M.frame(0,rrv_zeebb_M.getMax())
rds_9.plotOn(frame_zeebb_M_9)
frame_zeebb_M_9.Draw()

C9.cd(4)
frame_zmmbb_M_9 = rrv_zmmbb_M.frame(0,rrv_zmmbb_M.getMax())
rds_9.plotOn(frame_zmmbb_M_9)
frame_zmmbb_M_9.Draw()

#data     = sum_bb.generate(RooArgSet(rrv_bb_M),RooFit.Extended())
#data_200 = sum_bb_200.generate(RooArgSet(rrv_bb_M),RooFit.Extended())
#data_300 = sum_bb_300.generate(RooArgSet(rrv_bb_M),RooFit.Extended())
#data_400 = sum_bb_400.generate(RooArgSet(rrv_bb_M),RooFit.Extended())
#myHybridCalc     = RooStats.HybridCalculatorOriginal(data, sum_bb , bkg_bb ,RooArgSet())
#myHybridCalc_200 = RooStats.HybridCalculatorOriginal(data_200, sum_bb_200 , bkg_bb ,RooArgSet())
#myHybridCalc_300 = RooStats.HybridCalculatorOriginal(data_300, sum_bb_300 , bkg_bb ,RooArgSet())
#myHybridCalc_400 = RooStats.HybridCalculatorOriginal(data_400, sum_bb_400 , bkg_bb ,RooArgSet())
