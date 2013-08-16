####################################################
###                                               ###
### getYields_fromRDS.py                          ###
###                                               ###
### Small script to estimate the number of events ###
### for different data and MC samples             ###
### for a certain working point and selection     ###
###                                               ###
#####################################################

from ROOT import *
from zbbSamples import getSample, getDataLuminosity, getSamples

def RemoveErrorsHisto(h):

  x = h.GetXaxis()  
  hout = TH1D(h.GetName(),
                        h.GetTitle(),
			h.GetNbinsX(),
			x.GetXmin(),
			x.GetXmax())
  hout.SetFillColor(h.GetFillColor())
  for ihout in range (0, hout.GetNbinsX() + 2) :
    hout.SetBinContent(ihout, h.GetBinContent(ihout))  
  
  xout = hout.GetXaxis()
  xout.SetTitle(x.GetTitle())
  
  return hout

#####################################################
### sample/wp/selection of interest
#####################################################

WP       = "17"    #"HP","HPMET","HP_excl","HE","HEmet","He_excl"
channel  = "Mu"    #"El","Mu"
#extraCut = "eventSelectionbestzmassEle>76.&eventSelectionbestzmassEle<106.&jetmetbjet1pt>25&jetmetbjet2pt>25"
extraCut = "eventSelectionbestzmassMu>76.&eventSelectionbestzmassMu<106.&jetmetbjet1pt>25&jetmetbjet2pt>25"

#extraCut = ""
#extraCut = "mlphiggsvszbb>0.35&mlphiggsvstt>0.35&mlphiggsvszz>0.35"

totalCutString = ""+extraCut

#####################################################
### settings (this should move somewhere central) ### 
#####################################################

MCsampleList   = ["Zb","Zc","Zl","TT","ZZ","ZH125"]
SMMCsampleList = ["Zb","Zc","Zl","TT","ZZ"]
totsampleList  = ["DATA","Zb","Zc","Zl","TT","ZZ","ZH125"]
sampleList     = ["DATA","DY","TT","ZZ","ZH125"]

print getDataLuminosity(channel)

MCweight = {}

for sample in MCsampleList:
    print "the lumi of ", sample, " = ", getSample(sample,channel,"RDS").getLuminosity()
    MCweight[sample] = getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity()
    print "the weight of ", sample," = ", MCweight[sample]

#############
### files ###
#############

myRDS       = {}
myRDS_red   = {} 
myRDS_red_w = {} 


###########################################
##########INPUT FILES SELECTED HERE#######
###########################################

