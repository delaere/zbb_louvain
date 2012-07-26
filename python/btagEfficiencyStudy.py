import ROOT
import sys
import os 
from DataFormats.FWLite import Events, Handle
from eventSelection import *
from LumiReWeighting import *
from zbbCommons import zbblabel,zbbfile


def btagEfficiencyTreeProducer(stage=4, muChannel=True, path='../testfiles/'):
  # prepare output
  ROOT.gROOT.ProcessLine(
  "struct MyStruct {\
     Float_t     pt;\
     Float_t     eta;\
     Int_t       flavor;\
     Float_t     ssvhe;\
     Float_t     ssvhp;\
     Float_t     eventWeight;\
  };" )
  from ROOT import MyStruct
  mystruct = MyStruct()
  f = ROOT.TFile( 'mybtagEfftree.root', 'RECREATE' )
  tree = ROOT.TTree( 'btagEff', 'btag efficiency' )
  tree.Branch( 'data', mystruct, 'pt/F:eta/F:flavor/I:ssvhe/F:ssvhp/F:eventWeight/F' )
  # input
  dirList=os.listdir(path) 
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)
  metlabel=zbblabel.metlabel
  jetlabel=zbblabel.jetlabel
  zmulabel=zbblabel.zmumulabel
  zelelabel=zbblabel.zelelabel
  triggerlabel=zbblabel.triggerlabel
  vertexlabel = zbblabel.vertexlabel
  jetHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  vertexHandle = Handle ("vector<reco::Vertex>")
  trigInfoHandle = Handle ("pat::TriggerEvent")
  weight_engine = LumiReWeighting(zbbfile.pileupMC, zbbfile.pileupData, zbblabel.pulabel)
  # event loop
  eventCnt = 0
  for event in events:
    event.getByLabel (jetlabel,jetHandle)
    event.getByLabel (metlabel,metHandle)
    event.getByLabel (zmulabel,zmuHandle)
    event.getByLabel (zelelabel,zeleHandle)
    event.getByLabel (triggerlabel,trigInfoHandle)
    event.getByLabel (vertexlabel,vertexHandle)
    jets = jetHandle.product()
    met = metHandle.product()
    zCandidatesMu = zmuHandle.product()
    zCandidatesEle = zeleHandle.product()
    vertices = vertexHandle.product()
    #triggerInfo = trigInfoHandle.product()
    triggerInfo = None
    runNumber= event.eventAuxiliary().run()
    categoryData = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, vertices, jets, met, runNumber, muChannel)
    if vertices.size()>0 :
          vertex = vertices[0]
    else:
          vertex = None
    bestZcandidate = findBestCandidate(None,vertex,zCandidatesMu,zCandidatesEle)
    if isInCategory(stage, categoryData):
      eventCnt = eventCnt +1
      if eventCnt%100==0 : print ".",
      if eventCnt%1000==0 : print ""
      # event weight
      mystruct.eventWeight = weight_engine.weight( fwevent=event )
      # that's where we access the jets
      for jet in jets:
        if not isGoodJet(jet,bestZcandidate): continue
        mystruct.pt = jet.pt()
        mystruct.eta = jet.eta()
        mystruct.flavor = jet.partonFlavour()
        mystruct.ssvhe = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
        mystruct.ssvhp = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
        tree.Fill()
  f.Write()
  f.Close()
  print ""

