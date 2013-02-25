#!/nfs/soft/cms/slc5_amd64_gcc434/cms/cmssw/CMSSW_4_2_7/external/slc5_amd64_gcc434/bin/python
from itertools import combinations
import ROOT
from ROOT import TLorentzVector
import numpy as n
import sys
import os
from DataFormats.FWLite import Events, Handle
from eventSelection import eventCategories, eventCategory, isInCategory, findBestCandidate, isGoodJet, isBJet,findDijetPair,hasNoOverlap,isZcandidate,isGoodMet
from LumiReWeighting import LumiReWeighting
from monteCarloSelection import isZbEvent
from zbbCommons import zbblabel
from math import *
from ROOT import TFile, TTree, TH1F
from array import array

#---------------------------------------------------------------------------------------------
def Delta(par1,par2):
  delta_phi=abs(par2.phi()-par1.phi())
  if delta_phi>pi:
    delta_phi=(2*pi)-delta_phi;
  delta=sqrt((delta_phi)**2 + (par1.eta()-par2.eta())**2)
  return delta
#---------------------------------------------------------------------------------------------
#                                           Call Function
#---------------------------------------------------------------------------------------------
#------------------------------------FOR RUNNING with the script -----------------------------
def dumpAll(stage=9, muChannel=True, path="/home/fynu/lceard/store/Prod_MC_2011_V2/Summer11/Eff_2/DYJets_Summer11/",fileAll=None,numb=None):
  out_file_INCL= open(fileAll,"w")
  dirList=os.listdir(path)
  files=[]
  number=0
  numb = int(numb)
  filemin = numb*10
  filemax = numb*10 + 10
  try:
    dirList.remove("Ready_Files")
  except:
    pass
  try:
    dirList.remove("files.txt")
  except:
    pass
  dirList.sort()
  for fname in dirList:
    number+=1
    if number>filemin and number<filemax:
      files.append(path+fname)
      print 'file names', path+fname
  events = Events (files)

  metlabel="patMETsPF"
  jetlabel="cleanPatJets"
  jetgenlabel="patJets"
  jetalllabel="patJets"
  zmulabel="ZmuMatchedmuMatched"
  zelelabel="ZelMatchedelMatched"

  zeelabelAll="ZelAllelAll"
  zmmlabelAll="ZmuAllmuAll"
  
  genpartlabel="genParticles"
  labelElectron = "matchedElectrons"
  labelAllElectron = "allElectrons"
  labelAllMuon = "allMuons"
  labelMuon = "matchedMuons"
  vertexLabel ="goodPV"
  PULabel = "addPileupInfo"
  GenjetLabel= "genJets"

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

  numerator=0
  denominator=0
  a_coeff =0
  b_coeff =0
  c_coeff =0
  d_coeff =0
  e_coeff =0
  f_coeff =0
  g_coeff =0
  h_coeff =0
  i_coeff =0
  
  lljj=0
  llj=0

  ll_sel_jj=0
  ll_sel_j=0


  ll_match_jj=0
  ll_match_j=0
  
  ll_match_bbhe=0
  ll_match_bhe=0

  ll_match_bbhp=0
  ll_match_bhp=0

  gen_llbb=0
  gen_llbbacc=0


