import os
from AnalysisEvent import AnalysisEvent
from eventSelection import prepareAnalysisEvent

import ROOT
from itertools import combinations
from eventSelection import isGoodJet, isBJet

# a method to add some 4vectors to the event
#TODO: move to eventSelection and use in EventSelectionControlPlots
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
      return map(lambda v:ROOT.TLorentzVector(v.Px(),v.Py(),v.Pz(),v.E()),map(lambda (a,b):a+b,combinations(map(lambda j: j.p4(),filter(lambda jet: isGoodJet(jet,fwevent.bestZcandidate) and isBJet(jet,"HP"),fwevent.jets)),2)))
    elif candidate=="bbHE":
      return map(lambda v:ROOT.TLorentzVector(v.Px(),v.Py(),v.Pz(),v.E()),map(lambda (a,b):a+b,combinations(map(lambda j: j.p4(),filter(lambda jet: isGoodJet(jet,fwevent.bestZcandidate) and isBJet(jet,"HE"),fwevent.jets)),2)))
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
  # collections and producers used in the analysis
  prepareAnalysisEvent(fwevent, btagging="SSV",ZjetFilter="bcl",checkTrigger=True)
  fwevent.addProducer("bbHE",candidateproducer,candidate="bbHE")
  fwevent.addProducer("bbHP",candidateproducer,candidate="bbHP")
  fwevent.addProducer("ZbHE",candidateproducer,candidate="ZbHE")
  fwevent.addProducer("ZbHP",candidateproducer,candidate="ZbHP")
  fwevent.addProducer("ZbbHE",candidateproducer,candidate="ZbbHE")
  fwevent.addProducer("ZbbHP",candidateproducer,candidate="ZbbHP")
  # add some information to the event before printing
  # products from producers are not printed if they are not in cache
  tmp = fwevent.catMu, fwevent.catEle, fwevent.bbHE, fwevent.bbHP, fwevent.ZbHE, fwevent.ZbHP, fwevent.ZbbHE, fwevent.ZbbHP, fwevent.bestZmumuCandidate, fwevent.bestZelelCandidate, fwevent.bestZcandidate, fwevent.dijet_muChannel, fwevent.dijet_eleChannel
  # Now, wa can go on with the printing.
  print fwevent

