#!/usr/bin/env python 
import os
import sys
import PatAnalysis.CMSSW
from PatAnalysis.AnalysisEvent import AnalysisEvent
from PatAnalysis.EventSelection import prepareAnalysisEvent
from ROOT import TLorentzVector
from MonteCarloSelection import isZbEvent, getGenZparticle
from MonteCarloSelection import delta_R as Delta
from ObjectSelection import isGoodJet, isBJet, isGoodMet

# WARNING: this code has been reingeneered after the move to PatAnalysis.
# It is running, and should give an output close to the previous version, 
# but the focus has not been to be totally equivalent.
# It serves mostly as a example as it is now and it should be checked that 
# the code does actually what you intend it to do.

def Efficiency_acceptance(path="", output="-", muChannel=True, Njobs=1, jobNumber=1):

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

  # events
  events = AnalysisEvent(files)
  prepareAnalysisEvent(events)

  # counters
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
  ll_sel_jj=0
  ll_match_bbhe=0
  ll_match_bbhp=0
  gen_llbb=0
  gen_llbbacc=0

  # Event loop
  event_num=0
  for event in events:

    # event counter
    if event_num%1000==0:
      print 'Event', event_num
    event_num+=1

    # only consider Zb events
    if not isZbEvent(event):
      continue

    # looking for a Z genparticle candidate in the event
    ZgenAll = getGenZparticle(event,muChannel,not muChannel, 0, 100)
    ZgenAcc = getGenZparticle(event,muChannel,not muChannel, 20, 2.4)
    ZGen   = ZgenAll is not None
    ZGenOK = ZgenAcc is not None
    if ZGenOK:
      lep0 = ZgenAcc.daughter(0)
      lep1 = ZgenAcc.daughter(1)
    if ZGen:
      lep0b = ZgenAll.daughter(0)
      lep1b = ZgenAll.daughter(1)

    # GEN jet loop to locate b jets
    genbjet=[]
    genbjetb=[]
    NoGen=False
    Gen1b=False
    Gen2b=False
    for gj in event.sortedGenJets[0]:
      if gj.pt()>25 and abs(gj.eta())<2.1:
        if ZGenOK and Delta(gj,lep0)>0.5 and Delta(gj,lep1)>0.5:
          genbjet+=[gj]
        if ZGen and Delta(gj,lep0b)>0.5 and Delta(gj,lep1b)>0.5:
          genbjetb+=[gj]
    if len(genbjet)>1: 
       gen_llbbacc += 1
       Gen2b=True
       NoGen=False
    elif len(genbjet)==1:
       Gen1b=True
       NoGen=False
    else:
       NoGen=True
    if len(genbjetb)>1: gen_llbb += 1

    # RECO leptons matching with GEN leptons
    RecoZMatch=False
    Reco1b=False
    Reco2b=False
    noOverlapJet=[]  ## Reco jets with no overlap with the leptons
    jets_match=[] ### Reco jets collection in the acceptance matched with a b-flav jet

    if muChannel:
      bestZcandidate = event.bestZmumuCandidate
    else:
      bestZcandidate = event.bestZelelCandidate
    NoReco = bestZcandidate is None
    
    # matching by charge between GEN and RECO leptons
    # note that no pt/eta cut are applied here. They are put in ObjectSelection.
    if bestZcandidate and ZGen:
      Lrec0=bestZcandidate.daughter(0)
      Lrec1=bestZcandidate.daughter(1)
      if Lrec0.charge() == lep0.charge() and Lrec1.charge() == lep1.charge():
        RecoZMatch = Delta(Lrec0,lep0)<0.3 and Delta(Lrec1,lep1)<0.3
      elif Lrec0.charge() == lep1.charge() and Lrec1.charge() == lep0.charge():
        RecoZMatch = Delta(Lrec0,lep1)<0.3 and Delta(Lrec1,lep0)<0.3
 
    # Reco jets in the acceptance matched with GEN jet
    if RecoZMatch:
      for j in event.jets: # not the b jets?
        if j.pt()>25 and abs(j.eta())<2.1:
          oneJet= False
          for jb in genbjet:
            djg=Delta(j,jb)
            if djg<0.5 and oneJet==False:          
              jets_match+=[j]
              genbjet.remove(jb)
              oneJet=True
      for j in jets_match:
        if Delta(Lrec0,j)>0.5 and Delta(Lrec1,j)>0.5:
          noOverlapJet+=[j]     
      if len(noOverlapJet)==1:
        Reco1b=True
        NoReco=False
      elif len(noOverlapJet)>1:
        Reco2b=True 
        NoReco=False    
      else: NoReco=True
    else: NoReco=True 

    # computing coefficients
    if NoGen and Reco2b:
      numerator+=1
      a_coeff+=1
    if Gen1b and Reco2b:
      numerator+=1
      b_coeff+=1
    if Gen2b and Reco2b:
      numerator+=1
      c_coeff+=1
    if Gen2b and NoReco:
      denominator+=1
      i_coeff+=1
    if Gen2b and Reco1b:
      denominator+=1
      f_coeff+=1
    if Gen2b and Reco2b:
      denominator+=1
    if NoGen and Reco1b:
      d_coeff+=1
    if Gen1b and Reco1b:
      e_coeff+=1
    if NoGen and NoReco:
      g_coeff+=1
    if Gen1b and NoReco:
      h_coeff+=1

    # checking that jets have no overlap with leptons form the candidates
    if ZGen and not NoReco :
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
      if RecoZMatch and len(jetp)>1:
        ll_sel_jj+=1
      if RecoZMatch and len(bjethe)>1 and isGoodMet(event.MET[0],50):
        ll_match_bbhe+=1
      if RecoZMatch and len(bjethp)>1 and isGoodMet(event.MET[0],50):
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

# run as a script
if __name__=="__main__":
  import sys
  Efficiency_acceptance(*sys.argv[1:])

