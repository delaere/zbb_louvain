from ROOT import *
import os
gSystem.Load("DrawCanvas_C.so")

#Dir = "~/workspace/rootfiles/"
Dir = "~/workspace/testRew2/" ###### 1. DIRECOTY WHERE THE ROOTFILES ARE
#file = TFile(Dir+"MERGEDoverflowWithZH125.root","READ")
#file = TFile(Dir+"MERGEDoverflowWithHiggs.root","READ")
#file = TFile(Dir+"bkgNorm/mergedPlots_2012ABCD_V1_higgs_allMC_30GeV_stage18_database_bkgnorm.root","READ")
#file = TFile(Dir+"mergedPlots_2012ABCD_V1_higgs_allMC_30GeV_database_centrality_V57_JES0.root","READ")
#file = TFile(Dir+"mergedPlots_2012ABCD_V1_higgs_allMC_30GeV_subjets18.root","READ")
#nameF = "ZbblowMET_smallMll_RewFormformulaPol3DYdiv_NoRew_testRew.root"
#nameF = "Zbb_Rew_ZbblowMET_smallMll_RewFormformulaPol3DYdivNewSFs_NotNorm_testRew.root"
nameF = "Zjj_Rew_ZjjlowMET_smallMll_Mllbb350to750_RewFormformulaPol3DYdiv_NotNorm_testRew.root" ########## 2. NAME OF THE ROOTFILE
file = TFile(Dir+nameF,"READ")
#file = TFile(Dir+"MERGEDoverflowWithZZ_ZHtop.root","READ")
#path = "Electron/stage_37/jetmetAK5PF/"
#path = "Combined/stage_18/selection/"
#path = "Combined/stage_3/selection/"
#path = "Muon/stage_18/selection/"
#path = "Electron/stage_37/selection/"
path = "Combined/" ############# 3. DIRECTORY IN THE ROOTFILE
#path = "MuEG/"
#path = "Electron/"
#path = "EEChannel/Cut1/"

postfix = ""
if "ML" in Dir : postfix+="_ML"
else : postfix+="_MM"
if ("Cut1" or "Cut3") in path : postfix+="_2j"
else : postfix+="_3j"
if "MuMu" in path : postfix+="_MuMu"
elif "EE" in path : postfix+= "_EE"
if "SR" in  Dir : postfix+="_SR"
else : postfix+="_SR"
#postfix = "ZbbElMM"
#postfix = "ZbbCombMM"+"subjet"
#postfix = "ZbbEMUComb"+"NoRew"+"highMET"
#postfix = nameF.replace("_NoRew_testRew.root","") ######### 4. DEFINE SOME POSTFIX DIRECTLY FROM THE INPUT ROOFILENAME TO DEFINE THE OUTPUT DIRECTORY
postfix = nameF.replace("_NotNorm_testRew.root","") ######### 4. DEFINE SOME POSTFIX DIRECTLY FROM THE INPUT ROOFILENAME TO DEFINE THE OUTPUT DIRECTORY
#postfix = "ZbbMuMM"
os.system('mkdir '+Dir+postfix)
print postfix

labelCMS = 11 #11=left, 33=right, 22=centre

