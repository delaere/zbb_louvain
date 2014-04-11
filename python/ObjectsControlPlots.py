import ROOT
import array
from math import sin, fabs
from PatAnalysis.BaseControlPlots import BaseControlPlots
from JetCorrectionUncertainty import JetCorrectionUncertaintyProxy
from ObjectSelection import *
from zbbConfig import configuration

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
        if muon.pt()<20. : continue
        
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
        if electron.pt()<20. : continue
        
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
      self.add("SSVHEdiscDisc1","SSVHEdiscDisc1",200,0,10)
      self.add("SSVHPdiscDisc1","SSVHPdiscDisc1",200,0,10)
      self.add("CSVdiscDisc1","CSVdiscDisc1",100,0,1)
      self.add("JPdiscDisc1","JPdiscDisc1",100,0,2.5)
      self.add("MET","MET",100,0,200)
      self.add("METphi","MET #phi",70,-3.5,3.5)
      self.add("METsignificance","MET significance",1000,0,500)
      self.add("METphiNNregression","MET #ph for NN regression",70,-3.5,3.5)
      self.add("METNNregression","MET for NN regression",250,0,500)
      #List of the variables related to jets in the oreder of plotting (from python 2.7 use of 'OrderedDict' can simplify this)
      self.varOrdering = ["pt", "pt_totunc", "eta", "etapm", "phi", "energy", "mass", "jetid", "Flavor", "npf", "nch", "Chf", "Nhf", "cef", "nef", "Phf", "Elf", "Muf", "SSVHEdisc", "SSVHPdisc", "CSVdisc", "JPdisc", "nVertHE", "nVertHP", "SVmass", "SVpT", "Vtx3dL", "Vtx3deL", "VtxPt", "PtD", "beta", "betaStar", "PUIdMva", "overlapmu", "overlapele"]
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
          "overlapmu" : ["jets overlaps with muons",2,0,2],
          "overlapele" : ["jets overlaps with electrons",2,0,2],
          }
      for var in self.varOrdering:
          if not var in dicoVar :
              print "Warning:", var, " is not defined. This variable will not be plotted."
              self.varOrdering.remove(var)
              continue
          self.add("jets"+var,"All jet "+dicoVar[var][0],dicoVar[var][1],dicoVar[var][2],dicoVar[var][3])
      self.njets = 2
      for ijet in range(0,self.njets):
          for var in self.varOrdering:
              self.add("jet"+str(ijet+1)+var,"Jet "+str(ijet+1)+dicoVar[var][0],dicoVar[var][1],dicoVar[var][2],dicoVar[var][3])
      self.nbjets = 2
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
      if event.object().event().eventAuxiliary().isRealData():
        configuration.JERfactor = 0
        configuration.JESfactor = 0
      # process event and fill histograms
      for var in self.varOrdering : result["jets"+var] = []
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
          result["jetsFlavor"].append(jet.partonFlavour())
          result["jetsnpf"].append(rawjet.numberOfDaughters())
          result["jetsnch"].append(rawjet.chargedMultiplicity())
          result["jetsChf"].append(jet.chargedHadronEnergyFraction())
          result["jetsNhf"].append(jet.neutralHadronEnergyFraction())
          result["jetsnef"].append(rawjet.neutralEmEnergyFraction())
          result["jetscef"].append(rawjet.chargedEmEnergyFraction())
          result["jetsPhf"].append(jet.photonEnergyFraction())
          result["jetsElf"].append(jet.electronEnergyFraction())
          result["jetsMuf"].append(jet.muonEnergyFraction())
          result["jetsVtx3dL"].append(jetVtx3dL(jet))
          result["jetsVtx3deL"].append(jetVtx3deL(jet))
          result["jetsVtxPt"].append(jetVtxPt(jet))
          result["jetsPtD"].append(jetPtD(jet))
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
          result["jetsoverlapmu"].append(jet.hasOverlaps("muons"))
          result["jetsoverlapele"].append(jet.hasOverlaps("electrons"))	

          maxbdiscSSVHE = max(maxbdiscSSVHE,jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags"))
	  maxbdiscSSVHP = max(maxbdiscSSVHP,jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags"))
	  maxbdiscCSV = max(maxbdiscSSVHE,jet.bDiscriminator("combinedSecondaryVertexBJetTags"))
	  maxbdiscJP = max(maxbdiscSSVHP,jet.bDiscriminator("jetProbabilityBJetTags"))
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
              result["jet"+str(nj)+"Flavor"] = jet.partonFlavour()
              result["jet"+str(nj)+"npf"] = jet.numberOfDaughters()
              result["jet"+str(nj)+"nch"] = jet.chargedMultiplicity()
              result["jet"+str(nj)+"Chf"] = jet.chargedHadronEnergyFraction()
              result["jet"+str(nj)+"Nhf"] = jet.neutralHadronEnergyFraction()
              result["jet"+str(nj)+"nef"] = jet.neutralEmEnergyFraction()
              result["jet"+str(nj)+"cef"] = jet.chargedEmEnergyFraction()
              result["jet"+str(nj)+"Phf"] = jet.photonEnergyFraction()
              result["jet"+str(nj)+"Elf"] = jet.electronEnergyFraction()
              result["jet"+str(nj)+"Muf"] = jet.muonEnergyFraction()
              result["jet"+str(nj)+"Vtx3dL"] = jetVtx3dL(jet)
              result["jet"+str(nj)+"Vtx3deL"] = jetVtx3deL(jet)
              result["jet"+str(nj)+"VtxPt"] = jetVtxPt(jet)
              result["jet"+str(nj)+"PtD"] = jetPtD(jet)
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
              result["jet"+str(nj)+"PUIdMva"] = jet.userFloat("puJetMva")
              result["jet"+str(nj)+"overlapmu"] = jet.hasOverlaps("muons")
              result["jet"+str(nj)+"overlapele"] = jet.hasOverlaps("electrons")
          if nj==1: 
	    j1pt=jetPt
          if isBJet(jet,"HE",self.btagging): 
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
              result["bjet"+str(indexDijet)+"Flavor"] = jet.partonFlavour()
              if jetId(jet,"tight"): result["bjet"+str(indexDijet)+"jetid"] = 3
              elif jetId(jet,"medium"): result["bjet"+str(indexDijet)+"jetid"] = 2
              elif jetId(jet,"loose"): result["bjet"+str(indexDijet)+"jetid"] = 1
              else: result["bjet"+str(indexDijet)+"jetid"] = 0
              result["bjet"+str(indexDijet)+"npf"] = jet.numberOfDaughters()
              result["bjet"+str(indexDijet)+"nch"] = jet.chargedMultiplicity()
              result["bjet"+str(indexDijet)+"Chf"] = jet.chargedHadronEnergyFraction()
              result["bjet"+str(indexDijet)+"Nhf"] = jet.neutralHadronEnergyFraction()
              result["bjet"+str(indexDijet)+"nef"] = jet.neutralEmEnergyFraction()
              result["bjet"+str(indexDijet)+"cef"] = jet.chargedEmEnergyFraction()
              result["bjet"+str(indexDijet)+"Phf"] = jet.photonEnergyFraction()
              result["bjet"+str(indexDijet)+"Elf"] = jet.electronEnergyFraction()
              result["bjet"+str(indexDijet)+"Muf"] = jet.muonEnergyFraction()
              result["bjet"+str(indexDijet)+"Vtx3dL"] = jetVtx3dL(jet)
              result["bjet"+str(indexDijet)+"Vtx3deL"] = jetVtx3deL(jet)
              result["bjet"+str(indexDijet)+"VtxPt"] = jetVtxPt(jet)
              result["bjet"+str(indexDijet)+"PtD"] = jetPtD(jet)
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
              result["bjet"+str(indexDijet)+"overlapmu"] = jet.hasOverlaps("muons")
              result["bjet"+str(indexDijet)+"overlapele"] = jet.hasOverlaps("electrons")

              result["dptj1b1"] = jetPt-j1pt
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

