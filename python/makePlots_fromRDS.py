#######################################################
#
# Loop over entries
#
# Loop over jets per event
#
# Get flavor, pt, eta and select jets
#
# Get PV, pT, pTHat and determine per-event weigth
#
# Save in a RooDataSet
#   - m(SV)
#   - PV-cat, pT-cat, pThat-cat
#   - weight
#
# (c) Zbb-CP3 Warriors, 2011
#
####################################################

from ROOT import *
import os

gROOT.SetStyle("Plain")
gStyle.SetErrorX(0)

WP       = "HEHE"    #"HP","HPMET","HP_excl","HE","HEmet","He_excl"
channel  = "Mu"    #"El","Mu"
template = "hist"  #"keys", "hist"
jec      = 0       #1,3,5
numbins  = 80      #20,40,80
PVreduce = 0
if WP=="HP" : numbins=numbins/2

#if channel=="Mu" : cutString = 0#"jetmetMET<50&eventSelectionbestzmassMu>76&eventSelectionbestzmassMu<106"#&jetmetbjet1pt>26.&jetmetbjet2pt>26."
if channel=="Mu" : cutString = "jetmetbjet1pt>25.&jetmetbjet2pt>25."
#if channel=="El" : cutString = 0#"jetmetMET<50&eventSelectionbestzmassEle>76&eventSelectionbestzmassEle<106"#&jetmetbjet1pt>26.&jetmetbjet2pt>26."
if channel=="El" : cutString = "jetmetbjet1pt>25.&jetmetbjet2pt>25."

if template=="keys": numbins=40

### Getting a file and a tree

if   channel == "El" : file  = TFile("File_rds_zbb_El_MC.root")
elif channel == "Mu" : file  = TFile("File_rds_zbb_Mu_MC.root")

ws    = file.Get("ws")
myRDS = ws.data("rds_zbb")

if   channel == "El" : file_TT = TFile("File_rds_zbb_Ttbar_El_MC.root")
elif channel == "Mu" : file_TT = TFile("File_rds_zbb_Ttbar_Mu_MC.root")

ws_TT   = file_TT.Get("ws")
RDS_TT  = ws_TT.data("rds_zbb")

if   channel == "El" : file_ZZ = TFile("File_rds_zbb_ZZ_El_MC.root")
elif channel == "Mu" : file_ZZ = TFile("File_rds_zbb_ZZ_Mu_MC.root")

ws_ZZ   = file_ZZ.Get("ws")
RDS_ZZ  = ws_ZZ.data("rds_zbb")

if   channel == "El" : file_ZHbb = TFile("File_rds_zbb_ZHbb_El_MC.root")
elif channel == "Mu" : file_ZHbb = TFile("File_rds_zbb_ZHbb_Mu_MC.root")

ws_ZHbb   = file_ZHbb.Get("ws")
RDS_ZHbb  = ws_ZHbb.data("rds_zbb")

print "myRDS.numEntries() = ", myRDS.numEntries()

