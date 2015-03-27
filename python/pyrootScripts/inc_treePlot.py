import os, sys
lib_path = os.path.abspath('/nfs/soft/python/python-2.7.5-sl6_amd64_gcc44/lib/python2.7/site-packages/storm-0.20-py2.7-linux-x86_64.egg/')
lib_path2 = os.path.abspath('/nfs/soft/python/python-2.7.5-sl6_amd64_gcc44/lib/python2.7/site-packages/MySQL_python-1.2.3-py2.7-linux-x86_64.egg')
lib_path3 = os.path.abspath('/nfs/soft/python/python-2.7.5-sl6_amd64_gcc44/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg/')
sys.path.append(lib_path)
sys.path.append(lib_path2)
sys.path.append(lib_path3)


from UserCode.zbb_louvain.zbbSamples import *
from ROOT import *
import inc_Options   
 
def make1Dplot(tree, Stage, DYdiv, Var, output, rewFrom):
    th1d = TH1D(Var["title"],Var["title"],Var["bin"],Var["xmin"],Var["xmax"])
    tree.Draw(Var["name"]+">>"+Var["title"],"("+Stage["cut"]+DYdiv+")"+rewFrom)
    if not output.GetDirectory(Stage["dir"]) : output.mkdir(Stage["dir"])
    output.cd(Stage["dir"])
    th1d.Write()
    return


def readTree(sample,DirOut,rewForm={"Mu":"","El":""},chanToRunOn=["Mu","El"],bTag="JP"):
    theFile = inc_Options.path.replace("SAMPLE",sample).replace("BTAG",bTag)
    print theFile
    if "Zbb" in sample or "Zbx" in sample or "Zxx" in sample : 
      input = TFile.Open(theFile.replace(sample,"DY").replace("BTAG",bTag))
    else : 
      input = TFile.Open(theFile)
    tree = input.Get("rds_zbb")
    if not os.path.isdir(DirOut) : os.system('mkdir '+DirOut)
    outputName=DirOut+"/"+sample+".root"
    if os.path.exists(outputName) : os.system('rm '+outputName)
    output=TFile(outputName,"UPDATE")
    stages = inc_Options.Stages[DirOut.split("_")[0]]  #[stage for stage in inc_Options.Stages[DirOut.split("_")[0]] if stage in chanToRunOn]
    #print stages
    #print inc_Options.Stages[DirOut.split("_")[0]]
    for stage in stages :
	 if stage in chanToRunOn :
		print stage
		#stage=inc_Options.Stages[DirOut.split("_")[0]][chan]
		print rewForm[stage]
		print stages[stage] 
		if "Zbb" in sample or "Zbx" in sample or "Zxx" in sample :
                    for Var in inc_Options.Vars[DirOut.split("_")[0]] : make1Dplot(tree,stages[stage],"&&"+inc_Options.DYdiv[sample],inc_Options.Vars[DirOut.split("_")[0]][Var],output,rewForm[stage])

		else:
		    for Var in inc_Options.Vars[DirOut.split("_")[0]] : make1Dplot(tree,stages[stage],"",inc_Options.Vars[DirOut.split("_")[0]][Var],output,rewForm[stage])
    return

def readPlots(sample,DirOut,plot,rescale=False):
    input = TFile.Open(DirOut+"/"+sample+".root")
    th1d = input.Get(plot)
    if rescale: 
        if sample=="DY" : th1d.Scale(lumi["DATA"]/lumi["Zbb"])
        else : th1d.Scale(lumi["DATA"]/lumi[sample])
        #if sample=="DY" : th1d.Scale(getSample(name=sample+"_2014").source_dataset.xsection*lumi/46515036.)
        #else : 
#		th1d.Scale(getSample(name=sample+"_2014").source_dataset.xsection*lumi/getSample(name=sample+"_2014").nevents_processed)
#		print sample+"_2014 has a reweighting xSec*Lumi/Nevt of ", getSample(name=sample+"_2014").source_dataset.xsection*lumi/getSample(name=sample+"_2014").nevents_processed 
    return th1d
