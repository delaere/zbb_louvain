import ROOT
from DataFormats.FWLite import Events, Handle
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
ROOT.gSystem.Load("libPhysicsToolsUtilities.so")
#from myFuncTimer import print_timing


class LumiReWeighting:
   """A class to reweight MC according to number of pileup events."""

   def __init__(self, MonteCarloFileName=None, DataFileName=None, MonteCarloHistName="pileup", DataHistName="pileup", PileupSummaryInfo="addPileupInfo", systematicShift=0):
      # access histograms and initialize the weights
      self.engine = ROOT.edm.LumiReWeighting(MonteCarloFileName,DataFileName,MonteCarloHistName,DataHistName)
      self.PoissonMeanShifter = ROOT.reweight.PoissonMeanShifter(systematicShift)
      self.systematicShift = systematicShift
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
       # return the weight, maybe shifted for systematic studies
       return self.engine.weight3BX(npu)*self.shiftWeight(npu)
     else:
       print "ERROR:  no in-time beam crossing found! "
       return 0.
 
   def npu( self, fwevent):
     # get pileup summary information
     fwevent.getByLabel(self.PileupSummaryInfo, self.PupInfo)
     pileup = self.PupInfo.product()
     # find the "BX0" and the number of PU interactions in there
     npu = 0.
     nbc = 0
     for pvi in pileup:
       if pvi.getBunchCrossing() in [-1,0,1]:
         npu += pvi.getPU_NumInteractions()
         nbc += 1
         break
     if nbc>0 : npu = npu/nbc
     return npu

   def shiftWeight( self, npu):
     if self.systematicShift==0 :
       return 1
     else:
       return self.PoissonMeanShifter.ShiftWeight(npu)
