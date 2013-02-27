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
from eventSelection import categoryNames
from listForRDS import sampleList, totsampleList, sigMCsampleList, MCsampleList, bkgMCsampleList, lumi, dataPeriods, Extra_norm, namePlotList, min, max, binning
from globalLists import pathMergedRDS, pathRDS
import os

#####################################################
### sample/wp/selection of interest
#####################################################

runOnMergedRDS = True

btagWP = "HPHP" #choose between HE, HP, HEHE, HEHP, HPHP
llMassWP = "" #"" or "wide"
metWP = "MET" #"MET" or "", MET means met significance

wp = 0
for cat in categoryNames:
    if cat.find(btagWP)>-1:
        if (llMassWP=="" and cat.find("wide")==-1) or (llMassWP=="wide" and cat.find(btagWP)>-1):
            if (metWP=="" and cat.find("MET")==-1)  or (metWP=="MET" and cat.find("significance")>-1):
                break
    wp+=1

WP=str(wp)

channels  = [
    "EEChannel",
    "MuMuChannel",
    ]

#choose you set of cuts
extraCuts = [
    "",
    ## "eventSelectiondijetdR<1.",
##     "eventSelectiondijetdR<0.75",
##     "((eventSelectiondrllMu<1.&&eventSelectiondrllMu>0.)||(eventSelectiondrllEle<1.&&eventSelectiondrllEle>0.))",
##     "eventSelectiondijetPt>50",
##     "eventSelectiondijetPt>100",
##     "eventSelectiondijetPt>150",
##     "(eventSelectionbestzptEle>50||eventSelectionbestzptMu>50)",
##     "(eventSelectionbestzptEle>100||eventSelectionbestzptMu>100)",
##     "(eventSelectionbestzptEle>150||eventSelectionbestzptMu>150)",
##     "(eventSelectionbestzptEle>225||eventSelectionbestzptMu>225)",

    ]

extraCutsLep = {
    "EEChannel"     : "(eventSelectionbestzmassEle>76.&eventSelectionbestzmassEle<106.)",
    "MuMuChannel"   : "(eventSelectionbestzmassMu>76.&eventSelectionbestzmassMu<106.)"
    }

stringCut = {}
#titleCut = {}

for i in range(0,len(extraCuts)) :
    stringCut[extraCuts[i]]="Cut"+str(i+1)
    #if titleCuts[i] : titleCut[extraCuts[i]]=titleCuts[i]
    #titleCut[extraCuts[i]]=""

#####################################################
### settings (this should move somewhere central) ### 
#####################################################

MCweight = {}

for sample in MCsampleList:
    for channel in channels :
        print "the lumi of ", sample, " = ", lumi[sample]
        MCweight[channel+sample] = lumi["DATA"]/lumi[sample]/Extra_norm[channel+sample]
        print "the weight of ", channel+sample," = ", MCweight[channel+sample]

#############
### files ###
#############

myRDS_el    = {}
myRDS_mu    = {}
myRDS       = {}
myRDS_red   = {} 
myRDS_red_w = {}

path = pathMergedRDS
if not runOnMergedRDS : path = pathRDS

for sample in sampleList :
    if sample=="DATA" : continue
    redStage = "rc_eventSelection_"+WP+"==1"
    for channel in channels:
        print "Channel : ", channel
        if channel=="EEChannel" : file_mc  = TFile(path[sample+"_El_MC"])
        else : file_mc  = TFile(path[sample+"_Mu_MC"])
        
        tree_zbb = file_mc.Get("rds_zbb")
        ws_zbb = file_mc.Get("ws_ras")
        ras_zbb = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())
        rds_zbb = RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)
        
        nEntries = rds_zbb.numEntries()
        if sample == "DY" :
                myRDS[channel+"Zb"] = rds_zbb.reduce(redStage + "&mcSelectioneventType==3")
                myRDS[channel+"Zc"] = rds_zbb.reduce(redStage + "&mcSelectioneventType==2")
                myRDS[channel+"Zl"] = rds_zbb.reduce(redStage + "&mcSelectioneventType==1")
                print "myRDS.numEntries() for ", "Zb" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zb"].numEntries()
                print "myRDS.numEntries() for ", "Zc" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zc"].numEntries()
                print "myRDS.numEntries() for ", "Zl" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zl"].numEntries()
        else :
            myRDS[channel+sample] = rds_zbb.reduce(redStage)
            print "myRDS.numEntries() for ", sample , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+sample].numEntries()
            
        file_mc.Close()

