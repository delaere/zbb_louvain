#######################################################################################
###                                                                                 ###
### selectionCuts_fromRDS.py                                                        ###
###                                                                                 ###
### Small script to estimate the number of events                                   ###
### for different data and MC samples                                               ###
### for a certain working point and selection                                       ###
### inspired by getYileds_fromRDS.py                                                ###
### to be used doing :                                                              ###
### python selectionCuts_fromRDS.py >> yields.txt                                   ###
### you will find the yields table at the end of yields.txt                         ###
### Also histograms are produced and store in root files                            ###
### One root files is created by sample                                             ###
### The variables listed below are ploted for each channel and for each set of cuts ### 
### To combine them, use : combinePlots_forRDSanalyser.py (after sumChannels.C)     ###
#######################################################################################

from ROOT import *
#from zbbCommons import zbbnorm

#####################################################
### sample/wp/selection of interest
#####################################################

WP       = "9"  
channels  = [
    "EEChannel",
    "MuMuChannel",
    ]

#choose you set of cuts
extraCuts = [
    "jetmetMET<50.",
    "jetmetMET>50.",
    "jetmetMETsignificance<5.",
    "jetmetMETsignificance<7.5",
    "jetmetMETsignificance<10.",
    "jetmetMETsignificance>10."    
    ]

extraCutsLep = {
    "EEChannel"     : "(eventSelectionbestzmassEle>76.&eventSelectionbestzmassEle<106.)",
    "MuMuChannel"   : "(eventSelectionbestzmassMu>76.&eventSelectionbestzmassMu<106.)"
    }

stringCut = {}

for i in range(0,len(extraCuts)) :
    stringCut[extraCuts[i]]="Cut"+str(i+1)


#####################################################
### settings (this should move somewhere central) ### 
#####################################################

MCsampleList   = ["TT","Zb","Zc","Zl","ZZ","ZH"]#,"ZA"]
SMMCsampleList = ["TT","Zb","Zc","Zl","ZZ"]
NSMMCsampleList= ["ZH"]#,"ZA"]
totsampleList  = ["DATA","TT","Zb","Zc","Zl","ZZ","ZH"]#,"ZA"]

lumi = { "DATA" : 5.051                   ,
         "TT"   : (3701947./157.5)/1000.  ,
         "Zb"   : (35907791./3048.)/1000. ,
         "Zc"   : (35907791./3048.)/1000. ,
         "Zl"   : (35907791./3048.)/1000. ,
         "ZZ"   :  4191045./6206.         ,
         "ZH"   : (1000000./18.)*(50000./304791.),
         #"ZA"   : 70000./2.3
         }

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

filename_el = {"DATA": "File_rds_zbb_El_DATA.root",
               "TT"  : "File_rds_zbb_Ttbar_El_MC.root",
               "Zb"  : "File_rds_zbb_El_MC.root",
               "Zc"  : "File_rds_zbb_El_MC.root",
               "Zl"  : "File_rds_zbb_El_MC.root",  
               "ZZ"  : "File_rds_zbb_ZZ_El_MC.root",
               "ZH"  : "File_rds_zbb_ZHbb_El_MC.root",
               #"ZA"  : "File_rds_zbb_ZAbb_El_MC.root",
               }

filename_mu = {"DATA": "File_rds_zbb_Mu_DATA.root",
               "TT"  : "File_rds_zbb_Ttbar_Mu_MC.root",
               "Zb"  : "File_rds_zbb_Mu_MC.root",
               "Zc"  : "File_rds_zbb_Mu_MC.root",
               "Zl"  : "File_rds_zbb_Mu_MC.root",
               "ZZ"  : "File_rds_zbb_ZZ_Mu_MC.root",
               "ZH"  : "File_rds_zbb_ZHbb_Mu_MC.root",
               #"ZA"  : "File_rds_zbb_ZAbb_Mu_MC.root"
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
           "6"  : ws.var("BtaggingReweightingHP")  ,
           "7"  : ws.var("BtaggingReweightingHE")  ,
           "8"  : ws.var("BtaggingReweightingHP")  ,
           "9"  : ws.var("BtaggingReweightingHEHE"),
           "10" : ws.var("BtaggingReweightingHEHP"),
           "11" : ws.var("BtaggingReweightingHPHP"),
           "12" : ws.var("BtaggingReweightingHEHE"), 
           "13" : ws.var("BtaggingReweightingHEHP"),
           "14" : ws.var("BtaggingReweightingHPHP"),
           }

