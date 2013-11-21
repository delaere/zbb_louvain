import ROOT
import PatAnalysis.CMSSW

class LumiReWeighting:
   """A class to reweight MC according to number of pileup events."""

   def __init__(self, MonteCarloFileName, DataFileName, systematicShift=0):
      # set the names for histograms. In the new scheme, the data file contains three histograms for nominal and +/-1sigma.
      MonteCarloHistName = "pileup"
      DataHistName = { 0 : "pileup", -1 : "pileupDOWN1", 1 : "pileupUP1" }
      # access histograms and initialize the weights
      self.engine = ROOT.edm.LumiReWeighting(MonteCarloFileName,DataFileName,MonteCarloHistName,DataHistName[systematicShift])

   def weight( self, event=None, npu=None):
     """Lumi (PU) weight"""
     # returns the weight computed from the true number of interactions. 
     if npu is None and not event is None:
       # for data, immediately return 1.
       if event.object().event().eventAuxiliary().isRealData(): 
         return 1.
       # else, pick the npu from the event
       npu = self.npu(event)
     if not npu is None:
       # return the weight
       return self.engine.weight(npu)
     else:
       print "ERROR:  no in-time beam crossing found! "
       return 0.
 
   def npu( self, fwevent):
     # find the "BX0" and the true number of PU interactions in there
     for pvi in fwevent.PileupSummaryInfo:
       if pvi.getBunchCrossing()==0:
         return pvi.getTrueNumInteractions()
     return None

