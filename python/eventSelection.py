import ROOT

def selectedTriggers(triggerInfo):
  if triggerInfo is None:
    return []

  triggers = ("HLT_Mu13_Mu8_v2","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v4","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v5")
              
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
      triggers = ("HLT_Mu13_Mu8_v2")      
    else:
      triggers = ("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v4","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v5"
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
      if runNumber>=160410 and runNumber<163269 : outcome = "HLT_DoubleMu6_v1" in pathnames
      if runNumber>=163269 and runNumber<165121 : outcome = "HLT_DoubleMu7_v2" in pathnames
      if runNumber>=165121  : outcome = "HLT_Mu13_Mu8_v2" in pathnames
    else:
      if runNumber>=132440 and runNumber<=137028 : outcome = "HLT_Photon10_L1R" # should impose a cut at 15 GeV by hand
      if runNumber>=138564 and runNumber<=140401 : outcome = "HLT_Photon15_Cleaned_L1R" in pathnames
      if runNumber>=141956 and runNumber<=144114 : outcome = "HLT_Ele15_SW_CaloEleId_L1R" in pathnames
      if runNumber>=146428 and runNumber<=147116 : outcome = "HLT_Ele17_SW_CaloEleId_L1R" in pathnames
      if runNumber>=147146 and runNumber<=148102 : outcome = "HLT_Ele17_SW_TightEleId_L1R" in pathnames
      if runNumber>=148783 and runNumber<=149063 : outcome = "HLT_Ele22_SW_TighterCaloIdIsol_L1R_v1" in pathnames
      if runNumber>=149181 and runNumber<=149442 : outcome = "HLT_Ele22_SW_TighterCaloIdIsol_L1R_v2" in pathnames

      if runNumber>=160410 and runNumber<161217 : outcome = "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1" in pathnames
      if runNumber>=161217 and runNumber<163269 : outcome = "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v2" in pathnames
      if runNumber>=163269 and runNumber<165121 : outcome = "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v3" in pathnames
      if runNumber>=165121 and runNumber<=165970 : outcome = "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v4" in pathnames
      if runNumber>=165970 : outcome = "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v5" in pathnames

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
  # if everything ok, return the result of the lepton check
  return result

def findBestCandidate(muChannel, *zCandidates):
  """Finds the best Z candidate. Might be none.
     As input, the function takes an arbitrary number of collections of Z candidates.
     muChannel specify if we have to consider only muons (true), electrons (false) or both (none)."""
  bestZ = None
  bestM = -1000.
  if muChannel is None:
    for col in zCandidates:
      for z in col:
        if not isZcandidate(z): continue
        if abs(z.mass()-91.1876)<abs(bestM-91.1876) :
          bestM = z.mass()
          bestZ = z
  else:
    for col in zCandidates:
      for z in col:
        if not isZcandidate(z): continue
	if (muChannel==True and z.daughter(0).isElectron() ) or (muChannel==False and z.daughter(0).isMuon()) : continue
        if abs(z.mass()-91.1876)<abs(bestM-91.1876) :
          bestM = z.mass()
          bestZ = z
  return bestZ

def findDijetPair(jets, bestZcandidate=None, btagging="SSV"):
  """Find the best jet pair: high Pt and btagging."""
  # check number of good jets
  indices = [index for index,jet in enumerate(jets) if isGoodJet(jet,bestZcandidate) ]
  if len(indices)<1: return (None, None)
  if len(indices)<2: return (jets[indices[0]],None)
  jetList = []
  # start with HP b-jets
  for index in indices[:]:
    if isBJet(jets[index],"HP",btagging):
      jetList.append(index)
      indices.remove(index)
  if len(jetList)>=2: return (jets[jetList[0]],jets[jetList[1]])
  # continue with HE b-jets
  for index in indices[:]:
    if isBJet(jets[index],"HE",btagging):
      jetList.append(index)
      indices.remove(index)
  if len(jetList)>=2: return (jets[jetList[0]],jets[jetList[1]])
  # fill with remaining good jets
  for index in indices:
    jetList.append(index)
  return (jets[jetList[0]],jets[jetList[1]])

def isInCategory(category, categoryTuple):
  """Check if the event enters category X, given the tuple computed by eventCategory."""
  # category 0: All
  if category==0:
    return categoryTuple[0]!= -1
  # category 1: Trigger
  elif category==1:
    return categoryTuple[0]==1
  # category 2: di-lepton
  elif category==2:
    return isInCategory( 1, categoryTuple) and categoryTuple[1]==1
  # category 3: mass cut
  elif category==3:
    return isInCategory( 2, categoryTuple) and categoryTuple[2]==1
  # category 4: Z+jet
  elif category==4:
    return isInCategory( 3, categoryTuple) and categoryTuple[3]>0
  # category 5:  Z+b (HE)
  elif category==5:
    return isInCategory( 4, categoryTuple) and categoryTuple[4]>0
  # category 6:  Z+b (HP)
  elif category==6:
    return isInCategory( 4, categoryTuple) and categoryTuple[5]>0
  # category 7:  Z+b (HE+MET)
  elif category==7:
    return isInCategory( 5, categoryTuple) and categoryTuple[7]>0
  # category 8:  Z+b (HP+MET)
  elif category==8:
    return isInCategory( 6, categoryTuple) and categoryTuple[7]>0
  # categoty 9:  Z+bb (HEHE)
  elif category==9:
    return isInCategory( 4, categoryTuple) and categoryTuple[4]>1
  # categoty 10: Z+bb (HEHP)
  elif category==10:
    return isInCategory( 4, categoryTuple) and categoryTuple[4]+categoryTuple[5]-categoryTuple[6] > 1 and categoryTuple[5] > 0
  # categoty 11: Z+bb (HPHP)
  elif category==11:
    return isInCategory( 4, categoryTuple) and categoryTuple[5]>1
  # categoty 12: Z+bb (HEHE+MET)
  elif category==12:
    return isInCategory( 9, categoryTuple) and categoryTuple[7]>0
  # categoty 13: Z+bb (HEHP+MET)
  elif category==13:
    return isInCategory(10, categoryTuple) and categoryTuple[7]>0
  # categoty 14: Z+bb (HPHP+MET)
  elif category==14:
    return isInCategory(11, categoryTuple) and categoryTuple[7]>0
  # other does not exist
  else:
    return False

def eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, muChannel=True, btagging="SSV"):
  """Check analysis requirements for various steps."""
  output = []
  bestZcandidate = findBestCandidate(muChannel, zCandidatesMu, zCandidatesEle)
  # output[0]: Trigger
  if isTriggerOK(triggerInfo, muChannel):
    output.append(1)
  else:
    output.append(0)
  # output[1], output[2]: di-lepton and mass cut
  if bestZcandidate is None:
    output.append(0)
    output.append(0)
  else: 
    output.append(1)
    if abs(bestZcandidate.mass()-91.1876)<30.:
      output.append(1)
    else:
      output.append(0)
  # output[3] -> output[6] : (b)jets
  nJets = 0
  nBjetsHE = 0
  nBjetsHP = 0
  nBjetsHEHP = 0
  for jet in jets:
    if isGoodJet(jet,bestZcandidate):
      nJets += 1
      HE = isBJet(jet,"HE",btagging)
      HP = isBJet(jet,"HP",btagging)
      if HE: nBjetsHE += 1
      if HP: nBjetsHP += 1
      if HE and HP: nBjetsHEHP +=1
  output.append(nJets)
  output.append(nBjetsHE)
  output.append(nBjetsHP)
  output.append(nBjetsHEHP)
  # output[7] : MET
  if isGoodMet(met[0]):
    output.append(1)
  else: 
    output.append(0)
  # return the list of results
  return output

def eventCategories(): return 15

