from ROOT import *
from listForRDS import lumi
from llbbOptions import options_
import llbbSF
import array
import os

gROOT.SetBatch()

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

def createRDS(files={"test" : "test.root"}, options=None):
    if options is None : return None
    RDS = {}
    #run over all the samples
    for key in files:
        print "Make RDS for", key
        #Get file and tree
        tf = TFile.Open(files[key])
        tree = tf.Get("rds_zbb")
        #temporary file use to host the new "lighter" tree to be used to create the RDS
        tmpfile=TFile("tmp.root","RECREATE")
        newtree = tree.CopyTree(options.presel)
        #make the RDS
        ws_ras = tf.Get("workspace_ras")
        ras = RooArgSet(ws_ras.allVars(),ws_ras.allCats())
        rds = RooDataSet("rds_zbb"+key,"rds_zbb"+key,newtree,ras)
        #Add a variable with the reweighting information
        if not "DATA" in key :
            w = RooFormulaVar("w","w", "@0*@1*@2*@3",
                              RooArgList(ras["LeptonsReweightingweight"],ras["lumiReweightingLumiWeight"],ras[options.BTAG],ras["MonteCarloReweightingweight"])
                              )
            rds.addColumn(w)
        #Reduce RDS
        for cat in options.categories : RDS[key+cat] = rds.reduce(options.categories[cat])
    #Split DY sample
    for cat in options.categories:
        if "DYjets"+cat in RDS and options.doDYsplit : RDS = splitDY(RDS, cat)
    return RDS

#method to split the DY sample in Zbb, Zbx, Zxx
def splitDY(RDS, cat):
    print cat, "Will split DYjets in Zbb, Zbx and Zxx"
    rds = RDS["DYjets"+cat]
    #Split with jet flavour
    RDS["Zbb"+cat] = rds.reduce("abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)==5")
    RDS["Zbb"+cat].SetNameTitle(rds.GetName().replace("DYjets","Zbb"),rds.GetName().replace("DYjets","Zbb"))
    RDS["Zbx"+cat] = rds.reduce("(abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)!=5)")
    RDS["Zbx"+cat].SetNameTitle(rds.GetName().replace("DYjets","Zbx"),rds.GetName().replace("DYjets","Zbx"))
    RDS["Zxx"+cat] = rds.reduce("abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)!=5")
    RDS["Zxx"+cat].SetNameTitle(rds.GetName().replace("DYjets","Zxx"),rds.GetName().replace("DYjets","Zxx"))
    #Remove the DY RDS
    del RDS["DYjets"+cat]
    return RDS

def bkgNorm(RDS):
    #reweight the MC considering also the bkg normalisation from data
    for key in RDS:
        formula = "@0"
        if "DATA" in key : continue
        if "Zbb" in key : formula = "@0*(1.15*(@1==2)+1.30*(@1>2))"
        if "Zbx" in key : formula = "@0*1.30"
        if "Zxx" in key : formula = "@0*1.28"
        if "TT" in key : formula = "@0*1.05"
        ras = RDS[key].get()
        sfs = RooFormulaVar("sfs","sfs", formula, RooArgList(ras["w"], ras["jetmetnj"]))
        RDS[key].addColumn(sfs)
        RDS[key] = RooDataSet(RDS[key].GetName(),RDS[key].GetName(),RDS[key],RDS[key].get(),"",sfs.GetName())
    return RDS


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
		a["Zbb"+cat] = array.array('d', [0.0])
                tree.Branch("Zbb"+cat,a["Zbb"+cat],"Zbb"+cat+'/D')
                a["Zbx"+cat] = array.array('d', [0.0])
                tree.Branch("Zbx"+cat,a["Zbx"+cat],"Zbx"+cat+'/D')
                a["Zxx"+cat] = array.array('d', [0.0])
                tree.Branch("Zxx"+cat,a["Zxx"+cat],"Zxx"+cat+'/D')
	    else :
                a[key+cat] = array.array('d', [0.0])
	        tree.Branch(key+cat,a[key+cat],key+cat+'/D')
	    print 'key : ', key+cat

    print 'run over the samples'
    #Run over the samples
    for cutkey in options.cut :
        print 'cutkey : ', cutkey
        mH[0] = float(options.mH_list[cutkey])
        mA[0] = float(options.mA_list[cutkey])
        print 'mH , mA : ', mH, mA
        if (mA < mH) :
            for key in keys:
                for cat in options.categories :
                    #Select phase space
                    tmpTH1 = TH1D('MET','MET',100,0,1000)
                    if "DATA" in key : 
			reweighting = "" 
		    else :
			condition = options.Condition
			reweighting = options.rewForm[cat]
		        if "TT" in key: reweighting += llbbSF.SFlist[condition]["TT"]

		    if "DY" in key:
			condition = options.Condition
			reweighting_Zbb= reweighting+llbbSF.SFlist[condition]["Zbb"]
			reweighting_Zbx= reweighting+llbbSF.SFlist[condition]["Zbx"]
			reweighting_Zxx= reweighting+llbbSF.SFlist[condition]["Zxx"]
			Trees[key].Draw("jetmetMET >> MET","(abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 && "+options.cut[cutkey]+" && "+options.categories[cat]+")"+reweighting_Zbb)
			a["Zbb"+cat][0] = tmpTH1.Integral()*(lumi["DATA"]/lumi["Zbb"])
			tmpTH1.Delete()
			tmpTH1 = TH1D('MET','MET',100,0,1000)
			Trees[key].Draw("jetmetMET >> MET","(((abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5)) && "+options.cut[cutkey]+" && "+options.categories[cat]+")"+reweighting_Zbx)
                        a["Zbx"+cat][0] = tmpTH1.Integral()*(lumi["DATA"]/lumi["Zbx"])
                        tmpTH1.Delete()
			tmpTH1 = TH1D('MET','MET',100,0,1000)
			Trees[key].Draw("jetmetMET >> MET","(abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5 && "+options.cut[cutkey]+" && "+options.categories[cat]+")"+reweighting_Zxx)
                        a["Zxx"+cat][0] = tmpTH1.Integral()*(lumi["DATA"]/lumi["Zxx"])	
			tmpTH1.Delete()
		    else :
                        Trees[key].Draw("jetmetMET >> MET","("+options.cut[cutkey]+" && "+options.categories[cat]+")"+reweighting)
                        a[key+cat][0] = tmpTH1.Integral()*(lumi["DATA"]/lumi[key])
                        tmpTH1.Delete()
	                print 'a[key+cat] :', a[key+cat]
            tree.Fill()
                 
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
        if "DATA" not in sample : files[sample] = options.path.replace("NAME",sample)
        else : files[sample] = options.path.replace("NAME","Double2012")
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
