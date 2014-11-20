from ROOT import *
import array


expectList = [-1,
              0.975,
              0.84,
              0.5,
              0.16,
              0.025]

LambdaBin = { -1:1,
  0:2,
  1:3,
  2:4,
  10:5,
}



file = "/home/fynu/mvidal/scratch/Limits_HH/CMSSW_6_1_1/src/HiggsAnalysis/CombinedLimit/data/hh-bbww/NO-systematics/higgsCombineHHbbWW.Asymptotic.NoSys.root"

f=TFile(file)

tree = f.Get("limit")


entries = tree.GetEntriesFast()

print "number of entries = ", entries

myTG_cls = {}
expectedList = {}
g_cls={}

LambdaHypoList = [-1,0,1,2,10]

LambdaArray=array.array('f',LambdaHypoList)

for expects in expectList:
    #    myTH1_cls[str(expects)] = TH1F("TH1_"+str(expects),"TH1_"+str(expects),len(mhHypoList),
    #                                   min(mhHypoList)-2.5,
    #                                   max(mhHypoList)+2.5)
    
    myTG_cls[str(expects)] = TGraph(len(LambdaHypoList))
    
    print expects

point = 0    
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
            print "BIN = ", LambdaBin[tree.mh]
            
            myTG_cls[str(expects)].SetPoint(point,tree.mh, tree.limit)
            print "limit saved, limit = ", tree.limit
            print "            expect = ", tree.quantileExpected
            print "                mh = ", tree.mh
	    point +=1
 

    #g_cls[expects].GetXaxis().SetRange(min(mAHypoList),max(mAHypoList))
    
C = TCanvas("C","C",1200,500)
C.SetLeftMargin(0.2)
C.SetBottomMargin(0.2)
C.SetTitle(" ")


#    max_limit =  myTH1_cls["0.975"].GetMaximum()
#
#    line = TF1("line","1. ",10,mllbb)
#    line.SetTitle(" ")
#    line.GetYaxis().SetRangeUser(0,2*max_limit) 
#    line.GetYaxis().SetTitleSize(0.07)
#    line.GetYaxis().SetTitleOffset(0.8)
#    line.GetYaxis().SetTitle("95% C.L. on #Events")
#    line.GetYaxis().SetLabelSize(0.07)
#    line.GetXaxis().SetTitleSize(0.07)
#    line.GetXaxis().SetTitleOffset(1.2)
#    line.GetXaxis().SetTitle("M_{bb} (GeV)")
#    line.GetXaxis().SetLabelSize(0.07)
#     
#    line.Draw("")
  



max_limit =  myTG_cls["0.975"].GetMaximum()
myTG_cls["0.975"].SetTitle(" ")
myTG_cls["0.975"].GetYaxis().SetRangeUser(0,2*max_limit) 
myTG_cls["0.975"].GetYaxis().SetTitleSize(0.07)
myTG_cls["0.975"].GetYaxis().SetTitleOffset(0.8)
myTG_cls["0.975"].GetYaxis().SetTitle("95% C.L. on #Events")
myTG_cls["0.975"].GetYaxis().SetLabelSize(0.07)
myTG_cls["0.975"].GetXaxis().SetTitleSize(0.07)
myTG_cls["0.975"].GetXaxis().SetTitleOffset(1.2)
myTG_cls["0.975"].GetXaxis().SetTitle("\Lambda")
myTG_cls["0.975"].GetXaxis().SetLabelSize(0.07)
myTG_cls["0.975"].GetXaxis().SetRangeUser(-1.1,10.1)



for expects in expectList: 
    if expects == 0.975: 
        myTG_cls[str(expects)].Draw("")
    if (expects != -1.0 and expects != 0.975):
        myTG_cls[str(expects)].Draw("C,same")
#g_cls[-1].Draw("AC,same")
  

max_limit =  myTG_cls["0.975"].GetMaximum()

  
myTG_cls["0.975"].SetFillColor(kYellow)
myTG_cls["0.84"].SetFillColor(kGreen)
myTG_cls["0.16"].SetFillColor(kYellow)
myTG_cls["0.025"].SetFillColor(1001)

try: 
    myTG_cls["0.5"].Draw("*")
    
except:
    print "problem in plotting g_cls[0.5]"
    #myTH1_cls["-1"].SetLineWidth(3)
    #myTH1_cls["-1"].Draw("C*,same")
  
    #g_cls[0.5].Draw("C,same")
  
C.SetGridx()
C.SetGridy()

#line.Draw("same")

gPad.RedrawAxis()
gPad.RedrawAxis("g")

leg = TLegend(0.6,0.70,0.89,0.89)
leg.SetFillStyle(0)
leg.SetLineColor(0)
header = "#Lambda expected exclusion"
leg.SetHeader(header);
leg.Draw();

#path_plot = "/home/fynu/mvidal/scratch/Limits_HH/CMSSW_6_1_1/src/HiggsAnalysis/CombinedLimit/plots/"
name_plot = "Limit_brasilian.png"
C.Print(name_plot, "png")


##################
### THE END :( ###
##################
                                                                  
