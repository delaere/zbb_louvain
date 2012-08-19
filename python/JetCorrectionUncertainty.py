import os
import ROOT
from math import sqrt
from zbbCommons import zbbfile, zbblabel
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
      self._engine = ROOT.JetCorrectionUncertainty(file)

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
    ptgen = jet.genJet().pt()
    jersf = (jerCorrectionFactor(jet)-1.) * zbblabel.JERfactor
    jetpt = max(0., ptgen + (1.+jersf)*(jetpt-ptgen))
    # take into account JEC uncertainty
    jesunc = unc_tot_jet(jet) * zbblabel.JESfactor
    jetpt = jetpt + jesunc
    # return the jet pt, including all of the above
    return jetpt

  def jerCorrectionFactor(self,jet)
    eta = abs(jet.eta())
    if eta<0.5: return 1.052
    elif eta<1.1: return 1.057
    elif eta<1.7: return 1.096
    elif eta<2.3: return 1.134
    else return 1.288 # valid up to 5.0
