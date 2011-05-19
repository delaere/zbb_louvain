import ROOT

def selectedTriggers(triggerInfo):
  if triggerInfo is None:
    return []
  triggers = ("HLT_Mu3_v3", "HLT_Mu5_v3", "HLT_Mu8_v1", "HLT_Mu12_v1", "HLT_Mu15_v2", "HLT_Mu20_v1", "HLT_Mu24_v1", "HLT_Mu30_v1", "HLT_DoubleMu3_v3", "HLT_DoubleMu6_v1", "HLT_DoubleMu7_v1",
              "HLT_Ele8_v2", "HLT_Ele8_CaloIdL_CaloIsoVL_v2", "HLT_Ele8_CaloIdL_TrkIdVL_v2", "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v2", "HLT_Ele17_CaloIdL_CaloIsoVL_v2",
              "HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v2", "HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1", "HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v3", "HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v3",
              "HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v2"
              )
  paths = map(lambda trigger: triggerInfo.path(trigger),triggers)
  def isFired(path):
    if not path is None: 
      path.wasAccept() # error ReferenceError: attempt to access a null-pointer..... should change name
    else: 
      False
  pathout = map(lambda path:isFired(path),paths)
  #not sure if the all-in-one solution below is faster...
  #pathout = map(lambda trigger: if not triggerInfo.path(trigger) is None: triggerInfo.path(trigger).wasAccept() else: False, triggers)
  return pathout

def isTriggerOK(triggerInfo, muChannel=True, runNumber=None):
  """Checks if the proper trigger is passed"""
  # simple case: mu trigger for mu channel (1), ele trigger for ele channel (0)
  # more complex case: different trigger for various run ranges (lowest unprescaled)
  if triggerInfo is None:
    return True
  paths = triggerInfo.acceptedPaths()
  pathnames = map(lambda i: paths[i].name(),range(paths.size()))
  if runNumber is None:
    if muChannel:
      triggers = ("HLT_Mu3_v3", "HLT_Mu5_v3", "HLT_Mu8_v1", "HLT_Mu12_v1", "HLT_Mu15_v2", "HLT_Mu20_v1", "HLT_Mu24_v1", "HLT_Mu30_v1", "HLT_DoubleMu3_v3", "HLT_DoubleMu6_v1", "HLT_DoubleMu7_v1")
    else:
      triggers = ("HLT_Ele8_v2", "HLT_Ele8_CaloIdL_CaloIsoVL_v2", "HLT_Ele8_CaloIdL_TrkIdVL_v2", "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v2", "HLT_Ele17_CaloIdL_CaloIsoVL_v2",
              "HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v2", "HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1", "HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v3", "HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v3",
              "HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v2"
                  )
    intersect = list(set(pathnames) & set(triggers))
    outcome = len(intersect)>0
  else:
    if muChannel:
      if runNumber>=132440 and runNumber<=139980 : outcome = "HLT_Mu3" in pathnames
      if runNumber>=140058 and runNumber<=140401 : outcome = "HLT_Mu5" in pathnames
      if runNumber>=141956 and runNumber<=144114 : outcome = "HLT_Mu7" in pathnames
      if runNumber>=146428 and runNumber<=147116 : outcome = "HLT_Mu9" in pathnames
      if runNumber>=147146 and runNumber<=148102 : outcome = "HLT_Mu11" in pathnames
      if runNumber>=148783 and runNumber<=149442 : outcome = "HLT_Mu15_v1" in pathnames
    else:
      if runNumber>=132440 and runNumber<=137028 : outcome = "HLT_Photon10_L1R" # should impose a cut at 15 GeV by hand
      if runNumber>=138564 and runNumber<=140401 : outcome = "HLT_Photon15_Cleaned_L1R" in pathnames
      if runNumber>=141956 and runNumber<=144114 : outcome = "HLT_Ele15_SW_CaloEleId_L1R" in pathnames
      if runNumber>=146428 and runNumber<=147116 : outcome = "HLT_Ele17_SW_CaloEleId_L1R" in pathnames
      if runNumber>=147146 and runNumber<=148102 : outcome = "HLT_Ele17_SW_TightEleId_L1R" in pathnames
      if runNumber>=148783 and runNumber<=149063 : outcome = "HLT_Ele22_SW_TighterCaloIdIsol_L1R_v1" in pathnames
      if runNumber>=149181 and runNumber<=149442 : outcome = "HLT_Ele22_SW_TighterCaloIdIsol_L1R_v2" in pathnames
  return outcome
  # this is what we could do with the TriggerWeight product:
  #outcome = False
  #if runNumber is None:
  #  if muChannel:
  #    for i in range(6): outcome |= triggerInfo[i]
  #  else:
  #    for i in range(6,13): outcome |= triggerInfo[i]
  #else:
  #  if muChannel:
  #    if runNumber>=132440 and runNumber<=139980 : outcome = triggerInfo[0]  #HLT_Mu3
  #    if runNumber>=140058 and runNumber<=140401 : outcome = triggerInfo[1]  #HLT_Mu5
  #    if runNumber>=141956 and runNumber<=144114 : outcome = triggerInfo[2]  #HLT_Mu7
  #    if runNumber>=146428 and runNumber<=147116 : outcome = triggerInfo[3]  #HLT_Mu9
  #    if runNumber>=147146 and runNumber<=148102 : outcome = triggerInfo[4]  #HLT_Mu11
  #    if runNumber>=148783 and runNumber<=149442 : outcome = triggerInfo[5]  #HLT_Mu15_v1
  #  else:
  #    if runNumber>=132440 and runNumber<=137028 : outcome = triggerInfo[6]  #HLT_Photon10_L1R should impose a cut at 15 GeV by hand
  #    if runNumber>=138564 and runNumber<=140401 : outcome = triggerInfo[7]  #HLT_Photon15_Cleaned_L1R
  #    if runNumber>=141956 and runNumber<=144114 : outcome = triggerInfo[8]  #HLT_Ele15_SW_CaloEleId_L1R
  #    if runNumber>=146428 and runNumber<=147116 : outcome = triggerInfo[9]  #HLT_Ele17_SW_CaloEleId_L1R
  #    if runNumber>=147146 and runNumber<=148102 : outcome = triggerInfo[10] #HLT_Ele17_SW_TightEleId_L1R
  #    if runNumber>=148783 and runNumber<=149063 : outcome = triggerInfo[11] #HLT_Ele22_SW_TighterCaloIdIsol_L1R_v1
  #    if runNumber>=149181 and runNumber<=149442 : outcome = triggerInfo[12] #HLT_Ele22_SW_TighterCaloIdIsol_L1R_v2
  #return outcome

