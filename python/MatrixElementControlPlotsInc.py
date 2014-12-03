import ROOT
import array
from math import sqrt, pi
from PatAnalysis.BaseControlPlots import BaseControlPlots
from PatAnalysis.EventSelection import *
import os
confCfg = os.environ["PatAnalysisCfg"]
if confCfg : from UserCode.zbb_louvain.PatAnalysis.CPconfig import configuration
else : from zbbConfig import configuration

class MatrixElementControlPlotsInc(BaseControlPlots):
    """A class to create control plots for event selection"""

    readerREG = ROOT.TMVA.Reader("!Color:!Silent")
    var_jetBtag = array.array('f', [0])
    var_jetPt = array.array('f', [0])
    var_jetEta = array.array('f', [0])
    var_jetMetPhi = array.array('f', [0])
    var_jetChf = array.array('f', [0])
    var_jetPhf = array.array('f', [0])
    var_jetNhf = array.array('f', [0])
    var_jetElf = array.array('f', [0])
    var_jetMuf = array.array('f', [0])
    var_jetPtD = array.array('f', [0])
    var_jetVtxPt = array.array('f', [0])
    var_jetVtx3dL = array.array('f', [0])
    var_jetVtx3deL = array.array('f', [0])
    var_met = array.array('f', [0])
    var_rho = array.array('f', [0])

    def __init__(self, dir=None, dataset=None, purpose="matrixElements", mode="plots", prejets=""):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="me", dataset=dataset, mode=mode)
      self.prejets = prejets
    
    def beginJob(self):
      # declare histograms
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
      self.add("mu3pt","third muon Pt",1,0,99999.)
      self.add("mu3etapm","third muon Eta",50,-2.5,2.5)
      self.add("mu3phi","third muon phi",30,-4,4)
      self.add("mu3mass","third muon mass",1,0,99999.)
      self.add("mu3charge","third muon charge",3,-1.5,1.5)
      self.add("mu4pt","fourth muon Pt",1,0,99999.)
      self.add("mu4etapm","fourth muon Eta",50,-2.5,2.5)
      self.add("mu4phi","fourth muon phi",30,-4,4)
      self.add("mu4mass","fourth muon mass",1,0,99999.)
      self.add("mu4charge","fourth muon charge",3,-1.5,1.5)          
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
      self.add("el3pt","third electron Pt",1,0,99999.)
      self.add("el3etapm","third electron Eta",50,-2.5,2.5)
      self.add("el3phi","third electron phi",30,-4,4)
      self.add("el3mass","third electron mass",1,0,99999.)
      self.add("el3charge","third electron charge",3,-1.5,1.5)
      self.add("el4pt","fourth electron Pt",1,0,99999.)
      self.add("el4etapm","fourth electron Eta",50,-2.5,2.5)
      self.add("el4phi","fourth electron phi",30,-4,4)
      self.add("el4mass","fourth electron mass",1,0,99999.)
      self.add("el4charge","fourth electron charge",3,-1.5,1.5)      
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

      #Initialize Reader for NN Correction
      if configuration.doNNJetRegression == True:
        self.readerREG.AddVariable("jetBtag"   ,self.var_jetBtag)
        self.readerREG.AddVariable("jetPt"     ,self.var_jetPt)
        self.readerREG.AddVariable("jetEta"    ,self.var_jetEta)
        self.readerREG.AddVariable("jetMetPhi" ,self.var_jetMetPhi)
        self.readerREG.AddVariable("jetChf"    ,self.var_jetChf)
        self.readerREG.AddVariable("jetPhf"    ,self.var_jetPhf)
        self.readerREG.AddVariable("jetNhf"    ,self.var_jetNhf)
        self.readerREG.AddVariable("jetElf"    ,self.var_jetElf)
        self.readerREG.AddVariable("jetMuf"    ,self.var_jetMuf)
        self.readerREG.AddVariable("jetPtD"    ,self.var_jetPtD)
        self.readerREG.AddVariable("jetVtxPt"  ,self.var_jetVtxPt)
        self.readerREG.AddVariable("jetVtx3dL" ,self.var_jetVtx3dL)
        self.readerREG.AddVariable("jetVtx3deL",self.var_jetVtx3deL)
        self.readerREG.AddVariable("met"       ,self.var_met)
        self.readerREG.AddVariable("rho"       ,self.var_rho)
        self.readerREG.BookMVA("BDT_REG","/nfs/user/llbb/TMVAregression/factoryJetReg_BDT.weights.xml")
      
    def process(self, event):
      """MatrixElementControlPlotsInc"""
      result = { }
      # in all cases, we need a reco Z
      #bestZcandidate = event.bestZcandidate
      leptons = event.leptonsPair
      if leptons is None:
        return result
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
      if not event.object().event().eventAuxiliary().isRealData():
        genparts = event.genParticles
	for partg in genparts:
	  #if partg.status() ==3: print "st3 partid=",partg.pdgId()
	  #if partg.status() ==2: print "st2 partid=",partg.pdgId()
          if partg.pdgId()==5  and partg.status()==3:
            bq+=[partg]
	    #print "found b"
          if partg.pdgId()==-5 and partg.status()==3:
            bbarq+=[partg]
	    #print "found bbar"
            
          #If mu channel search for dimuon pair, if el channel search for dielectron pair
          if leptons[0].isMuon() and partg.pdgId()==13 and partg.status()==3:
            lm+=[partg]
	    #print "found lm"
          elif leptons[0].isMuon() and partg.pdgId()==-13 and partg.status()==3:
            lp+=[partg]
	    #print "found lp"
          elif leptons[0].isElectron() and partg.pdgId()==11 and partg.status()==3:
            lm+=[partg]
	    #print "found lm"
          elif leptons[0].isElectron() and partg.pdgId()==-11 and partg.status()==3:
            lp+=[partg]
	    #print "found lp"

      #Then fill ME inputs related to MET
      result["MET"] = event.MET[0].pt()
      result["METphi"] = event.MET[0].phi()

      #Then Fill ME inputs related to leptons and if MC event and matching lep rec-gen fill info for TFz
      #both leptons should be matched in order to fill the TF info
