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

WP =  "HE"

### Getting a file and a tree

file = { "HP"    : TFile("bTagPurRDS_HP.root") ,
         "HPMET" : TFile("bTagPurRDS_HP.root") ,
         "HE"    : TFile("bTagPurRDS_QCD_2_HE.root"),
         "HEMET" : TFile("bTagPurRDS_QCD_2_HE.root")
         }
ws = file[WP].Get("ws")
myRDS = ws.data("myRDS");

print "myRDS.numEntries() = ", myRDS.numEntries()

rrv_msv    = ws.var("rrv_msv")
rrv_bTagHE = ws.var("rrv_bTagHE")
rrv_bTagHP = ws.var("rrv_bTagHP")
rrv_pT     = ws.var("rrv_pT")
rrv_pT_unc = ws.var("rrv_pT_unc")
rc_flav    = ws.cat("rc_flav")

f_data = TFile("File_rds_zbb_Mu_DATA.root")
ws_data=f_data.Get("ws")
DATA = ws_data.data("rds_zbb")

if WP=="HE"   : DATA=DATA.reduce("rc_HE==1")
if WP=="HEMET": DATA=DATA.reduce("rc_HEMET==1")
if WP=="HP"   : DATA=DATA.reduce("rc_HP==1")
if WP=="HPMET": DATA=DATA.reduce("rc_HPMET==1")

RAS = DATA.get()
DATA_withunc = RooDataSet("rds_zbb_with_unc","rds_zbb_with_unc",RAS)

for i in range(0,DATA.numEntries()):
    RASi = DATA.get(i)
    ptVal = RASi.getRealValue("rrv_pT")
    ptuncVal = RASi.getRealValue("rrv_pT_unc")*ptVal
    RAS.setRealValue("rrv_pT",ptVal+5.*ptuncVal)
    DATA_withunc.add(RAS)

DATA = DATA_withunc


#myRDS.tree().Draw("rrv_msv")

myRDS_l = myRDS.reduce("rc_flav==1")
myRDS_c = myRDS.reduce("rc_flav==4")
myRDS_b = myRDS.reduce("rc_flav==5")

print "myRDS_l.numEntries() = ", myRDS_l.numEntries()
print "myRDS_c.numEntries() = ", myRDS_c.numEntries()
print "myRDS_b.numEntries() = ", myRDS_b.numEntries()

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
myRDH_c = RooDataHist("myRDH_c", "myRDH_c", RooArgSet(rrv_msv), myRDS_c)
myRDH_l = RooDataHist("myRDH_l", "myRDH_l", RooArgSet(rrv_msv), myRDS_l)

print "made datahists, making histpdfs"

myRHP   = RooHistPdf("myRHP",  "myRHP",  RooArgSet(rrv_msv),myRDH  )
myRHP_b = RooHistPdf("myRHP_b","myRHP_b",RooArgSet(rrv_msv),myRDH_b)
myRHP_c = RooHistPdf("myRHP_c","myRHP_c",RooArgSet(rrv_msv),myRDH_c)
myRHP_l = RooHistPdf("myRHP_l","myRHP_l",RooArgSet(rrv_msv),myRDH_l)

print "made histpdfs, going to plot"

Can=TCanvas("Can","Can")
Can.Divide(2,2)

Can.cd(1)
freem1 = rrv_msv.frame(40)
myRDS.plotOn(freem1)
myRHP.plotOn(freem1,RooFit.LineColor(kBlack))
freem1.Draw()

Can.cd(2)
freem2 = rrv_msv.frame(40)
myRDS.plotOn(freem2)
myRHP.plotOn(freem2,RooFit.LineColor(kBlack))
#myRKP_l.plotOn(freem2,RooFit.LineColor(kBlue))
#myRKP_c.plotOn(freem2,RooFit.LineColor(kGreen))
#myRKP_b.plotOn(freem2,RooFit.LineColor(kRed))
freem2.Draw()

Can.cd(3)
freem3 = rrv_msv.frame(40)
myRHP_l.plotOn(freem3,RooFit.LineColor(kBlue))
myRHP_c.plotOn(freem3,RooFit.LineColor(kGreen))
myRHP_b.plotOn(freem3,RooFit.LineColor(kRed))
freem3.Draw()



pTRegion = RooThresholdCategory("pTRegion","region of x",rrv_pT,"Background") ;

