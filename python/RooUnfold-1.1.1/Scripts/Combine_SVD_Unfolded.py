import sys
import ROOT
import glob
import array
from ROOT import *
gROOT.Macro("~/rootlogon.C")

#from DataFormats.FWLite import Events, Handle

from ROOT import RooUnfoldResponse
from ROOT import RooUnfold
from ROOT import RooUnfoldBayes
#from ROOT import RooUnfoldSvd
# from ROOT import RooUnfoldTUnfold

f_SVD5 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_DeltaRZbb/outSVD5.root")
f_SVD7 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_DeltaRZbb/outSVD7.root")
f_SVD8 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_DeltaRZbb/outSVD8.root")
f_SVD10 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_DeltaRZbb/outSVD10.root")
f_SVD14 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_DeltaRZbb/outSVD14.root")
f_SVD18 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_DeltaRZbb/outSVD18.root")

h_SVD5 = f_SVD5.Get("response")
h_SVD7 = f_SVD7.Get("response")
h_SVD8 = f_SVD8.Get("response")
h_SVD10 = f_SVD10.Get("response")
h_SVD14 = f_SVD14.Get("response")

output_file = TFile("DeltaRZbb_Combined_SVDs.root", 'RECREATE')
output_file.cd()


canvas_sup= TCanvas("canvas_tsup","canvas_sup", 500, 500)
canvas_sup.cd()
h_SVD5.SetLineColor(kOrange)
h_SVD7.SetLineColor(kBlue)
h_SVD8.SetLineColor(kCyan)
h_SVD10.SetLineColor(kMagenta)
h_SVD14.SetLineColor(kGreen)

h_SVD5.Draw("HIST")
h_SVD7.Draw("HIST SAME")
h_SVD8.Draw("HIST SAME")
h_SVD10.Draw("HIST SAME")
h_SVD14.Draw("HIST SAME")

legend = TLegend(0.1,0.7,0.48,0.9)
legend.AddEntry(h_SVD5,"k = 5","f")
legend.AddEntry(h_SVD7,"k = 7","f")
legend.AddEntry(h_SVD8,"k = 8","f")
legend.AddEntry(h_SVD10,"k = 10","f")
legend.AddEntry(h_SVD14,"k = 14","f")
legend.SetFillColor(kWhite);
legend.SetBorderSize(0);

legend.Draw()

output_file.cd()
canvas_sup.Write()

raw_input("Press ENTER to continue")
