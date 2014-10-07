# OLD methods to classify the DY events, based on parton-level information. Renamed to avoid name conflict with new methods.

import math
import operator
import itertools
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

def delta_R(part1,part2):
  return math.hypot((part1.eta() - part2.eta()), delta_phi(part1.phi(), part2.phi()))

def match_GenToHad(genjets, hadrons, dr):
  """match hadrons to jets and returns matched jets"""
  matched = []
  for hadron in hadrons:
    in_cone = []
    for jet in genjets:
      deltar = delta_R(hadron,jet)
      if deltar < dr:
        in_cone.append([deltar, jet, hadron])
    if in_cone:
      bestmatch = min(in_cone, key=operator.itemgetter(0))[1]
      matched.append(bestmatch)
      genjets.remove(bestmatch)
  return (matched,genjets)

def genjetCollectionsProducer(fwevent, ptcut=0, etacut=10, prejets=""):
  """Event producer that returns three subcollections of genjets, for b,c,l jets"""
  # list of hadrons in the final state
  bhads = [part for part in fwevent.genParticles if is_final_Bhad(part)]
  chads = [part for part in fwevent.genParticles if is_final_Dhad(part)]
  # list of genjets passing the pt,eta cuts
  #genjets = [ jet for jet in fwevent.genJets if (jet.pt()>ptcut and abs(jet.eta())<etacut) ]
  genjets = [ jet.genJet() for index,jet in enumerate(getattr(fwevent,prejets+"jets")) if (getattr(fwevent,"good"+prejets+"Jets_all")[index] and jet.genJet()) ]
  # now divide it in three independant collections
  (bjets, nonbjets)  = match_GenToHad(genjets,  bhads, 0.5)
  (cjets, lightjets) = match_GenToHad(nonbjets, chads, 0.5)
  return (bjets,cjets,lightjets)

def isRecoZbbEvent(dijet):
  """Classify events according to recojet flavour"""
  if not dijet[0] is None and not dijet[1] is None:
    return abs(dijet[0].partonFlavour())==5 and abs(dijet[1].partonFlavour())==5
  else : return False

def isRecoZbEvent(dijet):
  """Classify events according to recojet flavour"""
  if not dijet[0] is None and not dijet[1] is None:
    return (abs(dijet[0].partonFlavour())!=5 and abs(dijet[1].partonFlavour())==5) or (abs(dijet[0].partonFlavour())==5 and abs(dijet[1].partonFlavour())!=5)
  elif not dijet[0] is None:
    return abs(dijet[0].partonFlavour())==5
  elif not dijet[1] is None:
    return abs(dijet[1].partonFlavour())==5
  else : return False

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
      "HT"   : -1,
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
  partons = []
  nj = 0
  nb = 0
  nc = 0
  HT = 0
  for index,p in enumerate(pup) :
    if idup[index]==23 : isZ=True
    if abs(idup[index]) in [11,13,15] : lep.append(index)
    if istup[index]==1 and abs(idup[index]) in [1,2,3,4,5,21] :
      nj+=1
      partons.append(p)
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
  for j in partons:
    j_tlv = TLorentzVector(j[0], j[1], j[2], j[3])
    HT += j_tlv.Pt()
  out = {
    "isZ"  : isZ,
    "nLep" : len(lep),
    "llpt" : llpt,
    "HT"   : HT,
    "nj"   : nj,
    "nb"   : nb,
    "nc"   : nc,
    }
  return out

# methods to get a generator-level Z candidate

# This first version does basically what Roberto was doing in zbb_counter.
# It finds a Z decaying into lepton, checks the acceptance for leptons and the Z mass.
def getGenZparticle(event, muons=True, electrons=True, leptonPtCut=20, leptonEtaCut=2.4):
  """method to find a Z decaying into leptons."""
  for part in event.genParticles:
    if abs(part.pdgId()) == 23 and part.status()==3:
      l0=part.daughter(0)
      l1=part.daughter(1)
      if (l0 and l1 and l0.status()==3 and l1.status()==3 and ((muons and abs(l0.pdgId())==13 and abs(l1.pdgId())==13) or ( electrons and abs(l0.pdgId())==11 and abs(l1.pdgId())==11))):
        if l0.pt()>leptonPtCut and l1.pt()>leptonPtCut and abs(l0.eta())<leptonEtaCut and abs(l1.eta())<leptonEtaCut:
          l1c=TLorentzVector(l0.px(),l0.py(),l0.pz(),l0.energy())
          l2c=TLorentzVector(l1.px(),l1.py(),l1.pz(),l1.energy())
          if 76 <= (l1c+l2c).M() <= 106:
            return part
  return None

