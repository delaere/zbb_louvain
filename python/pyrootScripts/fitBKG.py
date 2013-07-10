#import
from ROOT import *
from optparse import OptionParser
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
lib_path2 = os.path.abspath('../analysisScripts/')
sys.path.append(lib_path2)
#parser options
parser = OptionParser()
parser.add_parser = OptionParser()
parser.add_option("-p", "--ptj1", dest="ptj1",
                  help="which sample to analyse.", metavar="PTJ1")
parser.add_option("-q", "--ptj2", dest="ptj2",
                  help="which sample to analyse.", metavar="PTJ2")
		  
parser.add_option("-b", "--jetbin", dest="jetbin",
                  help="which sample to analyse.", metavar="JETBIN")

parser.add_option("-v", "--binvar1", dest="binvar1",
                  help="which sample to analyse.", metavar="BINVAR1")

parser.add_option("-w", "--binvar2", dest="binvar2",
                  help="which sample to analyse.", metavar="BINVAR2")

parser.add_option("-n", "--numbersf", dest="numbersf",
                  help="which sample to analyse.", metavar="NUMBERSF")
parser.add_option("-m", "--ptz", dest="ptz",
                  help="which sample to analyse.", metavar="PTZ")

(options, args) = parser.parse_args()

#####################################
gROOT.SetStyle("Plain")
#####################################

# to adjust by user:
channelList   = ["Mu","El"]
jetcategoryList = ["2jet", "P2jet"]
dataLabel = "DATA"

useDYptBins = True
useDYjetBins = False
useMCTruth = True
from listForRDS import MCsampleList, totsampleList, DYrew
MCsampleList.remove("ZH125")
totsampleList.remove("ZH125")
if useMCTruth :
  totsampleList.remove("Zno")
  MCsampleList.remove("Zno")
              
#choose WP:
#WP        = "HPHPMETsig"

WP        = "HPHEMETsigWidell"
#WP        = "HPHPMETsigWidell"

#extraCut  = "&jetmetMETsignificance < 10 &mlphiggsvsbkg_125_comb_ML<0.5 & jetmetbjet1pt>20 & jetmetbjet2pt>20 "
#extraCut  = "&jetmetMETsignificance < 10 &mlphiggsvsbkg_125_comb_ML<0.5 & jetmetbjet1pt>"+ptj1+" & jetmetbjet2pt>"+ptj2
ptj1="40."#str(options.ptj1)
ptj2="25."#str(options.ptj2)
jetbin=str(options.jetbin)
numbersf=str(options.numbersf)
ptz="20."#str(options.ptz)

if jetbin == "2":
  extraCut = "jetmetMETsignificance < 10 && jetmetMETsignificance != 0 && ((eventSelectiondijetM<80||eventSelectiondijetM>150) &&jetmetnj==2)&& jetmetbjet1pt>"+ptj1+" && jetmetbjet2pt>"+ptj2+" "
elif jetbin == "3":
  extraCut = "jetmetMETsignificance < 10 && jetmetMETsignificance != 0 && ((eventSelectiondijetM<50||eventSelectiondijetM>150) &&jetmetnj>2) && jetmetbjet1pt>"+ptj1+" && jetmetbjet2pt>"+ptj2+" "
else:
  extraCut = "jetmetMETsignificance < 10 && jetmetMETsignificance != 0 && (((eventSelectiondijetM<80||eventSelectiondijetM>150) &&jetmetnj==2)||((eventSelectiondijetM<50||eventSelectiondijetM>150) &&jetmetnj>2))&& jetmetbjet1pt>"+ptj1+" && jetmetbjet2pt>"+ptj2 +" "

extraCutWithoutPtZ = extraCut

print "extraCut=", extraCut
print "fit bining=", int(options.binvar1),"X",int(options.binvar2)
print "jetbin=", jetbin
print "numbersf=", numbersf

keys      = False

extraCutList = {"mwnn"     : "jetmetMETsignificance < 10",#mlphiggsvsbkg_125_comb_ML>-0.1&mlphiggsvsbkg_125_comb_ML<0.5",
                "btag"    : "jetmetMETsignificance < 10",#mlphiggsvsbkg_125_comb_ML>-0.1&mlphiggsvsbkg_125_comb_ML<0.5",
		}
		
print "extraCut=", extraCut

ttbarVarList  = ["mwnn"]
mistagVarList = ["btag"]
#if channel=="Mu": ttbarVarList  = [ "mmumu" ]
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

ttMCNameList = ["TT-FullLept","ZZ"]
# maybe different if using QCD:
mistagMCNameList  = ["Zxx","Zbx","Zbb"]
dataNameList      = [dataLabel]
MCNameList        = MCsampleList #ttMCNameList+mistagMCNameList
dataAndMCNameList = totsampleList #ttMCNameList+mistagMCNameList+dataNameList

AlldataAndMCList = {}
dataAndMCList = {}
dataAndMCListZH = {}

category={"HE"         : "rc_eventSelection_5",
          "HP"         : "rc_eventSelection_6",
          "HEMET"      : "rc_eventSelection_7",
          "HPMET"      : "rc_eventSelection_8",
          "HPHEMETsig" : "rc_eventSelection_17",
          "HPHPMETsig" : "rc_eventSelection_18",
          "HPHEMETsigWidell" : "rc_eventSelection_11",
          "HPHPMETsigWidell" : "rc_eventSelection_12",
          }


