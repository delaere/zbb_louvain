from PatAnalysis.EventSelection import categoryName
from math import sqrt
import pickle
import os
confCfg = os.environ["PatAnalysisCfg"]
if confCfg : from UserCode.zbb_louvain.PatAnalysis.CPconfig import configuration
else : from zbbConfig import configuration

##______General functions______


def get_eta_key(eta):
   range =''
   if ( abs(eta)<=0.9):
      range = 'ptabseta<0.9'
   elif (abs(eta)> 0.9 and abs(eta)<=1.2):
      range = 'ptabseta0.9-1.2'
   elif (abs(eta)> 1.2 and abs(eta)<= 2.1 ):
      range = 'ptabseta1.2-2.1'   
   elif (abs(eta)> 2.1 and abs(eta)<= 2.4 ):
      range = 'ptabseta2.1-2.4'
   else:
      print 'ERROR: value not in range'
              
   return range

def get_eta_trigger_key(eta):
## N.B. needed for a different syntax for the new pkl file :-(
   range =''
   if ( abs(eta)<=0.9):
      range = '0.0,0.9'                  
   elif (abs(eta)> 0.9 and abs(eta)<=1.2):
      range = '0.9,1.2'
   elif (abs(eta)> 1.2 and  abs(eta)<= 2.1 ):
      range = '1.2,2.1'      
   elif (abs(eta)> 2.1 and  abs(eta)<= 2.4 ):
      range = '2.1,2.4'   
   else:
      print 'ERROR: value not in range'

   return range

def get_eta_trigger_key(eta1,eta2):
## N.B. needed for a different syntax for the new pkl file :-(
   range =''
   if (( abs(eta1)<=0.9 and abs(eta2)<=0.9 )):
      range = '(0.0,0.9)(0.0,0.9)'                  
   elif ((abs(eta1)> 0.9 and abs(eta1)<=1.2 and abs(eta2)<=0.9) or (abs(eta2)> 0.9 and abs(eta2)<=1.2 and abs(eta1)<=0.9)):
      range = '(0.9,1.2)(0.0,0.9)'
   elif ((abs(eta1)> 0.9 and abs(eta1)<=1.2 and abs(eta2)> 0.9 and abs(eta2)<=1.2 ) or (abs(eta2)> 0.9 and abs(eta2)<=1.2 and abs(eta1)> 0.9 and abs(eta1)<=1.2 )):
      range = '(0.9,1.2)(0.9,1.2)'
   elif ((abs(eta1)> 1.2 and abs(eta1)<=2.1 and abs(eta2)> 0.9 and abs(eta2)<=1.2 ) or (abs(eta2)> 1.2 and abs(eta2)<=2.1 and abs(eta1)> 0.9 and abs(eta1)<=1.2 )):
      range = '(1.2,2.1)(0.9,1.2)'
   elif ((abs(eta1)> 1.2 and abs(eta1)<=2.1 and abs(eta2)> 1.2 and abs(eta2)<=2.1 )):
      range = '(1.2,2.1)(1.2,2.1)'
   elif ((abs(eta1)> 1.2 and abs(eta1)<=2.1 and abs(eta2)<=0.9 ) or (abs(eta2)> 1.2 and abs(eta2)<=2.1 and abs(eta1)<=0.9 ) ):
      range = '(1.2,2.1)(0.0,0.9)'
   elif ((abs(eta1)> 2.1 and abs(eta1)<= 2.4 and abs(eta2)<=0.9 ) or (abs(eta2)> 2.1 and abs(eta2)<= 2.4 and abs(eta1)<=0.9 ) ):
      range = '(2.1,2.4)(0.0,0.9)'
   elif ((abs(eta1)> 2.1 and abs(eta1)<= 2.4 and abs(eta2)> 1.2 and abs(eta2)<=2.1 ) or ( abs(eta2)> 2.1 and abs(eta2)<= 2.4 and  abs(eta1)> 1.2 and abs(eta1)<=2.1 )):
      range = '(2.1,2.4)(1.2,2.1)'
   elif ((abs(eta1)> 2.1 and abs(eta1)<= 2.4 and abs(eta2)> 0.9 and abs(eta2)<=1.2 ) or ( abs(eta2)> 2.1 and  abs(eta2)<= 2.4 and abs(eta1)> 0.9 and abs(eta1)<=1.2 ) ):
      range = '(2.1,2.4)(0.9,1.2)'
   elif ((abs(eta1)> 2.1 and  abs(eta1)<= 2.4 and abs(eta2)> 2.1 and  abs(eta2)<= 2.4 ) ):
      range = '(2.1,2.4)(2.1,2.4)' 
   else:
      print 'ERROR: value not in range'

   return range

