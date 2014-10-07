import math
from copy import deepcopy
import MonteCarloSelection
import os
confCfg = os.environ["PatAnalysisCfg"]
if confCfg : from UserCode.zbb_louvain.PatAnalysis.CPconfig import configuration
else : from zbbConfig import configuration

class MonteCarloReWeighting:
   """A class to reweight MC according to kinematic uncertainties."""

   def __init__(self, shift=0, MCmode="none"):
     # do we reweight or not, by how much ?
     self._shift = shift 
     self._modes = [ "sign", "mc", "bpt", "zpt", "sfs_tt", "sfs_dy", "Merging", "all", "none" ]
     if not [m for m in self._modes if m in MCmode]:
       print "ERROR: ", MCmode, " is not a recognized mode for MonteCarloReWeighting."
       self._MCmode="none"
     else:
       self._MCmode=MCmode
     f = open(configuration.DYmerging,'r')
     if f :
        self._file = f
        self.bins = self._file.readlines()
     else : self._file = None
     
   def _eventWeight( self, fwevent=None, mode="none"):
     """(Internal) actual function to compute the event weight"""
     theZpt = 0.
     for particle in fwevent.genParticles:
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
       bjetptweight = math.exp(-1*0.015*25)*math.exp(0.015*maxbjetPt) #that's a 25% variation of the nominal slope: 0.059
     else:
       bjetptweight = 1
     # B) Z Pt reweighting: that one is tabulated from the data/mc comparison
     weightArgument = min(theZpt,175.)
     zptweight = -1.84241e-12 * weightArgument**6 + 1.41919e-09 * weightArgument**5 - \
                 3.89175e-07  * weightArgument**4 + 4.77903e-05 * weightArgument**3 - \
                 0.00266683   * weightArgument**2 + 0.0646297   * weightArgument + 0.320127
     #bkg sfs
     if "Merging" in mode:
        sfs_tt = 1.05
        njets = len([x for x in fwevent.goodJets_all if x])
        sfs_Zbb = 1.15*(njets==2)+1.30*(njets>2)
        sfs_Zbx = 1.30
        sfs_Zxx = 1.28
     else:
        #in case ontly the inclusive sample is used
        sfs_tt = 1.09
        njets = len([x for x in fwevent.goodJets_all if x])
        sfs_Zbb = 1.08*(njets==2)+1.14*(njets>2)
        sfs_Zbx = 1.14
        sfs_Zxx = 1.24
     sfs_dy = sfs_Zbb*MonteCarloSelection.isRecoZbbEvent(fwevent.dijet_all) + sfs_Zbx*MonteCarloSelection.isRecoZbEvent(fwevent.dijet_all) + sfs_Zxx*(not MonteCarloSelection.isRecoZbbEvent(fwevent.dijet_all) and not MonteCarloSelection.isRecoZbEvent(fwevent.dijet_all))
     sfs = sfs_tt*("sfs_tt" in mode) + sfs_dy*("sfs_dy" in mode)

     #dy merging reweighting
     info = MonteCarloSelection.LHEinfo(fwevent)
     w_dy = 0.
     for ptbin in [50, 70, 100, 180, float("inf")]:
        if info["llpt"]>=ptbin : continue
        for htbin in [200,400,float("inf")]:
           if info["HT"]>=htbin : continue
           for B in self.bins:
              if (("ll_pt<"+str(ptbin) in B and "HT<"+str(htbin) in B)
                  or ( ("ll_pt<"+str(ptbin) in B and htbin==float("inf") and not "HT<" in B) or (ptbin==float("inf") and "HT<"+str(htbin) in B and not "ll_pt<" in B) )
                  or (ptbin==float("inf") and htbin==float("inf") and not "HT<" in B and not "ll_pt<" in B and ">=" in B)):
                 w_dy = float(B.replace("\n","").split()[1])
                 break
           break
        break

     # Finalresult
     w_MC = {
        "sign" : (fwevent.genInfo.weight())/(abs(fwevent.genInfo.weight())),
        "mc" : fwevent.genInfo.weight(),
        "zpt" : 1+self._shift*(zptweight-1),
        "bpt" : 1+self._shift*(bjetptweight-1),
        "all" : 1+self._shift*(bjetptweight*zptweight-1),
        "sfs" : sfs,
        "Merging" : w_dy
        }

     w_tot = 1.
     for key in w_MC:
        if key in mode : w_tot *= w_MC[key]
     return w_tot

   def weight( self, fwevent=None ):
     """MC shape reweighting, computed from the MC truth"""
     # returns the weight computed from the MC truth only if needed. 
     if self._shift==0 and self._MCmode in ["bpt", "zpt", "all"]:
       return 1.
     # apply systematic shift ?
     if not fwevent is None:
       # for data, immediately return 1.
       if fwevent.object().event().eventAuxiliary().isRealData(): 
         return 1.
       else: 
         # check that fwevent and npu were not specified at the same time.
         return self._eventWeight(fwevent, self._MCmode)
     else: 
       return 1.

   def _match_obo(self, rec, gen, dr):
     """(Internal) matching for bjets"""
     gen2 = deepcopy(gen)
     matching = []
     for vec in rec:
        in_cone = []
        for part in gen2:
            deltar = math.hypot((vec.eta() - part.eta()), MonteCarloSelection.delta_phi(vec.phi(), part.phi()))
            if deltar < dr: in_cone.append([deltar, part])
        if in_cone:
            bestmatch = min(in_cone)[1]
            matching.append(vec)
            gen2.remove(bestmatch)
     return matching

   def _is_final_bhad(self, genpart):
     """(Internal) check if the bhadron is the final one"""
     if not MonteCarloSelection.is_Bhad(genpart): return False
     if len([genpart.daughter(i) for i in range(genpart.numberOfDaughters()) if MonteCarloSelection.is_Bhad(genpart.daughter(i))]): return False
     return True

