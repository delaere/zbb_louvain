import ROOT
import string
import intervalmap
from vertexAssociation import zVertex
from JetCorrectionUncertainty import JetCorrectionUncertaintyProxy
from zbbCommons import zbblabel
import monteCarloSelection
from math import sqrt

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
  return True

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
  return abs(electron.eta())<2.5 # and ( abs(electron.eta())< 1.442 or ( 1.566<abs(electron.eta()) and abs(electron.eta())<2.50 ) )
  ##return electron.eta()<2.5
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
  return abs(jet.eta())<2.4 and JECuncertaintyProxy.jetPt(jet)>20. and jetId(jet,"loose")

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
      print "Error: unforeseen working point for b-tagging. Use HE or HP"
      return False
  elif algo=="CSV":
    #HE is Loose WP and HP is Medium WP valid both for 2011 and 2012
    if workingPoint=="HE":
      return jet.bDiscriminator("combinedSecondaryVertexBJetTags")>0.244
    elif workingPoint=="HP":
      return jet.bDiscriminator("combinedSecondaryVertexBJetTags")>0.679
    else:
      print "Error: unforeseen working point for b-tagging. Use HE or HP"
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

def isTriggerMatchPair(l1,l2,runNumber,lumi_section):
  if l1.isMuon() :
    return True
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
      #if (l1.triggerObjectMatchesByPath("HLT_Mu17_*Mu8_*",0,1).size()>0 and l2.triggerObjectMatchesByPath("HLT_Mu17_*Mu8_*",0,1).size()>0) : # and (l1.triggerObjectMatchesByFilter("hltL3pfL1DoubleMu10MuOpen*L1f0L2pf0L3PreFiltered8").size()>0) and (l2.triggerObjectMatchesByFilter("hltL3pfL1DoubleMu10MuOpen*L1f0L2pf0L3PreFiltered8").size()>0 ) and l1.triggerObjectMatchesByFilter("hltL3fL1DoubleMu10MuOpen*L1f0L2f10L3Filtered17").size()>0) :
        #print runNumber
        
        #print l1.triggerObjectMatchesByFilter("hltL3fL1DoubleMu10MuOpen*L1f0L2f10L3Filtered17").size()>0			
        #print l2.triggerObjectMatchesByFilter("hltL3fL1DoubleMu10MuOpen*L1f0L2f10L3Filtered17").size()>0	
        
        #print l1.triggerObjectMatchesByFilter("*").size()>0
        #for i in range(0,l1.triggerObjectMatch(0).conditionNames().size()) : print "conditions", l1.triggerObjectMatch(0).conditionNames()[i]
        #for i in range(0,l1.triggerObjectMatch(0).filterLabels().size()) : print "labels", l1.triggerObjectMatch(0).filterLabels()[i]
        #for i in range(0,l1.triggerObjectMatch(0).pathNames().size()) : print "labels", l1.triggerObjectMatch(0).pathNames()[i]
      
      
      if (l1.triggerObjectMatchesByPath("HLT_Mu17_Mu8_v*",0,1).size()>0 and l2.triggerObjectMatchesByPath("HLT_Mu17_Mu8_v*",0,1).size()>0 and (l1.triggerObjectMatchesByFilter("hltL3pfL1DoubleMu10MuOpen*L1f0L2pf0L3PreFiltered8").size()>0) and (l2.triggerObjectMatchesByFilter("hltL3pfL1DoubleMu10MuOpen*L1f0L2pf0L3PreFiltered8").size()>0 ) and l1.triggerObjectMatchesByFilter("hltL3fL1DoubleMu10MuOpen*L1f0L2f10L3Filtered17").size()>0): 
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
       #print "run number > 165121"
           #print "l1.triggerObjectMatchesByPath(HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIso...) 0,1 " ,l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).size() 
       #print "l1.triggerObjectMatchesByPath(HLT_Ele17_CaloIdT_TrkIdVL_CaloIsoVL_TrkIso...) 0,1 " ,l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_v*",0,1).size() 
           #print "path * 0,1 " , (l1.triggerObjectMatchesByPath("*",0,0).size())
           #print "path * 1,0 " , (l1.triggerObjectMatchesByPath("*",1,0).size())
           if ((l1.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0) and (l1.triggerObjectMatchesByFilter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsoDoubleFilter").size()) and (l2.triggerObjectMatchesByPath("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",0,1).size()>0) and(l2.triggerObjectMatchesByFilter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsoDoubleFilter").size())) :
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