#---------------------------------------------------------------------------------------------
# Event loop
  event_num=0
  for event in events:
    nZ=0
    #print '----beginning of event --------------'
    if event_num%500==0:
      print 'Event', event_num  
    event_num+=1
    event.getByLabel (genpartlabel,genpartHandle)
    genparts = genpartHandle.product()
    if isZbEvent(event)==False and muChannel==False:
      #print " not Z+b"
      continue
    event.getByLabel (jetlabel,jetHandle)
    event.getByLabel (jetalllabel,jetallHandle)
    event.getByLabel (metlabel,metHandle)
    event.getByLabel (zmulabel,zmuHandle)
    event.getByLabel (zelelabel,zeleHandle)
    event.getByLabel (PULabel,PUHandle)
    event.getByLabel (labelElectron,electronHandle)
    event.getByLabel (labelMuon,muonHandle)
    event.getByLabel (vertexLabel, PrimaryVertexHandle)
    event.getByLabel (jetgenlabel,GenjetLabel,genJetHandle)
    event.getByLabel (labelAllElectron,AllelectronHandle)
    event.getByLabel (labelAllMuon,AllmuonHandle)

    event.getByLabel (zeelabelAll,zeleAllHandle)
    event.getByLabel (zmmlabelAll,zmuAllHandle)
        
    PU= PUHandle.product()
    jets = jetHandle.product()
    met = metHandle.product()
    zCandidatesMu = zmuHandle.product()
    zCandidatesEle = zeleHandle.product()

    zCandidatesEleAll = zeleAllHandle.product()
    zCandidatesMuAll = zmuAllHandle.product()
    
    vertices = PrimaryVertexHandle.product()
    muons = muonHandle.product()
    electrons = electronHandle.product()
    AllMu = AllmuonHandle.product()
    Allelec = AllelectronHandle.product()
    numberOfInteractions = PUHandle.product()[0].getPU_NumInteractions()
    run = event.eventAuxiliary().run()
    triggerInfo = None
    GenJet= genJetHandle.product()

    #--------------------------------------------------------------------------------------------
    #                                        Event Pile up Weight
    #--------------------------------------------------------------------------------------------

    

    #--------------------------------------------------------------------------------------------
    #                                      start work with GEN info
    #--------------------------------------------------------------------------------------------

    ## defined for each event

    # boolean
    GenZ=False
    GenZAcc=False
    GenZMass=False
    ZGenOK=False

    RecoZMatch=False
    RecoZAcc=False
    ZRecoOK=False

    ep=False
    em=False

    # containers
    b_hadron=[]
    anyLepPos=[]
    anyLepNeg=[]

    
    # GEN categories
    NoGen=True
    Gen1b=False
    Gen2b=False
    
    # RECO categories 
    NoReco=True
    Reco1b=False
    Reco2b=False


     
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

      ## not used, but useful ------------------------
      if muChannel==True and abs(id)==13 and part.status()==3:
        if part.charge()>0: anyLepPos+=part
        if part.charge()<0: anyLepNeg+=part
        
      if muChannel==False and abs(id)==11 and part.status()==3:
        if part.charge()>0: anyLepPos+=part
        if part.charge()<0: anyLepNeg+=part
      ## ---------------------------------------------  
        
      ## looking for a Z genparticle candidate in the event
      if id == 23 and part.status()==3  and GenZMass==False:
        #print 'status', part.status()
        l0=part.daughter(0)
        l1=part.daughter(1)
        if l0 and l1 and ((muChannel==True and abs(l0.pdgId())==13 and abs(l1.pdgId())==13) or (muChannel==False and abs(l0.pdgId())==11 and abs(l1.pdgId())==11) and l0.status()==3 and l1.status()==3):
          GenZ=True
          if l0.charge()>0:
            genPos=l0
            genNeg=l1
          if l0.charge()<0:
            genPos=l1
            genNeg=l0
          if (muChannel==True and l0.pt()>20 and l1.pt()>20 and abs(l0.eta())<2.1 and abs(l1.eta())<2.1) or (muChannel==False and l0.pt()>25 and l1.pt()>25 and abs(l0.eta())<2.5 and abs(l1.eta())<2.5):
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
      noGen=True
    
    #----------------------------------------------------------------------------------------------------------------
    #                                      GEN jet collection matched with  B-hadron
    #----------------------------------------------------------------------------------------------------------------
   
    genbjet=[]
    genbjetAll=[]

    if len(b_hadron)>0:
      b1=[]    
      d=9999.
      for gj in GenJet:
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
    #                                       ACCEPTANCE
    #----------------------------------------------------------------------------------------------------------------

    genbj_iso_A=[]
    genbj_iso_B=[]
    
    if GenZ==True and len(genbjet)>0 :
     lp=TLorentzVector(genPos.px(),genPos.py(),genPos.pz(),genPos.energy())
     ln=TLorentzVector(genNeg.px(),genNeg.py(),genNeg.pz(),genNeg.energy())
     invGen=(lp+ln).M() 
     if invGen>76 and invGen<106:
      for bj in genbjet :
        if Delta(bj,genPos)>0.5 and Delta(bj,genNeg)>0.5:
          genbj_iso_A+=[bj]
      if len(genbj_iso_A)>1 :
        gen_llbb+=1
        
    if ZGenOK==True and len(genbjet)>0 :
      for bj in genbjet :
        if Delta(bj,lep0)>0.5 and Delta(bj,lep1)>0.5:
          genbj_iso_B+=[bj]
      if len(genbj_iso_B)==1:    
        Gen1b=True
        NoGen=False
      elif len(genbj_iso_B)>1:          
        Gen2b=True
        NoGen=False
        gen_llbbacc+=1        
      else:
        noGen=True
    else:
      noGen=True

    ##---------------- RECO -------------------------------------------------
    
    ## OLD part---------------------------------------------------------------
    #lept_inAcc=[] ### RECO lepton collection of leptons within the acceptance
    #Sel_lept=[]   ### RECO lepton collection matched with gen leptons in the acceptance            
    ##---------------- RECO leptons in the acceptance
    ##     if muChannel==True :
    ##       for lep in AllMu:
    ##         if lep.pt()>20 and abs(lep.eta())<2.1:
    ##           lept_inAcc+=[lep]
    ##     if muChannel==False:
    ##       for lep in Allelec:
    ##         if lep.pt()>25 and abs(lep.eta())<2.5 and (abs(lep.eta())<1.442 or abs(lep.eta())>1.566):
    ##           lept_inAcc+=[lep]
    ##     if len(lept_inAcc)>1:RecoZAcc=True
    ##     else: NoReco=True

    ##     if RecoZAcc==True and GenZ==True:
    ##       for lf in lept_inAcc:
    ##         if lf.charge()>0 and dp>=0.3:
    ##           for al in anyLepPos: ## ADDED
    ##             dp = Delta(lf,al)
    ##             if dp<0.3:
    ##               Sel_lept+=[lf]
    ##               anyLepPos.remove(al)
    ##         if lf.charge()<0 and dm>=0.3:
    ##           for al in anyLepNeg: ##ADDED
    ##             dm = Delta(lf,genNeg)
    ##             if dm<0.3:
    ##               Sel_lept+=[lf]
    ##               anyLepNeg.remove(al)
    ##       if dp<0.3 and dm<0.3:
    ##         RecoZMatch=True


    ##--------------- RECO leptons matching with GEN leptons
    dp=999.9
    dm=999.9
    noOverlapJet=[]  ## Reco jets with no overlap with the leptons
    jets_match=[] ### Reco jets collection in the acceptance matched with a b-flav jet
    

   
    Zlep=[] ## vector of Z candidates
    LrecVec=[] # first is the POS lepton, second is the NEG lepton

    if muChannel==False and len(zCandidatesEleAll)>0 and GenZ==True:
      for zlep in zCandidatesEleAll:
        if zlep.mass()>76 and zlep.mass()<106 :
          Zlep+=[zlep]

    if muChannel==True and len(zCandidatesMuAll)>0 and GenZ==True:
      for zlep in zCandidatesMuAll:
        if zlep.mass()>76 and zlep.mass()<106 :
          Zlep+=[zlep]

    bestZcandidate = findBestCandidate(muChannel,Zlep)
    
    if bestZcandidate and GenZ==True:
      Lrec0=bestZcandidate.daughter(0)
      Lrec1=bestZcandidate.daughter(1)
      d0=999.9
      d1=999.9

      if muChannel==False:
        if Lrec0.charge()>0 and (Lrec0.pt()>25 and abs(Lrec0.eta())<2.5 and (abs(Lrec0.eta())<1.442 or abs(Lrec0.eta())>1.566)) and (Lrec1.pt()>25 and abs(Lrec1.eta())<2.5 and (abs(Lrec1.eta())<1.442 or abs(Lrec1.eta())>1.566)) :
         #print 'Lrec0.pt', Lrec0.pt()
         #print 'genPos.pt', genPos.pt()
         #print 'Lrec1.pt', Lrec1.pt()
         #print 'genNeg.pt', genNeg.pt()
         d0=Delta(Lrec0,genPos) 
         d1=Delta(Lrec1,genNeg)
         LrecVec+=[Lrec0]
         LrecVec+=[Lrec1]
        if Lrec0.charge()<0 and (Lrec0.pt()>25 and abs(Lrec0.eta())<2.5 and (abs(Lrec0.eta())<1.442 or abs(Lrec0.eta())>1.566)) and (Lrec1.pt()>25 and abs(Lrec1.eta())<2.5 and (abs(Lrec1.eta())<1.442 or abs(Lrec1.eta())>1.566)):
         #print 'Lrec0.pt', Lrec0.pt()
         #print 'genNeg.pt', genNeg.pt()
         #print 'Lrec1.pt', Lrec1.pt()
         #print 'genPos.pt', genPos.pt()
         d0=Delta(Lrec0,genNeg)
         d1=Delta(Lrec1,genPos)
         LrecVec+=[Lrec1]
         LrecVec+=[Lrec0]
        if d0<0.3 and d1<0.3:
          RecoZMatch=True


      if muChannel==True:
        if Lrec0.charge()>0 and ( Lrec0.pt()>20 and abs( Lrec0.eta())<2.1)  and  (Lrec1.pt()>20 and abs( Lrec1.eta())<2.1)  :
         #print 'Lrec0.pt', Lrec0.pt()
         #print 'genPos.pt', genPos.pt()
         #print 'Lrec1.pt', Lrec1.pt()
         #print 'genNeg.pt', genNeg.pt()
         d0=Delta(Lrec0,genPos) 
         d1=Delta(Lrec1,genNeg)
         LrecVec+=[Lrec0]
         LrecVec+=[Lrec1]
        if Lrec0.charge()<0 and ( Lrec0.pt()>20 and abs( Lrec0.eta())<2.1)  and  (Lrec1.pt()>20 and abs( Lrec1.eta())<2.1) :
         #print 'Lrec0.pt', Lrec0.pt()
         #print 'genNeg.pt', genNeg.pt()
         #print 'Lrec1.pt', Lrec1.pt()
         #print 'genPos.pt', genPos.pt()
         d0=Delta(Lrec0,genNeg)
         d1=Delta(Lrec1,genPos)
         LrecVec+=[Lrec1]
         LrecVec+=[Lrec0]
        if d0<0.3 and d1<0.3:
          RecoZMatch=True

    else: NoReco=True
 
   

    ## Reco jets in the acceptance matched with GEN jet
    if RecoZMatch:
      for j in jets:
        if j.pt()>25 and abs(j.eta())<2.1:
          oneJet= False
          for jb in genbjetAll:
            djg=Delta(j,jb)
            if djg<0.5 and oneJet==False:          
              jets_match+=[j]
              genbjetAll.remove(jb)
              oneJet=True

      ## Checking the overlap -----------
      for j in jets_match:
        #print LrecVec[0].pt()
        #print LrecVec[1].pt()
        if Delta(LrecVec[0],j)>0.5 and Delta(LrecVec[1],j)>0.5:
          noOverlapJet+=[j]     
          

      if len(noOverlapJet)==1:
        Reco1b=True
        NoReco=False

      elif  len(noOverlapJet)>1:
        Reco2b=True 
        NoReco=False    

      else: NoReco=True
      
    else: NoReco=True 

    #### computing coefficients:    

    if NoGen and Reco2b:
      numerator+=1
      a_coeff+=1
    if Gen1b and Reco2b:
      numerator+=1
      b_coeff+=1
    if Gen2b and Reco2b:
      numerator+=1
      c_coeff+=1

    
    if  Gen2b and NoReco :
      denominator+=1
      i_coeff+=1
    if  Gen2b and Reco1b :
      denominator+=1
      f_coeff+=1
    if  Gen2b and Reco2b :
      denominator+=1
      
    ### more

    if NoGen and Reco1b :
      d_coeff+=1
    if Gen1b and Reco1b :
      e_coeff+=1
    if NoGen and NoReco :
      g_coeff+=1
    if Gen1b and NoReco :
      h_coeff+=1

    #--------------------------------------------------------------------------------------
    # Epsilon_ll
    #-------------------------------------------------------------------------------------


    ZlepM=[]
    if (muChannel==True and len(zCandidatesMu)>0) or (muChannel==False and len(zCandidatesEle)>0) :
       if(muChannel==True):
         for zlep in zCandidatesMu:
           if zlep.mass()>76 and zlep.mass()<106 :
             ZlepM+=[zlep]
       if(muChannel==False):
         for zlep in zCandidatesEle:
           if zlep.mass()>76 and zlep.mass()<106 :
             ZlepM+=[zlep]

    bestZcandidate = findBestCandidate(muChannel,ZlepM)
    #if len(Zlep)>0 and len(jets_match)>1 and GenZAcc==True :
    #print 'reconstructed lepton size', len(Zlep) 
    if bestZcandidate and GenZ==True:
      Lrec0=bestZcandidate.daughter(0)
      Lrec1=bestZcandidate.daughter(1)
      d0=999.9
      d1=999.9
      if Lrec0.charge()>0:
        d0=Delta(Lrec0,genPos)
        d1=Delta(Lrec1,genNeg)
      if Lrec0.charge()<0:
        d0=Delta(Lrec0,genNeg)
        d1=Delta(Lrec1,genPos)
        
        ## checking that jets have no overlap with leptons form the candidates ##########################       
      jetp=[]
      bjethp=[]
      bjethe=[]
      
      for jet in jets_match:
        if isGoodJet(jet,bestZcandidate) :
          jetp+=[jet]     
          
        if isGoodJet(jet,bestZcandidate) and isBJet(jet, "HE", "SSV"):
          bjethe+=[jet]
          
        if isGoodJet(jet,bestZcandidate) and isBJet(jet, "HP", "SSV"):
          bjethp+=[jet]
             
      if d0<0.3 and d1<0.3 and len(jetp)>1:
        ll_sel_jj+=1

      if met:  
        if d0<0.3 and d1<0.3 and len(bjethe)>1 and isGoodMet(met[0],50):
          ll_match_bbhe+=1

        if d0<0.3 and d1<0.3 and len(bjethp)>1 and isGoodMet(met[0],50):
          ll_match_bbhp+=1
                                 
