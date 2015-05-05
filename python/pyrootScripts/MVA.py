from ROOT import *
from llbbOptions import *

class options_(options_):
    samples = [
        "DYjets",
        "TTFullLept",
        "TTSemiLept",
        "ZZ",
        "WZ",
        "WW",
        "Wt",
        "Wtbar",
        "ZH125",
        "ZA_262_99",
        ]

    signal = "ZA_262_99"
    
    path = "/nfs/user/acaudron/ControlPlots/cp5314p1/AllRDS/Nominal/RDS_NAME/NAME_Summer12_final_skimed_zmet.root"

    vars = [
        'max(boostselectionbestzptMu,boostselectionbestzptEle)',
        'max(boostselectiondrllMu,boostselectiondrllEle)',
        'boostselectiondijetPt',
        'boostselectiondijetdR',
        'boostselectionZbbPt',
        'boostselectiondphiZbb',
        'abs(boostselectionCosThetab1)',
        'jetmetMET'
        ]

def main():
    op = options_()
    files = {}
    trees = {}
    for sam in op.samples:
        files[sam] = TFile(op.path.replace("NAME",sam))
        trees[sam] = files[sam].Get("rds_zbb")
    fmva = TFile("testMVA.root","RECREATE")
    tmva = TMVA.Factory("2HDM",fmva,"!V")
    for v in op.vars : tmva.AddVariable(v,'F')
    for sam in op.samples:
        if sam==op.signal : continue
        tmva.AddBackgroundTree(trees[sam], lumi["DATA"]/lumi[sam])
    tmva.AddSignalTree(trees[op.signal], lumi["DATA"]/lumi[op.signal])
    tmva.PrepareTrainingAndTestTree(TCut("("+op.stages["Mu"]+")||("+op.stages["El"]+")"), "nTrain_Signal=0:nTest_Signal=0:nTrain_Background=0:nTest_Background=0:SplitMode=Random:NormMode=EqualNumEvents:!V")
    tmva.SetWeightExpression("1."+op.rewForm["Zbb"]["Mu"]) #Mu and El are the same
    #tmva.BookMethod(TMVA.Types.kBDT, "myBDT", "!V:BoostType=AdaBoost:NTrees=500:nEventsMin=50:nCuts=20:MaxDepth=10")
    tmva.BookMethod(TMVA.Types.kMLP, "MLP", "!H:!V:VarTransform=N:HiddenLayers=N-1:NCycles=750:TrainingMethod=BFGS")
    tmva.TrainAllMethods()
    tmva.TestAllMethods()
    tmva.EvaluateAllMethods()
    #reader = TMVA.Reader("!Color:!Silent")
    return

main()
