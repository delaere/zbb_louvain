from DataFormats.FWLite import Events, Handle
from eventSelection import *
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
     # the efficiency maps
     self._elePidWeight = PtEtaMap([50],[0.8, 1.44, 2.0],
                                   [[(0.9890,0.005), (0.993601,0.005), (0.974384,0.005), (1.00543,0.005)], 
                                    [(0.9351,0.005), (1.006160,0.007), (0.937660,0.006), (1.01478,0.009)]])
     self._eleIsoWeight = PtEtaMap([50],[1.6],
                                   [[(1.00509,0.005), (0.993324,0.005)], 
                                    [(1.04163,0.005), (1.032000,0.006)]])
     self._eleTrgWeight = PtEtaMap([50],[1.6],
                                   [[(1.00789,0.005), (1.00789,0.005)], 
                                    [(1.00897,0.005), (1.00897,0.005)]])
     self._muPidWeight  = PtEtaMap([50],[1.2],
                                   [[(0.992,0.004), (0.995,0.004)], 
                                    [(0.990,0.004), (0.998,0.005)]])
     self._muIsoWeight  = PtEtaMap([50],[1.2],
                                   [[(1.006,0.004), (1.003,0.004)], 
                                    [(0.999,0.004), (1.000,0.005)]])
     self._mu7TrgWeight = PtEtaMap([],[0.9, 1.5],
                                   [[(0.970,0.0010), (0.958,0.0010), (0.915,0.0050)]])
     self._mu8TrgWeight = PtEtaMap([],[0.9, 1.5],
                                   [[(0.978,0.0006), (0.971,0.0010), (0.924,0.0040)]])
     self._mu13TrgWeight= PtEtaMap([],[0.9, 1.5],
                                   [[(0.976,0.0007), (0.965,0.0010), (0.901,0.0040)]])
 
   def weight_ee(self,e1,e2):
     """Event weight for di-electrons."""
     lw = 1.
     # particle id
     lw *= self._elePidWeight[(e1.pt(),e1.eta())][0]
     lw *= self._elePidWeight[(e2.pt(),e2.eta())][0]
     # isolation
     lw *= self._eleIsoWeight[(e1.pt(),e1.eta())][0]
     lw *= self._eleIsoWeight[(e2.pt(),e2.eta())][0]
     # trigger
     lw *= self._eleTrgWeight[(e1.pt(),e1.eta())][0]
     lw *= self._eleTrgWeight[(e2.pt(),e2.eta())][0]
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
     lw *= (0.18*hlt_sf_run2011A1+0.82*hlt_sf_run2011A2)
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
         fwevent.getByLabel ("Ztighttight", self.zmuHandle_)
         zCandidatesMu = self.zmuHandle_.product()
         fwevent.getByLabel ("Zelel", self.zeleHandle_)
         zCandidatesEle = self.zeleHandle_.product()
         bestZcandidate = findBestCandidate(muChannel, zCandidatesMu, zCandidatesEle)
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

