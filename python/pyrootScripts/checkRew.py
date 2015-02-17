from treePlot import *
import os
from ROOT import TH1D, TH2D, TFile, TFormula
gROOT.SetBatch()
formulaName = "formulaPol3_C.so"
gSystem.Load(formulaName)

samples = [
    "Data2012",
    #"DY",
    "Zbb",
    "Zbx",
    "Zxx",
    "ZZ",
    "WZ",
    "ZH125",
    "WW",
    "Wt",
    "Wtbar",
    "TTFullLept",
    "TTSemiLept",
    ]
sampleToRew = [
    #"DY",
    "Zbb",
    "Zbx",
    "Zxx",
    ]
sampleNoWeight = ["Data2012"]
sampleToSub = [
    "ZZ",
    "WZ",
    "ZH125",
    "WW",
    "Wt",
    "Wtbar",
    "TTFullLept",
    "TTSemiLept",
    ]
plots={
    #"Mu":"Muon/boostselectionbestzmassMu",
    #"Ele":"Electron/boostselectionbestzmassEle"
    #"Mu":"Muon/boostselectionbestzptMu",
    #"Ele":"Electron/boostselectionbestzptEle"
    #"Mu":"Muon/boostselectiondetab1l2",
    #"Ele":"Electron/boostselectiondetab1l2"
    #"Mu":"Muon/boostselectionZbbM",
    #"Ele":"Electron/boostselectionZbbM"
    #"Mu":"Muon/boostselectionCentralityBoost",
    #"Ele":"Electron/boostselectionCentralityBoost"
    "Mu":"Muon/boostselectionCentrality",
    "Ele":"Electron/boostselectionCentrality"
    }

#extra = "ttbarCR_METsig15"
extra = "lowMET_smallMll_RewForm"+formulaName.replace("formula_","").replace("_C.so","")+"DYdiv"

makeNoRew = False
stage0 = "Zbb"
DirNoRew = stage0+extra+"_NoRew"
make2Dratio = False

makeRew = True
NormWeights = False
NormOut = False
stage1 = "Zbb"
DirRew = stage1+extra+"_Rew_"+stage0+extra#+"_"+plots["Mu"].split("/")[1].replace("Mu","").replace("Ele","").replace("boostselection","")
if not NormWeights : DirRew += "_NotNorm"
if NormOut : DirRew += "_OutNorm"

