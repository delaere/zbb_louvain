from PatAnalysis.EventSelection import categoryName
from zbbCommons import zbblabel, zbbsystematics, dataDirectory
from math import sqrt
import pickle

##______General functions______

def get_eta_key(eta):

   range =''
   if ( abs(eta)<=0.9):
      range = 'ptabseta<0.9'                  
   elif (abs(eta)> 0.9 and abs(eta)<=1.2):
      range = 'ptabseta0.9-1.2'
   elif (abs(eta)> 1.2 and  abs(eta)<= 2.4 ):
      range = 'ptabseta1.2-2.4'   
   else:
      print 'ERROR: value not in range'
        
   return range

def get_etaFiner_key(eta):

   range= ''
   if (eta>=-2.4 and eta< -2.1):
      range = '-2.4_-2.1'
   elif (eta>=-2.1 and eta< -1.6):
      range = '-2.1_-1.6'
   elif (eta>=-1.6 and  eta< -1.2 ):
      range = '-1.6_-1.2'
   elif (eta>=-1.2 and  eta< -0.9 ):
      range = '-1.2_-0.9'
   elif (eta>=-0.9 and  eta< -0.6 ):
      range = '-0.9_-0.6'
   elif (eta>=-0.6 and  eta< -0.3 ):
      range = '-0.6_-0.3'
   elif (eta>=-0.3 and  eta< -0.2 ):
      range = '-0.3_-0.2'
   elif (eta>=-0.2 and  eta< 0.2 ):
      range = '-0.2_0.2'
   elif (eta>= 0.2 and  eta< 0.3 ):
      range = '0.2_0.3'
   elif (eta>= 0.3 and  eta< 0.6 ):
      range = '0.3_0.6'
   elif (eta>= 0.6 and  eta< 0.9 ):
      range = '0.6_0.9'
   elif (eta>= 0.9 and  eta< 1.2 ):
      range = '0.9_1.2'
   elif (eta>= 1.2 and  eta< 1.6 ):
      range = '1.2_1.6'
   elif (eta>= 1.6 and  eta< 2.1 ):
      range = '1.6_2.1'
   elif (eta>= 2.1 and  eta<= 2.4 ):
      range = '2.1_2.4'
   else:
      print 'ERROR: value not in eta range'

   return range
  
def get_pt_key(pt):
   
   range = ''
   if (pt>=10 and  pt< 20 ):
      range = '10_20'   
   elif (pt>=20 and  pt< 25 ):
      range = '20_25'
   elif (pt>=25 and  pt< 30 ):
      range = '25_30'
   elif (pt>=30 and  pt< 35 ):
      range = '30_35'
   elif (pt>=35 and  pt< 40 ):
      range = '35_40'
   elif (pt>=40 and  pt< 50 ):
      range = '40_50'
   elif (pt>=50 and  pt< 60 ):
      range = '50_60'
   elif (pt>=60 and  pt< 90 ):
      range = '60_90'
   elif (pt>=90 and  pt<140 ):
      range = '90_140'
   elif (pt>= 140 ):
      range = '140_500'
   else:
      print 'ERROR: value not in range'

   return range
         
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

##### period_ABCD______ ID+ISO_SF

class MuonSFMap:
   """A binned map in eta (for the moment) for muon SF.
      Values can be extracted are (value,error). """

   def __init__(self):
     """Construct a MuonSFMap using pikle files."""
     f = open(dataDirectory+'Muon_ID_iso_Efficiencies_Run_2012ABCD_53X.pkl', 'r')
     if f :
        self._map = pickle.load(f)
        self._range = ''
     else :
        print 'ERROR: Input file for muon SF not existing!'

   def value(self,pt,eta,mode):

     """Return the SF or the uncertainty for a given pt and eta."""

     self._range= get_etaFiner_key(eta)

     if mode == '0'  :
        return self._map['combRelIsoPF04dBeta<02_Tight']['etapt20-500_2012ABCD'][self._range]['data/mc']['efficiency_ratio']
     elif mode == '+1'  :
        return self._map['combRelIsoPF04dBeta<02_Tight']['etapt20-500_2012ABCD'][self._range]['data/mc']['err_hi'] 
     elif mode == '-1' :
        return self._map['combRelIsoPF04dBeta<02_Tight']['etapt20-500_2012ABCD'][self._range]['data/mc']['err_low']
     else:  
        print 'ERROR: wrong \'mode\' specified: try \'0\',\'+1\' or \'-1\''
        return 0
        

##### period_AB______Mu17_Mu8_____Leg17
        
