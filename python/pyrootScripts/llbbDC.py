
from llbbOptions import options_
from ROOT import *
from listForRDS import lumi
import array
import os

class options_(options_):
    #list of samples
    samples = [
        "DYjets",
        "TTFullLept",
        "TTSemiLept",
        "ZZ",
        "WZ",
        "WW",
        "Wt",
        "Wtbar",
        "ZH125",
        ]
    print samples

def makeDataCards(options,dirLimits, JESsystValues, JERsystValues,BTAGbcsystValues,BTAGlsystValues):
    #Run over the different categories
    f = TFile.Open(options.output.replace("SYST","Nominal"),"read")
    tree = f.Get("yields")
    samplesList = options.samples
    dataCardsList = {}
    if "DYjets" in samplesList:
        samplesList.remove("DYjets")
        samplesList.append("Zbb2j")
        samplesList.append("Zbb3j")
        samplesList.append("Zbx")
        samplesList.append("Zxx")
    print 'sampleList : ', samplesList

    fZbx = TFile("/home/fynu/amertens/Delphes_Analysis/2hdm/syst_zbx.root")
    tgZbx = fZbx.Get("Graph")
    fZxx = TFile("/home/fynu/amertens/Delphes_Analysis/2hdm/syst_zxx.root")
    tgZxx = fZxx.Get("Graph")

    myTGraph_ratio = TGraph2D(10)
    myTGraph_ratio.SetName("Ratio CMSSW/Delphes")
    
    myTGraph_ratio.SetPoint(0,35,142,0.411)
    myTGraph_ratio.SetPoint(1,10,200,0.838)
    myTGraph_ratio.SetPoint(2,110,200,0.796)
    myTGraph_ratio.SetPoint(3,30,329,0.826)
    myTGraph_ratio.SetPoint(4,70,329,0.897)
    myTGraph_ratio.SetPoint(5,70,575,0.955)
    myTGraph_ratio.SetPoint(6,70,875,0.907)
    myTGraph_ratio.SetPoint(7,142,329,0.925)
    myTGraph_ratio.SetPoint(8,142,875,0.927)
    myTGraph_ratio.SetPoint(9,378,575,0.891)
    myTGraph_ratio.SetPoint(10,378,875,0.911)
    myTGraph_ratio.SetPoint(11,575,875,0.890)
    myTGraph_ratio.SetPoint(12,761,875,0.849)
    myTGraph_ratio.SetPoint(13,50,1200,0.9)
    myTGraph_ratio.SetPoint(14,1200,1200,0.85)
    
    myTGraph_errratio = TGraph2D(10)
    myTGraph_errratio.SetName("Ratio CMSSW/Delphes")

    myTGraph_errratio.SetPoint(0,35,142,0.52)
    myTGraph_errratio.SetPoint(1,50,200,0.046)
    myTGraph_errratio.SetPoint(2,90,200,0.033)
    myTGraph_errratio.SetPoint(3,30,329,0.101)
    myTGraph_errratio.SetPoint(4,70,329,0.020)
    myTGraph_errratio.SetPoint(5,70,575,0.019)
    myTGraph_errratio.SetPoint(6,70,875,0.039)
    myTGraph_errratio.SetPoint(7,142,329,0.018)
    myTGraph_errratio.SetPoint(9,142,875,0.016)
    myTGraph_errratio.SetPoint(10,378,575,0.016)
    myTGraph_errratio.SetPoint(11,378,875,0.015)
    myTGraph_errratio.SetPoint(12,575,875,0.016)
    myTGraph_errratio.SetPoint(13,761,875,0.021)
    myTGraph_errratio.SetPoint(14,50,1200,0.10)
    myTGraph_errratio.SetPoint(8,1200,1200,0.10)

    XSFile_path = "/home/fynu/amertens/Delphes_Analysis/2hdm/xs.root"
    XSFile = TFile(str(XSFile_path))
    xsG2D = XSFile.Get("Graph2D")

    pathDelphesEff = "/home/fynu/amertens/storage/THDM/eff_v1/"
    fileList = os.listdir(pathDelphesEff)

    myTGraph_eff = TGraph2D(len(fileList))
    myTGraph_errratio.SetName("Eff Delphes")
    i = 0
    for feff in fileList:
        DelphesFile = TFile(pathDelphesEff+feff)
        myG2D = DelphesFile.Get("Graph2D")
        mbb = feff.split("_")[1].split(".")[0]
        mllbb = feff.split("_")[0]
        myTGraph_eff.SetPoint(i,int(mbb),int(mllbb),myG2D.Interpolate(int(mbb),int(mllbb)))
        i += 1
    
    for entry in tree :
        for cat in options.categories:
            #Initiate the string to be included in the txt files to compute the limits
            observed = "-1"
            processes = ""
            yields = ""
            bins = ""
            order = ""
            i = 1
	    jesSystString = ""
	    jerSystString = ""
            btagbcSystString = ""
            btaglSystString = ""
            lumiSystString = ""
            leptSystString = ""
            bkg1SystString = ""
            bkg2SystString = ""
            bkg3SystString = ""
            bkg4SystString = ""
            zzSystString = ""
            wzSystString = ""
            wwSystString = ""
            zhSystString = ""
            twSystString = ""
            sigSystString = ""
            nloSystString = ""
            mA = getattr(entry,"mA")
	    mH = getattr(entry,"mH")
            
            eff = myTGraph_eff.Interpolate(int(mA),int(mH))
            if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA),int(mH)-0.1)
            if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA),int(mH)+0.1)
            if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA-0.1),int(mH))
            if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA+0.1),int(mH))
            if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA-0.1),int(mH)-0.01)
            if eff==0 and int(mA)<int(mH)-90 and int(mH)/int(mA)<5: print "eff=0", mA, mH
            ratio = myTGraph_ratio.Interpolate(int(mA),int(mH))
            errratio = myTGraph_errratio.Interpolate(int(mA),int(mH))
            xs=xsG2D.Interpolate(int(mA),int(mH))
            if xs == 0 : xs = xsG2D.Interpolate(int(mA),int(mH)-0.1)
            if xs == 0 : xs = xsG2D.Interpolate(int(mA),int(mH)+0.1)
            if xs == 0 : xs = xsG2D.Interpolate(int(mA-0.1),int(mH))
            if xs == 0 : xs = xsG2D.Interpolate(int(mA+0.1),int(mH))
            if xs == 0 : xs = xsG2D.Interpolate(int(mA-0.1),int(mH)-0.01)
            if xs == 0 and int(mA)<int(mH)-90 and int(mH)/int(mA)<5: print "xs=0", mA, mH
            if "Mu" in cat : fractLept = 0.55
            else : fractLept = 0.45

            SignalYields = 19.7*eff*ratio*xs*fractLept

            if eff<=0 : eff = 1.
            errDelphes = 1/sqrt(100000*eff)
            err_tot = 1+sqrt(errratio*errratio+errDelphes*errDelphes)

	    for sample in samplesList :
                #Select phase space
		key = sample+cat
		Nev = getattr(entry,key)

                #Update the string to be included in the txt file to compute the limits
                proc = key.replace(cat,"")
                N = str("%.3f" % Nev)
		jesSyst = JESsystValues[str(int(mA))+"_"+str(int(mH))][key]
		jesSystStr = str("%.3f" % jesSyst)

		jerSyst = JERsystValues[str(int(mA))+"_"+str(int(mH))][key]
                jerSystStr = str("%.3f" % jerSyst)

                btagbcSyst = BTAGbcsystValues[str(int(mA))+"_"+str(int(mH))][key]
                btagbcSystStr = str("%.3f" % btagbcSyst)

                btaglSyst = BTAGlsystValues[str(int(mA))+"_"+str(int(mH))][key]
                btaglSystStr = str("%.3f" % btaglSyst)
                
                if "DATA" in key : observed = observed.replace("-1", N.replace(".000",""))
                else:
                    if options.TRUEYIELDS : signal = str(SignalYields)+11*" "
                    else : signal = "1."+13*" "
                    processes += (15-len(proc))*" "+proc
                    yields += (15-len(N))*" "+N
                    bins += (15-1)*" "+"1"
                    order += (15-len(str(i)))*" "+str(i)
                    i += 1
		    jesSystString += (15-len(str(jesSystStr)))*" "+str(jesSystStr)
		    jerSystString += (15-len(str(jerSystStr)))*" "+str(jerSystStr)
		    btagbcSystString += (15-len(str(btagbcSystStr)))*" "+str(btagbcSystStr)
		    btaglSystString += (15-len(str(btaglSystStr)))*" "+str(btaglSystStr)
                    if "Zbb" in key or "Zbx" in key : nloSystString += (15-len(str("%.3f" % tgZbx.Eval(mH))))*" "+str("%.3f" % tgZbx.Eval(mH))
                    elif "Zxx" in key : nloSystString += (15-len(str("%.3f" % tgZxx.Eval(mH))))*" "+str("%.3f" % tgZxx.Eval(mH))
                    else : nloSystString += (15-len("-"))*" "+"-"
                    if not "Zbb" in key and not "Zbx" in key and not "Zxx" in key and not "TT" in key : lumiSystString += (15-len(str(1.026)))*" "+str(1.026)
                    else : lumiSystString += (15-len("-"))*" "+"-"
                    leptSystString += (15-len(str(1.03)))*" "+str(1.03)
                    if "TT" in key :
                        bkg1SystString += (15-len(str(options.TTBKG[0])))*" "+str(options.TTBKG[0])
                        bkg2SystString += (15-len(str(options.TTBKG[1])))*" "+str(options.TTBKG[1])
                        bkg3SystString += (15-len(str(options.TTBKG[2])))*" "+str(options.TTBKG[2])
                        bkg4SystString += (15-len(str(options.TTBKG[3])))*" "+str(options.TTBKG[3])
                    elif "Zbb2j" in key :
                        bkg1SystString += (15-len(str(options.ZbbBKG[0])))*" "+str(options.ZbbBKG[0])
                        bkg2SystString += (15-len(str(options.ZbbBKG[1])))*" "+str(options.ZbbBKG[1])
                        bkg3SystString += (15-len(str(options.ZbbBKG[2])))*" "+str(options.ZbbBKG[2])
                        bkg4SystString += (15-len(str(options.ZbbBKG[3])))*" "+str(options.ZbbBKG[3])
                    elif "Zbx" in key or "Zbb3j" in key:
                        bkg1SystString += (15-len(str(options.ZbbjBKG[0])))*" "+str(options.ZbbjBKG[0])
                        bkg2SystString += (15-len(str(options.ZbbjBKG[1])))*" "+str(options.ZbbjBKG[1])
                        bkg3SystString += (15-len(str(options.ZbbjBKG[2])))*" "+str(options.ZbbjBKG[2])
                        bkg4SystString += (15-len(str(options.ZbbjBKG[3])))*" "+str(options.ZbbjBKG[3])
                    elif "Zxx" in key :
                        bkg1SystString += (15-len(str(options.ZxxBKG[0])))*" "+str(options.ZxxBKG[0])
                        bkg2SystString += (15-len(str(options.ZxxBKG[1])))*" "+str(options.ZxxBKG[1])
                        bkg3SystString += (15-len(str(options.ZxxBKG[2])))*" "+str(options.ZxxBKG[2])
                        bkg4SystString += (15-len(str(options.ZxxBKG[3])))*" "+str(options.ZxxBKG[3])
                    else :
                        bkg1SystString += (15-len("-"))*" "+"-"
                        bkg2SystString += (15-len("-"))*" "+"-"
                        bkg3SystString += (15-len("-"))*" "+"-"
                        bkg4SystString += (15-len("-"))*" "+"-"
                    if "ZZ" in key : zzSystString += (15-len(str(1.15)))*" "+str(1.11)
                    else : zzSystString += (15-len("-"))*" "+"-"
                    if "WZ" in key : wzSystString += (15-len(str(1.15)))*" "+str(1.06)
                    else : wzSystString += (15-len("-"))*" "+"-"
                    if "WW" in key : wwSystString += (15-len(str(1.15)))*" "+str(1.09)
                    else : wwSystString += (15-len("-"))*" "+"-"
                    if "ZH" in key : zhSystString += (15-len(str(1.15)))*" "+str(1.07)
                    else : zhSystString += (15-len("-"))*" "+"-"
                    if "Wt" in key : twSystString += (15-len(str(1.15)))*" "+str(1.23)
                    else : twSystString += (15-len("-"))*" "+"-"
                    sigSystString += (15-len("-"))*" "+"-"
            #Get the template files and replace with the good values
            f = open("template.txt","r")
            newfile = f.read()
            newfile = newfile.replace("NCHANNELS",str(i-1)).replace("OBSERVED",observed).replace("SIGNAL",signal).replace("BINS",bins).replace("PROCESSES",processes).replace("ORDER",order).replace("YIELDS",yields).replace("JESBkg",jesSystString).replace("JESSIG",str(1.03)+"  ").replace("JERBkg",jerSystString).replace("JERSIG",str(1.01)+"  ").replace("BTAGbcBkg",btagbcSystString).replace("BTAGbcSIG",str(1.05)+"  ").replace("BTAGlBkg",btaglSystString).replace("BTAGlSIG",str(1.002)+"  ").replace("LUMISIG","1.026  ").replace("LUMIBKG",lumiSystString).replace("LEPTSIG","1.03   ").replace("LEPTBKG",leptSystString).replace("BKG1BKG",bkg1SystString).replace("BKG2BKG",bkg2SystString).replace("BKG3BKG",bkg3SystString).replace("BKG4BKG",bkg4SystString).replace("ZZNORM",zzSystString).replace("WZNORM",wzSystString).replace("WWNORM",wwSystString).replace("ZHNORM",zhSystString).replace("tWNORM",twSystString).replace("Lept",cat).replace("DYNLO",nloSystString).replace("SIGSIG",str("%.3f" % err_tot)).replace("SIGBKG",sigSystString)
            newdir = dirLimits
	    newfilename = str(int(mA))+"_"+str(int(mH))+".txt"
            #Check if directories exist othewise create them
            try:
                os.stat(newdir+"/"+cat)
            except:
                os.mkdir(newdir+"/"+cat)
            #Write output
            outfile = open(newdir+"/"+cat+"/"+newfilename,"w")
            outfile.write(newfile)
	    
            outfile.close()
            f.close()

	    dataCardsList[str(int(mA))+"_"+str(int(mH))]=newdir+"/"+cat+"/"+newfilename
        #break

    return dataCardsList

