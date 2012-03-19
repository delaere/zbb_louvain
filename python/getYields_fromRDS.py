from ROOT import *

file_el  = TFile("File_rds_zbb_ZZ_El_MC.root")
file_mu  = TFile("File_rds_zbb_ZZ_El_MC.root")

ws_el    = file_el.Get("ws")
ws_mu    = file_mu.Get("ws")

myRDS_el = ws_el.data("rds_zbb")
myRDS_mu = ws_mu.data("rds_zbb")

print "myRDS_el.numEntries() = ", myRDS_el.numEntries()
print "myRDS_mu.numEntries() = ", myRDS_mu.numEntries()

myRDS_el.append(myRDS_mu)
myRDS=myRDS_el
ws=ws_el

rrv_w_HE   = ws.var("BtaggingReweightingHE")
rrv_w_HP   = ws.var("BtaggingReweightingHP")
rrv_w_HEHE = ws.var("BtaggingReweightingHEHE")
rrv_w_HEHP = ws.var("BtaggingReweightingHEHP")
rrv_w_HPHP = ws.var("BtaggingReweightingHPHP")

rrv_w_lep  = ws.var("LeptonsReweightingweight")
rrv_w_lumi = ws.var("lumiReweightingLumiWeight")


w = { "HEHE" : RooFormulaVar("w","w", "@0*@1*@2", RooArgList(rrv_w_HEHE,rrv_w_lep,rrv_w_lumi)),
      "HPHP" : RooFormulaVar("w","w", "@0*@1*@2", RooArgList(rrv_w_HPHP,rrv_w_lep,rrv_w_lumi)) }



lumi_of_DATA = 2.1

MC_xsec = 6000.
MC_nevents = 4000000.
lumi_of_ZZ   = MC_nevents/MC_xsec

MC_weight = lumi_of_DATA/lumi_of_ZZ

print "lumi_of_ZZ = ", lumi_of_ZZ
print "MC_weight = ", MC_weight

myRDS_red = myRDS.reduce("rc_eventSelection_9==1")

myRDS_red.addColumn(w["HEHE"])

myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w")

print "the pure number of entries of ZZ MC = ", myRDS_red_w.numEntries()
print "the effective number of ZZ MC for this data-lumi = ", myRDS_red_w.numEntries()*(lumi_of_DATA/lumi_of_ZZ)


print "the effective weighted number of ZZ MC for this data lumi = ", myRDS_red_w.sumEntries()*(lumi_of_DATA/lumi_of_ZZ)




#num_TT_MC = RooRealVar("num_TT_MC","num_TT_MC",
#                       RDS_TT_red_w.sumEntries()*(lumi_of_DATA/lumi_of_TT))
#num_DY_MC = RooRealVar("num_DY_MC","num_DY_MC",
#                        RDS_DY_red_w.sumEntries()*(lumi_of_DATA/lumi_of_DY))
#total_MC = num_TT_MC.getVal()+num_DY_MC.getVal()
#
#print "the total (DY+TT) MC events = " , total_MC
#print "the lumi of DATA = 2.1 fb-1???"  , lumi_of_DATA
#print "the number of entries of DATA = ", DATA_red.numEntries()#
#
#norm = total_MC/DATA_red.numEntries()



    
