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
    if mode=="JetEn_withoutJES":
        mat_Down =[[3.17041303,-8.34993026],[-0.05246257, 7.15368494]]
        ##print mat_Down[0][1],", ",mat_Down[1][0],", ",mat_Down[1][0],", ",mat_Down[1][1] 
        mat_Up =[[3.17041303,-8.38016526],[-0.05246257, 7.17958835]]

    elif mode=="MuonEn":
        mat_Down =[[3.17041294,-8.3521289],[-0.05246257,7.15556872]]
        mat_Up =[[3.17041303,-8.35431508],[-0.05246257,7.15744157]]
    
    elif mode=="ElectronEn":
        mat_Down =[[3.17041303,-8.34993026],[-0.05246257,7.15368494]]
        mat_Up =[[3.12072423,-8.45206155],[-0.0615941,7.2637512 ]]

    elif mode=="ElectronEnChannelE":
        mat_Down =[[4.18850418,-11.06452208],[ -0.06308005,9.33711608]]
        mat_Up =[[4.18850456,-11.06543221],[ -0.06308006,9.33788355]]

        
    elif mode=="JetEn":
        mat_Down =[[3.23456058,-8.50565323],[-0.04498772,7.24478139]]
        mat_Up =[[3.11955101,-8.44504028],[-0.06168477,7.25312268]]

    elif mode=="JetRes":
        mat_Down =[[3.14583405,-8.17097585],[-0.0477428,7.05348283]]
        mat_Up =[[ 3.19705532,-8.70205262],[-0.05783531,7.36404113]]

    elif mode=="JetRes_withoutJER":
        mat_Down =[[3.1704131,-8.38183893],[-0.05246257,7.18102213]]
        mat_Up =[[ 3.17041303,-8.33808209],[-0.05246257,7.14353419]]

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

    print "sig Z+1b= ", abs(modified_yields_Down[0]-modified_yields_Up[0])*2/((modified_yields_Down[0]+modified_yields_Up[0])*lumi)*100, "%"
    print "sig Z+2b= ", abs(modified_yields_Down[1]-modified_yields_Up[1])*2/((modified_yields_Down[1]+modified_yields_Up[1])*lumi)*100, "%"

    