def getNlist(yieldfile,options):
    #Run over the different categories
    f = TFile.Open(yieldfile,"read")
    tree = f.Get("yields")
    samplesList = options.samples

    Nev={}

    if "DYjets" in samplesList:
        samplesList.remove("DYjets")
        #samplesList.append("Zbb")
        samplesList.append("Zbb2j")
        samplesList.append("Zbb3j")
        samplesList.append("Zbx")
        samplesList.append("Zxx")
    print 'sampleList : ', samplesList

    for entry in tree:
        mA = getattr(entry,"mA")
        mH = getattr(entry,"mH")
	    
	key = str(int(mA))+"_"+str(int(mH))
	Nev[key] = {}
	    
        for sample in samplesList :
	    for cat in options.categories:
                Nev[key][sample+cat] = getattr(entry,sample+cat)
    print Nev
    return Nev

def systValList(systName, fileNom, fileP, fileM, options):
    
    Nev_Nom = getNlist(fileNom,options)
    Nev_Plus = getNlist(fileP,options)
    Nev_Minus = getNlist(fileM,options)  
    systVal = {}
    for key in Nev_Nom :

	systVal[key] = {}
	for cat in options.categories :
	    print ' Syst Line for ', cat, key, " : ",

	    samples = [sample for sample in Nev_Nom[key] if cat in sample]
	    for sample in samples :
		samplekey = sample.replace(cat,"")
		Nn = Nev_Nom[key][sample]
		Np = Nev_Plus[key][sample]
		Nm = Nev_Minus[key][sample]

		if Nn != 0 : systErr = 1+(Np-Nm)/(2*Nn)
		else : systErr = 1
		systVal[key][sample] = systErr
	    print " " 
    return systVal
	    


def main():
    options = options_()
    dirLimits = options.dirLimits 
    JESsValList = systValList("JES", "treeV3_Nominal.root", "treeV3_JESup.root","treeV3_JESdown.root",options)
    JERsValList = systValList("JER", "treeV3_Nominal.root", "treeV3_JERup.root","treeV3_JERdown.root",options)
    BTAGbcsValList = systValList("BTAGbc", "treeV3_Nominal.root", "treeV3_BTAG_bc_up.root","treeV3_BTAG_bc_down.root",options)
    BTAGlsValList = systValList("BTAGl", "treeV3_Nominal.root", "treeV3_BTAG_light_up.root","treeV3_BTAG_light_down.root",options)
    dataCardsList = makeDataCards(options,dirLimits,JESsValList,JERsValList,BTAGbcsValList,BTAGlsValList)
main()
