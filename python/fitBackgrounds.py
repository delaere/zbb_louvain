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

mistagVarList = [ "msv1" ]
ttbarVarList  = [ "melel" ]

totVarList = mistagVarList+ttbarVarList 

###############################################

# fixed definitions:

ttMCNameList = ["TT","DY"]
# maybe different if using QCD:
mistagMCNameList = ["Zb","Zc","Zl"]
dataNameList = ["El_Data"]
dataAndMCNameList= ttMCNameList+mistagMCNameList+dataNameList

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
    #x.setMin(0.1)
    #x.setMax(5.1)
    #x.setBins(75)
    x.setMin(60)
    x.setMax(120)
    x.setBins(30)

    #todo: make this automatic for all variables
    
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

def makePdfList(dataAndMCList, mcName, var, RDH, RHP ) :
    varName=var.GetName()
    name=mcName+varName

    print "mcName    = ", mcName
    print "varName   = ", varName
    print "name      = ", name

    print "**** before cut: number of entries = " , dataAndMCList[mcName].numEntries()

    if varName=="jetmetbjet1SVmass":
        if mcName=="Zl":
            print "Zl dataset, going to cut on udsgc flav"
            dataAndMCList[name] = dataAndMCList[mcName].reduce("jetmetbjet1Flavor==1||jetmetbjet1Flavor==-1||jetmetbjet1Flavor==2||jetmetbjet1Flavor==-2||jetmetbjet1Flavor==3||jetmetbjet1Flavor==-3||jetmetbjet1Flavor==21")
        if mcName=="Zc":
            print "Zc dataset, going to cut on c flav"
            dataAndMCList[name]=dataAndMCList[mcName].reduce("jetmetbjet1Flavor==4||jetmetbjet1Flavor==-4")
        if mcName=="Zb":
            print "Zb dataset, going to cut on b flav"
            dataAndMCList[name]=dataAndMCList[mcName].reduce("jetmetbjet1Flavor==5||jetmetbjet1Flavor==-5")
    else:
        dataAndMCList[name]=dataAndMCList[mcName]
        print "DID NOT MATCH SAMPLE NAME"

    print "**** after cut: number of entries = " , dataAndMCList[mcName].numEntries()
    print "**** after cut: number of entries = " , dataAndMCList[name].numEntries()
        
    # todo: something goes wrong here with the cut on the dataset. Somethow it is not given to the RooDataHist correctly
    
    if keys:
        RKP[name] = RooKeysPdf( "RKP_tt_"+name,"myRKP_tt_"+name, var, dataAndMCs  )
    else :    
        RDH[name] = RooDataHist("RDH_"+name,"RDH_"+name, RooArgSet(var), dataAndMCList[name]   )
        RHP[name] = RooHistPdf( "RHP_"+name,"RHP_"+name, RooArgSet(var), RDH[name] )
    # else:    
    # parameterized?
    return

#############################################################################################################

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
    vars          = {}

    getDataAndMC(dataAndMCNameList, dataAndMCList)

    for varName in totVarList       : vars[varName] = getVariables(varNamesList[varName],dataAndMCList)

    ttPdfList       = RooArgList()
    ttFracList      = RooArgList()
    ttYieldList     = RooArgList()

    mistagPdfList   = RooArgList()
    mistagFracList  = RooArgList()
    mistagYieldList = RooArgList()

    RDH_tt={}
    RHP_tt={}
    RDH_mistag={}
    RHP_mistag={}

    Ntt={}
    Nmistag={}

    if len(ttbarVarList):
        for ttVarName in ttbarVarList:
            for ttMCName in ttMCNameList :
                pdfName = ttMCName+vars[ttVarName].GetName() 
                makePdfList(dataAndMCList, ttMCName, vars[ttVarName], RDH_tt, RHP_tt )
                Ntt[ttMCName]=RooRealVar("Ntt"+ttMCName,"Ntt"+ttMCName,0,dataAndMCList[ttMCName].numEntries())
                ttYieldList.add(Ntt[ttMCName])
                ttPdfList.add(RHP_tt[pdfName])

    if len(mistagVarList):        
        for mistagVarName in mistagVarList :
            for mistagMCName in mistagMCNameList :
                pdfName = mistagMCName+vars[mistagVarName].GetName() 
                makePdfList(dataAndMCList, mistagMCName, vars[mistagVarName], RDH_mistag, RHP_mistag )
                Nmistag[mistagMCName]=RooRealVar("Nmistag"+mistagMCName,"Nmistag"+mistagMCName,0,dataAndMCList[mistagMCName].numEntries())
                mistagYieldList.add(Nmistag[mistagMCName])#
                mistagPdfList.add(RHP_mistag[pdfName])

    if len(mistagVarList):
        mistagPdf = RooAddPdf("mistagPdf","mistagPdf",mistagPdfList,mistagYieldList)
        mistagPdf.fitTo(dataAndMCList["El_Data"])
        ## for vars in list
        frame = vars[mistagVarName].frame()
        dataAndMCList["El_Data"].plotOn(frame)
        mistagPdf.plotOn(frame)
        frame.Draw()

    if len(ttbarVarList):
        ttPdf = RooAddPdf("ttPdf","ttPdf",ttPdfList,ttYieldList)
        
        ttPdf.fitTo(dataAndMCList["El_Data"])
    
        frame = vars[ttVarName].frame()
        dataAndMCList["El_Data"].plotOn(frame)
        ttPdf.plotOn(frame)
        frame.Draw()

    #totPdfList = msvPdfList+ttPdfList    

    #if len(mistagVarList) >1 : msvPdf = makeSimMistagPdf(msvPdfs)
    #else                     : msvPdf = msvPdf.at(0)
    #if len(totVarList) >1    : totPdf = makeSimTotPdf(ttPdfList+msvPdfList)
    #else                     : totPdf = msvPdf.at(0)
        

    #totPdf.fitTo(dataAndMc["DATA"])

    #plot(data,pdfs,componentList)
