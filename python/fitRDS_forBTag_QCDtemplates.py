
#######################################################
#
# Loop over entries
#
# Loop over jets per event
#
# Get flavor, pt, eta and select jets
#
# Get PV, pT, pTHat and determine per-event weight
#
# Save in a RooDataSet
#   - m(SV)
#   - PV-cat, pT-cat, pThat-cat
#   - weight
#
# (c) Zbb-CP3 Warriors, 2011
#
####################################################

from ROOT import *
import os

gROOT.SetStyle("Plain")
gStyle.SetErrorX(0)

WP       = "HE"   #"HP","HPMET","HP_excl","HE","HEmet","He_excl"
channel  = "El"   #"El","Mu"
template = "hist" #"keys", "hist"
jec      = 0      #1,3,5  
numbins  = 40     #20,40,80

### Getting a file and a tree

file  = TFile("bTagPurRDS_QCD_5.root")
ws    = file.Get("ws")
myRDS = ws.data("myRDS");

myRDS = myRDS.reduce("rrv_pT>25")
myRDS = myRDS.reduce("rrv_eta<2.1")
myRDS = myRDS.reduce("rrv_eta>-2.1")

print "myRDS.numEntries() = ", myRDS.numEntries()

rrv_msv    = ws.var("rrv_msv")
rrv_bTagHE = ws.var("rrv_bTagHE")
rrv_bTagHP = ws.var("rrv_bTagHP")
rrv_pT     = ws.var("rrv_pT")
rrv_eta    = ws.var("rrv_eta")
rrv_nPV    = ws.var("rrv_nPV")
rrv_pT_unc = ws.var("rrv_pT_unc")
rc_flav    = ws.cat("rc_flav")
rc_sel     = ws.cat("rc_sel")

rrv_pT.setMin(25)
rrv_pT.setMax(150)
rrv_pT.setBins(25)

rrv_eta.setMin(-2.1)
rrv_eta.setMax( +2.1)
rrv_eta.setBins( 21)

rrv_msv.setMin(0)
rrv_msv.setMax(10)
rrv_msv.setBins(numbins)

rrv_nPV.setMin(0)
rrv_nPV.setMax(20)
rrv_nPV.setBins(20)

f_data = 0
if channel == "El"  : f_data = TFile("File_rds_zbb_El_DATA_elSel_forBTag.root")
elif channel == "Mu" : f_data = TFile("File_rds_zbb_Mu_DATA_muSel_forBTag.root")

ws_data=f_data.Get("ws")
DATA = ws_data.data("rds_zbb")

#DATA = DATA.reduce("rrv_nPV>7.5")
#DATA = DATA.reduce("rrv_nPV<7.5")

if WP=="HE"         :    DATA = DATA.reduce("rc_HE==1")
if WP=="HEMET"      :    DATA = DATA.reduce("rc_HEMET==1")
if WP=="HE_excl"    :    DATA = DATA.reduce("rc_HE_excl==1")
if WP=="HEMET_excl" :    DATA = DATA.reduce("rc_HEMET_excl==1")
if WP=="HP"         :    DATA = DATA.reduce("rc_HP==1")
if WP=="HPMET"      :    DATA = DATA.reduce("rc_HPMET==1")
if WP=="HP_excl"    :    DATA = DATA.reduce("rc_HP_excl==1")
if WP=="HPMET_excl" :    DATA = DATA.reduce("rc_HPMET_excl==1")

print "DATA.numEntries() = ", DATA.numEntries()


RAS = DATA.get()
DATA_withunc = RooDataSet("rds_zbb_with_unc","rds_zbb_with_unc",RAS)

for i in range(0,DATA.numEntries()):
    RASi = DATA.get(i)
    ptVal = RASi.getRealValue("rrv_pT")
    ptuncVal = RASi.getRealValue("rrv_pT_unc")*ptVal
    RAS.setRealValue("rrv_pT",ptVal+jec*ptuncVal)
    DATA_withunc.add(RAS)

DATA = DATA_withunc

if WP[:2]=="HP":  myRDS = myRDS.reduce("rc_sel==6")

#myRDS.tree().Draw("rrv_msv")

myRDS_l = myRDS.reduce("rc_flav==1")
myRDS_c = myRDS.reduce("rc_flav==4")
myRDS_b = myRDS.reduce("rc_flav==5")
#myRDS_g = myRDS.reduce("rc_flav==6")

print "myRDS_l.numEntries() = ", myRDS_l.numEntries()
print "myRDS_c.numEntries() = ", myRDS_c.numEntries()
print "myRDS_b.numEntries() = ", myRDS_b.numEntries()
#print "myRDS_g.numEntries() = ", myRDS_g.numEntries()

### This takes too long:
#print "redduced datasets, making keys"
#myRKP   = RooKeysPdf("myRKP",  "myRKP",  rrv_msv,myRDS)
#print "making b-keys"
#myRKP_b = RooKeysPdf("myRKP_b","myRKP_b",rrv_msv,myRDS_l)
#print "making c-keys"
#myRKP_c = RooKeysPdf("myRKP_c","myRKP_c",rrv_msv,myRDS_c)
#print "making l-keys"
#myRKP_l = RooKeysPdf("myRKP_l","myRKP_l",rrv_msv,myRDS_b)

print "making roodatahist"

myRDH   = RooDataHist("myRDH",   "myRDH",   RooArgSet(rrv_msv), myRDS  )
myRDH_b = RooDataHist("myRDH_b", "myRDH_b", RooArgSet(rrv_msv), myRDS_b)
#myRDH_g = RooDataHist("myRDH_g", "myRDH_g", RooArgSet(rrv_msv), myRDS_g)
myRDH_c = RooDataHist("myRDH_c", "myRDH_c", RooArgSet(rrv_msv), myRDS_c)
myRDH_l = RooDataHist("myRDH_l", "myRDH_l", RooArgSet(rrv_msv), myRDS_l)

print "made datahists, making histpdfs"

myRHP   = RooHistPdf("myRHP",  "myRHP",  RooArgSet(rrv_msv),myRDH  )
myRHP_b = RooHistPdf("myRHP_b","myRHP_b",RooArgSet(rrv_msv),myRDH_b)
#myRHP_g = RooHistPdf("myRHP_g","myRHP_g",RooArgSet(rrv_msv),myRDH_g)
myRHP_c = RooHistPdf("myRHP_c","myRHP_c",RooArgSet(rrv_msv),myRDH_c)
myRHP_l = RooHistPdf("myRHP_l","myRHP_l",RooArgSet(rrv_msv),myRDH_l)

print "made histpdfs, going to plot"

