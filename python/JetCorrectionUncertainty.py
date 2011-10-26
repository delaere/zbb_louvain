import os
import ROOT
from math import sqrt
from zbbCommons import zbbfile
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

    if 0 <abs(jet.eta())< 1.5 : unc_dep_eta=0.02
    if 1.5 <=abs(jet.eta())< 3.0  : unc_dep_eta=0.06
    if 3.0 <=abs(jet.eta()) : unc_dep_eta=0.20

    unc_tot=sqrt(pow(unc,2)+pow(0.015,2)+pow((0.2*0.8*2.2*1/jet.pt()),2)+pow(unc_dep_eta,2))
    return unc_tot

