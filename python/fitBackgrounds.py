#########################################################
#                                                       #
# Script to estimate backgrounds for Z+b-jets analysis. #
#                                                       #
# Functionality:                                        #
# - Estimate ttbar background                           #
# => Using m(ll) and MW/NN output                       #
# - Estimate Z+ucdsg background                         #
# => Using m(SV)                                        #
#                                                       #
#########################################################
#                                                       #
# Working points                                        #
# - SSV-HE                                              #
# - SSV-HP                                              #
#                                                       #
# Fit dimensionalities                                  #
# - 1D                                                  #
# - 1Dx1D (sim)                                         #
# - 2D                                                  #
# - 2Dx1D (sim)                                         #
#                                                       #
# Channels                                              #
# - El                                                  #
# - Mu                                                  #
# - Sum                                                 #
#                                                       #
# PDFs                                                  #
# - Hist                                                #
# - Keys                                                #
#                                                       #
# Fits                                                  #
# - With/without errors                                 #
# - RooFit & Root                                       #
#                                                       #
# - Fractions                                           #
# - Number of events                                    #
#                                                       #
# Also: include shape uncertainty                       #
#                                                       #
#########################################################

from ROOT import *

  
### settings you want to give from outside ###

WP        = "HE"
extraCuts = ""
keys      = False
binning   = 40

###############################################

# to adjust by user:

msvVarList = []
ttVarList  = [ "melel" ]

totVarList = msvVarList+ttVarList 

###############################################

# fixed definitions:

ttMCNameList = ["TT","DY"]
# maybe different if using QCD:
dyMCNameList = []#"Zb","Zc","Zl"]
dataNameList = ["El_Data"]
dataAndMCNameList= ttMCNameList+dyMCNameList+dataNameList

category={"HE"   : "rc_eventSelection_5",
          "HP"   : "rc_eventSelection_x",
          "HEHE" : "rc_eventSelection_x",
          "HPHP" : "rc_eventSelection_x",
          }


varNamesList = { "msv1"  : "jetmetbjet1SVmass"          ,
                 "msv2"  : "jetmetbjet2SVmass"          ,
                 "msv"   : "jetmetbjetSVmass"           ,
                 "melel" : "eventSelectionbestzmassEle" ,
                 "mmumu" : "eventSelectionbestzmassMu"  ,
                 "mwnn"  : "xxx"
                }

path = "~acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/condorRDSmaker/outputs/"

fileNameList = { "El_Data" : path+"File_rds_zbb_ElA_DATA.root",
                 "Mu_Data" : path+"File_rds_zbb_MuA_DATA.root",
                 "DY"      : path+"File_rds_zbb_El_MC.root",
                 "TT"      : path+"File_rds_zbb_TT_El_MC.root",
                 "Zb"      : path+"File_rds_zbb_El_MC.root",
                 "Zc"      : path+"File_rds_zbb_El_MC.root",
                 "Zl"      : path+"File_rds_zbb_El_MC.root",
                 }

##############################################

def getVariables(var,dataAndMCList) :
    print "var = ", var
    print "ras = ", dataAndMCList["TT"].get()
    print "var = ", dataAndMCList["TT"].get()[var]
    x = dataAndMCList["TT"].get()[var]
    x.setMin(60)
    x.setMax(120)
    x.setBins(30)
    return x
    

def getDataAndMC(dataAndMCNameList,dataAndMCList) :

    # check ws
    # otherwise: directly rds

    file = {}
    ws   = {}
    myRDS = {}

    #rrv_w_b = {"HE"    : ws[DYMC].var("BtaggingReweightingHE")  ,
    #           "HP"    : ws[DYMC].var("BtaggingReweightingHP")  ,
    #           "HEHE"  : ws[DYMC].var("BtaggingReweightingHEHE"),
    #           "HPHP"  : ws[DYMC].var("BtaggingReweightingHPHP")
    #           }
    #rrv_w_lep  = ws[DYMC].var("LeptonsReweightingweight")
    #rrv_w_lumi = ws[DYMC].var("lumiReweightingLumiWeight")
    #w = RooFormulaVar("w","w", "@0*@1*@2", RooArgList(rrv_w_b[WP],rrv_w_lep,rrv_w_lumi))

    for name in dataAndMCNameList :
        print "name = ", name
        print "fileNameList[name] = ", fileNameList[name]
        file[name]  = TFile.Open(fileNameList[name])
        ws[name]    = file[name].Get("ws")
        myRDS[name] = ws[name].data("rds_zbb")
        myRDS[name] = myRDS[name].reduce(category[WP]+"==1")
        myRDS[name] = myRDS[name].reduce("eventSelectionbestzmassEle<120&eventSelectionbestzmassEle>60")
        print "#entries for sample", name , " at WP ",  WP ," =", myRDS[name].numEntries() 
        print "after reweighting ...." 
        dataAndMCList[name]=myRDS[name]

    return 