#      if not leptons is None:
#        lrecpos = None
#	lrecneg = None
#	if leptons[0].isMuon():
#          mu1 = leptons[0]
#          mu2 = leptons[1]
#          if mu1.pt() < mu2.pt():
#            mu1 = leptons[1]
#            mu2 = leptons[0]
#          lvmu1 = ROOT.TLorentzVector(mu1.px(),mu1.py(),mu1.pz(),mu1.energy())
#          lvmu2 = ROOT.TLorentzVector(mu2.px(),mu2.py(),mu2.pz(),mu2.energy())
#          result["mu1pt"] = mu1.pt()
#          result["mu2pt"] = mu2.pt()
#          result["mu1etapm"] = mu1.eta()
#          result["mu2etapm"] = mu2.eta()
#          result["mu1phi"] = mu1.phi()
#          result["mu2phi"] = mu2.phi()
#          result["mu1mass"] = mu1.mass()
#          result["mu2mass"] = mu2.mass()
#          result["mu1charge"] = mu1.charge()
#          result["mu2charge"] = mu2.charge()
#          if mu1.charge() > 0 and mu2.charge() < 0:
#            lrecpos = mu1
#            lrecneg = mu2
#          elif mu2.charge() > 0 and mu1.charge() < 0:
#            lrecpos = mu2
#            lrecneg = mu1
#        if leptons[0].isElectron() :
#          ele1 = leptons[0]
#          ele2 = leptons[1]
#          if ele1.pt() < ele2.pt():
#            ele1 = leptons[1]
#            ele2 = leptons[0]
#          lvele1 = ROOT.TLorentzVector(ele1.px(),ele1.py(),ele1.pz(),ele1.energy())
#          lvele2 = ROOT.TLorentzVector(ele2.px(),ele2.py(),ele2.pz(),ele2.energy())
#          result["el1pt"] = ele1.pt()
#          result["el2pt"] = ele2.pt()
#          result["el1etapm"] = ele1.eta()
#          result["el2etapm"] = ele2.eta()
#          result["el1phi"] = ele1.phi()
#          result["el2phi"] = ele2.phi()
#          result["el1mass"] = ele1.mass()
#          result["el2mass"] = ele2.mass()
#          result["el1charge"] = ele1.charge()
#          result["el2charge"] = ele2.charge()
#          if ele1.charge() > 0 and ele2.charge() < 0:
#            lrecpos = ele1
#            lrecneg = ele2
#          elif ele2.charge() > 0 and ele1.charge() < 0:
#            lrecpos = ele2
#            lrecneg = ele1
    
      if not leptons is None : 
        nlept= len(leptons)
        lept1=leptons[0]
        lept2=leptons[1]
	lept3= None
	lept4= None
	if nlept > 2: lept3=leptons[2]
	if nlept > 3: lept4=leptons[3]
 	l1 = ROOT.TLorentzVector(lept1.px(),lept1.py(),lept1.pz(),lept1.energy())
        l2 = ROOT.TLorentzVector(lept2.px(),lept2.py(),lept2.pz(),lept2.energy())
        if lept1.charge() > 0 and lept2.charge() < 0:
            lrecpos = lept1
            lrecneg = lept2
        elif lept2.charge() > 0 and lept1.charge() < 0:	
            lrecpos = lept2
            lrecneg = lept1	
	    
	if lept1.isMuon():
          result["mu1pt"] = lept1.pt()
          result["mu1etapm"] = lept1.eta()
          result["mu1charge"] = lept1.charge()
	  result["mu1phi"] = lept1.phi()
	  result["mu1mass"] = lept1.mass()
	elif lept1.isElectron():
          result["el1pt"] = lept1.pt()
          result["el1etapm"] = lept1.eta()
          result["el1charge"] = lept1.charge()
	  result["el1phi"] = lept1.phi()
	  result["el1mass"] = lept1.mass()
	  
	if lept2.isMuon():
          result["mu2pt"] = lept2.pt()
          result["mu2etapm"] = lept2.eta()
          result["mu2charge"] = lept2.charge()
	  result["mu2phi"] = lept2.phi()
	  result["mu2mass"] = lept2.mass()
	elif lept2.isElectron():
          result["el2pt"] = lept2.pt()
          result["el2etapm"] = lept2.eta()
          result["el2charge"] = lept2.charge()
	  result["el2phi"] = lept2.phi()
	  result["el2mass"] = lept2.mass()
	if lept3 is not None:
	  if lept3.isMuon():	  
            result["mu3pt"] = lept3.pt()
            result["mu3etapm"] = lept3.eta()
            result["mu3charge"] = lept3.charge()
	    result["mu3phi"] = lept3.phi()
	    result["mu3mass"] = lept3.mass()
	  elif lept3.isElectron():	  
            result["el3pt"] = lept3.pt()
            result["el3etapm"] = lept3.eta()
            result["el3charge"] = lept3.charge()
	    result["el3phi"] = lept3.phi()
	    result["el3mass"] = lept3.mass()	  
	  if lept4 is not None:	  
	    if lept4.isMuon():	  
              result["mu4pt"] = lept4.pt()
              result["mu4etapm"] = lept4.eta()
              result["mu4charge"] = lept4.charge()
	      result["mu4phi"] = lept4.phi()
	      result["mu4mass"] = lept4.mass()
	    elif lept4.isElectron():	  
              result["el4pt"] = lept4.pt()
              result["el4etapm"] = lept4.eta()
              result["el4charge"] = lept4.charge()	  
              result["el4phi"] = lept4.phi()
              result["el4mass"] = lept4.mass()
        
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
      if not leptons is None:
	dijet = getattr(event,"di"+self.prejets+"jet_all")
        if not dijet[0] is None:
          b1 = ROOT.TLorentzVector(dijet[0].px(),dijet[0].py(),dijet[0].pz(),dijet[0].energy()) #self._JECuncertainty.jet(dijet[0])
	  jetPt = b1.Pt()
          bNNCorr1 = ROOT.TLorentzVector(0,0,0,0)#4-vec first NNcorr bjet

          result["bjet1pt"] = jetPt
          result["bjet1etapm"] = dijet[0].eta()
          result["bjet1phi"] = dijet[0].phi()
          result["bjet1mass"] = dijet[0].mass()
	  corrDijet0 = 1.
          if configuration.doNNJetRegression == True:
            self.var_jetBtag[0] = dijet[0].bDiscriminator("combinedSecondaryVertexBJetTags")
            self.var_jetPt[0] = jetPt
            self.var_jetEta[0] = dijet[0].eta()
            self.var_jetMetPhi[0] = abs(dijet[0].phi()-event.MET[0].phi())
            self.var_jetChf[0] = dijet[0].chargedHadronEnergyFraction()
            self.var_jetPhf[0] = dijet[0].photonEnergyFraction()
            self.var_jetNhf[0] = dijet[0].neutralHadronEnergyFraction()
            self.var_jetElf[0] = dijet[0].electronEnergyFraction()
            self.var_jetMuf[0] = dijet[0].muonEnergyFraction()
            self.var_jetPtD[0] = jetPtD(dijet[0])
            self.var_jetVtxPt[0] = jetVtxPt(dijet[0])
            self.var_jetVtx3dL[0] = jetVtx3dL(dijet[0])
            self.var_jetVtx3deL[0] = jetVtx3deL(dijet[0])
            self.var_met[0] = event.MET[0].pt()
            self.var_rho[0] = event.rho[0]
            corrDijet0 = self.readerREG.EvaluateRegression("BDT_REG")[0]/jetPt
