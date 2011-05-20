#! /usr/bin/env python

import ROOT
import sys
import os
from math import sin
from DataFormats.FWLite import Events, Handle
from eventSelection import *

class MuonsControlPlots:
    """A class to create control plots for muons"""

    def __init__(self, dir=None):
      # create output file if needed. If no file is given, it means it is delegated
      if dir is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("muons")
      else :
        self.f = None
        self.dir = dir
    
    def beginJob(self, muonlabel="matchedMuons", muonType="tight"):
      # declare histograms
      self.dir.cd()
      self.h_muonType = ROOT.TH1F("muonType","Muon type", 4,0,4)
      self.h_muonhits = ROOT.TH1F("muonhits","Muon hits",50,0,50)
      self.h_muonIso = ROOT.TH1F("muonIso","Muon isolatio",20,0,0.2)
      self.h_muonPt = ROOT.TH1F("muonPt","Muon Pt",500,0,500)
      self.h_muonEta = ROOT.TH1F("muonEta","Muon Eta",25,0,2.5)
      self.h_muonEtapm = ROOT.TH1F("muonEtapm","Muon Eta",50,-2.5,2.5)
      self.h_muonChi2 = ROOT.TH1F("muonChi2","Muon normalized chi2",100,0,20)
      self.h_muonPHits = ROOT.TH1F("muonPHits","Muon Pixel hits",10,0,10)
      self.h_muonSHits = ROOT.TH1F("muonSHits","Muon Strip hits",30,0,30)
      self.h_muonMatches = ROOT.TH1F("muonMatches","Muon matched segments",10,0,10)
      self.h_muonMHits = ROOT.TH1F("muonMHits","Muon muon hits",100,0,100)
      self.h_nmu = ROOT.TH1F("nmu","muon count",5,0,5)
      
      # prepare handles
      self.muonHandle = Handle ("vector<pat::Muon>")
      self.muonlabel = (muonlabel)
      self.muonType = (muonType)
    
    def processEvent(self,event, weight = 1.):
      # load event
      event.getByLabel (self.muonlabel,self.muonHandle)
      muons = self.muonHandle.product()
      # process event and fill histograms
      nmu = 0
      for muon in muons:
        # for muons:
        self.h_muonType.Fill(muon.isGlobalMuon()+2*muon.isTrackerMuon(),weight)
        if muon.isTrackerMuon():
          self.h_muonhits.Fill(muon.innerTrack().numberOfValidHits(),weight)
          self.h_muonPHits.Fill(muon.innerTrack().hitPattern().numberOfValidPixelHits(),weight)
          self.h_muonSHits.Fill(muon.innerTrack().hitPattern().numberOfValidStripHits(),weight)
        else:
          self.h_muonhits.Fill(0,weight)
          self.h_muonPHits.Fill(0,weight)
          self.h_muonSHits.Fill(0,weight)
        if muon.isGlobalMuon():
          self.h_muonMHits.Fill(muon.globalTrack().hitPattern().numberOfValidMuonHits(),weight)
        else:
          self.h_muonMHits.Fill(0,weight)
        if muon.isTrackerMuon() and muon.isGlobalMuon():
          self.h_muonChi2.Fill(muon.normChi2(),weight)
        else:
          self.h_muonChi2.Fill(0,weight)
        self.h_muonIso.Fill((muon.trackIso()+muon.caloIso())/muon.pt(),weight)
        self.h_muonPt.Fill(muon.pt(),weight)
        self.h_muonEta.Fill(abs(muon.eta()),weight)
        self.h_muonEtapm.Fill(muon.eta(),weight)
        self.h_muonMatches.Fill(muon.numberOfMatches(),weight)
        if isGoodMuon(muon,self.muonType) : nmu += 1
      self.h_nmu.Fill(nmu,weight)
    
    def endJob(self):
      self.dir.cd()
      self.dir.Write()
      if not self.f is None:
        self.f.Close()

