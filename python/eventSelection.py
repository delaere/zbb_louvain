import ROOT
import string

def selectedTriggers(triggerInfo):
  if triggerInfo is None:
    return []

  triggers = ("HLT_DoubleMu6_v1","HLT_DoubleMu7_v2","HLT_Mu13_Mu8_v2","HLT_Mu13_Mu8_v3","HLT_Mu13_Mu8_v4","HLT_Mu13_Mu8_v6","HLT_Mu13_Mu8_v7","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v2","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v3","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v4","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v5","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v6","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v5","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v7","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v5","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v8")
              
  paths = map(lambda trigger: triggerInfo.path(trigger),triggers)
  def isFired(path):
    if not path is None: 
      path.wasAccept() # error ReferenceError: attempt to access a null-pointer..... should change name
    else: 
      False
  pathout = map(lambda path:isFired(path),paths)
  return pathout

def isTriggerOK(triggerInfo, zCandidate, runNumber, muChannel=True):
  """Checks if the proper trigger is passed"""
  # simple case: mu trigger for mu channel (1), ele trigger for ele channel (0)
  # more complex case: different trigger for various run ranges (lowest unprescaled)
  if triggerInfo is None:
    return True
  paths = triggerInfo.acceptedPaths()
  pathnames = map(lambda i: paths[i].name(),range(paths.size()))
  #print "trigger path" , pathnames 
  if runNumber is None:
    if muChannel:
      triggers = ("HLT_DoubleMu6_v1","HLT_DoubleMu7_v2","HLT_Mu13_Mu8_v2","HLT_Mu13_Mu8_v3","HLT_Mu13_Mu8_v4","HLT_Mu13_Mu8_v7")      
    else:
      triggers = ("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v2","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v3","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v4","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v5","HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v6","HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6","HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v7","HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v8" )

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

      if runNumber>=160410 and runNumber<163269 :
        #print " path = HLT_DoubleMu6_v1" 
        outcome = "HLT_DoubleMu6_v1" in pathnames
        
      if runNumber>=163269 and runNumber<165121 :
        outcome = "HLT_DoubleMu7_v2" in pathnames
                
      if runNumber>=165121 and runNumber<167039 :
        outcome = "HLT_Mu13_Mu8_v2" in pathnames
                
      if runNumber>=167039 and runNumber<170249 :
        outcome = "HLT_Mu13_Mu8_v2" in pathnames
        if outcome==False:
          outcome = "HLT_Mu13_Mu8_v3" in pathnames
          if outcome==False:
            outcome = "HLT_Mu13_Mu8_v4" in pathnames
      if runNumber>=170249 :
        outcome = "HLT_Mu13_Mu8_v6" in pathnames
        if outcome==False:
          outcome = "HLT_Mu13_Mu8_v7" in pathnames
    else:
      if runNumber>=132440 and runNumber<=137028 : outcome = "HLT_Photon10_L1R" # should impose a cut at 15 GeV by hand
      if runNumber>=138564 and runNumber<=140401 : outcome = "HLT_Photon15_Cleaned_L1R" in pathnames
      if runNumber>=141956 and runNumber<=144114 : outcome = "HLT_Ele15_SW_CaloEleId_L1R" in pathnames
      if runNumber>=146428 and runNumber<=147116 : outcome = "HLT_Ele17_SW_CaloEleId_L1R" in pathnames
      if runNumber>=147146 and runNumber<=148102 : outcome = "HLT_Ele17_SW_TightEleId_L1R" in pathnames
      if runNumber>=148783 and runNumber<=149063 : outcome = "HLT_Ele22_SW_TighterCaloIdIsol_L1R_v1" in pathnames
      if runNumber>=149181 and runNumber<=149442 : outcome = "HLT_Ele22_SW_TighterCaloIdIsol_L1R_v2" in pathnames

      if runNumber>=160410 and runNumber<161217 :
        outcome = "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1" in pathnames
      if runNumber>=161217 and runNumber<163269 :
        outcome = "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v2" in pathnames
      if runNumber>=163269 and runNumber<165121 :
        outcome = "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v3" in pathnames
      if runNumber>=165121 and runNumber<165970 :
        outcome = "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v4" in pathnames
      if runNumber>=165970 and runNumber<167039 :
        outcome = "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v5" in pathnames
      if runNumber>=167039 and runNumber<170249 :
        outcome = "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v6" in pathnames
      if runNumber>=170249 :
        outcome = "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6" in pathnames
        if outcome == False:
          outcome = "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v7" in pathnames
          if outcome == False:
            outcome = "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v8" in pathnames

  #print "outcome ", outcome, "  triggerMatched : ", isTriggerMatchZcandidate(zCandidate,runNumber)
  return (outcome and isTriggerMatchZcandidate(zCandidate,runNumber))

