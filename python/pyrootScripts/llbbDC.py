
from llbbOptions import options_
from ROOT import *
from listForRDS import lumi
import array
import os


def makeDataCards(options,dirLimits, JESsystValues, JERsystValues,BTAGbcsystValues,BTAGlsystValues):
    #Run over the different categories
    f = TFile.Open("tree_Nominal.root","read")
    tree = f.Get("yields")
    samplesList = options.samples
    dataCardsList = {}
    if "DYjets" in samplesList:
        samplesList.remove("DYjets")
        samplesList.append("Zbb")
        #samplesList.append("Zbb2j")
        #samplesList.append("Zbb3j")
        samplesList.append("Zbx")
        samplesList.append("Zxx")
    print 'sampleList : ', samplesList

    fZbx = TFile("/home/fynu/amertens/Delphes_Analysis/2hdm/syst_zbx.root")
    tgZbx = fZbx.Get("Graph")
    fZxx = TFile("/home/fynu/amertens/Delphes_Analysis/2hdm/syst_zxx.root")
    tgZxx = fZxx.Get("Graph")

    for entry in tree :
    #treeName = "yields"
    #for entry in f.treeName :
        for cat in options.categories:
            #Initiate the string to be included in the txt files to compute the limits
            observed = "-1"
            processes = ""
            yields = ""
            signal = "SIGNAL"
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
            nloSystString = ""
            mA = getattr(entry,"mA")
	    mH = getattr(entry,"mH")

	    for sample in samplesList :
                #Select phase space
		key = sample+cat
		print key
		Nev = getattr(entry,key)
		print key, Nev

#                print rep, key, srRDSentries*(lumi["DATA"]/lumi[key.replace(cat,"")])
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
                #elif "ZA_350_70" in key : signal = signal.replace("SIGNAL", N)
                else:
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
                    if not "Zbb" in key and not "Zbx" in key and not "Zxx" in key and not "TT" in key : lumiSystString += (15-len(str(1.023)))*" "+str(1.023)
                    else : lumiSystString += (15-len("-"))*" "+"-"
                    leptSystString += (15-len(str(1.02)))*" "+str(1.02)
                    if "TT" in key :
                        bkg1SystString += (15-len(str(options.TTBKG[0])))*" "+str(options.TTBKG[0])
                        bkg2SystString += (15-len(str(options.TTBKG[1])))*" "+str(options.TTBKG[1])
                        bkg3SystString += (15-len(str(options.TTBKG[2])))*" "+str(options.TTBKG[2])
                        bkg4SystString += (15-len(str(options.TTBKG[3])))*" "+str(options.TTBKG[3])
                    #if "Zbb2j" in key :
                    elif "Zbb" in key :
                        bkg1SystString += (15-len(str(options.ZbbBKG[0])))*" "+str(options.ZbbBKG[0])
                        bkg2SystString += (15-len(str(options.ZbbBKG[1])))*" "+str(options.ZbbBKG[1])
                        bkg3SystString += (15-len(str(options.ZbbBKG[2])))*" "+str(options.ZbbBKG[2])
                        bkg4SystString += (15-len(str(options.ZbbBKG[3])))*" "+str(options.ZbbBKG[3])
                    elif "Zbx" in key:# or "Zbb3j" in key:
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
                    if "ZZ" in key : zzSystString += (15-len(str(1.15)))*" "+str(1.15)
                    else : zzSystString += (15-len("-"))*" "+"-"
                    if "WZ" in key : wzSystString += (15-len(str(1.15)))*" "+str(1.15)
                    else : wzSystString += (15-len("-"))*" "+"-"
                    if "WW" in key : wwSystString += (15-len(str(1.15)))*" "+str(1.15)
                    else : wwSystString += (15-len("-"))*" "+"-"
                    if "ZH" in key : zhSystString += (15-len(str(1.15)))*" "+str(1.15)
                    else : zhSystString += (15-len("-"))*" "+"-"
                    if "Wt" in key : twSystString += (15-len(str(1.15)))*" "+str(1.15)
                    else : twSystString += (15-len("-"))*" "+"-"
            #Get the template files and replace with the good values
            f = open("template.txt","r")
            newfile = f.read()
            newfile = newfile.replace("NCHANNELS",str(i-1)).replace("OBSERVED",observed).replace("SIGNAL",signal).replace("BINS",bins).replace("PROCESSES",processes).replace("ORDER",order).replace("YIELDS",yields).replace("JESBkg",jesSystString).replace("SIGNAL",str(1.)+"     ").replace("JESSIG",str(1.03)+"  ").replace("JERBkg",jerSystString).replace("JERSIG",str(1.03)+"  ").replace("BTAGbcBkg",btagbcSystString).replace("BTAGbcSIG",str(1.05)+"  ").replace("BTAGlBkg",btaglSystString).replace("BTAGlSIG",str(1.00)+"  ").replace("LUMISIG","1.023  ").replace("LUMIBKG",lumiSystString).replace("LEPTSIG","1.02   ").replace("LEPTBKG",leptSystString).replace("BKG1BKG",bkg1SystString).replace("BKG2BKG",bkg2SystString).replace("BKG3BKG",bkg3SystString).replace("BKG4BKG",bkg4SystString).replace("ZZNORM",zzSystString).replace("WZNORM",wzSystString).replace("WWNORM",wwSystString).replace("ZHNORM",zhSystString).replace("tWNORM",twSystString).replace("Lept",cat).replace("DYNLO",nloSystString)
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
        samplesList.append("Zbb")
        #samplesList.append("Zbb2j")
        #samplesList.append("Zbb3j")
        samplesList.append("Zbx")
        samplesList.append("Zxx")
    print 'sampleList : ', samplesList

    for entry in tree :
    #treeName = "yields"
    #for entry in f.treeName :

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
    #for cat in options.categories :
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
		print " | ", sample, systErr, 
	    print " " 
    return systVal
	    


def main():
    options = options_()
    dirLimits = options.dirLimits #"/home/fynu/amertens/storage/THDM/DataCards"
    JESsValList = systValList("JES", "tree_Nominal.root", "tree_JESup.root","tree_JESdown.root",options)
    JERsValList = systValList("JER", "tree_Nominal.root", "tree_JERup.root","tree_JERdown.root",options)
    BTAGbcsValList = systValList("BTAGbc", "tree_Nominal.root", "tree_BTAG_bc_up.root","tree_BTAG_bc_down.root",options)
    BTAGlsValList = systValList("BTAGl", "tree_Nominal.root", "tree_BTAG_light_up.root","tree_BTAG_light_down.root",options)
    dataCardsList = makeDataCards(options,dirLimits,JESsValList,JERsValList,BTAGbcsValList,BTAGlsValList)
main()