nameList = [
#eventSelectiontriggerSelection,
#eventSelectiontriggerBits,
#eventSelectionzmassMu,
    "eventSelectionbestzmassMu",
#eventSelectionzmassEle,
    "eventSelectionbestzmassEle",
#eventSelectionzptMu,
    "eventSelectionbestzptMu",
#eventSelectionzptEle,
    "eventSelectionbestzptEle",
    "eventSelectionscaldptZbj1",
    "eventSelectiondrZbj1",
    "eventSelectiondphiZbj1",
#eventSelectionscaldptZbb,
#eventSelectiondphiZbb,
    "eventSelectiondrZbb",
    "eventSelectiondijetM",
    "eventSelectiondijetPt",
    "eventSelectiondijetdR",
    "eventSelectiondijetSVdR",
#eventSelectiondphidijetMET,
#eventSelectionZbM,
#eventSelectionZbPt,
    "eventSelectionZbbM",
    "eventSelectionZbbPt",
#eventSelectioncategory,
#eventSelectionmu1pt,
#eventSelectionmu2pt,
#eventSelectionmu1eta,
#eventSelectionmu2eta,
#eventSelectionmu1etapm,
#eventSelectionmu2etapm,
#eventSelectionel1pt,
#eventSelectionel2pt,
#eventSelectionel1eta,
#eventSelectionel2eta,
#eventSelectionel1etapm,
#eventSelectionel2etapm,
#BtaggingReweightingHE,
#BtaggingReweightingHP,
#BtaggingReweightingHEexcl,
#BtaggingReweightingHPexcl,
#BtaggingReweightingHEHE,
#BtaggingReweightingHEHP,
#BtaggingReweightingHPHP,
#LeptonsReweightingweight,
#jetmetSSVHEdisc,
#jetmetSSVHPdisc,
#jetmetSVmass,
#jetmetTCHEdisc,
#jetmetTCHPdisc,
#jetmetSSVHEdiscDisc1,
#jetmetSSVHPdiscDisc1,
#jetmetTCHEdiscDisc1,
#jetmetTCHPdiscDisc1,
    "jetmetMET",
#jetmetMETphi,
#jetmetjetpt,
#jetmetjetpt_totunc,
#jetmetjetFlavor,
#jetmetjeteta,
#jetmetjetetapm,
#jetmetjetphi,
#jetmetjetoverlapmu,
#jetmetjetoverlapele,
#jetmetjet1pt,
#jetmetjet1pt_totunc,
#jetmetjet1Flavor,
#jetmetjet1eta,
#jetmetjet1etapm,
    "jetmetjet1SSVHEdisc",
    "jetmetjet1SSVHPdisc",
    "jetmetjet1SVmass",
    "jetmetjet1TCHEdisc",
    "jetmetjet1TCHPdisc",
#jetmetjet2pt,
#jetmetjet2pt_totunc,
#jetmetjet2Flavor,
#jetmetjet2eta,
#jetmetjet2etapm,
#jetmetjet2SSVHEdisc,
#jetmetjet2SSVHPdisc,
#jetmetjet2SVmass,
#jetmetjet2TCHEdisc,
#jetmetjet2TCHPdisc,
    "jetmetbjet1pt",
#jetmetbjet1pt_totunc,
#jetmetbjet1Flavor,
#jetmetbjet1eta,
#jetmetbjet1etapm,
#jetmetbjet1SSVHEdisc,
#jetmetbjet1SSVHPdisc,
#jetmetbjet1SVmass,
#jetmetbjet1TCHEdisc,
#jetmetbjet1TCHPdisc,
#jetmetbjet2pt,
#jetmetbjet2pt_totunc,
#jetmetbjet2Flavor,
#jetmetbjet2eta,
#jetmetbjet2etapm,
#jetmetbjet2SSVHEdisc,
#jetmetbjet2SSVHPdisc,
#jetmetbjet2SVmass,
#jetmetbjet2TCHEdisc,
#jetmetbjet2TCHPdisc,
#jetmetdptj1b1,
#jetmetnj,
#jetmetnb,
#jetmetnbP,
#jetmetnhf,
#jetmetnef,
#jetmetnpf,
#jetmetchf,
#jetmetnch,
#jetmetcef,
#jetmetjetid,
#vertexAssociationnvertices,
#vertexAssociationvx,
#vertexAssociationvy,
#vertexAssociationvz,
#vertexAssociationvxerr,
#vertexAssociationvyerr,
#vertexAssociationvzerr,
#vertexAssociationlepton_dz,
#vertexAssociationl1v_dz,
#vertexAssociationl2v_dz,
#vertexAssociationdistance,
#vertexAssociationsig,
#vertexAssociationratio1,
#vertexAssociationratio2,
#vertexAssociationratio3,
#vertexAssociationratio1b,
#vertexAssociationratio2b,
#vertexAssociationratio3b,
#vertexAssociationj1_ratio1,
#vertexAssociationj1_ratio2,
#vertexAssociationj1_ratio3,
#vertexAssociationj1_ratio1b,
#vertexAssociationj1_ratio2b,
#vertexAssociationj1_ratio3b,
#vertexAssociationgoodevent,
#vertexAssociationratio1b_nopu,
#vertexAssociationratio2b_nopu,
#vertexAssociationratio3b_nopu,
#vertexAssociationj1_ratio1b_nopu,
#vertexAssociationj1_ratio2b_nopu,
#vertexAssociationj1_ratio3b_nopu,
#mcSelectioneventType,
#lumiReweightingLumiWeight,
#lumiReweightingpu,
#lumiReweightingpv,
]

    
namePlotList = [
#    "eventSelectionbestzmassMu"  ,  ##
#    "eventSelectionbestzmassEle" ,
    "eventSelectionbestzptMu"    ,
    "eventSelectionbestzptEle"   ,
#    "jetmetbjet1pt"              ,   
#    "jetmetbjet2pt"              ,   
#    "jetmetMET"                  ,
#    "eventSelectiondphiZbb"      ,
#    "eventSelectiondphiZbj1"     , 
    "eventSelectiondijetPt"      ,#
#    "eventSelectiondijetM"       ,
#    "eventSelectiondijetdR"      ,
#    "eventSelectiondijetSVdR"    ,
#    "eventSelectionZbbM"         
    ]
    
max = {
    "eventSelectionbestzmassMu" :  200 ,  
    "eventSelectionbestzmassEle":  200 ,  
    "eventSelectionbestzptMu"   :  300 ,
    "eventSelectionbestzptEle"  :  300 ,
    "eventSelectiondijetPt"     :  300 ,
    "eventSelectiondrZbj1"      :    6 ,
    "jetmetbjet1pt"             :  250 ,
    "jetmetbjet2pt"             :  250 ,   
    "jetmetMET"                 :  200 , 
    "eventSelectiondphiZbj1"    :    6 ,
    "eventSelectiondphiZbb"     :    6 ,
    "eventSelectiondrZbb"       :    6 ,
    "eventSelectionscaldptZbj1" :  150 ,
    "eventSelectiondijetM"      :  600 ,
    "eventSelectiondijetdR"     :    5 ,
    "eventSelectiondijetSVdR"   :    5 ,
    "eventSelectionZbbM"        : 1000 ,
    "eventSelectionZbbPt"       :  300 ,
    "jetmetjet1SSVHEdisc"       :    6 ,
    "jetmetjet1SSVHPdisc"       :    6 ,
    "jetmetjet1SVmass"          :    6 ,
    "jetmetjet1TCHEdisc"        :   15 ,
    "jetmetjet1TCHPdisc"        :   15 ,
    "jetmetMET"                 :  250 
    }
    

