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
from zbbSamples import getSample, getDataLuminosity
from zbbSamples import channels, MCsamples, datasamples, sigMCsamples, bkgMCsamples, totsamples
from listForRDS import Extra_norm, namePlotList, namePlotListOnMerged, min, max, binning, PlotForCLs, SFs_fit, blindList
import os

#####################################################
### sample/wp/selection of interest
#####################################################

sampleType = "RDS" # "MERDS"
goTotCLS = False
DirOut="hist_newznothing"
doRew = False
useSFs = False
useMCTruth = True

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

#choose you set of cuts
extraCuts = [
    "",
    "jetmetbjet1pt>40&jetmetbjet2pt>25",
    "(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
    "(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)&jetmetbjet1pt>40&jetmetbjet2pt>25",    
    "jetmetnj==2",
    "jetmetnj==2&jetmetbjet1pt>40&jetmetbjet2pt>25",
    "jetmetnj==2&(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
    "jetmetnj==2&(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)&jetmetbjet1pt>40&jetmetbjet2pt>25",
    "jetmetnj>2",
    "jetmetnj>2&jetmetbjet1pt>40&jetmetbjet2pt>25",
    "jetmetnj>2&(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
    "jetmetnj>2&(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)&jetmetbjet1pt>40&jetmetbjet2pt>25",    
    #"vertexAssociationnvertices<13",
    #"vertexAssociationnvertices>=13&vertexAssociationnvertices<=17",
    #"vertexAssociationnvertices>17",
#    "(eventSelectiondijetM>80&eventSelectiondijetM<150)",
    #"newmlphiggsvsbkg_125_comb_MM_N<0.5&newmlphiggsvsbkg_125_comb_MM_N>=0.",
    #"newmlphiggsvsbkg_125_comb_MM_N>=0.5&newmlphiggsvsbkg_125_comb_MM_N<=1",
    #"ProdNN<0.5&ProdNN>=0.",
    #"ProdNN>=0.5&ProdNN<=1",
    #"SumWeightedNN<0.5&SumWeightedNN>=0.",
    #"SumWeightedNN>=0.5&SumWeightedNN<=1",
#    "jetmetbjet1pt>30",
#    "jetmetbjet2pt>30",
#    "jetmetbjet1pt>30&(eventSelectiondijetM<80||eventSelectiondijetM>150)",
#    "jetmetbjet2pt>30&(eventSelectiondijetM<80||eventSelectiondijetM>150)",

    ]

extraCutsLep = {
    "El"     : "(eventSelectionbestzmassEle>76.&eventSelectionbestzmassEle<106.)",
    "Mu"   : "(eventSelectionbestzmassMu>76.&eventSelectionbestzmassMu<106.)"
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

for sample in MCsamples:
    for channel in channels :
        print "the lumi of ", sample, " = ", getSample(sample,channel,sampleType).getLuminosity()
        MCweight[channel+sample] = getDataLuminosity(channel)/getSample(sample,channel,sampleType).getLuminosity()/Extra_norm[channel+sample]
        print "the weight of ", channel+sample," = ", MCweight[channel+sample]

#############
### files ###
#############

myRDS_el    = {}
myRDS_mu    = {}
myRDS       = {}
myRDS_red   = {} 
myRDS_red_w = {}

for sample in MCsamples :
    redStage = "rc_eventSelection_"+WP+"==1"
    for channel in channels:
        print "Channel : ", channel
        file_mc  = TFile(getSample(sample,channel,sampleType).path)
        tree_zbb1 = file_mc.Get("rds_zbb")
        tmpfile=TFile("tmp.root","RECREATE")
        tree_zbb=tree_zbb1.CopyTree(redStage.replace("==","_idx=="))
        ws_zbb = file_mc.Get("ws_ras")
        ras_zbb = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())
        rds_zbb = RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)
        nEntries = rds_zbb.numEntries()
        if sample == "DY" :
            if not useMCTruth :
                myRDS[channel+"Zbb"] = rds_zbb.reduce(redStage + "&mcSelectioneventType==6")
                myRDS[channel+"Zbx"] = rds_zbb.reduce(redStage + "&mcSelectioneventType>=4&mcSelectioneventType<6")
                myRDS[channel+"Zxx"] = rds_zbb.reduce(redStage + "&mcSelectioneventType<4&mcSelectioneventType>0")
                myRDS[channel+"Zno"] = rds_zbb.reduce(redStage + "&mcSelectioneventType==0")
            else :
                myRDS[channel+"Zbb"] = rds_zbb.reduce(redStage + "&abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)==5")
                myRDS[channel+"Zbx"] = rds_zbb.reduce(redStage + "&( (abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5) )")
                myRDS[channel+"Zxx"] = rds_zbb.reduce(redStage + "&abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)!=5")
            print "myRDS.numEntries() for ", "Zbb" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zbb"].numEntries()
            print "myRDS.numEntries() for ", "Zbx" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zbx"].numEntries()
            print "myRDS.numEntries() for ", "Zxx" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zxx"].numEntries()
            if not useMCTruth : print "myRDS.numEntries() for ", "Zno" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zno"].numEntries()
        else :
            myRDS[channel+sample] = rds_zbb.reduce(redStage)
            print "myRDS.numEntries() for ", sample , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+sample].numEntries()
        file_mc.Close()