class ElectronsControlPlots:
    """A class to create control plots for electrons"""

    def __init__(self, dir=None):
      # create output file if needed. If no file is given, it means it is delegated
      if dir is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("electrons")
      else :
        self.f = None
        self.dir = dir
    
    def beginJob(self, electronlabel="matchedElectrons", electronType="tight"):
      # declare histograms
      self.dir.cd()
      self.h_eleid = ROOT.TH1F("eleid","electron id",10,0,10)
      self.h_elemisshits = ROOT.TH1F("elemisshits","Electron missing hits",5,0,5)
      self.h_elept = ROOT.TH1F("elept","electron pt",500,0,500)
      self.h_eleeta = ROOT.TH1F("eleeta","electron eta",30,0,3)
      self.h_eleetapm = ROOT.TH1F("eleetapm","electron eta",60,-3,3)
      self.h_eledb = ROOT.TH1F("eledb","electron dB",100,0,0.05)
      self.h_eleoverlapmu = ROOT.TH1F("eleoverlapmu","electrons overlaps with muon",2,0,2)
      self.h_eleHcalIso = ROOT.TH1F("eleHcalIso","Electron HCAL relative isolation dr03",100,0,0.2)
      self.h_eleEcalIso = ROOT.TH1F("eleEcalIso","Electron ECAL relative isolation dr03",100,0,0.2)
      self.h_eleTkIso = ROOT.TH1F("eleTkIso","Electron Tk relative isolation dr03",100,0,0.2)
      self.h_eleHoE = ROOT.TH1F("eleHoE","Electron H over E",100,0,0.1)
      self.h_eledphi = ROOT.TH1F("eledphi","Electron dphi at calo",100,0,0.1)
      self.h_eledeta = ROOT.TH1F("eledeta","Electron deta at calo",100,0,0.01)
      self.h_eleinin = ROOT.TH1F("eleinin","Electron sigma ieta ieta",100,0,0.1)
      self.h_nel = ROOT.TH1F("nel","electron count",5,0,5)

      # prepare handles
      self.electronHandle = Handle ("vector<pat::Electron>")
      self.electronlabel = (electronlabel)
      self.electronType = (electronType)
    
    def processEvent(self,event, weight = 1.):
      # load event
      event.getByLabel (self.electronlabel,self.electronHandle)
      electrons = self.electronHandle.product()
      # lepton selection
      nel = 0
      for electron in electrons:
        # for electrons
        self.h_eleid.Fill(electron.electronID("simpleEleId85relIso"), weight)
        self.h_elemisshits.Fill(electron.gsfTrack().numberOfLostHits(), weight)
        scEt = (electron.ecalEnergy()*sin(electron.theta()))
        self.h_eleHcalIso.Fill(electron.dr03HcalTowerSumEt()/scEt, weight)
        self.h_eleEcalIso.Fill(electron.dr03EcalRecHitSumEt()/scEt, weight)
        self.h_eleTkIso.Fill(electron.dr03TkSumPt()/scEt, weight)
        self.h_eleHoE.Fill(electron.hadronicOverEm(), weight)
        self.h_eledphi.Fill(electron.deltaPhiEleClusterTrackAtCalo(), weight)
        self.h_eledeta.Fill(electron.deltaEtaEleClusterTrackAtCalo(), weight)
        self.h_eleinin.Fill(electron.scSigmaIEtaIEta(), weight)
        self.h_elept.Fill(electron.pt(), weight)
        self.h_eleeta.Fill(abs(electron.eta()), weight)
        self.h_eleetapm.Fill(electron.eta(), weight)
        self.h_eledb.Fill(abs(electron.dB()), weight)
        self.h_eleoverlapmu.Fill(electron.hasOverlaps("muons"), weight)
        if isGoodElectron(electron,self.electronType) : nel += 1
      self.h_nel.Fill(nel, weight)
    
    def endJob(self):
      self.dir.cd()
      self.dir.Write()
      if not self.f is None:
        self.f.Close()

