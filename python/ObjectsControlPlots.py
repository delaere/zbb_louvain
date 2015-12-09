import ROOT
import array
from math import sin, fabs
from PatAnalysis.BaseControlPlots import BaseControlPlots
from JetCorrectionUncertainty import JetCorrectionUncertaintyProxy
from ObjectSelection import *
import os
confCfg = os.environ["PatAnalysisCfg"]
if confCfg : from UserCode.zbb_louvain.PatAnalysis.CPconfig import configuration
else : from zbbConfig import configuration

class MuonsControlPlots(BaseControlPlots):
    """A class to create control plots for muons"""

    def __init__(self, dir=None, purpose="muons", dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)
    
    def beginJob(self, muonList="muons", muonType="tight"):
      # declare histograms
      self.add("muonType","Muon type (0:no type, 1:global, 2:tracker, 3:glob+track)", 4,0,4)
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
        if muon.pt()<8. : continue
        
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

    def __init__(self, dir=None, purpose="electrons", dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)
    
    def beginJob(self, electronList="electrons", electronType="tight"):
      # declare histograms
      self.add("eleid","electron id",10,0,10)
      self.add("eleMVAnontrig","electron MVA non trig",100,-1,1)
      self.add("eleMVAtrig","electron MVA trig",100,-1,1)
      self.add("eleMVAtrigNoIP","electron MVA trig no IP",100,-1,1)
      self.add("elemisshits","Electron missing hits",5,0,5)
      self.add("elept","electron pt",500,0,500)
      self.add("eleeta","electron eta",30,0,3)
      self.add("eleetapm","electron eta",60,-3,3)
      self.add("eledb","electron dB",100,0,0.05)
      self.add("eleoverlapmu","electrons overlaps with muon",2,0,2)
      self.add("elepfIsoPUc","Electron pfIsoPUCorrected",100,0,0.2)
      self.add("elepfIsoPUcMC","Electron pfIsoPUCorrectedMC",100,0,0.2)
      self.add("eleHcalDepth1Iso","Electron HcalDepth1Iso",1000,0,20)
      self.add("eleHcalDepth2Iso","Electron HcalDepth2Iso",1000,0,20)
      self.add("eleHcalDepth1BcIso","Electron HcalDepth1BcIso",1000,0,20)
      self.add("eleHcalDepth2BcIso","Electron HcalDepth2BcIso",1000,0,20)
      self.add("eleEcalIso","Electron EcalIso",1000,0,20)
      self.add("eleTkIso","Electron TkIso",1000,0,20)
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
      result["eleMVAnontrig"] = [ ]
      result["eleMVAtrig"] = [ ]
      result["eleMVAtrigNoIP"] = [ ]
      result["elemisshits"] = [ ]
      result["elept"] = [ ]
      result["eleeta"] = [ ]
      result["eleetapm"] = [ ]
      result["eledb"] = [ ]
      result["eleoverlapmu"] = [ ]
      result["elepfIsoPUc"] = [ ]
      result["elepfIsoPUcMC"] = [ ]
      result["eledphi"] = [ ]
      result["eledeta"] = [ ]
      result["eleinin"] = [ ]
      result["eleHcalDepth1Iso"] = [ ]
      result["eleHcalDepth2Iso"] = [ ]
      result["eleHcalDepth1BcIso"] = [ ]
      result["eleHcalDepth2BcIso"] = [ ]
      result["eleEcalIso"] = [ ]
      result["eleTkIso"] = [ ]
      nel = 0
      for electron in getattr(event, self.electronList):
        # for electrons
        if electron.pt()<8. : continue
        scEt = (electron.ecalEnergy()*sin(electron.theta()))
        result["eleid"].append(electron.userInt("MediumWP"))
        result["eleMVAnontrig"].append(electron.electronID("mvaNonTrigV0"))
        result["eleMVAtrig"].append(electron.electronID("mvaTrigV0"))
        result["eleMVAtrigNoIP"].append(electron.electronID("mvaTrigNoIPV0"))
        result["elemisshits"].append(electron.gsfTrack().numberOfLostHits())
        result["elepfIsoPUc"].append(electron.userFloat("PFIsoPUCorrected"))
        result["elepfIsoPUcMC"].append(electron.userFloat("PFIsoPUCorrectedMC"))
        result["eleHcalDepth1Iso"].append(electron.dr03IsolationVariables().hcalDepth1TowerSumEt/scEt)
        result["eleHcalDepth2Iso"].append(electron.dr03IsolationVariables().hcalDepth2TowerSumEt/scEt)
        result["eleHcalDepth1BcIso"].append(electron.dr03IsolationVariables().hcalDepth1TowerSumEtBc/scEt)
        result["eleHcalDepth2BcIso"].append(electron.dr03IsolationVariables().hcalDepth2TowerSumEtBc/scEt)
        result["eleEcalIso"].append(electron.dr03IsolationVariables().ecalRecHitSumEt/scEt)
        result["eleTkIso"].append(electron.dr03IsolationVariables().tkSumPt/scEt)
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

    def __init__(self, dir=None, purpose="jetmet", dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)
      self._JECuncertainty = JetCorrectionUncertaintyProxy()
    
    def beginJob(self, btagging="CSV", WP=["M","L"], prejets="", postjetsall="all",postjetsgood="all"):
      self.btagging=btagging
      self.WP=WP
      self.prejets=prejets
      self.postjetsall=postjetsall
      self.postjetsgood=postjetsgood
      # declare histograms
      self.add("SSVHEdiscDisc1","SSVHEdiscDisc1",200,0,10)
      self.add("SSVHPdiscDisc1","SSVHPdiscDisc1",200,0,10)
      self.add("CSVdiscDisc1","CSVdiscDisc1",100,0,1)
      self.add("JPdiscDisc1","JPdiscDisc1",100,0,2.5)
      self.add("MET","MET",1000,0,2000)
      self.add("METphi","MET #phi",70,-3.5,3.5)
      self.add("METsignificance","MET significance",1000,0,500)
      self.add("METphiNNregression","MET #ph for NN regression",70,-3.5,3.5)
      self.add("METNNregression","MET for NN regression",250,0,500)
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
      for var in self.varOrdering:
          if not var in dicoVar :
              print "Warning:", var, " is not defined. This variable will not be plotted."
              self.varOrdering.remove(var)
              continue
          self.add("jets"+var,"All jet "+dicoVar[var][0],dicoVar[var][1],dicoVar[var][2],dicoVar[var][3])
      self.njets = 5
      for ijet in range(0,self.njets):
          for var in self.varOrdering:
              self.add("jet"+str(ijet+1)+var,"Jet "+str(ijet+1)+dicoVar[var][0],dicoVar[var][1],dicoVar[var][2],dicoVar[var][3])
      self.nbjets = 4
      for ibjet in range(0,self.nbjets):
          for var in self.varOrdering:
              self.add("bjet"+str(ibjet+1)+var,"b-jet "+str(ibjet+1)+dicoVar[var][0],dicoVar[var][1],dicoVar[var][2],dicoVar[var][3])
      self.add("dptj1b1","Pt difference between leading jet and leading bjet",1000,-500,500)
      self.add("nj","jet count",15,-0.5,14.5)
      self.add("nb","b-jet count",5,-0.5,4.5)
      self.add("nbP","pure b-jet count",5,0,5)
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
      # process event and fill histograms
      for var in self.varOrdering : result["jets"+var] = []
      nj  = 0
      nb  = 0
      nbP = 0
      indexDijet = 0
      ind=2
      maxbdiscSSVHE = -1
      maxbdiscSSVHP = -1
      maxbdiscCSV  = -1
      maxbdiscJP  = -1
      dijet = getattr(event,"di"+self.prejets+"jet_"+self.postjetsall)
      goodJets = getattr(event,"good"+self.prejets+"Jets_"+self.postjetsgood)
