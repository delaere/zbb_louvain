import os
import ROOT
from math import sqrt
from random import gauss
from zbbCommons import zbbfile,zbbsystematics
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
ROOT.gSystem.Load("libCondFormatsJetMETObjects.so")

class JetCorrectionUncertaintyProxy:
  """A class to access JEC uncertainties"""

  def __init__(self,file=zbbfile.jecUncertainty):
    if not os.path.isfile(file):
      print "Error: ",file, ": No such file."
      self._engine = None
    else:
      self._engine = ROOT.JetCorrectionUncertainty(ROOT.JetCorrectorParameters(file, "Total"))

  def unc_tot_jet(self,jet):
    """Total (relative) JES uncertainty"""
    if self._engine is None: return 0
    self._engine.setJetEta(jet.eta())# Give rapidity of jet you want uncertainty on
    self._engine.setJetPt(jet.pt()) #Also give the corrected pt of the jet you want the uncertainty on
    unc = self._engine.getUncertainty(1)
    return unc

  def jetPt(self,jet):
    """Jet Pt, optionally varied for JES and JER"""
    jetpt = jet.pt()
    # smear to reproduce resolution measured in data
    # apply JetMet recommendation:  pT->max[0.,pTgen+c*(pT-pTgen)] 
    if abs(zbbsystematics.JERfactor)>0.01: # non-zero
      try:
        ptgen = jet.genJet().pt()
      except:
        ptgen = gauss(jetpt,self.jetEnergyResolution(jet))
      jersf = (self.jerCorrectionFactor(jet)-1.) * zbbsystematics.JERfactor
      jetpt = max(0., ptgen + (1.+jersf)*(jetpt-ptgen))
    # take into account JEC uncertainty
    if abs(zbbsystematics.JESfactor)>0.01: # non-zero
      jesunc = self.unc_tot_jet(jet) * zbbsystematics.JESfactor * jetpt
      jetpt = max(0., jetpt + jesunc)
    # return the jet pt, including all of the above
    return jetpt

  def jet(self,jet):
    """4-momentum of the jet, after variation of JES and JER.
       Pt is rescaled, while eta, phi and mass are fixed."""
    jetmomentum = ROOT.TLorentzVector()
    jetmomentum.SetPtEtaPhiM(self.jetPt(jet),jet.eta(),jet.phi(),jet.mass())
    return jetmomentum

  def jerCorrectionFactor(self,jet):
    """Scale factor to reproduce in MC the JER measured in data.
       Taken from https://twiki.cern.ch/twiki/bin/view/CMS/JetResolution r29"""
    eta = abs(jet.eta())
    if   eta<0.5: return 1.052
    elif eta<1.1: return 1.057
    elif eta<1.7: return 1.096
    elif eta<2.3: return 1.134
    else :        return 1.288 # valid up to 5.0

  def jetEnergyResolution(self,jet):
    """Simplified version of the CMSSW method. Implements sigma
       as in CondFormats/JetMETObjects/data/Spring10_PtResolution_AK5PF.txt
       (ERA: Spring10  ALG: ak5pfl2l3  TYPE: JetEta) """
    jeteta = abs(jet.eta())
    jetpt = jet.pt()
    if jeteta<0.5 :
      a = -0.349206
      b = 0.297831
      d = 0.471121
    elif jeteta<1.0:
      a = -0.499735
      b = 0.336391
      d = 0.430689
    elif jeteta<1.5:
      a = -0.561649
      b = 0.420293
      d = 0.392398
    elif jeteta<2.0:
      a = -1.12329
      b = 0.657891
      d = 0.139595
    else:
      a = 1.04792
      b = 0.466763
      d = 0.193137
    return sqrt(((cmp(a,0)*(a/jetpt)**2)+(b**2*(pow(jetpt,(d-1))))))
