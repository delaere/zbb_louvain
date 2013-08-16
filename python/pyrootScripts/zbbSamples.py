
# directories used to produce the skims etc.
dirPAT = "/nfs/user/llbb/Pat_8TeV_537/"
dirSkim = "/nfs/user/acaudron/skim537/"
dirTree2 = "/nfs/user/acaudron/Tree2_537/"
dirRDS = "/nfs/user/acaudron/RDS537/"
dirRDS_PUup = "/nfs/user/acaudron/RDS537_PUup/"
dirRDS_PUdown = "/nfs/user/acaudron/RDS537_PUdown/"
dirLHCO = "/nfs/user/acaudron/LHCO537/"

######################################################################
# dictionary giving a label to PATtuples in the SAMADhi database
# samples are refered to by name instead of id for clarity.
######################################################################

#TODO: fill the list
samples = {
   "label" : ("PAT","sampleName"),
   }

#TODO: fill the lists
dataSamples2011e = []
dataSamples2011m = []
dataSamples2012e = []
dataSamples2012m = []


#TODO: fill the lists
sigMCsampleList = ["ZH125"]#,"ZH120","ZH115","ZH130","ZH135"]#,"ZA"]
bkgMCsampleList = []
MCsampleList    = sigMCsampleList+bkgMCsampleList

######################################################################
# Functions to easily access samples, luminosity, etc.
######################################################################

def getSample(type=None,name=None,label=None):
  """Method to get the sample by type and name or by label (using the samples dictionary)"""
  # check arguments
  if label is None:
    if (type is None) or (name is None):
      raise ValueError("getSample is used either with (type,name) or with label argument")
  else:
    if (type is not None) or (name is not None):
      raise ValueError("getSample is used either with (type,name) or with label argument")
    else:
      type = samples[label][0]
      name = samples[label][1]
  # query the db to get the sample.
  dbstore = SAMADhi.DbStore()
  sample  = dbstore.find(SAMADhi.Sample,(SAMADhi.Sample.sampletype==type) & (SAMADhi.Sample.name==name))
  # return the unique matching sample. This will throw an exception if it does not exist.
  return sample.one()

# method to get lumi for a given data/mc sample: getSample(type,name).getLuminosity()
# this will return an exception if the sample does not exist, and None if the lumi is not stored / cannot be computed

def getDataLuminosity(channel, year, type="PAT"):
  """Method to get the total luminosity in data for a given year + channel. Uses the lists defined previously."""
  dataSamples = { "2011electrons": dataSamples2011e,
                  "2011muons": dataSamples2011m,
                  "2012electrons": dataSamples2012e,
                  "2012muons": dataSamples2012m }.get("%d%s"%(year,channel))
  lumi = 0.
  for sample in dataSamples:
    lumi += getSample(label=sample)
  return lumi

######################################################################
######################################################################

## for bookkeeping... just a list of what was used so far
#sampleList = [
#    "DATA",
#    "TT",
#    "TT-FullLept",
#    "ZZ",
#    "DY",
#    "DY50-70",
#    "DY70-100",
#    "DY100",
#    "DY180",
#    "DY1j",
#    "DY2j",
#    "DY3j",
#    "DY4j",
#    "ZH125",
#    "ZH120",
#    "ZH115",
#    "ZH130",
#    "ZH135"]
#listToProcess = [
#    "DY_MC",
#    "TT_MC",
#    "ZZ_MC",
#    "ZH125_MC",
#    "DY1j_MC",
#    "DY2j_MC",
#    "DY3j_MC",
#    "DY4j_MC",
#    "DY50-70_MC",
#    "DY70-100_MC",
#    "DY100_MC",
#    "DY180_MC",
#    "Zbb_MC",
#    "TT-FullLept_MC",
#    "TT-SemiLept_MC",
#    ]
#listsamples = [
#    "DoubleMu_DataA",
#    "DoubleMu_DataA06aug",
#    "DoubleMu_DataB",
#    "DoubleMu_DataC-v1",
#    "DoubleMu_DataC-v2",
#    "DoubleMu_DataD",
#    "SingleMu_DataA",
#    "SingleMu_DataA06aug",
#    "SingleMu_DataB",
#    "SingleMu_DataC-v1",
#    "SingleMu_DataC-v2",
#    "SingleMu_DataD",
#    "DoubleEle_DataA",
#    "DoubleEle_DataA06aug",
#    "DoubleEle_DataB",
#    "DoubleEle_DataC-v1",
#    "DoubleEle_DataC-v2",
#    "DoubleEle_DataD",
#    "SingleEle_DataA",
#    "SingleEle_DataA06aug",
#    "SingleEle_DataB",
#    "SingleEle_DataC-v1",
#    "SingleEle_DataC-v2",
#    "SingleEle_DataD",
#    "DY_MC",
#    "TT_MC",
#    "ZZ_MC",
#    "ZH110_MC",
#    "ZH115_MC",
#    "ZH120_MC",
#    "ZH125_MC",
#    "ZH130_MC",
#    "ZH135_MC",
#    "ZH140_MC",
#    "ZH145_MC",
#    "ZH150_MC",
#    "DY1j_MC",
#    "DY2j_MC",
#    "DY3j_MC",
#    "DY4j_MC",
#    "DY50-70_MC",
#    "DY70-100_MC",
#    "DY100_MC",
#    "DY180_MC",
#    "Zbb_MC",
#    "TT-FullLept_MC",
#    "TT-SemiLept_MC",
#    "TT-Hadronic_MC",
#    ]
#
##this splits the list in two: e and mu but is based on an arbitrary naming convention -> weak
#listToProcessEMu = []
#listsamplesEMu = []
#muChannel = {}
#
## this is basically a flag "isData". Can't we know that by another way?
#checkTrigger = {} 
#
##loop to generate lists defined above. Uses listsamples and listToProcess
#for sample in listsamples :
#    if "Data" in sample :
#        if sample in listToProcess : listToProcessEMu.append(sample)
#        listsamplesEMu.append(sample)
#        checkTrigger[sample]=True
#        if "Mu" in sample : muChannel[sample]=True
#        else : muChannel[sample]=False
#    else :
#        sampleEle=sample.replace("MC","")+"El_MC"
#        if sample in listToProcess : listToProcessEMu.append(sampleEle)
#        listsamplesEMu.append(sampleEle)
#        checkTrigger[sampleEle]=False
#        muChannel[sampleEle]=False
#        sampleMu=sample.replace("MC","")+"Mu_MC"
#        if sample in listToProcess : listToProcessEMu.append(sampleMu)
#        listsamplesEMu.append(sampleMu)
#        checkTrigger[sampleMu]=False
#        muChannel[sampleMu]=True
#
