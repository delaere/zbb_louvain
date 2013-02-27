from AnalysisEvent import AnalysisEvent
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
     # the efficiency maps
   
     # ===================== ELECTRONS 2012 A+B+C+D (WP medium) : https://twiki.cern.ch/twiki/bin/view/Main/EGammaScaleFactors2012#2012_8_TeV_data_53X  ==========
     # ===================== ELECTRONS RECO SF assumed ~1 according to e-gamma POG==========
     
     self._eleRecoWeight = PtEtaMap([30,40,50],[0.8, 1.442, 1.556, 2.0],
                                   [[(1.00,0.01), (1.00,0.01), (1.00,0.01), (1.00,0.01), (1.00,0.01)],   # 20-30 GeV
                                    [(1.00,0.01), (1.00,0.01), (1.00,0.01), (1.00,0.01), (1.00,0.01)],   # 30-40 GeV
                                    [(1.00,0.01), (1.00,0.01), (1.00,0.01), (1.00,0.01), (1.00,0.01)],   # 40-50 GeV
                                    [(1.00,0.01), (1.00,0.01), (1.00,0.01), (1.00,0.01), (1.00,0.01)]])  # 50-200 GeV
      
     self._eleIdIsoWeight = PtEtaMap([30,40,50],[0.8, 1.442, 1.556, 2.0],
                                   [[(1.004,sqrt(0.003**2+0.003**2)), (0.975,sqrt(0.013**2 +0.006**2)),  (1.034,sqrt(0.015**2+0.003**2)), (0.983, sqrt(0.006**2+0.009**2)), (1.025,sqrt(0.006**2+0.005**2))],     # 20-30 GeV
                                    [(1.003,sqrt(0.001**2+0.002**2)), (0.984,sqrt(0.001**2 +0.001**2)),  (1.006,sqrt(0.007**2+0.002**2)), (0.990, sqrt(0.003**2+0.001**2)), (1.022,sqrt(0.003**2+0.002**2))],     # 30-40 GeV
                                    [(1.007,sqrt(0.001**2+0.001**2)), (0.992,sqrt(0.001**2 +0.001**2)),  (0.991,sqrt(0.003**2+0.004**2)), (1.006, sqrt(0.002**2+0.002**2)), (1.013,sqrt(0.001**2+0.003**2))],     # 40-50 GeV
                                    [(1.007,sqrt(0.001**2+0.002**2)), (0.995,sqrt(0.002**2 +0.001**2)),  (0.993,sqrt(0.005**2+0.002**2)), (1.007, sqrt(0.003**2+0.0001**2)), (1.009,sqrt(0.002**2+0.001**2))]])    # 50-200 GeV

     #===== electron trigger ( https://indico.cern.ch/getFile.py/access?contribId=60&sessionId=7&resId=0&materialId=slides&confId=219050 ) ======================
     self._ele17TrgWeight = PtEtaMap([30,40,50],[0.8, 1.444, 1.55, 2.0],
                                   [[(0.978,0.0019),  (0.980,0.001), (1.00,0.001), (0.989,0.001), (0.984,0.001)],       # 20-30 GeV
                                    [(0.991,0.0012),  (0.992,0.001), (1.00,0.001), (0.995,0.001), (0.993,0.001)],       # 30-40 GeV
                                    [(0.993,0.0046),  (0.994,0.001), (1.00,0.001), (0.997,0.001), (0.997,0.001)],    # 40-50 GeV
                                    [(0.993,0.00047), (0.995,0.001), (1.00,0.001), (0.997,0.001), (0.996,0.001)]]) # 50-200 GeV

     self._ele8TrgWeight  = PtEtaMap([30,40,50],[0.8, 1.444, 1.55, 2.0],
                                   [[(0.980,0.001), (0.980,0.001), (1.00,0.00), (0.986,0.001), (0.985,0.001)],     # 20-30 GeV
                                    [(0.989,0.001), (0.989,0.001), (1.00,0.00), (0.991,0.001), (0.991,0.001)],  # 30-40 GeV
                                    [(0.991,0.001), (0.991,0.001), (1.00,0.00), (0.994,0.001), (0.993,0.001)],   # 40-50 GeV
                                    [(0.991,0.001), (0.992,0.001), (1.00,0.00), (0.995,0.001), (0.995,0.001)]])  # 50-200 GeV
     
     ## Note1: Trigger efficiency in the crack is assumed to be 1.00. The reason? not enough electrons in that bin at this stage to compute the efficiencies.

     # ===================== MUONS 2012A+B+C+D ========== error is not updated and SFs gave up to 2.1, we assume they are the same between 2.1 and 2.4
     ## CAVEAT: systematics assumed to come only from background modelling and added in quadrature ( https://twiki.cern.ch/twiki/bin/view/CMS/MuonTagAndProbe#Systematic_uncertainties )
     ## recommandation : https://indico.cern.ch/getFile.py/access?contribId=2&resId=0&materialId=slides&confId=233592
     self._muPidWeight  = PtEtaMap([],[0.9,1.2],
                                   [[(0.9939,sqrt(0.0002**2+0.002**2)), (0.9902,sqrt(0.0003**2+0.004**2)), (0.9970,sqrt(0.0003**2+0.004**2))]])
     self._muIsoWeight  = PtEtaMap([],[0.9,1.2],
                                   [[(0.9999,sqrt(0.0001**2+0.002**2)), (1.0013,sqrt(0.0002**2+0.004**2)), (1.0023,sqrt(0.0001**2+0.004**2))]]) 

     ## ============= muon  trigger==================
     ## ============ periodA (calculating the dz cut efficiency)=============
     self._mu8Trg_Mu17Mu8_A_Weight = PtEtaMap([30],[0.9,1.2,2.1],
                                   [[(0.959,sqrt(0.0014**2+0.0005**2)), (0.932,sqrt(0.003**2+0.0005**2)),(0.917,sqrt(0.002**2+0.0005**2)),(0.898,sqrt(0.004**2+0.0005**2))],
                                    [(0.955,sqrt(0.0005**2+0.0005**2)), (0.930,sqrt(0.0011**2+0.0005**2)),(0.905,sqrt(0.001**2+0.0005**2)),(0.913,sqrt(0.0019**2+0.0005**2))]
                                    ])
     self._mu17Trg_Mu17Mu8_A_Weight = PtEtaMap([30],[0.9,1.2,2.1],
                                   [[(0.957,sqrt(0.0014**2+0.0005**2)), (0.919,sqrt(0.0034**2+0.0005**2)),(0.900,sqrt(0.0021**2+0.0005**2)),(0.824,sqrt(0.005**2+0.0005**2))],
                                    [(0.954,sqrt(0.0049**2+0.0005**2)), (0.923,sqrt(0.0017**2+0.0005**2)),(0.896,sqrt(0.0013**2+0.0005**2)),(0.869,sqrt(0.003**2+0.0005**2))]
                                    ])
     self._mu17Trg_Mu17Mu8_dz_A_Weight = PtEtaMap([30],[0.9,1.2,2.1],
                                   [[(0.899,sqrt(0.0021**2+0.0005**2)), (0.912,sqrt(0.0036**2+0.0005**2)),(0.871,sqrt(0.0026**2+0.0005**2)),(0.879,sqrt(0.005**2+0.0005**2))],
                                    [(0.92,sqrt(0.0006**2+0.0005**2)), (0.897,sqrt(0.0014**2+0.0005**2)),(0.841,sqrt(0.0011**2+0.0005**2)),(0.856,sqrt(0.0025**2+0.0005**2))]
                                    ])
     
     ## ============= periodB (dz cut removed) ==============
     self._mu8Trg_Mu17Mu8_B_Weight = PtEtaMap([30],[0.9,1.2,2.1],
                                   [[(0.956,sqrt(0.0061**2+0.0005**2)), (0.928,sqrt(0.0013**2+0.0005**2)),(0.908,sqrt(0.00086**2+0.0005**2)),(0.898,sqrt(0.0018**2+0.0005**2))],
                                    [(0.954,sqrt(0.0021**2+0.0005**2)), (0.925,sqrt(0.0005**2+0.0005**2)),(0.897,sqrt(0.00038**2+0.0005**2)),(0.905,sqrt(0.0008**2+0.0005**2))]
                                    ])
     self._mu17Trg_Mu17Mu8_B_Weight = PtEtaMap([30],[0.9,1.2,2.1],
                                   [[(0.953,sqrt(0.00062**2+0.0005**2)), (0.914,sqrt(0.0014**2+0.0005**2)),(0.891,sqrt(0.0009**2+0.0005**2)),(0.829,sqrt(0.0022**2+0.0005**2))],
                                    [(0.952,sqrt(0.0002**2+0.0005**2)), (0.916,sqrt(0.0005**2+0.0005**2)),(0.887,sqrt(0.0004**2+0.0005**2)),(0.863,sqrt(0.001**2+0.0005**2))]
                                    ])
    
   def uncertainty_ee(self,e1,e2):
     """Relative uncertainty on the total weight.
        We assume the different contributions to be uncorrelated and sum the relative uncertainties in quadrature."""
     # particle id
     unc =  (self._eleRecoWeight[(e1.pt(),e1.eta())][1]/self._eleRecoWeight[(e1.pt(),e1.eta())][0] +  \
             self._eleRecoWeight[(e2.pt(),e2.eta())][1]/self._eleRecoWeight[(e2.pt(),e2.eta())][0])**2
     # isolation
     unc += (self._eleIdIsoWeight[(e1.pt(),e1.eta())][1]/self._eleIdIsoWeight[(e1.pt(),e1.eta())][0] +  \
             self._eleIdIsoWeight[(e2.pt(),e2.eta())][1]/self._eleIdIsoWeight[(e2.pt(),e2.eta())][0])**2
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
     pid_sf_run2011 = self._eleRecoWeight[(e1.pt(),e1.eta())][0]*self._eleRecoWeight[(e2.pt(),e2.eta())][0]
     # isolation 
     iso_sf_run2011 = self._eleIdIsoWeight[(e1.pt(),e1.eta())][0]*self._eleIdIsoWeight[(e2.pt(),e2.eta())][0]
     # trigger
     hlt_sf_run2011AB = self._ele8TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]+ \
                        self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele8TrgWeight[(e2.pt(),e2.eta())][0]- \
                        self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]

     lw = (pid_sf_run2011*iso_sf_run2011*hlt_sf_run2011AB)

     if abs(zbbsystematics.LeptonTnPfactor)<0.01 :
       return lw
     else:
       return lw + zbbsystematics.LeptonTnPfactor*self.uncertainty_ee(e1,e2)

   def uncertainty_mm(self,m1,m2):
     """Relative uncertainty on the total weight.
        We assume the different contributions to be uncorrelated and sum the relative uncertainties in quadrature."""
     # particle ID
     unc =  (self._muPidWeight[(m1.pt(),m1.eta())][1]/self._muPidWeight[(m1.pt(),m1.eta())][0] +  \
             self._muPidWeight[(m2.pt(),m2.eta())][1]/self._muPidWeight[(m2.pt(),m2.eta())][0])**2
     # isolation
     unc += (self._muIsoWeight[(m1.pt(),m1.eta())][1]/self._muIsoWeight[(m1.pt(),m1.eta())][0] +  \
             self._muIsoWeight[(m2.pt(),m2.eta())][1]/self._muIsoWeight[(m2.pt(),m2.eta())][0])**2
