#! /usr/bin/env python

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from baseControlPlots import BaseControlPlots
from eventSelection import *
#from myFuncTimer import print_timing

class EventSelectionControlPlots(BaseControlPlots):
    """A class to create control plots for event selection"""

    def __init__(self, dir=None, muChannel=True, checkTrigger=False, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="eventSelection", dataset=dataset, mode=mode)
      self.muChannel = muChannel
      self.checkTrigger = checkTrigger
    
    def beginJob(self, metlabel="patMETsPF", jetlabel="cleanPatJets", zmulabel="Ztighttight", zelelabel="Zelel", triggerlabel="patTriggerEvent", btagging="SSV"):
      self.btagging = btagging
      # declare histograms
      self.add("run","Run number",15000,160000,175000)
      self.add("triggerSelection","triggerSelection ",2,0,2)
      self.add("triggerBits","trigger bits",20,0,20)
      self.add("zmassMu","zmassMu",10000,0,1000)
      self.add("bestzmassMu","bestzmassMu",10000,0,1000)
      self.add("zmassEle","zmassEle",10000,0,1000)
      self.add("bestzmassEle","bestzmassEle",10000,0,1000)
      self.add("zptMu","zptMu",500,0,500)
      self.add("bestzptMu","bestzptMu",500,0,500)
      self.add("zptEle","zptEle",500,0,500)
      self.add("bestzptEle","bestzptEle",500,0,500)
      self.add("scaldptZbj1","scaldptZbj1",1000,-500,500)
      self.add("drZbj1","distance between Z and leading jet",100,0,5)
      self.add("dphiZbj1","dphiZbj1",40,0,4)
      self.add("scaldptZbb","scaldptZbb",1000,-500,500)
      self.add("dphiZbb","dphiZbb",40,0,4)
      self.add("drZbb","dphiZbb",100,0,5)
      self.add("dijetM","b bbar invariant mass",1000,0,1000)
      self.add("dijetPt","b bbar Pt",500,0,500)
      self.add("dijetdR","#Delta R (b bbar)",100,0,5)
      self.add("dijetSVdR","#Delta R (b bbar SV)",100,0,5)
      self.add("dphidijetMET","#Delta #phi (b bbar MET)",40,0,4)
      self.add("ZbM","Zb invariant mass",1000,0,1000)
      self.add("ZbPt","Zb Pt",500,0,500)
      self.add("ZbbM","Zbb invariant mass",1000,0,1000)
      self.add("ZbbPt","Zbb Pt",500,0,500)
      self.add("category","event category",eventCategories()+1,0,eventCategories()+1)  
      self.add("mu1pt","leading muon Pt",500,0,500)
      self.add("mu2pt","subleading muon Pt",500,0,500)
      self.add("mu1eta","leading muon Eta",25,0,2.5)
      self.add("mu2eta","subleading muon Eta",25,0,2.5)
      self.add("mu1etapm","leading muon Eta",50,-2.5,2.5)
      self.add("mu2etapm","subleading muon Eta",50,-2.5,2.5)
      self.add("el1pt","leading electron Pt",500,0,500)
      self.add("el2pt","subleading electron Pt",500,0,500)
      self.add("el1eta","leading electron Eta",25,0,2.5)
      self.add("el2eta","subleading electron Eta",25,0,2.5)
      self.add("el1etapm","leading electron Eta",50,-2.5,2.5)
      self.add("el2etapm","subleading electron Eta",50,-2.5,2.5)
      self.add("SSVHEdisc","SSVHEdisc",200,-10,10)
      self.add("SSVHPdisc","SSVHPdisc",200,-10,10)
      self.add("MET","MET",100,0,200)
      self.add("METphi","MET #phi",70,-3.5,3.5)
      self.add("jetpt","Jet Pt",100,15,215)
      self.add("jeteta","Jet eta",25,0, 2.5)
      self.add("jetetapm","Jet eta",50,-2.5, 2.5)
      self.add("jetphi","Jet phi",80,-4,4)
      self.add("jetoverlapmu","jets overlaps with muons",2,0,2)
      self.add("jetoverlapele","jets overlaps with electrons",2,0,2)
      self.add("jet1pt","leading jet Pt",500,15,515)
      self.add("jet1eta","leading jet Eta",25,0,2.5)
      self.add("jet1etapm","leading jet Eta",50,-2.5,2.5)
      self.add("jet2pt","subleading jet Pt",500,15,515)
      self.add("jet2eta","subleading jet Eta",25,0,2.5)
      self.add("jet2etapm","subleading jet Eta",50,-2.5,2.5)
      self.add("bjet1pt","leading bjet Pt",500,15,515)
      self.add("bjet1eta","leading bjet Eta",25,0,2.5)
      self.add("bjet1etapm","leading bjet Eta",50,-2.5,2.5)
      self.add("bjet2pt","subleading bjet Pt",500,15,515)
      self.add("bjet2eta","subleading bjet Eta",25,0,2.5)
      self.add("bjet2etapm","subleading bjet Eta",50,-2.5,2.5)
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
      self.jetHandle = Handle ("vector<pat::Jet>")
      self.metHandle = Handle ("vector<pat::MET>")
      self.zmuHandle = Handle ("vector<reco::CompositeCandidate>")
      self.zeleHandle = Handle ("vector<reco::CompositeCandidate>")
      self.trigInfoHandle = Handle ("pat::TriggerEvent")
      self.jetlabel = jetlabel
      self.metlabel = metlabel
      self.zmulabel = zmulabel
      self.zelelabel = zelelabel
      self.trigInfolabel = triggerlabel
    
    #@print_timing
    def process(self, event):
      """eventSelectionControlPlots"""
      result = { }
      # load event
      event.getByLabel(self.jetlabel,self.jetHandle)
      event.getByLabel(self.metlabel,self.metHandle)
      event.getByLabel(self.zmulabel,self.zmuHandle)
      event.getByLabel(self.zelelabel,self.zeleHandle)
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
      #TODO: debug that plot (empty)
      #self.h_triggerSelection.Fill(isTriggerOK(triggerInfo, self.muChannel),weight)
      #selTriggers = selectedTriggers(triggerInfo)
      #for trigger,triggered in enumerate(selTriggers):
      #  if triggered : self.h_triggerBit.Fill(trigger,weight)
      ## event category
      categoryData = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, self.muChannel)
      result["category"] = [ ]
      for category in range(eventCategories()):
        if isInCategory(category, categoryData):
          result["category"].append(category)
      result["run"] = event.eventAuxiliary().run()
      ## Z boson
      result["zmassMu"] = [ ]
      result["zptMu"] = [ ]
      for z in zCandidatesMu:
        result["zmassMu"].append(z.mass())
        result["zptMu"].append(z.pt())
      result["zmassEle"] = [ ]
      result["zptEle"] = [ ]
      for z in zCandidatesEle:
        result["zmassEle"].append(z.mass())
        result["zptEle"].append(z.pt())
      bestZcandidate = findBestCandidate(None,zCandidatesMu,zCandidatesEle) 
      if not bestZcandidate is None:
        if bestZcandidate.daughter(0).isMuon():
          mu1 = bestZcandidate.daughter(0)
          mu2 = bestZcandidate.daughter(1)
          if mu1.pt() < mu2.pt():
            mu1 = bestZcandidate.daughter(1)
            mu2 = bestZcandidate.daughter(0)
          result["bestzmassMu"] = bestZcandidate.mass()
          result["bestzptMu"] = bestZcandidate.pt()
          result["mu1pt"] = mu1.pt()
          result["mu2pt"] = mu2.pt()
          result["mu1etapm"] = mu1.eta()
          result["mu1eta"] = abs(mu1.eta())
          result["mu2eta"] = abs(mu2.eta())
          result["mu2etapm"] = mu2.eta()
        if bestZcandidate.daughter(0).isElectron() :
          ele1 = bestZcandidate.daughter(0)
          ele2 = bestZcandidate.daughter(1)
          if ele1.pt() < ele2.pt():
            ele1 = bestZcandidate.daughter(1)
            ele2 = bestZcandidate.daughter(0)
          result["bestzmassEle"] = bestZcandidate.mass()
          result["bestzptEle"] = bestZcandidate.pt()
          result["el1pt"] = ele1.pt()
          result["el2pt"] = ele2.pt()
          result["el1eta"] = abs(ele1.eta())
          result["el2eta"] = abs(ele2.eta())
          result["el1etapm"] = ele1.eta()
          result["el2etapm"] = ele2.eta()
      ## jet plots
      nj  = 0
      nb  = 0
      nbP = 0
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
      result["SSVHEdisc"] = [ ]
      result["SSVHPdisc"] = [ ]
      for jet in jets:
        #jetPt = jetpt(jet) 
        jetPt = jet.pt()
        if isGoodJet(jet,bestZcandidate):#hasNoOverlap(jet, bestZcandidate): 
          rawjet = jet.correctedJet("Uncorrected")
          #result["jetpt"].append(jetPt)
          result["jetpt"].append(jet.pt())
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
          nj += 1
          if nj==1: 
            result["jet1pt"] = jetPt #jet.pt()
            result["jet1eta"] = abs(jet.eta())
            result["jet1etapm"] = jet.eta()
          elif nj==2:
            result["jet2pt"] = jetPt #jet.pt()
            result["jet2eta"] = abs(jet.eta())
            result["jet2etapm"] = jet.eta()
          if isBJet(jet,"HE",self.btagging): 
            nb += 1
            if nb==1:
              result["bjet1pt"] = jetPt #jet.pt()
              result["bjet1eta"] = abs(jet.eta())
              result["bjet1etapm"] = jet.eta()
            elif nb==2:
              result["bjet2pt"] = jetPt #jet.pt()
              result["bjet2eta"] = abs(jet.eta())
              result["bjet2etapm"] = jet.eta()
          if isBJet(jet,"HP",self.btagging): nbP += 1
      result["nj"] = nj
      result["nb"] = nb
      result["nbP"] = nbP
      result["MET"] = met[0].pt()
      result["METphi"] = met[0].phi()
      ## plots looking for resonnances / kinematics
      if isInCategory(4, categoryData):
        # that method returns the best jet pair. When only one is btagged, it is the first one.
        # when two bjets are present, these are the two.
        # this means that in cat 4 we have here Zj and Zjj
        # in cat 5 we have Zb and Zbl
        # in cat 9 we have Zb and Zbb
        # later on, variables are refering to b-jets, sometimes they are not.
        z = ROOT.TLorentzVector(bestZcandidate.px(),bestZcandidate.py(),bestZcandidate.pz(),bestZcandidate.energy())
        dijet = findDijetPair(jets, bestZcandidate, self.btagging)
        if dijet[0] is None: return result # this should never happen
        b1 = ROOT.TLorentzVector(dijet[0].px(),dijet[0].py(),dijet[0].pz(),dijet[0].energy())
        Zb = z+b1
        result["ZbM"] = Zb.M()
        result["ZbPt"] = Zb.Pt()
        result["scaldptZbj1"] = bestZcandidate.pt()-dijet[0].pt()
        result["dphiZbj1"] = abs(z.DeltaPhi(b1))
        result["drZbj1"] = z.DeltaR(b1)
        if dijet[1] is None: return result
        b2 = ROOT.TLorentzVector(dijet[1].px(),dijet[1].py(),dijet[1].pz(),dijet[1].energy())
        if dijet[0].tagInfoSecondaryVertex("secondaryVertex").nVertices()>0 and dijet[1].tagInfoSecondaryVertex("secondaryVertex").nVertices()>0 :
          b1SVvec = dijet[0].tagInfoSecondaryVertex("secondaryVertex").flightDirection(0)
          b1SV = ROOT.TVector3(b1SVvec.x(),b1SVvec.y(),b1SVvec.z())
          b2SVvec = dijet[1].tagInfoSecondaryVertex("secondaryVertex").flightDirection(0)
          b2SV = ROOT.TVector3(b2SVvec.x(),b2SVvec.y(),b2SVvec.z())
          svdr = b1SV.DeltaR(b2SV)
        else:
          svdr = -1
        bb = b1 + b2
        Zbb = Zb + b2
        met4v = ROOT.TLorentzVector(met[0].px(),met[0].py(),met[0].pz(),met[0].energy())
        result["dijetM"] = bb.M()
        result["dijetPt"] = bb.Pt()
        result["dijetdR"] = b1.DeltaR(b2)
        result["dijetSVdR"] = svdr
        result["ZbbM"] = Zbb.M()
        result["ZbbPt"] = Zbb.Pt()
        result["scaldptZbb"] = bestZcandidate.pt()-bb.Pt()
        result["dphiZbb"] = abs(z.DeltaPhi(bb))
        result["drZbb"] = z.DeltaR(bb)
        result["dphidijetMET"] = bb.DeltaPhi(met4v)
      return result

