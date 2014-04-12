import ROOT
import MonteCarloSelection
from ObjectSelection import *
from zbbConfig import configuration
from PatAnalysis.CPconfig import configuration

#########################################################################
#  Standard methods  ####################################################
#########################################################################

# Everything is duplicated for Electrons and Muons. 
# For simplicity and clarity, methods are defined generically for each
# and the final (public) methods work by concatenating/splitting 

channels = [ "Muon", "Electron" ]

categories = [ 
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
  # category 1: Z candidate (wide mass window)
  elif category==1:
    return isInCategoryChannel( 0, categoryTuple) and categoryTuple[1]==1 and categoryTuple[2]<30.
  # category 2: Z candidate (narrow mass window)
  elif category==2:
    return isInCategoryChannel( 0, categoryTuple) and categoryTuple[1]==1 and categoryTuple[2]<15.
  # category 3: Z+jet
  elif category==3:
    return isInCategoryChannel( 2, categoryTuple) and categoryTuple[3]>0
  # category 4:  Z+b (HE), wide mass window
  elif category==4:
    return isInCategoryChannel( 1, categoryTuple) and categoryTuple[3]>0 and categoryTuple[4]>0
  # category 5:  Z+b (HP), wide mass window
  elif category==5:
    return isInCategoryChannel( 1, categoryTuple) and categoryTuple[3]>0 and categoryTuple[5]>0
  # category 6:  Z+b (HE)
  elif category==6:
    return isInCategoryChannel( 3, categoryTuple) and categoryTuple[4]>0
  # category 7:  Z+b (HP)
  elif category==7:
    return isInCategoryChannel( 3, categoryTuple) and categoryTuple[5]>0
  # category 8:  Z+b (HE+MET_significance)
  elif category==8:
    return isInCategoryChannel( 6, categoryTuple) and categoryTuple[8]>0
  # category 9:  Z+b (HP+MET_significance)
  elif category==9:
    return isInCategoryChannel( 7, categoryTuple) and categoryTuple[8]>0
  # categoty 10: Z+bb (HEHE), wide mass window
  elif category==10:
    return isInCategoryChannel( 4, categoryTuple) and categoryTuple[4]>1
  # categoty 11: Z+bb (HEHP), wide mass window
  elif category==11:
    return isInCategoryChannel( 5, categoryTuple) and categoryTuple[4]+categoryTuple[5]-categoryTuple[6] > 1
  # categoty 12: Z+bb (HPHP), wide mass window
  elif category==12:
    return isInCategoryChannel( 5, categoryTuple) and categoryTuple[5]>1
  # categoty 13: Z+bb (HEHE)
  elif category==13:
    return isInCategoryChannel( 3, categoryTuple) and categoryTuple[4]>1
  # categoty 14: Z+bb (HEHP)
  elif category==14:
    return isInCategoryChannel( 3, categoryTuple) and categoryTuple[4]+categoryTuple[5]-categoryTuple[6] > 1 and categoryTuple[5] > 0
  # categoty 15: Z+bb (HPHP)
  elif category==15:
    return isInCategoryChannel( 3, categoryTuple) and categoryTuple[5]>1
  # categoty 16: Z+bb (HEHE+MET_significance)
  elif category==16:
    return isInCategoryChannel(13, categoryTuple) and categoryTuple[8]>0
  # categoty 17: Z+bb (HEHP+MET_significance)
  elif category==17:
    return isInCategoryChannel(14, categoryTuple) and categoryTuple[8]>0
  # categoty 18: Z+bb (HPHP+MET_significance)
  elif category==18:
    return isInCategoryChannel(15, categoryTuple) and categoryTuple[8]>0
  # other does not exist
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
  bestZcandidate = event.bestZcandidate
  goodJets = event.goodJets_all
  if bestZcandidate is not None:
    if (bestZcandidate.daughter(0).isMuon() and not muChannel) or \
       (bestZcandidate.daughter(0).isElectron() and not eleChannel): bestZcandidate = None
  # output[0]: Trigger
  checkTrigger = event.object().event().eventAuxiliary().isRealData()
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
      HE = isBJet(jet,WP[1],btagging)
      HP = isBJet(jet,WP[0],btagging)
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

