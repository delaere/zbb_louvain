#definitions of lists used to produce CP, skim, RDS, LHCO

#comment/uncomment samples to processe
listToProcess = [
    #"DoubleMu_DataA",
    #"DoubleMu_DataA06aug",
    #"DoubleMu_DataB",
    #"DoubleMu_DataC-v1",
    #"DoubleMu_DataC-v2",
    #"DoubleMu_DataD",

    #"SingleMu_DataA",
    #"SingleMu_DataA06aug",
    #"SingleMu_DataB",
    #"SingleMu_DataC-v1",
    #"SingleMu_DataC-v2",
    #"SingleMu_DataD",


    #"DoubleEle_DataA",
    #"DoubleEle_DataA06aug",
    #"DoubleEle_DataB",
    #"DoubleEle_DataC-v1",
    #"DoubleEle_DataC-v2",
    #"DoubleEle_DataD",
    
    #"SingleEle_DataA",
    #"SingleEle_DataA06aug",
    #"SingleEle_DataB",
    #"SingleEle_DataC-v1",
    #"SingleEle_DataC-v2",
    #"SingleEle_DataD",


    "DY_MC",
    "TT_MC",
    "ZZ_MC",

    #"ZH110_MC",
    #"ZH115_MC",
    #"ZH120_MC",
    "ZH125_MC",
    #"ZH130_MC",
    #"ZH135_MC",
    #"ZH140_MC",
    #"ZH145_MC",
    #"ZH150_MC",
    
    "DY1j_MC",
    "DY2j_MC",
    "DY3j_MC",
    "DY4j_MC",

    "DY50-70_MC",
    "DY70-100_MC",
    "DY100_MC",
    "DY180_MC",

    "Zbb_MC",

    "TT-FullLept_MC",
    "TT-SemiLept_MC",
    #"TT-Hadronic_MC",
    ]

#list of existing samples : use to generate the other lists
listsamples = [
    "DoubleMu_DataA",
    "DoubleMu_DataA06aug",
    "DoubleMu_DataB",
    "DoubleMu_DataC-v1",
    "DoubleMu_DataC-v2",
    "DoubleMu_DataD",
    "SingleMu_DataA",
    "SingleMu_DataA06aug",
    "SingleMu_DataB",
    "SingleMu_DataC-v1",
    "SingleMu_DataC-v2",
    "SingleMu_DataD",
    "DoubleEle_DataA",
    "DoubleEle_DataA06aug",
    "DoubleEle_DataB",
    "DoubleEle_DataC-v1",
    "DoubleEle_DataC-v2",
    "DoubleEle_DataD",
    "SingleEle_DataA",
    "SingleEle_DataA06aug",
    "SingleEle_DataB",
    "SingleEle_DataC-v1",
    "SingleEle_DataC-v2",
    "SingleEle_DataD",
    "DY_MC",
    "TT_MC",
    "ZZ_MC",
    "ZH110_MC",
    "ZH115_MC",
    "ZH120_MC",
    "ZH125_MC",
    "ZH130_MC",
    "ZH135_MC",
    "ZH140_MC",
    "ZH145_MC",
    "ZH150_MC",
    "DY1j_MC",
    "DY2j_MC",
    "DY3j_MC",
    "DY4j_MC",
    "DY50-70_MC",
    "DY70-100_MC",
    "DY100_MC",
    "DY180_MC",
    "Zbb_MC",
    "TT-FullLept_MC",
    "TT-SemiLept_MC",
    "TT-Hadronic_MC",
    ]

