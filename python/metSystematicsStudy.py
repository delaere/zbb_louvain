import ROOT
import sys
import os 
from DataFormats.FWLite import Events, Handle
from eventSelection import *
from LumiReWeighting import *
from btaggingWeight import *
from LeptonsReweighting import *
from zbbCommons import zbblabel,zbbfile

# this method compares the efficiency of variants of MET produced by the PAT tool.
# there is no need for a special tool to compute the MET efficiency itself,
# as it is simply the ratio of the yield before/after the cut.
def metSystematicsStudy(stage=6, muChannel=True, path='../testfiles/'):
  # prepare output
  f = ROOT.TFile( 'metSystematics.root', 'RECREATE' )
  histogram = ROOT.TH1F( 'metsig_Systematics', 'metSystematics significance', 20,0,20)
  histogram2 = ROOT.TH1F( 'metcut_Systematics', 'metSystematics met', 20,0,20)
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
  # list of the met alternatives. The default one is in zbbCommons.
  metVariantLabels = [ "patType1CorrectedPFMetElectronEnDown" ,
                       "patType1CorrectedPFMetElectronEnUp" ,
                       "patType1CorrectedPFMetJetEnDown" ,
                       "patType1CorrectedPFMetJetEnUp",
                       "patType1CorrectedPFMetJetResDown",
                       "patType1CorrectedPFMetJetResUp", 
                       "patType1CorrectedPFMetMuonEnDown" ,
                       "patType1CorrectedPFMetTauEnDown" ,
                       "patType1CorrectedPFMetTauEnUp" ,
                       "patType1CorrectedPFMetUnclusteredEnDown",
                       "patType1CorrectedPFMetMuonEnUp" ,
                       "patType1CorrectedPFMetUnclusteredEnUp" ]
  #metHandles = [Handle ("vector<pat::MET>") for _ in metVariantLabels]
  metSignCut = 10.
  metcut = 50.
  # reweighting engines
  lumiWeightEngine = LumiReWeighting()
  btagWeightEngine = btaggingWeight(0,999,0,999,zbbfile.ssvperfData)
  catName = categoryName(stage)
  if catName.find("(HEHE") != -1:
    btagWeightEngine.setMode("HEHE")
  elif catName.find("(HEHP") != -1:
    btagWeightEngine.setMode("HEHP")
  elif catName.find("(HPHP") != -1:
    btagWeightEngine.setMode("HPHP")
  elif catName.find("(HE") != -1:
    if catName.find("exclusive") != -1:
      btagWeightEngine.setMode("HEexcl")
    else:
      btagWeightEngine.setMode("HE")
  elif catName.find("(HP") != -1:
    if catName.find("exclusive") != -1:
      btagWeightEngine.setMode("HPexcl")
    else:
      btagWeightEngine.setMode("HP")
  else: btagWeightEngine = None
  leptonWeightEngine = LeptonsReWeighting()
  # event loop
  eventCnt = 0
  totWeight = 0.
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
      if eventCnt%100==0 : print eventCnt
      # weight
      weight = 1.
      weight *= lumiWeightEngine.weight( fwevent = event )
      weight *= leptonWeightEngine.weight( event, muChannel )
      if btagWeightEngine is not None: weight *= btagWeightEngine.weight( event, muChannel )
      totWeight = totWeight + weight
      # now, get check the MET cut for all hypotheses.
      for idx,metVariant in enumerate(metVariantLabels):
        event.getByLabel (metVariant,metHandle)
        met = metHandle.product()
        if met[0].significance() < metSignCut:
          histogram.Fill(idx+1,weight)
        if met[0].pt() < metcut:
          histogram2.Fill(idx+1,weight)
  # summary and output
  histogram.Scale(1/totWeight)
  histogram2.Scale(1/totWeight)
  print "Processed ", eventCnt, " events, for a total weight of ", totWeight, "."
  print "Result:"
  histogram.Print("all")
  histogram2.Print("all")
  f.cd()
  resultMetSig = ROOT.TH1F("resultMetSig","resultMetSig",10000,0,1)
  resultMetCut = ROOT.TH1F("resultMetCut","resultMetCut",10000,0,1)
  for bin in range(1,21):
    if histogram.GetBinContent(bin)>0.01:
      resultMetSig.Fill(histogram.GetBinContent(bin))
    if histogram2.GetBinContent(bin)>0.01:
      resultMetCut.Fill(histogram2.GetBinContent(bin))
  f.Write()
  f.Close()

