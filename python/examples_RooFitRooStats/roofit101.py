#######################################################
###                                                 ###
### roofit101.py                                    ###  
###                                                 ###
### Basic RooFit example to construct a PDF         ###
###                                                 ###
### To be run as                                    ###
### >python -i roofit101.py                         ###
###                                                 ###
### Questions/comments: tristan.dupree@uclouvain.be ###
###                                                 ###
#######################################################

from ROOT import *

##################
### observable ###
##################

x = RooRealVar("x","x",-10,10)

######################
### gaussian model ###
######################

m = RooRealVar("m","mean",  0)
s = RooRealVar("s","sigma", 1)

g = RooGaussian("g","g",x,m,s)

##############################
### another gaussuan model ###
##############################

m2 = RooRealVar("m2","mean 2",  -1.5)
s2 = RooRealVar("s2","sigma 2",  3  )

g2 = RooGaussian("g2","g2",x,m2,s2)

################
### add them ###
################

f = RooRealVar("f","fraction",0.3)

sum = RooAddPdf("sum","sum",RooArgList(g,g2),RooArgList(f))

############
### draw ###
############

C=TCanvas("C","C",1200,400)
C.Divide(3)

C.cd(1)
f1 = x.frame()
g.plotOn(f1)
f1.Draw()

C.cd(2)
f2 = x.frame()
g2.plotOn(f2,RooFit.LineColor(kRed))
f2.Draw()

C.cd(3)
f3 = x.frame()
sum.plotOn(f3,RooFit.LineColor(kGreen))
sum.plotOn(f3,RooFit.Components("g"), RooFit.LineColor(kBlue),RooFit.LineStyle(kDashed))
sum.plotOn(f3,RooFit.Components("g2"),RooFit.LineColor(kRed),  RooFit.LineStyle(kDotted))
f3.Draw()
