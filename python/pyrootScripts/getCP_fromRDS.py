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
import math
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from zbbCommons import zbbnorm

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

WP       = "18"    #"HP","HPMET","HP_excl","HE","HEmet","He_excl"
channel  = "El"    #"El","Mu"
#extraCut = "eventSelectionbestzmassEle>76.&eventSelectionbestzmassEle<106.&jetmetbjet1pt>25&jetmetbjet2pt>25"
#extraCut = "eventSelectionbestzmassMu>76.&eventSelectionbestzmassMu<106.&jetmetbjet1pt>25&jetmetbjet2pt>25"

extraCut = "jetmetMETsignificance < 10"
#extraCut = "mlphiggsvsbkg_125_comb_MM_N<0.5&mlphiggsvsbkg_125_comb_MM_N>-1.5"
#extraCut = ""

totalCutString = ""+extraCut

#####################################################
### settings (this should move somewhere central) ### 
#####################################################

MCsampleList   = ["Zb","Zc","Zl","TT","ZZ","ZH125"]
SMMCsampleList = ["Zb","Zc","Zl","TT","ZZ"]
totsampleList  = ["DATA","Zb","Zc","Zl","TT","ZZ","ZH125"]
sampleList  = ["DATA","DY","TT","ZZ","ZH125"]


lumi = { "DATA"   : zbbnorm.lumi_totEl2011,
         "TT"     : zbbnorm.nev_TTjets_fall11/zbbnorm.xsec_TTjets_7TeV/1000.,
         "Zb"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "Zc"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "Zl"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "ZZ"     : zbbnorm.nev_ZZ_fall11/zbbnorm.xsec_ZZ_7TeV/1000.,
         "ZH125"  : zbbnorm.nev_ZH125_fall11/zbbnorm.xsec_ZH125_7TeV_Mu/1000.
         }
	 
Extra_norm={ "DATA" : 1.0,
             "TT"    : 0.91,
	     "Zb"    : 1.035,
	     "Zc"    : 0.91,
	     "Zl"    : 0.91,
	     "ZZ"    : 1.0,
	     "ZH125" : 100.0	      	      	      
            }
	    	 
print lumi["DATA"]

MCweight = {}

for sample in MCsampleList:
    print "the lumi of ", sample, " = ", (lumi[sample]*Extra_norm[sample])
    MCweight[sample] = lumi["DATA"]*Extra_norm[sample]/(lumi[sample])
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
#if channel  == "El" :
#  filename = {"DATA_A" : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ElA_DATA.root",
#                 "DATA_B" : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ElB_DATA.root",
#                 "TT"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_TT_El_MC.root",
#                 "DY"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_El_MC.root",
#                 "ZZ"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ZZ_El_MC.root",
#                 "ZH125"  : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ZH125_El_MC.root"
#                 }
#		 
#elif channel == "Mu" :
#  filename = {"DATA_A" : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_MuA_DATA.root",
#                 "DATA_B" : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_MuB_DATA.root",
#                 "TT"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_TT_Mu_MC.root",
#                 "DY"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_Mu_MC.root",
#                 "ZZ"     : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ZZ_Mu_MC.root",
#                 "ZH125"  : "FARM_makeRDSnoWS120718Adrien/File_rds_zbb_ZH125_Mu_MC.root"
#                 }
#else :
#  print "Invalid channel name = ", channel, ". Exitting!"
#  exit()
#

inputfolder ="/home/fynu/arnaudp/scratch/Zbb_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/scripts/ME_Analysis/Merging/"
#inputfolder ="/home/fynu/vizangarciaj/CMSSW44btag_120711/CMSSW_4_4_4/src/UserCode/zbb_louvain/scripts/ME_Analysis/Merging/testsCSV2011/"
#inputfolder ="/home/fynu/vizangarciaj/storage/CMSSW444_121207_forCSV2011Branch/CMSSW_4_4_4/src/UserCode/zbb_louvain/scripts/ME_Analysis/Merging/testCSV2011_124110/"


if channel  == "El" :
  filename = {"DATA_A" : inputfolder+"RDS_rdsME_ElA_DATA.root",
                 "DATA_B" : inputfolder+"RDS_rdsME_ElB_DATA.root",
                 "TT"     : inputfolder+"RDS_rdsME_TT_El_MC.root",
                 "DY"     : inputfolder+"RDS_rdsME_El_MC.root",
                 "ZZ"     : inputfolder+"RDS_rdsME_ZZ_El_MC.root",
                 "ZH125"  : inputfolder+"RDS_rdsME_ZH125_El_MC.root"
                 }
		 