var = {}
for name in namePlotList:
    print "name = ", name
    var[name] = ws.var(name)
    var[name].setMin(0)
    var[name].setMax(max[name])
    var[name].setBins(15)

rrv_msv    = ws.var("jetmetbjet1SVmass")
#rrv_bTagHE = ws.var("rrv_bTagHE")
#rrv_bTagHP = ws.var("rrv_bTagHP")
rrv_pT     = ws.var("jetmetjet1pt")
rrv_eta    = ws.var("jetmetjet1eta")
#rrv_nPV    = ws.var("eventSelectionnpf")
rrv_pT_unc = ws.var("jetmetjet1pt_totunc")
rc_flav    = ws.cat("mcSelectioneventType")

rrv_w_HE   = ws.var("BtaggingReweightingHE")
rrv_w_HP   = ws.var("BtaggingReweightingHP")
rrv_w_HEHE = ws.var("BtaggingReweightingHEHE")
rrv_w_HEHP = ws.var("BtaggingReweightingHEHP")
rrv_w_HPHP = ws.var("BtaggingReweightingHPHP")

rrv_w_lep  = ws.var("LeptonsReweightingweight")
rrv_w_lumi = ws.var("lumiReweightingLumiWeight")

rrv_pT.setMin(25)
rrv_pT.setMax(150)
rrv_pT.setBins(25)

rrv_eta.setMin(-2.1)
rrv_eta.setMax( +2.1)
rrv_eta.setBins( 21)

rrv_msv.setMin(0)
rrv_msv.setMax(10)
rrv_msv.setBins(numbins)

#rrv_nPV.setMin(0)
#rrv_nPV.setMax(20)
#rrv_nPV.setBins(20)

f_data = 0
if channel == "El"  : f_data = TFile("File_rds_zbb_El_DATA.root")
elif channel == "Mu" : f_data = TFile("File_rds_zbb_Mu_DATA.root")

ws_data=f_data.Get("ws")
DATA = ws_data.data("rds_zbb")

if PVreduce == 1:
    DATA = DATA.reduce("vertexAssociationnvertices<4.5")
    myRDS=myRDS.reduce("vertexAssociationnvertices<4.5")
if PVreduce == 2:
    DATA = DATA.reduce("vertexAssociationnvertices>4.5")
    DATA = DATA.reduce("vertexAssociationnvertices<7.5")
    myRDS=myRDS.reduce("vertexAssociationnvertices>4.5")
    myRDS=myRDS.reduce("vertexAssociationnvertices<7.5")
if PVreduce == 3:
    DATA = DATA.reduce("vertexAssociationnvertices>7.5")
    myRDS=myRDS.reduce("vertexAssociationnvertices>7.5")

if WP=="HE"         :
    DATA = DATA.reduce("rc_eventSelection_5==1")
    myRDS=myRDS.reduce("rc_eventSelection_5==1")
if WP=="HEMET"      :
    DATA = DATA.reduce("rc_HEMET==1")
    myRDS=myRDS.reduce("rc_HEMET==1")
if WP=="HE_excl"    :
    DATA = DATA.reduce("rc_HE_excl==1")
    myRDS=myRDS.reduce("rc_HE_excl==1")
if WP=="HEMET_excl" :
    DATA = DATA.reduce("rc_HEMET_excl==1")
    myRDS=myRDS.reduce("rc_HEMET_excl==1")
if WP=="HP"         :
    DATA = DATA.reduce("rc_eventSelection_6==1")
    myRDS=myRDS.reduce("rc_eventSelection_6==1")
if WP=="HPMET"      :
    DATA = DATA.reduce("rc_HPMET==1")
    myRDS=myRDS.reduce("rc_HPMET==1")
if WP=="HP_excl"    :
    DATA = DATA.reduce("rc_HP_excl==1")
    myRDS=myRDS.reduce("rc_HP_excl==1")
if WP=="HPMET_excl" :
    DATA = DATA.reduce("rc_HPMET_excl==1")
    myRDS=myRDS.reduce("rc_HPMET_excl==1")

print "DATA.numEntries() = ", DATA.numEntries()


RAS = DATA.get()
DATA_withunc = RooDataSet("rds_zbb_with_unc","rds_zbb_with_unc",RAS)

for i in range(0,DATA.numEntries()):
    RASi = DATA.get(i)
    ptVal = RASi.getRealValue("rrv_pT")
    ptuncVal = RASi.getRealValue("rrv_pT_unc")*ptVal
    RAS.setRealValue("rrv_pT",ptVal+jec*ptuncVal)
    DATA_withunc.add(RAS)

DATA = DATA_withunc

myRDS_l = myRDS.reduce("mcSelectioneventType==1")
myRDS_c = myRDS.reduce("mcSelectioneventType==2")
myRDS_b = myRDS.reduce("mcSelectioneventType==3")

