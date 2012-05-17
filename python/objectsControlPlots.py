#! /usr/bin/env python

import ROOT
import sys
import os
from math import sin, sqrt
from DataFormats.FWLite import Events, Handle
from baseControlPlots import BaseControlPlots
from eventSelection import *
from JetCorrectionUncertainty import JetCorrectionUncertaintyProxy
from zbbCommons import zbblabel,zbbfile
#from myFuncTimer import print_timing

############
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

    def __init__(self, dir=None, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="muons", dataset=dataset, mode=mode)
    
    def beginJob(self, muonlabel=zbblabel.muonlabel, muonType="tight"):
      # declare histograms
      self.add("muonType","Muon type", 4,0,4)
      self.add("muonhits","Muon hits",50,0,50)
      self.add("muonIso","Muon isolatio",20,0,0.2)
      self.add("muonPt","Muon Pt",500,0,500)
      self.add("muonEta","Muon Eta",25,0,2.5)
      self.add("muonEtapm","Muon Eta",50,-2.5,2.5)
      self.add("muonChi2","Muon normalized chi2",100,0,20)
      self.add("muonPHits","Muon Pixel hits",10,0,10)
      self.add("muonSHits","Muon Strip hits",30,0,30)
      self.add("muonMatches","Muon matched segments",10,0,10)
      self.add("muonMHits","Muon muon hits",100,0,100)
      self.add("muondb","muon dB",100,0,0.05)
      self.add("nmu","muon count",5,0,5)
      
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
      result["muondb"]     = [ ]
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
        result["muondb"].append(abs(muon.dB()))
      result["nmu"] = nmu
   
      return result
    

