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
from input_selectionCuts import inputs
from zbbCommons import zbbnorm
from eventSelection import categoryNames
from optparse import OptionParser


#####################################################
### sample/wp/selection of interest
#####################################################

######################################################

########################## Configuration############################################
nbinname=str(inputs.nbins)

print "nbins=",nbinname
	  

doZpTReweighting = False # false by default. If true, set slope and offset.
slope = 0.0013
offset_p = 0.93
offset_m = 1.09
slope_up = 0.0026
slope_down = 0.000005


# Scale factors ##
#  2jet bin

sf_tt=inputs.sf_tt_2jet
sf_zbb=inputs.sf_zbb_2jet
sf_zbx=inputs.sf_zbx_2jet
sf_zxx=inputs.sf_zxx_2jet
sf_ttp2=inputs.sf_tt_P2jet
sf_zbbp2=inputs.sf_zbb_P2jet
sf_zbxp2=inputs.sf_zbx_P2jet
sf_zxxp2=inputs.sf_zxx_P2jet

#I define string vars for the formula var (in order to make more readable the formulas)
str_sftt=str(sf_tt)
str_sfzbb=str(sf_zbb)
str_sfzbx=str(sf_zbx)
str_sfzxx=str(sf_zxx)
str_sfttp2=str(sf_ttp2)
str_sfzbbp2=str(sf_zbbp2)
str_sfzbxp2=str(sf_zbxp2)
str_sfzxxp2=str(sf_zxxp2)


#inputfolder ="/home/fynu/vizangarciaj/storage/RDS/CSVSel2011JER0/RDS20130515V1/"
#inputfolder ="/home/fynu/vizangarciaj/storage/RDS/CSVSel2011JER0/RDS20130521PTj1_40_PTj2_25_V1/"
#inputfolder ="/home/fynu/vizangarciaj/storage/RDS/CSVSel2011JER0/RDS20130522PTj1_40_PTj2_25_V2Camille/"
#inputfolder ="/home/fynu/vizangarciaj/storage/RDS/CSVSel2011JER0/RDS20130611PTj1_40_PTj2_25_V3noCSVProd/"
#inputfolder ="/home/fynu/vizangarciaj/storage/RDS/CSVSel2011JER0/RDS20130611PTj1_40_PTj2_25_V4noCSVProd/"
######################################################################################

name_ext=inputs.inputfolder.replace("/","")+"_nbin"+nbinname+inputs.suffix
    
if inputs.wp == 17:
  btagWP = "HEHP"
if inputs.wp == 18:
  btagWP = "HPHP"




print "working point: ",inputs.wp
WP=str(inputs.wp)

channels  = [
    "EEChannel",
    "MuMuChannel",
    ]

#choose you set of cutsu = RooFormulaVar("w2_u","w2_u", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 0.995*((@3>10)*(@3<190)*((((@4==2)*(0.0026*@3 +0.93)) + ((@4>2)*(-0.0026*@3 +1.09)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm,rrv_w_njet)) 


if inputs.category=="P2bin":
  extraCuts = [
      "jetmetMETsignificance < 10&jetmetnj>2 &eventSelectiondijetM>"+str(inputs.mbbmin_P2jet)+" &eventSelectiondijetM<"+str(inputs.mbbmax_P2jet)+" &(eventSelectionbestzptMu>"+str(inputs.ptzmin)+"||eventSelectionbestzptEle>"+str(inputs.ptzmin)+")&jetmetbjet1pt>"+str(inputs.ptj1min)+"&jetmetbjet2pt>"+str(inputs.ptj2min)+"",
      ]
elif inputs.category=="2bin" :
  extraCuts = [
      "jetmetMETsignificance < 10 &jetmetnj==2 &eventSelectiondijetM>"+str(inputs.mbbmin_2jet)+"&eventSelectiondijetM<"+str(inputs.mbbmax_2jet)+" &(eventSelectionbestzptMu>"+str(inputs.ptzmin)+"||eventSelectionbestzptEle>"+str(inputs.ptzmin)+")&jetmetbjet1pt>"+str(inputs.ptj1min)+"&jetmetbjet2pt>"+str(inputs.ptj2min)+"",
      ]
