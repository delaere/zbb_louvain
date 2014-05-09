import ROOT
import string
import intervalmap
from VertexAssociation import zVertex
from JetCorrectionUncertainty import JetCorrectionUncertaintyProxy
from math import sqrt
from zbbConfig import configuration

JECuncertaintyProxy = JetCorrectionUncertaintyProxy()
btagging=configuration.btagging

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
# merged lists of triggers
ourtriggers.mutriggers = list(set([item for sublist in [i for i in ourtriggers.murunMap.values()] for item in sublist]))
ourtriggers.eltriggers = list(set([item for sublist in [i for i in ourtriggers.elrunMap.values()] for item in sublist]))
ourtriggers.triggers   = list(set(ourtriggers.mutriggers) | set(ourtriggers.eltriggers))
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
    if muChannel:
      intersect = set(pathnames) & set(ourtriggers.mutriggers)
    else:
      intersect = set(pathnames) & set(ourtriggers.eltriggers)
  else:
    if muChannel:
      if ourtriggers.murunMap[runNumber] is None:
        print "muon unexpected runNumber : " , runNumber
        intersect = set()
      else:  
        intersect = set(pathnames) & set(ourtriggers.murunMap[runNumber])
    else:
      if ourtriggers.elrunMap[runNumber] is None:
        print "electron unexpected runNumber : " , runNumber
        intersect = set()
      else:  
        intersect = set(pathnames) & set(ourtriggers.elrunMap[runNumber])
  outcome = len(intersect)>0
  return (outcome and isTriggerMatchZcandidate(bestZcandidate,runNumber,event.lumi()))

def isLooseMuon(muon):
  """Perform additional checks that define a loose muon"""
  # see https://server06.fynu.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/Zbbmuonselection
  # anything on top of PAT cfg ?
  # cleaning ?
  #return True
  return muon.pt()>20.

def isTightMuon(muon):
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
  return (isLooseMuon(muon))

def isMatchedMuon(muon):
  """Perform additional checks that define a matched muon"""
  # see https://server06.fynu.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/Zbbmuonselection
  # anything else on top of PAT cfg ?
  # cleaning ?
  return (isTightMuon(muon) and True)

def isGoodMuon(muon,role):
  """Perform additional checks that define a good muon"""
  if string.find(role,"all")!=-1     : return isLooseMuon(muon)
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
  # overlap checking
  if not Z is None :
    if not hasNoOverlap(jet,Z) :
      return False 
  # pt, eta, and jetid
  return abs(jet.eta())<2.4 and JECuncertaintyProxy.jetPt(jet)>30. and jetId(jet,"loose")

def goodJets(event, muChannel=True, eleChannel=True):
  # best Z candidate
  if muChannel and eleChannel:
    bestZcandidate = event.bestZcandidate
  elif muChannel:
    bestZcandidate = event.bestZmumuCandidate
  elif eleChannel:
    bestZcandidate = event.bestZelelCandidate
  else:
    bestZcandidate = None
  # compute the good jets
  return map(lambda jet:isGoodJet(jet,bestZcandidate),event.jets)

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
    print "Error: unforeseen algo for b-tagging. Use SSV or CSV"
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
  #returns the 3D error of the http://31.media.tumblr.com/b31acfdd73732a25d45104495be8b617/tumblr_mig7og0YbH1r5xpw1o1_250.gifSV jet if it exists
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

def isTriggerMatchPair(l1,l2,runNumber,lumi_section):
  if l1.isMuon() :
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
        
  if l1.isElectron() :
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
    csvList = [(jet.bDiscriminator("combinedSecondaryVertexBJetTags"),index) for index,jet in enumerate(event.jets) if goodJets[index] ]
  elif btagging == "JP":
    csvList = [(jet.bDiscriminator("jetProbabilityBJetTags"),index) for index,jet in enumerate(event.jets) if goodJets[index] ]
    
  csvList.sort(reverse=True)
  indices = []
  for icsv in csvList:
    indices.append(icsv[1])
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

