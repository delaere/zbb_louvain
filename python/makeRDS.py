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
### - category, etc...                                                                   ###
###                                                                                      ###
### To do:                                                                               ###
### - check difference reco composite candidates (e.g. zbb vs home-brewn)                ###
### - clean up (proper loops and flags etc...and trigger info)                           ###
###                                                                                      ### 
############################################################################################
############################################################################################

import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle
from eventSelection import *
from ROOT import *

rrv_SV_M    = RooRealVar("rrv_SV_M",   "rrv_SV_M"   ,-1.,   5.)
rrv_bb_M    = RooRealVar("rrv_bb_M",   "rrv_bb_M"   ,-1.,1000.)
rrv_zeebb_M = RooRealVar("rrv_zeebb_M","rrv_zeebb_M",-1.,1000.)
rrv_zmmbb_M = RooRealVar("rrv_zmmbb_M","rrv_zmmbb_M",-1.,1000.)

rc_cat    = RooCategory("rc_cat",  "rc_cat")
rc_cat.defineType("0",0)
rc_cat.defineType("1",1)
rc_cat.defineType("2",2)
rc_cat.defineType("3",3)
rc_cat.defineType("4",4)
rc_cat.defineType("5",5)
rc_cat.defineType("6",6)
rc_cat.defineType("7",7)
rc_cat.defineType("8",8)
rc_cat.defineType("9",9)

rds_zbb   = RooDataSet("rds_zbb",  "rds_zbb",  RooArgSet(rrv_SV_M,
                                                         rrv_bb_M,
                                                         rrv_zeebb_M,
                                                         rrv_zmmbb_M,
                                                         rc_cat))


#def dumpEventList(muChannel=True, stage=9, path="/home/fynu/lceard/store/Prod_AOD_2011A/Json_191pb_GOLD/Mu_2011A_191pb/"):
def dumpEventList(muChannel=True, stage=9, path="/home/fynu/jdf/store/Zbb-TuneZ2_2/"):
    i=0
    dirList=os.listdir(path)
    files=[]
    for fname in dirList:
        files.append(path+fname)
    events = Events (files)

    metlabel="patMETsPF"
    jetlabel="cleanPatJets"
    zmulabel="Ztighttight"
    zellabel="Zelel"
    zmmbblabel="Zmmbb"
    zeebblabel="Zeebb"
    bblabel ="bbbar"
#    triggerlabel="patTriggerEvent"

    jetHandle   = Handle ("vector<pat::Jet>")
    metHandle   = Handle ("vector<pat::MET>")
    zmuHandle   = Handle ("vector<reco::CompositeCandidate>")
    zelHandle   = Handle ("vector<reco::CompositeCandidate>")
    zeebbHandle = Handle ("vector<reco::CompositeCandidate>")
    zmmbbHandle = Handle ("vector<reco::CompositeCandidate>")
    bbHandle    = Handle ("vector<reco::CompositeCandidate>")
#    trigInfoHandle = Handle ("pat::TriggerEvent")
    
    for event in events:

        rrv_SV_M.setVal(-1)
        rrv_bb_M.setVal(-1)
        rrv_zeebb_M.setVal(-1)
        rrv_zmmbb_M.setVal(-1)
        rc_cat.setIndex(0)
        
        if i%10000==0 : print "Processing... event ", i
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

        bestZcandidate = findBestCandidate(zCandidatesMu,zCandidatesEl)
        #category = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEl, jets, met, muChannel)
        category = eventCategory(None, zCandidatesMu, zCandidatesEl, jets, met, muChannel)
        if category > 7: print "cat = ", category

        rc_cat.setIndex(category)

        for jet in jets :
            tISV = jet.tagInfoSecondaryVertex("secondaryVertex")
            if tISV                    : rrv_SV_M.setVal(tISV.secondaryVertex(0).p4().M())
            if len(bbs)>0              : rrv_bb_M.setVal(bbs.at(0).mass())
            if len(zmmbbs)>0           : rrv_zmmbb_M.setVal(zmmbbs.at(0).mass())
            if len(zeebbs)>0           : rrv_zeebb_M.setVal(zeebbs.at(0).mass())
                    
        rds_zbb.add(RooArgSet(rrv_SV_M,
                              rrv_bb_M,
                              rrv_zmmbb_M,
                              rrv_zeebb_M,
                              rc_cat))
                                             
    ws = RooWorkspace("ws","workspace")
    getattr(ws,'import')(rds_zbb)
    ws.Print()

    lepChan = "el"
    if muChannel:
        lepChan = "mu"
    ws.writeToFile("File_rds_zbb_"+lepChan+"MC.root") #TODO: proper!
    gDirectory.Add(ws)
