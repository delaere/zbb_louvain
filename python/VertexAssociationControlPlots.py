from PatAnalysis.BaseControlPlots import BaseControlPlots
from VertexAssociation import *

class VertexAssociationControlPlots(BaseControlPlots):
    """A class to create control plots for vertex association"""

    def __init__(self, dir=None, purpose="vertexAssociation", dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose=purpose, dataset=dataset, mode=mode)
    
    def beginJob(self, sigcut = 2.):
      self.sigcut = sigcut
      # declare histograms
      self.add("nvertices","nvertices",60,-0.5,59.5)
      self.add("vx","vx",400,-0.2,0.2)
      self.add("vy","vy",400,-0.2,0.2)
      self.add("vz","vz",100,-25,25)
      self.add("vxerr","vxerr",100,0,0.01)
      self.add("vyerr","vyerr",100,0,0.01)
      self.add("vzerr","vzerr",100,0,0.02)
      self.add("lepton_dz","z distance between the two Z leptons",100,0,0.2)
      self.add("l1v_dz","z distance between lepton and vertex",100,0,1.)
      self.add("l2v_dz","z distance between lepton and vertex",100,0,1.)
      self.add("lvertex","index of the lepton vertex",20,-0.5,19.5)

    def process(self,event):
      """VertexAssociationControlPlots"""
      result = { }
      result["nvertices"] = event.vertices.size()
      if event.vertices.size()==0 : return result
      vertex = event.vertex
      result["vx"] = vertex.x()
      result["vy"] = vertex.y()
      result["vz"] = vertex.z()
      result["vxerr"] = vertex.xError()
      result["vyerr"] = vertex.yError()
      result["vzerr"] = vertex.zError()
      # relevant quantities to monitor: Z vs primary vertex
      bestZ = event.bestZcandidate
      if bestZ is None: return result
      lepton1 = bestZ.daughter(0)
      lepton2 = bestZ.daughter(1)
      result["lepton_dz"] = abs(lepton1.vz()-lepton2.vz())
      result["l1v_dz"] = abs(lepton1.vz()-vertex.z())
      result["l2v_dz"] = abs(lepton2.vz()-vertex.z())
      result["lvertex"] = findPrimaryVertexIndex(bestZ,event.vertices)
      return result

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], VertexAssociationControlPlots())

