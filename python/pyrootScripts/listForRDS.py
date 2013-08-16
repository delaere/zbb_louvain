
L_DY = "10325.26"
DYrew = {
    "50-70"   : "("+L_DY+"/(40626.58+"+L_DY+"))",
    "70-100"  : "("+L_DY+"/(27019.59+"+L_DY+"))",
    "100-180" : "("+L_DY+"/(78068.53+"+L_DY+"))",
    "180"     : "("+L_DY+"/(78068.53+341113.16+"+L_DY+"))",
    "1j"      : "("+L_DY+"/(41506.68+"+L_DY+"))",
    "2j"      : "("+L_DY+"/(119183.18+"+L_DY+"))",
    "3j"      : "("+L_DY+"/(203041.98+"+L_DY+"))",
    "4j"      : "("+L_DY+"/(277900.48+"+L_DY+"))",
    }

MuCorrFact = 1.0
Extra_norm={ "MuMuChannelDATA"  : 1.0,
             "EEChannelDATA"    : 1.0,
             "MuMuChannelTT"    : 1.0,#(2984./4412.)/MuCorrFact,
             "EEChannelTT"      : 1.0,
             "MuMuChannelTT-FullLept"    : (15000./62506.)/MuCorrFact,
             "EEChannelTT-FullLept"      : 15000./46492.,
	     "MuMuChannelZbb_Zbb"    : (20000./111784.)/MuCorrFact,
             "EEChannelZbb_Zbb"      : 20000./80672.,
	     "MuMuChannelZbb"    : 1.0/MuCorrFact,
             "EEChannelZbb"      : 1.0,
	     "MuMuChannelZbx"    : 1.0/MuCorrFact,
             "EEChannelZbx"      : 1.0,
	     "MuMuChannelZxx"    : 1.0/MuCorrFact,
             "EEChannelZxx"      : 1.0,
	     "MuMuChannelZno"    : 1.0/MuCorrFact,
             "EEChannelZno"      : 1.0,
	     "MuMuChannelZZ"    : (10000./16986.)/MuCorrFact,
             "EEChannelZZ"      : 10000./11936.,
	     "MuMuChannelZH125" : (10000./65412.)/MuCorrFact,
             "EEChannelZH125"   : 10000./48726.,

	     "MuMuChannelZH110" : (10000./58765.)/MuCorrFact,
             "EEChannelZH110"   : 10000./42745.,
	     "MuMuChannelZH115" : (10000./368736.)/MuCorrFact,
             "EEChannelZH115"   : 10000./44633.,
	     "MuMuChannelZH120" : (10000./63643.)/MuCorrFact,
             "EEChannelZH120"   : 10000./46265.,
	     "MuMuChannelZH130" : (10000./68489.)/MuCorrFact,
             "EEChannelZH130"   : 10000./50189.,
	     "MuMuChannelZH135" : (10000./69881.)/MuCorrFact,
             "EEChannelZH135"   : 10000./51567.,
	     "MuMuChannelZH140" : (10000./70994.)/MuCorrFact,
             "EEChannelZH140"   : 10000./52219.,
	     "MuMuChannelZH145" : (10000./73747.)/MuCorrFact,
             "EEChannelZH145"   : 10000./54375.,
	     "MuMuChannelZH150" : (10000./75391.)/MuCorrFact,
             "EEChannelZH150"   : 10000./56013.,

             "MuMuChannelDY50-70" : 4000./6517.,
             "EEChannelDY50-70" : 4000./4615.,
             "MuMuChannelDY70-100" : 2000./3242.,
             "EEChannelDY70-100" : 2000./2304.,
             "MuMuChannelDY100" : 5000./9040,
             "EEChannelDY100" : 5000./6789.,
             "MuMuChannelDY180" : 5000./7281.,
             "EEChannelDY180" : 5000./5648.,
             "MuMuChannelDY1j" : 5000./8655.,
             "EEChannelDY1j" : 5000./5942.,
             "MuMuChannelDY2j" : 15000./38485.,
             "EEChannelDY2j" : 15000./27727.,
             "MuMuChannelDY3j" : 15000./39129.,
             "EEChannelDY3j" : 15000./28325.,
             "MuMuChannelDY4j" : 25000./43536.,
             "EEChannelDY4j" : 25000./32339.,
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
          "MuMuChannelZno"    : 0.94,
          "EEChannelZno"      : 0.94,
          "MuMuChannelZZ"    : 1.0,
          "EEChannelZZ"      : 1.0,
          "MuMuChannelZH125" : 1.0,
          "EEChannelZH125"   : 1.0,
          }

