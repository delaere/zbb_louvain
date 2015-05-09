## Script to compute the ROC curve for a given 1D cut ##

from ROOT import *

def main():
    ### Get CPs for the MC and signal where the verible to test is plotted ###
    f_bkgs = TFile("../../test/Zbb_Rew_ZbbnoMETcut_smallMll_RewFormformulaPol3_NotNorm_testRew.root")
    f_sig = TFile("/nfs/user/acaudron/ControlPlots/cp5314p1/AllRDS/Nominal/RDS_ZA_575_142/ZA_575_142_Summer12_final_skimed_zmet.root")

    ### Get the variable to test for the bkgs ###
    metsig = f_bkgs.Get("Combined/jetmetMETsignificance")
    prim = metsig.GetListOfPrimitives()
    for obj in prim:
        if obj.InheritsFrom("THStack") and obj.GetName()==metsig.GetName():
            stack = obj
            break
    bkgs = stack.GetStack().Last()

    ### Get the variable to test for the signal ###
    t_sig = f_sig.Get("rds_zbb")
    sig = TH1D("sig","sig",80,0,40)
    t_sig.Draw("jetmetMETsignificance>>sig","(((rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106))||((rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106)))*leptonsReweightingweight*lumiReweightingLumiWeight*mcReweightingweight*btaggingReweightingMM")

    ### define the TGraphs ###
    effeff = TGraph(len(range(0,bkgs.GetNbinsX()+2)))
    effeff.SetName("effeff")

    sigEff = TGraph(len(range(0,bkgs.GetNbinsX()+2)))
    sigEff.SetName("sigEff")

    bkgEff = TGraph(len(range(0,bkgs.GetNbinsX()+2)))
    bkgEff.SetName("bkgEff")

    roc = TGraph(len(range(0,bkgs.GetNbinsX()+2)))
    roc.SetName("roc")

    print bkgs.Integral(0,bkgs.GetNbinsX()+1), sig.Integral(0,sig.GetNbinsX()+1)
    ### make the 1D scan ###
    for bin in reversed(range(0,bkgs.GetNbinsX()+2)):
        metcut = bkgs.GetXaxis().GetBinUpEdge(bin)
        ### compute the eff. ###
        eff_bkgs = bkgs.Integral(0,bin)/bkgs.Integral(0,bkgs.GetNbinsX()+1)
        eff_sig = sig.Integral(0,bin)/sig.Integral(0,sig.GetNbinsX()+1)
        ### compute the figure of merit ###
        fom = sqrt(bkgs.Integral(0,bin)+10*sig.Integral(0,bin))-sqrt(bkgs.Integral(0,bin))
        #if bkgs.Integral(0,bin)>0 : fom = sqrt(bkgs.Integral(0,bin)+sig.Integral(0,bin))/sqrt(bkgs.Integral(0,bin))
        #else : fom = 0.
        print eff_sig, eff_bkgs
        ### fill the graphs ###
        effeff.SetPoint(bin,eff_sig,eff_bkgs)
        sigEff.SetPoint(bin,metcut,eff_sig)
        bkgEff.SetPoint(bin,metcut,eff_bkgs)
        roc.SetPoint(bin,metcut,fom)
        print bin, metcut, fom

    k = TCanvas()
    ### plot graphs and get the point of max sign. ###
    #roc.Draw("AL")
    print "max is:", TMath.MaxElement(roc.GetN(),roc.GetY())
    sigEff.Draw("AL")
    bkgEff.Draw("L same")
    return (k,roc,sigEff,bkgEff,effeff)

(k,roc,sigEff,bkgEff,effeff) = main()
