import ROOT
import string
import intervalmap
import sys
from VertexAssociation import zVertex, isfromVertex, isFromVertex_SingleLepton
from JetCorrectionUncertainty import JetCorrectionUncertaintyProxy
from MonteCarloSelection import hadronFlavour
from math import sqrt
from operator import attrgetter

JECuncertaintyProxy = JetCorrectionUncertaintyProxy()

# here we declare our triggers
class ourTriggers: pass

ourtriggers = ourTriggers()
# muon triggers per runrange
ourtriggers.murunMap = intervalmap.intervalmap()
ourtriggers.murunMap[132440:139981] = ("HLT_Mu3",)
ourtriggers.murunMap[140058:140402] = ("HLT_Mu5",)
ourtriggers.murunMap[141956:144115] = ("HLT_Mu7",)
ourtriggers.murunMap[146428:147117] = ("HLT_Mu9",)
ourtriggers.murunMap[147146:148103] = ("HLT_Mu11",)
ourtriggers.murunMap[148783:149443] = ("HLT_Mu15_v1",)
### data 2011
ourtriggers.murunMap[160410:163269] = ("HLT_DoubleMu6_v1",)
ourtriggers.murunMap[163269:165121] = ("HLT_DoubleMu7_v2",)
ourtriggers.murunMap[165121:167044] = ("HLT_Mu13_Mu8_v2","HLT_Mu13_Mu8_v3",)
ourtriggers.murunMap[167078:170249] = ("HLT_Mu13_Mu8_v4",)
ourtriggers.murunMap[170249:173199] = ("HLT_Mu13_Mu8_v6",)
ourtriggers.murunMap[173236:178381] = ("HLT_Mu13_Mu8_v7",)
ourtriggers.murunMap[178420:179890] = ("HLT_Mu17_Mu8_v10",)#"HLT_Mu17_tkMu8_v3")
ourtriggers.murunMap[179959:180253] = ("HLT_Mu17_Mu8_v11",)#"HLT_Mu17_tkMu8_v4")
### data 2012
ourtriggers.murunMap[190455:] = ("HLT_Mu17_Mu8_v16",
                                 "HLT_Mu17_Mu8_v17",
                                 "HLT_Mu17_Mu8_v18",
                                 "HLT_Mu17_Mu8_v19",
                                 "HLT_Mu17_Mu8_v21",
                                 "HLT_Mu17_Mu8_v22",
                                 "HLT_Mu17_TkMu8_v9",
                                 "HLT_Mu17_TkMu8_v10",
                                 "HLT_Mu17_TkMu8_v11",
                                 "HLT_Mu17_TkMu8_v12",
                                 "HLT_Mu17_TkMu8_v13",
                                 "HLT_Mu17_TkMu8_v14",
                                 #"HLT_IsoMu24_v15",
                                 #"HLT_IsoMu24_v16",
                                 #"HLT_IsoMu24_v17",
                                 )

ourtriggers.muSinglerunMap = intervalmap.intervalmap()
ourtriggers.muSinglerunMap[190455:] = ("HLT_IsoMu24_v15",
                                       "HLT_IsoMu24_v16",
                                       "HLT_IsoMu24_v17",
                                       )

# electron triggers per runrange
ourtriggers.elrunMap = intervalmap.intervalmap()
ourtriggers.elrunMap[132440:137029] = ("HLT_Photon10_L1R",)
ourtriggers.elrunMap[138564:140402] = ("HLT_Photon15_Cleaned_L1R",)
ourtriggers.elrunMap[141956:144115] = ("HLT_Ele15_SW_CaloEleId_L1R",)
ourtriggers.elrunMap[146428:147117] = ("HLT_Ele17_SW_CaloEleId_L1R",)
ourtriggers.elrunMap[147146:148103] = ("HLT_Ele17_SW_TightEleId_L1R",)
ourtriggers.elrunMap[148783:149064] = ("HLT_Ele22_SW_TighterCaloIdIsol_L1R_v1",)
ourtriggers.elrunMap[149181:149443] = ("HLT_Ele22_SW_TighterCaloIdIsol_L1R_v2",)
### data 2011
ourtriggers.elrunMap[160410:161217] = ("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1",)
ourtriggers.elrunMap[161217:163269] = ("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v2",)
ourtriggers.elrunMap[163269:165121] = ("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v3",)
ourtriggers.elrunMap[165121:165970] = ("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v4",)
ourtriggers.elrunMap[165970:167039] = ("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v5",)
ourtriggers.elrunMap[167039:170249] = ("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v6",)
ourtriggers.elrunMap[170249:170760] = ("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6",)
ourtriggers.elrunMap[170826:173199] = ("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v7",)
ourtriggers.elrunMap[173236:178381] = ("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v8",)
ourtriggers.elrunMap[178420:179890] = ("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9",)
ourtriggers.elrunMap[179959:180253] = ("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v10",)
### data 2012
ourtriggers.elrunMap[190455:] = ("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15",
                                 "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v16",
                                 "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v17",
                                 "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v18",
                                 "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19",
                                 )

#e-mu triggers (only 2012. 2011 e-mu triggers to be implemented)
#Main ones
ourtriggers.emurunMap = intervalmap.intervalmap()
ourtriggers.emurunMap[190455:] = ("HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v4",
                                  "HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v5",
                                  "HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6",
                                  "HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v7",
                                  "HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v8",
                                  "HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9",
                                  "HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v4",
                                  "HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v5",
                                  "HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6",
                                  "HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v7",
                                  "HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v8",
                                  "HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9",
				  )

#higher thresholds (probably not add much efficiency, maybe for the future)
#ourtriggers.emurunMap[190456:190738] = ("HLT_Mu30_Ele30_CaloIdL_v3",)
#ourtriggers.emurunMap[190782:191411] = ("HLT_Mu30_Ele30_CaloIdL_v4",)
#ourtriggers.emurunMap[191691:193621] = ("HLT_Mu30_Ele30_CaloIdL_v5",)
#ourtriggers.emurunMap[193834:196531] = ("HLT_Mu30_Ele30_CaloIdL_v6",)
#ourtriggers.emurunMap[198022:199608] = ("HLT_Mu30_Ele30_CaloIdL_v7",)
#ourtriggers.emurunMap[199698:209151] = ("HLT_Mu30_Ele30_CaloIdL_v8",)