def get_etaFiner_key(eta):
## N.B. obsolete, but kept
   
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
      range = '140_300'
   else:
      print 'ERROR: value not in range'

   return range

class EleIDISO_SFReader:
   
  def __init__(self):
     """Embedding Ele ID-ISO SF."""
     f = open(configuration.dataDirectory+'scalefactors_ele_GsfIdMedium_2012rereco.txt', 'r')
     if f:
        self._file = f 
     else :
        print 'ERROR: Input file for muon SF not existing!'

  def value(self,pt,eta,mode):

       self._file.seek(0,0) 
       for line in self._file:
           vals = line.split() # find a new way for splitting           
           # === DEBUG ===
           #print line
           #print 'pt/eta', pt , eta
           #print 'abs(eta)', abs(eta)
           
           if( pt>= float(vals[0]) and pt<float(vals[1]) and abs(eta)>= float(vals[2]) and abs(eta)<float(vals[3])):
              if mode == '0'  :
                 return float(vals[4])                
              elif mode == '+1'  :
                 return float(vals[5])
              elif mode == '-1'  :   
                 return float(vals[6])
              else:  
                 print 'ERROR: wrong \'mode\' specified: try \'0\',\'+1\' or \'-1\''
                 return 0
       if (pt<=500):       
          print 'WARNING: Any electron sf range matching the specified eta/pt'
       return 1.


class EleTriggerHighPtLeg_SFReader:
   
  def __init__(self):
     """Embedding Electron Trigger High leg SF."""
     f = open(configuration.dataDirectory+'scalefactors_ele_IdMediumTrigger17Leg_2012rereco.txt', 'r')
     if f:
        self._file = f  
     else :
        print 'ERROR: Input file for muon SF not existing!'

  def value(self,pt,eta,mode):
        self._file.seek(0,0) 
        for line in self._file:
           vals = line.split() # find a new way for splitting
        
           if( pt>= float(vals[0]) and pt<float(vals[1]) and abs(eta)>= float(vals[2]) and abs(eta)< float(vals[3])):
              if mode == '0'  :
                 return float(vals[4])
              elif mode == '+1'  :
                 return float(vals[5])
              elif mode == '-1'  :   
                 return float(vals[6])
              else:  
                 print 'ERROR: wrong \'mode\' specified: try \'0\',\'+1\' or \'-1\''
                 return 0
        if (pt<=500):   
           print 'WARNING: Any electron sf range matching the specified eta/pt '
        return 1.


class EleTriggerLowPtLeg_SFReader:
   
  def __init__(self):
     """Embedding Electron Trigger Low leg SF."""
     f = open(configuration.dataDirectory+'scalefactors_ele_IdMediumTrigger8Leg_2012rereco.txt', 'r')
     if f:
        self._file = f  
     else :
        print 'ERROR: Input file for muon SF not existing!'

  def value(self,pt,eta,mode):
        self._file.seek(0,0) 
        for line in self._file:
           vals = line.split() # find a new way for splitting
           if( pt>= float(vals[0]) and pt<float(vals[1]) and abs(eta)>= float(vals[2]) and abs(eta)< float(vals[3])):
              if mode == '0'  :
                 return float(vals[4])
              elif mode == '+1'  :
                 return float(vals[5])
              elif mode == '-1'  :   
                 return float(vals[6])
              else:  
                 print 'ERROR: wrong \'mode\' specified: try \'0\',\'+1\' or \'-1\''
                 return 0
        if (pt<=200):   
           print 'WARNING: Any electron sf range matching the specified eta/pt'
        return 1.
       
         
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