rrv_w_lep  = ws.var("LeptonsReweightingweight")
rrv_w_lumi = ws.var("lumiReweightingLumiWeight")

w = RooFormulaVar("w","w", "@0*@1*@2", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))

#############
### PLOTS ###
#############

#################
### variables ###
#################
#here put all variables you want to plot and don't forget the binning

namePlotList = [
    "eventSelectionbestzmassMu"  ,  
    "eventSelectionbestzmassEle" ,
    "eventSelectionbestzptMu"    ,
    "eventSelectionbestzptEle"   ,
    "jetmetbjet1pt"              ,
    "jetmetbjet2pt"              ,
    "jetmetMET"                  ,
    "jetmetMETsignificance"      ,
    "eventSelectiondphiZbb"      ,
    "eventSelectiondphiZbj1"     ,
    "eventSelectiondijetPt"      ,
    "eventSelectiondijetM"       ,
    "eventSelectiondijetdR"      ,
    "eventSelectiondijetSVdR"    ,
    "jetmetjet1SVmass"           ,
    "eventSelectionZbbM"         ,
    "eventSelectionZbbPt"        ,
    "eventSelectionZbM"          ,
    "eventSelectiondrmumu"       , #to be changed in drMuMu
    "eventSelectiondrelel"         #to be changed in drEleEle
    ]

################
### minimums ###
################
min = {
    "eventSelectionbestzmassMu" :   60 ,  
    "eventSelectionbestzmassEle":   60 ,  
    "eventSelectionbestzptMu"   :    0.0001 , #to remove underflow
    "eventSelectionbestzptEle"  :    0.0001 ,
    "eventSelectiondijetPt"     :    0 ,
    "eventSelectiondrZbj1"      :    0 ,
    "jetmetbjet1pt"             :    5 ,
    "jetmetbjet2pt"             :    5 ,   
    "jetmetMET"                 :    0 ,
    "jetmetMETsignificance"     :    0 ,
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
    "jetmetjet1SVmass"          :    0.0001 ,
    "eventSelectiondrmumu"      :    0.0001 ,
    "eventSelectiondrelel"      :    0.0001 
    }

################
### maximums ###
################