#3leptons (maybe for the future)
#ourtriggers.emurunMap[190456:190738] = ("HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v12",)
#ourtriggers.emurunMap[190782:191411] = ("HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v13",)
#ourtriggers.emurunMap[191691:196531] = ("HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v14",)
#ourtriggers.emurunMap[198022:199608] = ("HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v15",)
#ourtriggers.emurunMap[199698:209151] = ("HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16",)
#
#ourtriggers.emurunMap[190456:190738] = ("HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v1",)
#ourtriggers.emurunMap[190782:191411] = ("HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v2",)
#ourtriggers.emurunMap[191691:196531] = ("HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v3",)
#ourtriggers.emurunMap[198022:199608] = ("HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v4",)
#ourtriggers.emurunMap[199698:209151] = ("HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5",)
#
#ourtriggers.emurunMap[190456:190738] = ("HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v3",)
#ourtriggers.emurunMap[190782:191411] = ("HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v4",)
#ourtriggers.emurunMap[191691:196531] = ("HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v5",)
#ourtriggers.emurunMap[198022:199608] = ("HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v6",)
#ourtriggers.emurunMap[199698:209151] = ("HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7",)
#
#ourtriggers.emurunMap[190456:190738] = ("HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v3",)
#ourtriggers.emurunMap[190782:191411] = ("HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v4",)
#ourtriggers.emurunMap[191691:196531] = ("HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v5",)
#ourtriggers.emurunMap[198022:199608] = ("HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v6",)
#ourtriggers.emurunMap[199698:209151] = ("HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7",)


# merged lists of triggers
ourtriggers.mutriggers  = list(set([item for sublist in [i for i in ourtriggers.murunMap.values()] for item in sublist]))
ourtriggers.eltriggers  = list(set([item for sublist in [i for i in ourtriggers.elrunMap.values()] for item in sublist]))
ourtriggers.emutriggers = list(set([item for sublist in [i for i in ourtriggers.emurunMap.values()] for item in sublist]))
ourtriggers.triggers   = list(set(ourtriggers.mutriggers) | set(ourtriggers.eltriggers) | set(ourtriggers.emutriggers))
ourtriggers.SingleMutriggers = list(set([item for sublist in [i for i in ourtriggers.muSinglerunMap.values()] for item in sublist]))

def electron_iswrongPS(electron, runNumber, lumi_section):
  if runNumber==171050 and (lumi_section==47 or lumi_section==92):
    return True
  if runNumber==171156 and (lumi_section==42 or lumi_section==211):
    return True
  if runNumber==171219 and (lumi_section==48 or lumi_section==163):
    return True
  if runNumber==171274 and (lumi_section==88 or lumi_section==148):
    return True
  if runNumber==171282 and (lumi_section==1 or lumi_section==172):
    return True
  if runNumber==171315 and (lumi_section==53 or lumi_section==226):
    return True
  if runNumber==171369 and (lumi_section==42 or lumi_section==162):
    return True
  if runNumber==171446 and (lumi_section==58 or lumi_section==374):
    return True
  if runNumber==171484 and (lumi_section==61 or lumi_section==358):
    return True
  if runNumber==171578 and (lumi_section==47 or lumi_section==347):
    return True
  else : return False

def selectedTriggers(triggerInfo):
  """Returns a list with the decision of each trigger considered in the analysis"""
  if triggerInfo is None:
    return []
  paths = map(lambda trigger: triggerInfo.path(trigger),ourtriggers.triggers)
  def isFired(path):
    if not not path :
      return path.wasAccept()
    else:
      return False
  return map(lambda path:isFired(path),paths)

def isTriggerOK(event,muChannel=True,eleChannel=True,perRun=True):
  """Checks if the proper trigger is passed"""
  # simple case: mu trigger for mu channel (1), ele trigger for ele channel (0)
  # more complex case: different trigger for various run ranges (lowest unprescaled)
  # trigger info
  triggerInfo = event.triggerInfo
  runNumber = event.run()
  # best Z candidate
  if muChannel and eleChannel:
    bestZcandidate = event.bestZcandidate
  elif muChannel:
    bestZcandidate = event.bestZmumuCandidate
  elif eleChannel:
    bestZcandidate = event.bestZelelCandidate
  if triggerInfo is None:
    return True
  paths = triggerInfo.acceptedPaths()
  #for i in range(paths.size()) : print paths[i].name()
  pathnames = map(lambda i: paths[i].name(),range(paths.size()))
  if not perRun:
    if muChannel and not eleChannel:
      intersect = set(pathnames) & set(ourtriggers.mutriggers)
    elif not muChannel and eleChannel:
      intersect = set(pathnames) & set(ourtriggers.eltriggers)
    elif muChannel and eleChannel:
      intersect = set(pathnames) & set(ourtriggers.emutriggers)
  else:
    if muChannel and not eleChannel:
      if ourtriggers.murunMap[runNumber] is None:
        print "muon unexpected runNumber : " , runNumber
        intersect = set()
      else:
        intersect = set(pathnames) & set(ourtriggers.murunMap[runNumber])
    elif not muChannel and eleChannel:
      if ourtriggers.elrunMap[runNumber] is None:
        print "electron unexpected runNumber : " , runNumber
        intersect = set()
      else:
        intersect = set(pathnames) & set(ourtriggers.elrunMap[runNumber])
    elif muChannel and eleChannel:
      if ourtriggers.emurunMap[runNumber] is None:
        print "e-mu unexpected runNumber : " , runNumber
        intersect = set()
      else:
        intersect = set(pathnames) & set(ourtriggers.emurunMap[runNumber])


  outcome = len(intersect)>0
  return (outcome and isTriggerMatchZcandidate(bestZcandidate,runNumber,event.lumi()))

def isTriggerIncOK(event,perRun=True):
  """Checks if the proper trigger is passed"""
  # simple case: mu trigger for mu channel (1), ele trigger for ele channel (0)
  # more complex case: different trigger for various run ranges (lowest unprescaled)
  # trigger info
  triggerInfo = event.triggerInfo
  runNumber = event.run()
  l1= None
  l2= None
  bestDileptcandidate = event.bestDiLeptCandidate
  if bestDileptcandidate is not None:
    l1=bestDileptcandidate[0]
    l2=bestDileptcandidate[1]


  if triggerInfo is None:
    return True
  paths = triggerInfo.acceptedPaths()
  #for i in range(paths.size()) : print paths[i].name()
  pathnames = map(lambda i: paths[i].name(),range(paths.size()))
  intersect = set()
  if not perRun and l1 is not None and l2 is not None:
    if l1.isMuon() and l2.isMuon():
      intersect = set(pathnames) & set(ourtriggers.mutriggers)
    elif l1.isElectron() and l2.isElectron():
      intersect = set(pathnames) & set(ourtriggers.eltriggers)
    elif (l1.isElectron() and l2.isMuon()) or(l2.isElectron() and l1.isMuon()):
        intersect = set(pathnames) & set(ourtriggers.emutriggers)
  elif perRun and l1 is not None and l2 is not None:
    if l1.isMuon() and l2.isMuon():
      if ourtriggers.murunMap[runNumber] is None:
        print "muon unexpected runNumber : " , runNumber
      else:
        intersect = set(pathnames) & set(ourtriggers.murunMap[runNumber])
    elif l1.isElectron() and l2.isElectron():
      if ourtriggers.elrunMap[runNumber] is None:
        print "electron unexpected runNumber : " , runNumber
      else:
        intersect = set(pathnames) & set(ourtriggers.elrunMap[runNumber])
    elif (l1.isElectron() and l2.isMuon()) or(l2.isElectron() and l1.isMuon()):
      if ourtriggers.emurunMap[runNumber] is None:
        print "e-mu unexpected runNumber : " , runNumber
      else:
        intersect = set(pathnames) & set(ourtriggers.emurunMap[runNumber])

  outcome = len(intersect)>0
  return (outcome and isTriggerMatchDileptcandidate(bestDileptcandidate,runNumber,event.lumi()))