for sample in sampleList :

    redStage = "rc_eventSelection_"+WP+"==1"

    if sample != "DATA":
        
        file_mc  = TFile(getSample(sample,channel,"RDS").path)
        
        nEntries = file_mc.Get("rds_zbb").numEntries()

        if   sample == "DY" :
          myRDS["Zb"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==3")
          myRDS["Zc"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==2")
          myRDS["Zl"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==1")
          print "myRDS.numEntries() for ", "Zb" , " = ", nEntries, ". After stage ", WP, " : ", myRDS["Zb"].numEntries()
          print "myRDS.numEntries() for ", "Zc" , " = ", nEntries, ". After stage ", WP, " : ", myRDS["Zc"].numEntries()
          print "myRDS.numEntries() for ", "Zl" , " = ", nEntries, ". After stage ", WP, " : ", myRDS["Zl"].numEntries()
        else :
	  myRDS[sample] = file_mc.Get("rds_zbb").reduce(redStage)
          print "myRDS.numEntries() for ", sample , " = ", nEntries, ". After stage ", WP, " : ", myRDS[sample].numEntries()
        
        file_mc.Close()

    else :
        nEntries = 0
        myRDS[sample] = None
        for datasample in getSamples(["DATA"],[channel],["RDS"])
          file = TFile(datasample.path)
          nEntries += file.Get("rds_zbb").numEntries()
          if myRDS[sample] is None:
            myRDS[sample] = file.Get("rds_zbb").reduce(redStage)
          else:
            myRDS[sample].append(file.Get("rds_zbb").reduce(redStage))
          file.Close()
        print "myRDS.numEntries() for ", sample , " = ", nEntries, ". After stage ", WP, " : ", myRDS[sample].numEntries()

###############
### weights ###
###############

ras_zbb = myRDS["Zb"].get()

rrv_w_b = {"5"  : ras_zbb["BtaggingReweightingHE"]  ,
           "6"  : ras_zbb["BtaggingReweightingHP"]  ,
           "7"  : ras_zbb["BtaggingReweightingHE"]  ,
           "8"  : ras_zbb["BtaggingReweightingHP"]  ,
           "9"  : ras_zbb["BtaggingReweightingHEHE"], 
           "10" : ras_zbb["BtaggingReweightingHEHP"],
           "11" : ras_zbb["BtaggingReweightingHPHP"],
           "12" : ras_zbb["BtaggingReweightingHEHE"],
           "13" : ras_zbb["BtaggingReweightingHEHP"],
           "14" : ras_zbb["BtaggingReweightingHPHP"],
           "15" : ras_zbb["BtaggingReweightingHE"]  ,
           "16" : ras_zbb["BtaggingReweightingHP"]  ,
           "17" : ras_zbb["BtaggingReweightingHEHE"], 
           "18" : ras_zbb["BtaggingReweightingHEHP"],
           "19" : ras_zbb["BtaggingReweightingHPHP"],
           
           }

rrv_w_lep  = ras_zbb["LeptonsReweightingweight"]
rrv_w_lumi = ras_zbb["lumiReweightingLumiWeight"]
rrv_w_ptz = ras_zbb["eventSelectionbestzptMu"]

#w = RooFormulaVar("w","w", "1.*1.", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))

w1 = RooFormulaVar("w1","w1", "@0*@1*@2", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))
#w2 = RooFormulaVar("w2","w2", "@0*@1*@2*1.1", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))

#357.15/402.1   392.86/400.05  393.94/401.23
#276.63/313.7 electron

#w2 = RooFormulaVar("w2","w2", "@0*@1*@2*(1.1*(392.86/400.05)*(-9.25908e-13* min(@3*@3*@3*@3*@3*@3,2.87229003906250000e+13) + 6.83686e-10* min(@3*@3*@3*@3*@3,1.64130859375000000e+11) -1.8346e-07 * min(@3*@3*@3*@3,9.37890625000000000e+08) + 2.19074e-05 *min(@3*@3*@3,5.35937500000000000e+06) -0.0011533 *min(@3*@3,3.06250000000000000e+04) + 0.0264567 *min(@3,175.) +0.687981))", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi,rrv_w_ptz)) 

#w2 = RooFormulaVar("w2","w2", "@0*@1*@2*(1.1*(1.)*(-9.25908e-13*2* min(@3*@3*@3*@3*@3*@3,2.87229003906250000e+13) + 6.83686e-10*2* min(@3*@3*@3*@3*@3,1.64130859375000000e+11) -1.8346e-07 *2* min(@3*@3*@3*@3,9.37890625000000000e+08) + 2.19074e-05 *2* min(@3*@3*@3,5.35937500000000000e+06) -0.0011533 *2* min(@3*@3,3.06250000000000000e+04) + 0.0264567 *2* min(@3,175.) +0.687981/2.))", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi,rrv_w_ptz))

w2 = RooFormulaVar("w2","w2", "@0*@1*@2*((419.86/414.71)*(-1.84241e-12 * min(@3*@3*@3*@3*@3*@3,2.87229003906250000e+13) + 1.41919e-09 * min(@3*@3*@3*@3*@3,1.64130859375000000e+11) - 3.89175e-07 * min(@3*@3*@3*@3,9.37890625000000000e+08) + 4.77903e-05 *min(@3*@3*@3,5.35937500000000000e+06) -0.00266683*min(@3*@3,3.06250000000000000e+04) + 0.0646297*min(@3,175.) +0.320127))", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi,rrv_w_ptz))

#w = RooFormulaVar("w","w", "1.", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))

#################################  
### working point & selection ###
#################################

muMassCut = "(eventSelectionbestzmassMu>76&eventSelectionbestzmassMu<106)"
elMassCut = "(eventSelectionbestzmassEle>76&eventSelectionbestzmassEle<106)"

for sample in totsampleList:
    myRDS_red[sample] = myRDS[sample].reduce("rc_eventSelection_"+WP+"==1")

    if extraCut : myRDS_red[sample] = myRDS_red[sample].reduce(extraCut)

    if channel =="Mu" :
        myRDS_red[sample]=myRDS_red[sample].reduce(muMassCut)
        totalCutString+="&"+muMassCut
    if channel =="El" :
        myRDS_red[sample]=myRDS_red[sample].reduce(elMassCut)
        totalCutString+="&"+elMassCut

    if sample != "DATA" : #myRDS_red[sample].addColumn(w)
        if sample == "Zb" :myRDS_red[sample].addColumn(w2)
        if sample != "Zb" :myRDS_red[sample].addColumn(w1)
    #myRDS_red[sample].addColumn(w)

    if sample != "DATA" :
#        myRDS_red_w[sample] = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red[sample],myRDS_red[sample].get(),"","w1")
        if sample == "Zb" : myRDS_red_w[sample] = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red[sample],myRDS_red[sample].get(),"","w2")
        if sample != "Zb" : myRDS_red_w[sample] = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red[sample],myRDS_red[sample].get(),"","w1")
        
    
    else : myRDS_red_w[sample] = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red[sample],myRDS_red[sample].get())

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
    print "the pure # of ", sample, " MC  ............... ", str(myRDS_red_w[sample].numEntries())[:6]
    sum_MC+=myRDS_red_w[sample].numEntries()