elif channel == "Mu" :
  filename = {"DATA_A" : inputfolder+"RDS_rdsME_MuA_DATA.root",
                 "DATA_B" : inputfolder+"RDS_rdsME_MuB_DATA.root",
                 "TT"     : inputfolder+"RDS_rdsME_TT_Mu_MC.root",
                 "DY"     : inputfolder+"RDS_rdsME_Mu_MC.root",
                 "ZZ"     : inputfolder+"RDS_rdsME_ZZ_Mu_MC.root",
                 "ZH125"  : inputfolder+"RDS_rdsME_ZH125_Mu_MC.root"
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
          #myRDS["Zb"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==3")
          #myRDS["Zc"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==2")
          #myRDS["Zl"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==1")
          myRDS["Zb"] = file_mc.Get("rds_zbb").reduce(redStage + "&abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)==5")
          myRDS["Zc"] = file_mc.Get("rds_zbb").reduce(redStage + "&((abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5)||(abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5))")
          myRDS["Zl"] = file_mc.Get("rds_zbb").reduce(redStage + "&abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)!=5")          
	  
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

rrv_w_b = {"5"  : ras_zbb["BtaggingReweightingHP"]  ,
           "6"  : ras_zbb["BtaggingReweightingHE"]  ,
           "7"  : ras_zbb["BtaggingReweightingHP"]  ,
           "8"  : ras_zbb["BtaggingReweightingHE"]  ,
           "9"  : ras_zbb["BtaggingReweightingHP"], 
           "10" : ras_zbb["BtaggingReweightingHEHE"],
           "11" : ras_zbb["BtaggingReweightingHEHP"],
           "12" : ras_zbb["BtaggingReweightingHPHP"],
           "13" : ras_zbb["BtaggingReweightingHEHE"],
           "14" : ras_zbb["BtaggingReweightingHEHP"],
           "15" : ras_zbb["BtaggingReweightingHEHP"]  ,
           "16" : ras_zbb["BtaggingReweightingHEHE"], 
           "17" : ras_zbb["BtaggingReweightingHEHP"],
           "18" : ras_zbb["BtaggingReweightingHPHP"],
           
           }

rrv_w_lep  = ras_zbb["LeptonsReweightingweight"]
rrv_w_lumi = ras_zbb["lumiReweightingLumiWeight"]
rrv_w_ptz = ras_zbb["eventSelectionbestzptMu"]
#rrv_w_ptz = ras_zbb["eventSelectionbestzptEle"]

#w1 = RooFormulaVar("w","w", "1.0", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))
#w2 = RooFormulaVar("w","w", "1.0", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))

w1 = RooFormulaVar("w1","w1", "@0*@1*@2", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))
w2 = RooFormulaVar("w2","w2", "@0*@1*@2", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))


# param from All region Muon Correct
#w2 = RooFormulaVar("w2","w2", "@0*@1*@2*(762.38/788.74)*((@3<10)+(@3>170) + ((@3>10)*(@3<170)*(-8.006e-12* pow(@3,6) +4.847e-09 * pow(@3,5)-1.109e-06* pow(@3,4) +1.19518e-04 * pow(@3,3) -0.00617*@3*@3 +0.144223*@3 -0.31819)))", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi,rrv_w_ptz))

# param from Control region Muon Correct
# MM_M muon : 762.38/786.
#w2 = RooFormulaVar("w2","w2", "@0*@1*@2*(2190.8/2231.4)*((@3<10)+(@3>170) + ((@3>10)*(@3<170)*(-9.4148e-12* pow(@3,6) +5.83e-09 * pow(@3,5)-1.358e-06* pow(@3,4) +1.478e-04 * pow(@3,3) -0.00763*@3*@3 +0.176722*@3 -0.601081)))", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi,rrv_w_ptz))

#----------------------------------------------------------------

# param from All region Electron Correct
#w2 = RooFormulaVar("w2","w2", "@0*@1*@2*(1.0)*((@3<10)+(@3>170) + ((@3>10)*(@3<170)*(1.35014e-13* pow(@3,6) +3.1e-10 * pow(@3,5)-1.655e-07* pow(@3,4) +2.8435e-05 * pow(@3,3) -0.00200135*@3*@3 +0.05769*@3 +0.273914)))", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi,rrv_w_ptz))

