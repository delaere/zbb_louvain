## Script to write the datacards for the limit computation reading yields and unc. from trees and using a template for the cards ##

import os, sys
import array
from llbbOptions import options_
from ROOT import *

class options_(options_):
    ### list of samples ###
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
        #"ZA_262_99",
        ]
    print samples

### average weights for an event in each samples ###
sampW = {
    "Zbb2j" : 100*0.171218433914,
    "Zbb3j": 100*0.171218433914,
    "Zbx" : 100*0.186451732393,
    "Zxx" : 100*0.242328346814,
    "TTFullLept" : 100*0.0386423126317,
    "TTSemiLept" : 100*0.0736080567437,
    "ZZ" : 100*0.0143406845306,
    "WZ" : 100*0.0703487484842,
    "WW" : 100*0.102420757387,
    "Wt" : 100*0.371548102609,
    "Wtbar" : 100*0.423700374958,
    "ZH125" : 100*0.000428740513781,
    }

### in case of toy data: compute the number of observed events in a given MA-MH bin ###
def toydata(mA, mH, channel, toy=1):
    f = TFile("toydata.root")
    h = f.Get("H"+str(toy)+"_"+channel)
    toydata = 0
    for x in range(1,h.GetNbinsX()+1):
        xlow = h.GetXaxis().GetBinLowEdge(x)
        xup = h.GetXaxis().GetBinUpEdge(x)
        for y in range(1,h.GetNbinsY()+1):
            ylow = h.GetYaxis().GetBinLowEdge(y)
            yup = h.GetYaxis().GetBinUpEdge(y)
            if xlow>=mA[0] and ylow>=mH[0] and xup<=mA[1] and yup<=mH[1] : toydata += h.GetBinContent(x,y)
    if mH[2]>mA[2]+91 :
        card = open("/nfs/user/acaudron/unblindedDatacards2HDM/"+channel+"/"+str(mA[2])+"_"+str(mH[2])+".txt")
        tot=0
        for l in card:
            if "rate" in l:
                mc = l.split()
                mc.remove("rate")
                if channel=="Mu" : mc.remove("0.550000000")
                else : mc.remove("0.450000000")
                for imc in mc : tot += float(imc)
                break
        print "New data/mc ratio:", mA[2], mH[2], toydata/max(tot,0.000001)
    return toydata