def isLooseMuon(muon):
  """Perform additional checks that define a loose muon"""
  # see https://server06.fynu.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/Zbbmuonselection

  # anything on top of PAT cfg ?
  # cleaning ?

  return True

def isTightMuon(muon):
  """Perform additional checks that define a tight muon"""
  # see https://server06.fynu.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/Zbbmuonselection

  # anything else on top of PAT cfg ?
  # cleaning ?

  return (isLooseMuon(muon) and True)

def isMatchedMuon(muon):
  """Perform additional checks that define a matched muon"""
  # see https://server06.fynu.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/Zbbmuonselection

  # anything else on top of PAT cfg ?
  # cleaning ?

  return (isTightMuon(muon) and True)

def isGoodMuon(muon,role):
  """Perform additional checks that define a good muon"""
  if role=="loose" : return isLooseMuon(muon)
  if role=="tight" : return isTightMuon(muon)
  if role=="matched" : return isMatchedMuon(muon)
  if role=="none" : return True
  print "Warning: Unknown muon role:",role
  return True

def isLooseElectron(electron):
  """Perform additional checks that define a loose electron"""

  # anything else on top of PAT cfg ?
  # cleaning ?
  # note: how to make a pat lepton from the shallowclone ?
  #if electron.hasOverlaps("muons"): return False

  return True

def isTightElectron(electron):
  """Perform additional checks that define a tight electron"""

  # anything else on top of PAT cfg ?
  # cleaning ?
  # note: how to make a pat lepton from the shallowclone ?
  #if electron.hasOverlaps("muons"): return False
  if electron.pt()<25. : return False

  return (isLooseElectron(electron) and True)

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
  if role=="loose" : return isLooseElectron(electron)
  if role=="tight" : return isTightElectron(electron)
  if role=="matched" : return isMatchedElectron(electron)
  if role=="none" : return True
  print "Warning: Unknown muon role:",role
  return True

