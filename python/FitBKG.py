from ROOT import *
gROOT.SetStyle("Plain")


  
###############################################

### settings you want to give from outside ###
# to adjust by user:

channelList   = ["Mu","El"]

dataLabel = "2012"

frac      = False
WP        = "HPHPMETsig"
extraCut  = "&jetmetMETsignificance < 10 &mlphiggsvsbkg_125_comb_MM_N<0.5&mlphiggsvsbkg_125_comb_MM_N>0."
keys      = False

extraCutList = {"mwnn"     : "jetmetMETsignificance < 10",#&mlphiggsvsbkg_125_comb_MM_N>-0.1&mlphiggsvsbkg_125_comb_MM_N<0.5&mlpZbbvsTT_mu_MM_N>-0.1",
                "mmumu"    : "jetmetMETsignificance < 10",#&mlphiggsvsbkg_125_comb_MM_N>-0.1&mlphiggsvsbkg_125_comb_MM_N<0.5&mlpZbbvsTT_mu_MM_N>-0.1",
		}
		
ttbarVarList  = ["mwnn"]
mistagVarList = ["msv2"]
#if channel=="Mu": ttbarVarList  = [ "mmumu" ]>-0.1
#if channel=="El": ttbarVarList  = [ "melel" ]

totVarList = ttbarVarList+mistagVarList

###############################################

# fixed definitions:
X={}

RHP_tt={}
Ntt={}
ftt={}
RDH_tt={}

ttbarData={}

ttMCNameList = ["TT","ZZ"]
# maybe different if using QCD:
mistagMCNameList  = ["Zxx","Zbx","Zbb"]
dataNameList      = [dataLabel]
MCNameList        = ttMCNameList+mistagMCNameList
dataAndMCNameList = ttMCNameList+mistagMCNameList+dataNameList

AlldataAndMCList = {}
dataAndMCList = {}
dataAndMCListZH = {}

category={"HE"         : "rc_eventSelection_5",
          "HP"         : "rc_eventSelection_6",
          "HEMET"      : "rc_eventSelection_7",
          "HPMET"      : "rc_eventSelection_8",
          "HPHEMETsig" : "rc_eventSelection_17",
          "HPHPMETsig" : "rc_eventSelection_18",
          }


varNamesList = { "msv1"  : "jetmetbjet1pt"          ,
                 #"msv2"  : "mlpZbbvsTT_MM_N",
		 "msv2"  : "jetmetbjetProdCSVdisc"          ,
                 #"msv2"  : "mlphiggsvsbkg_125_comb_MM_N" ,
		 "melel" : "eventSelectionbestzmassEle" ,
                 "mmumu" : "eventSelectionbestzmassMu"  ,
                 #mwnn"  : "jetmetMET",
		 "mwnn"  : "mlpZbbvsTT_mu_MM_N",
                 "w_b_HE"    : "BtaggingReweightingHE"  ,
                 "w_b_HP"    : "BtaggingReweightingHP"  ,
                 "w_b_HEHE"  : "BtaggingReweightingHEHE",
                 "w_b_HEHEMET"  : "BtaggingReweightingHEHE",
                 "w_b_HPHEMETsig"  : "BtaggingReweightingHEHP",
                 "w_b_HPHP"  : "BtaggingReweightingHPHP",
                 "w_b_HPHPMETsig"  : "BtaggingReweightingHPHP",
                 "w_lep"     : "LeptonsReweightingweight",
                 "jmul"      : "jetmetnj",
                 "w_lumi"    : "lumiReweightingLumiWeight",
                }

min = {"msv1"   :   20.,
       "msv2"   :   0.46,
       "msv"    :   0,
       "melel"  :  76,
       "mmumu"  :  76,
       "mwnn"   :  0.0,
       "mwnn_1"   :-0.2,
       "mwnn_2"   : 0.,
       "w_b_HE" : 0. , 
       "w_b_HP"    : 0.,
       "w_b_HEHE"  : 0.,
       "w_b_HEHEMET"  : 0.,
       "w_b_HPHEMETsig"  : 0.,
       "w_b_HPHPMETsig"  : 0.,
       "w_b_HPHP"  : 0.,
       "w_lep"     : 0.,
       "w_lumi"    : 0.,
       "jmul"      :2.
       }