def isLooseMuon(muon):
  """Perform additional checks that define a loose muon"""
  # see https://server06.fynu.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/Zbbmuonselection

  # anything on top of PAT cfg ?
  # cleaning ?

  return True

def isTightMuon(muon):
  """Perform additional checks that define a tight muon"""
  # see https://server06.fynu.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/Zbbmuonselection
  # to requires both muons to be matched
  #if muon().triggerObjectMatches().size()>0 :
  #if muMatches(muon).size() > 0 :
  # anything else on top of PAT cfg ?
  # cleaning ?
  
  if muon.hasMasterClone():
    mu = muon.masterClone()
    ROOT.SetOwnership( mu, False ) 
  else:
    mu = muon
  isMatched = mu.triggerObjectMatches().size()>0
  # don't impose matching for tight muons because the trigger -> should now be in the PAT anyway.
  #isMatched = True

  return (isLooseMuon(muon) and isMatched)

def isMatchedMuon(muon):
  """Perform additional checks that define a matched muon"""
  # see https://server06.fynu.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/Zbbmuonselection

  # anything else on top of PAT cfg ?
  # cleaning ?

  return (isTightMuon(muon) and True)

def isGoodMuon(muon,role):
  """Perform additional checks that define a good muon"""
  if string.find(role,"loose")!=-1   : return isLooseMuon(muon)
  if string.find(role,"tight")!=-1   : return isTightMuon(muon)
  if string.find(role,"matched")!=-1 : return isMatchedMuon(muon)
  if string.find(role,"none")!=-1    : return True
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
  #to correct the PAT error (temporary)
  if electron.pt()<25. : return False
 
  # impose matching and fiducial cut
  if electron.hasMasterClone():
    el = electron.masterClone()
    ROOT.SetOwnership( el, False ) 
  else:
    el = electron
    
  isID85 = el.electronID("simpleEleId85relIso")== 7  
  isEta = abs(el.eta())< 2.5  
  isdB = abs(el.dB())< 0.02 
  isMatched = el.triggerObjectMatches().size()>0
  #isMatched = True # for MC and data: now matching is enforced directly in the PAT. temporary correction due to PAT error
  superclusterEta = abs(el.superCluster().eta())
  fiducialCut = superclusterEta<1.4442 or (superclusterEta>1.566 and superclusterEta<2.5 )

  return (isLooseElectron(electron) and isID85 and isEta and isdB and isMatched and fiducialCut)

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
  if string.find(role,"loose")!=-1   : return isLooseElectron(electron)
  if string.find(role,"tight")!=-1   : return isTightElectron(electron)
  if string.find(role,"matched")!=-1 : return isMatchedElectron(electron)
  if string.find(role,"none")!=-1    : return True
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
  # to study the impact of PU on MC, request the jet to be matched to a genjet
  # outcome = outcome and not (jet.genJet() is None)
  # TODO: add vertex match (?)
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
  #TODO: add vertex match
  # if everything ok, return the result of the lepton check
  return result

def isTriggerMatchZcandidate(zCandidate, runNumber):
  if not zCandidate is None:
    daughter1 = zCandidate.daughter(0)
    daughter2 = zCandidate.daughter(1)
    Daugh1 = daughter1.masterClone()
    ROOT.SetOwnership( Daugh1, False )
    Daugh2 = daughter2.masterClone()
    ROOT.SetOwnership( Daugh2, False )
    case1 =  isTriggerMatchPair(Daugh1,Daugh2,runNumber) 
    case2 = isTriggerMatchPair(Daugh2,Daugh1,runNumber)
    #print "isTriggerMatchZcandidate decisions: ", case1, case2
    return (case1 or case2)
    #return (isTriggerMatchPair(Daugh1,Daugh2,runNumber) or isTriggerMatchPair(Daugh2,Daugh1,runNumber))
  else:
    return False