print "===> the pure # of MC ............... ", str(sum_MC)[:6]
print "===> the pure # of DATA ............... ", myRDS_red_w["DATA"].numEntries()

print "***"
sum_MC=0
for sample in MCsampleList:
    print "the effective # of ", sample, " MC for this lumi ... ", str(myRDS_red_w[sample].numEntries()*(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity()))[:6]
    sum_MC+=myRDS_red_w[sample].numEntries()*(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity())
print "===> the effective # of MC    ............... ", str(sum_MC)[:6]
print "===> the effective # of DATA  ............... ", myRDS_red_w["DATA"].numEntries()

print "***"

sum_MC=0
for sample in MCsampleList:
    print "the weighted effective # of ", sample, " MC for this data lumi = ", str(myRDS_red_w[sample].sumEntries()*(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity()))[:6]
    sum_MC+=myRDS_red_w[sample].sumEntries()*(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity())
print "===> the effective, weighted # of MC    ............... ", str(sum_MC)[:6]
print "===> the effective, weighted # of DATA  ............... ", myRDS_red_w["DATA"].numEntries()


#############
### PLOTS ###
#############

#################
### variables ###
#################

namePlotList = [
    "eventSelectionbestzmassMu"  ,  ##
    "eventSelectionbestzmassEle" ,
     "eventSelectionbestzptMu"    ,
     "eventSelectionbestzptEle"   ,
    "jetmetbjet1pt"              ,   
    "jetmetbjet2pt"              ,   
    "jetmetMET"                  ,
    "eventSelectiondphiZbb"      ,
    "eventSelectiondphiZbj1"     , 
    "eventSelectiondijetPt"      ,
    "eventSelectiondijetM"       ,
    "eventSelectiondijetdR"      ,
    "eventSelectiondijetSVdR"    ,
    "eventSelectionZbbM"         ,
#    "eventSelectiondrmumu"       ,
#    "eventSelectiondrelel"       ,
    "eventSelectionZbM"
    ,"mlpZbbvsTTtight"
     ,"jetmetnj"
     ,"mlpZbbvsTT_tight_Wmet"
     ,"mlphiggsvszbb"
    ,"mlphiggsvstt"
    ,"mlphiggsvszz"
    ,"mlphiggsvsbkg"
    ,"mlphiggsvsbkg_fulll"
    ,"mlphiggsvszbb_mu"
    ,"mlphiggsvstt_mu"
    ,"mlphiggsvszz_mu"
    ,"mlphiggsvsbkg_mu"
    ,"mlpZbbvsTT_mu"
    ,"mlpzbbvstt_multi_EE_tight"
    ,"Wgg"           
    ,"Wqq"           
    ,"Wtt"           
#    ,"Wtwb"           
    ,"Wzz3"          
    ,"Wzz0"           
    ,"Whi3"           
    ,"Whi0"
    ,"jetmetMETsignificance"
     ,"jetmetMET"
    ,"mlpzbbttmmll_MeTtest_mll_met"
    ,"mlpzbbttmlltest_mll"
    ]

