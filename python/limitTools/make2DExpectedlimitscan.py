###############
### imports ###
###############

import math
import os
from ROOT import *

###################
### Definitions ###
###################

numDirs=36
numFiles=36

massResol=0.15
bin_width = 1.5
step_fraction = 2.0/3.0

run_combine = 0
plot_c1 = 1
plot_c2 = 1
plot_c3 = 1
plot_c4 = 1
plot_c5 = 1

DataCards_path = "/home/fynu/amertens/storage/THDM/DataCards/Mu/"
#DataCards_path = "/home/fynu/amertens/scratch/CMSSW/CMSSW_6_1_1/src/2HDM/"

myTGraph = TGraph2D(100)
myTGraph.SetName("Limit")
h0 = TH2D("h1","Expected Exclusion (Events / (GeV^{2}))",500,0,1200,500,0,1200)
myTGraph.SetHistogram(h0)



myTGraph_sigma = TGraph2D(100)
myTGraph_sigma.SetName("Efficiency + Acceptance")
h1 = TH2D("h1","Efficiency x Acceptance",500,0,1200,500,0,1200)
myTGraph_sigma.SetHistogram(h1)


myTGraph_limit = TGraph2D(10)
myTGraph_limit.SetName("limit_on_sigma")
#myTGraph_limit.SetNpx(500)
#myTGraph_limit.SetNpy(500)

h2 = TH2D("h2","Expected Exclusion on #sigma (fb)",500,0,1200,500,0,1200)
myTGraph_limit.SetHistogram(h2)
#myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)
#myTGraph_limit.GetHistogram().GetXaxis().SetLimits(0,1000)

myTGraph2 = TGraph2D(100)
myTGraph2.SetName("Expected Exclusion (Events)")
h3 = TH2D("h3","Expected Exclusion (Events)",500,0,1200,500,0,1200)
myTGraph2.SetHistogram(h3)


mllbb=10
n=-1
m=-1
for i in range(1,numDirs):
  dmllbb=massResol*mllbb*bin_width
  step_mllbb = dmllbb*step_fraction

  MH_dir = "MH_"+str(int(mllbb))+"_Asymptotic_NOSYST_Blind_"
  #MH_dir = "MH_"+str(int(mllbb))+"_Asymptotic_Blind_"
  if run_combine == 1:
    mkdir_cmd = "mkdir "+MH_dir
    print mkdir_cmd
    rmdir_cmd = "rm -rf "+MH_dir
    os.system(rmdir_cmd)
    os.system(str(mkdir_cmd))
  mbb=10.0
  for j in range(1,numFiles):
    dmbb=massResol*mbb*bin_width
    step_mbb = dmbb*step_fraction
    if (mbb < mllbb) and (mllbb > 100) :
      #yield_path = "/home/fynu/amertens/scratch/CMSSW/CMSSW_6_1_1/src/2HDM/mH"+str(int(mllbb-dmllbb))+"to"+str(int(mllbb+dmllbb))+"/Combined/testmA"+str(int(mbb-dmbb))+"to"+str(int(mbb+dmbb))+".txt"
      yield_path = DataCards_path+str(int(mbb))+"_"+str(int(mllbb))+".txt"
      #combine_cmd = "combine -M Asymptotic -m "+str(int(mbb))+" -S 0 "+yield_path
      combine_cmd = "combine -M Asymptotic -m "+str(int(mbb))+" -S 0 --run=blind "+yield_path
      #combine_cmd = "combine -M ProfileLikelihood --significance --pvalue -m "+str(int(mbb))+" "+yield_path+" -t -1 --expectSignal=1"

      print combine_cmd
      try:
        file_path = MH_dir+"/higgsCombineTest.Asymptotic.mA"+str(int(mbb))+".root"
        if run_combine == 1:
          os.system(str(combine_cmd))
          cp_cmd = "cp higgsCombineTest.Asymptotic.mH"+str(int(mbb))+".root "+file_path
          os.system(str(cp_cmd))

        fList = TFile(str(file_path)) 
        mytree  = fList.Get("limit")
        #for entry in mytree:
        mytree.GetEntry(2);
      
