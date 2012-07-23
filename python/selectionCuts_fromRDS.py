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
from zbbCommons import zbbnorm

#####################################################
### sample/wp/selection of interest
#####################################################

WP       = "17"  
channels  = [
    "EEChannel",
    "MuMuChannel",
    ]

#choose you set of cuts
extraCuts = [
    "eventSelectiondijetdR>0",#no effect
    "((eventSelectionbestzmassEle>80.45&eventSelectionbestzmassEle<101.55)||(eventSelectionbestzmassMu>80.45&eventSelectionbestzmassMu<101.55))",
    #"(eventSelectionbestzptEle>20.||eventSelectionbestzptMu>20.)",
    "eventSelectiondphidijetMET<1.",
    "eventSelectiondphiZbb>2.25",
    "eventSelectiondijetM>95&eventSelectiondijetM<155",
    #"eventSelectionZbbM>176&eventSelectionZbbM<256",
    #"eventSelectiondphidijetMET<1.&eventSelectiondphiZbb>2.25",
    #"eventSelectiondphidijetMET<1.&eventSelectiondphiZbb>2.25&eventSelectiondijetM>95&eventSelectiondijetM<155",
    #"eventSelectiondphiZbb>2.25&eventSelectiondijetM>95&eventSelectiondijetM<155",
    #"(eventSelectionbestzptEle>20.||eventSelectionbestzptMu>20.)&eventSelectiondphidijetMET<1.",
    #"(eventSelectionbestzptEle>20.||eventSelectionbestzptMu>20.)&eventSelectiondphiZbb>2.5",
    #"eventSelectiondphidijetMET<1.&eventSelectiondphiZbb>2.5",
    #"(eventSelectionbestzptEle>20.||eventSelectionbestzptMu>20.)&eventSelectiondphidijetMET<1.&eventSelectiondphiZbb>2.5",
    #"(eventSelectionbestzptEle>20.||eventSelectionbestzptMu>20.)&eventSelectiondphidijetMET<1.&eventSelectiondphiZbb>2.5&eventSelectiondijetdR>1.5&eventSelectiondijetdR<3.",
    #"(eventSelectionbestzptEle>20.||eventSelectionbestzptMu>20.)&eventSelectiondphidijetMET<1.&eventSelectiondphiZbb>2.5&eventSelectionZbPt<150",
    ]

titleCuts = [
    "stage_"+WP,
    "mass Z",
    "dPhi(bb,MET)",
    "dPhi(Z,bb)",
    "bb mass",
    #"zbb mass",
    #"dPhi(bb,MET)+dPhi(Z,bb)",
    #"dPhi(bb,MET)+dPhi(Z,bb)+bb mass",
    #"dPhi(Z,bb)+bb mass",
    ]

extraCutsLep = {
    "EEChannel"     : "(eventSelectionbestzmassEle>76.&eventSelectionbestzmassEle<106.)",
    "MuMuChannel"   : "(eventSelectionbestzmassMu>76.&eventSelectionbestzmassMu<106.)"
    }

stringCut = {}
titleCut = {}

for i in range(0,len(extraCuts)) :
    stringCut[extraCuts[i]]="Cut"+str(i+1)
    if titleCuts[i] : titleCut[extraCuts[i]]=titleCuts[i]
    titleCut[extraCuts[i]]=""

#####################################################
### settings (this should move somewhere central) ### 
#####################################################

MCsampleList   = ["Zb","Zc","Zl","TT","ZZ","ZH115","ZH120","ZH125","ZH130","ZH135"]#,"ZA"]
SMMCsampleList = ["Zb","Zc","Zl","TT","ZZ"]
NSMMCsampleList= ["ZH115","ZH120","ZH125","ZH130","ZH135"]#,"ZA"]
totsampleList  = ["DATA","Zb","Zc","Zl","TT","ZZ","ZH115","ZH120","ZH125","ZH130","ZH135"]#,"ZA"]
sampleList     = ["DATA","DY","TT","ZZ","ZH115","ZH120","ZH125","ZH130","ZH135"]

