"""
Script to fit the backround to the data
"""

from ROOT import *
import inc_Options
from llbbNorm import lumi

 
gROOT.SetBatch()

#formulaName = "formulaPol3_C.so"
#gSystem.Load(formulaName)

class options_():
    #list of samples
    samples = [
        "DATA",
        "DYjets",
        "TTFullLept",
        "TTSemiLept",
        "ZZ",
        "WZ",
        "WW",
        "Wt",
        "Wtbar",
        "ZH125",
        #"ZA_350_70",
        ]
    #template for file name

    #Systematics
    #SYST = "Nominal"
    #SYST = "JESup"
    #SYST = "JESdown"
    #SYST = "JERup"
    #SYST = "JERdown"
    #SYST = "BTAG_bc_up"
    #SYST = "BTAG_bc_down"
    #SYST = "BTAG_light_up"
    #SYST = "BTAG_light_down"
    #SYST = "LEPup"
    SYST = "Nominal"
    print SYST
    
    #template for file name
    path = inc_Options.path.replace("SYST",SYST)

    #Varibales

    vars = {
           "bdtOutputZHAll_Mu_2j":["bdtOutputZHAll_Mu_2j", 40, -1.0, 1.0] ,
           "bdtOutputZHAll_Mu_3j":["bdtOutputZHAll_Mu_3j", 40, -1.0, 1.0] ,	   
           "bdtOutputZHAll_El_2j":["bdtOutputZHAll_El_2j", 40, -1.0, 1.0] ,	   
           "bdtOutputZHAll_El_3j":["bdtOutputZHAll_El_3j", 40, -1.0, 1.0] ,	   

	   }
    #stages
    stages = inc_Options.stagesFit


    print "stages:", stages
    doDYsplit=inc_Options.doDYsplit


    #BTAG weight
    BTAG = inc_Options.BTAG.replace("*","")

    print "BTAG:", BTAG
    
    #define cuts
    cuts = "("+stages["El"]+" || "+stages["Mu"]+")"
    #cuts = "("+stages["El"]+"_idx || "+stages["Mu"]+"_idx)&&jetmetMETsignificance < 10 && jetmetMETsignificance != 0 && ( (boostselectiondijetM<54||boostselectiondijetM>86) || (boostselectionZbbM<197||boostselectionZbbM>403) )"
    print "cut:", cuts
    #define categories
    categories = {
        "El_2j" : stages["El"].replace("_idx","")+"&&jetmetnj==2&&(eventSelectiondijetM<80||eventSelectiondijetM>150)",
        "El_3j" : stages["El"].replace("_idx","")+"&&jetmetnj>2&&(eventSelectiondijetM<50||eventSelectiondijetM>150)",
        "Mu_2j" : stages["Mu"].replace("_idx","")+"&&jetmetnj==2&&(eventSelectiondijetM<80||eventSelectiondijetM>150)",
        "Mu_3j" : stages["Mu"].replace("_idx","")+"&&jetmetnj>2&&(eventSelectiondijetM<50||eventSelectiondijetM>150)"
        }

    print "categories:", categories
    #colour code for the plots
    Colour = {
        "DYjets" : kBlue,
        "Zbb" : kRed,
        "Zbx" : kGreen,
        "Zxx" : kBlue,
        "TTFullLept" : kYellow,
        "TTSemiLept" : kTeal,
        "ZZ" : kMagenta,
        "WZ" : kCyan,
        "WW" : kOrange,
        "Wt" : kSpring,
        "Wtbar" : kSpring,
        "ZH125" : kBlack,
        "ZA_350_70" : kBlack,
        }
    #name of the output file
    outputName = "HistoForLimits.root"
    
#    PlotForCLsRaw = ["bdtOutputZHAll_Mu_2j",
#                     "bdtOutputZHAll_El_2j",
#                     "bdtOutputZHAll_Mu_3j",
#                     "bdtOutputZHAll_El_3j"
#                     ]
#    PlotForCLs = []
#    for plot in PlotForCLsRaw:
#      PlotForCLs.append(plot)
#      
#    for p in PlotForCLs :
#      min={}
#      max={}
#      binning={}
#      min[p] = -1.
#      max[p] = 1.
#      binning[p] = 40
    
#method to make all needed RDS