max = {"msv1" :    250,
       "msv2" :    1.,
       "msv"  :    6,
       "melel":  106,
       "mmumu":  106,
       "mwnn" :   1.0,
       "mwnn_1"   : 0.5,
       "mwnn_2"   : 0.5,
       "w_b_HE"    : 2., 
       "w_b_HP"    : 2.,
       "w_b_HEHE"  : 2.,
       "w_b_HEHEMET"  : 2.,
       "w_b_HPHEMETsig"  : 2.,
       "w_b_HPHPMETsig"  : 2.,
       "w_b_HPHP"  : 2.,
       "w_lep"     : 2.,
       "w_lumi"    : 2.,
       "jmul"      : 8. 
       }

bins = {"msv1" :   8,
        "msv2" :   4,
        "msv"  :   20,
        "melel":   34,
        "mmumu":   5,
        "mwnn" :   4,
        "mwnn_1"   : 20,
        "mwnn_2"   : 16,
        "w_b_HE"    : 100, 
        "w_b_HP"    : 100,
        "w_b_HEHE"  : 100,
        "w_b_HEHEMET"  : 100,
        "w_b_HPHEMETsig"  : 100,
        "w_b_HPHPMETsig"  : 100,
        "w_b_HPHP"  : 100,
        "w_lep"     : 100,
        "w_lumi"    : 100,
        "jmul"      : 6, 
        }

color = {"msv1" : kRed,
         "msv2" : kRed,
         "msv"  : kRed,
         "melel": kYellow,
         "mmumu": kYellow,
         "mwnn_1" :kYellow,
         }

C={}
myFrame={}

#path = "~acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/condorRDSmakerNoWS/outputs/"
path = "/nfs/user/acaudron/Tree2_537/"
pathData = "/nfs/user/acaudron/Tree2_537/"
fileNameList = {}

for chan in channelList:
    if chan=="El" : chanData="Ele"
    else : chanData=chan
    fileNameList["2012"+chan] = pathData+"RDS_rdsME_Double"+chanData+"_Data.root"
    fileNameList["ref"+chan] = path+"RDS_rdsME_DY_"+chan+"_MC.root"
    fileNameList["DY"+chan] = path+"RDS_rdsME_DY_"+chan+"_MC.root"
    fileNameList["TT"+chan] = path+"RDS_rdsME_TT_"+chan+"_MC.root"
    fileNameList["ZZ"+chan] = path+"RDS_rdsME_ZZ_"+chan+"_MC.root"
    fileNameList["Zbb"+chan] = path+"RDS_rdsME_DY_"+chan+"_MC.root"
    fileNameList["Zbx"+chan] = path+"RDS_rdsME_DY_"+chan+"_MC.root"
    fileNameList["Zxx"+chan] = path+"RDS_rdsME_DY_"+chan+"_MC.root"
    fileNameList["ZH125"+chan] = path+"RDS_rdsME_ZH125_"+chan+"_MC.root"	
for name in fileNameList:
	print name		    		  
				  
				  
from zbbCommons import zbbnorm

