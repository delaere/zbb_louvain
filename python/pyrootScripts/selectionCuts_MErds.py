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
from zbbSamples import getSample, getDataLuminosity, getSamples

#####################################
### lists of samples and channels ###
#####################################

from zbbSamples import channels
from zbbSamples import MCsamples as MCsampleList
from zbbSamples import bkgMCsamples as SMMCsampleList
from zbbSamples import sigMCsamples as NSMMCsampleList
from zbbSamples import totsamples as totsampleList
from zbbSamples import samples_RDS as sampleList

#####################################################
### sample/wp/selection of interest
#####################################################

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

wp = 18
WP=str(wp)
print "working point: ",wp

#choose you set of cuts
extraCuts = [
    "jetmetMETsignificance < 10",
    ]

titleCuts = [
    "stage_"+WP,
    "mass bb+dPhi(Z,bb)",
    "mass bb+mass Z",
    "dPhi(Z,bb)",
    "bb mass",
    "zbb mass",
    "dPhi(bb,MET)+dPhi(Z,bb)",
    "dPhi(bb,MET)+dPhi(Z,bb)+bb mass",
    #"dPhi(Z,bb)+bb mass",
    ""
    ]

extraCutsLep = {
    "El"     : "(eventSelectionbestzmassEle>76.&eventSelectionbestzmassEle<106.)",
    "Mu"     : "(eventSelectionbestzmassMu>76.&eventSelectionbestzmassMu<106.)"
    }

stringCut = {}
#titleCut = {}

for i in range(0,len(extraCuts)) :
    stringCut[extraCuts[i]]="Cut"+str(i+1)
    #if titleCuts[i] : titleCut[extraCuts[i]]=titleCuts[i]
    #titleCut[extraCuts[i]]=""

#############
### files ###
#############

myRDS_el    = {}
myRDS_mu    = {}
myRDS       = {}
myRDS_red   = {} 
myRDS_red_w = {}

for sample in sampleList :
    redStage = "rc_eventSelection_"+WP+"==1"
    for channel in channels:
        print "Channel : ", channel
        if sample != "DATA":
            file_mc = TFile(getSample(sample,channel,"RDS").path)
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
            nEntries = 0
            myRDS[sample] = None
            for datasample in getSamples(datasampleList,[channel],["RDS"])
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
tmp=myRDS["ElZc"].reduce("mcSelectioneventType==1")
ras_zbb = tmp.get()
tmp=0

btagRew = [
#    "BtaggingReweightingHE"  ,
#    "BtaggingReweightingHP"  ,
#    "BtaggingReweightingHEHE",
#    "BtaggingReweightingHEHP",
    "BtaggingReweightingHPHP",
    ]

for b in btagRew:
    if b.find(btagWP)>-1 : 
        #rrv_w_b=ras_zbb[b]
        rrv_w_b=ras_zbb["BtaggingReweightingHPHP"]
	break
rrv_w_lep  = ras_zbb["LeptonsReweightingweight"]
rrv_w_lumi = ras_zbb["lumiReweightingLumiWeight"]

#if channel=="El" :
rrv_w_ptze = ras_zbb["eventSelectionbestzptEle"]