#correspondance between PAT and skim
PATtoSkim = {
    "DoubleMu_DataA"      : "DoubleMu2012A" ,
    "DoubleMu_DataA06aug" : "DoubleMu2012A06aug" ,
    "DoubleMu_DataB"      : "DoubleMu2012B" ,
    "DoubleMu_DataC-v1"   : "DoubleMu2012C-v1" ,
    "DoubleMu_DataC-v2"   : "DoubleMu2012C-v2" ,
    "DoubleMu_DataD"      : "DoubleMu2012D" ,    
    "SingleMu_DataA"      : "SingleMu2012A" ,
    "SingleMu_DataA06aug" : "SingleMu2012A06aug" ,
    "SingleMu_DataB"      : "SingleMu2012B" ,
    "SingleMu_DataC-v1"   : "SingleMu2012C-v1" ,
    "SingleMu_DataC-v2"   : "SingleMu2012C-v2" ,
    "SingleMu_DataD"      : "SingleMu2012D" ,
    "DoubleEle_DataA"     : "DoubleEle2012A" ,
    "DoubleEle_DataA06aug": "DoubleEle2012A06aug" ,
    "DoubleEle_DataB"     : "DoubleEle2012B" ,
    "DoubleEle_DataC-v1"  : "DoubleEle2012C-v1" ,
    "DoubleEle_DataC-v2"  : "DoubleEle2012C-v2" ,
    "DoubleEle_DataD"     : "DoubleEle2012D" ,    
    "SingleEle_DataA"     : "SingleEle2012A" ,
    "SingleEle_DataA06aug": "SingleEle2012A06aug" ,
    "SingleEle_DataB"     : "SingleEle2012B" ,
    "SingleEle_DataC-v1"  : "SingleEle2012C-v1" ,
    "SingleEle_DataC-v2"  : "SingleEle2012C-v2" ,
    "SingleEle_DataD"     : "SingleEle2012D" ,
    "DY_MC"               : "Summer12_DYjets_S10" ,
    "TT_MC"               : "Summer12_TTjets_S10" ,
    "ZZ_MC"               : "Summer12_ZZ_S10" ,
    "ZH110_MC"            : "Summer12_ZH110_S10" ,
    "ZH115_MC"            : "Summer12_ZH115_S10" ,
    "ZH120_MC"            : "Summer12_ZH120_S10" ,
    "ZH125_MC"            : "Summer12_ZH125_S10" ,
    "ZH130_MC"            : "Summer12_ZH130_S10" ,
    "ZH135_MC"            : "Summer12_ZH135_S10" ,
    "ZH140_MC"            : "Summer12_ZH140_S10" ,
    "ZH145_MC"            : "Summer12_ZH145_S10" ,
    "ZH150_MC"            : "Summer12_ZH150_S10" ,
    "DY1j_MC"             : "Summer12_DY1jets_S10" ,
    "DY2j_MC"             : "Summer12_DY2jets_S10" ,
    "DY3j_MC"             : "Summer12_DY3jets_S10" ,
    "DY4j_MC"             : "Summer12_DY4jets_S10" ,
    "DY50-70_MC"          : "Summer12_DYjets_Pt50to70_S10" ,
    "DY70-100_MC"         : "Summer12_DYjets_Pt70to100_S10" ,
    "DY100_MC"            : "Summer12_DYjets_Pt100_S10" ,
    "DY180_MC"            : "Summer12_DYjets_Pt180_S10" ,
    "Zbb_MC"              : "Summer12_Zbb_S10" ,
    "TT-FullLept_MC"      : "Summer12_TTbarFullLept_S10" , 
    "TT-SemiLept_MC"      : "Summer12_TTbarSemiLept_S10" ,
    "TT-Hadronic_MC"      : "Summer12_TTbarHadronic_S10" ,
    }

#use to produce the skims and access to the PAT, skim
dirPAT = "/nfs/user/llbb/Pat_8TeV_537/"
#dirPAT = "/storage/data/cms/store/user/acaudron/Dec2012production8TeV/"
#dirSkim = "/nfs/user/acaudron/skim537/"
dirSkim = "/nfs/user/acaudron/skim537/"
pathPAT = {}
pathSkim = {}