freem1 = rrv_msv.frame()
myRDS_b.plotOn(freem1,RooFit.MarkerColor(kRed),RooFit.LineColor(kRed)) 
myRDH_b.plotOn(freem1,RooFit.MarkerColor(kRed),RooFit.LineColor(kRed)) 
myRHP_b.plotOn(freem1,RooFit.MarkerColor(kRed),RooFit.LineColor(kRed)) 
freem2 = rrv_msv.frame()
myRDS_c.plotOn(freem2,RooFit.MarkerColor(kGreen),RooFit.LineColor(kGreen)) 
myRDH_c.plotOn(freem2,RooFit.MarkerColor(kGreen),RooFit.LineColor(kGreen)) 
myRHP_c.plotOn(freem2,RooFit.MarkerColor(kGreen),RooFit.LineColor(kGreen)) 
freeem3 = rrv_msv.frame()
myRDS_l.plotOn(freeem3,RooFit.MarkerColor(kBlue),RooFit.LineColor(kBlue)) 
myRDH_l.plotOn(freeem3,RooFit.MarkerColor(kBlue),RooFit.LineColor(kBlue)) 
myRHP_l.plotOn(freeem3,RooFit.MarkerColor(kBlue),RooFit.LineColor(kBlue)) 

pTRegion  = RooThresholdCategory("pTRegion", "region of pT", rrv_pT, "pT") 
etaRegion = RooThresholdCategory("etaRegion","region of eta",rrv_eta,"eta") 
npvRegion = RooThresholdCategory("npvRegion","region of nPV",rrv_nPV,"nPV") 

# Specify thresholds and state assignments one-by-one.
# Each statement specifies that all values _below_ the given value
# (and above any lower specified threshold) are mapped to the
# category state with the given name
#
# Background | SideBand | Signal | SideBand | Background
#     4.23       5.23     8.23       9.23
pTRegion.addThreshold(             35, "1") 
pTRegion.addThreshold(             45, "2") 
pTRegion.addThreshold(             65, "3") 
pTRegion.addThreshold(            150, "4") 
pTRegion.addThreshold(rrv_pT.getMax(), "5") 

etaRegion.addThreshold(            3., "1")

#etaRegion.addThreshold(            -1., "1") 
#etaRegion.addThreshold(             1., "2") 
#etaRegion.addThreshold(rrv_eta.getMax(), "3") 

#npvRegion.addThreshold(             15, "1") 

npvRegion.addThreshold(             4.5, "1") 
npvRegion.addThreshold(             7.5, "2") 
npvRegion.addThreshold(             20., "3") 
#npvRegion.addThreshold(             6.5, "3") 
#npvRegion.addThreshold(             8.5, "4") 
#npvRegion.addThreshold(rrv_nPV.getMax(), "5") 

# Add values of threshold function to dataset so that it can be used as observable
myRDS.addColumn(pTRegion) 
myRDS_b.addColumn(pTRegion) 
#myRDS_g.addColumn(pTRegion) 
myRDS_c.addColumn(pTRegion) 
myRDS_l.addColumn(pTRegion) 
DATA.addColumn(pTRegion) 

myRDS.addColumn(etaRegion) 
myRDS_b.addColumn(etaRegion) 
#myRDS_g.addColumn(etaRegion) 
myRDS_c.addColumn(etaRegion) 
myRDS_l.addColumn(etaRegion) 
DATA.addColumn(etaRegion) 

myRDS.addColumn(npvRegion) 
myRDS_b.addColumn(npvRegion) 
#myRDS_g.addColumn(npvRegion) 
myRDS_c.addColumn(npvRegion) 
myRDS_l.addColumn(npvRegion) 
DATA.addColumn(npvRegion) 


RDS_per_pT = {}

RDS_b_per_pT = {}
#RDS_g_per_pT = {}
RDS_c_per_pT = {}
RDS_l_per_pT = {}

RKP_b_per_pT = {}
#RKP_g_per_pT = {}
RKP_c_per_pT = {}
RKP_l_per_pT = {}

myRDH_b = {}
#myRDH_g = {}
myRDH_c = {}
myRDH_l = {}

myRHP_b = {}
#myRHP_g = {}
myRHP_c = {}
myRHP_l = {}

#myRKP_g = {}
myRKP_b = {}
myRKP_c = {}
myRKP_l = {}

b_pdfList = RooArgList()
g_pdfList = RooArgList()
c_pdfList = RooArgList()
l_pdfList = RooArgList()

f_b={}
fracList = RooArgList()


DATA_per_pT = {}

### TODO: add #PV, eta
### First produce them also in data
### (Long term: properly produce data/MC RooDataSets in same way)

rrv_weight = RooRealVar("weight","weight",0)

RDS_weighted_per_pT = {}

