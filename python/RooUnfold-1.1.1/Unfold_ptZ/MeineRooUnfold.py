#!/usr/bin/env python
# ==============================================================================
#  File and Version Information:
#       $Id: RooUnfoldExample.py 302 2011-09-30 20:39:20Z T.J.Adye $
#
#  Description:
#       Simple example usage of the RooUnfold package using toy MC.
#
#  Author: Tim Adye <T.J.Adye@rl.ac.uk>
#
# ==============================================================================
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

## sys.path.append('/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/')
from UserCode.zbb_louvain.zbbCommons import zbbnorm
lumi=zbbnorm.lumi_totEle2011*1000 #in pb-1
lumi_Mu=zbbnorm.lumi_totMu2011*1000 #in pb-1
lumi_El=zbbnorm.lumi_totEle2011*1000 #in pb-1

#compute scales
ttScale_Mu = zbbnorm.xsec_TTjets_7TeV*lumi_Mu/zbbnorm.nev_TTjets_fall11     #157.5*5050./(3701947.)), #NLO MCFM proper Xs
print "ttScale_Mu",ttScale_Mu
zzScale_Mu = zbbnorm.xsec_ZZ_7TeV*lumi_Mu/zbbnorm.nev_ZZ_fall11             #6.206*5050./(4191045.)), #Xs 
print "zzScale_Mu",zzScale_Mu
dyScale_Mu = zbbnorm.xsec_DYjets_7TeV*lumi_Mu/zbbnorm.nev_DYjets_fall11     #3048.*5050./35907791.), #NLO MCFM
print "dyScale_Mu",dyScale_Mu

ttScale_El = zbbnorm.xsec_TTjets_7TeV*lumi_El/zbbnorm.nev_TTjets_fall11     #157.5*4990./(3701947.)), #NLO MCFM proper Xs
zzScale_El = zbbnorm.xsec_ZZ_7TeV*lumi_El/zbbnorm.nev_ZZ_fall11             #6.206*4990./(4191045.)), #Xs 
dyScale_El = zbbnorm.xsec_DYjets_7TeV*lumi_El/zbbnorm.nev_DYjets_fall11     #3048.*4990./35907791.), #NLO MCFM

#print "=========== getting data plot to unfold for setting the binning ============="
#f_data = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/combined_Plots_JES_final_V_SaveHisto_Combined.root")
#hdata = f_data.Get("h_data")
#print "data distribution :", hdata.GetTitle()
#print "number of bin in data histo : ", hdata.GetNbinsX() 
#print "minumum in data histo : ", hdata.GetXaxis().GetXmin()
#print "maximum in data histo : ", hdata.GetXaxis().GetXmax()

print "=========== getting data files  ============="
fMuon_A  = TFile("/nfs/user/acaudron/ControlPlots/cp444/ControlPlots_V4/ControlPlots_Mu2011A/Mu2011A_Fall11_final.root")
fMuon_B  = TFile("/nfs/user/acaudron/ControlPlots/cp444/ControlPlots_V4/ControlPlots_Mu2011B/Mu2011B_Fall11_final.root")
fEle_A   = TFile("/nfs/user/acaudron/ControlPlots/cp444/ControlPlots_V4/ControlPlots_Ele2011A/Ele2011A_Fall11_final.root")
fEle_B   = TFile("/nfs/user/acaudron/ControlPlots/cp444/ControlPlots_V4/ControlPlots_Ele2011B/Ele2011B_Fall11_final.root")

print "=========== getting mc files  ============="
fTTbar = TFile("/home/fynu/rcastello/Physics/Zbb/Aug2012_full2011/upgrade_version/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/ControlPlots_V5/ControlPlots_TT/CP_TTbar_v5_combined.root")
fZZ = TFile("/home/fynu/rcastello/Physics/Zbb/Aug2012_full2011/upgrade_version/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/ControlPlots_V5/ControlPlots_ZZ/CP_ZZ_v5_combined.root")
fZl = TFile("/home/fynu/rcastello/Physics/Zbb/Aug2012_full2011/upgrade_version/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/ControlPlots_V5/ControlPlots_Zl/CP_Zl_v5_combined.root")
fZc = TFile("/home/fynu/rcastello/Physics/Zbb/Aug2012_full2011/upgrade_version/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/ControlPlots_V5/ControlPlots_Zc/CP_Zc_v5_combined.root")
fZb = TFile("/home/fynu/rcastello/Physics/Zbb/Aug2012_full2011/upgrade_version/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/ControlPlots_V5/ControlPlots_Zb/CP_Zb_v5_combined.root")

