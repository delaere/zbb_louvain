

dataPeriods = [
    "A",
    "A06aug",
    "B",
    "C-v1",
    "C-v2",
    "D",
    ]

sampleList = [
    "DATA",
    #"TT",
    "TT-FullLept",
    "ZZ",
    "DY",
    "ZH125"
    ]#,"ZH120","ZH115","ZH130","ZH135"]

totsampleList  = [
    "DATA",
    #"TT",
    "TT-FullLept",
    "ZZ",
    "Zbb",
    "Zbx",
    "Zxx",
    "ZH125"
    ]#,"ZH120","ZH115","ZH130","ZH135"]#,"ZA"]

sigMCsampleList= ["ZH125"]#,"ZH120","ZH115","ZH130","ZH135"]#,"ZA"]
MCsampleList=[]
bkgMCsampleList=[]

for sample in totsampleList :
    if sample=="DATA" : continue
    MCsampleList.append(sample)
    if not sample in sigMCsampleList : bkgMCsampleList.append(sample)

from zbbCommons import zbbnorm
nev_DYjets_summer12=29310189 # to be used on events produced in 532p4
lumi = { "DATA"   : zbbnorm.lumi_tot2012,
         "TT"     : zbbnorm.nev_TTjets_summer12/zbbnorm.xsec_TTjets_8TeV/1000.,
         "TT-FullLept" : zbbnorm.nev_TTFullLept_summer12/zbbnorm.xsec_TTFullLept_8TeV/1000.,
         "Zbb"     : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "Zbx"     : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "Zxx"     : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
#         "Zbb"     : nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
#         "Zbx"     : nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
#         "Zxx"     : nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "ZZ"     : zbbnorm.nev_ZZ_summer12/zbbnorm.xsec_ZZ_8TeV/1000.,
         "ZH110"  : zbbnorm.nev_ZH110_summer12/zbbnorm.xsec_ZH110_8TeV/1000.,
         "ZH115"  : zbbnorm.nev_ZH115_summer12/zbbnorm.xsec_ZH115_8TeV/1000.,
         "ZH120"  : zbbnorm.nev_ZH120_summer12/zbbnorm.xsec_ZH120_8TeV/1000.,
         "ZH125"  : zbbnorm.nev_ZH125_summer12/zbbnorm.xsec_ZH125_8TeV/1000.,
         "ZH130"  : zbbnorm.nev_ZH130_summer12/zbbnorm.xsec_ZH130_8TeV/1000.,
         "ZH135"  : zbbnorm.nev_ZH135_summer12/zbbnorm.xsec_ZH135_8TeV/1000.
         }


MuCorrFact = 1.0
Extra_norm={ "MuMuChannelDATA"  : 1.0,
             "EEChannelDATA"    : 1.0,
             "MuMuChannelTT"    : 1.0,#(2984./4412.)/MuCorrFact,
             "EEChannelTT"      : 1.0,
             "MuMuChannelTT-FullLept"    : (15000./62506.)/MuCorrFact,
             "EEChannelTT-FullLept"      : 15000./46492.,
	     "MuMuChannelZbb"    : 1.0/MuCorrFact,
             "EEChannelZbb"      : 1.0,
	     "MuMuChannelZbx"    : 1.0/MuCorrFact,
             "EEChannelZbx"      : 1.0,
	     "MuMuChannelZxx"    : 1.0/MuCorrFact,
             "EEChannelZxx"      : 1.0,
	     "MuMuChannelZZ"    : (10000./16986.)/MuCorrFact,
             "EEChannelZZ"      : 10000./11936.,
	     "MuMuChannelZH125" : (10000./65412.)/MuCorrFact,
             "EEChannelZH125"   : 10000./48726.,
            }

SFs_fit={ "MuMuChannelDATA"  : 1.0,
          "EEChannelDATA"    : 1.0,
          "MuMuChannelTT"    : 1.03,
          "EEChannelTT"      : 1.03,
          "MuMuChannelTT-FullLept"    : 1.03,
          "EEChannelTT-FullLept"      : 1.03,
          "MuMuChannelZbb"    : 0.86,
          "EEChannelZbb"      : 0.86,
          "MuMuChannelZbx"    : 1.93,
          "EEChannelZbx"      : 1.93,
          "MuMuChannelZxx"    : 0.94,
          "EEChannelZxx"      : 0.94,
          "MuMuChannelZZ"    : 1.0,
          "EEChannelZZ"      : 1.0,
          "MuMuChannelZH125" : 1.0,
          "EEChannelZH125"   : 1.0,
          }

PlotForCLs = [
    "mlphiggsvsbkg_125_comb_MM_N",
    #"mlphiggsvsbkg_125_comb_MM_N_2011",
    ]

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
     "jetmetMETsignificance"                  ,
     "eventSelectiondphiZbb"      ,
##     "eventSelectiondphiZbj1"     , 
     "eventSelectiondijetPt"      ,
     "eventSelectiondijetM"       ,
     "eventSelectiondijetdR"      ,
##  #   "eventSelectiondijetSVdR"    ,
##     "eventSelectionZbbM"         ,
     "eventSelectiondrllMu"       ,
     "eventSelectiondrllEle"       ,
##     "eventSelectionZbM"
     "jetmetnj",
     "Wgg"           
     ,"Wqq"           
     ,"Wtt"           
     #    ,"Wtwb"           #to be added in the merged RDS (ttbar isr=0)
     ,"Wzz3"          
     ,"Wzz0"           
     ,"Whi3_125"           
     ,"Whi0_125"
     #,"jetmetMETsignificance"
    # ,"jetmetMET"

#    ,"mlpZbbvsTT_MM"
#    ,"mlpZbbvsTT_MM_N"
#    ,"mlpZbbvsTT_ML"
#    ,"mlpZbbvsTT_mu_MM"
     ,"mlpZbbvsTT_mu_MM_N"