print "myRDS_l.numEntries() = ", myRDS_l.numEntries()
print "myRDS_c.numEntries() = ", myRDS_c.numEntries()
print "myRDS_b.numEntries() = ", myRDS_b.numEntries()


rrv_pT.setMin(25)
rrv_pT.setMax(150)
rrv_pT.setBins(25)

rrv_eta.setMin(-2.5)
rrv_eta.setMax(2.5)
rrv_eta.setBins(10)

print "making the three keys pdfs" 

b_sumPdf=0
c_sumPdf=0
l_sumPdf=0

print "making the three hist pdfs"

gROOT.SetStyle("Plain")
gStyle.SetErrorX(0)

#freem = rrv_msv.frame(rrv_msv.getMin(),rrv_msv.getMax()/2.,rrv_msv.getBins()/2)
#freem.SetBarWidth(0.)
#freem.SetMarkerSize(0.7)
#freem.SetLineWidth(1)
#
#DATA.plotOn(freem,
#            RooFit.MarkerSize(0.3),
#            RooFit.XErrorSize(0.035),
#            RooFit.DrawOption("pe2"))
#sumPdf.plotOn(freem,RooFit.LineWidth(1),RooFit.LineColor(kBlack))
#sumPdf.plotOn(freem,RooFit.Components("b_sumPdf"),RooFit.LineWidth(1),RooFit.LineColor(kRed),  RooFit.LineStyle(kDashed))
#sumPdf.plotOn(freem,RooFit.Components("g_sumPdf"),RooFit.LineWidth(1),RooFit.LineColor(kMagenta),RooFit.LineStyle(kDashed))
#sumPdf.plotOn(freem,RooFit.Components("c_sumPdf"),RooFit.LineWidth(1),RooFit.LineColor(kGreen),RooFit.LineStyle(kDashed))
#sumPdf.plotOn(freem,RooFit.Components("l_sumPdf"),RooFit.LineWidth(1),RooFit.LineColor(kBlue), RooFit.LineStyle(kDashed))
#DATA.plotOn(freem,
#            RooFit.MarkerSize(0.3),
#            RooFit.XErrorSize(0.035),
#            RooFit.DrawOption("pe2"))
#sumPdf.paramOn(freem,DATA)
#freem.Draw()#
#
#C1.cd(2)
#freem2 = rrv_msv.frame(rrv_msv.getMin(),rrv_msv.getMax()/2.,rrv_msv.getBins()/2)
#freem2.SetBarWidth(0.)
#freem2.SetMarkerSize(0.7)
#freem2.SetLineWidth(1)
               
#DATA.plotOn(freem2,
#            RooFit.MarkerSize(0.7),
#            RooFit.XErrorSize(0.035),
#            RooFit.DrawOption("pe2"))
#sumPdf2.plotOn(freem2,RooFit.LineWidth(1),RooFit.Components("l_sumPdf,b_sumPdf,c_sumPdf"), RooFit.FillColor(kRed),  RooFit.DrawOption("F"), RooFit.LineColor(kBlack))
#sumPdf2.plotOn(freem2,RooFit.LineWidth(1),RooFit.Components("l_sumPdf,b_sumPdf,c_sumPdf"), RooFit.FillColor(kBlue), RooFit.DrawOption("F"), RooFit.LineColor(kBlack))
#sumPdf2.plotOn(freem2,RooFit.LineWidth(1),RooFit.Components("l_sumPdf,b_sumPdf,c_sumPdf"), RooFit.FillColor(kBlue), RooFit.LineColor(kBlack))
#sumPdf2.plotOn(freem2,RooFit.LineWidth(1),RooFit.Components("c_sumPdf,b_sumPdf"),          RooFit.FillColor(kGreen),RooFit.DrawOption("F"), RooFit.LineColor(kBlack))
#sumPdf2.plotOn(freem2,RooFit.LineWidth(1),RooFit.Components("c_sumPdf,b_sumPdf"),          RooFit.FillColor(kGreen),RooFit.LineColor(kBlack))
#sumPdf2.plotOn(freem2,RooFit.LineWidth(1),RooFit.Components("b_sumPdf"),                   RooFit.FillColor(kRed),  RooFit.DrawOption("F"), RooFit.LineColor(kBlack))
#sumPdf2.plotOn(freem2,RooFit.LineWidth(1),RooFit.Components("b_sumPdf"),                   RooFit.FillColor(kRed),  RooFit.LineColor(kBlack))
#DATA.plotOn(freem2,
#            RooFit.MarkerSize(0.7),
#            RooFit.XErrorSize(0.035),
#            RooFit.DrawOption("pe2"))
#sumPdf2.paramOn(freem2,DATA)
#freem2.Draw()

rrv_msv.SetTitle("Secondary vertex mass")
rrv_msv.setUnit("GeV")

#from drawStyle import *
#setStyle()

##########################################

lumi_of_TT = (3701947./157.5)/1000.
lumi_of_DY = (36257961./3048.)/1000.
lumi_of_ZZ = 4000000./6000.
lumi_of_ZHbb = 12000.
lumi_of_ZHbb = lumi_of_ZHbb
lumi_of_DATA = 2.130

