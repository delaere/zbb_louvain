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
   
     # ===================== ELECTRONS ========== 
     # NEW SF (13-11-2012): finer binning, Z inclusive, updated according to POG reccomendations
     # Systematics taken from the difference between two methods (counting vs fitting) and added in quadrature.

     self._elePidWeight = PtEtaMap([30,40,50],[0.8, 1.444, 1.55, 2.0],
                                   [[(0.998,sqrt(0.011**2+0.005**2)), (1.01,sqrt(0.0093**2+0.015**2)), (1.01,sqrt(0.021**2+0.0)), (0.996,sqrt(0.0084**2+0.003**2)), (0.999,sqrt(0.0086**2+0.005**2))],      # 20-30 GeV
                                    [(0.994,sqrt(0.017**2+0.001**2)), (0.995,sqrt(0.0023**2+0.001**2)), (0.994,sqrt(0.0058**2+0.002**2)), (0.993,sqrt(0.0033**2+0.001**2)), (0.993,sqrt(0.0038**2+0.0))],   # 30-40 GeV
                                    [(0.997,sqrt(0.0002**2+0.001**2)), (0.99,sqrt(0.0012**2+0.0)), (0.988,sqrt(0.0047**2+0.003**2)), (1.00,sqrt(0.0043**2+0.0)), (0.993,sqrt(0.0029**2+0.0))],
     # 40-50 GeV
                                    [(0.996,sqrt(0.0022**2+0.001**2)), (0.996,sqrt(0.0028**2+0.005**2)), (1.01,sqrt(0.002**2+0.01**2)), (1.00,sqrt(0.0037**2+0.0)), (0.996,sqrt(0.005**2+0.001**2))]])      # 50-200 GeV
 
     
     self._eleIsoWeight = PtEtaMap([30,40,50],[0.8, 1.444, 1.55, 2.0],
                                   [[(0.983,sqrt(0.0091**2+0.005**2)), (0.957,sqrt(0.010**2+0.011**2)), (0.894, sqrt(0.036**2+0.019**2)), (1.02, sqrt(0.017**2+0.01**2)), (1.01, sqrt(0.015**2+0.01**2))],   # 20-30 GeV
                                    [(0.993,sqrt(0.0032**2+0.003**2)), (0.982,sqrt(0.004**2+0.001**2)), (0.969, sqrt(0.019**2+0.006**2)), (0.987,sqrt(0.0075**2+0.005**2)), (1.01,sqrt(0.0042**2+0.0))],     # 30-40 GeV
                                    [(0.993,sqrt(0.0011**2+0.0)), (0.99, sqrt(0.0038**2+0.001**2)), (0.981,sqrt(0.025**2+0.003**2)), (0.994,sqrt(0.0027**2+0.002**2)), (1.01,sqrt(0.0036**2+0.012**2))],     # 40-50 GeV
                                    [(0.993,sqrt(0.0057**2+0.001**2)), (0.99, sqrt(0.0022**2+0.0)), (0.943,sqrt(0.011**2+0.023**2)), (1.00, sqrt(0.0045**2+0.016**2)), (1.03,sqrt(0.0064**2+0.0))]])         # 50-200 GeV

     #===== electron trigger ======================
     self._ele17TrgWeight = PtEtaMap([30,40,50],[0.8, 1.444, 1.55, 2.0],
                                   [[(0.984,0.0019), (0.986,0.0021), (1.00,0.0), (0.988,0.0037), (0.98,0.0038)],       # 20-30 GeV
                                    [(0.994,0.0012), (0.995,0.0003), (1.00,0.0), (0.994,0.0012), (0.995,0.001)],       # 30-40 GeV
                                    [(0.995,0.0046), (0.997,0.0005),  (1.00,0.00), (0.995,0.0009), (0.997,0.0014)],    # 40-50 GeV
                                    [(0.998,0.00047), (0.997,0.00075), (1.00,0.00), (0.998,0.00094), (0.998,0.0013)]]) # 50-200 GeV

     self._ele8TrgWeight  = PtEtaMap([30,40,50],[0.8, 1.444, 1.55, 2.0],
                                   [[(0.994,0.012), (0.998,0.0011),   (1.00,0.00), (0.997,0.0018), (0.997,0.0017)],     # 20-30 GeV
                                    [(0.997,0.0004), (0.998,0.00036),  (1.00,0.00), (0.999,0.00055), (0.999,0.00059)],  # 30-40 GeV
                                    [(0.998,0.00029), (0.99,0.00024),  (1.00,0.00), (0.998,0.00032), (1.00,0.00011)],   # 40-50 GeV
                                    [(0.999,0.00035), (0.999,0.00048), (1.00,0.00), (0.99,0.00065), (0.999,0.00074)]])  # 50-200 GeV
     
     ## Note1: Trigger efficiency in the crack is assumed to be 1.00. The reason? not enough electrons in that bin at this stage to compute the efficiencies.
     ## Note2: Systematics for the trigger not included, asked to POG how to estimate 

     # ===================== MUONS ========== 
     ## CAVEAT: systematics assumed to come only from background modelling and added in quadrature ( https://twiki.cern.ch/twiki/bin/view/CMS/MuonTagAndProbe#Systematic_uncertainties )
     
     self._muPidWeight  = PtEtaMap([],[0.9,2.1],
                                   [[(0.995,sqrt(0.001**2+0.002**2)), (0.972,sqrt(0.0012**2+0.004**2)), (0.978,sqrt(0.0041**2+0.004**2))]])
     self._muIsoWeight  = PtEtaMap([],[0.9,2.1],
                                   [[(0.9926,sqrt(0.0008**2+0.002**2)), (0.998,sqrt(0.0008**2+0.004**2)), (1.010,sqrt(0.0027**2+0.004**2))]]) 

     #===== muon trigger=====================
     self._mu7TrgWeight = PtEtaMap([],[1.2],
                                   [[(0.971,sqrt(0.0018**2+0.0005**2)), (0.948,sqrt(0.0031**2+0.0005**2))]])
     self._mu8Trg_Mu13Mu8_Weight = PtEtaMap([30,50],[1.2],
                                   [[(0.968,sqrt(0.0014**2+0.0005**2)), (0.935,sqrt(0.0023**2+0.0005**2))],
                                    [(0.967,sqrt(0.0007**2+0.0005**2)), (0.933,sqrt(0.0012**2+0.0005**2))],
                                    [(0.968,sqrt(0.0010**2+0.0005**2)), (0.939,sqrt(0.0019**2+0.0005**2))]])
     self._mu13Trg_Mu13Mu8_Weight = PtEtaMap([30,50],[1.2],
                                   [[(0.967,sqrt(0.0015**2+0.0005**2)), (0.924,sqrt(0.0025**2+0.0005**2))],
                                    [(0.967,sqrt(0.0007**2+0.0005**2)), (0.927,sqrt(0.0013**2+0.0005**2))],
                                    [(0.968,sqrt(0.0010**2+0.0005**2)), (0.934,sqrt(0.0019**2+0.0005**2))]])

     self._mu8Trg_Mu17Mu8_Weight = PtEtaMap([30,50],[1.2],
                                   [[(0.962,sqrt(0.0038**2+0.0005**2)), (0.919,sqrt(0.0037**2+0.0005**2))],
                                    [(0.967,sqrt(0.0010**2+0.0005**2)), (0.929,sqrt(0.0019**2+0.0005**2))],
                                    [(0.967,sqrt(0.0015**2+0.0005**2)), (0.930,sqrt(0.0032**2+0.0005**2))]])
     self._mu17Trg_Mu17Mu8_Weight = PtEtaMap([30,50],[1.2],
                                   [[(0.960,sqrt(0.0023**2+0.0005**2)), (0.907,sqrt(0.0036**2+0.0005**2))],
                                    [(0.965,sqrt(0.0010**2+0.0005**2)), (0.919,sqrt(0.0020**2+0.0005**2))],
                                    [(0.966,sqrt(0.0014**2+0.0005**2)), (0.923,sqrt(0.0033**2+0.0005**2))]])
    
   def uncertainty_ee(self,e1,e2):
     """Relative uncertainty on the total weight.
        We assume the different contributions to be uncorrelated and sum the relative uncertainties in quadrature."""
     # particle id
     unc =  (self._elePidWeight[(e1.pt(),e1.eta())][1]/self._elePidWeight[(e1.pt(),e1.eta())][0] +  \
             self._elePidWeight[(e2.pt(),e2.eta())][1]/self._elePidWeight[(e2.pt(),e2.eta())][0])**2
     # isolation
     unc += (self._eleIsoWeight[(e1.pt(),e1.eta())][1]/self._eleIsoWeight[(e1.pt(),e1.eta())][0] +  \
             self._eleIsoWeight[(e2.pt(),e2.eta())][1]/self._eleIsoWeight[(e2.pt(),e2.eta())][0])**2
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
     # particle ID
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
     # particle ID
     unc =  (self._muPidWeight[(m1.pt(),m1.eta())][1]/self._muPidWeight[(m1.pt(),m1.eta())][0] +  \
             self._muPidWeight[(m2.pt(),m2.eta())][1]/self._muPidWeight[(m2.pt(),m2.eta())][0])**2
     # isolation
     unc += (self._muIsoWeight[(m1.pt(),m1.eta())][1]/self._muIsoWeight[(m1.pt(),m1.eta())][0] +  \
             self._muIsoWeight[(m2.pt(),m2.eta())][1]/self._muIsoWeight[(m2.pt(),m2.eta())][0])**2
     # trigger (approximate)
     hlt_sf_run2011_a_unc = (self._mu7TrgWeight [(m1.pt(),m1.eta())][1]/self._mu7TrgWeight [(m1.pt(),m1.eta())][0] + \
                             self._mu7TrgWeight [(m2.pt(),m2.eta())][1]/self._mu7TrgWeight [(m2.pt(),m2.eta())][0])**2
     hlt_sf_run2011_b_unc = (abs(self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][1]+  \
                                 self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-   \
                                 self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-  \
                                 self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][1])/ \
                             (self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
                              self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-     \
                              self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
     hlt_sf_run2011_b_unc += ((self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
                              self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][1])/     \
                             (self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]+      \
                              self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-      \
                              self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
     hlt_sf_run2011_c_unc = (abs(self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][1]+  \
                                 self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-   \
                                 self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-  \
                                 self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][1])/ \
                             (self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
                              self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-     \
                              self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
     hlt_sf_run2011_c_unc += ((self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
                              self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][1])/     \
                             (self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]+      \
                              self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-      \
                              self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
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

