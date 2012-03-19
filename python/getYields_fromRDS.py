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

WP       = "11"    #"HP","HPMET","HP_excl","HE","HEmet","He_excl"
channel  = "El"    #"El","Mu"
extraCut = "jetmetbjet1pt>25.&jetmetbjet2pt>25."

kutString = ""+extraCut

#####################################################
### settings (this should move somewhere central) ### 
#####################################################

MCsampleList  = ["TT","DY","ZZ","ZHbb"]
totsampleList = ["DATA","TT","DY","ZZ","ZHbb"]

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
    myRDS_red[sample] = myRDS_el[sample].reduce("rc_eventSelection_"+WP+"==1")

    if extraCut : myRDS_red[sample] = myRDS_red[sample].reduce(extraCut)

    if channel =="Mu" :
        myRDS_red[sample]=myRDS_red[sample].reduce(muMassCut)
        kutString=kutString+"&"+muMassCut
    if channel =="El" :
        myRDS_red[sample]=myRDS_red[sample].reduce(elMassCut)
        kutString=kutString+"&"+muMassCut

    myRDS_red[sample].addColumn(w)

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
print "===> the pure # of ", sample, " MC    ............... ", str(sum_MC)[:4]
print "===> the pure # of ", sample, " DATA  ............... ", myRDS_red_w["DATA"].numEntries()

print "***"
sum_MC=0
for sample in MCsampleList:
    print "the effective # of ", sample, " MC for this lumi ... ", str(myRDS_red_w[sample].numEntries()*(lumi["DATA"]/lumi[sample]))[:4]
    sum_MC+=myRDS_red_w[sample].numEntries()*(lumi["DATA"]/lumi[sample])
print "===> the pure # of ", sample, " MC    ............... ", str(sum_MC)[:4]
print "===> the pure # of ", sample, " DATA  ............... ", myRDS_red_w["DATA"].numEntries()

print "***"

sum_MC=0
for sample in MCsampleList:
    print "the weighted effective # of ", sample, " MC for this data lumi = ", str(myRDS_red_w[sample].sumEntries()*(lumi["DATA"]/lumi[sample]))[:4]
    sum_MC+=myRDS_red_w[sample].sumEntries()*(lumi["DATA"]/lumi[sample])
print "===> the pure # of ", sample, " MC    ............... ", str(sum_MC)[:4]
print "===> the pure # of ", sample, " DATA  ............... ", myRDS_red_w["DATA"].numEntries()



#num_TT_MC = RooRealVar("num_TT_MC","num_TT_MC",
#                       RDS_TT_red_w.sumEntries()*(lumi_of_DATA/lumi_of_TT))
#num_DY_MC = RooRealVar("num_DY_MC","num_DY_MC",
#                        RDS_DY_red_w.sumEntries()*(lumi_of_DATA/lumi_of_DY))
#total_MC = num_TT_MC.getVal()+num_DY_MC.getVal()
#
#print "the total (DY+TT) MC events = " , total_MC
#print "the lumi of DATA = 2.1 fb-1???"  , lumi_of_DATA
#print "the number of entries of DATA = ", DATA_red.numEntries()#
#
#norm = total_MC/DATA_red.numEntries()



    
