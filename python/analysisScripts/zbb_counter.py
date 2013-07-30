#!/usr/bin/env python 
import os
import sys
import PatAnalysis.CMSSW
from ROOT import TLorentzVector
from PatAnalysis.AnalysisEvent import AnalysisEvent
from MonteCarloSelection import delta_R as Delta
from PatAnalysis.EventSelection import prepareAnalysisEvent

def countEvents(path="", output="-", muChannel=True, Njobs=1, jobNumber=1):

  # inputs
  if os.path.isdir(path):
    dirList=list(itertools.islice(os.listdir(path), jobNumber, None, Njobs))
    files=[]
    for fname in dirList:
      files.append(path+"/"+fname)
  elif os.path.isfile(path):
    files=[path]
  else:
    files=[]

  # output
  if output=="-":
    out_file_INCL = sys.stdout
  else:
    out_file_INCL = open(output,"w")

  # counters
  event_num=0
  NrGen1b=0
  NrGen2b=0
  NrGenZj=0
  NrGenZ=0

  # events
  events = AnalysisEvent(files)
  prepareAnalysisEvent(events)
  
  # Event loop
  for event in events:

    # event counter
    if event_num%1000==0:
      print 'Event', event_num  
    event_num+=1
   
    # looking for a Z genparticle candidate in the event
    ZGenOK = event.genZparticle is not None
    if ZGenOK:
      try:
        lep0 = event.genZparticle.daughter(0)
        lep1 = event.genZparticle.daughter(1)
      except:
        lep0 = event.genZparticle[0]
        lep1 = event.genZparticle[1]

    # GEN jet loop to locate jets
    genjetAcc=[]
    for gj in event.genJets:
      if gj.pt()>25 and abs(gj.eta())<2.1:
        if ZGenOK and Delta(gj,lep0)>0.5 and Delta(gj,lep1)>0.5:
          genjetAcc+=[gj]
    GenZj = len(genjetAcc)>0
    
    # GEN jet loop to locate b jets
    genbjet=[]
    for gj in event.sortedGenJets[0]:
      if gj.pt()>25 and abs(gj.eta())<2.1:
        if ZGenOK and Delta(gj,lep0)>0.5 and Delta(gj,lep1)>0.5:
          genbjet+=[gj]
    GenZ1b = len(genbjet)==1
    GenZ2b = len(genbjet)>1

    # count
    if ZGenOK: NrGenZ  += 1
    if GenZj : NrGenZj += 1
    if GenZ1b: NrGen1b += 1
    if GenZ2b: NrGen2b += 1 
  
  ##### closing file ad dump count
  out_file_INCL.write('============================='+'\n')   
  out_file_INCL.write('total : '+ str(event_num) +' \n')
  out_file_INCL.write('Z_kin : '+ str(NrGenZ) +' \n')
  out_file_INCL.write('Z+j   : '+ str(NrGenZj) +' \n')
  out_file_INCL.write('Z+1b  : '+ str(NrGen1b) +' \n')
  out_file_INCL.write('Z+2b  : '+ str(NrGen2b) +' \n')
  out_file_INCL.write('============================'+' \n')   
  out_file_INCL.close()

# run as a script
if __name__=="__main__":
  import sys
  countEvents(*sys.argv[1:])

