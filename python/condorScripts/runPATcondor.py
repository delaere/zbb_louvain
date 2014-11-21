#local
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ()

options.register ('option',
                  "Condor", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "Condor")

options.register ('slice',
                  0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Slice of sample")

options.register ('sample',
                  "DY", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "Sample name")


options.parseArguments()
slice = options.slice
sampleName = options.sample
print "slice number", slice
print "sample is ", sampleName

nevents = -1

if sampleName=="DY":
    runOnMC = True
    path1 = "/storage/data/cms/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/"
    path2 = "/storage/data/cms/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0001/"
    path3 = "/storage/data/cms/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0002/"
    pathList = [path1,path2,path3]
    njobs=1500
    
if "ZA" in sampleName:
    runOnMC = True
    path = "/home/fynu/amertens/storage/CMS_Prod/2HDM/THDM_"+sampleName.replace("ZA_","")+"_RECO/"
    pathList = [path]
    njobs=250

if sampleName=="ZA_575_142":
    runOnMC = True
    path = "/home/fynu/amertens/storage/CMS_Prod/2HDM/THDM_575_142_RECO/"
    pathList = [path]
    njobs=250

if sampleName=="ZA_350_15":
    runOnMC = True
    path = "/nfs/user/quertenmont/Higgs/i2HDM_Samples/14_04_22/llbb_350_15_RECO/"
    pathList = [path]
    njobs=250

if sampleName=="ZA_350_30":
    runOnMC = True
    path = "/nfs/user/quertenmont/Higgs/i2HDM_Samples/14_04_22/llbb_350_30_RECO/"
    pathList = [path]
    njobs=250

if sampleName=="ZA_350_70":
    runOnMC = True
    path = "/nfs/user/quertenmont/Higgs/i2HDM_Samples/14_04_22/llbb_350_70_RECO/"
    pathList = [path]
    njobs=250

if sampleName=="TT":
    runOnMC = True
    path = "/storage/data/cms/store/mc/Summer12_DR53X/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/"
    pathList = [path]
    njobs=722

if sampleName=="DataMuD":
    runOnMC = False
    path = "/storage/data/cms/store/data/Run2012D/DoubleMuParked/AOD/22Jan2013-v1/30001/"
    pathList = [path]
    njobs=300

if sampleName=="DataElD":
    runOnMC = False
    path = "/storage/data/cms/store/data/Run2012D/DoubleElectron/AOD/22Jan2013-v1/10001/"
    pathList = [path]
    njobs=300
    
    
import os

files=[]
for path in pathList:
    pathname = "file:"+path
    dirList=os.listdir(path)
    for fname in dirList:
        files.append(pathname+fname)
        
if slice: files = files[len(files)*(slice-1)/njobs:len(files)*slice/njobs]
print "input files are", files
print ""

if slice : out_fileName = 'pat53_'+str(slice)+'.root'
else     : out_fileName ='test.root'
print "output file is", out_fileName
print ""
#end local

                                                                        