def isTriggerMatchPair(l1,l2,runNumber):
    
  if l1.isMuon() :
    print "Muons"
    print "run number", runNumber
    if runNumber>=160410 and runNumber<163269 :
      #print "l1.triggerObjectMatchesByPath(HLT_DoubleMu6_v*) size", (l1.triggerObjectMatchesByPath("HLT_DoubleMu6_v*",1,0).size())
      if (l1.triggerObjectMatchesByPath("HLT_DoubleMu6_v*",1,0).size()>0) and (l2.triggerObjectMatchesByPath("HLT_DoubleMu6_v*",1,0).size()>0) :
        return True
    
    if runNumber>=163269 and runNumber<165121 :
      #print "l1.triggerObjectMatchesByPath(HLT_DoubleMu7_v*) size", (l1.triggerObjectMatchesByPath("HLT_DoubleMu7_v*",1,0).size())
      if (l1.triggerObjectMatchesByPath("HLT_DoubleMu7_v*",1,0).size()>0) and (l2.triggerObjectMatchesByPath("HLT_DoubleMu7_v*",1,0).size()>0):
        return True
        
    if runNumber >= 165121 :
      #print "l1.triggerObjectMatchesByPath(HLT_Mu13_Mu8_v*) size", (l1.triggerObjectMatchesByPath("HLT_Mu13_Mu8_v*",0,0).size())
      #print "l1.triggerObjectMatchesByFilter(hltDiMuonL3PreFiltered8) size",(l1.triggerObjectMatchesByFilter("hltDiMuonL3PreFiltered8").size())
      #print "l1.triggerObjectMatchesByFilter(hltSingleMu13L3Filtered13) size",(l1.triggerObjectMatchesByFilter("hltSingleMu13L3Filtered13").size())
      #print "l2.triggerObjectMatchesByPath(HLT_Mu13_Mu8_v*) size", (l2.triggerObjectMatchesByPath("HLT_Mu13_Mu8_v*",0,0).size())
      #print "l2.triggerObjectMatchesByFilter(hltDiMuonL3PreFiltered8) size",(l2.triggerObjectMatchesByFilter("hltDiMuonL3PreFiltered8").size())

      if (l1.triggerObjectMatchesByPath("HLT_Mu13_Mu8_v*",0,0).size()>0) and (l2.triggerObjectMatchesByPath("HLT_Mu13_Mu8_v*",0,0).size()>0) and ((l1.triggerObjectMatchesByFilter("hltDiMuonL3PreFiltered8").size()>0) or (l1.triggerObjectMatchesByFilter("hltDiMuonL3p5PreFiltered8").size()>0)) and ((l2.triggerObjectMatchesByFilter("hltDiMuonL3PreFiltered8").size()>0) or (l2.triggerObjectMatchesByFilter("hltDiMuonL3p5PreFiltered8").size()>0)) and (l1.triggerObjectMatchesByFilter("hltSingleMu13L3Filtered13").size()>0):
        return True
      
  if l1.isElectron() :
    if runNumber < 167039 :
      return True
    #if runNumber < 165121:
      #print "l1.triggerObjectMatchesByPath(HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*)size 0 1", (l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",0,1).size())
      #print "path *" , (l1.triggerObjectMatchesByPath("*",1,0))
      #print "filter_1 *",(l1.triggerObjectMatchesByFilter("hltEle17CaloIdIsoEle8CaloIdIsoPixelMatchDoubleFilter").size())
      #print "l2.triggerObjectMatchesByPath(HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*)size 0 1", (l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",0,1).size())
      #print "filter_2 *",(l2.triggerObjectMatchesByFilter("hltEle17CaloIdIsoEle8CaloIdIsoPixelMatchDoubleFilter").size())
      #if (l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",1,0).size()>0) and (l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",1,0).size()>0) :
        #return True
    
    #if runNumber >= 165121 and runNumber < 167039 :
      #print "l1.triggerObjectMatchesByPath(HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*)size 1 0", (l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",1,0).size())
      #print "path *" , (l1.triggerObjectMatchesByPath("*",1,0))
      #print "filter_1 *",(l1.triggerObjectMatchesByFilter("hltEle17CaloIdIsoEle8CaloIdIsoPixelMatchDoubleFilter").size())
      #print "l2.triggerObjectMatchesByPath(HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*)size 1 0", (l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",1,0).size())
      #print "filter_2 *",(l2.triggerObjectMatchesByFilter("hltEle17CaloIdIsoEle8CaloIdIsoPixelMatchDoubleFilter").size())
      #if (l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",0,1).size()>0) and (l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",0,1).size()>0):
        #return True

    if runNumber >= 167039 :
      #print "l1.triggerObjectMatchesByPath(HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*) size", (l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).size())
      #print "filter_1 *", (l1.triggerObjectMatchesByFilter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter").size())
      #print "(l2.triggerObjectMatchesByPath(HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*) size", (l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).size())
      #print "filter_2 *", (l1.triggerObjectMatchesByFilter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter").size())
      if (l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).size()>0) and (l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).size()>0):
        return True
        
  return False

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

