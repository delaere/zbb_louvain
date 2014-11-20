
from ROOT import *
from listForRDS import lumi
import os

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
        "ZA_350_70",
        ]
    #template for file name
    path = "/home/fynu/amertens/storage/Zbb_Analysis/OPTION/RDS_NAME/NAME_Summer12_final_skimedLL.root"
    #option to split or not the DY sample
    doDYsplit = True
    #stages
    stages = {
        "Mu" : "rc_stage_18",
        "El" : "rc_stage_37"
        }
    print "stages:", stages
    #BTAG weight
    BTAG = "BtaggingReweightingMM"
    if "11" in stages["Mu"] or "14" in stages["Mu"] or "17" in stages["Mu"] : BTAG = "BtaggingReweightingLM"
    elif "10" in stages["Mu"] or "13" in stages["Mu"] or "16" in stages["Mu"] : BTAG = "BtaggingReweightingLL"
    print "BTAG:", BTAG
    #define cuts
    presel = "("+stages["El"]+"_idx || "+stages["Mu"]+"_idx)"

#    rangeMassA = [
#        [20,40],
#        [40,60],
#	[60,80],
#	[80,100],
#	[100,120],
#	[120,140],
#	[140,160],
 #       ]
#    rangeMassH = [
#        [450,500],
#        ]


    rangeMassA = []
    mbb=10
    for i in range(1,36):
      dmbb=0.15*mbb*1.5
      step_mbb = dmbb/1.5
      rangeMassA.append([int(mbb-dmbb),int(mbb+dmbb)])
      mbb+=step_mbb

    rangeMassH = []
    mllbb=10
    for i in range(1,36):
      dmllbb=0.15*mllbb*1.5
      step_mllbb = dmllbb/1.5
      rangeMassH.append([int(mllbb-dmllbb),int(mllbb+dmllbb)])
      mllbb+=step_mllbb

    cut = {}
    for mA in rangeMassA:
        for mH in rangeMassH:
            key = "mA"+str(mA[0])+"to"+str(mA[1])+"_mH"+str(mH[0])+"to"+str(mH[1])
            cut[key] = "eventSelectiondijetM>="+str(mA[0])+"&&eventSelectiondijetM<"+str(mA[1])+"&&eventSelectionZbbM>="+str(mH[0])+"&&eventSelectionZbbM<"+str(mH[1])
            print "signal regions:", key, cut[key]
    #categories
    categories = {
        "Mu" : stages["Mu"],
        "El" : stages["El"],
        #"El2j" : stages["El"]+"&&jetmetnj==2",
        #"El3j" : stages["El"]+"&&jetmetnj>2",
        #"Mu2j" : stages["Mu"]+"&&jetmetnj==2",
        #"Mu3j" : stages["Mu"]+"&&jetmetnj>2"
        }
    print "categories:", categories
    #name of the output file
    output = "output.root"
    #name of the directory where the txt for the limit will be written
    dirLimits = "/home/fynu/amertens/scratch/CMSSW/CMSSW_6_1_1/src/2HDM/"
    
#method to make all needed RDS
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

def makeSR(output, RDS, rep, cut, categories, dirLmits):
    #Run over the different categories
    for cat in categories:
        #Prepare the output roofiles
        #output.mkdir(cat+rep,cut)
        #output.cd(cat+rep)
        #Get the keys sorted
        keys = [key for key in RDS if cat in key]
        keys.sort()
        #Initiate the string to be included in the txt files to compute the limits
        observed = "-1"
        processes = ""
        yields = ""
	signal = "SIGNAL"
        bins = ""
        order = ""
        i = 1
        #Run over the samples
        for key in keys:
            #Select phase space
            srRDSentries = RDS[key].sumEntries(cut)
            #srRDSentries = srRDS.sumEntries()
	    #srRDS.Delete()
            #Fill histograms
            #hist = TH1F(key.replace(cat,"").replace("DATA","data_obs"),key.replace(cat,""),1,0,1)
            #hist.SetBinContent(1, srRDS.sumEntries()*(lumi["DATA"]/lumi[key.replace(cat,"")]))
            #hist.SetBinContent(1, srRDSentries*(lumi["DATA"]/lumi[key.replace(cat,"")]))
            #hist.Write()
            #print rep, key, srRDS.sumEntries()*(lumi["DATA"]/lumi[key.replace(cat,"")])
            print rep, key, srRDSentries*(lumi["DATA"]/lumi[key.replace(cat,"")])
            #Update the string to be included in the txt file to compute the limits
            proc = key.replace(cat,"")
            #Nev = srRDS.sumEntries()*(lumi["DATA"]/lumi[key.replace(cat,"")])
            Nev = srRDSentries*(lumi["DATA"]/lumi[key.replace(cat,"")])
            N = str("%.3f" % Nev)
            if "DATA" in key : observed = observed.replace("-1", N.replace(".000",""))
	    elif "ZA_350_70" in key : signal = signal.replace("SIGNAL", N)
            else:
                processes += (15-len(proc))*" "+proc
                yields += (15-len(N))*" "+N
                bins += (15-1)*" "+"1"
                order += (15-len(str(i)))*" "+str(i)
                i += 1
        #Get the template files and replace with the good values
        f = open("template.txt","r")
        newfile = f.read()
        newfile = newfile.replace("NCHANNELS",str(i-1)).replace("OBSERVED",observed).replace("SIGNAL",signal).replace("BINS",bins).replace("PROCESSES",processes).replace("ORDER",order).replace("YIELDS",yields)
        newdir = dirLmits+rep.split("_")[1]
        #Check if directories exist othewise create them
        try:
            os.stat(newdir+"/"+cat)
        except:
            try:
                os.stat(newdir)
                os.mkdir(newdir+"/"+cat)
            except:
                os.mkdir(newdir)
                os.mkdir(newdir+"/"+cat)
        #Write output
        outfile = open(newdir+"/"+cat+"/test"+rep.split("_")[0]+".txt","w")
        outfile.write(newfile)
	outfile.close()
	f.close()
    return

