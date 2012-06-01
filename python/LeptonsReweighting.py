from DataFormats.FWLite import Events, Handle
from eventSelection import *
from zbbCommons import zbblabel
#from myFuncTimer import print_timing

class PtEtaMap:
   """A binned map in pt and eta.
      Bins are defined at construction time by defining the bin edges.
      It always extends from -inf to +inf.
      Values are tuples (value,error). """

   def __init__(self,ptbins,etabins,data=None):
     """Construct a PtEtaMap. If no data is given, it is initialized at zero."""
     self._ptbins = ptbins
     self._etabins = etabins
     if data is not None:
       self._data = data
     else:
       self._data = [ [ (0,0) for i in range(len(self._etabins)+1) ] for i in range(len(self._ptbins)+1) ]
     self.__check()

   def __setitem__(self, key, item):
     """Set the (value,error) for the bin at (pt,eta)."""
     assert isinstance(key,list) and isinstance(item,list) and len(key)==2 and len(item)==2
     self._data[self.__ptBin(key[0])][self.__etaBin(key[1])] = item

   def __getitem__(self, key):
     """Get the (value,error) for the bin at (pt,eta)."""
     return self._data[self.__ptBin(key[0])][self.__etaBin(key[1])]

   def value(self,pt,eta):
     """Return the value for pt and eta."""
     return self._data[self.__ptBin(pt)][self.__etaBin(eta)][0]

   def error(self,pt,eta):
     """Return the error for pt and eta."""
     return self._data[self.__ptBin(pt)][self.__etaBin(eta)][1]

   def __check(self):
     """Do some basic sanity checks"""
     if len(self._data)!=len(self._ptbins)+1: 
       raise IndexError('Pt bins mismatch')
     for ptbin in self._data:
       if len(ptbin)!=len(self._etabins)+1:
         raise IndexError('Eta bins mismatch')

   def __ptBin(self,pt):
     """Return the bin for pt."""
     if len(self._ptbins)>0:
       return reduce(lambda x,y:x+y,map(lambda x:pt>x,self._ptbins))
     else:
       return 0

   def __etaBin(self,eta):
     """Return the bin for eta."""
     if len(self._etabins)>0:
       return reduce(lambda x,y:x+y,map(lambda x:abs(eta)>x,self._etabins))
     else:
       return 0

   def __repr__(self):
     representation  = "Pt bins: " + repr(self._ptbins) + "\n"
     representation += "Eta bins: " + repr(self._etabins) + "\n"
     representation += "Data:" + "\n" + repr(self._data)
     return representation

   def __len__(self): 
     return (len(self._etabins)+1)*(len(self._ptbins)+1)