lumi = { "DATAMu"   : zbbnorm.lumi_tot2012,
         "DATAEl"     : zbbnorm.lumi_tot2012,
         "TTEl"       : zbbnorm.nev_TTjets_summer12/zbbnorm.xsec_TTjets_8TeV/1000.,
         "ZbbEl"       : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "ZbxEl"       : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "ZxxEl"       : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "ZZEl"       : zbbnorm.nev_ZZ_summer12/zbbnorm.xsec_ZZ_8TeV/1000./(10000./11936.),
         "TTMu"     : zbbnorm.nev_TTjets_summer12/zbbnorm.xsec_TTjets_8TeV/1000.,
         "ZbbMu"     : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "ZbxMu"     : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "ZxxMu"     : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "ZZMu"     : zbbnorm.nev_ZZ_summer12/zbbnorm.xsec_ZZ_8TeV/1000./(10000./16986.),
	 "ZH115El"    : zbbnorm.nev_ZH115_summer12/zbbnorm.xsec_ZH115_8TeV/1000.,
         "ZH120El"    : zbbnorm.nev_ZH120_summer12/zbbnorm.xsec_ZH120_8TeV/1000.,
	 "ZH115Mu"  : zbbnorm.nev_ZH115_summer12/zbbnorm.xsec_ZH115_8TeV/1000.,
         "ZH120Mu"  : zbbnorm.nev_ZH120_summer12/zbbnorm.xsec_ZH120_8TeV/1000.,
	 "ZH125El"    : zbbnorm.nev_ZH125_summer12/zbbnorm.xsec_ZH125_8TeV/1000./(10000./48726.),
	 "ZH125Mu"  : zbbnorm.nev_ZH125_summer12/zbbnorm.xsec_ZH125_8TeV/1000./(10000./65412.),
         "ZH130El"    : zbbnorm.nev_ZH130_summer12/zbbnorm.xsec_ZH130_8TeV/1000.,
         "ZH135El"    : zbbnorm.nev_ZH135_summer12/zbbnorm.xsec_ZH135_8TeV/1000.,
         "ZH130Mu"  : zbbnorm.nev_ZH130_summer12/zbbnorm.xsec_ZH130_8TeV/1000.,
         "ZH135Mu"  : zbbnorm.nev_ZH135_summer12/zbbnorm.xsec_ZH135_8TeV/1000.
	         }
		 
		 
def getVariables(varNamesList,varName,dataAndMCListZH) :
    var=varNamesList[varName]
    #y=dataAndMCList["Zl"]
    y=dataAndMCListZH["refMu"]
    #print "var = ", var
    #print "ras = ", y.get()
    #print "var = ", y.get()[var]
    x = y.get()[var]
    if x :
        x.setMin(min[varName])
        x.setMax(max[varName])
        x.setBins(bins[varName])
        return x
    else: return 0
    

def getDataAndMC(dataAndMCNameList,dataAndMCList,channel) :

    # check ws
    # otherwise: directly rds

    file = {}
    ws   = {}
    myRDS = {}

    print channel

    for name in dataAndMCNameList :
        print "name = ", name
        if name=="2012":
            print "making 2012 dataset"
            file["2012"+channel]  = TFile.Open(fileNameList["2012"+channel])
            tree_zbb = file["2012"+channel].Get("rds_zbb")
            ws_zbb = file["2012"+channel].Get("ws_ras")
            ras_zbb = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())
            myRDS["2012"+channel] = RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)
            print "Data numEntries() = ", myRDS["2012"+channel].numEntries()
        else :
            print "fileNameList[name+channel] = ", fileNameList[name+channel]
            file[name+channel]  = TFile.Open(fileNameList[name+channel])
            tree_zbb = file[name+channel].Get("rds_zbb")
            ws_zbb = file[name+channel].Get("ws_ras")
            ras_zbb = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())
            myRDS[name+channel] = RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)
            myRDS[name+channel].SetName(name+channel)
        print "*** Going to reduce RDS ", name        
	print "#entries for sample", name , " at WP ",  WP ," =", myRDS[name+channel].numEntries() 
	myRDS[name+channel] = myRDS[name+channel].reduce(category[WP]+"==1"+extraCut)
	print "#entries for sample", name , " at WP ",  WP ," =", myRDS[name+channel].numEntries() 
        if channel=="El": myRDS[name+channel] = myRDS[name+channel].reduce("eventSelectionbestzmassEle<106&eventSelectionbestzmassEle>76")
        if channel=="Mu": myRDS[name+channel] = myRDS[name+channel].reduce("eventSelectionbestzmassMu<106&eventSelectionbestzmassMu>76")
        print "#entries for sample", name , " at WP ",  WP ," =", myRDS[name+channel].numEntries() 
        dataAndMCList[name+channel]=myRDS[name+channel]

    return 