# param from Control region ElectronCorrect
# MM_M muon : .
#w2 = RooFormulaVar("w2","w2", "@0*@1*@2*(1.0)*((@3<10)+(@3>170) + ((@3>10)*(@3<170)*(-3.4399e-12* pow(@3,6) +2.544e-09 * pow(@3,5)-6.92e-07* pow(@3,4) +8.69e-05 * pow(@3,3) -0.00511*@3*@3 +0.1289*@3 -0.211998)))", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi,rrv_w_ptz))

#ee
#w2 = RooFormulaVar("w2","w2", "@0*@1*@2*(574.2/542.89)*((@3<10)+(@3>170) + ((@3>10)*(@3<170)*(-3.379031e-07 * pow(@3,3) +5.74726e-05 *@3*@3 +0.003684317*@3 +0.5997106)))", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi,rrv_w_ptz))

#mm 762.38/716.57 old categories
#w2 = RooFormulaVar("w2","w2", "@0*@1*@2*(616.14/583.10)*((@3<10)+(@3>170) + ((@3>10)*(@3<170)*(-3.379031e-07 * pow(@3,3) +5.74726e-05 *@3*@3 +0.003684317*@3 +0.5997106)))", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi,rrv_w_ptz))



#w = RooFormulaVar("w","w", "1.", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))

#----------------------------------------------------------------

#################################  
### working point & selection ###
#################################

#muMassCut = "(eventSelectionbestzmassMu>76&eventSelectionbestzmassMu<106)"
#elMassCut = "(eventSelectionbestzmassEle>76&eventSelectionbestzmassEle<106)"

muMassCut = "(eventSelectionbestzmassMu>50)"
elMassCut = "(eventSelectionbestzmassEle>50)"



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
    print "the effective # of ", sample, " MC for this lumi ... ", str(myRDS_red_w[sample].numEntries()*(lumi["DATA"]*Extra_norm[sample]/lumi[sample]))[:6]
    sum_MC+=myRDS_red_w[sample].numEntries()*(lumi["DATA"]*Extra_norm[sample]/lumi[sample])
print "===> the effective # of MC    ............... ", str(sum_MC)[:6]
print "===> the effective # of DATA  ............... ", myRDS_red_w["DATA"].numEntries()

print "***"

sum_MC=0
for sample in MCsampleList:
    print "the weighted effective # of ", sample, " MC for this data lumi = ", str(myRDS_red_w[sample].sumEntries()*(lumi["DATA"]*Extra_norm[sample]/(lumi[sample])))[:6]
    sum_MC+=myRDS_red_w[sample].sumEntries()*(lumi["DATA"]*Extra_norm[sample]/(lumi[sample]))
print "===> the effective, weighted # of MC    ............... ", str(sum_MC)[:6]
print "===> the effective, weighted # of DATA  ............... ", myRDS_red_w["DATA"].numEntries()


#############
### PLOTS ###
#############

#################
### variables ###
#################

