#!/nfs/soft/cms/slc5_amd64_gcc434/cms/cmssw/CMSSW_4_2_7/external/slc5_amd64_gcc434/bin/python
from itertools import combinations
import ROOT
from ROOT import TLorentzVector
import numpy as n
import sys
import os
from DataFormats.FWLite import Events, Handle
from LumiReWeighting import LumiReWeighting
from zbbCommons import zbblabel
from math import *
from ROOT import TFile, TTree, TH1F
from array import array


def Delta(par1,par2):
  delta_phi=abs(par2.phi()-par1.phi())
  if delta_phi>pi:
    delta_phi=(2*pi)-delta_phi;
  delta=sqrt((delta_phi)**2 + (par1.eta()-par2.eta())**2)
  return delta

#---------------------------------- for RUNNING in batch------------------------------------------------------
#def dumpAll(muChannel=True, path="/storage/data/cms/store/user/castello/Unfolding2012/DYJets_unfolding_test/",fileAll="output.out"):
#def dumpAll(muChannel=True, path="/storage/data/cms/store/user/castello/Unfolding2012/DYJets_unfolding_noRecoBias/",fileAll="output.out"):


###############################################################
##   out_file_INCL= open(fileAll,"w")
##   dirList=os.listdir(path)
##   files=[]
##   dirList.sort()
##   for fname in dirList:
##       files.append(path+fname)
##       print 'file names', path+fname      
### for quick run######################
#read input files
#  files=[]  
#  files.append(infile1)
#  files.append(infile2)
#  #files.append(infile3)

###########################################################

def dumpAll(stage=9, muChannel=True, path="/storage/data/cms/store/user/castello/Unfolding2012/DYJets_unfolding_noRecoBias_jetNoNuBSM/castello/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/unfolding2012_v2_DYJets_unfolding_noRecoBias_jetNoNuBSM/1954ed00d02907f647c9352bb10d836e/",fileAll=None, numb=None, output=None):
  out_file_INCL= open(fileAll,"w")
  dirList=os.listdir(path)
  files=[]
  number=0
  numb = int(numb)
  filemin = numb*1
  filemax = numb*1 + 2
  dirList.sort()
  #print 'number', numb, '\n'
  #print 'filemin', filemin,'\n'
  #print 'filemax', filemax,'\n'
  for fname in dirList:
    number+=1
    print 'file names', path+fname
    if number>filemin and number<filemax:
      files.append(path+fname)
      out_file_INCL.write('File name: '+ path+fname +' \n')

      
  events = Events (files)
  jetlabel="cleanPatJets"
  jetgenlabel="patJets"
  jetalllabel="patJets"

  zeelabelAll="ZelAllelAll"
  zmmlabelAll="ZmuAllmuAll"
  
  genpartlabel="prunedGen"
  labelElectron = "matchedElectrons"
  labelAllElectron = "allElectrons"
  labelAllMuon = "allMuons"
  labelMuon = "matchedMuons"
  vertexLabel ="goodPV"
  PULabel = "addPileupInfo"
  #GenjetLabel= "prunedJets"
  GenjetLabel= "prunedNoNuBSMJets" ## new jet collection from Andrew

  jetHandle = Handle ("vector<pat::Jet>")
  jetallHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  
  zeleAllHandle = Handle ("vector<reco::CompositeCandidate>")
  zmuAllHandle = Handle ("vector<reco::CompositeCandidate>")
  
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  genpartHandle =  Handle("std::vector<reco::GenParticle>")
  muonHandle = Handle ("vector<pat::Muon>")
  electronHandle = Handle ("vector<pat::Electron>")
  PrimaryVertexHandle = Handle ("vector<reco::Vertex>")
  AllelectronHandle = Handle ("vector<pat::Electron>")
  AllmuonHandle = Handle ("vector<pat::Muon>")
  genJetHandle = Handle ("vector<reco::GenJet>")
  PUHandle= Handle("std::vector<PileupSummaryInfo>")
  #---------------------------------------------------------------------------------------------
  gen_llbb=0
  gen_llbbacc=0
  NrGen1b=0
  NrGen2b=0
  NrGenZj=0
  NrGenZ=0
  
  #---------------------------------------------------------------------------------------------
  # Event loop
  event_num=0
  for event in events:
   #if event_num > -1: 
    if event_num%1000==0:
      print 'Event', event_num  
    event_num+=1
    event.getByLabel (genpartlabel,genpartHandle)
    genparts = genpartHandle.product()
    event.getByLabel (jetlabel,jetHandle)
    event.getByLabel (jetalllabel,jetallHandle)
   
    #event.getByLabel (PULabel,PUHandle)
    #event.getByLabel (labelElectron,electronHandle)
    #event.getByLabel (labelMuon,muonHandle)
    #event.getByLabel (vertexLabel, PrimaryVertexHandle)
    event.getByLabel (GenjetLabel,genJetHandle) #jetgenlabel,
    #event.getByLabel (labelAllElectron,AllelectronHandle)
    #event.getByLabel (labelAllMuon,AllmuonHandle)
        
    #PU= PUHandle.product()
    jets = jetHandle.product()
    
    #vertices = PrimaryVertexHandle.product()
    #muons = muonHandle.product()
    #electrons = electronHandle.product()
    #AllMu = AllmuonHandle.product()
    #Allelec = AllelectronHandle.product()
    #numberOfInteractions = PUHandle.product()[0].getPU_NumInteractions()
    run = event.eventAuxiliary().run()
    triggerInfo = None
    GenJet= genJetHandle.product()

    #--------------------------------------------------------------------------------------------
    #                                      start work with GEN info
    #--------------------------------------------------------------------------------------------

    ## defined for each event
    
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
     
    ## GEN particle MAIN loop (for extracting leptons and B-hadrons)
    for part in genparts:
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
        #print 'status', part.status()
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
            #print 'invGenMass-->', invGen
            if invGen>76 and invGen<106:
              GenZMass=True

    if (GenZ and GenZAcc and GenZMass):
      ZGenOK=True
    else:
      ZGenOK=False
      noGen=True
    
    #----------------------------------------------------------------------------------------------------------------
    #                                      GEN jet collection matched with  B-hadron
    #----------------------------------------------------------------------------------------------------------------

    genjetAcc=[]
    genbjetAcc=[]
    genbjet=[]
    genbjetAll=[]

    for gj in GenJet:
      if gj.pt()>25 and abs(gj.eta())<2.1:
        if  ZGenOK==True and Delta(gj,lep0)>0.5 and Delta(gj,lep1)>0.5:
          genjetAcc+=[gj]


    #print 'genJetAcc size= ', len(genjetAcc)  
    if ZGenOK==True and len(genjetAcc)>0 :
      GenZj=True
    
    if len(b_hadron)>0:
      b1=[]
      d=9999.
      for gj in GenJet:
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
          
    #----------------------------------------------------------------------------------------------------------------
    #                                       ISOLATION from leptons
    #----------------------------------------------------------------------------------------------------------------

    genbj_iso=[]
         
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


## FOR RUNNING LOCALLY --------------------------
##dumpAll()

## FOR RUNNING WITH SCRIPT ----------------------
for num, arg in enumerate(sys.argv):
  print num, arg
 
dumpAll(fileAll=sys.argv[1],numb=sys.argv[2])
