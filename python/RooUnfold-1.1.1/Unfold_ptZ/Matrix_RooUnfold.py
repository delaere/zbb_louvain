#!/usr/bin/env python
# ==============================================================================
#  File and Version Information:
#       $Id: RooUnfoldExample.py 302 2011-09-30 20:39:20Z T.J.Adye $
#
#  Description:
#       Simple example usage of the RooUnfold package using toy MC.
#
#  Author: Tim Adye <T.J.Adye@rl.ac.uk>
#
# ==============================================================================
import sys
import ROOT
import glob
import os
import itertools
from ROOT import *
from optparse import OptionParser
gROOT.Macro("~/rootlogon.C")
##gROOT.LoadMacro("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/RooUnfold-1.1.1/libRooUnfold.so")

parser = OptionParser()
parser.add_option("-i", "--inputPath", dest="path",
                  help="Read input file from DIR.", metavar="DIR")
parser.add_option("-o", "--output", dest='outputname',
                  help="Save output as FILE.", metavar="FILE")
parser.add_option("--Njobs", type="int", dest='Njobs', default="1",
                  help="Number of jobs when splitting the processing.")
parser.add_option("--jobNumber", type="int", dest='jobNumber', default="0",
                  help="Number of the job is a splitted set of jobs.")
(options,args) = parser.parse_args()

from DataFormats.FWLite import Events, Handle

sys.path.append('/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/')
from eventSelection import *
from monteCarloSelection_NEW import *
from zbbCommons import zbblabel, isZbbSelection, zbbfile
btagAlgo="SSV"
from ROOT import RooUnfoldResponse
from ROOT import RooUnfold


class composite_part():
  def __init__(self, lovec, d1=None, d2=None):
    self.lovec = lovec
    self.d1 = d1
    self.d2 = d2

# ==============================================================================
#  Gaussian smearing, systematic translation, and variable inefficiency
# ==============================================================================
#path="/storage/data/cms/store/user/castello/Unfolding2012/DYJets_unfolding_noRecoBias/"
#input_file=glob.glob(path+"*")
dirList=list(itertools.islice(os.listdir(options.path),options.jobNumber, None,options.Njobs))
files=[]
for fname in dirList:
  files.append(options.path+"/"+fname)
events = Events (files)
    
genHandle = Handle ("vector<reco::GenParticle>")
genjetHandle = Handle ("vector<reco::GenJet>")
jetHandle = Handle ("vector<pat::Jet>")
metHandle = Handle ("vector<pat::MET>")
zmuHandle = Handle ("vector<reco::CompositeCandidate>")
zeleHandle = Handle ("vector<reco::CompositeCandidate>")
genInfoHandle = Handle("GenEventInfoProduct")
trigInfoHandle = Handle ("pat::TriggerEvent")
vertexHandle = Handle ("vector<reco::Vertex>")
rhoHandle = Handle("double")

hTrue= TH1D ("true", "Test Truth", 25 , 0., 500.)
hMeas= TH1D ("meas", "Test Measured", 25 , 0., 500.)

# ==============================================================================
#  Example Unfolding
# ==============================================================================
print "=========== getting data to unfold for setting the binning ============="
f_data = TFile("/home/fynu/lceard/scratch/4_4_4_V2/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/combined_Plots_JES_final_V_SaveHisto_Combined.root")
hdata = f_data.Get("h_data")
print "data distribution :", hdata.GetTitle()
print "number of bin in data histo : ", hdata.GetNbinsX() 
print "minumum in data histo : ", hdata.GetXaxis().GetXmin()
print "maximum in data histo : ", hdata.GetXaxis().GetXmax()

##launching on condor with -o option
output_file = TFile(options.outputname,'RECREATE')
output_file.cd()

print "==================================== TRAIN ===================================="
response= RooUnfoldResponse (hdata.GetNbinsX(),hdata.GetXaxis().GetXmin(),hdata.GetXaxis().GetXmax());

