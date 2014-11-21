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

def make1Dplot(tree, Stage, Var, output, rewFrom):
    th1d = TH1D(Var["name"],Var["title"],Var["bin"],Var["xmin"],Var["xmax"])
    tree.Draw(Var["name"]+">>"+Var["name"],Stage["cut"]+rewFrom)
    if not output.cd(Stage["dir"]) : output.mkdir(Stage["dir"])
    output.cd(Stage["dir"])
    th1d.Write()
    return

def readTree(sample,DirOut,rewFrom={"Mu":"","Ele":""}):
    input = TFile.Open(Options.fileName.replace("SAMPLE",sample))
    tree = input.Get("rds_zbb")
    if not os.path.isdir(DirOut) : os.system('mkdir '+DirOut)
    outputName=DirOut+"/"+sample+".root"
    if os.path.exists(outputName) : os.system('rm '+outputName)
    output=TFile(outputName,"UPDATE")
    stages = Options.Stages[DirOut[:3]]
    for stage in stages:
        print rewFrom[stage]
        print stages[stage]
        for Var in Options.Vars[DirOut[:3]] : make1Dplot(tree,stages[stage],Options.Vars[DirOut[:3]][Var],output,rewFrom[stage])
    return

def readPlots(sample,DirOut,plot,rescale=False):
    input = TFile.Open(DirOut+"/"+sample+".root")
    th1d = input.Get(plot)
    if rescale:
        if sample=="DY" : th1d.Scale(getSample(name=sample+"_2014").source_dataset.xsection*lumi/46515036.)
        else : th1d.Scale(getSample(name=sample+"_2014").source_dataset.xsection*lumi/getSample(name=sample+"_2014").nevents_processed)
    return th1d
