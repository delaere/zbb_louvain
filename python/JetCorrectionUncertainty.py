import os
import ROOT
import PatAnalysis.CMSSW
from math import sqrt
from random import gauss
confCfg = os.environ["PatAnalysisCfg"]
if confCfg : from UserCode.zbb_louvain.PatAnalysis.CPconfig import configuration
else : from zbbConfig import configuration

class JetCorrectionUncertaintyProxy:
  """A class to access JEC uncertainties"""

  def __init__(self,fileAK5=configuration.jecUncertaintyAK5, fileAK7=configuration.jecUncertaintyAK7):
    self._engine = {}
    if not os.path.isfile(fileAK5):
      print "Error: ",fileAK5, ": No such file."
      self._engine["AK5"] = None
    else:
      self._engine["AK5"] = ROOT.JetCorrectionUncertainty(ROOT.JetCorrectorParameters(fileAK5, "Total"))
    if not os.path.isfile(fileAK7):
      print "Warning: ",fileAK7, ": No such file."
      self._engine["AK7"] = None
    else:
      self._engine["AK7"] = ROOT.JetCorrectionUncertainty(ROOT.JetCorrectorParameters(fileAK7, "Total"))

  def unc_tot_jet(self,jet,cone="AK5"):
    """Total (relative) JES uncertainty"""
    if self._engine[cone] is None: return 0
    self._engine[cone].setJetEta(jet.eta())# Give rapidity of jet you want uncertainty on
    self._engine[cone].setJetPt(jet.pt()) #Also give the corrected pt of the jet you want the uncertainty on
    unc = self._engine[cone].getUncertainty(1)
    return unc

  def jetPt(self,jet,cone="AK5"):
    """Jet Pt, optionally varied for JES and JER"""
    jetpt = jet.pt()
    # smear to reproduce resolution measured in data
    # apply JetMet recommendation:  pT->max[0.,pTgen+c*(pT-pTgen)] 
    if abs(configuration.JERfactor)>0.01: # non-zero
      try:
        ptgen = jet.genJet().pt()
      except:
        ptgen = gauss(jetpt,self.jetEnergyResolution(jet))
      jersf = (self.jerCorrectionFactor(jet)-1.) * configuration.JERfactor
      jetpt = max(0., ptgen + (1.+jersf)*(jetpt-ptgen))
    # take into account JEC uncertainty
    if abs(configuration.JESfactor)>0.01: # non-zero
      jesunc = self.unc_tot_jet(jet,cone) * configuration.JESfactor * jetpt
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

  def Scale(self,jet,cone="AK5"):
    """Jet Pt, optionally varied for JES and JER"""
    jetpt = jet.pt()
    # smear to reproduce resolution measured in data
    # apply JetMet recommendation:  pT->max[0.,pTgen+c*(pT-pTgen)] 
    if abs(configuration.JERfactor)>0.01: # non-zero
      #print "JER"
      try:
        ptgen = jet.genJet().pt()
      except:
        ptgen = gauss(jetpt,self.jetEnergyResolution(jet))
      jersf = (self.jerCorrectionFactor(jet)-1.) * configuration.JERfactor
      jetpt = max(0., ptgen + (1.+jersf)*(jetpt-ptgen))
    # take into account JEC uncertainty
    if abs(configuration.JESfactor)>0.01: # non-zero
      #print "JEC"
      jesunc = self.unc_tot_jet(jet, cone) * configuration.JESfactor * jetpt
      jetpt = max(0., jetpt + jesunc)
    # return the jet pt, including all of the above
    if abs(configuration.JERfactor)>0.01 or abs(configuration.JESfactor)>0.01 : jet.scaleEnergy(jetpt/jet.pt())
    return 