namePlotList = [
    "eventSelectionbestzmassMu"  , 
    "eventSelectionbestzmassEle" ,
     "eventSelectionbestzptMu",    
     "eventSelectionbestzptEle"   ,
    "jetmetbjet1pt"              ,   
    "jetmetbjet2pt"              ,   
    "jetmetbjet1CSVdisc"              ,   
    "jetmetbjet2CSVdisc"              ,   
    "jetmetbjetMinCSVdisc"              ,   
    "jetmetbjetMaxCSVdisc"              ,
    "jetmetbjetProdCSVdisc"              ,   
    "jetmetMET"                  ,
    "eventSelectiondphiZbb"      ,
    "eventSelectiondphiZbj1"     , 
    "eventSelectiondijetPt"      ,
    "eventSelectiondijetM"       ,
    "eventSelectiondijetdR"      ,
 #   "eventSelectiondijetSVdR"    ,
    "eventSelectionZbbM"         ,
 #   "eventSelectiondrmumu"       ,
#   "eventSelectiondrelel"       ,
    "eventSelectionZbM"
     ,"jetmetnj"
    ,"Wgg"           
    ,"Wqq"           
    ,"Wtt"           
#    ,"Wtwb"           
    ,"Wzz3"          
    ,"Wzz0"           
    ,"Whi3_125"           
    ,"Whi0_125"
    ,"jetmetMETsignificance"
     ,"jetmetMET"

    #,"mlpZbbvsTT_MM"
    ,"mlpZbbvsTT_MM_N"
    #,"mlpZbbvsTT_ML"
    #,"mlpZbbvsTT_mu_MM"
    ,"mlpZbbvsTT_mu_MM_N"
    #,"mlpZbbvsTT_mu_ML"
    #,"mlphiggsvszbb_125_MM"
    #,"mlphiggsvstt_125_MM"
    #,"mlphiggsvszz_125_MM"
    #,"mlphiggsvsbkg_125_MM"
    #,"mlphiggsvszbb_125_ML"
    #,"mlphiggsvstt_125_ML"
    #,"mlphiggsvszz_125_ML"
    #,"mlphiggsvsbkg_125_ML"
    #,"mlphiggsvszbb_125_MM_N"
    #,"mlphiggsvstt_125_MM_N"
    #,"mlphiggsvszz_125_MM_N"
    #,"mlphiggsvsbkg_125_MM_N"
    #,"mlphiggsvszbb_125_mu_MM"
    #,"mlphiggsvstt_125_mu_MM"
    #,"mlphiggsvszz_125_mu_MM"
    #,"mlphiggsvsbkg_125_mu_MM"
    #,"mlphiggsvszbb_125_mu_ML"
    #,"mlphiggsvstt_125_mu_ML"
    #,"mlphiggsvszz_125_mu_ML"
    #,"mlphiggsvsbkg_125_mu_ML"
    #,"mlphiggsvszbb_125_mu_MM_N"
    #,"mlphiggsvstt_125_mu_MM_N"
    #,"mlphiggsvszz_125_mu_MM_N"
    #,"mlphiggsvsbkg_125_mu_MM_N"
   ,"mlphiggsvsbkg_125_comb_MM_N"
   ,"mlphiggsvszbb_125_comb_MM_N"
   ,"mlphiggsvszz_125_comb_MM_N"
   ,"mlphiggsvstt_125_comb_MM_N"
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
    "jetmetbjet1CSVdisc"             :    0 ,
    "jetmetbjet2CSVdisc"             :    0 ,   
    "jetmetbjetMinCSVdisc"             :    0 ,
    "jetmetbjetMaxCSVdisc"             :    0 ,
    "jetmetbjetProdCSVdisc"             :    0 ,
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
    ,"jetmetnj":2
    ,"Wgg"      :    16 
    ,"Wqq"      :    16 
    ,"Wtt"      :    20 
#    ,"Wtwb"      :    20 
    ,"Wzz3"      :    8 
    ,"Wzz0"      :    18
    ,"Whi3_125"      :    11 
    ,"Whi0_125"      :    21 
    ,"jetmetMETsignificance" : 0
    ,"jetmetMET" : 0

    ,"mlpZbbvsTT_MM" : 0
    ,"mlpZbbvsTT_MM_N" : 0
    ,"mlpZbbvsTT_ML" : 0
    ,"mlpZbbvsTT_mu_MM" : 0
    ,"mlpZbbvsTT_mu_MM_N" : 0
    ,"mlpZbbvsTT_mu_ML" : 0
    ,"mlphiggsvszbb_125_MM" : 0
    ,"mlphiggsvstt_125_MM" : 0
    ,"mlphiggsvszz_125_MM" : 0
    ,"mlphiggsvsbkg_125_MM" : 0
    ,"mlphiggsvszbb_125_ML" : 0
    ,"mlphiggsvstt_125_ML" : 0
    ,"mlphiggsvszz_125_ML" : 0
    ,"mlphiggsvsbkg_125_ML" : 0
    ,"mlphiggsvszbb_125_MM_N" : 0
    ,"mlphiggsvstt_125_MM_N" : 0
    ,"mlphiggsvszz_125_MM_N" : 0
    ,"mlphiggsvsbkg_125_MM_N" : 0
    ,"mlphiggsvszbb_125_mu_MM" : 0
    ,"mlphiggsvstt_125_mu_MM" : 0
    ,"mlphiggsvszz_125_mu_MM" : 0
    ,"mlphiggsvsbkg_125_mu_MM" : 0
    ,"mlphiggsvszbb_125_mu_ML" : 0
    ,"mlphiggsvstt_125_mu_ML" : 0
    ,"mlphiggsvszz_125_mu_ML" : 0
    ,"mlphiggsvsbkg_125_mu_ML" : 0
    ,"mlphiggsvszbb_125_mu_MM_N" : 0
    ,"mlphiggsvstt_125_mu_MM_N" : 0
    ,"mlphiggsvszz_125_mu_MM_N" : 0
    ,"mlphiggsvsbkg_125_mu_MM_N" : 0
    ,"mlphiggsvsbkg_125_comb_MM_N" : 0
    ,"mlphiggsvszbb_125_comb_MM_N" : 0
    ,"mlphiggsvstt_125_comb_MM_N" : 0
    ,"mlphiggsvszz_125_comb_MM_N" : 0
    }

