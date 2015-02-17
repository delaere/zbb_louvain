from ROOT import *
from listForRDS import lumi
import array
import os

gROOT.SetBatch()

SFlist = {}
SFlist["Nominal"]={"Zbb"    : "*((jetmetnj==2 )*1.18 + (jetmetnj>2)*1.29)",
          "Zbx"    : "*1.29",
          "Zxx"      : "*1.29",
	  "TT"      : "*1.05"}
SFlist["JESdown"]={"Zbb"    : "*((jetmetnj==2 )*1.23 + (jetmetnj>2)*1.40)",
          "Zbx"    : "*1.40",
          "Zxx"      : "*1.41",
          "TT"      : "*1.07"}
SFlist["JESup"]={"Zbb"    : "*((jetmetnj==2 )*1.13 + (jetmetnj>2)*1.17)",
          "Zbx"    : "*1.17",
          "Zxx"      : "*1.19",
          "TT"      : "*1.04"}
SFlist["JERup"]={"Zbb"    : "*((jetmetnj==2 )*1.19 + (jetmetnj>2)*1.28)",
          "Zbx"    : "*1.28",
          "Zxx"      : "*1.25",
          "TT"      : "*1.06"}
SFlist["JERdown"]={"Zbb"    : "*((jetmetnj==2 )*1.18 + (jetmetnj>2)*1.30)",
          "Zbx"    : "*1.30",
          "Zxx"      : "*1.28",
          "TT"      : "*1.05"}
SFlist["BTAG_light_up"]={"Zbb"    : "*((jetmetnj==2 )*1.17 + (jetmetnj>2)*1.28)",
          "Zbx"    : "*1.28",
          "Zxx"      : "*1.12",
          "TT"      : "*1.05"}
SFlist["BTAG_light_down"]={"Zbb"    : "*((jetmetnj==2 )*1.19 + (jetmetnj>2)*1.29)",
          "Zbx"    : "*1.29",
          "Zxx"      : "*1.49",
          "TT"      : "*1.05"}
SFlist["BTAG_bc_down"]={"Zbb"    : "*((jetmetnj==2 )*1.23 + (jetmetnj>2)*1.34)",
          "Zbx"    : "*1.34",
          "Zxx"      : "*1.35",
          "TT"      : "*1.1"}
SFlist["BTAG_bc_up"]={"Zbb"    : "*((jetmetnj==2 )*1.13 + (jetmetnj>2)*1.23)",
          "Zbx"    : "*1.23",
          "Zxx"      : "*1.24",
          "TT"      : "*1.01"}