class ElectronsControlPlots(BaseControlPlots):
    """A class to create control plots for electrons"""

    def __init__(self, dir=None, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="electrons", dataset=dataset, mode=mode)
    
    def beginJob(self, electronlabel=zbblabel.electronlabel, electronType="tight"):
      # declare histograms
      self.add("eleid","electron id",10,0,10)
      self.add("elemisshits","Electron missing hits",5,0,5)
      self.add("elept","electron pt",500,0,500)
      self.add("eleeta","electron eta",30,0,3)
      self.add("eleetapm","electron eta",60,-3,3)
      self.add("eledb","electron dB",100,0,0.05)
      self.add("eleoverlapmu","electrons overlaps with muon",2,0,2)
      self.add("eleHcalIso","Electron HCAL relative isolation dr03",100,0,0.2)
      self.add("eleEcalIso","Electron ECAL relative isolation dr03",100,0,0.2)
      self.add("eleTkIso","Electron Tk relative isolation dr03",100,0,0.2)
      self.add("eleHoE","Electron H over E",100,0,0.1)
      self.add("eledphi","Electron dphi at calo",100,0,0.1)
      self.add("eledeta","Electron deta at calo",100,0,0.01)
      self.add("eleinin","Electron sigma ieta ieta",100,0,0.1)
      self.add("nel","electron count",5,0,5)
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

    def __init__(self, dir=None, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated

      BaseControlPlots.__init__(self, dir=dir, purpose="jetmet", dataset=dataset, mode=mode)
      self._JECuncertainty = JetCorrectionUncertaintyProxy()
    
    def beginJob(self, jetlabel=zbblabel.jetlabel, metlabel=zbblabel.metlabel, zmulabel=zbblabel.zmumulabel, zelelabel=zbblabel.zelelabel, btagging="SSV"):
      self.btagging=btagging
      # declare histograms
      self.add("SSVHEdisc","SSVHEdisc",200,-10,10)
      self.add("nVertHE","Number of two-tracks vertices in jets",5,-0.5,4.5)
      self.add("SSVHPdisc","SSVHPdisc",200,-10,10)
      self.add("nVertHP","Number of three-tracks vertices in jets",5,-0.5,4.5)
      self.add("SVmass","SVmass",20,0,5)
      self.add("TCHEdisc","TCHEdisc",200,-10,10)
      self.add("TCHPdisc","TCHPdisc",200,-10,10)
      self.add("SSVHEdiscDisc1","SSVHEdiscDisc1",200,-10,10)
      self.add("SSVHPdiscDisc1","SSVHPdiscDisc1",200,-10,10)
      self.add("TCHEdiscDisc1","TCHEdiscDisc1",200,-10,10)
      self.add("TCHPdiscDisc1","TCHPdiscDisc1",200,-10,10)
      self.add("MET","MET",100,0,200)
      self.add("METphi","MET #phi",70,-3.5,3.5)
      self.add("METsignificance","MET significance",100,0,10)
      self.add("jetpt","Jet Pt",100,15,215)
      self.add("jetpt_totunc","Jet Pt total uncertainty",100,0,1)
      self.add("jetFlavor","Jet Flavor (MC)",21,-10.5,10.5)
      self.add("jeteta","Jet eta",25,0, 2.5)
      self.add("jetetapm","Jet eta",50,-2.5, 2.5)
      self.add("jetphi","Jet phi",80,-4,4)
      self.add("jetoverlapmu","jets overlaps with muons",2,0,2)
      self.add("jetoverlapele","jets overlaps with electrons",2,0,2)
      self.add("jetbeta","Jet beta function",20,-1,1)
      self.add("jetbetaStar","Jet beta* function",20,-1,1)
      self.add("jet1pt","leading jet Pt",500,15,515)
      self.add("jet1pt_totunc","leading jet Pt total uncertainty",100,0,100)
      self.add("jet1Flavor","leading jet Flavor (MC)",21,-10.5,10.5)
      self.add("jet1eta","leading jet Eta",25,0,2.5)
      self.add("jet1etapm","leading jet Eta",50,-2.5,2.5)
      self.add("jet1SSVHEdisc","leading jet SSVHE discriminant",200,-10,10)
      self.add("jet1nVertHE","Number of two-tracks vertices in leading jet",5,-0.5,4.5)
      self.add("jet1SSVHPdisc","leading jet SSVHP discriminant",200,-10,10)
      self.add("jet1nVertHP","Number of three-tracks vertices in leading jet",5,-0.5,4.5)
      self.add("jet1SVmass","leading jet SV mass",20,0,5)
      self.add("jet1TCHEdisc","leading jet TCHE discriminant",200,-10,10)
      self.add("jet1TCHPdisc","leading jet TCHP discriminant",200,-10,10)
      self.add("jet1beta","leading jet beta function",20,-1,1)
      self.add("jet1betaStar","leading jet beta* function",20,-1,1)
      self.add("jet2pt","subleading jet Pt",500,15,515)
      self.add("jet2pt_totunc","subleading jet Pt total uncertainty",100,0,100)
      self.add("jet2Flavor","subleading jet Flavor (MC)",21,-10.5,10.5)
      self.add("jet2eta","subleading jet Eta",25,0,2.5)
      self.add("jet2etapm","subleading jet Eta",50,-2.5,2.5)
      self.add("jet2SSVHEdisc","subleading jet SSVHE discriminant",200,-10,10)
      self.add("jet2nVertHE","Number of two-tracks vertices in subleading jet",5,-0.5,4.5)
      self.add("jet2SSVHPdisc","subleading jet SSVHP discriminant",200,-10,10)
      self.add("jet2nVertHP","Number of two-tracks vertices in subleading jet",5,-0.5,4.5)
      self.add("jet2SVmass","subleading jet SV mass",20,0,5)
      self.add("jet2TCHEdisc","subleading jet TCHE discriminant",200,-10,10)
      self.add("jet2TCHPdisc","subleading jet TCHP discriminant",200,-10,10)
      self.add("jet2beta","subleading jet beta function",20,-1,1)
      self.add("jet2betaStar","subleading jet beta* function",20,-1,1)
      self.add("bjet1pt","leading bjet Pt",500,15,515)
      self.add("bjet1pt_totunc","leading bjet Pt total uncertainty",100,0,100)
      self.add("bjet1Flavor","leading bjet Flavor (MC)",21,-10.5,10.5)
      self.add("bjet1eta","leading bjet Eta",25,0,2.5)
      self.add("bjet1etapm","leading bjet Eta",50,-2.5,2.5)
      self.add("bjet1SSVHEdisc","leading bjet SSVHE discriminant",200,-10,10)
      self.add("bjet1nVertHE","Number of two-tracks vertices in leading bjet",5,-0.5,4.5)
      self.add("bjet1SSVHPdisc","leading bjet SSVHP discriminant",200,-10,10)
      self.add("bjet1nVertHP","Number of three-tracks vertices in leading bjet",5,-0.5,4.5)
      self.add("bjet1SVmass","leading bjet SV mass",20,0,5)
      self.add("bjet1TCHEdisc","leading bjet TCHE discriminant",200,-10,10)
      self.add("bjet1TCHPdisc","leading bjet TCHP discriminant",200,-10,10)
      self.add("bjet1beta","leading bjet beta function",20,-1,1)
      self.add("bjet1betaStar","leading bjet beta* function",20,-1,1)
      self.add("bjet2pt","subleading bjet Pt",500,15,515)
      self.add("bjet2pt_totunc","subleading bjet Pt total uncertainty",100,0,100)
      self.add("bjet2Flavor","subleading bjet Flavor (MC)",21,-10.5,10.5)
      self.add("bjet2eta","subleading bjet Eta",25,0,2.5)
      self.add("bjet2etapm","subleading bjet Eta",50,-2.5,2.5)
      self.add("bjet2SSVHEdisc","subleading bjet SSVHE discriminant",200,-10,10)
      self.add("bjet2nVertHE","Number of two-tracks vertices in subleading bjet",5,-0.5,4.5)
      self.add("bjet2SSVHPdisc","subleading bjet SSVHP discriminant",200,-10,10)
      self.add("bjet2nVertHP","Number of three-tracks vertices in subleading bjet",5,-0.5,4.5)
      self.add("bjet2SVmass","subleading bjet SV mass",20,0,5)
      self.add("bjet2TCHEdisc","subleading bjet TCHE discriminant",200,-10,10)
      self.add("bjet2TCHPdisc","subleading bjet TCHP discriminant",200,-10,10)
      self.add("bjet2beta","subleading bjet beta function",20,-1,1)
      self.add("bjet2betaStar","subleading bjet beta* function",20,-1,1)
      self.add("dptj1b1","Pt difference between leading jet and leading bjet",1000,-500,500)
      self.add("nj","jet count",15,0,15)
      self.add("nb","b-jet count",5,0,5)
      self.add("nbP","pure b-jet count",5,0,5)
      self.add("nhf","neutral hadron energy fraction",101,0,1.01)
      self.add("nef","neutral EmEnergy fraction",101,0,1.01)
      self.add("npf","total multiplicity",50,0,50)
      self.add("chf","charged hadron energy fraction",101,0,1.01)
      self.add("nch","charged multiplicity",50,0,50)
      self.add("cef","charged EmEnergy fraction",101,0,1.01)
      self.add("jetid","Jet Id level (none, loose, medium, tight)",4,0,4)
      # prepare handles
      self.jetHandle = Handle("vector<pat::Jet>")
      self.metHandle = Handle("vector<pat::MET>")
      self.zmuHandle = Handle ("vector<reco::CompositeCandidate>")
      self.zeleHandle = Handle ("vector<reco::CompositeCandidate>")
      self.jetlabel  = jetlabel
      self.metlabel  = metlabel
      self.zmulabel = zmulabel
      self.zelelabel = zelelabel
    
    #@print_timing
    def process(self, event):
      """JetmetControlPlots"""
      result = { }
      # load event
      event.getByLabel(self.jetlabel,self.jetHandle)
      event.getByLabel(self.metlabel,self.metHandle)
      event.getByLabel(self.zmulabel,self.zmuHandle)
      event.getByLabel(self.zelelabel,self.zeleHandle)
      jets = self.jetHandle.product()
      met  = self.metHandle.product()
      zCandidatesMu = self.zmuHandle.product()
      zCandidatesEle = self.zeleHandle.product()
      bestZcandidate = findBestCandidate(None,zCandidatesMu,zCandidatesEle)
      # process event and fill histograms
      result["SSVHEdisc"] = [ ]
      result["SSVHPdisc"] = [ ]
      result["nVertHE"] = [ ]
      result["nVertHP"] = [ ]
      result["SVmass"] = [ ]
      result["SSVHEmass"] = [ ]
      result["SSVHPmass"] = [ ]
      result["TCHEdisc"] = [ ]
      result["TCHPdisc"] = [ ]
      result["jetpt"] = [ ]
      result["jetpt_totunc"] = [ ]
      result["jetFlavor"] = [ ]
      result["jeteta"] = [ ]
      result["jetetapm"] = [ ]
      result["jetphi"] = [ ]
      result["jetoverlapmu"] = [ ]
      result["jetoverlapele"] = [ ]
      result["jetbeta"] = [ ]
      result["jetbetaStar"] = [ ]
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
        jetPt = jet.pt()
        if isGoodJet(jet,bestZcandidate):
        #if isGoodJet(jet) and not jet.hasOverlaps("muons") and not jet.hasOverlaps("electrons"): 
          rawjet = jet.correctedJet("Uncorrected")
          result["jetpt"].append(jetPt)
	  result["jetpt_totunc"].append(self._JECuncertainty.unc_tot_jet(jet))
	  result["jetFlavor"].append(jet.partonFlavour())
          result["jeteta"].append(abs(jet.eta()))
          result["jetetapm"].append(jet.eta())
          result["jetphi"].append(jet.phi())
          result["jetoverlapmu"].append(jet.hasOverlaps("muons"))
          result["jetoverlapele"].append(jet.hasOverlaps("electrons"))
          result["jetbeta"].append(jet.userFloat("beta"))
          result["jetbetaStar"].append(jet.userFloat("betaStar"))
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
	  tISV = jet.tagInfoSecondaryVertex("secondaryVertex")
          nHEvert = 0
          nHPvert = 0
	  if tISV :
            nHEvert = tISV.nVertices()
            nHPvert = sum( tISV.nVertexTracks(v) >=3 for v in range(nHEvert))
	    if tISV.secondaryVertex(0) :
	      result["SVmass"].append(tISV.secondaryVertex(0).p4().mass())
          result["nVertHE"].append(nHEvert)
          result["nVertHP"].append(nHPvert)
          result["TCHEdisc"].append(jet.bDiscriminator("trackCountingHighEffBJetTags"))
          result["TCHPdisc"].append(jet.bDiscriminator("trackCountingHighPurBJetTags"))
	  maxbdiscSSVHE = max(maxbdiscSSVHE,jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"))
	  maxbdiscSSVHP = max(maxbdiscSSVHP,jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"))
	  maxbdiscTCHE = max(maxbdiscSSVHE,jet.bDiscriminator("trackCountingHighEffBJetTags"))
	  maxbdiscTCHP = max(maxbdiscSSVHP,jet.bDiscriminator("trackCountingHighPurBJetTags"))
          nj += 1
          if nj==1: 
	    j1pt=jetPt
            result["jet1pt"] = jetPt
	    result["jet1pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
	    result["jet1Flavor"] = jet.partonFlavour()
            result["jet1eta"] = abs(jet.eta())
            result["jet1etapm"] = jet.eta()
            result["jet1SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
            result["jet1SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
            result["jet1nVertHE"] = nHEvert
            result["jet1nVertHP"] = nHPvert
	    if tISV :
	      if tISV.secondaryVertex(0) :
	        result["jet1SVmass"] = tISV.secondaryVertex(0).p4().mass()
            result["jet1TCHEdisc"] = jet.bDiscriminator("trackCountingHighEffBJetTags")
            result["jet1TCHPdisc"] = jet.bDiscriminator("trackCountingHighPurBJetTags")
            result["jet1beta"] = jet.userFloat("beta")
            result["jet1betaStar"] = jet.userFloat("betaStar")
          elif nj==2:
            result["jet2pt"] = jetPt
	    result["jet2pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
	    result["jet2Flavor"] = jet.partonFlavour()
            result["jet2eta"] = abs(jet.eta())
            result["jet2etapm"] = jet.eta()
            result["jet2SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
            result["jet2SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
            result["jet2nVertHE"] = nHEvert
            result["jet2nVertHP"] = nHPvert
	    if tISV :
	      if tISV.secondaryVertex(0) :
	        result["jet2SVmass"] = tISV.secondaryVertex(0).p4().mass()
            result["jet2TCHEdisc"] = jet.bDiscriminator("trackCountingHighEffBJetTags")
            result["jet2TCHPdisc"] = jet.bDiscriminator("trackCountingHighPurBJetTags")
            result["jet2beta"] = jet.userFloat("beta")
            result["jet2betaStar"] = jet.userFloat("betaStar")
          if isBJet(jet,"HE",self.btagging): 
            nb += 1
            if nb==1:
              result["bjet1pt"] = jetPt
	      result["bjet1pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
	      result["bjet1Flavor"] = jet.partonFlavour()
              result["bjet1eta"] = abs(jet.eta())
              result["bjet1etapm"] = jet.eta()
              result["bjet1SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
              result["bjet1SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
              result["bjet1nVertHE"] = nHEvert
              result["bjet1nVertHP"] = nHPvert
	      if tISV :
	        if tISV.secondaryVertex(0) :
	          result["bjet1SVmass"] = tISV.secondaryVertex(0).p4().mass()
              result["bjet1TCHEdisc"] = jet.bDiscriminator("trackCountingHighEffBJetTags")
              result["bjet1TCHPdisc"] = jet.bDiscriminator("trackCountingHighPurBJetTags")
	      result["dptj1b1"] = jetPt-j1pt
              result["bjet1beta"] = jet.userFloat("beta")
              result["bjet1betaStar"] = jet.userFloat("betaStar")
            elif nb==2:
              result["bjet2pt"] = jetPt
	      result["bjet2pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
	      result["bjet2Flavor"] = jet.partonFlavour()
              result["bjet2eta"] = abs(jet.eta())
              result["bjet2etapm"] = jet.eta()
              result["bjet2SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
              result["bjet2SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
	      if tISV :
	        if tISV.secondaryVertex(0) :
	          result["bjet2SVmass"] = tISV.secondaryVertex(0).p4().mass()
              result["bjet2TCHEdisc"] = jet.bDiscriminator("trackCountingHighEffBJetTags")
              result["bjet2TCHPdisc"] = jet.bDiscriminator("trackCountingHighPurBJetTags")
              result["bjet2nVertHE"] = nHEvert
              result["bjet2nVertHP"] = nHPvert
              result["bjet2beta"] = jet.userFloat("beta")
              result["bjet2betaStar"] = jet.userFloat("betaStar")
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
      result["METsignificance"] = 0.
      if met[0].getSignificanceMatrix()(0,0)<1e10 and met[0].getSignificanceMatrix()(1,1)<1e10: 
        result["METsignificance"] = met[0].significance()
      return result

def runTest():
  output = ROOT.TFile(zbbfile.controlPlots, "RECREATE")
  jetmetPlots = JetmetControlPlots(output.mkdir("jetmet"))
  electronsPlots = ElectronsControlPlots(output.mkdir("electrons"))
  muonsPlots = MuonsControlPlots(output.mkdir("muons"))

  path="../testfiles/"
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

