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

channels = [ "Muon", "Electron"]

categories = []

if configuration.run_on_emu == True:
  categories = [
    "Trigger",
    "e-mu",
    "e-mu + jets",
    "e-mu + 1b (HE)",
    "e-mu + 1b (HP)",
    "e-mu + 2b (HEHE)",
    "e-mu + 2b (HPHP)",
    "e-mu + 2b (HEHE) + METSIG",
    "e-mu + Mll > 95 GeV",
    "e-mu + jets + Mll > 95 GeV",
    "e-mu + 1b (HE)+ Mll > 95 GeV",
    "e-mu + 1b (HP)+ Mll > 95 GeV",
    "e-mu + 2b (HEHE)+ Mll > 95 GeV",
    "e-mu + 2b (HPHP)+ Mll > 95 GeV",
    "e-mu + 2b (HEHE) + METSIG + Mll > 95 GeV",
]
else:

  categories = [ 
  "Trigger", 
  "ll + 2b (HPHP) + Mll > 20 GeV ",
  "ll + 2b (HPHP) + Mll > 20 GeV + METSIG",      
  "ll + 2b (HPHP) + 20 <  Mll < 60 GeV ",
  "ll + 2b (HPHP) + 20 <  Mll < 60 GeV + METSIG",
  "ll + 2b (HPHP) + 60 <  Mll < 120 GeV ",
  "ll + 2b (HPHP) + 60 <  Mll < 120 GeV + METSIG",
  "ll + 2b (HPHP) + 120 <  Mll  GeV ",
  "ll + 2b (HPHP) + 120 <  Mll  GeV + METSIG",
  ]

categoryNames = [ chan+"/"+cat for chan in channels for cat in categories ]

def isInCategory(category, categoryTuple):
  if category<len(categories):
    return isInCategoryChannel(category%len(categories), categoryTuple[:len(categoryTuple)/2])
  else:
    return isInCategoryChannel(category%len(categories), categoryTuple[len(categoryTuple)/2:])

def isInCategoryChannel(category, categoryTuple):
  """Check if the event enters category X, given the tuple computed by eventCategory."""
  if configuration.run_on_emu == True:
    # category 0: Trigger
    if category==0:
      return categoryTuple[0]==1
    # category 1:e-mu
    elif category==1:
      return isInCategoryChannel( 0, categoryTuple) and categoryTuple[1]==3  and categoryTuple[2]>10
    # category 2:e-mu + jets
    elif category==2:
      return isInCategoryChannel( 1, categoryTuple) and categoryTuple[3]>0
    # category 3: e-mu + 1b (HE)
    elif category==3:
      return isInCategoryChannel( 2, categoryTuple) and categoryTuple[4]>0
    # category 4: e-mu + 1b (HP)
    elif category==4:
      return isInCategoryChannel( 3, categoryTuple) and categoryTuple[5]>0
    # category 5: e-mu + 2b (HEHE)
    elif category==5:
      return isInCategoryChannel( 3, categoryTuple) and categoryTuple[4]>1
     # category 6:e-mu + 2b (HPHP)
    elif category==6:
      return isInCategoryChannel( 4, categoryTuple) and categoryTuple[5]>1
     # category 7:e-mu + 2b (HEHE) + MET_sig
    elif category==7:
      return isInCategoryChannel( 5, categoryTuple) and categoryTuple[8]>0
  #   # category 8:e-mu + Mll > 95 GeV
    elif category==8:
      return isInCategoryChannel( 1, categoryTuple) and categoryTuple[2]>95
    # category 9:e-mu + jets + Mll > 95 GeV
    elif category==9:
      return isInCategoryChannel( 2, categoryTuple) and  categoryTuple[2]>95
    # category 10: e-mu + 1b (HE)+ Mll > 95 GeV
    elif category==10:
      return isInCategoryChannel( 3, categoryTuple) and  categoryTuple[2]>95
    # category 11: e-mu + 1b (HP)+ Mll > 95 GeV
    elif category==11:
      return isInCategoryChannel( 4, categoryTuple) and  categoryTuple[2]>95
    # category 12: e-mu + 2b (HEHE) + Mll > 95 GeV
    elif category==12:
      return isInCategoryChannel( 5, categoryTuple) and  categoryTuple[2]>95
     # category 13:e-mu + 2b (HPHP) + Mll > 95 GeV
    elif category==13:
      return isInCategoryChannel( 6, categoryTuple) and  categoryTuple[2]>95
      # category 14:e-mu + 2b (HEHE) + Mll > 95 GeV
    elif category==14:
      return isInCategoryChannel( 7, categoryTuple) and categoryTuple[2]>95
    else:
      return False
  else:
    # category 0: Trigger
    if category==0:
      return categoryTuple[0]==1
   # category 1:e-e + 2b (HPHP) + Mll >20  GeV
    elif category==1:
      return isInCategoryChannel(0, categoryTuple) and (categoryTuple[1]==1 or categoryTuple[1]==2) and categoryTuple[5]>1 and categoryTuple[2] > 10 and categoryTuple[2] > 20
   # category 2:e-e + 2b (HEHE) + Mll > 20 GeV + MET_sig
    elif category==2:
      return isInCategoryChannel(1, categoryTuple) and categoryTuple[8]>0
   # category 3:e-e + 2b (HEHE) + 20 < Mll < 60 GeV
    elif category==3:
      return isInCategoryChannel(0, categoryTuple) and (categoryTuple[1]==1 or categoryTuple[1]==2) and categoryTuple[5]>1  and categoryTuple[2] > 20 and categoryTuple[2] < 60
   # category 4:e-e + 2b (HEHE) + 20 < Mll < 60 GeV + MET_sig
    elif category==4:
      return isInCategoryChannel(3, categoryTuple) and categoryTuple[8]>0
   # category 5:e-e + 2b (HEHE) + 60 < Mll < 120 GeV
    elif category==5:
      return isInCategoryChannel(0, categoryTuple) and (categoryTuple[1]==1 or categoryTuple[1]==2) and categoryTuple[5]>1  and categoryTuple[2] > 60 and categoryTuple[2] < 120
   # category 6:e-e + 2b (HEHE) + 60 < Mll < 120 GeV + MET_sig
    elif category==6:
      return isInCategoryChannel(5, categoryTuple) and categoryTuple[8]>0
   # category 7:e-e + 2b (HEHE) + 120 < Mll
    elif category==7:
      return isInCategoryChannel(0, categoryTuple) and (categoryTuple[1]==1 or categoryTuple[1]==2) and categoryTuple[5]>1  and categoryTuple[2] > 120
   # category 8:e-e + 2b (HEHE) + 120 < Mll  + MET_sig
    elif category==8:
      return isInCategoryChannel(7, categoryTuple) and categoryTuple[8]>0

