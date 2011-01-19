#! /usr/bin/env python

import ROOT
import sys
from DataFormats.FWLite import Events, Handle
from eventSelection import *

class eventSelectionControlPlots:
    """A class to create control plots for event selection"""

    def __init__(self, file=None):
      # create output file if needed. If no file is given, it means it is delegated
      if file is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("eventSelection")
        self.owner = True
      else :
        self.f = file
        self.dir = file.pwd()
        self.owner = False
    
    def beginJob(self, jetlabel="cleanPatJets", zlabel="Ztightloose", vertexlabel="goodPV" ):
      # declare histograms
      self.dir.cd()
      self.h_triggerSelection = ROOT.TH1I("triggerSelection","triggerSelection ",2,0,2)
      self.h_triggerBit = ROOT.TH1I("triggerBits","trigger bits",20,0,20)
      self.h_SSVHEdisc = ROOT.TH1F("SSVHEdisc","SSVHEdisc",100,-5,5)
      self.h_SSVHPdisc = ROOT.TH1F("SSVHPdisc","SSVHPdisc",100,-5,5)
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
      self.h_vecdptZbj1 = ROOT.TH1F("vecdptZbj1","vecdptZbj1",500,0,500)
      self.h_dphiZbj1 = ROOT.TH1F("dphiZbj1","dphiZbj1",80,-4,4)
      self.h_dijetM = ROOT.TH1F("dijetM","b bbar invariant mass",1000,0,1000)
      self.h_dijetPt = ROOT.TH1F("dijetPt","b bbar Pt",500,0,500)
      self.h_ZbM = ROOT.TH1F("ZbM","Zb invariant mass",1000,0,1000)
      self.h_ZbPt = ROOT.TH1F("ZbPt","Zb Pt",500,0,500)
      self.h_ZbbM = ROOT.TH1F("ZbbM","Zbb invariant mass",1000,0,1000)
      self.h_ZbbPt = ROOT.TH1F("ZbbPt","Zbb Pt",500,0,500)
      self.h_ZbbM2D = ROOT.TH1F("ZbbM2D","Zbb mass vs bb mass",100,0,1000,100,0,1000)
      self.h_category = ROOT.TH1I("category","event category",10,0,10)  
      self.h_jetpt = ROOT.TH1F("jetpt","Jet Pt",100,15,215)
      self.h_jeteta = ROOT.TH1F("jeteta","Jet eta",50,-2.5, 2.5)
      self.h_jetphi = ROOT.TH1F("jetphi","Jet phi",80,-4,4)
      self.h_jetoverlapmu = ROOT.TH1I("jetoverlapmu","jets overlaps with muons",2,0,2)
      self.h_jetoverlapele = ROOT.TH1I("jetoverlapele","jets overlaps with electrons",2,0,2)
      self.h_eleid = ROOT.TH1I("eleid","electron id",10,0,10)
      self.h_elept = ROOT.TH1F("elept","electron pt",500,0,500)
      self.h_eleeta = ROOT.TH1F("eleeta","electron eta",100,-5,5)
      self.h_eledb = ROOT.TH1F("eledb","electron dB",100,0,0.1)
      self.h_eleoverlapmu = ROOT.TH1I("eleoverlapmu","electrons overlaps with muon",2,0,2)
      # prepare handles
      self.jetHandle = Handle ("vector<pat::Jet>")
      self.zHandle = Handle ("vector<reco::CompositeCandidate>")
      self.vertexHandle = Handle ("vector<reco::Vertex>")
      self.jetlabel = (jetlabel)
      self.zlabel = (zlabel)
      self.vertexlabel = (vertexlabel)
    
    def processEvent(self,event):
      # load event
      event.getByLabel (self.jetlabel,self.jetHandle)
      event.getByLabel (self.zlabel,self.zHandle)
      event.getByLabel (self.vertexlabel,self.vertexHandle)
      jets = self.jetHandle.product()
      zs = self.zHandle.product()
      vs = self.vertexHandle.product()
      # process event and fill histograms
      # for now, I use the Z candidate to select the channel. This is not robust w.r.t. overlaps in the datasets.
      for i in range(13):
        if triggerInfo[i]: self.h_triggers.Fill(i)
      bestZcandidate = findBestCandidate(zCandidatesMu,zCandidatesEle) 
      # trigger
      self.h_triggerSelection.Fill(isTriggerOK(triggerInfo, bestZcandidate.daughter(0).isMuon()))
      trigger = 0
      for trigger in range(triggerInfo.size()):
        if triggerInfo[trigger] : self.h_triggerBit.Fill(trigger)
      # lepton selection
      for muon in muons:
        # for muons:
        # could be done for each category of muons
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
        # could be done for each category of electrons
        self.h_eleid.Fill(electron.electronID("simpleEleId85relIso"))
        # add variables from  simpleEleId85relIso (see twiki)
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
          self.h_SSVHEdisc.Fill(jet.bDiscriminant("simpleSecondaryVertexHighEffBJetTags"))
          self.h_SSVHPdisc.Fill(jet.bDiscriminant("simpleSecondaryVertexHighPurBJetTags"))
          #eventually complement with variables from the btagging (check paper)
      # Z boson
      for z in zCandidatesMu:
        self.h_zmassMu.Fill(z.mass())
        self.h_zptMu.Fill(z.pt())
      if bestZcandidate.daughter(0).isMuon():
        self.h_massBestMu.Fill(bestZcandidate.mass())
        self.h_ptBestMu.Fill(bestZcandidate.pt())
      for z in zCandidatesEle:
        self.h_zmassEle.Fill(z.mass())
        self.h_zptEle.Fill(z.pt())
      if bestZcandidate.daughter(0).isElectron() :
        self.h_massBestEle.Fill(bestZcandidate.mass())
        self.h_ptBestEle.Fill(bestZcandidate.pt())
      # some topological quantities
      self.h_met.Fill(met.pt())
      self.h_scaldptZbj1.Fill(bestZcandidate.pt()-bjet1.pt())
      self.h_vecdptZbj1.Fill(sqrt((bestZcandidate.px()+bjet1.px())**2+(bestZcandidate.py()+bjet1.py())**2))
      self.h_dphiZbj1.Fill(dphi(bestZcandidate,bjet1))
      bb = bjet1 + bjet2
      self.h_dijetM.Fill(bb.mass())
      self.h_dijetPt.Fill(bb.pt())
      Zb = bestZcandidate + bjet1
      self.h_ZbM.Fill(Zb.mass())
      self.h_ZbPt.Fill(Zb.pt())
      Zbb = Zb + bjet2
      self.h_ZbbM.Fill(Zbb.mass())
      self.h_ZbbPt.Fill(Zbb.pt())
      self.h_ZbbM2D.Fill(Zbb.mass(),bb.mass())
      # event category
      self.h_category.Fill(eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets))
    
    def endJob(self):
      self.f.cd()
      self.f.Write()
      if self.owner:
        self.f.Close()