for i in range(1,5):
    for j in range(1,2):
        for k in range(1,4):

            str_i = "pTRegion==pTRegion::"+str(i)
            str_j = "etaRegion==etaRegion::"+str(j)
            str_k = "npvRegion==npvRegion::"+str(k)
            #str_ijk = "pTRegion==pTRegion::"+str(i)+",etaRegion==etaRegion::"+str(j)+",npvRegion==npvRegion::"+str(k)
            print "str_i = ", str_i
            print "str_j = ", str_j
            
            RDS_per_pT[i,j,k]    = myRDS.reduce(str_i)
            RDS_per_pT[i,j,k]    = RDS_per_pT[i,j,k].reduce(str_j)
            RDS_per_pT[i,j,k]    = RDS_per_pT[i,j,k].reduce(str_k)
            
            print "RDS_per_pT[", i , j, k, "].numEntries() = ", RDS_per_pT[i,j,k].numEntries()

            RDS_b_per_pT[i,j,k]  = myRDS_b.reduce(str_i)
            RDS_b_per_pT[i,j,k]  = RDS_b_per_pT[i,j,k].reduce(str_j)
            RDS_b_per_pT[i,j,k]  = RDS_b_per_pT[i,j,k].reduce(str_k)
            print "RDS_b_per_pT[",i , "," , j , ",", k ,"].numEntries() = ",   RDS_b_per_pT[i,j,k].numEntries()
            
            #RDS_g_per_pT[i,j,k]  = myRDS_g.reduce(str_i)
            #RDS_g_per_pT[i,j,k]  = RDS_g_per_pT[i,j,k].reduce(str_j)
            #RDS_g_per_pT[i,j,k]  = RDS_g_per_pT[i,j,k].reduce(str_k)
            
            RDS_c_per_pT[i,j,k]  = myRDS_c.reduce(str_i)
            RDS_c_per_pT[i,j,k]  = RDS_c_per_pT[i,j,k].reduce(str_j)
            RDS_c_per_pT[i,j,k]  = RDS_c_per_pT[i,j,k].reduce(str_k)
            print "RDS_c_per_pT[",i , "," , j , ",", k ,"].numEntries() = ",   RDS_c_per_pT[i,j,k].numEntries()
            
            RDS_l_per_pT[i,j,k]  = myRDS_l.reduce(str_i) 
            RDS_l_per_pT[i,j,k]  = RDS_l_per_pT[i,j,k].reduce(str_j) 
            RDS_l_per_pT[i,j,k]  = RDS_l_per_pT[i,j,k].reduce(str_k) 
            print "RDS_l_per_pT[",i , "," , j , ",", k ,"].numEntries() = ",   RDS_l_per_pT[i,j,k].numEntries()

            DATA_per_pT[i,j,k] = DATA.reduce(str_i)
            DATA_per_pT[i,j,k] = DATA_per_pT[i,j,k].reduce(str_j)
            DATA_per_pT[i,j,k] = DATA_per_pT[i,j,k].reduce(str_k)
            print "DATA_per_pT[",i , "," , j , ",", k ,"].numEntries() = ",   DATA_per_pT[i,j,k].numEntries()
            
            #RKP_per_pT[i]    = RooKeysPdf("RKP_per_pT"+str(i),  "RKP_per_pT"+str(i),rrv_msv,RDS_per_pT[i])

            myRKP_b[i,j,k]  = RooKeysPdf("RKP_b_per_pT"+str(i)+str(j)+str(k),
                                         "RKP_b_per_pT"+str(i)+str(j)+str(k),
                                         rrv_msv,
                                         RDS_b_per_pT[i,j,k])
            #myRKP_g[i,j,k]  = RooKeysPdf("RKP_g_per_pT"+str(i)+str(j)+str(k),
            #                             "RKP_g_per_pT"+str(i)+str(j)+str(k),
            #                             rrv_msv,
            #                             RDS_g_per_pT[i,j,k])
            myRKP_c[i,j,k]  = RooKeysPdf("RKP_c_per_pT"+str(i)+str(j)+str(k),
                                         "RKP_c_per_pT"+str(i)+str(j)+str(k),
                                         rrv_msv,
                                         RDS_c_per_pT[i,j,k])
            myRKP_l[i,j,k]  = RooKeysPdf("RKP_l_per_pT"+str(i)+str(j)+str(k),
                                         "RKP_l_per_pT"+str(i)+str(j)+str(k),
                                         rrv_msv,
                                         RDS_l_per_pT[i,j,k])

           #myRDH   = RooDataHist("myRDH",   "myRDH",   RooArgSet(rrv_msv), myRDS  )
            myRDH_b[i,j,k] = RooDataHist("myRDH_b"+str(i)+str(j)+str(k), "myRDH_b"+str(i)+str(j)+str(k), RooArgSet(rrv_msv), RDS_b_per_pT[i,j,k])
            #myRDH_g[i,j,k] = RooDataHist("myRDH_g"+str(i)+str(j)+str(k), "myRDH_g"+str(i)+str(j)+str(k), RooArgSet(rrv_msv), RDS_g_per_pT[i,j,k])
            myRDH_c[i,j,k] = RooDataHist("myRDH_c"+str(i)+str(j)+str(k), "myRDH_c"+str(i)+str(j)+str(k), RooArgSet(rrv_msv), RDS_c_per_pT[i,j,k])
            myRDH_l[i,j,k] = RooDataHist("myRDH_l"+str(i)+str(j)+str(k), "myRDH_l"+str(i)+str(j)+str(k), RooArgSet(rrv_msv), RDS_l_per_pT[i,j,k])

            print "made datahists, making histpdfs"
    
            #myRHP   = RooHistPdf("myRHP",  "myRHP",  RooArgSet(rrv_msv),myRDH  )
            myRHP_b[i,j,k] = RooHistPdf("myRHP_b"+str(i)+str(j)+str(k),"myRHP_b"+str(i)+str(j)+str(k),RooArgSet(rrv_msv),myRDH_b[i,j,k])
            #myRHP_g[i,j,k] = RooHistPdf("myRHP_g"+str(i)+str(j)+str(k),"myRHP_g"+str(i)+str(j)+str(k),RooArgSet(rrv_msv),myRDH_g[i,j,k])
            myRHP_c[i,j,k] = RooHistPdf("myRHP_c"+str(i)+str(j)+str(k),"myRHP_c"+str(i)+str(j)+str(k),RooArgSet(rrv_msv),myRDH_c[i,j,k])
            myRHP_l[i,j,k] = RooHistPdf("myRHP_l"+str(i)+str(j)+str(k),"myRHP_l"+str(i)+str(j)+str(k),RooArgSet(rrv_msv),myRDH_l[i,j,k])


            print "DATA_per_pT[", i , j, k, "].numEntries() = ", DATA_per_pT[i,j,k].numEntries()

            f_b[i,j,k] = RooConstVar("f"+str(i)+str(j)+str(k),
                                     "f"+str(i)+str(j)+str(k),
                                     RDS_per_pT[i,j,k].numEntries()*1.0/DATA_per_pT[i,j,k].numEntries())
            print "frac ", i,j,k, " = ", f_b[i,j,k].getVal()
            fracList.add(f_b[i,j,k])

            b_pdfList.add(myRKP_b[i,j,k])
            #g_pdfList.add(myRKP_g[i,j,k])
            c_pdfList.add(myRKP_c[i,j,k])
            l_pdfList.add(myRKP_l[i,j,k])

            rrv_weight.setVal(1./f_b[i,j,k].getVal())
            RDS_per_pT[i,j,k].addColumn(rrv_weight)
            print "weight = ", 1./f_b[i,j,k].getVal()

# Make plot of data in x
# Use calculated category to select sideband data
testframe = rrv_msv.frame()
myRDS.plotOn(testframe)
myRDS.plotOn(testframe,RooFit.Cut("pTRegion==pTRegion::1"),RooFit.MarkerColor(kRed),RooFit.LineColor(kRed)) 
                  

RDS_per_pT[1,1,1].plotOn(testframe,RooFit.MarkerColor(kRed),RooFit.LineColor(kRed)) 
RDS_per_pT[2,1,1].plotOn(testframe,RooFit.MarkerColor(kBlue),RooFit.LineColor(kBlue)) 

testframe.Draw()

#Can.cd(4)#
#
#testframe2 = rrv_msv.frame()#
#
#RDS_per_pT[1].plotOn(testframe2,RooFit.MarkerColor(kRed),RooFit.LineColor(kRed)) 
##RKP_per_pT[1].plotOn(testframe2,RooFit.LineColor(kRed)) 
#RDS_per_pT[2].plotOn(testframe2,RooFit.MarkerColor(kBlue),RooFit.LineColor(kBlue)) 
##RKP_per_pT[2].plotOn(testframe2,RooFit.LineColor(kBlue)) 
#testframe2.Draw()