def runTest():
  controlPlots = EventSelectionControlPlots(muChannel=True)
  path="/home/fynu/lceard/store/Prod_AOD_2011A/Round2_ReRecoMay10_204pb/Mu_2011A_May10ReRe_204pb/"
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

def dumpEventList(stage=6, muChannel=True, path="/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/"):
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)
  metlabel="patMETsPF"
  jetlabel="cleanPatJets"
  zmulabel="Ztighttight"
  zelelabel="Zelel"
  triggerlabel="patTriggerEvent"
  jetHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  trigInfoHandle = Handle ("pat::TriggerEvent")
  for event in events:
    event.getByLabel (jetlabel,jetHandle)
    event.getByLabel (metlabel,metHandle)
    event.getByLabel (zmulabel,zmuHandle)
    event.getByLabel (zelelabel,zeleHandle)
    event.getByLabel (triggerlabel,trigInfoHandle)
    jets = jetHandle.product()
    met = metHandle.product()
    zCandidatesMu = zmuHandle.product()
    zCandidatesEle = zeleHandle.product()
    triggerInfo = trigInfoHandle.product()
    categoryData = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, muChannel)
    if isInCategory(stage, categoryData):
      print "Run", event.eventAuxiliary().run(), ", Lumisection", event.eventAuxiliary().luminosityBlock(), ", Event", event.eventAuxiliary().id().event()
