import ROOT
import array
from math import sin, sqrt
from PatAnalysis.BaseControlPlots import BaseControlPlots
from JetCorrectionUncertainty import JetCorrectionUncertaintyProxy
from ObjectSelection import *
from zbbCommons import zbblabel,zbbfile,zbbsystematics

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
    masspoints=[110,115,120,125,130,135,140,145,150]#needed for isrjet

    def __init__(self, dir=None, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated

      BaseControlPlots.__init__(self, dir=dir, purpose="jetmet", dataset=dataset, mode=mode)
      self._JECuncertainty = JetCorrectionUncertaintyProxy()
    
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
      self.add("jet1pt","leading jet Pt",1000,0,1000)
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
      self.add("jet2pt","subleading jet Pt",1000,0,1000)
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
      self.add("bjet1pt","leading bjet Pt",1000,0,1000)
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
      self.add("bjet2pt","subleading bjet Pt",1000,0,1000)
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
      self.add("isrjetpt","isr jet Pt",1000,0,1000)
      self.add("isrjetetapm","isr jet Eta",50,-2.5,2.5)
      self.add("isrjetphi","isr jet Phi",25,-4,4)
      self.add("isrjetmass","isr jet mass",1000,0,3000.)
      self.add("fsrjetDRpt","jet Pt jet closet in DR to b or bbar",1000,0,1000)
      self.add("fsrjetDRetapm","jet Eta jet closet in DR to b or bbar",50,-2.5,2.5)
      self.add("fsrjetDRphi","jet Phi jet closet in DR to b or bbar",25,-4,4)
      self.add("fsrjetDRmass","jet mass jet closet in DR to b or bbar",1000,0,3000.)
      self.add("fsrDR","closest DR between a third jet and b or bbar",100,0,5)
      self.add("trijetMdr","invariant mass of b+bbar+fsrjetDR",1000,0,1000)
      for imass in range(len(self.masspoints)):
          self.add("fsrjetpt_"+str(self.masspoints[imass]),"fsr jet Pt for mH="+str(self.masspoints[imass])+"GeV",1000,0,1000)
          self.add("fsrjetetapm_"+str(self.masspoints[imass]),"fsr jet Eta for mH="+str(self.masspoints[imass])+"GeV",50,-2.5,2.5)
          self.add("fsrjetphi_"+str(self.masspoints[imass]),"fsr jet Phi for mH="+str(self.masspoints[imass])+"GeV",25,-4,4)
          self.add("fsrjetmass_"+str(self.masspoints[imass]),"fsr jet mass for mH="+str(self.masspoints[imass])+"GeV",1000,0,3000.)
          self.add("trijetM_"+str(self.masspoints[imass]),"invariant mass of b+bbar+fsrjet (mH="+str(self.masspoints[imass])+"GeV)",1000,0,1000)

    def process(self, event):
      """JetmetControlPlots"""
      result = { }
      if event.object().event().eventAuxiliary().isRealData():
        zbbsystematics.JERfactor = 0
        zbbsystematics.JESfactor = 0
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
      dijet = event.dijet_all
      goodJets = event.goodJets_all
      for index,jet in enumerate(event.jets):
        #jetPt = jet.pt()
        jetPt = self._JECuncertainty.jetPt(jet)
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
            result["jet1Nhf"] = jet.neutralHadronEnergyFraction()
            result["jet1Phf"] = jet.photonEnergyFraction()
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
            result["jet2Nhf"] = jet.neutralHadronEnergyFraction()
            result["jet2Phf"] = jet.photonEnergyFraction()
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
              result["bjet1Nhf"] = jet.neutralHadronEnergyFraction()
              result["bjet1Phf"] = jet.photonEnergyFraction()
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
	      bjet1svmass=-1
	      bjet1svpt=-1
	      if tISV :
	        if tISV.secondaryVertex(0) :
	          bjet1svmass = tISV.secondaryVertex(0).p4().mass()
                  bjet1svpt = tISV.secondaryVertex(0).p4().pt()
              result["bjet1SVmass"] = bjet1svmass
	      result["bjet1SVpT"] = bjet1svpt
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
              result["bjet2Nhf"] = jet.neutralHadronEnergyFraction()
              result["bjet2Phf"] = jet.photonEnergyFraction()
              result["bjet2Elf"] = jet.electronEnergyFraction()
              result["bjet2Muf"] = jet.muonEnergyFraction()
              result["bjet2Vtx3dL"] = jetVtx3dL(jet)
              result["bjet2Vtx3deL"] = jetVtx3deL(jet)
              result["bjet2VtxPt"] = jetVtxPt(jet)
              result["bjet2PtD"] = jetPtD(jet)
              result["bjet2SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
              result["bjet2SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
	      bjet2svmass=-1
	      bjet2svpt=-1
	      if tISV :
	        if tISV.secondaryVertex(0) :
	          bjet2svmass = tISV.secondaryVertex(0).p4().mass()
                  bjet2svpt = tISV.secondaryVertex(0).p4().pt()
              result["bjet2SVmass"] = bjet2svmass
	      result["bjet2SVpT"] = bjet2svpt
              result["bjet2CSVdisc"] = jet.bDiscriminator("combinedSecondaryVertexBJetTags")
              result["bjet2JPdisc"] = jet.bDiscriminator("jetProbabilityBJetTags")
              result["bjet2nVertHE"] = nHEvert
              result["bjet2nVertHP"] = nHPvert
              result["bjet2beta"] = jet.userFloat("beta")
              result["bjet2betaStar"] = jet.userFloat("betaStar")	      
          if isBJet(jet,"HP",self.btagging): nbP += 1

      #second loop to jets to chose ISR and FSR jets. It would be better to do this with only one loop
      fsrjet={}
      #init diffmass to huge number
      diffmass={}
      trijetM={}
      for imass in range(len(self.masspoints)):
          diffmass[self.masspoints[imass]] = 10000.
          fsrjet[self.masspoints[imass]] = None
          trijetM[self.masspoints[imass]] = 0.0
      ijet = 0
      firstJet = True
      isrjet = None
      fsrjetDR  = None#closest jet in DR to b or bbar
      fsrDR = 999.9
      fsrjet4vec = ROOT.TLorentzVector(0,0,0,0)
      if nj > 2 : #if there are 3 good jets and we select 2 b-jets
          b1 = ROOT.TLorentzVector(self._JECuncertainty.jetPt(dijet[0]),dijet[0].eta(),dijet[0].phi(),dijet[0].mass())
          b2 = ROOT.TLorentzVector(self._JECuncertainty.jetPt(dijet[1]),dijet[1].eta(),dijet[1].phi(),dijet[1].mass())
          for index,jet in enumerate(event.jets):
              goodJets = event.goodJets_mu if self.muChannel else event.goodJets_ele
              if goodJets[index] and not jet in dijet:
                  #print "there is isrjet"
                  if firstJet == True:
                      isrjet = jet
                      firstJet = False
                      #print "assigning isr jet to jet with pt=", jet.pt()
                  extrajet4vec = ROOT.TLorentzVector(0,0,0,0)
                  extrajet4vec.SetPtEtaPhiM(self._JECuncertainty.jetPt(jet), jet.eta(), jet.phi(), jet.mass())
                  
                  #setting fsr jet based on DR criteria
                  tmpdr = min(extrajet4vec.DeltaR(b1), extrajet4vec.DeltaR(b2))
                  if (tmpdr < fsrDR):
                      fsrDR = tmpdr
                      fsrjetDR = jet
                      fsrjet4vec = extrajet4vec
                      
                  #setting fsr jet based on closest invariant mass of 3 jet system to a given higgs mass criteria
                  threejet4vec = b1 + b2 + extrajet4vec
                  for imass in range(len(self.masspoints)):
                      #print "masspoint[",imass,"]=",self.masspoints[imass]
                      if fabs(threejet4vec.M() - self.masspoints[imass]) < diffmass[self.masspoints[imass]]:
                          diffmass[self.masspoints[imass]] = fabs(threejet4vec.M() - self.masspoints[imass])
                          fsrjet[self.masspoints[imass]] = jet
                          trijetM[self.masspoints[imass]] = threejet4vec.M()
              ijet+=1
              
              if not isrjet is None:
                  result["isrjetpt"] = self._JECuncertainty.jetPt(isrjet)
                  result["isrjetetapm"] = isrjet.eta()
                  result["isrjetphi"] = isrjet.phi()
                  result["isrjetmass"] = isrjet.mass()
              else:
                  result["isrjetpt"] = 0
                  result["isrjetetapm"] = 0
                  result["isrjetphi"] = 0
                  result["isrjetmass"] = 0
                  
              if not fsrjetDR is None:
                  result["fsrjetDRpt"] = self._JECuncertainty.jetPt(fsrjetDR)
                  result["fsrjetDRetapm"] = fsrjetDR.eta()
                  result["fsrjetDRphi"] = fsrjetDR.phi()
                  result["fsrjetDRmass"] = fsrjetDR.mass()
                  result["fsrDR"] = fsrDR
                  result["trijetMdr"] = (b1 + b2 + fsrjet4vec).M()
              else:
                  result["fsrjetDRpt"] = 0
                  result["fsrjetDRetapm"] = 0
                  result["fsrjetDRphi"] = 0
                  result["fsrjetDRmass"] = 0
                  result["fsrDR"] = 0
                  result["trijetMdr"] = 0
                  
              for imass in range(len(self.masspoints)):
                  if not fsrjet[self.masspoints[imass]] is None:
                      result["fsrjetpt_"+str(self.masspoints[imass])] = self._JECuncertainty.jetPt(fsrjet[self.masspoints[imass]])
                      result["fsrjetetapm_"+str(self.masspoints[imass])] = fsrjet[self.masspoints[imass]].eta()
                      result["fsrjetphi_"+str(self.masspoints[imass])] = fsrjet[self.masspoints[imass]].phi()
                      result["fsrjetmass_"+str(self.masspoints[imass])] = fsrjet[self.masspoints[imass]].mass()
                      result["trijetM_"+str(self.masspoints[imass])] = trijetM[self.masspoints[imass]]
                  else:
                      result["fsrjetpt_"+str(self.masspoints[imass])] = 0
                      result["fsrjetetapm_"+str(self.masspoints[imass])] = 0
                      result["fsrjetphi_"+str(self.masspoints[imass])] = 0
                      result["fsrjetmass_"+str(self.masspoints[imass])] = 0
                      result["trijetM_"+str(self.masspoints[imass])] = 0
                      
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

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  if sys.argv[2]=="Jetmet":
    runTest(sys.argv[1], JetmetControlPlots())
  elif sys.argv[2]=="Electrons":
    runTest(sys.argv[1], ElectronsControlPlots())
  elif sys.argv[2]=="Muons":
    runTest(sys.argv[1], MuonsControlPlots())

