from datetime import datetime
from math import sin
import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from eventSelection import jetId, findBestCandidate, isGoodJet, isBJet, isGoodElectron, isGoodMuon, eventCategory, isInCategory
from zbbCommons import zbblabel
from monteCarloSelection import isZbEvent, isZcEvent


files_run = open("files_Ele_Stage12_ZHEHEMET_eventslist_Aug05.txt","w")
#files_run = open("files_Ele_Stage12_ZHEHEMET_eventslist_May10.txt","w")
#files_run = open("files_Ele_Stage12_ZHEHEMET_eventslist_PV4.txt","w")
#files_run = open("files_Ele_Stage12_ZHEHEMET_eventslist_PV6.txt","w")

def main(cat=12 , path="/home/fynu/lceard/store/Prod_data_2011A_V2/Aug05ReReco/Ele_Aug05ReReco/"):
#def main(cat=12 , path="/home/fynu/lceard/store/Prod_data_2011A_V2/May10ReReco/Ele_May10/"):
#def main(cat=12 , path="/home/fynu/lceard/store/Prod_data_2011A_V2/PromptRecoV4/Ele_PromptRecoV4/"):
#def main(cat=12 , path="/home/fynu/lceard/store/Prod_data_2011A_V2/PromptRecoV6/Ele_PromptRecoV6/"):


  """Dump event number list of a given run"""
  dirList=os.listdir(path)
  files=[]
  for fname in dirList:
    files.append(path+fname)
     
  fwevents = Events (files)
  jetHandle = Handle ("vector<pat::Jet>")
  metHandle = Handle ("vector<pat::MET>")
  zmuHandle = Handle ("vector<reco::CompositeCandidate>")
  zeleHandle = Handle ("vector<reco::CompositeCandidate>")
  trigInfoHandle = Handle ("pat::TriggerEvent")
  #genHandle = Handle ("vector<reco::GenParticle>")
  
  for fwevent in fwevents:
    #if fwevent.eventAuxiliary().run()==run :
      #print  fwevent.eventAuxiliary().run(), fwevent.eventAuxiliary().id().event()    
      # in case a fwevent is provided, use it
      #PrintEvent(fwevent)
      # load objects
      #vertexHandle = Handle ("vector<reco::Vertex>")
      #electronHandle = Handle ("vector<pat::Electron>")
      #muonHandle = Handle ("vector<pat::Muon>")
      #fwevent.getByLabel (zbblabel.electronlabel,electronHandle)
      #fwevent.getByLabel (zbblabel.muonlabel,muonHandle)
           
      fwevent.getByLabel (zbblabel.jetlabel,jetHandle)
      fwevent.getByLabel (zbblabel.metlabel,metHandle)
      fwevent.getByLabel (zbblabel.zmumulabel,zmuHandle)
      fwevent.getByLabel (zbblabel.zelelabel,zeleHandle)
      #fwevent.getByLabel (zbblabel.vertexlabel,vertexHandle)
      fwevent.getByLabel (zbblabel.triggerlabel,trigInfoHandle)
      triggerInfo = trigInfoHandle.product()
      #triggerInfo = None
      #vertices = vertexHandle.product()
      #electrons = electronHandle.product()
      #muons = muonHandle.product()
      jets = jetHandle.product()
      met = metHandle.product()
      zCandidatesMu = zmuHandle.product()
      zCandidatesEle = zeleHandle.product()
      #rawjet = jet.correctedJet("Uncorrected")
      run = fwevent.eventAuxiliary().run()
      # category
      #catMu = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, run, muChannel=True, btagging="SSV", massWindow=15.)
      catEle = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, jets, met, run, muChannel=False, btagging="SSV", massWindow=15.)
      #print "Event category info in muon channel:",catMu
      #print "Event category info in electron channel:",catEle
      
      #print isInCategory(cat,catMu)
      if isInCategory(cat,catEle):
        print "run", fwevent.eventAuxiliary().run(), "lumi section", fwevent.eventAuxiliary().luminosityBlock(), "event" , fwevent.eventAuxiliary().id().event()
        print >> files_run , fwevent.eventAuxiliary().id().event()
  
   
if __name__ == "__main__":
  main()