#w2_e = RooFormulaVar("w2","w2", "@0*@1*@2", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi))
w2_e = RooFormulaVar("w2","w2", "@0*@1*@2*(574.2/542.89)*((@3<10)+(@3>170) + ((@3>10)*(@3<170)*(-3.379031e-07 * pow(@3,3) +5.74726e-05 *@3*@3 +0.003684317*@3 +0.5997106)))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptze))
#w2_e = RooFormulaVar("w2","w2", "@0*@1*@2*@3", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptz))

#if channel=="Mu" :
rrv_w_ptzm = ras_zbb["eventSelectionbestzptMu"]    

# param from Control region Muon Correct
w2_m = RooFormulaVar("w2","w2", "@0*@1*@2*(762.38/716.57)*((@3<10)+(@3>170) + ((@3>10)*(@3<170)*(-3.379031e-07 * pow(@3,3) +5.74726e-05 *@3*@3 +0.003684317*@3 +0.5997106)))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm))
#w2_m = RooFormulaVar("w2","w2", "@0*@1*@2*@3", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptz))
w1 = RooFormulaVar("w1","w1", "@0*@1*@2", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi))
#w2_m = RooFormulaVar("w2","w2", "@0*@1*@2", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi))
#############
### PLOTS ###
#############

#################
### variables ###
#################
#here put all variables you want to plot and don't forget the binning

plotList = [
#   "mlphiggsvsbkg_115_MM_N"      : (15.,0.,1.),
#   "mlphiggsvsbkg_120_MM_N"      : (15.,0.,1.),
#   "mlphiggsvsbkg_125_MM_N"      : (15.,0.,1.),
#   "mlphiggsvsbkg_130_MM_N"      : (15.,0.,1.),
#   "mlphiggsvsbkg_135_MM_N"      : (15.,0.,1.),
#   "mlphiggsvsbkg_115_mu_MM_N"   : (15.,0.,1.),
#   "mlphiggsvsbkg_120_mu_MM_N"   : (15.,0.,1.),
#   "mlphiggsvsbkg_125_mu_MM_N"   : (15.,0.,1.),
#   "mlphiggsvsbkg_130_mu_MM_N"   : (15.,0.,1.),
#   "mlphiggsvsbkg_135_mu_MM_N"   : (15.,0.,1.),
    "mlphiggsvsbkg_115_comb_MM_N" : (20.,0.,1.),
    "mlphiggsvsbkg_120_comb_MM_N" : (20.,0.,1.),
    "mlphiggsvsbkg_125_comb_MM_N" : (20.,0.,1.),
    "mlphiggsvsbkg_130_comb_MM_N" : (20.,0.,1.),
    "mlphiggsvsbkg_135_comb_MM_N" : (20.,0.,1.),
    ]

var = {}
for name in plotList:
    print "name = ", name
    var[name] = ras_zbb[name]
    var[name].setMin(plotList[name][1])
    var[name].setMax(plotList[name][2])
    var[name].setBins(plotList[name][0])

th1 = {}

#################################  
### working point & selection ###
#################################

sumSMMC = {}
sumNSMMC = {}
sumDATA = {}
nevts = {}
rdh = {}

w2=1

for channel in channels :
    print "channel ... ", channel
    if channel=="Mu":w2=w2_m
    if channel=="El":w2=w2_e
    for sample in totsampleList :
        print "sample ... ", sample
        for cut in extraCuts :
            if cut=="" : iCut=extraCutsLep[channel]
            else : iCut=cut+"&"+extraCutsLep[channel]
            print "cuts ... ", iCut
            
            myRDS_red = myRDS[channel+sample]

            if iCut : myRDS_red = myRDS_red.reduce(iCut)
            
            if sample != "DATA":# myRDS_red.addColumn(w)
                if sample == "Zb" :myRDS_red.addColumn(w2)
                if sample != "Zb" :myRDS_red.addColumn(w1)
                
            if sample != "DATA":# myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w")
                if sample == "Zb" : myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w2")
                if sample != "Zb" : myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w1")
        


            else               : myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get())

            nevts["pure"+sample+channel+cut]     = myRDS_red_w.numEntries()
            if sample in MCsampleList :
                nevts["effective"+sample+channel+cut]= myRDS_red_w.numEntries()*(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity())
                nevts["weighted"+sample+channel+cut] = myRDS_red_w.sumEntries()*(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity())
            
            if sample in SMMCsampleList :
                if sample==SMMCsampleList[0]:
                    sumSMMC["pure"+channel+cut]     = 0
                    sumSMMC["effective"+channel+cut]= 0
                    sumSMMC["weighted"+channel+cut] = 0
                sumSMMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumSMMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity())
                sumSMMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity())
            if sample in NSMMCsampleList :
                if sample==NSMMCsampleList[0]:
                    sumNSMMC["pure"+channel+cut]     = 0
                    sumNSMMC["effective"+channel+cut]= 0
                    sumNSMMC["weighted"+channel+cut] = 0
                sumNSMMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumNSMMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity())
                sumNSMMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity())
            if sample=="DATA":
                sumDATA[channel+cut]=myRDS_red_w.numEntries()
            for name in plotList:
                if channel=="El" and (name.find("Mu")>-1 or name.find("mumu")>-1) : continue
                if channel=="Mu" and (name.find("Ele")>-1 or name.find("elel")>-1) : continue	
		
		m1=name.replace("mlphiggsvsbkg_","")
		mass=m1.replace("_comb_MM_N","")
		samp=sample
		if sample == "DATA" : samp="data_obs"
		if "ZH" in sample : samp = sample.replace("ZH","signal")
		if not "ZH" in sample : samp=samp+mass
		th1[channel+sample+name+cut] = TH1D(name+samp,name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                myRDS_red_w.fillHistogram(th1[channel+sample+name+cut], RooArgList(var[name]))
		
		rdh[channel+sample+name+cut] = RooDataHist("rdh_"+channel+sample+name+cut, "rdh_"+channel+sample+name+cut,
                                      RooArgSet(var[name]),myRDS_red)
				      
		for bin in range(0,var[name].getBins()):       
                    binras = rdh[channel+sample+name+cut].get(bin)
                    a, b = Double(1), Double(1)
                    rdh[channel+sample+name+cut].weightError(a,b)
                    aw = rdh[channel+sample+name+cut].weight()
		    print "factor",a,b , "nbr entries= ",aw 
                    if aw>0 : a=a/aw
                    if aw>0 : b=b/aw
                    th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"]= TH1D(name+samp+"_"+samp+"stat_bin"+str(bin+1)+"Up",name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                    myRDS_red_w.fillHistogram(th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"], RooArgList(var[name]))
                    th1[channel+sample+name+cut+"stat"+str(bin+1)+"Down"]= TH1D(name+samp+"_"+samp+"stat_bin"+str(bin+1)+"Down",name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                    myRDS_red_w.fillHistogram(th1[channel+sample+name+cut+"stat"+str(bin+1)+"Down"], RooArgList(var[name]))
                    tmp = th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"].GetBinContent(bin+1)
                    if aw>0 :
		        th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"].SetBinContent(bin+1,tmp*(1.+b))
                        th1[channel+sample+name+cut+"stat"+str(bin+1)+"Down"].SetBinContent(bin+1,tmp*(1.-a))
		    else :
			th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"].SetBinContent(bin+1,tmp+b)	    
		    print "bin", bin+1 ,"--- nominal =",tmp," --- variation Up =",b, th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"].GetBinContent(bin+1)," --- variation Down =",a, th1[channel+sample+name+cut+"stat"+str(bin+1)+"Down"].GetBinContent(bin+1)
		
            
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
    for sample in MCsampleList : print '{0}'.ljust(10).format(nevts["pure"+sample+"El"+cut]+nevts["pure"+sample+"Mu"+cut]),
    print '{0}'.ljust(10).format(sumSMMC["pure"+"El"+cut]+sumSMMC["pure"+"Mu"+cut]), '{0}'.ljust(10).format(sumNSMMC["pure"+"El"+cut]+sumNSMMC["pure"+"Mu"+cut])
print " "
print "normalized MC yields ......................................................."
print "Cuts".ljust(10),
for sample in MCsampleList : print sample.ljust(10),
print "totSMMC".ljust(10), "totNSMMC".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsampleList : print '{0:.2f}'.format(nevts["effective"+sample+"El"+cut]+nevts["effective"+sample+"Mu"+cut]).ljust(10),
    print '{0:.2f}'.format(sumSMMC["effective"+"El"+cut]+sumSMMC["effective"+"Mu"+cut]).ljust(10), '{0:.2f}'.format(sumNSMMC["effective"+"El"+cut]+sumNSMMC["effective"+"Mu"+cut]).ljust(10)
print " "
print "weighted and normalized MC yields vs DATA yield ............................"
print "Cuts".ljust(10),
for sample in MCsampleList : print sample.ljust(10),
print "totSMMC".ljust(10), "totNSMMC".ljust(10), "DATA".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsampleList : print '{0:.2f}'.format(nevts["weighted"+sample+"El"+cut]+nevts["weighted"+sample+"Mu"+cut]).ljust(10),
    print '{0:.2f}'.format(sumSMMC["weighted"+"El"+cut]+sumSMMC["weighted"+"Mu"+cut]).ljust(10), '{0:.2f}'.format(sumNSMMC["weighted"+"El"+cut]+sumNSMMC["weighted"+"Mu"+cut]).ljust(10), '{0}'.ljust(10).format(nevts["pure"+"DATA"+"El"+cut]+nevts["pure"+"DATA"+"Mu"+cut])
print "............................................................................"
print "............................................................................"
print " "
print " "

#################
###  outputs  ###
#################
   
file={}
file["Out"]=TFile("CSV_CLS/histoStage"+WP+"extraCuts.root","RECREATE")
#her you could choose the root ouput filenames
for channel in channels:
    if channel=="Combined" : continue
    chDir=file["Out"].mkdir(channel,channel)
    file["Out"].cd(channel)
    for sample in totsampleList:
    #file[sample]=TFile("CSV_CLS/histoStage"+WP+"extraCuts"+sample+".root","RECREATE")
        #for cut in extraCuts:
        #    chDir.mkdir(stringCut[cut],stringCut[cut])  
        for name in plotList:
            if channel=="El" and (name.find("Mu")>-1 or name.find("mumu")>-1) : continue
            if channel=="Mu" and (name.find("Ele")>-1 or name.find("elel")>-1) : continue
            if not sample == "DATA" : th1[channel+sample+name+cut].Scale(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity())
            th1[channel+sample+name+cut].Write()
	    Nbin=th1[channel+sample+name+cut].GetNbinsX();
	    for bin in range(1,Nbin+1):
                if not sample == "DATA" :th1[channel+sample+name+cut+"stat"+str(bin)+"Down"].Scale(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity())
                th1[channel+sample+name+cut+"stat"+str(bin)+"Down"].Write()
                if not sample == "DATA" :th1[channel+sample+name+cut+"stat"+str(bin)+"Up"].Scale(getDataLuminosity(channel)/getSample(sample,channel,"RDS").getLuminosity())
                th1[channel+sample+name+cut+"stat"+str(bin)+"Up"].Write()
file["Out"].Close()

