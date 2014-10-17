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
  "Z (wide)", 
  "Z (narrow)", 
  "Z+MET", 
  "Z+CA8 (HP+MET significance)",
  "Z+CA8, subjets dr<0.4 (HP+MET significance)",
  "Z+Subjets (HPHP+MET significance)",
  "Z+Subjets, Subjets dr>=0.4 (HPHP+MET significance)",
  "Z+bb (HPHP+MET significance)",
  "Z+CA8 or subjets (HPHP+MET significance)",
  "Z+CA8 or subjets, not AK5 (HPHP+MET significance)",
]

categoryNames = [ chan+"/"+cat for chan in channels for cat in categories ]

def isInCategory(category, categoryTuple):
  if category<len(categories):
    return isInCategoryChannel(category%len(categories), categoryTuple[:len(categoryTuple)/2])
  else:
    return isInCategoryChannel(category%len(categories), categoryTuple[len(categoryTuple)/2:])

def getNumber(text="", varName=""):
  if not varName+"!" in text: return "9999"
  return text.split(varName)[1].split("!")[1]

def isInCategoryChannel(category, categoryTuple):
  """Check if the event enters category X, given the tuple computed by eventCategory."""
  Mll = float(getNumber(categoryTuple[0],"Mll"))
  subdrjj = float(getNumber(categoryTuple[0],"subdrjj"))
  TrigAndZnarrow = "TriggerOK" in categoryTuple[0] and "OneZcand" in categoryTuple[0] and Mll<15.
  zfilter = getNumber(categoryTuple[0],"Zfilter")
  # category 0: Trigger
  if category==0:
    return "TriggerOK" in categoryTuple[0] and (zfilter=="none" or zfilter=="0b")
  # category 1: Z candidate (wide mass window)
  elif category==1:
    return isInCategoryChannel( 0, categoryTuple) and "OneZcand" in categoryTuple[0] and Mll<30.
  # category 2: Z candidate (narrow mass window)
  elif category==2:
    return isInCategoryChannel( 0, categoryTuple) and "OneZcand" in categoryTuple[0] and Mll<15.
  # category 3: Z+MET
  elif category==3:
    return isInCategoryChannel( 2, categoryTuple) and "passMETsigCut" in categoryTuple[0]
  # category 4: Z+CA8 (HP+MET significance)
  elif category==4:
    return TrigAndZnarrow and int(getNumber(categoryTuple[0],"nBfatjetsHP"))>0 and getNumber(categoryTuple[0],"OKsubjet")==zfilter
  # category 5: Z+CA8, subjets dr<0.4 (HP+MET significance)
  elif category==5:
    return isInCategoryChannel( 4, categoryTuple) and subdrjj<0.4 and subdrjj>=0. 
  # category 6: Z+Subjets (HPHP+MET significance)
  elif category==6:
    return TrigAndZnarrow and int(getNumber(categoryTuple[0],"nBsubjetsHP"))>1 and getNumber(categoryTuple[0],"OKsubjet")==zfilter
  # category 7: Z+Subjets, subjets dr>=0.4 (HPHP+MET significance)
  elif category==7:
    return isInCategoryChannel( 6, categoryTuple) and subdrjj>=0.4
  # category 8: Z+bb (HPHP+MET significance)
  elif category==8:
    return TrigAndZnarrow and int(getNumber(categoryTuple[0],"nBjetsHP"))>1 and getNumber(categoryTuple[0],"OKjet")==zfilter
  # category 9: Z+CA8/subjets (HPHP+MET significance)
  elif category==9:
    return isInCategoryChannel( 5, categoryTuple) or isInCategoryChannel( 7, categoryTuple)
  # categoty 10: Z+CA8/subjets not AK5(HPHP+MET significance)
  elif category==10:
    return not isInCategoryChannel( 8, categoryTuple) and isInCategoryChannel( 9, categoryTuple)
  # other does not exist
  else:
    return False

def eventCategory(event,btagging="CSV", WP=["M","L"], ZjetFilter="none"):
  return eventCategoryChannel(event, muChannel=configuration.muChannel, eleChannel=False,btagging=btagging, WP=WP, ZjetFilter=ZjetFilter) + \
         eventCategoryChannel(event, muChannel=False, eleChannel=configuration.eleChannel,btagging=btagging, WP=WP, ZjetFilter=ZjetFilter)
  