# Specify thresholds and state assignments one-by-one.
# Each statement specifies that all values _below_ the given value
# (and above any lower specified threshold) are mapped to the
# category state with the given name
#
# Background | SideBand | Signal | SideBand | Background
#     4.23       5.23     8.23       9.23
pTRegion.addThreshold(             30, "1") 
pTRegion.addThreshold(             50, "2") 
pTRegion.addThreshold(             80, "3") 
pTRegion.addThreshold(            150, "4") 
pTRegion.addThreshold(rrv_pT.getMax(), "5") 

# Add values of threshold function to dataset so that it can be used as observable
myRDS.addColumn(pTRegion) 
myRDS_b.addColumn(pTRegion) 
myRDS_c.addColumn(pTRegion) 
myRDS_l.addColumn(pTRegion) 
DATA.addColumn(pTRegion) 

# Make plot of data in x
# Use calculated category to select sideband data
testframe = rrv_msv.frame()
myRDS.plotOn(testframe)
myRDS.plotOn(testframe,RooFit.Cut("pTRegion==pTRegion::1"),RooFit.MarkerColor(kRed),RooFit.LineColor(kRed)) 
                    

RDS_per_pT = {}
RDS_b_per_pT = {}
RDS_c_per_pT = {}
RDS_l_per_pT = {}
RKP_b_per_pT = {}
RKP_c_per_pT = {}
RKP_l_per_pT = {}

myRDH_b = {}
myRDH_c = {}
myRDH_l = {}

myRHP_b = {}
myRHP_c = {}
myRHP_l = {}

myRKP_b = {}
myRKP_c = {}
myRKP_l = {}


DATA_per_pT = {}

for i in range(1,5):
    RDS_per_pT[i]    = myRDS.reduce("pTRegion==pTRegion::"+str(i))
    print "RDS_per_pT[", i , "].numEntries() = ", RDS_per_pT[i].numEntries()
    RDS_b_per_pT[i]  = myRDS_b.reduce("pTRegion==pTRegion::"+str(i)) 
    RDS_c_per_pT[i]  = myRDS_c.reduce("pTRegion==pTRegion::"+str(i)) 
    RDS_l_per_pT[i]  = myRDS_l.reduce("pTRegion==pTRegion::"+str(i)) 
    DATA_per_pT[i] = DATA.reduce("pTRegion==pTRegion::"+str(i)) 
    #RKP_per_pT[i]    = RooKeysPdf("RKP_per_pT"+str(i),  "RKP_per_pT"+str(i),rrv_msv,RDS_per_pT[i])
    myRKP_b[i]  = RooKeysPdf("RKP_b_per_pT"+str(i),"RKP_b_per_pT"+str(i),rrv_msv,RDS_b_per_pT[i])
    myRKP_c[i]  = RooKeysPdf("RKP_c_per_pT"+str(i),"RKP_c_per_pT"+str(i),rrv_msv,RDS_c_per_pT[i])
    myRKP_l[i]  = RooKeysPdf("RKP_l_per_pT"+str(i),"RKP_l_per_pT"+str(i),rrv_msv,RDS_l_per_pT[i])

    #myRDH   = RooDataHist("myRDH",   "myRDH",   RooArgSet(rrv_msv), myRDS  )
    myRDH_b[i] = RooDataHist("myRDH_b"+str(i), "myRDH_b"+str(i), RooArgSet(rrv_msv), RDS_b_per_pT[i])
    myRDH_c[i] = RooDataHist("myRDH_c"+str(i), "myRDH_c"+str(i), RooArgSet(rrv_msv), RDS_c_per_pT[i])
    myRDH_l[i] = RooDataHist("myRDH_l"+str(i), "myRDH_l"+str(i), RooArgSet(rrv_msv), RDS_l_per_pT[i])

    print "made datahists, making histpdfs"
    
    #myRHP   = RooHistPdf("myRHP",  "myRHP",  RooArgSet(rrv_msv),myRDH  )
    myRHP_b[i] = RooHistPdf("myRHP_b"+str(i),"myRHP_b"+str(i),RooArgSet(rrv_msv),myRDH_b[i])
    myRHP_c[i] = RooHistPdf("myRHP_c"+str(i),"myRHP_c"+str(i),RooArgSet(rrv_msv),myRDH_c[i])
    myRHP_l[i] = RooHistPdf("myRHP_l"+str(i),"myRHP_l"+str(i),RooArgSet(rrv_msv),myRDH_l[i])