def isTriggerHambOK(event,perRun=True):
  """Checks if the proper trigger is passed"""
  # Only simple case: mu trigger for mu channel (1)
  triggerInfo = event.triggerInfo
  runNumber = event.run()
  l1= None
  l2= None
  bestDileptcandidate = event.bestHambDiMuCandidate
  if bestDileptcandidate is not None:
    l1=bestDileptcandidate[0]
    l2=bestDileptcandidate[1]
  if triggerInfo is None:
    return True
  paths = triggerInfo.acceptedPaths()
  #for i in range(paths.size()) : print paths[i].name()
  pathnames = map(lambda i: paths[i].name(),range(paths.size()))
  intersect = set()
  if l1 is not None and l2 is not None:
    if l1.isMuon() and l2.isMuon():
      if not perRun:
        intersect = set(pathnames) & set(ourtriggers.mutriggers)
      else:
        if ourtriggers.murunMap[runNumber] is None:
          print "muon unexpected runNumber : " , runNumber
        else:
          intersect = set(pathnames) & set(ourtriggers.murunMap[runNumber])
  outcome = len(intersect)>0
  return (outcome and isTriggerMatchDileptcandidate(bestDileptcandidate,runNumber,event.lumi()))

#Splitting the tirgger selection and matching (29-11-2015 -- Nadjieh)
def passDiMuTrigger(event,perRun=True):
  """Checks if the proper trigger is passed, no matching with offline muons"""
  triggerInfo = event.triggerInfo
  runNumber = event.run()
  if triggerInfo is None:
    return True
  paths = triggerInfo.acceptedPaths()
  pathnames = map(lambda i: paths[i].name(),range(paths.size()))
  intersect = set()
  if not perRun:
    intersect = set(pathnames) & set(ourtriggers.mutriggers)
  else:
        if ourtriggers.murunMap[runNumber] is None:
          print "muon unexpected runNumber : " , runNumber
        else:
          intersect = set(pathnames) & set(ourtriggers.murunMap[runNumber])
  outcome = len(intersect)>0
  return outcome



#Does not do matching for the moment!
def isSingleMuTriggerOK(event,perRun=True):
  """Checks if the proper trigger is passed"""
  # Only simple case: mu trigger for mu channel (1)
  triggerInfo = event.triggerInfo
  runNumber = event.run()
  if triggerInfo is None:
    return True
  paths = triggerInfo.acceptedPaths()
  #for i in range(paths.size()) : print paths[i].name()
  pathnames = map(lambda i: paths[i].name(),range(paths.size()))
  intersect = set()
  if not perRun:
    intersect = set(pathnames) & set(ourtriggers.SingleMutriggers)
  else:
    if ourtriggers.muSinglerunMap[runNumber] is None:
      print "muon unexpected runNumber : " , runNumber
    else:
      intersect = set(pathnames) & set(ourtriggers.muSinglerunMap[runNumber])
  outcome = len(intersect)>0
  return (outcome)

def isLooseMuon(muon, pt_ = 20., eta = 2.5):
  """Perform additional checks that define a loose muon"""
  # see https://server06.fynu.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/Zbbmuonselection
  # anything on top of PAT cfg ?
  # cleaning ?
  #return True
  return (muon.pt()> pt_ and abs(muon.eta()) < eta)

def isTightMuon(muon, pt_ = 20, eta = 2.5):
  """Perform additional checks that define a tight muon"""
  # see https://server06.fynu.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/Zbbmuonselection
  # to requires both muons to be matched
  #if muon().triggerObjectMatches().size()>0 :
  #if muMatches(muon).size() > 0 :
  # anything else on top of PAT cfg ?
  # cleaning ?
  #if muon.hasMasterClone():
  #  mu = muon.masterClone()
  #  ROOT.SetOwnership( mu, False )
  #else:
  #  mu = muon
  #return (isLooseMuon(muon, pt_))
  return (isLooseMuon(muon, pt_, eta))

def isMatchedMuon(muon, pt_ = 20., eta = 2.5):
  """Perform additional checks that define a matched muon"""
  # see https://server06.fynu.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/Zbbmuonselection
  # anything else on top of PAT cfg ?
  # cleaning ?
  return (isTightMuon(muon, pt_, eta) and True)

def isGoodMuon(muon,role, pt_ = 20., eta = 2.5):
  """Perform additional checks that define a good muon"""
  if string.find(role,"all")!=-1     : return isLooseMuon(muon, pt_, eta)
  if string.find(role,"tight")!=-1   : return isTightMuon(muon, pt_, eta)
  if string.find(role,"matched")!=-1 : return isMatchedMuon(muon, pt_, eta)
  if string.find(role,"none")!=-1    : return True
  print "Warning: Unknown muon role:",role
  return True

def isLooseElectron(electron):
  """Perform additional checks that define a loose electron"""
  # anything else on top of PAT cfg ?
  # cleaning ?
  # note: how to make a pat lepton from the shallowclone ?
  #if electron.hasOverlaps("muons"): return False
  return electron.pt()>20. # and ( abs(electron.eta())< 1.442 or ( 1.566<abs(electron.eta()) and abs(electron.eta())<2.50 ) ) to use superCluster use the electron masterClone() as the example in isTightElectron
  #return True

def isTightElectron(electron):
  """Perform additional checks that define a tight electron"""
  # anything else on top of PAT cfg ?
  # cleaning ?
  # note: how to make a pat lepton from the shallowclone ?
  #if electron.hasOverlaps("muons"): return False
  #to correct the PAT error (temporary)
  #if electron.hasMasterClone():
  #  el = electron.masterClone()
  #  ROOT.SetOwnership( el, False )
  #else:
  #  el = electron
  ##everything should be in the pat now
  return (isLooseElectron(electron))

def isMatchedElectron(electron):
  """Perform additional checks that define a matched electron"""
  # anything else on top of PAT cfg ?
  # cleaning ?
  # note: how to make a pat lepton from the shallowclone ?
  #print "has electron a clone? ",electron.hasMasterClone()
  #print "clone:",electron.masterClone().isNonnull()
  #if electron.hasOverlaps("muons"): return False
  return (isTightElectron(electron) and True)