#        j+=1
#      if (mbb < mllbb) and (mllbb > 100) :


	if mytree.limit > 0:

  	  print "Expected Limit(",(i-1)*numDirs+(j-1) , ", " , int(mbb) , ", " , int(mllbb),") = ", mytree.limit
	  limit=mytree.limit
          limitGev2=mytree.limit/(2*dmbb*2*dmllbb)
	  n+=1
          myTGraph.SetPoint(n, mbb, mllbb, limitGev2)
	  myTGraph2.SetPoint(n, mbb, mllbb, limit)
	  try :
            DelphesFile_path = "/home/fynu/amertens/storage/THDM/histos/H_ZA_eff_"+str(int(mllbb))+"_"+str(int(mbb))+".root"
	    if os.path.isfile(str(DelphesFile_path)) :
	      DelphesFile = TFile(str(DelphesFile_path))
              myG2D = DelphesFile.Get("Graph2D")
              effZ = myG2D.GetZ()
              eff = effZ[35*(i-1)+j-1]

	      print "efficiency(",int(mbb), ", ", int(mllbb), ") =", eff

              if eff > 0 : 
  	        m+=1
	        myTGraph_sigma.SetPoint(m, mbb, mllbb, eff)
	        #myTGraph_limit.SetPoint(m, mbb, mllbb, log10(limit/(20*eff)))
	        myTGraph_limit.SetPoint(m, mbb, mllbb, limit/(20*eff))
        
	    #else :
	      #m+=1
	      #myTGraph_sigma.SetPoint(n, mbb, mllbb, 0)
	      #myTGraph_limit.SetPoint(m, mbb, mllbb, 0)

	  #else :
	    #m+=1
	    #myTGraph_sigma.SetPoint(n, mbb, mllbb, 0)
	    #myTGraph_limit.SetPoint(m, mbb, mllbb, 0)

	  except:
	    print DelphesFile_path, " not existing . "
	  #m+=1
	  #myTGraph_sigma.SetPoint(n, mbb, mllbb, 0)
	  #myTGraph_limit.SetPoint(m, mbb, mllbb, 0)

      #myTGraph.SetPoint(n, mbb, mllbb, mytree.limit)
      #else : 
	#myTGraph.SetPoint(n, mbb, mllbb, 0)
	#myTGraph2.SetPoint(n, mbb, mllbb, 0)
	#m+=1
	#myTGraph_sigma.SetPoint(n, mbb, mllbb, 0)
	#myTGraph_limit.SetPoint(m, mbb, mllbb, 0)
      except:
        print 'no background events'
      #myTGraph.SetPoint(n, mbb, mllbb, 0)
      #myTGraph2.SetPoint(n, mbb, mllbb, 0)
      #m+=1
      #myTGraph_sigma.SetPoint(n, mbb, mllbb, 0)
      #myTGraph_limit.SetPoint(m, mbb, mllbb, 0)


    mbb+=step_mbb

    print '##############################################'
    print 'mbb:', mbb, 'myTGraph size', myTGraph.GetN()
    print '##############################################'

  mllbb+=step_mllbb

'''
  hadd_cmd = "hadd "+MH_dir+"/higgsCombineTest.ProfileLikelihood.root "+MH_dir+"/higgsCombineTest.ProfileLikelihood.mA*.root"
  os.system(str(hadd_cmd))
  fList = TFile(MH_dir+"/higgsCombineTest.ProfileLikelihood.root")
  mytree  = fList.Get("limit")
  j=0
  for entry in mytree:
    print "p-value(",(i-1)*5+(j-1) , ", " , mbb , ", " , mllbb,") = ", entry.limit
    j+=1
    myTGraph.SetPoint((i-1)*5+(j-1), mbb, mllbb,entry.limit)
'''

#C=TCanvas("C","C",2000,1000)
#C.Divide(2)
#C.cd(1)
#myTGraph.Draw("CONT")
#C.cd(2)
#myTGraph.Draw("surf1")
#C.Print("Exp_Limit_allBkg.png","png")
#C.Print("Exp_Limit_allBkg.C","cxx")

#myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)

print 'M value :', m

xtitlesize=0.05
ytitlesize=0.05
ztitlesize=0.05

xtitleoffset=1.1
ytitleoffset=1.3
ztitleoffset=1.1

rightmargin=0.2
leftmargin=0.15
bottommargin=0.15