RDS_per_pT[1].plotOn(testframe,RooFit.MarkerColor(kRed),RooFit.LineColor(kRed)) 
RDS_per_pT[2].plotOn(testframe,RooFit.MarkerColor(kBlue),RooFit.LineColor(kBlue)) 

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


b_pdfList = RooArgList()
c_pdfList = RooArgList()
l_pdfList = RooArgList()

f_b={}
fracList = RooArgList()
thresholdList = RooArgList(RooConstVar("t0","t0",rrv_pT.getMin()),
                           RooConstVar("t1","t1",30),
                           RooConstVar("t2","t2",50),
                           RooConstVar("t3","t3",80),
                           RooConstVar("t4","t4",150))

### TODO: add #PV, eta
### First produce them also in data
### (Long term: properly produce data/MC RooDataSets in same way)

rrv_weight = RooRealVar("weight","weight",0)

RDS_weighted_per_pT = {}


for i in range(1,5):
    f_b[i] = RooConstVar("f"+str(i),"f"+str(i),RDS_per_pT[i].numEntries()*1.0/DATA_per_pT[i].numEntries())
    print "frac ", i, " = ", f_b[i].getVal()
    fracList.add(f_b[i])
    b_pdfList.add(myRKP_b[i])
    c_pdfList.add(myRKP_c[i])
    l_pdfList.add(myRKP_l[i])

    rrv_weight.setVal(1./f_b[i].getVal())
    RDS_per_pT[i].addColumn(rrv_weight)


RDS_sum = RooDataSet("RDS_sum","RDS_sum",RDS_per_pT[i].get())
for i in range(1,5): RDS_sum.append(RDS_per_pT[i])



RDS_sum_weighted = RooDataSet("RDS_sum_weighted",
                              "RDS_sum_weighted",
                              RDS_sum,
                              RDS_sum.get(),
                              "",
                              "weight")


RDH_tot          = RooDataHist("myRDH_tot",   "myRDH_tot",   RooArgSet(rrv_pT), RDS_sum)
RDH_tot_weighted = RooDataHist("myRDH_tot_w", "myRDH_tot_w", RooArgSet(rrv_pT), RDS_sum_weighted)
RHP_tot          = RooHistPdf( "myRHP_tot",   "myRHP_tot",   RooArgSet(rrv_pT), RDH_tot  )
RHP_tot_weighted = RooHistPdf( "myRHP_tot_w", "myRHP_tot_w", RooArgSet(rrv_pT), RDH_tot_weighted)

Cee=TCanvas("Cee","Cee",800,400)
Cee.Divide(2)

Cee.cd(1)
FRAME1 = rrv_pT.frame(0,150,30)
DATA.plotOn(FRAME1)
RHP_tot.plotOn(FRAME1,RooFit.LineColor(kRed))
RHP_tot_weighted.plotOn(FRAME1,RooFit.LineColor(kGreen))
FRAME1.Draw()

Cee.cd(2).SetLogy()
FRAME2 = rrv_pT.frame(0,150,30)
DATA.plotOn(FRAME2)
RHP_tot.plotOn(FRAME2,RooFit.LineColor(kRed))
RHP_tot_weighted.plotOn(FRAME2,RooFit.LineColor(kGreen))
FRAME2.Draw()

print "making the three keys pdfs" 

b_sumPdf = RooAddPdf("b_sumPdf","b_sumPdf",b_pdfList,fracList)
c_sumPdf = RooAddPdf("c_sumPdf","c_sumPdf",c_pdfList,fracList)
l_sumPdf = RooAddPdf("l_sumPdf","l_sumPdf",l_pdfList,fracList)
#b_sumPdf = RooKeysPdf("myRKP_b","myRKP_b",rrv_msv,myRDS_l)
#c_sumPdf = RooKeysPdf("myRKP_b","myRKP_b",rrv_msv,myRDS_c)
#l_sumPdf = RooKeysPdf("myRKP_b","myRKP_b",rrv_msv,myRDS_b)

print "making the three hist pdfs"

myRDS_l = RDS_sum_weighted.reduce("rc_flav==1")
myRDS_c = RDS_sum_weighted.reduce("rc_flav==4")
myRDS_b = RDS_sum_weighted.reduce("rc_flav==5")