class LeptonsReWeighting:
   """A class to reweight MC to fix lepton efficiency."""

   def __init__(self):
     # handle to event objects
     self.zmuHandle_  = Handle ("vector<reco::CompositeCandidate>")
     self.zeleHandle_ = Handle ("vector<reco::CompositeCandidate>")
     self.vertexHandle_ = Handle ("vector<reco::Vertex>")
     self.rhoHandle_ = Handle ("double")
     # the efficiency maps
     self._elePidWeight_A = PtEtaMap([50],[0.8, 1.44, 2.0],
                                   [[(1.002,0.006), (1.001,0.007), (1.009,0.008), (1.008,0.010)], 
                                    [(1.004,0.005), (0.984,0.029), (0.993,0.009), (0.944,0.020)]])
     self._eleIsoWeight_A = PtEtaMap([50],[1.6],
                                   [[(1.004,0.006), (1.043,0.007)], 
                                    [(0.988,0.006), (1.013,0.012)]])
     self._ele17TrgWeight_A1 = PtEtaMap([],[0.8, 1.6],
                                        [[(0.99,0.010), (0.99,0.010), (0.99,0.010)]])
     self._ele8TrgWeight_A1  = PtEtaMap([],[0.8, 1.6],
                                        [[(0.99,0.010), (0.99,0.010), (0.99,0.010)]])
     self._ele17TrgWeight_A2 = PtEtaMap([],[0.8, 1.6],
                                        [[(0.990,0.001), (0.989,0.001), (0.989,0.001)]])
     self._ele8TrgWeight_A2  = PtEtaMap([],[0.8, 1.6],
                                        [[(0.991,0.001), (0.989,0.001), (0.989,0.001)]])
     
     self._muPidWeight  = PtEtaMap([50],[1.2],
                                   [[(0.995,0.004), (0.993,0.004)], 
                                    [(0.987,0.004), (0.996,0.005)]])
     self._muIsoWeight  = PtEtaMap([50],[1.2],
                                   [[(1.022,0.004), (1.017,0.004)], 
                                    [(1.001,0.004), (1.002,0.005)]])
     self._mu7TrgWeight = PtEtaMap([],[0.9, 1.5],
                                   [[(0.971,0.0010), (0.957,0.0010), (0.954,0.0050)]])
     self._mu8TrgWeight = PtEtaMap([],[0.9, 1.5],
                                   [[(0.973,0.0010), (0.964,0.0010), (0.952,0.0040)]])
     self._mu13TrgWeight = PtEtaMap([],[0.9, 1.5],
                                   [[(0.973,0.0010), (0.962,0.0010), (0.946,0.0040)]])
 
   def weight_ee(self,e1,e2):
     """Event weight for di-electrons."""
     # particle id
     pid_sf_run2011A = self._elePidWeight_A[(e1.pt(),e1.eta())][0]*self._elePidWeight_A[(e2.pt(),e2.eta())][0]
     # isolation
     iso_sf_run2011A = self._eleIsoWeight_A[(e1.pt(),e1.eta())][0]*self._eleIsoWeight_A[(e2.pt(),e2.eta())][0]
     # trigger
     hlt_sf_run2011A1 = self._ele8TrgWeight_A1[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight_A1 [(e2.pt(),e2.eta())][0]+ \
                        self._ele17TrgWeight_A1[(e1.pt(),e1.eta())][0]*self._ele8TrgWeight_A1 [(e2.pt(),e2.eta())][0]- \
                        self._ele17TrgWeight_A1[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight_A1[(e2.pt(),e2.eta())][0]
     hlt_sf_run2011A2 = self._ele8TrgWeight_A2[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight_A2 [(e2.pt(),e2.eta())][0]+ \
                        self._ele17TrgWeight_A2[(e1.pt(),e1.eta())][0]*self._ele8TrgWeight_A2 [(e2.pt(),e2.eta())][0]- \
                        self._ele17TrgWeight_A2[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight_A2[(e2.pt(),e2.eta())][0]
     #lw = (0.5*pid_sf_run2011A1*iso_sf_run2011A1*hlt_sf_run2011A1)+(0.5*pid_sf_run2011A2*iso_sf_run2011A2*hlt_sf_run2011A2)
     lw = (pid_sf_run2011A*iso_sf_run2011A*0.5*(hlt_sf_run2011A1+hlt_sf_run2011A2))
     
     return lw

   def weight_mm(self,m1,m2):
     """Event weight for di-muons."""
     lw = 1.
     # particle id
     lw *= self._muPidWeight[(m1.pt(),m1.eta())][0]
     lw *= self._muPidWeight[(m2.pt(),m2.eta())][0]
     # isolation
     lw *= self._muIsoWeight[(m1.pt(),m1.eta())][0]
     lw *= self._muIsoWeight[(m2.pt(),m2.eta())][0]
     # trigger
     hlt_sf_run2011A1 = self._mu7TrgWeight [(m1.pt(),m1.eta())][0]*self._mu7TrgWeight [(m2.pt(),m2.eta())][0]
     hlt_sf_run2011A2 = self._mu8TrgWeight [(m1.pt(),m1.eta())][0]*self._mu13TrgWeight[(m2.pt(),m2.eta())][0] + \
                        self._mu13TrgWeight[(m1.pt(),m1.eta())][0]*self._mu8TrgWeight [(m2.pt(),m2.eta())][0] - \
                        self._mu13TrgWeight[(m1.pt(),m1.eta())][0]*self._mu13TrgWeight[(m2.pt(),m2.eta())][0]
     lw *= (0.11*hlt_sf_run2011A1+0.89*hlt_sf_run2011A2)
     return lw

   #@print_timing
   def weight( self, fwevent=None, electrons=None, muons=None, muChannel=True):
     """Lepton eff weight"""
     # if fwevent is defined, get electrons and muons from there
     if not(fwevent is None):
       # sanity check
       if not(electrons is None) or not(muons is None):
         print "Warning: LeptonsReWeighting: electrons and muon collections will be overwritten."
         electrons=None
         muons=None
       # for data, immediately return 1.
       if fwevent.object().event().eventAuxiliary().isRealData():
         return 1.
       # extract the electrons and muons collections from the event.
       else :
         fwevent.getByLabel (zbblabel.zmumulabel, self.zmuHandle_)
         zCandidatesMu = self.zmuHandle_.product()
         fwevent.getByLabel (zbblabel.zelelabel, self.zeleHandle_)
         zCandidatesEle = self.zeleHandle_.product()
         fwevent.getByLabel(zbblabel.vertexlabel,self.vertexHandle_)
         vertices = self.vertexHandle_.product()
         if vertices.size()>0 :
            vertex = vertices[0]
         else:
            vertex = None
         fwevent.getByLabel("kt6PFJetsForIsolation","rho",self.rhoHandle_)
         rho = self.rhoHandle_.product()
         bestZcandidate = findBestCandidate(muChannel, rho, vertex, zCandidatesMu, zCandidatesEle)
         if not bestZcandidate is None:
           if muChannel :
             muons = [ bestZcandidate.daughter(0), bestZcandidate.daughter(1) ]
           else :
             electrons = [ bestZcandidate.daughter(0), bestZcandidate.daughter(1) ]
     # sanity check
     if not(electrons is None) and not(muons is None):
       print "Warning: LeptonsReWeighting: electrons and muon collections are both defined."
     # now compute the weight with electrons and muons that we have
     if not(electrons is None):
       return self.weight_ee(electrons[0],electrons[1])
     if not(muons is None):
       return self.weight_mm(muons[0],muons[1])
     return 1.