doRatio = True
listofvars = [ ##### 5. CHOOSE THE VARIABLE TO PLOT

    #"boostselectionZbbM",
    #"boostselectionbestzpt",
    #"jetmetMET",
    #"boostselectiondijetM",
    #"boostselectiondijetPt",
    #"jetmetnj",
    #"jetmetMETsignificance",
    #"jetmetbjet1pt",
    #"jetmetbjet2pt",
    #"jetmetbjet1SVmass",
    #"jetmetbjet2SVmass",
    #"jetmetbjet1nVertHE",
    #"jetmetbjet2nVertHE",
    #"jetmetbjet1nVertHP",
    #"jetmetbjet2nVertHP",
    #"nSVsHE",
    #"nSVsHP",
    #"sumSVs",

    #"boostselectionbestzmass",
    "boostselectiondphiZbb",
    #"jetmetbjet1CSVdisc",
    #"boostselectiondrll",
    #"boostselectiondijetdR",
    #"jetmetbjet2CSVdisc",
    "boostselectiondrZbb",
    
    #"detab1b2",
    #"eventSelectionllbbM_inc",
    #"boostselectiondetab1l2",
    
    #"boostselectionbestzeta",
    #"boostselectionbestzphi",
    #"boostselectionZbbEta",
    #"boostselectionZbbPhi",
    #"detaZbb",
    #"dphiZjcentral",
    #"dphiZjforw",
    #"boostselectionscaldptZbj1",
    #"boostselectiondphiZbj1",
    #"boostselectiondrZbj1",
    #"boostselectionZbM",
    #"boostselectionZbPt",
    #"boostselectiondijetEta",
    #"boostselectiondijetPhi",
    #"vertexAssociationnvertices",
    #"boostselectionbestzmassMu",
    #"boostselectiondetab2l1",
    #"boostselectionZbbPt",
    #"boostselectionCentrality",
    #"boostselectionCentralityBoost",

    #"maxjeteta",
    #"minjeteta",
    #"matrixElementsbjet2etapm",
    #"matrixElementsbjet1etapm",
    #"matrixElementsbjet2pt",
    #"matrixElementsbjet1pt",

    #"jetmetjet1JPdisc",
    #"jetmetjet1PUIdMva",
    #"jetmetjet1energy",
    #"jetmetjet1etapm",
    #"jetmetjet1npf",
    #"jetmetjet1nch",
    #"jetmetjet1Chf",
    #"jetmetjet1Nhf",
    #"jetmetjet1cef",
    #"jetmetjet1nef",
    #"jetmetjet1Phf",
    #"jetmetjet1Elf",
    #"jetmetjet1Muf",
    #"jetmetjet1pt_etaorder",

    #"jetmetjet2JPdisc",
    #"jetmetjet2PUIdMva",
    #"jetmetjet2energy",
    #"jetmetjet2etapm",
    #"jetmetjet2npf",
    #"jetmetjet2nch",
    #"jetmetjet2Chf",
    #"jetmetjet2Nhf",
    #"jetmetjet2cef",
    #"jetmetjet2nef",
    #"jetmetjet2Phf",
    #"jetmetjet2Elf",
    #"jetmetjet2Muf",
    #"jetmetjet2pt_etaorder",

    #"llpt",
    #"HT",
    #"nJets",
    #"nbJets",
    #"ncJets",
    

    #"nmu",
    #"muonIso",
    #"nel",
    #"elepfIsoPUc",

    #"mu1pt",
    #"mu2OApt",
    #"mu1eta",
    #"mu2eta",
    #"drllMu",
    #"bestzmassMu",
    #"bestzptMu",
    #"el1pt",
    #"el2pt",
    #"el1eta",
    #"el2eta",
    #"drllEle",
    #"bestzmassEle",
    #"bestzptEle",

    #"bestzmass",
    #"bestzpt",
    #"dijetM",
    #"dijetPt",
    #"dijetdR",
    #"ZbbM",
    #"ZbbPt",
    #"dphiZbb",
    #"drll", 
    #"Centrality",
    #"detab1l2",
    #"detab2l1",

    #"MET",
    #"METsignificance",
    #"METphi",
    #"jetspt",
    #"jetseta",
    #"jetsnpf",
    #"jetsnch",
    #"jetsChf",
    #"jetsPtD",
    #"jetsbeta",
    #"jetsbetaStar",
    #"jetsPUIdMva",
    #"jetsPUIdWP",
    #"jet1pt",
    #"jet1eta",
    #"jet1npf",
    #"jet1nch",
    #"jet1Chf",
    #"jet1PtD",
    #"jet1beta",
    #"jet1betaStar",
    #"jet1PUIdMva",
    #"jet1PUIdWP",
    #"bjet1pt",
    #"bjet1eta", 
    #"bjet1CSVdisc", 
    #"bjet1SVmass", 
    #"bjet1npf",
    #"bjet1nch",
    #"bjet1Chf",
    #"bjet1PtD",
    #"bjet1beta",
    #"bjet1betaStar",
    #"bjet1PUIdMva",
    #"bjet1PUIdWP",
    #"bjet2pt",
    #"bjet2eta",
    #"bjet2CSVdisc", 
    #"bjet2SVmass", 
    #"bjet2npf",
    #"bjet2nch",
    #"bjet2Chf",
    #"bjet2PtD",
    #"bjet2beta",
    #"bjet2betaStar",
    #"bjet2PUIdMva",
    #"bjet2PUIdWP",
    #"stage_3/jetmetAK5PF/nb",
    #"stage_6/jetmetAK5PF/nb",
    #"nj",
    #"nb",
    #"nbP",

    #"Wgg",
    #"Wqq",
    #"Wtt",
    #"Wzz3",
    #"Wzz0",
    #"Whi3_125",
    #"Whi0_125",
    #"mlpZbbvsTT_mu_MM_N",
    #"mlpDYvsTT_2012",
    #"jetmetbjetProdCSVdisc",
    #"eventSelectiondijetM",
    #"eventSelectionbestzpt",
    #"eventSelectiondijetPt",
    #"jetmetbjet1pt",
    #"jetmetbjet2pt",
    #"eventSelectiondphiZbb",
    #"jetmetbjet1CSVdisc",
    #"jetmetbjet2CSVdisc",
    #"jetmetbjet1SVmass",
    #"jetmetbjet2SVmass",
    #"vertexAssociationnvertices",
    #"eventSelectiondijetdR",
    #"eventSelectiondrll",
    #"jetmetbjet1beta",
    #"jetmetbjet2beta",


    #"bdt",

    #"ProdNN_2j_125",
    #"ProdNN_ML_2j_125",
    #"NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520_125",
    #"NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520_125",
    #"NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520_125",#25                                                                                                                                          
    #"NN_Higgs125vsBkg_2jcomb_2_2_2_500_Nj2Mbb50_200Pt402520_125",
    #"NN_Higgs125vsBkg_2jcomb_6_6_131_Nj2Mbb80_150Pt402520_3_125",
    #"NN_Higgs125vsBkg_2jcomb_9_3_100_Nj2Mbb80_150Pt402520_8_125",
    #"NN_Higgs125vsBkg_2jcomb_9_3_100_Nj2Mbb80_150Pt402520_21_125",
    #"NN_Higgs125vsBkg_2jcomb_2_500_Nj2Mbb80_150Pt402520_1_125",#30                                                                                                                                       
    #"NN_Higgs125vsDYcomb_12_120_Nj2Mbb80_150Pt402520_2_125",
    #"NN_Higgs125vsZZcomb_2_2_1000_Nj2Mbb80_150Pt402520_125",#40                                                                                                                                          
    #"NN_Higgs125vsTTcomb_6_3_2_150_Nj2Mbb80_150Pt402520_125",
    #"NN_Higgs125vsBkg_2jcomb_4_5000_Nj2Mbb80_150Pt402520_125",#45  ###############                                                                                                      
    #"NN_Higgs125vsBkg_2jcomb_4_2_500_Nj2Mbb80_150Pt402520_125",

    #"ProdNN_3j_125",
    #"ProdNN_ML_3j_125",
    #"NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt_125",
    #"NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt_125",
    #"NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt_125",
    #"NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_9_125",
    #"NN_Higgs125vsBkg_3jcomb_9_9_300_Nj3_Mbb50_150_Pt402520_4_125",
    #"NN_Higgs125vsBkg_3jcomb_5_600_Nj3_Mbb50_150_Pt402520_1_125",
    #"NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_4_125",
    #"NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_5_125",#35                                                                                                                                  
    #"NN_Higgs125vsDYcombMbbjdRbjdRbb_12_9_6_3_210_Nj3MbbPt_125",
    #"NN_Higgs125vsZZcombMbbjdRbjdRbb_9_100_Nj3Mbb50_150_Pt_125",
    #"NN_Higgs125vsTTcombMbbjdRbjdRbb_2_2_600_Nj3Mbb50_150_Pt_125",
    #"NN_Higgs125vsBkg_3jcomb_prodCSV_5_3_1000_Nj3Mbb50_150Pt_125", ############
    #"NN_Higgs125vsBkg_3jcomb_prodCSV_3_2_1000_Nj3Mbb50_150Pt_125",

    #"NN_ZZvsDYcomb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20",
    #"NN_ZZvsTTcomb_2_1000_Nj2Mbb45_115Pt402520",
    #"NN_ZZvsBkg_2jcomb_12_50_Nj2Mbb45_115Pt402520",

    #"NN_ZZvsDYcombMbbjdRbjdRbb_12_50_Nj3Mbb15_115Pt402520",#50                                                                                                                                        
    #"NN_ZZvsTTcombMbbjdRbjdRbb_3_2_500_Nj3Mbb15_115Pt402520",
    #"NN_ZZvsBkg_3jcomb_prodCSV_9_200_Nj3Mbb15_115Pt402520",

    ]
listofcanvas = []
for var in listofvars :
    canvas = file.Get(path+var)
    name = canvas.GetName()
    if "/" in var : name = var.replace("/","").replace("_","")
    newcanvas = canvas.Clone()
    newcanvas.SetName(canvas.GetName()+name+postfix)
    newcanvas.SetTitle(canvas.GetName()+name+postfix)
    print newcanvas.GetName()
    DrawCanvas(newcanvas, labelCMS)
    if doRatio : 
        rationewcanvas = newcanvas.Clone()
        rationewcanvas.SetName(newcanvas.GetName()+"_ratio")
        rationewcanvas.SetTitle(newcanvas.GetName()+"_ratio")
        DrawCanvasWithRatio(rationewcanvas,true)
        ratio = DrawCanvasWithRatio(rationewcanvas,true)
    if not doRatio : listofcanvas.append(newcanvas)
    else : listofcanvas.append(ratio)

def save(listofcanvas=listofcanvas):
    for c in listofcanvas:
        if not c: continue
        c.Print(Dir+postfix+"/"+c.GetName()+".pdf","pdf")
        c.Print(Dir+postfix+"/"+c.GetName()+".png","png")
        c.Print(Dir+postfix+"/"+c.GetName()+".root","root")