################
### maximums ###
################
max = {
    "eventSelectionbestzmassMu" :  120 ,  
    "eventSelectionbestzmassEle":  120 ,  
    "eventSelectionbestzptMu"   :  500 ,
    "eventSelectionbestzptEle"  :  500 ,
    "eventSelectiondijetPt"     :  360 ,
    "eventSelectiondrZbj1"      :    5 ,
    "jetmetbjet1pt"             :  265 ,
    "jetmetbjet2pt"             :  265 ,   
    "jetmetbjet1CSVdisc"             :  1 ,
    "jetmetbjet2CSVdisc"             :  1 ,   
    "jetmetbjetMinCSVdisc"             :    1 ,
    "jetmetbjetMaxCSVdisc"             :    1 ,
    "jetmetbjetProdCSVdisc"             :    1 ,
    "jetmetMET"                 :  200 , 
    "eventSelectiondphiZbj1"    :  3.2 ,
    "eventSelectiondphiZbb"     :  3.2 ,
    "eventSelectiondrZbb"       :    5 ,
    "eventSelectionscaldptZbj1" :  250 ,
    "eventSelectiondijetM"      :  240 ,
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
    ,"jetmetnj":8
    ,"Wgg"      :    24 
    ,"Wqq"      :    24 
    ,"Wtt"      :    30 
#    ,"Wtwb"      :    24 
    ,"Wzz3"      :    16 
    ,"Wzz0"      :   28
    ,"Whi3_125"      :    21
    ,"Whi0_125"      :    31
    ,"jetmetMETsignificance" : 80
    ,"jetmetMET" : 100

    ,"mlpZbbvsTT_MM" : 1
    ,"mlpZbbvsTT_MM_N" : 1
    ,"mlpZbbvsTT_ML" : 1
    ,"mlpZbbvsTT_mu_MM" : 1
    ,"mlpZbbvsTT_mu_MM_N" : 1
    ,"mlpZbbvsTT_mu_ML" : 1
    ,"mlphiggsvszbb_125_MM" : 1
    ,"mlphiggsvstt_125_MM" : 1
    ,"mlphiggsvszz_125_MM" : 1
    ,"mlphiggsvsbkg_125_MM" : 1
    ,"mlphiggsvszbb_125_ML" : 1
    ,"mlphiggsvstt_125_ML" : 1
    ,"mlphiggsvszz_125_ML" : 1
    ,"mlphiggsvsbkg_125_ML" : 1
    ,"mlphiggsvszbb_125_MM_N" : 1
    ,"mlphiggsvstt_125_MM_N" : 1
    ,"mlphiggsvszz_125_MM_N" : 1
    ,"mlphiggsvsbkg_125_MM_N" : 1
    ,"mlphiggsvszbb_125_mu_MM" : 1
    ,"mlphiggsvstt_125_mu_MM" : 1
    ,"mlphiggsvszz_125_mu_MM" : 1
    ,"mlphiggsvsbkg_125_mu_MM" : 1
    ,"mlphiggsvszbb_125_mu_ML" : 1
    ,"mlphiggsvstt_125_mu_ML" : 1
    ,"mlphiggsvszz_125_mu_ML" : 1
    ,"mlphiggsvsbkg_125_mu_ML" : 1
    ,"mlphiggsvszbb_125_mu_MM_N" : 1
    ,"mlphiggsvstt_125_mu_MM_N" : 1
    ,"mlphiggsvszz_125_mu_MM_N" : 1
    ,"mlphiggsvsbkg_125_mu_MM_N" : 1
    ,"mlphiggsvsbkg_125_comb_MM_N" : 1
    ,"mlphiggsvszbb_125_comb_MM_N" : 1
    ,"mlphiggsvstt_125_comb_MM_N" : 1
    ,"mlphiggsvszz_125_comb_MM_N" : 1
    }