def findDijetPair(event, btagging="CSV", muChannel=True, eleChannel=False):
  """Find the best jet pair: high Pt and btagging."""
  # the proper goodJets list
  if muChannel and eleChannel:
    goodJets = event.goodJets_common
  elif muChannel:
    goodJets = event.goodJets_mu
  elif eleChannel:
    goodJets = event.goodJets_ele
  else:
    goodJets = event.goodJets
  # check number of good jets
  indices_pt = [index for index,jet in enumerate(event.jets) if goodJets[index] ]
  csvList = [(jet.bDiscriminator("combinedSecondaryVertexBJetTags"),index) for index,jet in enumerate(event.jets) if goodJets[index] ]
  csvList.sort(reverse=True)
  indices = []
  for icsv in csvList:
    indices.append(icsv[1])
  if len(indices)<1: return (None, None)
  if len(indices)<2: return (event.jets[indices[0]],None)
  jetList = []
  # start with HP b-jets
  for index in indices[:]:
    if isBJet(event.jets[index],"HP",btagging):
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
    if isBJet(event.jets[index],"HE",btagging):
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

categoryNames = [ 
  "Trigger", 
  "Z (wide)", 
  "Z (narrow)", 
  "Z+jet", 
  "Z+b (HE) wide", 
  "Z+b (HP) wide", 
  "Z+b (HE)", 
  "Z+b (HP)", 
  "Z+b (HE+MET significance)", 
  "Z+b (HP+MET significance)",
  "Z+bb (HEHE) wide", 
  "Z+bb (HEHP) wide", 
  "Z+bb (HPHP) wide", 
  "Z+bb (HEHE)", 
  "Z+bb (HEHP)", 
  "Z+bb (HPHP)", 
  "Z+bb (HEHE+MET significance)", 
  "Z+bb (HEHP+MET significance)", 
  "Z+bb (HPHP+MET significance)",
]

def eventCategories(): return len(categoryNames)

def categoryName(category):
  """Check if the event enters category X, given the tuple computed by eventCategory."""
  if category<eventCategories() and category>=0: return categoryNames[category]
  else: return "None"

def isInCategory(category, categoryTuple):
  """Check if the event enters category X, given the tuple computed by eventCategory."""
  # category 0: Trigger
  if category==0:
    return categoryTuple[0]==1
  # category 1: Z candidate (wide mass window)
  elif category==1:
    return isInCategory( 0, categoryTuple) and categoryTuple[1]==1 and categoryTuple[2]<30.
  # category 2: Z candidate (narrow mass window)
  elif category==2:
    return isInCategory( 0, categoryTuple) and categoryTuple[1]==1 and categoryTuple[2]<15.
  # category 3: Z+jet
  elif category==3:
    return isInCategory( 2, categoryTuple) and categoryTuple[3]>0
  # category 4:  Z+b (HE), wide mass window
  elif category==4:
    return isInCategory( 1, categoryTuple) and categoryTuple[3]>0 and categoryTuple[4]>0
  # category 5:  Z+b (HP), wide mass window
  elif category==5:
    return isInCategory( 1, categoryTuple) and categoryTuple[3]>0 and categoryTuple[5]>0
  # category 6:  Z+b (HE)
  elif category==6:
    return isInCategory( 3, categoryTuple) and categoryTuple[4]>0
  # category 7:  Z+b (HP)
  elif category==7:
    return isInCategory( 3, categoryTuple) and categoryTuple[5]>0
  # category 8:  Z+b (HE+MET_significance)
  elif category==8:
    return isInCategory( 6, categoryTuple) and categoryTuple[8]>0
  # category 9:  Z+b (HP+MET_significance)
  elif category==9:
    return isInCategory( 7, categoryTuple) and categoryTuple[8]>0
  # categoty 10: Z+bb (HEHE), wide mass window
  elif category==10:
    return isInCategory( 4, categoryTuple) and categoryTuple[4]>1
  # categoty 11: Z+bb (HEHP), wide mass window
  elif category==11:
    return isInCategory( 5, categoryTuple) and categoryTuple[4]+categoryTuple[5]-categoryTuple[6] > 1
  # categoty 12: Z+bb (HPHP), wide mass window
  elif category==12:
    return isInCategory( 5, categoryTuple) and categoryTuple[5]>1
  # categoty 13: Z+bb (HEHE)
  elif category==13:
    return isInCategory( 3, categoryTuple) and categoryTuple[4]>1
  # categoty 14: Z+bb (HEHP)
  elif category==14:
    return isInCategory( 3, categoryTuple) and categoryTuple[4]+categoryTuple[5]-categoryTuple[6] > 1 and categoryTuple[5] > 0
  # categoty 15: Z+bb (HPHP)
  elif category==15:
    return isInCategory( 3, categoryTuple) and categoryTuple[5]>1
  # categoty 16: Z+bb (HEHE+MET_significance)
  elif category==16:
    return isInCategory(13, categoryTuple) and categoryTuple[8]>0
  # categoty 17: Z+bb (HEHP+MET_significance)
  elif category==17:
    return isInCategory(14, categoryTuple) and categoryTuple[8]>0
  # categoty 18: Z+bb (HPHP+MET_significance)
  elif category==18:
    return isInCategory(15, categoryTuple) and categoryTuple[8]>0
  # other does not exist
  else:
    return False