#b_sumHist = RooDataHist("b_sumHist", "b_sumHist", RooArgSet(rrv_pT), myRDS_b)
#b_sumPdf  = RooHistPdf( "b_sumPdf",  "b_sumPdf",  RooArgSet(rrv_pT), b_sumHist)
#c_sumHist = RooDataHist("c_sumHist", "c_sumHist", RooArgSet(rrv_pT), myRDS_c)
#c_sumPdf  = RooHistPdf( "c_sumPdf",  "c_sumPdf",  RooArgSet(rrv_pT), c_sumHist)
#l_sumHist = RooDataHist("l_sumHist", "l_sumHist", RooArgSet(rrv_pT), myRDS_l)
#l_sumPdf  = RooHistPdf( "l_sumPdf",  "l_sumPdf",  RooArgSet(rrv_pT), l_sumHist)




#Nb = RooRealVar("Nb","Nb",myRDS.numEntries()*0.6,0,myRDS.numEntries())
#Nc = RooRealVar("Nc","Nc",myRDS.numEntries()*0.3,0,myRDS.numEntries())
#Nl = RooRealVar("Nl","Nl",myRDS.numEntries()*0.1,0,myRDS.numEntries())

Nb = RooRealVar("Nb","Nb",myRDS.numEntries()*0.6,0,myRDS.numEntries())
Nc = RooRealVar("Nc","Nc",myRDS.numEntries()*0.3,0,myRDS.numEntries())
Nl = RooRealVar("Nl","Nl",myRDS.numEntries()*0.1,0,myRDS.numEntries())

#f_Sum_b = RooRealVar("f_Sum_b","f_Sum_b",0.6,0.,1.)
#f_Sum_c = RooRealVar("f_Sum_c","f_Sum_c",0.6,0.,1.)

f_Sum_b = RooRealVar("f_Sum_b","f_Sum_b",0.6,0.,1.)
f_Sum_c = RooRealVar("f_Sum_c","f_Sum_c",0.3,0.,1.)



sumPdf = RooAddPdf("sumPdf","sumPdf",
                   RooArgList(b_sumPdf, c_sumPdf, l_sumPdf),
                   RooArgList(Nb,       Nc       ,Nl        ) )
sumPdf2 = RooAddPdf("sumPdf2","sumPdf2",
                    RooArgList(b_sumPdf, c_sumPdf, l_sumPdf),
                    RooArgList(f_Sum_b,  f_Sum_c            ) )

rrv_msv.setRange("r",0,5)

print " fit DATA with JES"

sumPdf.fitTo(DATA,RooFit.Extended(),RooFit.Range("r"))

sumPdf2.fitTo(DATA,RooFit.Range("r"))

C1 = TCanvas("C1","C1",1000,400)
C1.Divide(2)

C1.cd(1)
freem = rrv_msv.frame(0,5,40)

DATA.plotOn(freem,RooLinkedList())
sumPdf.plotOn(freem,RooFit.LineColor(kBlack))
sumPdf.plotOn(freem,RooFit.Components("b_sumPdf"),RooFit.LineColor(kRed),  RooFit.LineStyle(kDashed))
sumPdf.plotOn(freem,RooFit.Components("c_sumPdf"),RooFit.LineColor(kGreen),RooFit.LineStyle(kDashed))
sumPdf.plotOn(freem,RooFit.Components("l_sumPdf"),RooFit.LineColor(kBlue), RooFit.LineStyle(kDashed))
sumPdf.paramOn(freem,DATA)
freem.Draw()

C1.cd(2)
freem2 = rrv_msv.frame(0,5,40)

DATA.plotOn(freem2,RooLinkedList())
sumPdf2.plotOn(freem2,RooFit.LineColor(kBlack))
sumPdf2.plotOn(freem2,RooFit.Components("l_sumPdf,b_sumPdf,c_sumPdf"), RooFit.FillColor(kBlue), RooFit.DrawOption("F"), RooFit.LineColor(kBlack))
sumPdf2.plotOn(freem2,RooFit.Components("l_sumPdf,b_sumPdf,c_sumPdf"), RooFit.FillColor(kBlue), RooFit.LineColor(kBlack))
sumPdf2.plotOn(freem2,RooFit.Components("c_sumPdf,b_sumPdf"),          RooFit.FillColor(kGreen),RooFit.DrawOption("F"), RooFit.LineColor(kBlack))
sumPdf2.plotOn(freem2,RooFit.Components("c_sumPdf,b_sumPdf"),          RooFit.FillColor(kGreen),RooFit.LineColor(kBlack))
sumPdf2.plotOn(freem2,RooFit.Components("b_sumPdf"),                   RooFit.FillColor(kRed),  RooFit.DrawOption("F"), RooFit.LineColor(kBlack))
sumPdf2.plotOn(freem2,RooFit.Components("b_sumPdf"),                   RooFit.FillColor(kRed),  RooFit.LineColor(kBlack))
DATA.plotOn(freem2,RooLinkedList())
sumPdf2.paramOn(freem2,DATA)
freem2.Draw()

