#! /usr/bin/env python

import ROOT
import sys
from DataFormats.FWLite import Events, Handle
from eventSelection import *

class EventSelectionControlPlots:
    """A class to create control plots for event selection"""

    def __init__(self, dir=None, muChannel=True):
      # create output file if needed. If no file is given, it means it is delegated
      if dir is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("eventSelection")
      else :
        self.f = None
        self.dir = dir
      self.muChannel = muChannel
    
    def beginJob(self, jetlabel="cleanPatJets", zmulabel="Ztightloose", zelelabel="Zelel", triggerlabel="WeightFromTrigger"):
      # declare histograms
      self.dir.cd()
      self.h_triggerSelection = ROOT.TH1I("triggerSelection","triggerSelection ",2,0,2)
      self.h_triggerBit = ROOT.TH1I("triggerBits","trigger bits",20,0,20)
      self.h_zmassMu = ROOT.TH1F("zmassMu","zmassMu",2000,0,200)
      self.h_massBestMu = ROOT.TH1F("bestzmassMu","bestzmassMu",2000,0,200)
      self.h_zmassEle = ROOT.TH1F("zmassEle","zmassEle",2000,0,200)
      self.h_massBestEle = ROOT.TH1F("bestzmassEle","bestzmassEle",2000,0,200)
      self.h_zptMu = ROOT.TH1F("zptMu","zptMu",500,0,500)
      self.h_ptBestMu = ROOT.TH1F("bestzptMu","bestzptMu",500,0,500)
      self.h_zptEle = ROOT.TH1F("zptEle","zptEle",500,0,500)
      self.h_ptBestEle = ROOT.TH1F("bestzptEle","bestzptEle",500,0,500)
      self.h_scaldptZbj1 = ROOT.TH1F("scaldptZbj1","scaldptZbj1",500,0,500)
      self.h_drZbj1 = ROOT.TH1F("drZbj1","distance between Z and leading jet",100,0,5)
      self.h_vecdptZbj1 = ROOT.TH1F("vecdptZbj1","vecdptZbj1",500,0,500)
      self.h_dphiZbj1 = ROOT.TH1F("dphiZbj1","dphiZbj1",80,-4,4)
      self.h_dijetM = ROOT.TH1F("dijetM","b bbar invariant mass",1000,0,1000)
      self.h_dijetPt = ROOT.TH1F("dijetPt","b bbar Pt",500,0,500)
      self.h_ZbM = ROOT.TH1F("ZbM","Zb invariant mass",1000,0,1000)
      self.h_ZbPt = ROOT.TH1F("ZbPt","Zb Pt",500,0,500)
      self.h_ZbbM = ROOT.TH1F("ZbbM","Zbb invariant mass",1000,0,1000)
      self.h_ZbbPt = ROOT.TH1F("ZbbPt","Zbb Pt",500,0,500)
      self.h_ZbbM2D = ROOT.TH2F("ZbbM2D","Zbb mass vs bb mass",100,0,1000,100,0,1000)
      self.h_category = ROOT.TH1I("category","event category",10,0,10)  
      self.h_mu1pt = ROOT.TH1F("mu1pt","leading muon Pt",500,0,500)
      self.h_mu2pt = ROOT.TH1F("mu2pt","subleading muon Pt",500,0,500)
      self.h_mu1eta = ROOT.TH1F("mu1eta","leading muon Eta",50,-2.5,2.5)
      self.h_mu2eta = ROOT.TH1F("mu2eta","subleading muon Eta",50,-2.5,2.5)
      self.h_el1pt = ROOT.TH1F("el1pt","leading electron Pt",500,0,500)
      self.h_el2pt = ROOT.TH1F("el2pt","subleading electron Pt",500,0,500)
      self.h_el1eta = ROOT.TH1F("el1eta","leading electron Eta",50,-2.5,2.5)
      self.h_el2eta = ROOT.TH1F("el2eta","subleading electron Eta",50,-2.5,2.5)
      
      # prepare handles
      self.jetHandle = Handle ("vector<pat::Jet>")
      self.zmuHandle = Handle ("vector<reco::CompositeCandidate>")
      self.zeleHandle = Handle ("vector<reco::CompositeCandidate>")
      self.trigInfoHandle = Handle ("vector<bool>")
      self.jetlabel = (jetlabel)
      self.zmulabel = (zmulabel)
      self.zelelabel = (zelelabel)
      self.trigInfolabel = (triggerlabel)
    
    def processEvent(self,event):
      # load event
      event.getByLabel (self.jetlabel,self.jetHandle)
      event.getByLabel (self.zmulabel,self.zmuHandle)
      event.getByLabel (self.zelelabel,self.zeleHandle)
      #event.getByLabel (self.trigInfolabel,"SelectedTriggers",self.trigInfoHandle)
      jets = self.jetHandle.product()
      zCandidatesMu = self.zmuHandle.product()
      zCandidatesEle = self.zeleHandle.product()
      #triggerInfo = self.trigInfoHandle.product()
      triggerInfo = None

      ## trigger
      # TODO: ROOT BUG HERE : vector<bool> dictionnary is incomplete
      #for i in range(13):
      #  if triggerInfo[i] : self.h_triggers.Fill(i)
      #self.h_triggerSelection.Fill(isTriggerOK(triggerInfo, self.muChannel))
      #trigger = 0
      #for trigger in range(triggerInfo.size()):
      #  if triggerInfo[trigger] : self.h_triggerBit.Fill(trigger)

      # Z boson
      for z in zCandidatesMu:
        self.h_zmassMu.Fill(z.mass())
        self.h_zptMu.Fill(z.pt())
      for z in zCandidatesEle:
        self.h_zmassEle.Fill(z.mass())
        self.h_zptEle.Fill(z.pt())
      bestZcandidate = findBestCandidate(zCandidatesMu,zCandidatesEle) 
      if not bestZcandidate is None:
        if bestZcandidate.daughter(0).isMuon():
          self.h_massBestMu.Fill(bestZcandidate.mass())
          self.h_ptBestMu.Fill(bestZcandidate.pt())
        if bestZcandidate.daughter(0).isElectron() :
          self.h_massBestEle.Fill(bestZcandidate.mass())
          self.h_ptBestEle.Fill(bestZcandidate.pt())

      # event category
      category = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, self.muChannel)
      self.h_category.Fill(category)

      # some topological quantities
      if category>= 2:
        #dilepton plots
        if bestZcandidate.daughter(0).isMuon():
          mu1 = bestZcandidate.daughter(0)
          mu2 = bestZcandidate.daughter(1)
          if mu1.pt() < mu2.pt():
            mu1 = bestZcandidate.daughter(1)
            mu2 = bestZcandidate.daughter(0)
          self.h_mu1pt.Fill(mu1.pt())
          self.h_mu2pt.Fill(mu2.pt())
          self.h_mu1eta.Fill(mu1.eta())
          self.h_mu2eta.Fill(mu2.eta())
        elif bestZcandidate.daughter(0).isElectron():
          ele1 = bestZcandidate.daughter(0)
          ele2 = bestZcandidate.daughter(1)
          if ele1.pt() < ele2.pt():
            ele1 = bestZcandidate.daughter(1)
            ele2 = bestZcandidate.daughter(0)
          self.h_el1pt.Fill(ele1.pt())
          self.h_el2pt.Fill(ele2.pt())
          self.h_el1eta.Fill(ele1.eta())
          self.h_el2eta.Fill(ele2.eta())
      if category>= 5:
        #bjets plots
        nJets = 0
        bjet1 = None
        bjet2 = None
        for jet in jets:
          if isGoodJet(jet):
            if isBJet(jet,"HE"): 
              nJets += 1
              if nJets==1: bjet1 = jet
              elif nJets==2: bjet2 = jet
              else : break
        if bjet1 is None: return # we stop here is no bjet... should not be the case in category 5
        b1 = ROOT.TLorentzVector(bjet1.px(),bjet1.py(),bjet1.pz(),bjet1.energy())
        z = ROOT.TLorentzVector(bestZcandidate.px(),bestZcandidate.py(),bestZcandidate.pz(),bestZcandidate.energy())
        Zb = z+b1
        self.h_scaldptZbj1.Fill(bestZcandidate.pt()-bjet1.pt())
        self.h_vecdptZbj1.Fill(Zb.Pt())
        self.h_drZbj1.Fill(z.DeltaR(b1))
        self.h_dphiZbj1.Fill(z.DeltaPhi(b1))
        self.h_ZbM.Fill(Zb.M())
        self.h_ZbPt.Fill(Zb.Pt())
        if bjet2 is None: return # the rest is about bb pairs
        b2 = ROOT.TLorentzVector(bjet2.px(),bjet2.py(),bjet2.pz(),bjet2.energy())
        bb = b1 + b2
        self.h_dijetM.Fill(bb.M())
        self.h_dijetPt.Fill(bb.Pt())
        Zbb = Zb + b2
        self.h_ZbbM.Fill(Zbb.M())
        self.h_ZbbPt.Fill(Zbb.Pt())
        self.h_ZbbM2D.Fill(Zbb.M(),bb.M())
    
    def endJob(self):
      self.dir.cd()
      self.dir.Write()
      if not self.f is None:
        self.f.Close()

def runTest():
  controlPlots = EventSelectionControlPlots(muChannel=True)
  path="/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/"
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)
  controlPlots.beginJob()
  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    controlPlots.processEvent(event)
    i += 1
  controlPlots.endJob()

