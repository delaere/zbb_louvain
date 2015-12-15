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

  "Trigger -- no matching", #0
  #signal
  "Trigger no match + 2mu", #1
  "Trigger no match + 2mu + HLT match", #2
  "Trigger no match + 2mu + HLT match + >1j", #3
  "Trigger no match + 2mu + HLT match + >1j + >= 1b (HP)", #4
  "Trigger no match + 2mu + HLT match + >1j + >= 1b (HP) + MetSig < 6", #5
  "Trigger no match + 2mu + HLT match + >1j + >= 1b (HP) + MetSig < 6 + [20,70]", #6
  "Trigger no match + 2mu + HLT match + >1j + >= 1b (HP) + MetSig < 6 + [10,120]", #7
  "Trigger no match + 2mu + HLT match + >1j + >= 1b (HP) + MetSig > 10 + [20,70]", #8
]

categoryNames = [ chan+"/"+cat for chan in channels for cat in categories ]

def isInCategory(category, categoryTuple):
  return isInCategoryChannel(category,categoryTuple)

def isInCategoryChannel(category, categoryTuple):
  """Check if the event enters category X, given the tuple computed by eventCategory."""
  # category 0: Trigger -- no matching
  if category==0:
    return categoryTuple[0]==1
  # category 1: dimu HLT `and` dimuon candidte
  elif category==1:
    return (isInCategoryChannel(0, categoryTuple) and categoryTuple[1]==1)
  # category 2: dimu HLT `and` dimuon candidte `and` muons matched with HLT objects
  elif category==2:
    return (isInCategoryChannel(1, categoryTuple) and categoryTuple[3]==1)
  # category 3: dimu HLT `and` dimuon candidte `and` muons matched with HLT objects `and` at least 2 jets
  elif category==3:
    return (isInCategoryChannel(2, categoryTuple) and categoryTuple[4]>1)
  # category 4: dimu HLT `and` dimuon candidte `and` muons matched with HLT objects `and` at least 2 jets `and` the highest tag is tight
  elif category==4:
    return (isInCategoryChannel(3, categoryTuple) and categoryTuple[6]>0)
  # category 5: dimu HLT `and` dimuon candidte `and` muons matched with HLT objects `and` at least 2 jets `and` the highest tag is tight `and` MetSig
  elif category==5:
    return (isInCategoryChannel(4, categoryTuple) and categoryTuple[8]<6)
  # category 6: dimu HLT `and` dimuon candidte `and` muons matched with HLT objects `and` at least 2 jets `and` the highest tag is tight `and` MetSig `and` mll in [20,70]
  elif category==6:
    return (isInCategoryChannel(5, categoryTuple) and categoryTuple[2] > configuration.lowmassMu and categoryTuple[2] < configuration.highmassMu)
  # category 7: DY bkg 5 + mll in [10,120]
  elif category==7:
    return (isInCategoryChannel(5, categoryTuple) and categoryTuple[2] > 10. and categoryTuple[2] < 120.)
  # category 8: Tt bkg 4 + mll in [20,70] + MetSig > 10.
  elif category==8:
    return (isInCategoryChannel(4, categoryTuple) and categoryTuple[2] > 20. and categoryTuple[2] < 70. and categoryTuple[8] > 10)



def eventCategory(event,btagging="CSV", WP=["M","L"], ZjetFilter="none"):
  if event.object().event().eventAuxiliary().isRealData():
    configuration.JERfactor = 0
    configuration.JESfactor = 0
    configuration.isRealData = True   
  else: # Is it data? useful for blinding
    configuration.isRealData = False   
  return eventCategoryChannel(event, muChannel=configuration.muChannel, btagging=btagging, WP=WP, ZjetFilter=ZjetFilter)
  