################
### binning  ###
################
binning = {
    "eventSelectionbestzmassMu" :   24 , #2GeV 
    "eventSelectionbestzmassEle":   24 ,  
    "eventSelectionbestzptMu"   :   25 , #20GeV
    "eventSelectionbestzptEle"  :   25 ,
    "eventSelectiondijetPt"     :   18 ,
    "eventSelectiondrZbj1"      :   10 , #0.5
    "jetmetbjet1pt"             :   26 , #10GeV
    "jetmetbjet2pt"             :   26 ,   
    "jetmetbjet1CSVdisc"             :  50  ,
    "jetmetbjet2CSVdisc"             :  50  ,
    "jetmetbjetMinCSVdisc"             : 50 ,
    "jetmetbjetMaxCSVdisc"             :   50 ,
    "jetmetbjetProdCSVdisc"             :  50 ,   
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
    ,"Wgg"      :    20 
    ,"Wqq"      :    20 
    ,"Wtt"      :    25 
 #   ,"Wtwb"      :    24 
    ,"Wzz3"      :    16 
    ,"Wzz0"      :    20 
    ,"Whi3_125"      :    20 
    ,"Whi0_125"      :    20
    ,"jetmetMETsignificance" : 80
    ,"jetmetMET" : 20

    ,"mlpZbbvsTT_MM" : 20
    ,"mlpZbbvsTT_MM_N" : 10
    ,"mlpZbbvsTT_ML" : 20
    ,"mlpZbbvsTT_mu_MM" : 20
    ,"mlpZbbvsTT_mu_MM_N" : 20
    ,"mlpZbbvsTT_mu_ML" : 20
    ,"mlphiggsvszbb_125_MM" : 20
    ,"mlphiggsvstt_125_MM" : 20
    ,"mlphiggsvszz_125_MM" : 20
    ,"mlphiggsvsbkg_125_MM" : 20
    ,"mlphiggsvszbb_125_ML" : 20
    ,"mlphiggsvstt_125_ML" : 20
    ,"mlphiggsvszz_125_ML" : 20
    ,"mlphiggsvsbkg_125_ML" : 20
    ,"mlphiggsvszbb_125_MM_N" : 20
    ,"mlphiggsvstt_125_MM_N" : 20
    ,"mlphiggsvszz_125_MM_N" : 20
    ,"mlphiggsvsbkg_125_MM_N" : 20
    ,"mlphiggsvszbb_125_mu_MM" : 20
    ,"mlphiggsvstt_125_mu_MM" : 20
    ,"mlphiggsvszz_125_mu_MM" : 20
    ,"mlphiggsvsbkg_125_mu_MM" : 20
    ,"mlphiggsvszbb_125_mu_ML" : 20
    ,"mlphiggsvstt_125_mu_ML" : 20
    ,"mlphiggsvszz_125_mu_ML" : 20
    ,"mlphiggsvsbkg_125_mu_ML" : 20
    ,"mlphiggsvszbb_125_mu_MM_N" : 20
    ,"mlphiggsvstt_125_mu_MM_N" : 20
    ,"mlphiggsvszz_125_mu_MM_N" : 20
    ,"mlphiggsvsbkg_125_mu_MM_N" : 20
    ,"mlphiggsvsbkg_125_comb_MM_N" : 20
    ,"mlphiggsvszbb_125_comb_MM_N" : 20
    ,"mlphiggsvstt_125_comb_MM_N" : 20
    ,"mlphiggsvszz_125_comb_MM_N" : 20
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
                                myRDS_red_w[sample].sumEntries()*(lumi["DATA"]*Extra_norm[sample]/lumi[sample]))
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
    lumiratio[sample]=lumi["DATA"]*Extra_norm[sample]/lumi[sample]
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

