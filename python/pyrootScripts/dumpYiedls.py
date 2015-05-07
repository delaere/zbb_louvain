## plot to compute yields from control plots ##

from ROOT import *
import math

### Get the rootfile ###
f = TFile("Zbb_Rew_ZbblowMET_smallMll_RewFormformulaPol3_PAS_NotNorm_testRew.root")

yields = {}
### run over the channels ###
for Dir in ["Muon","Electron","Combined"]:
    print Dir
    ### get one canvas ###
    c = f.Get(Dir+"/jetmetMET")
    l = c.GetListOfPrimitives()
    yields[Dir] = {}
    mc = None
    for obj in l:
        if not obj.GetName()==c.GetName() : continue
        ### get data and MC stack to obtain the number of events and the stat. unc. ###
        if obj.InheritsFrom("TH1") : yields[Dir]["DATA"] = [obj.Integral(0,obj.GetNbinsX()+1),math.sqrt(obj.Integral(0,obj.GetNbinsX()+1))]
        elif mc is None and obj.InheritsFrom("THStack"):
            H = obj.GetHists()
            mc = True
            yields[Dir]["MC"] = [0,0]
            for h in H : 
                err = h.GetSumw2()
                e = 0
                for i in range(0,err.GetSize()) : e+=err[i]
                yields[Dir][h.GetTitle()] = [h.Integral(0,h.GetNbinsX()+1),math.sqrt(e)]
                yields[Dir]["MC"][0] += yields[Dir][h.GetTitle()][0]
                yields[Dir]["MC"][1] += yields[Dir][h.GetTitle()][1]*yields[Dir][h.GetTitle()][1]
    yields[Dir]["MC"][1] = math.sqrt(yields[Dir]["MC"][1])

### Order in which to print the yields ###
ls = ["Zh", "WW", "WZ", "ZZ", "tW", "#bar{t}W", "t#bar{t} lept", "t#bar{t} dilep", "Z+xx", "Z+bx", "Z+bb", "MC", "DATA"]

### print the yields ###
for d in yields:
    print d
    for s in ls : print s,
    print ""
    for s in ls: 
        if yields[d][s][0]>1 : print str("%.0f" % yields[d][s][0])+"+-"+str("%.0f" % yields[d][s][1]),
        else : print str("%.2f" % yields[d][s][0])+"+-"+str("%.2f" % yields[d][s][1]),
    print ""
    print ""
    print ""
