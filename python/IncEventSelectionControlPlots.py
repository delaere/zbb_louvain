import ROOT
import array
from PatAnalysis.BaseControlPlots import BaseControlPlots
from ObjectSelection import *
from JetCorrectionUncertainty import JetCorrectionUncertaintyProxy
import os
confCfg = os.environ["PatAnalysisCfg"]
if confCfg : from UserCode.zbb_louvain.PatAnalysis.CPconfig import configuration
else : from zbbConfig import configuration

class IncEventSelectionControlPlots(BaseControlPlots):
    """A class to create control plots for event selection"""

    def __init__(self, dir=None, dataset=None,purpose="eventSelection", mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      if not configuration.RDSasCP : purpose="eventSelection"
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)
      
    def beginJob(self):
      # declare histograms
      self.add("run","Run number",50000,160000,210000)
      self.add("event","Event number",1000,0,5e9)
      self.add("ls","Lumi section",2000,0,2000)      
      self.add("triggerSelection","triggerSelection ",2,0,2)
      self.add("triggerBits","trigger bits",20,0,20)
      self.add("triggerDouble","Double trigger",2,0,2)
      self.add("triggerSingle","Single trigger",2,0,2)
      self.add("triggerEMU","E-MU trigger",2,0,2)
      self.add("zmassMu","zmassMu",10000,0,1000)
      self.add("bestzmassMu","bestzmassMu",10000,0,1000)
      self.add("zmassEle","zmassEle",10000,0,1000)
      self.add("bestzmassEle","bestzmassEle",10000,0,1000)
      self.add("zptMu","zptMu",1000,0,1000)
      self.add("bestzptMu","bestzptMu",1000,0,1000)
      self.add("zptEle","zptEle",1000,0,1000)
      self.add("bestzptEle","bestzptEle",1000,0,1000)
      self.add("scaldptZbj1","scaldptZbj1",1000,-500,500)
      self.add("drZbj1","distance between Z and leading jet",100,0,5)
      self.add("dphiZbj1","dphiZbj1",40,-3.15,3.15)
      self.add("scaldptZbb","scaldptZbb",1000,-500,500)
      self.add("dphiZbb","dphiZbb",40,0,3.15)
      self.add("drZbb","drZbb",100,0,5)
      self.add("dijetM","b bbar invariant mass",3000,0,3000)
      self.add("dijetPt","b bbar Pt",1000,0,1000)
      self.add("dijetdR","#Delta R (b bbar)",100,0,5)
      self.add("dijetSVdR","#Delta R (b bbar SV)",100,0,5)
      self.add("dphidijetMET","#Delta #phi (b bbar MET)",40,0,3.15)
      self.add("ZbM","Zb invariant mass",1000,0,1000)
      self.add("ZbPt","Zb Pt",500,0,500)
      self.add("ZbbM","Zbb invariant mass",1000,0,1000)
      self.add("ZbbPt","Zbb Pt",500,0,500)
      self.add("mu1pt","leading muon Pt",500,0,500)
      self.add("mu2pt","subleading muon Pt",500,0,500)
      self.add("mu1eta","leading muon Eta",25,0,2.5)
      self.add("mu2eta","subleading muon Eta",25,0,2.5)
      self.add("mu1etapm","leading muon Eta",50,-2.5,2.5)
      self.add("mu2etapm","subleading muon Eta",50,-2.5,2.5)
      self.add("drllMu","drllMu",100,0,5)
      self.add("el1pt","leading electron Pt",1000,0,1000)
      self.add("el2pt","subleading electron Pt",1000,0,1000)
      self.add("el1eta","leading electron Eta",25,0,2.5)
      self.add("el2eta","subleading electron Eta",25,0,2.5)
      self.add("el1etapm","leading electron Eta",50,-2.5,2.5)
      self.add("el2etapm","subleading electron Eta",50,-2.5,2.5)
      self.add("drllEle","drllEle",100,0,5)
      
      #inclusive search
      self.add("mu1pt_inc","leading muon Pt",1000,0,1000)
      self.add("mu2pt_inc","subleading muon Pt",1000,0,1000)
      self.add("mu1eta_inc","leading muon Eta",25,0,2.5)
      self.add("mu2eta_inc","subleading muon Eta",25,0,2.5)
      self.add("mu1etapm_inc","leading muon Eta",50,-2.5,2.5)
      self.add("mu2etapm_inc","subleading muon Eta",50,-2.5,2.5)
      self.add("mu1charge_inc","mu1 charge",5,-2.5,2.5)
      self.add("mu2charge_inc","mu2 charge",5,-2.5,2.5)
      self.add("mu3pt_inc","third muon Pt",1000,0,1000)
      self.add("mu4pt_inc","fourth muon Pt",1000,0,1000)
      self.add("mu3eta_inc","third muon Eta",25,0,2.5)
      self.add("mu4eta_inc","fourth muon Eta",25,0,2.5)
      self.add("mu3etapm_inc","third muon Eta",50,-2.5,2.5)
      self.add("mu4etapm_inc","fourth muon Eta",50,-2.5,2.5)
      self.add("mu3charge_inc","mu3 charge",5,-2.5,2.5)
      self.add("mu4charge_inc","mu4 charge",5,-2.5,2.5)      
      self.add("el1pt_inc","leading electron Pt",1000,0,1000)
      self.add("el2pt_inc","subleading electron Pt",1000,0,1000)
      self.add("el1eta_inc","leading electron Eta",25,0,2.5)
      self.add("el2eta_inc","subleading electron Eta",25,0,2.5)
      self.add("el1etapm_inc","leading electron Eta",50,-2.5,2.5)
      self.add("el2etapm_inc","subleading electron Eta",50,-2.5,2.5)      
      self.add("el1charge_inc","el1 charge",5,-2.5,2.5)
      self.add("el2charge_inc","el2 charge",5,-2.5,2.5)
      self.add("el3pt_inc","third electron Pt",1000,0,1000)
      self.add("el4pt_inc","fourth electron Pt",1000,0,1000)
      self.add("el3eta_inc","third electron Eta",25,0,2.5)
      self.add("el4eta_inc","fourth electron Eta",25,0,2.5)
      self.add("el3etapm_inc","third electron Eta",50,-2.5,2.5)
      self.add("el4etapm_inc","fourth electron Eta",50,-2.5,2.5)      
      self.add("el3charge_inc","el3 charge",5,-2.5,2.5)
      self.add("el4charge_inc","el4 charge",5,-2.5,2.5)     
      self.add("dilepchargesum_inc","Lepton1 charge + Lepton 2 charge",5,-2.5,2.5)
      self.add("dilepM_inc","dilepM_inc",1000,0,1000)
      self.add("dilepPt_inc","dilepPt_inc",1000,0,1000)
      self.add("drll_inc","drll_inc",50,0,5)
      self.add("dphill_inc","dphill_inc",50,0,3.15)
      self.add("dijetM_inc","b bbar invariant mass",1000,0,2000)
      self.add("dijetPt_inc","b bbar Pt",1000,0,2000)
      self.add("dijetdR_inc","#Delta R (b bbar)",50,0,5)
      self.add("dijetSVdR_inc","#Delta R (b bbar SV)",100,0,5)
      self.add("dphidijetMET_inc","#Delta #phi (b bbar MET)",40,-3.15,3.15)      
      self.add("MET_inc","Missing transverse energy",1000,0,2000)
      self.add("METsignificance_inc","missing transverse energy significance",1000,0,500)
      self.add("llbbM_inc","llbb invariant mass",4000,0,2000)
      self.add("llbbPt_inc","llbb Pt",1000,0,2000)
      self.add("drllbb_inc","drbbll_inc",50,0,5)           
      self.add("nlept_inc","number of leptons",5,0,5)
   
      
	      

    def process(self, event):
      """eventSelectionControlPlots"""
      result = { }
      if event.object().event().eventAuxiliary().isRealData():
        checkTrigger = True
        configuration.JERfactor = 0
        configuration.JESfactor = 0
      else:
        checkTrigger = False
      ## trigger
      result["triggerSelection"] = checkTrigger==False or event.isTriggerOK 
      #result["triggerBits"] = [index for index,trigger in enumerate(selectedTriggers(event.triggerInfo)) if trigger==1]
      triggerList = []
      paths = event.triggerInfo.acceptedPaths()

      triggers = []
      SingleTrig = 0
      DoubleTrig = 0
      EMUTrig    = 0
      for i in range(paths.size()) :
          name = paths[i].name()
          #print name
          for trig_name in ["HLT_Mu17_Mu8","HLT_Mu17_TkMu8","HLT_Mu13_Mu8","HLT_IsoMu24_v","HLT_Mu8_Ele17","HLT_Mu17_Ele8","HLT_Mu30_Ele30","HLT_DoubleMu5_Ele8","HLT_DoubleMu8_Ele8","HLT_Mu8_DoubleEle8","HLT_Mu8_Ele8","HLT_Mu7_Ele7"] :
              if name.find(trig_name)>-1 : triggers.append(trig_name)

      if paths.size()>0 : triggerList.append(0)
      if "HLT_Mu17_Mu8" in triggers or "HLT_Mu17_TkMu8" in triggers :
          triggerList.append(1)
          DoubleTrig = 1
      if "HLT_Mu17_Mu8" in triggers : triggerList.append(2)
      if "HLT_Mu17_TkMu8" in triggers : triggerList.append(3)
      if len(triggerList)==1 :
          if "HLT_Mu13_Mu8" in triggers : triggerList.append(4)
          if "HLT_IsoMu24_v" in triggers : triggerList.append(5)
      if "HLT_IsoMu24_v" in triggers : SingleTrig=1
      if len(triggers)==0 : triggerList.append(6)
      if len(triggerList)==1 or len(triggerList)>4 : print "error", len(triggerList)
      
      if "HLT_Mu8_Ele17" in triggers or "HLT_Mu17_Ele8" in triggers or "HLT_Mu30_Ele30" in triggers or "HLT_DoubleMu5_Ele8" in triggers or "HLT_DoubleMu8_Ele8" in triggers or "HLT_Mu8_DoubleEle8" in triggers or "HLT_Mu8_Ele8" in triggers or "HLT_Mu7_Ele7" in triggers : 
        EMUTrig=1
      result["triggerBits"] = triggerList
      result["triggerSingle"] = SingleTrig
      result["triggerDouble"] = DoubleTrig
      result["triggerEMU"] = EMUTrig
      result["run"] = event.run()
      result["event"] = event.event()
      result["ls"] = event.lumi()
      ## Z boson
      result["zmassMu"] = [ ]
      result["zptMu"] = [ ]
      for z in event.Zmumu:
        result["zmassMu"].append(z.mass())
        result["zptMu"].append(z.pt())
      result["zmassEle"] = [ ]
      result["zptEle"] = [ ]
      for z in event.Zelel:
        result["zmassEle"].append(z.mass())
        result["zptEle"].append(z.pt())
	
      bestZcandidate = event.bestZcandidate
      #bestDileptcandidate = event.bestDiLeptCandidate
      leptons = event.leptonsPair
      #if we have 2 lept. passing sanity cut, trigger matching and vertex association (so not coming from Z necessairly)
      nlept = 0
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
	mass=(l1+l2).M()

        result["nlept_inc"] =nlept	
        result["dilepM_inc"] =mass	
        result["dilepPt_inc"] =(l1+l2).Pt()	
	result["drll_inc"] = l1.DeltaR(l2)  
	result["dphill_inc"] = abs(l1.DeltaPhi(l2))  
	result["dilepchargesum_inc"] = lept1.charge() + lept2.charge()
	if lept1.isMuon():
          result["mu1pt_inc"] = lept1.pt()
          result["mu1etapm_inc"] = lept1.eta()
          result["mu1eta_inc"] = abs(lept1.eta())
          result["mu1charge_inc"] = lept1.charge()
	elif lept1.isElectron():
          result["el1pt_inc"] = lept1.pt()
          result["el1etapm_inc"] = lept1.eta()
          result["el1eta_inc"] = abs(lept1.eta())	  
          result["el1charge_inc"] = lept1.charge()
	if lept2.isMuon():
          result["mu2pt_inc"] = lept2.pt()
          result["mu2etapm_inc"] = lept2.eta()
          result["mu2eta_inc"] = abs(lept2.eta())	    
          result["mu2charge_inc"] = lept2.charge()
	elif lept2.isElectron():
          result["el2pt_inc"] = lept2.pt()
          result["el2etapm_inc"] = lept2.eta()
          result["el2eta_inc"] = abs(lept2.eta())            
          result["el2charge_inc"] = lept2.charge()
	if lept3 is not None:
	  if lept3.isMuon():	  
            result["mu3pt_inc"] = lept3.pt()
            result["mu3etapm_inc"] = lept3.eta()
            result["mu3eta_inc"] = abs(lept3.eta())
            result["mu3charge_inc"] = lept3.charge()
	  elif lept3.isElectron():	  
            result["el3pt_inc"] = lept3.pt()
            result["el3etapm_inc"] = lept3.eta()
            result["el3eta_inc"] = abs(lept3.eta())
            result["el3charge_inc"] = lept3.charge()	  
	  if lept4 is not None:	  
	    if lept4.isMuon():	  
              result["mu4pt_inc"] = lept4.pt()
              result["mu4etapm_inc"] = lept4.eta()
              result["mu4eta_inc"] = abs(lept4.eta())
              result["mu4charge_inc"] = lept4.charge()
	    elif lept4.isElectron():	  
              result["el4pt_inc"] = lept4.pt()
              result["el4etapm_inc"] = lept4.eta()
              result["el4eta_inc"] = abs(lept4.eta())
              result["el4charge_inc"] = lept4.charge()	  
  	  

        dijet = event.dijet_all
        if not dijet[0] is None:
           b1 = ROOT.TLorentzVector(dijet[0].px(),dijet[0].py(),dijet[0].pz(),dijet[0].energy())
        if not dijet[1] is None:
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
	  ll=l1+l2
	  result["drllbb_inc"] = ll.DeltaR(bb)
	  met = event.MET     
          met4v = ROOT.TLorentzVector(met[0].px(),met[0].py(),met[0].pz(),met[0].energy())
	  llbb = l1+l2+bb
	  result["llbbM_inc"] = llbb.M()
	  result["llbbPt_inc"] = llbb.Pt()
          result["dijetM_inc"] = bb.M()
          result["dijetPt_inc"] = bb.Pt()
          result["dijetdR_inc"] = b1.DeltaR(b2)
          result["dijetSVdR_inc"] = svdr
	  result["dphidijetMET_inc"] = bb.DeltaPhi(met4v)
	  result["MET_inc"]= event.MET[0].pt()
	  result["METsignificance_inc"] = 0.
	  if event.MET[0].getSignificanceMatrix()(0,0)<1e10 and event.MET[0].getSignificanceMatrix()(1,1)<1e10: 
            result["METsignificance_inc"] = event.MET[0].significance()


      if bestZcandidate is not None:
        if bestZcandidate.daughter(0).isMuon():
          mu1 = bestZcandidate.daughter(0)
          mu2 = bestZcandidate.daughter(1)
          if mu1.pt() < mu2.pt():
            mu1 = bestZcandidate.daughter(1)
            mu2 = bestZcandidate.daughter(0)
          lvmu1 = ROOT.TLorentzVector(mu1.px(),mu1.py(),mu1.pz(),mu1.energy())
          lvmu2 = ROOT.TLorentzVector(mu2.px(),mu2.py(),mu2.pz(),mu2.energy())
          result["drllMu"] = lvmu1.DeltaR(lvmu2)
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
          lvele1 = ROOT.TLorentzVector(ele1.px(),ele1.py(),ele1.pz(),ele1.energy())
          lvele2 = ROOT.TLorentzVector(ele2.px(),ele2.py(),ele2.pz(),ele2.energy())
          result["drllEle"] = lvele1.DeltaR(lvele2)  
          result["bestzmassEle"] = bestZcandidate.mass()
          result["bestzptEle"] = bestZcandidate.pt()
          result["el1pt"] = ele1.pt()
          result["el2pt"] = ele2.pt()
          result["el1eta"] = abs(ele1.eta())
          result["el2eta"] = abs(ele2.eta())
          result["el1etapm"] = ele1.eta()
          result["el2etapm"] = ele2.eta()
	  
        dijet = event.dijet_all
        if not dijet[0] is None:
          z  = ROOT.TLorentzVector(bestZcandidate.px(),bestZcandidate.py(),bestZcandidate.pz(),bestZcandidate.energy())
          b1 = ROOT.TLorentzVector(dijet[0].px(),dijet[0].py(),dijet[0].pz(),dijet[0].energy())
          Zb = z+b1
          result["ZbM"] = Zb.M()
          result["ZbPt"] = Zb.Pt()
          result["scaldptZbj1"] = bestZcandidate.pt()-dijet[0].pt()
          result["dphiZbj1"] = abs(z.DeltaPhi(b1))
          result["drZbj1"] = z.DeltaR(b1)
        if not dijet[1] is None:
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
          met = event.MET
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