#list of El and/or Mu samples to processed/used for RDS, LHCO ...
listToProcessEMu = []
listsamplesEMu = []

#use to produce RDS and LHCO and to acces to RDS, LHCO
#dirRDS = "/nfs/user/acaudron/RDS537/"
#dirRDS = "/nfs/user/acaudron/RDS53X_update19fb/"
dirRDS = "/nfs/user/acaudron/RDS537/"
dirRDS_PUup = "/nfs/user/acaudron/RDS537_PUup/"
dirRDS_PUdown = "/nfs/user/acaudron/RDS537_PUdown/"
dirLHCO = "/nfs/user/acaudron/LHCO537/"
pathSkimEMu = {}
pathRDS = {}
pathLHCO = {}
muChannel = {}
checkTrigger = {}

#use to produce/access to Tree2, MergedTree and MergedRDS
dirTree2 = "/nfs/user/acaudron/Tree2_537/"
pathTree2 = {}
pathMergedTree = {}
pathMergedRDS = {}

#loop to generate lists defined above
for sample in listsamples :
    pathPAT[sample]   = dirPAT+PATtoSkim[sample]+"/"
    pathSkim[sample]  = dirSkim+sample+"/"
    if "Data" in sample :
        if sample in listToProcess : listToProcessEMu.append(sample)
        listsamplesEMu.append(sample)
        checkTrigger[sample]=True
        pathSkimEMu[sample]  = dirSkim+sample+"/"
        pathRDS[sample]   = dirRDS+"File_rds_zbb_"+sample+".root"
        pathLHCO[sample]  = dirLHCO+"outCMStoLHCO"+sample+"V1_0.root"
        pathTree2[sample] = dirTree2+"ME_zbb_" +sample+".root"
        pathMergedTree[sample] = dirTree2+"Tree_rdsME_" +sample+".root"
        pathMergedRDS[sample] = dirTree2+"RDS_rdsME_" +sample+".root"
        if "Mu" in sample : muChannel[sample]=True
        else : muChannel[sample]=False
    else :
        sampleEle=sample.replace("MC","")+"El_MC"
        if sample in listToProcess : listToProcessEMu.append(sampleEle)
        listsamplesEMu.append(sampleEle)
        checkTrigger[sampleEle]=False
        muChannel[sampleEle]=False
        pathSkimEMu[sampleEle] = dirSkim+sample+"/"
        pathRDS[sampleEle]     = dirRDS+"File_rds_zbb_"+sampleEle+".root"
        pathLHCO[sampleEle]    = dirLHCO+"outCMStoLHCO"+sampleEle+"V1_0.root"
        pathTree2[sampleEle] = dirTree2+"ME_zbb_" +sampleEle+".root"
        pathMergedTree[sampleEle] = dirTree2+"Tree_rdsME_" +sampleEle+".root"
        pathMergedRDS[sampleEle] = dirTree2+"RDS_rdsME_" +sampleEle+".root"
        
        sampleMu=sample.replace("MC","")+"Mu_MC"
        if sample in listToProcess : listToProcessEMu.append(sampleMu)
        listsamplesEMu.append(sampleMu)
        checkTrigger[sampleMu]=False
        muChannel[sampleMu]=True
        pathSkimEMu[sampleMu] = dirSkim+sample+"/"
        pathRDS[sampleMu]     = dirRDS+"File_rds_zbb_"+sampleMu+".root"
        pathLHCO[sampleMu]    = dirLHCO+"outCMStoLHCO"+sampleMu+"V1_0.root"
        pathTree2[sampleMu] = dirTree2+"ME_zbb_" +sampleMu+".root"
        pathMergedTree[sampleMu] = dirTree2+"Tree_rdsME_" +sampleMu+".root"
        pathMergedRDS[sampleMu] = dirTree2+"RDS_rdsME_" +sampleMu+".root"

def printList(listOfObjetcs=[listsamplesEMu,muChannel]):
    print listOfObjetcs