PlotForCLs = [
    "mlphiggsvsbkg_125_comb_MM_N_2011",

    "mlphiggsvsbkg_125_comb_MM_N",

    "SumNN",
    "ProdNN",
    "SumWeightedNN",

    "newmlphiggsvszbb_125_comb_MM_N",
    "newmlphiggsvszz_125_comb_MM_N",
    "newmlphiggsvstt_125_comb_MM_N",
    "newmlphiggsvsbkg_125_comb_MM_N",

    "mlphiggsvsbkg_125_comb_MM_N_1_10000",
    "mlphiggsvsbkg_125_comb_MM_N_1_5000",
    "mlphiggsvsbkg_125_comb_MM_N_2_10000",
    "mlphiggsvsbkg_125_comb_MM_N_2_5000",
    "mlphiggsvsbkg_125_comb_MM_N_3_5000",
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_10000",
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_5000",
    "mlphiggsvsbkg_125_comb_MM_N_2_4_10000",
    "mlphiggsvsbkg_125_comb_MM_N_2_5_3_1_1000",
    "mlphiggsvsbkg_125_comb_MM_N_3_2_10000",
    ]

blindList = [
    "mlphiggsvstt_125_comb_MM_N_2011",
    "mlphiggsvszz_125_comb_MM_N_2011",
    "mlphiggsvszbb_125_comb_MM_N_2011",
    "mlphiggsvsbkg_125_comb_MM_N_2011",

    "mlphiggsvszbb_125_comb_MM_N",
    "mlphiggsvszz_125_comb_MM_N",
    "mlphiggsvstt_125_comb_MM_N",
    "mlphiggsvsbkg_125_comb_MM_N",

    "SumNN",
    "ProdNN",
    "SumWeightedNN",
    
 
    "newmlphiggsvszbb_125_comb_MM_N",
    "newmlphiggsvstt_125_comb_MM_N",
    "newmlphiggsvszz_125_comb_MM_N",
    "newmlphiggsvsbkg_125_comb_MM_N",

    "mlphiggsvsbkg_125_comb_MM_N_1_10000",
    "mlphiggsvsbkg_125_comb_MM_N_1_5000",
    "mlphiggsvsbkg_125_comb_MM_N_2_10000",
    "mlphiggsvsbkg_125_comb_MM_N_2_5000",
    "mlphiggsvsbkg_125_comb_MM_N_3_5000",
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_10000",
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_5000",
    "mlphiggsvsbkg_125_comb_MM_N_2_4_10000",
    "mlphiggsvsbkg_125_comb_MM_N_2_5_3_1_1000",
    "mlphiggsvsbkg_125_comb_MM_N_3_2_10000",    
    ]

namePlotList = [
     "eventSelectionbestzmassMu"  , 
     "eventSelectionbestzmassEle" ,
     "eventSelectionbestzptMu"    ,    
     "eventSelectionbestzptEle"   ,
     "jetmetbjet1pt"              ,   
     "jetmetbjet2pt"              ,   
     "jetmetbjet1CSVdisc"         ,   
     "jetmetbjet2CSVdisc"         ,
     "jetmetbjet1JPdisc"         ,
     "jetmetbjet2JPdisc"         ,
     "jetmetbjet1SSVHEdisc"         ,
     "jetmetbjet2SSVHEdisc"         ,
     "jetmetMET"                  ,
     "jetmetMETsignificance"      ,
     "eventSelectiondphiZbb"      ,
##     "eventSelectiondphiZbj1"     , 
     "eventSelectiondijetPt"      ,
     "eventSelectiondijetM"       ,
     "eventSelectiondijetdR"      ,
##  #   "eventSelectiondijetSVdR"    ,
##     "eventSelectionZbbM"         ,
     "eventSelectiondrllMu"       ,
     "eventSelectiondrllEle"      ,
##     "eventSelectionZbM"          ,
     "jetmetnj"                   ,
     "vertexAssociationnvertices" ,
     "jetmetbjet1beta" ,
     "jetmetbjet1betaStar" ,
     "jetmetbjet2beta" ,
     "jetmetbjet2betaStar",

     "mcSelectionnJets",
     "mcSelectionnbJets",
     "mcSelectionncJets",
     "mcSelectionllpt",
     ]