def JESPlus(name, h, hnum, hden):
  hshift = hnum.Clone()
  hshift.Divide(hden)
  ax = h.GetXaxis()
  hout = TH1D(name, h.GetTitle(), h.GetNbinsX(), ax.GetXmin(), ax.GetXmax())
  
  for i in range (0,  hout.GetNbinsX() + 2):
    v = h.GetBinContent(i)*(1 + 0.5*(hshift.GetBinContent(i) - 1))
    hout.SetBinContent(i, v);
    hout.SetBinError(i, 0);
  
  return hout

#creates down variation for h based on the difference between hnum and hden
def JESMinus(name, h, hnum, hden):
  hshift = hnum.Clone()
  hshift.Divide(hden)
  ax = h.GetXaxis()
  hout = TH1D(name, h.GetTitle(), h.GetNbinsX(), ax.GetXmin(), ax.GetXmax())
  
  for i in range (0,  hout.GetNbinsX() + 2):
    v = h.GetBinContent(i)/(1 + 0.5*(hshift.GetBinContent(i) - 1))
    hout.SetBinContent(i, v);
    hout.SetBinError(i, 0);
  
  return hout

def createRDS(files={"test" : "test.root"}, options=None):
    if options is None : return None
    RDS = {}
    for key in sorted(files.keys()):
    
    
        fileIn = TFile.Open("/nfs/user/cbeluffi/ControlPlots/RDS_JP_V4/RDS_TTFullLept/TTFullLept_Summer12_final.root","read")	
	ws_ras = fileIn.Get("workspace_ras") # get the RooArgSet from the file
	
	ras = RooArgSet(ws_ras.allVars(),ws_ras.allCats()) # define a new RooArgSet using the one you got from the file

	bdtOutputZHAll_Mu_2j= RooRealVar("bdtOutputZHAll_Mu_2j", "bdtOutputZHAll_Mu_2j", -2.0, 2.0) 
	bdtOutputZHAll_El_2j= RooRealVar("bdtOutputZHAll_El_2j", "bdtOutputZHAll_El_2j", -2.0, 2.0)  
	bdtOutputZHAll_Mu_3j= RooRealVar("bdtOutputZHAll_Mu_3j", "bdtOutputZHAll_Mu_3j", -2.0, 2.0) 
	bdtOutputZHAll_El_3j= RooRealVar("bdtOutputZHAll_El_3j", "bdtOutputZHAll_El_3j", -2.0, 2.0)  
	
		
	ras.add(bdtOutputZHAll_Mu_2j)
	ras.add(bdtOutputZHAll_El_2j) 
	ras.add(bdtOutputZHAll_Mu_3j)
	ras.add(bdtOutputZHAll_El_3j) 	
	
        print "Make RDS for", key
        tf = TFile.Open(files[key])
        tree = tf.Get("rds_zbb")
        tmpfile=TFile("tmp"+options.SYST+".root","RECREATE")
        newtree = tree.CopyTree(options.cuts)
        print "entries", newtree.GetEntries()
        #ws_ras = tf.Get("workspace_ras")
        #ras = RooArgSet(ws_ras.allVars(),ws_ras.allCats())
        if not "DATA" in key:
#            if not "DYjets" in key : w = RooFormulaVar("w","w", "@0*@1*@2*@3",
#                                                       RooArgList(ras["leptonsReweightingweight"],ras["lumiReweightingLumiWeight"],ras[options.BTAG],ras["mcReweightingweight"])
#                                                       )
#            else :
#                print key
#                myform = "( formula(@4,@5,@6) )"
#                w = RooFormulaVar("w","w", "@0*@1*@2*@3*"+myform,
#                                     RooArgList(ras["leptonsReweightingweight"],ras["lumiReweightingLumiWeight"],ras[options.BTAG],ras["mcReweightingweight"],ras["boostselectionZbbM"],ras["jetmetbjet1Flavor"],ras["jetmetbjet2Flavor"])
#                                     )
                w = RooFormulaVar("w","w", "@0*@1*@2*@3",
                                                       RooArgList(ras["leptonsReweightingweight"],ras["lumiReweightingLumiWeight"],ras[options.BTAG],ras["mcReweightingweight"])
                                                       )        
        rds = RooDataSet("rds_zbb"+key,"rds_zbb"+key,newtree,ras)
        if not "DATA" in key : rds.addColumn(w)
        if not "DATA" in key : rds = RooDataSet(rds.GetName(),rds.GetName(),rds,rds.get(),"",w.GetName())
        for cat in options.categories : RDS[key+cat] = rds.reduce(options.categories[cat])
    for cat in options.categories:
        if "DYjets"+cat in RDS and options.doDYsplit : RDS = splitDY(RDS, cat) 
    return RDS