### function which makes the datacards ###
def makeDataCards(options, dirLimits, JESsystValues, JERsystValues, BTAGbcsystValues, BTAGlsystValues, MCstatList, toy=1):
    ### Get the file and the nominal tree ###
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

    ### Get rootfiles for the systematics on the NLO/LO reweightings ###
    fZbx = TFile("/home/fynu/amertens/Delphes_Analysis/2hdm/syst_zbx.root")
    tgZbx = fZbx.Get("Graph")
    fZxx = TFile("/home/fynu/amertens/Delphes_Analysis/2hdm/syst_zxx.root")
    tgZxx = fZxx.Get("Graph")

    ### TGraph CMSSW/Delphes signal efficiencies ###
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

    ### Unc. on CMSSW/Delphes signal efficiencies ###
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

    ### get graphs for the signal cross-section and BRs ###
    XSFile_path = "/home/fynu/amertens/Delphes_Analysis/2hdm/generation/sushi/SusHi-1.4.1/xsec_v2.root"
    XSFile = TFile(str(XSFile_path))
    ggH_G2D = XSFile.Get("nnloXsec")
    HZA_G2D = XSFile.Get("ZA_BR")
    Abb_G2D = XSFile.Get("bb_BR")

    ### get the signal Delphes efficiency map ###
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

    ### start running over the bins ###
    for entry in tree :
        for cat in options.categories:
            ### Initiate the strings to be included in the txt files to compute the limits ###
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
            zbb2jStatSystString = "lnN      -         "
            zbb3jStatSystString = "lnN      -         "
            zbxStatSystString = "lnN      -         "
            zxxStatSystString = "lnN      -         "
            ttfullStatSystString = "lnN      -         "
            ttsemiStatSystString = "lnN      -         "
            zzStatSystString = "lnN      -         "
            wzStatSystString = "lnN      -         "
            wwStatSystString = "lnN      -         "
            zhStatSystString = "lnN      -         "
            twStatSystString = "lnN      -         "
            tbarwStatSystString = "lnN      -         "
            sigSystString = ""
            nloSystString = ""

            ### Get MA and MH ###
            mA = getattr(entry,"mA")
	    mH = getattr(entry,"mH")

            ### Get the eff., cross-section and BRs for this bin ###
            eff = myTGraph_eff.Interpolate(int(mA),int(mH))
            if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA),int(mH)-0.1)
            if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA),int(mH)+0.1)
            if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA-0.1),int(mH))
            if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA+0.1),int(mH))
            if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA-0.1),int(mH)-0.01)
            if eff==0 and int(mA)<int(mH)-90 and int(mH)/int(mA)<5: print "eff=0", mA, mH
            ratio = myTGraph_ratio.Interpolate(int(mA),int(mH))
            errratio = myTGraph_errratio.Interpolate(int(mA),int(mH))

            ggH_=ggH_G2D.Interpolate(int(mA),int(mH))
            if ggH_ == 0 : ggH_ = ggH_G2D.Interpolate(int(mA),int(mH)-0.1)
            if ggH_ == 0 : ggH_ = ggH_G2D.Interpolate(int(mA),int(mH)+0.1)
            if ggH_ == 0 : ggH_ = ggH_G2D.Interpolate(int(mA-0.1),int(mH))
            if ggH_ == 0 : ggH_ = ggH_G2D.Interpolate(int(mA+0.1),int(mH))
            if ggH_ == 0 : ggH_ = ggH_G2D.Interpolate(int(mA-0.1),int(mH)-0.01)
            if ggH_ == 0 and int(mA)<int(mH)-90 and int(mH)/int(mA)<5: print "ggH_=0", mA, mH

            HZA_=HZA_G2D.Interpolate(int(mA),int(mH))
            if HZA_ == 0 : HZA_ = HZA_G2D.Interpolate(int(mA),int(mH)-0.1)
            if HZA_ == 0 : HZA_ = HZA_G2D.Interpolate(int(mA),int(mH)+0.1)
            if HZA_ == 0 : HZA_ = HZA_G2D.Interpolate(int(mA-0.1),int(mH))
            if HZA_ == 0 : HZA_ = HZA_G2D.Interpolate(int(mA+0.1),int(mH))
            if HZA_ == 0 : HZA_ = HZA_G2D.Interpolate(int(mA-0.1),int(mH)-0.01)
            if HZA_ == 0 and int(mA)<int(mH)-90 and int(mH)/int(mA)<5: print "HZA_=0", mA, mH

            Abb_=Abb_G2D.Interpolate(int(mA),int(mH))
            if Abb_ == 0 : Abb_ = Abb_G2D.Interpolate(int(mA),int(mH)-0.1)
            if Abb_ == 0 : Abb_ = Abb_G2D.Interpolate(int(mA),int(mH)+0.1)
            if Abb_ == 0 : Abb_ = Abb_G2D.Interpolate(int(mA-0.1),int(mH))
            if Abb_ == 0 : Abb_ = Abb_G2D.Interpolate(int(mA+0.1),int(mH))
            if Abb_ == 0 : Abb_ = Abb_G2D.Interpolate(int(mA-0.1),int(mH)-0.01)
            if Abb_ == 0 and int(mA)<int(mH)-90 and int(mH)/int(mA)<5: print "Abb_=0", mA, mH

            ### If no signal model assume, only assume 1 signal event ee+mm channels combined ###
            ### 0.55 and 0.45 are chosen to represent the difference in efficency between the 2 channels ###
            if "Mu" in cat : fractLept = 0.55
            else : fractLept = 0.45

            ### Compute the expected number of signal events ###
            if options.TRUEYIELDS : SignalYields = 19.7*eff*ratio*ggH_*HZA_*Abb_*0.06729*fractLept*1000
            else : SignalYields = fractLept
            #if SignalYields<0.01 : print "SignalYields =", SignalYields, mA, mH

            ### Compute the unc. on the signal efficieny ###
            if eff<=0 : eff = 1.
            errDelphes = 1/sqrt(100000*eff)
            err_tot = 1+sqrt(errratio*errratio+errDelphes*errDelphes)

            signal = str("%.9f" % SignalYields)+" "
            newdata = 0.
	    for sample in samplesList :
                ### Get the yields for this sample and category ###
		key = sample+cat
		Nev = getattr(entry,key)

                ### Update the strings to be included in the txt file to compute the limits ###
                proc = key.replace(cat,"")
                N = str("%.3f" % Nev)
                ### Choose which observation to use: true data, no data, toy data ###
                if "DATA" in key:
                    if options.data=="useToy" : observed = observed.replace("-1", str(toydata(mA=[int(0.775*mA),int(1.225*mA),int(mA)],mH=[int(0.775*mH),int(1.225*mH),int(mH)],channel=cat,toy=toy)))
                    elif options.data=="sigInj" : continue
                    else : observed = observed.replace("-1", N.replace(".000",""))
                ### Choose what to do with this signal ###
                elif "ZA_262_99" in key and not options.data=="sigInj" : signal = N  
                elif "ZA_262_99" in key : newdata += Nev
                ### Care about other MCs ###
                else:
                    ### calculate fake data in case of signal injection ###
                    newdata += Nev

                    ### care of JES syst. ###
                    jesSyst = JESsystValues[str(int(mA))+"_"+str(int(mH))][key]
                    jesSystStr = str("%.3f" % jesSyst)

                    ### care of JER syst. ###
                    jerSyst = JERsystValues[str(int(mA))+"_"+str(int(mH))][key]
                    jerSystStr = str("%.3f" % jerSyst)

                    ### care of BTAG syst. ###
                    btagbcSyst = BTAGbcsystValues[str(int(mA))+"_"+str(int(mH))][key]
                    btagbcSystStr = str("%.3f" % btagbcSyst)
                    
                    btaglSyst = BTAGlsystValues[str(int(mA))+"_"+str(int(mH))][key]
                    btaglSystStr = str("%.3f" % btaglSyst)

                    ### care of MC stat. syst. ###
                    if Nev>0 : statSyst = 1+MCstatList[str(int(mA))+"_"+str(int(mH))][key]/Nev
                    else : statSyst = 1*sampW[key.replace(cat,"")]
                    statSystStr = str("%.3f" % statSyst)

                    ### make all strings with a length of 15 ###
                    processes += (15-len(proc))*" "+proc
                    yields += (15-len(N))*" "+N
                    bins += (15-1)*" "+"1"
                    order += (15-len(str(i)))*" "+str(i)
                    i += 1
		    jesSystString += (15-len(str(jesSystStr)))*" "+str(jesSystStr)
		    jerSystString += (15-len(str(jerSystStr)))*" "+str(jerSystStr)
		    btagbcSystString += (15-len(str(btagbcSystStr)))*" "+str(btagbcSystStr)
		    btaglSystString += (15-len(str(btaglSystStr)))*" "+str(btaglSystStr)

                    ### care of NLO/LO syst. ###
                    if "Zbb" in key or "Zbx" in key : nloSystString += (15-len(str("%.3f" % tgZbx.Eval(mH))))*" "+str("%.3f" % tgZbx.Eval(mH))
                    elif "Zxx" in key : nloSystString += (15-len(str("%.3f" % tgZxx.Eval(mH))))*" "+str("%.3f" % tgZxx.Eval(mH))
                    else : nloSystString += (15-len("-"))*" "+"-"

                    ### care of lumi syst. ###
                    if not "Zbb" in key and not "Zbx" in key and not "Zxx" in key and not "TT" in key : lumiSystString += (15-len(str(1.026)))*" "+str(1.026)
                    else : lumiSystString += (15-len("-"))*" "+"-"

                    ### care of lept. syst. ###
                    leptSystString += (15-len(str(1.03)))*" "+str(1.03)

                    ### care of bkg fit syst. (+stat. syst. with case of 0 events lnN-> gmN) ###
                    if "TT" in key:
                        bkg1SystString += (15-len(str(options.TTBKG[0])))*" "+str(options.TTBKG[0])
                        bkg2SystString += (15-len(str(options.TTBKG[1])))*" "+str(options.TTBKG[1])
                        bkg3SystString += (15-len(str(options.TTBKG[2])))*" "+str(options.TTBKG[2])
                        bkg4SystString += (15-len(str(options.TTBKG[3])))*" "+str(options.TTBKG[3])
                        if "Full" in key:
                            ttfullStatSystString += (15-len(statSystStr))*" "+statSystStr
                            if Nev==0 : ttfullStatSystString = ttfullStatSystString.replace("lnN","gmN 0")
                            ttsemiStatSystString += (15-len("-"))*" "+"-"
                        else:
                            ttfullStatSystString += (15-len("-"))*" "+"-"
                            ttsemiStatSystString += (15-len(statSystStr))*" "+statSystStr
                            if Nev==0 : ttsemiStatSystString = ttsemiStatSystString.replace("lnN","gmN 0")
                        zbb2jStatSystString += (15-len("-"))*" "+"-"
                        zbb3jStatSystString += (15-len("-"))*" "+"-"
                        zbxStatSystString += (15-len("-"))*" "+"-"
                        zxxStatSystString += (15-len("-"))*" "+"-"
                    elif "Zbb2j" in key:
                        bkg1SystString += (15-len(str(options.ZbbBKG[0])))*" "+str(options.ZbbBKG[0])
                        bkg2SystString += (15-len(str(options.ZbbBKG[1])))*" "+str(options.ZbbBKG[1])
                        bkg3SystString += (15-len(str(options.ZbbBKG[2])))*" "+str(options.ZbbBKG[2])
                        bkg4SystString += (15-len(str(options.ZbbBKG[3])))*" "+str(options.ZbbBKG[3])
                        ttfullStatSystString += (15-len("-"))*" "+"-"
                        ttsemiStatSystString += (15-len("-"))*" "+"-"
                        zbb2jStatSystString += (15-len(statSystStr))*" "+statSystStr
                        if Nev==0 : zbb2jStatSystString = zbb2jStatSystString.replace("lnN","gmN 0")
                        zbb3jStatSystString += (15-len("-"))*" "+"-"
                        zbxStatSystString += (15-len("-"))*" "+"-"
                        zxxStatSystString += (15-len("-"))*" "+"-"
                    elif "Zbx" in key or "Zbb3j" in key:
                        bkg1SystString += (15-len(str(options.ZbbjBKG[0])))*" "+str(options.ZbbjBKG[0])
                        bkg2SystString += (15-len(str(options.ZbbjBKG[1])))*" "+str(options.ZbbjBKG[1])
                        bkg3SystString += (15-len(str(options.ZbbjBKG[2])))*" "+str(options.ZbbjBKG[2])
                        bkg4SystString += (15-len(str(options.ZbbjBKG[3])))*" "+str(options.ZbbjBKG[3])
                        ttfullStatSystString += (15-len("-"))*" "+"-"
                        ttsemiStatSystString += (15-len("-"))*" "+"-"
                        zbb2jStatSystString += (15-len("-"))*" "+"-"
                        if "Zbb3j" in key:
                            zbb3jStatSystString += (15-len(statSystStr))*" "+statSystStr
                            if Nev==0 : zbb3jStatSystString = zbb3jStatSystString.replace("lnN","gmN 0")
                            zbxStatSystString += (15-len("-"))*" "+"-"
                        else:
                            zbb3jStatSystString += (15-len("-"))*" "+"-"
                            zbxStatSystString += (15-len(statSystStr))*" "+statSystStr
                            if Nev==0 : zbxStatSystString = zbxStatSystString.replace("lnN","gmN 0")
                        zxxStatSystString += (15-len("-"))*" "+"-"
                    elif "Zxx" in key:
                        bkg1SystString += (15-len(str(options.ZxxBKG[0])))*" "+str(options.ZxxBKG[0])
                        bkg2SystString += (15-len(str(options.ZxxBKG[1])))*" "+str(options.ZxxBKG[1])
                        bkg3SystString += (15-len(str(options.ZxxBKG[2])))*" "+str(options.ZxxBKG[2])
                        bkg4SystString += (15-len(str(options.ZxxBKG[3])))*" "+str(options.ZxxBKG[3])
                        ttfullStatSystString += (15-len("-"))*" "+"-"
                        ttsemiStatSystString += (15-len("-"))*" "+"-"
                        zbb2jStatSystString += (15-len("-"))*" "+"-"
                        zbb3jStatSystString += (15-len("-"))*" "+"-"
                        zbxStatSystString += (15-len("-"))*" "+"-"
                        zxxStatSystString += (15-len(statSystStr))*" "+statSystStr
                        if Nev==0 : zxxStatSystString = zxxStatSystString.replace("lnN","gmN 0")
                    else:
                        bkg1SystString += (15-len("-"))*" "+"-"
                        bkg2SystString += (15-len("-"))*" "+"-"
                        bkg3SystString += (15-len("-"))*" "+"-"
                        bkg4SystString += (15-len("-"))*" "+"-"
                        ttfullStatSystString += (15-len("-"))*" "+"-"
                        ttsemiStatSystString += (15-len("-"))*" "+"-"
                        zbb2jStatSystString += (15-len("-"))*" "+"-"
                        zbb3jStatSystString += (15-len("-"))*" "+"-"
                        zbxStatSystString += (15-len("-"))*" "+"-"
                        zxxStatSystString += (15-len("-"))*" "+"-"

                    ### care of other bkg norm. syst. (+stat. syst. with case of 0 events lnN-> gmN) ###
                    if "ZZ" in key:
                        zzSystString += (15-len(str(1.15)))*" "+str(1.11)
                        zzStatSystString += (15-len(statSystStr))*" "+statSystStr
                        if Nev==0 : zzStatSystString = zzStatSystString.replace("lnN","gmN 0")
                    else:
                        zzStatSystString += (15-len("-"))*" "+"-"
                        zzSystString += (15-len("-"))*" "+"-"
                    if "WZ" in key:
                        wzStatSystString += (15-len(statSystStr))*" "+statSystStr
                        if Nev==0 : wzStatSystString = wzStatSystString.replace("lnN","gmN 0")
                        wzSystString += (15-len(str(1.15)))*" "+str(1.07)
                    else:
                        wzStatSystString += (15-len("-"))*" "+"-"
                        wzSystString += (15-len("-"))*" "+"-"
                    if "WW" in key:
                        wwStatSystString += (15-len(statSystStr))*" "+statSystStr
                        if Nev==0 : wwStatSystString = wwStatSystString.replace("lnN","gmN 0")
                        wwSystString += (15-len(str(1.15)))*" "+str(1.07)
                    else:
                        wwStatSystString += (15-len("-"))*" "+"-"
                        wwSystString += (15-len("-"))*" "+"-"
                    if "ZH" in key:
                        zhStatSystString += (15-len(statSystStr))*" "+statSystStr
                        if Nev==0 : zhStatSystString = zhStatSystString.replace("lnN","gmN 0")
                        zhSystString += (15-len(str(1.15)))*" "+str(1.07)
                    else:
                        zhStatSystString += (15-len("-"))*" "+"-"
                        zhSystString += (15-len("-"))*" "+"-"
                    if "Wt" in key:
                        if "bar" in key:
                            tbarwStatSystString += (15-len(statSystStr))*" "+statSystStr
                            if Nev==0 : tbarwStatSystString = tbarwStatSystString.replace("lnN","gmN 0")
                            twStatSystString += (15-len("-"))*" "+"-"
                        else:
                            tbarwStatSystString += (15-len("-"))*" "+"-"
                            twStatSystString += (15-len(statSystStr))*" "+statSystStr
                            if Nev==0 : twStatSystString = twStatSystString.replace("lnN","gmN 0")
                        twSystString += (15-len(str(1.15)))*" "+str(1.23)
                    else:
                        tbarwStatSystString += (15-len("-"))*" "+"-"
                        twStatSystString += (15-len("-"))*" "+"-"
                        twSystString += (15-len("-"))*" "+"-"
                    sigSystString += (15-len("-"))*" "+"-"
            if options.data=="sigInj" : observed = observed.replace("-1", str(int(newdata)))
            ### Get the template files and replace with the good values ###
            f = open("template.txt","r")
            newfile = f.read()
            newfile = newfile.replace("NCHANNELS",str(i-1)).replace("OBSERVED",observed).replace("SIGNAL",signal).replace("BINS",bins).replace("PROCESSES",processes).replace("ORDER",order).replace("YIELDS",yields).replace("JESBkg",jesSystString).replace("JESSIG",str(1.03)+"  ").replace("JERBkg",jerSystString).replace("JERSIG",str(1.01)+"  ").replace("BTAGbcBkg",btagbcSystString).replace("BTAGbcSIG",str(1.05)+"  ").replace("BTAGlBkg",btaglSystString).replace("BTAGlSIG",str(1.002)+"  ").replace("LUMISIG","1.026  ").replace("LUMIBKG",lumiSystString).replace("LEPTSIG","1.03   ").replace("LEPTBKG",leptSystString).replace("BKG1BKG",bkg1SystString).replace("BKG2BKG",bkg2SystString).replace("BKG3BKG",bkg3SystString).replace("BKG4BKG",bkg4SystString).replace("ZZNORM",zzSystString).replace("WZNORM",wzSystString).replace("WWNORM",wwSystString).replace("ZHNORM",zhSystString).replace("tWNORM",twSystString).replace("Lept",cat).replace("DYNLO",nloSystString).replace("SIGSIG",str("%.3f" % err_tot)).replace("SIGBKG",sigSystString).replace("lnN      -         Zbb2jSTAT",zbb2jStatSystString).replace("lnN      -         Zbb3jSTAT",zbb3jStatSystString).replace("lnN      -         ZbxSTAT",zbxStatSystString).replace("lnN      -         ZxxSTAT",zxxStatSystString).replace("lnN      -         TTFullSTAT",ttfullStatSystString).replace("lnN      -         TTSemiSTAT",ttsemiStatSystString).replace("lnN      -         ZZSTAT",zzStatSystString).replace("lnN      -         WZSTAT",wzStatSystString).replace("lnN      -         WWSTAT",wwStatSystString).replace("lnN      -         ZHSTAT",zhStatSystString).replace("lnN      -         tWSTAT",twStatSystString).replace("lnN      -         tbarWSTAT",tbarwStatSystString)
            newdir = dirLimits
            ### datacard name ###
            if options.data=="useToy" : newfilename = str(int(mA))+"_"+str(int(mH))+"_"+str(toy)+".txt"
            else : newfilename = str(int(mA))+"_"+str(int(mH))+".txt"
            ### Check if directories exist othewise create them ###
            try:
                os.stat(newdir+"/"+cat)
            except:
                os.mkdir(newdir+"/"+cat)
            ### Write output ###
            outfile = open(newdir+"/"+cat+"/"+newfilename,"w")
            outfile.write(newfile)
	    
            outfile.close()
            f.close()

	    dataCardsList[str(int(mA))+"_"+str(int(mH))]=newdir+"/"+cat+"/"+newfilename
        #break
    return dataCardsList