categoryNames = [ 
  "All", 
  "Trigger", 
  "di-lepton", 
  "Z", 
  "Z+jet", 
  "Z+b (HE)", 
  "Z+b (HP)", 
  "Z+b (HE+MET)", 
  "Z+b (HP+MET)", 
  "Z+bb (HEHE)", 
  "Z+bb (HEHP)", 
  "Z+bb (HPHP)", 
  "Z+bb (HEHE+MET)", 
  "Z+bb (HEHP+MET)", 
  "Z+bb (HPHP+MET)", 
  "Z+1b (HE exclusive)", 
  "Z+1b (HP exclusive)",
  "Z+1b (HE exclusive + MET)",
  "Z+1b (HP exclusive + MET)",
  "Z+bb (HEHE) + Zpt cut",
  "Z+bb (HEHE) + dR(SV) cut",
  "Z+bb (HPHP+MET) + Zpt cut",
  "Z+bb (HPHP+MET) + dR(SV) cut",
]

def eventCategories(): return len(categoryNames)

def categoryName(category):
  """Check if the event enters category X, given the tuple computed by eventCategory."""
  if category<eventCategories() and category>=0: return categoryNames[category]
  else: return "None"

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
  # categoty 15: Z+1b (HE exclusive)
  elif category==15:
    return isInCategory( 4, categoryTuple) and categoryTuple[4]==1 and categoryTuple[5]==categoryTuple[6]
  # categoty 16: Z+1b (HP exclusive)
  elif category==16:
    return isInCategory( 4, categoryTuple) and categoryTuple[5]==1 and categoryTuple[4]==categoryTuple[6]  
  # categoty 17: Z+1b (HE exclusive + MET)
  elif category==17:
    return isInCategory( 15, categoryTuple ) and categoryTuple[7]>0
  # categoty 18: Z+1b (HP exclusive + MET)
  elif category==18:
    return isInCategory( 16, categoryTuple ) and categoryTuple[7]>0
  # some temporary stuff
  elif category==19:
    return isInCategory(9, categoryTuple) and categoryTuple[8]>80 # and categoryTuple[8]<120
  elif category==20:
    return isInCategory(9, categoryTuple) and categoryTuple[10]>0.6 and categoryTuple[10]<1.1 and categoryTuple[8]>80 
  elif category==21:
    return isInCategory(14, categoryTuple) and categoryTuple[8]>80 # and categoryTuple[8]<120
  elif category==22:
    return isInCategory(14, categoryTuple) and categoryTuple[10]>0.6 and categoryTuple[10]<1.1 and categoryTuple[8]>80 
  # other does not exist
  else:
    return False

def eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, runNumber, muChannel=True, btagging="SSV", massWindow=30.):
  """Check analysis requirements for various steps."""
  output = []
  bestZcandidate = findBestCandidate(muChannel, zCandidatesMu, zCandidatesEle)
  # output[0]: Trigger
  if isTriggerOK(triggerInfo,bestZcandidate, runNumber, muChannel):
    output.append(1)
    #print "passed"
  else:
    output.append(0)
  # output[1], output[2]: di-lepton and mass cut
  if bestZcandidate is None:
    output.append(0)
    output.append(0)
  else: 
    output.append(1)
    if abs(bestZcandidate.mass()-90)<massWindow: #to comply with the others
#    if abs(bestZcandidate.mass()-91.1876)<massWindow:
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
  # additional quantities. For now, put the floats... might become cuts later on.
  # output[8] : Z Pt
  if bestZcandidate is None:
    output.append(-1)
  else:
    output.append(bestZcandidate.pt())
  # output[9] : delta R (bb)
  # output[10] : delta R (bb) via SV
  dijet = findDijetPair(jets, bestZcandidate, btagging)
  if dijet[0] is None or dijet[1] is None: 
    output.append(-1)
    output.append(-1)
  else:
    b1 = ROOT.TLorentzVector(dijet[0].px(),dijet[0].py(),dijet[0].pz(),dijet[0].energy())
    b2 = ROOT.TLorentzVector(dijet[1].px(),dijet[1].py(),dijet[1].pz(),dijet[1].energy())
    output.append(b1.DeltaR(b2))
    if dijet[0].tagInfoSecondaryVertex("secondaryVertex").nVertices()>0 and dijet[1].tagInfoSecondaryVertex("secondaryVertex").nVertices()>0:
      b1SVvec = dijet[0].tagInfoSecondaryVertex("secondaryVertex").flightDirection(0)
      b1SV = ROOT.TVector3(b1SVvec.x(),b1SVvec.y(),b1SVvec.z())
      b2SVvec = dijet[1].tagInfoSecondaryVertex("secondaryVertex").flightDirection(0)
      b2SV = ROOT.TVector3(b2SVvec.x(),b2SVvec.y(),b2SVvec.z())
      output.append(b1SV.DeltaR(b2SV))
    else:
      output.append(-1)
  # return the list of results
  return output