def runTest():
  controlPlots = eventSelectionControlPlots()
  files = ["/home/fynu/jdf/scratch/CMSSW_3_9_7/src/Analysis/Analysis/MURun2010B-DiLeptonMu-Dec22Skim_tracks.root"]
#  files = ["/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_10_1_1ji.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_11_1_rUv.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_12_1_55h.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_13_1_6jY.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_14_1_9wH.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_15_1_yTY.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_16_1_aIs.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_17_1_ccv.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_18_1_73c.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_19_1_y3l.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_1_1_Zlh.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_20_1_x6N.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_21_1_p76.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_22_1_KYP.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_23_1_aev.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_24_1_4Uz.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_25_1_wvg.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_26_1_kqK.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_27_1_Pk8.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_28_1_PV6.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_29_1_4jI.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_2_1_Clt.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_30_1_OZC.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_31_1_dZY.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_32_1_tv8.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_33_1_QxH.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_34_1_dpf.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_35_1_gM5.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_36_1_Qr9.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_37_1_Dcx.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_38_1_MM6.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_39_1_eEA.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_3_1_8TE.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_40_1_9Km.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_41_1_7Vi.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_42_1_h7i.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_43_1_D2c.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_44_1_9nZ.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_45_1_ZI2.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_46_1_O6e.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_47_1_wL6.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_48_1_6aV.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_49_1_YD2.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_4_1_QVO.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_50_1_Rh9.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_51_1_ErJ.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_52_1_81z.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_53_1_mo6.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_54_1_fW8.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_55_1_kmS.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_56_1_trf.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_57_1_znE.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_58_1_giA.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_59_1_t8m.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_5_1_0gw.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_60_1_UT7.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_61_1_02X.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_62_1_0mU.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_63_1_4SN.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_64_1_zLt.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_65_1_3Xb.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_66_1_GvE.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_67_1_Kat.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_68_1_fEE.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_69_1_ibF.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_6_1_F3i.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_70_1_P3m.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_71_1_dsR.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_72_1_kDn.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_73_1_tk2.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_74_1_a85.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_75_1_T7O.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_76_1_Y4g.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_77_1_b5T.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_78_1_cjo.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_79_1_GN1.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_7_1_9hj.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_8_1_Vrv.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_9_1_tgy.root"]
  events = Events (files)
  controlPlots.beginJob()
  i = 0
  for event in events:
    controlPlots.processEvent(event)
    if i%1000==0 : print "Processing... event ", i
    i += 1
  controlPlots.endJob()