#            print "Corr1ME =",corr," evt=",event.event()
#	    print " var =",self.var_jetBtag[0]
#            print " var =",self.var_jetPt[0]
#            print " var =",self.var_jetEta[0]
#	    print " var =",self.var_jetMetPhi[0]
#	    print " var =",self.var_jetChf[0]
#	    print " var =",self.var_jetPhf[0]
#	    print " var =",self.var_jetNhf[0]
#	    print " var =",self.var_jetElf[0]
#	    print " var =",self.var_jetMuf[0]
#	    print " var =",self.var_jetPtD[0]
#	    print " var =",self.var_jetVtxPt[0]
#	    print " var =",self.var_jetVtx3dL[0]
#	    print " var =",self.var_jetVtx3deL[0]
#	    print " var =",self.var_met[0]
#	    print " var =",self.var_rho[0]
          bNNCorr1.SetPtEtaPhiM(jetPt*corrDijet0, dijet[0].eta(), dijet[0].phi(), dijet[0].mass()*corrDijet0)
          result["bjet1ptNNCorr"] = jetPt*corrDijet0
          result["bjet1massNNCorr"] = dijet[0].mass()*corrDijet0

        if not dijet[1] is None:
          b2 = ROOT.TLorentzVector(dijet[1].px(),dijet[1].py(),dijet[1].pz(),dijet[1].energy()) #self._JECuncertainty.jet(dijet[1])
	  jetPt = b2.Pt()
          bNNCorr2 = ROOT.TLorentzVector(0,0,0,0)#4-vec second NNcorr bjet

          result["bjet2pt"] = jetPt
          result["bjet2etapm"] = dijet[1].eta()
          result["bjet2phi"] = dijet[1].phi()
          result["bjet2mass"] = dijet[1].mass()
	  corrDijet1 = 1.
          if configuration.doNNJetRegression == True:
            self.var_jetBtag[0] = dijet[1].bDiscriminator("combinedSecondaryVertexBJetTags")
            self.var_jetPt[0] = jetPt
            self.var_jetEta[0] = dijet[1].eta()
            self.var_jetMetPhi[0] = abs(dijet[1].phi()-event.MET[0].phi())
            self.var_jetChf[0] = dijet[1].chargedHadronEnergyFraction()
            self.var_jetPhf[0] = dijet[1].photonEnergyFraction()
            self.var_jetNhf[0] = dijet[1].neutralHadronEnergyFraction()
            self.var_jetElf[0] = dijet[1].electronEnergyFraction()
            self.var_jetMuf[0] = dijet[1].muonEnergyFraction()
            self.var_jetPtD[0] = jetPtD(dijet[1])
            self.var_jetVtxPt[0] = jetVtxPt(dijet[1])
            self.var_jetVtx3dL[0] = jetVtx3dL(dijet[1])
            self.var_jetVtx3deL[0] = jetVtx3deL(dijet[1])
            self.var_met[0] = event.MET[0].pt()
            self.var_rho[0] = event.rho[0]
            corrDijet1 = self.readerREG.EvaluateRegression("BDT_REG")[0]/jetPt