else:
  extraCuts = [
      "jetmetMETsignificance < 10 & ((jetmetnj==2 &eventSelectiondijetM>"+str(inputs.mbbmin_2jet)+"&eventSelectiondijetM<"+str(inputs.mbbmax_2jet)+") || (jetmetnj>2 &eventSelectiondijetM>"+str(inputs.mbbmin_P2jet)+"&eventSelectiondijetM<"+str(inputs.mbbmax_P2jet)+")) &(eventSelectionbestzptMu>"+str(inputs.ptzmin)+"||eventSelectionbestzptEle>"+str(inputs.ptzmin)+")&jetmetbjet1pt>"+str(inputs.ptj1min)+"&jetmetbjet2pt>"+str(inputs.ptj2min)+"",
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
    "EEChannel"     : "(eventSelectionbestzmassEle>76.&eventSelectionbestzmassEle<106.)",#&eventSelectionbestzptEle>100.&eventSelectionbestzptEle>50)",
    "MuMuChannel"   : "(eventSelectionbestzmassMu>76.&eventSelectionbestzmassMu<106.)"#&eventSelectionbestzptMu>100.&eventSelectionbestzptMu>50)"
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

MCsampleList   = ["Zb","Zc","Zl","TT","ZZ","ZH125","ZbPtZUp","ZbPtZDown","ZcPtZUp","ZcPtZDown","ZH120","ZH115","ZH130","ZH135"]#,"ZbPtZUp","ZbPtZDown"]#,"ZA"]
SMMCsampleList = ["Zb","Zc","Zl","TT","ZZ"]
NSMMCsampleList= ["ZH125","ZH120","ZH115","ZH130","ZH135"]#,"ZA"]
totsampleList  = ["DATA","Zb","Zc","Zl","TT","ZZ","ZH125","ZbPtZUp","ZbPtZDown","ZcPtZUp","ZcPtZDown","ZH120","ZH115","ZH130","ZH135"]#,"ZbPtZUp","ZbPtZDown"]#,"ZA"]
sampleList     = ["DATA","DY","TT","ZZ","ZH125","DYPt100","ZH120","ZH115","ZH130","ZH135"]

        
lumi = { "DATAMuMuChannel"   : zbbnorm.lumi_totMu2011,
         "DATAEEChannel"     : zbbnorm.lumi_totEle2011,
         "TTEEChannel"     : zbbnorm.nev_TTjets_fall11/(zbbnorm.xsec_TTjets_7TeV)/1000.,
         "ZbEEChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZbPtZDownEEChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZbPtZUpEEChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZcPtZDownEEChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZcPtZUpEEChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZcEEChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZlEEChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZZEEChannel"     : zbbnorm.nev_ZZ_fall11/(zbbnorm.xsec_ZZ_7TeV)/1000.,
         "TTMuMuChannel"     : zbbnorm.nev_TTjets_fall11/(zbbnorm.xsec_TTjets_7TeV)/1000.,
         "ZbMuMuChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZbPtZDownMuMuChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZbPtZUpMuMuChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZcPtZDownMuMuChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZcPtZUpMuMuChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,        
	 "ZcMuMuChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZlMuMuChannel"     : zbbnorm.nev_DYjets_fall11/(zbbnorm.xsec_DYjets_7TeV)/1000.,
         "ZZMuMuChannel"     : zbbnorm.nev_ZZ_fall11/zbbnorm.xsec_ZZ_7TeV/1000.,
	 "ZH115EEChannel"  : zbbnorm.nev_ZH115_fall11/zbbnorm.xsec_ZH115_7TeV_El/1000.,
         "ZH120EEChannel"  : zbbnorm.nev_ZH120_fall11/zbbnorm.xsec_ZH120_7TeV_El/1000.,
	 "ZH115MuMuChannel"  : zbbnorm.nev_ZH115_fall11/zbbnorm.xsec_ZH115_7TeV_Mu/1000.,
         "ZH120MuMuChannel"  : zbbnorm.nev_ZH120_fall11/zbbnorm.xsec_ZH120_7TeV_Mu/1000.,
	 "ZH125EEChannel"  : zbbnorm.nev_ZH125_fall11/zbbnorm.xsec_ZH125_7TeV_El/1000.,
	 "ZH125MuMuChannel"  : zbbnorm.nev_ZH125_fall11/zbbnorm.xsec_ZH125_7TeV_Mu/1000.,
         "ZH130EEChannel"  : zbbnorm.nev_ZH130_fall11/zbbnorm.xsec_ZH130_7TeV_El/1000.,
         "ZH135EEChannel"  : zbbnorm.nev_ZH135_fall11/zbbnorm.xsec_ZH135_7TeV_El/1000.,
         "ZH130MuMuChannel"  : zbbnorm.nev_ZH130_fall11/zbbnorm.xsec_ZH130_7TeV_Mu/1000.,
         "ZH135MuMuChannel"  : zbbnorm.nev_ZH135_fall11/zbbnorm.xsec_ZH135_7TeV_Mu/1000.
	         }

MCweight = {}

#for sample in MCsampleList:
#    print "the lumi of ", sample, " = ", lumi[sample+channel]
#    MCweight[sample] = lumi["DATAMuMuChannel"]/lumi[sample+channel]
#    print "the weight of ", sample," = ", MCweight[sample+channel]

#############
### files ###
#############

myRDS_el    = {}
myRDS_mu    = {}
myRDS       = {}
myRDS_lpt       = {}
myRDS_red   = {} 
myRDS_red_w = {}


filename_el = {"DATA_A" : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ElA_DATA.root",
               "DATA_B" : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ElB_DATA.root",
               "TT"     : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_TT_El_MC.root",
               "DY"     : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_El_MC.root",
               "ZZ"     : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZZ_El_MC.root",
               "ZH125"  : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZH125_El_MC.root",
               "ZH115"  : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZH115_El_MC.root",
               "ZH120"  : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZH120_El_MC.root",
               "ZH130"  : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZH130_El_MC.root",
               "ZH135"  : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZH135_El_MC.root",
	       "DYPt100": inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_DY_Pt100_El_MC.root",
               }
filename_mu = {"DATA_A" : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_MuA_DATA.root",
               "DATA_B" : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_MuB_DATA.root",
               "TT"     : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_TT_Mu_MC.root",
               "DY"     : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_Mu_MC.root",
               "ZZ"     : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZZ_Mu_MC.root",
               "ZH125"  : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZH125_Mu_MC.root",
               "ZH115"  : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZH115_Mu_MC.root",
               "ZH120"  : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZH120_Mu_MC.root",
               "ZH130"  : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZH130_Mu_MC.root",
               "ZH135"  : inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_ZH135_Mu_MC.root",
	       "DYPt100": inputs.inputprefolder+inputs.inputfolder+"/RDS_rdsME_DY_Pt100_Mu_MC.root",              
               }


for sample in sampleList :

    redStage = "rc_eventSelection_"+WP+"==1"
    for channel in channels:
        print "Channel : ", channel
        if sample != "DATA":
            
            if channel=="EEChannel" : file_mc  = TFile(filename_el[sample])
            else : file_mc  = TFile(filename_mu[sample])
            
            nEntries = file_mc.Get("rds_zbb").numEntries()
        
            if sample == "DY":
                #myRDS[channel+"Zb"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==3")
                #myRDS[channel+"Zc"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==2")
                #myRDS[channel+"Zl"] = file_mc.Get("rds_zbb").reduce(redStage + "&mcSelectioneventType==1")

                myRDS[channel+"Zb"] = file_mc.Get("rds_zbb").reduce(redStage + "&abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)==5")#&eventSelectionbestzptEle<120&eventSelectionbestzptMu<120")
                myRDS[channel+"Zc"] = file_mc.Get("rds_zbb").reduce(redStage + "&((abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5)||(abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5 ))")#&eventSelectionbestzptEle<120&eventSelectionbestzptMu<120")
                myRDS[channel+"Zl"] = file_mc.Get("rds_zbb").reduce(redStage + "&abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)!=5")#&eventSelectionbestzptEle<120&eventSelectionbestzptMu<120")
                print "myRDS.numEntries() for ", "Zb" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zb"].sumEntries()
                print "myRDS.numEntries() for ", "Zc" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zc"].sumEntries()
                print "myRDS.numEntries() for ", "Zl" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zl"].sumEntries()

		myRDS[channel+"ZbPtZDown"] = file_mc.Get("rds_zbb").reduce(redStage + "&abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)==5")
		myRDS[channel+"ZbPtZUp"] = file_mc.Get("rds_zbb").reduce(redStage + "&abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)==5")
		
		myRDS[channel+"ZcPtZDown"] = file_mc.Get("rds_zbb").reduce(redStage +"&((abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5)||(abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5 ))")
		myRDS[channel+"ZcPtZUp"] = file_mc.Get("rds_zbb").reduce(redStage + "&((abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5)||(abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5 ))")
		
	    if sample == "DYPt100" :
                tmp1 = file_mc.Get("rds_zbb").reduce(redStage + "&abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)==5&(eventSelectionbestzptEle>120||eventSelectionbestzptMu>120)")
                tmp2 = file_mc.Get("rds_zbb").reduce(redStage + "&((abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5)||(abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5 ))&(eventSelectionbestzptEle>120||eventSelectionbestzptMu>120)")
                tmp3= file_mc.Get("rds_zbb").reduce(redStage + "&abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)!=5&(eventSelectionbestzptEle>120||eventSelectionbestzptMu>120)")
		tmp1Down = file_mc.Get("rds_zbb").reduce(redStage + "&abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)==5&(eventSelectionbestzptEle>120||eventSelectionbestzptMu>120)")
		tmp1Up= file_mc.Get("rds_zbb").reduce(redStage + "&abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)==5&(eventSelectionbestzptEle>120||eventSelectionbestzptMu>120)")	
		tmp1Downc = file_mc.Get("rds_zbb").reduce(redStage + "&((abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5)||(abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5 ))&(eventSelectionbestzptEle>120||eventSelectionbestzptMu>120)")
		tmp1Upc= file_mc.Get("rds_zbb").reduce(redStage + "&((abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5)||(abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5 ))&(eventSelectionbestzptEle>120||eventSelectionbestzptMu>120)")	
		
		myRDS[channel+"Zb"].append(tmp1)
		myRDS[channel+"Zc"].append(tmp2)
		myRDS[channel+"Zl"].append(tmp3)
		myRDS[channel+"ZbPtZDown"].append(tmp1Down)
		myRDS[channel+"ZbPtZUp"].append(tmp1Up)
		myRDS[channel+"ZcPtZDown"].append(tmp1Downc)
		myRDS[channel+"ZcPtZUp"].append(tmp1Upc)	
			
		print "myRDS.sumEntries() for ", "Zb" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zb"].sumEntries()
                print "myRDS.sumEntries() for ", "Zc" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zc"].sumEntries()
                print "myRDS.sumEntries() for ", "Zl" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zl"].sumEntries()
		
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



if inputs.wp==17:
  btagRew = [
      "BtaggingReweightingHEHP",
      ]
if inputs.wp==18:
  btagRew = [
      "BtaggingReweightingHPHP",
      ]    

# For PtZ reweighting part:

for b in btagRew:
    if b.find(btagWP)>-1 : 
        #rrv_w_b=ras_zbb[b]
	if inputs.wp==17:
          rrv_w_b=ras_zbb["BtaggingReweightingHEHP"]
	  break
	if inputs.wp==18:
          rrv_w_b=ras_zbb["BtaggingReweightingHPHP"]
	  break	
	
rrv_w_lep  = ras_zbb["LeptonsReweightingweight"]
rrv_w_lumi = ras_zbb["lumiReweightingLumiWeight"]
rrv_w_ptzgen = ras_zbb["mcSelectionZptSt3"]

if inputs.wp==17:
  rrv_w_b=ras_zbb["BtaggingReweightingHEHP"]
if inputs.wp==18:
  rrv_w_b=ras_zbb["BtaggingReweightingHPHP"]

rrv_w_njet = ras_zbb["jetmetnj"]

#if channel=="EEChannel" :
rrv_w_ptze = ras_zbb["eventSelectionbestzptEle"]


if doZpTReweighting:#needs to be update in case we want to put the reweighting back
  wzbb_e = RooFormulaVar("w2","w2", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 0.9969*((@3>10)*(@3<190)*((((@4==2)*(slope*@3 +offset_p)) + ((@4>2)*(-slope*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptze,rrv_w_njet))
  wzbb_ec = RooFormulaVar("w2c","w2c", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 0.9999*((@3>10)*(@3<190)*((((@4==2)*(slope*@3 +offset_p)) + ((@4>2)*(-slope*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptze,rrv_w_njet))

  wzbb_e_u = RooFormulaVar("w2_u","w2_u", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 0.99*((@3>10)*(@3<190)*((((@4==2)*(slope_up*@3 +offset_p)) + ((@4>2)*(-slope_up*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptze,rrv_w_njet))
  wzbb_e_uc = RooFormulaVar("w2_uc","w2_uc", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 1.0064*((@3>10)*(@3<190)*((((@4==2)*(slope_up*@3 +offset_p)) + ((@4>2)*(-slope_up*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptze,rrv_w_njet))
  wzbb_e_d = RooFormulaVar("w2_d","w2_d", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 1.0088*((@3>10)*(@3<190)*((((@4==2)*(slope_down*@3 +offset_p)) + ((@4>2)*(-0.0003*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptze,rrv_w_njet))
  wzbb_e_dc = RooFormulaVar("w2_dc","w2_dc", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 1.002*((@3>10)*(@3<190)*((((@4==2)*(slope_down*@3 +offset_p)) + ((@4>2)*(-0.0003*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptze,rrv_w_njet))

else :
  wzbb_e = RooFormulaVar("w2","w2", "@0*@1*@2*((@3<120)+((@3>120))*15.85/(55.75))*(("+str_sfzbb+"*(@4==2)) + ("+str_sfzbbp2+"*(@4>2)))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptze,rrv_w_njet))
  wzbb_ec = RooFormulaVar("w2c","w2c", "@0*@1*@2*((@3<120)+((@3>120))*15.85/(55.75))*(("+str_sfzbx+"*(@4==2)) + ("+str_sfzbxp2+"*(@4>2)))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptze,rrv_w_njet))
  wz_e = RooFormulaVar("w1_z","w1_z", "@0*@1*@2*((@3<120)+((@3>120))*15.85/(55.75))*(("+str_sfzxx+"*(@4==2)) + ("+str_sfzxxp2+"*(@4>2)))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptze,rrv_w_njet))
  wzt_e = RooFormulaVar("w1t_z","w1t_z", "@0*@1*@2*(("+str_sftt+"*(@4==2)) + ("+str_sfttp2+"*(@4>2)))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptze,rrv_w_njet))
  wzbb_e_u = 1.0
  wzbb_e_uc =1.0
  wzbb_e_d = 1.0
  wzbb_e_dc =1.0
  
  



#if channel=="MuMuChannel" :
rrv_w_ptzm = ras_zbb["eventSelectionbestzptMu"]  

if doZpTReweighting:  
  wzbb_m = RooFormulaVar("w2","w2", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 0.996*((@3>10)*(@3<190)*((((@4==2)*(slope*@3 +offset_p)) + ((@4>2)*(-slope*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm,rrv_w_njet))
  wzbb_mc = RooFormulaVar("w2c","w2c", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 1.0001*((@3>10)*(@3<190)*((((@4==2)*(slope*@3 +offset_p)) + ((@4>2)*(-slope*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm,rrv_w_njet))

  wzbb_m_u = RooFormulaVar("w2_u","w2_u", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 0.995*((@3>10)*(@3<190)*((((@4==2)*(slope_up*@3 +offset_p)) + ((@4>2)*(-slope_up*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm,rrv_w_njet))
  wzbb_m_uc = RooFormulaVar("w2_uc","w2_uc", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 1.005*((@3>10)*(@3<190)*((((@4==2)*(slope_up*@3 +offset_p)) + ((@4>2)*(-slope_up*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm,rrv_w_njet))
  wzbb_m_d = RooFormulaVar("w2_d","w2_d", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 1.006*((@3>10)*(@3<190)*((((@4==2)*(slope_down*@3 +offset_p)) + ((@4>2)*(-0.0003*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm,rrv_w_njet))
  wzbb_m_dc = RooFormulaVar("w2_dc","w2_dc", "@0*@1*@2*((@3<120)+((@3>120)*15.85/(55.75)))*((@3<10)+(@3>190) + 1.004*((@3>10)*(@3<190)*((((@4==2)*(slope_down*@3 +offset_p)) + ((@4>2)*(-0.0003*@3 +offset_m)))-1) +1))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm,rrv_w_njet))


else:
  wzbb_m = RooFormulaVar("w2","w2", "@0*@1*@2*((@3<120)+((@3>120))*15.85/(55.75))*(("+str_sfzbb+"*(@4==2)) + ("+str_sfzbbp2+"*(@4>2)))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm,rrv_w_njet))
  wzbb_mc = RooFormulaVar("w2c","w2c", "@0*@1*@2*((@3<120)+((@3>120))*15.85/(55.75))*(("+str_sfzbx+"*(@4==2)) + ("+str_sfzbxp2+"*(@4>2)))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm,rrv_w_njet))
  wz_m = RooFormulaVar("w1_z","w1_Z", "@0*@1*@2*((@3<120)+((@3>120))*15.85/(55.75))*(("+str_sfzxx+"*(@4==2)) + ("+str_sfzxxp2+"*(@4>2)))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm,rrv_w_njet))
  wzt_m = RooFormulaVar("w1t_z","w1t_z", "@0*@1*@2*(("+str_sftt+"*(@4==2)) + ("+str_sfttp2+"*(@4>2)))", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptzm,rrv_w_njet))
  wzbb_m_u = 1.0
  wzbb_m_uc =1.0
  wzbb_m_d = 1.0
  wzbb_m_dc = 1.0 
  
  



w1 = RooFormulaVar("w1","w1", "@0*@1*@2", RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi))

#############
### PLOTS ###
#############

#################
### variables ###
#################
#here put all variables you want to plot and don't forget the binning

if inputs.category=="2bin":
  namePlotList = [
    "mlphiggsvsbkg_125_comb_2jets_ML",   
    "mlphiggsvsbkg_115_comb_2jets_ML",   
    "mlphiggsvsbkg_120_comb_2jets_ML",   
    "mlphiggsvsbkg_130_comb_2jets_ML",   
    "mlphiggsvsbkg_135_comb_2jets_ML"
    ]
elif inputs.category=="P2bin":
  namePlotList = [
    "mlphiggsvsbkg_125_comb_P2jets_ML",
    "mlphiggsvsbkg_115_comb_P2jets_ML",
    "mlphiggsvsbkg_120_comb_P2jets_ML",
    "mlphiggsvsbkg_130_comb_P2jets_ML",
    "mlphiggsvsbkg_135_comb_P2jets_ML"
    ]
elif inputs.category=="Both":
  namePlotList = [
    "mlphiggsvsbkg_125_comb_ML",
    ]
else:
  print "Unknown category:", inputs.category, " exitting"
  exit()
#namePlotList = [
#    #"eventSelectiondijetM",
#    "mlphiggsvsbkg_125_comb_P2jets_ML",
#    "mlphiggsvsbkg_125_comb_2jets_ML",   
#    "mlphiggsvsbkg_115_comb_P2jets_ML",
#    "mlphiggsvsbkg_115_comb_2jets_ML",   
#    "mlphiggsvsbkg_120_comb_P2jets_ML",
#    "mlphiggsvsbkg_120_comb_2jets_ML",   
#    "mlphiggsvsbkg_130_comb_P2jets_ML",
#    "mlphiggsvsbkg_130_comb_2jets_ML",   
#    "mlphiggsvsbkg_135_comb_P2jets_ML",
#    "mlphiggsvsbkg_135_comb_2jets_ML",   
#    "MLPproduct_2jets",
#    "MLPproduct_P2jets"    
#    ]

################
### minimums ###
################
min = {
    "eventSelectiondijetM"		      :    115,
    "mlphiggsvsbkg_125_comb_P2jets_ML"		:	0,
    "mlphiggsvsbkg_125_comb_2jets_ML"		:	0,   
    "mlphiggsvsbkg_115_comb_P2jets_ML"		:	0,
    "mlphiggsvsbkg_115_comb_2jets_ML"		:	0,   
    "mlphiggsvsbkg_120_comb_P2jets_ML"		:	0,
    "mlphiggsvsbkg_120_comb_2jets_ML"		:	0,   
    "mlphiggsvsbkg_130_comb_P2jets_ML"		:	0,
    "mlphiggsvsbkg_130_comb_2jets_ML"		:	0,   
    "mlphiggsvsbkg_135_comb_P2jets_ML"		:	0,
    "mlphiggsvsbkg_135_comb_2jets_ML"		:	0,   

    "mlphiggsvsbkg_115_comb_MM_N"             :    0,
    "mlphiggsvsbkg_120_comb_MM_N"             :    0,
    "mlphiggsvsbkg_125_comb_MM_N"             :    0,
    "mlphiggsvsbkg_130_comb_MM_N"             :    0,
    "mlphiggsvsbkg_135_comb_MM_N"             :    0,
    "mlphiggsvsbkg_125_comb_ML"             :    0,
    "MLPproduct_2jets"				:0,
    "MLPproduct_P2jets"				:0,     
}

################
### maximums ###
################

max = {    
    "eventSelectiondijetM"		      :    145,
    "mlphiggsvsbkg_125_comb_P2jets_ML"		:	1.,
    "mlphiggsvsbkg_125_comb_2jets_ML"		:	1.,   
    "mlphiggsvsbkg_115_comb_P2jets_ML"		:	1.,
    "mlphiggsvsbkg_115_comb_2jets_ML"		:	1.,   
    "mlphiggsvsbkg_120_comb_P2jets_ML"		:	1.,
    "mlphiggsvsbkg_120_comb_2jets_ML"		:	1.,   
    "mlphiggsvsbkg_130_comb_P2jets_ML"		:	1.,
    "mlphiggsvsbkg_130_comb_2jets_ML"		:	1.,   
    "mlphiggsvsbkg_135_comb_P2jets_ML"		:	1.,
    "mlphiggsvsbkg_135_comb_2jets_ML"		:	1.,   
    "mlphiggsvsbkg_115_comb_MM_N"             :    1.,
    "mlphiggsvsbkg_120_comb_MM_N"             :    1.,
    "mlphiggsvsbkg_125_comb_MM_N"             :    1.,
    "mlphiggsvsbkg_130_comb_MM_N"             :    1.,
    "mlphiggsvsbkg_135_comb_MM_N"             :    1.,
    "mlphiggsvsbkg_125_comb_ML"             :    1.,
    "MLPproduct_2jets"				:1,  
    "MLPproduct_P2jets"				:1,       
    }

################
### binning  ###
################


binning = {
    "eventSelectiondijetM"		      :    5,
    "mlphiggsvsbkg_125_comb_P2jets_ML"		:	inputs.nbins,
    "mlphiggsvsbkg_125_comb_2jets_ML"		:	inputs.nbins,   
    "mlphiggsvsbkg_115_comb_P2jets_ML"		:	inputs.nbins,
    "mlphiggsvsbkg_115_comb_2jets_ML"		:	inputs.nbins,   
    "mlphiggsvsbkg_120_comb_P2jets_ML"		:	inputs.nbins,
    "mlphiggsvsbkg_120_comb_2jets_ML"		:	inputs.nbins,   
    "mlphiggsvsbkg_130_comb_P2jets_ML"		:	inputs.nbins,
    "mlphiggsvsbkg_130_comb_2jets_ML"		:	inputs.nbins,   
    "mlphiggsvsbkg_135_comb_P2jets_ML"		:	inputs.nbins,
    "mlphiggsvsbkg_135_comb_2jets_ML"		:	inputs.nbins,   
    "mlphiggsvsbkg_115_comb_MM_N"             :    inputs.nbins,
    "mlphiggsvsbkg_120_comb_MM_N"             :    inputs.nbins,
    "mlphiggsvsbkg_125_comb_MM_N"             :    inputs.nbins,
    "mlphiggsvsbkg_130_comb_MM_N"             :    inputs.nbins,
    "mlphiggsvsbkg_135_comb_MM_N"             :    inputs.nbins,   
    "mlphiggsvsbkg_125_comb_ML"             :    inputs.nbins,
    "MLPproduct_2jets"				:inputs.nbins,  
    "MLPproduct_P2jets"				:inputs.nbins,       
    }

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

sumSMMC = {}
sumNSMMC = {}
sumDATA = {}
nevts = {}
rdh = {}


w2=1
w2c=1
w2_u=1
w2_d=1
w1_z=1
w2_uc=1
w2_dc=1
for channel in channels :
    print "channel ... ", channel
    
    if channel=="MuMuChannel":w1_z=wz_m
    if channel=="EEChannel":w1_z=wz_e  
      
    if doZpTReweighting:  
      if channel=="MuMuChannel":w2_u=wzbb_m_u
      if channel=="EEChannel":w2_u=wzbb_e_u
      if channel=="MuMuChannel":w2_d=wzbb_m_d
      if channel=="EEChannel":w2_d=wzbb_e_d    
      if channel=="MuMuChannel":w2_uc=wzbb_m_uc
      if channel=="EEChannel":w2_uc=wzbb_e_uc 
      if channel=="MuMuChannel":w2_dc=wzbb_m_dc
      if channel=="EEChannel":w2_dc=wzbb_e_dc 
      
    else:
      if channel=="MuMuChannel":w2=wzbb_m
      if channel=="EEChannel":w2=wzbb_e
      if channel=="MuMuChannel":w2c=wzbb_mc
      if channel=="EEChannel":w2c=wzbb_ec    
      if channel=="MuMuChannel":w1_z=wz_m
      if channel=="EEChannel":w1_z=wz_e
      if channel=="MuMuChannel":w1t_z=wzt_m
      if channel=="EEChannel":w1t_z=wzt_e    
          
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
	        if sample == "Zc" :myRDS_red.addColumn(w2c)        
         	if sample == "Zl" :myRDS_red.addColumn(w1_z)
        	if sample == "TT" :myRDS_red.addColumn(w1t_z)	
		if sample != "Zb" and sample != "TT" and sample !="ZbPtZUp" and sample !="ZcPtZUp" and sample !="ZcPtZDown"and sample != "Zc" and sample != "Zl"and sample != "ZbPtZDown":myRDS_red.addColumn(w1)
		if doZpTReweighting:
		  if sample == "ZbPtZUp" : myRDS_red.addColumn(w2_u)
		  if sample == "ZcPtZUp" : myRDS_red.addColumn(w2_uc)
		  if sample == "ZbPtZDown" : myRDS_red.addColumn(w2_d)
		  if sample == "ZcPtZDown" : myRDS_red.addColumn(w2_dc)		
                
            if sample != "DATA":# myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w")
                if sample == "Zb": myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w2")
                if sample == "Zc": myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w2c")     
                if sample == "Zl" :myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w1_z")
                if sample == "TT" :myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w1t_z")	
                if sample != "Zb" and sample != "TT" and sample !="ZbPtZUp"and sample !="ZcPtZUp"and sample !="ZcPtZDown" and sample != "Zc" and sample != "Zl"and sample != "ZbPtZDown":myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w1")
		if doZpTReweighting:               
		  if sample == "ZbPtZUp" : myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w2_u")
		  if sample == "ZcPtZUp" : myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w2_uc")
		  if sample == "ZbPtZDown" : myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w2_d")
		  if sample == "ZcPtZDown" : myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w2_dc")		


            else               : myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get())

            nevts["pure"+sample+channel+cut]     = myRDS_red_w.numEntries()
            if sample in MCsampleList :
                nevts["effective"+sample+channel+cut]= myRDS_red_w.numEntries()*(lumi["DATA"+channel]/lumi[sample+channel])
                nevts["weighted"+sample+channel+cut] = myRDS_red_w.sumEntries()*(lumi["DATA"+channel]/lumi[sample+channel])
            
            if sample in SMMCsampleList :
                if sample==SMMCsampleList[0]:
                    sumSMMC["pure"+channel+cut]     = 0
                    sumSMMC["effective"+channel+cut]= 0
                    sumSMMC["weighted"+channel+cut] = 0
                sumSMMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumSMMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(lumi["DATA"+channel]/lumi[sample+channel])
                sumSMMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(lumi["DATA"+channel]/lumi[sample+channel])
            if sample in NSMMCsampleList :
                if sample==NSMMCsampleList[0]:
                    sumNSMMC["pure"+channel+cut]     = 0
                    sumNSMMC["effective"+channel+cut]= 0
                    sumNSMMC["weighted"+channel+cut] = 0
                sumNSMMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumNSMMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(lumi["DATA"+channel]/lumi[sample+channel])
                sumNSMMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(lumi["DATA"+channel]/lumi[sample+channel])
            if sample=="DATA":
                sumDATA[channel+cut]=myRDS_red_w.numEntries()
            for name in namePlotList:
                if channel=="EEChannel" and (name.find("Mu")>-1 or name.find("mumu")>-1) : continue
                if channel=="MuMuChannel" and (name.find("Ele")>-1 or name.find("elel")>-1) : continue	
		
		m1=name.replace("mlphiggsvsbkg_","")
		#mass=m1.replace("_comb_P2jets_ML","")
		if inputs.category=="P2bin":
		  mass=m1.replace("_comb_P2jets_ML","")
		elif  inputs.category=="2bin":
		  mass=m1.replace("_comb_2jets_ML","")
		elif inputs.category=="Both":
		  mass=m1.replace("_comb_ML","")
		else:
		  print "Unknown category:", inputs.category, " exit"
		  exit()
		#mass="125"
		samp=sample
		if sample == "DATA" : samp="data_obs"
		if "ZH" in sample : samp = sample.replace("ZH","signal")
                if not "ZH" in sample and sample != "ZbPtZUp" and sample != "ZbPtZDown"and sample != "ZcPtZUp" and sample != "ZcPtZDown": samp=samp+mass
		th1[channel+sample+name+cut] = TH1D(name+samp,name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                myRDS_red_w.fillHistogram(th1[channel+sample+name+cut], RooArgList(var[name]))
		
		rdh[channel+sample+name+cut] = RooDataHist("rdh_"+channel+sample+name+cut, "rdh_"+channel+sample+name+cut,
                                      RooArgSet(var[name]),myRDS_red)
		
		if not "Up" in sample :	
		    if not "Down" in sample :	      
		        for bin in range(0,var[name].getBins()):
			    templatenumber=var[name].getBins() - bin
                            binras = rdh[channel+sample+name+cut].get(bin)
                            a, b = Double(1), Double(1)
                            rdh[channel+sample+name+cut].weightError(a,b)
                            aw = rdh[channel+sample+name+cut].weight()
		            #print "factor",a,b , "nbr entries= ",aw 
                            if aw>0 : a=a/aw
                            if aw>0 : b=b/aw
                            th1[channel+sample+name+cut+"stat"+str(templatenumber)+"Up"]= TH1D(name+samp+"_"+samp+"stat_"+channel+inputs.category+str(templatenumber)+"Up",name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                            myRDS_red_w.fillHistogram(th1[channel+sample+name+cut+"stat"+str(templatenumber)+"Up"], RooArgList(var[name]))
                            th1[channel+sample+name+cut+"stat"+str(templatenumber)+"Down"]= TH1D(name+samp+"_"+samp+"stat_"+channel+inputs.category+str(templatenumber)+"Down",name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                            myRDS_red_w.fillHistogram(th1[channel+sample+name+cut+"stat"+str(templatenumber)+"Down"], RooArgList(var[name]))
                            tmp = th1[channel+sample+name+cut+"stat"+str(templatenumber)+"Up"].GetBinContent(bin+1)
                            if aw>0 :
		                th1[channel+sample+name+cut+"stat"+str(templatenumber)+"Up"].SetBinContent(bin+1,tmp*(1.+b))
                                th1[channel+sample+name+cut+"stat"+str(templatenumber)+"Down"].SetBinContent(bin+1,tmp*(1.-a))
		            else :
			        th1[channel+sample+name+cut+"stat"+str(templatenumber)+"Up"].SetBinContent(bin+1,tmp+b)	    
		            #print "bin", templatenumber ,"--- nominal =",tmp," --- variation Up =",b, th1[channel+sample+name+cut+"stat"+str(templatenumber)+"Up"].GetBinContent(templatenumber)," --- variation Down =",a, th1[channel+sample+name+cut+"stat"+str(templatenumber)+"Down"].GetBinContent(templatenumber)
		
            
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
file["Out"]=TFile("CSV_CLS/histoStage"+WP+"extraCuts"+inputs.category+name_ext+".root","RECREATE")
#her you could choose the root ouput filenames
for channel in channels:
    if channel=="Combined" : continue
    chDir=file["Out"].mkdir(channel,channel)
    file["Out"].cd(channel)
    for sample in totsampleList:
    #file[sample]=TFile("CSV_CLS/histoStage"+WP+"extraCuts"+sample+".root","RECREATE")
        #for cut in extraCuts:
        #    chDir.mkdir(stringCut[cut],stringCut[cut])  
        for name in namePlotList:
            if channel=="EEChannel" and (name.find("Mu")>-1 or name.find("mumu")>-1) : continue
            if channel=="MuMuChannel" and (name.find("Ele")>-1 or name.find("elel")>-1) : continue
            if not sample == "DATA" : th1[channel+sample+name+cut].Scale(lumi["DATA"+channel]/lumi[sample+channel])
            th1[channel+sample+name+cut].Write()
	    #if not sample == "DATA" : th1[channel+sample+name+cut].Write()
	    Nbin=th1[channel+sample+name+cut].GetNbinsX();
            if sample !="ZbPtZUp" and sample !="ZbPtZDown" and sample !="ZcPtZUp" and sample !="ZcPtZDown":
	        for bin in range(1,Nbin+1):
                    if not sample == "DATA":th1[channel+sample+name+cut+"stat"+str(bin)+"Down"].Scale(lumi["DATA"+channel]/lumi[sample+channel])
                    if not sample == "DATA":th1[channel+sample+name+cut+"stat"+str(bin)+"Down"].Write()
                    if not sample == "DATA":th1[channel+sample+name+cut+"stat"+str(bin)+"Up"].Scale(lumi["DATA"+channel]/lumi[sample+channel])
                    if not sample == "DATA":th1[channel+sample+name+cut+"stat"+str(bin)+"Up"].Write()

    for sample in totsampleList:
        for name in namePlotList:
	    if sample == "DATA":
	        th1[channel+"DATA"+name+cut].Scale(0)
	    	for sampl in totsampleList:
		    if sampl !="ZbPtZUp" and sampl !="ZbPtZDown" and sampl !="DATA"and sampl !="ZH125"and sampl !="ZH120"and sampl !="ZH115"and sampl !="ZH130"and sampl !="ZH135":
		        th1[channel+"DATA"+name+cut].Add(th1[channel+sampl+name+cut])
	        #th1[channel+"DATA"+name+cut].Write()
	    
file["Out"].Close()

