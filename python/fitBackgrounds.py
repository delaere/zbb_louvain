
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
gROOT.SetStyle("Plain")
  
### settings you want to give from outside ###

frac      = false
WP        = "HE"
extraCut  = ""
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

category={"HE"         : "rc_eventSelection_5",
          "HP"         : "rc_eventSelection_6",
          "HEMET"      : "rc_eventSelection_7",
          "HPMET"      : "rc_eventSelection_8",
          "HEHE"       : "rc_eventSelection_9",
          "HPHP"       : "rc_eventSelection_11",
          "HEMETsig"   : "rc_eventSelection_15",
          "HPMETsig"   : "rc_eventSelection_16",
          "HEHEMETsig" : "rc_eventSelection_17",
          "HPHPMETsig" : "rc_eventSelection_19",
          }


varNamesList = { "msv1"  : "jetmetbjet1SVmass"          ,
                 "msv2"  : "jetmetbjet2SVmass"          ,
                 "msv"   : "jetmetbjetSVmass"           ,
                 "melel" : "eventSelectionbestzmassEle" ,
                 "mmumu" : "eventSelectionbestzmassMu"  ,
                 "mwnn"  : "mlpZbbvsTT"
                }

min = {"msv1" :   0,
       "msv2" :   0,
       "msv"  :   0,
       "melel":  60,
       "mmumu":  60,
       "mwnn" :-0.2}

max = {"msv1" :    5,
       "msv2" :    5,
       "msv"  :    5,
       "melel":  120,
       "mmumu":  120,
       "mwnn" :    1.2}

bins = {"msv1" :   60,
        "msv2" :   60,
        "msv"  :   60,
        "melel":   60,
        "mmumu":   60,
        "mwnn" :   60}

color = {"msv1" : kRed,
         "msv2" : kRed,
         "msv"  : kRed,
         "melel": kYellow,
         "mmumu": kYellow,
         }

C={}

path = "~acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/condorRDSmaker/outputs/"

fileNameList = { "El_Data" : path+"File_rds_zbb_ElA_DATA.root",
                 "Mu_Data" : path+"File_rds_zbb_MuA_DATA.root",
                 "DY"      : path+"File_rds_zbb_El_MC.root",
                 #"TT"      : "/home/fynu/vizangarciaj/scratch/RDSME120802/RDS_rdsME_TT_El_MC.root",
                 "TT"      : path+"File_rds_zbb_TT_El_MC.root",
                 "Zb"      : path+"File_rds_zbb_El_MC.root",
                 "Zc"      : path+"File_rds_zbb_El_MC.root",
                 "Zl"      : path+"File_rds_zbb_El_MC.root",
                 }

##############################################

