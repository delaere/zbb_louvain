#######################################################
###                                                 ###
### Hgg.py                                          ###  
###                                                 ###
### RooFit/RooStats example of a toy H->gg search   ###
### - construction of exp+gauss pdf                 ###
### - fit                                           ###
### - profile likelihood for search                 ###
###                                                 ###
### To be run as                                    ###
### >python -i Hgg.py                               ###
###                                                 ###
### Questions/comments: tristan.dupree@uclouvain.be ###
###                                                 ###
#######################################################

from ROOT import *

N=1000
  
##################
### observable ###
##################

m_gg = RooRealVar("m_gg","m_gg",100,200,"GeV/c^{2}")

####################
### signal model ###
####################

m_H = RooRealVar("m_H","mean", 125,120,130)
s_H = RooRealVar("s_H","sigma",  2,  1, 3)

sig = RooGaussian("sig","signal",m_gg,m_H,s_H)

########################
### background model ###
########################

Gamma_bkg = RooRealVar("Gamma_bkg","Gamma_bkg",-0.03,-0.1,-0.01)

bkg = RooExponential("bkg","bkg",m_gg,Gamma_bkg)

###################
### total model ###
###################

f = RooRealVar("f","fraction",0.05,0,0.1)

sum = RooAddPdf("sum","sum",RooArgList(sig,bkg),RooArgList(f))

#####################
### total model 2 ###
#####################

B = RooRealVar("B","N(B)",(1-f.getVal())*N,0,1.1*N)
S = RooRealVar("S","N(S)",f.getVal()*N,0,2.*f.getVal()*N)

sum2 = RooAddPdf("sum2","sum2",RooArgList(sig,bkg),RooArgList(S,B))

#######################
### generate toy mc ###
#######################

data = sum.generate(RooArgSet(m_gg),N)

###########
### fit ###
###########

sum.fitTo(data)

############
### draw ###
############

C=TCanvas("C","C",1200,400)
C.Divide(3)

C.cd(1)
f1 = m_gg.frame()
sig.plotOn(f1,RooFit.LineColor(kGreen))
f1.Draw()

C.cd(2)
f2 = m_gg.frame()
bkg.plotOn(f2,RooFit.LineColor(kRed))
f2.Draw()

C.cd(3)
f3 = m_gg.frame(50)
data.plotOn(f3)
sum.plotOn(f3)
sum.plotOn(f3,RooFit.Components("sig"),RooFit.LineColor(kGreen),RooFit.LineStyle(kDashed))
sum.plotOn(f3,RooFit.Components("bkg"),RooFit.LineColor(kRed),  RooFit.LineStyle(kDotted))
sum.plotOn(f3)
data.plotOn(f3)
sum.paramOn(f3,data)
f3.Draw()

##########################
### PROFILE LIKELIHOOD ###
##########################

#Gamma_bkg.setConstant(kTRUE)
#m_H.setConstant(kTRUE)
#s_H.setConstant(kTRUE)

sum2.fitTo(data,RooFit.Extended())

### see also http://root.cern.ch/root/html/tutorials/roostats/StandardProfileLikelihoodDemo.C.html

# can also do 2D
# 1D (number of signal events) should be sufficient

plc_S = RooStats.ProfileLikelihoodCalculator(data,sum2,RooArgSet(S))
plot_S = RooStats.LikelihoodIntervalPlot(plc_S.GetInterval())

plot_S.SetMaximum(10)

print "plotting likelihood of S alone"

C_profLik=TCanvas("C_profLik","C_profLik",400,350)
plot_S.Draw()

###########
### FIN ###
###########
