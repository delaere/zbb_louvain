#####################################################
###                                               ###
### getYields_fromRDS.py                          ###
###                                               ###
### Small script to estimate the number of events ###
### for different data and MC samples             ###
### for a certain working point and selection     ###
###                                               ###
#####################################################

from ROOT import *

#####################################################
### sample/wp/selection of interest
#####################################################

WP       = "9"    #"HP","HPMET","HP_excl","HE","HEmet","He_excl"
channel  = "Mu"    #"El","Mu"
extraCut = "jetmetbjet1pt>25.&jetmetbjet2pt>25.&jetmetMET<50."

totalCutString = ""+extraCut

#####################################################
### settings (this should move somewhere central) ### 
#####################################################

MCsampleList   = ["TT","DY","ZZ","ZHbb"]
SMMCsampleList = ["TT","DY","ZZ"]
totsampleList  = ["DATA","TT","DY","ZZ","ZHbb"]

lumi = { "DATA" : 2.1                     ,
         "TT"   : (3701947./157.5)/1000.  ,
         "DY"   : (36257961./3048.)/1000. ,
         "ZZ"   : 4000000./6000.          ,
         "ZHbb" : 12000.                  }

MCweight = {}

for sample in MCsampleList:
    print "the lumi of ", sample, " = ", lumi[sample]
    MCweight[sample] = lumi["DATA"]/lumi[sample]
    print "the weight of ", sample," = ", MCweight[sample]

#############
### files ###
#############

myRDS_el    = {}
myRDS_mu    = {}
myRDS       = {}
myRDS_red   = {} 
myRDS_red_w = {} 


filename_el = {"DATA" : "File_rds_zbb_El_DATA.root",
               "TT"  : "File_rds_zbb_Ttbar_El_MC.root",
               "DY"  : "File_rds_zbb_El_MC.root",
               "ZZ"  : "File_rds_zbb_ZZ_El_MC.root",
               "ZHbb": "File_rds_zbb_ZHbb_El_MC.root"
               }

filename_mu = {"DATA" : "File_rds_zbb_Mu_DATA.root",
               "TT"  : "File_rds_zbb_Ttbar_Mu_MC.root",
               "DY"  : "File_rds_zbb_Mu_MC.root",
               "ZZ"  : "File_rds_zbb_ZZ_Mu_MC.root",
               "ZHbb": "File_rds_zbb_ZHbb_Mu_MC.root"
               }

for sample in totsampleList :

    file_el  = TFile(filename_el[sample])
    file_mu  = TFile(filename_mu[sample])

    ws_el    = file_el.Get("ws")
    ws_mu    = file_mu.Get("ws")

    myRDS_el[sample] = ws_el.data("rds_zbb")
    myRDS_mu[sample] = ws_mu.data("rds_zbb")

    print "myRDS_el.numEntries() for ", sample , " = ", myRDS_el[sample].numEntries()
    print "myRDS_mu.numEntries() for ", sample , " = ", myRDS_mu[sample].numEntries()

    ws=ws_el

###############
### weights ###
###############

rrv_w_b = {"5"  : ws.var("BtaggingReweightingHE")  ,
           "7"  : ws.var("BtaggingReweightingHP")  ,
           "9"  : ws.var("BtaggingReweightingHEHE"), 
           "11" : ws.var("BtaggingReweightingHPHP")
           }

rrv_w_lep  = ws.var("LeptonsReweightingweight")
rrv_w_lumi = ws.var("lumiReweightingLumiWeight")


w = RooFormulaVar("w","w", "@0*@1*@2", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))

#################################  
### working point & selection ###
#################################

muMassCut = "(eventSelectionbestzmassMu>76&eventSelectionbestzmassMu<106)"
elMassCut = "(eventSelectionbestzmassEle>76&eventSelectionbestzmassEle<106)"

for sample in totsampleList:
    if   channel=="El" : myRDS_red[sample] = myRDS_el[sample].reduce("rc_eventSelection_"+WP+"==1")
    elif channel=="Mu" : myRDS_red[sample] = myRDS_mu[sample].reduce("rc_eventSelection_"+WP+"==1")

    if extraCut : myRDS_red[sample] = myRDS_red[sample].reduce(extraCut)

    if channel =="Mu" :
        myRDS_red[sample]=myRDS_red[sample].reduce(muMassCut)
        totalCutString+="&"+muMassCut
    if channel =="El" :
        myRDS_red[sample]=myRDS_red[sample].reduce(elMassCut)
        totalCutString+="&"+muMassCut

    if sample != "DATA": myRDS_red[sample].addColumn(w)
    #myRDS_red[sample].addColumn(w)

    myRDS_red_w[sample] = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red[sample],myRDS_red[sample].get(),"","w")

