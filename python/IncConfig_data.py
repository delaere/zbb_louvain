import os
from zbbConfig_data import *


configuration.eventSelection = configuration.pythonpath+"IncEventSelection"

configuration.eventProducers.append(eventProducer("isEMUTriggerOK", "ObjectSelection", "isTriggerOK", { "muChannel":True,"eleChannel":True,"perRun":True } ))
configuration.eventProducers.append(eventProducer("bestDiLeptCandidate", "ObjectSelection", "findBestDiLeptCandidate", { "muChannel":True,"eleChannel":True } ))