#thresholdList = RooArgList(RooConstVar("t0","t0",rrv_pT.getMin()),
#                           RooConstVar("t1","t1",30),
#                           RooConstVar("t2","t2",50),
#                           RooConstVar("t3","t3",80),
#                           RooConstVar("t4","t4",150))




RDS_sum = RooDataSet("RDS_sum","RDS_sum",RDS_per_pT[i,j,k].get())
for i in range(1,5):
    for j in range(1,2):
        for k in range(1,4):
            RDS_sum.append(RDS_per_pT[i,j,k])

RDS_sum_weighted = RooDataSet("RDS_sum_weighted",
                              "RDS_sum_weighted",
                              RDS_sum,
                              RDS_sum.get(),
                              "",
                              "weight")

RDH_tot          = RooDataHist("myRDH_tot",   "myRDH_tot",   RooArgSet(rrv_pT,rrv_nPV,rrv_eta), RDS_sum)
RDH_tot_weighted = RooDataHist("myRDH_tot_w", "myRDH_tot_w", RooArgSet(rrv_pT,rrv_nPV,rrv_eta), RDS_sum_weighted)
RHP_tot          = RooHistPdf( "myRHP_tot",   "myRHP_tot",   RooArgSet(rrv_pT,rrv_nPV,rrv_eta), RDH_tot  )
RHP_tot_weighted = RooHistPdf( "myRHP_tot_w", "myRHP_tot_w", RooArgSet(rrv_pT,rrv_nPV,rrv_eta), RDH_tot_weighted)

Cee=TCanvas("Cee","Cee",600,1000)
Cee.Divide(2,3)

Cee.cd(1)
FRAME1 = rrv_pT.frame()
DATA.plotOn(FRAME1)
RHP_tot.plotOn(FRAME1,RooFit.LineColor(kRed))
RHP_tot_weighted.plotOn(FRAME1,RooFit.LineColor(kGreen))
FRAME1.Draw()

Cee.cd(2).SetLogy()
FRAME2 = rrv_pT.frame()
DATA.plotOn(FRAME2)
RHP_tot.plotOn(FRAME2,RooFit.LineColor(kRed))
RHP_tot_weighted.plotOn(FRAME2,RooFit.LineColor(kGreen))
FRAME2.Draw()

Cee.cd(3)
FRAME3 = rrv_eta.frame()
DATA.plotOn(FRAME3)
RHP_tot.plotOn(FRAME3,RooFit.LineColor(kRed))
RHP_tot_weighted.plotOn(FRAME3,RooFit.LineColor(kGreen))
FRAME3.Draw()

Cee.cd(4).SetLogy()
FRAME4 = rrv_eta.frame()
DATA.plotOn(FRAME4)
RHP_tot.plotOn(FRAME4,RooFit.LineColor(kRed))
RHP_tot_weighted.plotOn(FRAME4,RooFit.LineColor(kGreen))
FRAME4.Draw()

Cee.cd(5)
FRAME5 = rrv_nPV.frame()
DATA.plotOn(FRAME5)
RHP_tot.plotOn(FRAME5,RooFit.LineColor(kRed))
RHP_tot_weighted.plotOn(FRAME5,RooFit.LineColor(kGreen))
FRAME5.Draw()

Cee.cd(6).SetLogy()
FRAME6 = rrv_nPV.frame()
DATA.plotOn(FRAME6)
RHP_tot.plotOn(FRAME6,RooFit.LineColor(kRed))
RHP_tot_weighted.plotOn(FRAME6,RooFit.LineColor(kGreen))
FRAME6.Draw()


print "making the three keys pdfs" 

b_sumPdf=0
g_sumPdf=0
c_sumPdf=0
l_sumPdf=0

b_sumHist=0
c_sumHist=0
l_sumHist=0

print "making the three hist pdfs"

myRDS_l = RDS_sum_weighted.reduce("rc_flav==1")
myRDS_c = RDS_sum_weighted.reduce("rc_flav==4")
myRDS_b = RDS_sum_weighted.reduce("rc_flav==5")
#myRDS_g = RDS_sum_weighted.reduce("rc_flav==6")

if template == "keys":
    b_sumPdf = RooAddPdf("b_sumPdf","b_sumPdf",b_pdfList,fracList)
    g_sumPdf = RooAddPdf("g_sumPdf","g_sumPdf",g_pdfList,fracList)
    c_sumPdf = RooAddPdf("c_sumPdf","c_sumPdf",c_pdfList,fracList)
    l_sumPdf = RooAddPdf("l_sumPdf","l_sumPdf",l_pdfList,fracList)
    #b_sumPdf = RooKeysPdf("myRKP_b","myRKP_b",rrv_msv,myRDS_l)
    #c_sumPdf = RooKeysPdf("myRKP_b","myRKP_b",rrv_msv,myRDS_c)
    #l_sumPdf = RooKeysPdf("myRKP_b","myRKP_b",rrv_msv,myRDS_b)
elif template == "hist":
    b_sumHist = RooDataHist("b_sumHist", "b_sumHist", RooArgSet(rrv_msv), myRDS_b)
    b_sumPdf  = RooHistPdf( "b_sumPdf",  "b_sumPdf",  RooArgSet(rrv_msv), b_sumHist)
    #g_sumHist = RooDataHist("g_sumHist", "g_sumHist", RooArgSet(rrv_msv), myRDS_g)
    #g_sumPdf  = RooHistPdf( "g_sumPdf",  "g_sumPdf",  RooArgSet(rrv_msv), g_sumHist)
    c_sumHist = RooDataHist("c_sumHist", "c_sumHist", RooArgSet(rrv_msv), myRDS_c)
    c_sumPdf  = RooHistPdf( "c_sumPdf",  "c_sumPdf",  RooArgSet(rrv_msv), c_sumHist)
    l_sumHist = RooDataHist("l_sumHist", "l_sumHist", RooArgSet(rrv_msv), myRDS_l)
    l_sumPdf  = RooHistPdf( "l_sumPdf",  "l_sumPdf",  RooArgSet(rrv_msv), l_sumHist)

#Nb = RooRealVar("Nb","Nb",myRDS.numEntries()*0.6,0,myRDS.numEntries())
#Nc = RooRealVar("Nc","Nc",myRDS.numEntries()*0.3,0,myRDS.numEntries())
#Nl = RooRealVar("Nl","Nl",myRDS.numEntries()*0.1,0,myRDS.numEntries())