if plot_c1:
  
  C=TCanvas("C","C",1000,900)
  ROOT.gStyle.SetPalette(1)
  ROOT.gStyle.SetOptStat(0)
  
  gPad.SetLogz()
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  myTGraph_limit.GetHistogram().Draw("colz")
  #gPad.Update()
  
  #myTGraph_limit.GetHistogram().GetXaxis().SetLimits(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)
  
  #myTGraph_limit.GetHistogram().SetMargin(0.0)
  myTGraph_limit.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_limit.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_limit.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_limit.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_limit.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_limit.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_limit.GetHistogram().SetMinimum(10)
  #myTGraph_limit.GetHistogram().GetXaxis().SetRangeUser(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetRangeUser(0,1000)
  #myTGraph_limit.GetHistogram().SetTitle("Expected Exclusion on #sigma")
  
  gPad.Modified()
  gPad.Update()

  
'''
# code for PCOL Option
C.cd(2)
gPad.SetRightMargin(0.2)
gPad.SetLeftMargin(0.2)
gPad.SetBottomMargin(0.2)
myTGraph_limit.Draw("pcol")
myTGraph_limit.GetXaxis().SetTitle("M_{bb}")
myTGraph_limit.GetXaxis().SetTitleSize(0.07)
myTGraph_limit.GetXaxis().SetTitleOffset(1.1)
myTGraph_limit.GetYaxis().SetTitle("M_{Zbb}")
myTGraph_limit.GetYaxis().SetTitleSize(0.07)
myTGraph_limit.GetYaxis().SetTitleOffset(1.1)
myTGraph_limit.SetMarkerStyle(20)
myTGraph_limit.SetMarkerSize(1)
myTGraph_limit.SetTitle("Expected Exclusion on #sigma")
gPad.Modified()
gPad.Update()
gPad.GetView().TopView()
#myTGraph_limit.GetZaxis().SetRangeUser(1,10000.0)

C.Print("Exp_Lim_Xsec_colz.png","png")

C2=TCanvas("C2","C2",750,1000)
ROOT.gStyle.SetPalette(55)
'''
#C2.SetRightMargin(0.2)
#C2.SetLeftMargin(0.2)
#C2.Divide(2)

if plot_c2 : 
  C2=TCanvas("C2","C2",1000,900)
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  myTGraph.GetHistogram().Draw("colz")
  gPad.Update()
  #myTGraph.SetTitle("Expected Exclusion (Events / GeV^{2})")
  myTGraph.GetHistogram().GetXaxis().SetTitle("M_{bb} (GeV)")
  myTGraph.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph.GetHistogram().GetYaxis().SetTitle("M_{Zbb} (GeV)")
  myTGraph.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph.GetHistogram().GetZaxis().SetTitle("Expected Exclusion (Events / GeV^{2})")
  myTGraph.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  #myTGraph.SetMarkerStyle(20)
  #myTGraph.Draw("colz")
  #gPad.Update()
  gPad.Update()
  C2.Print("Exp_Eff_BW_allBkg_colz_final.png","png")
  

if plot_c3:  
  C3=TCanvas("C3","C3",1000,900)
  ROOT.gStyle.SetPalette(1)
  #set_palette("color", 999)
  ROOT.gStyle.SetOptStat(0)
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  myTGraph2.GetHistogram().Draw("colz")
  gPad.Update()
  #myTGraph2.GetHistogram().SetTitle("Expected Exclusion (Events / GeV^{2})")
  myTGraph2.GetHistogram().GetXaxis().SetTitle("M_{bb} (GeV)")
  myTGraph2.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph2.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph2.GetHistogram().GetYaxis().SetTitle("M_{Zbb} (GeV)")
  myTGraph2.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph2.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  #myTGraph2.GetHistogram().GetZaxis().SetTitle("Expected Exclusion (Events / GeV^{2})")
  myTGraph2.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph2.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  gPad.Modified()
  gPad.Update()
  
#C2.SetLogz()


if plot_c4:
 
  C4=TCanvas("C4","C4",1000,900)
 
  C4.Update()
  C4.Modified()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  #gPad.SetTopMargin()
  gPad.SetLogz()
  myTGraph_sigma.GetHistogram().Draw("colz")
  myTGraph_sigma.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_sigma.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_sigma.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_sigma.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_sigma.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_sigma.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_sigma.GetHistogram().GetZaxis().SetTitle("#epsilon #times Acc.")
  myTGraph_sigma.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph_sigma.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  #myTGraph_sigma.SetMarkerStyle(20)
 
  #C2.Modified()
  gPad.Modified()
  gPad.Update()
  C4.Print("Limit_Efficiency.png","png")



