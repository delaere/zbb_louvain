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

f_SVD7 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_ptZ/outSVD7.root")
f_Bayes4 = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_ptZ/outBayes4.root")

h_SVD7 = f_SVD7.Get("response")
h_Bayes4 = f_Bayes4.Get("response")

output_file = TFile("Combined_rootfiles/pT_Z_Combined_Mix.root", 'RECREATE')
#output_file = TFile("dRZbb_Combined_Mix.root", 'RECREATE')
output_file.cd()


canvas_sup= TCanvas("canvas_tsup","canvas_sup", 500, 500)
canvas_sup.cd()
h_SVD7.SetLineColor(kOrange+10)
h_Bayes4.SetLineColor(kViolet)

h_SVD7.Draw("HIST")
h_Bayes4.Draw("HIST SAME")

legend = TLegend(0.1,0.7,0.48,0.9)
legend.AddEntry(h_SVD7,"SVD (k=7)","f")
legend.AddEntry(h_Bayes4,"Bayes(k=4)","f")
legend.SetFillColor(kWhite);
legend.SetBorderSize(0);

legend.Draw()

output_file.cd()
canvas_sup.Write()

raw_input("Press ENTER to continue")