lumi = { "DATA"   : zbbnorm.lumi_tot2011,
         "TT"     : zbbnorm.nev_TTjets_fall11/zbbnorm.xsec_TTjets_7TeV/1000.,
         "Zb"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "Zc"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "Zl"     : zbbnorm.nev_DYjets_fall11/zbbnorm.xsec_DYjets_7TeV/1000.,
         "ZZ"     : zbbnorm.nev_ZZ_fall11/zbbnorm.xsec_ZZ_7TeV/1000.,
         "ZH115"  : zbbnorm.nev_ZH115_fall11/zbbnorm.xsec_ZH115_7TeV/1000.,
         "ZH120"  : zbbnorm.nev_ZH120_fall11/zbbnorm.xsec_ZH120_7TeV/1000.,
         "ZH125"  : zbbnorm.nev_ZH125_fall11/zbbnorm.xsec_ZH125_7TeV/1000.,
         "ZH130"  : zbbnorm.nev_ZH130_fall11/zbbnorm.xsec_ZH130_7TeV/1000.,
         "ZH135"  : zbbnorm.nev_ZH135_fall11/zbbnorm.xsec_ZH135_7TeV/1000.
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

filename_el = {"DATA_A" : "condorRDSmakerNoWS/outputs/File_rds_zbb_ElA_DATA.root",
               "DATA_B" : "condorRDSmakerNoWS/outputs/File_rds_zbb_ElB_DATA.root",
               "TT"     : "condorRDSmakerNoWS/outputs/File_rds_zbb_TT_El_MC.root",
               "DY"     : "condorRDSmakerNoWS/outputs/File_rds_zbb_El_MC.root",
               "ZZ"     : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZZ_El_MC.root",
               "ZH115"  : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZH115_El_MC.root",
               "ZH120"  : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZH120_El_MC.root",
               "ZH125"  : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZH125_El_MC.root",
               "ZH130"  : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZH130_El_MC.root",
               "ZH135"  : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZH135_El_MC.root"
               }

filename_mu = {"DATA_A" : "condorRDSmakerNoWS/outputs/File_rds_zbb_MuA_DATA.root",
               "DATA_B" : "condorRDSmakerNoWS/outputs/File_rds_zbb_MuB_DATA.root",
               "TT"     : "condorRDSmakerNoWS/outputs/File_rds_zbb_TT_Mu_MC.root",
               "DY"     : "condorRDSmakerNoWS/outputs/File_rds_zbb_Mu_MC.root",
               "ZZ"     : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZZ_Mu_MC.root",
               "ZH115"  : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZH115_Mu_MC.root",
               "ZH120"  : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZH120_Mu_MC.root",
               "ZH125"  : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZH125_Mu_MC.root",
               "ZH130"  : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZH130_Mu_MC.root",
               "ZH135"  : "condorRDSmakerNoWS/outputs/File_rds_zbb_ZH135_Mu_MC.root"
               }


for sample in sampleList :

    redStage = "rc_eventSelection_"+WP+"==1"
    for channel in channels:
        print "Channel : ", channel
        if sample != "DATA":
            
            if channel=="EEChannel" : file_mc  = TFile(filename_el[sample])
            else : file_mc  = TFile(filename_mu[sample])
            
            nEntries = file_mc.Get("rds_zbb").numEntries()
        
            if sample == "DY" :
                myRDS[channel+"Zb"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==3")
                myRDS[channel+"Zc"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==2")
                myRDS[channel+"Zl"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==1")
                print "myRDS.numEntries() for ", "Zb" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zb"].numEntries()
                print "myRDS.numEntries() for ", "Zc" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zc"].numEntries()
                print "myRDS.numEntries() for ", "Zl" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zl"].numEntries()
            else :
                myRDS[channel+sample] = file_mc.Get("rds_zbb").reduce(redStage)
                print "myRDS.numEntries() for ", sample , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+sample].numEntries()
        
            file_mc.Close()

        else :
            if channel=="EEChannel": 
                file_A  = TFile(filename_el["DATA_A"])
                file_B  = TFile(filename_el["DATA_B"])
            else:
                file_A  = TFile(filename_mu["DATA_A"])
                file_B  = TFile(filename_mu["DATA_B"])
            
            nEntries = file_A.Get("rds_zbb").numEntries()+file_B.Get("rds_zbb").numEntries()
            
            myRDS[channel+sample] = file_A.Get("rds_zbb").reduce(redStage)
            tmp = file_B.Get("rds_zbb").reduce(redStage)
            myRDS[channel+sample].append(tmp)
            
            print "myRDS.numEntries() for ", sample , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+sample].numEntries()
            
            file_A.Close()
            file_B.Close()

###############
### weights ###
###############
tmp=myRDS["EEChannelZc"].reduce("mcSelectioneventType==1")
ras_zbb = tmp.get()
tmp=0

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
    "eventSelectiondphidijetMET" ,
    "eventSelectiondphiZbb"      ,
    "eventSelectiondphiZbj1"     ,
    "eventSelectiondrZbb"        ,
    "eventSelectiondrZbj1"       ,
    "eventSelectiondijetPt"      ,
    "eventSelectiondijetM"       ,
    "eventSelectiondijetdR"      ,
    "eventSelectiondijetSVdR"    ,
    "jetmetjet1SVmass"           ,
    "eventSelectionZbbM"         ,
    "eventSelectionZbbPt"        ,
    "eventSelectionZbM"          ,
    "eventSelectiondrMuMu"       , 
    "eventSelectiondrEleEle"     
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
    "jetmetbjet1pt"             :    5 ,
    "jetmetbjet2pt"             :    5 ,   
    "jetmetMET"                 :    0 ,
    "jetmetMETsignificance"     :    0 ,
    "eventSelectiondphidijetMET":    0 ,
    "eventSelectiondphiZbj1"    :    0 ,
    "eventSelectiondphiZbb"     :    0 ,
    "eventSelectiondrZbj1"      :    0 ,
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
    "eventSelectiondrMuMu"      :    0 ,
    "eventSelectiondrEleEle"    :    0 
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
    "jetmetbjet1pt"             :  265 ,
    "jetmetbjet2pt"             :  265 ,   
    "jetmetMET"                 :  200 ,
    "jetmetMETsignificance"     :   20 ,
    "eventSelectiondphidijetMET":  3.2 ,
    "eventSelectiondphiZbj1"    :  3.2 ,
    "eventSelectiondphiZbb"     :  3.2 ,
    "eventSelectiondrZbj1"      :    5 ,
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
    "eventSelectiondrMuMu"      :    5 ,
    "eventSelectiondrEleEle"    :    5 
    }

################
### binning  ###
################

binning = {
    "eventSelectionbestzmassMu" :   30  , #2GeV 
    "eventSelectionbestzmassEle":   30  ,  
    "eventSelectionbestzptMu"   :   18  , #20GeV
    "eventSelectionbestzptEle"  :   18 ,
    "eventSelectiondijetPt"     :   18 ,
    "jetmetbjet1pt"             :   26 , #10GeV
    "jetmetbjet2pt"             :   26 ,   
    "jetmetMET"                 :   20 , #10GeV
    "jetmetMETsignificance"     :   40 , #0.5
    "eventSelectiondphidijetMET":   16 , #0.2
    "eventSelectiondphiZbj1"    :   16 , 
    "eventSelectiondphiZbb"     :   16 ,
    "eventSelectiondrZbj1"      :   10 , #0.5
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
    "eventSelectiondrMuMu"      :   10 , #0.5
    "eventSelectiondrEleEle"    :   10 
    }

var = {}
for name in namePlotList:
    print "name = ", name
    var[name] = ras_zbb[name]
    var[name].setMin(min[name])
    var[name].setMax(max[name])
    var[name].setBins(5*binning[name])

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
            
            myRDS_red = myRDS[channel+sample]

            if iCut : myRDS_red = myRDS_red.reduce(iCut)
            
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
    file[sample]=TFile("Higgs1bin/histoStage"+WP+"extraCuts"+sample+".root","RECREATE")
    for channel in channels:
        if channel=="Combined" : continue
        chDir=file[sample].mkdir(channel,channel)
        for cut in extraCuts:
            chDir.mkdir(stringCut[cut],titleCut[cut])
            chDir.cd(stringCut[cut])
            for name in namePlotList:
                if channel=="EEChannel" and (name.find("Mu")>-1 or name.find("mumu")>-1) : continue
                if channel=="MuMuChannel" and (name.find("Ele")>-1 or name.find("elel")>-1) : continue
                th1[channel+sample+name+cut].Write()
    file[sample].Close()

