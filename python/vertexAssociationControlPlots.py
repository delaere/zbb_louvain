#! /usr/bin/env python

import ROOT
import sys
from DataFormats.FWLite import Events, Handle
from vertexAssociation import *

class vertexAssociationControlPlots:
    """A class to create control plots for vertex association"""

    def __init__(self, file=None):
      # create output file if needed. If no file is given, it means it is delegated
      if file is None:
        self.f = ROOT.TFile("controlPlots.root", "RECREATE")
        self.dir = self.f.mkdir("vertexAssociation")
        self.owner = True
      else :
        self.f = file
        self.dir = file.pwd()
        self.owner = False
    
    def beginJob(self, jetlabel="cleanPatJets", zlabel="Ztightloose", vertexlabel="goodPV" ):
      # declare histograms
      self.dir.cd()
      self.h_vx = ROOT.TH1F("vx","vx",400,-0.2,0.2)
      self.h_vy = ROOT.TH1F("vy","vy",400,-0.2,0.2)
      self.h_vz = ROOT.TH1F("vz","vz",100,-25,25)
      self.h_vxerr = ROOT.TH1F("vxerr","vxerr",100,0,0.1)
      self.h_vyerr = ROOT.TH1F("vyerr","vyerr",100,0,0.1)
      self.h_vzerr = ROOT.TH1F("vzerr","vzerr",100,0,0.1)
      self.h_lepton_dz = ROOT.TH1F("lepton_dz","z distance between the two Z leptons",100,0,1.)
      self.h_l1v_dz = ROOT.TH1F("l1v_dz","z distance between lepton and vertex",100,0,2.)
      self.h_l2v_dz = ROOT.TH1F("l2v_dz","z distance between lepton and vertex",100,0,2.)
      self.h_distance = ROOT.TH1F("distance","vertex/track distance in z",1000,0,10)
      self.h_sig = ROOT.TH1F("sig","vertex/track significance in z",1000,0,10)
      self.h_ratio1 = ROOT.TH1F("ratio1","jet/vertex association ratio v1",100,0,1)
      self.h_ratio2 = ROOT.TH1F("ratio2","jet/vertex association ratio v2",100,0,1)
      self.h_ratio3 = ROOT.TH1F("ratio3","jet/vertex association ratio v3",100,0,1)
      self.h_goodevent = ROOT.TH1I("goodevent","pass or not Z+jet to vertex association",2,0,2)
      # prepare handles
      self.jetHandle = Handle ("vector<pat::Jet>")
      self.zHandle = Handle ("vector<reco::CompositeCandidate>")
      self.vertexHandle = Handle ("vector<reco::Vertex>")
      self.jetlabel = (jetlabel)
      self.zlabel = (zlabel)
      self.vertexlabel = (vertexlabel)
    
    def processEvent(self,event):
      # load event
      event.getByLabel (self.jetlabel,self.jetHandle)
      event.getByLabel (self.zlabel,self.zHandle)
      event.getByLabel (self.vertexlabel,self.vertexHandle)
      jets = self.jetHandle.product()
      zs = self.zHandle.product()
      vs = self.vertexHandle.product()
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
      self.h_vx.Fill(vertex.x()) # control plot
      self.h_vy.Fill(vertex.y()) # control plot
      self.h_vz.Fill(vertex.z()) # control plot
      self.h_vxerr.Fill(vertex.xError()) # control plot
      self.h_vyerr.Fill(vertex.yError()) # control plot
      self.h_vzerr.Fill(vertex.zError()) # control plot
      # relevant quantities to monitor: Z vs primary vertex
      lepton1 = bestZ.daughter(0)
      lepton2 = bestZ.daughter(1)
      self.h_lepton_dz.Fill(abs(lepton1.vz()-lepton2.vz()))  # control plot
      self.h_l1v_dz.Fill(abs(lepton1.vz()-vertex.z())) # control plot
      self.h_l2v_dz.Fill(abs(lepton2.vz()-vertex.z())) # control plot
      # relevant quantities to monitor: jets vs primary vertex
      for jet in jets: 
        ptsum = 0.
        ptsumx = 0.
        ptsumy = 0.
        ptsumall = 0.
        for i in range(jet.getPFConstituents().size()):
          if jet.getPFConstituent(i).trackRef().isNull():
            continue
          distance = (jet.getPFConstituent(i).vz() - vertex.z())
          self.h_distance.Fill(distance)
          error = (jet.getPFConstituent(i).trackRef().dzError()**2 + vertex.zError()**2)**(1/2.)
          #error = vertex.zError()
          sig = distance/error
          self.h_sig.Fill(sig) # control plot
          if abs(sig)<sigcut :
            ptsum += jet.getPFConstituent(i).pt()
            ptsumx += jet.getPFConstituent(i).px()
            ptsumy += jet.getPFConstituent(i).py()
          ptsumall += jet.getPFConstituent(i).pt()
        self.h_ratio1.Fill(ptsum/jet.et()) # control plot
        if ptsumall>0 : 
          ratio = ptsum/ptsumall
        else:
          ratio = -1.
        self.h_ratio2.Fill(ratio) # control plot
        self.h_ratio3.Fill((ptsumx**2+ptsumy**2)**(0.5)/jet.et()) # control plot
      self.h_goodevent.Fill(checkVertexAssociation(bestZ, jets, vs))
    
    def endJob(self):
      self.f.cd()
      self.f.Write()
      if self.owner:
        self.f.Close()

