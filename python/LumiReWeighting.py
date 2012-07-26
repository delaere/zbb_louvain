import ROOT
from DataFormats.FWLite import Events, Handle
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
ROOT.gSystem.Load("libPhysicsToolsUtilities.so")
from zbbCommons import zbblabel,zbbfile
#from myFuncTimer import print_timing


class LumiReWeighting:
   """A class to reweight MC according to number of pileup events."""

   def __init__(self, MonteCarloFileName=zbbfile.pileupMC, DataFileName=zbbfile.pileupData, PileupSummaryInfo=zbblabel.pulabel, systematicShift=0):
      # set the names for histograms. In the new scheme, the data file contains three histograms for nominal and +/-1sigma.
      MonteCarloHistName = "pileup"
      DataHistName = { 0 : "pileup", -1 : "pileupDOWN1", 1 : "pileupUP1" }
      # access histograms and initialize the weights
      self.engine = ROOT.edm.LumiReWeighting(MonteCarloFileName,DataFileName,MonteCarloHistName,DataHistName[systematicShift])
      self.PileupSummaryInfo = PileupSummaryInfo
      self.PupInfo = Handle ("std::vector< PileupSummaryInfo >")

   #@print_timing
   def weight( self, npu=None, fwevent=None):
     """Lumi (PU) weight"""
     # returns the weight computed from the true number of interactions. 
     # apply systematic shift ?
     if not fwevent is None:
       # for data, immediately return 1.
       if fwevent.object().event().eventAuxiliary().isRealData(): 
         return 1.
       else: 
         # check that fwevent and npu were not specified at the same time.
         if not npu is None:
           print "warning: Both npu and event are specified. npu will be ignored"
         npu = self.npu(fwevent)
     if not npu is None:
       # return the weight
       return self.engine.weight(npu)
     else:
       print "ERROR:  no in-time beam crossing found! "
       return 0.
 
   def npu( self, fwevent):
     # get pileup summary information
     fwevent.getByLabel(self.PileupSummaryInfo, self.PupInfo)
     pileup = self.PupInfo.product()
     # find the "BX0" and the true number of PU interactions in there
     for pvi in pileup:
       if pvi.getBunchCrossing()==0:
         return pvi.getTrueNumInteractions()
     return None