Nb = RooRealVar("N_{b}","N_{b}",DATA.numEntries()*0.70,0,DATA.numEntries())
Ng = RooRealVar("N_{g}","N_{g}",DATA.numEntries()*0.01                     )
Nc = RooRealVar("N_{c}","N_{c}",DATA.numEntries()*0.20,0,DATA.numEntries())
Nl = RooRealVar("N_{l}","N_{l}",DATA.numEntries()*0.10,0,DATA.numEntries())

#f_Sum_b = RooRealVar("f_Sum_b","f_Sum_b",0.6,0.,1.)
#f_Sum_c = RooRealVar("f_Sum_c","f_Sum_c",0.6,0.,1.)

f_Sum_b = RooRealVar("f_{b}","f_{b}", 0.70, 0.00, 1.  )
#f_Sum_g = RooRealVar("f_{g}","f_{g}", 0.01, 0.01, 0.01)
f_Sum_c = RooRealVar("f_{c}","f_{c}", 0.20, 0.00, 1.  )


templateC = TCanvas("templateC","templateC", 1150,400)
templateC.Divide(3)
templateC.cd(1)
templateCframe_b = rrv_msv.frame(rrv_msv.getMin(),rrv_msv.getMax()*0.6,rrv_msv.getBins()*6/10)
b_sumHist.plotOn(templateCframe_b)
templateCframe_b.Draw()
templateC.cd(2)
templateCframe_c = rrv_msv.frame(rrv_msv.getMin(),rrv_msv.getMax()*0.6,rrv_msv.getBins()*6/10)
c_sumHist.plotOn(templateCframe_c)
templateCframe_c.Draw()
templateC.cd(3)
templateCframe_l = rrv_msv.frame(rrv_msv.getMin(),rrv_msv.getMax()*0.6,rrv_msv.getBins()*6/10)
l_sumHist.plotOn(templateCframe_l)
templateCframe_l.Draw()



sumPdf = RooAddPdf("sumPdf","sumPdf",
                   RooArgList(b_sumPdf, c_sumPdf, l_sumPdf),
                   RooArgList(Nb,      Nc       ,Nl        ) )
sumPdf2 = RooAddPdf("sumPdf2","sumPdf2",
                    RooArgList(b_sumPdf, c_sumPdf, l_sumPdf),
                    RooArgList(f_Sum_b,  f_Sum_c            ) )
#sumPdf = RooAddPdf("sumPdf","sumPdf",
#                   RooArgList(b_sumPdf, g_sumPdf, c_sumPdf, l_sumPdf),
#                   RooArgList(Nb,       Ng,       Nc       ,Nl        ) )
#sumPdf2 = RooAddPdf("sumPdf2","sumPdf2",
#                    RooArgList(b_sumPdf, g_sumPdf, c_sumPdf, l_sumPdf),
#                    RooArgList(f_Sum_b,  f_Sum_g,  f_Sum_c            ) )

rrv_msv.setRange("r",0,6)
rrv_msv.SetTitle("m(SV) (GeV/c^{2})")

print " fit DATA with JES"

sumPdf.fitTo(DATA,RooFit.Extended(),RooFit.Range("r"))

f_Sum_b.setVal(Nb.getVal()/(Nb.getVal()+Nc.getVal()+Nl.getVal()))
f_Sum_c.setVal(Nc.getVal()/(Nb.getVal()+Nc.getVal()+Nl.getVal()))


gROOT.SetStyle("Plain")
gStyle.SetErrorX(0)

C1 = TCanvas("C1","C1",1000,450)
C1.Divide(2)

C1.cd(1)
fitfreem = rrv_msv.frame(rrv_msv.getMin(),rrv_msv.getMax()*0.6,rrv_msv.getBins()*6/10)
fitfreem.SetBarWidth(0.)
fitfreem.SetMarkerSize(1.3);
fitfreem.SetLineWidth(1)