max = {
    "eventSelectionbestzmassMu" :  120 ,  
    "eventSelectionbestzmassEle":  120 ,  
    "eventSelectionbestzptMu"   :  360.0001 ,
    "eventSelectionbestzptEle"  :  360.0001 ,
    "eventSelectiondijetPt"     :  360 ,
    "eventSelectiondrZbj1"      :    5 ,
    "jetmetbjet1pt"             :  265 ,
    "jetmetbjet2pt"             :  265 ,   
    "jetmetMET"                 :  200 ,
    "jetmetMETsignificance"     :   20 ,
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
    "jetmetjet1SVmass"          :    5.0001 ,
    "eventSelectiondrmumu"      :    5.0001 ,
    "eventSelectiondrelel"      :    5.0001 
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
    "jetmetMETsignificance"     :   40 , #0.5
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
    var[name] = ws.var(name)
    var[name].setMin(min[name])
    var[name].setMax(max[name])
    var[name].setBins(binning[name])

th1 = {}

#################################  
### working point & selection ###
#################################

sumSMMC = {}
sumNSMMC = {}
sumDATA = {}
nevts = {}

for channel in channels :
    print "channel ... ", channel
    for sample in totsampleList :
        print "sample ... ", sample
        for cut in extraCuts :
            iCut=cut+"&"+extraCutsLep[channel]
            print "cuts ... ", iCut
            
            if   channel=="EEChannel" : myRDS_red = myRDS_el[sample].reduce("rc_eventSelection_"+WP+"==1")
            elif channel=="MuMuChannel" : myRDS_red = myRDS_mu[sample].reduce("rc_eventSelection_"+WP+"==1")
            else :
                myRDS_red = myRDS_el[sample].reduce("rc_eventSelection_"+WP+"==1")
                myRDS_red.append(myRDS_mu[sample].reduce("rc_eventSelection_"+WP+"==1"))

            if iCut : myRDS_red = myRDS_red.reduce(iCut)

            if   sample == "Zb" : isZbcl = "mcSelectioneventType==3"
            elif sample == "Zc" : isZbcl = "mcSelectioneventType==2"
            elif sample == "Zl" : isZbcl = "mcSelectioneventType==1"
            else                : isZbcl = ""
    
            if isZbcl : myRDS_red = myRDS_red.reduce(isZbcl)
            
            if sample != "DATA": myRDS_red.addColumn(w)
                
            if sample != "DATA": myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w")
            else               : myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get())

            nevts["pure"+sample+channel+cut]     = myRDS_red_w.numEntries()
            if sample in MCsampleList :
                nevts["effective"+sample+channel+cut]= myRDS_red_w.numEntries()*(lumi["DATA"]/lumi[sample])
                nevts["weighted"+sample+channel+cut] = myRDS_red_w.sumEntries()*(lumi["DATA"]/lumi[sample])
            
            if sample in SMMCsampleList :
                if sample==SMMCsampleList[0]:
                    sumSMMC["pure"+channel+cut]     = 0
                    sumSMMC["effective"+channel+cut]= 0
                    sumSMMC["weighted"+channel+cut] = 0
                sumSMMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumSMMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(lumi["DATA"]/lumi[sample])
                sumSMMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(lumi["DATA"]/lumi[sample])
            if sample in NSMMCsampleList :
                if sample==NSMMCsampleList[0]:
                    sumNSMMC["pure"+channel+cut]     = 0
                    sumNSMMC["effective"+channel+cut]= 0
                    sumNSMMC["weighted"+channel+cut] = 0
                sumNSMMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumNSMMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(lumi["DATA"]/lumi[sample])
                sumNSMMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(lumi["DATA"]/lumi[sample])
            if sample=="DATA":
                sumDATA[channel+cut]=myRDS_red_w.numEntries()
            for name in namePlotList:
                if channel=="EEChannel" and (name.find("Mu")>-1 or name.find("mumu")>-1) : continue
                if channel=="MuMuChannel" and (name.find("Ele")>-1 or name.find("elel")>-1) : continue
                th1[channel+sample+name+cut] = TH1D(name,name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                myRDS_red_w.fillHistogram(th1[channel+sample+name+cut], RooArgList(var[name]))
            
#################
### printouts ###
#################
print " "
print " "
print "**************************************************************************************************************************"
print "*** DATA/MC COMPARISONS***************************************************************************************************"
print "**************************************************************************************************************************"
print "working point ... ", WP
print "**************************************************************************************************************************"

for channel in channels:
    print "............................................................................"
    print "Channel ..", channel, "....................................................."
    print " "
    print "pure MC yields  ............................................................"
    print "Cuts".ljust(10),
    for sample in MCsampleList : print sample.ljust(10),
    print "totSMMC".ljust(10), "totNSMMC".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsampleList : print '{0}'.ljust(10).format(nevts["pure"+sample+channel+cut]),
        print '{0}'.ljust(10).format(sumSMMC["pure"+channel+cut]), '{0}'.ljust(10).format(sumNSMMC["pure"+channel+cut])
    print " "
    print "normalized MC yields ......................................................."
    print "Cuts".ljust(10),
    for sample in MCsampleList : print sample.ljust(10),
    print "totSMMC".ljust(10), "totNSMMC".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsampleList : print '{0:.2f}'.format(nevts["effective"+sample+channel+cut]).ljust(10),
        print '{0:.2f}'.format(sumSMMC["effective"+channel+cut]).ljust(10), '{0:.2f}'.format(sumNSMMC["effective"+channel+cut]).ljust(10)
    print " "
    print "weighted and normalized MC yields vs DATA yield ............................"
    print "Cuts".ljust(10),
    for sample in MCsampleList : print sample.ljust(10),
    print "totSMMC".ljust(10), "totNSMMC".ljust(10), "DATA".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsampleList : print '{0:.2f}'.format(nevts["weighted"+sample+channel+cut]).ljust(10),
        print '{0:.2f}'.format(sumSMMC["weighted"+channel+cut]).ljust(10), '{0:.2f}'.format( sumNSMMC["weighted"+channel+cut]).ljust(10), '{0}'.ljust(10).format( nevts["pure"+"DATA"+channel+cut])
    print "............................................................................"
    print "............................................................................"
    print " "
    print " "

print "............................................................................"
print "Channel .. Combined ........................................................"
print " "
print "pure MC yields  ............................................................"
print "Cuts".ljust(10),
for sample in MCsampleList : print sample.ljust(10),
print "totSMMC".ljust(10), "totNSMMC".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsampleList : print '{0}'.ljust(10).format(nevts["pure"+sample+"EEChannel"+cut]+nevts["pure"+sample+"MuMuChannel"+cut]),
    print '{0}'.ljust(10).format(sumSMMC["pure"+"EEChannel"+cut]+sumSMMC["pure"+"MuMuChannel"+cut]), '{0}'.ljust(10).format(sumNSMMC["pure"+"EEChannel"+cut]+sumNSMMC["pure"+"MuMuChannel"+cut])
print " "
print "normalized MC yields ......................................................."
print "Cuts".ljust(10),
for sample in MCsampleList : print sample.ljust(10),
print "totSMMC".ljust(10), "totNSMMC".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsampleList : print '{0:.2f}'.format(nevts["effective"+sample+"EEChannel"+cut]+nevts["effective"+sample+"MuMuChannel"+cut]).ljust(10),
    print '{0:.2f}'.format(sumSMMC["effective"+"EEChannel"+cut]+sumSMMC["effective"+"MuMuChannel"+cut]).ljust(10), '{0:.2f}'.format(sumNSMMC["effective"+"EEChannel"+cut]+sumNSMMC["effective"+"MuMuChannel"+cut]).ljust(10)
print " "
print "weighted and normalized MC yields vs DATA yield ............................"
print "Cuts".ljust(10),
for sample in MCsampleList : print sample.ljust(10),
print "totSMMC".ljust(10), "totNSMMC".ljust(10), "DATA".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsampleList : print '{0:.2f}'.format(nevts["weighted"+sample+"EEChannel"+cut]+nevts["weighted"+sample+"MuMuChannel"+cut]).ljust(10),
    print '{0:.2f}'.format(sumSMMC["weighted"+"EEChannel"+cut]+sumSMMC["weighted"+"MuMuChannel"+cut]).ljust(10), '{0:.2f}'.format(sumNSMMC["weighted"+"EEChannel"+cut]+sumNSMMC["weighted"+"MuMuChannel"+cut]).ljust(10), '{0}'.ljust(10).format(nevts["pure"+"DATA"+"EEChannel"+cut]+nevts["pure"+"DATA"+"MuMuChannel"+cut])
print "............................................................................"
print "............................................................................"
print " "
print " "

#################
###  outputs  ###
#################
   
file={}
#her you could choose the root ouput filenames
for sample in totsampleList:
    file[sample]=TFile("histoStage"+WP+"extraCuts"+sample+".root","RECREATE")
    for channel in channels:
        if channel=="Combined" : continue
        chDir=file[sample].mkdir(channel,channel)
        for cut in extraCuts:
            chDir.mkdir(stringCut[cut],stringCut[cut])
            chDir.cd(stringCut[cut])
            for name in namePlotList:
                if channel=="EEChannel" and (name.find("Mu")>-1 or name.find("mumu")>-1) : continue
                if channel=="MuMuChannel" and (name.find("Ele")>-1 or name.find("elel")>-1) : continue
                th1[channel+sample+name+cut].Write()
    file[sample].Close()

