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

f_SVD2 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_ptZ/outBayes2.root")
f_SVD4 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_ptZ/outBayes4.root")
f_SVD8 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_ptZ/outBayes8.root")
f_SVD12 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_ptZ/outBayes12.root")
f_SVD20 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_ptZ/outBayes20.root")

h_SVD2 = f_SVD2.Get("response")
h_SVD4 = f_SVD4.Get("response")
h_SVD8 = f_SVD8.Get("response")
h_SVD12 = f_SVD12.Get("response")
h_SVD20 = f_SVD20.Get("response")

output_file = TFile("Combined_rootfiles/pT_Z_Combined_BayesS.root", 'RECREATE')
output_file.cd()


canvas_sup= TCanvas("canvas_tsup","canvas_sup", 500, 500)
canvas_sup.cd()
h_SVD2.SetLineColor(kOrange)
h_SVD4.SetLineColor(kBlue)
h_SVD8.SetLineColor(kCyan)
h_SVD12.SetLineColor(kMagenta)
h_SVD20.SetLineColor(kGreen)

h_SVD2.Draw("HIST")
h_SVD4.Draw("HIST SAME")
h_SVD8.Draw("HIST SAME")
h_SVD12.Draw("HIST SAME")
h_SVD20.Draw("HIST SAME")

legend = TLegend(0.1,0.7,0.48,0.9)
legend.AddEntry(h_SVD2,"k = 2","f")
legend.AddEntry(h_SVD4,"k = 4","f")
legend.AddEntry(h_SVD8,"k = 8","f")
legend.AddEntry(h_SVD12,"k = 12","f")
legend.AddEntry(h_SVD20,"k = 20","f")
legend.SetFillColor(kWhite);
legend.SetBorderSize(0);

legend.Draw()

output_file.cd()
canvas_sup.Write()

raw_input("Press ENTER to continue")