#TODO: replace the checkTrigger flag by isData
def eventCategory(event, muChannel=True, eleChannel=True, btagging="CSV", ZjetFilter="bcl", checkTrigger=True, perRun=True):
  """Check analysis requirements for various steps."""
  # first of all: ZjetFilter. If failed, we don't even evaluate the rest of the vector and we return the special -1 value.
  if not ZjetFilter=="bcl":
    if ('bb' in ZjetFilter) or ('bx' in ZjetFilter) or ('xx' in ZjetFilter) :
      if monteCarloSelection.isZbbEvent(event) and not ('bb' in ZjetFilter): return [-1]
      if (monteCarloSelection.isZbcEvent(event) or monteCarloSelection.isZblEvent(event)) and not ('bx' in ZjetFilter): return [-1]
      if not monteCarloSelection.isZbEvent(event) and not ('xx' in ZjetFilter): return [-1]
    else :
      if monteCarloSelection.isZbEvent(event) and not ('b' in ZjetFilter): return [-1]
      if (monteCarloSelection.isZcEvent(event) and not monteCarloSelection.isZbEvent(event)) and not ('c' in ZjetFilter): return [-1]
      if (not monteCarloSelection.isZcEvent(event) and not monteCarloSelection.isZbEvent(event)) and not ('l' in ZjetFilter): return [-1]
  output = []
  if muChannel and eleChannel:
    bestZcandidate = event.bestZcandidate
    goodJets = event.goodJets_all
  elif muChannel:
    bestZcandidate = event.bestZmumuCandidate
    goodJets = event.goodJets_mu
  elif eleChannel:
    bestZcandidate = event.bestZelelCandidate
    goodJets = event.goodJets_ele
  # output[0]: Trigger
  if checkTrigger==False or (event.isMuTriggerOK and muChannel) or (event.isEleTriggerOK and eleChannel):
    output.append(1)
  else:
    output.append(0)
  # output[1], output[2]: di-lepton and mass cut
  if bestZcandidate is None:
    output.append(0)
    output.append(0)
  else: 
    output.append(1)
    output.append(abs(bestZcandidate.mass()-91))
  # output[3] -> output[6] : (b)jets
  nJets = 0
  nBjetsHE = 0
  nBjetsHP = 0
  nBjetsHEHP = 0
  for index,jet in enumerate(event.jets):
    if goodJets[index]:
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
  if isGoodMet(event.MET[0]):
    output.append(1)
  else: 
    output.append(0)
  # output[8] : MET Significance
  if isGoodMet_Sig(event.MET[0]):
    output.append(1)
  else: 
    output.append(0)
  # additional quantities. For now, put the floats... might become cuts later on.
  # output[9] : Z Pt
  if bestZcandidate is None:
    output.append(-1)
  else:
    output.append(bestZcandidate.pt())
  # output[10] : delta R (bb)
  # output[11] : delta R (bb) via SV
  dijet = findDijetPair(event, btagging, muChannel, eleChannel)
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
  #print output
  return output