#  Train with a MC_gen
k=j=l=f=x=0
weight=1
for event in events :
  if k%10000==0 : print "event number ", k
  #if k==20000 :  break
  ##if k==100 :  break
  k=k+1
  
  genElectrons=[]
  genMuons=[]
  genjets=[]
  genZCandidates=[]

  DeltaM=10000000000000
  isGoodJet = False
  areGoodJets = False
  isbestgenZcandidate = False
  stophere=False
  
  event.getByLabel("prunedGen",genHandle)
  event.getByLabel("prunedJets",genjetHandle)
  event.getByLabel(zbblabel.jetlabel,jetHandle)
  event.getByLabel(zbblabel.metlabel,metHandle)
  event.getByLabel(zbblabel.zmumulabel,zmuHandle)
  event.getByLabel(zbblabel.zelelabel,zeleHandle)
  event.getByLabel(zbblabel.vertexlabel,vertexHandle)
  event.getByLabel(zbblabel.triggerlabel,trigInfoHandle)
  event.getByLabel("kt6PFJetsForIsolation","rho",rhoHandle)

  genParticles = genHandle.product()
  genJets = genjetHandle.product()
  jets = jetHandle.product()
  met = metHandle.product()
  zCandidatesMu = zmuHandle.product()
  zCandidatesEle = zeleHandle.product()
  triggerInfo = trigInfoHandle.product()
  vertices = vertexHandle.product()
  rho = rhoHandle.product()
  triggerInfo = None ##for MC

  #if not(isZbbEvent(genParticles,genJets,25,2.1)) : continue

  for genPart in genParticles :
    if (abs(genPart.pdgId())==11 and genPart.status()==1 and genPart.pt()>20 and abs(genPart.eta())<2.4) :
      genElectrons.append(genPart)
    if (abs(genPart.pdgId())==13 and genPart.status()==1 and genPart.pt()>20 and abs(genPart.eta())<2.4):
      genMuons.append(genPart)

  for genEle in genElectrons:
    genEle1 = ROOT.TLorentzVector(genEle.px(),genEle.py(),genEle.pz(),genEle.energy())
    genEle1_charge=genEle.charge()
    for genEle in genElectrons:
      if (genEle.charge()*genEle1_charge==-1) :
        genEle2= ROOT.TLorentzVector(genEle.px(),genEle.py(),genEle.pz(),genEle.energy())
        genZcandidate=genEle1+genEle2
        if(genZcandidate.M()>=76 and genZcandidate.M()<=106):
          comp_genZcand=composite_part(genZcandidate,genEle1,genEle2)
          genZCandidates.append(comp_genZcand)
          MuChannel = False
        else :continue
      else: continue
      
  for genMu in genMuons:
    genMu1 = ROOT.TLorentzVector(genMu.px(),genMu.py(),genMu.pz(),genMu.energy())
    genMu1_charge=genMu.charge()
    for genMu in genMuons:
      if (genMu.charge()*genMu1_charge==-1) :
        genMu2= ROOT.TLorentzVector(genMu.px(),genMu.py(),genMu.pz(),genMu.energy())
        genZcandidate=genMu1+genMu2
        if(genZcandidate.M()>=76 and genZcandidate.M()<=106):
          comp_genZcand = composite_part(genZcandidate,genMu1,genMu2)
          genZCandidates.append(comp_genZcand)
          MuChannel = True
        else : continue
      else: continue
      
  if len(genZCandidates) == 0 :
    #print "no Z candidate"
    continue
  
  for genZcandidate_comp in genZCandidates:
    if genZcandidate_comp.lovec is None :
      print "genZcandidate_comp.lovec is None",genZcandidate_comp.lovec
      break
    else :
      delta_m=abs(genZcandidate_comp.lovec.M()-91.1876)
      #print"delta m",delta_m 
      if delta_m < DeltaM :
        bestgenZcandidate_comp=genZcandidate_comp
        bestgenZcandidate=genZcandidate_comp.lovec
        DeltaM=delta_m
        if not (bestgenZcandidate is None) : isbestgenZcandidate = True
    
  for genJet in genJets:
    if stophere==True : break
    if (genJet.pt()>25 and abs(genJet.eta())<2.1):
      genJet_prv = genJet
      jv =  ROOT.TLorentzVector(genJet.px(),genJet.py(),genJet.pz(),genJet.energy())
      dr1 = jv.DeltaR(bestgenZcandidate_comp.d1)
      dr2 = jv.DeltaR(bestgenZcandidate_comp.d2)
      if (dr1 > 0.5 and dr2 > 0.5) :
        isGoodJet = True
        for genJet in genJets:
          if genJet == genJet_prv : continue
          if (genJet.pt()>25 and abs(genJet.eta())<2.1):
            jv =  ROOT.TLorentzVector(genJet.px(),genJet.py(),genJet.pz(),genJet.energy())
            dr1 = jv.DeltaR(bestgenZcandidate_comp.d1)
            dr2 = jv.DeltaR(bestgenZcandidate_comp.d2)
            if (dr1 > 0.5 and dr2 > 0.5) :
              areGoodJets = True
              #print "genJet.pt()",genJet.pt()
              #print "genJet_prv.pt()",genJet_prv.pt()
              #print "next"
              stophere= True
              break
            else : continue
          else: continue
      else : continue
    else : continue

  if not(isbestgenZcandidate and areGoodJets and isZbbEvent(genParticles,genJets,25,2.1)) : continue
  else :
    x=x+1
    #print "Truth"
    hTrue.Fill(bestgenZcandidate.Pt(),weight)
        
##lumi_section = event.eventAuxiliary().luminosityBlock() ##lumi_section = 0 for MC
  runNumber= event.eventAuxiliary().run()  
  if vertices.size()>0 :
    vertex = vertices[0]
  else:
    vertex = None
  bestZcandidate = findBestCandidate(None,vertex,zCandidatesMu,zCandidatesEle)
  cat = eventCategory(triggerInfo, zCandidatesMu, zCandidatesEle, vertices, jets, met, runNumber, MuChannel, btagging="SSV", lumi_section=0)
  #print "MuChannel", MuChannel

  if(isbestgenZcandidate and areGoodJets and isZbbEvent(genParticles,genJets,25,2.1)):
    if (isInCategory(16,cat)):
    ##isInCategory(16) for Zbb+METSign
      j=j+1
      #print "Measured"
      response.Fill(bestZcandidate.pt(),bestgenZcandidate.Pt(),weight) 
      hMeas.Fill(bestZcandidate.pt(),weight)
    else:
      l=l+1
      #print "Miss"
      response.Miss(bestgenZcandidate.Pt(),weight)

  if (isInCategory(16,cat)) :
    if not ((isbestgenZcandidate) and isGoodJet and isZbbEvent(genParticles,genJets,25,2.1)):
      f=f+1
      #print "Fake"
      response.Fake(bestZcandidate.pt(),weight)


output_file.WriteTObject(hMeas)
output_file.WriteTObject(hTrue)
output_file.WriteTObject(response, "response_pT_Z")

## #raw_input("Press ENTER to continue")
print "tot number of events = ",k
print "number that survived gen cuts",x
print "number of events in matrix = ",j    
print "number of events in fakes = ",f    
print "number of events in missed = ",l  
print ""
