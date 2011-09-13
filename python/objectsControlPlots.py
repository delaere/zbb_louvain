#! /usr/bin/env python

import ROOT
import sys
import os
from math import sin
from DataFormats.FWLite import Events, Handle
from baseControlPlots import BaseControlPlots
from eventSelection import *
#from myFuncTimer import print_timing

## TODO: Remove later... for data only
#ROOT.gSystem.Load("libFWCoreFWLite.so");
#ROOT.AutoLibraryLoader.enable()
#L2L3res = ROOT.FactorizedJetCorrector("L2Relative","../testfiles/JEC/GR_R_42_V20_AK5PF_L2Relative_L2L3Residual.txt")
#def jetpt(jet):
#  L2L3res.setJetEta(jet.pt())
#  L2L3res.setJetPt(jet.eta())
#  return jet.pt()*L2L3res.getCorrection()
############

class MuonsControlPlots(BaseControlPlots):
    """A class to create control plots for muons"""

    def __init__(self, dir=None):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="muons")
    
    def beginJob(self, muonlabel="matchedMuons", muonType="tight"):
      # declare histograms
      self.addHisto("muonType","Muon type", 4,0,4)
      self.addHisto("muonhits","Muon hits",50,0,50)
      self.addHisto("muonIso","Muon isolatio",20,0,0.2)
      self.addHisto("muonPt","Muon Pt",500,0,500)
      self.addHisto("muonEta","Muon Eta",25,0,2.5)
      self.addHisto("muonEtapm","Muon Eta",50,-2.5,2.5)
      self.addHisto("muonChi2","Muon normalized chi2",100,0,20)
      self.addHisto("muonPHits","Muon Pixel hits",10,0,10)
      self.addHisto("muonSHits","Muon Strip hits",30,0,30)
      self.addHisto("muonMatches","Muon matched segments",10,0,10)
      self.addHisto("muonMHits","Muon muon hits",100,0,100)
      self.addHisto("nmu","muon count",5,0,5)
      
      # prepare handles
      self.muonHandle = Handle ("vector<pat::Muon>")
      self.muonlabel  = muonlabel
      self.muonType   = muonType
    
    #@print_timing
    def process(self, event):
      """objectsControlPlots"""
      result = { }
      # load event
      event.getByLabel (self.muonlabel,self.muonHandle)
      muons = self.muonHandle.product()
      # process event and fill histograms
      result["muonType"]   = [ ]
      result["muonhits"]   = [ ]
      result["muonIso"]    = [ ]
      result["muonPt"]     = [ ]
      result["muonEta"]    = [ ]
      result["muonEtapm"]  = [ ]
      result["muonChi2"]   = [ ]
      result["muonPHits"]  = [ ]
      result["muonSHits"]  = [ ]
      result["muonMatches"]= [ ]
      result["muonMHits"]  = [ ]
      nmu = 0
      for muon in muons:
        # for muons:
        result["muonType"].append(muon.isGlobalMuon()+2*muon.isTrackerMuon())
        if muon.isTrackerMuon():
          result["muonhits"].append(muon.innerTrack().numberOfValidHits())
          result["muonPHits"].append(muon.innerTrack().hitPattern().numberOfValidPixelHits())
          result["muonSHits"].append(muon.innerTrack().hitPattern().numberOfValidStripHits())
        else:
          result["muonhits"].append(0)
          result["muonPHits"].append(0)
          result["muonSHits"].append(0)
        if muon.isGlobalMuon():
          result["muonMHits"].append(muon.globalTrack().hitPattern().numberOfValidMuonHits())
        else:
          result["muonMHits"].append(0)
        if muon.isTrackerMuon() and muon.isGlobalMuon():
          result["muonChi2"].append(muon.normChi2())
        else:
          result["muonChi2"].append(0)
        result["muonIso"].append((muon.trackIso()+muon.caloIso())/muon.pt())
        result["muonPt"].append(muon.pt())
        result["muonEta"].append(abs(muon.eta()))
        result["muonEtapm"].append(muon.eta())
        result["muonMatches"].append(muon.numberOfMatches())
        if isGoodMuon(muon,self.muonType) : nmu += 1
      result["nmu"] = nmu
   
      return result
    