class IncJetControlPlots(BaseControlPlots):
    """A class to create control plots for lightjets and b-jets separately"""
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

    def __init__(self, dir=None, dataset=None,purpose="IncJet", mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)
      self._JECuncertainty = JetCorrectionUncertaintyProxy()

    def beginJob(self, btagging="CSV", WP=["M","L"], prejets=""):
      self.btagging=btagging
      self.WP=WP
      self.prejets=prejets
      #List of the variables related to jets in the oreder of plotting (from python 2.7 use of 'OrderedDict' can simplify this)
      self.varOrdering = ["pt", "pt_totunc", "eta", "etapm", "phi", "energy", "mass", "jetid", "Flavor", "npf", "nch", "Chf", "Nhf", "cef", "nef", "Phf", "Elf", "Muf", "SSVHEdisc", "SSVHPdisc", "CSVdisc", "JPdisc", "nVertHE", "nVertHP", "SVmass", "SVpT", "Vtx3dL", "Vtx3deL", "VtxPt", "PtD", "beta", "betaStar", "PUIdMva", "PUIdWP", "overlapmu", "overlapele"]
      #Definitions (title, bins, xmin, xmax) of the variables to be plotted
      dicoVar = {
          "pt" : ["Pt",1000,0,1000],
          "pt_totunc" : ["Pt total uncertainty",100,0,1],
          "eta" : ["Eta",25,0,2.5],
          "etapm" : ["Eta",50,-2.5,2.5],
          "phi" : ["Phi",25,-4,4],
          "energy" : ["energy",125,0,3000],
          "mass" : ["mass",125,0,500],
          "jetid" : ["Jet Id level (none, loose, medium, tight)",4,0,4],
          "Flavor" : ["Flavor (MC)",29,-6.5,22.5],
          "npf" : ["total multiplicity",50,0,50],
          "nch" : ["charged multiplicity",50,0,50],
          "Chf" : ["charged hadron energy fraction",100,0,1.5],
          "Nhf" : ["neutral hadron energy fraction",100,0,1.5],
          "cef" : ["charged EmEnergy fraction",101,0,1.01],
          "nef" : ["neutral EmEnergy fraction",101,0,1.01],
          "Phf" : ["photon energy fraction",100,0,1.5],
          "Elf" : ["electron energy fraction",100,0,1.5],
          "Muf" : ["muon energy fraction",100,0,1.5],
          "SSVHEdisc" : ["SSVHE discriminant",200,0,10],
          "SSVHPdisc" : ["SSVHP discriminant",200,0,10],
          "CSVdisc" : ["CSV discriminant",100,0,1],
          "JPdisc" : ["JP discriminant",100,0,2.5],
          "nVertHE" : ["Number of two-tracks vertices",5,-0.5,4.5],
          "nVertHP" : ["Number of three-tracks vertices",5,-0.5,4.5],
          "SVmass" : ["SV mass",20,0,5],
          "SVpT" : ["SV pT",100,0,200],
          "Vtx3dL" : ["secondary vertex 3d flight distance",100,0,16],
          "Vtx3deL" : ["secondary vertex 3d flight distance error",200,0,3],
          "VtxPt" : ["secondary vertex PT",100,0,270],
          "PtD" : ["constituentPt",100,0,1.5],
          "beta" : ["beta function",20,-1,1],
          "betaStar" : ["beta* function",20,-1,1],
          "PUIdMva" : ["PU id MVA",100,0,1],
          "PUIdWP" : ["PU id WP (0:no, 4:loose, 6:medium, 7:tight)",8,-0.5,7.5],
          "overlapmu" : ["jets overlaps with muons",2,0,2],
          "overlapele" : ["jets overlaps with electrons",2,0,2],
          }
      self.add("NlightJets","Number of light jets",10,0,10)
      self.add("NbJets","Number of b jets",6,0,6)
      self.njets = 5
      for ijet in range(0,self.njets):
          for var in self.varOrdering:
              self.add("jet"+str(ijet+1)+var,"Jet "+str(ijet+1)+dicoVar[var][0],dicoVar[var][1],dicoVar[var][2],dicoVar[var][3])
      self.nbjets = 4
      for ibjet in range(0,self.nbjets):
          for var in self.varOrdering:
              self.add("bjet"+str(ibjet+1)+var,"b-jet "+str(ibjet+1)+dicoVar[var][0],dicoVar[var][1],dicoVar[var][2],dicoVar[var][3])

    def process(self,event):
      """IncJetControlPlots"""
      result = {}
      # declare histograms
      nj=0
      nb=0
      goodJets = getattr(event,"good"+self.prejets+"Jets_all")
      for index,jet in enumerate(getattr(event,self.prejets+"jets")):
        jetPt = jet.pt()
        if goodJets[index]: 
		if isBJet(jet,self.WP[0],self.btagging): 
                    nb+=1
		    if nb<self.nbjets+1: 
			
			result["bjet"+str(nb)+"pt"] = jetPt
		        result["bjet"+str(nb)+"pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
		        result["bjet"+str(nb)+"eta"] = abs(jet.eta())
		        result["bjet"+str(nb)+"etapm"] = jet.eta()
		        result["bjet"+str(nb)+"phi"] = jet.phi()
		        result["bjet"+str(nb)+"energy"] = jet.energy()
		        result["bjet"+str(nb)+"mass"] = jet.mass()
		        result["bjet"+str(nb)+"Flavor"] = jet.partonFlavour()
		        if jetId(jet,"tight"): result["bjet"+str(nb)+"jetid"] = 3
		        elif jetId(jet,"medium"): result["bjet"+str(nb)+"jetid"] = 2
		        elif jetId(jet,"loose"): result["bjet"+str(nb)+"jetid"] = 1
		        else: result["bjet"+str(nb)+"jetid"] = 0
		        if jet.isPFJet():
		  	  result["bjet"+str(nb)+"npf"] = jet.numberOfDaughters()
		  	  result["bjet"+str(nb)+"nch"] = jet.chargedMultiplicity()
		  	  result["bjet"+str(nb)+"Chf"] = jet.chargedHadronEnergyFraction()
		  	  result["bjet"+str(nb)+"Nhf"] = jet.neutralHadronEnergyFraction()
		  	  result["bjet"+str(nb)+"nef"] = jet.neutralEmEnergyFraction()
		  	  result["bjet"+str(nb)+"cef"] = jet.chargedEmEnergyFraction()
		  	  result["bjet"+str(nb)+"Phf"] = jet.photonEnergyFraction()
		  	  result["bjet"+str(nb)+"Elf"] = jet.electronEnergyFraction()
		  	  result["bjet"+str(nb)+"Muf"] = jet.muonEnergyFraction()
		  	  result["bjet"+str(nb)+"PtD"] = jetPtD(jet)
		        result["bjet"+str(nb)+"Vtx3dL"] = jetVtx3dL(jet)
		        result["bjet"+str(nb)+"Vtx3deL"] = jetVtx3deL(jet)
		        result["bjet"+str(nb)+"VtxPt"] = jetVtxPt(jet)
		        result["bjet"+str(nb)+"SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
		        result["bjet"+str(nb)+"SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
		        bjetsvmass=-1
		        bjetsvpt=-1
			tISV = jet.tagInfoSecondaryVertex("secondaryVertex")
                        nHEvert = 0
                        nHPvert = 0
                        if tISV :
                             nHEvert = tISV.nVertices()
                             nHPvert = sum( tISV.nVertexTracks(v) >=3 for v in range(nHEvert))
		             if tISV.secondaryVertex(0) :
		  	  		bjetsvmass = tISV.secondaryVertex(0).p4().mass()
		  	  		bjetsvpt = tISV.secondaryVertex(0).p4().pt()
		        result["bjet"+str(nb)+"nVertHE"] = nHEvert
		        result["bjet"+str(nb)+"nVertHP"] = nHPvert
		        result["bjet"+str(nb)+"SVmass"] = bjetsvmass
		        result["bjet"+str(nb)+"SVpT"] = bjetsvpt
		        result["bjet"+str(nb)+"CSVdisc"] = jet.bDiscriminator("combinedSecondaryVertexBJetTags")
		        result["bjet"+str(nb)+"JPdisc"] = jet.bDiscriminator("jetProbabilityBJetTags")
		        result["bjet"+str(nb)+"beta"] = jet.userFloat("beta")
		        result["bjet"+str(nb)+"betaStar"] = jet.userFloat("betaStar")
		        result["bjet"+str(nb)+"PUIdMva"] = jet.userFloat("puJetMva")
		        result["bjet"+str(nb)+"PUIdWP"] = jet.userInt("puJetId")
		        result["bjet"+str(nb)+"overlapmu"] = jet.hasOverlaps("muons")
		        result["bjet"+str(nb)+"overlapele"] = jet.hasOverlaps("electrons")
		else :
			nj+=1
			if nj < self.njets+1 :
				result["jet"+str(nj)+"pt"] = jetPt
			        result["jet"+str(nj)+"pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
			        result["jet"+str(nj)+"eta"] = abs(jet.eta())
			        result["jet"+str(nj)+"etapm"] = jet.eta()
			        result["jet"+str(nj)+"phi"] = jet.phi()
			        result["jet"+str(nj)+"energy"] = jet.energy()
			        result["jet"+str(nj)+"mass"] = jet.mass()	    
			        if jetId(jet,"tight"): result["jet"+str(nj)+"jetid"] = 3
			        elif jetId(jet,"medium"): result["jet"+str(nj)+"jetid"] = 2
			        elif jetId(jet,"loose"): result["jet"+str(nj)+"jetid"] = 1
			        else: result["jet"+str(nj)+"jetid"] = 0
			        result["jet"+str(nj)+"Flavor"] = jet.partonFlavour()
			        if jet.isPFJet():
			            result["jet"+str(nj)+"npf"] = jet.numberOfDaughters()
			            result["jet"+str(nj)+"nch"] = jet.chargedMultiplicity()
			            result["jet"+str(nj)+"Chf"] = jet.chargedHadronEnergyFraction()
			            result["jet"+str(nj)+"Nhf"] = jet.neutralHadronEnergyFraction()
			            result["jet"+str(nj)+"nef"] = jet.neutralEmEnergyFraction()
			            result["jet"+str(nj)+"cef"] = jet.chargedEmEnergyFraction()
			            result["jet"+str(nj)+"Phf"] = jet.photonEnergyFraction()
			            result["jet"+str(nj)+"Elf"] = jet.electronEnergyFraction()
			            result["jet"+str(nj)+"Muf"] = jet.muonEnergyFraction()
			            result["jet"+str(nj)+"PtD"] = jetPtD(jet)
			        result["jet"+str(nj)+"Vtx3dL"] = jetVtx3dL(jet)
			        result["jet"+str(nj)+"Vtx3deL"] = jetVtx3deL(jet)
			        result["jet"+str(nj)+"VtxPt"] = jetVtxPt(jet)
			        result["jet"+str(nj)+"SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
			        result["jet"+str(nj)+"SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
				tISV = jet.tagInfoSecondaryVertex("secondaryVertex")
				nHEvert = 0
				nHPvert = 0
			        result["jet"+str(nj)+"nVertHE"] = nHEvert
			        result["jet"+str(nj)+"nVertHP"] = nHPvert
			        if tISV :
			            nHEvert = tISV.nVertices()
				    nHPvert = sum( tISV.nVertexTracks(v) >=3 for v in range(nHEvert))
			            if tISV.secondaryVertex(0) :
			                result["jet"+str(nj)+"SVmass"] = tISV.secondaryVertex(0).p4().mass()
			                result["jet"+str(nj)+"SVpT"] = tISV.secondaryVertex(0).p4().pt()
			        result["jet"+str(nj)+"CSVdisc"] = jet.bDiscriminator("combinedSecondaryVertexBJetTags")
			        result["jet"+str(nj)+"JPdisc"] = jet.bDiscriminator("jetProbabilityBJetTags")
			        result["jet"+str(nj)+"beta"] = jet.userFloat("beta")
			        result["jet"+str(nj)+"betaStar"] = jet.userFloat("betaStar")
			        result["jet"+str(nj)+"PUIdMva"] = jet.userFloat("puJetMva")
			        result["jet"+str(nj)+"PUIdWP"] = jet.userInt("puJetId")
			        result["jet"+str(nj)+"overlapmu"] = jet.hasOverlaps("muons")
			        result["jet"+str(nj)+"overlapele"] = jet.hasOverlaps("electrons")
		result["NlightJets"]=nj
		result["NbJets"]=nb
      return result			
			

class IncLepControlPlots(BaseControlPlots):
    """A class to create control plots for leptons inclusively"""

    def __init__(self, dir=None, dataset=None,purpose="IncLep", mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)

    def beginJob(self):
      #List of the variables related to leps in the oreder of plotting (from python 2.7 use of 'OrderedDict' can simplify this)
      self.varOrdering = ["pt","eta", "etapm", "phi", "energy", "isMuon", "isElectron"]
      #Definitions (title, bins, xmin, xmax) of the variables to be plotted
      dicoVar = {
          "pt" : ["Pt",1000,0,1000],
          "eta" : ["Eta",25,0,2.5],
          "etapm" : ["Eta",50,-2.5,2.5],
          "phi" : ["Phi",25,-4,4],
          "energy" : ["energy",125,0,3000],
          "isMuon" : ["isMuon",2,0,2],
          "isElectron" : ["isElectron",2,0,2],
          }
      self.add("Nel","Number of electrons",5,0,5)
      self.add("Nmu","Number of muons",5,0,5)
      self.nleps = 4
      for ilep in range(0,self.nleps):
          for var in self.varOrdering:
              self.add("lep"+str(ilep+1)+var,"Lep "+str(ilep+1)+dicoVar[var][0],dicoVar[var][1],dicoVar[var][2],dicoVar[var][3])

    def process(self,event):
      """IncLepControlPlots"""
      result = {}
      # declare histograms
      nel=0
      nmu=0
      goodLeps = event.leptonsPair
      if goodLeps is not None:
	      for index,lep in enumerate(goodLeps):
		if index < self.nleps:
			result["lep"+str(index+1)+"pt"] = lep.pt()
			result["lep"+str(index+1)+"eta"] = abs(lep.eta())
			result["lep"+str(index+1)+"etapm"] = lep.eta()
			result["lep"+str(index+1)+"phi"] = lep.phi()
			result["lep"+str(index+1)+"energy"] = lep.energy()
			result["lep"+str(index+1)+"isMuon"] = lep.isMuon()
			result["lep"+str(index+1)+"isElectron"] = lep.isElectron()
			if lep.isElectron() : nel += 1 
			elif lep.isMuon(): nmu +=1
      result["Nel"]=nel
      result["Nmu"]=nmu
      return result			
if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], EventSelectionControlPlots())