def hasNoOverlap(jet, Z):
  """check overlap between jets and leptons from the Z"""
  l1 = Z.daughter(0)
  l2 = Z.daughter(1)
  l1v = ROOT.TLorentzVector(l1.px(),l1.py(),l1.pz(),l1.energy())
  l2v = ROOT.TLorentzVector(l2.px(),l2.py(),l2.pz(),l2.energy())
  jv =  ROOT.TLorentzVector(jet.px(),jet.py(),jet.pz(),jet.energy())
  dr1 = jv.DeltaR(l1v)
  dr2 = jv.DeltaR(l2v)
  if (dr1>0.5 and dr2>0.5): return True
  else : return False
    
def jetId(jet,level="loose"):
  """jet id - This corresponds to the jet id selection for PF jets"""
  rawjet = jet # TODO: in principle, one should do: rawjet = jet.correctedJet("RAW") 
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

def isGoodJet(jet, Z = None):
  """Perform additional checks that define a good jet"""
  # restrict in eta
  outcome = abs(jet.eta())<2.1
  outcome = outcome and jet.pt()>25
  # overlap checking
  # the following would be too dangerous for bjets... would probably need to restrict to tight leptons
#  if jet.hasOverlaps("muons"): return False
#  if jet.hasOverlaps("electrons"): return False
  if not Z is None :
    outcome = outcome
    if not hasNoOverlap(jet,Z) :
      return False 
  # check jetid (loose)
  outcome = outcome and jetId(jet,"loose")
  return outcome

def isGoodMet(met,cut=40):
  """Apply the MET cut"""
  return met.pt()<cut

def isBJet(jet,workingPoint,algo="SSV"):
  """Perform b-tagging"""
  if algo=="SSV":
    if workingPoint=="HE":
      return jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")>1.74
    elif workingPoint=="HP":
      return jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")>2.0
    else:
      print "Error: unforeseen working point for b-tagging. Use HE or HP"
      return False
  elif algo=="TC":
    if workingPoint=="HE":
      return jet.bDiscriminator("trackCountingHighEffBJetTags")>3.3
    elif workingPoint=="HP":
      return jet.bDiscriminator("trackCountingHighPurBJetTags")>3.41
    else:
      print "Error: unforeseen working point for b-tagging. Use HE or HP"
      return False
  else:
    print "Error: unforeseen algo for b-tagging. Use SSV or TC"
    return False


def isZcandidate(zCandidate):
  """Checks that this is a suitable candidate from lepton quality"""
  result = True
  flavor = 1
  charge = 1
  for r in zCandidate.roles():
    daughter = zCandidate.daughter(r)
    charge *= daughter.charge()
    if daughter.isMuon() :
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
  # if everything ok, return the result of the lepton check
  return result

def findBestCandidate(*zCandidates):
  """Finds the best Z candidate. Might be none.
     As input, the function takes an arbitrary number of collections of Z candidates."""
  bestZ = None
  bestM = -1000.
  for col in zCandidates:
    for z in col:
      if not isZcandidate(z): continue
      if abs(z.mass()-91.1876)<abs(bestM-91.1876) :
        bestM = z.mass()
        bestZ = z
  return bestZ

def eventCategories(): return 10

def eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, muChannel=True, btagging="SSV"):
  """See up to which level the event passes the selection"""
  if not isTriggerOK(triggerInfo, muChannel): return 0
  if muChannel:
    bestZcandidate = findBestCandidate(zCandidatesMu)
  else:
    bestZcandidate = findBestCandidate(zCandidatesEle)
  #looking for both would potentially introduce double counting and suffers from 
  #the absence of trigger in MC.
  #bestZcandidate = findBestCandidate(zCandidatesMu,zCandidatesEle)
  if bestZcandidate is None : return 1
  if abs(bestZcandidate.mass()-91.1876)>30. : return 2
  nJets    = 0
  nBjetsHE = 0
  nBjetsHP = 0
  for jet in jets:
    if isGoodJet(jet,bestZcandidate):
      nJets += 1
      if isBJet(jet,"HE",btagging): nBjetsHE += 1
      if isBJet(jet,"HP",btagging): nBjetsHP += 1
  if nJets==0: return 3
  if nBjetsHE==0: return 4
  if not isGoodMet(met[0]): return 5
  if nBjetsHP==0: return 6
  if nBjetsHE==1: return 7
  if nBjetsHP==1: return 8
  return 9

