from ROOT import *
gSystem.Load("ReadMVA_C.so")
from llbbOptions import *
import os

Options = options_()
Options.fileName = Options.path.replace("SYST",Options.SYST)

def make1Dplot(tree, Stage, DYdiv, Var, output, rewFrom):
    th1d = TH1D(Var["name"],Var["title"],Var["bin"],Var["xmin"],Var["xmax"])
    th1d.Sumw2()
    tree.Draw(Var["title"]+">>"+Var["name"],"("+Stage["cut"]+DYdiv+")"+rewFrom)
    if not output.cd(Stage["dir"]) : output.mkdir(Stage["dir"])
    output.cd(Stage["dir"])
    th1d.Write()
    return

def make2Dplot(tree, Stage, DYdiv, Var1, Var2, output, rewFrom):
    th2d = TH2D(Var1["name"]+"_vs_"+Var2["name"],Var1["title"]+" vs "+Var2["title"],Var1["bin"],Var1["xmin"],Var1["xmax"],Var2["bin"],Var2["xmin"],Var2["xmax"])
    th2d.Sumw2()
    tree.Draw("("+Var2["title"]+"):("+Var1["title"]+")>>"+Var1["name"]+"_vs_"+Var2["name"],"("+Stage["cut"]+DYdiv+")"+rewFrom,"colz")
    print "("+Var1["title"]+"):("+Var2["title"]+")>>"+Var1["name"]+"_vs_"+Var2["name"], th2d.Integral(1,Var1["bin"],1,Var2["bin"]), th2d.GetBinContent(0,0)
    if not output.cd(Stage["dir"]) : output.mkdir(Stage["dir"])
    output.cd(Stage["dir"])
    th2d.Write()
    return

def readTree(sample,DirOut,rewFrom={"Mu":"","El":""}):
    fileName = Options.fileName
    if sample == "Data2012" : fileName = Options.path_data
    if "Zbb" in sample or "Zbx" in sample or "Zxx" in sample : input = TFile.Open(fileName.replace("NAME","DY"))
    else : input = TFile.Open(fileName.replace("NAME",sample))
    tree = input.Get("rds_zbb")
    if not os.path.isdir(DirOut) : os.system('mkdir '+DirOut)
    outputName=DirOut+"/"+sample+".root"
    if os.path.exists(outputName) : os.system('rm '+outputName)
    output=TFile(outputName,"UPDATE")
    stages = Options.Stages[DirOut[:3]]
    for stage in stages:
        print rewFrom[stage]
        print stages[stage]
        if "Zbb" in sample or "Zbx" in sample or "Zxx" in sample :
            for Var in sorted(Vars[DirOut[:3]].keys()) : make1Dplot(tree,stages[stage],"&&"+Options.DYdiv[sample],Vars[DirOut[:3]][Var],output,rewFrom[stage])
            for var2D in Vars2D[DirOut[:3]] : make2Dplot(tree,stages[stage],"&&"+Options.DYdiv[sample],Vars[DirOut[:3]][var2D[0]],Vars[DirOut[:3]][var2D[1]],output,rewFrom[stage])
        else :
            for Var in sorted(Vars[DirOut[:3]].keys()) : make1Dplot(tree,stages[stage],"",Vars[DirOut[:3]][Var],output,rewFrom[stage])
            for var2D in Vars2D[DirOut[:3]] : make2Dplot(tree,stages[stage],"",Vars[DirOut[:3]][var2D[0]],Vars[DirOut[:3]][var2D[1]],output,rewFrom[stage])
    return

def readPlots(sample,DirOut,plot,rescale=False):
    input = TFile.Open(DirOut+"/"+sample+".root")
    th1d = input.Get(plot)
    if rescale:
        if sample=="DY" : th1d.Scale(lumi["DATA"]/lumi["Zbb"])
        else : th1d.Scale(lumi["DATA"]/lumi[sample])
    return th1d