def eventCategory(event,btagging="CSV", WP=["M","L"], ZjetFilter="none"):
  if event.object().event().eventAuxiliary().isRealData():
    configuration.JERfactor = 0
    configuration.JESfactor = 0
  return eventCategoryChannel(event, muChannel=configuration.muChannel, eleChannel=False,btagging=btagging, WP=WP, ZjetFilter=ZjetFilter) + \
         eventCategoryChannel(event, muChannel=False, eleChannel=configuration.eleChannel,btagging=btagging, WP=WP, ZjetFilter=ZjetFilter)
  
def eventCategoryChannel(event, muChannel=True, eleChannel=True, btagging="CSV", WP=["M","L"], ZjetFilter="none"):
  """Check analysis requirements for various steps."""
  # first of all: ZjetFilter. If failed, we don't even evaluate the rest of the vector and we return the special -1 value.
  if not ZjetFilter=="none":
    if MonteCarloSelection.isRecoZbbEvent(event) and not ('2b' in ZjetFilter): return [-1]
    if (MonteCarloSelection.isRecoZbEvent(event) and not MonteCarloSelection.isRecoZbbEvent(event)) and not ('1b' in ZjetFilter): return [-1]
    if (not MonteCarloSelection.isRecoZbbEvent(event) and not MonteCarloSelection.isRecoZbEvent(event)) and not ('0b' in ZjetFilter): return [-1]
  output = []
  # find the best Z candidate, and make sure it is of the proper type.
  bestDiLeptcandidate = event.bestDiLeptCandidate
  goodJets = event.goodJets_all
  nlept = 0
  # output[0]: Trigger
  checkTrigger = event.object().event().eventAuxiliary().isRealData()
#  if checkTrigger==False or (event.isMuTriggerOK and muChannel and not eleChannel) or (event.isEleTriggerOK and eleChannel and not muChannel) or (event.isINCTriggerOK and eleChannel and muChannel):
  if checkTrigger==False or event.isINCTriggerOK :
    output.append(1)
  else:
    output.append(0)
  # output[1], 1: mumu, 2:ee, 3:emu, 4:more than 2 leptons
  # output[2]: di-lepton system mass

  if bestDiLeptcandidate is None:
    output.append(0)
    output.append(0)
  else:
    for i in range(0,3) :
      if bestDiLeptcandidate[i] is not None:
        nlept += 1
    lept1=bestDiLeptcandidate[0]
    lept2=bestDiLeptcandidate[1]
    lept3= bestDiLeptcandidate[2]
    l1 = ROOT.TLorentzVector(lept1.px(),lept1.py(),lept1.pz(),lept1.energy())
    l2 = ROOT.TLorentzVector(lept2.px(),lept2.py(),lept2.pz(),lept2.energy())
    mass=(l1+l2).M()
    mass2 = 0
    mass3 = 0
    if lept3 is not None:
      l3 = ROOT.TLorentzVector(lept3.px(),lept3.py(),lept3.pz(),lept3.energy())
      mass2 =  (l3+l2).M()
      mass3 =  (l3+l1).M()

    
    if lept1.isMuon() and lept2.isMuon() :
      #mumu channel only filled for muChannel=True
      if muChannel:
        output.append(1)
      else: output.append(0)
      #ee channel only filled for eleChannel=True
    if lept1.isElectron() and lept2.isElectron() :
      #elel channel only filled for elChannel=True
      if eleChannel:
        output.append(2)
      else: output.append(0)

    if (lept1.isElectron() and lept2.isMuon()) or (lept2.isElectron() and lept1.isMuon()) :
      output.append(3) 
    if nlept > 2:
      output.append(4)
    if lept3 is not None:
      if mass >5 and mass3 >5 and mass2 > 5:
        m1 = abs(mass-91)
        m2 = abs(mass2-91)
	m3 = abs(mass3-91)
	if m1 > m2 and m1 > m3:
	  output.append (mass)
	elif m2 > m1 and m2 > m3:
	  output.append (mass2)
	elif m3 > m1 and m3 > m2:
	  output.append (mass3)
    else:
      output.append(mass)

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