## TH2 Plot
#for sample in totsampleList:
#    for name in namePlotList:
#        th2[sample+"whi3_125"+name] = TH2D("whi3_125"+name+"_"+sample,"whi3_125"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["Whi3_125"].getBins(),var["Whi3_125"].getMin(),var["Whi3_125"].getMax())
#        myRDS_red_w[sample].fillHistogram(th2[sample+"whi3_125"+name], RooArgList(var[name],var["Whi3_125"]))
#        CANVAS[sample+"whi3_125"+name] = TCanvas("CANVAS_whi3_125"+name,"CANVASwhi3_125"+name,1200,600)
#        th2[sample+"whi3_125"+name].Draw()

#        th2[sample+"whi0_125"+name] = TH2D(#"whi0_125"+name+"_"+sample,"whi0_125"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["Whi0_125"].getBins(),var["Whi0_125"].getMin(),var["Whi0_125"].getMax())
#        myRDS_red_w[sample].fillHistogram(th2[sample+"whi0_125"+name], RooArgList(var[name],var["Whi0_125"]))
#        CANVAS[sample+"whi0_125"+name] = TCanvas("CANVAS_whi0_125"+name,"CANVASwhi0_125"+name,1200,600)
#        th2[sample+"whi0_125"+name].Draw()

#        th2[sample+"wgg"+name] = TH2D("wgg"+name+"_"+sample,"wgg"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["Wgg"].getBins(),var["Wgg"].getMin(),var["Wgg"].getMax())
#        myRDS_red_w[sample].fillHistogram(th2[sample+"wgg"+name], RooArgList(var[name],var["Wgg"]))
#        CANVAS[sample+"wgg"+name] = TCanvas("CANVAS_wgg"+name,"CANVASwgg"+name,1200,600)
#        th2[sample+"wgg"+name].Draw()


#        th2[sample+"wqq"+name] = TH2D("wqq"+name+"_"+sample,"wqq"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["Wqq"].getBins(),var["Wqq"].getMin(),var["Wqq"].getMax())
#        myRDS_red_w[sample].fillHistogram(th2[sample+"wqq"+name], RooArgList(var[name],var["Wqq"]))
#        CANVAS[sample+"wqq"+name] = TCanvas("CANVAS_wqq"+name,"CANVASwqq"+name,1200,600)
#        th2[sample+"wqq"+name].Draw()

 #       th2[sample+"wtt"+name] = TH2D("wtt"+name+"_"+sample,"wtt"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["Wtt"].getBins(),var["Wtt"].getMin(),var["Wtt"].getMax())
#        myRDS_red_w[sample].fillHistogram(th2[sample+"wtt"+name], RooArgList(var[name],var["Wtt"]))
#        CANVAS[sample+"wtt"+name] = TCanvas("CANVAS_wtt"+name,"CANVASwtt"+name,1200,600)
#        th2[sample+"wtt"+name].Draw()

#        th2[sample+"mlphiggsvsbkg_125_comb_MM_N"+name] = TH2D("mlphiggsvsbkg_125_comb_MM_N"+name+"_"+sample,"mlphiggsvsbkg_125_comb_MM_N"+name+"_"+sample,var[name].getBins(),var[name].getMin(),var[name].getMax(),var["mlphiggsvsbkg_125_comb_MM_N"].getBins(),var["mlphiggsvsbkg_125_comb_MM_N"].getMin(),var["mlphiggsvsbkg_125_comb_MM_N"].getMax())
#        myRDS_red_w[sample].fillHistogram(th2[sample+"mlphiggsvsbkg_125_comb_MM_N"+name], RooArgList(var[name],var["mlphiggsvsbkg_125_comb_MM_N"]))
#        CANVAS[sample+"mlphiggsvsbkg_125_comb_MM_N"+name] = TCanvas("CANVAS_mlphiggsvsbkg_125"+name,"CANVASmlphiggsvsbkg_125_comb_MM_N"+name,1200,600)
#        th2[sample+"mlphiggsvsbkg_125_comb_MM_N"+name].Draw()
#    
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

plot = TFile("Plot_ee_100H125_MM_allR.root","RECREATE")
for name in namePlotList:
    CANVAS[name].Write()
    #for sample in totsampleList:
    #    th2[sample+"wtt"+name].Write()
    #    th2[sample+"wqq"+name].Write()
    #    th2[sample+"wgg"+name].Write()
    #    th2[sample+"whi0_125"+name].Write()
    #    th2[sample+"whi3_125"+name].Write()
    #    th2[sample+"mlphiggsvsbkg_125_comb_MM_N"+name].Write()

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