##      # trigger (approximate) ==== FIXME!! ===============
##      hlt_sf_run2011_a_unc = (self._mu7TrgWeight [(m1.pt(),m1.eta())][1]/self._mu7TrgWeight [(m1.pt(),m1.eta())][0] + \
##                              self._mu7TrgWeight [(m2.pt(),m2.eta())][1]/self._mu7TrgWeight [(m2.pt(),m2.eta())][0])**2
##      hlt_sf_run2011_b_unc = (abs(self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][1]+  \
##                                  self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-   \
##                                  self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-  \
##                                  self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][1])/ \
##                              (self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
##                               self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-     \
##                               self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
##      hlt_sf_run2011_b_unc += ((self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
##                               self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][1])/     \
##                              (self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]+      \
##                               self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-      \
##                               self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
##      hlt_sf_run2011_c_unc = (abs(self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][1]+  \
##                                  self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-   \
##                                  self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-  \
##                                  self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][1])/ \
##                              (self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
##                               self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-     \
##                               self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
##      hlt_sf_run2011_c_unc += ((self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
##                               self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][1])/     \
##                              (self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]+      \
##                               self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-      \
##                               self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
##      unc += 0.002*hlt_sf_run2011_a_unc + 0.643*hlt_sf_run2011_b_unc + 0.024*hlt_sf_run2011_c_unc
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
     #hlt_sf_run2011_a = self._mu7TrgWeight [(m1.pt(),m1.eta())][0]*self._mu7TrgWeight [(m2.pt(),m2.eta())][0]

     hlt_sf_run2011_a = self._mu17Trg_Mu17Mu8_dz_A_Weight[(m1.pt(),m1.eta())][0] *\
                        (self._mu8Trg_Mu17Mu8_A_Weight [(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_A_Weight[(m2.pt(),m2.eta())][0] + \
                        self._mu17Trg_Mu17Mu8_A_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_A_Weight [(m2.pt(),m2.eta())][0] - \
                        self._mu17Trg_Mu17Mu8_A_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_A_Weight[(m2.pt(),m2.eta())][0])

     hlt_sf_run2011_b = self._mu8Trg_Mu17Mu8_B_Weight [(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_B_Weight[(m2.pt(),m2.eta())][0] + \
                        self._mu17Trg_Mu17Mu8_B_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_B_Weight [(m2.pt(),m2.eta())][0] - \
                        self._mu17Trg_Mu17Mu8_B_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_B_Weight[(m2.pt(),m2.eta())][0]
     
     lw *= 0.966 #(0.13*hlt_sf_run2011_a+0.87* hlt_sf_run2011_b) ##percentage according to the lumi in which they were not prescaled.

     if abs(zbbsystematics.LeptonTnPfactor)<0.01 :
       return lw
     else:
       return lw + zbbsystematics.LeptonTnPfactor*self.uncertainty_mm(m1,m2)

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
         bestZcandidate = fwevent.bestZmumuCandidate if muChannel else fwevent.bestZelelCandidate 
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

