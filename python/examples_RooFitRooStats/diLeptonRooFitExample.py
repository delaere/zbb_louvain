########################################################
########################################################
###                                                  ###
### Script to fit for number of Z'(l+l-) candidates  ###
### using di-lepton invariant mass m(ll) spectrum    ###
###                                                  ###
### To be run as                                     ###                                     
### > python -i diLeptonRooFitExample.py             ###
###                                                  ### 
### Ex.1: fit for fraction of signal events          ### 
### Ex.2: fit for number of sig&bkg events           ###  
###                                                  ### 
### Possible extensions                              ###  
### - change signal model (voigt, template)          ###
### - change background model (template: histo/keys) ###
### - estimate CLs (RooStats)                        ###
###                                                  ###
### Questions/comments: tristan.dupree@uclouvain.be  ###
###                                                  ###
########################################################
########################################################

from ROOT import *

##################
### parameters ###
##################

# bkg: "rhp" or "rkp" or "gen"
bkgfitmodel = "rhp"
# sig: "rhp" or "rkp" or "gen"
sigfitmodel = "gen"

###################
### observables ###
###################

m_ll = RooRealVar("m_ll","m(l^{+}l^{-})",0.100,2.5,"TeV/c^{2}")

################################
### signal model to generate ###
### (Gaussian)               ###
################################

sigma = RooRealVar("sigma","sigma",0.025,0.015,0.035)
mean  = RooRealVar("mean", "mean", 2.1)

sig_gen = RooGaussian("sig_gen","sig_gen",m_ll, mean, sigma)

########################
### background model ###
### (exp(c*m_ll))    ###
########################

coeff = RooRealVar("coeff","coeff",-1.)

bkg_gen = RooExponential("bkg_gen","bkg_gen",m_ll,coeff)

#########################
### generate toy "MC" ###
#########################

data_bkg = bkg_gen.generate(RooArgSet(m_ll), 1000)
data_sig = sig_gen.generate(RooArgSet(m_ll),  100)
data=data_sig
data.append(data_bkg)

mc_bkg = bkg_gen.generate(RooArgSet(m_ll),  3000)
mc_sig = sig_gen.generate(RooArgSet(m_ll),   300)
mc_sig.SetName("mc_sig")
mc_bkg.SetName("mc_bkg")

ws = RooWorkspace("ws","workspace")
getattr(ws,'import')(mc_sig)
getattr(ws,'import')(mc_bkg)
ws.Print()
#ws.writeToFile("File_rds_zbb_"+channel+"_"+muSel[muChannel[channel]]+"_forBTag.root")
#gDirectory.Add(ws)
                
####################
### model to fit ###
####################

print "getting MC distributions for signal and background"
mc_sig = ws.data("mc_sig")
mc_bkg = ws.data("mc_bkg")

# sig

print "making RooKeysPdf to model signal"
sig_rkp = RooKeysPdf( "bkg_rhp","bkg_rhp",          m_ll , mc_sig )

#sig_fit = sig_rkp
sig_fit = sig_gen
sig_fit.SetName("sig_fit")

# bkg

print "making RooHistPdf to model background"
bkg_rdh = RooDataHist("bkg_rdh","bkg_rdh",RooArgSet(m_ll), mc_bkg )
bkg_rhp = RooHistPdf( "bkg_rhp","bkg_rhp",RooArgSet(m_ll), bkg_rdh )

print "making RooKeysPdf to model background"
bkg_rkp = RooKeysPdf( "bkg_rhp","bkg_rhp",          m_ll , mc_bkg )

### bkg fit options
#bkg_fit = bkg_gen
bkg_fit = bkg_rhp
#bkg_fit = bkg_rkp
bkg_fit.SetName("bkg_fit")

bkg_fit = {"rhp" : bkg_rhp,
           "gen" : bkg_gen,
           "rkp" : bkg_rkp
           }
sig_fit = {"gen" : sig_gen,
           "rkp" : sig_rkp
           }

# sum (number of events)

n_bkg = RooRealVar("n_bkg","n_bkg", 0.9*data.numEntries(),0.50*data.numEntries(),1.10*data.numEntries())
n_sig = RooRealVar("n_sig","n_sig", 0.1*data.numEntries(),0.01*data.numEntries(),0.50*data.numEntries())

sum_n = RooAddPdf("sum_n","sum_n",
                  RooArgList(sig_fit[sigfitmodel],bkg_fit[bkgfitmodel]),
                  RooArgList(n_sig,n_bkg))

# sum (fractions)

f_sig = RooRealVar("f_sig","f_sig",0.1,0.,1.)

sum_f = RooAddPdf("sum_f","sum_f",
                  RooArgList(sig_fit[sigfitmodel],bkg_fit[bkgfitmodel]),
                  RooArgList(f_sig))

###################
### perform fit ###
###################

# fit for fraction:

sum_f.fitTo(data)

# fit for number of events:

sum_n.fitTo(data,RooFit.Extended())

############
### plot ###
############

gROOT.SetStyle("Plain")

C = TCanvas("C","C",800,400)
C.Divide(2)

C.cd(1)
f1 = m_ll.frame()
data.plotOn(f1)
sum_n.plotOn(f1)
sum_n.paramOn(f1)
f1.Draw()

C.cd(2).SetLogy()
f2 = m_ll.frame()
data.plotOn(f2)
sum_f.plotOn(f2)
sum_f.plotOn(f2,RooFit.Components("bkg_fit"),RooFit.LineStyle(kDashed),RooFit.LineColor(kRed))
sum_f.plotOn(f2,RooFit.Components("sig_fit"),RooFit.LineStyle(kDashed),RooFit.LineColor(kGreen))
f2.Draw()

###########
### msg ###
###########

print "***********************************************"
print "That was the generation of toy MC + fit + plot"
print "***********************************************"

###############
### The End ###
###############
