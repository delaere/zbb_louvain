from ROOT import *
import array



mllbb=10
numDirs=36

massResol=0.15
bin_width = 1.5
step_fraction = 2.0/3.0

expectList = [-1,
              0.975,
              0.84,
              0.5,
              0.16,
              0.025]

mABin = { 10:1,
  11:2,
  13:3,
  15:4,
  17:5,
  20:6,
  23:7,
  26:8,
  30:9,
  35:10,
  40:11,
  46:12,
  53:13,
  61:14,
  70:15,
  81:16,
  93:17,
  107:18,
  123:19,
  142:20,
  163:21,
  188:22,
  216:23,
  248:24,
  286:25,
  329:26,
  378:27,
  435:28,
  500:29,
  575:30,
  662:31,
  761:32,
  875:33,
  1006:34,
  1158:35,
  1331:36,
}


for i in range(1,numDirs):
  dmllbb=massResol*mllbb*bin_width
  step_mllbb = dmllbb*step_fraction
  
  MH_dir = "MH_"+str(int(mllbb))+"_Asymptotic_"
  file = MH_dir+"/higgsCombineTest.Asymptotic.root"

  f=TFile(file)

  tree = f.Get("limit")

  try:
    entries = tree.GetEntriesFast()
  
    print "number of entries = ", entries
  
    myTH1_cls = {}
    expectedList = {}
    g_cls={}
  
  
    mAHypoList = []
  
    mbb=10.0
  
  
  
    for jentry in range(1,37) :
      dmbb=massResol*mbb*bin_width
      step_mbb = dmbb*step_fraction
      mAHypoList.append(int(mbb))
      mbb+=step_mbb
  
    mbb = 10.0
  
    #print mAHypoList
  
    mAarray=array.array('f',mAHypoList)
  
    print mAarray
  
    for expects in expectList:
    #    myTH1_cls[str(expects)] = TH1F("TH1_"+str(expects),"TH1_"+str(expects),len(mhHypoList),
    #                                   min(mhHypoList)-2.5,
    #                                   max(mhHypoList)+2.5)
  
       myTH1_cls[str(expects)] = TH1F("TH1_"+str(expects),"TH1_"+str(expects),len(mAHypoList)-1, mAarray)
  
       print expects
   
    for jentry in xrange(entries) :
   
      # get the next tree in the chain and verify
      ientry = tree.LoadTree( jentry )
      if ientry < 0: bla
      
      # copy next entry into memory and verify
      nb = tree.GetEntry( jentry )
      if nb <= 0: continue
  
      #print "going to loop over jets"
      for expects in expectList:
          if 0.99*abs(expects) < abs(tree.quantileExpected) < 1.01*abs(expects) :
              print "BIN = ", mABin[tree.mh]
              
              myTH1_cls[str(expects)].SetBinContent(mABin[tree.mh], tree.limit)
              print "limit saved, limit = ", tree.limit
              print "            expect = ", tree.quantileExpected
              print "                mh = ", tree.mh
  
    for expects in expectList:
      g_cls[expects] = TGraph(myTH1_cls[str(expects)])
      
      #g_cls[expects].GetYaxis().SetTitle("#sigma(Z[ll]+H[bb])_{95%CL}/#sigma(Z[ll]+H[bb])_{SM}, l=e,#mu")
      #g_cls[expects].GetXaxis().SetTitle("m_{H} (GeV/c^{2})")
      g_cls[expects].GetYaxis().SetTitle("95% C.L. on #Events")
      g_cls[expects].GetXaxis().SetTitle("M_{bb} (GeV)")
      g_cls[expects].SetMaximum(500.)
      g_cls[expects].SetMinimum(0.00001)


      g_cls[expects].GetXaxis().SetRange(min(mAHypoList),max(mAHypoList))
      
    C = TCanvas("C","C",1200,500)
    C.SetLeftMargin(0.2)
    C.SetBottomMargin(0.2)
    C.SetTitle(" ")


    max_limit =  myTH1_cls["0.975"].GetMaximum()

    line = TF1("line","1. ",10,mllbb)
    line.SetTitle(" ")
    line.GetYaxis().SetRangeUser(0,2*max_limit) 
    line.GetYaxis().SetTitleSize(0.07)
    line.GetYaxis().SetTitleOffset(0.8)
    line.GetYaxis().SetTitle("95% C.L. on #Events")
    line.GetYaxis().SetLabelSize(0.07)
    line.GetXaxis().SetTitleSize(0.07)
    line.GetXaxis().SetTitleOffset(1.2)
    line.GetXaxis().SetTitle("M_{bb} (GeV)")
    line.GetXaxis().SetLabelSize(0.07)
     
    line.Draw("")
  


    for expects in expectList: 
      if expects != -1 : 
        myTH1_cls[str(expects)].SetStats(0)
        myTH1_cls[str(expects)].Draw("C,same")
  
    #g_cls[-1].Draw("AC,same")
  
  
    myTH1_cls["0.975"].SetFillColor(kYellow)
    myTH1_cls["0.84"].SetFillColor(kGreen)
    myTH1_cls["0.16"].SetFillColor(kYellow)
    myTH1_cls["0.025"].SetFillColor(1001)
   
    try: 
      g_cls[0.5].Draw("*")

    except:
      print "problem in plotting g_cls[0.5]"
    #myTH1_cls["-1"].SetLineWidth(3)
    #myTH1_cls["-1"].Draw("C*,same")
  
    #g_cls[0.5].Draw("C,same")
  
    C.SetGridx()
    C.SetGridy()

    line.Draw("same")


    gPad.RedrawAxis()
    gPad.RedrawAxis("g")


    leg = TLegend(0.6,0.70,0.89,0.89)
    leg.SetFillStyle(0)
    leg.SetLineColor(0)
    header = "M_{Zbb} = ["+str(int(mllbb-dmllbb))+","+str(int(mllbb+dmllbb))+"]"
    leg.SetHeader(header);
    leg.Draw();

  
    path_plot = "/home/fynu/amertens/scratch/CMSSW/CMSSW_6_1_1/src/HiggsAnalysis/CombinedLimit/python/BrazilianBandPlots/BrazilianBandPlot_"+str(mllbb)+".png"
    C.Print(path_plot, "png")

  except:
    print 'no background events'

  mllbb+=step_mllbb
##################
### THE END :( ###
##################
                                                                  