#mlpZbbvsTT_mu_MM_N
#mlpDYvsTT_2012
varNamesList = { "btag"  : "jetmetbjetProdCSVdisc"   ,
		 "mwnn"  : "mlpDYvsTT_2012",
                 "w_b_HE"    : "BtaggingReweightingHE"  ,
                 "w_b_HP"    : "BtaggingReweightingHP"  ,
                 "w_b_HEHE"  : "BtaggingReweightingHEHE",
                 "w_b_HEHEMET"  : "BtaggingReweightingHEHE",
                 "w_b_HPHEMETsig"  : "BtaggingReweightingHEHP",
                 "w_b_HPHP"  : "BtaggingReweightingHPHP",
                 "w_b_HPHPMETsig"  : "BtaggingReweightingHPHP",
                 "w_b_HPHEMETsigWidell"  : "BtaggingReweightingHEHP",
                 "w_b_HPHPMETsigWidell"  : "BtaggingReweightingHPHP",
                 "w_lep"     : "LeptonsReweightingweight",
                 "jmul"      : "jetmetnj",
                 "w_lumi"    : "lumiReweightingLumiWeight",
                 "nj" : "mcSelectionnJets",
                 "llpt" : "mcSelectionllpt",
                }

min = {
  "btag"   :   0.244*0.679,
  #"btag"   :   0.679*0.679,
  "mwnn"   :  0.0,
  "w_b_HE" : 0. , 
  "w_b_HP"    : 0.,
  "w_b_HEHE"  : 0.,
  "w_b_HEHEMET"  : 0.,
  "w_b_HPHEMETsig"  : 0.,
  "w_b_HPHPMETsig"  : 0.,
  "w_b_HPHEMETsigWidell"  : 0.,
  "w_b_HPHPMETsigWidell"  : 0.,
  "w_b_HPHP"  : 0.,
  "w_lep"     : 0.,
  "w_lumi"    : 0.,
  "jmul"      :2.
  }

max = {"btag" :    1.,
       "mwnn" :   1.0,
       "w_b_HE"    : 2., 
       "w_b_HP"    : 2.,
       "w_b_HEHE"  : 2.,
       "w_b_HEHEMET"  : 2.,
       "w_b_HPHEMETsig"  : 2.,
       "w_b_HPHPMETsig"  : 2.,
       "w_b_HPHEMETsigWidell"  : 2.,
       "w_b_HPHPMETsigWidell"  : 2.,
       "w_b_HPHP"  : 2.,
       "w_lep"     : 2.,
       "w_lumi"    : 2.,
       "jmul"      : 8. 
       }

bins = {"btag" :   int(options.binvar1),
        "mwnn" :   int(options.binvar2),
        "w_b_HE"    : 100, 
        "w_b_HP"    : 100,
        "w_b_HEHE"  : 100,
        "w_b_HEHEMET"  : 100,
        "w_b_HPHEMETsig"  : 100,
        "w_b_HPHPMETsig"  : 100,
        "w_b_HPHEMETsigWidell"  : 100,
        "w_b_HPHPMETsigWidell"  : 100,
        "w_b_HPHP"  : 100,
        "w_lep"     : 100,
        "w_lumi"    : 100,
        "jmul"      : 6, 
        }

color = {"msv1" : kRed,
         "btag" : kRed,
         "msv"  : kRed,
         "melel": kYellow,
         "mmumu": kYellow,
         "mwnn_1" :kYellow,
         }

C={}
myFrame={}

#get RDS paths
from globalLists import pathMergedRDS
path = pathMergedRDS

#get file names
fileNameList = {}
from listForRDS import sampleList
sampleList.remove("ZH125")
for sample in sampleList:
  if "DATA" not in sample :
    #if sample in mistagMCNameList : s = "DY"
    #else : s = sample
    s = sample
    for c in ["Mu","El"]:
      fileNameList[sample+c] = path[s+"_"+c+"_MC"]
      #if sample=="Zbb" :
      #  fileNameList["ref"+c] = fileNameList[sample+c]
      #  fileNameList["DY"+c] = fileNameList[sample+c]
  else :
    for c in ["Mu","Ele"]:
      fileNameList[sample+c.replace("Ele","El")] = path["Double"+c+"_DataA"].replace("DataA","Data")
#print file name
for name in fileNameList:
	print name, fileNameList[name]

#get lumi rescalling        
from listForRDS import lumi, Extra_norm		 
		 
def getVariables(varNamesList,varName,dataAndMCListZH) :
    var=varNamesList[varName]
    #y=dataAndMCList["Zl"]
    y=dataAndMCListZH["ZbbMu2jet"].reduce("jetmetnj==0")
    print "var = ", var
    print "ras = ", y.get()
    print "var = ", y.get()[var]
    x = y.get()[var]
    if x :
      if varName in min : x.setMin(min[varName])
      if varName in max : x.setMax(max[varName])
      if varName in bins : x.setBins(bins[varName])
      return x
    else: return 0
    
