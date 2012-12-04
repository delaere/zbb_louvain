import ROOT
import math
from copy import deepcopy
from AnalysisEvent import AnalysisEvent
from zbbCommons import zbblabel,zbbfile
#from myFuncTimer import print_timing

class MonteCarloReWeighting:
   """A class to reweight MC according to kinematic uncertainties."""

   def __init__(self, shift=0):
     # do we reweight or not, by how much ?
     self._shift = shift 
     self._modes = [ "sign", "mc", "bpt", "zpt", "all", "none" ]
   #@print_timing
   def weight( self, fwevent=None, MCmode="none"):
     """MC shape reweighting, computed from the MC truth"""
     # returns the weight computed from the MC truth only if needed. 
     if self._shift==0:
       return 1.
     if not MCmode in self._modes:
        print "ERROR: ", MCmode, " is not a recognized mode for MonteCarloReWeighting."
        return 1.
     # apply systematic shift ?
     if not fwevent is None:
       # for data, immediately return 1.
       if fwevent.object().event().eventAuxiliary().isRealData(): 
         return 1.
       else: 
         # check that fwevent and npu were not specified at the same time.
         return _eventWeight(fwevent, MCmode)

   def _eventWeight( self, fwevent=None, mode="none"):
     """(Internal) actual function to compute the event weight"""
     theZpt = 0.
     for part in fwevent.genParticles:
       if particle.pdgId() == 23:
         theZpt = particle.pt()
         break
     bparts = [part for part in fwevent.genParticles if (499 < math.fabs(part.pdgId()) < 600) or (4999 < math.fabs(part.pdgId()) < 6000)]
     bhads = [part for part in bparts if self._is_final_bhad(part)]
     gen_b_jets = self._match_obo(fwevent.genJets, bhads, 0.5)
     maxbjetPt = 0.
     for bjet in gen_b_jets:
       if bjet.pt() > maxbjetPt:
         maxbjetPt = bjet.pt()
     # apply the recipe
     # A) bjet Pt reweighting
     if math.fabs(maxbjetPt-25)<10:
       math.exp(-1*0.015*25)*math.exp(0.015*maxbjetPt) #that's a 25% variation of the nominal slope: 0.059
     else:
       bjetptweight = 1
     # B) Z Pt reweighting: that one is tabulated from the data/mc comparison
     weightArgument = min(theZpt,175.)
     zptweight = -1.84241e-12 * weightArgument**6 + 1.41919e-09 * weightArgument**5 - \
                 3.89175e-07  * weightArgument**4 + 4.77903e-05 * weightArgument**3 - \
                 0.00266683   * weightArgument**2 + 0.0646297   * weightArgument + 0.320127
     # final result
     if mode=="sign":
       return (event.genInfo.weight())/(abs(event.genInfo.weight()))
     if mode=="mc":
       return event.genInfo.weight()
     if mode=="zpt" : 
       return 1+self._shift*(zptweight-1)
     if mode=="bpt" : 
       return 1+self._shift*(bjetptweight-1)
     if mode=="all" :
       return 1+self._shift*(bjetptweight*zptweight-1)
     return 1.

   def _match_obo(self, rec, gen, dr):
     """(Internal) matching for bjets"""
     gen2 = deepcopy(gen)
     matching = []
     for vec in rec:
        in_cone = []
        for part in gen2:
            deltar = math.hypot((vec.eta() - part.eta()), delta_phi(vec.phi(), part.phi()))
            if deltar < dr: in_cone.append([deltar, part])
        if in_cone:
            bestmatch = min(in_cone)[1]
            matching.append(vec)
            gen2.remove(bestmatch)
     return matching

   def _is_final_bhad(genpart):
     """(Internal) check if the bhadron is the final one"""
     if not is_bhad(genpart): return False
     if len([genpart.daughter(i) for i in range(genpart.numberOfDaughters()) if is_bhad(genpart.daughter(i))]): return False
     return True