def eventCategoryChannel(event, muChannel=True, btagging="CSV", WP=["M","L"], ZjetFilter="none"):
  """Check analysis requirements for various steps."""
  # first of all: ZjetFilter. If failed, we don't even evaluate the rest of the vector and we return the special -1 value.
  if not ZjetFilter=="none":
    if MonteCarloSelection.isRecoZbbEvent(event) and not ('2b' in ZjetFilter): return [-1]
    if (MonteCarloSelection.isRecoZbEvent(event) and not MonteCarloSelection.isRecoZbbEvent(event)) and not ('1b' in ZjetFilter): return [-1]
    if (not MonteCarloSelection.isRecoZbbEvent(event) and not MonteCarloSelection.isRecoZbEvent(event)) and not ('0b' in ZjetFilter): return [-1]
  output = []
  # find the best Z candidate, and make sure it is of the proper type.
  bestDiLeptcandidate = event.bestHambDiMuCandidate
  goodJets = event.goodJets_all
  nlept = 0
  higgs = ROOT.TLorentzVector(0,0,0,0)
  mass = -1  
  mbb = -1
  mu1pt = -1
  mu2pt = -1
  jet1pt = -1
  jet2pt = -1
  # output[0]: Trigger Only! No matching
  checkTrigger = event.object().event().eventAuxiliary().isRealData()
  if checkTrigger==False or event.isDiMuTriggerNoMatchOK:
    #print "MC does not need trigger"
    output.append(1)
  else:
    output.append(0)
  # output[1], 1: mumu, 2:ee, 3:emu, 4:more than 2 leptons
  # output[2]: di-lepton system mass, default value: -1
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
    higgs = l1+l2
   
    if lept1.isMuon() and lept2.isMuon() and nlept==2:
      #mumu channel only filled for muChannel=True
      if muChannel:
        output.append(1)
        mu1pt = l1.Pt()
	mu2pt = l2.Pt()
      else: output.append(0)
    output.append(mass)

  #output[3]: triggerMatched with muons
  if checkTrigger==False or event.isHambDiMuTriggerOK :
    #print "Matching for MC"
    output.append(1)  
  else:
    output.append(0)      
    
  # output[4] -> output[6] : (b)jets
  nJets = 0
  nBjetsHE = 0
  nBjetsHP = 0
  pt = []
  #print WP[0]
  for index,jet in enumerate(event.jets):
    if goodJets[index]:
      nJets += 1
      pt.append(jet.pt())
      HE = isBJet(jet,WP[1],btagging)#Loose
      HP = isBJet(jet,WP[0],btagging)#Medium
      if HE: nBjetsHE += 1
      if HP: nBjetsHP += 1
  output.append(nJets)
  output.append(nBjetsHE)
  output.append(nBjetsHP)
  if len(pt) > 1:
    pt.sort(reverse=True)
    jet1pt = pt[0]
    jet2pt = pt[1]
  # output[7] and [8] : MET and MET Significance
  MetToCutOn=getMet(event = event,type = configuration.MetType)
  output.append(isMetLowerThan(met = MetToCutOn,cut = configuration.MetCut))
  #output.append(isMetSigLowerThan(met = MetToCutOn,cut = configuration.MetSigCut))
  metSig = MetToCutOn.significance();
  if MetToCutOn.getSignificanceMatrix()(0,0)<1e10 and MetToCutOn.getSignificanceMatrix()(1,1)<1e10 :
      output.append(metSig)
  else:
      output.append(9999)
  
  # output[9] : bb DR
  # output[10] : bb SVDR
  # output[11]: bb invariant mass, default value: -1
  dijet = event.dijet_muChannel
  if dijet[0] is None or dijet[1] is None: 
    output.append(-1)
    output.append(-1)
    output.append(-1)
  else:
    b1 = ROOT.TLorentzVector(dijet[0].px(),dijet[0].py(),dijet[0].pz(),dijet[0].energy())
    b2 = ROOT.TLorentzVector(dijet[1].px(),dijet[1].py(),dijet[1].pz(),dijet[1].energy())
    higgs = higgs + b1 + b2  
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


  # output[12]: "mbb - mll", default value: -999
  # output[13]: "Higgs candidate mass - mH: 0"
  if (mbb != -1) and (mass != -1):
    output.append(abs(mbb - mass))
    output.append(abs(higgs.M()-configuration.mH))
  else:
    output.append(-999)
    output.append(0)

  # output[14] --> output[17]: "pt's"
  output.append(mu1pt)
  output.append(mu2pt)
  output.append(jet1pt)
  output.append(jet2pt)

  #print "The length of CategoryChannel is "
  #print len(output)
  # return the list of results
  
  mymatched = event.goodJets_muMatched
  
  return output