class MuonTriggerEffMap_leg17_AB:
   """A binned map in eta only (for the moment) for Trigger efficiencies.
      Values can be extracted are (value,error). """

   def __init__(self):
     """Construct a MuonTriggerEffMap using pikle files."""
     f = open(dataDirectory+'MuonEfficiencies_Run_2012A_2012_B_53X.pkl', 'r')
     if f :
        self._map = pickle.load(f)
        self._eta_range = ''
        self._pt_range = ''
     else :
        print 'ERROR: Input file for Trigger efficiencies not existing!'

   def value(self,pt,eta,mode):

     """Return the eff or the uncertainty for a given pt and eta."""
     
     self._eta_range= get_eta_key(eta)+'_2012B'
     self._pt_range= get_pt_key(pt)

     if mode == '0'  :
        return self._map['DoubleMu17Mu8_Mu17_Tight'][self._eta_range][self._pt_range]['data']['efficiency'] 
     elif mode == '+1'  :
        return self._map['DoubleMu17Mu8_Mu17_Tight'][self._eta_range][self._pt_range]['data']['err_hi']
     elif mode == '-1' : 
        return self._map['DoubleMu17Mu8_Mu17_Tight'][self._eta_range][self._pt_range]['data']['err_low']
     else:  
        print 'ERROR: wrong \'mode\' specified: try \'0\',\'+1\' or \'-1\''
        return 0
        


##### period_AB________Mu17_Mu8_____Leg8

class MuonTriggerEffMap_leg8_AB:
   """A binned map in eta only (for the moment) for Trigger efficiencies.
      Values can be extracted are (value,error). """

   def __init__(self):
     """Construct a MuonTriggerEffMap using pikle files."""
     f = open(dataDirectory+'MuonEfficiencies_Run_2012A_2012_B_53X.pkl', 'r')
     if f :
        self._map = pickle.load(f)
        self._eta_range = ''
        self._pt_range = ''
     else :
        print 'ERROR: Input file for Trigger efficiencies not existing!'
   
   def value(self,pt,eta,mode):

     """Return the eff or the uncertainty for a given pt and eta."""

     self._eta_range= get_eta_key(eta)+'_2012B'
     self._pt_range= get_pt_key(pt)

     if mode == '0'  :
        return self._map['DoubleMu17Mu8_Mu8_Tight'][self._eta_range][self._pt_range]['data']['efficiency'] 
     elif mode == '+1'  :
        return self._map['DoubleMu17Mu8_Mu8_Tight'][self._eta_range][self._pt_range]['data']['err_hi']
     elif mode == '-1' : 
        return self._map['DoubleMu17Mu8_Mu8_Tight'][self._eta_range][self._pt_range]['data']['err_low']
     else:  
        print 'ERROR: wrong \'mode\' specified: try \'0\',\'+1\' or \'-1\''     
        return 0

class LeptonsReWeighting:
   """A class to reweight MC to fix lepton efficiency."""

   def __init__(self):

     
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

     # ===================== Muon ID-ISO 2012A+B+C+D ==========
     # Updated to the values provided by muon POG: https://twiki.cern.ch/twiki/bin/view/CMS/MuonReferenceEffs#2012_data

     self._muIDISOWeight  = MuonSFMap()

     ## ==================== Muon Trigger ==================

     self._muTRIGGERWeight_leg17_A  = MuonTriggerEffMap_leg17_AB()
     self._muTRIGGERWeight_leg8_A  = MuonTriggerEffMap_leg8_AB()

     self._muTRIGGERWeight_leg17_B  = MuonTriggerEffMap_leg17_AB()
     self._muTRIGGERWeight_leg8_B  = MuonTriggerEffMap_leg8_AB()

     ## CAVEAT: C and D have to be updated once available in the muon POG
     
     self._muTRIGGERWeight_leg17_C  = MuonTriggerEffMap_leg17_AB()
     self._muTRIGGERWeight_leg8_C  = MuonTriggerEffMap_leg8_AB()

     self._muTRIGGERWeight_leg17_D  = MuonTriggerEffMap_leg17_AB()
     self._muTRIGGERWeight_leg8_D  = MuonTriggerEffMap_leg8_AB()
         
    
   def uncertainty_ee(self,e1,e2):
     """Relative uncertainty on the total weight.
        We assume the different contributions to be uncorrelated and sum the relative uncertainties in quadrature."""
     # reco
     unc =  (self._eleRecoWeight[(e1.pt(),e1.eta())][1]/self._eleRecoWeight[(e1.pt(),e1.eta())][0] +  \
             self._eleRecoWeight[(e2.pt(),e2.eta())][1]/self._eleRecoWeight[(e2.pt(),e2.eta())][0])**2
     # id-isolation
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
     # ID and isolation uncertainty (TO BE FIXED)
     unc =  (self._muIDISOWeight.value(m1.pt(),m1.eta(),'+1')/self._muIDISOWeight.value(m1.pt(),m1.eta(),'+1')+  \
             self._muIDISOWeight.value(m2.pt(),m2.eta(),'+1')/self._muIDISOWeight.value(m2.pt(),m2.eta(),'+1'))**2
     