DATA.plotOn(fitfreem,
            RooFit.MarkerSize(1.3),
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
sumPdf.plotOn(fitfreem,RooFit.LineWidth(1),RooFit.LineColor(kBlack))
chisq_ext = fitfreem.chiSquare(3)
myResidHist1 = fitfreem.residHist()
myPullHist1  = fitfreem.pullHist()

sumPdf.plotOn(fitfreem,RooFit.Components("b_sumPdf"),RooFit.LineWidth(1),RooFit.LineColor(kRed),  RooFit.LineStyle(kDashed))
sumPdf.plotOn(fitfreem,RooFit.Components("g_sumPdf"),RooFit.LineWidth(1),RooFit.LineColor(kMagenta),RooFit.LineStyle(kDashed))
sumPdf.plotOn(fitfreem,RooFit.Components("c_sumPdf"),RooFit.LineWidth(1),RooFit.LineColor(kGreen),RooFit.LineStyle(kDashed))
sumPdf.plotOn(fitfreem,RooFit.Components("l_sumPdf"),RooFit.LineWidth(1),RooFit.LineColor(kBlue), RooFit.LineStyle(kDashed))
DATA.plotOn(fitfreem,
            RooFit.MarkerSize(1.3),
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
sumPdf.paramOn(fitfreem,DATA)
fitfreem.Draw()


sumPdf2.fitTo(DATA,RooFit.Range("r"))

C1.cd(2)
fitfreem2 = rrv_msv.frame(rrv_msv.getMin(),rrv_msv.getMax()*0.6,rrv_msv.getBins()*6/10)
fitfreem2.SetBarWidth(0.)
fitfreem2.SetMarkerSize(1.3);
fitfreem2.SetLineWidth(1)
               
DATA.plotOn(fitfreem2,
            RooFit.MarkerSize(1.3),
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
sumPdf.plotOn(fitfreem2, RooFit.LineWidth(1), RooFit.LineColor(kBlack))
chisq_frac = fitfreem2.chiSquare(2)
myResidHist2 = fitfreem2.residHist()
myPullHist2  = fitfreem2.pullHist()

sumPdf2.plotOn(fitfreem2,RooFit.LineWidth(1),RooFit.Components("l_sumPdf,b_sumPdf,c_sumPdf"), RooFit.FillColor(kRed),  RooFit.DrawOption("F"), RooFit.LineColor(kBlack))
sumPdf2.plotOn(fitfreem2,RooFit.LineWidth(1),RooFit.Components("l_sumPdf,b_sumPdf,c_sumPdf"), RooFit.FillColor(kBlue), RooFit.DrawOption("F"), RooFit.LineColor(kBlack))
sumPdf2.plotOn(fitfreem2,RooFit.LineWidth(1),RooFit.Components("l_sumPdf,b_sumPdf,c_sumPdf"), RooFit.FillColor(kBlue), RooFit.LineColor(kBlack))
sumPdf2.plotOn(fitfreem2,RooFit.LineWidth(1),RooFit.Components("c_sumPdf,b_sumPdf"),          RooFit.FillColor(kGreen),RooFit.DrawOption("F"), RooFit.LineColor(kBlack))
sumPdf2.plotOn(fitfreem2,RooFit.LineWidth(1),RooFit.Components("c_sumPdf,b_sumPdf"),          RooFit.FillColor(kGreen),RooFit.LineColor(kBlack))
sumPdf2.plotOn(fitfreem2,RooFit.LineWidth(1),RooFit.Components("b_sumPdf"),                   RooFit.FillColor(kRed),  RooFit.DrawOption("F"), RooFit.LineColor(kBlack))
sumPdf2.plotOn(fitfreem2,RooFit.LineWidth(1),RooFit.Components("b_sumPdf"),                   RooFit.FillColor(kRed),  RooFit.LineColor(kBlack))
DATA.plotOn(fitfreem2,
            RooFit.MarkerSize(1.3),
            RooFit.XErrorSize(0.035),
            RooFit.DrawOption("pe2"))
sumPdf2.paramOn(fitfreem2,DATA)
fitfreem2.Draw()


############################


# Create a new frame to draw the residual distribution and add the distribution to the frame
freem3 = rrv_msv.frame(RooFit.Range(rrv_msv.getMin(),rrv_msv.getMax()*0.6),
                       RooFit.Bins(rrv_msv.getBins()*6/10),
                       RooFit.Name("residual (fitted pdf - data) for m(SV)"),
                       RooFit.Title("residual (fitted pdf - data) for m(SV)"))
freem3.addPlotable(myResidHist1,"P")
# Create a new frame to draw the pull distribution and add the distribution to the frame
freem5 = rrv_msv.frame(RooFit.Range(rrv_msv.getMin(),rrv_msv.getMax()*0.6),
                       RooFit.Bins(rrv_msv.getBins()*6/10),
                       RooFit.Name("pull [(fitted pdf - data)/sigma] for m(SV)"),
                       RooFit.Title("pull [(fitted pdf - data)/sigma] for m(SV)"))
freem5.addPlotable(myPullHist1,"P") 
# Create a new frame to draw the residual distribution and add the distribution to the frame
freem4 = rrv_msv.frame(RooFit.Range(rrv_msv.getMin(),rrv_msv.getMax()*0.6),
                       RooFit.Bins(rrv_msv.getBins()*6/10),
                       RooFit.Name("residual (fitted pdf - data) for m(SV)"),
                       RooFit.Title("residual (fitted pdf - data) for m(SV)"))
freem4.addPlotable(myResidHist2,"P")
# Create a new frame to draw the pull distribution and add the distribution to the frame
freem6 = rrv_msv.frame(RooFit.Range(rrv_msv.getMin(),rrv_msv.getMax()*0.6),
                       RooFit.Bins(rrv_msv.getBins()*6/10),
                       RooFit.Name("pull [(fitted pdf - data)/sigma] for m(SV)"),
                       RooFit.Title("pull [(fitted pdf - data)/sigma] for m(SV)"))
freem6.addPlotable(myPullHist2,"P") 

Ceee = TCanvas("Ceee","Ceee",1000,900)
Ceee.Divide(2,2)

Ceee.cd(1)
freem3.Draw()
Ceee.cd(2)
freem4.Draw()
Ceee.cd(3)
freem5.Draw()
Ceee.cd(4)
freem6.Draw()

# TLegend* leg1 = new TLegend(0.50, 0.5625, 0.85, 0.95-0.20, "", "NDC");
# // leg1->AddEntry( f_frac->getObject(0), "data ");
# leg1->AddEntry( f_frac->getObject(0), "Data ","PLE");
# leg1->AddEntry( f_frac->getObject(5), "b-jets"  ,"F");
# leg1->AddEntry( f_frac->getObject(3), "c-jets"  ,"F");

# leg1->SetFillColor(0);
# leg1->SetShadowColor(0);

# leg1->Draw();

# TLatex lat;
# lat.DrawLatex(2.,14.,"#splitline{CMS Preliminary}{#sqrt{s} = 7 TeV, L = 36 pb^{-1}}");

# TLatex lat;
# lat.DrawLatex(2.5,6,"High purity b-tagging");
            

#C1.cd(3)
#freem3 = rrv_pT.frame(0,250)
#DATA.plotOn(freem3,RooLinkedList())
#sumPdf2.plotOn(freem3,RooFit.LineColor(kBlack))
#freem3.Draw()

jecString=""
if jec : jecString+="_"+str(jec)+"sigmaJEC"

C1.SaveAs("~/public/ZbbLeptonPhoton/bPurPlots/bPurFit_QCDtemplate"+channel+"_"+WP+"_"+template+jecString+".pdf")

C_msv_perpT_flav = TCanvas("C_msv_perpT_flav","C_msv_perpT_flav",1100,400)
C_msv_perpT_flav.Divide(3)

C_msv_perpT_flav.cd(1)        
f_msv_perpT_b = rrv_msv.frame(0,5,40)
myRKP_b[1,1,1].plotOn(f_msv_perpT_b,RooFit.LineColor(kBlack))
myRKP_b[2,1,1].plotOn(f_msv_perpT_b,RooFit.LineColor(kBlue))
myRKP_b[3,1,1].plotOn(f_msv_perpT_b,RooFit.LineColor(kGreen))
myRKP_b[4,1,1].plotOn(f_msv_perpT_b,RooFit.LineColor(kOrange))
f_msv_perpT_b.Draw()

#C_msv_perpT_flav.cd(2)        
#f_msv_perpT_g = rrv_msv.frame(0,5,40)
#myRKP_g[1,1,1].plotOn(f_msv_perpT_g,RooFit.LineColor(kBlack))
#myRKP_g[2,1,1].plotOn(f_msv_perpT_g,RooFit.LineColor(kBlue))
#myRKP_g[3,1,1].plotOn(f_msv_perpT_g,RooFit.LineColor(kGreen))
#myRKP_g[4,1,1].plotOn(f_msv_perpT_g,RooFit.LineColor(kOrange))
#f_msv_perpT_g.Draw()

C_msv_perpT_flav.cd(2)        
f_msv_perpT_c = rrv_msv.frame(0,5,40)
myRKP_c[1,1,1].plotOn(f_msv_perpT_c,RooFit.LineColor(kBlack))
myRKP_c[2,1,1].plotOn(f_msv_perpT_c,RooFit.LineColor(kBlue))
myRKP_c[3,1,1].plotOn(f_msv_perpT_c,RooFit.LineColor(kGreen))
myRKP_c[4,1,1].plotOn(f_msv_perpT_c,RooFit.LineColor(kOrange))
f_msv_perpT_c.Draw()

C_msv_perpT_flav.cd(3)        
f_msv_perpT_l = rrv_msv.frame(0,5,40)
myRKP_l[1,1,1].plotOn(f_msv_perpT_l,RooFit.LineColor(kBlack))
myRKP_l[2,1,1].plotOn(f_msv_perpT_l,RooFit.LineColor(kBlue))
myRKP_l[3,1,1].plotOn(f_msv_perpT_l,RooFit.LineColor(kGreen))
myRKP_l[4,1,1].plotOn(f_msv_perpT_l,RooFit.LineColor(kOrange))
f_msv_perpT_l.Draw()

C_msv_perpT_all = TCanvas("C_msv_perpT_all","C_msv_perpT_all",1000,400)
C_msv_perpT_all.Divide(2)

C_msv_perpT_all.cd(1)        
f_msv_perpT_MC = rrv_msv.frame(0,5,40)
RDS_per_pT[1,1,1].plotOn(f_msv_perpT_MC,RooFit.MarkerColor(kBlack), RooFit.LineColor(kBlack)) 
RDS_per_pT[2,1,1].plotOn(f_msv_perpT_MC,RooFit.MarkerColor(kBlue),  RooFit.LineColor(kBlue)) 
RDS_per_pT[3,1,1].plotOn(f_msv_perpT_MC,RooFit.MarkerColor(kGreen), RooFit.LineColor(kGreen)) 
RDS_per_pT[4,1,1].plotOn(f_msv_perpT_MC,RooFit.MarkerColor(kOrange),RooFit.LineColor(kOrange)) 
f_msv_perpT_MC.Draw()

C_msv_perpT_all.cd(2)        
f_msv_perpT_DATA = rrv_msv.frame(0,5,40)
DATA_per_pT[1,1,1].plotOn(f_msv_perpT_DATA,RooFit.MarkerColor(kBlack) ,RooFit.LineColor(kBlack))
DATA_per_pT[2,1,1].plotOn(f_msv_perpT_DATA,RooFit.MarkerColor(kBlue)  ,RooFit.LineColor(kBlue) )
DATA_per_pT[3,1,1].plotOn(f_msv_perpT_DATA,RooFit.MarkerColor(kGreen) ,RooFit.LineColor(kGreen) )
DATA_per_pT[4,1,1].plotOn(f_msv_perpT_DATA,RooFit.MarkerColor(kOrange),RooFit.LineColor(kOrange) )
f_msv_perpT_DATA.Draw()




Can=TCanvas("Can","Can",1000,600)
Can.Divide(3,2)
Can.cd(1)
freem1.Draw()
Can.cd(2)
freem2.Draw()
Can.cd(3)
freeem3.Draw()

Can.cd(4)
freem4 = rrv_msv.frame()
myRDS_b.plotOn(freem4,RooFit.MarkerColor(kRed),RooFit.LineColor(kRed)) 
b_sumPdf.plotOn(freem4,RooFit.MarkerColor(kRed),RooFit.LineColor(kRed)) 
freem4.Draw()

Can.cd(5)
freem5 = rrv_msv.frame()
myRDS_c.plotOn(freem5,RooFit.MarkerColor(kGreen),RooFit.LineColor(kGreen)) 
c_sumPdf.plotOn(freem5,RooFit.MarkerColor(kGreen),RooFit.LineColor(kGreen)) 
freem5.Draw()

Can.cd(6)
freem6 = rrv_msv.frame()
myRDS_l.plotOn(freem6,RooFit.MarkerColor(kBlue),RooFit.LineColor(kBlue)) 
l_sumPdf.plotOn(freem6,RooFit.MarkerColor(kBlue),RooFit.LineColor(kBlue)) 
freem6.Draw()

#Can.cd(4)
#freem4 = rrv_msv.frame()
#myRDS.plotOn(freem4)
#myRHP_l.plotOn(freem4,RooFit.LineColor(kBlue))
#myRHP_c.plotOn(freem4,RooFit.LineColor(kGreen))
#myRHP_b.plotOn(freem4,RooFit.LineColor(kRed))
##myRHP_g.plotOn(freem4,RooFit.LineColor(kMagenta))
#freem4.Draw()

###############################################

myRDS_b = myRDS.reduce("rc_flav==5")
myRDS_g = myRDS.reduce("rc_flav==6")

myRDH_b = RooDataHist("myRDH_b", "myRDH_b", RooArgSet(rrv_msv), myRDS_b)
myRHP_b = RooHistPdf( "myRHP_b", "myRHP_b", RooArgSet(rrv_msv), myRDH_b )
myRDH_g = RooDataHist("myRDH_g", "myRDH_g", RooArgSet(rrv_msv), myRDS_g)
myRHP_g = RooHistPdf( "myRHP_g", "myRHP_g", RooArgSet(rrv_msv), myRDH_g )

myRKP_b = RooKeysPdf("myRKP_b","myRKP_b",rrv_msv,myRDS_b)
myRKP_g = RooKeysPdf("myRKP_g","myRKP_g",rrv_msv,myRDS_g)

gluonframe1 = rrv_msv.frame(0,6)
myRKP_b.plotOn(gluonframe1, RooFit.LineColor(kRed))
myRKP_g.plotOn(gluonframe1, RooFit.LineColor(kMagenta))

gluonframe2 = rrv_msv.frame(0,6)
myRDS_b.plotOn(gluonframe2, RooFit.MarkerColor(kRed))

gluonframe3 = rrv_msv.frame(0,6)
myRHP_b.plotOn(gluonframe3, RooFit.LineColor(kRed))
myRHP_g.plotOn(gluonframe3, RooFit.LineColor(kMagenta))

gluonframe4 = rrv_msv.frame(0,6)
myRDS_g.plotOn(gluonframe4, RooFit.MarkerColor(kMagenta))

gluonCanvas = TCanvas("gluonCanvas","gluonCanvas",800,800)
gluonCanvas.Divide(2,2)
gluonCanvas.cd(1)
gluonframe1.Draw()
gluonCanvas.cd(2)
gluonframe2.Draw()
gluonCanvas.cd(3)
gluonframe3.Draw()
gluonCanvas.cd(4)
gluonframe4.Draw()



print "#########################"

print "PRINTING SOME INFO"
print "===> chi-square(2) = ", chisq_frac
print "===> chi-square(3) = ", chisq_ext 
print "myRDS_b.numEntries() = ", myRDS_b.numEntries()   
print "myRDS_c.numEntries() = ", myRDS_c.numEntries()   
print "myRDS_l.numEntries() = ", myRDS_l.numEntries()   
print "DATA.numEntries()    = ", DATA.numEntries()   
print "myRDS_b.sumEntries() = ", myRDS_b.sumEntries()   
print "myRDS_c.sumEntries() = ", myRDS_c.sumEntries()   
print "myRDS_l.sumEntries() = ", myRDS_l.sumEntries()   
print "DATA.numEntries()    = ", DATA.numEntries()   









#make RooDataHist
#make RooHistPdf

###---------------------------------------------------------------------------------------------####

#    for (int ijet = 0; ijet < nJet; ijet++) {
#        float residual = 1.
#        if ( Run > 0 ) residual = Jet_residual[ijet]
#        float ptjet = Jet_pt[ijet] * Jet_jes[ijet] * residual
#         float etajet = fabs(Jet_eta[ijet])
#         if ( !(etajet >= EtaMin && etajet < EtaMax) ) continue#
#
#         ngoodj++; selecjet[ngoodj]=ijet; #
#
## njets = nJet;
## int npv = nPV; 
## if ( npv >= 20 ) npv = 20;
## int npu = nPU; 
##
## if ( pthat > 0. ){
##   if (PU_bunch[nPU] != 0) continue;#
#
#     #### make weight #
#
#    ### Loop on jets
#    for (int isel = 0; isel < ngoodj; isel++) :
#        
#        int ijet = selecjet[isel];
#   if ( ijet == 0 ) {
#     allevents++;
#     if ( allevents%100000 == 0 ) std::cout << "events : " << allevents << std::endl ;
#      hData_All_NJets->Fill( njets , ww1 );
#     hData_NJets->Fill( numjet , ww1 );
##
#
#     numjet = 0;
#     ntagjet = 0;
#   }
#
#   float ptjet = Jet_pt[ijet] * Jet_jes[ijet] * residual;
#   int flavour = abs( Jet_flavour[ijet] );
#   if ( flavour >= 1 && flavour <= 3 ) flavour = 1;#
#
#   if ( !(ptjet >= PtMin && ptjet < PtMax) ) continue;
#   if ( !(etajet >= EtaMin && etajet < EtaMax) ) continue;
#
#   hData_All_JetPV->Fill( npv , 1. );
#   hData_All_JetPt->Fill( ptjet , ww1 );
#   hData_All_JetEta->Fill( fabs(etajet) , 1. );
#   hData_All_JetRun->Fill( Run , 1. );
#   hAllFlav_All_Flavour->Fill( flavour , 1. );
#
#   double mass2vx ;
#
#   #if (Jet_SvxMass[ijet] >6.5) mass2vx =6.499 ;
#   #else if (Jet_SvxMass[ijet] <0.05) mass2vx =-0.99 ;
#   else mass2vx=Jet_SvxMass[ijet];
#   
##// High Purity Secondary Vertex
##   else if ( NN == 5 ) {
##     if ( Jet_SvxHP[ijet] > 1.  )  varpos =  5.*Jet_SvxHP[ijet];
##     if ( Jet_SvxNHP[ijet] < -1. ) varneg = -5.*Jet_SvxNHP[ijet];
##     if ( Jet_SvxHP[ijet] > TagCut )  TagPos = true;
##     if (-Jet_SvxNHP[ijet] > TagCut ) TagNeg = true;
##     cat = Jet_histSvx[ijet];
##   }
#
#   if ( flavour == 1 || 2 || 3 || flavour == 21 ) : LIGHT
#   elif (flavour == 4)                            : C  
#   elif (flavour == 5)                            : B#
#
#   #check if (nBFromGSplit>0) {
#   #    for (int igluon =0; igluon<nBFromGSplit; igluon++){
#   #	 double comp = fabs( bFromGSplit_pT[igluon] - ptjet) ;  comp = comp/bFromGSplit_pT[igluon] ;
#   #	 if ( comp > 1.1 )  continue;
#   #	 if (bFromGSplit_eta[igluon] < 0.8*EtaMin )  continue;
#   #	 if (bFromGSplit_eta[igluon] > 1.2*EtaMax )  continue;
#   #	 double test = deltaR(etajet, phijet , bFromGSplit_eta[igluon],bFromGSplit_phi[igluon]) ;
#   #	 DeltaRGluonSp->Fill(test,ww);
#   #
#   #	 if (test < 0.15){issplit = 1 ; DeltaRGluonMass->Fill(test,mass2vx); break;}#
##
#
#  # todo: also check pos/neg



### some beautiful hardcoded arrays of weights

# float nevt[14] = {0,1650000,6583068,6600000,6589956,6127528,6220160,6432669,3990085,4245695,
#	4053888,2093222,2196200,293139};
# float xsec[14] = {3.675e+10, 8.159e+08, 5.312e+07, 6.359e+06, 7.843e+05, 1.151e+05, 2.426e+04, 1.168e+03, 7.022e+01,
#		  1.555e+01,1.8444,3.321e-01,1.087e-02,3.575e-04};

# float WeightPtHat[14];
# for (Int_t k=0; k<14; k++){
#   WeightPtHat[k] = lumidata*xsec[k]/nevt[k]/1000. ;
#   cout << "WeightPtHat[" << k << "] = " << WeightPtHat[k] << endl;
# }

# float WeightPU[20] = {0.747694 ,0.853661 ,0.882735 ,0.915668 ,0.951334 ,0.987061 ,1.021296 ,1.052876 ,1.081233 ,1.105996 ,1.126985 ,1.144090 ,1.157152 ,1.165910 ,1.169945 ,1.168780 ,1.161875 ,1.148769 ,1.129215 ,0.631684};
# float WeightPt[15] ={ 1., 0.617427, 0.181917, 0.720309, 2.317049, 8.048693, 18.743258, 35.954548, 107.985794, 130.051636, 219.512650, 331.493652, 340.109497, 
#346.113312, 350.579224};

#Long64_t nentries = fChain->GetEntriesFast();

#f = TFile("/scratch/tdupree/bMistagTuples/ForTristan/qcd30a50/JetTree_10_1_Hth.root");
##f.cd("JetTree_10_1_Hth.root.root:/mistag")
##tree = gDirectory.Get("ttree;3")
#mytsjeen = f.Get("mistag/ttree;3")

filename = "/afs/cern.ch/user/t/tdupree/public/ZbbLeptonPhoton/bPurPlots/bPurFit_QCDtemplate"+channel+"_"+WP+"_"+template+jecString+".txt"

my_file = open(filename,"w")
print "filename = ", filename
print >> my_file, "##############################################################"
print >> my_file, "WP = ", WP
print >> my_file, "channel = ", channel

print >> my_file, "--------------------> for di-", channel, "sample at selection step ", WP
print >> my_file, "--------------------> "
print >> my_file, "--------------------> P = (", str(f_Sum_b.getVal()*100.)[:4] , " +/- ",  str(f_Sum_b.getError()*100.)[:4] , " ) % "

print "VOILA!!!"


