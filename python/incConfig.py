import os
from zbbConfig import *

configuration.eventSelection = configuration.pythonpath+"IncEventSelection"

configuration.eventProducers.append(eventProducer("bestDiLeptCandidate", "ObjectSelection", "findBestDiLeptCandidate", { "muChannel":True,"eleChannel":True } ))
configuration.eventProducers.append(eventProducer("isEMUTriggerOK", "ObjectSelection", "isTriggerIncOK", {"perRun":True } ))
#configuration.controlPlots.append(controlPlot("selection", "IncEventSelectionControlPlots", "IncEventSelectionControlPlots", { }))


#control plot classes (since we don't want ZbbEventSelectionControlPlots I replace the whole list
# as it is not straightforward to replace ZbbEventSelectionControlPlots by IncEventSelectionControlPlots
configuration.controlPlots = [ 
    controlPlot("jetmetAK5PF", "ObjectsControlPlots", "JetmetControlPlots", { "btagging":configuration.btagging, "WP":configuration.WP }),
    controlPlot("allMets", "ObjectsControlPlots", "MetControlPlots", { }),
    controlPlot("vertexAssociation", "VertexAssociationControlPlots", "VertexAssociationControlPlots", { }),
    controlPlot("selection", "IncEventSelectionControlPlots", "IncEventSelectionControlPlots", { }),
    controlPlot("matrixElements", "MatrixElementControlPlots", "MatrixElementControlPlots", { }),
    ]

if configuration.runningMode == "plots" :
    plotCP = [
      controlPlot("allmuons", "ObjectsControlPlots", "MuonsControlPlots", { "muonList":"allmuons", "muonType":"none" }),
      controlPlot("tightmuons", "ObjectsControlPlots", "MuonsControlPlots", { "muonType":"tight" }),
      controlPlot("allelectrons", "ObjectsControlPlots", "ElectronsControlPlots", { "electronList":"allelectrons", "electronType":"none" }),
      controlPlot("tightelectrons", "ObjectsControlPlots", "ElectronsControlPlots", { "electronType":"tight" }),
      ]
    for cp in plotCP : configuration.controlPlots.append(cp)
