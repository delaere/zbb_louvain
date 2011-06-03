#! /usr/bin/env python

import ROOT
import sys
from DataFormats.FWLite import Events, Handle
from vertexAssociation import *

class VertexAssociationControlPlots:
    """A class to create control plots for vertex association"""

    def __init__(self, dir=None):
      # create output file if needed. If no file is given, it means it is delegated
      if dir is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("vertexAssociation")
      else :
        self.f = None
        self.dir = dir
    
    def beginJob(self, jetlabel="cleanPatJets", zlabel="Ztighttight", vertexlabel="goodPV" ):
      # declare histograms
      self.dir.cd()
      self.h_nvertices = ROOT.TH1F("nvertices","nvertices",30,0,30)
      self.h_vx = ROOT.TH1F("vx","vx",400,-0.2,0.2)
      self.h_vy = ROOT.TH1F("vy","vy",400,-0.2,0.2)
      self.h_vz = ROOT.TH1F("vz","vz",100,-25,25)
      self.h_vxerr = ROOT.TH1F("vxerr","vxerr",100,0,0.01)
      self.h_vyerr = ROOT.TH1F("vyerr","vyerr",100,0,0.01)
      self.h_vzerr = ROOT.TH1F("vzerr","vzerr",100,0,0.02)
      self.h_lepton_dz = ROOT.TH1F("lepton_dz","z distance between the two Z leptons",100,0,0.2)
      self.h_l1v_dz = ROOT.TH1F("l1v_dz","z distance between lepton and vertex",100,0,1.)
      self.h_l2v_dz = ROOT.TH1F("l2v_dz","z distance between lepton and vertex",100,0,1.)
      self.h_distance = ROOT.TH1F("distance","vertex/track distance in z",1000,0,10)
      self.h_sig = ROOT.TH1F("sig","vertex/track significance in z",1000,0,10)
      self.h_ratio1 = ROOT.TH1F("ratio1","jet/vertex association ratio v1",100,0,1)
      self.h_ratio2 = ROOT.TH1F("ratio2","jet/vertex association ratio v2",100,0,1)
      self.h_ratio3 = ROOT.TH1F("ratio3","jet/vertex association ratio v3",100,0,1)
      self.h_goodevent = ROOT.TH1F("goodevent","pass or not Z+jet to vertex association",2,0,2)
      # prepare handles
      self.jetHandle = Handle ("vector<pat::Jet>")
      self.zHandle = Handle ("vector<reco::CompositeCandidate>")
      self.vertexHandle = Handle ("vector<reco::Vertex>")
      self.jetlabel = (jetlabel)
      self.zlabel = (zlabel)
      self.vertexlabel = (vertexlabel)
    
    def processEvent(self,event, weight = 1.):
      # load event
      event.getByLabel (self.jetlabel,self.jetHandle)
      event.getByLabel (self.zlabel,self.zHandle)
      event.getByLabel (self.vertexlabel,self.vertexHandle)
      jets = self.jetHandle.product()
      zs = self.zHandle.product()
      vs = self.vertexHandle.product()
      self.h_nvertices.Fill(vs.size(), weight) # control plot
      sigcut = 5.
      # only events with one Z candidate
      if zs.size()==0 : return
      # select the Z
      bestZ = zs[0]
      bestM = -1000.
      for z in zs :
        if abs(z.mass()-91.1876)<abs(bestM-91.1876) :
          bestM = z.mass()
          bestZ = z
      # select the vertex
      vertex = findPrimaryVertex(bestZ, vs)
      self.h_vx.Fill(vertex.x(), weight) # control plot
      self.h_vy.Fill(vertex.y(), weight) # control plot
      self.h_vz.Fill(vertex.z(), weight) # control plot
      self.h_vxerr.Fill(vertex.xError(), weight) # control plot
      self.h_vyerr.Fill(vertex.yError(), weight) # control plot
      self.h_vzerr.Fill(vertex.zError(), weight) # control plot
      # relevant quantities to monitor: Z vs primary vertex
      lepton1 = bestZ.daughter(0)
      lepton2 = bestZ.daughter(1)
      self.h_lepton_dz.Fill(abs(lepton1.vz()-lepton2.vz()), weight)  # control plot
      self.h_l1v_dz.Fill(abs(lepton1.vz()-vertex.z()), weight) # control plot
      self.h_l2v_dz.Fill(abs(lepton2.vz()-vertex.z()), weight) # control plot
      # relevant quantities to monitor: jets vs primary vertex
      for jet in jets: 
        ptsum = 0.
        ptsumx = 0.
        ptsumy = 0.
        ptsumall = 0.
        #for i in range(jet.getPFConstituents().size()):
        #  if jet.getPFConstituent(i).trackRef().isNull():
        #    continue
        #  distance = (jet.getPFConstituent(i).vz() - vertex.z())
        #  self.h_distance.Fill(distance, weight)
        #  error = (jet.getPFConstituent(i).trackRef().dzError()**2 + vertex.zError()**2)**(1/2.)
        #  #error = vertex.zError()
        #  sig = distance/error
        #  self.h_sig.Fill(sig, weight) # control plot
        #  if abs(sig)<sigcut :
        #    ptsum += jet.getPFConstituent(i).pt()
        #    ptsumx += jet.getPFConstituent(i).px()
        #    ptsumy += jet.getPFConstituent(i).py()
        #  ptsumall += jet.getPFConstituent(i).pt()
        #self.h_ratio1.Fill(ptsum/jet.et(), weight) # control plot
        #if ptsumall>0 : 
        #  ratio = ptsum/ptsumall
        #else:
        #  ratio = -1.
        #self.h_ratio2.Fill(ratio, weight) # control plot
        #self.h_ratio3.Fill((ptsumx**2+ptsumy**2)**(0.5)/jet.et(), weight) # control plot
      self.h_goodevent.Fill(checkVertexAssociation(bestZ, jets, vs), weight)
    
    def endJob(self):
      self.dir.cd()
      self.dir.Write()
      if not self.f is None:
        self.f.Close()

def runTest():
  controlPlots = VertexAssociationControlPlots()
  path="/storage/data/cms/store/user/favereau/MURun2010B-DiLeptonMu-Dec22/"
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

