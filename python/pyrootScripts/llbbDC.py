from llbbOptions import options_
from ROOT import *
from listForRDS import lumi
import array
import os


def makeDataCards(options,dirLimits, JESsystValues):
    #Run over the different categories
    f = TFile.Open("tree.root","read")
    tree = f.Get("yields")
    samplesList = options.samples
    dataCardsList = {}
    if "DYjets" in samplesList:
        samplesList.remove("DYjets")
        samplesList.append("Zbb")
        samplesList.append("Zbx")
        samplesList.append("Zxx")
    print 'sampleList : ', samplesList

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
                if "DATA" in key : observed = observed.replace("-1", N.replace(".000",""))
                elif "ZA_350_70" in key : signal = signal.replace("SIGNAL", N)
                else:
                    processes += (15-len(proc))*" "+proc
                    yields += (15-len(N))*" "+N
                    bins += (15-1)*" "+"1"
                    order += (15-len(str(i)))*" "+str(i)
                    i += 1
		    jesSystString += (15-len(str(jesSystStr)))*" "+str(jesSystStr)
            #Get the template files and replace with the good values
            f = open("template.txt","r")
            newfile = f.read()
            newfile = newfile.replace("NCHANNELS",str(i-1)).replace("OBSERVED",observed).replace("SIGNAL",signal).replace("BINS",bins).replace("PROCESSES",processes).replace("ORDER",order).replace("YIELDS",yields).replace("JESBkg",jesSystString).replace("SIGNAL",str(1)+"     ").replace("JESSIG",str(1.03)+"  ")
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
    dirLimits = "/home/fynu/amertens/storage/THDM/DataCards"
    JESsValList = systValList("JES", "tree_Nom.root", "tree_JESup.root","tree_JESdown.root",options)
    dataCardsList = makeDataCards(options,dirLimits,JESsValList)
main()
