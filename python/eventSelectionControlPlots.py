#! /usr/bin/env python

import ROOT
import sys
from math import sin
from DataFormats.FWLite import Events, Handle
from eventSelection import *

#TODO: split between eventSelection and object control plots
class eventSelectionControlPlots:
    """A class to create control plots for event selection"""

    def __init__(self, file=None, muChannel=True):
      # create output file if needed. If no file is given, it means it is delegated
      if file is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("eventSelection")
        self.owner = True
      else :
        self.f = file
        self.dir = file.pwd()
        self.owner = False
      self.muChannel = muChannel
    
    def beginJob(self, jetlabel="cleanPatJets", zmulabel="Ztightloose", zelelabel="Zelel", vertexlabel="goodPV", triggerlabel="WeightFromTrigger", muonlabel="matchedMuons", electronlabel="matchedElectrons", metlabel="patMETsPF" ):
      # declare histograms
      self.dir.cd()
      self.h_triggerSelection = ROOT.TH1I("triggerSelection","triggerSelection ",2,0,2)
      self.h_triggerBit = ROOT.TH1I("triggerBits","trigger bits",20,0,20)
      self.h_SSVHEdisc = ROOT.TH1F("SSVHEdisc","SSVHEdisc",200,-10,10)
      self.h_SSVHPdisc = ROOT.TH1F("SSVHPdisc","SSVHPdisc",200,-10,10)
      self.h_zmassMu = ROOT.TH1F("zmassMu","zmassMu",2000,0,200)
      self.h_massBestMu = ROOT.TH1F("bestzmassMu","bestzmassMu",2000,0,200)
      self.h_zmassEle = ROOT.TH1F("zmassEle","zmassEle",2000,0,200)
      self.h_massBestEle = ROOT.TH1F("bestzmassEle","bestzmassEle",2000,0,200)
      self.h_zptMu = ROOT.TH1F("zptMu","zptMu",500,0,500)
      self.h_ptBestMu = ROOT.TH1F("bestzptMu","bestzptMu",500,0,500)
      self.h_zptEle = ROOT.TH1F("zptEle","zptEle",500,0,500)
      self.h_ptBestEle = ROOT.TH1F("bestzptEle","bestzptEle",500,0,500)
      self.h_met = ROOT.TH1F("MET","MET",100,0,200)
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
      self.h_jetpt = ROOT.TH1F("jetpt","Jet Pt",100,15,215)
      self.h_jeteta = ROOT.TH1F("jeteta","Jet eta",50,-2.5, 2.5)
      self.h_jetphi = ROOT.TH1F("jetphi","Jet phi",80,-4,4)
      self.h_jetoverlapmu = ROOT.TH1I("jetoverlapmu","jets overlaps with muons",2,0,2)
      self.h_jetoverlapele = ROOT.TH1I("jetoverlapele","jets overlaps with electrons",2,0,2)
      self.h_muonType = ROOT.TH1I("muonType","Muon type", 4,0,4)
      self.h_muonhits = ROOT.TH1I("muonhits","Muon hits",50,0,50)
      self.h_muonIso = ROOT.TH1F("muonIso","Muon isolatio",100,0,1)
      self.h_muonPt = ROOT.TH1F("muonPt","Muon Pt",500,0,500)
      self.h_muonEta = ROOT.TH1F("muonEta","Muon Eta",50,-2.5,2.5)
      self.h_muonChi2 = ROOT.TH1F("muonChi2","Muon normalized chi2",100,0,20)
      self.h_muonPHits = ROOT.TH1I("muonPHits","Muon Pixel hits",10,0,10)
      self.h_muonSHits = ROOT.TH1I("muonSHits","Muon Strip hits",30,0,30)
      self.h_muonMatches = ROOT.TH1I("muonMatches","Muon matched segments",10,0,10)
      self.h_muonMHits = ROOT.TH1I("muonMHits","Muon muon hits",100,0,100)
      self.h_eleid = ROOT.TH1I("eleid","electron id",10,0,10)
      self.h_elemisshits = ROOT.TH1I("elemisshits","Electron missing hits",5,0,5)
      self.h_elept = ROOT.TH1F("elept","electron pt",500,0,500)
      self.h_eleeta = ROOT.TH1F("eleeta","electron eta",100,-5,5)
      self.h_eledb = ROOT.TH1F("eledb","electron dB",100,0,0.05)
      self.h_eleoverlapmu = ROOT.TH1I("eleoverlapmu","electrons overlaps with muon",2,0,2)
      self.h_eleHcalIso = ROOT.TH1F("eleHcalIso","Electron HCAL relative isolation dr03",100,0,0.2)
      self.h_eleEcalIso = ROOT.TH1F("eleEcalIso","Electron ECAL relative isolation dr03",100,0,0.2)
      self.h_eleTkIso = ROOT.TH1F("eleTkIso","Electron Tk relative isolation dr03",100,0,0.2)
      self.h_eleHoE = ROOT.TH1F("eleHoE","Electron H over E",100,0,0.1)
      self.h_eledphi = ROOT.TH1F("eledphi","Electron dphi at calo",100,0,0.1)
      self.h_eledeta = ROOT.TH1F("eledeta","Electron deta at calo",100,0,0.01)
      self.h_eleinin = ROOT.TH1F("eleinin","Electron sigma ieta ieta",100,0,0.1)
      self.h_mu1pt = ROOT.TH1F("mu1pt","leading muon Pt",500,0,500)
      self.h_mu2pt = ROOT.TH1F("mu2pt","subleading muon Pt",500,0,500)
      self.h_mu1eta = ROOT.TH1F("mu1eta","leading muon Eta",50,-2.5,2.5)
      self.h_mu2eta = ROOT.TH1F("mu2eta","subleading muon Eta",50,-2.5,2.5)
      self.h_el1pt = ROOT.TH1F("el1pt","leading electron Pt",500,0,500)
      self.h_el2pt = ROOT.TH1F("el2pt","subleading electron Pt",500,0,500)
      self.h_el1eta = ROOT.TH1F("el1eta","leading electron Eta",50,-2.5,2.5)
      self.h_el2eta = ROOT.TH1F("el2eta","subleading electron Eta",50,-2.5,2.5)
      self.h_jet1pt = ROOT.TH1F("jet1pt","leading jet Pt",500,0,500)
      self.h_jet1eta = ROOT.TH1F("jet1eta","leading jet Eta",50,-2.5,2.5)
      self.h_jet2pt = ROOT.TH1F("jet2pt","subleading jet Pt",500,0,500)
      self.h_jet2eta = ROOT.TH1F("jet2eta","subleading jet Eta",50,-2.5,2.5)
      self.h_nmu = ROOT.TH1I("nmu","muon count",5,0,5)
      self.h_nel = ROOT.TH1I("nel","electron count",5,0,5)
      self.h_nl = ROOT.TH2I("nl","number of electron vs number of muons",5,0,5,5,0,5)
      self.h_nj = ROOT.TH1I("nj","jet count",15,0,15)
      self.h_nb = ROOT.TH1I("nb","b-jet count",5,0,5)
      self.h_nbP = ROOT.TH1I("nbP","pure b-jet count",5,0,5)
      self.h_njb = ROOT.TH2I("njb","number of bjets vs number of jets",15,0,15,5,0,5)
      
      # prepare handles
      self.jetHandle = Handle ("vector<pat::Jet>")
      self.zmuHandle = Handle ("vector<reco::CompositeCandidate>")
      self.zeleHandle = Handle ("vector<reco::CompositeCandidate>")
      self.vertexHandle = Handle ("vector<reco::Vertex>")
      self.trigInfoHandle = Handle ("vector<bool>")
      self.muonHandle = Handle ("vector<pat::Muon>")
      self.electronHandle = Handle ("vector<pat::Electron>")
      self.metHandle = Handle ("vector<pat::MET>")
      self.jetlabel = (jetlabel)
      self.zmulabel = (zmulabel)
      self.zelelabel = (zelelabel)
      self.vertexlabel = (vertexlabel)
      self.trigInfolabel = (triggerlabel)
      self.electronlabel = (electronlabel)
      self.muonlabel = (muonlabel)
      self.metlabel = (metlabel)
    
    def processEvent(self,event):
      # load event
      event.getByLabel (self.jetlabel,self.jetHandle)
      event.getByLabel (self.zmulabel,self.zmuHandle)
      event.getByLabel (self.zelelabel,self.zeleHandle)
      event.getByLabel (self.vertexlabel,self.vertexHandle)
      event.getByLabel (self.trigInfolabel,"SelectedTriggers",self.trigInfoHandle)
      event.getByLabel (self.electronlabel,self.electronHandle)
      event.getByLabel (self.muonlabel,self.muonHandle)
      event.getByLabel (self.metlabel,self.metHandle)
      jets = self.jetHandle.product()
      zCandidatesMu = self.zmuHandle.product()
      zCandidatesEle = self.zeleHandle.product()
      vs = self.vertexHandle.product()
      triggerInfo = self.trigInfoHandle.product()
      muons = self.muonHandle.product()
      electrons = self.electronHandle.product()
      met = self.metHandle.product()
      # process event and fill histograms
      # TODO: ROOT BUG HERE : vector<bool> dictionnary is incomplete
      #for i in range(13):
      #  if triggerInfo[i] : self.h_triggers.Fill(i)
      ## trigger
      self.h_triggerSelection.Fill(isTriggerOK(triggerInfo, self.muChannel))
      #trigger = 0
      #for trigger in range(triggerInfo.size()):
      #  if triggerInfo[trigger] : self.h_triggerBit.Fill(trigger)
      # lepton selection
      for muon in muons:
        # for muons:
        # could be done for each category of muons -> call the package several times
        self.h_muonType.Fill(muon.isGlobalMuon()+2*muon.isTrackerMuon())
        self.h_muonhits.Fill(muon.innerTrack().numberOfValidHits())
        self.h_muonIso.Fill((muon.trackIso()+muon.caloIso())/muon.pt())
        self.h_muonPt.Fill(muon.pt())
        self.h_muonEta.Fill(muon.eta())
        self.h_muonChi2.Fill(muon.normChi2())
        self.h_muonPHits.Fill(muon.innerTrack().hitPattern().numberOfValidPixelHits())
        self.h_muonSHits.Fill(muon.innerTrack().hitPattern().numberOfValidStripHits())
        self.h_muonMatches.Fill(muon.numberOfMatches())
        self.h_muonMHits.Fill(muon.globalTrack().hitPattern().numberOfValidMuonHits())
      for electron in electrons:
        # for electrons
        # could be done for each category of electrons -> call the package several times
        self.h_eleid.Fill(electron.electronID("simpleEleId85relIso"))
        self.h_elemisshits.Fill(electron.gsfTrack().numberOfLostHits())
        scEt = (electron.ecalEnergy()*sin(electron.theta()))
        self.h_eleHcalIso.Fill(electron.dr03HcalTowerSumEt()/scEt)
        self.h_eleEcalIso.Fill(electron.dr03EcalRecHitSumEt()/scEt)
        self.h_eleTkIso.Fill(electron.dr03TkSumPt()/scEt)
        self.h_eleHoE.Fill(electron.hadronicOverEm())
        self.h_eledphi.Fill(electron.deltaPhiEleClusterTrackAtCalo())
        self.h_eledeta.Fill(electron.deltaEtaEleClusterTrackAtCalo())
        self.h_eleinin.Fill(electron.scSigmaIEtaIEta())
        self.h_elept.Fill(electron.pt())
        self.h_eleeta.Fill(electron.eta())
        self.h_eledb.Fill(abs(electron.dB()))
        self.h_eleoverlapmu.Fill(electron.hasOverlaps("muons"))
        # add any additional cut at fwlite level
      # jets 
      for jet in jets:
        self.h_jetpt.Fill(jet.pt())
        self.h_jeteta.Fill(jet.eta())
        self.h_jetphi.Fill(jet.phi())
        self.h_jetoverlapmu.Fill(jet.hasOverlaps("muons"))
        self.h_jetoverlapele.Fill(jet.hasOverlaps("electrons"))
        # add plots as soon as the jet selection is in place
        # B-tagging
        if isGoodJet(jet):
          self.h_SSVHEdisc.Fill(jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"))
          self.h_SSVHPdisc.Fill(jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"))
          #eventually complement with variables from the btagging (check paper)
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
      nmu = 0
      nel = 0
      nj  = 0
      nb  = 0
      nbP = 0
      for muon in muons: 
        if isGoodMuon(muon,"tight") : nmu += 1
      for electron in electrons: 
        if isGoodElectron(electron,"tight") : nel += 1
      for jet in jets: 
        if isGoodJet(jet) : 
          nj += 1
          if isBJet(jet,"HE"): nb += 1
          if isBJet(jet,"HP"): nbP += 1
      self.h_nmu.Fill(nmu)
      self.h_nel.Fill(nel)
      self.h_nl.Fill(nmu,nel)
      self.h_nj.Fill(nj)
      self.h_nb.Fill(nb)
      self.h_nbP.Fill(nbP)
      self.h_njb.Fill(nj,nb)
      category = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, self.muChannel)
      self.h_category.Fill(category)
      # some topological quantities
      self.h_met.Fill(met[0].pt())
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
      if category>= 4:
        #dijet plots
        nJets = 0
        for jet in jets:
          if isGoodJet(jet):
            nJets += 1
            if nJets==1: 
              self.h_jet1pt.Fill(jet.pt())
              self.h_jet1eta.Fill(jet.eta())
            elif nJets==2:
              self.h_jet2pt.Fill(jet.pt())
              self.h_jet2eta.Fill(jet.eta())
            else: break
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
      self.f.cd()
      self.f.Write()
      if self.owner:
        self.f.Close()

def runTest():
  controlPlots = eventSelectionControlPlots(muChannel=True)
  #  files = ["/home/fynu/jdf/scratch/CMSSW_3_9_7/src/Analysis/Analysis/MURun2010B-DiLeptonMu-Dec22Skim_tracks.root"]
  files = ["/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_10_1_zfw.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_11_1_8zm.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_1_1_hFh.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_12_1_bWc.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_13_1_EGn.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_14_1_nho.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_15_1_FGk.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_16_1_q9o.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_17_1_lZO.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_18_1_U3J.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_19_1_2Du.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_20_1_iI6.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_21_1_ph0.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_2_1_jge.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_22_1_7dk.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_23_1_N7q.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_24_1_H1E.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_25_1_wz7.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_26_1_ELV.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_27_1_z0U.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_28_1_ZE0.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_29_1_vUl.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_30_1_ZcI.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_31_1_oHq.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_3_1_j7H.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_32_1_r7r.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_33_1_ng7.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_34_1_Zwv.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_35_1_Oxk.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_36_1_ZMW.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_37_1_gM9.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_38_1_eb2.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_39_1_BWr.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_40_1_gO6.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_4_1_2hA.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_42_1_ycF.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_43_1_T5w.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_44_1_Yo3.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_45_1_tTS.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_46_1_jTW.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_47_1_int.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_48_1_VAA.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_49_1_BCS.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_50_1_lhR.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_51_1_Evz.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_5_1_Eu9.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_52_1_tQi.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_53_1_66T.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_54_1_2Ct.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_55_1_7pn.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_56_1_mcj.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_57_1_Oce.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_58_1_GcV.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_59_1_iy4.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_60_1_8aK.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_61_1_Ysv.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_6_1_o1C.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_62_1_nZC.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_63_1_tfg.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_64_1_25e.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_65_1_FFM.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_66_1_IBY.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_67_1_QIt.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_68_1_Joo.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_69_1_Qgj.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_70_1_EFb.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_71_1_eDK.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_7_1_S6R.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_72_1_8a8.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_73_1_F5T.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_74_1_QzT.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_75_1_W1B.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_76_1_D0X.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_77_1_uvb.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_78_1_k6c.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_79_1_ZNq.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_8_1_YxD.root",
  "/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_9_1_CC8.root"]

  events = Events (files)
  controlPlots.beginJob()
  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    controlPlots.processEvent(event)
    i += 1
  controlPlots.endJob()