def getDataAndMC(dataAndMCNameList,dataAndMCList,channel, jetcat) :

    # check ws
    # otherwise: directly rds

    file = {}
    ws   = {}
    myRDS = {}

    print channel

    cutptz = ""
    if channel == "Mu":
      cutptz = " && eventSelectionbestzptMu > " + ptz
    elif channel == "El":
      cutptz = " && eventSelectionbestzptEle > " + ptz
    else:
      print "not found channel=", channel, " aborting"
      exit()	
    extraCut = extraCutWithoutPtZ + cutptz
    print " extraCut for channel = ", channel, " = ", extraCut
    if jetcat=="2jet":
      extraCut+="&&jetmetnj==2"
    elif jetcat=="P2jet":
      extraCut+="&&jetmetnj>2"
    else:
      print "Unknown jetcat=",jetcat," aborting"
      exit()
    for sample in sampleList :
        if ("DY" in sample and sample[-1]=="0" and not useDYptBins) or ("DY" in sample and sample[-1]=="j" and not useDYjetBins) : continue
        print "sample = ", sample
        print "making dataset"
        file[sample+channel] = TFile.Open(fileNameList[sample+channel])
        tree_zbb1 = file[sample+channel].Get("rds_zbb")
        tmpfile=TFile("tmp.root","RECREATE")
        tree_zbb=tree_zbb1.CopyTree(extraCut)
        ws_zbb = file[sample+channel].Get("ws_ras")
        ras_zbb = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())
        rds_zbb = RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)
        
        nEntries = rds_zbb.numEntries()
        if sample == "DY" : 
          if not useMCTruth :
            myRDS["Zbb"+channel+jetcat] = rds_zbb.reduce(category[WP]+"==1" + "&mcSelectioneventType==6")
            myRDS["Zbx"+channel+jetcat] = rds_zbb.reduce(category[WP]+"==1" + "&mcSelectioneventType>=4&mcSelectioneventType<6")
            myRDS["Zxx"+channel+jetcat] = rds_zbb.reduce(category[WP]+"==1" + "&mcSelectioneventType<4&mcSelectioneventType>0")
            myRDS["Zno"+channel+jetcat] = rds_zbb.reduce(category[WP]+"==1" + "&mcSelectioneventType==0")
          else :
            myRDS["Zbb"+channel+jetcat] = rds_zbb.reduce(category[WP]+"==1" + "&(abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)==5 & jetmetnj>1)")
            myRDS["Zbx"+channel+jetcat] = rds_zbb.reduce(category[WP]+"==1" + "&( (abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5)  & jetmetnj>1)")
            myRDS["Zxx"+channel+jetcat] = rds_zbb.reduce(category[WP]+"==1" + "&( (abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)!=5 & jetmetnj>1) || jetmetnj==1 )")
            print "myRDS.numEntries() for ", "Zbb" , " = ", nEntries, ". After stage ", WP, " : ", myRDS["Zbb"+channel+jetcat].numEntries()
            print "myRDS.numEntries() for ", "Zbx" , " = ", nEntries, ". After stage ", WP, " : ", myRDS["Zbx"+channel+jetcat].numEntries()
            print "myRDS.numEntries() for ", "Zxx" , " = ", nEntries, ". After stage ", WP, " : ", myRDS["Zxx"+channel+jetcat].numEntries()
            if not useMCTruth : print "myRDS.numEntries() for ", "Zno" , " = ", nEntries, ". After stage ", WP, " : ", myRDS["Zno"+channel+jetcat].numEntries()
        elif ("DY" in sample and sample[-1]=="0" and useDYptBins) or ("DY" in sample and sample[-1]=="j" and useDYjetBins) :
          if not useMCTruth :
            myRDS["Zbb"+channel+jetcat].append(rds_zbb.reduce(category[WP]+"==1" + "&mcSelectioneventType==6"))
            myRDS["Zbx"+channel+jetcat].append(rds_zbb.reduce(category[WP]+"==1" + "&mcSelectioneventType>=4&mcSelectioneventType<6"))
            myRDS["Zxx"+channel+jetcat].append(rds_zbb.reduce(category[WP]+"==1" + "&mcSelectioneventType<4&mcSelectioneventType>0"))
            myRDS["Zno"+channel+jetcat].append(rds_zbb.reduce(category[WP]+"==1" + "&mcSelectioneventType==0"))
          else :
            myRDS["Zbb"+channel+jetcat].append(rds_zbb.reduce(category[WP]+"==1" + "&abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)==5"))
            myRDS["Zbx"+channel+jetcat].append(rds_zbb.reduce(category[WP]+"==1" + "&( (abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5) )"))
            myRDS["Zxx"+channel+jetcat].append(rds_zbb.reduce(category[WP]+"==1" + "&abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)!=5"))
            print "myRDS.numEntries() for ", "Zbb" , " = ", nEntries, ". After stage ", WP, " : ", myRDS["Zbb"+channel+jetcat].numEntries()
            print "myRDS.numEntries() for ", "Zbx" , " = ", nEntries, ". After stage ", WP, " : ", myRDS["Zbx"+channel+jetcat].numEntries()
            print "myRDS.numEntries() for ", "Zxx" , " = ", nEntries, ". After stage ", WP, " : ", myRDS["Zxx"+channel+jetcat].numEntries()
            if not useMCTruth : print "myRDS.numEntries() for ", "Zno" , " = ", nEntries, ". After stage ", WP, " : ", myRDS["Zno"+channel+jetcat].numEntries()
        else :
          myRDS[sample+channel+jetcat]=rds_zbb.reduce(category[WP]+"==1")
          print "myRDS.numEntries() for ", sample , " = ", nEntries, ". After stage ", WP, " : ", myRDS[sample+channel+jetcat].numEntries()
    for key in myRDS :      
      if "Widell" in WP :
        print "Do not apply narrow ll window requirement"
      else:  
        if "El" in key : myRDS[key] = myRDS[key].reduce("eventSelectionbestzmassEle<106&eventSelectionbestzmassEle>76")
        if "Mu" in key : myRDS[key] = myRDS[key].reduce("eventSelectionbestzmassMu<106&eventSelectionbestzmassMu>76")        
        print "#entries for sample", sample , " at WP ",  WP ," =", myRDS[key].numEntries() 
      dataAndMCList[key]=myRDS[key]
    return 

