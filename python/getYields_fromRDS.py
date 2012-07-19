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
from zbbCommons import zbbnorm

#####################################################
### sample/wp/selection of interest
#####################################################

WP       = "9"    #"HP","HPMET","HP_excl","HE","HEmet","He_excl"
channel  = "Mu"    #"El","Mu"
extraCut = ""#jetmetbjet1pt>25.&jetmetbjet2pt>25.&jetmetMET<50."

totalCutString = ""+extraCut

#####################################################
### settings (this should move somewhere central) ### 
#####################################################

MCsampleList   = ["Zb","Zc","Zl","TT","ZZ","ZH125"]
SMMCsampleList = ["Zb","Zc","Zl","TT","ZZ"]
totsampleList  = ["DATA","Zb","Zc","Zl","TT","ZZ","ZH125"]
sampleList  = ["DATA","DY","TT","ZZ","ZH125"]


lumi = { "DATA"   : zbbnorm.lumi_tot2011,
         "TT"     : zbbnorm.nev_TTjets_fall11/zbbnorm.xsec_TTjets_7TeV/1000.,
         "Zb"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "Zc"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "Zl"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "ZZ"     : zbbnorm.nev_ZZ_fall11/zbbnorm.xsec_ZZ_7TeV/1000.,
         "ZH125"  : zbbnorm.nev_ZH125_fall11/zbbnorm.xsec_ZH125_7TeV/1000.
         }
print lumi["DATA"]

MCweight = {}

for sample in MCsampleList:
    print "the lumi of ", sample, " = ", lumi[sample]
    MCweight[sample] = lumi["DATA"]/lumi[sample]
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
if channel  == "El" :
  filename = {"DATA_A" : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ElA_DATA.root",
                 "DATA_B" : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ElB_DATA.root",
                 "TT"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_TT_El_MC.root",
                 "DY"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_El_MC.root",
                 "ZZ"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ZZ_El_MC.root",
                 "ZH125"  : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ZH125_El_MC.root"
                 }
		 
elif channel == "Mu" :
  filename = {"DATA_A" : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_MuA_DATA.root",
                 "DATA_B" : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_MuB_DATA.root",
                 "TT"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_TT_Mu_MC.root",
                 "DY"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_Mu_MC.root",
                 "ZZ"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ZZ_Mu_MC.root",
                 "ZH125"  : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ZH125_Mu_MC.root"
                 }
else :
  print "Invalid channel name = ", channel, ". Exitting!"
  exit()


for sample in sampleList :

    redStage = "rc_eventSelection_"+WP+"==1"

    if sample != "DATA":
        
        file_mc  = TFile(filename[sample])
        
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
        file_A  = TFile(filename["DATA_A"])
        file_B  = TFile(filename["DATA_B"])

        nEntries = file_A.Get("rds_zbb").numEntries()+file_B.Get("rds_zbb").numEntries()

        myRDS[sample] = file_A.Get("rds_zbb").reduce(redStage)
        tmp = file_B.Get("rds_zbb").reduce(redStage)
        myRDS[sample].append(tmp)

        print "myRDS.numEntries() for ", sample , " = ", nEntries, ". After stage ", WP, " : ", myRDS[sample].numEntries()

        file_A.Close()
        file_B.Close()

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


w = RooFormulaVar("w","w", "@0*@1*@2", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))

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

    if sample != "DATA" : myRDS_red[sample].addColumn(w)
    #myRDS_red[sample].addColumn(w)

    if sample != "DATA" : myRDS_red_w[sample] = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red[sample],myRDS_red[sample].get(),"","w")
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
    print "the effective # of ", sample, " MC for this lumi ... ", str(myRDS_red_w[sample].numEntries()*(lumi["DATA"]/lumi[sample]))[:6]
    sum_MC+=myRDS_red_w[sample].numEntries()*(lumi["DATA"]/lumi[sample])
print "===> the effective # of MC    ............... ", str(sum_MC)[:6]
print "===> the effective # of DATA  ............... ", myRDS_red_w["DATA"].numEntries()

print "***"

sum_MC=0
for sample in MCsampleList:
    print "the weighted effective # of ", sample, " MC for this data lumi = ", str(myRDS_red_w[sample].sumEntries()*(lumi["DATA"]/lumi[sample]))[:6]
    sum_MC+=myRDS_red_w[sample].sumEntries()*(lumi["DATA"]/lumi[sample])
print "===> the effective, weighted # of MC    ............... ", str(sum_MC)[:6]
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
#    "eventSelectionbestzptMu"    ,
#    "eventSelectionbestzptEle"   ,
#    "jetmetbjet1pt"              ,   
#    "jetmetbjet2pt"              ,   
#    "jetmetMET"                  ,
#    "eventSelectiondphiZbb"      ,
#    "eventSelectiondphiZbj1"     , 
#    "eventSelectiondijetPt"      ,#
#    "eventSelectiondijetM"       ,
    "eventSelectiondijetdR"      ,
#    "eventSelectiondijetSVdR"    ,
#    "eventSelectionZbbM"         ,
    #"eventSelectiondrmumu"       ,
    #"eventSelectiondrelel"       ,
    "eventSelectionZbM"
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
    }

################
### maximums ###
################
max = {
    "eventSelectionbestzmassMu" :  120 ,  
    "eventSelectionbestzmassEle":  120 ,  
    "eventSelectionbestzptMu"   :  360 ,
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
    "eventSelectiondijetM"      :  600 ,
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
    }

################
### binning  ###
################
binning = {
    "eventSelectionbestzmassMu" :   30 , #2GeV 
    "eventSelectionbestzmassEle":   30 ,  
    "eventSelectionbestzptMu"   :   18 , #20GeV
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
    "eventSelectiondijetM"      :   12 , #50GeV
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

#norm["ZHbb"] = 10*norm["ZHbb"]

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
    #for sample in ("DY","TT","ZZ"): th1_copy[sample+name].DrawNormalized("same hist",num_MC[sample].getVal())
    
    
file={}
for sample in totsampleList:
    file[sample]=TFile("TH1s"+sample+".root","RECREATE")
    #for name in namePlotList: th1[sample+name].Write("th1_"+name)
    for name in namePlotList: th1[sample+name].Write()
    file[sample].Close()
