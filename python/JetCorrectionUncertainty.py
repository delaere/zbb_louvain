import os
import ROOT
from math import sqrt
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
    if self._engine is None: return 0
    self._engine.setJetEta(jet.eta())# Give rapidity of jet you want uncertainty on
    self._engine.setJetPt(jet.pt()) #Also give the corrected pt of the jet you want the uncertainty on
    unc = self._engine.getUncertainty(1)
    return unc

  def jetPt(self,jet):
    jetpt = jet.pt()
    # smear to reproduce resolution measured in data
    # apply JetMet recommendation:  pT->max[0.,pTgen+c*(pT-pTgen)] 
    try:
      ptgen = jet.genJet().pt()
    except:
      ptgen = jetpt # here, we could do something more clever. The official recipe involves randomly sampling the measured resolution.
    jersf = (self.jerCorrectionFactor(jet)-1.) * zbbsystematics.JERfactor
    jetpt = max(0., ptgen + (1.+jersf)*(jetpt-ptgen))
    # take into account JEC uncertainty
    jesunc = self.unc_tot_jet(jet) * zbbsystematics.JESfactor * jetpt
    jetpt = max(0., jetpt + jesunc)
    # return the jet pt, including all of the above
    return jetpt

  def jerCorrectionFactor(self,jet):
    eta = abs(jet.eta())
    if   eta<0.5: return 1.052
    elif eta<1.1: return 1.057
    elif eta<1.7: return 1.096
    elif eta<2.3: return 1.134
    else :        return 1.288 # valid up to 5.0