#method to split the DY sample in Zbb, Zbx, Zxx
def splitDY(RDS, cat):
    print "Will split DYjets in Zbb, Zbx and Zxx"
    rds = RDS["DYjets"+cat]
    RDS["Zbb"+cat] = rds.reduce("abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)==5")
    #RDS["Zbb"+cat] = rds.reduce("abs(subjetmetbjet1Flavor)==5 & abs(subjetmetbjet2Flavor)==5")
    RDS["Zbb"+cat].SetNameTitle(rds.GetName().replace("DYjets","Zbb"),rds.GetName().replace("DYjets","Zbb"))
    RDS["Zbx"+cat] = rds.reduce("(abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)!=5)")
    #RDS["Zbx"+cat] = rds.reduce("(abs(subjetmetbjet1Flavor)!=5 & abs(subjetmetbjet2Flavor)==5) || (abs(subjetmetbjet1Flavor)==5 & abs(subjetmetbjet2Flavor)!=5)")
    RDS["Zbx"+cat].SetNameTitle(rds.GetName().replace("DYjets","Zbx"),rds.GetName().replace("DYjets","Zbx"))
    RDS["Zxx"+cat] = rds.reduce("abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)!=5")
    #RDS["Zxx"+cat] = rds.reduce("abs(subjetmetbjet1Flavor)!=5 & abs(subjetmetbjet2Flavor)!=5")
    RDS["Zxx"+cat].SetNameTitle(rds.GetName().replace("DYjets","Zxx"),rds.GetName().replace("DYjets","Zxx"))
    del RDS["DYjets"+cat]
    return RDS

#method to get roovars from the rooargset
def getVars(vars, ras,options=None):
    print "Getting variables"
    myvars = {}
    for key in vars:
          myvars[key] = ras[vars[key][0]]
          myvars[key].setBins(vars[key][1])
          myvars[key].setMin(vars[key][2])
          myvars[key].setMax(vars[key][3])
      
    return myvars

def makeHistoCLS(files,RDS,options,myvars):
  th1 = {}
  rdh = {}
  keys = []
  fileOut=TFile(options.outputName,"RECREATE")
  for key in sorted(files.keys()): 
    if key != "DYjets":
      keys.append(key)
    if key == "DYjets" and options.doDYsplit :
    
      keys.extend(("Zbb","Zbx","Zxx"))
  for key in keys:   

    for cat in options.categories:
         for name in myvars:
	     if not cat in name : continue
#             th1[key+name] = TH1D(name.replace("j","jUp").replace("j","jDown")+key,name+key+cat,myvars[name].getBins(),myvars[name].getMin(),myvars[name].getMax())
             th1[key+name] = TH1D(key+name,key+name,myvars[name].getBins(),myvars[name].getMin(),myvars[name].getMax())
             
	     RDS[key+cat].fillHistogram(th1[key+name], RooArgList(myvars[name]))
	 
             #if syst!="" : continue
	     