#===  Muon ID SF
#===  (https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonReferenceEffs#22Jan2013_ReReco_of_2012_data_re)

class MuonIDSFReader:
   """A binned map in eta (for the moment) for muon SF.
      Values can be extracted are (value,error). """

   def __init__(self):
     """Construct a MuonIDSFReader using pikle files."""
     f = open(configuration.dataDirectory+'MuonEfficiencies_Run2012ReReco_53X.pkl', 'r')
     if f :
        self._map = pickle.load(f)
        self._eta_range = ''
        self._pt_range = ''
     else :
        print 'ERROR: Input file for muon SF not existing!'

   def value(self,pt,eta,mode):

     """Return the SF or the uncertainty for a given pt and eta."""

     self._eta_range= get_eta_key(eta)
     self._pt_range= get_pt_key(pt)

     if mode == '0'  :
        return self._map['Tight'][self._eta_range][self._pt_range]['data/mc']['efficiency_ratio']
     elif mode == '+1'  :
        return self._map['Tight'][self._eta_range][self._pt_range]['data/mc']['err_hi'] 
     elif mode == '-1' :
        return self._map['Tight'][self._eta_range][self._pt_range]['data/mc']['err_low']
     else:  
        print 'ERROR: wrong \'mode\' specified: try \'0\',\'+1\' or \'-1\''
        return 0

#===  Muon ISO SF
#===  (https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonReferenceEffs#22Jan2013_ReReco_of_2012_data_re)

class MuonISOSFReader:
   """A binned map in eta (for the moment) for muon SF.
      Values can be extracted are (value,error). """

   def __init__(self):
     """Construct a MuonISOSFReader using pikle files."""
     f = open(configuration.dataDirectory+'MuonEfficiencies_ISO_Run_2012ReReco_53X.pkl', 'r')
     if f :
        self._map = pickle.load(f)
        self._eta_range = ''
        self._pt_range = ''
     else :
        print 'ERROR: Input file for muon SF not existing!'

   def value(self,pt,eta,mode):

     """Return the SF or the uncertainty for a given pt and eta."""

     self._eta_range= get_eta_key(eta)
     self._pt_range= get_pt_key(pt)

     if mode == '0'  :
        return self._map['combRelIsoPF04dBeta<02_Tight'][self._eta_range][self._pt_range]['data/mc']['efficiency_ratio']
     elif mode == '+1'  :
        return self._map['combRelIsoPF04dBeta<02_Tight'][self._eta_range][self._pt_range]['data/mc']['err_hi'] 
     elif mode == '-1' :
        return self._map['combRelIsoPF04dBeta<02_Tight'][self._eta_range][self._pt_range]['data/mc']['err_low']
     else:  
        print 'ERROR: wrong \'mode\' specified: try \'0\',\'+1\' or \'-1\''
        return 0    
        

#=== Muon Trigger efficiencies 
#=== 2012ABC for Mu17Mu8 OR Mu17TkMu8
        
class MuonTriggerEffReader_Mu17Mu8_OR_Mu17TkMu8:
   """A binned map in eta of both muons for HLT 2012 trigger efficiencies.
      Values can be extracted are (value,error). """

   def __init__(self):
     """Construct a MuonTriggerEffReader using pikle files."""
     f = open(configuration.dataDirectory+'MuHLTEfficiencies_Run_2012ABCD_53X_DR03-2.pkl', 'r')
     if f :
        self._map = pickle.load(f)
        self._eta_range = ''
     else :
        print 'ERROR: Input file for Trigger efficiencies not existing!'

   def value(self,eta1,eta2,mode):

     """Return the eff or the uncertainty for a given pt and eta."""
     
     #self._eta_range= "("+get_eta_trigger_key(eta1)+")("+get_eta_trigger_key(eta2)+")"
     self._eta_range= get_eta_trigger_key(eta1,eta2)  ## new one

     if mode == '0'  :
        return self._map['Mu17Mu8_OR_Mu17TkMu8']['Tight']['(eta,eta)']['(20<mu1<Infty,20<mu2<Infty)'][self._eta_range]['data']['efficiency']
     elif mode == '+1'  :
        return self._map['Mu17Mu8_OR_Mu17TkMu8']['Tight']['(eta,eta)']['(20<mu1<Infty,20<mu2<Infty)'][self._eta_range]['data']['syst_uncrt'] ## add in quadrature the stats uncertainties (TBD)
     elif mode == '-1' : 
        return self._map['Mu17Mu8_OR_Mu17TkMu8']['Tight']['(eta,eta)']['(20<mu1<Infty,20<mu2<Infty)'][self._eta_range]['data']['syst_uncrt'] ## add in quadrature the stats uncertainties (TBD)
     else:  
        print 'ERROR: wrong \'mode\' specified: try \'0\',\'+1\' or \'-1\''
        return 0

