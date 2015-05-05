from llbbOptions import *
from ROOT import *
gROOT.SetBatch()
formulaName = "formulaPol3_C.so"
gSystem.Load(formulaName)

class options_(options_):
        #list of samples
        samples = [
            "DATA",
            "DYjets",
            "TTFullLept",
            "TTSemiLept",
            "ZZ",
            "WZ",
            "WW",
            "Wt",
            "Wtbar",
            "ZH125",
            ]

        SYST = "Nominal"

        path = options_.path.replace("SYST",SYST)

        stages = options_.stagesFit
        categories = {
            "El2j" : stages["El"]+"&&jetmetnj==2",
            "El3j" : stages["El"]+"&&jetmetnj>2",
            "Mu2j" : stages["Mu"]+"&&jetmetnj==2",
            "Mu3j" : stages["Mu"]+"&&jetmetnj>2"
            }
        
lowX = 0.679*0.679
highX = 1.0
            
def main():
    options = options_()
    files = {}
    MC = TH2D("MC", "MC", 4*len(options.categories), lowX, lowX+(highX-lowX)*len(options.categories), 7, 60, 120)
    DATA = TH2D("DATA", "DATA", 4*len(options.categories), lowX, lowX+(highX-lowX)*len(options.categories), 7, 60, 120)
    #MC = TH1D("MC", "MC", 12*len(options.categories), lowX, lowX+(highX-lowX)*len(options.categories))
    #DATA = TH1D("DATA", "DATA", 12*len(options.categories), lowX, lowX+(highX-lowX)*len(options.categories))
    for sample in options.samples:
        print sample
        if "DATA" not in sample : files[sample] = TFile(options.path.replace("NAME",sample.replace("jets","")))
        else : files[sample] = TFile("/nfs/user/acaudron/ControlPlots/cp5314p1/AllRDS/Nominal/RDS_Data2012/Data2012_Summer12_final_skimed_zmet.root")
        t = files[sample].Get("rds_zbb")
        extra = options.wtt*("TT" in sample) + (options.wdy+"*formula(boostselectionZbbM,jetmetbjet1Flavor,jetmetbjet2Flavor)")*("DY" in sample)
        if len(extra)>0 : extra = "*"+extra
        shift = 0.0
	tmp = TH2D("tmp", "tmp", 4*len(options.categories), lowX, lowX+(highX-lowX)*len(options.categories), 7, 60, 120)
        #tmp = TH1D("tmp", "tmp", 12*len(options.categories), lowX, lowX+(highX-lowX)*len(options.categories))
        for cat in options.categories:
	    print cat
	    if not sample=="DATA" : print t.Draw("boostselectionbestzmass"+cat[:2].replace("El","Ele")+":("+str(shift)+"+jetmetbjet1CSVdisc*jetmetbjet2CSVdisc)>>+tmp","("+options.categories[cat]+")"+options.rewForm["Zbb"][cat[:2]]+extra+"*"+str(lumi["DATA"]/lumi[sample.replace("DYjets","Zbb")]))
	    else : print t.Draw("boostselectionbestzmass"+cat[:2].replace("El","Ele")+":("+str(shift)+"+jetmetbjet1CSVdisc*jetmetbjet2CSVdisc)>>+tmp",options.categories[cat])
	    #if not sample=="DATA" : print t.Draw("("+str(shift)+"+jetmetbjet1CSVdisc*jetmetbjet2CSVdisc)>>+tmp","("+options.categories[cat]+")"+options.rewForm["Zbb"][cat[:2]]+extra+"*"+str(lumi["DATA"]/lumi[sample.replace("DYjets","Zbb")]))
	    #else : print t.Draw("("+str(shift)+"+jetmetbjet1CSVdisc*jetmetbjet2CSVdisc)>>+tmp",options.categories[cat])
            shift += (1-lowX)
	    print tmp.Integral()
	if not sample=="DATA" : MC.Add(tmp)
	else : DATA.Add(tmp)
	print ""
    print MC.Integral()
    print DATA.Integral()
    print DATA.Chi2Test(MC,"UW P CHI2/NDF")
    print "KT test", DATA.KolmogorovTest(MC)
            
main()