print "the lumi of TT MC = ", lumi_of_TT        
print "the lumi of DY MC = ", lumi_of_DY
print "the lumi of ZZ MC = ", lumi_of_ZZ
print "the lumi of ZHbb MC = ", lumi_of_ZHbb

if cutString :
    RDS_TT = RDS_TT.reduce(cutString)
    myRDS  = myRDS.reduce(cutString)
    DATA   = DATA.reduce(cutString)
    RDS_ZZ = RDS_ZZ.reduce(cutString)
    RDS_ZHbb = RDS_ZHbb.reduce(cutString)

if WP == "HEHE":
    RDS_ZHbb_red = RDS_ZHbb.reduce("rc_eventSelection_9==1")
    RDS_ZZ_red = RDS_ZZ.reduce("rc_eventSelection_9==1")
    RDS_TT_red = RDS_TT.reduce("rc_eventSelection_9==1")
    RDS_DY_red = myRDS.reduce("rc_eventSelection_9==1")
    DATA_red   = DATA.reduce("rc_eventSelection_9==1")
elif WP == "HPHP":
    RDS_ZHbb_red = RDS_ZHbb.reduce("rc_eventSelection_11==1")
    RDS_ZZ_red = RDS_ZZ.reduce("rc_eventSelection_11==1")
    RDS_TT_red = RDS_TT.reduce("rc_eventSelection_11==1")
    RDS_DY_red = myRDS.reduce("rc_eventSelection_11==1")
    DATA_red   = DATA.reduce("rc_eventSelection_11==1")
elif WP=="HE":
    RDS_ZHbb_red = RDS_ZHbb.reduce("rc_eventSelection_5==1")
    RDS_ZZ_red = RDS_ZZ.reduce("rc_eventSelection_5==1")
    RDS_TT_red = RDS_TT.reduce("rc_eventSelection_5==1")
    RDS_DY_red = myRDS.reduce("rc_eventSelection_5==1")
    DATA_red   = DATA.reduce("rc_eventSelection_5==1")
elif WP=="HP":
    RDS_ZHbb_red = RDS_ZHbb.reduce("rc_eventSelection_6==1")
    RDS_ZZ_red = RDS_ZZ.reduce("rc_eventSelection_6==1")
    RDS_TT_red = RDS_TT.reduce("rc_eventSelection_6==1")
    RDS_DY_red = myRDS.reduce("rc_eventSelection_6==1")
    DATA_red   = DATA.reduce("rc_eventSelection_6==1")

if channel == "El":
    RDS_ZHbb_red = RDS_ZHbb_red.reduce("eventSelectionbestzmassEle>50")
    RDS_ZZ_red = RDS_ZZ_red.reduce("eventSelectionbestzmassEle>50")
    RDS_TT_red = RDS_TT_red.reduce("eventSelectionbestzmassEle>50")
    RDS_DY_red = RDS_DY_red.reduce("eventSelectionbestzmassEle>50")
    DATA_red   = DATA_red.reduce("eventSelectionbestzmassEle>50")
elif channel == "Mu" :    
    RDS_ZHbb_red = RDS_ZHbb_red.reduce("eventSelectionbestzmassMu>50")
    RDS_ZZ_red = RDS_ZZ_red.reduce("eventSelectionbestzmassMu>50")
    RDS_TT_red = RDS_TT_red.reduce("eventSelectionbestzmassMu>50")
    RDS_DY_red = RDS_DY_red.reduce("eventSelectionbestzmassMu>50")
    DATA_red   = DATA_red.reduce("eventSelectionbestzmassMu>50")

gStyle.SetPalette(1)

C=TCanvas("C","C",800,400)
C.Divide(2)
C.cd(1)
DATA_red.tree().Draw("eventSelectiondijetPt:eventSelectionbestzptMu","","contz")
C.cd(2)
RDS_DY_red.tree().Draw("eventSelectiondijetPt:eventSelectionbestzptMu","","contz")

bla

#rrv_w_HE   = ws.var("BtaggingReweightingHE")
#rrv_w_HP   = ws.var("BtaggingReweightingHP")
#rrv_w_HEHP = ws.var("BtaggingReweightingHEHP")
#rrv_w_HPHP = ws.var("BtaggingReweightingHPHP")
#
#rrv_w_HEHE = ws.var("BtaggingReweightingHEHE")
#rrv_w_lep  = ws.var("LeptonsReweightingweight")
#rrv_w_lumi = ws.var("lumiReweightingLumiWeight")

if   WP == "HEHE": w = RooFormulaVar("w","w", "@0*@1*@2", RooArgList(rrv_w_HEHE,rrv_w_lep,rrv_w_lumi)) 
elif WP == "HPHP": w = RooFormulaVar("w","w", "@0*@1*@2", RooArgList(rrv_w_HPHP,rrv_w_lep,rrv_w_lumi)) 

w_HEHE = RooFormulaVar("w_HEHE","w_HEHE", "@0", RooArgList(rrv_w_HEHE)) 
w_lep  = RooFormulaVar("w_lep", "w_lep",  "@0", RooArgList(rrv_w_lep)) 
w_lumi = RooFormulaVar("w_lumi","w_lumi", "@0", RooArgList(rrv_w_lumi)) 

