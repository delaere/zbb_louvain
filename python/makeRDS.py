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
rrv_zbb_M   = RooRealVar("rrv_zbb_M",  "rrv_zbb_M",  -1.,1000.)
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
                                                         rrv_zbb_M,
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
        rrv_zbb_M.setVal(-1)
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

        bestZcandidate = findBestCandidate(None,zCandidatesMu,zCandidatesEl)
        #category = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEl, jets, met, muChannel)
        category = eventCategory(None, zCandidatesMu, zCandidatesEl, jets, met, muChannel)
        if category > 7:
            print "cat = ", category
            print "Run", event.eventAuxiliary().run(), ", Lumisection", event.eventAuxiliary().luminosityBlock(), ", Event", event.eventAuxiliary().id().event()

            
        rc_cat.setIndex(category)
        
        nJets = 0
        bjet1 = None
        bjet2 = None
        for jet in jets :
            tISV = jet.tagInfoSecondaryVertex("secondaryVertex")
            if tISV :
                if tISV.secondaryVertex(0) :
                    rrv_SV_M.setVal(tISV.secondaryVertex(0).p4().M())
            if len(bbs)>0              : rrv_bb_M.setVal(bbs.at(0).mass())
            if len(zmmbbs)>0           : rrv_zmmbb_M.setVal(zmmbbs.at(0).mass())
            if len(zeebbs)>0           : rrv_zeebb_M.setVal(zeebbs.at(0).mass())
                    
            if category>= 5:
                btagging = "SSV"
                if isGoodJet(jet,bestZcandidate):
                    if isBJet(jet,"HE",btagging):
                        nJets += 1
                        if nJets==1:   bjet1 = jet
                        elif nJets==2: bjet2 = jet
                        else : break

        if category>=8:
            if bjet1 is None: return # we stop here is no bjet... should not be the case in category 
            if bjet2 is None: return # we stop here is no bjet2... should not be the case in category 5
            b1 = ROOT.TLorentzVector(bjet1.px(),bjet1.py(),bjet1.pz(),bjet1.energy())
            z = ROOT.TLorentzVector(bestZcandidate.px(),bestZcandidate.py(),bestZcandidate.pz(),bestZcandidate.energy())
            Zb = z+b1
            b2 = ROOT.TLorentzVector(bjet2.px(),bjet2.py(),bjet2.pz(),bjet2.energy())
            bb = b1+b2
            Zbb = z+b1+b2
            rrv_bb_M.setVal(bb.M())
            rrv_zbb_M.setVal(Zbb.M())
                                                                                                    
                    
        rds_zbb.add(RooArgSet(rrv_SV_M,
                              rrv_bb_M,
                              rrv_zbb_M,
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