def isGoodElectron(electron,role):
  """Perform additional checks that define a good electron"""
  if string.find(role,"all")!=-1   : return isLooseElectron(electron)
  if string.find(role,"tight")!=-1   : return isTightElectron(electron)
  if string.find(role,"matched")!=-1 : return isMatchedElectron(electron)
  if string.find(role,"none")!=-1    : return True
  print "Warning: Unknown electron role:",role
  return True

def hasNoOverlap(jet, Z = None, lepPair = None):
  """check overlap between jets and leptons"""

  #If Z candidate is given, it checks the overlap of the jet with the Z leptons
  #If lepPair is given, it checks the overlap of the jet with the pair of leptons
  #Only Z candidate or lepPair should be provided, otherwise the code exits

  if (not Z is None) and (not lepPair is None):
    print "hasNoOverlap called with both Z and lepPair candidate, aborting!"
    sys.exit(1)

  if (not Z is None) :
    l1 = Z.daughter(0)
    l2 = Z.daughter(1)

  if (not lepPair is None) :
    l1 = lepPair[0]
    l2 = lepPair[1]

  l1v = ROOT.TLorentzVector(l1.px(),l1.py(),l1.pz(),l1.energy())
  l2v = ROOT.TLorentzVector(l2.px(),l2.py(),l2.pz(),l2.energy())
  jv =  ROOT.TLorentzVector(jet.px(),jet.py(),jet.pz(),jet.energy())
  dr1 = jv.DeltaR(l1v)
  dr2 = jv.DeltaR(l2v)
  if (dr1>0.5 and dr2>0.5): return True
  else : return False

def jetId(jet,level="loose"):
  """jet id - This corresponds to the jet id selection for PF jets"""
  rawjet = jet.correctedJet("Uncorrected")
  nhf = ( rawjet.neutralHadronEnergy() + rawjet.HFHadronEnergy() ) / rawjet.energy()
  nef = rawjet.neutralEmEnergyFraction()
  nconstituents = rawjet.numberOfDaughters()
  chf = rawjet.chargedHadronEnergyFraction()
  nch = rawjet.chargedMultiplicity()
  cef = rawjet.chargedEmEnergyFraction()
  if level=="loose":
    return nhf<0.99 and nef<0.99 and  nconstituents>1 and chf>0 and nch>0 and cef<0.99
  elif level=="medium":
    return nhf<0.95 and nef<0.95 and  nconstituents>1 and chf>0 and nch>0 and cef<0.99
  elif level=="tight":
    return nhf<0.90 and nef<0.90 and  nconstituents>1 and chf>0 and nch>0 and cef<0.99
  else:
    print "Error: unknown jetid level:",level
    return False

def allJets(event, jets="rawjets"):
  eventrawjets = getattr(event, jets)
  if event.object().event().eventAuxiliary().isRealData() : return eventrawjets
  for jet in eventrawjets : JECuncertaintyProxy.Scale(jet)
  return eventrawjets

def isGoodJet(jet, Z = None, lepPair = None, pt = 30.):
  """Perform additional checks that define a good jet"""
  #If Z candidate is given, it checks the overlap of the jet with the Z leptons
  #If lepPair is given, it checks the overlap of the jet with the pair of leptons
  # overlap checking
  if not Z is None :
    if not hasNoOverlap(jet,Z=Z) :
      return False

  if not lepPair is None :
    if not hasNoOverlap(jet,Z=None,lepPair=lepPair) :
      return False

  # pt, eta, and jetid
  return abs(jet.eta())<2.4 and jet.pt()>pt and jetId(jet,"loose")

def goodJets(event, muChannel=True, eleChannel=True, pt=30.):
  # leptons pair
  if muChannel and eleChannel:
    pair = event.leptonsPair
  elif muChannel:
    pair = event.muonsPair
  elif eleChannel:
    pair = event.electronsPair
  else:
    pair = None
  # compute the good jets
  return map(lambda jet:isGoodJet(jet,lepPair=pair,pt=pt),event.jets)

def getMet(event,type="PF"):
  """Return the MET value you are interested in (type can be PF, MVA or NoPU)"""
  return{
	'PF':event.MET[0],
	'MVA':event.MVAMET[0],
	'NoPU':event.NoPUMET[0],
	}[type]

def isMetHigherThan(met,cut=20):
  """Apply a lower MET threshold"""
  return met.pt()>cut

def isMetLowerThan(met,cut=20):
  """Apply an upper MET threshold"""
  return met.pt()<cut

def isMetSigHigherThan(met,cut=10):
  """Apply a lower MET threshold"""
  if met.getSignificanceMatrix()(0,0)<1e10 and met.getSignificanceMatrix()(1,1)<1e10 :
    return met.significance()>cut
  else :
    return False

def isMetSigLowerThan(met,cut=10):
  """Apply an upper MET threshold"""
  if met.getSignificanceMatrix()(0,0)<1e10 and met.getSignificanceMatrix()(1,1)<1e10 :
    return met.significance()<cut
  else :
    return False

def isGoodMet(met,cut=50):
  """Apply the MET cut"""
  return met.pt()<cut

def isGoodMet_Sig(met,cut=10):
  """Apply the MET cut"""
  if met.getSignificanceMatrix()(0,0)<1e10 and met.getSignificanceMatrix()(1,1)<1e10 :
    return met.significance()<cut
  else :
    return False

def isBJet(jet,workingPoint,algo="CSV"):
  """Perform b-tagging"""
  if algo=="SSV":
    if workingPoint=="HE":
      return jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")>1.74 and jet.eta()<2.1
    elif workingPoint=="HP":
      return jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")>2.0 and jet.eta()<2.1
    else:
      print "Error: unforeseen working point for SSV. Use HE or HP"
      return False
  elif algo=="CSV":
    #WP valid both for 2011 and 2012
    if workingPoint=="L":
      return jet.bDiscriminator("combinedSecondaryVertexBJetTags")>0.244
    elif workingPoint=="M":
      return jet.bDiscriminator("combinedSecondaryVertexBJetTags")>0.679
    elif workingPoint=="T":
      return jet.bDiscriminator("combinedSecondaryVertexBJetTags")>0.898
    else:
      print "Error: unforeseen working point for CSV. Use L, M or T"
      return False
  elif algo=="JP":
    #WP valid both for 2011 and 2012
    if workingPoint=="L":
      return jet.bDiscriminator("jetProbabilityBJetTags")>0.275
    elif workingPoint=="M":
      return jet.bDiscriminator("jetProbabilityBJetTags")>0.545
    elif workingPoint=="T":
      return jet.bDiscriminator("jetProbabilityBJetTags")>0.790
    else:
      print "Error: unforeseen working point for CSV. Use L, M or T"
      return False
  else:
    print "Error: unforeseen algo for b-tagging. Use SSV, CSV or JP"
    return False