RDS_TT_red.addColumn(w) 
RDS_DY_red.addColumn(w)
RDS_ZZ_red.addColumn(w) 
RDS_ZHbb_red.addColumn(w) 

RDS_TT_red.addColumn(w_HEHE) 
RDS_DY_red.addColumn(w_HEHE)
RDS_ZZ_red.addColumn(w_HEHE) 
RDS_ZHbb_red.addColumn(w_HEHE) 

RDS_TT_red.addColumn(w_lep) 
RDS_DY_red.addColumn(w_lep)
RDS_ZZ_red.addColumn(w_lep) 
RDS_ZHbb_red.addColumn(w_lep) 

RDS_TT_red.addColumn(w_lumi) 
RDS_DY_red.addColumn(w_lumi)
RDS_ZZ_red.addColumn(w_lumi) 
RDS_ZHbb_red.addColumn(w_lumi) 

RDS_TT_red_w = RooDataSet("RDS_TT_red_w","RDS_TT_red_w",RDS_TT_red,RDS_TT_red.get(),"","w")
RDS_DY_red_w = RooDataSet("RDS_DY_red_w","RDS_DY_red_w",RDS_DY_red,RDS_DY_red.get(),"","w")
RDS_ZZ_red_w = RooDataSet("RDS_ZZ_red_w","RDS_ZZ_red_w",RDS_ZZ_red,RDS_ZZ_red.get(),"","w")
RDS_ZHbb_red_w = RooDataSet("RDS_ZHbb_red_w","RDS_ZHbb_red_w",RDS_ZHbb_red,RDS_ZHbb_red.get(),"","w")

RDS_TT_red_w_HEHE = RooDataSet("RDS_TT_red_w_HEHE","RDS_TT_red_w_HEHE",RDS_TT_red,RDS_TT_red.get(),"","w_HEHE")
RDS_DY_red_w_HEHE = RooDataSet("RDS_DY_red_w_HEHE","RDS_DY_red_w_HEHE",RDS_DY_red,RDS_DY_red.get(),"","w_HEHE")
RDS_ZZ_red_w_HEHE = RooDataSet("RDS_ZZ_red_w_HEHE","RDS_ZZ_red_w_HEHE",RDS_ZZ_red,RDS_ZZ_red.get(),"","w_HEHE")

RDS_TT_red_w_lep  = RooDataSet("RDS_TT_red_w_lep", "RDS_TT_red_w_lep", RDS_TT_red,RDS_TT_red.get(),"","w_lep")
RDS_DY_red_w_lep  = RooDataSet("RDS_DY_red_w_lep", "RDS_DY_red_w_lep", RDS_DY_red,RDS_DY_red.get(),"","w_lep")
RDS_ZZ_red_w_lep  = RooDataSet("RDS_ZZ_red_w_lep", "RDS_ZZ_red_w_lep", RDS_ZZ_red,RDS_ZZ_red.get(),"","w_lep")

RDS_TT_red_w_lumi = RooDataSet("RDS_TT_red_w_lumi","RDS_TT_red_w_lumi",RDS_TT_red,RDS_TT_red.get(),"","w_lumi")
RDS_DY_red_w_lumi = RooDataSet("RDS_DY_red_w_lumi","RDS_DY_red_w_lumi",RDS_DY_red,RDS_DY_red.get(),"","w_lumi")
RDS_ZZ_red_w_lumi = RooDataSet("RDS_ZZ_red_w_lumi","RDS_ZZ_red_w_lumi",RDS_ZZ_red,RDS_ZZ_red.get(),"","w_lumi")