### data
h_data_MuA = fMuon_A.Get("MuMuChannel/stage_16/selection/bestzptMu")
print h_data_MuA
h_data_MuB = fMuon_B.Get("MuMuChannel/stage_16/selection/bestzptMu")
h_data_Mu = h_data_MuA.Clone()
h_data_Mu.Add(h_data_MuB)
h_data_ElA = fEle_A.Get("EEChannel/stage_16/selection/bestzptEle")
h_data_ElB = fEle_B.Get("EEChannel/stage_16/selection/bestzptEle")
h_data_El = h_data_ElA.Clone()
h_data_El.Add(h_data_ElB)

## h_data_Combined= h_data_Mu.Clone()
## #h_data_Combined.Sumw2()
## #h_data_Combined.Scale(lumi_Mu/lumi_El)
## h_data_Combined.Add(h_data_El)
## h_data_Combined.Rebin(20)

## ## MC
## h_TTbar_Mu      = fTTbar.Get("MuMuChannel/stage_16/selection/bestzptMu")
## h_ZZ_Mu         = fZZ.Get("MuMuChannel/stage_16/selection/bestzptMu")
## h_Zl_Mu         = fZl.Get("MuMuChannel/stage_16/selection/bestzptMu")
## h_Zc_Mu         = fZc.Get("MuMuChannel/stage_16/selection/bestzptMu")
## h_Zb_Mu         = fZb.Get("MuMuChannel/stage_16/selection/bestzptMu")
## h_DY_Mu = h_Zl_Mu.Clone()
## h_DY_Mu.Add(h_Zc_Mu)
## h_DY_Mu.Add(h_Zb_Mu)

## h_TTbar_El      = fTTbar.Get("EEChannel/stage_16/selection/bestzptEle")
## h_ZZ_El         = fZZ.Get("EEChannel/stage_16/selection/bestzptEle")
## h_Zl_El         = fZl.Get("EEChannel/stage_16/selection/bestzptEle")
## h_Zc_El         = fZc.Get("EEChannel/stage_16/selection/bestzptEle")
## h_Zb_El         = fZb.Get("EEChannel/stage_16/selection/bestzptEle")
## h_DY_El = h_Zl_El.Clone()
## h_DY_El.Add(h_Zc_El)
## h_DY_El.Add(h_Zb_El)

h_TTbar      = fTTbar.Get("Combined/stage_16/selection/bestzpt")
h_ZZ         = fZZ.Get("Combined/stage_16/selection/bestzpt")
h_Zl         = fZl.Get("Combined/stage_16/selection/bestzpt")
h_Zc         = fZc.Get("Combined/stage_16/selection/bestzpt")
h_Zb         = fZb.Get("Combined/stage_16/selection/bestzpt")
h_DY = h_Zl.Clone()
h_DY.Add(h_Zc)
h_DY.Add(h_Zb)

#Scale mC
## h_TTbar_Mu.Sumw2()
## h_TTbar_Mu.Scale(ttScale_Mu)
## h_ZZ_Mu.Sumw2()
## h_ZZ_Mu.Scale(zzScale_Mu)
## h_DY_Mu.Sumw2()
## h_DY_Mu.Scale(dyScale_Mu)

## h_TTbar_El.Sumw2()
## h_TTbar_El.Scale(ttScale_El)
## h_ZZ_El.Sumw2()
## h_ZZ_El.Scale(zzScale_El)
## h_DY_El.Sumw2()
## h_DY_El.Scale(dyScale_El)

h_TTbar.Sumw2()
h_TTbar.Scale(ttScale_Mu)
h_ZZ.Sumw2()
h_ZZ.Scale(zzScale_Mu)
h_Zc.Sumw2()
h_Zc.Scale(dyScale_Mu)
h_Zb.Sumw2()
h_Zb.Scale(dyScale_Mu)
h_Zl.Sumw2()
h_Zl.Scale(dyScale_Mu)


