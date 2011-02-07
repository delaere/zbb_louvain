#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from eventSelection import *

class EventSelectionControlPlots:
    """A class to create control plots for event selection"""

    def __init__(self, dir=None, muChannel=True, checkTrigger=False):
      # create output file if needed. If no file is given, it means it is delegated
      if dir is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("eventSelection")
      else :
        self.f = None
        self.dir = dir
      self.muChannel = muChannel
      self.checkTrigger = checkTrigger
    
    def beginJob(self, metlabel="patMETsPF", jetlabel="cleanPatJets", zmulabel="Ztighttight", zelelabel="Zelel", triggerlabel="patTriggerEvent"):
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
      self.h_dphiZbj1 = ROOT.TH1F("dphiZbj1","dphiZbj1",40,0,4)
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
      self.h_mu1eta = ROOT.TH1F("mu1eta","leading muon Eta",25,0,2.5)
      self.h_mu2eta = ROOT.TH1F("mu2eta","subleading muon Eta",25,0,2.5)
      self.h_el1pt = ROOT.TH1F("el1pt","leading electron Pt",500,0,500)
      self.h_el2pt = ROOT.TH1F("el2pt","subleading electron Pt",500,0,500)
      self.h_el1eta = ROOT.TH1F("el1eta","leading electron Eta",25,0,2.5)
      self.h_el2eta = ROOT.TH1F("el2eta","subleading electron Eta",25,0,2.5)

