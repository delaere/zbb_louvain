import CMSSW
from DataFormats.FWLite import Events, Handle
from FWCore.ParameterSet.Types import InputTag
from inspect import getargspec
from datetime import datetime
from collections import Iterable
from types import StringTypes

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
         engineArgs = getargspec(engine.weight).args
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

   def addProducer(self,name,producer,**kwargs):
     """Register a producer to create new high-level analysis objects."""
     # sanity checks
     if name in self._producers:
       raise KeyError("%r producer is already declared", name)
     if name in self._collections:
       raise KeyError("%r is already declared as a collection", name)
     if hasattr(self,name):
       raise AttributeError("%r object already has attribute %r" % (type(self).__name__, attr))
     # remove name and producer from kwargs
     if "name" in kwargs: del kwargs["name"]
     if "producer" in kwargs: del kwargs["producer"]
     # store
     self._producers[name] = (producer,kwargs)

   def removeProducer(self,name):
     """Forget about the producer.
        This method will delete both the product from the cache (if any) and the producer.
        To simply clear the cache, use "del event.name" instead."""
     del self._producers[name]
     if name in self.vardict:
       delattr(self,name)

   def run(self):
     """Run number"""
     return self.eventAuxiliary().run()

   def event(self):
     """Event number"""
     return self.eventAuxiliary().id().event()

   def lumi(self):
     """Lumisection"""
     return self.eventAuxiliary().luminosityBlock()

   def to(self,run,event,lumi=None):
     """Jump to some event,run,lumisection"""
     if self._veryFirstTime:
       self._createFWLiteEvent()
     if lumi is None:
       return self._event.to ( long(run), long(event) )
     else:
       return self._event.to ( long(run), long(lumi), long(event) )

   def __getitem__(self,index):
     """Jump to some event,run,(lumisection) or to a given event index"""
     if len(index) == 3:
       self.to(index[0],index[1],index[2])
     elif len(index) == 2:
       self.to(index[0],index[1])
     elif len(index) == 1:
       self.to(index[0])
     else:
       raise TypeError("Events must be indexed by run, event, (lumi) or by event index.")
     return self

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
       self.getByLabel(self._collections[attr]["collection"],self._collections[attr]["handle"])
       return self.vardict.setdefault(attr, self._collections[attr]["handle"].product())
     if attr in self._producers:
       return self.vardict.setdefault(attr, self._producers[attr][0](self, **self._producers[attr][1]))
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
       mystring += "*** %s has %d elements\n" % (colname,len(collection))
       mystring += reduce(lambda a,b: a+b,map(str,collection))
     mystring += "\n-----------------------------------------------------------------\n"
     # list the registered producers
     mystring += "Producers:\n"
     mystring += dictjoin(self._producers)
     mystring += "\n-----------------------------------------------------------------\n"
     # list the content of vardict, excluding collections
     mystring += "Content of the cache:\n"
     for k, v in self.vardict.iteritems():
       if k in self._collections.keys() : continue
       if isinstance(v,Iterable) and not isinstance(v,StringTypes):
         try:
           thisstring = "%s => vector of %d objects(s)\n" % (k,len(v))
         except:
           mystring += "%s => %s\n"%(k,str(v))
         else:
           try:
             for it,vec in enumerate(v):
               thisstring += "%s[%d] = %s\n"%(k,it,str(vec))
           except: 
             mystring += "%s => %s\n"%(k,str(v))
           else:
             mystring += thisstring
       else:
         mystring += "%s => %s\n"%(k,str(v))
     return mystring

