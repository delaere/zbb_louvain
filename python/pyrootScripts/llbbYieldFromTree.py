from ROOT import *
from llbbOptions import *
import array
import os
from math import sqrt
formulaName = "formulaPol3_C.so"
gSystem.Load(formulaName)
gROOT.SetBatch()

class options_(options_):
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
        #"ZA_286_93",
        #"ZA_262_99"
        ]
    print samples
    
    #Systematics
    SYST = "Nominal"
    #SYST = "JESup"
    #SYST = "JESdown"
    #SYST = "JERup"
    #SYST = "JERdown"
    #SYST = "BTAG_bc_up"
    #SYST = "BTAG_bc_down"
    #SYST = "BTAG_light_up"
    #SYST = "BTAG_light_down"
    path = options_.path.replace("SYST",SYST)
    
    #output
    output = options_.output.replace("SYST",SYST).replace("V3","V4")

def createTree(files={"test" : "test.root"}, options=None):
    if options is None : return None
    Trees = {}
    #run over all the samples
    for key in files:
        print "Make RDS for", key
        #Get file and tree
        tf = TFile.Open(files[key])
	Trees[key] = tf.Get("rds_zbb")
    return Trees

def makeRF(output, Trees, options): #opt_cut, categories, dirLmits):
    tree = TTree("yields","tree containing all informations for yields")

    print "create RootFile "
    mA = array.array('d', [0.0])
    mH = array.array('d', [0.0])
    tree.Branch('mA',mA,'mA/D')
    tree.Branch('mH',mH,'mH/D')
    #Prepare the output roofiles
    #output.mkdir(cat+rep,cut)
    #output.cd(cat+rep)
    #Get the keys sorted
    keys = [key for key in Trees ] #if cat in key]
    keys.sort()
    #Initiate the string to be included in the txt files to compute the limits
    a = {}
    print "creating branches "
    for key in keys:
	for cat in options.categories :
	    if "DY" in key:
		a["Zbb2j"+cat] = array.array('d', [0.0])
                tree.Branch("Zbb2j"+cat,a["Zbb2j"+cat],"Zbb2j"+cat+'/D')
		a["Zbb3j"+cat] = array.array('d', [0.0])
                tree.Branch("Zbb3j"+cat,a["Zbb3j"+cat],"Zbb3j"+cat+'/D')
                a["Zbx"+cat] = array.array('d', [0.0])
                tree.Branch("Zbx"+cat,a["Zbx"+cat],"Zbx"+cat+'/D')
                a["Zxx"+cat] = array.array('d', [0.0])
                tree.Branch("Zxx"+cat,a["Zxx"+cat],"Zxx"+cat+'/D')
	    else :
                a[key+cat] = array.array('d', [0.0])
	        tree.Branch(key+cat,a[key+cat],key+cat+'/D')
	    #print 'key : ', key+cat

    print 'run over the samples'
    #Run over the samples
    for cutkey in options.cut :
        print 'cutkey : ', cutkey
        mH[0] = float(options.mH_list[cutkey])
        mA[0] = float(options.mA_list[cutkey])
        #if int(mH[0]) != 216 : continue
        #if int(mA[0]) != 23 : continue
        print 'mH , mA : ', mH[0], mA[0]
        if mA < mH : 
            for key in keys:
                print "key is ", key
                for cat in options.categories:
                    print "cat is ", cat
                    #Select phase space
                    #tmpTH1 = TH1D('MET','MET',100,0,1000)
                    if "DATA" in key : reweighting = "" 
		    else :
			condition = options.SYST
			reweighting = options.rewForm["Zbb"][cat]
		        if "TT" in key : reweighting += SFlist[condition]["TT"]
                    err = True
		    if "DY" in key:
			condition = options.SYST
			reweighting_Zbb = reweighting+SFlist[condition]["Zbb"]+"*formula(boostselectionZbbM,jetmetbjet1Flavor,jetmetbjet2Flavor)"
			reweighting_Zbx = reweighting+SFlist[condition]["Zbx"]+"*formula(boostselectionZbbM,jetmetbjet1Flavor,jetmetbjet2Flavor)"
			reweighting_Zxx = reweighting+SFlist[condition]["Zxx"]+"*formula(boostselectionZbbM,jetmetbjet1Flavor,jetmetbjet2Flavor)"

			tmpTH1 = TH1D('MET','MET',100,0,1000)
                        tmpTH1.Sumw2();
			numEnt = Trees[key].Draw("jetmetMET >> MET","(abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 && jetmetnj==2 && "+options.cut[cutkey]+" && "+options.categories[cat]+")"+reweighting_Zbb)
                        tmpArray = tmpTH1.GetSumw2()
                        sum = 0
                        for arr in range(0,tmpArray.GetSize()) : sum+=tmpArray[arr]
                        if not err : a["Zbb2j"+cat][0] = tmpTH1.Integral()*(lumi["DATA"]/lumi["Zbb"])
                        else : a["Zbb2j"+cat][0] = sqrt(sum)*(lumi["DATA"]/lumi["Zbb"])
                        #print "Zbb2j"+cat, numEnt, a["Zbb2j"+cat][0], (lumi["DATA"]/lumi["Zbb"])
                        tmpTH1.Delete()
			
			tmpTH1 = TH1D('MET','MET',100,0,1000)
                        tmpTH1.Sumw2();
			numEnt = Trees[key].Draw("jetmetMET >> MET","(abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 && jetmetnj>2 && "+options.cut[cutkey]+" && "+options.categories[cat]+")"+reweighting_Zbb)
                        tmpArray = tmpTH1.GetSumw2()
                        sum = 0
                        for arr in range(0,tmpArray.GetSize()) : sum+=tmpArray[arr]
                        if not err : a["Zbb3j"+cat][0] = tmpTH1.Integral()*(lumi["DATA"]/lumi["Zbb"])
                        else : a["Zbb3j"+cat][0] = sqrt(sum)*(lumi["DATA"]/lumi["Zbb"])
                        #print "Zbb3j"+cat, numEnt, a["Zbb3j"+cat][0], (lumi["DATA"]/lumi["Zbb"])
			tmpTH1.Delete()
			
			tmpTH1 = TH1D('MET','MET',100,0,1000)
                        tmpTH1.Sumw2();
			numEnt = Trees[key].Draw("jetmetMET >> MET","(((abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5)) && "+options.cut[cutkey]+" && "+options.categories[cat]+")"+reweighting_Zbx)
                        tmpArray = tmpTH1.GetSumw2()
                        sum = 0
                        for arr in range(0,tmpArray.GetSize()) : sum+=tmpArray[arr]
                        if not err : a["Zbx"+cat][0] = tmpTH1.Integral()*(lumi["DATA"]/lumi["Zbx"])
                        else : a["Zbx"+cat][0] = sqrt(sum)*(lumi["DATA"]/lumi["Zbx"])
                        #print "Zbx"+cat, numEnt, a["Zbx"+cat][0], (lumi["DATA"]/lumi["Zbx"])
                        tmpTH1.Delete()

			tmpTH1 = TH1D('MET','MET',100,0,1000)
                        tmpTH1.Sumw2();
			numEnt = Trees[key].Draw("jetmetMET >> MET","(abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5 && "+options.cut[cutkey]+" && "+options.categories[cat]+")"+reweighting_Zxx)
                        tmpArray = tmpTH1.GetSumw2()
                        sum = 0
                        for arr in range(0,tmpArray.GetSize()) : sum+=tmpArray[arr]
                        if not err : a["Zxx"+cat][0] = tmpTH1.Integral()*(lumi["DATA"]/lumi["Zxx"])
                        else : a["Zxx"+cat][0] = sqrt(sum)*(lumi["DATA"]/lumi["Zxx"])
                        #print "Zxx"+cat, numEnt, a["Zxx"+cat][0], (lumi["DATA"]/lumi["Zxx"])
			tmpTH1.Delete()
		    else :
			tmpTH1 = TH1D('MET','MET',100,0,1000)
                        tmpTH1.Sumw2();
                        numEnt = Trees[key].Draw("jetmetMET >> MET","("+options.cut[cutkey]+" && "+options.categories[cat]+")"+reweighting)
                        #print "("+options.cut[cutkey]+" && "+options.categories[cat]+")"+reweighting
                        tmpArray = tmpTH1.GetSumw2()
                        sum = 0
                        for arr in range(0,tmpArray.GetSize()) : sum+=tmpArray[arr]
                        if not err : a[key+cat][0] = tmpTH1.Integral()*(lumi["DATA"]/lumi[key])
                        else : a[key+cat][0] = sqrt(sum)*(lumi["DATA"]/lumi[key])
                        #print key+cat, numEnt, a[key+cat][0], (lumi["DATA"]/lumi[key])
                        #print "Option Mll", mA[0], mH[0], a[key+cat][0]
                        tmpTH1.Delete()
                        #tmpTH1 = TH1D('MET','MET',100,0,1000)
                        #Trees[key].Draw("jetmetMET >> MET","("+options.cut[cutkey]+" && "+options.categories[cat]+"&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106)"+reweighting)
                        #print "("+options.cut[cutkey]+" && "+options.categories[cat]+"&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106)"+reweighting
                        #print "Small Mll", mA[0], mH[0], tmpTH1.Integral()*(lumi["DATA"]/lumi[key])
                        #tmpTH1.Delete()
	                #print 'a[key+cat] :', a[key+cat]
            tree.Fill()
            #if a["TTFullLeptMu"][0]>1 : break         
    #Write output
    tree.Write()
    output.Write()
    output.Close()
    return

def main():
    print "Start main"
    options = options_()
    print options.samples
    #get file name
    files = {}
    for sample in options.samples:
	if "DY" in sample : files[sample] = options.path.replace("NAME","DY")
        elif "DATA" not in sample : files[sample] = options.path.replace("NAME",sample)
        else : files[sample] = options.path_data
        print files[sample]
    #get RDS
    Trees = createTree(files=files, options=options)
    #RDS = bkgNorm(RDS)
    #Make and store hists
    output = TFile(options.output,"RECREATE")
    print Trees
    #for key in options.cut : makeRF(output, RDS, key, options.cut[key], options.categories, options.dirLimits)
    makeRF(output, Trees, options)
    return

main()