if plot_c5:
  
  C5=TCanvas("C5","C5",1000,900)
  
  C5.Update()
  C5.Modified()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  #gPad.SetTopMargin()
  gPad.SetLogz()
  CMSSWPoints = TGraph(12)
  CMSSWPoints.SetPoint(0,35,142)
  CMSSWPoints.SetPoint(1,30,329)
  CMSSWPoints.SetPoint(2,142,575)
  CMSSWPoints.SetPoint(3,70,575)
  CMSSWPoints.SetPoint(4,378,875)
  CMSSWPoints.SetPoint(5,70,875)
  CMSSWPoints.SetPoint(6,142,329)
  CMSSWPoints.SetPoint(7,70,329)
  CMSSWPoints.SetPoint(8,378,575)
  CMSSWPoints.SetPoint(9,142,875)
  CMSSWPoints.SetPoint(10,575,875)
  CMSSWPoints.SetPoint(11,761,875)
  
  CMSSWPoints.SetMarkerStyle(21)
  CMSSWPoints.GetXaxis().SetLimits(0,1200)
  CMSSWPoints.SetMinimum(0)
  CMSSWPoints.SetMaximum(1200)
  '''
  CMSSWPoints.GetXaxis().SetTitle("M_{A}")
  CMSSWPoints.GetYaxis().SetTitle("M_{H}")
  #CMSSWPoints.GetXaxis().SetTitleOffSet(1.1)
  CMSSWPoints.GetYaxis().SetTitleOffset(1.5)
  CMSSWPoints.GetXaxis().SetTitleSize(0.06)
  CMSSWPoints.GetYaxis().SetTitleSize(0.06)
  CMSSWPoints.GetXaxis().SetLabelSize(0.05)
  CMSSWPoints.GetYaxis().SetLabelSize(0.05)
  CMSSWPoints.GetXaxis().SetNdivisions(5)
  CMSSWPoints.GetYaxis().SetNdivisions(5)
  '''
  myTGraph_sigma.GetHistogram().Draw("colz")
  CMSSWPoints.Draw("P")
  LineBoostedRegion = TLine(0,0,120,1200)
  #LineKin = TLine(0,90,1110,1200)
  #LineOneOne = TLine(0,0,1000,1000)
  #LineBoostedRegion.SetLineColor(kRed)
  LineBoostedRegion.SetLineWidth(3)
  LineBoostedRegion.SetLineStyle(2)
  LineBoostedRegion.Draw()
  #LineKin.SetLineWidth(3)
  #LineKin.Draw()
  #LineOneOne.SetLineWidth(3)
  #LineOneOne.Draw()
  t1 = TPaveText(0.5,0.35,0.7,0.50,"brNDC")
  t1.AddText("M_{A}+M_{Z}>M_{H}")
  t1.SetFillColor(0)
  t1.Draw("same")
  
  
  #myTGraph_sigma.GetHistogram().SetTitle("Acceptance + Selection Efficiency")
  
  myTGraph_sigma.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_sigma.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_sigma.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_sigma.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_sigma.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_sigma.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_sigma.GetHistogram().GetZaxis().SetTitle("#epsilon #times Acc.")
  myTGraph_sigma.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph_sigma.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  #myTGraph_sigma.SetMarkerStyle(20)
  
  #C2.Modified()
  gPad.Modified()
  gPad.Update()
  C5.Print("Limit_Efficiency.png","png")
  


f = TFile("limits.root","recreate")
myTGraph.Write()
myTGraph_sigma.Write()
f.Close()



'''
C2=TCanvas("C2","C2",2000,1000)
C2.Divide(2)
ROOT.gStyle.SetPalette(52)
C2.cd(1)
myTGraph.GetXaxis().SetTitle("m_{bb}")
myTGraph.GetYaxis().SetTitle("m_{llbb}")
myTGraph.Draw("colz")
myTGraph.GetZaxis().SetRangeUser(0,10)
C2.cd(2).SetLogz()
myTGraph.Draw("colz")
C2.Print("Exp_Lim_BW_allBkg.png","png")
C2.Print("Exp_Lim_BW_allBkg.C","cxx")
'''


print "==> Now you have your 2D p-value scans of MH vs MA :-)"

###########
### FIN ###
###########