### background subtraction
print "=========== background subtraction  ============="
##### Mu Channel #########
## Ndata_Mu= 522
## Ntot_Mu= 480
## Ntt_Mu= 80
## Nzz_Mu= 12
## Nzbb_Mu= 350-35
## f_tt_Mu= 0.13
## Pbb_Mu= 0.75
## SF_zz_Mu=1
## print "SF_zz_Mu", SF_zz_Mu
## SF_tt_Mu=(Ndata_Mu*f_tt_Mu)/Ntt_Mu
## print "SF_tt_Mu", SF_tt_Mu
## SF_dy_Mu=Ndata_Mu*(1-Pbb_Mu)/(Ntot_Mu-Ntt_Mu-Nzz_Mu-Nzbb_Mu)
## print "SF_dy_Mu", SF_dy_Mu

## h_TTbar_Mu.Scale(SF_tt_Mu)
## h_ZZ_Mu.Scale(SF_zz_Mu)
## h_DY_Mu.Scale(SF_dy_Mu)
## hDataCorr_Mu = h_data_Mu.Clone()
## hDataCorr_Mu.Add(h_TTbar_Mu,-1)
## hDataCorr_Mu.Add(h_ZZ_Mu,-1)
## hDataCorr_Mu.Add(h_DY_Mu,-1)

## ##### El Channel #########
## Ndata_El= 362
## Ntot_El= 357
## Ntt_El= 62
## Nzz_El= 8
## Nzbb_El= 258-26
## f_tt_El= 0.14
## Pbb_El = 0.74
## SF_zz_El=1
## print "SF_zz_El", SF_zz_El
## SF_tt_El=(Ndata_El*f_tt_El)/Ntt_El
## print "SF_tt_El", SF_tt_El
## SF_dy_El=Ndata_El*(1-Pbb_El)/(Ntot_El-Ntt_El-Nzz_El-Nzbb_El)
## print "SF_dy_El", SF_dy_El

## h_TTbar_El.Scale(SF_tt_El)
## h_ZZ_El.Scale(SF_zz_El)
## h_Zc_El.Scale(SF_dy_El)
## h_Zl_El.Scale(SF_dy_El)
## hDataCorr_El = h_data_El.Clone()
## hDataCorr_El.Add(h_TTbar_El,-1)
## hDataCorr_El.Add(h_ZZ_El,-1)
## hDataCorr_El.Add(h_Zc_El,-1)
## hDataCorr_El.Add(h_Zl_El,-1)

## #### Combined data Background subtracted ####
## hDataCorr = hDataCorr_Mu.Clone() 
## hDataCorr.Sumw2()
## #hDataCorr.Scale(lumi_Mu/lumi_El)
## hDataCorr.Add(hDataCorr_El)
## hDataCorr.Rebin(20)

print "=========== getting data plot to unfold for setting the binning ============="
## print "data distribution :", hDataCorr.GetTitle()
## print "number of bin in data histo : ",hDataCorr .GetNbinsX() 
## print "minumum in data histo : ", hDataCorr.GetXaxis().GetXmin()
## print "maximum in data histo : ", hDataCorr.GetXaxis().GetXmax()

##f_data = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/combined_Plots_JES_final_V_SaveHisto_Combined.root")
##hdata = f_data.Get("h_data")
hdata=h_data_El.Clone()
hdata.Add(h_data_Mu)
hdata.Rebin(20)
print "data distribution :", hdata.GetTitle()
print "number of bin in data histo : ", hdata.GetNbinsX() 
print "minumum in data histo : ", hdata.GetXaxis().GetXmin()
print "maximum in data histo : ", hdata.GetXaxis().GetXmax()
Ndata = 884
Ntot = 837
Ntt = 142
Nzz = 20
Nzbb = 608-61
f_tt = 0.145
Pbb = 0.745
SF_zz = 1
print "SF_zz", SF_zz
SF_tt =(Ndata*f_tt)/Ntt
print "SF_tt", SF_tt
SF_dy =Ndata*(1-Pbb)/(Ntot-Ntt-Nzz-Nzbb)
print "SF_dy", SF_dy

bck=h_TTbar.Clone()
bck.Add(h_ZZ)
bck.Add(h_Zc)
bck.Add(h_Zl)
bck.Add(h_Zb)
bck.Rebin(20)

