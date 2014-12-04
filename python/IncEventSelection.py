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

channels = ["Muon", "Electron","MuE"]

categories = [ 
  "Trigger", 
  "ll ",
  "lll ",
  "ll + jets",
  "ll + 1b (HE)",
  "ll + 1b (HP)",
  "ll + 2b (HEHE)",
  "ll + 2b (HPHP)",
  "ll + 2b (HPHP) + METSIG < cut",
  "ll + 2b (HPHP) + METSIG > cut",
  ]

categoryNames = [ chan+"/"+cat for chan in channels for cat in categories ]

def isInCategory(category, categoryTuple):
  if category<len(categories):
    return isInCategoryChannel(category%len(categories), categoryTuple[:len(categoryTuple)/3])
  elif category >= len(categories) and category < 2*len(categories) :
    return isInCategoryChannel(category%len(categories), categoryTuple[len(categoryTuple)/3:2*len(categoryTuple)/3])
  else:
    return isInCategoryChannel(category%len(categories), categoryTuple[2*len(categoryTuple)/3:len(categoryTuple)])

def isInCategoryChannel(category, categoryTuple):
    """Check if the event enters category X, given the tuple computed by eventCategory."""
   # category 0: Trigger
    if category==0:
      return categoryTuple[0]==1
   # category 1:e-e 
    elif category==1:
      return isInCategoryChannel( 0, categoryTuple) and categoryTuple[1]==1 
    # category 1:3 leptons    
     elif category==2:
      return isInCategoryChannel( 1, categoryTuple) and categoryTuple[2]> 2     
   # category 2:e-e + jets 
    elif category==3:
      return isInCategoryChannel( 1, categoryTuple) and categoryTuple[3]>1
   # category 3:e-e + 1b (HE)
    elif category==4:
      return isInCategoryChannel( 2, categoryTuple) and categoryTuple[4]>0
   # category 4:e-e + 1b (HP)
    elif category==5:
      return isInCategoryChannel( 3, categoryTuple) and categoryTuple[5]>0
   # category 5:e-e + 2b (HEHE)
    elif category==6:
      return isInCategoryChannel( 3, categoryTuple) and categoryTuple[4]>1
   # category 6:e-e + 2b (HPHP)
    elif category==7:
      return isInCategoryChannel( 4, categoryTuple) and categoryTuple[5]>1
   # category 7:e-e + 2b (HEHE) + MET_sig
    elif category==8:
      return isInCategoryChannel( 5, categoryTuple) and categoryTuple[8] == 1
   # category 8:e-e + 2b (HEHE) + MET_sig
    elif category==9:
      return isInCategoryChannel( 5, categoryTuple) and categoryTuple[8] == 0
    else:
      return False
      
def eventCategory(event,btagging="CSV", WP=["M","L"], ZjetFilter="none"):
  if event.object().event().eventAuxiliary().isRealData():
    configuration.JERfactor = 0
    configuration.JESfactor = 0
  return eventCategoryChannel(event, muChannel=True, eleChannel=False,btagging=btagging, WP=WP, ZjetFilter=ZjetFilter) + \
         eventCategoryChannel(event, muChannel=False, eleChannel=True,btagging=btagging, WP=WP, ZjetFilter=ZjetFilter) + \
	 eventCategoryChannel(event, muChannel=False, eleChannel=False,btagging=btagging, WP=WP, ZjetFilter=ZjetFilter)
  
def eventCategoryChannel(event, muChannel=True, eleChannel=True, btagging="CSV", WP=["M","L"], ZjetFilter="none"):
  """Check analysis requirements for various steps."""
  # first of all: ZjetFilter. If failed, we don't even evaluate the rest of the vector and we return the special -1 value.
  if not ZjetFilter=="none":
    if MonteCarloSelection.isRecoZbbEvent(event) and not ('2b' in ZjetFilter): return [-1]
    if (MonteCarloSelection.isRecoZbEvent(event) and not MonteCarloSelection.isRecoZbbEvent(event)) and not ('1b' in ZjetFilter): return [-1]
    if (not MonteCarloSelection.isRecoZbbEvent(event) and not MonteCarloSelection.isRecoZbEvent(event)) and not ('0b' in ZjetFilter): return [-1]
  output = []
  # find the best Z candidate, and make sure it is of the proper type.
  bestDiLeptcandidate = event.leptonsPair
  if bestDiLeptcandidate is None : nlept=0
  else : nlept= len(bestDiLeptcandidate)
  goodJets = event.goodJets_all
  # output[0]: Trigger
  checkTrigger = event.object().event().eventAuxiliary().isRealData()
#  if checkTrigger==False or (event.isMuTriggerOK and muChannel and not eleChannel) or (event.isEleTriggerOK and eleChannel and not muChannel) or (event.isINCTriggerOK and eleChannel and muChannel):
  if checkTrigger==False or event.isINCTriggerOK :
    output.append(1)
  else:
    output.append(0)
  # output[1], 1 if the muon (electron) channel is on and the two leading leptons are muons (electrons). For e-mu, it's 1 if the leading leptons are e-mu and Mu/El channel are at false
  # output[2]: number of leptons

  if bestDiLeptcandidate is None:
    output.append(0)
    output.append(0)
  else:

    lept1=bestDiLeptcandidate[0]
    lept2=bestDiLeptcandidate[1]

    
    if lept1.isMuon() and lept2.isMuon() :
      #mumu channel only filled for muChannel=True
      if muChannel:
        output.append(1)
      else: output.append(0)
      #ee channel only filled for eleChannel=True
    if lept1.isElectron() and lept2.isElectron() :
      #elel channel only filled for elChannel=True
      if eleChannel:
        output.append(1)
      else: output.append(0)

    if (lept1.isElectron() and lept2.isMuon()) or (lept2.isElectron() and lept1.isMuon()) :
	if not eleChannel and not muChannel :
         output.append(1)
	else : output.append(0) 

  #fill with number of leptons
  output.append(nlept)

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
  # output[7] and [8] : MET and MET Significance
  MetToCutOn=getMet(event = event,type = configuration.MetType)
  if configuration.MetRegion=="Low":
      output.append(isMetLowerThan(met = MetToCutOn,cut = configuration.MetCut))
      output.append(isMetSigLowerThan(met = MetToCutOn,cut = configuration.MetSigCut))
  elif configuration.MetRegion=="High":
      output.append(isMetHigherThan(met = MetToCutOn,cut = configuration.MetCut))
      output.append(isMetSigHigherThan(met = MetToCutOn,cut = configuration.MetSigCut))
  else:
      print "Warning : unforeseen MetRegion, must be \"Low\" or \"High\", the MET cut may be meaningless"

  # output[9] : bb DR
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