def jetPtD(jet):
  #input of VBF NN regression
  #returns the jet constituent Pt Distribution defined as sqrt(Sum(Pt**2))/Sum(Pt)
  # where the sum goes to the jet constituents
  #For 5X samples there is a method to access it:
  #return jet.constituentPtDistribution()
  #For 4X it is necessary to loop over the jet constituents

  pfConst = jet.getPFConstituents()
  sum_ptconst = 0
  sum_ptconst2 = 0

  for iConst in range (0, pfConst.size()):
    ptconst = pfConst[iConst].pt()
    ptconst2 = ptconst * ptconst
    sum_ptconst += ptconst
    sum_ptconst2 += ptconst2

  if sum_ptconst != 0:
    ptD = sqrt(sum_ptconst2)/sum_ptconst
  else:
    ptD = 0

  return ptD

def jetVtx3dL(jet):
  #input of VBF NN regression
  #returns the 3D of the SV jet if it exists
  output = 0
  tisv = jet.tagInfoSecondaryVertex()
  if tisv.nVertices()>0:
    output = tisv.flightDistance(0).value()
  return output

def jetVtx3deL(jet):
  #input of VBF NN regression
  #returns the 3D error of the SV jet if it exists

  output = 0
  tisv = jet.tagInfoSecondaryVertex()
  if tisv.nVertices()>0:
    output = tisv.flightDistance(0).error()
  return output


def jetVtxPt(jet):
  #input of VBF NN regression
  #it is basically the jet PT of the jet secondary vertex
  #  (in fact it sums vectorially all SV in the jet)
  VtxPt = 0
  tisv = jet.tagInfoSecondaryVertex()
  if tisv.nVertices()>0:
    for ivtx in range(0, tisv.nVertices()):
      if ivtx == 0:
        vertexSum = tisv.secondaryVertex(ivtx).p4()
      else:
        vertexSum += tisv.secondaryVertex(ivtx).p4()
    TLvertexSum = ROOT.TLorentzVector(vertexSum.px(),vertexSum.py(),vertexSum.pz(),vertexSum.energy())
    VtxPt = TLvertexSum.Pt()
  return VtxPt

def isZcandidate(zCandidate,vertex=None):
  """Checks that this is a suitable candidate from lepton quality"""
  result = True
  flavor = 1
  charge = 1
  triggerMatch = 1
  for r in zCandidate.roles():
    daughter = zCandidate.daughter(r)
    charge *= daughter.charge()
    if daughter.isMuon():
      flavor *= -1
      result = result and isGoodMuon(zCandidate.daughter(r),r)
    elif zCandidate.daughter(r).isElectron():
      result = result and isGoodElectron(zCandidate.daughter(r),r)
  # check that leptons are opposite charge (should always be the case)
  if charge != -1:
    print "Error: Z is not made of a proper lepton pair (charge issue)"
    return False
  # check that leptons are same flavor (should always be the case)
  if flavor != 1:
    print "Error: Z is not made of a proper lepton pair (flavor issue)"
    return False
  # vertex match
  if not vertex is None:
    result = result and zVertex(zCandidate,0.05,vertex)
  # if everything ok, return the result of the lepton check
  return result


def isTriggerMatchZcandidate(zCandidate, runNumber, lumi_section):
  if not zCandidate is None:
    daughter1 = zCandidate.daughter(0)
    daughter2 = zCandidate.daughter(1)
    Daugh1 = daughter1.masterClone()
    ROOT.SetOwnership( Daugh1, False )
    Daugh2 = daughter2.masterClone()
    ROOT.SetOwnership( Daugh2, False )
    case1 =  isTriggerMatchPair(Daugh1,Daugh2,runNumber,lumi_section)
    case2 = isTriggerMatchPair(Daugh2,Daugh1,runNumber,lumi_section)
    return (case1 or case2)
  else:
    return False

#trigger matching for inclusive selection
def isTriggerMatchDileptcandidate(bestDileptCandidate,runNumber, lumi_section):
  if not bestDileptCandidate is None:
    daughter1 = bestDileptCandidate[0]
    daughter2 = bestDileptCandidate[1]
    case1 = isTriggerMatchPair(daughter1,daughter2,runNumber,lumi_section)
    case2 = isTriggerMatchPair(daughter1,daughter2,runNumber,lumi_section)
    return (case1 or case2)
  else:
    return False

def isTriggerMatchPair(l1,l2,runNumber,lumi_section):
  if l1.isMuon() and l2.isMuon():
    #return True
    if runNumber>=160410 and runNumber<163269 :
      if (l1.triggerObjectMatchesByPath("HLT_DoubleMu6_v*",0,0).size()>0) and (l2.triggerObjectMatchesByPath("HLT_DoubleMu6_v*",0,0).size()>0) :
        return True
    if runNumber>=163269 and runNumber<165121 :
      if (l1.triggerObjectMatchesByPath("HLT_DoubleMu7_v*",0,0).size()>0) and (l2.triggerObjectMatchesByPath("HLT_DoubleMu7_v*",0,0).size()>0):
        return True
    if runNumber >= 165121 and runNumber< 178420:
      if (l1.triggerObjectMatchesByPath("HLT_Mu13_Mu8_v*",0,1).size()>0) and (l2.triggerObjectMatchesByPath("HLT_Mu13_Mu8_v*",0,1).size()>0) and ((l1.triggerObjectMatchesByFilter("hltDiMuonL3PreFiltered8").size()>0) or (l1.triggerObjectMatchesByFilter("hltDiMuonL3p5PreFiltered8").size()>0)) and ((l2.triggerObjectMatchesByFilter("hltDiMuonL3PreFiltered8").size()>0) or (l2.triggerObjectMatchesByFilter("hltDiMuonL3p5PreFiltered8").size()>0)) and (l1.triggerObjectMatchesByFilter("hltSingleMu13L3Filtered13").size()>0):
        return True
    if runNumber >= 178420 and runNumber< 180253:
      if (l1.triggerObjectMatchesByPath("HLT_Mu17_Mu8_v*",0,1).size()>0 and l2.triggerObjectMatchesByPath("HLT_Mu17_Mu8_v*",0,1).size()>0 and (l1.triggerObjectMatchesByFilter("hltDiMuonL3p5PreFiltered8").size()>0) and (l2.triggerObjectMatchesByFilter("hltDiMuonL3p5PreFiltered8").size()>0 ) and l1.triggerObjectMatchesByFilter("hltSingleMu13L3Filtered17").size()>0):
        return True
