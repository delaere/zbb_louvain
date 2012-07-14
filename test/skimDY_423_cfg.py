########################################
###
### Script to skim a (DY MC) sample
###
### Todo:
###
###  1)   do naming to PAT2 in a proper way
###       ( a lot of the code below is just a copy-past of
###         PhysicsTools.PatAlgos.patTemplate_cfg to avoid
###         renaming the process to "PAT2" in a proper way )
###        When that is done a lot of code can be removed
###  2)   Change print frequency (1/100 or 1/1000)
###       Currently takes most time I think
###
###  Doei! T
###
###################################################

## import skeleton process
#from PhysicsTools.PatAlgos.patTemplate_cfg import *

import FWCore.ParameterSet.Config as cms

###

import FWCore.ParameterSet.VarParsing as VarParsing

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

options.register ('sample',
                  "TT_MC", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "Sample to process")

options.register ('slice',
                  0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Slice of sample")

# setup any defaults you want
#options.sample = 'XXX'
#options.slice  = '666'

# get and parse the command line arguments
options.parseArguments()

### define process

process = cms.Process("PAT2")

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

## Options and Output Report
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

## Source
from PhysicsTools.PatAlgos.tools.cmsswVersionTools import pickRelValInputFiles
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:/storage/data/cms/users/llbb/production2012_44X/Fall11_ZZ/PATskim-Zjets_9_2_JjJ.root')
                            )


## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.AlCa.autoCond import autoCond
#process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )
process.load("Configuration.StandardSequences.MagneticField_cff")

## Test JEC from test instances of the global DB
#process.load("PhysicsTools.PatAlgos.patTestJEC_cfi")

## Test JEC from local sqlite file
#process.load("PhysicsTools.PatAlgos.patTestJEC_local_cfi")

## Standard PAT Configuration File
process.load("PhysicsTools.PatAlgos.patSequences_cff")

## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.out = cms.OutputModule("PoolOutputModule",
                                                              fileName = cms.untracked.string('patTuple.root'),
                                                              # save only events passing the full path
                                                              SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                                                              # save PAT Layer 1 output; you need a '*' to
                                                              # unpack the list of commands 'patEventContent'
                                                              outputCommands = cms.untracked.vstring('drop *', *patEventContent )
                                                              )

process.outpath = cms.EndPath(process.out)


process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.4 $'),
    annotation = cms.untracked.string('PAT tuple for Z+b analysis'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/UserCode/zbb_louvain/test/skimDY_423_cfg.py,v $')
    #name = cms.untracked.string('PAT2')
)

#process.name = cms.string("PAT2")

#from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning
#from PhysicsTools.PatAlgos.patEventContent_cff import patExtraAodEventContent
#from PhysicsTools.PatAlgos.patEventContent_cff import patTriggerEventContent


# for the latest reprocessed samples. You can find it here : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions
process.GlobalTag.globaltag = cms.string('START44_V13::All')

## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")


# running on data, remove genparticle references in objects
#from PhysicsTools.PatAlgos.tools.coreTools import *
#from PhysicsTools.PatAlgos.tools.jetTools import *

#---------------------------- JET
#------------------------------------------------------------------------------------------------------------------------------------------------
#
#from PhysicsTools.PatAlgos.tools.jetTools import *

#------------------------------ b-jets 
#------------------------------------------------------------------------------------------------------------------------------------------------		
# b-jet filter

# additional collections and candidates
#process.bjets = process.cleanPatJets.clone( preselection = 'bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 1.74' )
#process.bjets.src = "bjets"
##process.bjets = process.cleanPatJets.clone( preselection = 'bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 1.74' )

#------------------------------ Filter

process.CSVMbjets = cms.EDFilter("PATJetSelector",
                            src = cms.InputTag("CSVbjets"),
                            cut = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")>0.679'),
                            filter = cms.bool(True)
                            )

process.bFilter = cms.EDFilter("CandViewCountFilter",
                               src = cms.InputTag("bjets"),
                               minNumber = cms.uint32(1),
                               )

process.CSVbFilter = cms.EDFilter("CandViewCountFilter",
                                  src = cms.InputTag("CSVbjets"),
                                  minNumber = cms.uint32(1),
                                  )

process.zMuMuFilter = cms.EDFilter("CandViewCountFilter",
                               src = cms.InputTag("zmuMatchedmuMatched"),
                               minNumber = cms.uint32(1),
                               )

process.zElElFilter = cms.EDFilter("CandViewCountFilter",
                               src = cms.InputTag("zelMatchedelMatched"),
                               minNumber = cms.uint32(1),
                               )


#------------------------------ Sequence
#------------------------------------------------------------------------------------------------------------------------------------------------		
# vertex filter
# triggers based on loose leptons for skimming #in the talk

# run additional collections and candidates
#process.patDefaultSequence *= process.bjets

# Run it

process.p4 = cms.Path(process.zMuMuFilter*process.bFilter)
process.p5 = cms.Path(process.zMuMuFilter*process.CSVMbjets)
#process.p5 = cms.Path(process.CSVbFilter)
process.p6 = cms.Path(process.zElElFilter*process.bFilter)
process.p7 = cms.Path(process.zElElFilter*process.CSVMbjets)

process.out.SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p4','p5','p6','p7'))

process.out.outputCommands = cms.untracked.vstring('keep *')

### options ###
sample = options.sample
slice  = options.slice
print "*** GOING TO LOOK AT ", sample 
print "*** dataset slice #  ", slice 
###############

path = {"DY_MC"    : "/storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_DYjets_v4/" ,
        "TT_MC"    : "/storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_TTbar_v3/" ,
        "Mu_DataA" : "/storage/data/cms/users/llbb/Production_5fb/Data/Mu2011A/50e19e0266f4f061bdccd79330eb70f3/" ,
        "El_DataA" : "/storage/data/cms/users/llbb/Production_5fb/Data/Ele2011A/50e19e0266f4f061bdccd79330eb70f3/" ,
        "Mu_DataB" : "/storage/data/cms/users/llbb/Production_5fb/Data/Mu2011B/50e19e0266f4f061bdccd79330eb70f3/" ,
        "El_DataB" : "/storage/data/cms/users/llbb/Production_5fb/Data/Ele2011B/50e19e0266f4f061bdccd79330eb70f3/" ,
        "ZZ_MC"    : "/storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_ZZ_v2/" ,
        "ZH115_MC" : "/storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_ZHbb_115/" ,
        "ZH120_MC" : "/storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_ZHbb_120/" ,
        "ZH125_MC" : "/storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_ZHbb_125/" ,
        "ZH130_MC" : "/storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_ZHbb_130/" ,
        "ZH135_MC" : "/storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_ZHbb_135/" ,
        "Zbb_MC"   : "/storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/zbbProd/" ,
        "tW_MC"    : "/storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_T_tW_v3/" ,
        "tbarW_MC" : "/storage/data/cms/users/llbb/productionJune2012_444/MCwithMatching/Fall11_Tbar_tW_v3/" 
        }

pathname = "file:"+path[sample]

import os

dirList=os.listdir(path[sample])
files=[]
for fname in dirList:
    files.append(pathname+fname)

print files
njobs=10
if slice: files = files[len(files)*(slice-1)/njobs:len(files)*slice/njobs]

print files

process.source.fileNames = files           

process.maxEvents.input = -1

if slice : process.out.fileName = '/storage/data/cms/store/user/acaudron/skim444/'+sample+'/'+sample+'_'+str(slice)+'.root'
else     : process.out.fileName = '/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/test/'+sample+'.root'

#process.options.wantSummary = False
