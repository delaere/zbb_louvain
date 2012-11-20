from DataFormats.FWLite import Events, Handle
from FWCore.ParameterSet.Types import InputTag
import inspect
from datetime import datetime
from math import sin

class AnalysisEvent(Events):
   """A class that complements fwlite::Events with analysis facilities.
      The class provides the following additional functionalities:
        1. instrumentation for event weight
             A set of weight classes can be defined, and the event weight
             is computed and cached using those.
        2. list of event products used in the analysis
             It allows to ask later on simply for "jets" or "electrons"
             to run the fwlite::Handle machinery and/or get the cached result.
        3. a list of "producers" of analysis high-level quantities
             It allows to run "analysis on demand", by automatically running
             the defined producers to fill the cache, and later use that one.
        4. a volatile dictionary
             It allows to use the event as an heterogenous container for
             any analysis product. The event is properly reset when iterating 
             to the next event.
   """

   def __init__(self, inputFiles = '', **kwargs):
     """Initialize the AnalysisEvent like a standard Event, plus additional features."""
     # initialization of base functionalities
     Events.__init__(self,inputFiles,**kwargs)
     # additional features:
     # 1. instrumentation for event weight
     self._weightCache = {}
     self._weightEngines = {}
     # 2. a list of event products used in the analysis
     self._collections = {} 
     # 3. a list of "producers" of analysis high-level quantities
     self._producers = {}
     # 4. volatile dictionary. User can add any quantity to the event and it will be 
     #    properly erased in the iteration step. 
     self.__dict__["vardict"] = {}
     
   def addWeight(self, name, weightClass):
     """Declare a new class (engine) to compute the weights.
        weightClass must have a weight() method returning a float."""
     if name in self._weightEngines:
       raise KeyError("%s weight engine is already declared" % name)
     self._weightEngines[name] = weightClass
     self._weightCache.clear()

   def delWeight(self, name):
     """Remove one weight engine from the internal list."""
     # just to clean the dictionnary
     del self._weightEngines[name]
     self._weightCache.clear()

   def weight(self, weightList=None, **kwargs):
     """Return the event weight. Arguments:
         * weightList is the list of engines to use, as a list of strings. 
              Default: all defined engines.
         * the other named arguments are forwarded to the engines.
        The output is the product of the selected individual weights."""
     # first check in the cache if the result is there already
     if weightList is None:
       weightList=self._weightEngines.keys()
     kwargs["weightList"] = weightList
     # compute the weight or use the cached value
     myhash = self._dicthash(kwargs)
     if not myhash in self._weightCache : 
       w = 1.
       for weightElement in weightList:
         engine = self._weightEngines[weightElement]
         engineArgs = inspect.getargspec(engine.weight).args
         subargs = dict((k,v) for k,v in kwargs.iteritems() if k in engineArgs)
         w *= self._weightCache.setdefault("weightElement:%s # %s" %(weightElement,self._dicthash(subargs)),engine.weight(self,**subargs))
       self._weightCache[myhash] = w
     return self._weightCache[myhash]

   def addCollection(self, name, handle, inputTag):
     """Register an event collection as used by the analysis.
        Example: addCollection("jets","vector<pat::Jet>","cleanPatJets" """
     if name in self._collections:
       raise KeyError("%r collection is already declared", name)
     if name in self._producers:
       raise KeyError("%r is already declared as a producer", name)
     if hasattr(self,name):
       raise AttributeError("%r object already has attribute %r" % (type(self).__name__, attr))
     self._collections[name] = {"handle":Handle(handle),"collection":inputTag}

   def removeCollection(self,name):
     """Forget about the named event collection.
        This method will delete both the product from the cache (if any) and the definition.
        To simply clear the cache, use "del event.name" instead. """
     del self._collections[name]
     if name in self.vardict:
       delattr(self,name)

   def getCollection(self,name):
     """Retrieve the event product or return the cached collection.
        Note that the prefered way to get the collection is instead to access the "event.name" attribute."""
     if not name in self._collections:
       raise AttributeError("%r object has no attribute %r" % name)
     if not name in self.vardict:
       self.getByLabel(self._collections[name]["collection"],self._collections[name]["handle"])
       self.vardict[name] = self._collections[name]["handle"].product()
     return getattr(self,name)

   def addProducer(self,name,producer):
     """Register a producer to create new high-level analysis objects."""
     if name in self._producers:
       raise KeyError("%r producer is already declared", name)
     if name in self._collections:
       raise KeyError("%r is already declared as a collection", name)
     if hasattr(self,name):
       raise AttributeError("%r object already has attribute %r" % (type(self).__name__, attr))
     self._producers[name] = producer

   def removeProducer(self,name):
     """Forget about the producer.
        This method will delete both the product from the cache (if any) and the producer.
        To simply clear the cache, use "del event.name" instead."""
     del self._producers[name]
     if name in self.vardict:
       delattr(self,name)

   def _next (self):
     """(Internal) Iterator internals"""
     # I was willing to call the super._next() with some additional stuff but I didn't find a way.
     # So, I just duplicate the code with some modifications.
     if self._veryFirstTime:
       self._createFWLiteEvent()
     if self._toBegin:
       self._toBeginCode()
     while not self._event.atEnd() :
       self.vardict.clear() #added
       self._weightCache.clear() #added
       yield self
       self._eventCounts += 1
       if self._maxEvents > 0 and self._eventCounts >= self._maxEvents:
         break
       # Have we been asked to go to the first event?
       if self._toBegin:
         self._toBeginCode()
       else:
         # if not, lets go to the next event
         self._event.__preinc__()

   def __getattr__(self, attr):
     """Overloaded getter to handle properly:
          - volatile analysis objects
          - event collections
          - data producers"""
     if attr in self.__dict__["vardict"]:
       return self.vardict[attr]
     if attr in self._collections:
       return getCollection(attr)
     if attr in self._producers:
       return self.vardict.setdefault(attr, self._producers[attr](self))
     raise AttributeError("%r object has no attribute %r" % (type(self).__name__, attr))

   def __setattr__(self, name, value):
     """Overloaded setter that puts any new attribute in the volatile dict."""
     if name in self.__dict__  or not "vardict" in self.__dict__ or name[0]=='_':
       self.__dict__[name] = value
     else:
       if name in self._collections or name in self._producers:
         raise AttributeError("%r object %r attribute is read-only (event collection)" % (type(self).__name__, name))
       self.vardict[name] = value

   def __delattr__(self, name):
     """Overloaded del method to handle the volatile internal dictionary."""
     if name=="vardict":
       raise AttributeError("%r object has no attribute %r" % (type(self).__name__, name))
     if name in self.__dict__:
       del self.__dict__[name]
     elif name in self.vardict:
       del self.vardict[name]
     else:
       raise AttributeError("%r object has no attribute %r" % (type(self).__name__, name))

   def _dicthash(self,dict):
     return (lambda d,j='=',s=';': s.join([j.join((str(k),str(v))) for k,v in d.iteritems()]))(dict)

   def __str__(self):
     """Event text dump."""
     dictjoin = lambda d,j=' => ',s='\n': s.join([j.join((str(k),str(v))) for k,v in d.iteritems()])
     mystring = "=================================================================\n"
     # general information
     mystring += "Run %d - Lumisection %d, Event %d\n" % (self.eventAuxiliary().run(), 
                                                          self.eventAuxiliary().luminosityBlock(),
                                                          self.eventAuxiliary().id().event())
     mystring += "Recorded on %s\n" % datetime.fromtimestamp(self.eventAuxiliary().time().unixTime()).strftime("%Y-%m-%d %H:%M:%S")
     mystring += "-----------------------------------------------------------------\n"
     # weights
     if len(self._weightCache)==0: 
       #mystring += "No weight computed so far. \n" 
       #mystring += "No weight computed so far. Default weight is %f.\n" % self.weight(weightList=self._weightEngines.keys())
       mystring += "No weight computed so far. Default weight is %f.\n" % self.weight()
     else:
       mystring += "Weights:\n"
       mystring += dictjoin(self._weightCache)
     mystring += "\n-----------------------------------------------------------------\n"
     # list the collections
     mystring += "Collections:\n"
     for colname in self._collections.keys():
       collection = self.getCollection(colname)
       handle = str(self._collections[colname]["handle"])
       try:
         mystring += "*** %s has %d elements\n" % (colname,len(collection))
         if "reco::Vertex" in handle:
           mystring += reduce(lambda a,b: a+b,map(self._vertexString,collection))
         elif "pat::Electron" in handle:
           mystring += reduce(lambda a,b: a+b,map(self._electronString,collection))
         elif "pat::Muon" in handle:
           mystring += reduce(lambda a,b: a+b,map(self._muonString,collection))
         elif "pat::Jet" in handle:
           mystring += reduce(lambda a,b: a+b,map(self._jetString,collection))
         elif "pat::MET" in handle:
           mystring += reduce(lambda a,b: a+b,map(self._metString,collection))
         elif "reco::CompositeCandidate" in handle:
           mystring += reduce(lambda a,b: a+b,map(self._candidateString,collection))
       except TypeError:
         pass
     mystring += "\n-----------------------------------------------------------------\n"
     # list the registered producers
     mystring += "Producers:\n"
     mystring += dictjoin(self._producers)
     mystring += "\n-----------------------------------------------------------------\n"
     # list the content of vardict, excluding producers and collections
     mystring += "Content of the cache:\n"
     mystring += dictjoin(dict((k,v) for k, v in self.vardict.iteritems() if not (k in self._producers.keys() or k in self._collections.keys())))
     return mystring

   def _vertexString(self, vertex):
     theString =  "Vertex position: (%f,%f,%f) +/- (%f,%f,%f)\n" % (vertex.x(), vertex.y(),vertex.z(),vertex.xError(),vertex.yError(),vertex.zError())
     theString += "  Number of tracks: %d\n" % vertex.tracksSize()
     theString += "  chi2/ndof: %f/%d\n" % (vertex.chi2(),vertex.ndof())
     return theString

   def _lorentzVectorString(self, label, lorentzVector):
     theString =  "%s candidate\n" % label
     theString += "   (pt, eta, phi) = (%f,%f,%f)\n" % (lorentzVector.Pt(), lorentzVector.Eta(), lorentzVector.Phi())
     theString += "   mass = %f GeV\n" % lorentzVector.M() 
     theString += "   p = %f GeV; mt = %f GeV\n" % (lorentzVector.P(), lorentzVector.Mt())
     return theString

   def _candidateString(self, label, candidate):
     theString =  "%s candidate\n" % label
     theString += "  (pt, eta, phi) = (%f,%f,%f)\n" % (candidate.pt(), candidate.eta(), candidate.phi())
     theString += "  mass = %f GeV\n" % candidate.mass()
     theString += "  charge: %d\n" % candidate.charge()
     theString += "  p = %f GeV; mt = %f GeV\n" % (candidate.p(), candidate.mt())
     return theString

   def _metString(self, met):
     theString = "Missing Et: %f at phi= %f with a significance of %f\n" % (met.et(),met.phi(),met.significance())
     return theString

   def _jetString(self, jet):
     theString =  self._candidateString("jet",jet)
     theString += "  nhf=%f\n" % (( jet.neutralHadronEnergy() + jet.HFHadronEnergy() ) / jet.energy())
     theString += "  nef=%f\n" % (jet.neutralEmEnergyFraction())
     theString += "  nconstituents=%d\n" % (jet.numberOfDaughters())
     theString += "  chf=%f\n" % (jet.chargedHadronEnergyFraction())
     theString += "  nch=%d\n" % (jet.chargedMultiplicity())
     theString += "  cef=%f\n" % (jet.chargedEmEnergyFraction())
     theString += "  B-tagging information:\n"
     theString += "     SSVHE: %f\n" % jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")
     theString += "     SSVHP: %f\n" % jet.bDiscriminator("simpleSecondaryVertexHighPurBJetTags")
     taginfo = jet.tagInfoSecondaryVertex("secondaryVertex")
     if not taginfo is None and jet.bDiscriminator("simpleSecondaryVertexHighEffBJetTags")>0:
       sv = taginfo.secondaryVertex(0)
       if not sv is None:
         distance = taginfo.flightDistance(0,True)
         dir = taginfo.flightDirection(0)
         dirv = ROOT.TVector3(dir.x(),dir.y(),dir.z())
         dirj = ROOT.TVector3(jet.px(),jet.py(),jet.pz())
         theString += "     details about the secondary vertex:\n"
         theString += "     * number of tracks: %d\n" % sv.tracksSize()
         theString += "     * chi2: %f\n" % sv.chi2()
         theString += "     * distance: %f+/-%f" % (distance.value(),distance.error())
         theString += "     * distance significance: %f\n" % distance.significance()
         theString += "     * flight direction: %f,%f,%f\n" % (dir.x(),dir.y(),dir.z())
         theString += "     * dR(jet): %f\n" % dirv.DeltaR(dirj)
         theString += "     * mass: %f\n" % sv.p4().M()
     return theString

   def _electronString(self, electron):
     theString =  self._candidateString("electron",electron)
     scEt = (electron.ecalEnergy()*sin(electron.theta()))
     superclusterEta = abs(electron.superCluster().eta())
     theString += "  Number of missing hits: %d\n" % electron.gsfTrack().numberOfLostHits()
     theString += "  SuperCluster Et: %f\n" % scEt
     theString += "  HCAL isolation: %f\n"  % electron.dr03HcalTowerSumEt()/scEt
     theString += "  ECAL isolation: %f\n"  % electron.dr03EcalRecHitSumEt()/scEt
     theString += "  Tk   isolation: %f\n"  % electron.dr03TkSumPt()/scEt
     theString += "  H over E: %f\n" % electron.hadronicOverEm()
     theString += "  dphi: %f\n" % electron.deltaPhiEleClusterTrackAtCalo()
     theString += "  deta: %f\n" % electron.deltaEtaEleClusterTrackAtCalo()
     theString += "  inin: %f\n" % electron.scSigmaIEtaIEta()
     theString += "  d0: %f\n"   % abs(electron.dB())
     theString += "  supercluster eta: %f\n" % electron.superCluster().eta(),
     if superclusterEta<1.4442 or (superclusterEta>1.566 and superclusterEta<2.5 ):
       theString += " => in fiducial region\n"
     else:
       theString += " => out of fiducial region\n"
     return theString

   def _muonString(self, muon):
     theString =  self._candidateString("muon",muon)
     if muon.isTrackerMuon():
       theString += "  Number of hits (all, pixels, strips): %d,%d,%d\n" % (muon.innerTrack().numberOfValidHits(),
                                                                            muon.innerTrack().hitPattern().numberOfValidPixelHits(),
                                                                            muon.innerTrack().hitPattern().numberOfValidStripHits())
     if muon.isGlobalMuon():
       theString += "  Number of muon hits: %d\n" % muon.globalTrack().hitPattern().numberOfValidMuonHits()
     if muon.isTrackerMuon() and muon.isGlobalMuon():
       theString += "  Chi2: %f\n" % muon.normChi2()
     theString += "  Isolation: (%f+%f)/pt = %f\n" % (muon.trackIso(),muon.caloIso(),(muon.trackIso()+muon.caloIso())/muon.pt())
     return theString