#C1.cd(3)
#freem3 = rrv_pT.frame(0,250)
#DATA.plotOn(freem3,RooLinkedList())
#sumPdf2.plotOn(freem3,RooFit.LineColor(kBlack))
#freem3.Draw()

C_msv_perpT_flav = TCanvas("C_msv_perpT_flav","C_msv_perpT_flav",1500,400)
C_msv_perpT_flav.Divide(3)

C_msv_perpT_flav.cd(1)        
f_msv_perpT_b = rrv_msv.frame(0,5,40)
myRKP_b[1].plotOn(f_msv_perpT_b,RooFit.LineColor(kBlack))
myRKP_b[2].plotOn(f_msv_perpT_b,RooFit.LineColor(kBlue))
myRKP_b[3].plotOn(f_msv_perpT_b,RooFit.LineColor(kGreen))
myRKP_b[4].plotOn(f_msv_perpT_b,RooFit.LineColor(kOrange))
f_msv_perpT_b.Draw()

C_msv_perpT_flav.cd(2)        
f_msv_perpT_c = rrv_msv.frame(0,5,40)
myRKP_c[1].plotOn(f_msv_perpT_c,RooFit.LineColor(kBlack))
myRKP_c[2].plotOn(f_msv_perpT_c,RooFit.LineColor(kBlue))
myRKP_c[3].plotOn(f_msv_perpT_c,RooFit.LineColor(kGreen))
myRKP_c[4].plotOn(f_msv_perpT_c,RooFit.LineColor(kOrange))
f_msv_perpT_c.Draw()

C_msv_perpT_flav.cd(3)        
f_msv_perpT_l = rrv_msv.frame(0,5,40)
myRKP_l[1].plotOn(f_msv_perpT_l,RooFit.LineColor(kBlack))
myRKP_l[2].plotOn(f_msv_perpT_l,RooFit.LineColor(kBlue))
myRKP_l[3].plotOn(f_msv_perpT_l,RooFit.LineColor(kGreen))
myRKP_l[4].plotOn(f_msv_perpT_l,RooFit.LineColor(kOrange))
f_msv_perpT_l.Draw()

C_msv_perpT_all = TCanvas("C_msv_perpT_all","C_msv_perpT_all",1000,400)
C_msv_perpT_all.Divide(2)

C_msv_perpT_all.cd(1)        
f_msv_perpT_MC = rrv_msv.frame(0,5,40)
RDS_per_pT[1].plotOn(f_msv_perpT_MC,RooFit.MarkerColor(kBlack), RooFit.LineColor(kBlack)) 
RDS_per_pT[2].plotOn(f_msv_perpT_MC,RooFit.MarkerColor(kBlue),  RooFit.LineColor(kBlue)) 
RDS_per_pT[3].plotOn(f_msv_perpT_MC,RooFit.MarkerColor(kGreen), RooFit.LineColor(kGreen)) 
RDS_per_pT[4].plotOn(f_msv_perpT_MC,RooFit.MarkerColor(kOrange),RooFit.LineColor(kOrange)) 
f_msv_perpT_MC.Draw()

C_msv_perpT_all.cd(2)        
f_msv_perpT_DATA = rrv_msv.frame(0,5,40)
DATA_per_pT[1].plotOn(f_msv_perpT_DATA,RooFit.MarkerColor(kBlack) ,RooFit.LineColor(kBlack))
DATA_per_pT[2].plotOn(f_msv_perpT_DATA,RooFit.MarkerColor(kBlue)  ,RooFit.LineColor(kBlue) )
DATA_per_pT[3].plotOn(f_msv_perpT_DATA,RooFit.MarkerColor(kGreen) ,RooFit.LineColor(kGreen) )
DATA_per_pT[4].plotOn(f_msv_perpT_DATA,RooFit.MarkerColor(kOrange),RooFit.LineColor(kOrange) )
f_msv_perpT_DATA.Draw()















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