def setWeights(dataAndMCList,MCNameList,w,channel) :
    for name in MCNameList :
        print "***BEFORE numEntries() = ", dataAndMCList[name+channel].numEntries()
        dataAndMCList[name+channel].addColumn(w)
    for name in MCNameList :
        dataAndMCList[name+channel] = RooDataSet(dataAndMCList[name+channel].GetName(),
                                         dataAndMCList[name+channel].GetName(),
                                         dataAndMCList[name+channel],
                                         dataAndMCList[name+channel].get(),
                                         "",
                                         w.GetName())
        print "***AFTER numEntries() for sample ", name , " = ", dataAndMCList[name+channel].numEntries()
        print "sumEntries() = ", dataAndMCList[name+channel].sumEntries()

    return

def makePdfList(dataAndMCList, mcName, var, RDH, RHP, var2, channel ) :
    varName=var.GetName()
    name=mcName

    #print "mcName    = ", mcName
    #print "varName   = ", varName
    print "name      = ", name

    print "**** before cut: number of entries = " , dataAndMCList[mcName].numEntries()

    if mcName=="Zxx"+channel:
        print "Zxx dataset, going to cut on udsgc flav"
        dataAndMCList[name] = dataAndMCList[mcName].reduce("abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)!=5")
    	print " Zxx after reduce = ", dataAndMCList[name].numEntries()
    if mcName=="Zbx"+channel:
        print "Zbx dataset, going to cut on c flav"
        dataAndMCList[name]=dataAndMCList[mcName].reduce("(abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)==5) ||(abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)!=5) ")
    if mcName=="Zbb"+channel:
        print "Zbb dataset, going to cut on b flav"
        dataAndMCList[name]=dataAndMCList[mcName].reduce("abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)==5")
    else:
        dataAndMCList[name]=dataAndMCList[mcName]
        print "DID NOT MATCH SAMPLE NAME"

    print "**** after cut: number of entries = " , dataAndMCList[mcName].numEntries()
    print "**** after cut: number of entries = " , dataAndMCList[name].numEntries()
        
    # todo: something goes wrong here with the cut on the dataset. Somethow it is not given to the RooDataHist correctly
    
    if var2:
        RDH[name] = RooDataHist("RDH_"+name,"RDH_"+name, RooArgSet(var,var2), dataAndMCList[name]   )
        RHP[name] = RooHistPdf( "RHP_"+name,"RHP_"+name, RooArgSet(var,var2), RDH[name] )
    elif keys:
        RKP[name] = RooKeysPdf( "RKP_tt_"+name,"myRKP_tt_"+name, var, dataAndMCs  )
    else :    
        RDH[name] = RooDataHist("RDH_"+name,"RDH_"+name, RooArgSet(var), dataAndMCList[name]   )
        RHP[name] = RooHistPdf( "RHP_"+name,"RHP_"+name, RooArgSet(var), RDH[name] )
    # else:    
    # parameterized?
    return

