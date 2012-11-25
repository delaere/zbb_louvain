import sys
import os
import ROOT
from AnalysisEvent import AnalysisEvent
from itertools import combinations
from eventSelection import jetId, findBestCandidate, isGoodJet, isBJet, isGoodElectron, isGoodMuon, eventCategory
from zbbCommons import zbblabel

#these methods are temporary interfaces during the transition to the new framework.
def category(fwevent,muChannel=True,  btagging="SSV"):
  runNumber= fwevent.eventAuxiliary().run()
  return eventCategory(fwevent.trigger, fwevent.Zmumu, fwevent.Zelel, fwevent.vertices, fwevent.jets, fwevent.MET, runNumber, muChannel, btagging)

def vertex(event):
  vertices = event.vertices
  if vertices.size()>0 :
    return vertices[0]
  else:
    return None

def bestZcandidate(fwevent):
  return findBestCandidate(None,fwevent.vertex,fwevent.Zmumu,fwevent.Zelel)

# a method to add some 4vectors to the event
def candidateproducer(fwevent,candidate):
  if fwevent.bestZcandidate is not None:
    if candidate=="ZbHP":
      for jet in fwevent.jets:
        if isGoodJet(jet,fwevent.bestZcandidate) and isBJet(jet,"HP") :
          b = ROOT.TLorentzVector(jet.px(),jet.py(),jet.pz(),jet.energy())
          z = ROOT.TLorentzVector(fwevent.bestZcandidate.px(),fwevent.bestZcandidate.py(),fwevent.bestZcandidate.pz(),fwevent.bestZcandidate.energy())
          return z+b
    elif candidate=="ZbHE":
      for jet in fwevent.jets:
        if isGoodJet(jet,fwevent.bestZcandidate) and isBJet(jet,"HE") :
          b = ROOT.TLorentzVector(jet.px(),jet.py(),jet.pz(),jet.energy())
          z = ROOT.TLorentzVector(fwevent.bestZcandidate.px(),fwevent.bestZcandidate.py(),fwevent.bestZcandidate.pz(),fwevent.bestZcandidate.energy())
          return z+b
    elif candidate=="bbHP":
      return map(sum,combinations(filter(lambda jet: isGoodJet(jet,fwevent.bestZcandidate) and isBJet(jet,"HP"),fwevent.jets),2))
    elif candidate=="bbHE":
      return map(sum,combinations(filter(lambda jet: isGoodJet(jet,fwevent.bestZcandidate) and isBJet(jet,"HE"),fwevent.jets),2))
    elif candidate=="ZbbHP":
      z = ROOT.TLorentzVector(fwevent.bestZcandidate.px(),fwevent.bestZcandidate.py(),fwevent.bestZcandidate.pz(),fwevent.bestZcandidate.energy())
      return map(lambda a:a+z,fwevent.bbHP)
    elif candidate=="ZbbHE":
      z = ROOT.TLorentzVector(fwevent.bestZcandidate.px(),fwevent.bestZcandidate.py(),fwevent.bestZcandidate.pz(),fwevent.bestZcandidate.energy())
      return map(lambda a:a+z,fwevent.bbHE)
  return None

# the main method
def DumpEventInfo(fwevent=None, run=None, event=None, lumi=None, path="../testfiles/"):
  """Dump informations about a given event"""
  # in case no fwevent is provided, find it using run,event,(lumi)
  if fwevent is None:
    if (run is None) or (event is None):
      print "DumpEventInfo Error: either pass a fwlite event or give both run and event number"
      return
    # find event based on run  and event
    if os.path.isdir(path):
      dirList=os.listdir(path)
      files=[]
      for fname in dirList:
        files.append(path+fname)
    elif os.path.isfile(path):
      files=[path]
    else:
      files=[]
    events = AnalysisEvent(files)
    DumpEventInfo(events[(run,event,lumi)])
    return
  # collections used in the analysis
  fwevent.addCollection("vertices","vector<reco::Vertex>",zbblabel.vertexlabel)
  fwevent.addCollection("jets","vector<pat::Jet>",zbblabel.jetlabel)
  fwevent.addCollection("MET","vector<pat::MET>",zbblabel.metlabel)
  fwevent.addCollection("Zmumu","vector<reco::CompositeCandidate>",zbblabel.zmumulabel)
  fwevent.addCollection("Zelel","vector<reco::CompositeCandidate>",zbblabel.zelelabel)
  fwevent.addCollection("trigger","pat::TriggerEvent",zbblabel.triggerlabel)
  fwevent.addCollection("electrons","vector<pat::Electron>",zbblabel.allelectronslabel)
  fwevent.addCollection("muons","vector<pat::Muon>",zbblabel.allmuonslabel)
  # producers used later on
  fwevent.addProducer("catMu",category,muChannel=True)
  fwevent.addProducer("catEle",category,muChannel=False)
  fwevent.addProducer("vertex",vertex)
  fwevent.addProducer("bestZcandidate",bestZcandidate)
  fwevent.addProducer("bbHE",candidateproducer,candidate="bbHE")
  fwevent.addProducer("bbHP",candidateproducer,candidate="bbHP")
  fwevent.addProducer("ZbHE",candidateproducer,candidate="ZbHE")
  fwevent.addProducer("ZbHP",candidateproducer,candidate="ZbHP")
  fwevent.addProducer("ZbbHE",candidateproducer,candidate="ZbbHE")
  fwevent.addProducer("ZbbHP",candidateproducer,candidate="ZbbHP")
  # add some information to the event before printing
  # products from producers are not printed if they are not in cache
  tmp = fwevent.catMu, fwevent.catEle, fwevent.ZbHE, fwevent.ZbHP, fwevent.ZbbHE, fwevent.ZbbHP
  # Now, wa can go on with the printing.
  print fwevent