for channel in channels:
    print "Channel : ", channel
    file={}
    for period in dataPeriods :
        if channel=="EEChannel": 
            file[period]  = TFile(path["DoubleEle_Data"+period])
        else:
            file[period]  = TFile(path["DoubleMu_Data"+period])
        
    tree_zbb = file["A"].Get("rds_zbb")
    ws_zbb = file["A"].Get("ws_ras")
    ras_zbb = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())
    rds_zbb = RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)

    for period in dataPeriods :
        if period=="A" : continue
        tree_zbb = file[period].Get("rds_zbb")
        ws_zbb = file[period].Get("ws_ras")
        ras_zbb = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())
        tmp = RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)
        rds_zbb.append(tmp)
    
    nEntries = rds_zbb.numEntries()
    
    myRDS[channel+"DATA"] = rds_zbb.reduce(redStage)
    
    print "myRDS.numEntries() for ", sample , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+sample].numEntries()

    for period in dataPeriods : file[period].Close()
    
###############
### weights ###
###############
tmp=myRDS["EEChannelTT"].reduce("mcSelectioneventType==1")
ras_zbb = tmp.get()
tmp=0

btagRew = [
    "BtaggingReweightingHE"  ,
    "BtaggingReweightingHP"  ,
    "BtaggingReweightingHEHE",
    "BtaggingReweightingHEHP",
    "BtaggingReweightingHPHP",
    ]

for b in btagRew:
    if b.find(btagWP)>-1 : 
        rrv_w_b=ras_zbb[b]
        break
rrv_w_lep  = ras_zbb["LeptonsReweightingweight"]
rrv_w_lumi = ras_zbb["lumiReweightingLumiWeight"]

w = {}
for channel in channels :
    for sample in totsampleList :
        rescale=1./Extra_norm[channel+sample]
        w[channel+sample]=RooFormulaVar("w","w", "@0*@1*@2*"+str(rescale), RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi))

#############
### PLOTS ###
#############

var = {}
for name in namePlotList:
    print "name = ", name
    var[name] = ras_zbb[name]
    var[name].setMin(min[name])
    var[name].setMax(max[name])
    var[name].setBins(binning[name])

th1 = {}

#################################  
### working point & selection ###
#################################

sumbkgMC = {}
sumsigMC = {}
sumDATA = {}
nevts = {}