print "the pure number of entries of TT MC = ", RDS_TT_red_w.numEntries() 
print "the pure number of entries of DY MC = ", RDS_DY_red_w.numEntries() 
print "the pure number of entries of ZZ MC = ", RDS_ZZ_red_w.numEntries() 
print "the pure number of entries of ZHbb MC = ", RDS_ZHbb_red_w.numEntries() 
print "***"
print "the effective number of TT MC for this data-lumi = ", RDS_TT_red_w.numEntries()*(lumi_of_DATA/lumi_of_TT)
print "the effective number of DY MC for this data-lumi = ", RDS_DY_red_w.numEntries()*(lumi_of_DATA/lumi_of_DY)
print "the effective number of ZZ MC for this data-lumi = ", RDS_ZZ_red_w.numEntries()*(lumi_of_DATA/lumi_of_ZZ)
print "the effective number of ZHbb MC for this data-lumi = ", RDS_ZHbb_red_w.numEntries()*(lumi_of_DATA/lumi_of_ZHbb)
print "***"
print "the effective weighted (w_HEHE) number of TT MC for this data lumi = ", RDS_TT_red_w_HEHE.sumEntries()*(lumi_of_DATA/lumi_of_TT)
print "the effective weighted (w_HEHE) number of DY MC for this data lumi = ", RDS_DY_red_w_HEHE.sumEntries()*(lumi_of_DATA/lumi_of_DY)
print "the effective weighted (w_HEHE) number of ZZ MC for this data lumi = ", RDS_ZZ_red_w_HEHE.sumEntries()*(lumi_of_DATA/lumi_of_ZZ)
print "***"
print "the effective weighted (w_lep)  number of TT MC for this data lumi = ", RDS_TT_red_w_lep.sumEntries()*(lumi_of_DATA/lumi_of_TT)
print "the effective weighted (w_lep)  number of DY MC for this data lumi = ", RDS_DY_red_w_lep.sumEntries()*(lumi_of_DATA/lumi_of_DY)
print "the effective weighted (w_lep)  number of ZZ MC for this data lumi = ", RDS_ZZ_red_w_lep.sumEntries()*(lumi_of_DATA/lumi_of_ZZ)
print "***"
print "the effective weighted (w_lumi) number of TT MC for this data lumi = ", RDS_TT_red_w_lumi.sumEntries()*(lumi_of_DATA/lumi_of_TT)
print "the effective weighted (w_lumi) number of DY MC for this data lumi = ", RDS_DY_red_w_lumi.sumEntries()*(lumi_of_DATA/lumi_of_DY)
print "the effective weighted (w_lumi) number of ZZ MC for this data lumi = ", RDS_ZZ_red_w_lumi.sumEntries()*(lumi_of_DATA/lumi_of_ZZ)
print "***"
print "==> the effective weighted (w_HEHE*w_lep*w_lumi) number of TT MC for this data lumi = ", RDS_TT_red_w.sumEntries()*(lumi_of_DATA/lumi_of_TT)
print "==> the effective weighted (w_HEHE*w_lep*w_lumi) number of DY MC for this data lumi = ", RDS_DY_red_w.sumEntries()*(lumi_of_DATA/lumi_of_DY)
print "==> the effective weighted (w_HEHE*w_lep*w_lumi) number of ZZ MC for this data lumi = ", RDS_ZZ_red_w.sumEntries()*(lumi_of_DATA/lumi_of_ZZ)
print "==> the effective weighted (w_HEHE*w_lep*w_lumi) number of ZHbb MC for this data lumi = ", RDS_ZHbb_red_w.sumEntries()*(lumi_of_DATA/lumi_of_ZHbb)

num_TT_MC = RooRealVar("num_TT_MC","num_TT_MC",
                       RDS_TT_red_w.sumEntries()*(lumi_of_DATA/lumi_of_TT))
num_ZZ_MC = RooRealVar("num_ZZ_MC","num_ZZ_MC",
                       RDS_ZZ_red_w.sumEntries()*(lumi_of_DATA/lumi_of_ZZ))
num_ZHbb_MC = RooRealVar("num_ZHbb_MC","num_ZHbb_MC",
                       RDS_ZHbb_red_w.sumEntries()*(lumi_of_DATA/lumi_of_ZHbb))

num_DY_MC = RooRealVar("num_DY_MC","num_DY_MC",
                       RDS_DY_red_w.sumEntries()*(lumi_of_DATA/lumi_of_DY))

total_MC = num_TT_MC.getVal()+num_DY_MC.getVal()+num_ZZ_MC.getVal()+num_ZHbb_MC.getVal()

print "the total (DY+TT+ZZ) MC events = " , total_MC
print "the lumi of DATA = 2.1 fb-1???"  , lumi_of_DATA
print "the number of entries of DATA = ", DATA_red.numEntries()

norm = total_MC/DATA_red.numEntries()

print "MC normalization = ", norm

var_frame = {}

