CSVWP="MM"#type MM or ML
class inputs:

  inputprefolder="/home/fynu/vizangarciaj/storage/RDS/CSVSel2011JER0/"
  suffix = "_mbbCR"
  #inputfolder ="RDS20130515V1/"
  #inputfolder ="RDS20130521PTj1_40_PTj2_25_V1/"
  #inputfolder ="RDS20130522PTj1_40_PTj2_25_V2Camille/"
  
  #inputfolder ="RDS20130611PTj1_40_PTj2_25_V4noCSVProd/"
  nbins=17
  
  if CSVWP=="MM":
    wp=18
    sf_tt_2jet=1.00467
    sf_zbb_2jet=1.09852
    sf_zbx_2jet=1.28849
    sf_zxx_2jet=0.870528

    sf_tt_P2jet=1.00467
    sf_zbb_P2jet=1.28849
    sf_zbx_P2jet=1.28849
    sf_zxx_P2jet=0.870528
    inputfolder="RDS20130611PTj1_40_PTj2_25_V3noCSVProd/"
    
  elif CSVWP=="ML":
    wp=17
    sf_tt_2jet=0.89821
    sf_zbb_2jet=0.979895
    sf_zbx_2jet=1.14435
    sf_zxx_2jet=0.867991

    sf_tt_P2jet=0.89821
    sf_zbb_P2jet=1.14435
    sf_zbx_P2jet=1.14435
    sf_zxx_P2jet=0.867991
    inputfolder ="RDS20130522PTj1_40_PTj2_25_V2Camille/"
    
  
  category = "2bin" # choose between P2bin and 2bin
  
  ptj1min=40
  ptj2min=25
  ptzmin=20
  mbbmin_2jet=80
  mbbmax_2jet=150
  mbbmin_P2jet=50
  mbbmax_P2jet=150
  
  
#  sf_tt_2jet=0.655227
#  sf_zbb_2jet=0.912631
#  sf_zbx_2jet=1.3
#  sf_zxx_2jet=1.26556
#
#  sf_tt_P2jet=0.481284
#  sf_zbb_P2jet=1.25028
#  sf_zbx_P2jet=1.30236
#  sf_zxx_P2jet=0.70557