def makeTtPdfList(dataAndMCList, ttMCNames, ttVar, ttPdfList, RDH_tt, RHP_tt ) :
    print "*** ttMCNameList = "
    print ttMCNameList
    print "*** end ttMCNameList "
    mcName=ttMCNames
    ttVarName=ttVar.GetName()
    name=mcName+ttVarName
    if keys:
        RKP_tt[name] = RooKeysPdf( "RKP_tt_"+name,"myRKP_tt_"+name, ttVar, dataAndMCs  )
    else :    
        RDH_tt[mcName] = RooDataHist("RDH_tt_"+name,"myRDH_tt_"+name, RooArgSet(ttVar), dataAndMCList[ttMCNames]   )
        RHP_tt[mcName] = RooHistPdf( "RHP_tt_"+name,"myRHP_tt_"+name, RooArgSet(ttVar), RDH_tt[mcName] )
        #ttPdfList.add(RHP_tt[name])
    return
    # else:    
    # parameterized?

# def makeMsvPDF :

#def makeSimMistagPdf(msvPdfs) :
    # use b/c/l fraction simultaneously

#def makeSimTotPdf(ttPdfList+msvPdfList) :
    # use ttbar fraction simultaneuously
    
#def performFit :

#def plot:
    # loop over MC components
    
##############################################
    
def main():

    dataAndMCList = {}
    #dataAndMCs    = {}
    vars          = {}

    #for dataAndMcs in dataAndMcList  : dataAndMCList[dataAndMcs] = getDataAndMC(dataAndMcs)
    getDataAndMC(dataAndMCNameList, dataAndMCList)

    for varName in totVarList       : vars[varName] = getVariables(varNamesList[varName],dataAndMCList)

    ttFracList = RooArgList()
    ttYieldList = RooArgList()
    Ntt={}
    msvPdfList=RooArgList()

    RDH_tt={}
    RHP_tt={}
    
    #for ttVarName in ttVarList   : ttPdfList[ttVarName] = makeTtPdfList(dataAndMCList, ttMCNameList, vars[ttVarName], ttPdfList )
    ttPdfList=RooArgList()

    for ttVarName in ttVarList:
        for ttMCNames in ttMCNameList :
            makeTtPdfList(dataAndMCList, ttMCNames, vars[ttVarName], ttPdfList, RDH_tt, RHP_tt )
           
            Ntt[ttMCNames]=RooRealVar("Ntt"+ttMCNames,"Ntt"+ttMCNames,0,dataAndMCList[ttMCNames].numEntries())
            ttYieldList.add(Ntt[ttMCNames])

            print "RHP_tt = ", RHP_tt
            print "test = ", RHP_tt[ttMCNames]

            ttPdfList.add(RHP_tt[ttMCNames])

    ttPdf = RooAddPdf("ttPdf","ttPdf",ttPdfList,ttYieldList)

    ttPdf.fitTo(dataAndMCList["El_Data"])
    
    frame = vars[ttVarName].frame()
    dataAndMCList["El_Data"].plotOn(frame)
    ttPdf.plotOn(frame)
    frame.Draw()

    bla

    #for msvVarName in msvVarNameList : msvPdfList[msvVar] = makeMistagPdf(udsgcMCList, msvVar)

    totPdfList = msvPdfList+ttPdfList    

    if msvVars.len() >1 : msvPdf = makeSimMistagPdf(msvPdfs)
    else                : msvPdf = msvPdf.at(0)
    if allVars.len() >1 : totPdf = makeSimTotPdf(ttPdfList+msvPdfList)
    else                : totPdf = msvPdf.at(0)
        

    totPdf.fitTo(dataAndMc["DATA"])

    plot(data,pdfs,componentList)