for name in namePlotList:
    var[name]
    rdh_TT = RooDataHist("rdh_TT", "rdh_TT",
                         RooArgSet(var[name]),
                         RDS_TT_red_w)
    rdh_DY = RooDataHist("rdh_DY", "rdh_DY",
                         RooArgSet(var[name]),
                         RDS_DY_red_w)
    rdh_ZZ = RooDataHist("rdh_ZZ", "rdh_ZZ",
                         RooArgSet(var[name]),
                         RDS_ZZ_red_w)
    rdh_ZHbb = RooDataHist("rdh_ZHbb", "rdh_ZHbb",
                         RooArgSet(var[name]),
                         RDS_ZHbb_red_w)

    rhp_TT = RooHistPdf("rhp_TT","rhp_TT",
                        RooArgSet(var[name]),
                        rdh_TT)
    rhp_DY = RooHistPdf("rhp_DY","rhp_DY",
                        RooArgSet(var[name]),
                        rdh_DY)
    rhp_ZZ = RooHistPdf("rhp_ZZ","rhp_ZZ",
                        RooArgSet(var[name]),
                        rdh_ZZ)
    rhp_ZHbb = RooHistPdf("rhp_ZHbb","rhp_ZHbb",
                        RooArgSet(var[name]),
                        rdh_ZHbb)
    sum = RooAddPdf("sum","sum",RooArgList(rhp_TT,rhp_DY,rhp_ZZ,rhp_ZHbb),RooArgList(num_TT_MC,num_DY_MC,num_ZZ_MC,num_ZHbb_MC)    )


    var_frame[name] = var[name].frame()
    DATA_red.plotOn(var_frame[name],
                    RooFit.MarkerSize(1.0),
                    RooFit.XErrorSize(0.035),
                    RooFit.DrawOption("pe2"))
    #sum.plotOn(var_frame[name],
    #           RooFit.Normalization(norm),
    #           RooFit.LineColor(kBlack))
    sum.plotOn(var_frame[name],
               RooFit.Components("rhp_TT,rhp_DY,rhp_ZZ,rhp_ZHbb"),
               RooFit.LineColor(kBlack),
               RooFit.FillColor(kGreen-7),
               RooFit.DrawOption("F"),
               RooFit.LineWidth(1),
               RooFit.Normalization(norm))
    sum.plotOn(var_frame[name],
               RooFit.Components("rhp_TT,rhp_DY,rhp_ZZ,rhp_ZHbb"),
               RooFit.LineColor(kBlack),
               RooFit.FillColor(kGreen-7),
               RooFit.LineWidth(1),
               RooFit.Normalization(norm))
    sum.plotOn(var_frame[name],
               RooFit.Components("rhp_TT,rhp_DY,rhp_ZZ"),
               RooFit.LineColor(kBlack),
               RooFit.FillColor(kYellow-7),
               RooFit.DrawOption("F"),
               RooFit.LineWidth(1),
               RooFit.Normalization(norm))
    sum.plotOn(var_frame[name],
               RooFit.Components("rhp_TT,rhp_DY,rhp_ZZ"),
               RooFit.LineColor(kBlack),
               RooFit.FillColor(kYellow-7),
               RooFit.LineWidth(1),
               RooFit.Normalization(norm))
    sum.plotOn(var_frame[name],
               RooFit.Components("rhp_DY,rhp_ZZ"),
               RooFit.LineColor(kBlack),
               RooFit.FillColor(kRed-7),
               RooFit.DrawOption("F"),
               RooFit.LineWidth(1),
               RooFit.Normalization(norm))
    sum.plotOn(var_frame[name],
               RooFit.Components("rhp_DY,rhp_ZZ"),
               RooFit.LineColor(kBlack),
               RooFit.FillColor(kRed-7),
               RooFit.LineWidth(1),
               RooFit.Normalization(norm))
    sum.plotOn(var_frame[name],
               RooFit.Components("rhp_ZZ"),
               RooFit.LineColor(kBlack),
               RooFit.FillColor(kBlue-7),
               RooFit.DrawOption("F"),
               RooFit.LineWidth(1),
               RooFit.Normalization(norm))
    sum.plotOn(var_frame[name],
               RooFit.Components("rhp_ZZ"),
               RooFit.LineColor(kBlack),
               RooFit.FillColor(kBlue-7),
               RooFit.LineWidth(1),
               RooFit.Normalization(norm))
    DATA_red.plotOn(var_frame[name],
                    RooFit.MarkerSize(1.0),
                    RooFit.XErrorSize(0.035),
                    RooFit.DrawOption("pe2"))

#######################################################

from drawStyle import *

setStyle()

CANVAS = {}

for name in namePlotList :
    CANVAS[name] = TCanvas("CANVAS"+name,"CANVAS"+name,600,600)

    borderX = CANVAS[name].GetWindowWidth()-CANVAS[name].GetWw()
    borderY = CANVAS[name].GetWindowHeight()-CANVAS[name].GetWh()
    CANVAS[name].SetCanvasSize(500,500)
    CANVAS[name].SetWindowSize(500+borderX,500+borderY)
    
    CANVAS[name].Modified()
    CANVAS[name].Update()
#float x = frame->GetX1() + (frame->GetX2()-frame->GetX1())*0.03;
#float y = frame->GetY2() - (frame->GetY2()-frame->GetY1())*0.1;

    CANVAS[name].UseCurrentStyle()

#######################################################

    var_frame[name].Draw()

    leg1 = TLegend(0.72, 0.55, 0.92, 0.95-0.15, "", "NDC")
    leg1.AddEntry( var_frame[name].getObject(0), "Data ", "PLE")
    leg1.AddEntry( var_frame[name].getObject(2), "Z+H(bb)"  ,"F")
    leg1.AddEntry( var_frame[name].getObject(4), "tt"  ,"F")
    leg1.AddEntry( var_frame[name].getObject(6), "DY"  ,"F")
    leg1.AddEntry( var_frame[name].getObject(8), "ZZ"  ,"F")
    
    leg1.SetTextSize(0.04)
    leg1.SetFillColor(0)
    leg1.SetShadowColor(0)
    leg1.SetBorderSize(0)
    
    leg1.Draw()
    
    lat=TLatex()
    lat.SetTextSize(0.04)
    lat.DrawLatex(0.55*var[name].getMax(),0.88*var_frame[name].GetMaximum(),"#splitline{CMS Preliminary}{#sqrt{s} = 7 TeV, L = 2.1 fb^{-1}}")
    
    lat2=TLatex()
    lat2.SetTextSize(0.04)
    if WP=="HE" : lat2.DrawLatex(0.55*var[name].getMax(),0.45*var_frame[name].GetMaximum(),"High eff. b-tagging")
    if WP=="HP" : lat2.DrawLatex(0.55*var[name].getMax(),0.45*var_frame[name].GetMaximum(),"High purity b-tagging")
    
    CANVAS[name].Draw()

###########################################################


