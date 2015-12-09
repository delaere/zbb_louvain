import ROOT
from PatAnalysis.BaseControlPlots import BaseControlPlots
from ObjectSelection import selectedTriggers
import os
confCfg = os.environ["PatAnalysisCfg"]
if confCfg : from UserCode.zbb_louvain.PatAnalysis.CPconfig import configuration
else : from zbbConfig import configuration

Mode = configuration.runningMode

class HambEventSelectionControlPlots(BaseControlPlots):
    """A class to create control plots for event selection"""

    #def __init__(self, dir=None, dataset=None, mode=Mode):
    def __init__(self, dir=None, purpose="eventSelection", dataset=None, mode=Mode):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="eventSelection", dataset=dataset, mode=mode)
    
    def beginJob(self, mode=Mode):
      nBinH = 1000
      xMaxH = 1000.
      nBinDM = 100
      xMaxDM = 100.
      nBinMuPt = 500
      xMaxMuPt = 500.
      nBinMET = 100
      xMaxMET = 200.
      nBinMETsig = 1000
      xMaxMETsig = 500.
      if not (mode == "plots" ):
	nBinH = 10000
        xMaxH = 10000.
        nBinDM = 10000
        xMaxDM = 10000.
        nBinMuPt = 10000
        xMaxMuPt = 10000.
        nBinMET = 1000
        xMaxMET = 10000.
        nBinMETsig = 10000
        xMaxMETsig = 10000.
      #print str(mode)+", DiffM numbers: "+repr(xMaxDM)+"\t"+repr(nBinDM)
      # H -> aa -> mumu bb 
      self.add("run","Run number",50000,160000,210000)
      self.add("event","Event number",1000,0,5e9)
      self.add("ls","Lumi section",2000,0,2000)      
      self.add("triggerSelection","triggerSelection ",2,0,2)
      self.add("triggerBits","trigger bits",20,0,20)
      self.add("triggerDouble","Double trigger",2,0,2)
      self.add("triggerSingle","Single trigger",2,0,2)
      self.add("triggerEMU","E-MU trigger",2,0,2)

      # Higgs candidate plots
      self.add("dphiaa","#Delta #phi (a,a)",40,0,3.15)
      self.add("aadR","#Delta R (a,a)",100,0,5)
      self.add("dphiHiggsMET","#Delta #phi (H, MET)",40,0,3.15)
      self.add("hPt","Higgs p_{T}",nBinH,0,xMaxH)
      self.add("hMass","Higgs mass",nBinH,0,xMaxH)
      self.add("diffMassaa","#Delta m(a,a)",nBinDM,0,xMaxDM)
	
      # di-mu plots
      self.add("amassMu","di-#mu mass",10000,0,1000)
      self.add("aptMu","di-#mu p_{T}",nBinH,0,1000)
      self.add("dphiaMuMET","#Delta #phi (a_{#mu}, MET)",40,0,3.15)
      self.add("diMudR","#Delta R (#mu,#mu)",100,0,5)
      self.add("dphidiMu","#Delta #phi (#mu,#mu)",40,0,3.15)

      # di-b-jets plots
      self.add("amassBjet","di-b-jet mass",1000,0,1000)
      self.add("aptBjet","di-b-jet p_{T}",1000,0,1000)
      self.add("dphiaBjetMET","#Delta #phi (a_{b}, MET)",40,0,3.15)
      self.add("diBjetdR","#Delta R (b,b)",100,0,5)
      self.add("dphidiBjet","#Delta #phi (b,b)",40,0,3.15)
      self.add("diBjetSVdR","#Delta R_{SV} (b,b)",100,0,5)

      # basic distributions
      self.add("mu1pt","leading muon Pt",nBinMuPt,0,xMaxMuPt)
      self.add("mu2pt","subleading muon Pt",nBinMuPt,0,xMaxMuPt)
      self.add("mu1eta","leading muon Eta",25,0,2.5)
      self.add("mu2eta","subleading muon Eta",25,0,2.5)
      self.add("mu1etapm","leading muon Eta",50,-2.5,2.5)
      self.add("mu2etapm","subleading muon Eta",50,-2.5,2.5)

      self.add("jet1pt","leading jet Pt",nBinMuPt,0,xMaxMuPt)
      self.add("jet2pt","subleading jet Pt",nBinMuPt,0,xMaxMuPt)
      self.add("jet1CSV","leading jet CSV",2000,-1.,1.)
      self.add("jet2CSV","subleading jet CSV",2000,-1.,1.)

      self.add("matchedjet1pt","leading matched jet Pt",nBinMuPt,0,xMaxMuPt)
      self.add("matchedjet2pt","subleading matched jet Pt",nBinMuPt,0,xMaxMuPt)
      self.add("matchedjet1CSV","leading matched jet CSV",2000,-1.,1.)
      self.add("matchedjet2CSV","subleading matched jet CSV",2000,-1.,1.)

      self.add("MET_hamb","Missing transverse energy",nBinMET,0,xMaxMET)
      self.add("METsignificance_hamb","missing transverse energy significance",nBinMETsig,0,xMaxMETsig)
      

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
      result["triggerSelection"] = checkTrigger==False or event.isHambDiMuTriggerOK 
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
	
      bestDileptcandidate = event.bestHambDiMuCandidate
      if not bestDileptcandidate is None: 
        met = event.MET     
        met4v = ROOT.TLorentzVector(met[0].px(),met[0].py(),met[0].pz(),met[0].energy())

        #basic distributions
        result["mu1pt"] = bestDileptcandidate[0].pt()
        result["mu1etapm"] = bestDileptcandidate[0].eta()
        result["mu1eta"] = abs(bestDileptcandidate[0].eta())
        result["mu2pt"] = bestDileptcandidate[1].pt()
        result["mu2etapm"] = bestDileptcandidate[1].eta()
        result["mu2eta"] = abs(bestDileptcandidate[1].eta())
        result["MET_hamb"]= event.MET[0].pt()
        result["METsignificance_hamb"] = 0.
	if event.MET[0].getSignificanceMatrix()(0,0)<1e10 and event.MET[0].getSignificanceMatrix()(1,1)<1e10: 
          result["METsignificance_hamb"] = event.MET[0].significance()


 	l1 = ROOT.TLorentzVector(bestDileptcandidate[0].px(),bestDileptcandidate[0].py(),bestDileptcandidate[0].pz(),bestDileptcandidate[0].energy())
 	l2 = ROOT.TLorentzVector(bestDileptcandidate[1].px(),bestDileptcandidate[1].py(),bestDileptcandidate[1].pz(),bestDileptcandidate[1].energy())
	amu=l1+l2

        # di-mu plots
        result["amassMu"] = amu.M()	
        result["aptMu"] = amu.Pt()
	result["diMudR"] = l1.DeltaR(l2)  
        result["dphidiMu"] = l1.DeltaPhi(l2)    
        result["dphiaMuMET"] = amu.DeltaPhi(met4v)

	#Jet selection
        dijet = event.dijet_muChannel
        matchedjets = event.dijet_matchedJetWithB
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

          abb = b1 + b2
	  higgs = amu + abb

          # di-b-jets plots
	  sortedIndecies = [0,1]
	  if dijet[1].pt() > dijet[0].pt():
	     sortedIndecies = [1,0]
	  #jetpts = [dijet[0].pt(), dijet[1].pt()]
	  #jetpts.sort(reverse=True)
          result["jet1pt"] = dijet[sortedIndecies[0]].pt()
          result["jet2pt"] = dijet[sortedIndecies[1]].pt()
	  result["jet1CSV"] = dijet[sortedIndecies[0]].bDiscriminator("combinedSecondaryVertexBJetTags")
	  result["jet2CSV"] = dijet[sortedIndecies[1]].bDiscriminator("combinedSecondaryVertexBJetTags")
	  
	  if len(matchedjets) == 2:
	     sortedIndecies = [0,1]
	     if matchedjets[1].pt() >  matchedjets[0].pt():
                sortedIndecies = [1,0]
  	     result["matchedjet1pt"] = matchedjets[sortedIndecies[0]].pt()
             result["matchedjet2pt"] = matchedjets[sortedIndecies[1]].pt()
             result["matchedjet1CSV"] = matchedjets[sortedIndecies[0]].bDiscriminator("combinedSecondaryVertexBJetTags")
             result["matchedjet2CSV"] = matchedjets[sortedIndecies[1]].bDiscriminator("combinedSecondaryVertexBJetTags")
	  else:
             result["matchedjet1pt"] = -100
             result["matchedjet2pt"] = -100
             result["matchedjet1CSV"] = -100 
             result["matchedjet2CSV"] = -100

	  result["amassBjet"] = abb.M()
	  result["aptBjet"] = abb.Pt()
	  result["dphiaBjetMET"] = abb.DeltaPhi(met4v)
          result["diBjetdR"] = b1.DeltaR(b2)
          result["dphidiBjet"] = b1.DeltaPhi(b2)
          result["diBjetSVdR"] = svdr

          # Higgs candidate plots
	  result["dphiaa"] = abb.DeltaPhi(amu)
          result["aadR"] = abb.DeltaR(amu)
          result["dphiHiggsMET"] = higgs.DeltaPhi(met4v)
          result["hPt"] = higgs.Pt()
          result["hMass"] = higgs.M()
          result["diffMassaa"] = abs(abb.M()-amu.M())	  
      
      return result

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], EventSelectionControlPlots())


