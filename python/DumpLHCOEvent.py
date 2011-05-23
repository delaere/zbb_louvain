from itertools import combinations
import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from eventSelection import eventCategories, isInCategory, findBestCandidate, isGoodJet

def DumpLHCOEvent(fwevent=None, run=None, event=None, lumi=None, path="", file=None):
  """Dump informations about a given event in the LHCO format for MadWeight"""
  # output must be specified
  if file is None:
    print "Output must be specified. Set file argument to the file object opened for writing"
    return
  # in case no fwevent is provided, find it using run,event,(lumi)
  if fwevent is None:
    if (run is None) or (event is None):
      print "DumpLHCOEvent Error: either pass a fwlite event or give both run and event number"
      return
    # find event based on run  and event
    dirList=os.listdir(path)
    files=[]
    for fname in dirList:
      files.append(path+fname)
    events = Events (files)
    # there is the method to(run, event) can we use it ???
    for fwevent in events:
      if fwevent.eventAuxiliary().run()==run and fwevent.eventAuxiliary().id().event()==event and ( lumi is None or fwevent.eventAuxiliary().luminosityBlock()==lumi) :
        break
    if fwevent.eventAuxiliary().run()==run and fwevent.eventAuxiliary().id().event()==event and ( lumi is None or fwevent.eventAuxiliary().luminosityBlock()==lumi) :
      DumpLHCOEvent(fwevent)
    else:
      print "Event not found."
    return
  # in case a fwevent is provided, use it
  PrintEvent(fwevent)
  # load objects
  jetHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  fwevent.getByLabel ("cleanPatJets",jetHandle)
  fwevent.getByLabel ("patMETsPF",metHandle)
  fwevent.getByLabel ("Ztighttight",zmuHandle)
  fwevent.getByLabel ("Zelel",zeleHandle)
  jets = jetHandle.product()
  met = metHandle.product()
  zCandidatesMu = zmuHandle.product()
  zCandidatesEle = zeleHandle.product()
  # find the best z candidate
  bestZcandidate = findBestCandidate(None,zCandidatesMu,zCandidatesEle)
  # print its constituents
  PrintLepton(bestZcandidate.daughter(0),file,1)
  PrintLepton(bestZcandidate.daughter(1),file,2)
  # loop over jets and print
  counter = 3
  for jet in jets:
    if isGoodJet(jet) :
      PrintJet(jet,file,counter)
      counter = counter + 1
  # print MET
  PrintMET(met[0],file,counter)

def PrintEvent(event, file) :
  file.write('0' + srt(event.eventAuxiliary().run()) + ' ' +srt(event.eventAuxiliary().id().event())+' \n')

def PrintLepton(lepton, file, index) :
  if lepton.isMuon():
    file.write(str(index) + ' 2' + str(lepton.eta()) + ' ' + str(lepton.phi()) + ' ' + str(lepton.pt()) + ' ' + str(lepton.mass()) + ' ' + str(lepton.charge()) + ' 0 0 0 0 \n')
  elif lepton.isElectron():
    file.write(str(index) + ' 1' + str(lepton.eta()) + ' ' + str(lepton.phi()) + ' ' + str(lepton.pt()) + ' ' + str(lepton.mass()) + ' ' + str(lepton.charge()) + ' 0 0 0 0 \n')
  else:
    print "ERROR: can only handle electrons or muons"

def PrintJet(jet, file, index) :
  file.write(str(index) + ' 4' + str(jet.eta()) + ' ' + str(jet.phi()) + ' ' + str(jet.pt()) + ' ' + str(jet.mass()) + ' ' + str(jet.charge()) + ' 2 0 0 0 \n')

def PrintMET(met, file, index) :
  file.write(str(index) + ' 6' + str(met.eta()) + ' ' + str(met.phi()) + ' ' + str(met.pt()) + ' 0 0 0 0 0 0 \n')

def dumpAll(stage=7, muChannel=True, path="/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/", fileAll="INCL.lhco", file2j="2jets.lhco", file3j="3jets.lhco"):
  # prepare output
  out_file_INCL= open(fileAll,"w")
  out_file_2j= open(file2j,"w")
  out_file_3j= open(file3j,"w")
  # read and process data
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)
  metlabel="patMETsPF"
  jetlabel="cleanPatJets"
  zmulabel="Ztighttight"
  zelelabel="Zelel"
  triggerlabel="patTriggerEvent"
  jetHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  trigInfoHandle = Handle ("pat::TriggerEvent")
  for event in events:
    event.getByLabel (jetlabel,jetHandle)
    event.getByLabel (metlabel,metHandle)
    event.getByLabel (zmulabel,zmuHandle)
    event.getByLabel (zelelabel,zeleHandle)
    event.getByLabel (triggerlabel,trigInfoHandle)
    jets = jetHandle.product()
    met = metHandle.product()
    zCandidatesMu = zmuHandle.product()
    zCandidatesEle = zeleHandle.product()
    triggerInfo = trigInfoHandle.product()
    for jet in jets:
      if isGoodJet(jet): 
        jetCount = jetCount+1
    if isInCategory(stage, triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, muChannel) and jetCount>1 :
      DumpLHCOEvent(event, out_file_INCL)
      if jetCount>2:
        DumpLHCOEvent(event, out_file_3j)
      else : 
        DumpLHCOEvent(event, out_file_2j)
  # close files
  out_file_INCL.close()  
  out_file_2j.close()
  out_file_3j.close()