def main():
    #if needed make plots for rew
    rewFrom = Options.rewFrom[stage0]
    if makeNoRew:
        for sample in samples:
            if sample in sampleNoWeight : readTree(sample,DirNoRew)
            else: 
                if "TT" in sample and stage0=="Zbb" : readTree(sample,DirNoRew,{"Mu":rewFrom["Mu"]+"*"+Options.wtt,"Ele":rewFrom["Ele"]+"*"+Options.wtt})
                elif (sample=="DY" or sample=="Zbb" or sample=="Zbx" or sample=="Zxx") and stage0=="Zbb" : readTree(sample,DirNoRew,{"Mu":rewFrom["Mu"]+"*"+Options.wdy,"Ele":rewFrom["Ele"]+"*"+Options.wdy})
                else : readTree(sample,DirNoRew,rewFrom)
        os.system('cd '+DirNoRew+'; cp ../SUM.sh .; source SUM.sh; cd ..')
        f = open("../../test/input.txt","w")
        f.write(DirNoRew)
        f.close()
        os.system('cd ../../test/; combinePlots combinePlots_Trees.py; cd -')
    if make2Dratio:
        fratio = TFile("../../test/"+DirNoRew+"_testRew.root","UPDATE")
        for plot2D in Options.Vars2D[stage0]:
            Var1 = Options.Vars[stage0][plot2D[0]]
            Var2 = Options.Vars[stage0][plot2D[1]]
            for channel in ["Muon","Electron","Combined"]:
                data = TH2D(Var1["name"]+"_vs_"+Var2["name"]+"_data",Var1["title"]+" vs "+Var2["title"],Var1["bin"]/5,Var1["xmin"],Var1["xmax"],Var2["bin"]/5,Var2["xmin"],Var2["xmax"])
                mc = TH2D(Var1["name"]+"_vs_"+Var2["name"]+"_mc",Var1["title"]+" vs "+Var2["title"],Var1["bin"]/5,Var1["xmin"],Var1["xmax"],Var2["bin"]/5,Var2["xmin"],Var2["xmax"])
                th2d = {}
                #get histos
                for sample in samples:
                    print sample, channel+"/"+plot2D[0]+"_vs_"+plot2D[1]
                    if sample in sampleNoWeight:
                        th2d[sample] = readPlots(sample,DirNoRew,channel+"/"+plot2D[0]+"_vs_"+plot2D[1])
                        data.Add(th2d[sample])
                    else:
                        th2d[sample] = readPlots(sample,DirNoRew,channel+"/"+plot2D[0]+"_vs_"+plot2D[1],rescale=True)
                        mc.Add(th2d[sample])
                ratio = TH2D(data)
                ratio.SetName(data.GetName()+"MC_ratio")
                ratio.Divide(mc)
                print data.GetName()
                fratio.cd(channel)
                data.Write()
                mc.Write()
                ratio.Write()
                
    #compute Rewe
    if not makeRew : return
    rewFromNew = {}
    #differen channels
    for channel in plots:
        Var = Options.Vars[stage0]["boostselectionZbbM"]
        #f = open("formula.txt","r")
        #rewFromNew[channel] = rewFrom[channel] + "*(0.588711+0.0016774*"+Var["name"]+"-1.23045e-06*"+Var["name"]+"*"+Var["name"]+")"
        #rewFromNew[channel] = rewFrom[channel] + "*(0.393175+0.00299873*"+Var["name"]+"-3.65296e-06*"+Var["name"]+"*"+Var["name"]+"+1.20951e-09*"+Var["name"]+"*"+Var["name"]+"*"+Var["name"]+")"
        #rewFromNew[channel] = rewFrom[channel] + "*(0.484993+0.00254296*"+Var["name"]+"-2.996e-06*"+Var["name"]+"*"+Var["name"]+"+9.20487e-10*"+Var["name"]+"*"+Var["name"]+"*"+Var["name"]+")"
        if "lljjMass_jjMass" in formulaName : rewFromNew[channel] = rewFrom[channel] + "*formula(boostselectionZbbM,boostselectiondijetM)"
        elif "Pol3" in formulaName :
            print "Pol3"
            rewFromNew[channel] = rewFrom[channel] + "*formula(boostselectionZbbM,jetmetbjet1Flavor,jetmetbjet2Flavor)"
        else : rewFromNew[channel] = rewFrom[channel] + "*formula(boostselectionZbbM,boostselectiondrll"+channel+")"
        #rewFromNew[channel] = rewFrom[channel] + "*formula(boostselectionbestzpt"+channel+",boostselectiondijetdR)"
        continue
        plot = plots[channel]
        th1d = {}
        #get histos
        for sample in samples:
            print sample, plot
            if sample in sampleNoWeight : th1d[sample] = readPlots(sample,DirNoRew,plot)
            else : th1d[sample] = readPlots(sample,DirNoRew,plot,rescale=True)
        #sum MC and data substraction
        Var = Options.Vars[stage0][plot.split('/')[1]]
        print Var
        totMC = TH1D(Var["name"],Var["title"],Var["bin"],Var["xmin"],Var["xmax"])
        for sample in samples:
            if sample == sampleNoWeight[0] : continue
            elif sample in sampleToSub : th1d[sampleNoWeight[0]].Add(th1d[sample],-1)
            else : totMC.Add(th1d[sample])
        #scale to 1 to remove effects from normalisation effect
        #if NormWeights:
        #    th1d[sampleNoWeight[0]].Scale(1./th1d[sampleNoWeight[0]].Integral())
        #    totMC.Scale(1./totMC.Integral())
        #get ratio and reweighting
        th1d[sampleNoWeight[0]].Divide(totMC)
        rewFrom = Options.rewFrom[stage1]
        weight = "*("
        for i in range(1,Var["bin"]+1):
            ratio = th1d[sampleNoWeight[0]].GetBinContent(i)
            xmin = th1d[sampleNoWeight[0]].GetXaxis().GetBinLowEdge(i)
            xmax = th1d[sampleNoWeight[0]].GetXaxis().GetBinUpEdge(i)
            weight += str(ratio)+"*("+Var["name"]+">="+str(xmin)+"&&"+Var["name"]+"<"+str(xmax)+")+"
        #weight = weight[:-1]+")"
        weight += str(th1d[sampleNoWeight[0]].GetBinContent(Var["bin"]+1))+"*("+Var["name"]+">="+str(xmax)+"))"
        print weight
        rewFromNew[channel] = rewFrom[channel] + weight
    #make plot with rew
    for sample in samples:
        if sample in sampleNoWeight : readTree(sample,DirRew)
        elif sample in sampleToRew :
            if "TT" in sample and stage1=="Zbb" : readTree(sample,DirRew,{"Mu":rewFromNew["Mu"]+"*"+Options.wtt,"Ele":rewFromNew["Ele"]+"*"+Options.wtt})
            elif (sample=="DY" or sample=="Zbb" or sample=="Zbx" or sample=="Zxx") and stage1=="Zbb" : readTree(sample,DirRew,{"Mu":rewFromNew["Mu"]+"*"+Options.wdy,"Ele":rewFromNew["Ele"]+"*"+Options.wdy})
            else : readTree(sample,DirRew,rewFromNew)
        else:
            if "TT" in sample and stage1=="Zbb" : readTree(sample,DirRew,{"Mu":rewFrom["Mu"]+"*"+Options.wtt,"Ele":rewFrom["Ele"]+"*"+Options.wtt})
            elif (sample=="DY" or sample=="Zbb" or sample=="Zbx" or sample=="Zxx") and stage1=="Zbb" : readTree(sample,DirRew,{"Mu":rewFrom["Mu"]+"*"+Options.wdy,"Ele":rewFrom["Ele"]+"*"+Options.wdy})
            else : readTree(sample,DirRew,rewFrom)
    os.system('cd '+DirRew+'; cp ../SUM.sh .; source SUM.sh; cd ..')
    f = open("../../test/input.txt","w")
    f.write(DirRew)
    f.close()
    os.system('cd ../../test/; combinePlots combinePlots_Trees.py; cd -')

main()
