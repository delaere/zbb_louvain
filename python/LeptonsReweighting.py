from DataFormats.FWLite import Events, Handle
from eventSelection import *
from zbbCommons import zbblabel, zbbsystematics
from math import sqrt
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
     #self.rhoHandle_ = Handle ("double")
     # the efficiency maps

     ## CAVEAT: systematics due to TnP method still missing.

     self._elePidWeight = PtEtaMap([],[0.9, 1.44],
                                   [[(0.997,0.0036), (1.00,0.0045), (1.01,0.0055)]])
     self._eleIsoWeight = PtEtaMap([],[0.9, 1.44],
                                   [[(1.00,0.0041), (0.993,0.0055), (1.010,0.008)]])
     
     self._ele17TrgWeight = PtEtaMap([30,50],[1.4],
                                        [[(0.983,0.0012), (0.982,0.0028)],
                                         [(0.995,0.0026), (0.995,0.0048)],
                                         [(0.998,0.0041), (0.998,0.0006)]])
     self._ele8TrgWeight  = PtEtaMap([30,50],[1.4],
                                        [[(0.995,0.0012), (0.998,0.0012)],
                                         [(0.998,0.0002), (0.999,0.0003)],
                                         [(0.999,0.0003), (0.999,0.0004)]])
     
     ## CAVEAT: systematics due to TnP method still missing.
     
     self._muPidWeight  = PtEtaMap([],[0.9,2.1],
                                   [[(0.995,0.001), (0.972,0.0012), (0.978,0.0041)]])
     self._muIsoWeight  = PtEtaMap([],[0.9,2.1],
                                   [[(0.9926,0.0008), (0.998,0.0008), (1.010,0.0027)]]) 
     self._mu7TrgWeight = PtEtaMap([],[1.2],
                                   [[(0.971,0.0018), (0.948,0.0031)]])
     self._mu8Trg_Mu13Mu8_Weight = PtEtaMap([30,50],[1.2],
                                   [[(0.968,0.0014), (0.935,0.0023)],
                                    [(0.967,0.0007), (0.933,0.0012)],
                                    [(0.968,0.0010), (0.939,0.0019)]])
     self._mu13Trg_Mu13Mu8_Weight = PtEtaMap([30,50],[1.2],
                                   [[(0.967,0.0015), (0.924,0.0025)],
                                    [(0.967,0.0007), (0.927,0.0013)],
                                    [(0.968,0.0010), (0.934,0.0019)]])

     self._mu8Trg_Mu17Mu8_Weight = PtEtaMap([30,50],[1.2],
                                   [[(0.962,0.0038), (0.919,0.0037)],
                                    [(0.967,0.0010), (0.929,0.0019)],
                                    [(0.967,0.0015), (0.930,0.0032)]])
     self._mu17Trg_Mu17Mu8_Weight = PtEtaMap([30,50],[1.2],
                                   [[(0.960,0.0023), (0.907,0.0036)],
                                    [(0.965,0.0010), (0.919,0.0020)],
                                    [(0.966,0.0014), (0.923,0.0033)]])
    
   def uncertainty_ee(self,e1,e2):
     """Relative uncertainty on the total weight.
        We assume the different contributions to be uncorrelated and sum the relative uncertainties in quadrature."""
     # particle id
     unc =  (self._elePidWeight[(e1.pt(),e1.eta())][1]/self._elePidWeight[(e1.pt(),e1.eta())][0] +  \
             self._elePidWeight[(e2.pt(),e2.eta())][1]/self._elePidWeight[(e2.pt(),e2.eta())][0])**2
     # isolation
     unc += (self._eleIsoWeight[(e1.pt(),e1.eta())][1]*self._eleIsoWeight[(e1.pt(),e1.eta())][0] +  \
             self._eleIsoWeight[(e2.pt(),e2.eta())][1]*self._eleIsoWeight[(e2.pt(),e2.eta())][0])**2
     # trigger (approximate)
     unc += (abs(self._ele8TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][1]+  \
                self._ele17TrgWeight[(e1.pt(),e1.eta())][1]*self._ele8TrgWeight[(e2.pt(),e2.eta())][0]-   \
                self._ele17TrgWeight[(e1.pt(),e1.eta())][1]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]-  \
                self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][1])/ \
             (self._ele8TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]+     \
              self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele8TrgWeight[(e2.pt(),e2.eta())][0]-     \
              self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]))**2
     unc += ((self._ele8TrgWeight[(e1.pt(),e1.eta())][1]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]+     \
             self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele8TrgWeight[(e2.pt(),e2.eta())][1])/     \
            (self._ele8TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]+      \
             self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele8TrgWeight[(e2.pt(),e2.eta())][0]-      \
             self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]))**2
     #outcome
     return sqrt(unc)
  
   def weight_ee(self,e1,e2):
     """Event weight for di-electrons."""
     # particle id
     pid_sf_run2011 = self._elePidWeight[(e1.pt(),e1.eta())][0]*self._elePidWeight[(e2.pt(),e2.eta())][0]
     # isolation
     iso_sf_run2011 = self._eleIsoWeight[(e1.pt(),e1.eta())][0]*self._eleIsoWeight[(e2.pt(),e2.eta())][0]
     # trigger
     hlt_sf_run2011AB = self._ele8TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]+ \
                        self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele8TrgWeight[(e2.pt(),e2.eta())][0]- \
                        self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]

     lw = (pid_sf_run2011*iso_sf_run2011*hlt_sf_run2011AB)

     if abs(zbbsystematics.LeptonTnPfactor)<0.01 :
       return lw
     else:
       return lw * (1+zbbsystematics.LeptonTnPfactor*self.uncertainty_ee(e1,e2))

   def uncertainty_mm(self,m1,m2):
     """Relative uncertainty on the total weight.
        We assume the different contributions to be uncorrelated and sum the relative uncertainties in quadrature."""
     # particle id
     unc =  (self._muPidWeight[(e1.pt(),e1.eta())][1]/self._muPidWeight[(e1.pt(),e1.eta())][0] +  \
             self._muPidWeight[(e2.pt(),e2.eta())][1]/self._muPidWeight[(e2.pt(),e2.eta())][0])**2
     # isolation
     unc += (self._muIsoWeight[(e1.pt(),e1.eta())][1]*self._muIsoWeight[(e1.pt(),e1.eta())][0] +  \
             self._muIsoWeight[(e2.pt(),e2.eta())][1]*self._muIsoWeight[(e2.pt(),e2.eta())][0])**2
     # trigger (approximate)
     hlt_sf_run2011_a_unc = (self._mu7TrgWeight [(m1.pt(),m1.eta())][1]/self._mu7TrgWeight [(m1.pt(),m1.eta())][0] + \
                             self._mu7TrgWeight [(m2.pt(),m2.eta())][1]/self._mu7TrgWeight [(m2.pt(),m2.eta())][0])**2
     hlt_sf_run2011_b_unc = (abs(self._mu8Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][1]+  \
                                 self._mu13Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][1]*self._mu8Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][0]-   \
                                 self._mu13Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][1]*self._mu13Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][0]-  \
                                 self._mu13Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][1])/ \
                             (self._mu8Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][0]+     \
                              self._mu13Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][0]-     \
                              self._mu13Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][0]))**2
     hlt_sf_run2011_b_unc += ((self._mu8Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][1]*self._mu13Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][0]+     \
                              self._mu13Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][1])/     \
                             (self._mu8Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][0]+      \
                              self._mu13Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][0]-      \
                              self._mu13Trg_Mu13Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(e2.pt(),e2.eta())][0]))**2
     hlt_sf_run2011_c_unc = (abs(self._mu8Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][1]+  \
                                 self._mu17Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][1]*self._mu8Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][0]-   \
                                 self._mu17Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][1]*self._mu17Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][0]-  \
                                 self._mu17Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][1])/ \
                             (self._mu8Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][0]+     \
                              self._mu17Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][0]-     \
                              self._mu17Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][0]))**2
     hlt_sf_run2011_c_unc += ((self._mu8Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][1]*self._mu17Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][0]+     \
                              self._mu17Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][1])/     \
                             (self._mu8Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][0]+      \
                              self._mu17Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][0]-      \
                              self._mu17Trg_Mu17Mu8_Weight[(e1.pt(),e1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(e2.pt(),e2.eta())][0]))**2
     unc += 0.002*hlt_sf_run2011_a_unc + 0.643*hlt_sf_run2011_b_unc + 0.024*hlt_sf_run2011_c_unc
     #outcome
     return sqrt(unc)

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
     hlt_sf_run2011_a = self._mu7TrgWeight [(m1.pt(),m1.eta())][0]*self._mu7TrgWeight [(m2.pt(),m2.eta())][0]

     hlt_sf_run2011_b = self._mu8Trg_Mu13Mu8_Weight [(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0] + \
                        self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight [(m2.pt(),m2.eta())][0] - \
                        self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]

     hlt_sf_run2011_c = self._mu8Trg_Mu17Mu8_Weight [(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0] + \
                        self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight [(m2.pt(),m2.eta())][0] - \
                        self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]
     
     lw *= (0.044*hlt_sf_run2011_a+0.802*hlt_sf_run2011_b+0.154* hlt_sf_run2011_c) ##percentage according to the lumi in which they were not prescaled.

     if abs(zbbsystematics.LeptonTnPfactor)<0.01 :
       return lw
     else:
       return lw * (1+zbbsystematics.LeptonTnPfactor*self.uncertainty_mm(m1,m2))

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
         #fwevent.getByLabel("kt6PFJetsForIsolation","rho",self.rhoHandle_)
         #rho = self.rhoHandle_.product()
         bestZcandidate = findBestCandidate(muChannel, vertex, zCandidatesMu, zCandidatesEle)
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