#################
### printouts ###
#################

print "***"
print "*** DATA/MC COMPARISONS"
print "***"
print "channel ......... ", channel
print "working point ... ", WP
print "extra cut ....... ", extraCut
print "***"

sum_MC=0
for sample in MCsampleList:
    print "the pure # of ", sample, " MC  ............... ", str(myRDS_red_w[sample].numEntries())[:4]
    sum_MC+=myRDS_red_w[sample].numEntries()
print "===> the pure # of MC ............... ", str(sum_MC)[:4]
print "===> the pure # of DATA ............... ", myRDS_red_w["DATA"].numEntries()

print "***"
sum_MC=0
for sample in MCsampleList:
    print "the effective # of ", sample, " MC for this lumi ... ", str(myRDS_red_w[sample].numEntries()*(lumi["DATA"]/lumi[sample]))[:4]
    sum_MC+=myRDS_red_w[sample].numEntries()*(lumi["DATA"]/lumi[sample])
print "===> the effective # of MC    ............... ", str(sum_MC)[:4]
print "===> the effective # of DATA  ............... ", myRDS_red_w["DATA"].numEntries()

print "***"

sum_MC=0
for sample in MCsampleList:
    print "the weighted effective # of ", sample, " MC for this data lumi = ", str(myRDS_red_w[sample].sumEntries()*(lumi["DATA"]/lumi[sample]))[:4]
    sum_MC+=myRDS_red_w[sample].sumEntries()*(lumi["DATA"]/lumi[sample])
print "===> the effective, weighted # of MC    ............... ", str(sum_MC)[:4]
print "===> the effective, weighted # of DATA  ............... ", myRDS_red_w["DATA"].numEntries()


#############
### PLOTS ###
#############

#################
### variables ###
#################

namePlotList = [
#    "eventSelectionbestzmassMu"  ,  ##
#    "eventSelectionbestzmassEle" ,
    "eventSelectionbestzptMu"    ,
    "eventSelectionbestzptEle"   ,
#    "jetmetbjet1pt"              ,   
#    "jetmetbjet2pt"              ,   
#    "jetmetMET"                  ,
#    "eventSelectiondphiZbb"      ,
#    "eventSelectiondphiZbj1"     , 
    "eventSelectiondijetPt"      ,#
    "eventSelectiondijetM"       ,
    "eventSelectiondijetdR"      ,
#    "eventSelectiondijetSVdR"    ,
    "eventSelectionZbbM"         
    ]

################
### maximums ###
################

max = {
    "eventSelectionbestzmassMu" :  200 ,  
    "eventSelectionbestzmassEle":  200 ,  
    "eventSelectionbestzptMu"   :  300 ,
    "eventSelectionbestzptEle"  :  300 ,
    "eventSelectiondijetPt"     :  300 ,
    "eventSelectiondrZbj1"      :    6 ,
    "jetmetbjet1pt"             :  250 ,
    "jetmetbjet2pt"             :  250 ,   
    "jetmetMET"                 :  200 , 
    "eventSelectiondphiZbj1"    :    6 ,
    "eventSelectiondphiZbb"     :    6 ,
    "eventSelectiondrZbb"       :    6 ,
    "eventSelectionscaldptZbj1" :  150 ,
    "eventSelectiondijetM"      :  600 ,
    "eventSelectiondijetdR"     :    5 ,
    "eventSelectiondijetSVdR"   :    5 ,
    "eventSelectionZbbM"        : 1000 ,
    "eventSelectionZbbPt"       :  300 ,
    "jetmetjet1SSVHEdisc"       :    6 ,
    "jetmetjet1SSVHPdisc"       :    6 ,
    "jetmetjet1SVmass"          :    6 ,
    "jetmetjet1TCHEdisc"        :   15 ,
    "jetmetjet1TCHPdisc"        :   15 ,
    "jetmetMET"                 :  250 
    }
    

var = {}
for name in namePlotList:
    print "name = ", name
    var[name] = ws.var(name)
    var[name].setMin(0)
    var[name].setMax(max[name])
    var[name].setBins(15)


###############
### sum pdf ###
###############

num_MC = {}

numList = RooArgList()

for sample in MCsampleList:
    num_MC[sample] = RooRealVar("num_MC_"+sample,"num_MC_"+sample,
                                myRDS_red_w[sample].sumEntries()*(lumi["DATA"]/lumi[sample]))
