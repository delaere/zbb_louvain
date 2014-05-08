import ROOT
from PatAnalysis.BaseControlPlots import BaseControlPlots
from JetCorrectionUncertainty import JetCorrectionUncertaintyProxy
from ObjectSelection import selectedTriggers
from zbbConfig import configuration

class ZbbEventSelectionControlPlots(BaseControlPlots):
    """A class to create control plots for event selection"""

    def __init__(self, dir=None, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="eventSelection", dataset=dataset, mode=mode)
      self._JECuncertainty = JetCorrectionUncertaintyProxy()
    
    def beginJob(self):
      # declare histograms
      self.add("run","Run number",50000,160000,210000)
      self.add("event","Event number",1000,0,5e9)
      self.add("ls","Lumi section",2000,0,2000)      
      self.add("triggerSelection","triggerSelection ",2,0,2)
      self.add("triggerBits","trigger bits",20,0,20)
      self.add("triggerDouble","Double trigger",2,0,2)
      self.add("triggerSingle","Single trigger",2,0,2)
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
      self.add("dphiZbj1","dphiZbj1",40,0,3.15)
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
      for i in range(paths.size()) :
          name = paths[i].name()
          #print name
          for trig_name in ["HLT_Mu17_Mu8","HLT_Mu17_TkMu8","HLT_Mu13_Mu8","HLT_IsoMu24_v"] :
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
      
      result["triggerBits"] = triggerList
      result["triggerSingle"] = SingleTrig
      result["triggerDouble"] = DoubleTrig
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
      if not bestZcandidate is None:
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
      ## plots looking for resonnances / kinematics
      # that method returns the best jet pair. When only one is btagged, it is the first one.
      # when two bjets are present, these are the two.
      # later on, variables are refering to b-jets, even if some are light jets
      if not bestZcandidate is None:
        dijet = event.dijet_all
        if not dijet[0] is None:
          z  = ROOT.TLorentzVector(bestZcandidate.px(),bestZcandidate.py(),bestZcandidate.pz(),bestZcandidate.energy())
          b1 = self._JECuncertainty.jet(dijet[0])
          Zb = z+b1
          result["ZbM"] = Zb.M()
          result["ZbPt"] = Zb.Pt()
          result["scaldptZbj1"] = bestZcandidate.pt()-dijet[0].pt()
          result["dphiZbj1"] = abs(z.DeltaPhi(b1))
          result["drZbj1"] = z.DeltaR(b1)
        if not dijet[1] is None:
          b2 = self._JECuncertainty.jet(dijet[1])
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

