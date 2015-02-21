##############################################
#
# Background SFs fitted on Data for DY subprocesses and TTbar
# Compute for H -> ZA analysis at 8 TeV using a 2D map of M(ll) between 60-120 GeV (7 bins) and CSV product of the 2 selected b-tagged jets (4 bins)
# Simulinous fit of ee and mm channels and ==2jets >=3jets categories
# Same is done for Nominal and systematics
# DY reweighted for M(lljj) at NLO using NLO/LO ratio derived with Delphes
#
##############################################

SFlist = {}

SFlist["Nominal"]={
    "Zbb"    : "*((jetmetnj==2 )*1.16 + (jetmetnj>2)*1.27)",
    "Zbx"    : "*1.27",
    "Zxx"    : "*1.27",
    "TT"     : "*1.04"
    }
#*******************************************
SFlist["JESup"]={
    "Zbb"    : "*((jetmetnj==2 )*1.12 + (jetmetnj>2)*1.15)",
    "Zbx"    : "*1.15",
    "Zxx"    : "*1.17",
    "TT"     : "*1.03"
    }
SFlist["JESdown"]={
    "Zbb"    : "*((jetmetnj==2 )*1.22 + (jetmetnj>2)*1.38)",
    "Zbx"    : "*1.38",
    "Zxx"    : "*1.39",
    "TT"     : "*1.05"
    }
#*******************************************
SFlist["JERup"]={
    "Zbb"    : "*((jetmetnj==2 )*1.17 + (jetmetnj>2)*1.26)",
    "Zbx"    : "*1.26",
    "Zxx"    : "*1.23",
    "TT"     : "*1.04"
    }
SFlist["JERdown"]={
    "Zbb"    : "*((jetmetnj==2 )*1.17 + (jetmetnj>2)*1.28)",
    "Zbx"    : "*1.28",
    "Zxx"    : "*1.27",
    "TT"     : "*1.04"
    }
#*******************************************
SFlist["BTAG_light_up"]={
    "Zbb"    : "*((jetmetnj==2 )*1.16 + (jetmetnj>2)*1.27)",
    "Zbx"    : "*1.27",
    "Zxx"    : "*1.11",
    "TT"     : "*1.04"
    }
SFlist["BTAG_light_down"]={
    "Zbb"    : "*((jetmetnj==2 )*1.17 + (jetmetnj>2)*1.27)",
    "Zbx"    : "*1.27",
    "Zxx"    : "*1.46",
    "TT"     : "*1.04"
    }
#*******************************************
SFlist["BTAG_bc_up"]={
    "Zbb"    : "*((jetmetnj==2 )*1.11 + (jetmetnj>2)*1.22)",
    "Zbx"    : "*1.22",
    "Zxx"    : "*1.22",
    "TT"     : "*1.00"
    }
SFlist["BTAG_bc_down"]={
    "Zbb"    : "*((jetmetnj==2 )*1.22 + (jetmetnj>2)*1.32)",
    "Zbx"    : "*1.32",
    "Zxx"    : "*1.33",
    "TT"     : "*1.08"
    }