class ElectronsControlPlots(BaseControlPlots):
    """A class to create control plots for electrons"""

    def __init__(self, dir=None):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="electrons")
    
    def beginJob(self, electronlabel="matchedElectrons", electronType="tight"):
      # declare histograms
      self.addHisto("eleid","electron id",10,0,10)
      self.addHisto("elemisshits","Electron missing hits",5,0,5)
      self.addHisto("elept","electron pt",500,0,500)
      self.addHisto("eleeta","electron eta",30,0,3)
      self.addHisto("eleetapm","electron eta",60,-3,3)
      self.addHisto("eledb","electron dB",100,0,0.05)
      self.addHisto("eleoverlapmu","electrons overlaps with muon",2,0,2)
      self.addHisto("eleHcalIso","Electron HCAL relative isolation dr03",100,0,0.2)
      self.addHisto("eleEcalIso","Electron ECAL relative isolation dr03",100,0,0.2)
      self.addHisto("eleTkIso","Electron Tk relative isolation dr03",100,0,0.2)
      self.addHisto("eleHoE","Electron H over E",100,0,0.1)
      self.addHisto("eledphi","Electron dphi at calo",100,0,0.1)
      self.addHisto("eledeta","Electron deta at calo",100,0,0.01)
      self.addHisto("eleinin","Electron sigma ieta ieta",100,0,0.1)
      self.addHisto("nel","electron count",5,0,5)
      # prepare handles
      self.electronHandle = Handle ("vector<pat::Electron>")
      self.electronlabel  = electronlabel
      self.electronType   = electronType
    
    #@print_timing
    def process(self, event):
      """ElectronsControlPlots"""
      result = { }
      # load event
      event.getByLabel (self.electronlabel,self.electronHandle)
      electrons = self.electronHandle.product()
      # lepton selection
      result["eleid"] = [ ]
      result["elemisshits"] = [ ]
      result["elept"] = [ ]
      result["eleeta"] = [ ]
      result["eleetapm"] = [ ]
      result["eledb"] = [ ]
      result["eleoverlapmu"] = [ ]
      result["eleHcalIso"] = [ ]
      result["eleEcalIso"] = [ ]
      result["eleTkIso"] = [ ]
      result["eleHoE"] = [ ]
      result["eledphi"] = [ ]
      result["eledeta"] = [ ]
      result["eleinin"] = [ ]
      nel = 0
      for electron in electrons:
        # for electrons
        scEt = (electron.ecalEnergy()*sin(electron.theta()))
        result["eleid"].append(electron.electronID("simpleEleId85relIso"))
        result["elemisshits"].append(electron.gsfTrack().numberOfLostHits())
        result["eleHcalIso"].append(electron.dr03HcalTowerSumEt()/scEt)
        result["eleEcalIso"].append(electron.dr03EcalRecHitSumEt()/scEt)
        result["eleTkIso"].append(electron.dr03TkSumPt()/scEt)
        result["eleHoE"].append(electron.hadronicOverEm())
        result["eledphi"].append(electron.deltaPhiEleClusterTrackAtCalo())
        result["eledeta"].append(electron.deltaEtaEleClusterTrackAtCalo())
        result["eleinin"].append(electron.scSigmaIEtaIEta())
        result["elept"].append(electron.pt())
        result["eleeta"].append(abs(electron.eta()))
        result["eleetapm"].append(electron.eta())
        result["eledb"].append(abs(electron.dB()))
        result["eleoverlapmu"].append(electron.hasOverlaps("muons"))
        if isGoodElectron(electron,self.electronType) : nel += 1
      result["nel"] = nel
      return result
    