################
### minimums ###
################
min = {
    "eventSelectionbestzmassMu" :   60 ,  
    "eventSelectionbestzmassEle":   60 ,  
    "eventSelectionbestzptMu"   :    0 ,
    "eventSelectionbestzptEle"  :    0 ,
    "eventSelectiondijetPt"     :    0 ,
    "eventSelectiondrZbj1"      :    0 ,
    "jetmetbjet1pt"             :    5 ,
    "jetmetbjet2pt"             :    5 ,   
    "jetmetMET"                 :    0 , 
    "eventSelectiondphiZbj1"    :    0 ,
    "eventSelectiondphiZbb"     :    0 ,
    "eventSelectiondrZbb"       :    0 ,
    "eventSelectionscaldptZbj1" : -250 ,
    "eventSelectiondijetM"      :    0 ,
    "eventSelectiondijetdR"     :    0 ,
    "eventSelectiondijetSVdR"   :    0 ,
    "eventSelectionZbbM"        :    0 ,
    "eventSelectionZbM"         :    0 ,
    "eventSelectionZbbPt"       :    0 ,
    "jetmetjet1SSVHEdisc"       :    0 ,
    "jetmetjet1SSVHPdisc"       :    0 ,
    "jetmetjet1SVmass"          :    0 ,
    "eventSelectiondrmumu"      :    0 ,
    "eventSelectiondrelel"      :    0 
    ,"mlpZbbvsTTtight" : -0.2
    ,"mlpZbbvsTT_tight_Wmet" : -0.2
    ,"mlpzbbvstt_multi_EE_tight" : -0.2
    ,"jetmetnj":2
    ,"mlphiggsvszbb": -0.5
    ,"mlphiggsvstt": -0.5
    ,"mlphiggsvszz": -0.5
    ,"mlphiggsvsbkg": -0.5
    ,"mlphiggsvsbkg_fulll": -0.5
    ,"mlphiggsvszbb_mu" : -0.5
    ,"mlphiggsvstt_mu" : -0.5
    ,"mlphiggsvszz_mu" : -0.5
    ,"mlphiggsvsbkg_mu" : -0.5
    ,"mlpZbbvsTT_mu" : -0.5
    ,"Wgg"      :    15 
    ,"Wqq"      :    15 
    ,"Wtt"      :    20 
#    ,"Wtwb"      :    20 
    ,"Wzz3"      :    7 
    ,"Wzz0"      :    16 
    ,"Whi3"      :    11 
    ,"Whi0"      :    18 
    ,"jetmetMETsignificance" : 0
    ,"jetmetMET" : 0
    ,"mlpzbbttmmll_MeTtest_mll_met" :-0.2
    ,"mlpzbbttmlltest_mll" : -0.2
    }

