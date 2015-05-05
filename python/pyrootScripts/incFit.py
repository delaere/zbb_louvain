"""
Script to fit the backround to the data
"""

from ROOT import *
import inc_Options
from llbbNorm import lumi

gROOT.SetBatch()

formulaName = "formulaPol3_C.so"
gSystem.Load(formulaName)

class options_():
    #list of samples
    samples = [
        "DATA",
        "DYjets",
        "TTFullLept",
#        "TTSemiLept",
        "ZZ",
#        "WZ",
#        "WW",
#        "Wt",
#        "Wtbar",
        #"ZH125",
        #"ZA_350_70",
        ]

    SYST = inc_Options.SYST
    print SYST

    path = inc_Options.path.replace("SYST",SYST)

    #Varibales
    BIN = 3
    vars = {
        "zmassEle" : ["eventSelectiondilepM_inc", 4, 60., 120.] ,
        "zmassMu"  : ["eventSelectiondilepM_inc", 4, 60., 120.] ,
        "MET"      : ["jetmetMET", 7, 0., 100.] ,
        "JPprodMM"   : ["JPprod", BIN, 0, 2.1] ,
        "CSVprodMM": ["CSVprod", 4, 0.679*0.679, 1] ,
        #"CSVprodML": ["CSVprod", 4, 0.244*0.679, 1] ,
        #"CSVprodLL": ["CSVprod", 12, 0.244*0.244, 1] ,
        "JP1"      : ["jetmetbjet1JPdisc", BIN, 0, 1.5] ,
        "JP2"      : ["jetmetbjet2JPdisc", BIN, 0, 1.5],
        "CSV1"     : ["jetmetbjet1CSVdisc", BIN, 0.679, 1] ,
        "CSV2"     : ["jetmetbjet2CSVdisc", BIN, 0.679, 1] ,
        "SV1"      : ["jetmetbjet1SVmass", BIN, 0, 5] ,
        "SV2"      : ["jetmetbjet2SVmass", BIN, 0, 5] ,
	"MLPTTDY_El_noCat"      : ["MLPTTDY_El_noCat", 4, -0.1,1.1] ,
	"MLPTTDY_Mu_noCat"      : ["MLPTTDY_Mu_noCat", 4, -0.1,1.1] ,
	"bdtTTDY_El_noCat"      : ["bdtTTDY_El_noCat", 6, -0.8,0.5] ,
	"bdtTTDY_Mu_noCat"      : ["bdtTTDY_Mu_noCat", 6, -0.8,0.5] ,	
	
	
        }
    thevars = { "El" : ["MLPTTDY_El_noCat","JPprodMM"], "Mu" : ["MLPTTDY_Mu_noCat","JPprodMM"] }
     
    print "variables to be used:", thevars
    #stages
    stages = inc_Options.stagesFit
    doDYsplit=inc_Options.doDYsplit

    print "stages:", stages

    #BTAG weight
    BTAG = inc_Options.BTAG.replace("*","")
    print "BTAG:", BTAG
    bTag = inc_Options.bTag
    
    #define cuts
    cuts = "("+stages["El"]+" || "+stages["Mu"]+")"
    #cuts = "("+stages["El"]+"_idx || "+stages["Mu"]+"_idx)&&jetmetMETsignificance < 10 && jetmetMETsignificance != 0 && ( (boostselectiondijetM<54||boostselectiondijetM>86) || (boostselectionZbbM<197||boostselectionZbbM>403) )"
    print "cut:", cuts
    #define categories
    categories = {
        "El2j" : stages["El"].replace("_idx","")+"&&jetmetnj==2&&(eventSelectiondijetM<80||eventSelectiondijetM>150)",
        "El3j" : stages["El"].replace("_idx","")+"&&jetmetnj>2&&(eventSelectiondijetM<50||eventSelectiondijetM>150)",
        "Mu2j" : stages["Mu"].replace("_idx","")+"&&jetmetnj==2&&(eventSelectiondijetM<80||eventSelectiondijetM>150)",
        "Mu3j" : stages["Mu"].replace("_idx","")+"&&jetmetnj>2&&(eventSelectiondijetM<50||eventSelectiondijetM>150)"
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
    output = "FitJPProd3_zmass4_"+SYST+".root"
    
#method to make all needed RDS
def createRDS(files={"test" : "test.root"}, options=None):
    if options is None : return None
    RDS = {}
    for key in sorted(files.keys()):
    
    
	fileIn = TFile.Open("/nfs/user/cbeluffi/ControlPlots/RDS_JP_Nominal/RDS_TTFullLept/TTFullLept_Summer12_final.root","read")
	ws_ras = fileIn.Get("workspace_ras") # get the RooArgSet from the file
	
	ras = RooArgSet(ws_ras.allVars(),ws_ras.allCats()) # define a new RooArgSet using the one you got from the file

	MLPTTDY_El_noCat= RooRealVar("MLPTTDY_El_noCat", "MLPTTDY_El_noCat", -2.0, 2.0) 
	MLPTTDY_Mu_noCat= RooRealVar("MLPTTDY_Mu_noCat", "MLPTTDY_Mu_noCat", -2.0, 2.0)  
	bdtTTDY_El_noCat= RooRealVar("bdtTTDY_El_noCat", "bdtTTDY_El_noCat", -2.0, 2.0) 
	bdtTTDY_Mu_noCat= RooRealVar("bdtTTDY_Mu_noCat", "bdtTTDY_Mu_noCat", -2.0, 2.0)  
	
		
	ras.add(MLPTTDY_El_noCat)
	ras.add(MLPTTDY_Mu_noCat) 
	ras.add(bdtTTDY_El_noCat)
	ras.add(bdtTTDY_Mu_noCat) 	
	
        print "Make RDS for", key
        tf = TFile.Open(files[key])
        tree = tf.Get("rds_zbb")
        tmpfile=TFile("tmp"+options.SYST+".root","RECREATE")
        newtree = tree.CopyTree(options.cuts)
        print "entries", newtree.GetEntries()
        #ws_ras = tf.Get("workspace_ras")
        #ras = RooArgSet(ws_ras.allVars(),ws_ras.allCats())
        if not "DATA" in key:
            w = RooFormulaVar("w","w", "@0*@1*@2*@3",
                                                       RooArgList(ras["leptonsReweightingweight"],ras["lumiReweightingLumiWeight"],ras[options.BTAG],ras["mcReweightingweight"])
                                                       )

 
        csvprod = RooFormulaVar("CSVprod","CSVprod","@0*@1",RooArgList(ras["jetmetbjet1CSVdisc"],ras["jetmetbjet2CSVdisc"]))

        jpprod = RooFormulaVar("JPprod","JPprod","@0*@1*(@0*@1<2.0)+2.0*(@0*@1>=2.0)",RooArgList(ras["jetmetbjet1JPdisc"],ras["jetmetbjet2JPdisc"]))
	#jpprod = RooFormulaVar("JPprod","JPprod","@0*@1",RooArgList(ras["jetmetbjet1JPdisc"],ras["jetmetbjet2JPdisc"]))
	#jpprod = RooFormulaVar("JPprod","JPprod","0*(@0*@1<=1.0)+1*(1<@0*@1<=1.5)+2*(@0*@1>1.5)",RooArgList(ras["jetmetbjet1JPdisc"],ras["jetmetbjet2JPdisc"]))
        rds = RooDataSet("rds_zbb"+key,"rds_zbb"+key,newtree,ras)
        if not "DATA" in key : rds.addColumn(w)
        rds.addColumn(csvprod)
        rds.addColumn(jpprod)
        if not "DATA" in key : rds = RooDataSet(rds.GetName(),rds.GetName(),rds,rds.get(),"",w.GetName())
        for cat in options.categories : 
	  RDS[key+cat] = rds.reduce(options.categories[cat])
	  print key+cat, RDS[key+cat].sumEntries()
	
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
def getVars(vars, ras):
    print "Getting variables"
    myvars = {}
    for key in vars:
        myvars[key] = ras[vars[key][0]]
        myvars[key].setBins(vars[key][1])
        myvars[key].setMin(vars[key][2])
        myvars[key].setMax(vars[key][3])
    return myvars

def makePdfs(RDS, myvars, thevars):
    print "Make PDFs"
    RDH = {}
    RHP = {}
    for key in RDS:
        if "Mu" in key : ras_vars = RooArgSet(myvars[thevars["Mu"][0]],myvars[thevars["Mu"][1]])
        else : ras_vars = RooArgSet(myvars[thevars["El"][0]],myvars[thevars["El"][1]])
        RDH[key] = RooDataHist("RDH_"+key,"RDH_"+key, ras_vars, RDS[key])
        RHP[key] = RooHistPdf("RHP_"+key,"RHP_"+key, ras_vars, RDH[key])
    return (RDH, RHP)

def addPdfs(RDS, RHP, categories, SFs, flavor):
    print "Add PDFs"
    PdfList2D = {}
    N_exp = {}
    N = {}
    YieldList2D = {}
    Pdf2D = {}
    simPdf = RooSimultaneous("sim","sim",flavor)
    for cat in categories:
        PdfList2D[cat] = RooArgList()
        YieldList2D[cat] = RooArgList()
        for key in RHP :
            if "DATA" in key : continue
            if not cat in key : continue
            PdfList2D[cat].add(RHP[key])
#	    
#	    
#            if "TTFull" in key and "Mu" in cat:
#	       N_exp[key]=RooConstVar("N_exp_"+key,"N_exp_"+key,
#                                   (RDS[key].sumEntries()*2.4*(lumi["DATA"]/lumi[key.replace(cat,"")])))	
#            elif "TTFull" in key and "El" in cat:
#	       N_exp[key]=RooConstVar("N_exp_"+key,"N_exp_"+key,
#                                   (RDS[key].sumEntries()*1.6*(lumi["DATA"]/lumi[key.replace(cat,"")])))	    
#	    else:
	    N_exp[key]=RooConstVar("N_exp_"+key,"N_exp_"+key,
                                   (RDS[key].sumEntries()*(lumi["DATA"]/lumi[key.replace(cat,"")])))	
	    print "After rew. ", key, RDS[key].sumEntries(),  RDS[key].sumEntries()*(lumi["DATA"]/lumi[key.replace(cat,"")]) 	
	    
	       
            N[key] = RooFormulaVar("N_"+key,"N_"+key,"@0*@1",RooArgList(N_exp[key],SFs[key]))
            YieldList2D[cat].add(N[key])
        Pdf2D[cat] = RooAddPdf("Pdf2D"+cat,"Pdf2D"+cat,PdfList2D[cat],YieldList2D[cat])
        simPdf.addPdf(Pdf2D[cat],cat)
    return (Pdf2D,simPdf,PdfList2D,N_exp,N,YieldList2D)
            
def drawFit(RHP, RAP, RDS, myvars, options=None):
    if options is None : return
    c = {}
    frame = {}
    for index, cat in enumerate(options.categories):
        if "Mu" in cat : thevars = options.thevars["Mu"]
        else : thevars = options.thevars["El"]
        for var in thevars:
            CANVAS = TCanvas(var+cat,var+cat,300,300)
	    print "make plot bug var+cat", var+cat
            frame[var+cat] =  myvars[var].frame()
            RDS["DATA"+cat].plotOn(frame[var+cat])
            sumSample = ""
            keys = []
            for sample in options.samples:
                if sample == "DATA" : continue
                if sample == "DYjets" and options.doDYsplit :
                    keys.extend(("Zbb","Zbx","Zxx"))
                    sumSample += RHP["Zbb"+cat].GetName()+","+RHP["Zbx"+cat].GetName()+","+RHP["Zxx"+cat].GetName()+","
                else :
                    keys.append(sample)
                    sumSample += RHP[sample+cat].GetName()+","
		    print "Pdf sum", sample+cat, RHP[sample+cat].dataHist().sumEntries()
            for index, k in enumerate(keys):
	        print "sum sample: ", sumSample
                if index > 0 : sumSample = sumSample.replace(RHP[keys[index-1]+cat].GetName()+",","")
                RAP[cat].plotOn(frame[var+cat],
                                RooFit.Components(sumSample),
                                RooFit.DrawOption("F"),
                                RooFit.LineColor(kBlack),
                                RooFit.FillColor(options.Colour[k]-7),
                                RooFit.LineWidth(1)
                                )
            RDS["DATA"+cat].plotOn(frame[var+cat])
            RAP[cat].paramOn(frame[var+cat],RDS["DATA"+cat])
            frame[var+cat].Draw()
            c[var+cat] = CANVAS
    C = TCanvas("CANVAS","CANVAS",1200,600)
    C.Divide(len(options.categories),2)
    i = 1
    for cat in sorted(options.categories.keys()):
        if "Mu" in cat : thevars = options.thevars["Mu"]
        else : thevars = options.thevars["El"]
        for var in thevars:
            key = var+cat
            C.cd(i)
            i+=1
            c[key].DrawClonePad()
	    print "canvas name: ", key
    C.SaveAs(options.output)
    return C
    
def main():
    print "Start main"
    options = options_()
    print options.samples
    #get file name
    files = {}
    bTag=options.bTag
    SYST=options.SYST
    for sample in options.samples:
        if "DATA" not in sample : files[sample] = options.path.replace("SAMPLE",sample).replace("BTAG",bTag)
        else : files[sample] = options.path.replace("SAMPLE","Data2012").replace("BTAG",bTag).replace("SYST",SYST)
        print files[sample]                    
    #get RDS
    RDS = createRDS(files=files, options=options)
    #Get RooArgSet
    for key in RDS:
        if "DATA" in key : continue
        ras = RDS[key].get()
        break
    #get roovars
    myvars = getVars(options.vars, ras)
    #SFs
    print "Define SFs"
    SF_zbb_2jet=RooRealVar("SF_zbb","SF_zbb",1.0,0.5, 2.0)
    SF_zbx_2jet=RooRealVar("SF_zbbj","SF_zbbj",1.0,0.5, 2.0)
    SF_zxx_2jet=RooRealVar("SF_zxx","SF_zxx",1.0,0.5,5.0)
    SF_zbb_3jet=SF_zbx_2jet
    SF_zbx_3jet=SF_zbx_2jet
    SF_zxx_3jet=SF_zxx_2jet
    SF_tt=RooRealVar("SF_tt","SF_tt",1.0,0.5, 2.0)

    #SF_zbb_2jetEE=RooRealVar("SF_zbbEE","SF_zbbEE",1.,0.5, 2.)
    #SF_zbx_2jetEE=RooRealVar("SF_zbbjEE","SF_zbbjEE",1.,0.5, 2.)
    #SF_zxx_2jetEE=RooRealVar("SF_zxxEE","SF_zxxEE",1.,0.5, 5.)
    #SF_zbb_3jetEE=SF_zbx_2jetEE
    #SF_zbx_3jetEE=SF_zbx_2jetEE
    #SF_zxx_3jetEE=SF_zxx_2jetEE
    #SF_ttEE=RooRealVar("SF_ttEE","SF_ttEE",1.,0.5, 2.)

    SF_zz=RooRealVar("SF_zz", "SF_zz", 1., 1., 1.)
    SF_wz=RooRealVar("SF_wz", "SF_wz", 1., 1., 1.)
    SF_ww=RooRealVar("SF_ww", "SF_ww", 1., 1., 1.)
    SF_wt=RooRealVar("SF_wt", "SF_wt", 1., 1., 1.)
    SF_wtbar=RooRealVar("SF_wtbar", "SF_wtbar", 1., 1., 1.)
#    SF_zh=RooRealVar("SF_zh", "SF_zh", 1., 1., 1.)
#    SF_za=RooRealVar("SF_za", "SF_za", 1., 1., 1.)

    SFs={
        "TTFullLeptEl2j":SF_tt,
#        "TTSemiLeptEl2j":SF_tt,
        "ZbbEl2j":SF_zbb_2jet,
        "ZbxEl2j":SF_zbx_2jet,
        "ZxxEl2j":SF_zxx_2jet,
        "ZZEl2j":SF_zz,
#        "WZEl2j":SF_wz,
#        "WWEl2j":SF_ww,
#        "WtEl2j":SF_wt,
#        "WtbarEl2j":SF_wtbar,
#        "ZH125El2j":SF_zh,
#        "ZA_350_70El2j":SF_za,

        "TTFullLeptMu2j":SF_tt,
#        "TTSemiLeptMu2j":SF_tt,
        "ZbbMu2j":SF_zbb_2jet,
        "ZbxMu2j":SF_zbx_2jet,
        "ZxxMu2j":SF_zxx_2jet,
        "ZZMu2j":SF_zz,
#        "WZMu2j":SF_wz,
#        "WWMu2j":SF_ww,
#        "WtMu2j":SF_wt,
#        "WtbarMu2j":SF_wtbar,
#        "ZH125Mu2j":SF_zh,
#        "ZA_350_70Mu2j":SF_za,

        "TTFullLeptEl3j":SF_tt,
#        "TTSemiLeptEl3j":SF_tt,
        "ZbbEl3j":SF_zbb_3jet,
        "ZbxEl3j":SF_zbx_3jet,
        "ZxxEl3j":SF_zxx_3jet,
        "ZZEl3j":SF_zz,
#        "WZEl3j":SF_wz,
#        "WWEl3j":SF_ww,
#        "WtEl3j":SF_wt,
#        "WtbarEl3j":SF_wtbar,
#        "ZH125El3j":SF_zh,
#        "ZA_350_70El3j":SF_za,
        
        "TTFullLeptMu3j":SF_tt,
#        "TTSemiLeptMu3j":SF_tt,
        "ZbbMu3j":SF_zbb_3jet,
        "ZbxMu3j":SF_zbx_3jet,
        "ZxxMu3j":SF_zxx_3jet,
        "ZZMu3j":SF_zz,
#        "WZMu3j":SF_wz,
#        "WWMu3j":SF_ww,
#        "WtMu3j":SF_wt,
#        "WtbarMu3j":SF_wtbar,
#        "ZH125Mu3j":SF_zh,
#        "ZA_350_70Mu3j":SF_za,
        }

    #categories for simultaneous fit
    flavor = RooCategory("cat","cat")
    flavor.defineType("El2j")
    flavor.defineType("El3j")
    flavor.defineType("Mu2j")
    flavor.defineType("Mu3j")
    
    flavor.setLabel("El2j")
    RDS["DATAEl2j"].addColumn(flavor)
    
    flavor.setLabel("El3j")
    RDS["DATAEl3j"].addColumn(flavor)
    
    flavor.setLabel("Mu2j")
    RDS["DATAMu2j"].addColumn(flavor)
    
    flavor.setLabel("Mu3j")
    RDS["DATAMu3j"].addColumn(flavor)

    #get roohistpdfs and roodatahists
    (RDH, RHP) = makePdfs(RDS, myvars, options.thevars)       
    #get rooaddpdf
    (RAP, simPdfs,PdfList2D,N_exp,N,YieldList2D) = addPdfs(RDS, RHP, options.categories, SFs, flavor)
    #make the data
    print "Make DATA to be fitted"
    DATA = RooDataSet("DATA","DATA",RDS["DATAEl2j"],RDS["DATAEl2j"].get())
    DATA.append(RDS["DATAMu2j"])
    DATA.append(RDS["DATAEl3j"])
    DATA.append(RDS["DATAMu3j"])
    #do the fit
    print "Do the fit..."
    simPdfs.fitTo(DATA)
    #draw fit
    return drawFit(RHP, RAP, RDS, myvars, options)

c_ = main()

