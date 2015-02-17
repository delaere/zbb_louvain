import os, sys
lib_path = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/storm-0.20-py2.7-linux-x86_64.egg/')
lib_path2 = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/MySQL_python-1.2.3-py2.7-linux-x86_64.egg')
lib_path3 = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg/')
sys.path.append(lib_path)
sys.path.append(lib_path2)
sys.path.append(lib_path3)
from UserCode.zbb_louvain.zbbSamples import *
lumi=(19.7)*1000

from ROOT import *
import Options

def make1Dplot(tree, Stage, DYdiv, Var, output, rewFrom):
    th1d = TH1D(Var["name"],Var["title"],Var["bin"],Var["xmin"],Var["xmax"])
    tree.Draw(Var["title"]+">>"+Var["name"],"("+Stage["cut"]+DYdiv+")"+rewFrom)
    if not output.cd(Stage["dir"]) : output.mkdir(Stage["dir"])
    output.cd(Stage["dir"])
    th1d.Write()
    return

def make2Dplot(tree, Stage, Var1, Var2, output, rewFrom):
    th2d = TH2D(Var1["name"]+"_vs_"+Var2["name"],Var1["title"]+" vs "+Var2["title"],Var1["bin"]/5,Var1["xmin"],Var1["xmax"],Var2["bin"]/5,Var2["xmin"],Var2["xmax"])
    tree.Draw("("+Var2["title"]+"):("+Var1["title"]+")>>"+Var1["name"]+"_vs_"+Var2["name"],Stage["cut"]+rewFrom,"colz")
    print "("+Var1["title"]+"):("+Var2["title"]+")>>"+Var1["name"]+"_vs_"+Var2["name"], th2d.Integral(1,Var1["bin"],1,Var2["bin"]), th2d.GetBinContent(0,0)
    if not output.cd(Stage["dir"]) : output.mkdir(Stage["dir"])
    output.cd(Stage["dir"])
    th2d.Write()
    return

def readTree(sample,DirOut,rewFrom={"Mu":"","Ele":""}):
    fileName = Options.fileName
    if sample == "Data2012" : fileName = "/nfs/user/acaudron/ControlPlots/cp5314p1/AllRDS/Nominal/RDS_Data2012/Data2012_Summer12_final_skimed_zmet.root"
    if "Zbb" in sample or "Zbx" in sample or "Zxx" in sample : input = TFile.Open(fileName.replace("SAMPLE","DY"))
    else : input = TFile.Open(fileName.replace("SAMPLE",sample))
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
            for Var in sorted(Options.Vars[DirOut[:3]].keys()) : make1Dplot(tree,stages[stage],"&&"+Options.DYdiv[sample],Options.Vars[DirOut[:3]][Var],output,rewFrom[stage])
        else :
            for Var in sorted(Options.Vars[DirOut[:3]].keys()) : make1Dplot(tree,stages[stage],"",Options.Vars[DirOut[:3]][Var],output,rewFrom[stage])
        #for var2D in Options.Vars2D[DirOut[:3]] : make2Dplot(tree,stages[stage],Options.Vars[DirOut[:3]][var2D[0]],Options.Vars[DirOut[:3]][var2D[1]],output,rewFrom[stage])
    return

def readPlots(sample,DirOut,plot,rescale=False):
    input = TFile.Open(DirOut+"/"+sample+".root")
    th1d = input.Get(plot)
    if rescale:
        if sample=="DY" : th1d.Scale(getSample(name=sample+"_2014").source_dataset.xsection*lumi/46515036.)
        else : th1d.Scale(getSample(name=sample+"_2014").source_dataset.xsection*lumi/getSample(name=sample+"_2014").nevents_processed)
    return th1d
