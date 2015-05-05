from inc_treePlot import *
import inc_Options
import os
from ROOT import TH1D,TMath
gROOT.SetBatch()

bTag=inc_Options.bTag
stage0 = "llbbX"     #"lljets"  #"llbbX"
chanToRunOn=["Mu","El","MuE"]
cat=inc_Options.cat


applySF=True
SFstrg=""
if applySF: SFstrg="SFRew"
else: SFstrg="noSFRew"

extra = "_bTag"+bTag+"MM_"+SFstrg+"_"+cat     

samples = [
    #"DoubleEle2012A",
    #"DoubleEle2012B",
    #"DoubleEle2012C",
    #"DoubleEle2012D",
    #"DoubleMu2012A",
    #"DoubleMu2012B",
    #"DoubleMu2012C",
    #"DoubleMu2012D",
    #"MuEG2012A",
    #"MuEG2012B",
    #"MuEG2012C",
    #"MuEG2012D",
    "Data2012",
    "DYjets",
    "Zbb",
    "Zbx",
    "Zxx",
    "DYjets_M10to50",
    "ZZ",
    "WZ",
    "ZH125",
    "WW",
    "Wt",
    "Wtbar",
    "TTFullLept",
    "TTSemiLept"
    ]
sampleToRew = [
    "DYjets",
    "Zbb",
    "Zbx",
    "Zxx",    
    "TTFullLept"
    ]
sampleNoWeight = [
    "Data2012",
    "DoubleEle2012A",
    "DoubleEle2012B",
    "DoubleEle2012C",
    "DoubleEle2012D",
    "DoubleMu2012A",
    "DoubleMu2012B",
    "DoubleMu2012C",
    "DoubleMu2012D",
    "MuEG2012A",
    "MuEG2012B",
    "MuEG2012C",
    "MuEG2012D"
    ]
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
    "El":"Electron/boostselectionCentrality",
    "MuE":"MuE/boostselectionCentrality"
    }


DirRew = stage0+extra


def main():
    #if needed make plots for rew
    rewForm = inc_Options.rewForm[stage0]
    for sample in samples:
        if sample in sampleNoWeight : readTree(sample,DirRew)
        elif sample in sampleToRew and applySF:
            if   sample=="TTFullLept"  : readTree(sample,DirRew,{"Mu":rewForm["Mu"]+"*"+inc_Options.wtt,"El":rewForm["El"]+"*"+inc_Options.wtt,"MuE":rewForm["MuE"]+"*"+inc_Options.wtt})
            elif (sample=="DYjets" or sample=="Zbb" or sample=="Zbx" or sample=="Zxx")  : readTree(sample,DirRew,{"Mu":rewForm["Mu"]+"*"+inc_Options.wdy,"El":rewForm["El"]+"*"+inc_Options.wdy,"MuE":rewForm["MuE"]+"*"+inc_Options.wdy})
       
        else:
            readTree(sample,DirRew,rewForm)
	    
	    
	    
    os.system('cd '+DirRew+'; cp ../SUM.sh .;chmod +x SUM.sh;./SUM.sh; cd ..')
    f = open("../../test/input.txt","w")
    f.write(DirRew)
    f.close()
    os.system('cd ../../test/; combinePlots combinePlots_Trees.py; cd -')

main()