### function to get the yields from the input trees ###
def getNlist(yieldfile,options):
    ### Get file and tree ###
    f = TFile.Open(yieldfile,"read")
    tree = f.Get("yields")
    samplesList = options.samples

    Nev={}

    if "DYjets" in samplesList:
        samplesList.remove("DYjets")
        samplesList.append("Zbb2j")
        samplesList.append("Zbb3j")
        samplesList.append("Zbx")
        samplesList.append("Zxx")
    print 'sampleList : ', samplesList

    ### run over the bins, get the yields and store  them in dict. ###
    for entry in tree:
        mA = getattr(entry,"mA")
        mH = getattr(entry,"mH")
	    
	key = str(int(mA))+"_"+str(int(mH))
	Nev[key] = {}
	    
        for sample in samplesList :
	    for cat in options.categories:
                try:
                    Nev[key][sample+cat] = getattr(entry,sample+cat)
                except:
                    Nev[key][sample+cat] = 0
                    print "For", sample+cat, "and", key, "sample not found!"
    print Nev
    return Nev

### Compute syst. from Nominal and +- variations ###
def systValList(systName, fileNom, fileP, fileM, options):
    ### Get dict. with yields for the 3 cases ###
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
                ### Get the yields for this sample in this category and for this bin ###
		Nn = Nev_Nom[key][sample]
		Np = Nev_Plus[key][sample]
		Nm = Nev_Minus[key][sample]
                ### Compute the relative unc. and add 1. ###
		if Nn != 0 : systErr = abs(1+(Np-Nm)/(2*Nn))
		else : systErr = 1
		systVal[key][sample] = systErr
	    print " " 
    return systVal
	    