################
### maximums ###
################
max = {
    "eventSelectionbestzmassMu" :  120 ,  
    "eventSelectionbestzmassEle":  120 ,  
    "eventSelectionbestzptMu"   :  500 ,
    "eventSelectionbestzptEle"  :  360 ,
    "eventSelectiondijetPt"     :  360 ,
    "eventSelectiondrZbj1"      :    5 ,
    "jetmetbjet1pt"             :  265 ,
    "jetmetbjet2pt"             :  265 ,   
    "jetmetMET"                 :  200 , 
    "eventSelectiondphiZbj1"    :  3.2 ,
    "eventSelectiondphiZbb"     :  3.2 ,
    "eventSelectiondrZbb"       :    5 ,
    "eventSelectionscaldptZbj1" :  250 ,
    "eventSelectiondijetM"      :  300 ,
    "eventSelectiondijetdR"     :    5 ,
    "eventSelectiondijetSVdR"   :    5 ,
    "eventSelectionZbbM"        : 1000 ,
    "eventSelectionZbM"         :  800 ,
    "eventSelectionZbbPt"       :  500 ,
    "jetmetjet1SSVHEdisc"       :    8 ,
    "jetmetjet1SSVHPdisc"       :    8 ,
    "jetmetjet1SVmass"          :    5 ,
    "eventSelectiondrmumu"      :    5 ,
    "eventSelectiondrelel"      :    5 
    ,"mlpZbbvsTTtight"  :1.2
    ,"mlpZbbvsTT_tight_Wmet" : 1.2
    ,"mlphiggsvszbb" : 1.5
    ,"mlphiggsvstt" : 1.5
    ,"mlphiggsvszz" : 1.5
    ,"mlphiggsvsbkg" : 1.5
    ,"mlphiggsvsbkg_fulll": 1.5
    ,"mlphiggsvszbb_mu": 1.5
    ,"mlphiggsvstt_mu" : 1.5
    ,"mlphiggsvszz_mu" : 1.5
    ,"mlphiggsvsbkg_mu" : 1.5
    ,"mlpZbbvsTT_mu" : 1.5
    ,"mlpzbbvstt_multi_EE_tight" : 1.2
    ,"jetmetnj":8
    ,"Wgg"      :    25 
    ,"Wqq"      :    25 
    ,"Wtt"      :    30 
#    ,"Wtwb"      :    30 
    ,"Wzz3"      :    17 
    ,"Wzz0"      :    26 
    ,"Whi3"      :    21
    ,"Whi0"      :    32
    ,"jetmetMETsignificance" : 80
    ,"jetmetMET" : 100
    ,"mlpzbbttmmll_MeTtest_mll_met" : 1.2
    ,"mlpzbbttmlltest_mll" : 1.2
    }

################
### binning  ###
################
binning = {
    "eventSelectionbestzmassMu" :   30 , #2GeV 
    "eventSelectionbestzmassEle":   30 ,  
    "eventSelectionbestzptMu"   :   25 , #20GeV
    "eventSelectionbestzptEle"  :   18 ,
    "eventSelectiondijetPt"     :   18 ,
    "eventSelectiondrZbj1"      :   10 , #0.5
    "jetmetbjet1pt"             :   26 , #10GeV
    "jetmetbjet2pt"             :   26 ,   
    "jetmetMET"                 :   20 , #10GeV 
    "eventSelectiondphiZbj1"    :   16 , #0.2
    "eventSelectiondphiZbb"     :   16 ,
    "eventSelectiondrZbb"       :   10 , #0.5
    "eventSelectionscaldptZbj1" :   50 , #10GeV
    "eventSelectiondijetM"      :   120 , #50GeV
    "eventSelectiondijetdR"     :   10 , #0.5
    "eventSelectiondijetSVdR"   :   10 ,
    "eventSelectionZbbM"        :   20 , #50GeV
    "eventSelectionZbM"         :   16 ,
    "eventSelectionZbbPt"       :   50 , #10GeV
    "jetmetjet1SSVHEdisc"       :   16 , #0.5
    "jetmetjet1SSVHPdisc"       :   16 ,
    "jetmetjet1SVmass"          :   20 , #0.25GeV
    "eventSelectiondrmumu"      :   10 , #0.5
    "eventSelectiondrelel"      :   10
    ,"jetmetnj" : 6
    ,"mlpZbbvsTTtight" :20
    ,"mlpZbbvsTT_tight_Wmet" : 20
    ,"mlphiggsvszbb" : 30
    ,"mlphiggsvstt" : 30
    ,"mlphiggsvszz" : 30
    ,"mlphiggsvsbkg" : 30
    ,"mlphiggsvsbkg_fulll": 30
    ,"mlpzbbvstt_multi_EE_tight" : 20
    ,"mlphiggsvszbb_mu": 30
    ,"mlphiggsvstt_mu" : 30
    ,"mlphiggsvszz_mu" : 30
    ,"mlphiggsvsbkg_mu" :30 
    ,"mlpZbbvsTT_mu" : 30
    ,"Wgg"      :    25 
    ,"Wqq"      :    25 
    ,"Wtt"      :    25 
 #   ,"Wtwb"      :    30 
    ,"Wzz3"      :    20 
    ,"Wzz0"      :    25 
    ,"Whi3"      :    20 
    ,"Whi0"      :    35
    ,"jetmetMETsignificance" : 80
    ,"jetmetMET" : 20
    ,"mlpzbbttmmll_MeTtest_mll_met" : 20
    ,"mlpzbbttmlltest_mll" : 20
    }
    

