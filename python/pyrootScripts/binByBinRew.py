from ROOT import *
from zbbSamples import channels, getSample, getDataLuminosity
from zbbSamples import samples_RDS as allSamples
lib_path = os.path.abspath('../')
sys.path.append(lib_path)

channels  = [
    "EEChannel",
    "MuMuChannel",
    ]

var = {
    "El" : "EEChannel/Cut2/eventSelectionbestzptEle",
    "Mu" : "MuMuChannel/Cut2/eventSelectionbestzptMu",
    }


DataZbRatio = {}
zptRew = {}

for c in channels :
    files = {}
    histos = {}

    for l in allSamples :
        files[l]=TFile(getSample(l,c,"RDS").path,"READ")
        histos[l]=files[l].Get(var[c])

    nbins = histos["DATA"].GetNbinsX()
    
    zptRew[c]="("

    for i in range(1,nbins+1):
        x1=histos["DATA"].GetBinLowEdge(i)
        x2=x1+histos["DATA"].GetBinWidth(i)
        DataZbRatio[c]=histos["DATA"].GetBinContent(i)
        for l in allSamples :
            if l=="Zbx" or l=="Zbb" or l=="DATA" : continue
            DataZbRatio[c]=DataZbRatio[c]-histos[l].GetBinContent(i)*(getDataLuminosity(c)/getSample(l,c,"RDS").getLuminosity())
        if (histos["Zbb"].GetBinContent(i)+histos["Zbx"].GetBinContent(i))>0 : 
            DataZbRatio[c]=float(DataZbRatio[c])/(histos["Zbb"].GetBinContent(i)*(getDataLuminosity(c)/getSample("Zbb",c,"RDS").getLuminosity())+
                                                  histos["Zbx"].GetBinContent(i)*(getDataLuminosity(c)/getSample("Zbx",c,"RDS").getLuminosity()))
        else : DataZbRatio[c]=0
        if DataZbRatio[c]<0 : DataZbRatio[c]=1.0
        print DataZbRatio[c]
        zptRew[c]+="(@3>="+str(x1)+")*(@3<"+str(x2)+")*"+str(DataZbRatio[c])
        zptRew[c]+="+"
    zptRew[c]+="(@3>="+str(x2)+"))"
    print c, zptRew[c]
