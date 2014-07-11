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

channels = [ "Muon" ]

categories = [ 
  "Trigger", #0
  ## 2 M b-tag
  "ll + 2b (HPHP) + 20 < Mll < 70 GeV", #1
  "ll + 2b (HPHP) + 20 < Mll < 70 GeV + Mbb > 15", #2
  "ll + 2b (HPHP) + 20 < Mll < 70 GeV + Mbb > 15 + METSIG", #3
  "ll + 2b (HPHP) + 20 < Mll < 70 GeV + DMaa < 30", #4
  "ll + 2b (HPHP) + 20 < Mll < 70 GeV + DMaa < 30 + METSIG", #5
  "ll + 2b (HPHP) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30", #6     
  "ll + 2b (HPHP) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30 + METSIG", #7
  ## 1 M 1 L b-tag
  "ll + 2b (HPHE) + 20 < Mll < 70 GeV", #8
  "ll + 2b (HPHE) + 20 < Mll < 70 GeV + Mbb > 15", #9
  "ll + 2b (HPHE) + 20 < Mll < 70 GeV + Mbb > 15 + METSIG", #10
  "ll + 2b (HPHE) + 20 < Mll < 70 GeV + DMaa < 30", #11
  "ll + 2b (HPHE) + 20 < Mll < 70 GeV + DMaa < 30 + METSIG", #12
  "ll + 2b (HPHE) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30", #13     
  "ll + 2b (HPHE) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30 + METSIG", #14
  ## 2 L b-tag
  "ll + 2b (HEHE) + 20 < Mll < 70 GeV", #8
  "ll + 2b (HEHE) + 20 < Mll < 70 GeV + Mbb > 15", #9
  "ll + 2b (HEHE) + 20 < Mll < 70 GeV + Mbb > 15 + METSIG", #10
  "ll + 2b (HEHE) + 20 < Mll < 70 GeV + DMaa < 30", #11
  "ll + 2b (HEHE) + 20 < Mll < 70 GeV + DMaa < 30 + METSIG", #12
  "ll + 2b (HEHE) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30", #13     
  "ll + 2b (HEHE) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30 + METSIG", #14
]

categoryNames = [ chan+"/"+cat for chan in channels for cat in categories ]

def isInCategory(category, categoryTuple):
  #print "=================================="
  #print category
  #print len(categories)
  #mylen = len(categoryTuple)
  #print len(categoryTuple)
  #print "What is category number?"
  #print category%len(categories)
  #print "What is first? "  
  #myS1 = :len(categoryTuple)/2
  #print myS1
  #print "What is second?"
  #print len(categoryTuple)/2:
  #print "+++++++++++++++"
  #for mys in range(0,mylen):
  #  print categoryTuple[mys]
  #print "+++++++++++++++"
  #print categoryTuple[:len(categoryTuple)/2]
  #print categoryTuple[:6]
  #print categoryTuple[0:6]
  #print "---------------"
  
  #print categoryTuple[len(categoryTuple)/2:]
  #print categoryTuple[6:]
  #print categoryTuple[6:12]

  return isInCategoryChannel(category,categoryTuple)
  #if category<len(categories):
  #  return isInCategoryChannel(category%len(categories), categoryTuple[:len(categoryTuple)/2])
  #else:
  #  return isInCategoryChannel(category%len(categories), categoryTuple[len(categoryTuple)/2:])