##### closing file ad dump count

  out_file_INCL.write('GEN Z(ll)bb w lepton acc (NUM): '+ str(gen_llbbacc) +' \n')
  out_file_INCL.write('GEN Z(ll)bb (DEN): '+ str(gen_llbb) +' \n')
  

  out_file_INCL.write('RECO Z(ll)bb (NUM) : '+ str(numerator) +' \n')
  out_file_INCL.write('GEN  Z(ll)bb w lep acc (DEN): '+ str(denominator) +' \n')
  
  out_file_INCL.write(' ---------------checks------------------------------'+' \n')
  out_file_INCL.write('       | '+ 'NoGen' +' | ' +'Gen1b' +' | '+'Gen2b' +' | '+' \n')
  out_file_INCL.write('Reco2b | '+ str(a_coeff) + ' | ' + str(b_coeff) +' | '+ str(c_coeff) +' | '+' \n')
  out_file_INCL.write('Reco1b | '+ str(d_coeff) + ' | ' + str(e_coeff) +' | '+ str(f_coeff) +' | '+' \n')
  out_file_INCL.write('NoReco | '+ str(g_coeff) + ' | ' + str(h_coeff) +' | '+ str(i_coeff) +' | '+' \n')
  out_file_INCL.write(' -----------------------------------------------------'+' \n')
  out_file_INCL.write(' TOTAL '+ str(a_coeff+b_coeff+c_coeff+d_coeff+e_coeff+f_coeff+g_coeff+h_coeff+i_coeff)+' \n')
    
  out_file_INCL.write('RECO Z(ll)jj -ID,ISO,TRG-: '+ str(ll_sel_jj) +' \n')
  out_file_INCL.write('RECO:Z(ll)bb (HE) '+ str(ll_match_bbhe) +' \n')
  out_file_INCL.write('RECO:Z(ll)bb (HP) '+ str(ll_match_bbhp) +' \n')
  
  out_file_INCL.close()


## FOR RUNNING WITH SCRIPT ---------------------------
for num, arg in enumerate(sys.argv):
  print num, arg
 
dumpAll(fileAll=sys.argv[1],numb=sys.argv[2])