for sample in SMMCsampleList:
    numList.add(num_MC[sample])

#####################
### normalization ###
#####################

norm={}
lumiratio={}

for sample in MCsampleList:
    norm[sample] = num_MC[sample].getVal()/myRDS_red_w["DATA"].numEntries()
    print "num MC for ", sample, " = ", num_MC[sample].getVal()
    print "MC normalization for ", sample, " = ", norm[sample]
    lumiratio[sample]=lumi["DATA"]/lumi[sample]
    print "lumi ratio for ", sample, " = ", lumiratio[sample]

norm["ZHbb"] = 10*norm["ZHbb"]

#############
### plots ###
#############

var_frame = {}

#from drawStyle import *
#setStyle()
CANVAS = {}

gROOT.SetStyle("Plain")



rdh = {}
rhp = {}
rap = {}

th1 = {}
th1_copy = {}

componentString={}

for name in namePlotList:
    sampleList = RooArgList()
    for sample in totsampleList:
        th1[sample+name] = TH1D("th1_"+sample+name,"th1_"+sample+name,var[name].getBins(),var[name].getMin(),var[name].getMax())
        myRDS_red_w[sample].fillHistogram(th1[sample+name], RooArgList(var[name]))
        th1_copy[sample+name] = TH1D(th1[sample+name])
    for sample in MCsampleList:
        rdh[sample] = RooDataHist("rdh_"+sample, "rdh_"+sample,
                                  RooArgSet(var[name]),
                                  myRDS_red_w[sample])
        rhp[sample] = RooHistPdf("rhp_"+sample,"rhp_"+sample,
                                 RooArgSet(var[name]),
                                 rdh[sample])
    for sample in SMMCsampleList:
        sampleList.add(rhp[sample])

    print "sampleList = ", sampleList    
    print "numList    = ", numList    
    rap[name] = RooAddPdf("sum"+name,"sum"+name,sampleList,numList)    

    var_frame[name] = var[name].frame()
    myRDS_red_w["DATA"].plotOn(var_frame[name],
                               RooFit.MarkerSize(1.0),
                               RooFit.XErrorSize(0.035),
                               RooFit.DrawOption("pe2"))
    rap[name].plotOn(var_frame[name],
                     RooFit.Components("rhp_TT,rhp_DY,rhp_ZZ"),
                     RooFit.LineColor(kBlack),
                     RooFit.FillColor(kRed-7),
                     RooFit.DrawOption("F"),
                     RooFit.LineWidth(1),
                     RooFit.Normalization((num_MC["TT"].getVal()+num_MC["DY"].getVal()+num_MC["ZZ"].getVal())/myRDS_red_w["DATA"].numEntries()))
    rap[name].plotOn(var_frame[name],
                     RooFit.Components("rhp_TT,rhp_ZZ"),
                     RooFit.LineColor(kBlack),
                     RooFit.FillColor(kYellow-7),
                     RooFit.DrawOption("F"),
                     RooFit.LineWidth(1),
                     RooFit.Normalization((+num_MC["DY"].getVal()+num_MC["TT"].getVal()+num_MC["ZZ"].getVal())/myRDS_red_w["DATA"].numEntries()))
    rap[name].plotOn(var_frame[name],
                     RooFit.Components("rhp_ZZ"),
                     RooFit.LineColor(kBlack),
                     RooFit.FillColor(kPink-7),
                     RooFit.DrawOption("F"),
                     RooFit.LineWidth(1),
                     RooFit.Normalization((num_MC["DY"].getVal()+num_MC["TT"].getVal()+num_MC["ZZ"].getVal())/myRDS_red_w["DATA"].numEntries()))
    rhp["ZHbb"].plotOn(var_frame[name],
                       RooFit.LineColor(kRed),
                       RooFit.LineWidth(1),
                       RooFit.Normalization(norm["ZHbb"]))
    myRDS_red_w["DATA"].plotOn(var_frame[name],
                               RooFit.MarkerSize(1.0),
                               RooFit.XErrorSize(0.035),
                               RooFit.DrawOption("pe2"))


    CANVAS[name] = TCanvas("CANVAS"+name,"CANVAS"+name,1200,600)
    CANVAS[name].Divide(2)
    
    CANVAS[name].cd(1)                                 
    var_frame[name].Draw()
    CANVAS[name].cd(2)
    th1_copy["DATA"+name].Draw()                                      
    for sample in ("DY","TT","ZZ"): th1_copy[sample+name].DrawNormalized("same hist",num_MC[sample].getVal())
    
    