var = {}
for name in namePlotList:
    print "name = ", name
    var[name] = ras_zbb[name] #ws.var(name)
    var[name].setMin(min[name])
    var[name].setMax(max[name])
    var[name].setBins(binning[name])


###############
### sum pdf ###
###############

num_MC = {}

numList = RooArgList()

for sample in MCsampleList:
    num_MC[sample] = RooRealVar("num_MC_"+sample,"num_MC_"+sample,
                                myRDS_red_w[sample].sumEntries()*(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity()))
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
    lumiratio[sample]=getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity()
    print "lumi ratio for ", sample, " = ", lumiratio[sample]

#norm["ZHbb"] = 50*norm["ZHbb"]

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

th2 = {}
th1 = {}
th1_copy = {}

componentString={}

# TH2 Plot
for sample in totsampleList:
    for name in namePlotList:
        th2[sample+"whi3"+name] = TH2D("whi3"+name+"_"+sample,"whi3"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["Whi3"].getBins(),var["Whi3"].getMin(),var["Whi3"].getMax())
        myRDS_red_w[sample].fillHistogram(th2[sample+"whi3"+name], RooArgList(var[name],var["Whi3"]))
#        CANVAS[sample+"whi3"+name] = TCanvas("CANVAS_whi3"+name,"CANVASwhi3"+name,1200,600)
#        th2[sample+"whi3"+name].Draw()

        th2[sample+"whi0"+name] = TH2D("whi0"+name+"_"+sample,"whi0"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["Whi0"].getBins(),var["Whi0"].getMin(),var["Whi0"].getMax())
        myRDS_red_w[sample].fillHistogram(th2[sample+"whi0"+name], RooArgList(var[name],var["Whi0"]))
#        CANVAS[sample+"whi0"+name] = TCanvas("CANVAS_whi0"+name,"CANVASwhi0"+name,1200,600)
#        th2[sample+"whi0"+name].Draw()

        th2[sample+"wgg"+name] = TH2D("wgg"+name+"_"+sample,"wgg"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["Wgg"].getBins(),var["Wgg"].getMin(),var["Wgg"].getMax())
        myRDS_red_w[sample].fillHistogram(th2[sample+"wgg"+name], RooArgList(var[name],var["Wgg"]))
#        CANVAS[sample+"wgg"+name] = TCanvas("CANVAS_wgg"+name,"CANVASwgg"+name,1200,600)
#        th2[sample+"wgg"+name].Draw()


        th2[sample+"wqq"+name] = TH2D("wqq"+name+"_"+sample,"wqq"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["Wqq"].getBins(),var["Wqq"].getMin(),var["Wqq"].getMax())
        myRDS_red_w[sample].fillHistogram(th2[sample+"whi3"+name], RooArgList(var[name],var["Wqq"]))
#        CANVAS[sample+"wqq"+name] = TCanvas("CANVAS_wqq"+name,"CANVASwqq"+name,1200,600)
#        th2[sample+"wqq"+name].Draw()

        th2[sample+"wtt"+name] = TH2D("wtt"+name+"_"+sample,"wtt"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["Wtt"].getBins(),var["Wtt"].getMin(),var["Wtt"].getMax())
        myRDS_red_w[sample].fillHistogram(th2[sample+"wtt"+name], RooArgList(var[name],var["Wtt"]))
