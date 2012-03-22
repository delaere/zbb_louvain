########################################################
########################################################
###                                                  ###
### Script to make generic PDF                       ###    
###                                                  ###
### To be run as                                     ### 
### > python -i genericPdfExample.pdf                ###
###                                                  ### 
########################################################
########################################################

from ROOT import *


###################
### observables ###
###################

m_ll = RooRealVar("m_ll","m(l^{+}l^{-})",0.100,2.5,"TeV/c^{2}")

# exp(N-ax) x^b

a = RooRealVar("a","a",1.3)
b = RooRealVar("b","b",1.0)
N = RooRealVar("N","N",0.1)

genPdf = RooGenericPdf("genPdf","genPdf","exp(N-a*m_ll)*pow(m_ll,b)",RooArgList(N,a,b,m_ll))

data = genPdf.generate(RooArgSet(m_ll),1000)

C=TCanvas("C","C",500,500)

frame=m_ll.frame()
data.plotOn(frame)
genPdf.plotOn(frame)
frame.Draw()