def prepareAnalysisEvent(event, btagging="CSV",ZjetFilter="bcl",checkTrigger=True):
  # collections
  event.addCollection("lheParticles","LHEEventProduct","source")
  event.addCollection("genParticles","vector<reco::GenParticle>",zbblabel.genlabel)
  event.addCollection("genJets","vector<reco::GenJet>",zbblabel.genjetlabel)
  event.addCollection("genInfo","GenEventInfoProduct",zbblabel.genInfolabel)
  event.addCollection("vertices","vector<reco::Vertex>",zbblabel.vertexlabel)
  event.addCollection("jets","vector<pat::Jet>",zbblabel.jetlabel)
  event.addCollection("MET","vector<pat::MET>",zbblabel.metlabel)
  event.addCollection("METNNregression","vector<pat::MET>","patMETsPF")
  event.addCollection("Zmumu","vector<reco::CompositeCandidate>",zbblabel.zmumulabel)
  event.addCollection("Zelel","vector<reco::CompositeCandidate>",zbblabel.zelelabel)
  event.addCollection("triggerInfo","pat::TriggerEvent",zbblabel.triggerlabel)
  event.addCollection("electrons","vector<pat::Electron>",zbblabel.electronlabel)
  event.addCollection("muons","vector<pat::Muon>",zbblabel.muonlabel)
  event.addCollection("allelectrons","vector<pat::Electron>",zbblabel.allelectronslabel)
  event.addCollection("allmuons","vector<pat::Muon>",zbblabel.allmuonslabel)
  event.addCollection("PileupSummaryInfo","std::vector< PileupSummaryInfo >",zbblabel.pulabel)
  event.addCollection("rho","double",(zbblabel.rholabel,"rho"))

  # producers
  event.addProducer("vertex",vertex)
  event.addProducer("goodJets_mu",goodJets,muChannel=True,eleChannel=False)
  event.addProducer("goodJets_ele",goodJets,muChannel=False,eleChannel=True)
  event.addProducer("goodJets_all",goodJets,muChannel=True,eleChannel=True)
  event.addProducer("goodJets_none",goodJets,muChannel=False,eleChannel=False)
  event.addProducer("isMuTriggerOK",isTriggerOK,muChannel=True,eleChannel=False,perRun=True)
  event.addProducer("isEleTriggerOK",isTriggerOK,muChannel=False,eleChannel=True,perRun=True)
  event.addProducer("isTriggerOK",isTriggerOK,muChannel=True,eleChannel=True,perRun=True)
  event.addProducer("catMu",eventCategory,muChannel=True,eleChannel=False,btagging=btagging,ZjetFilter=ZjetFilter,checkTrigger=checkTrigger,perRun=True)
  event.addProducer("catEle",eventCategory,muChannel=False,eleChannel=True,btagging=btagging,ZjetFilter=ZjetFilter,checkTrigger=checkTrigger,perRun=True)
  event.addProducer("bestZmumuCandidate",findBestCandidate,muChannel=True,eleChannel=False)
  event.addProducer("bestZelelCandidate",findBestCandidate,muChannel=False,eleChannel=True)
  event.addProducer("bestZcandidate",findBestCandidate,muChannel=True,eleChannel=True)
  event.addProducer("dijet_muChannel",findDijetPair,btagging=btagging,muChannel=True,eleChannel=False)
  event.addProducer("dijet_eleChannel",findDijetPair,btagging=btagging,muChannel=False,eleChannel=True)
  #event.addProducer("bbHE",candidateproducer,candidate="bbHE")
  #event.addProducer("bbHP",candidateproducer,candidate="bbHP")
  #event.addProducer("ZbHE",candidateproducer,candidate="ZbHE")
  #event.addProducer("ZbHP",candidateproducer,candidate="ZbHP")
  #event.addProducer("ZbbHE",candidateproducer,candidate="ZbbHE")
  #event.addProducer("ZbbHP",candidateproducer,candidate="ZbbHP")

  #from other modules
  monteCarloSelection.prepareAnalysisEvent(event)