### jet stuff

      self.h_SSVHEdisc = ROOT.TH1F("SSVHEdisc","SSVHEdisc",200,-10,10)
      self.h_SSVHPdisc = ROOT.TH1F("SSVHPdisc","SSVHPdisc",200,-10,10)
      self.h_met = ROOT.TH1F("MET","MET",100,0,200)
      self.h_phimet = ROOT.TH1F("METphi","MET #phi",70,-3.5,3.5)
      self.h_jetpt = ROOT.TH1F("jetpt","Jet Pt",100,15,215)
      self.h_jeteta = ROOT.TH1F("jeteta","Jet eta",25,0, 2.5)
      self.h_jetphi = ROOT.TH1F("jetphi","Jet phi",80,-4,4)
      self.h_jetoverlapmu = ROOT.TH1I("jetoverlapmu","jets overlaps with muons",2,0,2)
      self.h_jetoverlapele = ROOT.TH1I("jetoverlapele","jets overlaps with electrons",2,0,2)
      self.h_jet1pt = ROOT.TH1F("jet1pt","leading jet Pt",500,0,500)
      self.h_jet1eta = ROOT.TH1F("jet1eta","leading jet Eta",25,0,2.5)
      self.h_jet2pt = ROOT.TH1F("jet2pt","subleading jet Pt",500,0,500)
      self.h_jet2eta = ROOT.TH1F("jet2eta","subleading jet Eta",25,0,2.5)
      self.h_bjet1pt = ROOT.TH1F("bjet1pt","leading bjet Pt",500,0,500)
      self.h_bjet1eta = ROOT.TH1F("bjet1eta","leading bjet Eta",25,0,2.5)
      self.h_bjet2pt = ROOT.TH1F("bjet2pt","subleading bjet Pt",500,0,500)
      self.h_bjet2eta = ROOT.TH1F("bjet2eta","subleading bjet Eta",25,0,2.5)
      self.h_nj = ROOT.TH1I("nj","jet count",15,0,15)
      self.h_nb = ROOT.TH1I("nb","b-jet count",5,0,5)
      self.h_nbP = ROOT.TH1I("nbP","pure b-jet count",5,0,5)
      self.h_njb = ROOT.TH2I("njb","number of bjets vs number of jets",15,0,15,5,0,5)
      self.h_nhf = ROOT.TH1F("nhf","neutral hadron energy fraction",101,0,1.01)
      self.h_nef = ROOT.TH1F("nef","neutral EmEnergy fraction",101,0,1.01)
      self.h_nconstituents = ROOT.TH1I("npf","total multiplicity",50,0,50)
      self.h_chf = ROOT.TH1F("chf","charged hadron energy fraction",101,0,1.01)
      self.h_nch = ROOT.TH1I("nch","charged multiplicity",50,0,50)
      self.h_cef = ROOT.TH1F("cef","charged EmEnergy fraction",101,0,1.01)
      self.h_jetid = ROOT.TH1I("jetid","Jet Id level (none, loose, medium, tight)",4,0,4)
      
      # prepare handles
      self.jetHandle = Handle ("vector<pat::Jet>")
      self.metHandle = Handle ("vector<pat::MET>")
      self.zmuHandle = Handle ("vector<reco::CompositeCandidate>")
      self.zeleHandle = Handle ("vector<reco::CompositeCandidate>")
      self.trigInfoHandle = Handle ("pat::TriggerEvent")
      self.jetlabel = (jetlabel)
      self.metlabel = (metlabel)
      self.zmulabel = (zmulabel)
      self.zelelabel = (zelelabel)
      self.trigInfolabel = (triggerlabel)
    
    def processEvent(self,event):
      # load event
      event.getByLabel (self.jetlabel,self.jetHandle)
      event.getByLabel (self.metlabel,self.metHandle)
      event.getByLabel (self.zmulabel,self.zmuHandle)
      event.getByLabel (self.zelelabel,self.zeleHandle)
      jets = self.jetHandle.product()
      met = self.metHandle.product()
      zCandidatesMu = self.zmuHandle.product()
      zCandidatesEle = self.zeleHandle.product()
      if self.checkTrigger:
        event.getByLabel (self.trigInfolabel,self.trigInfoHandle)
        triggerInfo = self.trigInfoHandle.product()
      else:
        triggerInfo = None

      ## trigger
      self.h_triggerSelection.Fill(isTriggerOK(triggerInfo, self.muChannel))
      selTriggers = selectedTriggers(triggerInfo)
      for trigger,triggered in enumerate(selTriggers):
        if triggered : self.h_triggerBit.Fill(trigger)

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
      category = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, self.muChannel)
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
          self.h_mu1eta.Fill(abs(mu1.eta()))
          self.h_mu2eta.Fill(abs(mu2.eta()))
        elif bestZcandidate.daughter(0).isElectron():
          ele1 = bestZcandidate.daughter(0)
          ele2 = bestZcandidate.daughter(1)
          if ele1.pt() < ele2.pt():
            ele1 = bestZcandidate.daughter(1)
            ele2 = bestZcandidate.daughter(0)
          self.h_el1pt.Fill(ele1.pt())
          self.h_el2pt.Fill(ele2.pt())
          self.h_el1eta.Fill(abs(ele1.eta()))
          self.h_el2eta.Fill(abs(ele2.eta()))
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
        self.h_dphiZbj1.Fill(abs(z.DeltaPhi(b1)))
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


      # process event and fill histograms
      # jets 
      nj  = 0
      nb  = 0
      nbP = 0
      for jet in jets:
        if category>=4 and isGoodJet(jet,bestZcandidate):#hasNoOverlap(jet, bestZcandidate): 
          self.h_jetpt.Fill(jet.pt())
          self.h_jeteta.Fill(abs(jet.eta()))
          self.h_jetphi.Fill(jet.phi())
          self.h_jetoverlapmu.Fill(jet.hasOverlaps("muons"))
          self.h_jetoverlapele.Fill(jet.hasOverlaps("electrons"))
          rawjet = jet # TODO: in principle, one should do: rawjet = jet.correctedJet("RAW") but one needs RAW factors in the tuple
          self.h_nhf.Fill(( rawjet.neutralHadronEnergy() + rawjet.HFHadronEnergy() ) / rawjet.energy())
          self.h_nef.Fill(rawjet.neutralEmEnergyFraction())
          self.h_nconstituents.Fill(rawjet.numberOfDaughters())
          self.h_chf.Fill(rawjet.chargedHadronEnergyFraction())
          self.h_nch.Fill(rawjet.chargedMultiplicity())
          self.h_cef.Fill(rawjet.chargedEmEnergyFraction())
          if jetId(jet,"tight"): self.h_jetid.Fill(3)
          elif jetId(jet,"medium"): self.h_jetid.Fill(2)
          elif jetId(jet,"loose"): self.h_jetid.Fill(1)
          else: self.h_jetid.Fill(0)
          # B-tagging
          self.h_SSVHEdisc.Fill(jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"))
          self.h_SSVHPdisc.Fill(jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"))
          #eventually complement with variables from the btagging (check paper)
          nj += 1
          if nj==1: 
            self.h_jet1pt.Fill(jet.pt())
            self.h_jet1eta.Fill(abs(jet.eta()))
          elif nj==2:
            self.h_jet2pt.Fill(jet.pt())
            self.h_jet2eta.Fill(abs(jet.eta()))
          if isBJet(jet,"HE"): 
            nb += 1
            if nb==1:
              self.h_bjet1pt.Fill(jet.pt())
              self.h_bjet1eta.Fill(abs(jet.eta()))
            elif nb==2:
              self.h_bjet2pt.Fill(jet.pt())
              self.h_bjet2eta.Fill(abs(jet.eta()))
          if isBJet(jet,"HP"): nbP += 1
      self.h_nj.Fill(nj)
      self.h_nb.Fill(nb)
      self.h_nbP.Fill(nbP)
      self.h_njb.Fill(nj,nb)
      self.h_met.Fill(met[0].pt())
      self.h_phimet.Fill(met[0].phi())


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