def setWeights(dataAndMCList,MCNameList,vars,channel,jetcat) :
    for name in MCNameList :      
      if True : ext="Extra_norm"
      else : ext=""
      if channel=="Mu" : ch="MuMuChannel"
      else : ch="EEChannel"
      #if useDYptBins : llptFormula = "*( (@3<50.)*1.+(@3>=50.)*(@3<70.)*"+DYrew["50-70"]+"+(@3>=70.)*(@3<100.)*"+DYrew["70-100"]+"+(@3>=100.)*(@3<180.)*"+DYrew["100-180"]+"+(@3>=180.)*"+DYrew["180"]+" )"
      if useDYptBins : llptFormula = "*( (@3<50.)*1.+(@3>=50.)*(@3<70.)*"+DYrew[ch+"DY50-70"+ext]+"+(@3>=70.)*(@3<100.)*"+DYrew[ch+"DY70-100"+ext]+"+(@3>=100.)*(@3<180.)*"+DYrew[ch+"DY100"+ext]+"+(@3>=180.)*"+DYrew[ch+"DY180"+ext]+" )"
      else : llptFormula = "*1."

      if useDYjetBins : njFormula = "*( (@4==0)*1.+(@4==1)*"+DYrew["1j"]+"+(@4==2)*"+DYrew["2j"]+"+(@4==3)*"+DYrew["3j"]+"+(@4==4)*"+DYrew["4j"]+"+(@4>4)*1. )"
      else : njFormula = "*1."
      
      w = RooFormulaVar("w","w", "@0*@1*@2", RooArgList(vars["w_lep"],vars["w_lumi"],vars["w_b_"+WP]))
      if name in ["Zno","Zxx","Zbx","Zbb"] :
        w = RooFormulaVar("w","w", "@0*@1*@2"+llptFormula+njFormula, RooArgList(vars["w_lep"],vars["w_lumi"],vars["w_b_"+WP],vars["llpt"],vars["nj"]))
      print "***BEFORE numEntries() = ", dataAndMCList[name+channel+jetcat].numEntries()
      dataAndMCList[name+channel+jetcat].addColumn(w)

    for name in MCNameList :
        dataAndMCList[name+channel+jetcat] = RooDataSet(dataAndMCList[name+channel+jetcat].GetName(),
                                         dataAndMCList[name+channel+jetcat].GetName(),
                                         dataAndMCList[name+channel+jetcat],
                                         dataAndMCList[name+channel+jetcat].get(),
                                         "",
                                         w.GetName())
        print "***AFTER numEntries() for sample ", name , " = ", dataAndMCList[name+channel+jetcat].numEntries()
        print "sumEntries() = ", dataAndMCList[name+channel+jetcat].sumEntries()
    return

def makePdfList(dataAndMCList, mcName, var, RDH, RHP, var2, channel, jetcat ) :
    varName=var.GetName()
    name=mcName

    print "mcName    = ", mcName
    print "varName   = ", varName
    print "name      = ", name

    print "**** before cut: number of entries = " , dataAndMCList[mcName+jetcat].numEntries()

    if mcName=="Zxx"+channel:
        print "Zxx dataset, going to cut on udsgc flav"
        dataAndMCList[name+jetcat] = dataAndMCList[mcName+jetcat].reduce("abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)!=5")
    	print " Zxx after reduce = ", dataAndMCList[name+jetcat].numEntries()
    if mcName=="Zbx"+channel:
        print "Zbx dataset, going to cut on c flav"
        dataAndMCList[name+jetcat]=dataAndMCList[mcName+jetcat].reduce("(abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)==5) ||(abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)!=5) ")
    if mcName=="Zbb"+channel:
        print "Zbb dataset, going to cut on b flav"
        dataAndMCList[name+jetcat]=dataAndMCList[mcName+jetcat].reduce("abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)==5")
    else:
        dataAndMCList[name+jetcat]=dataAndMCList[mcName+jetcat]
        print "DID NOT MATCH SAMPLE NAME"

    print "**** after cut: number of entries = " , dataAndMCList[mcName+jetcat].numEntries()
    print "**** after cut: number of entries = " , dataAndMCList[name+jetcat].numEntries()
        
    # todo: something goes wrong here with the cut on the dataset. Somethow it is not given to the RooDataHist correctly
    
    if var2:
        print "var2 for ", name+jetcat
        RDH[name+jetcat] = RooDataHist("RDH_"+name+jetcat,"RDH_"+name+jetcat, RooArgSet(var,var2), dataAndMCList[name+jetcat]   )
        RHP[name+jetcat] = RooHistPdf( "RHP_"+name+jetcat,"RHP_"+name+jetcat, RooArgSet(var,var2), RDH[name+jetcat] )
    elif keys:
        # I belive it never enters here (I don't know what dataAndMCs is)
	print "entery keys, not really supported, aborting"
	exit()
        RKP[name+jetcat] = RooKeysPdf( "RKP_tt_"+name+jetcat,"myRKP_tt_"+name+jetcat, var, dataAndMCs  )
    else :    
        print "else for ", name+jetcat
        RDH[name+jetcat] = RooDataHist("RDH_"+name+jetcat,"RDH_"+name+jetcat, RooArgSet(var), dataAndMCList[name+jetcat]   )
        RHP[name+jetcat] = RooHistPdf( "RHP_"+name+jetcat,"RHP_"+name+jetcat, RooArgSet(var), RDH[name+jetcat] )
    # else:    
    # parameterized?
    return

