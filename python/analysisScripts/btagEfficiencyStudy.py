import ROOT
import sys
import os 
from AnalysisEvent import AnalysisEvent
from eventSelection import *
from LumiReWeighting import *
from zbbCommons import zbblabel,zbbfile

def btagEfficiencyTreeProducer(stageName="Z+jet", muChannel=True, path='../testfiles/'):
  #search for category number
  stage=-1
  for cat in categoryNames :
    stage+=1
    if cat==stageName : break
  # prepare output
  path='/nfs/user/llbb/Pat_8TeV_532p4/DYjets_Summer12_V2/'
  ROOT.gROOT.ProcessLine(
  "struct MyStruct {\
     Float_t     pt;\
     Float_t     eta;\
     Int_t       flavor;\
     Float_t     ssvhe;\
     Float_t     ssvhp;\
     Float_t     csv;\
     Float_t     eventWeight;\
  };" )
  from ROOT import MyStruct
  mystruct = MyStruct()
  f = ROOT.TFile( 'mybtagEfftree.root', 'RECREATE' )
  tree = ROOT.TTree( 'btagEff', 'btag efficiency' )
  tree.Branch( 'data', mystruct, 'pt/F:eta/F:flavor/I:ssvhe/F:ssvhp/F:csv/F:eventWeight/F' )
  # input
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
  prepareAnalysisEvent(events,btagging="CSV",ZjetFilter="bcl",checkTrigger=False)
  weight_engine = LumiReWeighting(zbbfile.pileupMC, zbbfile.pileupData)
  # event loop
  eventCnt = 0
  print "starting loop on events"
  for event in events:
    categoryData = event.catMu if muChannel else event.catEle
    goodJets = event.goodJets_mu if muChannel else event.goodJets_ele
    if isInCategory(stage, categoryData):
      eventCnt = eventCnt +1
      if eventCnt%100==0 : print ".",
      if eventCnt%1000==0 : print ""
      # event weight
      mystruct.eventWeight = weight_engine.weight( event=event )
      # that's where we access the jets
      for index,jet in enumerate(event.jets):
        if not goodJets[index]: continue
        mystruct.pt = jet.pt()
        mystruct.eta = jet.eta()
        mystruct.flavor = jet.partonFlavour()
        mystruct.ssvhe = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
        mystruct.ssvhp = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
        mystruct.csv = jet.bDiscriminator("combinedSecondaryVertexBJetTags")
        tree.Fill()
  f.Write()
  f.Close()
  print ""

