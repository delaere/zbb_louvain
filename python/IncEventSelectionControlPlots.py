import ROOT
from PatAnalysis.BaseControlPlots import BaseControlPlots
from ObjectSelection import selectedTriggers
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
      self.add("mu1pt_inc","leading muon Pt",500,0,500)
      self.add("mu2pt_inc","subleading muon Pt",500,0,500)
      self.add("mu1eta_inc","leading muon Eta",25,0,2.5)
      self.add("mu2eta_inc","subleading muon Eta",25,0,2.5)
      self.add("mu1etapm_inc","leading muon Eta",50,-2.5,2.5)
      self.add("mu2etapm_inc","subleading muon Eta",50,-2.5,2.5)
      self.add("mu1charge_inc","mu1 charge",5,-2.5,2.5)
      self.add("mu2charge_inc","mu2 charge",5,-2.5,2.5)
      self.add("mu3pt_inc","third muon Pt",500,0,500)
      self.add("mu4pt_inc","fourth muon Pt",500,0,500)
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
      self.add("dijetM_inc","b bbar invariant mass",500,0,1000)
      self.add("dijetPt_inc","b bbar Pt",250,0,500)
      self.add("dijetdR_inc","#Delta R (b bbar)",50,0,5)
      self.add("dijetSVdR_inc","#Delta R (b bbar SV)",100,0,5)
      self.add("dphidijetMET_inc","#Delta #phi (b bbar MET)",40,-3.15,3.15)      
      self.add("MET_inc","Missing transverse energy",100,0,200)
      self.add("METsignificance_inc","missing transverse energy significance",1000,0,500)
      self.add("llbbM_inc","llbb invariant mass",1000,0,500)
      self.add("llbbPt_inc","llbb Pt",250,0,500)
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

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], EventSelectionControlPlots())

