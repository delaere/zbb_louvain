from treePlot import *
import os
from ROOT import TH1D
gROOT.SetBatch()

samples = [
    "Data2012",
    "DY",
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
    "DY",
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
extra = "lowMET_largeMll_bareljet1jet2"

makeNoRew = True
stage0 = "Zjj"
DirNoRew = stage0+extra+"_NoRew"

makeRew = False
NormWeights = False
NormOut = False
stage1 = "Zjj"
DirRew = stage1+extra+"_Rew_"+stage0+extra+"_"+plots["Mu"].split("/")[1].replace("Mu","").replace("Ele","").replace("boostselection","")
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
                elif sample=="DY" and stage0=="Zbb" : readTree(sample,DirNoRew,{"Mu":rewFrom["Mu"]+"*"+Options.wdy,"Ele":rewFrom["Ele"]+"*"+Options.wdy})
                else : readTree(sample,DirNoRew,rewFrom)
        os.system('cd '+DirNoRew+'; cp ../SUM.sh .; source SUM.sh; cd ..')
        f = open("../../test/input.txt","w")
        f.write(DirNoRew)
        f.close()
        os.system('cd ../../test/; combinePlots combinePlots_Trees.py; cd -')
    #compute Rewe
    if not makeRew : return
    rewFromNew = {}
    #differen channels
    for channel in plots:
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
        if NormWeights:
            th1d[sampleNoWeight[0]].Scale(1./th1d[sampleNoWeight[0]].Integral())
            totMC.Scale(1./totMC.Integral())
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
            elif sample=="DY" and stage1=="Zbb" : readTree(sample,DirRew,{"Mu":rewFromNew["Mu"]+"*"+Options.wdy,"Ele":rewFromNew["Ele"]+"*"+Options.wdy})
            else : readTree(sample,DirRew,rewFromNew)
        else:
            if "TT" in sample and stage1=="Zbb" : readTree(sample,DirRew,{"Mu":rewFrom["Mu"]+"*"+Options.wtt,"Ele":rewFrom["Ele"]+"*"+Options.wtt})
            elif sample=="DY" and stage1=="Zbb" : readTree(sample,DirRew,{"Mu":rewFrom["Mu"]+"*"+Options.wdy,"Ele":rewFrom["Ele"]+"*"+Options.wdy})
            else : readTree(sample,DirRew,rewFrom)
    os.system('cd '+DirRew+'; cp ../SUM.sh .; source SUM.sh; cd ..')
    f = open("../../test/input.txt","w")
    f.write(DirRew)
    f.close()
    os.system('cd ../../test/; combinePlots combinePlots_Trees.py; cd -')

main()