def isInCategoryChannel(category, categoryTuple):
  """Check if the event enters category X, given the tuple computed by eventCategory."""
  # category 0: Trigger
  if category==0:
    return categoryTuple[0]==1

 # category 1:mu-mu + 2b (HPHP) + 20 < Mll <70  GeV
  elif category==1:
    return isInCategoryChannel(0, categoryTuple) and categoryTuple[1]==1 and categoryTuple[5]>1 and categoryTuple[2] > 20 and categoryTuple[2] < 70

 # category 2:mu-mu + 2b (HPHP) + 20 < Mll < 70 GeV + Mbb > 15
  elif category==2:
    return isInCategoryChannel(1, categoryTuple) and categoryTuple[10]>15 

 # category 3:mu-mu + 2b (HPHP) + 20 < Mll < 70 GeV + Mbb > 15 + METSIG 
  elif category==3:
    return isInCategoryChannel(2, categoryTuple) and categoryTuple[7]>0

 # category 4:mu-mu + 2b (HPHP) + 20 < Mll < 70 GeV + DMaa < 30
  elif category==4:
    return isInCategoryChannel(1, categoryTuple) and abs(categoryTuple[11])<30 

 # category 5:mu-mu + 2b (HPHP) + 20 < Mll < 70 GeV + DMaa < 30 + METSIG 
  elif category==5:
    return isInCategoryChannel(4, categoryTuple) and categoryTuple[7]>0

 # category 6:mu-mu + 2b (HPHP) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30
  elif category==6:
    return isInCategoryChannel(2, categoryTuple) and abs(categoryTuple[11])<30

 # category 7:mu-mu + 2b (HPHP) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30 + METSIG
  elif category==7:
    return isInCategoryChannel(6, categoryTuple) and categoryTuple[7]>0

 # category 8:mu-mu + 2b (HPHE) + 20 < Mll <70  GeV
  elif category==8:
    return isInCategoryChannel(0, categoryTuple) and categoryTuple[1]==1 and categoryTuple[5] == 1 and categoryTuple[4] == 1 and categoryTuple[2] > 20 and categoryTuple[2] < 70

 # category 9:mu-mu + 2b (HPHE) + 20 < Mll < 70 GeV + Mbb > 15
  elif category==9:
    return isInCategoryChannel(8, categoryTuple) and categoryTuple[10]>15

 # category 10:mu-mu + 2b (HPHE) + 20 < Mll < 70 GeV + Mbb > 15 + METSIG 
  elif category==10:
    return isInCategoryChannel(9, categoryTuple) and categoryTuple[7]>0
  
 # category 11:mu-mu + 2b (HPHE) + 20 < Mll < 70 GeV + DMaa < 30
  elif category==11:
    return isInCategoryChannel(8, categoryTuple) and abs(categoryTuple[11])<30

 # category 12:mu-mu + 2b (HPHE) + 20 < Mll < 70 GeV + DMaa < 30 + METSIG 
  elif category==12:
    return isInCategoryChannel(11, categoryTuple) and categoryTuple[7]>0

 # category 13:mu-mu + 2b (HPHE) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30
  elif category==13:
    return isInCategoryChannel(9, categoryTuple) and abs(categoryTuple[11])<30

 # category 14:mu-mu + 2b (HPHE) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30 + METSIG
  elif category==14:
    return isInCategoryChannel(13, categoryTuple) and categoryTuple[7]>0

 # category 15:mu-mu + 2b (HEHE) + 20 < Mll <70  GeV
  elif category==15:
    return isInCategoryChannel(0, categoryTuple) and categoryTuple[1]==1 and categoryTuple[4]>1 and categoryTuple[2] > 20 and categoryTuple[2]<70

 # category 16:mu-mu + 2b (HEHE) + 20 < Mll < 70 GeV + Mbb > 15
  elif category==16:
    return isInCategoryChannel(15, categoryTuple) and categoryTuple[10]>15

 # category 17:mu-mu + 2b (HEHE) + 20 < Mll < 70 GeV + Mbb > 15 + METSIG 
  elif category==17:
    return isInCategoryChannel(16, categoryTuple) and categoryTuple[7]>0

 # category 18:mu-mu + 2b (HEHE) + 20 < Mll < 70 GeV + DMaa < 30
  elif category==18:
    return isInCategoryChannel(15, categoryTuple) and abs(categoryTuple[11])<30

 # category 19:mu-mu + 2b (HEHE) + 20 < Mll < 70 GeV + DMaa < 30 + METSIG 
  elif category==19:
    return isInCategoryChannel(18, categoryTuple) and categoryTuple[7]>0

 # category 20:mu-mu + 2b (HEHE) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30
  elif category==20:
    return isInCategoryChannel(16, categoryTuple) and abs(categoryTuple[11])<30

 # category 21:mu-mu + 2b (HPHE) + 20 < Mll < 70 GeV + Mbb > 15 + DMaa < 30 + METSIG
  elif category==21:
    return isInCategoryChannel(20, categoryTuple) and categoryTuple[7]>0 

