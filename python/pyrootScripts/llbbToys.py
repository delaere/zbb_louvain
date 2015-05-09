## Script to make toy data from MC expectation ##

from array import array
from ROOT import *
from llbbOptions import *

class options_(options_):
    ### define bins ###
    mA_ = [0]
    mbb=10
    sigma=1.0
    for i in range(1,36):
        dmbb=0.15*mbb*1.5
        step_mbb = sigma*0.15*mbb
        mA_.extend([int(mbb-dmbb),int(mbb+dmbb),int(mbb)])
        mbb+=step_mbb

    mH_ = [0]
    mllbb=10
    for i in range(1,36):
        dmllbb=0.15*mllbb*1.5
        step_mllbb = dmllbb/1.5
        mH_.extend([int(mllbb-dmllbb),int(mllbb+dmllbb),int(mllbb)])
        mllbb+=step_mllbb

    ### order bins (centre and boundaries) and remove double ###
    mA_ = sorted(mA_)
    mH_ = sorted(mH_)
    for i, m in enumerate(mA_):
        if i==0 : continue
        if mA_[i] == mA_[i-1] : mA_.pop(i) 
    for i, m in enumerate(mH_):
        if i==0 : continue
        if mH_[i] == mH_[i-1] : mH_.pop(i) 
    print mA_
    print mH_
    

opt = options_()
### get root files with 2D MC disctribution with 1 GeV*1 GeV bins ###
f = TFile("../../test/Zbb_Rew_ZbblowMET_smallMll_RewFormformulaPol3_2DMbbMllbb_NotNorm_testRew.root")
### create arrays ###
mA_ = array('f',opt.mA_)
mH_ = array('f',opt.mH_)

### real MC histo definition using the arrays for the binning ###
h2D_Mu = TH2D("h2D_Mu","h2D_Mu",len(opt.mA_)-1,mA_,len(opt.mH_)-1,mH_)
h2D_El = TH2D("h2D_El","h2D_El",len(opt.mA_)-1,mA_,len(opt.mH_)-1,mH_)

### Get histo from rootfile ###
old2D_Mu = f.Get("Muon/boostselectiondijetM_vs_boostselectionZbbM_mc")
old2D_El = f.Get("Electron/boostselectiondijetM_vs_boostselectionZbbM_mc")

### transform the original hsito into the new one with the variable binning ###
for i in range(0,old2D_Mu.GetNbinsX()+1):
    x = old2D_Mu.GetXaxis().GetBinCenter(i)
    for j in range(0,old2D_Mu.GetNbinsY()+1):
        y = old2D_Mu.GetYaxis().GetBinCenter(j)
        w_Mu = old2D_Mu.GetBinContent(i,j)
        w_El = old2D_El.GetBinContent(i,j)
        h2D_Mu.Fill(x,y,w_Mu)
        h2D_El.Fill(x,y,w_El)

### Set gRandom options ###
gRandom = TRandom3(0)
gRandom.SetSeed(0)

listTH2 = []

### define output file ###
out = TFile("toydata.root","RECREATE")
### create histo for sum of all toys ###
all_Mu = TH2D("all_Mu","all_El",len(opt.mA_)-1,mA_,len(opt.mH_)-1,mH_)
all_El = TH2D("all_El","all_El",len(opt.mA_)-1,mA_,len(opt.mH_)-1,mH_)
### run over the toys ###
for i in range(0,1000):
    ### define histos ###
    tmp_Mu = TH2D("H"+str(i)+"_Mu","H"+str(i)+"_Mu",len(opt.mA_)-1,mA_,len(opt.mH_)-1,mH_)
    tmp_El = TH2D("H"+str(i)+"_El","H"+str(i)+"_El",len(opt.mA_)-1,mA_,len(opt.mH_)-1,mH_)

    ### Random fill with N events=number of expected MC ###
    tmp_Mu.FillRandom(h2D_Mu,int(h2D_Mu.Integral()))
    tmp_El.FillRandom(h2D_El,int(h2D_El.Integral()))

    listTH2.append(tmp_Mu)
    listTH2.append(tmp_El)

    all_Mu.Add(tmp_Mu)
    all_El.Add(tmp_El)

    ### write toys ###
    tmp_Mu.Write()
    tmp_El.Write()

### write sum of toys and real MC ###
all_Mu.Write()
all_El.Write()
h2D_Mu.Write()
h2D_El.Write()
