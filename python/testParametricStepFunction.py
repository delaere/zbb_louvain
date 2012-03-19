from ROOT import *

nbins  = 10
xMin   = -2.
xMax   = +3.
xRange = xMax-xMin

limitsArray = TArrayD(nbins+1)

for i in range(0,nbins+1):
    limit_i = xMin+i*xRange/nbins
    print "limit_i = ", limit_i
    limitsArray.SetAt(limit_i,i)
                                   
list = RooArgList("list")

binHeight = {}
for i in range(0,nbins-1) :
    binHeight[i] = RooRealVar("binHeight_"+str(i),"bin "+str(i)+" value",
                              1./xRange,1./xRange*0.7,1./xRange*1.3)
    print "adding binheight number ", i
    list.add(binHeight[i]) # up to binHeight8, ie. 9 parameters

x = RooRealVar("x","x",xMin,xMax)

bkgPdf = RooParametricStepFunction("bkgPdf","bkgPdf",
                                   x,
                                   list,
                                   limitsArray,
                                   nbins)

cat = RooCategory("cat","cat")
cat.defineType("MC")
cat.defineType("data")


MC=bkgPdf.generate(RooArgSet(x),10000)
cat.setLabel("MC")
MC.addColumn(cat)

mean   = RooRealVar("mean", "mean", 0,-1., 1.)
sigma  = RooRealVar("sigma","sigma",0.5, 0.3,0.7)
sigPdf = RooGaussian("sigPdf","sigPdf",x,mean,sigma)

sigFrac = RooRealVar("sigFrac","sigFrac",0.7,0.4,0.9)

totPdf = RooAddPdf("totPdf","totPdf",RooArgList(sigPdf,bkgPdf),RooArgList(sigFrac)) 

data=totPdf.generate(RooArgSet(x),10000)
cat.setLabel("data")
data.addColumn(cat)

simPdf = RooSimultaneous("sim","sim",cat)
simPdf.addPdf(bkgPdf,"MC")
simPdf.addPdf(totPdf,"data")

dataPlusMC = RooDataSet("dataPlusMC","dataPlusMC",data,RooArgSet(x,cat))

dataPlusMC.append(MC)

r = simPdf.fitTo(dataPlusMC,RooFit.Save())

C=TCanvas("C","C",800,400)
C.Divide(2)

C.cd(1)
f1 = x.frame(xMin,xMax,nbins)
MC.plotOn(f1)
bkgPdf.plotOn(f1)
bkgPdf.plotOn(f1,RooFit.VisualizeError(r,2),RooFit.FillColor(kGray+1))
bkgPdf.plotOn(f1,RooFit.VisualizeError(r,1),RooFit.FillColor(kGray))
bkgPdf.plotOn(f1,RooFit.LineColor(kBlack))
MC.plotOn(f1)
bkgPdf.paramOn(f1,MC)
f1.Draw()

C.cd(2)
f2 = x.frame(xMin,xMax,nbins)
data.plotOn(f2)
totPdf.plotOn(f2)
totPdf.plotOn(f2,RooFit.Components("bkgPdf"),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))
totPdf.plotOn(f2,RooFit.Components("sigPdf"),RooFit.LineColor(kGreen),RooFit.LineStyle(kDashed))
sigPdf.paramOn(f2,data)
f2.Draw()
      
      