for channel in channels:
    print "Channel : ", channel
    file={}
    for sample in datasamples :
      file[sample] = TFile(getSample(sample,channel,sampleType).path)
    rds_zbb = None
    for sample in datasamples :
      tree_zbb1 = file[sample].Get("rds_zbb")
      tmpfile=TFile("tmp.root","RECREATE")
      tree_zbb=tree_zbb1.CopyTree(redStage.replace("==","_idx=="))
      ws_zbb = file[sample].Get("ws_ras")
      ras_zbb = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())
      if rds_zbb is None:
        rds_zbb = RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)
      else:
        rds_zbb.append(RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)) 
    nEntries = rds_zbb.numEntries()
    myRDS[channel+"DATA"] = rds_zbb.reduce(redStage)
    print "myRDS.numEntries() for DATA = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"DATA"].numEntries()
    for sample in datasamples : file[sample].Close()
    
###############
### weights ###
###############
tmp=myRDS["ElZZ"].reduce("mcSelectioneventType==1")
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
rrv_w_ptz = {
    "Mu" : ras_zbb["eventSelectionbestzptMu"],
    "El" : ras_zbb["eventSelectionbestzptEle"]
}
w = {}
rewFormula = {}
for channel in channels :
    if doRew :
        if channel=="El" : rewFormula[channel] = "*(1172.93/1391.86)*((0.945437+0.00378645*20)*(@3<20)+(0.945437+0.00378645*@3)*(@3>20)*(@3<200)+(0.945437+0.00378645*200.)*(@3>200))"
        else : rewFormula[channel] = "*(1606.22/1913.74)*((0.945437+0.00378645*20)*(@3<20)+(0.945437+0.00378645*@3)*(@3>20)*(@3<200)+(0.945437+0.00378645*200.)*(@3>200))"
    else : rewFormula[channel] = ""
    for sample in totsamples :
        rescale=1./Extra_norm[channel+sample]
        if sampleType=="RDS" : rescale=1.
        if useSFs : rescale*=SFs_fit[channel+sample]
        if sample!="Zbb" : w[channel+sample]=RooFormulaVar("w","w", "@0*@1*@2*"+str(rescale), RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi))
        else : w[channel+sample]=RooFormulaVar("w","w", "@0*@1*@2*"+str(rescale)+rewFormula[channel], RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptz[channel]))
#############
### PLOTS ###
#############
        
if sampleType=="MERDS" : namePlotList+=namePlotListOnMerged
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
rdh = {}