#############################################################################################################
def main():

    plot = TFile("Fit_result.root","RECREATE")

    vars          = {}
    frame ={}
    for channel in channelList:
        getDataAndMC(dataAndMCNameList, AlldataAndMCList,channel)
        getDataAndMC(["ref"], dataAndMCListZH,channel)
        print "AlldataAndMCList", AlldataAndMCList
    print " pass get Data and MC "
    
    for channel in channelList:
        for mcnames in MCNameList :
            for ttVarName in ttbarVarList:
	        print "in loop reduce extra cut"
                AlldataAndMCList[mcnames+channel] = AlldataAndMCList[mcnames+channel].reduce(extraCutList[ttVarName])
	    
    for varName in varNamesList      : vars[varName] = getVariables(varNamesList,varName,dataAndMCListZH)

    for channel in channelList:   
        weight = RooFormulaVar("w","w", "@0*@1*@2", RooArgList(vars["w_lep"],vars["w_lumi"],vars["w_b_"+WP]))
        setWeights(AlldataAndMCList,MCNameList,weight,channel)
        print "AlldataAndMCList", AlldataAndMCList
    print "pass reweighting" 


	
    SF_zbb=RooRealVar("SF_zbb","SF_zbb",1.,0.5, 3.)
    SF_zbx=RooRealVar("SF_zxx","SF_zbx",1.,0.5, 3.)
    SF_zxx=RooRealVar("SF_zxx","SF_zxx",1.,0.5, 3.)
    SF_tt_e=RooRealVar("SF_tt_m","SF_tt",1.,0.5, 3.)
    SF_tt_m=RooRealVar("SF_tt_m","SF_tt",1.,0.5, 3.)    
    SF_zz=RooRealVar("SF_zz","SF_zz",1.,1. , 1.)

    SF={"TTEl":SF_tt_m,
        "ZbbEl":SF_zbb,
        "ZbxEl":SF_zbx,
	"ZxxEl":SF_zxx,
	"ZZEl":SF_zz,
	"TTMu":SF_tt_m,
        "ZbbMu":SF_zbb,
        "ZbxMu":SF_zbx,
	"ZxxMu":SF_zxx,
	"ZZMu":SF_zz
	}

    flavor = RooCategory("El","El")
    flavor.defineType("El")
    flavor.setLabel("El")
    #print flavor, AlldataAndMCList["2012El"]
    AlldataAndMCList["2012El"].addColumn(flavor)
    flavorMu = RooCategory("Mu","Mu")
    flavorMu.defineType("Mu")   
    flavorMu.setLabel("Mu")
    AlldataAndMCList["2012Mu"].addColumn(flavorMu)    
    
    Pdf2D={}
    N={}
    N_exp={}
    myRAS_1D={}
    myRAS_2D={}
    myRDH_2D={}
    myRHP_2D={}
    myRDH_1D={}
    myRHP_1D={}
    PdfList2D={}
    YieldList2D={}
		    
    for channel in channelList:
        PdfList2D[channel]    = RooArgList()
        YieldList2D[channel]   = RooArgList()

        ### 2 variables, matching the names "var1" and "var2" in the RooDataSet myRDS

        if len(ttbarVarList) and len(mistagVarList):
            for ttVarName in ttbarVarList:  
	        for mistagVarName in mistagVarList:
    	            for  mcnames in MCNameList:
		        ### make 1D-PDF
		        print "make 1D-PDF"
		    
		        makePdfList(AlldataAndMCList, mcnames+channel,vars[ttVarName],myRDH_2D, myRHP_2D ,vars[mistagVarName],channel)
		      
		        PdfList2D[channel].add(myRHP_2D[mcnames+channel])
		    
		        N_exp[mcnames+channel]=RooConstVar("N_exp_"+mcnames+channel,"N_exp_"+mcnames+channel,
                                               (AlldataAndMCList[mcnames+channel].sumEntries()*(lumi["DATA"+channel]/lumi[mcnames+channel])))
						     
		        N[mcnames+channel] = RooFormulaVar("N_"+mcnames,"N_"+mcnames+channel,"@0*@1",RooArgList(N_exp[mcnames+channel],SF[mcnames+channel]))
		  
		        print "yields expected for ",mcnames+channel,N_exp[mcnames+channel].getValV()
		      		    
		        YieldList2D[channel].add(N[mcnames+channel])
				          
        print "make pdf"
        #print PdfList2D[channel],YieldList2D[channel]
        Pdf2D[channel] = RooAddPdf("Pdf2D"+channel,"Pdf2D"+channel,PdfList2D[channel],YieldList2D[channel])
 
 
    simPdf = RooSimultaneous("sim","sim",flavor)
    for channel in channelList:
        simPdf.addPdf(Pdf2D[channel],channel)
        
    DATA = RooDataSet("DATA","DATA",AlldataAndMCList["2012El"],AlldataAndMCList["2012El"].get())
    print "before appending nbr data :",DATA.numEntries()
    DATA.append(AlldataAndMCList["2012Mu"])
    print "after appending nbr data :",DATA.numEntries()
   
    print "reach fit level"
    #simPdf.fitTo(DATA)#,Verbose(true))
    
    for channel in channelList:
    	Pdf2D[channel].fitTo(AlldataAndMCList[dataLabel+channel])

    ttframe={}
    mistagframe={}
    newfile = TFile("test.root","RECREATE") 
    CANVAS = TCanvas("CANVAS","CANVAS",1200,600)
    CANVAS.Divide(4)
    
    for ttVarName in ttbarVarList:  
        for mistagVarName in mistagVarList:
            th2Sigall = TH2D("Sigall","Sigall",vars[ttVarName].getBins(),vars[ttVarName].getMin(),vars[ttVarName].getMax(),vars[mistagVarName].getBins(),vars[mistagVarName].getMin(),vars[mistagVarName].getMax())
	    th2BKGall = TH2D("BKGall","BKGall",vars[ttVarName].getBins(),vars[ttVarName].getMin(),vars[ttVarName].getMax(),vars[mistagVarName].getBins(),vars[mistagVarName].getMin(),vars[mistagVarName].getMax())

	    for channel in channelList:
                ttframe[channel] = vars[ttVarName].frame()
     	        AlldataAndMCList[dataLabel+channel].plotOn(ttframe[channel])
	    
	        th2Sig = TH2D("Sig","Sig",vars[ttVarName].getBins(),vars[ttVarName].getMin(),vars[ttVarName].getMax(),vars[mistagVarName].getBins(),vars[mistagVarName].getMin(),vars[mistagVarName].getMax())
                AlldataAndMCList[dataLabel+channel].fillHistogram(th2Sig, RooArgList(vars[ttVarName],vars[mistagVarName]))	    
                AlldataAndMCList[dataLabel+channel].fillHistogram(th2Sigall, RooArgList(vars[ttVarName],vars[mistagVarName]))	    
	        th2Sig.Write()
	        Pdf2D[channel].plotOn(ttframe[channel],
                     RooFit.LineColor(kBlue),
                     RooFit.LineWidth(2)
                     )

	        chi=ttframe[channel].chiSquare()
   	        print "Chi square for Var 1:",chi
	    
	        th2BKG = TH2D("BKG","BKG",vars[ttVarName].getBins(),vars[ttVarName].getMin(),vars[ttVarName].getMax(),vars[mistagVarName].getBins(),vars[mistagVarName].getMin(),vars[mistagVarName].getMax())
                Pdf2D[channel].fillHistogram(th2BKG, RooArgList(vars[ttVarName],vars[mistagVarName]))
                Pdf2D[channel].fillHistogram(th2BKGall, RooArgList(vars[ttVarName],vars[mistagVarName]))
                th2BKG.Write()
		print "---------------------------------------------------------------------------------------------------------------"
	        res=[]
		print "Channel =" , channel
	        OUTT=th2Sig.Chi2Test(th2BKG,"UW P CHI2/NDF")
	        print "Chi2 for 2D plot", OUTT
		print "---------------------------------------------------------------------------------------------------------------"
		
	     
	        Pdf2D[channel].plotOn(ttframe[channel],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel].GetName()+","+myRHP_2D["TT"+channel].GetName()+","+myRHP_2D["Zbb"+channel].GetName()+","+myRHP_2D["Zbx"+channel].GetName()+","+myRHP_2D["Zxx"+channel].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kBlue-7),
                         RooFit.LineWidth(1)
	    		)

	    
	        Pdf2D[channel].plotOn(ttframe[channel],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel].GetName()+","+myRHP_2D["TT"+channel].GetName()+","+myRHP_2D["Zbb"+channel].GetName()+","+myRHP_2D["Zbx"+channel].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kGreen-7),
                         RooFit.LineWidth(1)
	    		)	
	        Pdf2D[channel].plotOn(ttframe[channel],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel].GetName()+","+myRHP_2D["TT"+channel].GetName()+","+myRHP_2D["Zbb"+channel].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kRed-7),
                         RooFit.LineWidth(1)
	    		)			
	        Pdf2D[channel].plotOn(ttframe[channel],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel].GetName()+","+myRHP_2D["TT"+channel].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kYellow-7),
                         RooFit.LineWidth(1)
	    		)			
	        Pdf2D[channel].plotOn(ttframe[channel],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kBlack-7),
                         RooFit.LineWidth(1)
	    		)			
	        AlldataAndMCList[dataLabel+channel].plotOn(ttframe[channel])
	


                mistagframe[channel] = vars[mistagVarName].frame()
	        AlldataAndMCList[dataLabel+channel].plotOn(mistagframe[channel])

	        Pdf2D[channel].plotOn(mistagframe[channel],
                     RooFit.LineColor(kBlue),
                     RooFit.LineWidth(2)
                     )
		     
	        chid=mistagframe[channel].chiSquare()
   	        print "Chi square for Var 2:",chid
	    	     
	        Pdf2D[channel].plotOn(mistagframe[channel],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel].GetName()+","+myRHP_2D["TT"+channel].GetName()+","+myRHP_2D["Zbb"+channel].GetName()+","+myRHP_2D["Zbx"+channel].GetName()+","+myRHP_2D["Zxx"+channel].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kBlue-7),
                         RooFit.LineWidth(1)
	    		)
	        Pdf2D[channel].plotOn(mistagframe[channel],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel].GetName()+","+myRHP_2D["TT"+channel].GetName()+","+myRHP_2D["Zbb"+channel].GetName()+","+myRHP_2D["Zbx"+channel].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kGreen-7),
                         RooFit.LineWidth(1)
	    		)	
	        Pdf2D[channel].plotOn(mistagframe[channel],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel].GetName()+","+myRHP_2D["TT"+channel].GetName()+","+myRHP_2D["Zbb"+channel].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kRed-7),
                         RooFit.LineWidth(1)
	    		)			
	        Pdf2D[channel].plotOn(mistagframe[channel],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel].GetName()+","+myRHP_2D["TT"+channel].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kYellow-7),
                         RooFit.LineWidth(1)
	    		)			
	        Pdf2D[channel].plotOn(mistagframe[channel],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kBlack-7),
                         RooFit.LineWidth(1)
	    		)
	        AlldataAndMCList[dataLabel+channel].plotOn(mistagframe[channel])

	    print "---------------------------------------------------------------------------------------------------------------"
	    res=[]
	    OUTT=th2Sigall.Chi2Test(th2BKGall,"UW P CHI2/NDF")
	    print "Chi2 for 2D plot", OUTT
	    print "---------------------------------------------------------------------------------------------------------------"
            th2Sigall.Write()
            th2BKGall.Write()


    CANVAS.cd(1)
    Pdf2D["El"].paramOn(ttframe["El"],AlldataAndMCList[dataLabel+"El"])
    ttframe["El"].Draw()		
    CANVAS.cd(2)
    Pdf2D["El"].paramOn(mistagframe["El"],AlldataAndMCList[dataLabel+"El"])
    mistagframe["El"].Draw()
    CANVAS.cd(3)
    Pdf2D["Mu"].paramOn(ttframe["Mu"],AlldataAndMCList[dataLabel+"Mu"])
    ttframe["Mu"].Draw()		
    CANVAS.cd(4)
    Pdf2D["Mu"].paramOn(mistagframe["Mu"],AlldataAndMCList[dataLabel+"Mu"])
    mistagframe["Mu"].Draw()
    CANVAS.SaveAs("FIT.pdf")
    
    plot.Close()
    bla
