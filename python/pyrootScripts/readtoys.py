from ROOT import *
from llbbOptions import *

f = TFile("toydata.root")

job = "1"
#h = f.Get("H"+job)
h = f.Get("h2D")
print h.Integral()

opt = options_()

for mA in opt.rangeMassA:
    for mH in opt.rangeMassH:
        toydata = 0
        for x in range(1,h.GetNbinsX()+1):
            xlow = h.GetXaxis().GetBinLowEdge(x)
            xup = h.GetXaxis().GetBinUpEdge(x)
            for y in range(1,h.GetNbinsY()+1):
                ylow = h.GetYaxis().GetBinLowEdge(y)
                yup = h.GetYaxis().GetBinUpEdge(y)
                if xlow>=mA[0] and ylow>=mH[0] and xup<=mA[1] and yup<=mH[1]:
                    toydata += h.GetBinContent(x,y)
        if mH[2]>mA[2]+91 :
            card = open("/nfs/user/acaudron/unblindedDatacards2HDM/El/"+str(mA[2])+"_"+str(mH[2])+".txt")
            tot=0
            for l in card:
                if "rate" in l:
                    mc = l.split()
                    mc.remove("rate")
                    #mc.remove("0.5500")
                    #mc.remove("0.4500")
                    #mc.remove("0.550000000")
                    mc.remove("0.450000000")
                    for imc in mc : tot += float(imc)
                    break
            if tot-toydata>0.01 : print mA[2], mH[2], toydata, "%.3f" % toydata, tot, tot-toydata, tot/max(toydata,0.00001)