class JetmetControlPlots:
    """A class to create control plots for jets and MET"""

    def __init__(self, dir=None):
      # create output file if needed. If no file is given, it means it is delegated
      if dir is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("jetmet")
      else :
        self.f = None
        self.dir = dir
    
    def beginJob(self, jetlabel="cleanPatJets", metlabel="patMETsPF" , btagging="SSV"):
      self.btagging=btagging
      # declare histograms
      self.dir.cd()
      self.h_SSVHEdisc = ROOT.TH1F("SSVHEdisc","SSVHEdisc",200,-10,10)
      self.h_SSVHPdisc = ROOT.TH1F("SSVHPdisc","SSVHPdisc",200,-10,10)
      self.h_TCHEdisc = ROOT.TH1F("TCHEdisc","TCHEdisc",200,-10,10)
      self.h_TCHPdisc = ROOT.TH1F("TCHPdisc","TCHPdisc",200,-10,10)
      self.h_SSVHEdiscJet1 = ROOT.TH1F("SSVHEdiscJet1","SSVHEdiscJet1",200,-10,10)
      self.h_SSVHPdiscJet1 = ROOT.TH1F("SSVHPdiscJet1","SSVHPdiscJet1",200,-10,10)
      self.h_TCHEdiscJet1 = ROOT.TH1F("TCHEdiscJet1","TCHEdiscJet1",200,-10,10)
      self.h_TCHPdiscJet1 = ROOT.TH1F("TCHPdiscJet1","TCHPdiscJet1",200,-10,10)
      self.h_SSVHEdiscbJet1 = ROOT.TH1F("SSVHEdiscbJet1","SSVHEdiscbJet1",200,-10,10)
      self.h_SSVHPdiscbJet1 = ROOT.TH1F("SSVHPdiscbJet1","SSVHPdiscbJet1",200,-10,10)
      self.h_TCHEdiscbJet1 = ROOT.TH1F("TCHEdiscbJet1","TCHEdiscbJet1",200,-10,10)
      self.h_TCHPdiscbJet1 = ROOT.TH1F("TCHPdiscbJet1","TCHPdiscbJet1",200,-10,10)
      self.h_SSVHEdiscDisc1 = ROOT.TH1F("SSVHEdiscDisc1","SSVHEdiscDisc1",200,-10,10)
      self.h_SSVHPdiscDisc1 = ROOT.TH1F("SSVHPdiscDisc1","SSVHPdiscDisc1",200,-10,10)
      self.h_TCHEdiscDisc1 = ROOT.TH1F("TCHEdiscDisc1","TCHEdiscDisc1",200,-10,10)
      self.h_TCHPdiscDisc1 = ROOT.TH1F("TCHPdiscDisc1","TCHPdiscDisc1",200,-10,10)
      self.h_met = ROOT.TH1F("MET","MET",100,0,200)
      self.h_phimet = ROOT.TH1F("METphi","MET #phi",70,-3.5,3.5)
      self.h_jetpt = ROOT.TH1F("jetpt","Jet Pt",100,15,215)
      self.h_jeteta = ROOT.TH1F("jeteta","Jet eta",25,0, 2.5)
      self.h_jetetapm = ROOT.TH1F("jetetapm","Jet eta",50,-2.5, 2.5)
      self.h_jetphi = ROOT.TH1F("jetphi","Jet phi",80,-4,4)
      self.h_jetoverlapmu = ROOT.TH1F("jetoverlapmu","jets overlaps with muons",2,0,2)
      self.h_jetoverlapele = ROOT.TH1F("jetoverlapele","jets overlaps with electrons",2,0,2)
      self.h_jet1pt = ROOT.TH1F("jet1pt","leading jet Pt",500,15,515)
      self.h_jet1eta = ROOT.TH1F("jet1eta","leading jet Eta",25,0,2.5)
      self.h_jet1etapm = ROOT.TH1F("jet1etapm","leading jet Eta",50,-2.5,2.5)
      self.h_jet2pt = ROOT.TH1F("jet2pt","subleading jet Pt",500,15,515)
      self.h_jet2eta = ROOT.TH1F("jet2eta","subleading jet Eta",25,0,2.5)
      self.h_jet2etapm = ROOT.TH1F("jet2etapm","subleading jet Eta",50,-2.5,2.5)
      self.h_bjet1pt = ROOT.TH1F("bjet1pt","leading bjet Pt",500,15,515)
      self.h_bjet1eta = ROOT.TH1F("bjet1eta","leading bjet Eta",25,0,2.5)
      self.h_bjet1etapm = ROOT.TH1F("bjet1etapm","leading bjet Eta",50,-2.5,2.5)
      self.h_bjet2pt = ROOT.TH1F("bjet2pt","subleading bjet Pt",500,15,515)
      self.h_bjet2eta = ROOT.TH1F("bjet2eta","subleading bjet Eta",25,0,2.5)
      self.h_bjet2etapm = ROOT.TH1F("bjet2etapm","subleading bjet Eta",50,-2.5,2.5)
      self.h_dptj1b1 = ROOT.TH1F("dptj1b1","Pt difference between leading jet and leading bjet",1000,-500,500)
      self.h_nj = ROOT.TH1F("nj","jet count",15,0,15)
      self.h_nb = ROOT.TH1F("nb","b-jet count",5,0,5)
      self.h_nbP = ROOT.TH1F("nbP","pure b-jet count",5,0,5)
      self.h_njb = ROOT.TH2I("njb","number of bjets vs number of jets",15,0,15,5,0,5)
      self.h_nhf = ROOT.TH1F("nhf","neutral hadron energy fraction",101,0,1.01)
      self.h_nef = ROOT.TH1F("nef","neutral EmEnergy fraction",101,0,1.01)
      self.h_nconstituents = ROOT.TH1F("npf","total multiplicity",50,0,50)
      self.h_chf = ROOT.TH1F("chf","charged hadron energy fraction",101,0,1.01)
      self.h_nch = ROOT.TH1F("nch","charged multiplicity",50,0,50)
      self.h_cef = ROOT.TH1F("cef","charged EmEnergy fraction",101,0,1.01)
      self.h_jetid = ROOT.TH1F("jetid","Jet Id level (none, loose, medium, tight)",4,0,4)
      
      # prepare handles
      self.jetHandle = Handle ("vector<pat::Jet>")
      self.metHandle = Handle ("vector<pat::MET>")
      self.jetlabel = (jetlabel)
      self.metlabel = (metlabel)
    
    def processEvent(self,event, weight = 1.):
      # load event
      event.getByLabel (self.jetlabel,self.jetHandle)
      event.getByLabel (self.metlabel,self.metHandle)
      jets = self.jetHandle.product()
      met = self.metHandle.product()
      # process event and fill histograms
      # jets 
      nj  = 0
      nb  = 0
      nbP = 0
      maxbdiscSSVHE = -1
      maxbdiscSSVHP = -1
      maxbdiscTCHE  = -1
      maxbdiscTCHP  = -1
      for jet in jets:
        if isGoodJet(jet) and not jet.hasOverlaps("muons") and not jet.hasOverlaps("electrons"): 
          self.h_jetpt.Fill(jet.pt(), weight)
          self.h_jeteta.Fill(abs(jet.eta()), weight)
          self.h_jetetapm.Fill(jet.eta(), weight)
          self.h_jetphi.Fill(jet.phi(), weight)
          self.h_jetoverlapmu.Fill(jet.hasOverlaps("muons"), weight)
          self.h_jetoverlapele.Fill(jet.hasOverlaps("electrons"), weight)
          rawjet = jet # TODO: in principle, one should do: rawjet = jet.correctedJet("RAW") but one needs RAW factors in the tuple
          self.h_nhf.Fill(( rawjet.neutralHadronEnergy() + rawjet.HFHadronEnergy() ) / rawjet.energy(), weight)
          self.h_nef.Fill(rawjet.neutralEmEnergyFraction(), weight)
          self.h_nconstituents.Fill(rawjet.numberOfDaughters(), weight)
          self.h_chf.Fill(rawjet.chargedHadronEnergyFraction(), weight)
          self.h_nch.Fill(rawjet.chargedMultiplicity(), weight)
          self.h_cef.Fill(rawjet.chargedEmEnergyFraction(), weight)
          if jetId(jet,"tight"): self.h_jetid.Fill(3, weight)
          elif jetId(jet,"medium"): self.h_jetid.Fill(2, weight)
          elif jetId(jet,"loose"): self.h_jetid.Fill(1, weight)
          else: self.h_jetid.Fill(0, weight)
          # B-tagging
          self.h_SSVHEdisc.Fill(jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"), weight)
          self.h_SSVHPdisc.Fill(jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"), weight)
          self.h_TCHEdisc.Fill(jet.bDiscriminator("trackCountingHighEffBJetTags"), weight)
          self.h_TCHPdisc.Fill(jet.bDiscriminator("trackCountingHighPurBJetTags"), weight)
	  maxbdiscSSVHE = max(maxbdiscSSVHE,jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"), weight)
	  maxbdiscSSVHP = max(maxbdiscSSVHP,jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"), weight)
	  maxbdiscTCHE = max(maxbdiscSSVHE,jet.bDiscriminator("trackCountingHighEffBJetTags"), weight)
	  maxbdiscTCHP = max(maxbdiscSSVHP,jet.bDiscriminator("trackCountingHighPurBJetTags"), weight)
          #eventually complement with variables from the btagging (check paper)
          nj += 1
          if nj==1: 
	    j1pt=jet.pt()
            self.h_jet1pt.Fill(jet.pt(), weight)
            self.h_jet1eta.Fill(abs(jet.eta()), weight)
            self.h_jet1etapm.Fill(jet.eta(), weight)
            self.h_SSVHEdiscJet1.Fill(jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"), weight)
            self.h_SSVHPdiscJet1.Fill(jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"), weight)
            self.h_TCHEdiscJet1.Fill(jet.bDiscriminator("trackCountingHighEffBJetTags"), weight)
            self.h_TCHPdiscJet1.Fill(jet.bDiscriminator("trackCountingHighPurBJetTags"), weight)
          elif nj==2:
            self.h_jet2pt.Fill(jet.pt(), weight)
            self.h_jet2eta.Fill(abs(jet.eta()), weight)
            self.h_jet2etapm.Fill(jet.eta(), weight)
          if isBJet(jet,"HE",self.btagging): 
            nb += 1
            if nb==1:
              self.h_bjet1pt.Fill(jet.pt(), weight)
              self.h_bjet1eta.Fill(abs(jet.eta()), weight)
              self.h_bjet1etapm.Fill(jet.eta(), weight)
              self.h_SSVHEdiscbJet1.Fill(jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"), weight)
              self.h_SSVHPdiscbJet1.Fill(jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"), weight)
              self.h_TCHEdiscbJet1.Fill(jet.bDiscriminator("trackCountingHighEffBJetTags"), weight)
              self.h_TCHPdiscbJet1.Fill(jet.bDiscriminator("trackCountingHighPurBJetTags"), weight)
	      self.h_dptj1b1.Fill(jet.pt()-j1pt, weight)
            elif nb==2:
              self.h_bjet2pt.Fill(jet.pt(), weight)
              self.h_bjet2eta.Fill(abs(jet.eta()), weight)
              self.h_bjet2etapm.Fill(jet.eta(), weight)
          if isBJet(jet,"HP",self.btagging): nbP += 1
      self.h_SSVHEdiscDisc1.Fill(maxbdiscSSVHE, weight)
      self.h_SSVHPdiscDisc1.Fill(maxbdiscSSVHP, weight)
      self.h_TCHEdiscDisc1.Fill(maxbdiscTCHE, weight)
      self.h_TCHPdiscDisc1.Fill(maxbdiscTCHP, weight)
      self.h_nj.Fill(nj, weight)
      self.h_nb.Fill(nb, weight)
      self.h_nbP.Fill(nbP, weight)
      self.h_njb.Fill(nj,nb, weight)
      self.h_met.Fill(met[0].pt(), weight)
      self.h_phimet.Fill(met[0].phi(), weight)
    
    def endJob(self):
      self.dir.cd()
      self.dir.Write()
      if not self.f is None:
        self.f.Close()

def runTest():
  output = ROOT.TFile("controlPlots.root", "RECREATE")
  jetmetPlots = JetmetControlPlots(output.mkdir("jetmet"))
  electronsPlots = ElectronsControlPlots(output.mkdir("electrons"))
  muonsPlots = MuonsControlPlots(output.mkdir("muons"))

  path="/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/"
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)

  muonsPlots.beginJob()
  electronsPlots.beginJob()
  jetmetPlots.beginJob()
  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    jetmetPlots.processEvent(event)
    muonsPlots.processEvent(event)
    electronsPlots.processEvent(event)
    i += 1
  jetmetPlots.endJob()
  muonsPlots.endJob()
  electronsPlots.endJob()
  output.Close()

