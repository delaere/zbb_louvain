from ROOT import *
from listForRDS import lumi
import array
import os

gROOT.SetBatch()

SFlist = {}
SFlist["Nom"]={"Zbb"    : "*((jetmetnj==2 )*1.15 + (jetmetnj>2)*1.30)",
          "Zbx"    : "*1.30",
          "Zxx"      : "*1.28",
	  "TT"      : "*1.05"}
SFlist["JESdown"]={"Zbb"    : "*((jetmetnj==2 )*1.20 + (jetmetnj>2)*1.41)",
          "Zbx"    : "*1.41",
          "Zxx"      : "*1.40",
          "TT"      : "*1.07"}
SFlist["JESup"]={"Zbb"    : "*((jetmetnj==2 )*1.10 + (jetmetnj>2)*1.18)",
          "Zbx"    : "*1.18",
          "Zxx"      : "*1.18",
          "TT"      : "*1.04"}