for channel in channels :
    print "channel ... ", channel
    for sample in totsamples :
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
            if sample in MCsamples :
                nevts["effective"+sample+channel+cut]= myRDS_red_w.numEntries()*(getDataLuminosity(channel)/getSample(sample,channel,sampleType).getLuminosity())
                nevts["weighted"+sample+channel+cut] = myRDS_red_w.sumEntries()*(getDataLuminosity(channel)/getSample(sample,channel,sampleType).getLuminosity())
            
            if sample in bkgMCsamples :
                if sample==bkgMCsamples[0]:
                    sumbkgMC["pure"+channel+cut]     = 0
                    sumbkgMC["effective"+channel+cut]= 0
                    sumbkgMC["weighted"+channel+cut] = 0
                sumbkgMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumbkgMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(getDataLuminosity(channel)/getSample(sample,channel,sampleType).getLuminosity())
                sumbkgMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(getDataLuminosity(channel)/getSample(sample,channel,sampleType).getLuminosity())
            sumsigMC["pure"+channel+cut]     = 0
            sumsigMC["effective"+channel+cut]= 0
            sumsigMC["weighted"+channel+cut] = 0
            if sample in sigMCsamples :
                sumsigMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumsigMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(getDataLuminosity(channel)/getSample(sample,channel,sampleType).getLuminosity())
                sumsigMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(getDataLuminosity(channel)/getSample(sample,channel,sampleType).getLuminosity())
            if sample=="DATA":
                sumDATA[channel+cut]=myRDS_red_w.numEntries()
            for name in namePlotList:
                if not goTotCLS :
                    th1[channel+sample+name+cut] = TH1D(name,name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                    myRDS_red_w.fillHistogram(th1[channel+sample+name+cut], RooArgList(var[name]))
                    if name in blindList and sample=="DATA":
                        overflow=0
                        for bin in range(1,th1[channel+sample+name+cut].GetNbinsX()+1) :
                            if th1[channel+sample+name+cut].GetBinCenter(bin) > 0.5:
                                overflow+=th1[channel+sample+name+cut].GetBinContent(bin)
                                th1[channel+sample+name+cut].SetBinContent(bin,0)
                        th1[channel+sample+name+cut].SetBinContent(th1[channel+sample+name+cut].GetNbinsX(),overflow)
                else :
                    if not name in PlotForCLs : continue
                    #m1=name.replace("_","")
                    #mass=m1.replace("_comb_MM_N","")
                    mass="125"
                    samp=sample
                    if sample == "DATA" : samp="data_obs"
                    if "ZH" in sample : samp = sample.replace("ZH","signal")
                    if not "ZH" in sample : samp=samp+mass
                    th1[channel+sample+name+cut] = TH1D(name+samp,name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                    myRDS_red_w.fillHistogram(th1[channel+sample+name+cut], RooArgList(var[name]))
                    
                    rdh[channel+sample+name+cut] = RooDataHist("rdh_"+channel+sample+name+cut, "rdh_"+channel+sample+name+cut, RooArgSet(var[name]),myRDS_red)
				      
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
    for sample in MCsamples : print sample.ljust(10),
    print "totbkgMC".ljust(10), "totsigMC".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsamples : print '{0}'.ljust(10).format(nevts["pure"+sample+channel+cut]),
        print '{0}'.ljust(10).format(sumbkgMC["pure"+channel+cut]), '{0}'.ljust(10).format(sumsigMC["pure"+channel+cut])
    print " "
    print "normalized MC yields ......................................................."
    print "Cuts".ljust(10),
    for sample in MCsamples : print sample.ljust(10),
    print "totbkgMC".ljust(10), "totsigMC".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsamples : print '{0:.2f}'.format(nevts["effective"+sample+channel+cut]).ljust(10),
        print '{0:.2f}'.format(sumbkgMC["effective"+channel+cut]).ljust(10), '{0:.2f}'.format(sumsigMC["effective"+channel+cut]).ljust(10)
    print " "
    print "weighted and normalized MC yields vs DATA yield ............................"
    print "Cuts".ljust(10),
    for sample in MCsamples : print sample.ljust(10),
    print "totbkgMC".ljust(10), "totsigMC".ljust(10), "DATA".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsamples : print '{0:.2f}'.format(nevts["weighted"+sample+channel+cut]).ljust(10),
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
for sample in MCsamples : print sample.ljust(10),
print "totbkgMC".ljust(10), "totsigMC".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsamples : print '{0}'.ljust(10).format(nevts["pure"+sample+"El"+cut]+nevts["pure"+sample+"Mu"+cut]),
    print '{0}'.ljust(10).format(sumbkgMC["pure"+"El"+cut]+sumbkgMC["pure"+"Mu"+cut]), '{0}'.ljust(10).format(sumsigMC["pure"+"El"+cut]+sumsigMC["pure"+"Mu"+cut])
print " "
print "normalized MC yields ......................................................."
print "Cuts".ljust(10),
for sample in MCsamples : print sample.ljust(10),
print "totbkgMC".ljust(10), "totsigMC".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsamples : print '{0:.2f}'.format(nevts["effective"+sample+"El"+cut]+nevts["effective"+sample+"Mu"+cut]).ljust(10),
    print '{0:.2f}'.format(sumbkgMC["effective"+"El"+cut]+sumbkgMC["effective"+"Mu"+cut]).ljust(10), '{0:.2f}'.format(sumsigMC["effective"+"El"+cut]+sumsigMC["effective"+"Mu"+cut]).ljust(10)
print " "
print "weighted and normalized MC yields vs DATA yield ............................"
print "Cuts".ljust(10),
for sample in MCsamples : print sample.ljust(10),
print "totbkgMC".ljust(10), "totsigMC".ljust(10), "DATA".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsamples : print '{0:.2f}'.format(nevts["weighted"+sample+"El"+cut]+nevts["weighted"+sample+"Mu"+cut]).ljust(10),
    print '{0:.2f}'.format(sumbkgMC["weighted"+"El"+cut]+sumbkgMC["weighted"+"Mu"+cut]).ljust(10), '{0:.2f}'.format(sumsigMC["weighted"+"El"+cut]+sumsigMC["weighted"+"Mu"+cut]).ljust(10), '{0}'.ljust(10).format(nevts["pure"+"DATA"+"El"+cut]+nevts["pure"+"DATA"+"Mu"+cut])
print "............................................................................"
print "............................................................................"
print " "
print " "

#################
###  outputs  ###
#################
   
file={}
#her you could choose the root ouput dir
os.system('mkdir '+DirOut)

if goTotCLS :
    file["Out"]=TFile(DirOut+"/histoStage"+WP+"extraCuts.root","RECREATE")
    for channel in channels:
        if channel=="Combined" : continue
        chDir=file["Out"].mkdir(channel,channel)
        file["Out"].cd(channel)
        for sample in totsamples:
            for name in namePlotList:
                if not name in PlotForCLs : continue
                if not sample == "DATA" : th1[channel+sample+name+cut].Scale(getDataLuminosity(channel)/getSample(sample,channel,sampleType).getLuminosity())
                th1[channel+sample+name+cut].Write()
                Nbin=th1[channel+sample+name+cut].GetNbinsX();
                for bin in range(1,Nbin+1):
                    if not sample == "DATA" :th1[channel+sample+name+cut+"stat"+str(bin)+"Down"].Scale(getDataLuminosity(channel)/getSample(sample,channel,sampleType).getLuminosity())
                    th1[channel+sample+name+cut+"stat"+str(bin)+"Down"].Write()
                    if not sample == "DATA" :th1[channel+sample+name+cut+"stat"+str(bin)+"Up"].Scale(getDataLuminosity(channel)/getSample(sample,channel,sampleType).getLuminosity())
                    th1[channel+sample+name+cut+"stat"+str(bin)+"Up"].Write()
    file["Out"].Close()
else :
    for sample in totsamples:
        file[sample]=TFile(DirOut+"/histoStage"+WP+"extraCuts"+sample+".root","RECREATE")
        for channel in channels:
            if channel=="Combined" : continue
            chDir=file[sample].mkdir(channel,channel)
            for cut in extraCuts:
                chDir.mkdir(stringCut[cut],cut)
                chDir.cd(stringCut[cut])
                for name in namePlotList:
                    th1[channel+sample+name+cut].Write()
        file[sample].Close()
