#! /usr/bin/env python

############################################################################################
############################################################################################
###                                                                                      ### 
### makeRDS.py (TdP)                                                                     ### 
###                                                                                      ###  
### Construct a RooDataSet containing observables used in final fit in e.g. Higgs search ###
### - m(Zbb)                                                                             ###
### - m(bb)                                                                              ###
### - m(SV)                                                                              ###
### - catEgory, Etc...                                                                   ###
###                                                                                      ###
### To Do:                                                                               ###
### - check difference reco composite candidates (e.g. zbb vs home-brewn)                ###
### - clean up: MC vs data, trigger info, parse options properly                         ###
###                                                                                      ### 
############################################################################################
############################################################################################

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from eventSelection import *
from ROOT import *

from eventSelection import eventCategories, eventCategory, isInCategory

###################
### Run options ###
###################

channel = "El_DATA" #"Mu_DATA" "El_DATA", "Mu_MC", "El_MC", "Ttbar_Mu_MC", "Ttbar_El_MC"

############
### Maps ###
############

muChannel = { "Mu_DATA"     : True,
              "El_DATA"     : False,
              "Mu_MC"       : True,
              "El_MC"       : False,
              "Ttbar_Mu_MC" : True,
              "Ttbar_El_MC" : False
              }

muSel = { True  : "muSel",
          False : "elSel" }

path = { "Mu_DATA"     : "/home/fynu/lceard/store/Prod_AOD_2011A/Json_Tot1078pb_PromptV4/Mu_2011A_1078pb_v4/" ,
         "El_DATA"     : "/home/fynu/lceard/store/Prod_AOD_2011A/Json_Tot1078pb_PromptV4/Ele_2011A_1078pb_v4/",
         "Ttbar_Mu_MC" : "/home/fynu/lceard/store/MC_Summer11/TTJets/",
         "Ttbar_El_MC" : "/home/fynu/lceard/store/MC_Summer11/TTJets/",
         "Mu_MC"       : "/home/fynu/lceard/store/MC_Summer11/DYJetsToLL/",
         "El_MC"       : "/home/fynu/lceard/store/MC_Summer11/DYJetsToLL/"
         }

#def dumpEventList(muChannel=True, stage=9, path="/home/fynu/jdf/store/Zbb-TuneZ2_2/"):

############################################
### Define RooRealVars and RooCategories ###
############################################

### leptons
rrv_ll_M    = RooRealVar("rrv_ll_M",   "rrv_ll_M"   ,-1.,1000.)
### selection
rc_HE    = RooCategory("rc_HE",   "rc_HE")
rc_HP    = RooCategory("rc_HP",   "rc_HP")
rc_HEMET = RooCategory("rc_HEMET","rc_HEMET")
rc_HPMET = RooCategory("rc_HPMET","rc_HPMET")
rc_HE_excl    = RooCategory("rc_HE_excl",   "rc_HE_excl")
rc_HP_excl    = RooCategory("rc_HP_excl",   "rc_HP_excl")
rc_HEMET_excl = RooCategory("rc_HEMET_excl","rc_HEMET_excl")
rc_HPMET_excl = RooCategory("rc_HPMET_excl","rc_HPMET_excl")

rc_HE.defineType("not_acc",0)
rc_HP.defineType("not_acc",0)
rc_HEMET.defineType("not_acc",0)
rc_HPMET.defineType("not_acc",0)
rc_HE_excl.defineType("not_acc",0)
rc_HP_excl.defineType("not_acc",0)
rc_HEMET_excl.defineType("not_acc",0)
rc_HPMET_excl.defineType("not_acc",0)

rc_HE.defineType("acc",1)
rc_HP.defineType("acc",1)
rc_HEMET.defineType("acc",1)
rc_HPMET.defineType("acc",1)
rc_HE_excl.defineType("acc",1)
rc_HP_excl.defineType("acc",1)
rc_HEMET_excl.defineType("acc",1)
rc_HPMET_excl.defineType("acc",1)

#######################################
### Define RooArgSet and RooDataSet ###
#######################################

obsSet = RooArgSet(rrv_ll_M)
obsSet.add(rc_HE)
obsSet.add(rc_HP)
obsSet.add(rc_HEMET)
obsSet.add(rc_HPMET)
obsSet.add(rc_HE_excl)
obsSet.add(rc_HP_excl)
obsSet.add(rc_HEMET_excl)
obsSet.add(rc_HPMET_excl)


rds_zbb   = RooDataSet("rds_zbb",  "rds_zbb", obsSet)

###########
### JEC ###
###########

AutoLibraryLoader.enable()
ROOT.gSystem.Load("libCondFormatsJetMETObjects.so")
test = JetCorrectionUncertainty("./Jec10V1_Uncertainty_KT4PF.txt")

