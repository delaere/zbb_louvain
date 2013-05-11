# OLD methods to classify the DY events, based on parton-level information. Renamed to avoid name conflict with new methods.

import math
from ROOT import TLorentzVector

def isGenZlEvent(genParticles,ptcut=15, onlyStatus3=False):
  """Select events with at least one light parton > ptcut. isZlEvent != not(isZbEvent or isZcEvent) """
  hasUDSG = False
  for part in genParticles:
    if onlyStatus3 and part.status()!=3: break;
    if part.pdgId() in [-1,-2,-3,3,2,1,9,21] and part.pt()>ptcut : 
      hasUDSG = True
      break
  return hasUDSG

def isGenZbEvent(genParticles,ptcut=15, onlyStatus3=False):
  """Select events with at least one b parton > ptcut"""
  hasB = False
  for i,part in enumerate(genParticles):
    if onlyStatus3 and part.status()!=3: break;
    if part.pdgId() in [-5,5] and part.pt()>ptcut : 
      hasB = True
      break
  return hasB

def isGenZcEvent(genParticles,ptcut=15, onlyStatus3=False):
  """Select events with at least one c parton > ptcut"""
  hasC = False
  for part in genParticles:
    if onlyStatus3 and part.status()!=3: break;
    if part.pdgId() in [-4,4] and part.pt()>ptcut : 
      hasC = True
      break
  return hasC

# NEW version of the event classification, based on the presence of genjets matched with the corresponding hadron in the final state.
# Note that while it provides methods with same names as before, the arguments change from genParticles to event.

def is_Bhad(genpart):
  """Utility function: returns true if the genpart is a B hadron"""
  pdgid = math.fabs(genpart.pdgId())
  return (499 < pdgid < 600) or (4999 < pdgid < 6000)

def is_Dhad(genpart):
  """Utility function: returns true if the genpart is a D hadron"""
  pdgid = math.fabs(genpart.pdgId())
  return (399 < pdgid < 500) or (3999 < pdgid < 5000)

def is_final_Bhad(genpart):
  """Utility function: returns true if the genpart is a B hadron in the final state"""
  if not is_Bhad(genpart): return False
  if len([genpart.daughter(i) for i in range(genpart.numberOfDaughters()) if is_Bhad(genpart.daughter(i))]): return False
  return True

def is_final_Dhad(genpart):
  """Utility function: returns true if the genpart is a D hadron in the final state"""
  if not is_Dhad(genpart): return False
  if len([genpart.daughter(i) for i in range(genpart.numberOfDaughters()) if is_Dhad(genpart.daughter(i))]): return False
  return True

def delta_phi(phi1,phi2):
  dphi = math.fabs(phi1-phi2)
  if dphi > math.pi : dphi = 2*math.pi-dphi
  return dphi

def match_GenToHad(genjets, hadrons, dr):
  """match hadrons to jets and returns matched jets"""
  matched = []
  for hadron in hadrons:
    in_cone = []
    for jet in genjets:
      deltar = math.hypot((hadron.eta() - jet.eta()), delta_phi(hadron.phi(), jet.phi()))
      if deltar < dr: in_cone.append([deltar, jet])
    if in_cone:
      bestmatch = min(in_cone)[1]
      matched.append(jet)
      genjets.remove(bestmatch)
  return (matched,genjets)

def genjetCollectionsProducer(fwevent, ptcut=0, etacut=10):
  """Event producer that returns three subcollections of genjets, for b,c,l jets"""
  # list of hadrons in the final state
  bhads = [part for part in fwevent.genParticles if is_final_Bhad(part)]
  chads = [part for part in fwevent.genParticles if is_final_Dhad(part)]
  # list of genjets passing the pt,eta cuts
  #genjets = [ jet for jet in fwevent.genJets if (jet.pt()>ptcut and abs(jet.eta())<etacut) ]
  genjets = [ jet.genJet() for index,jet in enumerate(fwevent.jets) if (fwevent.goodJets_all[index] and jet.genJet()) ]
  # now divide it in three independant collections
  (bjets, nonbjets)  = match_GenToHad(genjets,  bhads, 0.5)
  (cjets, lightjets) = match_GenToHad(nonbjets, chads, 0.5)
  return (bjets,cjets,lightjets)