#=== 2012ABC for Mu17 SingleLeg

class MuonTriggerEffReader_Mu17Leg:
   """A binned map in eta of both muons for HLT 2012 trigger efficiencies.
      Values can be extracted are (value,error). """

   def __init__(self):
     """Construct a MuonTriggerEffReader using pikle files."""
     f = open(configuration.dataDirectory+'HLT_DoubleMu_Efficiencies_Run_2012ABCD_53X_SingleLegs.pkl', 'r')
     if f :
        self._map = pickle.load(f)
        self._eta_range = ''
     else :
        print 'ERROR: Input file for Trigger efficiencies not existing!'

   def value(self,eta1,eta2,mode):

     """Return the eff or the uncertainty for a given pt and eta."""
     
     #self._eta_range= "("+get_eta_trigger_key(eta1)+")("+get_eta_trigger_key(eta2)+")"
     self._eta_range= get_eta_trigger_key(eta1,eta2)  ## new one

     if mode == '0'  :
        return self._map['Mu17Mu8_Mu17Leg']['Tight']['eta']['20<mu2<Infty'][self._eta_range]['data']['efficiency']
     elif mode == '+1'  :
        return self._map['Mu17Mu8_Mu17Leg']['Tight']['eta']['20<mu2<Infty'][self._eta_range]['data']['stat_uncrt'] ## add in quadrature the stats uncertainties (TBD)
     elif mode == '-1' : 
        return self._map['Mu17Mu8_Mu17Leg']['Tight']['eta']['20<mu2<Infty'][self._eta_range]['data']['stat_uncrt'] ## add in quadrature the stats uncertainties (TBD)
     else:  
        print 'ERROR: wrong \'mode\' specified: try \'0\',\'+1\' or \'-1\''
        return 0

#=== 2012ABC for Mu8 SingleLeg

class MuonTriggerEffReader_Mu8Leg:
   """A binned map in eta of both muons for HLT 2012 trigger efficiencies.
      Values can be extracted are (value,error). """

   def __init__(self):
     """Construct a MuonTriggerEffReader using pikle files."""
     f = open(configuration.dataDirectory+'HLT_DoubleMu_Efficiencies_Run_2012ABCD_53X_SingleLegs.pkl', 'r')
     if f :
        self._map = pickle.load(f)
        self._eta_range = ''
     else :
        print 'ERROR: Input file for Trigger efficiencies not existing!'

   def value(self,eta1,eta2,mode):

     """Return the eff or the uncertainty for a given pt and eta."""
     
     #self._eta_range= "("+get_eta_trigger_key(eta1)+")("+get_eta_trigger_key(eta2)+")"
     self._eta_range= get_eta_trigger_key(eta1,eta2)  ## new one

     if mode == '0'  :
        return self._map['Mu17Mu8_Mu8Leg']['Tight']['eta']['20<mu2<Infty'][self._eta_range]['data']['efficiency']
     elif mode == '+1'  :
        return self._map['Mu17Mu8_Mu8Leg']['Tight']['eta']['20<mu2<Infty'][self._eta_range]['data']['stat_uncrt'] ## add in quadrature the stats uncertainties (TBD)
     elif mode == '-1' : 
        return self._map['Mu17Mu8_Mu8Leg']['Tight']['eta']['20<mu2<Infty'][self._eta_range]['data']['stat_uncrt'] ## add in quadrature the stats uncertainties (TBD)

     else:  
        print 'ERROR: wrong \'mode\' specified: try \'0\',\'+1\' or \'-1\''
        return 0


