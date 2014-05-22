import ROOT
import MonteCarloSelection
from ObjectSelection import *
import os
confCfg = os.environ["PatAnalysisCfg"]
if confCfg : from UserCode.zbb_louvain.PatAnalysis.CPconfig import configuration
else : from zbbConfig import configuration

#########################################################################
#  Standard methods  ####################################################
#########################################################################

# Everything is duplicated for Electrons and Muons. 
# For simplicity and clarity, methods are defined generically for each
# and the final (public) methods work by concatenating/splitting 

channels = [ "Muon", "Electron" ]

categories = [ 
  "Trigger", 
  "non Z (small)", 
  "non Z (big)", 
  "e-mu + jets", 
  "small inv. mass + 2b (HEHE)", 
  "small inv. mass + 2b (HEHP)", 
  "small inv. mass + 2b (HPHP)", 
  "small inv. mass + 2b (HEHE) + METSIG", 
]

categoryNames = [ chan+"/"+cat for chan in channels for cat in categories ]

def isInCategory(category, categoryTuple):
  if category<len(categories):
    return isInCategoryChannel(category%len(categories), categoryTuple[:len(categoryTuple)/2])
  else:
    return isInCategoryChannel(category%len(categories), categoryTuple[len(categoryTuple)/2:])

def isInCategoryChannel(category, categoryTuple):
  """Check if the event enters category X, given the tuple computed by eventCategory."""
  # category 0: Trigger
  if category==0:
    return categoryTuple[0]==1
  # category 1: non Z candidate (small inv. mass)
  elif category==1:
    return isInCategoryChannel( 0, categoryTuple) and categoryTuple[1]==1 and categoryTuple[2]<75. 
  # category 2: non Z candidate (big inv. mass)
  elif category==2:
    return isInCategoryChannel( 0, categoryTuple) and categoryTuple[1]==1 and categoryTuple[2]>110.
  # category 3: e-mu+jet
  elif category==3:
    return isInCategoryChannel( 0, categoryTuple) and categoryTuple[3]>0 and categoryTuple[4]>0 and categoryTuple[5]>0
  # categoty 4: small inv. mass + 2b (HEHE)
  elif category==4:
    return isInCategoryChannel( 1, categoryTuple) and categoryTuple[7]>1
  # categoty 5: small inv. mass + 2b  (HEHP)
  elif category==5:
    return isInCategoryChannel( 1, categoryTuple) and categoryTuple[6]+categoryTuple[7]-categoryTuple[8] > 1 and categoryTuple[7] > 0
  # categoty 6: small inv. mass + 2b (HPHP)
  elif category==6:
    return isInCategoryChannel( 1, categoryTuple) and categoryTuple[7]>1
  # categoty 7: small inv. mass + 2b  (HEHE) + Met sig
  elif category==7:
    return isInCategoryChannel(4, categoryTuple) and categoryTuple[8]>0
  # categoty 17: Z+bb (HEHP+MET_significance)
  else:
    return False

def eventCategory(event,btagging="CSV", WP=["M","L"], ZjetFilter="bcl"):
  if event.object().event().eventAuxiliary().isRealData():
    configuration.JERfactor = 0
    configuration.JESfactor = 0
  return eventCategoryChannel(event, muChannel=configuration.muChannel, eleChannel=False,btagging=btagging, WP=WP, ZjetFilter=ZjetFilter) + \
         eventCategoryChannel(event, muChannel=False, eleChannel=configuration.eleChannel,btagging=btagging, WP=WP, ZjetFilter=ZjetFilter)
  
def eventCategoryChannel(event, muChannel=True, eleChannel=True, btagging="CSV", WP=["M","L"], ZjetFilter="bcl"):
  """Check analysis requirements for various steps."""
  # first of all: ZjetFilter. If failed, we don't even evaluate the rest of the vector and we return the special -1 value.
  if not ZjetFilter=="bcl":
    if MonteCarloSelection.isZbEvent(event) and not ('b' in ZjetFilter): return [-1]
    if (MonteCarloSelection.isZcEvent(event) and not MonteCarloSelection.isZbEvent(event)) and not ('c' in ZjetFilter): return [-1]
    if (not MonteCarloSelection.isZcEvent(event) and not MonteCarloSelection.isZbEvent(event)) and not ('l' in ZjetFilter): return [-1]
  output = []
  # find the best Z candidate, and make sure it is of the proper type.
  bestDiLeptcandidate = event.bestDiLeptCandidate
  goodJets = event.goodJets_all
#  if bestZcandidate is not None:
#    if (bestZcandidate.daughter(0).isMuon() and not muChannel) or \
#       (bestZcandidate.daughter(0).isElectron() and not eleChannel): bestZcandidate = None
  # output[0]: Trigger
  checkTrigger = event.object().event().eventAuxiliary().isRealData()
  if checkTrigger==False or (event.isMuTriggerOK and muChannel and not eleChannel) or (event.isEleTriggerOK and eleChannel and not muChannel) or (event.isEMUTriggerOK and eleChannel and muChannel):
    output.append(1)
  else:
    output.append(0)
  # output[1], output[2]: is di-lepton system and mass 
  # output[3], output[4]: number of muons, number of electrons
  nmu =0
  ne =0  
  if bestDiLeptcandidate is None:
    output.append(0)
    output.append(0)
  else: 
    output.append(1)
    lept1=bestDiLeptcandidate[0]
    lept2=bestDiLeptcandidate[1]    
    l1 = ROOT.TLorentzVector(lept1.px(),lept1.py(),lept1.pz(),lept1.energy())
    l2 = ROOT.TLorentzVector(lept2.px(),lept2.py(),lept2.pz(),lept2.energy())
    
    mass=(l1+l2).Mag()
    output.append(mass)

    if isGoodMuon(lept1,"tight"):
      nmu +=1
    if isGoodMuon(lept2,"tight"):
      nmu +=1
    if isGoodElectron(lept1,"tight"):
      ne +=1
    if isGoodElectron(lept2,"tight"):    
      ne +=1 
  output.append(nmu)
  output.append(ne)     
  # output[5] -> output[8] : (b)jets
  nJets = 0
  nBjetsHE = 0
  nBjetsHP = 0
  nBjetsHEHP = 0
  for index,jet in enumerate(event.jets):
    if goodJets[index]:
      nJets += 1
      HE = isBJet(jet,WP[1],btagging)
      HP = isBJet(jet,WP[0],btagging)
      if HE: nBjetsHE += 1
      if HP: nBjetsHP += 1
      if HE and HP: nBjetsHEHP +=1
  output.append(nJets)
  output.append(nBjetsHE)
  output.append(nBjetsHP)
  output.append(nBjetsHEHP)
  # output[9] : MET
  if isGoodMet(event.MET[0]):
    output.append(1)
  else: 
    output.append(0)
  # output[10] : MET Significance
  if isGoodMet_Sig(event.MET[0]):
    output.append(1)
  else: 
    output.append(0)
#  # additional quantities. For now, put the floats... might become cuts later on.
#  # output[11] : Z Pt
#  if bestZcandidate is None:
#    output.append(-1)
#  else:
#    output.append(bestZcandidate.pt())
#  # output[12] : delta R (bb)
#  # output[13] : delta R (bb) via SV
  dijet = event.dijet_all
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