def getVariables(varNamesList,varName,dataAndMCList) :
    var=varNamesList[varName]
    print "var = ", var
    print "ras = ", dataAndMCList["TT"].get()
    print "var = ", dataAndMCList["TT"].get()[var]
    x = dataAndMCList["TT"].get()[var]
    x.setMin(min[varName])
    x.setMax(max[varName])
    x.setBins(bins[varName])

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
        if ws[name]:
            myRDS[name] = ws[name].data("rds_zbb")
        else :   
            myRDS[name] = file[name].Get("rds_zbb")
        myRDS[name] = myRDS[name].reduce(category[WP]+"==1"+extraCut)
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

    for varName in totVarList       : vars[varName] = getVariables(varNamesList,varName,dataAndMCList)

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

    Ntt=[]
    Nmistag=[]
    ftt=[] 
    fmistag=[] 
    

    if len(ttbarVarList):
        for ttVarName in ttbarVarList:
            for ttMCName in ttMCNameList :
                pdfName = ttMCName+vars[ttVarName].GetName() 
                makePdfList(dataAndMCList, ttMCName, vars[ttVarName], RDH_tt, RHP_tt )
                ttPdfList.add(RHP_tt[pdfName])
                Ntt.append(RooRealVar("N_"+ttMCName,"N_"+ttMCName,0,dataAndMCList[ttMCName].numEntries()))
                ftt.append(RooRealVar("f_"+ttMCName,"f_{"+ttMCName+"}",0,1.))
        for Ntts in Ntt: ttYieldList.add(Ntts)
        ftt = ftt[:len(ftt)-1]
        for ftts in ftt: ttFracList.add(ftts)

    if len(mistagVarList):        
        for mistagVarName in mistagVarList :
            for mistagMCName in mistagMCNameList :
                pdfName = mistagMCName+vars[mistagVarName].GetName() 
                makePdfList(dataAndMCList, mistagMCName, vars[mistagVarName], RDH_mistag, RHP_mistag )
                mistagPdfList.add(RHP_mistag[pdfName])

                Nmistag.append(RooRealVar("N_"+mistagMCName,"N_"+mistagMCName,0,dataAndMCList[mistagMCName].numEntries()))
                fmistag.append(RooRealVar("f_"+mistagMCName,"f_{"+mistagMCName+"}",0,1.))

        for Nmistags in Nmistag: mistagYieldList.add(Nmistags)
        fmistag = fmistag[:len(fmistag)-1]
        for fmistags in fmistag: mistagFracList.add(fmistags)
                

    if len(mistagVarList):
        if frac : mistagPdf = RooAddPdf("mistagPdf","mistagPdf",mistagPdfList,mistagFracList)
        else    : mistagPdf = RooAddPdf("mistagPdf","mistagPdf",mistagPdfList,mistagYieldList)
        mistagPdf.fitTo(dataAndMCList["El_Data"])
        ## for vars in list
        frame = vars[mistagVarName].frame()
        dataAndMCList["El_Data"].plotOn(frame)
        mistagPdf.plotOn(frame)
        for mistagVarName in mistagVarList:
            mistagPdf.plotOn(frame,
                             RooFit.Components("RHP_Zb"+vars[mistagVarName].GetName()+",RHP_Zc"+vars[mistagVarName].GetName()+",RHP_Zl"+vars[mistagVarName].GetName()),
                             RooFit.DrawOption("F"),
                             RooFit.LineColor(kBlack),
                             RooFit.FillColor(kBlue-7),
                             RooFit.LineWidth(1)
                             )
            mistagPdf.plotOn(frame,
                             RooFit.Components("RHP_Zb"+vars[mistagVarName].GetName()+",RHP_Zc"+vars[mistagVarName].GetName()+",RHP_Zl"+vars[mistagVarName].GetName()),
                             RooFit.LineColor(kBlack),
                             RooFit.FillColor(kBlue-7),
                             RooFit.LineWidth(1))
            mistagPdf.plotOn(frame,
                             RooFit.Components("RHP_Zc"+vars[mistagVarName].GetName()+",RHP_Zb"+vars[mistagVarName].GetName()),
                             RooFit.DrawOption("F"),
                             RooFit.LineColor(kBlack),
                             RooFit.FillColor(kGreen-7),
                             RooFit.LineWidth(1))
            mistagPdf.plotOn(frame,
                             RooFit.Components("RHP_Zc"+vars[mistagVarName].GetName()+",RHP_Zb"+vars[mistagVarName].GetName()),
                             RooFit.LineColor(kBlack),
                             RooFit.FillColor(kGreen-7),
                             RooFit.LineWidth(1))
            mistagPdf.plotOn(frame,
                             RooFit.Components("RHP_Zb"+vars[mistagVarName].GetName()),
                             RooFit.DrawOption("F"),
                             RooFit.LineColor(kBlack),
                             RooFit.FillColor(kRed-7),
                             RooFit.LineWidth(1))
            mistagPdf.plotOn(frame,
                             RooFit.Components("RHP_Zb"+vars[mistagVarName].GetName()),
                             RooFit.LineColor(kBlack),
                             RooFit.FillColor(kRed-7),
                             RooFit.LineWidth(1))
        dataAndMCList["El_Data"].plotOn(frame)
        mistagPdf.paramOn(frame,dataAndMCList["El_Data"])
        C["mistag"]=TCanvas("mistag","mistag")
        frame.Draw()

    if len(ttbarVarList):
        if frac : ttPdf = RooAddPdf("ttPdf","ttPdf",ttPdfList,ttFracList)
        else    : ttPdf = RooAddPdf("ttPdf","ttPdf",ttPdfList,ttYieldList)
        
        ttPdf.fitTo(dataAndMCList["El_Data"])
    
        frame = vars[ttVarName].frame()
        dataAndMCList["El_Data"].plotOn(frame)
        ttPdf.plotOn(frame)
        for ttVarName in ttbarVarList:
            ttPdf.plotOn(frame,
                         RooFit.Components("RHP_DY"+vars[ttVarName].GetName()+",RHP_TT"+vars[ttVarName].GetName()),
                         RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kBlue-7),
                         RooFit.LineWidth(1)
                         )
            ttPdf.plotOn(frame,
                         RooFit.Components("RHP_DY"+vars[ttVarName].GetName()+",RHP_TT"+vars[ttVarName].GetName()),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kBlue-7),
                         RooFit.LineWidth(1))
            ttPdf.plotOn(frame,
                         RooFit.Components("RHP_TT"+vars[ttVarName].GetName()),
                         RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kYellow-7),
                         RooFit.LineWidth(1)
                         )
            ttPdf.plotOn(frame,
                         RooFit.Components("RHP_TT"+vars[ttVarName].GetName()),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kYellow-7),
                         RooFit.LineWidth(1))
        dataAndMCList["El_Data"].plotOn(frame)
        ttPdf.paramOn(frame,dataAndMCList["El_Data"])

        C["tt"]=TCanvas("tt","tt")
        frame.Draw()

    #totPdfList = msvPdfList+ttPdfList    

    #if len(mistagVarList) >1 : msvPdf = makeSimMistagPdf(msvPdfs)
    #else                     : msvPdf = msvPdf.at(0)
    #if len(totVarList) >1    : totPdf = makeSimTotPdf(ttPdfList+msvPdfList)
    #else                     : totPdf = msvPdf.at(0)
        

    #totPdf.fitTo(dataAndMc["DATA"])

    #plot(data,pdfs,componentList)