### data 2012
    if runNumber >= 180253 :
      #print "runNumber", runNumber
      #print 'l1.triggerObjectMatchesByPath("HLT_Mu17_Mu8_*",0,1).size()', l1.triggerObjectMatchesByPath("HLT_Mu17_Mu8_*",0,1).size(),
      #print 'l2.triggerObjectMatchesByPath("HLT_Mu17_Mu8_*",0,1).size()', l2.triggerObjectMatchesByPath("HLT_Mu17_Mu8_*",0,1).size()
      #print 'hltDiMuonGlbFiltered17TrkFiltered8', l1.triggerObjectMatchesByFilter("hltDiMuonGlbFiltered17TrkFiltered8").size(),
      #print l2.triggerObjectMatchesByFilter("hltDiMuonGlbFiltered17TrkFiltered8").size()
      #if ((l1.triggerObjectMatchesByPath("HLT_Mu17_TkMu8_v*",0,1).size()>0 and l2.triggerObjectMatchesByPath("HLT_Mu17_TkMu8_*",0,1).size()>0) and (l1.triggerObjectMatchesByFilter("hltDiMuonGlbFiltered17TrkFiltered8").size()>0 and l2.triggerObjectMatchesByFilter("hltDiMuonGlbFiltered17TrkFiltered8").size()>0)) or ((l1.triggerObjectMatchesByPath("HLT_Mu17_Mu8_v*",0,1).size()>0 and l2.triggerObjectMatchesByPath("HLT_Mu17_Mu8_*",0,1).size()>0) and (l1.triggerObjectMatchesByFilter("hltL3pfL1DoubleMu10MuOpen*L1f0L2pf0L3PreFiltered8").size()>0 and l2.triggerObjectMatchesByFilter("hltL3pfL1DoubleMu10MuOpen*L1f0L2pf0L3PreFiltered8").size()>0)) :
      #if ((l1.triggerObjectMatchesByPath("HLT_Mu17_Mu8_v*",0,1).size()>0 and l2.triggerObjectMatchesByPath("HLT_Mu17_Mu8_*",0,1).size()>0) and (l1.triggerObjectMatchesByFilter("hltL3pfL1DoubleMu10MuOpen*L1f0L2pf0L3PreFiltered8").size()>0 and l2.triggerObjectMatchesByFilter("hltL3pfL1DoubleMu10MuOpen*L1f0L2pf0L3PreFiltered8").size()>0)) :
      if ((l1.triggerObjectMatchesByPath("HLT_Mu17_TkMu8_v*",0,1).size()>0 and l2.triggerObjectMatchesByPath("HLT_Mu17_TkMu8_*",0,1).size()>0) or (l1.triggerObjectMatchesByPath("HLT_Mu17_Mu8_v*",0,1).size()>0 and l2.triggerObjectMatchesByPath("HLT_Mu17_Mu8_*",0,1).size()>0)) :
          #for i in range(0,l1.triggerObjectMatch(0).conditionNames().size()) : print "conditions "+str(i), l1.triggerObjectMatch(0).conditionNames()[i],
          #print ''
          #for i in range(0,l1.triggerObjectMatch(0).filterLabels().size()) : print "labels "+str(i), l1.triggerObjectMatch(0).filterLabels()[i],
          #print ''
          #for i in range(0,l1.triggerObjectMatch(0).pathNames().size()) : print "path "+str(i), l1.triggerObjectMatch(0).pathNames()[i],
          #print ''
          #print runNumber
          return True

  if l1.isElectron() and l2.isElectron():
    if electron_iswrongPS(l1, runNumber, lumi_section):
      return False
    else :
       if runNumber < 165121:
           if (l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",0,0).size()>0)and (l1.triggerObjectMatchesByFilter("hltEle17CaloIdIsoEle8CaloIdIsoPixelMatchDoubleFilter").size()>0) and (l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",0,0).size()>0) and (l2.triggerObjectMatchesByFilter("hltEle17CaloIdIsoEle8CaloIdIsoPixelMatchDoubleFilter").size()>0) :
             return True
       if runNumber >= 165121 and runNumber < 190455:
           if ((l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0) and (l1.triggerObjectMatchesByFilter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter").size()) and (l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0) and(l2.triggerObjectMatchesByFilter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter").size())) or ((l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_v*",0,1).size()>0) and (l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_v*",0,1).size()>0)) :
             return True
       if runNumber >= 190455 :
           #print "rn", runNumber
           #print "l1.triggerObjectMatchesByPath(HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIso...) 0,1 " ,l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).size()
       #print "l1.triggerObjectMatchesByPath(HLT_Ele17_CaloIdT_TrkIdVL_CaloIsoVL_TrkIso...) 0,1 " ,l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_v*",0,1).size()
           #print "path * 0,1 " , (l1.triggerObjectMatchesByPath("*",0,0).size())
           #print "path * 1,0 " , (l1.triggerObjectMatchesByPath("*",1,0).size())

           #if ((l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0) and (l1.triggerObjectMatchesByFilter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsoDoubleFilter").size()) and (l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0) and (l2.triggerObjectMatchesByFilter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsoDoubleFilter").size())) :
           if l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0 and l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0 :
             #print runNumber
             #l1DoublePaths = []
             #for j in range(0,l1.triggerObjectMatches().size()):
             #  for i in range(0,l1.triggerObjectMatch(j).pathNames().size()):
             #    if "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v" in l1.triggerObjectMatch(j).pathNames()[i] : l1DoublePaths.append(j)
             #l2DoublePaths = []
             #for j in range(0,l2.triggerObjectMatches().size()):
             #  for i in range(0,l2.triggerObjectMatch(j).pathNames().size()):
             #    if "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v" in l2.triggerObjectMatch(j).pathNames()[i] : l2DoublePaths.append(j)

             #for j in l1DoublePaths:
             #  for i in range(0,l1.triggerObjectMatch(j).conditionNames().size()):
             #    print "conditions l1: "+str(j)+";"+str(i)+".", l1.triggerObjectMatch(j).conditionNames()[i]
             #    print 'l1.eta', l1.eta()
                 #print "labels l1: "+str(j)+";"+str(i)+".", l1.triggerObjectMatch(j).filterLabels()[i]
                 #print ''
             #for j in l2DoublePaths:
             #  for i in range(0,l2.triggerObjectMatch(j).conditionNames().size()):
             #    print "conditions l2: "+str(j)+";"+str(i)+".", l2.triggerObjectMatch(j).conditionNames()[i]
             #    print 'l2.eta', l2.eta()
                 #print "labels l2: "+str(j)+";"+str(i)+".", l2.triggerObjectMatch(j).filterLabels()[i]
                 #print ''

             #print runNumber
             return True

  if (l1.isElectron() and l2.isMuon() ) or (l2.isElectron() and l1.isMuon() ):
    if runNumber >= 190455:
      if (l1.triggerObjectMatchesByPath("HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0 and l2.triggerObjectMatchesByPath("HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0) or (l1.triggerObjectMatchesByPath("HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0 and l2.triggerObjectMatchesByPath("HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0):
        return True

  return False

def findBestCandidate(event, muChannel=True, eleChannel=False):
  """Finds the best Z candidate. Might be none.
     As input, the function takes an arbitrary number of collections of Z candidates.
     muChannel specify if we have to consider only muons (true), electrons (false) or both (none)."""
  bestZ = None
  bestM = -1000.
  vertex = event.vertex
  if muChannel:
    for z in event.Zmumu:
      if not isZcandidate(z,vertex): continue
      if abs(z.mass()-91.1876)<abs(bestM-91.1876) :
        bestM = z.mass()
        bestZ = z
  if eleChannel:
    for z in event.Zelel:
      if not isZcandidate(z,vertex): continue
      if abs(z.mass()-91.1876)<abs(bestM-91.1876) :
        bestM = z.mass()
        bestZ = z
  return bestZ

def leptonsFromPV_ptSorted(event):
	muList=[muon for muon in event.muons if isGoodMuon(muon, "tight") and isFromVertex_SingleLepton(muon,0.05,event.vertex)]
 	elList=[electron for electron in event.electrons if isGoodElectron(electron, "tight") and isFromVertex_SingleLepton(electron,0.05,event.vertex)]
	lepList=muList+elList
	ptSortedLepList = sorted(lepList,reverse=True,key=attrgetter('pt'))
	return ptSortedLepList if len(ptSortedLepList)>1 else None

def leptonsFromPV_ptSorted_DRllVetoOnFirstTwo(event, DRll_cut=0.3):
	if event.ptSortedLeptons is not None :
		l1=event.ptSortedLeptons[0]
		l2=event.ptSortedLeptons[1]
		DRll=ROOT.TLorentzVector(l1.px(),l1.py(),l1.pz(),l1.energy()).DeltaR(ROOT.TLorentzVector(l2.px(),l2.py(),l2.pz(),l2.energy()))
		return event.ptSortedLeptons if DRll>DRll_cut else None
	else :
		return None

def findBestDiLeptCandidate(event, muChannel=True, eleChannel=True):
  muList = []
  elList = []
  leptList = []
  first_lept = None
  second_lept = None
  third_lept = None
  fourth_lept = None

  for mu in event.muons:
    if isGoodMuon(mu, "tight"):
        muList.append(mu)

  for el in event.electrons:
    if isGoodElectron(el, "tight"):
        elList.append(el)

  if len(muList) > 0  :
    if len(elList) > 0 :
      if elList[0].pt() > muList[0].pt():
        first_lept = elList[0]
        elList.remove(elList[0])
      elif elList[0].pt() < muList[0].pt():
        first_lept = muList[0]
        muList.remove(muList[0])
    else :
      first_lept = muList[0]
      muList.remove(muList[0])
  else:
    if len(elList) > 0:
      first_lept = elList[0]
      elList.remove(elList[0])

  if len(muList) > 0  :
    if len(elList) > 0 :
      if elList[0].pt() > muList[0].pt():
        second_lept = elList[0]
        elList.remove(elList[0])
      elif elList[0].pt() < muList[0].pt():
        second_lept = muList[0]
        muList.remove(muList[0])
    else :
      second_lept = muList[0]
      muList.remove(muList[0])
  else:
    if len(elList) > 0:
      second_lept = elList[0]
      elList.remove(elList[0])

  if len(muList) > 0  :
    if len(elList) > 0 :
      if elList[0].pt() > muList[0].pt():
        third_lept = elList[0]
        elList.remove(elList[0])
      elif elList[0].pt() < muList[0].pt():
        third_lept = muList[0]
        muList.remove(muList[0])
    else :
      third_lept = muList[0]
      muList.remove(muList[0])
  else:
    if len(elList) > 0:
      third_lept = elList[0]
      elList.remove(elList[0])

  if len(muList) > 0  :
    if len(elList) > 0 :
      if elList[0].pt() > muList[0].pt():
        fourth_lept = elList[0]
        elList.remove(elList[0])
      elif elList[0].pt() < muList[0].pt():
        fourth_lept = muList[0]
        muList.remove(muList[0])
    else :
      fourth_lept = muList[0]
      muList.remove(muList[0])
  else:
    if len(elList) > 0:
      fourth_lept = elList[0]
      elList.remove(elList[0])

  #Force the DR of the first 2 leptons to be > 0.3 for the moment
  if first_lept is None or second_lept is None: return None
  else:
    #l1v = ROOT.TLorentzVector(leptList[0].px(),leptList[0].py(),leptList[0].pz(),leptList[0].energy())
    #l2v = ROOT.TLorentzVector(leptList[1].px(),leptList[1].py(),leptList[1].pz(),leptList[1].energy())
    l1v = ROOT.TLorentzVector(first_lept.px(),first_lept.py(),first_lept.pz(),first_lept.energy())
    l2v = ROOT.TLorentzVector(second_lept.px(),second_lept.py(),second_lept.pz(),second_lept.energy())
    if l1v.DeltaR(l2v) < 0.3: return None

  vertex_cond=False
  result = False
  leptList.append(first_lept)
  leptList.append(second_lept)
  leptList.append(third_lept)
  leptList.append(fourth_lept)


  if (first_lept is not None  and second_lept is not None ):
     vertex_cond = isfromVertex(first_lept, second_lept, 0.05)
     if third_lept is not None:
       vertex_cond = isfromVertex(third_lept, second_lept, 0.05)
       if fourth_lept is not None:
         vertex_cond = isfromVertex(third_lept, fourth_lept, 0.05)

  if (vertex_cond is True):
    result = True




  if (result == True):
    return (leptList[0],leptList[1],leptList[2],leptList[3])
  else:
    return None



def findBestHambDiMuCandidate(event, muChannel=True, leadPt = 20., secPt = 20., MuEta = 2.4):
  muList = []
  for mu in event.muons:
    if(len(muList) == 0):
      if isGoodMuon(mu, "tight",leadPt,MuEta):
	muList.append(mu)
    elif(len(muList) == 1):
      if isGoodMuon(mu, "tight",secPt,MuEta):
        muList.append(mu)
    else: break
  if len(muList) < 2: return None
  if muList[0] is None or muList[1] is None: return None
  if not (isfromVertex(muList[0], muList[1], 0.05)):
    return None
  return (muList[0],muList[1])    
    
def diLeptonsPair(event, bestLeptonCand="bestZcandidate"):
  cand = getattr(event, bestLeptonCand)
  if cand is None : return None
  if type(cand) is list or type(cand) is tuple:
    if not len(cand)>1 : return None
    return cand
  else:
    try:
      return [cand.daughter(0), cand.daughter(1)]
    except:
      return [None, None]

def findJetsMatchedWithB(event): #for muon channel only
  """Find a pair of jets, matched with b genJets."""
  goodMatchedJets = event.goodJets_muMatched
  ret = []
  for index,jet in enumerate(event.jets):
     if goodMatchedJets[index]:
	ret.append(jet)
  return ret 

def goodJetMatchedWithB(event): #for muon channel only
  """Produce an array of booleans whether a jet is matched"""
  goodJets = event.goodJets_mu
  bGenJets = event.sortedGenJets[0]
  #if not len(bGenJets) == 2:
  #  return None
  matchedJetsIndex = []
  for iGenJet in bGenJets:
    minDR = 1000
    index = -1
    gen = ROOT.TLorentzVector(iGenJet.px(),iGenJet.py(),iGenJet.pz(),iGenJet.energy())
    for i, iJet in enumerate(goodJets):
       if not iJet: continue
       newJet = True
       if not len(matchedJetsIndex) == 0:
          for j in range(len(matchedJetsIndex)):
             if i == matchedJetsIndex[j]:
                newJet = False
                break;
       if not newJet:
          continue
       jet = ROOT.TLorentzVector(event.jets[i].px(),event.jets[i].py(),event.jets[i].pz(),event.jets[i].energy())
       if jet.DeltaR(gen) < minDR:
          minDR = jet.DeltaR(gen)
          index = i
    matchedJetsIndex.append(index)
  matchedJetsIndex.sort()
  ret = []
  for i, iJet in enumerate(goodJets):
     found = False
     for matchIndex in matchedJetsIndex:
        if(i == matchIndex):
	   found = True 
     if found: ret.append(True)
     else: ret.append(False)
  return ret


def findDijetPair(event, btagging="CSV", WP=["M","L"], muChannel=True, eleChannel=False):
  """Find the best jet pair: high Pt and btagging."""
  # the proper goodJets list
  if muChannel and eleChannel:
    goodJets = event.goodJets_all
  elif muChannel:
    goodJets = event.goodJets_mu
  elif eleChannel:
    goodJets = event.goodJets_ele
  else:
    goodJets = event.goodJets_none
  # check number of good jets
  indices_pt = [index for index,jet in enumerate(event.jets) if goodJets[index] ]
  if btagging == "CSV":
    btagList = [(jet.bDiscriminator("combinedSecondaryVertexBJetTags"),index) for index,jet in enumerate(event.jets) if goodJets[index] ]
  elif btagging == "JP":
    btagList = [(jet.bDiscriminator("jetProbabilityBJetTags"),index) for index,jet in enumerate(event.jets) if goodJets[index] ]

  btagList.sort(reverse=True)
  indices = []
  for ibtag in btagList:
    indices.append(ibtag[1])
  if len(indices)<1: return (None, None)
  if len(indices)<2: return (event.jets[indices[0]],None)
  jetList = []
  # start with HP b-jets
  for index in indices[:]:
    if isBJet(event.jets[index],WP[0],btagging):
      jetList.append(index)
      indices.remove(index)
      indices_pt.remove(index)
  if len(jetList)>=2:
    if event.jets[jetList[0]].pt()>event.jets[jetList[1]].pt() :
      return (event.jets[jetList[0]],event.jets[jetList[1]])
    else :
      return (event.jets[jetList[1]],event.jets[jetList[0]])
  # continue with HE b-jets
  for index in indices[:]:
    if isBJet(event.jets[index],WP[1],btagging):
      jetList.append(index)
      indices.remove(index)
      indices_pt.remove(index)
  if len(jetList)>=2:
    if event.jets[jetList[0]].pt()>event.jets[jetList[1]].pt() :
      return (event.jets[jetList[0]],event.jets[jetList[1]])
    else :
      return (event.jets[jetList[1]],event.jets[jetList[0]])
  # fill with remaining good jets
  for index in indices_pt:
    jetList.append(index)
  return (event.jets[jetList[0]],event.jets[jetList[1]])

def vertex(event):
  vertices = event.vertices
  if vertices.size()>0 :
    return vertices[0]
  else:
    return None



#Get fat jets candidate with pt>20. and with 2 good subjets with pt>pt
def fatjets(event, pt=30.):
  fatjets = []
  prunedCSV = 0
  fatjet = None
  #run over all pruned fat jets
  prunedjets = allJets(event, jets="rawprunedjets", checksubjets=True, cone="AK7")
  for pruned in prunedjets:
    if pruned.pt()>2*pt and pruned.bDiscriminator("combinedSecondaryVertexBJetTags")>prunedCSV and pruned.numberOfDaughters() == 2:
      if isGoodJet(pruned.daughter(0), lepPair = event.bestZcandidate, pt = pt) and isGoodJet(pruned.daughter(1), lepPair = event.bestZcandidate, pt = pt):
        #if true replace the fatjet candidate
        prunedCSV = pruned.bDiscriminator("combinedSecondaryVertexBJetTags")
        fatjet = pruned
  if not fatjet is None : fatjets.append(fatjet)
  return fatjets

#Get the 2 subjets
def subjets(event):
  subjets = []
  j1 = None
  j2 = None
  prunedPt = 0
  #check if a good fatjet candidate
  if len(event.fatjets) == 1:
    pruned = event.fatjets[0]
    j1 = pruned.daughter(0)
    j2 = pruned.daughter(1)
  elif len(event.fatjets) > 1 : print "Error: more than 1 fat jets selected."
  if not (j1 is None and j2 is None):
    subjets.append(j1)
    subjets.append(j2)
  #redifine the subjet flavour using hadron (default flavour definition can be wrong as can match one parton to several jets)
  if not event.object().event().eventAuxiliary().isRealData() : hadronFlavour(event.genParticles, subjets)
  return subjets

def jetMult(event, btagging="CSV", WP=["M","L"], prejets=""):
  goodJets = getattr(event, "good"+prejets+"Jets_all")
  nJets = 0
  nBjetsHE = 0
  nBjetsHP = 0
  nBjetsHEHP = 0
  for index,jet in enumerate(getattr(event,prejets+"jets")):
    if goodJets[index]:
      nJets += 1
      HE = isBJet(jet,WP[1],btagging)
      HP = isBJet(jet,WP[0],btagging)
      if HE: nBjetsHE += 1
      if HP: nBjetsHP += 1
      if HE and HP: nBjetsHEHP +=1
  if nJets>1:
    dijet = getattr(event, "di"+prejets+"jet_all")
    j1 = ROOT.TLorentzVector(dijet[0].px(),dijet[0].py(),dijet[0].pz(),dijet[0].energy())
    j2 = ROOT.TLorentzVector(dijet[1].px(),dijet[1].py(),dijet[1].pz(),dijet[1].energy())
    dr = j1.DeltaR(j2)
  else : dr = -1      
  jetInfo = {
    "nj" : nJets,
    "nbHE" : nBjetsHE,
    "nbHP" : nBjetsHP,
    "nbHEHP" : nBjetsHEHP,
    "drj1j2" : dr
    }
  return jetInfo