def runTest():
  controlPlots = vertexAssociationControlPlots()
  files = ["/home/fynu/jdf/scratch/CMSSW_3_9_7/src/Analysis/Analysis/MURun2010B-DiLeptonMu-Dec22Skim_tracks.root"]
#  files = ["/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_10_1_1ji.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_11_1_rUv.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_12_1_55h.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_13_1_6jY.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_14_1_9wH.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_15_1_yTY.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_16_1_aIs.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_17_1_ccv.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_18_1_73c.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_19_1_y3l.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_1_1_Zlh.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_20_1_x6N.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_21_1_p76.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_22_1_KYP.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_23_1_aev.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_24_1_4Uz.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_25_1_wvg.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_26_1_kqK.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_27_1_Pk8.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_28_1_PV6.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_29_1_4jI.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_2_1_Clt.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_30_1_OZC.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_31_1_dZY.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_32_1_tv8.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_33_1_QxH.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_34_1_dpf.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_35_1_gM5.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_36_1_Qr9.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_37_1_Dcx.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_38_1_MM6.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_39_1_eEA.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_3_1_8TE.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_40_1_9Km.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_41_1_7Vi.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_42_1_h7i.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_43_1_D2c.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_44_1_9nZ.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_45_1_ZI2.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_46_1_O6e.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_47_1_wL6.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_48_1_6aV.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_49_1_YD2.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_4_1_QVO.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_50_1_Rh9.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_51_1_ErJ.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_52_1_81z.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_53_1_mo6.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_54_1_fW8.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_55_1_kmS.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_56_1_trf.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_57_1_znE.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_58_1_giA.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_59_1_t8m.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_5_1_0gw.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_60_1_UT7.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_61_1_02X.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_62_1_0mU.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_63_1_4SN.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_64_1_zLt.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_65_1_3Xb.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_66_1_GvE.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_67_1_Kat.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_68_1_fEE.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_69_1_ibF.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_6_1_F3i.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_70_1_P3m.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_71_1_dsR.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_72_1_kDn.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_73_1_tk2.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_74_1_a85.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_75_1_T7O.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_76_1_Y4g.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_77_1_b5T.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_78_1_cjo.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_79_1_GN1.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_7_1_9hj.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_8_1_Vrv.root",
#  "/home/fynu/lceard/store/MURun2010B-DiLeptonMu-Dec22/MURun2010B-DiLeptonMu-Dec22Skim_9_1_tgy.root"]
  events = Events (files)
  controlPlots.beginJob()
  i = 0
  for event in events:
    controlPlots.processEvent(event)
    if i%1000==0 : print "Processing... event ", i
    i += 1
  controlPlots.endJob()