h_TTbar.Scale(SF_tt)
h_ZZ.Scale(SF_zz)
h_Zc.Scale(SF_dy)
h_Zl.Scale(SF_dy)
hbackground=h_TTbar.Clone()
hbackground.Add(h_ZZ)
hbackground.Add(h_Zc)
hbackground.Add(h_Zl)
hbackground.Rebin(20)
print "background bin" , hbackground.GetNbinsX()

hdataCombineCorr= hdata.Clone()
hdataCombineCorr.Add(hbackground,-1)


print "=========== getting response matrix ============="
#file = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Matrix_Unfolding_NoWeight/merged.root")
file = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/RooUnfold-1.1.1/Unfold_ptZ/Matrix_Unfolding/merged.root")
#response= RooUnfoldResponse(25,0,500);
response = file.Get("response_pT_Z")
print "response_1", response

hTrue = file.Get("true")
hMeas = file.Get("meas")
true = file.Get("truht")
### rebinning to merge the last bins
xbins = array.array('d',[0.0,20.0,40.0,60.0,80.0,100.0,120.0,140.0,160.0,180.0,200.0,220.0,240.0,260.0,280.0,300.0,320.0,340.0,500.0])
## hTrue.Rebin((len(xbins)-1),"hTrue",xbins)
## hMeas.Rebin((len(xbins)-1),"hMeas",xbins)
## hdataCombineCorr.Rebin((len(xbins)-1),"hdataCombineCorr",xbins)
## hdata.Rebin((len(xbins)-1),"hdata",xbins)
## ##response.Rebin((len(xbins)-1),"response",xbins)
## for i in range(0,hTrue.GetNbinsX() ):
##     print "Content bin ", i , ": ", response_1.GetBinContent(hTrue,i)
  
## hresponse = response_1.Hresponse()
## hresponse.RebinX((len(xbins)-1),"hresponse",xbins)
## hresponse.RebinY((len(xbins)-1),"hresponse",xbins)
## print "hresponse",hresponse
## response =  RooUnfoldResponse(response_1.Hmeasured(), response_1.Htruth(), hresponse)

print "response", response
response.ls()

print "hTrue", hTrue
print "hMeas", hMeas
print "response.Hmeasured()", response.Hmeasured()
print "response.Htruth()",response.Htruth()

output_file = TFile("outBayes20.root", 'RECREATE')
#output_file = TFile("outSVD7.root", 'RECREATE')
output_file.cd()
#response.Write()

print "================================ TEST TECHNICAL ==============================="
## hTrue= TH1D ("true", "Test Truth", 25 , 0., 500.)
## hMeas= TH1D ("meas", "Test Measured", 25 , 0., 500.)

print "=============================== TEST STATISTICAL =============================="
#hTrue_stat= TH1D ("true", "Test Truth", 25 , 0., 500.)
#hMeas_stat= TH1D ("meas", "Test Measured", 25 , 0., 500.)

print "=============================== TEST SYSTEMATICS =============================="
#input_file = TFile()

print "==================================== UNFOLD ==================================="
print "================================ SVD Unfold =============================="
print "=================== Unfold the test ============================="
unfold_test= RooUnfoldBayes (response, hMeas, 20)    #  OR
#unfold_test= RooUnfoldSvd     (response, hMeas, 7)   #  OR
#unfold_test= RooUnfoldTUnfold (response, hMeas)

print "================= Unfold the data ============================="
unfold = RooUnfoldBayes (response, hdataCombineCorr, 20)    #  OR
#unfold = RooUnfoldSvd     (response, hdataCombineCorr, 7)   #  OR
#unfold= RooUnfoldTUnfold (response, hdata)

hReco= unfold.Hreco()
hReco.Write()

canvas_subtraction= TCanvas("canvas_subtraction","canvas_subtraction", 500, 500)
canvas_subtraction.cd()
hdata.SetLineColor(kMagenta+2)
hdata.SetMarkerStyle(20)
hdata.SetMarkerColor(kMagenta+2)
hdata.Draw("P,E")
bck.SetLineColor(kGreen+2)
bck.Draw("HIST SAME")
hbackground.SetLineColor(kOrange)
hbackground.SetFillColor(kOrange)
hbackground.Draw("HIST SAME")
hdataCombineCorr.SetMarkerStyle(20)
hdataCombineCorr.Draw("P,E,SAME")
hdata.Draw("P,E,SAME")
canvas_subtraction.Write()