def unc_tot_jet(jet):
    test.setJetEta(jet.eta())# Give rapidity of jet you want uncertainty on
    test.setJetPt(jet.pt()) #Also give the corrected pt of the jet you want the uncertainty on
    unc = test.getUncertainty(1)
    #print "unc = ", unc
    
    if 0 <abs(jet.eta())< 1.5 : unc_dep_eta=0.02
    if 1.5 <=abs(jet.eta())<3.0  : unc_dep_eta=0.06
    if 3.0 <=abs(jet.eta()) : unc_dep_eta=0.20
    
    unc_tot=sqrt(pow(unc,2)+pow(0.015,2)+pow((0.2*0.8*2.2*1/jet.pt()),2)+pow(unc_dep_eta,2))
    #print unc_tot
    return unc_tot

########################
### Run Forest, run! ###
########################

def makeRDS(_muChan=muChannel[channel], _path=path[channel]) :
    print "*** RUN FOREST, RUN! ***" 
    print "channel   = ", channel
    print "muChannel = ", _muChan
    print "path      = ", _path
    print "muon or electron selection...", muSel[muChannel[channel]]
    i=0
    dirList=os.listdir(_path)
    files=[]
    for fname in dirList:
        files.append(_path+fname)
    print files
    files = files[:1000]
    print files
    events = Events (files)

    metlabel="patMETsPF"
    jetlabel="cleanPatJets"
    zmulabel="Ztighttight"
    zellabel="Zelel"
    zmmbblabel="Zmmbb"
    zeebblabel="Zeebb"
    bblabel ="bbbar"
    #triggerlabel="patTriggerEvent"

    jetHandle   = Handle ("vector<pat::Jet>")
    metHandle   = Handle ("vector<pat::MET>")
    zmuHandle   = Handle ("vector<reco::CompositeCandidate>")
    zelHandle   = Handle ("vector<reco::CompositeCandidate>")
    zeebbHandle = Handle ("vector<reco::CompositeCandidate>")
    zmmbbHandle = Handle ("vector<reco::CompositeCandidate>")
    bbHandle    = Handle ("vector<reco::CompositeCandidate>")
    #trigInfoHandle = Handle ("pat::TriggerEvent")
    
    for event in events:

        rrv_ll_M.setVal(-1)

        rc_HE.setIndex(0)
        rc_HP.setIndex(0)
        rc_HEMET.setIndex(0)
        rc_HPMET.setIndex(0)
        rc_HE_excl.setIndex(0)
        rc_HP_excl.setIndex(0)
        rc_HEMET_excl.setIndex(0)
        rc_HPMET_excl.setIndex(0)
        
        if i%1000==0 : print "Processing... event ", i
        i += 1
        event.getByLabel (    jetlabel,     jetHandle)
        event.getByLabel (    metlabel,     metHandle)
        event.getByLabel (    zmulabel,     zmuHandle)
        event.getByLabel (    zellabel,     zelHandle)
        #event.getByLabel (triggerlabel,trigInfoHandle)
        event.getByLabel (  zeebblabel,   zeebbHandle)
        event.getByLabel (  zmmbblabel,   zmmbbHandle)
        event.getByLabel (     bblabel,      bbHandle)

        jets          = jetHandle.product()
        met           = metHandle.product()
        zCandidatesMu = zmuHandle.product()
        zCandidatesEl = zelHandle.product()
        #triggerInfo   = trigInfoHandle.product()
        zmmbbs        = zmmbbHandle.product()
        zeebbs        = zeebbHandle.product()
        bbs           = bbHandle.product()

        bestZcandidate = findBestCandidate(None,zCandidatesMu,zCandidatesEl)

        myCatData = eventCategory(None, zCandidatesMu, zCandidatesEl, jets, met, muChannel[channel], massWindow=100)    

        if bestZcandidate and isInCategory(5, myCatData):
            #print "Run", event.eventAuxiliary().run(), ", Lumisection", event.eventAuxiliary().luminosityBlock(), ", Event", event.eventAuxiliary().id().event()
            for jet in jets :
                tISV = jet.tagInfoSecondaryVertex("secondaryVertex")
                if tISV :
                    if tISV.secondaryVertex(0) :

                        rrv_ll_M.setVal(bestZcandidate.mass())

                        rc_HE.setIndex(1)
                        if isInCategory(6, myCatData):  rc_HP.setIndex(1)
                        if isInCategory(7, myCatData):  rc_HEMET.setIndex(1)
                        if isInCategory(8, myCatData):  rc_HPMET.setIndex(1)
                        if isInCategory(15, myCatData): rc_HE_excl.setIndex(1)
                        if isInCategory(16, myCatData): rc_HP_excl.setIndex(1)
                        if isInCategory(17, myCatData): rc_HEMET_excl.setIndex(1)
                        if isInCategory(18, myCatData): rc_HPMET_excl.setIndex(1)
                       
                        rds_zbb.add(obsSet)              
                                             
    ws = RooWorkspace("ws","workspace")
    getattr(ws,'import')(rds_zbb)
    ws.Print()

    ws.writeToFile("File_rds_zbb_"+channel+"_"+muSel[muChannel[channel]]+"_forTtbar.root") 
    gDirectory.Add(ws)