#        CANVAS[sample+"wtt"+name] = TCanvas("CANVAS_wtt"+name,"CANVASwtt"+name,1200,600)
#        th2[sample+"wtt"+name].Draw()

        th2[sample+"mlphiggsvsbkg"+name] = TH2D("mlphiggsvsbkg"+name+"_"+sample,"mlphiggsvsbkg"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["mlphiggsvsbkg"].getBins(),var["mlphiggsvsbkg"].getMin(),var["mlphiggsvsbkg"].getMax())
        myRDS_red_w[sample].fillHistogram(th2[sample+"mlphiggsvsbkg"+name], RooArgList(var[name],var["mlphiggsvsbkg"]))
#        CANVAS[sample+"mlphiggsvsbkg"+name] = TCanvas("CANVAS_mlphiggsvsbkg"+name,"CANVASmlphiggsvsbkg"+name,1200,600)
#        th2[sample+"mlphiggsvsbkg"+name].Draw()
    
#-----------------------------------
for name in namePlotList:
        sampleList = RooArgList()
        for sample in totsampleList:
            th1[sample+name] = TH1D(name,name,var[name].getBins(),var[name].getMin(),var[name].getMax())
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

        totalMConDATA = (num_MC["Zb"].getVal()+num_MC["Zc"].getVal()+num_MC["Zl"].getVal()+num_MC["TT"].getVal()+num_MC["ZZ"].getVal())/myRDS_red_w["DATA"].numEntries()
        var_frame[name] = var[name].frame()
        myRDS_red_w["DATA"].plotOn(var_frame[name],
                                   RooFit.MarkerSize(1.0),
                                   RooFit.XErrorSize(0.035),
                                   RooFit.DrawOption("pe2"))
        rap[name].plotOn(var_frame[name],
                         RooFit.Components("rhp_TT,rhp_Zb,rhp_ZZ,rhp_Zc,rhp_Zl"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kBlue-7),
                         RooFit.DrawOption("F"),
                         RooFit.LineWidth(1),
                         RooFit.Normalization(totalMConDATA))
        rap[name].plotOn(var_frame[name],
                         RooFit.Components("rhp_TT,rhp_Zb,rhp_ZZ,rhp_Zc"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kGreen-7),
                         RooFit.DrawOption("F"),
                         RooFit.LineWidth(1),
                         RooFit.Normalization(totalMConDATA))
        rap[name].plotOn(var_frame[name],
                         RooFit.Components("rhp_TT,rhp_Zb,rhp_ZZ"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kRed-7),
                         RooFit.DrawOption("F"),
                         RooFit.LineWidth(1),
                         RooFit.Normalization(totalMConDATA))
        rap[name].plotOn(var_frame[name],
                         RooFit.Components("rhp_TT,rhp_ZZ"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kYellow-7),
                         RooFit.DrawOption("F"),
                         RooFit.LineWidth(1),
                         RooFit.Normalization(totalMConDATA))
        rap[name].plotOn(var_frame[name],
                         RooFit.Components("rhp_ZZ"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kPink-7),
                         RooFit.DrawOption("F"),
                         RooFit.LineWidth(1),
                         RooFit.Normalization(totalMConDATA))
        rhp["ZH125"].plotOn(var_frame[name],
                            RooFit.LineColor(kRed),
                            RooFit.LineWidth(1),
                            RooFit.Normalization(norm["ZH125"]))
        myRDS_red_w["DATA"].plotOn(var_frame[name],
                                   RooFit.MarkerSize(1.0),
                                   RooFit.XErrorSize(0.035),
                                   RooFit.DrawOption("pe2"))
        
        
        CANVAS[name] = TCanvas("CANVAS"+name,"CANVAS"+name,1200,600)
        CANVAS[name].Divide(2)
        
        CANVAS[name].cd(1)
        var_frame[name].Draw()
        CANVAS[name].cd(2)
        th1["DATA"+name].Draw()
        #CANVAS[name].SaveAs(name+"_"+channel+".gif")
        #CANVAS[name].SaveAs(name+"_"+channel+".eps")

        
        for sample in ("Zb","Zc","Zl","TT","ZZ"): th1[sample+name].DrawNormalized("same hist",num_MC[sample].getVal())
        #th1_copy["DATA"+name].Draw()
        #for sample in ("DY","TT","ZZ"): th1_copy[sample+name].DrawNormal

