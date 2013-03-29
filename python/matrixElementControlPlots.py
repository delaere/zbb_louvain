#! /usr/bin/env python
import ROOT
import sys
import os
import array
from DataFormats.FWLite import Events, Handle
from math import sqrt, pi
from AnalysisEvent import AnalysisEvent
from baseControlPlots import BaseControlPlots
from eventSelection import *
from JetCorrectionUncertainty import JetCorrectionUncertaintyProxy
from zbbCommons import zbbme, zbblabel
#from myFuncTimer import print_timing

class MatrixElementControlPlots(BaseControlPlots):
    """A class to create control plots for event selection"""

    def __init__(self, dir=None, muChannel=True, checkTrigger=False, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="me", dataset=dataset, mode=mode)
      self.muChannel = muChannel
      self.checkTrigger = checkTrigger
      self._JECuncertainty = JetCorrectionUncertaintyProxy()
    
    def beginJob(self, btagging="CSV"):
      # declare histograms
      self.btagging =btagging 
      
      self.add("bjet1pt","leading bjet Pt",1,0.,99999.)
      self.add("bjet1ptNNCorr","leading bjet Pt NNCorr",1,0.,99999.)
      self.add("bjet1etapm","leading bjet Eta",50,-2.5,2.5)
      self.add("bjet1phi","leading bjet Phi",25,-4,4)
      self.add("bjet1mass","leading bjet mass",1,0.,99999.)
      self.add("bjet1massNNCorr","leading bjet mass NNCorr",1,0.,99999.)
      self.add("bjet2pt","subleading bjet Pt",1,0.,99999.)
      self.add("bjet2ptNNCorr","subleading bjet Pt NNCorr",1,0.,99999.)
      self.add("bjet2etapm","subleading bjet Eta",50,-2.5,2.5)
      self.add("bjet2phi","subleading bjet Phi",25,-4,4)
      self.add("bjet2mass","subleading bjet mass",1,0.,99999.)
      self.add("bjet2massNNCorr","subleading bjet mass NNCorr",1,0.,99999.)
      self.add("mu1pt","leading muon Pt",1,0,99999.)
      self.add("mu1etapm","leading muon Eta",50,-2.5,2.5)
      self.add("mu1phi","leading muon phi",30,-4,4)
      self.add("mu1mass","leading muon mass",1,0,99999.)
      self.add("mu1charge","leading muon charge",3,-1.5,1.5)
      self.add("mu2pt","subleading muon Pt",1,0,99999.)
      self.add("mu2etapm","subleading muon Eta",50,-2.5,2.5)
      self.add("mu2phi","subleading muon phi",30,-4,4)
      self.add("mu2mass","subleading muon mass",1,0,99999.)
      self.add("mu2charge","subleading muon charge",3,-1.5,1.5)    
      self.add("el1pt","leading electron Pt",1,0,99999.)
      self.add("el1etapm","leading electron Eta",50,-2.5,2.5)
      self.add("el1phi","leading electron phi",30,-4,4)
      self.add("el1mass","leading electron mass",1,0,99999.)
      self.add("el1charge","leading electron charge",3,-1.5,1.5)
      self.add("el2pt","subleading electron Pt",1,0,99999.)
      self.add("el2etapm","subleading electron Eta",50,-2.5,2.5)
      self.add("el2phi","subleading electron phi",30,-4,4)
      self.add("el2mass","subleading electron mass",1,0,99999.)
      self.add("el2charge","subleading electron charge",3,-1.5,1.5)
      self.add("MET","MET",1,0,99999.)
      self.add("METphi","MET #phi",70,-3.5,3.5)

      self.add("bbM","",1000,0,1000)
      self.add("bbNNCorrM","",1000,0,1000)


      #Jet Block for TF study
  
      # Jet TF Block  -------------------------------------------------      
      

      
      self.add("FilledJetTF","event used to fill jet TF",2,-0.5,1.5)
      self.add("FilledLepTF","event used to fill lepton TF",2,-0.5,1.5)
      self.add("E_b","E_b", 1, -99999., 99999.)
      self.add("E_jb","E_jb", 1, -99999., 99999.)
      self.add("DeltaE_jet","DeltaE_jet", 1, -99999., 99999.)
      self.add("E_ab","E_ab", 1, -99999., 99999.)
      self.add("E_jab","E_jab", 1, -99999., 99999.)
      self.add("DeltaE_ajet","DeltaE_ajet", 1, -99999., 99999.)  

      self.add("NNCorrE_jb","NNCorrE_jb", 1, -99999., 99999.)
      self.add("DeltaNNCorrE_jet","DeltaNNCorrE_jet", 1, -99999., 99999.)
      self.add("NNCorrE_jab","NNCorrE_jab", 1, -99999., 99999.)
      self.add("DeltaNNCorrE_ajet","DeltaNNCorrE_ajet", 1, -99999., 99999.)  


      self.add("phi_b","phi_b", 1, -99999., 99999.);
      self.add("phi_ab","phi_ab", 1, -99999., 99999.);
      self.add("phi_jb","phi_jb", 1, -99999., 99999.);
      self.add("phi_jab","phi_jab", 1, -99999., 99999.);
      self.add("Deltaphi_jet","Deltaphi_jet", 1, -99999., 99999.);
      self.add("Deltaphi_ajet","Deltaphi_ajet", 1, -99999., 99999.);
      self.add("Eta_b","Eta_b", 1, -99999., 99999.);
      self.add("Eta_ab","Eta_ab", 1, -99999., 99999.);
      self.add("Eta_jb","Eta_jb", 1, -99999., 99999.);
      self.add("Eta_jab","Eta_jab", 1, -99999., 99999.);
      self.add("DeltaEta_jet","DeltaEta_jet", 1, -99999., 99999.);
      self.add("DeltaEta_ajet","DeltaEta_ajet", 1, -99999., 99999.);

      # Leptons TF Block -------------------------------------------------
      self.add("E_lgm","E_lgm", 1, -99999., 99999.)
      self.add("E_lrm","E_lrm", 1, -99999., 99999.)
      self.add("DeltaE_lm","DeltaE_lm", 1, -99999., 99999.)
      self.add("E_lgp","E_lgp", 1, -99999., 99999.)
      self.add("E_lrp","E_lrp", 1, -99999., 99999.)
      self.add("DeltaE_lp","DeltaE_lp", 1, -99999., 99999.)
      self.add("phi_lgm","phi_lgm", 1, -99999., 99999.);
      self.add("phi_lgp","phi_lgp", 1, -99999., 99999.);
      self.add("phi_lrm","phi_lrm", 1, -99999., 99999.);
      self.add("phi_lrp","phi_lrp", 1, -99999., 99999.);
      self.add("Deltaphi_lm","Deltaphi_lm", 1, -99999., 99999.);
      self.add("Deltaphi_lp","Deltaphi_lp", 1, -99999., 99999.);
      self.add("Eta_lgm","Eta_lgm", 1, -99999., 99999.);
      self.add("Eta_lgp","Eta_lgp", 1, -99999., 99999.);
      self.add("Eta_lrm","Eta_lrm", 1, -99999., 99999.);
      self.add("Eta_lrp","Eta_lrp", 1, -99999., 99999.);
      self.add("DeltaEta_lm","DeltaEta_lm", 1, -99999., 99999.);
      self.add("DeltaEta_lp","DeltaEta_lp", 1, -99999., 99999.);

      self.add("PtInv_lgp",     "PtInv_lgp", 1, -99999., 99999.);
      self.add("PtInv_lgm",     "PtInv_lgm", 1, -99999., 99999.);
      self.add("PtInv_lrp",     "PtInv_lrp", 1, -99999., 99999.);
      self.add("PtInv_lrm",     "PtInv_lrm", 1, -99999., 99999.);
      self.add("DeltaPtInv_lp","DeltaPtInv_lp", 1, -99999., 99999.);
      self.add("DeltaPtInv_lm","DeltaPtInv_lm", 1, -99999., 99999.);


      self.zmulabel = zbblabel.zmumulabel
      self.zelelabel = zbblabel.zelelabel
      self.vertexlabel = zbblabel.vertexlabel
      self.genlabel=zbblabel.genlabel
      self.metlabel=zbblabel.metlabel
      self.jetlabel = zbblabel.jetlabel
      
      self.genHandle = Handle ("vector<reco::GenParticle>")      
      self.metHandle = Handle ("vector<pat::MET>")
      self.zmuHandle = Handle ("vector<reco::CompositeCandidate>")
      self.zeleHandle = Handle ("vector<reco::CompositeCandidate>")
      self.vertexHandle = Handle ("vector<reco::Vertex>") 
      self.jetHandle = Handle ("vector<pat::Jet>")
      
           
    #@print_timing
    def process(self, event):
      """matrixElementControlPlots"""
      result = { }      
      
      event.getByLabel (self.metlabel,self.metHandle)      
      event.getByLabel(self.zmulabel,self.zmuHandle)
      event.getByLabel(self.zelelabel,self.zeleHandle)
      event.getByLabel(self.vertexlabel,self.vertexHandle)
      event.getByLabel(self.jetlabel,self.jetHandle)
      
      #print "is this real data  = ",
      isrealdata = event.object().event().eventAuxiliary().isRealData()
      
      if not isrealdata:
        event.getByLabel (self.genlabel,self.genHandle)
        particles = self.genHandle.product()
      met = self.metHandle.product()  
      zCandidatesMu = self.zmuHandle.product()
      zCandidatesEle = self.zeleHandle.product()
      vertices = self.vertexHandle.product()  
      jets = self.jetHandle.product()
      
            
      ## First initialize generator level infor for Transfer Function if MC sample\
      
      # partonic information for the b-quark matching
      bq=[]
      bbarq=[]
      bjet=[]
      dR1=10
      dR2=10
      dR3=10
      dR4=10

      #gen level info and matching 
      lp=[]
      lm=[]
      #dRxy; x=gen, y=rec, p=positive, n=negative charge
      dRpp=10
      dRnn=10
      dRpn=10
      dRnp=10

      
      result["FilledJetTF"]=0
      result["FilledLepTF"]=0      
      if not isrealdata:
        #particles = event.genParticles
	for partg in particles:
	  #if partg.status() ==3: print "st3 partid=",partg.pdgId()
	  #if partg.status() ==2: print "st2 partid=",partg.pdgId()
          if partg.pdgId()==5  and partg.status()==3:
            bq+=[partg]
	    #print "found b"
          if partg.pdgId()==-5 and partg.status()==3:
            bbarq+=[partg]
	    #print "found bbar"
            
          #If mu channel search for dimuon pair, if el channel search for dielectron pair
          if self.muChannel and partg.pdgId()==13 and partg.status()==3:
            lm+=[partg]
	    #print "found lm"
          elif self.muChannel and partg.pdgId()==-13 and partg.status()==3:
            lp+=[partg]
	    #print "found lp"
          elif self.muChannel==False and partg.pdgId()==11 and partg.status()==3:
            lm+=[partg]
	    #print "found lm"
          elif self.muChannel==False and partg.pdgId()==-11 and partg.status()==3:
            lp+=[partg]
	    #print "found lp"

      #Then fill ME inputs related to MET
      result["MET"] = met[0].pt()
      #result["METphi"] = event.met[0].phi()

      #Then Fill ME inputs related to leptons and if MC event and matching lep rec-gen fill info for TF
      #both leptons should be matched in order to fill the TF info      
      
      if vertices.size()>0 :
          vertex = vertices[0]
      else:
          vertex = None
      bestZcandidate = findBestCandidate(None,vertex,zCandidatesMu,zCandidatesEle)
      if not bestZcandidate is None:
        lrecpos = None
	lrecneg = None
	if bestZcandidate.daughter(0).isMuon():
          mu1 = bestZcandidate.daughter(0)
          mu2 = bestZcandidate.daughter(1)
          if mu1.pt() < mu2.pt():
            mu1 = bestZcandidate.daughter(1)
            mu2 = bestZcandidate.daughter(0)
          lvmu1 = ROOT.TLorentzVector(mu1.px(),mu1.py(),mu1.pz(),mu1.energy())
          lvmu2 = ROOT.TLorentzVector(mu2.px(),mu2.py(),mu2.pz(),mu2.energy())
          result["mu1pt"] = mu1.pt()
          result["mu2pt"] = mu2.pt()
          result["mu1etapm"] = mu1.eta()
          result["mu2etapm"] = mu2.eta()
          result["mu1phi"] = mu1.phi()
          result["mu2phi"] = mu2.phi()
          result["mu1mass"] = mu1.mass()
          result["mu2mass"] = mu2.mass()
          result["mu1charge"] = mu1.charge()
          result["mu2charge"] = mu2.charge()
          if mu1.charge() > 0 and mu2.charge() < 0:
            lrecpos = mu1
            lrecneg = mu2
          elif mu2.charge() > 0 and mu1.charge() < 0:
            lrecpos = mu2
            lrecneg = mu1
        if bestZcandidate.daughter(0).isElectron() :
          ele1 = bestZcandidate.daughter(0)
          ele2 = bestZcandidate.daughter(1)
          if ele1.pt() < ele2.pt():
            ele1 = bestZcandidate.daughter(1)
            ele2 = bestZcandidate.daughter(0)
          lvele1 = ROOT.TLorentzVector(ele1.px(),ele1.py(),ele1.pz(),ele1.energy())
          lvele2 = ROOT.TLorentzVector(ele2.px(),ele2.py(),ele2.pz(),ele2.energy())
          result["el1pt"] = ele1.pt()
          result["el2pt"] = ele2.pt()
          result["el1etapm"] = ele1.eta()
          result["el2etapm"] = ele2.eta()
          result["el1phi"] = ele1.phi()
          result["el2phi"] = ele2.phi()
          result["el1mass"] = ele1.mass()
          result["el2mass"] = ele2.mass()
          result["el1charge"] = ele1.charge()
          result["el2charge"] = ele2.charge()
          if ele1.charge() > 0 and ele2.charge() < 0:
            lrecpos = ele1
            lrecneg = ele2
          elif ele2.charge() > 0 and ele1.charge() < 0:
            lrecpos = ele2
            lrecneg = ele1
        
        if lp:
	  "lp exist"
	if lm:
	  "lm also exist"
	if not lrecpos is None:
	  "lrecpos exists"
	if not lrecneg is None:
	  "lrecneg exists"
	if (not lp) and (not lm) and (lrecpos is None) and (lrecneg is None):
	  "neither lp, or lm, or lrecpos, orlrecneg exist"
	if lp and  lm and (not lrecpos is None) and (not lrecneg is None):
          dRpp= Delta(lrecpos,lp[0])
          dRnn= Delta(lrecneg,lm[0])
          dRnp= Delta(lrecpos,lm[0])
          dRpn= Delta(lrecneg,lp[0])

          dRmatch=0.3
          #print "dRpp=", dRpp, " dRnn=", dRnn, " dRpn=", dRpn, " dRnp=", dRnp
          if dRpp<dRmatch and dRnn<dRmatch and dRpp<dRnp and dRnn<dRpn:
              result["FilledLepTF"]=1      

              result["E_lgm"]=lm[0].energy()
              result["E_lrm"]=lrecneg.energy()
              result["E_lgp"]=lp[0].energy()
              result["E_lrp"]=lrecpos.energy()
              result["DeltaE_lp"]=lp[0].energy()-lrecpos.energy()
              result["DeltaE_lm"]=lm[0].energy()-lrecneg.energy()
              result["phi_lgm"]=lm[0].phi()
              result["phi_lrm"]=lrecneg.phi()
              result["phi_lgp"]=lp[0].phi()
              result["phi_lrp"]=lrecpos.phi()
              delta_phi1=lp[0].phi()-lrecpos.phi()
              delta_phi2=lm[0].phi()-lrecneg.phi()
              if delta_phi1>pi:
                delta_phi1=(2*pi)-delta_phi1
              if delta_phi2>pi:
                delta_phi2=(2*pi)-delta_phi2
              result["Deltaphi_lp"]=delta_phi1
              result["Deltaphi_lm"]=delta_phi2
              result["Eta_lgm"]=lm[0].eta()
              result["Eta_lrm"]=lrecneg.eta()
              result["Eta_lgp"]=lp[0].eta()
              result["Eta_lrp"]=lrecpos.eta()
              result["DeltaEta_lp"]=lp[0].eta()-lrecpos.eta()
              result["DeltaEta_lm"]=lm[0].eta()-lrecneg.eta()

              result["PtInv_lgp"]=1./lp[0].pt()
              result["PtInv_lgm"]=1./lm[0].pt()
              result["PtInv_lrp"]=1./lrecpos.pt()
              result["PtInv_lrm"]=1./lrecneg.pt()
              result["DeltaPtInv_lp"]=1./lp[0].pt()-1./lrecpos.pt()
              result["DeltaPtInv_lm"]=1./lm[0].pt()-1./lrecneg.pt()

      # that method returns the best jet pair. When only one is btagged, it is the first one.
      # when two bjets are present, these are the two.
      # later on, variables are refering to b-jets, even if some are light jets

      #Then Fill ME inputs related to jets and if MC event and matching jet rec-gen fill info for TF
      #both jets should be matched in order to fill the TF info
      if not bestZcandidate is None:
        dijet = findDijetPair(jets, bestZcandidate, self.btagging)
        if not dijet[0] is None:
          b1 = self._JECuncertainty.jet(dijet[0])
	  jetPt = b1.Pt()
          bNNCorr1 = ROOT.TLorentzVector(0,0,0,0)#4-vec first NNcorr bjet

          result["bjet1pt"] = jetPt
          result["bjet1etapm"] = dijet[0].eta()
          result["bjet1phi"] = dijet[0].phi()
          result["bjet1mass"] = dijet[0].mass()
	  corrDijet0 = 1.


        if not dijet[1] is None:
          b2 = self._JECuncertainty.jet(dijet[1])
	  jetPt = b2.Pt()
          bNNCorr2 = ROOT.TLorentzVector(0,0,0,0)#4-vec second NNcorr bjet

          result["bjet2pt"] = jetPt
          result["bjet2etapm"] = dijet[1].eta()
          result["bjet2phi"] = dijet[1].phi()
          result["bjet2mass"] = dijet[1].mass()
	  corrDijet1 = 1.

          if bq and  bbarq :
            dR1= Delta(dijet[0],bq[0])
            dR2= Delta(dijet[1],bbarq[0])
            dR3= Delta(dijet[0],bbarq[0])
            dR4= Delta(dijet[1], bq[0])


                                                            
            dRmatch=0.3
	    #print "dR1=", dR1, " dR2=", dR2, " dR3=", dR3, " dR4=", dR4
            if  bq and bbarq:
              #print "AFTER IF: dR1=", dR1, " dR2=", dR2, " dR3=", dR3, " dR4=", dR4
              if dR1<dRmatch and dR2<dRmatch and dR1<dR4 and dR2<dR3:
	        result["FilledJetTF"]=1
                result["E_b"]=bq[0].energy()
                result["E_jb"]=dijet[0].energy()
                result["NNCorrE_jb"]=dijet[0].energy()*corrDijet0
                result["E_ab"]=bbarq[0].energy()
                result["E_jab"]=dijet[1].energy()
                result["NNCorrE_jab"]=dijet[1].energy()*corrDijet1
                result["DeltaE_ajet"]=bbarq[0].energy()-dijet[1].energy()
                result["DeltaE_jet"]=bq[0].energy()-dijet[0].energy()
                result["DeltaNNCorrE_ajet"]=bbarq[0].energy()-dijet[1].energy()*corrDijet1
                result["DeltaNNCorrE_jet"]=bq[0].energy()-dijet[0].energy()*corrDijet0
                result["phi_b"]=bq[0].phi()
                result["phi_jb"]=dijet[0].phi()
                result["phi_ab"]=bbarq[0].phi()
                result["phi_jab"]=dijet[1].phi()
                delta_phi1=bbarq[0].phi()-dijet[1].phi()
                delta_phi2=bq[0].phi()-dijet[0].phi()
                if delta_phi1>pi:
                  delta_phi1=(2*pi)-delta_phi1
                if delta_phi2>pi:
                  delta_phi2=(2*pi)-delta_phi2
                result["Deltaphi_ajet"]=delta_phi1
                result["Deltaphi_jet"]=delta_phi2
                result["Eta_b"]=bq[0].eta()
                result["Eta_jb"]=dijet[0].eta()
                result["Eta_ab"]=bbarq[0].eta()
                result["Eta_jab"]=dijet[1].eta()
                result["DeltaEta_ajet"]=bbarq[0].eta()-dijet[1].eta()
                result["DeltaEta_jet"]=bq[0].eta()-dijet[0].eta()
    
              if dR4<dRmatch and dR3<dRmatch and dR4<dR1 and dR3<dR2:      
	        result["FilledJetTF"]=1
                result["E_b"]=bq[0].energy()
                result["E_jb"]=dijet[1].energy()
                result["NNCorrE_jb"]=dijet[1].energy()*corrDijet1
                result["E_ab"]=bbarq[0].energy()
                result["E_jab"]=dijet[0].energy()
                result["NNCorrE_jab"]=dijet[0].energy()*corrDijet0
                result["DeltaE_ajet"]=bbarq[0].energy()-dijet[0].energy()
                result["DeltaE_jet"]=bq[0].energy()-dijet[1].energy()
                result["DeltaNNCorrE_ajet"]=bbarq[0].energy()-dijet[0].energy()*corrDijet0
                result["DeltaNNCorrE_jet"]=bq[0].energy()-dijet[1].energy()*corrDijet1
                result["phi_b"]=bq[0].phi()
                result["phi_jb"]=dijet[1].phi()
                result["phi_ab"]=bbarq[0].phi()
                result["phi_jab"]=dijet[0].phi()
                delta_phi1=bbarq[0].phi()-dijet[0].phi()
                delta_phi2=bq[0].phi()-dijet[1].phi()
                if delta_phi1>pi:
                  delta_phi1=(2*pi)-delta_phi1
                if delta_phi2>pi:
                    delta_phi2=(2*pi)-delta_phi2
                result["Deltaphi_ajet"]=delta_phi1
                result["Deltaphi_jet"]=delta_phi2
                result["Eta_b"]=bq[0].eta()
                result["Eta_jb"]=dijet[1].eta()
                result["Eta_ab"]=bbarq[0].eta()
                result["Eta_jab"]=dijet[0].eta()
                result["DeltaEta_ajet"]=bbarq[0].eta()-dijet[0].eta()
                result["DeltaEta_jet"]=bq[0].eta()-dijet[1].eta()
      
      return result

def runTest(path='../testfiles/'):
  controlPlots = MatrixElementControlPlots(muChannel=True)
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
  controlPlots.beginJob()
  i = 0
  for event in events:
    if i%1000==0 : print "Processing... event ", i
    controlPlots.processEvent(event)
    i += 1
  controlPlots.endJob()

def Delta(par1,par2):
  delta_phi=abs(par2.phi()-par1.phi())
  if delta_phi>pi:
    delta_phi=(2*pi)-delta_phi;
  delta=sqrt((delta_phi)**2 + (par1.eta()-par2.eta())**2)
  return delta
