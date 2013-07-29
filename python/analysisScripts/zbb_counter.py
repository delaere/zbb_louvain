#!/nfs/soft/cms/slc5_amd64_gcc434/cms/cmssw/CMSSW_4_2_7/external/slc5_amd64_gcc434/bin/python
import os
import CMSSW
from ROOT import TLorentzVector
from AnalysisEvent import AnalysisEvent
import EventSelection

#TODO: move Delta to a "utilities.py"
def Delta(par1,par2):
  delta_phi=abs(par2.phi()-par1.phi())
  if delta_phi>pi:
    delta_phi=(2*pi)-delta_phi;
  delta=sqrt((delta_phi)**2 + (par1.eta()-par2.eta())**2)
  return delta

def countEvents(path="", output="", muChannel=True, Njobs=1, jobNumber=1):

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

  # events
  events = AnalysisEvent(files)
  EventSelection.prepareAnalysisEvent(events)
      
  # output
  out_file_INCL= open(output,"w")

  # counters
  gen_llbb=0
  gen_llbbacc=0
  NrGen1b=0
  NrGen2b=0
  NrGenZj=0
  NrGenZ=0
  
  # Event loop
  event_num=0
  for event in events:

    # display some counter
    if event_num%1000==0:
      print 'Event', event_num  
    event_num+=1
   
    # boolean
    GenZ=False
    GenZAcc=False
    GenZMass=False
    ZGenOK=False

    # containers
    b_hadron=[]
    b_quark=[]
   
    # GEN categories
    NoGen=True
    GenZ1b=False
    GenZ2b=False
    GenZj=False
     
    #TODO: it should be generalized and/or use the existing methods for unfolding (Jerome+Ludivine)
    #          - method to find b hadrons
    #          - method to find gen Z
    #          - method to find b jets 
    #          - method to do the isolation
    ## GEN particle loop (for extracting leptons and B-hadrons)
    for part in event.genParticles:
      id = abs(part.pdgId())
      ## looking for a B-hadron candidate (meson)
      if (id>499 and id<600):
        hasBottomedDaughter = False
        for i in range(0, part.numberOfDaughters()):
          idDau=abs(part.daughter(i).pdgId())
          if (idDau>499 and idDau<600):
            hasBottomedDaughter = True
        if hasBottomedDaughter == False:
           b_hadron+=[part]
      ## looking for a B-hadron candidate (baryon)
      if (id>4999 and id<6000):
        hasBottomedDaughter = False
        for i in range(0, part.numberOfDaughters()):
          idDau=abs(part.daughter(i).pdgId())
          if (idDau>4999 and idDau<6000):
            hasBottomedDaughter = True
        if hasBottomedDaughter == False:
           b_hadron+=[part]
      ## looking for a Z genparticle candidate in the event
      if id == 23 and part.status()==3 and GenZMass==False:
        l0=part.daughter(0)
        l1=part.daughter(1)
        if (l0 and l1 and l0.status()==3 and l1.status()==3 and ((muChannel==True and abs(l0.pdgId())==13 and abs(l1.pdgId())==13) or ( muChannel==False and abs(l0.pdgId())==11 and abs(l1.pdgId())==11))):
          GenZ=True
          if (muChannel==True and l0.pt()>20 and l1.pt()>20 and abs(l0.eta())<2.4 and abs(l1.eta())<2.4) or (muChannel==False and l0.pt()>20 and l1.pt()>20 and abs(l0.eta())<2.4 and abs(l1.eta())<2.4):
            GenZAcc=True
            if l0.charge()>0:
              lep0=l0
              lep1=l1
            if l0.charge()<0:
              lep1=l0
              lep0=l1
            l1c=TLorentzVector(lep0.px(),lep0.py(),lep0.pz(),lep0.energy())
            l2c=TLorentzVector(lep1.px(),lep1.py(),lep1.pz(),lep1.energy())
            invGen=(l1c+l2c).M()
            if invGen>76 and invGen<106:
              GenZMass=True
    if (GenZ and GenZAcc and GenZMass):
      ZGenOK=True
    else:
      ZGenOK=False
      noGen=True
    
    # some containers
    genjetAcc=[]
    genbjetAcc=[]
    genbjet=[]
    genbjetAll=[]

    # GEN jet loop to locate jets
    for gj in event.genJets:
      if gj.pt()>25 and abs(gj.eta())<2.1:
        if  ZGenOK==True and Delta(gj,lep0)>0.5 and Delta(gj,lep1)>0.5:
          genjetAcc+=[gj]

    if ZGenOK==True and len(genjetAcc)>0 :
      GenZj=True
    
    # GEN jet loop to locate b jets
    if len(b_hadron)>0:
      b1=[]
      d=9999.
      for gj in event.genJets:
        if gj.pt()>25 and abs(gj.eta())<2.1:
           genbjetAcc+=[gj]
        oneB=False
        for b_it in b_hadron :
          if oneB==False :
            d=Delta(gj,b_it) 
            if d<0.5 :
              b_hadron.remove(b_it)
              genbjetAll+=[gj]
              oneB=True          
              if gj.pt()>25 and abs(gj.eta())<2.1:
                genbjet+=[gj]
          else: break
          
    genbj_iso=[]
         
    # jet isolation
    if ZGenOK==True and len(genbjet)>0 :
      for bj in genbjet :
        if Delta(bj,lep0)>0.5 and Delta(bj,lep1)>0.5:
          genbj_iso+=[bj]
      if len(genbj_iso)==1:    
        GenZ1b=True
        noGen=False
      elif len(genbj_iso)>1:          
        GenZ2b=True
        noGen=False
      else:
        noGen=True
    else:
      noGen=True

    # count
    if(ZGenOK==True):
      NrGenZ+=1
    if(GenZj==True):
      NrGenZj+=1
    if(GenZ1b==True):
      NrGen1b+=1
    if(GenZ2b==True):  
      NrGen2b+=1 
  
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
  countEvents(sys.argv[1:]):

