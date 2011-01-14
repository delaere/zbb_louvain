def isTriggerOK(triggerInfo, muchannel=True, runNumber=None):
  """Checks if the proper trigger is passed"""
  # simple case: mu trigger for mu channel (1), ele trigger for ele channel (0)
  # more complex case: different trigger for various run ranges (lowest unprescaled)

  # IMPORTANT: to be fast, it uses the vector from TriggerWeight and assumes the order within.

  outcome = False
  if runNumber is None:
    if muChannel:
      for i in range(6): outcome |= triggerInfo[i]
    else:
      for i in range(6,13): outcome |= triggerInfo[i]
  else:
    if muChannel:
      if runNumber>=132440 and runNumber<=139980 : outcome = triggerInfo[0]  #HLT_Mu3
      if runNumber>=140058 and runNumber<=140401 : outcome = triggerInfo[1]  #HLT_Mu5
      if runNumber>=141956 and runNumber<=144114 : outcome = triggerInfo[2]  #HLT_Mu7
      if runNumber>=146428 and runNumber<=147116 : outcome = triggerInfo[3]  #HLT_Mu9
      if runNumber>=147146 and runNumber<=148102 : outcome = triggerInfo[4]  #HLT_Mu11
      if runNumber>=148783 and runNumber<=149442 : outcome = triggerInfo[5]  #HLT_Mu15_v1
    else:
      if runNumber>=132440 and runNumber<=137028 : outcome = triggerInfo[6]  #HLT_Photon10_L1R should impose a cut at 15 GeV by hand
      if runNumber>=138564 and runNumber<=140401 : outcome = triggerInfo[7]  #HLT_Photon15_Cleaned_L1R
      if runNumber>=141956 and runNumber<=144114 : outcome = triggerInfo[8]  #HLT_Ele15_SW_CaloEleId_L1R
      if runNumber>=146428 and runNumber<=147116 : outcome = triggerInfo[9]  #HLT_Ele17_SW_CaloEleId_L1R
      if runNumber>=147146 and runNumber<=148102 : outcome = triggerInfo[10] #HLT_Ele17_SW_TightEleId_L1R
      if runNumber>=148783 and runNumber<=149063 : outcome = triggerInfo[11] #HLT_Ele22_SW_TighterCaloIdIsol_L1R_v1
      if runNumber>=149181 and runNumber<=149442 : outcome = triggerInfo[12] #HLT_Ele22_SW_TighterCaloIdIsol_L1R_v2
  return outcome

def isLooseMuon(muon):
  """Perform additional checks that define a loose muon"""
  #TODO: implement
  # anything on top of PAT cfg ?
  # cleaning ?
  #muon.pt()>20.
  return True

def isTightMuon(muon):
  """Perform additional checks that define a tight muon"""
  #TODO: implement
  # check trigger matching
  # anything else on top of PAT cfg ?
  # cleaning ?
  #muon.pt()>20.
  return True

def isGoodElectron(electron):
  """Perform additional checks that define a good electron"""
  #TODO: implement
  # check trigger matching
  # anything else on top of PAT cfg ?
  # cleaning ?
  #electron.pt()>20.
  return True

def isGoodJet(jet)
  """Perform additional checks that define a good jet"""
  #TODO: implement
  # perform cleaning
  # jet id ?
  # abs(jet.eta())<2.1
  # dR(leptons)>0.4
  return True

def isBJet(jet,workingPoint)
  """Perform b-tagging"""
  if workingPoint=="HE":
    return jet.bDiscriminant("simpleSecondaryVertexHighEffBJetTags")>1.7
  elif workingPoint=="HP":
    return jet.bDiscriminant("simpleSecondaryVertexHighPurBJetTags")>2.0
  else:
    print "Error: unforeseen working point for b-tagging. Use HE or HP"
    return False

def isZcandidate(zCandidate):
  """Checks that this is a suitable candidate from lepton quality"""
  lepton1 = zcandidate.daughter(0)
  lepton2 = zcandidate.daughter(1)
  # check that leptons are opposite charge (should always be the case)
  if lepton1.charge()*lepton2.charge() != -1:
    print "Error: Z is not made of a proper lepton pair (charge issue)"
    return False
  # check that the leptons pass all quality criterias
  if lepton1.isMuon() and lepton2.isMuon():
    #is there a way to know in which collection is each lepton ?
    return (isLooseMuon(lepton1) and isLooseMuon(lepton2) and (isTightMuon(lepton1) or isTightMuon(lepton2)))
  elif lepton1.isElectron() and lepton2.isElectron():
    return (isGoodElectron(lepton1) and isGoodElectron(lepton2))
  else:
    print "Error: Z is not made of a proper lepton pair (Flavor issue)"
    return False

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

def eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets):
  """See up to which level the event passes the selection"""
  #TODO: add vertex constraints when ready
  bestZcandidate = findBestCandidate(zCandidatesMu,zCandidatesEle)
  if not isTriggerOK(triggerInfo, bestZcandidate.daughter(0).isMuon()): return 0
  if bestZcandidate is None : return 1
  if abs(bestZcandidate.mass-91.1876)<15.): return 2
  nJets    = 0
  nBjetsHE = 0
  nBjetsHP = 0
  for jet in jets:
    if isGoodJet(jet):
      nJets += 1
      if isBJet(jet,"HE"): nBjetsHE += 1
      if isBJet(jet,"HP"): nBjetsHP += 1
  if njets==0: return 3
  if nBjetsHE==0: return 4 # we can do this way because HP is a subset of HE
  if nBjetsHP==0: return 5 #
  return 6

