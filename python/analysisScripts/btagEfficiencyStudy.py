import ROOT
import sys
import os 

from UserCode.zbb_louvain.PatAnalysis.AnalysisEvent import AnalysisEvent
theUserConf = __import__(os.path.splitext('UserCode.zbb_louvain.zbbConfig')[0])
os.environ["PatAnalysisCfg"]='UserCode.zbb_louvain.zbbConfig'
from UserCode.zbb_louvain.PatAnalysis.CPconfig import configuration
import UserCode.zbb_louvain.PatAnalysis.EventSelection as EventSelection
from UserCode.zbb_louvain.ZbbEventSelection import *

def btagEfficiencyTreeProducer(stageName="Z+jet", output="mybtagEfftree.root", path='../testfiles/'):
  #search for category number
  stage=-1
  liststage = []
  for cat in categoryNames :
    stage+=1
    if stageName in cat : liststage.append(stage)
  print "Will run on stages: "
  for ls in liststage : print categoryNames[ls]
  # prepare output
  #path='/nfs/user/llbb/Pat_8TeV_ReReco/Summer12_DYjets/pat53_1.root'
  ROOT.gROOT.ProcessLine(
  "struct MyStruct {\
     Float_t     pt;\
     Float_t     eta;\
     Int_t       flavor;\
     Float_t     ssvhe;\
     Float_t     ssvhp;\
     Float_t     csv;\
     Float_t     jbp;\
     Float_t     jp;\
     Float_t     csvv1;\
     Float_t     ivfhe;\
     Float_t     ivfhp;\
     Float_t     sv2;\
     Float_t     csvivf;\
     Float_t     csvv1sl;\
     Float_t     eventWeight;\
  };" )
  from ROOT import MyStruct
  mystruct = MyStruct()
  f = ROOT.TFile( output, 'RECREATE' )
  tree = ROOT.TTree( 'btagEff', 'btag efficiency' )
  tree.Branch( 'data', mystruct, 'pt/F:eta/F:flavor/I:ssvhe/F:ssvhp/F:csv/F:jbp/F:jp/F:csvv1/F:ivfhe/F:ivfhp/F:sv2/F:csvivf/F:csvv1sl/F:eventWeight/F' )
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
  EventSelection.prepareAnalysisEvent(events)
  # event loop
  eventCnt = 0
  print "starting loop on events"
  for event in events:
    categoryData = event.category
    if event.bestZmumuCandidate and event.bestZelelCandidate : goodJets = event.goodJets_all
    elif event.bestZelelCandidate : goodJets = event.goodJets_ele
    elif event.bestZmumuCandidate : goodJets = event.goodJets_mu
    else : goodJets = event.goodJets_none
    Pass = 0
    for ls in liststage:
      if isInCategory(ls, categoryData) : Pass+=1
    if Pass>0:
      eventCnt = eventCnt +1
      if eventCnt%100==0 : print ".",
      if eventCnt%1000==0 : print eventCnt
      # event weight
      mystruct.eventWeight = event.weight(weightList=["PileUp"])
      # that's where we access the jets
      for index,jet in enumerate(event.jets):
        if not goodJets[index]: continue
        mystruct.pt = jet.pt()
        mystruct.eta = jet.eta()
        mystruct.flavor = jet.partonFlavour()
        mystruct.ssvhe = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
        mystruct.ssvhp = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
        mystruct.csv = jet.bDiscriminator("combinedSecondaryVertexBJetTags")
        mystruct.jbp = jet.bDiscriminator("jetBProbabilityBJetTags")
        mystruct.jp = jet.bDiscriminator("jetProbabilityBJetTags")
        mystruct.csvv1 = jet.bDiscriminator("combinedSecondaryVertexV1BJetTags")
        mystruct.ivfhe = jet.bDiscriminator("simpleInclusiveSecondaryVertexHighEffBJetTags")
        mystruct.ivfhp = jet.bDiscriminator("simpleInclusiveSecondaryVertexHighPurBJetTags")
        mystruct.sv2 = jet.bDiscriminator("doubleSecondaryVertexHighEffBJetTags")
        mystruct.csvivf = jet.bDiscriminator("combinedInclusiveSecondaryVertexBJetTags")
        mystruct.csvv1sl = jet.bDiscriminator("combinedSecondaryVertexSoftPFLeptonV1BJetTags")
        tree.Fill()
  f.Write()
  f.Close()
  print ""

if len(sys.argv) >2 : btagEfficiencyTreeProducer(output=sys.argv[1], path=sys.argv[2])