def main(toy=1):
    options = options_()
    ### define output directory ###
    dirLimits = options.dirLimits
    ### get syst. unc. ###
    JESsValList = systValList("JES", options.output.replace("_SYST.root","")+"_Nominal.root", options.output.replace("_SYST.root","")+"_JESup.root",options.output.replace("_SYST.root","")+"_JESdown.root",options)
    JERsValList = systValList("JER", options.output.replace("_SYST.root","")+"_Nominal.root", options.output.replace("_SYST.root","")+"_JERup.root",options.output.replace("_SYST.root","")+"_JERdown.root",options)
    BTAGbcsValList = systValList("BTAGbc", options.output.replace("_SYST.root","")+"_Nominal.root", options.output.replace("_SYST.root","")+"_BTAG_bc_up.root",options.output.replace("_SYST.root","")+"_BTAG_bc_down.root",options)
    BTAGlsValList = systValList("BTAGl", options.output.replace("_SYST.root","")+"_Nominal.root", options.output.replace("_SYST.root","")+"_BTAG_light_up.root",options.output.replace("_SYST.root","")+"_BTAG_light_down.root",options)
    ### get MC stat. unc. ###
    MCstatList = getNlist("treeErrStat_Nominal.root",options)
    ### create the datacards ###
    dataCardsList = makeDataCards(options,dirLimits,JESsValList,JERsValList,BTAGbcsValList,BTAGlsValList,MCstatList,toy=toy)
    
if options_.data=="useToy" and len(sys.argv)>0 : main(toy=int(sys.argv[1]))
else : main()
