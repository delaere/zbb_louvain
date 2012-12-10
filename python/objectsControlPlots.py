#! /usr/bin/env python

import ROOT
import sys
import os
from math import sin, sqrt
from AnalysisEvent import AnalysisEvent
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
    
    def beginJob(self, muonList="muons", muonType="tight"):
      # declare histograms
      self.add("muonType","Muon type", 4,0,4)
      self.add("muonTckLayers","Muon Tck Layers",50,0,50)
      self.add("muonIso","Muon isolation",20,0,0.2)
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
      self.muonType = muonType
      self.muonList = muonList
    
    #@print_timing
    def process(self, event):
      """objectsControlPlots"""
      result = { }
      # process event and fill histograms
      result["muonType"]        = [ ]
      result["muonTckLayers"]   = [ ]
      result["muonIso"]         = [ ]
      result["muonPt"]          = [ ]
      result["muonEta"]         = [ ]
      result["muonEtapm"]       = [ ]
      result["muonChi2"]        = [ ]
      result["muonPHits"]       = [ ]
      result["muonSHits"]       = [ ]
      result["muonMatches"]     = [ ]
      result["muonMHits"]       = [ ]
      result["muondb"]          = [ ]
      nmu = 0
      for muon in getattr(event, self.muonList):
        # for muons:
        chargedHadronIso = muon.pfIsolationR04().sumChargedHadronPt
        chargedHadronIsoPU = muon.pfIsolationR04().sumPUPt  
        neutralHadronIso  = muon.pfIsolationR04().sumNeutralHadronEt
        photonIso  = muon.pfIsolationR04().sumPhotonEt
        
        RelativeIsolationDBetaCorr=(chargedHadronIso + max(photonIso+neutralHadronIso-0.5*chargedHadronIsoPU ,0.))/(max(0.5,muon.pt()))
        
        result["muonType"].append(muon.isGlobalMuon()+2*muon.isTrackerMuon())
        if muon.isTrackerMuon():
          ###result["muonhits"].append(muon.innerTrack().numberOfValidHits())
          result["muonTckLayers"].append(muon.innerTrack().hitPattern().trackerLayersWithMeasurement())
          result["muonPHits"].append(muon.innerTrack().hitPattern().numberOfValidPixelHits())
          result["muonSHits"].append(muon.innerTrack().hitPattern().numberOfValidStripHits())
        else:
          ##result["muonhits"].append(0)
          result["muonTckLayers"].append(0)
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
        result["muonIso"].append(RelativeIsolationDBetaCorr)
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
    
    def beginJob(self, electronList="electrons", electronType="tight"):
      # declare histograms
      self.add("eleid","electron id",10,0,10)
      self.add("elemisshits","Electron missing hits",5,0,5)
      self.add("elept","electron pt",500,0,500)
      self.add("eleeta","electron eta",30,0,3)
      self.add("eleetapm","electron eta",60,-3,3)
      self.add("eledb","electron dB",100,0,0.05)
      self.add("eleoverlapmu","electrons overlaps with muon",2,0,2)
      self.add("elechargedIso","Electron charged Hadron isolation ",100,0,0.2)
      self.add("elephotonIso","Electron photon isolation",100,0,0.2)
      self.add("eleneutralIso","Electron neutral Hadron isolation ",100,0,0.2)
      self.add("elepfIsoPUc","Electron pfIsoPUCorrected",100,0,0.2)
      self.add("elepfIsoPUcMC","Electron pfIsoPUCorrectedMC",100,0,0.2)
      #self.add("eleHoE","Electron H over E",100,0,0.1)
      self.add("eledphi","Electron dphi at calo",100,0,0.1)
      self.add("eledeta","Electron deta at calo",100,0,0.01)
      self.add("eleinin","Electron sigma ieta ieta",100,0,0.1)
      self.add("nel","electron count",5,0,5)
      self.electronType   = electronType
      self.electronList   = electronList

    #@print_timing
    def process(self, event):
      """ElectronsControlPlots"""
      result = { }
      # lepton selection
      result["eleid"] = [ ]
      result["elemisshits"] = [ ]
      result["elept"] = [ ]
      result["eleeta"] = [ ]
      result["eleetapm"] = [ ]
      result["eledb"] = [ ]
      result["eleoverlapmu"] = [ ]
      #result["elechargedIso"] = [ ]
      #result["elephotonIso"] = [ ]
      #result["eleneutralIso"] = [ ]
      result["elepfIsoPUc"] = [ ]
      result["elepfIsoPUcMC"] = [ ]
      #result["eleHoE"] = [ ]
      result["eledphi"] = [ ]
      result["eledeta"] = [ ]
      result["eleinin"] = [ ]
      nel = 0
      for electron in getattr(event, self.electronList):
        # for electrons
        scEt = (electron.ecalEnergy()*sin(electron.theta()))
        result["eleid"].append(electron.userInt("MediumWP"))
        result["elemisshits"].append(electron.gsfTrack().numberOfLostHits())
        #result["elechargedIso"].append()
        #result["elephotonIso"].append()
        #result["eleneutralIso"].append()
        result["elepfIsoPUc"].append(electron.userFloat("PFIsoPUCorrected"))
        result["elepfIsoPUcMC"].append(electron.userFloat("PFIsoPUCorrectedMC"))
        #result["eleHcalIso"].append(electron.dr03HcalTowerSumEt()/scEt)
        #result["eleEcalIso"].append(electron.dr03EcalRecHitSumEt()/scEt)
        #result["eleTkIso"].append(electron.dr03TkSumPt()/scEt)
        #result["eleHoE"].append(electron.hadronicOverEm())
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

    def __init__(self, dir=None, dataset=None, muChannel=True, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated

      BaseControlPlots.__init__(self, dir=dir, purpose="jetmet", dataset=dataset, mode=mode)
      self._JECuncertainty = JetCorrectionUncertaintyProxy()
      self.muChannel = muChannel
    
    def beginJob(self, btagging="CSV"):
      self.btagging=btagging
      # declare histograms
      self.add("SSVHEdisc","SSVHEdisc",200,0,10)
      self.add("nVertHE","Number of two-tracks vertices in jets",5,-0.5,4.5)
      self.add("SSVHPdisc","SSVHPdisc",200,0,10)
      self.add("nVertHP","Number of three-tracks vertices in jets",5,-0.5,4.5)
      self.add("SVmass","SVmass",20,0,5)
      self.add("SVpT","SVpT",100,0,200)
      self.add("CSVdisc","CSVdisc",100,0,1)
      self.add("JPdisc","JPdisc",100,0,2.5)
      self.add("SSVHEdiscDisc1","SSVHEdiscDisc1",200,0,10)
      self.add("SSVHPdiscDisc1","SSVHPdiscDisc1",200,0,10)
      self.add("CSVdiscDisc1","CSVdiscDisc1",100,0,1)
      self.add("JPdiscDisc1","JPdiscDisc1",100,0,2.5)
      self.add("MET","MET",100,0,200)
      self.add("METphi","MET #phi",70,-3.5,3.5)
      self.add("METsignificance","MET significance",100,0,20)
      self.add("METphiNNregression","MET #ph for NN regression",70,-3.5,3.5)
      self.add("METNNregression","MET for NN regression",250,0,500)
      self.add("jetpt","Jet Pt",100,15,215)
      self.add("jetpt_totunc","Jet Pt total uncertainty",100,0,1)
      self.add("jetFlavor","Jet Flavor (MC)",29,-6.5,22.5)
      self.add("jeteta","Jet eta",25,0, 2.5)
      self.add("jetetapm","Jet eta",50,-2.5, 2.5)
      self.add("jetphi","Jet phi",80,-4,4)
      self.add("jetoverlapmu","jets overlaps with muons",2,0,2)
      self.add("jetoverlapele","jets overlaps with electrons",2,0,2)
      self.add("jetbeta","Jet beta function",20,-1,1)
      self.add("jetbetaStar","Jet beta* function",20,-1,1)
      self.add("jet1pt","leading jet Pt",500,15,515)
      self.add("jet1pt_totunc","leading jet Pt total uncertainty",100,0,100)
      self.add("jet1Flavor","leading jet Flavor (MC)",29,-6.5,22.5)
      self.add("jet1eta","leading jet Eta",25,0,2.5)
      self.add("jet1etapm","leading jet Eta",50,-2.5,2.5)
      self.add("jet1phi","leading jet Phi",25,-4,4)
      self.add("jet1energy","leading jet energy",125,0,3000)
      self.add("jet1mass","leading jet mass",125,0,500)
      self.add("jet1Chf","charged hadron energy fraction leading jet",100,0,1.5)
      self.add("jet1Nhf","neutral hadron energy fraction leading jet",100,0,1.5)
      self.add("jet1Phf","photon energy fraction leading jet",100,0,1.5)
      self.add("jet1Elf","electron energy fraction leading jet",100,0,1.5)
      self.add("jet1Muf","muon energy fraction leading jet",100,0,1.5)
      self.add("jet1Vtx3dL","secondary vertex 3d flight distance leading jet",100,0,16)
      self.add("jet1Vtx3deL","secondary vertex 3d flight distance error leading jet",200,0,3)
      self.add("jet1VtxPt","secondary vertex PT for leading jet",100,0,270)
      self.add("jet1PtD","constituentPt leading jet",100,0,1.5)
      self.add("jet1SSVHEdisc","leading jet SSVHE discriminant",200,0,10)
      self.add("jet1nVertHE","Number of two-tracks vertices in leading jet",5,-0.5,4.5)
      self.add("jet1SSVHPdisc","leading jet SSVHP discriminant",200,0,10)
      self.add("jet1nVertHP","Number of three-tracks vertices in leading jet",5,-0.5,4.5)
      self.add("jet1SVmass","leading jet SV mass",20,0,5)
      self.add("jet1SVpT","leading jet SV pT",100,0,200)
      self.add("jet1CSVdisc","leading jet CSV discriminant",100,0,1)
      self.add("jet1JPdisc","leading jet JP discriminant",100,0,2.5)
      self.add("jet1beta","leading jet beta function",20,-1,1)
      self.add("jet1betaStar","leading jet beta* function",20,-1,1)
      self.add("jet2pt","subleading jet Pt",500,15,515)
      self.add("jet2pt_totunc","subleading jet Pt total uncertainty",100,0,100)
      self.add("jet2Flavor","subleading jet Flavor (MC)",29,-6.5,22.5)
      self.add("jet2eta","subleading jet Eta",25,0,2.5)
      self.add("jet2etapm","subleading jet Eta",50,-2.5,2.5)
      self.add("jet2phi","subleading bjet Phi",25,-4,4)
      self.add("jet2energy","subleading bjet energy",125,0,3000)
      self.add("jet2mass","subleading bjet mass",125,0,500)
      self.add("jet2Chf","charged hadron energy fraction leading jet",100,0,1.5)
      self.add("jet2Nhf","neutral hadron energy fraction leading jet",100,0,1.5)
      self.add("jet2Phf","photon energy fraction leading jet",100,0,1.5)
      self.add("jet2Elf","electron energy fraction leading jet",100,0,1.5)
      self.add("jet2Muf","muon energy fraction leading jet",100,0,1.5)
      self.add("jet2Vtx3dL","secondary vertex 3d flight distance leading jet",100,0,16)
      self.add("jet2Vtx3deL","secondary vertex 3d flight distance error leading jet",200,0,3)
      self.add("jet2VtxPt","secondary vertex PT for leading jet",100,0,270)
      self.add("jet2PtD","constituentPt leading jet",100,0,1.5)
      self.add("jet2SSVHEdisc","subleading jet SSVHE discriminant",200,0,10)
      self.add("jet2nVertHE","Number of two-tracks vertices in subleading jet",5,-0.5,4.5)
      self.add("jet2SSVHPdisc","subleading jet SSVHP discriminant",200,0,10)
      self.add("jet2nVertHP","Number of two-tracks vertices in subleading jet",5,-0.5,4.5)
      self.add("jet2SVmass","subleading jet SV mass",20,0,5)
      self.add("jet2SVpT","subleading jet SV pT",100,0,200)
      self.add("jet2CSVdisc","subleading jet CSV discriminant",100,0,1)
      self.add("jet2JPdisc","subleading jet JP discriminant",100,0,2.5)
      self.add("jet2beta","subleading jet beta function",20,-1,1)
      self.add("jet2betaStar","subleading jet beta* function",20,-1,1)
      self.add("bjet1pt","leading bjet Pt",500,15,515)
      self.add("bjet1pt_totunc","leading bjet Pt total uncertainty",100,0,100)
      self.add("bjet1Flavor","leading bjet Flavor (MC)",29,-6.5,22.5)
      self.add("bjet1eta","leading bjet Eta",25,0,2.5)
      self.add("bjet1etapm","leading bjet Eta",50,-2.5,2.5)
      self.add("bjet1phi","leading bjet Phi",25,-4,4)
      self.add("bjet1energy","leading bjet energy",125,0,3000)
      self.add("bjet1mass","leading bjet mass",125,0,500)
      self.add("bjet1Chf","charged hadron energy fraction leading bjet",100,0,1.5)
      self.add("bjet1Nhf","neutral hadron energy fraction leading bjet",100,0,1.5)
      self.add("bjet1Phf","photon energy fraction leading bjet",100,0,1.5)
      self.add("bjet1Elf","electron energy fraction leading bjet",100,0,1.5)
      self.add("bjet1Muf","muon energy fraction leading bjet",100,0,1.5)
      self.add("bjet1Vtx3dL","secondary vertex 3d flight distance leading bjet",100,0,16)
      self.add("bjet1Vtx3deL","secondary vertex 3d flight distance error leading bjet",200,0,3)
      self.add("bjet1VtxPt","secondary vertex PT for leading bjet",100,0,270)
      self.add("bjet1PtD","constituentPt leading jet",100,0,1.5)
      self.add("bjet1SSVHEdisc","leading bjet SSVHE discriminant",200,1.74,10)
      self.add("bjet1nVertHE","Number of two-tracks vertices in leading bjet",5,-0.5,4.5)
      self.add("bjet1SSVHPdisc","leading bjet SSVHP discriminant",200,0,10)
      self.add("bjet1nVertHP","Number of three-tracks vertices in leading bjet",5,-0.5,4.5)
      self.add("bjet1SVmass","leading bjet SV mass",20,0,5)
      self.add("bjet1SVpT","leading bjet SV pT",100,0,200)
      self.add("bjet1CSVdisc","leading bjet CSV discriminant",100,0,1)
      self.add("bjet1JPdisc","leading bjet JP discriminant",100,0,2.5)
      self.add("bjet1beta","leading bjet beta function",20,-1,1)
      self.add("bjet1betaStar","leading bjet beta* function",20,-1,1)
      self.add("bjet2pt","subleading bjet Pt",500,15,515)
      self.add("bjet2pt_totunc","subleading bjet Pt total uncertainty",100,0,100)
      self.add("bjet2Flavor","subleading bjet Flavor (MC)",29,-6.5,22.5)
      self.add("bjet2eta","subleading bjet Eta",25,0,2.5)
      self.add("bjet2etapm","subleading bjet Eta",50,-2.5,2.5)
      self.add("bjet2phi","subleading bjet Phi",25,-4,4)
      self.add("bjet2energy","subleading bjet energy",125,0,3000)
      self.add("bjet2mass","subleading bjet mass",125,0,500)
      self.add("bjet2Chf","charged hadron energy fraction sublieading bjet",100,0,1.5)
      self.add("bjet2Nhf","neutral hadron energy fraction sublieading bjet",100,0,1.5)
      self.add("bjet2Phf","photon energy fraction sublieading bjet",100,0,1.5)
      self.add("bjet2Elf","electron energy fraction sublieading bjet",100,0,1.5)
      self.add("bjet2Muf","muon energy fraction sublieading bjet",100,0,1.5)
      self.add("bjet2Vtx3dL","secondary vertex 3d flight distance sublieading bjet",100,0,16)
      self.add("bjet2Vtx3deL","secondary vertex 3d flight distance error sublieading bjet",200,0,3)
      self.add("bjet2VtxPt","secondary vertex PT for sublieading bjet",100,0,270)
      self.add("bjet2PtD","constituentPt sublieading bjet",100,0,1.5)
      self.add("bjet2SSVHEdisc","subleading bjet SSVHE discriminant",200,1.74,10)
      self.add("bjet2nVertHE","Number of two-tracks vertices in subleading bjet",5,-0.5,4.5)
      self.add("bjet2SSVHPdisc","subleading bjet SSVHP discriminant",200,0,10)
      self.add("bjet2nVertHP","Number of three-tracks vertices in subleading bjet",5,-0.5,4.5)
      self.add("bjet2SVmass","subleading bjet SV mass",20,0,5)
      self.add("bjet2SVpT","subleading bjet SV pT",100,0,200)
      self.add("bjet2CSVdisc","subleading bjet CSV discriminant",100,0,1)
      self.add("bjet2JPdisc","subleading bjet JP discriminant",100,0,2.5)
      self.add("bjet2beta","subleading bjet beta function",20,-1,1)
      self.add("bjet2betaStar","subleading bjet beta* function",20,-1,1)
      self.add("dptj1b1","Pt difference between leading jet and leading bjet",1000,-500,500)
      self.add("nj","jet count",15,-0.5,14.5)
      self.add("nb","b-jet count",5,-0.5,4.5)
      self.add("nbP","pure b-jet count",5,0,5)
      self.add("nhf","neutral hadron energy fraction",101,0,1.01)
      self.add("nef","neutral EmEnergy fraction",101,0,1.01)
      self.add("npf","total multiplicity",50,0,50)
      self.add("chf","charged hadron energy fraction",101,0,1.01)
      self.add("nch","charged multiplicity",50,0,50)
      self.add("cef","charged EmEnergy fraction",101,0,1.01)
      self.add("jetid","Jet Id level (none, loose, medium, tight)",4,0,4)
      self.add("rho", "Rho Variable",100,0,100)
    
    #@print_timing
    def process(self, event):
      """JetmetControlPlots"""
      result = { }
      # process event and fill histograms
      result["SSVHEdisc"] = [ ]
      result["SSVHPdisc"] = [ ]
      result["nVertHE"] = [ ]
      result["nVertHP"] = [ ]
      result["SVmass"] = [ ]
      result["SVpT"] = [ ]
      result["SSVHEmass"] = [ ]
      result["SSVHPmass"] = [ ]
      result["CSVdisc"] = [ ]
      result["JPdisc"] = [ ]
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
      indexDijet = 0
      maxbdiscSSVHE = -1
      maxbdiscSSVHP = -1
      maxbdiscCSV  = -1
      maxbdiscJP  = -1
      dijet =  event.dijet_muChannel if self.muChannel else event.dijet_eleChannel
      for index,jet in enumerate(event.jets):
        #jetPt = jet.pt()
        jetPt = self._JECuncertainty.jetPt(jet)
        goodJets = event.goodJets_mu if self.muChannel else event.goodJets_ele
        if goodJets[index]:
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
	      result["SVpT"].append(tISV.secondaryVertex(0).p4().pt())
          result["nVertHE"].append(nHEvert)
          result["nVertHP"].append(nHPvert)
          result["CSVdisc"].append(jet.bDiscriminator("combinedSecondaryVertexBJetTags"))
          result["JPdisc"].append(jet.bDiscriminator("jetProbabilityBJetTags"))
	  maxbdiscSSVHE = max(maxbdiscSSVHE,jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"))
	  maxbdiscSSVHP = max(maxbdiscSSVHP,jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"))
	  maxbdiscCSV = max(maxbdiscSSVHE,jet.bDiscriminator("combinedSecondaryVertexBJetTags"))
	  maxbdiscJP = max(maxbdiscSSVHP,jet.bDiscriminator("jetProbabilityBJetTags"))
          nj += 1
          if nj==1: 
	    j1pt=jetPt
            result["jet1pt"] = jetPt
	    result["jet1pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
	    result["jet1Flavor"] = jet.partonFlavour()
            result["jet1eta"] = abs(jet.eta())
            result["jet1etapm"] = jet.eta()
            result["jet1phi"] = jet.phi()
            result["jet1energy"] = jet.energy()
            result["jet1mass"] = jet.mass()	    
            result["jet1Chf"] = jet.chargedHadronEnergyFraction()
            result["jet1Phf"] = jet.neutralHadronEnergyFraction()
            result["jet1Nhf"] = jet.photonEnergyFraction()
            result["jet1Elf"] = jet.electronEnergyFraction()
            result["jet1Muf"] = jet.muonEnergyFraction()
            result["jet1Vtx3dL"] = jetVtx3dL(jet)
            result["jet1Vtx3deL"] = jetVtx3deL(jet)
            result["jet1VtxPt"] = jetVtxPt(jet)
            result["jet1PtD"] = jetPtD(jet)
            result["jet1SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
            result["jet1SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
            result["jet1nVertHE"] = nHEvert
            result["jet1nVertHP"] = nHPvert
	    if tISV :
	      if tISV.secondaryVertex(0) :
	        result["jet1SVmass"] = tISV.secondaryVertex(0).p4().mass()
	        result["jet1SVpT"] = tISV.secondaryVertex(0).p4().pt()
            result["jet1CSVdisc"] = jet.bDiscriminator("combinedSecondaryVertexBJetTags")
            result["jet1JPdisc"] = jet.bDiscriminator("jetProbabilityBJetTags")
            result["jet1beta"] = jet.userFloat("beta")
            result["jet1betaStar"] = jet.userFloat("betaStar")
          elif nj==2:
            result["jet2pt"] = jetPt
	    result["jet2pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
	    result["jet2Flavor"] = jet.partonFlavour()
            result["jet2eta"] = abs(jet.eta())
            result["jet2etapm"] = jet.eta()
            result["jet2phi"] = jet.phi()
            result["jet2energy"] = jet.energy()
            result["jet2mass"] = jet.mass()
            result["jet2Chf"] = jet.chargedHadronEnergyFraction()
            result["jet2Phf"] = jet.neutralHadronEnergyFraction()
            result["jet2Nhf"] = jet.photonEnergyFraction()
            result["jet2Elf"] = jet.electronEnergyFraction()
            result["jet2Muf"] = jet.muonEnergyFraction()
            result["jet2Vtx3dL"] = jetVtx3dL(jet)
            result["jet2Vtx3deL"] = jetVtx3deL(jet)
            result["jet2VtxPt"] = jetVtxPt(jet)
            result["jet2PtD"] = jetPtD(jet)
            result["jet2SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
            result["jet2SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
            result["jet2nVertHE"] = nHEvert
            result["jet2nVertHP"] = nHPvert
	    if tISV :
	      if tISV.secondaryVertex(0) :
	        result["jet2SVmass"] = tISV.secondaryVertex(0).p4().mass()
	        result["jet2SVpT"] = tISV.secondaryVertex(0).p4().pt()
            result["jet2CSVdisc"] = jet.bDiscriminator("combinedSecondaryVertexBJetTags")
            result["jet2JPdisc"] = jet.bDiscriminator("jetProbabilityBJetTags")
            result["jet2beta"] = jet.userFloat("beta")
            result["jet2betaStar"] = jet.userFloat("betaStar")            
          if isBJet(jet,"HE",self.btagging): 
            nb += 1
            if indexDijet==0 and jet in dijet:
              indexDijet+=1
              result["bjet1pt"] = jetPt
	      result["bjet1pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
	      result["bjet1Flavor"] = jet.partonFlavour()
              result["bjet1eta"] = abs(jet.eta())
              result["bjet1etapm"] = jet.eta()
              result["bjet1phi"] = jet.phi()
              result["bjet1energy"] = jet.energy()
              result["bjet1mass"] = jet.mass()
              result["bjet1Chf"] = jet.chargedHadronEnergyFraction()
              result["bjet1Phf"] = jet.neutralHadronEnergyFraction()
              result["bjet1Nhf"] = jet.photonEnergyFraction()
              result["bjet1Elf"] = jet.electronEnergyFraction()
              result["bjet1Muf"] = jet.muonEnergyFraction()
              result["bjet1Vtx3dL"] = jetVtx3dL(jet)
              result["bjet1Vtx3deL"] = jetVtx3deL(jet)
              result["bjet1VtxPt"] = jetVtxPt(jet)
              result["bjet1PtD"] = jetPtD(jet)
              result["bjet1SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
              result["bjet1SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
              result["bjet1nVertHE"] = nHEvert
              result["bjet1nVertHP"] = nHPvert
	      if tISV :
	        if tISV.secondaryVertex(0) :
	          result["bjet1SVmass"] = tISV.secondaryVertex(0).p4().mass()
                  result["bjet1SVpT"] = tISV.secondaryVertex(0).p4().pt()
              result["bjet1CSVdisc"] = jet.bDiscriminator("combinedSecondaryVertexBJetTags")
              result["bjet1JPdisc"] = jet.bDiscriminator("jetProbabilityBJetTags")
	      result["dptj1b1"] = jetPt-j1pt
              result["bjet1beta"] = jet.userFloat("beta")
              result["bjet1betaStar"] = jet.userFloat("betaStar")
            elif indexDijet==1 and jet in dijet:
              indexDijet+=1
              result["bjet2pt"] = jetPt
	      result["bjet2pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
	      result["bjet2Flavor"] = jet.partonFlavour()
              result["bjet2eta"] = abs(jet.eta())
              result["bjet2etapm"] = jet.eta()
              result["bjet2phi"] = jet.phi()
              result["bjet2energy"] = jet.energy()
              result["bjet2mass"] = jet.mass()
              result["bjet2Chf"] = jet.chargedHadronEnergyFraction()
              result["bjet2Phf"] = jet.neutralHadronEnergyFraction()
              result["bjet2Nhf"] = jet.photonEnergyFraction()
              result["bjet2Elf"] = jet.electronEnergyFraction()
              result["bjet2Muf"] = jet.muonEnergyFraction()
              result["bjet2Vtx3dL"] = jetVtx3dL(jet)
              result["bjet2Vtx3deL"] = jetVtx3deL(jet)
              result["bjet2VtxPt"] = jetVtxPt(jet)
              result["bjet2PtD"] = jetPtD(jet)
              result["bjet2SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
              result["bjet2SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
	      if tISV :
	        if tISV.secondaryVertex(0) :
	          result["bjet2SVmass"] = tISV.secondaryVertex(0).p4().mass()
                  result["bjet2SVpT"] = tISV.secondaryVertex(0).p4().pt()
              result["bjet2CSVdisc"] = jet.bDiscriminator("combinedSecondaryVertexBJetTags")
              result["bjet2JPdisc"] = jet.bDiscriminator("jetProbabilityBJetTags")
              result["bjet2nVertHE"] = nHEvert
              result["bjet2nVertHP"] = nHPvert
              result["bjet2beta"] = jet.userFloat("beta")
              result["bjet2betaStar"] = jet.userFloat("betaStar")
          if isBJet(jet,"HP",self.btagging): nbP += 1
      result["SSVHEdiscDisc1"] = maxbdiscSSVHE
      result["SSVHPdiscDisc1"] = maxbdiscSSVHP
      result["CSVdiscDisc1"] = maxbdiscCSV
      result["JPdiscDisc1"] = maxbdiscJP
      result["nj"] = nj
      result["nb"] = nb
      result["nbP"] = nbP
      result["MET"] = event.MET[0].pt()
      result["METphi"] = event.MET[0].phi()
      result["METNNregression"] = event.METNNregression[0].pt()
      result["METphiNNregression"] = event.METNNregression[0].phi()
      result["METsignificance"] = 0.
      if event.MET[0].getSignificanceMatrix()(0,0)<1e10 and event.MET[0].getSignificanceMatrix()(1,1)<1e10: 
        result["METsignificance"] = event.MET[0].significance()
      #rho
      result["rho"] = event.rho[0]

      return result

def runTest(path="../testfiles/"):
  output = ROOT.TFile(zbbfile.controlPlots, "RECREATE")
  jetmetPlots = JetmetControlPlots(output.mkdir("jetmet"))
  electronsPlots = ElectronsControlPlots(output.mkdir("electrons"))
  muonsPlots = MuonsControlPlots(output.mkdir("muons"))

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
  prepareAnalysisEvent(events,checkTrigger=False)

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