namePlotListOnMC = [
    "mcSelectionnJets",
    "mcSelectionnbJets",
    "mcSelectionncJets",
    "mcSelectionllpt",
    ]


namePlotListOnMerged = [
     "jetmetbjetMinCSVdisc"   ,   
     "jetmetbjetMaxCSVdisc"   ,
     "jetmetbjetProdCSVdisc"  ,   
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
     ,"mlphiggsvsbkg_125_comb_MM_N_2011"
     ,"mlphiggsvszbb_125_comb_MM_N_2011"
     ,"mlphiggsvszz_125_comb_MM_N_2011"
     ,"mlphiggsvstt_125_comb_MM_N_2011"
     ,"mlphiggsvsbkg_125_comb_MM_N"
     ,"mlphiggsvszbb_125_comb_MM_N"
     ,"mlphiggsvszz_125_comb_MM_N"
     ,"mlphiggsvstt_125_comb_MM_N"
     ,"newmlphiggsvsbkg_125_comb_MM_N"
     ,"newmlphiggsvszbb_125_comb_MM_N"
     ,"newmlphiggsvszz_125_comb_MM_N"
     ,"newmlphiggsvstt_125_comb_MM_N"
     ,"SumNN"
     ,"ProdNN"
     ,"SumWeightedNN",
    "mlphiggsvsbkg_125_comb_MM_N_1_10000",
    "mlphiggsvsbkg_125_comb_MM_N_1_5000",
    "mlphiggsvsbkg_125_comb_MM_N_2_10000",
    "mlphiggsvsbkg_125_comb_MM_N_2_5000",
    "mlphiggsvsbkg_125_comb_MM_N_3_5000",
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_10000",
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_5000",
    "mlphiggsvsbkg_125_comb_MM_N_2_4_10000",
    "mlphiggsvsbkg_125_comb_MM_N_2_5_3_1_1000",
    "mlphiggsvsbkg_125_comb_MM_N_3_2_10000",

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
    "jetmetbjet1CSVdisc"        :    0.679 ,
    "jetmetbjet2CSVdisc"        :    0.679 ,   
    "jetmetbjet1JPdisc"        :    0. ,
    "jetmetbjet2JPdisc"        :    0. ,
    "jetmetbjet1SSVHEdisc"        :    0. ,
    "jetmetbjet2SSVHEdisc"        :    0. , 
    "jetmetbjetMinCSVdisc"      :    0.679 ,
    "jetmetbjetMaxCSVdisc"      :    0.679 ,
    "jetmetbjetProdCSVdisc"     :    0.679*0.679 ,
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
    "jetmetjet1SSVHPdisc"       :    0 ,
    "jetmetjet1SVmass"          :    0 ,
    "eventSelectiondrllMu"      :    0 ,
    "eventSelectiondrllEle"     :    0 
    ,"jetmetnj" : 2
    ,"vertexAssociationnvertices" : -0.5
    ,"jetmetbjet1beta" : -1
    ,"jetmetbjet1betaStar" : -1
    ,"jetmetbjet2beta" : -1
    ,"jetmetbjet2betaStar" : -1
    
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
    ,"newmlphiggsvsbkg_125_comb_MM_N" : 0
    ,"newmlphiggsvszbb_125_comb_MM_N" : 0
    ,"newmlphiggsvstt_125_comb_MM_N" : 0
    ,"newmlphiggsvszz_125_comb_MM_N" : 0
    ,"SumNN" : 0
    ,"ProdNN" : 0
    ,"SumWeightedNN" : 0,
    "mlphiggsvsbkg_125_comb_MM_N_1_10000" : 0,
    "mlphiggsvsbkg_125_comb_MM_N_1_5000" : 0,
    "mlphiggsvsbkg_125_comb_MM_N_2_10000" : 0,
    "mlphiggsvsbkg_125_comb_MM_N_2_5000" : 0,
    "mlphiggsvsbkg_125_comb_MM_N_3_5000" : 0,
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_10000" : 0,
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_5000" : 0,
    "mlphiggsvsbkg_125_comb_MM_N_2_4_10000" : 0,
    "mlphiggsvsbkg_125_comb_MM_N_2_5_3_1_1000" : 0,
    "mlphiggsvsbkg_125_comb_MM_N_3_2_10000" : 0,

    "mcSelectionnJets" : -0.5,
    "mcSelectionnbJets" : -0.5,
    "mcSelectionncJets" : -0.5,
    "mcSelectionllpt" : 0,
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
    "jetmetbjet1JPdisc"             :  2.5 ,
    "jetmetbjet2JPdisc"             :  2.5 ,   
    "jetmetbjet1SSVHEdisc"             :  10 ,
    "jetmetbjet2SSVHEdisc"             :  10 ,   
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
    "jetmetjet1SSVHPdisc"       :    8 ,
    "jetmetjet1SVmass"          :    5 ,
    "eventSelectiondrllMu"      :    5 ,
    "eventSelectiondrllEle"      :    5 
    ,"jetmetnj" :  8
    ,"vertexAssociationnvertices" : 59.5
    ,"jetmetbjet1beta" : 1
    ,"jetmetbjet1betaStar" : 1
    ,"jetmetbjet2beta" : 1
    ,"jetmetbjet2betaStar" : 1
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
    ,"newmlphiggsvsbkg_125_comb_MM_N" : 1
    ,"newmlphiggsvszbb_125_comb_MM_N" : 1
    ,"newmlphiggsvstt_125_comb_MM_N" : 1
    ,"newmlphiggsvszz_125_comb_MM_N" : 1
    ,"SumNN" : 1
    ,"ProdNN" : 1
    ,"SumWeightedNN" : 1,
    "mlphiggsvsbkg_125_comb_MM_N_1_10000" : 1,
    "mlphiggsvsbkg_125_comb_MM_N_1_5000" : 1,
    "mlphiggsvsbkg_125_comb_MM_N_2_10000" : 1,
    "mlphiggsvsbkg_125_comb_MM_N_2_5000" : 1,
    "mlphiggsvsbkg_125_comb_MM_N_3_5000" : 1,
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_10000" : 1,
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_5000" : 1,
    "mlphiggsvsbkg_125_comb_MM_N_2_4_10000" : 1,
    "mlphiggsvsbkg_125_comb_MM_N_2_5_3_1_1000" : 1,
    "mlphiggsvsbkg_125_comb_MM_N_3_2_10000" : 1,

    "mcSelectionnJets" : 9.5,
    "mcSelectionnbJets" : 9.5,
    "mcSelectionncJets" : 9.5,
    "mcSelectionllpt" : 500,
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
    "jetmetbjet1JPdisc"             :  20  ,
    "jetmetbjet2JPdisc"             :  20  ,
    "jetmetbjet1SSVHEdisc"             :  60  , 
   "jetmetbjet2SSVHEdisc"             :  60  ,
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
    "jetmetjet1SSVHPdisc"       :   16 ,
    "jetmetjet1SVmass"          :   20 , #0.25GeV
    "eventSelectiondrllMu"      :   10 , #0.5
    "eventSelectiondrllEle"      :   10
    ,"jetmetnj" : 6
    ,"vertexAssociationnvertices" : 60
    ,"jetmetbjet1beta" : 20
    ,"jetmetbjet1betaStar" : 20
    ,"jetmetbjet2beta" : 20
    ,"jetmetbjet2betaStar" : 20
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
    ,"newmlphiggsvsbkg_125_comb_MM_N" : 20
    ,"newmlphiggsvszbb_125_comb_MM_N" : 20
    ,"newmlphiggsvstt_125_comb_MM_N" : 20
    ,"newmlphiggsvszz_125_comb_MM_N" : 20
    ,"SumNN" : 20
    ,"ProdNN" : 20
    ,"SumWeightedNN" : 20,
    "mlphiggsvsbkg_125_comb_MM_N_1_10000" : 20,
    "mlphiggsvsbkg_125_comb_MM_N_1_5000" : 20,
    "mlphiggsvsbkg_125_comb_MM_N_2_10000" : 20,
    "mlphiggsvsbkg_125_comb_MM_N_2_5000" : 20,
    "mlphiggsvsbkg_125_comb_MM_N_3_5000" : 20,
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_10000" : 20,
    "mlphiggsvsbkg_125_comb_MM_N_2_3_2_5000" : 20,
    "mlphiggsvsbkg_125_comb_MM_N_2_4_10000" : 20,
    "mlphiggsvsbkg_125_comb_MM_N_2_5_3_1_1000" : 20,
    "mlphiggsvsbkg_125_comb_MM_N_3_2_10000" : 20,

    "mcSelectionnJets"  : 10,
    "mcSelectionnbJets" : 10,
    "mcSelectionncJets" : 10,
    "mcSelectionllpt" : 25,
    }
    
