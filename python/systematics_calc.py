import ROOT
import sys
import os
import commands
import itertools
import time
import glob
import math
import datetime

def syst(flavor,mode):

    if mode=="MuonEn":
        mat_Down =[[3.17041294,-8.3521289],[-0.05246257,7.15556872]]
        mat_Up =[[3.17041303,-8.35431508],[-0.05246257,7.15744157]]
    
    elif mode=="ElectronEn":
        mat_Down =[[3.17041303,-8.34993026],[-0.05246257,7.15368494]]
        mat_Up =[[3.12072423,-8.45206155],[-0.0615941,7.2637512 ]]

    elif mode=="ElectronEnChannelE":
        mat_Down =[[4.18850418,-11.06452208],[ -0.06308005,9.33711608]]
        mat_Up =[[4.18850456,-11.06543221],[ -0.06308006,9.33788355]]

    elif mode=="JES_onjets": ##JES on jets only
        mat_Down =[[3.35777268,-8.79206442],[-0.04706438,7.50540379]]
        ##mat_Down =[[3.358,-8.792],[-0.047,7.505]]
        mat_Up =[[3.25116496,-8.69646903],[-0.06481426,7.47060989]]
        ##mat_Up =[[3.251,-8.696],[-0.065,7.471]]

    elif mode=="JetEn_withoutJES": ##JES on MET only
        mat_Down =[[3.17041303,-8.34993026],[-0.05246257, 7.15368494]]
        ##print mat_Down[0][1],", ",mat_Down[1][0],", ",mat_Down[1][0],", ",mat_Down[1][1] 
        mat_Up =[[3.17041303,-8.38016526],[-0.05246257, 7.17958835]]
       
    elif mode=="JetEn":  ## JES on jets and MET
        mat_Down =[[3.35944331,-8.83778801],[-0.04672464,7.5342471]]
        mat_Up =[[3.25221282,-8.80920526],[-0.0641893,7.57279609]]

    elif mode=="JER": ##JER on jets only
        mat_Down =[[3.26607861,-8.44377494],[-0.0495677,7.29783867]]
        mat_Up =[[3.32386479,-9.0501284],[-0.06012931,7.66303096]]

    elif mode=="JetRes_withoutJER":##JER on MET only 
        mat_Down =[[3.1704131,-8.38183893],[-0.05246257,7.18102213]]
        mat_Up =[[ 3.17041303,-8.33808209],[-0.05246257,7.14353419]]

    elif mode=="JetRes": ##JER on jets and MET
        mat_Down =[[3.14583405,-8.17097585],[-0.0477428,7.05348283]]
        mat_Up =[[ 3.19705532,-8.70205262],[-0.05783531,7.36404113]]


    else :
        print " Mode not found"


    if flavor == "m" :
        lumi = lumi_totMu2011=5.275
        yields = [6701,296]
        print " Muon Channel"
    elif flavor == "e" :
        lumi = lumi_totEle2011=5.217 #in fb-1
        yields = [5262,194]
        print " Electron Channel"

    print "lumi = ", lumi 

    print "original yields :"
    print "[ " , yields[0], " ]"
    print "[ " , yields[1], " ]"
    
    modified_yields_Down = [((mat_Down[0][0]*yields[0]+mat_Down[0][1]*yields[1])/lumi),((mat_Down[1][0]*yields[0]+mat_Down[1][1]*yields[1])/lumi)]

    modified_yields_Up = [((mat_Up[0][0]*yields[0]+mat_Up[0][1]*yields[1])/lumi),((mat_Up[1][0]*yields[0]+mat_Up[1][1]*yields[1])/lumi)]
    
    print "Yields with Variation Down :"
    print "[ ", modified_yields_Down[0], " ]"
    print "[ ", modified_yields_Down[1], " ]"

    print "Yields with Variation Up :"
    print "[ ", modified_yields_Up[0], " ]"
    print "[ ", modified_yields_Up[1], " ]"

    print "sig Z+1b= ", abs(modified_yields_Down[0]-modified_yields_Up[0])*2/((modified_yields_Down[0]+modified_yields_Up[0]))*100, "%"
    print "sig Z+2b= ", abs(modified_yields_Down[1]-modified_yields_Up[1])*2/((modified_yields_Down[1]+modified_yields_Up[1]))*100, "%"

    