plot = TFile("All_plot_mm_ptzrew_rescale_100higgs_correl.root","RECREATE")
for name in namePlotList:
    CANVAS[name].Write()
    for sample in totsampleList:
        th2[sample+"wtt"+name].Write()
        th2[sample+"wqq"+name].Write()
        th2[sample+"wgg"+name].Write()
        th2[sample+"whi0"+name].Write()
        th2[sample+"whi3"+name].Write()
        th2[sample+"mlphiggsvsbkg"+name].Write()

plot.Close()

#----------------------------------------------------------------------


file={}
for sample in totsampleList:
  file[sample]=TFile("TH1s"+sample+".root","RECREATE")
  #for name in namePlotList: th1[sample+name].Write("th1_"+name)
  for name in namePlotList:
    if name == "eventSelectionbestzptMu" and channel =="El":
      continue
    if name == "eventSelectionbestzptEle" and channel =="Mu":
      continue
    th1[sample+name].Write()
  file[sample].Close()
    
#This file contains the yields for the given lumi
fileYields=TFile("THYields.root", "RECREATE")

StackCanvas={}
for name in namePlotList:

  if name == "eventSelectionbestzptMu" and channel =="El":
    continue
  if name == "eventSelectionbestzptEle" and channel =="Mu":
    continue

  #First save signal/s
  signalSamples = ["ZH125"]
  for signalsample in signalSamples:
    signoerror = RemoveErrorsHisto(th1[signalsample+name])
    signoerror.Scale(MCweight[signalsample])
    signoerror.SetLineColor(kRed)
    signoerror.Write("th_"+name+"_"+signalsample)
    
  #for sample in totsampleList:
  orderSamplesPlot = ["DATA", "ZZ", "TT", "Zb","Zc","Zl"]
  stack = THStack("stack"+name, "Normalized to lumi")
  StackCanvas[name] = TCanvas("StackCanvas"+name,"StackCanvas"+name,1200,600)
  for sample in orderSamplesPlot:
    
    if not sample == "DATA":
      #print "MCweight[", sample,"]=", MCweight[sample]
      th1[sample+name].Scale(MCweight[sample])
    if sample == "Zl" :
      th1[sample+name].SetFillColor(kBlue-7)
      #th1[sample+name].SetMarkerStyle(21)
      #th1[sample+name].SetMarkerColor(kBlue-7)
    if sample == "Zc" :
      th1[sample+name].SetFillColor(kGreen-7),
      #th1[sample+name].SetMarkerStyle(21),
      #th1[sample+name].SetMarkerColor(kGreen-7),
    if sample == "Zb" :
      th1[sample+name].SetFillColor(kRed-7)
      #th1[sample+name].SetMarkerStyle(21)
      #th1[sample+name].SetMarkerColor(kRed-7)
    if sample == "TT" :
      th1[sample+name].SetFillColor(kYellow-7),
      #th1[sample+name].SetMarkerStyle(21),
      #th1[sample+name].SetMarkerColor(kYellow-7),
    if sample == "ZZ" :
      th1[sample+name].SetFillColor(kPink-7),
      #th1[sample+name].SetMarkerStyle(21),
      #th1[sample+name].SetMarkerColor(kPink-7),
	
    if not sample == "DATA":
      th1[sample+name].Write("th_"+name+"_"+sample)
      x=1==1
    else:
      th1[sample+name].Write("th_"+name+"_"+sample)
    
    if not sample == "DATA":
      thnoerrors = RemoveErrorsHisto(th1[sample+name])
      #stack.Add(th1[sample+name], "hist p")
      stack.Add(thnoerrors)
  stack.Write()
  
  if stack.GetMaximum() > th1["DATA"+name]:
    stack.Draw()
    th1["DATA"+name].Draw("sames")
  else:
    th1["DATA"+name].Draw()
    stack.Draw("sames")
  StackCanvas[name].Write("cv"+name)
  
fileYields.Close()                