def isZbbEvent(event):
  """Classify events according to genjets matched with final state hadrons"""
  bjets = event.sortedGenJets[0]
  return len(bjets)>1

def isZbcEvent(event):
  """Classify events according to genjets matched with final state hadrons"""
  bjets = event.sortedGenJets[0]
  cjets = event.sortedGenJets[1]
  return len(bjets)==1 and len(cjets)>0

def isZblEvent(event):
  """Classify events according to genjets matched with final state hadrons"""
  bjets = event.sortedGenJets[0]
  cjets = event.sortedGenJets[1]
  return len(bjets)==1 and len(cjets)==0

def isZccEvent(event):
  """Classify events according to genjets matched with final state hadrons"""
  bjets = event.sortedGenJets[0]
  cjets = event.sortedGenJets[1]
  return len(bjets)==0 and len(cjets)>1

def isZclEvent(event):
  """Classify events according to genjets matched with final state hadrons"""
  bjets = event.sortedGenJets[0]
  cjets = event.sortedGenJets[1]
  return len(bjets)==0 and len(cjets)==1

def isZllEvent(event):
  """Classify events according to genjets matched with final state hadrons"""
  bjets = event.sortedGenJets[0]
  cjets = event.sortedGenJets[1]
  lightjets = event.sortedGenJets[2]
  return len(bjets)==0 and len(cjets)==0 and len(lightjets)>0

def isZlEvent(event):
  """Classify events according to genjets matched with final state hadrons"""
  return isZllEvent(event)

def isZcEvent(event):
  """Classify events according to genjets matched with final state hadrons"""
  return isZclEvent(event) or isZccEvent(event)

def isZbEvent(event):
  """Classify events according to genjets matched with final state hadrons"""
  return isZbbEvent(event) or isZbcEvent(event) or isZblEvent(event)

def LHEinfo(event):
  if event.lheParticles is None :
    out = {
      "isZ"  : -1,
      "nLep" : -1,
      "llpt" : -1,
      "nj"   : -1,
      "nb"   : -1,
      "nc"   : -1,
      }      
    return out
  hepeup = event.lheParticles.hepeup()
  pup = hepeup.PUP
  idup = hepeup.IDUP
  istup = hepeup.ISTUP
  nup = hepeup.NUP
  isZ=False
  lep=[]
  nj = 0
  nb = 0
  nc = 0
  for index,p in enumerate(pup) :
    if idup[index]==23 : isZ=True
    if abs(idup[index]) in [11,13,15] : lep.append(index)
    if istup[index]==1 and abs(idup[index]) in [1,2,3,4,5,21] : nj+=1
    if istup[index]==1 and abs(idup[index])==5 : nb+=1
    if istup[index]==1 and abs(idup[index])==4 : nc+=1
    #print "status ", istup[index], "PID ", idup[index]
  if len(lep)>1:
    if len(lep)>2 : print "Error, too much lhe leptons : ", len(lep)
    if not (idup[lep[0]]+idup[lep[1]])==0 : "Error, lhe leptons have same charge"
    l1=TLorentzVector(pup[lep[0]][0],pup[lep[0]][1],pup[lep[0]][2],pup[lep[0]][3])
    l2=TLorentzVector(pup[lep[1]][0],pup[lep[1]][1],pup[lep[1]][2],pup[lep[1]][3])
    zcand=l1+l2
    llpt = zcand.Pt()
  else :
    llpt=-1
  out = {
    "isZ"  : isZ,
    "nLep" : len(lep),
    "llpt" : llpt,
    "nj"   : nj,
    "nb"   : nb,
    "nc"   : nc,
    }
  return out

def prepareAnalysisEvent(event):
  event.addProducer("sortedGenJets",genjetCollectionsProducer,ptcut=20,etacut=2.4)