# This second version is what Ludivine is doing for the unfolding.
# It finds a lepton pair at generator level that is compatible with the Z hypothesis.
# By construction, it is closer to what we do at reco level and does not require that 
# the leptons be from a gen Z explicitely.
def getGenZleptonPair(event, muons=True, electrons=True, leptonPtCut=20, leptonEtaCut=2.4):
  # get gen electrons and muons
  genElectrons=[]
  genMuons=[]
  for genPart in event.genParticles :
    if electrons and abs(genPart.pdgId())==11 and genPart.status()==1 and genPart.pt()>leptonPtCut and abs(genPart.eta())<leptonEtaCut:
      genElectrons.append(genPart)
    if muons and abs(genPart.pdgId())==13 and genPart.status()==1 and genPart.pt()>leptonPtCut and abs(genPart.eta())<leptonEtaCut:
      genMuons.append(genPart)
  # build pairs
  genZCandidates=[]
  for lpair in itertools.chain(itertools.combinations(genElectrons,2),itertools.combinations(genMuons,2)):
    lepton1 = lpair[0]
    lepton2 = lpair[1]
    if lepton1.charge() != lepton2.charge():
      genZcandidate=TLorentzVector(lepton1.px(),lepton1.py(),lepton1.pz(),lepton1.energy()) + \
                    TLorentzVector(lepton2.px(),lepton2.py(),lepton2.pz(),lepton2.energy())
      if 76 <= genZcandidate.M() <= 106 :
        genZCandidates.append((genZcandidate,lepton1,lepton2))
  # find best option based on the mass
  def massDiff(z):
    return abs(z[0].M()-91.1876)
  if len(genZCandidates)>0:
    return min(genZCandidates, key=massDiff)[1:]
  else:
    return None

def getMEMET_4v(event):
      neutrinos_4v = TLorentzVector()
      for particle in event.genParticles:
                if (particle.status()==3 and (abs(particle.pdgId())==12 or abs(particle.pdgId())==14 or abs(particle.pdgId())==16)):
                        neutrinos_4v += TLorentzVector(particle.px(),particle.py(),particle.pz(),particle.energy())
      return neutrinos_4v

def getNumberOfStatus3Neutrinos(event):
      NumberOfNeutrinos=0
      for particle in event.genParticles:
                if (particle.status()==3 and (abs(particle.pdgId())==12 or abs(particle.pdgId())==14 or abs(particle.pdgId())==16)):
			NumberOfNeutrinos+=1
      return NumberOfNeutrinos

def hadronFlavour(genParticles, jets):
  # list of hadrons in the final state
  bhads = [part for part in genParticles if is_final_Bhad(part)]
  chads = [part for part in genParticles if is_final_Dhad(part)]
  # list of genjets passing the pt,eta cuts
  genjets = [ jet.genJet() for index,jet in enumerate(jets) if jet.genJet() ]
  # now divide it in three independant collections
  (b, nonbjets)  = match_GenToHad(genjets,  bhads, 0.5)
  (c, l) = match_GenToHad(nonbjets, chads, 0.5)
  for jet in jets:
    genjet = jet.genJet()
    if not genjet : # probably PU, just check it was not assigned to b or c
      if abs(jet.partonFlavour()) in [4, 5] : jet.setPartonFlavour(0)
      continue
    if genjet in b :
      if not abs(jet.partonFlavour())==5 : jet.setPartonFlavour(5) # we don't look at the sign
    elif genjet in c :
      if not abs(jet.partonFlavour())==4 : jet.setPartonFlavour(4)
    else: # if no b or c hadrons matched and jet flavour is 4 or 5 then assume is gluon
      if abs(jet.partonFlavour()) in [4, 5] : jet.setPartonFlavour(21)
  return