class LeptonsReWeighting:
   """A class to reweight MC to fix lepton efficiency."""

   def __init__(self):

     # ===== initializing the weights

     self._muIDWeight  = MuonIDSFReader()
     self._muISOWeight  = MuonISOSFReader()
     self._muTRIGGERWeight  = MuonTriggerEffReader_Mu17Mu8_OR_Mu17TkMu8()
     self._mu17TrgWeight  = MuonTriggerEffReader_Mu17Leg()
     self._mu8TrgWeight  = MuonTriggerEffReader_Mu8Leg() 

     self._eleIDISOWeight = EleIDISO_SFReader()
     self._ele17TrgWeight = EleTriggerHighPtLeg_SFReader()
     self._ele8TrgWeight = EleTriggerLowPtLeg_SFReader()


   def weight_mm(self,m1,m2):
     """Event weight for di-muons."""
     lw = 1.
     # The final per-event weight (convolving ID, ISO and Trigger)
     lw *= self._muIDWeight.value(m1.pt(),m1.eta(),'0')
     lw *= self._muIDWeight.value(m2.pt(),m2.eta(),'0')
     lw *= self._muISOWeight.value(m1.pt(),m1.eta(),'0')
     lw *= self._muISOWeight.value(m2.pt(),m2.eta(),'0')
     lw *= self._muTRIGGERWeight.value(m1.eta(),m2.eta(),'0')

     if abs(configuration.LeptonTnPfactor)<0.01 :
       return lw
     else:
       return lw + configuration.LeptonTnPfactor*self.uncertainty_mm(m1,m2)
         


   def uncertainty_mm(self,m1,m2):
     """Relative uncertainty on the total weight.
        We assume the different contributions to be uncorrelated and sum the relative uncertainties in quadrature."""
     
     unc =  (self._muIDWeight.value(m1.pt(),m1.eta(),'+1')/self._muIDWeight.value(m1.pt(),m1.eta(),'0') +   \
            self._muIDWeight.value(m2.pt(),m2.eta(),'+1')/self._muIDWeight.value(m2.pt(),m2.eta(),'0'))**2 +   \
            (self._muISOWeight.value(m1.pt(),m1.eta(),'+1')/self._muISOWeight.value(m1.pt(),m1.eta(),'0') + \
            self._muISOWeight.value(m2.pt(),m2.eta(),'+1')/self._muISOWeight.value(m2.pt(),m2.eta(),'0'))**2 + \
            (self._muTRIGGERWeight.value(m1.eta(),m2.eta(),'+1')/self._muTRIGGERWeight.value(m1.eta(),m2.eta(),'0'))**2
         
     return sqrt(unc)


   def weight_ee(self,e1,e2):
     """Event weight for di-electrons."""

     lw = 1.
     lw *= self._eleIDISOWeight.value(e1.pt(),e1.eta(),'0')
     lw *= self._eleIDISOWeight.value(e2.pt(),e2.eta(),'0')
     lw *= self._ele17TrgWeight.value(e1.pt(),e1.eta(),'0')* self._ele8TrgWeight.value(e2.pt(),e2.eta(),'0') + self._ele8TrgWeight.value(e1.pt(),e1.eta(),'0')* self._ele17TrgWeight.value(e2.pt(),e2.eta(),'0') - self._ele17TrgWeight.value(e1.pt(),e1.eta(),'0')* self._ele17TrgWeight.value(e2.pt(),e2.eta(),'0')  ## formula for the asymmetric trigger
          
     if abs(configuration.LeptonTnPfactor)<0.01 :
       return lw
     else:
       return lw + configuration.LeptonTnPfactor*self.uncertainty_ee(e1,e2)


   def uncertainty_ee(self,e1,e2):
     ## TBD (rc feb.2014) 
     """Relative uncertainty on the total weight.
        We assume the different contributions to be uncorrelated and sum the relative uncertainties in quadrature."""
     # reco
     unc =  (self._eleIDISOWeight.value(e1.pt(),e1.eta(),'1')/self._eleIDISOWeight.value(e1.pt(),e1.eta(),'0')+ \
             self._eleIDISOWeight.value(e2.pt(),e2.eta(),'1')/self._eleIDISOWeight.value(e2.pt(),e2.eta(),'0'))**2
     # trigger (approximate) TO BE IMPLEMENTED! FIXME
     # unc += (abs(self._ele8TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][1]+  \
     #           self._ele17TrgWeight[(e1.pt(),e1.eta())][1]*self._ele8TrgWeight[(e2.pt(),e2.eta())][0]-   \
     #           self._ele17TrgWeight[(e1.pt(),e1.eta())][1]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]-  \
     #           self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][1])/ \
     #        (self._ele8TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]+     \
     #         self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele8TrgWeight[(e2.pt(),e2.eta())][0]-     \
     #         self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]))**2
     # unc += ((self._ele8TrgWeight[(e1.pt(),e1.eta())][1]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]+     \
     #        self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele8TrgWeight[(e2.pt(),e2.eta())][1])/     \
     #       (self._ele8TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]+      \
     #        self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele8TrgWeight[(e2.pt(),e2.eta())][0]-      \
     #        self._ele17TrgWeight[(e1.pt(),e1.eta())][0]*self._ele17TrgWeight[(e2.pt(),e2.eta())][0]))**2
     #outcome
     return sqrt(unc)

   
   def weight_em(self,e1,m1):
     """Event weight for e-mu events."""
     lw = 1.
     # The final per-event weight (convolving ID, ISO and Trigger)
     lw *= self._muIDWeight.value(m1.pt(),m1.eta(),'0')
     lw *= self._muISOWeight.value(m1.pt(),m1.eta(),'0')     
     lw *= self._eleIDISOWeight.value(e1.pt(),e1.eta(),'0')
     lw *= self._ele17TrgWeight.value(e1.pt(),e1.eta(),'0')* self._mu8TrgWeight.value(m1.pt(),m1.eta(),'0') + self._ele8TrgWeight.value(e1.pt(),e1.eta(),'0')* self._mu17TrgWeight.value(m1.pt(),m1.eta(),'0') - self._ele17TrgWeight.value(e1.pt(),e1.eta(),'0')* self._mu17TrgWeight.value(m1.pt(),m1.eta(),'0')  ## formula for the OR of the unprescaled  e-mu triggers

     if abs(configuration.LeptonTnPfactor)<0.01 :
       return lw
     else:
       return lw + configuration.LeptonTnPfactor*self.uncertainty_em(e1,m1)
         
   def uncertainty_em(self,e1,m1):
     ## TBD (rc may.2014) 
     """Relative uncertainty on the total weight.
        We assume the different contributions to be uncorrelated and sum the relative uncertainties in quadrature."""
     # reco
     unc =  1.0 # --> TO BE IMPLEMENTED! FIXME
     return sqrt(unc)

  
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
           muons = fwevent.muonsPair
           if muons is None : return 1.
           return self.weight_mm(muons[0],muons[1])
         elif forceMode == "Electron":
           electrons = fwevent.electronsPair
           if electrons is None : return 1.
           return self.weight_ee(electrons[0],electrons[1])
         elif forceMode == "MuEl":
           muel = fwevent.muelPair
           if muel is None : return 1.
           if muel[0].isElectron() : return self.weight_em(muel[0],muel[1])
           else : return self.weight_em(muel[1],muel[0])
         else :
           leptons = fwevent.leptonsPair
           if leptons is None : return 1
           if leptons[0].isMuon() and leptons[0].isMuon() : return self.weight_mm(leptons[0],leptons[1])
           elif leptons[0].isElectron() and leptons[0].isElectron() : return self.weight_ee(leptons[0],leptons[1])
           elif leptons[0].isElectron() and leptons[0].isMuon() : return self.weight_em(leptons[0],leptons[1])
           elif leptons[0].isMuon() and leptons[0].isElectron() : return self.weight_em(leptons[1],leptons[0])
           else : print "None of the case was found: MuMu, ElEl, MuEl, ElMu..."
       return 1.