canvas_test= TCanvas("canvas_test","canvas_test", 500, 500)
canvas_test.cd()
hReco_test = unfold_test.Hreco()
#unfold_test.PrintTable (cout, hTrue)
hReco_test.SetLineColor(2)
hReco_test.Draw("HIST")
hTrue.SetLineColor(8)
hMeas.SetLineColor(4)
hMeas.Draw("HIST SAME")
hTrue.Draw("HIST SAME")
output_file.cd()
canvas_test.Write()

canvas_data= TCanvas("canvas_data","canvas_data", 500, 500)
canvas_data.cd()
#hdata.Draw()
hReco= unfold.Hreco()
unfold.PrintTable (cout, hTrue)
hReco.SetLineColor(2)
hReco.SetMarkerStyle(20)
hReco.SetMarkerColor(2)
hReco.Draw("P,E")
hTrue.Sumw2()
hTrue.Scale(dyScale_Mu)
hTrue.SetLineColor(8)
hTrue.Draw("HIST SAME")
hMeas.Sumw2()
hMeas.Scale(dyScale_Mu)
hMeas.SetLineColor(4)
hMeas.Draw("HIST SAME")
hReco.Draw("P,E,SAME")
hdataCombineCorr.Draw("P,E,SAME")
output_file.cd()
canvas_data.Write()

canvas_dataNorm= TCanvas("canvas_dataNorm","canvas_dataNorm", 500, 500)
canvas_dataNorm.cd()
hReco= unfold.Hreco()
#xbins = array.array('d',[20.0,40.0,60.0,80.0,100.0,120.0,140.0,160.0,180.0,200.0,500.0])
## xbins = array.array('d',[0.0,20.0,40.0,60.0,80.0,100.0,120.0,140.0,160.0,180.0,200.0,220.0,240.0,260.0,280.0,300.0,320.0,340.0,360.0,380.0,400.0,420.0,440.0,460.0,480.0,500.0])
## hReco.Rebin((len(xbins)-1),"hReco_binned",xbins)
## hReco_binned.SetBinContent((len(xbins)-9), 0.0)
## hReco_binned.SetBinContent((len(xbins)-8), 0.0)
## hReco_binned.SetBinContent((len(xbins)-7), 0.0)
## hReco_binned.SetBinContent((len(xbins)-6), 0.0)
## hReco_binned.SetBinContent((len(xbins)-5), 0.0)
## hReco_binned.SetBinContent((len(xbins)-4), 0.0)
hReco.SetLineColor(2)
hReco.Sumw2()
hdataCombineCorr.SetLineColor(1)
hdataCombineCorr.Sumw2()
hReco.DrawNormalized("HIST")
hdataCombineCorr.DrawNormalized("HIST SAME")
hReco.DrawNormalized("HIST SAME")
output_file.cd()
canvas_dataNorm.Write()

canvas_mcNorm= TCanvas("canvas_mcNorm","canvas_mcNorm", 500, 500)
canvas_mcNorm.cd()
hReco_test= unfold_test.Hreco()
hReco_test.SetLineColor(2)
hReco_test.Sumw2()
hReco_test.DrawNormalized("E")
hTrue.SetLineColor(8)
hTrue.DrawNormalized("HIST SAME")
hMeas.SetLineColor(4)
hMeas.DrawNormalized("HIST SAME")
output_file.cd()
canvas_mcNorm.Write()

## canvas_logdi= TCanvas("canvas_logdi","canvas_logdi", 500, 500)
## canvas_logdi.cd()
## canvas_logdi.SetLogy()
## h_dvector = unfold.Impl().GetD()
## h_dvector_test = unfold_test.Impl().GetD()
## print "h_dvector", h_dvector
## print "h_dvector_test", h_dvector_test
## h_dvector.SetLineColor(36)
## h_dvector.Draw("HIST")
## output_file.cd()
## canvas_logdi.Write()

#raw_input("Press ENTER to continue")
## print "tot number of events = ",k
## print "number that survived gen cuts",x
## print "number of events in matrix = ",j    
## print "number of events in missed = ",l  







## ###OLD OLD OLD VERSION
## canvas_subtraction= TCanvas("canvas_subtraction","canvas_subtraction", 500, 500)
## canvas_subtraction.cd()
## bck.SetLineColor(3)
## bck.Draw("HIST")
## hdataCombineCorr.SetLineColor(2)
## hdataCombineCorr.Draw("HIST SAME")
## hdata.Draw("E SAME")
## hbackground.SetLineColor(8)
## hbackground.Draw("HIST SAME")
## #hDataCorr.Draw("SAME")
## canvas_subtraction.Write()

