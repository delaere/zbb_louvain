import FWCore.ParameterSet.Config as cms
from CommonTools.ParticleFlow.goodOfflinePrimaryVertices_cfi import goodOfflinePrimaryVertices

def setupGoodVertex (process):
    process.goodPV = goodOfflinePrimaryVertices.clone(filter=cms.bool(True))
    
def changeVertexCollection (process,seqName='patDefaultSequence'):
    pvCollection=cms.InputTag('goodPV')
    print ""
    print "Switching PV collection for PAT:", pvCollection
    print "***********************************"

    # PV sources to be exchanged:
    pvExchange = ['Vertices','vertices','pvSrc','primaryVertices','srcPVs','vertexes','primaryVertex','vertexTag']
    # PV sources NOT to be exchanged:
    #noPvExchange = ['src','PVProducer','primaryVertexSrc','vertexSrc','primaryVertex']

    # find out all added jet collections (they don't belong to PAT)
    interPostfixes = []
    #for m in getattr(process,seqName).moduleNames():
    #    if m.startswith('patJets') and not len(m)==len('patJets'):
    #        print m
    #        interPostfix = m.replace('patJets','')
    #        interPostfixes.append(interPostfix)
            
    # exchange the primary vertex source of all relevant modules
    for m in getattr(process,seqName).moduleNames():
        modName = m
        # only if the module has a source with a relevant name
        for namePvSrc in pvExchange:
            if hasattr(getattr(process,m),namePvSrc):
                # only if the module is not coming from an added jet collection
                interPostFixFlag = False
                for pfix in interPostfixes:
                    if modName.endswith(pfix):
                        interPostFixFlag = True
                        interPostFixFlag = True
                        break
                if not interPostFixFlag:
                    if getattr(getattr(process,m),namePvSrc) == cms.InputTag("offlinePrimaryVertices"):
                        setattr(getattr(process,m),namePvSrc,pvCollection)
                        print m, "REPLACED"
                    else :
                        print m, "UNCHANGED", getattr(getattr(process,m),namePvSrc)