def eventCategoryChannel(event, muChannel=True, eleChannel=True, btagging="CSV", WP=["M","L"], ZjetFilter="none"):
  output = ["Event info:\n "]
  output[0] += "Zfilter!"+ZjetFilter+"!\n "
  # find the best Z candidate, and make sure it is of the proper type.
  bestZcandidate = event.bestZcandidate
  if bestZcandidate is not None:
    if (bestZcandidate.daughter(0).isMuon() and not muChannel) or \
       (bestZcandidate.daughter(0).isElectron() and not eleChannel): bestZcandidate = None
  # output[0]: Trigger
  checkTrigger = event.object().event().eventAuxiliary().isRealData()
  if checkTrigger==False or (event.isMuTriggerOK and muChannel) or (event.isEleTriggerOK and eleChannel):
    output[0] += "TriggerOK\n "
  # output[1], output[2]: di-lepton and mass cut
  if not bestZcandidate is None:
    output[0] += "OneZcand "
    output[0] += "Mll!"+str(abs(bestZcandidate.mass()-91))+"!\n "
  else : output[0] += "Mll!9999!\n "
  output[0] += eventCategoryChannelTemp(event, muChannel=True, eleChannel=True, btagging="CSV", WP=["M","L"], ZjetFilter=ZjetFilter, prejets="")
  output[0] += eventCategoryChannelTemp(event, muChannel=True, eleChannel=True, btagging="CSV", WP=["M","L"], ZjetFilter=ZjetFilter, prejets="fat")
  output[0] += eventCategoryChannelTemp(event, muChannel=True, eleChannel=True, btagging="CSV", WP=["M","L"], ZjetFilter=ZjetFilter, prejets="sub")
  # output[21] : MET
  if isGoodMet_Sig(event.MET[0]):
    output[0] += "passMETsigCut\n "
  # return the list of results
  #if "OneZcand" in output[0] and "passMETsigCut" in output[0] : print output[0]
  return output

def eventCategoryChannelTemp(event, muChannel=True, eleChannel=True, btagging="CSV", WP=["M","L"], ZjetFilter="none", prejets=""):
  """Check analysis requirements for various steps."""
  output = ""
  # first of all: ZjetFilter. If failed, we don't even evaluate the rest of the vector and we return the special -1 value.
  dijet = getattr(event, "di"+prejets+"jet_all")
  # output[3] -> output[8] : (b)jets
  if not ZjetFilter=="none":
    if MonteCarloSelection.isRecoZbbEvent(dijet) and '2b' in ZjetFilter : output += "OK"+prejets+"jet!2b!\n "
    elif MonteCarloSelection.isRecoZbEvent(dijet) and '1b' in ZjetFilter : output += "OK"+prejets+"jet!1b!\n "
    elif not MonteCarloSelection.isRecoZbbEvent(dijet) and not MonteCarloSelection.isRecoZbEvent(dijet) and '0b' in ZjetFilter : output += "OK"+prejets+"jet!0b!\n "
  else : output += "OK"+prejets+"jet!none!\n "
  goodJets = getattr(event, "good"+prejets+"Jets_all")
  nJets = 0
  nBjetsHE = 0
  nBjetsHP = 0
  nBjetsHEHP = 0
  for index,jet in enumerate(getattr(event,prejets+"jets")):
    if goodJets[index]:
      nJets += 1
      HE = isBJet(jet,WP[1],btagging)
      HP = isBJet(jet,WP[0],btagging)
      if HE: nBjetsHE += 1
      if HP: nBjetsHP += 1
      if HE and HP: nBjetsHEHP +=1
  output += "n"+prejets+"jets!"+str(nJets)+"!\n "
  output += "nB"+prejets+"jetsHE!"+str(nBjetsHE)+"!\n "
  output += "nB"+prejets+"jetsHP!"+str(nBjetsHP)+"!\n "
  output += "nB"+prejets+"jetsHEHP!"+str(nBjetsHEHP)+"!\n "
  if nJets>1:
    j1 = ROOT.TLorentzVector(dijet[0].px(),dijet[0].py(),dijet[0].pz(),dijet[0].energy())
    j2 = ROOT.TLorentzVector(dijet[1].px(),dijet[1].py(),dijet[1].pz(),dijet[1].energy())
    output += prejets+"drjj!"+str(j1.DeltaR(j2))+"!\n "
  else : output += prejets+"drjj!-1!\n "
  return output

