from PatAnalysis.BaseControlPlots import BaseControlPlots
from MonteCarloSelection import isZbbEvent, isZbcEvent, isZblEvent, isZccEvent, isZclEvent, isZlEvent

class MonteCarloSelectionControlPlots(BaseControlPlots):
    """A class to create control plots for MC event selection"""

    def __init__(self, dir=None, dataset=None, mode="plots"):
      # create output file if needed. If no file is given, it means it is delegated
      BaseControlPlots.__init__(self, dir=dir, purpose="mcSelection", dataset=dataset, mode=mode)

    def beginJob(self):
      # declare histograms
      self.add("eventType","Event Type (0,ll,cl,cc,bl,bc,bb)+Z",10,-0.5,9.5)

      self.add("LepPosPx","Generator cuadrivector, LepPosPx", 400, -400, 400)
      self.add("LepPosPy","Generator cuadrivector, LepPosPy", 400, -400, 400)
      self.add("LepPosPz","Generator cuadrivector, LepPosPz", 400, -400, 400)
      self.add("LepPosEn","Generator cuadrivector, LepPosEn", 400, 0, 400)

      self.add("LepNegPx","Generator cuadrivector, LepNegPx", 400, -400, 400)
      self.add("LepNegPy","Generator cuadrivector, LepNegPy", 400, -400, 400)
      self.add("LepNegPz","Generator cuadrivector, LepNegPz", 400, -400, 400)
      self.add("LepNegEn","Generator cuadrivector, LepNegEn", 400, 0, 400)

      self.add("BottomPx","Generator cuadrivector, BottomPx", 400, -400, 400)
      self.add("BottomPy","Generator cuadrivector, BottomPy", 400, -400, 400)
      self.add("BottomPz","Generator cuadrivector, BottomPz", 400, -400, 400)
      self.add("BottomEn","Generator cuadrivector, BottomEn", 400, 0, 400)

      self.add("AntibottomPx","Generator cuadrivector, AntibottomPx", 400, -400, 400)
      self.add("AntibottomPy","Generator cuadrivector, AntibottomPy", 400, -400, 400)
      self.add("AntibottomPz","Generator cuadrivector, AntibottomPz", 400, -400, 400)
      self.add("AntibottomEn","Generator cuadrivector, AntibottomEn", 400, 0, 400)

      self.add("FlavLepPos","FlavLepPos status3", 32, -16., 16.)
      self.add("FlavLepNeg","FlavLepNeg status3", 32, -16., 16.)

      self.add("NLepPos","NLepPos status3", 10, -0.5, 9.5)
      self.add("NLepNeg","NLepNeg status3", 10, -0.5, 9.5)
      self.add("NBottom","NBottom status3", 10, -0.5, 9.5)
      self.add("NAntibottom","NAntibottom status3", 10, -0.5, 9.5)

      # various local variables
      self.cjet = 0
      self.bjet = 0
      self.ljet = 0
      self.i = 0
      self._ran = False

    def process(self,event):
      """monteCarloSelectionControlPlots"""
      result = { }
      self._ran = True
     
      #Fill some gen information for the status 3 leptons and b, and bbar quarks
      nLepPos = 0
      nLepNeg = 0
      nBottom = 0
      nAntibottom = 0
      flavLepPos = 0
      flavLepNeg = 0

      lepPosPx = 0
      lepPosPy = 0
      lepPosPz = 0
      lepPosEn = 0

      lepNegPx = 0
      lepNegPy = 0
      lepNegPz = 0
      lepNegEn = 0

      bottomPx = 0
      bottomPy = 0
      bottomPz = 0
      bottomEn = 0

      antibottomPx = 0
      antibottomPy = 0
      antibottomPz = 0
      antibottomEn = 0
      
      particles = event.genParticles

      for part in particles:
	if part.status()!=3: break;
        
	if part.pdgId() == -11 or part.pdgId() == -13 or part.pdgId() == -15  :
	  if nLepPos == 0 :
	    lepPosPx = part.px()
	    lepPosPy = part.py()
	    lepPosPz = part.pz()
	    lepPosEn = part.energy()
	    flavLepPos = part.pdgId()
          nLepPos =+ 1

	if part.pdgId() == 11 or part.pdgId() == 13 or part.pdgId() == 15  :
	  if nLepNeg == 0 : 
	    lepNegPx = part.px()
	    lepNegPy = part.py()
	    lepNegPz = part.pz()
	    lepNegEn = part.energy()
	    flavLepNeg = part.pdgId()
          nLepNeg =+ 1

	if part.pdgId() == 5 :
	  if nBottom == 0 : 
	    bottomPx = part.px()
	    bottomPy = part.py()
	    bottomPz = part.pz()
	    bottomEn = part.energy()
          nBottom =+ 1

	if part.pdgId() == -5 :
	  if nAntibottom == 0 : 
	    antibottomPx = part.px()
	    antibottomPy = part.py()
	    antibottomPz = part.pz()
	    antibottomEn = part.energy()
          nAntibottom =+ 1

      result["NLepPos"] = nLepPos
      result["NLepNeg"] = nLepNeg
      result["NBottom"] = nBottom
      result["NAntibottom"] = nAntibottom
      result["FlavLepPos"] = flavLepPos
      result["FlavLepNeg"] = flavLepNeg

      result["LepPosPx"] = lepPosPx
      result["LepPosPy"] = lepPosPy
      result["LepPosPz"] = lepPosPz
      result["LepPosEn"] = lepPosEn

      result["LepNegPx"] = lepNegPx
      result["LepNegPy"] = lepNegPy
      result["LepNegPz"] = lepNegPz
      result["LepNegEn"] = lepNegEn

      result["BottomPx"] = bottomPx
      result["BottomPy"] = bottomPy
      result["BottomPz"] = bottomPz
      result["BottomEn"] = bottomEn

      result["AntibottomPx"] = antibottomPx
      result["AntibottomPy"] = antibottomPy
      result["AntibottomPz"] = antibottomPz
      result["AntibottomEn"] = antibottomEn
      
      #Clasify the event in Zbb,Zbc,Zbl,Zcc, Zcl, or Zll
      self.i += 1
      if isZbbEvent(event):
        self.bjet += 1
        result["eventType"] = 6
        return result
      if isZbcEvent(event):
        self.bjet += 1
        result["eventType"] = 5
        return result
      if isZblEvent(event):
        self.bjet += 1
        result["eventType"] = 4
        return result
      if isZccEvent(event):
        self.cjet += 1
        result["eventType"] = 3
        return result
      if isZclEvent(event):
        self.cjet += 1
        result["eventType"] = 2
        return result
      if isZlEvent(event):
        self.ljet += 1
        result["eventType"] = 1
        return result
      result["eventType"] = 0
      return result

    def endJob(self):
      BaseControlPlots.endJob(self)
      if self._ran:
        print "summary: out of",self.i,"events:",self.cjet,"cZ events",self.bjet,"bZ events and",self.ljet," light jets events."

if __name__=="__main__":
  import sys
  from BaseControlPlots import runTest
  runTest(sys.argv[1], MonteCarloSelectionControlPlots())