for channel in channels :
    print "channel ... ", channel
    for sample in totsampleList :
        print "sample ... ", sample
        for cut in extraCuts :
            if cut=="" : iCut=extraCutsLep[channel]
            else : iCut=cut+"&"+extraCutsLep[channel]
            print "cuts ... ", iCut
            
            myRDS_red = myRDS[channel+sample]

            print "myRDS_red.numEntries()", myRDS_red.numEntries()

            if iCut : myRDS_red = myRDS_red.reduce(iCut)
            
            if sample != "DATA": myRDS_red.addColumn(w[channel+sample])
                
            if sample != "DATA": myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w")
            else               : myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get())

            nevts["pure"+sample+channel+cut]     = myRDS_red_w.numEntries()
            print "myRDS_red_w.numEntries()", myRDS_red_w.numEntries()
            if sample in MCsampleList :
                nevts["effective"+sample+channel+cut]= myRDS_red_w.numEntries()*(lumi["DATA"]/lumi[sample])
                nevts["weighted"+sample+channel+cut] = myRDS_red_w.sumEntries()*(lumi["DATA"]/lumi[sample])
            
            if sample in bkgMCsampleList :
                if sample==bkgMCsampleList[0]:
                    sumbkgMC["pure"+channel+cut]     = 0
                    sumbkgMC["effective"+channel+cut]= 0
                    sumbkgMC["weighted"+channel+cut] = 0
                sumbkgMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumbkgMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(lumi["DATA"]/lumi[sample])
                sumbkgMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(lumi["DATA"]/lumi[sample])
            sumsigMC["pure"+channel+cut]     = 0
            sumsigMC["effective"+channel+cut]= 0
            sumsigMC["weighted"+channel+cut] = 0
            if sample in sigMCsampleList :
                sumsigMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumsigMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(lumi["DATA"]/lumi[sample])
                sumsigMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(lumi["DATA"]/lumi[sample])
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
    print "totbkgMC".ljust(10), "totsigMC".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsampleList : print '{0}'.ljust(10).format(nevts["pure"+sample+channel+cut]),
        print '{0}'.ljust(10).format(sumbkgMC["pure"+channel+cut]), '{0}'.ljust(10).format(sumsigMC["pure"+channel+cut])
    print " "
    print "normalized MC yields ......................................................."
    print "Cuts".ljust(10),
    for sample in MCsampleList : print sample.ljust(10),
    print "totbkgMC".ljust(10), "totsigMC".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsampleList : print '{0:.2f}'.format(nevts["effective"+sample+channel+cut]).ljust(10),
        print '{0:.2f}'.format(sumbkgMC["effective"+channel+cut]).ljust(10), '{0:.2f}'.format(sumsigMC["effective"+channel+cut]).ljust(10)
    print " "
    print "weighted and normalized MC yields vs DATA yield ............................"
    print "Cuts".ljust(10),
    for sample in MCsampleList : print sample.ljust(10),
    print "totbkgMC".ljust(10), "totsigMC".ljust(10), "DATA".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsampleList : print '{0:.2f}'.format(nevts["weighted"+sample+channel+cut]).ljust(10),
        print '{0:.2f}'.format(sumbkgMC["weighted"+channel+cut]).ljust(10), '{0:.2f}'.format( sumsigMC["weighted"+channel+cut]).ljust(10), '{0}'.ljust(10).format( nevts["pure"+"DATA"+channel+cut])
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
print "totbkgMC".ljust(10), "totsigMC".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsampleList : print '{0}'.ljust(10).format(nevts["pure"+sample+"EEChannel"+cut]+nevts["pure"+sample+"MuMuChannel"+cut]),
    print '{0}'.ljust(10).format(sumbkgMC["pure"+"EEChannel"+cut]+sumbkgMC["pure"+"MuMuChannel"+cut]), '{0}'.ljust(10).format(sumsigMC["pure"+"EEChannel"+cut]+sumsigMC["pure"+"MuMuChannel"+cut])
print " "
print "normalized MC yields ......................................................."
print "Cuts".ljust(10),
for sample in MCsampleList : print sample.ljust(10),
print "totbkgMC".ljust(10), "totsigMC".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsampleList : print '{0:.2f}'.format(nevts["effective"+sample+"EEChannel"+cut]+nevts["effective"+sample+"MuMuChannel"+cut]).ljust(10),
    print '{0:.2f}'.format(sumbkgMC["effective"+"EEChannel"+cut]+sumbkgMC["effective"+"MuMuChannel"+cut]).ljust(10), '{0:.2f}'.format(sumsigMC["effective"+"EEChannel"+cut]+sumsigMC["effective"+"MuMuChannel"+cut]).ljust(10)
print " "
print "weighted and normalized MC yields vs DATA yield ............................"
print "Cuts".ljust(10),
for sample in MCsampleList : print sample.ljust(10),
print "totbkgMC".ljust(10), "totsigMC".ljust(10), "DATA".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsampleList : print '{0:.2f}'.format(nevts["weighted"+sample+"EEChannel"+cut]+nevts["weighted"+sample+"MuMuChannel"+cut]).ljust(10),
    print '{0:.2f}'.format(sumbkgMC["weighted"+"EEChannel"+cut]+sumbkgMC["weighted"+"MuMuChannel"+cut]).ljust(10), '{0:.2f}'.format(sumsigMC["weighted"+"EEChannel"+cut]+sumsigMC["weighted"+"MuMuChannel"+cut]).ljust(10), '{0}'.ljust(10).format(nevts["pure"+"DATA"+"EEChannel"+cut]+nevts["pure"+"DATA"+"MuMuChannel"+cut])
print "............................................................................"
print "............................................................................"
print " "
print " "

#################
###  outputs  ###
#################
   
file={}
#her you could choose the root ouput filenames
DirOut="Weights"
os.system('mkdir '+DirOut)
for sample in totsampleList:
    file[sample]=TFile(DirOut+"/histoStage"+WP+"extraCuts"+sample+".root","RECREATE")
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