#############################################################################################################
def main():

    plot = TFile("Fit_result.root","RECREATE")

    vars = {}
    frame ={}
    for channel in channelList:
      for jetcat in jetcategoryList:
        getDataAndMC(dataAndMCNameList, AlldataAndMCList,channel,jetcat)
        getDataAndMC(["ref"], dataAndMCListZH,channel,jetcat)
    
    print " pass get Data and MC "
    
    for channel in channelList:
        for mcnames in MCNameList :
            for ttVarName in ttbarVarList:
	      for jetcat in jetcategoryList:
	        #print "in loop reduce extra cut"
                AlldataAndMCList[mcnames+channel+jetcat] = AlldataAndMCList[mcnames+channel+jetcat].reduce(extraCutList[ttVarName])
	    
    for varName in varNamesList : vars[varName] = getVariables(varNamesList,varName,dataAndMCListZH)
    
    for channel in channelList:   
      for jetcat in jetcategoryList:
        setWeights(AlldataAndMCList,MCNameList,vars,channel,jetcat)

    print "pass reweighting" 

    if (numbersf=="7"):
      SF_zbb_2jet=RooRealVar("SF_zbb_2jet","SF_zbb_2jet",1.,0.5, 2.)
      SF_zbx_2jet=RooRealVar("SF_zbx_2jet","SF_zbx_2jet",1.,0.5, 2.)
      SF_zxx_2jet=RooRealVar("SF_zxx_2jet","SF_zxx_2jet",1.,0.5, 2.)
      SF_zbb_P2jet=RooRealVar("SF_zbb_P2jet","SF_zbb_P2jet",1.,0.5, 2.)
      SF_zbx_P2jet=RooRealVar("SF_zbx_P2jet","SF_zbx_P2jet",1.,0.5, 2.)
      SF_zxx_P2jet=RooRealVar("SF_zxx_P2jet","SF_zxx_P2jet",1.,0.5, 2.)
    
    elif (numbersf=="5ZbbZbx"):
      SF_zbb_2jet=RooRealVar("SF_zbb_2jet","SF_zbb_2jet",1.,0.5, 2.)
      SF_zbx_2jet=RooRealVar("SF_zbb_2jet","SF_zbx_2jet",1.,0.5, 2.)
      SF_zxx_2jet=RooRealVar("SF_zxx_2jet","SF_zxx_2jet",1.,0.5, 2.)
      SF_zbb_P2jet=RooRealVar("SF_zbb_P2jet","SF_zbb_P2jet",1.,0.5, 2.)
      SF_zbx_P2jet=RooRealVar("SF_zbb_P2jet","SF_zbx_P2jet",1.,0.5, 2.)
      SF_zxx_P2jet=RooRealVar("SF_zxx_P2jet","SF_zxx_P2jet",1.,0.5, 2.)
    
    elif (numbersf=="5ZxxZbx"):
      SF_zbb_2jet=RooRealVar("SF_zbb_2jet","SF_zbb_2jet",1.,0.5, 2.)
      SF_zbx_2jet=RooRealVar("SF_zxx_2jet","SF_zbx_2jet",1.,0.5, 2.)
      SF_zxx_2jet=RooRealVar("SF_zxx_2jet","SF_zxx_2jet",1.,0.5, 2.)
      SF_zbb_P2jet=RooRealVar("SF_zbb_P2jet","SF_zbb_P2jet",1.,0.5, 2.)
      SF_zbx_P2jet=RooRealVar("SF_zxx_P2jet","SF_zbx_P2jet",1.,0.5, 2.)
      SF_zxx_P2jet=RooRealVar("SF_zxx_P2jet","SF_zxx_P2jet",1.,0.5, 2.)
    elif (numbersf=="5"):
      SF_zbb_2jet=RooRealVar("SF_zbb_2jet","SF_zbb_2jet",1.,0.5, 2.)
      SF_zbx_2jet=RooRealVar("SF_zbb_2jet","SF_zbx_2jet",1.,0.5, 2.)
      SF_zxx_2jet=RooRealVar("SF_zxx_2jet","SF_zxx_2jet",1.,0.5, 2.)
      SF_zbb_P2jet=RooRealVar("SF_zbb_P2jet","SF_zbb_P2jet",1.,0.5, 2.)
      SF_zbx_P2jet=RooRealVar("SF_zxx_P2jet","SF_zbx_P2jet",1.,0.5, 2.)
      SF_zxx_P2jet=RooRealVar("SF_zxx_P2jet","SF_zxx_P2jet",1.,0.5, 2.)

    elif (numbersf=="5P"):
      SF_zbb_2jet=RooRealVar("SF_zbb_2jet","SF_zbb_2jet",1.,0.5, 2.)
      SF_zbx_2jet=RooRealVar("SF_zxx_2jet","SF_zbx_2jet",1.,0.5, 2.)
      SF_zxx_2jet=RooRealVar("SF_zxx_2jet","SF_zxx_2jet",1.,0.5, 2.)
      SF_zbb_P2jet=RooRealVar("SF_zbb_P2jet","SF_zbb_P2jet",1.,0.5, 2.)
      SF_zbx_P2jet=RooRealVar("SF_zbb_P2jet","SF_zbx_P2jet",1.,0.5, 2.)
      SF_zxx_P2jet=RooRealVar("SF_zxx_P2jet","SF_zxx_P2jet",1.,0.5, 2.)
    elif (numbersf=="4Rad"):
      SF_zbb_2jet=RooRealVar("SF_zbb_2jet","SF_zbb_2jet",1.,0.5, 2.)
      SF_zbx_2jet=RooRealVar("SF_zbx_2jet","SF_zbx_2jet",1.,0.5, 2.)
      SF_zxx_2jet=RooRealVar("SF_zxx_2jet","SF_zxx_2jet",1.,0.5, 2.)
      SF_zbb_P2jet=SF_zbx_2jet
      SF_zbx_P2jet=SF_zbx_2jet
      SF_zxx_P2jet=SF_zxx_2jet
    else:
      print "Unkwnonwn value for numbersf=",numbersf, " valid values are 7, 5ZbbZbx, 5ZxxZbx, 5, 5P"
    SF_tt_m=RooRealVar("SF_tt_m","SF_tt",1.,0.5, 2.)    
    SF_zz=RooRealVar("SF_zz","SF_zz",1.,1. , 1.)

    SF={
    	"TT-FullLeptEl2jet":SF_tt_m,
        "ZbbEl2jet":SF_zbb_2jet,
        "ZbxEl2jet":SF_zbx_2jet,
	"ZxxEl2jet":SF_zxx_2jet,
	"ZZEl2jet":SF_zz,
	"TT-FullLeptMu2jet":SF_tt_m,
        "ZbbMu2jet":SF_zbb_2jet,
        "ZbxMu2jet":SF_zbx_2jet,
	"ZxxMu2jet":SF_zxx_2jet,
	"ZZMu2jet":SF_zz,

    	"TT-FullLeptElP2jet":SF_tt_m,
        "ZbbElP2jet":SF_zbb_P2jet,
        "ZbxElP2jet":SF_zbx_P2jet,
        "ZxxElP2jet":SF_zxx_P2jet,
	"ZZElP2jet":SF_zz,
	"TT-FullLeptMuP2jet":SF_tt_m,
        "ZbbMuP2jet":SF_zbb_P2jet,
        "ZbxMuP2jet":SF_zbx_P2jet,
	"ZxxMuP2jet":SF_zxx_P2jet,
 	"ZZMuP2jet":SF_zz
	}
    
    flavor = RooCategory("cat","cat")
    flavor.defineType("El2jet")
    flavor.defineType("ElP2jet")
    flavor.defineType("Mu2jet")
    flavor.defineType("MuP2jet") 

    flavor.setLabel("El2jet")
    AlldataAndMCList[dataLabel+"El2jet"].addColumn(flavor)

    flavor.setLabel("ElP2jet")
    AlldataAndMCList[dataLabel+"ElP2jet"].addColumn(flavor)

    flavor.setLabel("Mu2jet")
    AlldataAndMCList[dataLabel+"Mu2jet"].addColumn(flavor)

    flavor.setLabel("MuP2jet")
    AlldataAndMCList[dataLabel+"MuP2jet"].addColumn(flavor)
   
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
      for jetcat in jetcategoryList:
        PdfList2D[channel+jetcat]    = RooArgList()
        YieldList2D[channel+jetcat]   = RooArgList()

        ### 2 variables, matching the names "var1" and "var2" in the RooDataSet myRDS

        if len(ttbarVarList) and len(mistagVarList):
            for ttVarName in ttbarVarList:  
	        for mistagVarName in mistagVarList:
    	            for  mcnames in MCNameList:
		       
		        ### make 1D-PDF
		        print "make 1D-PDF"
		    
		        makePdfList(AlldataAndMCList, mcnames+channel,vars[ttVarName],myRDH_2D, myRHP_2D ,vars[mistagVarName],channel, jetcat)
		      
		        PdfList2D[channel+jetcat].add(myRHP_2D[mcnames+channel+jetcat])
                        if channel=="Mu" : c="MuMuChannel"
                        else : c="EEChannel"
		        N_exp[mcnames+channel+jetcat]=RooConstVar("N_exp_"+mcnames+channel+jetcat,"N_exp_"+mcnames+channel+jetcat,
                                               (AlldataAndMCList[mcnames+channel+jetcat].sumEntries()*(lumi["DATA"]/lumi[mcnames]/Extra_norm[c+mcnames])))
						     
		        N[mcnames+channel+jetcat] = RooFormulaVar("N_"+mcnames,"N_"+mcnames+channel+jetcat,"@0*@1",RooArgList(N_exp[mcnames+channel+jetcat],SF[mcnames+channel+jetcat]))
		  
		        print "yields expected for ",mcnames+channel+jetcat,N_exp[mcnames+channel+jetcat]
		      		    
		        YieldList2D[channel+jetcat].add(N[mcnames+channel+jetcat])
				          
        print "make pdf"
        print PdfList2D[channel+jetcat],YieldList2D[channel+jetcat]
        Pdf2D[channel+jetcat] = RooAddPdf("Pdf2D"+channel+jetcat,"Pdf2D"+channel+jetcat,PdfList2D[channel+jetcat],YieldList2D[channel+jetcat])

 
 
    simPdf = RooSimultaneous("sim","sim",flavor)
    for channel in channelList:
      for jetcat in jetcategoryList:
        simPdf.addPdf(Pdf2D[channel+jetcat],channel+jetcat)
        
    DATA = RooDataSet("DATA","DATA",AlldataAndMCList[dataLabel+"El2jet"],AlldataAndMCList[dataLabel+"El2jet"].get())
    print "before appending nbr data :",DATA.numEntries()
    DATA.append(AlldataAndMCList[dataLabel+"Mu2jet"])
    DATA.append(AlldataAndMCList[dataLabel+"ElP2jet"])
    DATA.append(AlldataAndMCList[dataLabel+"MuP2jet"])
    print "after appending nbr data :",DATA.numEntries()
   
    print "reach fit level"
    simPdf.fitTo(DATA)#,Verbose(true))
    #for channel in channelList:
    #	Pdf2D[channel].fitTo(AlldataAndMCList[dataLabel+channel])

    ttframe={}
    mistagframe={}

    CANVAS = TCanvas("CANVAS","CANVAS",1200,600)
    CANVAS.Divide(4,2)
    
    for ttVarName in ttbarVarList:  
        for mistagVarName in mistagVarList:
            th2Sigall = TH2D("Sigall","Sigall",vars[ttVarName].getBins(),vars[ttVarName].getMin(),vars[ttVarName].getMax(),vars[mistagVarName].getBins(),vars[mistagVarName].getMin(),vars[mistagVarName].getMax())
	    th2BKGall = TH2D("BKGall","BKGall",vars[ttVarName].getBins(),vars[ttVarName].getMin(),vars[ttVarName].getMax(),vars[mistagVarName].getBins(),vars[mistagVarName].getMin(),vars[mistagVarName].getMax())

	    for channel in channelList:
	      for jetcat in jetcategoryList:
                ttframe[channel+jetcat] = vars[ttVarName].frame()
     	        AlldataAndMCList[dataLabel+channel+jetcat].plotOn(ttframe[channel+jetcat])
	    
	        th2Sig = TH2D("Sig","Sig",vars[ttVarName].getBins(),vars[ttVarName].getMin(),vars[ttVarName].getMax(),vars[mistagVarName].getBins(),vars[mistagVarName].getMin(),vars[mistagVarName].getMax())
                AlldataAndMCList[dataLabel+channel+jetcat].fillHistogram(th2Sig, RooArgList(vars[ttVarName],vars[mistagVarName]))	    
                AlldataAndMCList[dataLabel+channel+jetcat].fillHistogram(th2Sigall, RooArgList(vars[ttVarName],vars[mistagVarName]))	    
	        th2Sig.Write()
	        Pdf2D[channel+jetcat].plotOn(ttframe[channel+jetcat],
                     RooFit.LineColor(kBlue),
                     RooFit.LineWidth(2)
                     )

	        chi=ttframe[channel+jetcat].chiSquare()
   	        print "Chi square for Var 1:",chi
	    
	        th2BKG = TH2D("BKG","BKG",vars[ttVarName].getBins(),vars[ttVarName].getMin(),vars[ttVarName].getMax(),vars[mistagVarName].getBins(),vars[mistagVarName].getMin(),vars[mistagVarName].getMax())
                Pdf2D[channel+jetcat].fillHistogram(th2BKG, RooArgList(vars[ttVarName],vars[mistagVarName]))
                Pdf2D[channel+jetcat].fillHistogram(th2BKGall, RooArgList(vars[ttVarName],vars[mistagVarName]))
                th2BKG.Write()
		print "---------------------------------------------------------------------------------------------------------------"
	        res=[]
		print "Channel =" , channel+jetcat
	        OUTT=th2Sig.Chi2Test(th2BKG,"UW P CHI2/NDF")
	        print "Chi2 for 2D plot", OUTT
		print "---------------------------------------------------------------------------------------------------------------"
		
	     
	        Pdf2D[channel+jetcat].plotOn(ttframe[channel+jetcat],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel+jetcat].GetName()+","+myRHP_2D["TT-FullLept"+channel+jetcat].GetName()+","+myRHP_2D["Zbb"+channel+jetcat].GetName()+","+myRHP_2D["Zbx"+channel+jetcat].GetName()+","+myRHP_2D["Zxx"+channel+jetcat].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kBlue-7),
                         RooFit.LineWidth(1)
	    		)

	    
	        Pdf2D[channel+jetcat].plotOn(ttframe[channel+jetcat],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel+jetcat].GetName()+","+myRHP_2D["TT-FullLept"+channel+jetcat].GetName()+","+myRHP_2D["Zbb"+channel+jetcat].GetName()+","+myRHP_2D["Zbx"+channel+jetcat].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kGreen-7),
                         RooFit.LineWidth(1)
	    		)	
	        Pdf2D[channel+jetcat].plotOn(ttframe[channel+jetcat],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel+jetcat].GetName()+","+myRHP_2D["TT-FullLept"+channel+jetcat].GetName()+","+myRHP_2D["Zbb"+channel+jetcat].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kRed-7),
                         RooFit.LineWidth(1)
	    		)			
	        Pdf2D[channel+jetcat].plotOn(ttframe[channel+jetcat],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel+jetcat].GetName()+","+myRHP_2D["TT-FullLept"+channel+jetcat].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kYellow-7),
                         RooFit.LineWidth(1)
	    		)			
	        Pdf2D[channel+jetcat].plotOn(ttframe[channel+jetcat],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel+jetcat].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kBlack),
                         RooFit.LineWidth(1)
	    		)			
	        AlldataAndMCList[dataLabel+channel+jetcat].plotOn(ttframe[channel+jetcat])
	


                mistagframe[channel+jetcat] = vars[mistagVarName].frame()
	        AlldataAndMCList[dataLabel+channel+jetcat].plotOn(mistagframe[channel+jetcat])

	        Pdf2D[channel+jetcat].plotOn(mistagframe[channel+jetcat],
                     RooFit.LineColor(kBlue),
                     RooFit.LineWidth(2)
                     )
		     
	        chid=mistagframe[channel+jetcat].chiSquare()
   	        print "Chi square for Var 2:",chid
	    	     
	        Pdf2D[channel+jetcat].plotOn(mistagframe[channel+jetcat],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel+jetcat].GetName()+","+myRHP_2D["TT-FullLept"+channel+jetcat].GetName()+","+myRHP_2D["Zbb"+channel+jetcat].GetName()+","+myRHP_2D["Zbx"+channel+jetcat].GetName()+","+myRHP_2D["Zxx"+channel+jetcat].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kBlue-7),
                         RooFit.LineWidth(1)
	    		)
	        Pdf2D[channel+jetcat].plotOn(mistagframe[channel+jetcat],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel+jetcat].GetName()+","+myRHP_2D["TT-FullLept"+channel+jetcat].GetName()+","+myRHP_2D["Zbb"+channel+jetcat].GetName()+","+myRHP_2D["Zbx"+channel+jetcat].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kGreen-7),
                         RooFit.LineWidth(1)
	    		)	
	        Pdf2D[channel+jetcat].plotOn(mistagframe[channel+jetcat],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel+jetcat].GetName()+","+myRHP_2D["TT-FullLept"+channel+jetcat].GetName()+","+myRHP_2D["Zbb"+channel+jetcat].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kRed-7),
                         RooFit.LineWidth(1)
	    		)			
	        Pdf2D[channel+jetcat].plotOn(mistagframe[channel+jetcat],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel+jetcat].GetName()+","+myRHP_2D["TT-FullLept"+channel+jetcat].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kYellow-7),
                         RooFit.LineWidth(1)
	    		)			
	        Pdf2D[channel+jetcat].plotOn(mistagframe[channel+jetcat],
	    		 RooFit.Components(myRHP_2D["ZZ"+channel+jetcat].GetName()),
	                 RooFit.DrawOption("F"),
                         RooFit.LineColor(kBlack),
                         RooFit.FillColor(kBlack),
                         RooFit.LineWidth(1)
	    		)
	        AlldataAndMCList[dataLabel+channel+jetcat].plotOn(mistagframe[channel+jetcat])
		#mistagframe[channel+jetcat].SetStats(0)
		#ttframe[channel+jetcat].SetStats(0)
		

	    print "---------------------------------------------------------------------------------------------------------------"
	    res=[]
	    OUTT=th2Sigall.Chi2Test(th2BKGall,"UW P CHI2/NDF")
	    print "Chi2 for 2D plot", OUTT
	    print "---------------------------------------------------------------------------------------------------------------"
            th2Sigall.Write()
            th2BKGall.Write()


    CANVAS.cd(1)
    Pdf2D["El"+"2jet"].paramOn(ttframe["El"+"2jet"],AlldataAndMCList[dataLabel+"El"+"2jet"])
    ttframe["El"+"2jet"].Draw()		
    CANVAS.cd(2)
    Pdf2D["El"+"2jet"].paramOn(mistagframe["El"+"2jet"],AlldataAndMCList[dataLabel+"El"+"2jet"])
    mistagframe["El"+"2jet"].Draw()
    CANVAS.cd(3)
    Pdf2D["Mu"+"2jet"].paramOn(ttframe["Mu"+"2jet"],AlldataAndMCList[dataLabel+"Mu"+"2jet"])
    ttframe["Mu"+"2jet"].Draw()		
    CANVAS.cd(4)
    Pdf2D["Mu"+"2jet"].paramOn(mistagframe["Mu"+"2jet"],AlldataAndMCList[dataLabel+"Mu"+"2jet"])
    mistagframe["Mu"+"2jet"].Draw()
    
    CANVAS.cd(5)
    Pdf2D["El"+"P2jet"].paramOn(ttframe["El"+"P2jet"],AlldataAndMCList[dataLabel+"El"+"P2jet"])
    ttframe["El"+"P2jet"].Draw()		
    CANVAS.cd(6)
    Pdf2D["El"+"P2jet"].paramOn(mistagframe["El"+"P2jet"],AlldataAndMCList[dataLabel+"El"+"P2jet"])
    mistagframe["El"+"P2jet"].Draw()
    CANVAS.cd(7)
    Pdf2D["Mu"+"P2jet"].paramOn(ttframe["Mu"+"P2jet"],AlldataAndMCList[dataLabel+"Mu"+"P2jet"])
    ttframe["Mu"+"P2jet"].Draw()		
    CANVAS.cd(8)
    Pdf2D["Mu"+"P2jet"].paramOn(mistagframe["Mu"+"P2jet"],AlldataAndMCList[dataLabel+"Mu"+"P2jet"])
    mistagframe["Mu"+"P2jet"].Draw()
    
    
    CANVAS.SaveAs("FIT.pdf")
    
    exit()
    

main()