#	     th1[key+name+"_jesUp"] = JESPlus(key+name+"_JESUp", th1[key+name], th1[key+name+"_JESPlus"], th1[key+name+"_JESMinus"])
#	     th1[key+name+"_jesDown"] = JESMinus(key+name+"_JESDown", th1[key+name], th1[key+name+"_JESPlus"], th1[key+name+"_JESMinus"])

	 
	 
	     th1[key+name].Write()
             rdh[key+name] = RooDataHist("rdh_"+name, "rdh_"+name, RooArgSet(myvars[name]),RDS[key+cat])
             for bin in range(0,myvars[name].getBins()):
                  if bin < (myvars[name].getBins()/2) : continue
                  Binras = rdh[key+name].get(bin)
                  a, b = Double(1), Double(1)
                  rdh[key+name].weightError(a,b)
                  aw = rdh[key+name].weight()
                  #print "factor",a,b , "nbr entries= ",aw
                  if aw>0 : a=a/aw
                  if aw>0 : b=b/aw
                  th1[key+name+"stat_bin"+str(bin+1)+"Up"]= TH1D(key+name+"stat_bin"+str(bin+1)+"Up",key+name+"stat_bin"+str(bin+1)+"Up",myvars[name].getBins(),myvars[name].getMin(),myvars[name].getMax())
                  RDS[key+cat].fillHistogram(th1[key+name+"stat_bin"+str(bin+1)+"Up"], RooArgList(myvars[name]))
                  th1[key+name+"stat_bin"+str(bin+1)+"Down"]= TH1D(key+name+"stat_bin"+str(bin+1)+"Down",key+name+"stat_bin"+str(bin+1)+"Down",myvars[name].getBins(),myvars[name].getMin(),myvars[name].getMax())
                  RDS[key+cat].fillHistogram(th1[key+name+"stat_bin"+str(bin+1)+"Down"], RooArgList(myvars[name]))
                  tmp = th1[key+name+"stat_bin"+str(bin+1)+"Up"].GetBinContent(bin+1)
                  if aw>0 :
                        th1[key+name+"stat_bin"+str(bin+1)+"Up"].SetBinContent(bin+1,tmp*(1.+b))
                        th1[key+name+"stat_bin"+str(bin+1)+"Down"].SetBinContent(bin+1,tmp*(1.-a))
                  else :
                        th1[key+name+"stat_bin"+str(bin+1)+"Up"].SetBinContent(bin+1,tmp+b)
                  #print "bin", bin+1 ,"--- nominal =",tmp," --- variation Up =",b, th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"].GetBinContent(bin+1)," --- variation Down =",a, th1[channel+sample+name+cut+"stat"+str(bin+1)+"Down"].GetBinContent(bin+1)
                  th1[key+name].Scale(lumi["DATA"]/lumi[key.replace(cat,"")])
	          th1[key+name+"stat_bin"+str(bin+1)+"Up"].Scale(lumi["DATA"]/lumi[key.replace(cat,"")])
	          th1[key+name+"stat_bin"+str(bin+1)+"Down"].Scale(lumi["DATA"]/lumi[key.replace(cat,"")])
	          th1[key+name+"stat_bin"+str(bin+1)+"Up"].Write()
	          th1[key+name+"stat_bin"+str(bin+1)+"Down"].Write()
		  
#		  th1[key+name+"_jesUp"].Scale(lumi["DATA"]/lumi[key.replace(cat,"")])
#		  th1[key+name+"_jesUp"].Write()
#		  th1[key+name+"_jesDown"].Scale(lumi["DATA"]/lumi[key.replace(cat,"")])
#		  th1[key+name+"_jesDown"].Write()		  

#             Nbin=th1[name].GetNbinsX();
#             for bin in range(1,Nbin+1):
#               if bin < (Nbin/2+1) : continue
#               print "bin: ", bin
#               th1[name].Scale(lumi["DATA"]/lumi[key.replace(cat,"")])
#	       th1[name+"stat_bin"+str(bin+1)+"Up"].Scale(lumi["DATA"]/lumi[key.replace(cat,"")])
#	       th1[name+"stat_bin"+str(bin+1)+"Down"].Scale(lumi["DATA"]/lumi[key.replace(cat,"")])
#               th1[name].Write()
#	       th1[name+"stat_bin"+str(bin+1)+"Up"].Write()
#	       th1[name+"stat_bin"+str(bin+1)+"Down"].Write()		  
  fileOut.Close()	     


            
    
def main():
    print "Start main"
    options = options_()
    cat= options.categories
    print options.samples
    #get file name
    files = {}
    for sample in options.samples:
        if "DATA" not in sample : files[sample] = options.path.replace("NAME",sample.replace("jets",""))
        else : files[sample] = "/home/fynu/cbeluffi/storage/RDS/5320_JP_Skimmed_V5/llbbX/Data2012_Summer12_final_skimed_llbbX_withWeights_V0_BDT.root"#options.path.replace("NAME","Data2012")
        print files[sample]                    
    #get RDS
    RDS = createRDS(files=files, options=options)
    #Get RooArgSet
    for key in RDS:
        if "DATA" in key : continue
        ras = RDS[key].get()
        break
    #get roovars
    myvars = getVars(options.vars, ras, options=options)
    makeHistoCLS(files,RDS, options,myvars )
    


c_ = main()

