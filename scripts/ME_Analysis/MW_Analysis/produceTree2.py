
import os

list=["DoubleEle_DataA", "DoubleEle_DataA06aug", "DoubleEle_DataB", "DoubleEle_DataC-v1","DoubleEle_DataC-v2", "DoubleEle_DataD","DoubleMu_DataA", "DoubleMu_DataA06aug", "DoubleMu_DataB", "DoubleMu_DataC-v1", "DoubleMu_DataC-v2", "DoubleMu_DataD", "DY_Mu_MC", "DY_El_MC", "TT_Mu_MC", "TT_El_MC", "ZZ_Mu_MC", "ZZ_El_MC", "ZH125_Mu_MC", "ZH125_El_MC"]
doIt={
    "DoubleEle_DataA" : False,
    "DoubleEle_DataA06aug" : False,
    "DoubleEle_DataB" : False,
    "DoubleEle_DataC-v1" : False,
    "DoubleEle_DataC-v2" : False,
    "DoubleEle_DataD" : False,
    "DoubleMu_DataA" : False,
    "DoubleMu_DataA06aug" : False,
    "DoubleMu_DataB" : False,
    "DoubleMu_DataC-v1" : False,
    "DoubleMu_DataC-v2" : False,
    "DoubleMu_DataD" : False,
    "DY_Mu_MC" : True,
    "DY_El_MC" : True,
    "TT_Mu_MC" : True,
    "TT_El_MC" : True,
    "ZZ_Mu_MC" : True,
    "ZZ_El_MC" : True,
    "ZH125_Mu_MC" : True,
    "ZH125_El_MC" : True
    }

channel={
    "DoubleEle_DataA" : "ee", 
    "DoubleEle_DataA06aug" : "ee",
    "DoubleEle_DataB" : "ee", 
    "DoubleEle_DataC-v1" : "ee",
    "DoubleEle_DataC-v2" : "ee", 
    "DoubleEle_DataD" : "ee",
    "DoubleMu_DataA" : "mumu",
    "DoubleMu_DataA06aug" : "mumu",
    "DoubleMu_DataB" : "mumu",
    "DoubleMu_DataC-v1" : "mumu",
    "DoubleMu_DataC-v2" : "mumu",
    "DoubleMu_DataD" : "mumu",
    "DY_Mu_MC" : "mumu",
    "DY_El_MC" : "ee",
    "TT_Mu_MC" : "mumu",
    "TT_El_MC" : "ee",
    "ZZ_Mu_MC" : "mumu",
    "ZZ_El_MC" : "ee",
    "ZH125_Mu_MC" : "mumu",
    "ZH125_El_MC" : "ee"
    }

out={
    "DoubleEle_DataA" : "DoubleDataA_537", 
    "DoubleEle_DataA06aug" : "DoubleDataA06aug_537",
    "DoubleEle_DataB" : "DoubleDataB_537", 
    "DoubleEle_DataC-v1" : "DoubleDataC-v1",
    "DoubleEle_DataC-v2" : "DoubleDataC-v2_537", 
    "DoubleEle_DataD" : "DoubleDataD_537",
    "DoubleMu_DataA" : "DoubleDataA_537",
    "DoubleMu_DataA06aug" : "DoubleData06aug_537",
    "DoubleMu_DataB" : "DoubleDataB_537",
    "DoubleMu_DataC-v1" : "DoubleDataC-v1",
    "DoubleMu_DataC-v2" : "DoubleDataC-v2_537",
    "DoubleMu_DataD" : "DoubleDataD_537",
    "DY_Mu_MC" : "DY_537",
    "DY_El_MC" : "DY_537",
    "TT_Mu_MC" : "ttbar_537",
    "TT_El_MC" : "ttbar_537",
    "ZZ_Mu_MC" : "ZZ_537",
    "ZZ_El_MC" : "ZZ_537",
    "ZH125_Mu_MC" : "ZH125_537",
    "ZH125_El_MC" : "ZH125_537"
    }

nevts={
    "DoubleEle_DataA" : 923,
    "DoubleEle_DataA06aug" : 100,
    "DoubleEle_DataB" : 5199,
    "DoubleEle_DataC-v1" : 586,
    "DoubleEle_DataC-v2" : 7751,
    "DoubleEle_DataD" : 9722,
    "DoubleMu_DataA" : 1145,
    "DoubleMu_DataA06aug" : 130,
    "DoubleMu_DataB" : 7441,
    "DoubleMu_DataC-v1" : 837,
    "DoubleMu_DataC-v2" : 10905,
    "DoubleMu_DataD" : 13736,
    "DY_Mu_MC" : 11876,
    "DY_El_MC" : 8205,
    "TT_Mu_MC" : 4308,
    "TT_El_MC" : 3128,
    "ZZ_Mu_MC" : 10000,
    "ZZ_El_MC" : 10000,
    "ZH125_Mu_MC" : 10000,
    "ZH125_El_MC" : 10000
    }


for s in list :
    if not doIt[s] : continue
    isEl=1
    if channel[s]=="ee" : isEl=0
    isDY=0
    if s=="DY_Mu_MC" or s=="DY_El_MC" : isDY=1
    #os.system('./Combination_'+channel[s]+'_CSV_2012.sh '+out[s]+'_'+channel[s]+' outCMStoLHCO'+s+'_CSV2012Sel_V2_0_LHCO.root outCMStoLHCO'+s+'_CSV2012Sel_V2_0.root '+str(nevts[s])+' '+str(isDY)+' '+str(isEl))
    os.system('./Combination_'+channel[s]+'_CSV_2012.sh '+out[s]+'_'+channel[s]+' outCMStoLHCO'+s+'V3_0_LHCO.root outCMStoLHCO'+s+'V3_0.root '+str(nevts[s])+' '+str(isDY)+' '+str(isEl))
    os.system('mv '+out[s]+'_'+channel[s]+'.root ME_zbb_'+s+'_537.root')
    os.system('cp ME_zbb_'+s+'_537.root /nfs/user/acaudron/Tree2_537/ME_zbb_'+s+'.root')