def makeSRSyst(output, RDS, RDSp, RDSm, rep, cut, categories, dirLmits):
    #Run over the different categories
    for cat in categories:
        #Prepare the output roofiles
        #output.mkdir(cat+rep,cut)
        #output.cd(cat+rep)
        #Get the keys sorted
        keys = [key for key in RDS if cat in key]
        keys.sort()
        #Initiate the string to be included in the txt files to compute the limits
        observed = "-1"
        processes = ""
        yields = ""
        signal = "SIGNAL"
        bins = ""
        order = ""
        i = 1
        #Run over the samples
        for key in keys:
            #Select phase space
            srRDSentries = RDS[key].sumEntries(cut) 
            print rep, key, srRDSentries*(lumi["DATA"]/lumi[key.replace(cat,"")])
            #Update the string to be included in the txt file to compute the limits
            proc = key.replace(cat,"")
            #Nev = srRDS.sumEntries()*(lumi["DATA"]/lumi[key.replace(cat,"")])
            Nev = srRDSentries*(lumi["DATA"]/lumi[key.replace(cat,"")])
            N = str("%.3f" % Nev)


            # JES Syst Up
            srRDSPentries = RDSp[key].sumEntries(cut)
            NevP = srRDSPentries*(lumi["DATA"]/lumi[key.replace(cat,"")])
            # JES Syst Down
            srRDSMentries = RDSm[key].sumEntries(cut)
            NevM = srRDSMentries*(lumi["DATA"]/lumi[key.replace(cat,"")])

            #syst computation
            syst_val = (NevP-NevM)/(2*Nev)
            syst = str("%.3f" % syst_val)

            if "DATA" in key : observed = observed.replace("-1", N.replace(".000",""))
            elif "ZA_350_70" in key : 
                signal = signal.replace("SIGNAL", N)
                signal_syst = signal_syst.replace("JESSIG", syst)
            else:
                processes += (15-len(proc))*" "+proc
                yields += (15-len(N))*" "+N
                bins += (15-1)*" "+"1"
                order += (15-len(str(i)))*" "+str(i)
                i += 1
		jes_syst += (15-len(syst))*" "+syst


        #Get the template files and replace with the good values
        f = open("template.txt","r")
        newfile = f.read()
        newfile = newfile.replace("NCHANNELS",str(i-1)).replace("OBSERVED",observed).replace("SIGNAL",signal).replace("BINS",bins).replace("PROCESSES",processes).replace("ORDER",order).replace("YIELDS",yields).replace("JESBkg",jes_syst).replace("JESSIG", signal_syst)
        newdir = dirLmits+rep.split("_")[1]
        #Check if directories exist othewise create them
        try:
            os.stat(newdir+"/"+cat)
        except:
            try:
                os.stat(newdir)
                os.mkdir(newdir+"/"+cat)
            except:
                os.mkdir(newdir)
                os.mkdir(newdir+"/"+cat)
        #Write output
        outfile = open(newdir+"/"+cat+"/test"+rep.split("_")[0]+".txt","w")
        outfile.write(newfile)
        outfile.close()
        f.close()
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
    RDS = createRDS(files=files, options=options)
    RDS = bkgNorm(RDS)
    #Make and store hists
    output = TFile(options.output,"RECREATE")
    for key in options.cut : makeSR(output, RDS, key, options.cut[key], options.categories, options.dirLimits)
    return

main()
