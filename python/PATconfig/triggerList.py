
#all non-prescaled triggers should be copied in the nonPrescalePath list
singleMuPath = [
    #Main ones  
    'path("HLT_IsoMu24_eta2p1_v*")',
    'path("HLT_IsoMu24_v*")',
    #higher thresholds
    'path("HLT_IsoMu30_v*")',
    'path("HLT_IsoMu30_eta2p1_v*")',
    'path("HLT_IsoMu34_eta2p1_v*")',
    'path("HLT_IsoMu40_eta2p1_v*")',
    'path("HLT_Mu40_eta2p1_v*")',
    'path("HLT_Mu50_eta2p1_v*")',
    #prescaled or partially prescaled 
    'path("HLT_Mu5_v*")',
    'path("HLT_Mu8_v*")',
    'path("HLT_Mu12_v*")',
    'path("HLT_Mu15_eta2p1_v*")',
    'path("HLT_Mu17_v*")',
    'path("HLT_IsoMu20_eta2p1_v*")',
    'path("HLT_Mu24_eta2p1_v*")',
    'path("HLT_Mu24_v*")',
    'path("HLT_Mu30_eta2p1_v*")',
    'path("HLT_Mu30_v*")',
    ]

doubleMuPath = [
    #Main ones
    'path("HLT_Mu17_Mu8_v*")',
    'path("HLT_Mu17_TkMu8_v*")',
    #higher thresholds
    'path("HLT_Mu22_TkMu8_v*")',
    'path("HLT_Mu22_TkMu22_v*")',
    #3muons
    'path("HLT_DoubleMu5_IsoMu5_v*")',
    'path("HLT_TripleMu5_v*")',
    #prescaled or partially prescaled
    'path("HLT_Mu13_Mu8_v*")',
    'path("HLT_Mu13_Mu8_NoDZ_v*")',
    'path("HLT_Mu17_TkMu8_NoDZ_v*")',
    ]

singleElePath = [
    #Main one
    'path("HLT_Ele27_WP80_v*")', #prescaled in the first menus
    'path("HLT_Ele32_WP70_v*")', #only present in the first menus
    #higher thresholds
    'path("HLT_Ele32_WP70_PFMT50_v*")',
    'path("HLT_Ele80_CaloIdVT_TrkIdT_v*")', 
    'path("HLT_Ele80_CaloIdVT_GsfTrkIdT_v*")', #not in first data
    'path("HLT_Ele90_CaloIdVT_GsfTrkIdT_v*")', #not in first data
    'path("HLT_Ele100_CaloIdVT_TrkIdT_v*")',
    #prescaled or partially prescaled
    'path("HLT_Ele22_CaloIdL_CaloIsoVL_v*")',
    'path("HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")',
    'path("HLT_Ele27_WP70_v*")',
    'path("HLT_Ele30_CaloIdVT_TrkIdT_v*")',
    'path("HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_*")',
    'path("HLT_Ele65_CaloIdVT_TrkIdT_v*")',
    ]


doubleElePath = [
    #Main one
    'path("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")',
    #higher thresholds
    'path("HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v*")',
    'path("HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v*")',
    'path("HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v*")',
    'path("HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v*")', #HFT?
    'path("HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v*")',
    #3electrons
    'path("HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v*")',
    'path("HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v*")',
    'path("HLT_TripleEle10_CaloIdL_TrkIdVL_v*")',
    #prescaled or partially prescaled
    'path("HLT_Ele17_CaloIdL_CaloIsoVL_v*")',
    'path("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")',
    'path("HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v*")',
    'path("HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v*")',
    'path("HLT_Ele8_CaloIdL_CaloIsoVL_v*")',
    'path("HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")',
    'path("HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v*")',
    ]

MuEGPath = [
    #Main ones
    'path("HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")',
    'path("HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")',
    #higher thresholds
    'path("HLT_Mu30_Ele30_CaloIdL_v*")',
    #3leptons
    'path("HLT_DoubleMu5_Ele8_CaloIdT_TrkIdT_v*")', 
    'path("HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v*")',
    'path("HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v*")',
    'path("HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v*")',
    'path("HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v*")',
    #prescaled or partially prescaled
    'path("HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v*")',
    ]

nonPrescalePath = [

    ###singleMuPath = [
    #Main ones
    'HLT_IsoMu24_eta2p1_v*',
    'HLT_IsoMu24_v*',
    #higher thresholds
    'HLT_IsoMu30_v*',
    'HLT_IsoMu30_eta2p1_v*',
    'HLT_IsoMu34_eta2p1_v*',
    'HLT_IsoMu40_eta2p1_v*',
    'HLT_Mu40_eta2p1_v*',
    'HLT_Mu50_eta2p1_v*',

    ###doubleMuPath = [
    #Main ones
    'HLT_Mu17_Mu8_v*',
    'HLT_Mu17_TkMu8_v*',
    #higher thresholds
    'HLT_Mu22_TkMu8_v*',
    'HLT_Mu22_TkMu22_v*',
    #3muons
    'HLT_DoubleMu5_IsoMu5_v*',
    'HLT_TripleMu5_v*',

    ###singleElePath = [
    #Main one
    'HLT_Ele27_WP80_v*', #prescaled in the first menus
    'HLT_Ele32_WP70_v*', #only present in the first menus
    #higher thresholds
    'HLT_Ele32_WP70_PFMT50_v*',
    'HLT_Ele80_CaloIdVT_TrkIdT_v*',
    'HLT_Ele80_CaloIdVT_GsfTrkIdT_v*', #not in first data
    'HLT_Ele90_CaloIdVT_GsfTrkIdT_v*', #not in first data
    'HLT_Ele100_CaloIdVT_TrkIdT_v*',

    ###doubleElePath = [
    #Main one
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*',
    #higher thresholds
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v*',
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v*',
    'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v*',
    'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v*', #HFT?
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v*',
    #3electrons
    'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v*',
    'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v*',
    'HLT_TripleEle10_CaloIdL_TrkIdVL_v*',

    ###MuEGPath = [
    #Main ones
    'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*',
    'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*',
    #higher thresholds
    'HLT_Mu30_Ele30_CaloIdL_v*',
    #3leptons
    'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdT_v*',
    'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v*',
    'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v*',
    'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v*',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v*'

]