#            print "Corr2ME =",corr," evt=",event.event()
#	    print " var =",self.var_jetBtag[0]
#            print " var =",self.var_jetPt[0]
#            print " var =",self.var_jetEta[0]
#	    print " var =",self.var_jetMetPhi[0]
#	    print " var =",self.var_jetChf[0]
#	    print " var =",self.var_jetPhf[0]
#	    print " var =",self.var_jetNhf[0]
#	    print " var =",self.var_jetElf[0]
#	    print " var =",self.var_jetMuf[0]
#	    print " var =",self.var_jetPtD[0]
#	    print " var =",self.var_jetVtxPt[0]
#	    print " var =",self.var_jetVtx3dL[0]
#	    print " var =",self.var_jetVtx3deL[0]
#	    print " var =",self.var_met[0]
#	    print " var =",self.var_rho[0]
          bNNCorr2.SetPtEtaPhiM(jetPt*corrDijet1, dijet[1].eta(), dijet[1].phi(), dijet[1].mass()*corrDijet1)
          result["bjet2ptNNCorr"] = jetPt*corrDijet1
          result["bjet2massNNCorr"] = dijet[1].mass()*corrDijet1
          result["bbM"] = (b1 + b2).M()
	  result["bbNNCorrM"] = (bNNCorr1 + bNNCorr2).M()	

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

def Delta(par1,par2):
  delta_phi=abs(par2.phi()-par1.phi())
  if delta_phi>pi:
    delta_phi=(2*pi)-delta_phi;
  delta=sqrt((delta_phi)**2 + (par1.eta()-par2.eta())**2)
  return delta

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], MatrixElementControlPlotsInc())