##    # trigger (approximate) ==== FIXME!! ===============
##    hlt_sf_run2011_a_unc = (self._mu7TrgWeight [(m1.pt(),m1.eta())][1]/self._mu7TrgWeight [(m1.pt(),m1.eta())][0] + \
##                            self._mu7TrgWeight [(m2.pt(),m2.eta())][1]/self._mu7TrgWeight [(m2.pt(),m2.eta())][0])**2
##    hlt_sf_run2011_b_unc = (abs(self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][1]+  \
##                                self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-   \
##                                self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-  \
##                                self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][1])/ \
##                            (self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
##                             self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-     \
##                             self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
##    hlt_sf_run2011_b_unc += ((self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
##                             self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][1])/     \
##                            (self._mu8Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]+      \
##                             self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]-      \
##                             self._mu13Trg_Mu13Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu13Trg_Mu13Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
##    hlt_sf_run2011_c_unc = (abs(self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][1]+  \
##                                self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-   \
##                                self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-  \
##                                self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][1])/ \
##                            (self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
##                             self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-     \
##                             self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
##    hlt_sf_run2011_c_unc += ((self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][1]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]+     \
##                             self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][1])/     \
##                            (self._mu8Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]+      \
##                             self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu8Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]-      \
##                             self._mu17Trg_Mu17Mu8_Weight[(m1.pt(),m1.eta())][0]*self._mu17Trg_Mu17Mu8_Weight[(m2.pt(),m2.eta())][0]))**2
##    unc += 0.002*hlt_sf_run2011_a_unc + 0.643*hlt_sf_run2011_b_unc + 0.024*hlt_sf_run2011_c_unc
    
     return sqrt(unc)

   def weight_mm(self,m1,m2):
     """Event weight for di-muons."""
     lw = 1.

     # particle id and isolation
     lw *= self._muIDISOWeight.value(m1.pt(),m1.eta(),'0')
     lw *= self._muIDISOWeight.value(m2.pt(),m2.eta(),'0')

     # Trigger
     hlt_sf_run2012_a = (self._muTRIGGERWeight_leg8_A.value(m1.pt(),m1.eta(),'0')*self._muTRIGGERWeight_leg17_A.value(m2.pt(),m2.eta(),'0') +\
                         self._muTRIGGERWeight_leg17_A.value(m1.pt(),m1.eta(),'0')*self._muTRIGGERWeight_leg8_A.value(m2.pt(),m2.eta(),'0') -\
                         self._muTRIGGERWeight_leg17_A.value(m1.pt(),m1.eta(),'0')*self._muTRIGGERWeight_leg17_A.value(m2.pt(),m2.eta(),'0'))

     hlt_sf_run2012_b = (self._muTRIGGERWeight_leg8_B.value(m1.pt(),m1.eta(),'0')*self._muTRIGGERWeight_leg17_B.value(m2.pt(),m2.eta(),'0') +\
                         self._muTRIGGERWeight_leg17_B.value(m1.pt(),m1.eta(),'0')*self._muTRIGGERWeight_leg8_B.value(m2.pt(),m2.eta(),'0') -\
                         self._muTRIGGERWeight_leg17_B.value(m1.pt(),m1.eta(),'0')*self._muTRIGGERWeight_leg17_B.value(m2.pt(),m2.eta(),'0'))
                         
     lw *= (0.5*hlt_sf_run2012_a + 0.5*hlt_sf_run2012_b) ##percentage according to the lumi in which they were not prescaled (apparently same efficinecy for AB)
     #lw *= 0.966 ## temporary solution!

     if abs(zbbsystematics.LeptonTnPfactor)<0.01 :
       return lw
     else:
       return lw + zbbsystematics.LeptonTnPfactor*self.uncertainty_mm(m1,m2)

   def weight( self, fwevent=None, electrons=None, muons=None, category=None, forceMode = None):
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
         if forceMode == "Muon":
           bestZcandidate = fwevent.bestZmumuCandidate
         elif forceMode == "Electron":
           bestZcandidate = fwevent.bestZelelCandidate
         else:
           bestZcandidate = fwevent.bestZcandidate
         if not bestZcandidate is None:
           if bestZcandidate.daughter(0).isMuon():
             muons = [ bestZcandidate.daughter(0), bestZcandidate.daughter(1) ]
           else:
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