## canvas_test= TCanvas("canvas_test","canvas_test", 500, 500)
## canvas_test.cd()
## hReco_test = unfold_test.Hreco()
## #unfold_test.PrintTable (cout, hTrue)
## hReco_test.SetLineColor(2)
## hReco_test.Draw()
## hTrue.SetLineColor(8)
## hMeas.SetLineColor(4)
## hMeas.Draw("SAME")
## hTrue.Draw("SAME")
## output_file.cd()
## canvas_test.Write()

## canvas_data= TCanvas("canvas_data","canvas_data", 500, 500)
## canvas_data.cd()
## #hdata.Draw()
## hReco= unfold.Hreco()
## unfold.PrintTable (cout, hTrue)
## hReco.SetLineColor(2)
## hReco.Draw()
## hdataCombineCorr.Draw("SAME")
## hTrue.Sumw2()
## hTrue.Scale(dyScale_Mu)
## hTrue.SetLineColor(8)
## hTrue.Draw("HIST SAME")
## hMeas.Sumw2()
## hMeas.Scale(dyScale_Mu)
## hMeas.SetLineColor(4)
## hMeas.Draw("HIST SAME")
## output_file.cd()
## canvas_data.Write()

## canvas_dataNorm= TCanvas("canvas_dataNorm","canvas_dataNorm", 500, 500)
## canvas_dataNorm.cd()
## hReco= unfold.Hreco()
## #xbins = array.array('d',[20.0,40.0,60.0,80.0,100.0,120.0,140.0,160.0,180.0,200.0,500.0])
## ## xbins = array.array('d',[0.0,20.0,40.0,60.0,80.0,100.0,120.0,140.0,160.0,180.0,200.0,220.0,240.0,260.0,280.0,300.0,320.0,340.0,360.0,380.0,400.0,420.0,440.0,460.0,480.0,500.0])
## ## hReco.Rebin((len(xbins)-1),"hReco_binned",xbins)
## ## hReco_binned.SetBinContent((len(xbins)-9), 0.0)
## ## hReco_binned.SetBinContent((len(xbins)-8), 0.0)
## ## hReco_binned.SetBinContent((len(xbins)-7), 0.0)
## ## hReco_binned.SetBinContent((len(xbins)-6), 0.0)
## ## hReco_binned.SetBinContent((len(xbins)-5), 0.0)
## ## hReco_binned.SetBinContent((len(xbins)-4), 0.0)
## hReco.SetLineColor(2)
## hReco.Sumw2()
## hdataCombineCorr.SetLineColor(1)
## hdataCombineCorr.Sumw2()
## hReco.DrawNormalized("HIST")
## hdataCombineCorr.DrawNormalized("HIST SAME")
## hReco.DrawNormalized("HIST SAME")
## output_file.cd()
## canvas_dataNorm.Write()

## canvas_mcNorm= TCanvas("canvas_mcNorm","canvas_mcNorm", 500, 500)
## canvas_mcNorm.cd()
## hReco_test= unfold_test.Hreco()
## hReco_test.SetLineColor(2)
## hReco_test.Sumw2()
## hReco_test.DrawNormalized("P")
## hTrue.SetLineColor(8)
## hTrue.DrawNormalized("HIST SAME")
## hMeas.SetLineColor(4)
## hMeas.DrawNormalized("HIST SAME")
## output_file.cd()
## canvas_mcNorm.Write()

## ## canvas_logdi= TCanvas("canvas_logdi","canvas_logdi", 500, 500)
## ## canvas_logdi.cd()
## ## canvas_logdi.SetLogy()
## ## h_dvector = unfold.Impl().GetD()
## ## h_dvector_test = unfold_test.Impl().GetD()
## ## print "h_dvector", h_dvector
## ## print "h_dvector_test", h_dvector_test
## ## h_dvector.Draw("HIST")
## ## output_file.cd()
## ## canvas_logdi.Write()

## raw_input("Press ENTER to continue")
## ## print "tot number of events = ",k
## ## print "number that survived gen cuts",x
## ## print "number of events in matrix = ",j    
## ## print "number of events in missed = ",l  

