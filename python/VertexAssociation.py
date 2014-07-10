def checkVertexAssociation(zcandidate, jets, vertices):
  # condition 1: both leptons are from the same vertex
  if not zVertex(zcandidate, 0.05):
    return False
  # condition 2: strict lepton to vertex association
  vertex = findPrimaryVertex(zcandidate, vertices)
  if not zVertex(zcandidate, 0.05,vertex):
    return False
  # condition 3: at least one of the jets is associated to the z vertex.
  for jet in jets:
    if jetVertex(vertex, jet, 2, 2, 0.5):
      return True
  return False

def findPrimaryVertex(zcandidate, vertices):
  # look for closest vertex
  # vertices are already filtered... no need to check quality
  lepton1 = zcandidate.daughter(0)
  lepton2 = zcandidate.daughter(1)
  vz = (lepton1.vz()+lepton2.vz())/2.
  mindz = 1000.
  closestVertex = vertices[0]
  for vertex in vertices:
    if abs(vertex.z()-vz)<mindz :
      mindz = abs(vertex.z()-vz)
      closestVertex = vertex
  return closestVertex

def findPrimaryVertexIndex(zcandidate, vertices):
  # look for closest vertex
  # vertices are already filtered... no need to check quality
  lepton1 = zcandidate.daughter(0)
  lepton2 = zcandidate.daughter(1)
  vz = (lepton1.vz()+lepton2.vz())/2.
  mindz = 1000.
  closestVertex = 0
  for index,vertex in enumerate(vertices):
    if abs(vertex.z()-vz)<mindz :
      mindz = abs(vertex.z()-vz)
      closestVertex = index
  return closestVertex

def zVertex(zcandidate, cut, vertex=None):
  lepton1 = zcandidate.daughter(0)
  lepton2 = zcandidate.daughter(1)
  if vertex is None:
    #loose criteria: both leptons close one of each other
    return abs(lepton1.vz()-lepton2.vz())<cut
  else:
    #strict criteria: both leptons are close to the (same) vertex
    if not type(vertex).__name__ == 'reco::Vertex' :
      print "Warning : argument vertex is not of type reco::Vertex "
      return abs(lepton1.vz()-lepton2.vz())<cut
    return (abs(lepton1.vz()-vertex.z())<cut and abs(lepton2.vz()-vertex.z())<cut)

def isfromVertex(lepton1, lepton2, cut, vertex=None):
  if vertex is None:
    #loose criteria: both leptons close one of each other
    return abs(lepton1.vz()-lepton2.vz())<cut
  else:
    #strict criteria: both leptons are close to the (same) vertex
    if not type(vertex).__name__ == 'reco::Vertex' :
      print "Warning : argument vertex is not of type reco::Vertex "
      return abs(lepton1.vz()-lepton2.vz())<cut
    return (abs(lepton1.vz()-vertex.z())<cut and abs(lepton2.vz()-vertex.z())<cut)

def isFromVertex_SingleLepton(lepton, cut, vertex=None):
    if vertex is None:
        print "Warning : No vertex given, will return true"
        return True
    else:
        return abs(lepton.vz()-vertex.z())<cut

def jetVertex(vertex, jet, algo, sigmaCut, fraction):
  if algo==1 : return jetVertex_1(vertex, jet, sigmaCut, fraction)
  #if algo==2 : return jetVertex_2(vertex, jet, sigmaCut, fraction)
  if algo==2 : return jetVertex_2b(vertex, jet, fraction)
  if algo==3 : return jetVertex_3(vertex, jet, sigmaCut, fraction)

def jetVertex_1(vertex, jet, sigcut, etcut):
  ptsum = 0.
  for i in range(jet.getPFConstituents().size()):
    #make sure the object is usable
    #the last condition is a fix if we miss muons and electrons in the file, for rare occurences...
    #apparently something in the vz() calculation.
    if jet.getPFConstituent(i).trackRef().isNull():
      continue
    if jet.getPFConstituent(i).muonRef().isNonnull () or jet.getPFConstituent(i).gsfTrackRef().isNonnull ():
      continue
    distance = (jet.getPFConstituent(i).vz() - vertex.z())
    error = (jet.getPFConstituent(i).trackRef().dzError()**2 + vertex.zError()**2)**(1/2.)
    #error = vertex.zError()
    sig = distance/error
    if abs(sig)<sigcut :
      ptsum += jet.getPFConstituent(i).pt()
  if ptsum/jet.et() > etcut :
    return True
  else :
    return False

def jetVertex_2(vertex, jet, sigcut, ptcut):
  ptsum = 0.
  ptsumall = 0.
  for i in range(jet.getPFConstituents().size()):
    if jet.getPFConstituent(i).trackRef().isNull():
      continue
    if jet.getPFConstituent(i).muonRef().isNonnull () or jet.getPFConstituent(i).gsfTrackRef().isNonnull ():
      continue
    distance = (jet.getPFConstituent(i).vz() - vertex.z())
    error = (jet.getPFConstituent(i).trackRef().dzError()**2 + vertex.zError()**2)**(1/2.)
    #error = vertex.zError()
    sig = distance/error
    if abs(sig)<sigcut :
      ptsum += jet.getPFConstituent(i).pt()
    ptsumall += jet.getPFConstituent(i).pt()
  if ptsumall==0.:
     return False
  if ptsum/ptsumall > ptcut :
    return True
  else :
    return False

def jetVertex_3(vertex, jet, sigcut, etcut):
  ptsumx = 0.
  ptsumy = 0.
  for i in range(jet.getPFConstituents().size()):
    if jet.getPFConstituent(i).trackRef().isNull():
      continue
    if jet.getPFConstituent(i).muonRef().isNonnull () or jet.getPFConstituent(i).gsfTrackRef().isNonnull ():
      continue
    distance = (jet.getPFConstituent(i).vz() - vertex.z())
    error = (jet.getPFConstituent(i).trackRef().dzError()**2 + vertex.zError()**2)**(1/2.)
    #error = vertex.zError()
    sig = distance/error
    if abs(sig)<sigcut :
      ptsumx += jet.getPFConstituent(i).px()
      ptsumy += jet.getPFConstituent(i).py()
  if (ptsumx**2+ptsumy**2)**(0.5)/jet.et() > etcut :
    return True
  else :
    return False

def jetVertex_2b(vertex, jet, ptcut):
  """ alternate to jetVertex_2 where we try to directly use tracks associated to the vertex.
      This requires a patched DataFormat/RecoVertex where tracks are public (only a pb in python). """
  ptsum = 0.
  ptsumall = 0.
  trackrefs = map(lambda x:vertex.tracks_[x].key(),range(vertex.tracks_.size()))
  for i in range(jet.getPFConstituents().size()):
    if jet.getPFConstituent(i).trackRef().isNull():
      continue
    try:
      trackrefs.index(jet.getPFConstituent(i).trackRef().key())
    except:
      pass
    else:
      ptsum += jet.getPFConstituent(i).pt()
    ptsumall += jet.getPFConstituent(i).pt()
  if ptsumall==0.:
     return False
  if ptsum/ptsumall > ptcut :
    return True
  else :
    return False
