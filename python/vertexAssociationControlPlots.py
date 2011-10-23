#! /usr/bin/env python

import ROOT
import sys
from DataFormats.FWLite import Events, Handle
from baseControlPlots import BaseControlPlots
from vertexAssociation import *
from zbbCommons import zbblabel
#from myFuncTimer import print_timing

class VertexAssociationControlPlots(BaseControlPlots):
    """A class to create control plots for vertex association"""

    def __init__(self, dir=None, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="vertexAssociation", dataset=dataset, mode=mode)
    
    def beginJob(self, jetlabel=zbblabel.jetlabel, zlabel=zbblabel.zmumulabel, vertexlabel=zbblabel.vertexlabel , sigcut = 2.):
      self.sigcut = sigcut
      # declare histograms
      self.add("nvertices","nvertices",30,0,30)
      self.add("vx","vx",400,-0.2,0.2)
      self.add("vy","vy",400,-0.2,0.2)
      self.add("vz","vz",100,-25,25)
      self.add("vxerr","vxerr",100,0,0.01)
      self.add("vyerr","vyerr",100,0,0.01)
      self.add("vzerr","vzerr",100,0,0.02)
      self.add("lepton_dz","z distance between the two Z leptons",100,0,0.2)
      self.add("l1v_dz","z distance between lepton and vertex",100,0,1.)
      self.add("l2v_dz","z distance between lepton and vertex",100,0,1.)
      self.add("distance","vertex/track distance in z",2000,-10,10)
      self.add("sig","vertex/track significance in z",2000,-10,10)
      self.add("ratio1","jet/vertex association ratio v1",100,0,1)
      self.add("ratio2","jet/vertex association ratio v2",100,0,1)
      self.add("ratio3","jet/vertex association ratio v3",100,0,1)
      self.add("ratio1b","jet/vertex association ratio v1 using vertexing",100,0,1)
      self.add("ratio2b","jet/vertex association ratio v2 using vertexing",100,0,1)
      self.add("ratio3b","jet/vertex association ratio v3 using vertexing",100,0,1)
      self.add("j1_ratio1","leading jet/vertex association ratio v1",100,0,1)
      self.add("j1_ratio2","leading jet/vertex association ratio v2",100,0,1)
      self.add("j1_ratio3","leading jet/vertex association ratio v3",100,0,1)
      self.add("j1_ratio1b","leading jet/vertex association ratio v1 using vertexing",100,0,1)
      self.add("j1_ratio2b","leading jet/vertex association ratio v2 using vertexing",100,0,1)
      self.add("j1_ratio3b","leading jet/vertex association ratio v3 using vertexing",100,0,1)
      self.add("goodevent","pass or not Z+jet to vertex association",2,0,2)
      # some plots with only the jets associated to genjets. Filled only for MC, allows to check PU effect more directly.
      # I do only duplicate some plots relevant for the PU study.
      self.add("ratio1b_nopu","jet/vertex association ratio v1 using vertexing",100,0,1)
      self.add("ratio2b_nopu","jet/vertex association ratio v2 using vertexing",100,0,1)
      self.add("ratio3b_nopu","jet/vertex association ratio v3 using vertexing",100,0,1)
      self.add("j1_ratio1b_nopu","leading jet/vertex association ratio v1 using vertexing",100,0,1)
      self.add("j1_ratio2b_nopu","leading jet/vertex association ratio v2 using vertexing",100,0,1)
      self.add("j1_ratio3b_nopu","leading jet/vertex association ratio v3 using vertexing",100,0,1)
      # prepare handles
      self.jetHandle = Handle ("vector<pat::Jet>")
      self.zHandle = Handle ("vector<reco::CompositeCandidate>")
      self.vertexHandle = Handle ("vector<reco::Vertex>")
      self.jetlabel = (jetlabel)
      self.zlabel = (zlabel)
      self.vertexlabel = (vertexlabel)

    def jetSelection(self, jet, Z):
      """This corresponds to the loose jet id selection for PF jets and avoid overlap with leptons"""
      rawjet = jet.correctedJet("Uncorrected")
      nhf = ( rawjet.neutralHadronEnergy() + rawjet.HFHadronEnergy() ) / rawjet.energy()
      nef = rawjet.neutralEmEnergyFraction()
      nconstituents = rawjet.numberOfDaughters()
      chf = rawjet.chargedHadronEnergyFraction()
      nch = rawjet.chargedMultiplicity()
      cef = rawjet.chargedEmEnergyFraction()
      l1 = Z.daughter(0)
      l2 = Z.daughter(1)
      l1v = ROOT.TLorentzVector(l1.px(),l1.py(),l1.pz(),l1.energy())
      l2v = ROOT.TLorentzVector(l2.px(),l2.py(),l2.pz(),l2.energy())
      jv =  ROOT.TLorentzVector(jet.px(),jet.py(),jet.pz(),jet.energy())
      dr1 = jv.DeltaR(l1v)
      dr2 = jv.DeltaR(l2v)
      return nhf<0.99 and nef<0.99 and  nconstituents>1 and chf>0 and nch>0 and cef<0.99 and dr1>0.5 and dr2>0.5

    #@print_timing
    def process(self,event):
      """vertexAssociationControlPlots"""
      result = { }
      # load event
      event.getByLabel (self.jetlabel,self.jetHandle)
      event.getByLabel (self.zlabel,self.zHandle)
      event.getByLabel (self.vertexlabel,self.vertexHandle)
      jets = self.jetHandle.product()
      zs = self.zHandle.product()
      vs = self.vertexHandle.product()
      result["nvertices"] = vs.size()
      # only events with one Z candidate
      if zs.size()==0 : return result
      # select the Z
      bestZ = zs[0]
      bestM = -1000.
      for z in zs :
        if abs(z.mass()-91.1876)<abs(bestM-91.1876) :
          bestM = z.mass()
          bestZ = z
      # select the vertex
      vertex = findPrimaryVertex(bestZ, vs)
      result["vx"] = vertex.x()
      result["vy"] = vertex.y()
      result["vz"] = vertex.z()
      result["vxerr"] = vertex.xError()
      result["vyerr"] = vertex.yError()
      result["vzerr"] = vertex.zError()
      # relevant quantities to monitor: Z vs primary vertex
      lepton1 = bestZ.daughter(0)
      lepton2 = bestZ.daughter(1)
      result["lepton_dz"] = abs(lepton1.vz()-lepton2.vz())
      result["l1v_dz"] = abs(lepton1.vz()-vertex.z())
      result["l2v_dz"] = abs(lepton2.vz()-vertex.z())
      # relevant quantities to monitor: jets vs primary vertex
      firstJet = True
      result["ratio1"] = [ ]
      result["ratio2"] = [ ]
      result["ratio3"] = [ ]
      result["ratio1b"] = [ ]
      result["ratio2b"] = [ ]
      result["ratio3b"] = [ ]
      result["ratio1b_nopu"] = [ ]
      result["ratio2b_nopu"] = [ ]
      result["ratio3b_nopu"] = [ ]
      result["j1_ratio1"] = 0
      result["j1_ratio2"] = 0
      result["j1_ratio3"] = 0
      result["j1_ratio1b"] = 0
      result["j1_ratio2b"] = 0
      result["j1_ratio3b"] = 0
      result["j1_ratio1b_nopu"] = 0
      result["j1_ratio2b_nopu"] = 0
      result["j1_ratio3b_nopu"] = 0
      result["distance"] = [ ]
      result["sig"] = [ ]
      for jet in jets: 
        if not self.jetSelection(jet,bestZ) : continue
        ptsum = 0.
        ptsumx = 0.
        ptsumy = 0.
        ptsumall = 0.
        isMcPrimaryJet = not (jet.genJet() is None)
        for i in range(jet.getPFConstituents().size()):
          #make sure the object is usable
          #the last condition is a fix if we miss muons and electrons in the file, for rare occurences... 
          #apparently something in the vz() calculation.
          if (not jet.getPFConstituent(i).isAvailable ()) or jet.getPFConstituent(i).isNull ():
            continue
          if jet.getPFConstituent(i).trackRef().isNull():
            continue
          if jet.getPFConstituent(i).muonRef().isNonnull () or jet.getPFConstituent(i).gsfTrackRef().isNonnull ():
            continue
          distance = (jet.getPFConstituent(i).vz() - vertex.z())
          result["distance"].append(distance)
          error = (jet.getPFConstituent(i).trackRef().dzError()**2 + vertex.zError()**2)**(1/2.)
          sig = distance/error
          result["sig"].append(sig)
          if abs(sig)<self.sigcut :
            ptsum += jet.getPFConstituent(i).pt()
            ptsumx += jet.getPFConstituent(i).px()
            ptsumy += jet.getPFConstituent(i).py()
          ptsumall += jet.getPFConstituent(i).pt()
        result["ratio1"].append(ptsum/jet.et())
        if firstJet: result["j1_ratio1"] = ptsum/jet.et()
        if ptsumall>0 : 
          ratio = ptsum/ptsumall
        else:
          ratio = -1.
        result["ratio2"].append(ratio)
        if firstJet: result["j1_ratio2"] = ratio
        result["ratio3"].append((ptsumx**2+ptsumy**2)**(0.5)/jet.et())
        if firstJet: result["j1_ratio3"] = (ptsumx**2+ptsumy**2)**(0.5)/jet.et() 
        # now, the same methods but using directly the vertex for the matching
        ptsumx = 0.
        ptsumy = 0.
        ptsum = 0.
        ptsumall = 0.
        trackrefs = map(lambda x:vertex.tracks_[x].key(),range(vertex.tracks_.size()))
        for i in range(jet.getPFConstituents().size()):
          if jet.getPFConstituent(i).trackRef().isNull():
            continue
          try:
            trackrefs.index(jet.getPFConstituent(i).trackRef().key())
          except:
            pass
          else:
            ptsum += jet.getPFConstituent(i).pt()
            ptsumx += jet.getPFConstituent(i).px()
            ptsumy += jet.getPFConstituent(i).py()
          ptsumall += jet.getPFConstituent(i).pt()
        result["ratio1b"].append(ptsum/jet.et())
        if isMcPrimaryJet: result["ratio1b_nopu"].append(ptsum/jet.et())
        if firstJet: 
          result["j1_ratio1b"] = ptsum/jet.et()
          if isMcPrimaryJet: result["j1_ratio1b_nopu"] = ptsum/jet.et()
        if ptsumall>0 : 
          ratio = ptsum/ptsumall
        else:
          ratio = -1.
        result["ratio2b"].append(ratio)
        if isMcPrimaryJet: result["ratio2b_nopu"].append(ratio)
        if firstJet: 
          result["j1_ratio2b"] = ratio
          if isMcPrimaryJet: result["j1_ratio2b_nopu"] = ratio
        result["ratio3b"].append((ptsumx**2+ptsumy**2)**(0.5)/jet.et())
        if isMcPrimaryJet: result["ratio3b_nopu"].append((ptsumx**2+ptsumy**2)**(0.5)/jet.et())
        if firstJet: 
          result["j1_ratio3b"] = (ptsumx**2+ptsumy**2)**(0.5)/jet.et()
          if isMcPrimaryJet: result["j1_ratio3b_nopu"] = (ptsumx**2+ptsumy**2)**(0.5)/jet.et()
        firstJet = False
      result["goodevent"] = checkVertexAssociation(bestZ, jets, vs)
      return result
    

def runTest():
  controlPlots = VertexAssociationControlPlots()
  #path="/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/"
  path="../testfiles/ttbar/"
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
  events = Events (files)
  controlPlots.beginJob()
  i = 0
  for event in events:
    controlPlots.processEvent(event)
    if i%1000==0 : print "Processing... event ", i
    i += 1
  controlPlots.endJob()

