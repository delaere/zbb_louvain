import SAMADhi.SAMADhi as SAMADhi
import operator

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

channels   = ["Mu","El"]
types      = ["PAT","RDS", "MERDS"]

#TODO: fill the list
samples = {
   # PAT-tuples
   ("DoubleMu_A","Mu","PAT")  : "sampleName", 
   ("DoubleEle_A","El","PAT") : "sampleName", 
   ("DoubleMu_B","Mu","PAT")  : "sampleName", 
   ("DoubleEle_B","El","PAT") : "sampleName", 
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
   ("TT","","PAT")      : "sampleName", 
   ("Zbb","","PAT")     : "sampleName", 
   ("Zbx","","PAT")     : "sampleName", 
   ("Zxx","","PAT")     : "sampleName", 
   ("ZZ","","PAT")      : "sampleName", 
   ("ZH115","","PAT")   : "sampleName", 
   ("ZH120","","PAT")   : "sampleName", 
   ("ZH125","","PAT")   : "sampleName", 
   ("ZH130","","PAT")   : "sampleName", 
   ("ZH135","","PAT")   : "sampleName", 
#    "TT-FullLept",
#    "TT-SemiLept_MC",
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
   # RDS
   ("DATA","Mu","RDS")  : "sampleName", 
   ("DATA","El","RDS")  : "sampleName", 
   ("TT","El","RDS")    : "sampleName", 
   ("Zbb","El","RDS")   : "sampleName", 
   ("Zbx","El","RDS")   : "sampleName", 
   ("Zxx","El","RDS")   : "sampleName", 
   ("ZZ","El","RDS")    : "sampleName", 
   ("TT","Mu","RDS")    : "sampleName", 
   ("Zbb","Mu","RDS")   : "sampleName", 
   ("Zbx","Mu","RDS")   : "sampleName", 
   ("Zxx","Mu","RDS")   : "sampleName", 
   ("ZZ","Mu","RDS")    : "sampleName", 
   ("ZH115","El","RDS") : "sampleName", 
   ("ZH115","Mu","RDS") : "sampleName", 
   ("ZH120","El","RDS") : "sampleName", 
   ("ZH120","Mu","RDS") : "sampleName", 
   ("ZH125","El","RDS") : "sampleName", 
   ("ZH125","Mu","RDS") : "sampleName", 
   ("ZH130","El","RDS") : "sampleName", 
   ("ZH130","Mu","RDS") : "sampleName", 
   ("ZH135","El","RDS") : "sampleName", 
   ("ZH135","Mu","RDS") : "sampleName", 
 }

# statis lists
sigMCsamples = ["ZH125"]#,"ZH120","ZH115","ZH130","ZH135"]#,"ZA"]
bkgMCsamples = ["Zbb","Zbx","Zxx","TT","ZZ"]
datasamples  = ["DoubleMu_A","DoubleEle_A","DoubleMu_B","DoubleEle_B"]

# dynamic lists
MCsamples    = sigMCsamples+bkgMCsamples
totsamples   = MCsamples+datasamples
allSamples   = list(set(map(operator.itemgetter(0),samples.keys())))
samples_RDS  = list(set(map(operator.itemgetter(0),filter(lambda k:k[2]=='RDS',samples.keys()))))
samples_PAT  = list(set(map(operator.itemgetter(0),filter(lambda k:k[2]=='PAT',samples.keys()))))

# check that the list of channels is complete
# check that the lists are only made of konwn samples
# check that all samples exist and are of the proper type
assert set(map(operator.itemgetter(1),samples.keys()))==set(channels+[""])
assert set(map(operator.itemgetter(2),samples.keys()))==set(types)
assert reduce(operator.and_,map(lambda x: x in allSamples, sigMCsamples), True) 
assert reduce(operator.and_,map(lambda x: x in allSamples, bkgMCsamples), True) 
assert reduce(operator.and_,map(lambda x: x in allSamples, datasamples ), True)
def checkSamples():
  dbstore = SAMADhi.DbStore()
  for key, name in samples.iteritems():
    type = key[2]
    sample = dbstore.find(SAMADhi.Sample,(SAMADhi.Sample.name==unicode(name)))
    assert sample.count()==1
  return True
assert checkSamples()

######################################################################
# Functions to easily access samples, luminosity, etc.
######################################################################

def getSample(label=None,channel="",type=None,name=None):
  """Method to get the sample by type and name or by label (using the samples dictionary)"""
  # check arguments
  if (label is not None) or (type is not None):
    if (label is None) or (type is None) or (name is not None):
      raise ValueError("getSample is used either with (label,channel,type) or with name argument")
  if (label is None) and (type is None) and (name is None):
    raise ValueError("getSample is used either with (label,channel,type) or with name argument")
  # find name if not set
  if name is None:
    if (label,channel,type) in samples.keys():
      name = samples[(label,channel,type)]
    else:
      return None
  # query the db to get the sample.
  dbstore = SAMADhi.DbStore()
  sample  = dbstore.find(SAMADhi.Sample,SAMADhi.Sample.name==unicode(name))
  # return the unique matching sample. This will throw an exception if it does not exist.
  return sample.one()

# method to get lumi for a given data/mc sample: getSample(label,channel,type).getLuminosity()
# this will return an exception if the sample does not exist, and None if the lumi is not stored / cannot be computed

def getDataLuminosity(channel, type="PAT"):
  """Method to get the total luminosity in data for a given channel."""
  assert channel in channels
  lumi = 0.
  for label in datasamples:
    sample = getSample(label,channel,type)
    if sample is not None: lumi += sample.getLuminosity()
  return lumi

def filterSamples(sampleList, processList, channelList, typeList):
  """Filter the samples to contain only the proper combinations of process+channel+type"""
  if processList is None:
    processList = allSamples
  if channelList is None: 
    channelList = channels + [""]
  if typeList is None:
    typeList = types
  spl = {}
  for samplekey in [(a,b,c) for a in processList for b in channelList for c in typeList] :
    if samplekey in sampleList:
      spl = {samplekey: sampleList[samplekey]}
  return spl
  #return { samplekey: sampleList[samplekey] for samplekey in [(a,b,c) for a in processList for b in channelList for c in typeList] if samplekey in sampleList }  #from python 2.7 only

def getSamples(processList=None, channelList=None, typeList=None):
  """Method to get a list of SAMADhi samples from a dictionary of samples"""
  output = []
  dbstore = SAMADhi.DbStore()
  theSamples = filterSamples(samples,processList, channelList, typeList)
  for key,name in samples.iteritems():
    output += dbstore.find(SAMADhi.Sample,SAMADhi.Sample.name==unicode(name)).one()
  return output