def eventCategory(event,btagging="CSV", WP=["M","L"], ZjetFilter="bcl"):
  if event.object().event().eventAuxiliary().isRealData():
    configuration.JERfactor = 0
    configuration.JESfactor = 0
  return eventCategoryChannel(event, muChannel=configuration.muChannel, btagging=btagging, WP=WP, ZjetFilter=ZjetFilter)
  
def eventCategoryChannel(event, muChannel=True, btagging="CSV", WP=["M","L"], ZjetFilter="bcl"):
  """Check analysis requirements for various steps."""
  # first of all: ZjetFilter. If failed, we don't even evaluate the rest of the vector and we return the special -1 value.
  if not ZjetFilter=="bcl":
    if MonteCarloSelection.isZbEvent(event) and not ('b' in ZjetFilter): return [-1]
    if (MonteCarloSelection.isZcEvent(event) and not MonteCarloSelection.isZbEvent(event)) and not ('c' in ZjetFilter): return [-1]
    if (not MonteCarloSelection.isZcEvent(event) and not MonteCarloSelection.isZbEvent(event)) and not ('l' in ZjetFilter): return [-1]
  output = []
  # find the best Z candidate, and make sure it is of the proper type.
  bestDiLeptcandidate = event.bestHambDiMuCandidate
  goodJets = event.goodJets_all
  nlept = 0
  # output[0]: Trigger
  checkTrigger = event.object().event().eventAuxiliary().isRealData()
#  if checkTrigger==False or (event.isMuTriggerOK and muChannel and not eleChannel) or (event.isEleTriggerOK and eleChannel and not muChannel) or (event.isINCTriggerOK and eleChannel and muChannel):
  if checkTrigger==False or event.isHambDiMuTriggerOK :
    output.append(1)  
  else:
    output.append(0)      
  # output[1], 1: mumu, 2:ee, 3:emu, 4:more than 2 leptons
  # output[2]: di-lepton system mass, default value: -1
  mass = -1  
  if bestDiLeptcandidate is None:
    output.append(0)
    output.append(-1) 
  else:
    nDilep = len(bestDiLeptcandidate) 
    for i in range(0,nDilep) :
      if bestDiLeptcandidate[i] is not None:
        nlept += 1    
    lept1=bestDiLeptcandidate[0]
    lept2=bestDiLeptcandidate[1] 
    l1 = ROOT.TLorentzVector(lept1.px(),lept1.py(),lept1.pz(),lept1.energy())
    l2 = ROOT.TLorentzVector(lept2.px(),lept2.py(),lept2.pz(),lept2.energy())
    mass=(l1+l2).M()	
   
    if lept1.isMuon() and lept2.isMuon() and nlept==2:
      #mumu channel only filled for muChannel=True
      if muChannel:
        output.append(1)
      else: output.append(0)
    output.append(mass)
    
  # output[3] -> output[5] : (b)jets
  nJets = 0
  nBjetsHE = 0
  nBjetsHP = 0
  for index,jet in enumerate(event.jets):
    if goodJets[index]:
      nJets += 1
      HE = isBJet(jet,WP[1],btagging)#Loose
      HP = isBJet(jet,WP[0],btagging)#Medium
      if HE: nBjetsHE += 1
      if HP: nBjetsHP += 1
  output.append(nJets)
  output.append(nBjetsHE)
  output.append(nBjetsHP)
  # output[6] and [7] : MET and MET Significance
  MetToCutOn=getMet(event = event,type = configuration.MetType)
  output.append(isMetLowerThan(met = MetToCutOn,cut = configuration.MetCut))
  output.append(isMetSigLowerThan(met = MetToCutOn,cut = configuration.MetSigCut))
  
  # output[8] : bb DR
  # output[9] : bb SVDR
  # output[10]: bb invariant mass, default value: -1
  mbb = -1
  dijet = event.dijet_muChannel
  if dijet[0] is None or dijet[1] is None: 
    output.append(-1)
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
    mbb = (b1+b2).M()
    output.append(mbb)


  # output[11]: "mbb - mll", default value: -999
  if (mbb != -1) and (mass != -1):
    output.append(abs(mbb - mass))
  else:
    output.append(-999)
  print "The length of CategoryChannel is "
  print len(output)
  # return the list of results
  return output