#      if dijet is None or goodJets is None:
#	print "Cannot process event"	
#	return result
#      if dijet is None:
#	print "Cannot process event"	
#	return
      for index,jet in enumerate(getattr(event,self.prejets+"jets")):
        jetPt = jet.pt()
        if goodJets[index]:
          rawjet = jet.correctedJet("Uncorrected")
          result["jetspt"].append(jetPt)
	  result["jetspt_totunc"].append(self._JECuncertainty.unc_tot_jet(jet))
          result["jetseta"].append(abs(jet.eta()))
          result["jetsetapm"].append(jet.eta())
          result["jetsphi"].append(jet.phi())
	  result["jetsenergy"].append(jet.energy())
          result["jetsmass"].append(jet.mass())
          if jetId(jet,"tight"): result["jetsjetid"].append(3)
          elif jetId(jet,"medium"): result["jetsjetid"].append(2)
          elif jetId(jet,"loose"): result["jetsjetid"].append(1)
          else: result["jetsjetid"].append(0)
          result["jetsFlavor"].append(jet.partonFlavour() if jet.genJet() else 20)
          if jet.isPFJet():
              result["jetsnpf"].append(rawjet.numberOfDaughters())
              result["jetsnch"].append(rawjet.chargedMultiplicity())
              result["jetsChf"].append(jet.chargedHadronEnergyFraction())
              result["jetsNhf"].append(jet.neutralHadronEnergyFraction())
              result["jetsnef"].append(rawjet.neutralEmEnergyFraction())
              result["jetscef"].append(rawjet.chargedEmEnergyFraction())
              result["jetsPhf"].append(jet.photonEnergyFraction())
              result["jetsElf"].append(jet.electronEnergyFraction())
              result["jetsMuf"].append(jet.muonEnergyFraction())
              result["jetsPtD"].append(jetPtD(jet))
          result["jetsVtx3dL"].append(jetVtx3dL(jet))
          result["jetsVtx3deL"].append(jetVtx3deL(jet))
          result["jetsVtxPt"].append(jetVtxPt(jet))
          result["jetsSSVHEdisc"].append(jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"))
          result["jetsSSVHPdisc"].append(jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"))
	  tISV = jet.tagInfoSecondaryVertex("secondaryVertex")
          nHEvert = 0
          nHPvert = 0
	  if tISV :
            nHEvert = tISV.nVertices()
            nHPvert = sum( tISV.nVertexTracks(v) >=3 for v in range(nHEvert))
	    if tISV.secondaryVertex(0) :
	      result["jetsSVmass"].append(tISV.secondaryVertex(0).p4().mass())
	      result["jetsSVpT"].append(tISV.secondaryVertex(0).p4().pt())
          result["jetsnVertHE"].append(nHEvert)
          result["jetsnVertHP"].append(nHPvert)
          result["jetsCSVdisc"].append(jet.bDiscriminator("combinedSecondaryVertexBJetTags"))
          result["jetsJPdisc"].append(jet.bDiscriminator("jetProbabilityBJetTags"))
          result["jetsbeta"].append(jet.userFloat("beta"))
          result["jetsbetaStar"].append(jet.userFloat("betaStar"))
          result["jetsPUIdMva"].append(jet.userFloat("puJetMva"))
          result["jetsPUIdWP"].append(jet.userInt("puJetId"))
          result["jetsoverlapmu"].append(jet.hasOverlaps("muons"))
          result["jetsoverlapele"].append(jet.hasOverlaps("electrons"))	

          maxbdiscSSVHE = max(maxbdiscSSVHE,jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"))
	  maxbdiscSSVHP = max(maxbdiscSSVHP,jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"))
	  maxbdiscCSV = max(maxbdiscCSV,jet.bDiscriminator("combinedSecondaryVertexBJetTags"))
	  maxbdiscJP = max(maxbdiscJP,jet.bDiscriminator("jetProbabilityBJetTags"))
          nj += 1
          if nj<self.njets+1 :
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
              result["jet"+str(nj)+"Flavor"] = jet.partonFlavour() if jet.genJet() else 20
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
              result["jet"+str(nj)+"nVertHE"] = nHEvert
              result["jet"+str(nj)+"nVertHP"] = nHPvert
              if tISV :
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
          if nj==1: 
	    j1pt=jetPt
          if isBJet(jet,self.WP[1],self.btagging): 
            nb += 1
	    if jet in dijet:
              indexDijet+=1
              if indexDijet > self.nbjets : print "Error: more than 2 jets in dijet pair!!"
              result["bjet"+str(indexDijet)+"pt"] = jetPt
	      result["bjet"+str(indexDijet)+"pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
	      result["bjet"+str(indexDijet)+"eta"] = abs(jet.eta())
              result["bjet"+str(indexDijet)+"etapm"] = jet.eta()
              result["bjet"+str(indexDijet)+"phi"] = jet.phi()
              result["bjet"+str(indexDijet)+"energy"] = jet.energy()
              result["bjet"+str(indexDijet)+"mass"] = jet.mass()
              result["bjet"+str(indexDijet)+"Flavor"] = jet.partonFlavour() if jet.genJet() else 20
              if jetId(jet,"tight"): result["bjet"+str(indexDijet)+"jetid"] = 3
              elif jetId(jet,"medium"): result["bjet"+str(indexDijet)+"jetid"] = 2
              elif jetId(jet,"loose"): result["bjet"+str(indexDijet)+"jetid"] = 1
              else: result["bjet"+str(indexDijet)+"jetid"] = 0
              if jet.isPFJet():
                  result["bjet"+str(indexDijet)+"npf"] = jet.numberOfDaughters()
                  result["bjet"+str(indexDijet)+"nch"] = jet.chargedMultiplicity()
                  result["bjet"+str(indexDijet)+"Chf"] = jet.chargedHadronEnergyFraction()
                  result["bjet"+str(indexDijet)+"Nhf"] = jet.neutralHadronEnergyFraction()
                  result["bjet"+str(indexDijet)+"nef"] = jet.neutralEmEnergyFraction()
                  result["bjet"+str(indexDijet)+"cef"] = jet.chargedEmEnergyFraction()
                  result["bjet"+str(indexDijet)+"Phf"] = jet.photonEnergyFraction()
                  result["bjet"+str(indexDijet)+"Elf"] = jet.electronEnergyFraction()
                  result["bjet"+str(indexDijet)+"Muf"] = jet.muonEnergyFraction()
                  result["bjet"+str(indexDijet)+"PtD"] = jetPtD(jet)
              result["bjet"+str(indexDijet)+"Vtx3dL"] = jetVtx3dL(jet)
              result["bjet"+str(indexDijet)+"Vtx3deL"] = jetVtx3deL(jet)
              result["bjet"+str(indexDijet)+"VtxPt"] = jetVtxPt(jet)
              result["bjet"+str(indexDijet)+"SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
              result["bjet"+str(indexDijet)+"SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
              result["bjet"+str(indexDijet)+"nVertHE"] = nHEvert
              result["bjet"+str(indexDijet)+"nVertHP"] = nHPvert
	      bjetsvmass=-1
	      bjetsvpt=-1
	      if tISV :
	        if tISV.secondaryVertex(0) :
	          bjetsvmass = tISV.secondaryVertex(0).p4().mass()
                  bjetsvpt = tISV.secondaryVertex(0).p4().pt()
              result["bjet"+str(indexDijet)+"SVmass"] = bjetsvmass
	      result["bjet"+str(indexDijet)+"SVpT"] = bjetsvpt
	      result["bjet"+str(indexDijet)+"CSVdisc"] = jet.bDiscriminator("combinedSecondaryVertexBJetTags")
              result["bjet"+str(indexDijet)+"JPdisc"] = jet.bDiscriminator("jetProbabilityBJetTags")
	      result["bjet"+str(indexDijet)+"beta"] = jet.userFloat("beta")
              result["bjet"+str(indexDijet)+"betaStar"] = jet.userFloat("betaStar")
              result["bjet"+str(indexDijet)+"PUIdMva"] = jet.userFloat("puJetMva")
              result["bjet"+str(indexDijet)+"PUIdWP"] = jet.userInt("puJetId")
              result["bjet"+str(indexDijet)+"overlapmu"] = jet.hasOverlaps("muons")
              result["bjet"+str(indexDijet)+"overlapele"] = jet.hasOverlaps("electrons")

              result["dptj1b1"] = jetPt-j1pt
            else:	      
              ind+=1
              if ind > self.nbjets : print "Error: more than 4 b jets in the event!!"
	      else: 
                result["bjet"+str(ind)+"pt"] = jetPt
	        result["bjet"+str(ind)+"pt_totunc"] = self._JECuncertainty.unc_tot_jet(jet)
	        result["bjet"+str(ind)+"eta"] = abs(jet.eta())
                result["bjet"+str(ind)+"etapm"] = jet.eta()
                result["bjet"+str(ind)+"phi"] = jet.phi()
                result["bjet"+str(ind)+"energy"] = jet.energy()
                result["bjet"+str(ind)+"mass"] = jet.mass()
                result["bjet"+str(ind)+"Flavor"] = jet.partonFlavour()
                if jetId(jet,"tight"): result["bjet"+str(ind)+"jetid"] = 3
                elif jetId(jet,"medium"): result["bjet"+str(ind)+"jetid"] = 2
                elif jetId(jet,"loose"): result["bjet"+str(ind)+"jetid"] = 1
                else: result["bjet"+str(ind)+"jetid"] = 0
                if jet.isPFJet():
                  result["bjet"+str(ind)+"npf"] = jet.numberOfDaughters()
                  result["bjet"+str(ind)+"nch"] = jet.chargedMultiplicity()
                  result["bjet"+str(ind)+"Chf"] = jet.chargedHadronEnergyFraction()
                  result["bjet"+str(ind)+"Nhf"] = jet.neutralHadronEnergyFraction()
                  result["bjet"+str(ind)+"nef"] = jet.neutralEmEnergyFraction()
                  result["bjet"+str(ind)+"cef"] = jet.chargedEmEnergyFraction()
                  result["bjet"+str(ind)+"Phf"] = jet.photonEnergyFraction()
                  result["bjet"+str(ind)+"Elf"] = jet.electronEnergyFraction()
                  result["bjet"+str(ind)+"Muf"] = jet.muonEnergyFraction()
                  result["bjet"+str(ind)+"PtD"] = jetPtD(jet)
                result["bjet"+str(ind)+"Vtx3dL"] = jetVtx3dL(jet)
                result["bjet"+str(ind)+"Vtx3deL"] = jetVtx3deL(jet)
                result["bjet"+str(ind)+"VtxPt"] = jetVtxPt(jet)
                result["bjet"+str(ind)+"SSVHEdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
                result["bjet"+str(ind)+"SSVHPdisc"] = jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
                result["bjet"+str(ind)+"nVertHE"] = nHEvert
                result["bjet"+str(ind)+"nVertHP"] = nHPvert
	        bjetsvmass=-1
	        bjetsvpt=-1
	        if tISV :
	          if tISV.secondaryVertex(0) :
	            bjetsvmass = tISV.secondaryVertex(0).p4().mass()
                    bjetsvpt = tISV.secondaryVertex(0).p4().pt()
                result["bjet"+str(ind)+"SVmass"] = bjetsvmass
	        result["bjet"+str(ind)+"SVpT"] = bjetsvpt
	        result["bjet"+str(ind)+"CSVdisc"] = jet.bDiscriminator("combinedSecondaryVertexBJetTags")
                result["bjet"+str(ind)+"JPdisc"] = jet.bDiscriminator("jetProbabilityBJetTags")
	        result["bjet"+str(ind)+"beta"] = jet.userFloat("beta")
                result["bjet"+str(ind)+"betaStar"] = jet.userFloat("betaStar")
                result["bjet"+str(ind)+"PUIdMva"] = jet.userFloat("puJetMva")
                result["bjet"+str(ind)+"PUIdWP"] = jet.userInt("puJetId")
                result["bjet"+str(ind)+"overlapmu"] = jet.hasOverlaps("muons")
                result["bjet"+str(ind)+"overlapele"] = jet.hasOverlaps("electrons")

                result["dptj1b1"] = jetPt-j1pt	      
	      
          if isBJet(jet,self.WP[0],self.btagging): nbP += 1

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
          b1 = ROOT.TLorentzVector(dijet[0].px(),dijet[0].py(),dijet[0].pz(),dijet[0].energy())
          b2 = ROOT.TLorentzVector(dijet[1].px(),dijet[1].py(),dijet[1].pz(),dijet[1].energy())
          for index,jet in enumerate(getattr(event,self.prejets+"jets")):
              if goodJets[index] and not jet in dijet:
                  #print "there is isrjet"
                  if firstJet == True:
                      isrjet = jet
                      firstJet = False
                      #print "assigning isr jet to jet with pt=", jet.pt()
                  extrajet4vec = ROOT.TLorentzVector(0,0,0,0)
                  extrajet4vec.SetPtEtaPhiM(jet.pt(), jet.eta(), jet.phi(), jet.mass())
                  
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
              result["isrjetpt"] = isrjet.pt()
              result["isrjetetapm"] = isrjet.eta()
              result["isrjetphi"] = isrjet.phi()
              result["isrjetmass"] = isrjet.mass()
          else:
              result["isrjetpt"] = 0
              result["isrjetetapm"] = 0
              result["isrjetphi"] = 0
              result["isrjetmass"] = 0
              
          if not fsrjetDR is None:
              result["fsrjetDRpt"] = fsrjetDR.pt()
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
                  result["fsrjetpt_"+str(self.masspoints[imass])] = fsrjet[self.masspoints[imass]].pt()
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


class MetControlPlots(BaseControlPlots):
    """A class to create control plots for MET"""

    def __init__(self, dir=None, purpose="mets", dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)

    def beginJob(self):
      # declare histograms
      self.add("PFMETNoCorr_Pt","PF MET Pt",600,0,600)
      self.add("PFMETNoCorr_Phi","PF MET Phi",320,-3.2,3.2)
      self.add("PFMETNoCorr_Px","PF MET Px",1000,-500,500)
      self.add("PFMETNoCorr_Py","PF MET Py",1000,-500,500)
      self.add("PFMETNoCorr_Significance","PF MET Significance",500,0,250)

      self.add("PFMET01Phi_Pt","PF MET Pt",600,0,600)
      self.add("PFMET01Phi_Phi","PF MET Phi",320,-3.2,3.2)
      self.add("PFMET01Phi_Px","PF MET Px",1000,-500,500)
      self.add("PFMET01Phi_Py","PF MET Py",1000,-500,500)
      self.add("PFMET01Phi_Significance","PF MET Significance",500,0,250)

      self.add("PFMET01_Pt","PF MET Pt",600,0,600)
      self.add("PFMET01_Phi","PF MET Phi",320,-3.2,3.2)
      self.add("PFMET01_Px","PF MET Px",1000,-500,500)
      self.add("PFMET01_Py","PF MET Py",1000,-500,500)
      self.add("PFMET01_Significance","PF MET Significance",500,0,250)

      self.add("PFMET1_Pt","PF MET Pt",600,0,600)
      self.add("PFMET1_Phi","PF MET Phi",320,-3.2,3.2)
      self.add("PFMET1_Px","PF MET Px",1000,-500,500)
      self.add("PFMET1_Py","PF MET Py",1000,-500,500)
      self.add("PFMET1_Significance","PF MET Significance",500,0,250)

      self.add("PFMETPhi_Pt","PF MET Pt",600,0,600)
      self.add("PFMETPhi_Phi","PF MET Phi",320,-3.2,3.2)
      self.add("PFMETPhi_Px","PF MET Px",1000,-500,500)
      self.add("PFMETPhi_Py","PF MET Py",1000,-500,500)
      self.add("PFMETPhi_Significance","PF MET Significance",500,0,250)

      self.add("PFMET1Phi_Pt","PF MET Pt",600,0,600)
      self.add("PFMET1Phi_Phi","PF MET Phi",320,-3.2,3.2)
      self.add("PFMET1Phi_Px","PF MET Px",1000,-500,500)
      self.add("PFMET1Phi_Py","PF MET Py",1000,-500,500)
      self.add("PFMET1Phi_Significance","PF MET Significance",500,0,250)
      
      self.add("MVAMET_Pt","MVA MET Pt",600,0,600)
      self.add("MVAMET_Phi","MVA MET Phi",320,-3.2,3.2)
      self.add("MVAMET_Px","MVA MET Px",1000,-500,500)
      self.add("MVAMET_Py","MVA MET Py",1000,-500,500)
      self.add("MVAMET_Significance","MVA MET Significance",800,0,400)

      self.add("NoPUMET_Pt","NoPileUp MET Pt",600,0,600)
      self.add("NoPUMET_Phi","NoPileUp MET Phi",320,-3.2,3.2)
      self.add("NoPUMET_Px","NoPileUp MET Px",1000,-500,500)
      self.add("NoPUMET_Py","NoPileUp MET Py",1000,-500,500)
      self.add("NoPUMET_Significance","NoPileUp MET Significance",600,0,600)

    def process(self, event):
      """MetControlPlots"""
      result = { }
		
      result["PFMETNoCorr_Pt"] = event.PFMETNoCorr[0].pt()
      result["PFMETNoCorr_Phi"] = event.PFMETNoCorr[0].phi()
      result["PFMETNoCorr_Px"] = event.PFMETNoCorr[0].px()
      result["PFMETNoCorr_Py"] = event.PFMETNoCorr[0].py()
      result["PFMETNoCorr_Significance"] = event.PFMETNoCorr[0].significance()

      result["PFMET01Phi_Pt"] = event.PFMET01Phi[0].pt()
      result["PFMET01Phi_Phi"] = event.PFMET01Phi[0].phi()
      result["PFMET01Phi_Px"] = event.PFMET01Phi[0].px()
      result["PFMET01Phi_Py"] = event.PFMET01Phi[0].py()
      result["PFMET01Phi_Significance"] = event.PFMET01Phi[0].significance()

      result["PFMET01_Pt"] = event.PFMET01[0].pt()
      result["PFMET01_Phi"] = event.PFMET01[0].phi()
      result["PFMET01_Px"] = event.PFMET01[0].px()
      result["PFMET01_Py"] = event.PFMET01[0].py()
      result["PFMET01_Significance"] = event.PFMET01[0].significance()

      result["PFMET1_Pt"] = event.PFMET1[0].pt()
      result["PFMET1_Phi"] = event.PFMET1[0].phi()
      result["PFMET1_Px"] = event.PFMET1[0].px()
      result["PFMET1_Py"] = event.PFMET1[0].py()
      result["PFMET1_Significance"] = event.PFMET1[0].significance()

      result["PFMETPhi_Pt"] = event.PFMETPhi[0].pt()
      result["PFMETPhi_Phi"] = event.PFMETPhi[0].phi()
      result["PFMETPhi_Px"] = event.PFMETPhi[0].px()
      result["PFMETPhi_Py"] = event.PFMETPhi[0].py()
      result["PFMETPhi_Significance"] = event.PFMETPhi[0].significance()
      
      result["PFMET1Phi_Pt"] = event.PFMET1Phi[0].pt()
      result["PFMET1Phi_Phi"] = event.PFMET1Phi[0].phi()
      result["PFMET1Phi_Px"] = event.PFMET1Phi[0].px()
      result["PFMET1Phi_Py"] = event.PFMET1Phi[0].py()
      result["PFMET1Phi_Significance"] = event.PFMET1Phi[0].significance()

      result["MVAMET_Pt"] = event.MVAMET[0].pt()
      result["MVAMET_Phi"] = event.MVAMET[0].phi()
      result["MVAMET_Px"] = event.MVAMET[0].px()
      result["MVAMET_Py"] = event.MVAMET[0].py()
      result["MVAMET_Significance"] = event.MVAMET[0].significance()
      
      result["NoPUMET_Pt"] = event.NoPUMET[0].pt()
      result["NoPUMET_Phi"] = event.NoPUMET[0].phi()
      result["NoPUMET_Px"] = event.NoPUMET[0].px()
      result["NoPUMET_Py"] = event.NoPUMET[0].py()
      result["NoPUMET_Significance"] = event.NoPUMET[0].significance()
	
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