#    ,"mlpZbbvsTT_mu_ML"
#    ,"mlphiggsvszbb_125_MM"
#   ,"mlphiggsvstt_125_MM"
#    ,"mlphiggsvszz_125_MM"
#    ,"mlphiggsvsbkg_125_MM"
#    ,"mlphiggsvszbb_125_ML"
#    ,"mlphiggsvstt_125_ML"
#    ,"mlphiggsvszz_125_ML"
#    ,"mlphiggsvsbkg_125_ML"
#    ,"mlphiggsvszbb_125_MM_N"
#    ,"mlphiggsvstt_125_MM_N"
#    ,"mlphiggsvszz_125_MM_N"
#    ,"mlphiggsvsbkg_125_MM_N"
#    ,"mlphiggsvszbb_125_mu_MM"
#    ,"mlphiggsvstt_125_mu_MM"
#    ,"mlphiggsvszz_125_mu_MM"
#    ,"mlphiggsvsbkg_125_mu_MM"
#    ,"mlphiggsvszbb_125_mu_ML"
#    ,"mlphiggsvstt_125_mu_ML"
#    ,"mlphiggsvszz_125_mu_ML"
#    ,"mlphiggsvsbkg_125_mu_ML"
#    ,"mlphiggsvszbb_125_mu_MM_N"
#    ,"mlphiggsvstt_125_mu_MM_N"
#    ,"mlphiggsvszz_125_mu_MM_N"
#    ,"mlphiggsvsbkg_125_mu_MM_N"
#     ,"mlphiggsvsbkg_125_comb_MM_N_2011"
#     ,"mlphiggsvszbb_125_comb_MM_N_2011"
#     ,"mlphiggsvszz_125_comb_MM_N_2011"
#     ,"mlphiggsvstt_125_comb_MM_N_2011"
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
    "jetmetbjet1pt"             :    0 ,
    "jetmetbjet2pt"             :    0 ,   
    "jetmetbjet1CSVdisc"             :    0.679 ,
    "jetmetbjet2CSVdisc"             :    0.679 ,   
    "jetmetbjetMinCSVdisc"             :    0.679 ,
    "jetmetbjetMaxCSVdisc"             :    0.679 ,
    "jetmetbjetProdCSVdisc"             :    0.679*0.679 ,
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
    "eventSelectiondrllMu"      :    0 ,
    "eventSelectiondrllEle"      :    0 
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
    ,"mlphiggsvsbkg_125_comb_MM_N_2011" : 0
    ,"mlphiggsvszbb_125_comb_MM_N_2011" : 0
    ,"mlphiggsvstt_125_comb_MM_N_2011" : 0
    ,"mlphiggsvszz_125_comb_MM_N_2011" : 0
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
    "jetmetbjet1pt"             :  260 ,
    "jetmetbjet2pt"             :  260 ,   
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
    "eventSelectiondrllMu"      :    5 ,
    "eventSelectiondrllEle"      :    5 
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
    ,"mlphiggsvsbkg_125_comb_MM_N_2011" : 1
    ,"mlphiggsvszbb_125_comb_MM_N_2011" : 1
    ,"mlphiggsvstt_125_comb_MM_N_2011" : 1
    ,"mlphiggsvszz_125_comb_MM_N_2011" : 1
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
    "jetmetbjet1CSVdisc"             :  20  ,
    "jetmetbjet2CSVdisc"             :  20  ,
    "jetmetbjetMinCSVdisc"             : 20 ,
    "jetmetbjetMaxCSVdisc"             :   20 ,
    "jetmetbjetProdCSVdisc"             :  20 ,   
    "jetmetMET"                 :   20 , #10GeV 
    "eventSelectiondphiZbj1"    :   16 , #0.2
    "eventSelectiondphiZbb"     :   16 ,
    "eventSelectiondrZbb"       :   10 , #0.5
    "eventSelectionscaldptZbj1" :   50 , #10GeV
    "eventSelectiondijetM"      :   240 , #50GeV
    "eventSelectiondijetdR"     :   10 , #0.5
    "eventSelectiondijetSVdR"   :   10 ,
    "eventSelectionZbbM"        :   20 , #50GeV
    "eventSelectionZbM"         :   16 ,
    "eventSelectionZbbPt"       :   50 , #10GeV
    "jetmetjet1SSVHEdisc"       :   16 , #0.5
    "jetmetjet1SSVHPdisc"       :   16 ,
    "jetmetjet1SVmass"          :   20 , #0.25GeV
    "eventSelectiondrllMu"      :   10 , #0.5
    "eventSelectiondrllEle"      :   10
    ,"jetmetnj" : 6
    ,"Wgg"      :    20 
    ,"Wqq"      :    20 
    ,"Wtt"      :    25 
 #   ,"Wtwb"      :    24 
    ,"Wzz3"      :    16 
    ,"Wzz0"      :    20 
    ,"Whi3_125"      :    20 
    ,"Whi0_125"      :    20
    ,"jetmetMETsignificance" : 40
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
    ,"mlphiggsvsbkg_125_comb_MM_N_2011" : 20
    ,"mlphiggsvszbb_125_comb_MM_N_2011" : 20
    ,"mlphiggsvstt_125_comb_MM_N_2011" : 20
    ,"mlphiggsvszz_125_comb_MM_N_2011" : 20
    ,"mlphiggsvsbkg_125_comb_MM_N" : 20
    ,"mlphiggsvszbb_125_comb_MM_N" : 20
    ,"mlphiggsvstt_125_comb_MM_N" : 20
    ,"mlphiggsvszz_125_comb_MM_N" : 20
    }
    
