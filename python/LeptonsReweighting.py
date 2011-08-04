from DataFormats.FWLite import Events, Handle
from eventSelection import *
#from myFuncTimer import print_timing

class LeptonsReWeighting:
   """A class to reweight MC to fix lepton efficiency."""

   def __init__(self):
     #make 4 (pT,eta) bins for electrons
     self.mEleTPID_     = [ 0.989 ,0.993601 ,0.974384 ,1.00543 ,0.9351 ,1.00616 ,0.93766 ,1.01478 ]
     self.mEleTPIDerr_  = [ 0.005 ,0.005 ,0.005 ,0.005 ,0.005 ,0.007 ,0.006 ,0.009 ]
     self.mEleTPISO_    = [ 1.00509 ,0.993324 ,1.04163 ,1.0320 ]
     self.mEleTPISOerr_ = [ 0.005 ,0.005 ,0.005 ,0.006 ]
     self.mEleTPTRG_    = [ 1.00789, 1.00789, 1.00897, 1.00897 ]
     self.mEleTPTRGerr_ = [ 0.005 ,0.005 ,0.005 ,0.005 ]
     #make 4 (pT,eta) bins for muons
     self.mMuTPID_      = [ 0.992, 0.995, 0.990, 0.998 ]
     self.mMuTPIDerr_   = [ 0.004, 0.004, 0.004, 0.005 ]
     self.mMuTPISO_     = [ 1.006, 1.003, 0.999, 1.000 ]
     self.mMuTPISOerr_  = [ 0.004, 0.004, 0.004, 0.005 ]
     self.mMuTPTRG_     = [ 0.976, 0.976, 0.965, 0.965, 0.901, 0.901 ]
     self.mMuTPTRGerr_  = [ 0.0007, 0.0007, 0.001, 0.001, 0.004, 0.004 ]
     # handle to event objects
     self.zmuHandle_  = Handle ("vector<reco::CompositeCandidate>")
     self.zeleHandle_ = Handle ("vector<reco::CompositeCandidate>")

   def eleWeight( self, pt, eta):
     # binning
     ptbins   = [ 50 ]
     etabins1 = [ 0.8, 1.44, 2.0 ]
     etabins2 = [ 1.6 ]
     # compute the bin
     lBinpT   = reduce(lambda x,y:x+y,map(lambda x:pt>x,ptbins))
     lBinEta1 = reduce(lambda x,y:x+y,map(lambda x:eta>x,etabins1))
     lBinEta2 = reduce(lambda x,y:x+y,map(lambda x:eta>x,etabins2))
     lBin1 = 2*lBinEta1+lBinpT;
     lBin2 = 2*lBinEta2+lBinpT;
     # return the proper weight
     return self.mEleTPID_[lBin1]*self.mEleTPISO_[lBin2]*self.mEleTPTRG_[lBin2]

   def muWeight( self, pt, eta):
     # binning
     ptbins   = [ 50 ]
     etabins1 = [ 1.2 ]
     etabins2 = [ 0.9, 1.5 ]
     # compute the bin
     lBinpT   = reduce(lambda x,y:x+y,map(lambda x:pt>x,ptbins))
     lBinEta1 = reduce(lambda x,y:x+y,map(lambda x:eta>x,etabins1))
     lBinEta2 = reduce(lambda x,y:x+y,map(lambda x:eta>x,etabins2))
     lBin1 = 2*lBinEta1+lBinpT;
     lBin2 = 2*lBinEta2+lBinpT;
     # return the proper weight
     return self.mMuTPID_[lBin1]*self.mMuTPISO_[lBin1]*self.mMuTPTRG_[lBin2]

   #@print_timing
   def weight( self, fwevent=None, electrons=None, muons=None, muChannel=True):
     """Lepton eff weight"""
     lw = 1
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
       for electron in electrons:
         lw *= self.eleWeight(electron.pt(), electron.eta())
     if not(muons is None):
       for muon in muons:
         lw *= self.muWeight(muon.pt(), muon.eta())
     return lw