class JetmetControlPlots(BaseControlPlots):
    """A class to create control plots for jets and MET"""

    def __init__(self, dir=None):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="jetmet")
    
    def beginJob(self, jetlabel="cleanPatJets", metlabel="patMETsPF", btagging="SSV"):
      self.btagging=btagging
      # declare histograms
      self.addHisto("SSVHEdisc","SSVHEdisc",200,-10,10)
      self.addHisto("SSVHPdisc","SSVHPdisc",200,-10,10)
      self.addHisto("TCHEdisc","TCHEdisc",200,-10,10)
      self.addHisto("TCHPdisc","TCHPdisc",200,-10,10)
      self.addHisto("SSVHEdiscJet1","SSVHEdiscJet1",200,-10,10)
      self.addHisto("SSVHPdiscJet1","SSVHPdiscJet1",200,-10,10)
      self.addHisto("TCHEdiscJet1","TCHEdiscJet1",200,-10,10)
      self.addHisto("TCHPdiscJet1","TCHPdiscJet1",200,-10,10)
      self.addHisto("SSVHEdiscbJet1","SSVHEdiscbJet1",200,-10,10)
      self.addHisto("SSVHPdiscbJet1","SSVHPdiscbJet1",200,-10,10)
      self.addHisto("TCHEdiscbJet1","TCHEdiscbJet1",200,-10,10)
      self.addHisto("TCHPdiscbJet1","TCHPdiscbJet1",200,-10,10)
      self.addHisto("SSVHEdiscDisc1","SSVHEdiscDisc1",200,-10,10)
      self.addHisto("SSVHPdiscDisc1","SSVHPdiscDisc1",200,-10,10)
      self.addHisto("TCHEdiscDisc1","TCHEdiscDisc1",200,-10,10)
      self.addHisto("TCHPdiscDisc1","TCHPdiscDisc1",200,-10,10)
      self.addHisto("MET","MET",100,0,200)
      self.addHisto("METphi","MET #phi",70,-3.5,3.5)
      self.addHisto("jetpt","Jet Pt",100,15,215)
      self.addHisto("jeteta","Jet eta",25,0, 2.5)
      self.addHisto("jetetapm","Jet eta",50,-2.5, 2.5)
      self.addHisto("jetphi","Jet phi",80,-4,4)
      self.addHisto("jetoverlapmu","jets overlaps with muons",2,0,2)
      self.addHisto("jetoverlapele","jets overlaps with electrons",2,0,2)
      self.addHisto("jet1pt","leading jet Pt",500,15,515)
      self.addHisto("jet1eta","leading jet Eta",25,0,2.5)
      self.addHisto("jet1etapm","leading jet Eta",50,-2.5,2.5)
      self.addHisto("jet2pt","subleading jet Pt",500,15,515)
      self.addHisto("jet2eta","subleading jet Eta",25,0,2.5)
      self.addHisto("jet2etapm","subleading jet Eta",50,-2.5,2.5)
      self.addHisto("bjet1pt","leading bjet Pt",500,15,515)
      self.addHisto("bjet1eta","leading bjet Eta",25,0,2.5)
      self.addHisto("bjet1etapm","leading bjet Eta",50,-2.5,2.5)
      self.addHisto("bjet2pt","subleading bjet Pt",500,15,515)
      self.addHisto("bjet2eta","subleading bjet Eta",25,0,2.5)
      self.addHisto("bjet2etapm","subleading bjet Eta",50,-2.5,2.5)
      self.addHisto("dptj1b1","Pt difference between leading jet and leading bjet",1000,-500,500)
      self.addHisto("nj","jet count",15,0,15)
      self.addHisto("nb","b-jet count",5,0,5)
      self.addHisto("nbP","pure b-jet count",5,0,5)
      self.addHisto("nhf","neutral hadron energy fraction",101,0,1.01)
      self.addHisto("nef","neutral EmEnergy fraction",101,0,1.01)
      self.addHisto("npf","total multiplicity",50,0,50)
      self.addHisto("chf","charged hadron energy fraction",101,0,1.01)
      self.addHisto("nch","charged multiplicity",50,0,50)
      self.addHisto("cef","charged EmEnergy fraction",101,0,1.01)
      self.addHisto("jetid","Jet Id level (none, loose, medium, tight)",4,0,4)
      # prepare handles
      self.jetHandle = Handle("vector<pat::Jet>")
      self.metHandle = Handle("vector<pat::MET>")
      self.jetlabel  = jetlabel
      self.metlabel  = metlabel
    
    #@print_timing
    def process(self, event):
      """JetmetControlPlots"""
      result = { }
      # load event
      event.getByLabel(self.jetlabel,self.jetHandle)
      event.getByLabel(self.metlabel,self.metHandle)
      jets = self.jetHandle.product()
      met  = self.metHandle.product()
      # process event and fill histograms
      result["SSVHEdisc"] = [ ]
      result["SSVHPdisc"] = [ ]
      result["TCHEdisc"] = [ ]
      result["TCHPdisc"] = [ ]
      result["jetpt"] = [ ]
      result["jeteta"] = [ ]
      result["jetetapm"] = [ ]
      result["jetphi"] = [ ]
      result["jetoverlapmu"] = [ ]
      result["jetoverlapele"] = [ ]
      result["nhf"] = [ ]
      result["nef"] = [ ]
      result["npf"] = [ ]
      result["chf"] = [ ]
      result["nch"] = [ ]
      result["cef"] = [ ]
      result["jetid"] = [ ]
      # jets 
      nj  = 0
      nb  = 0
      nbP = 0
      maxbdiscSSVHE = -1
      maxbdiscSSVHP = -1
      maxbdiscTCHE  = -1
      maxbdiscTCHP  = -1
      for jet in jets:
        #jetPt = jetpt(jet)
        jetPt = jet.pt()
        if isGoodJet(jet) and not jet.hasOverlaps("muons") and not jet.hasOverlaps("electrons"): 
          rawjet = jet.correctedJet("Uncorrected")
          result["jetpt"].append(jetPt)
          result["jeteta"].append(abs(jet.eta()))
          result["jetetapm"].append(jet.eta())
          result["jetphi"].append(jet.phi())
          result["jetoverlapmu"].append(jet.hasOverlaps("muons"))
          result["jetoverlapele"].append(jet.hasOverlaps("electrons"))
          result["nhf"].append(( rawjet.neutralHadronEnergy() + rawjet.HFHadronEnergy() ) / rawjet.energy())
          result["nef"].append(rawjet.neutralEmEnergyFraction())
          result["npf"].append(rawjet.numberOfDaughters())
          result["chf"].append(rawjet.chargedHadronEnergyFraction())
          result["nch"].append(rawjet.chargedMultiplicity())
          result["cef"].append(rawjet.chargedEmEnergyFraction())
          if jetId(jet,"tight"): result["jetid"].append(3)
          elif jetId(jet,"medium"): result["jetid"].append(2)
          elif jetId(jet,"loose"): result["jetid"].append(1)
          else: result["jetid"].append(0)
          # B-tagging
          result["SSVHEdisc"].append(jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"))
          result["SSVHPdisc"].append(jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"))
          result["TCHEdisc"].append(jet.bDiscriminator("trackCountingHighEffBJetTags"))
          result["TCHPdisc"].append(jet.bDiscriminator("trackCountingHighPurBJetTags"))
	  maxbdiscSSVHE = max(maxbdiscSSVHE,jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"))
	  maxbdiscSSVHP = max(maxbdiscSSVHP,jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"))
	  maxbdiscTCHE = max(maxbdiscSSVHE,jet.bDiscriminator("trackCountingHighEffBJetTags"))
	  maxbdiscTCHP = max(maxbdiscSSVHP,jet.bDiscriminator("trackCountingHighPurBJetTags"))
          nj += 1
          if nj==1: 
	    j1pt=jetPt#jet.pt()
            result["jet1pt"] = jetPt#jet.pt()
            result["jet1eta"] = abs(jet.eta())
            result["jet1etapm"] = jet.eta()
            result["SSVHEdiscJet1"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
            result["SSVHPdiscJet1"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
            result["TCHEdiscJet1"] = jet.bDiscriminator("trackCountingHighEffBJetTags")
            result["TCHPdiscJet1"] = jet.bDiscriminator("trackCountingHighPurBJetTags")
          elif nj==2:
            result["jet2pt"] = jetPt#jet.pt()
            result["jet2eta"] = abs(jet.eta())
            result["jet2etapm"] = jet.eta()
          if isBJet(jet,"HE",self.btagging): 
            nb += 1
            if nb==1:
              result["bjet1pt"] = jetPt#jet.pt()
              result["bjet1eta"] = abs(jet.eta())
              result["bjet1etapm"] = jet.eta()
              result["SSVHEdiscbJet1"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
              result["SSVHPdiscbJet1"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
              result["TCHEdiscbJet1"] = jet.bDiscriminator("trackCountingHighEffBJetTags")
              result["TCHPdiscbJet1"] = jet.bDiscriminator("trackCountingHighPurBJetTags")
	      result["dptj1b1"] = jetPt-j1pt#jet.pt()-j1pt
            elif nb==2:
              result["bjet2pt"] = jetPt#jet.pt()
              result["bjet2eta"] = abs(jet.eta())
              result["bjet2etapm"] = jet.eta()
          if isBJet(jet,"HP",self.btagging): nbP += 1
      result["SSVHEdiscDisc1"] = maxbdiscSSVHE
      result["SSVHPdiscDisc1"] = maxbdiscSSVHP
      result["TCHEdiscDisc1"] = maxbdiscTCHE
      result["TCHPdiscDisc1"] = maxbdiscTCHP
      result["nj"] = nj
      result["nb"] = nb
      result["nbP"] = nbP
      result["MET"] = met[0].pt()
      result["METphi"] = met[0].phi()
      return result
    

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

