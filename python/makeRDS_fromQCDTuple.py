#######################################################
#
# Loop over entries
#
# Loop over jets per event
#
# Get flavor, pt, eta and select jets
#
# Get PV, pT, pTHat and determine per-event weight
#
# Save in a RooDataSet
#   - m(SV)
#   - PV-cat, pT-cat, pThat-cat
#   - weight
#
# (c) Zbb-CP3 Warriors, 2011
#
####################################################

from ROOT import *
import os

#####

whichSample = 2

### Getting a file and a tree

paths = {}
paths[1] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd30a50/"
paths[2] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd50a80/"
paths[3] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd80a120/"
paths[4] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd120a170/"
paths[5] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd170a300/"
paths[6] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd300a470_v1/"
paths[7] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd470a600/"
paths[8] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd600a800/"
paths[9] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd800a1000/"
paths[10] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd1000a1400/"
paths[11] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd1400a1800/"
paths[12] = "/scratch/tdupree/bMistagTuples/ForTristan/qcd1800/"
    
dirLists={}
files=[]

path = paths[whichSample]

dirList = os.listdir(path)
for fname in dirList :
    files.append(path+fname)

print "files = ", files

trees = []
#ef = TFile()
#ce = TTree()

x = {}

for file in files :
    x[file] = TFile(file)
    trees.append(x[file].Get("mistag/ttree;3"))

###############################################################
#
# NB: I would like to simply add all TTrees into one single TTree
# ( Such that we dont have to loop over the TTrees ) 
# However, I didnt manage (probably since I am a moron)
# Most obvious would be to use TChain.Add,
# but apparently TFile.Get returns a TTree and not a TChain...
# Suggestions welcome!
#
##############################################################

### The RooDataSet I wanna fill

rrv_msv    = RooRealVar("rrv_msv",    "rrv_msv",    -1,   10)
rrv_bTagHE = RooRealVar("rrv_bTagHE", "rrv_bTagHE", -1,   10)
rrv_bTagHP = RooRealVar("rrv_bTagHP", "rrv_bTagHP", -1,   10)
rrv_pT     = RooRealVar("rrv_pT",     "rrv_pT",      0, 1000)
rrv_eta    = RooRealVar("rrv_eta",    "rrv_eta",   -10,   10)
rrv_nPV    = RooRealVar("rrv_nPV",    "rrv_nPV",     0,   50)
rrv_nPU    = RooRealVar("rrv_nPU",    "rrv_nPU",     0,   50)

rc_flav = RooCategory("rc_flav","rc_flav")
rc_flav.defineType("l",1) 
rc_flav.defineType("c",4) 
rc_flav.defineType("b",5) 
rc_flav.defineType("g",6) 
rc_flav.defineType("x",9) 

rc_sel = RooCategory("rc_sel","rc_sel")
rc_sel.defineType("HE",5) 
rc_sel.defineType("HP",6) 

# - pThat
# - pT
# - PV

myRDS = RooDataSet("myRDS","myRDS",RooArgSet(rrv_msv,
                                             rrv_bTagHE,
                                             rrv_bTagHP,
                                             rrv_pT,
                                             rrv_eta,
                                             rrv_nPV,
                                             rrv_nPU,
                                             rc_flav,
                                             rc_sel))


### NOW LET'S GO!!!

numSaved = 0

for tree in trees:
    entries = tree.GetEntriesFast()

    for jentry in xrange(entries) :
        # get the next tree in the chain and verify
        ientry = tree.LoadTree( jentry )
        if ientry < 0:
            bla

        # copy next entry into memory and verify
        nb = tree.GetEntry( jentry )
        if nb <= 0:
            continue

        for i in range(0,len(tree.Jet_pt)):
            #print "Jet_pt      = ", tree.Jet_pt[ i ]
            #print "Jet_eta     = ", tree.Jet_eta[ i ]
            #print "Jet_flavour = ", tree.Jet_flavour[ i ]
            #print "Jet_Svx     = ", tree.Jet_Svx[ i ]
            #print "Jet_SvxHP   = ", tree.Jet_SvxHP[ i ]
            #print "Jet_SvxMass = ", tree.Jet_SvxMass[ i ]
            #print "pthat       = ", tree.pthat
            #print "pt       = ", tree.Jet_pt[i]
            #print "eta       = ", tree.Jet_eta[i]
            #print "*** #PU = ", tree.nPU
            #print "*** #PV = ", tree.nPV
            rrv_msv.setVal(    tree.Jet_SvxMass[ i ] )
            rrv_bTagHE.setVal( tree.Jet_Svx[ i ]     )
            rrv_bTagHP.setVal( tree.Jet_SvxHP[ i ]   )
            rrv_pT.setVal(     tree.Jet_pt[i]        )  
            rrv_eta.setVal(    tree.Jet_eta[i]       )
            rrv_nPU.setVal(    tree.nPU              )
            rrv_nPV.setVal(    tree.nPV              )
            if tree.Jet_Svx[ i ] > 1.74 and tree.Jet_pt[i] < 150:
                rc_sel.setLabel("HE")
                if tree.Jet_SvxHP[ i ] > 2.00               : rc_sel.setLabel("HP")
                if tree.Jet_flavour[ i ] == ( 1 or 2 or 3 ) : rc_flav.setLabel("l")
                elif tree.Jet_flavour[ i ] == 4             : rc_flav.setLabel("c")
                elif tree.Jet_flavour[ i ] == 5             : rc_flav.setLabel("b")
                else                                        : rc_flav.setLabel("x")

#                    for gl in range(0,tree.nBFromGSplit):
#                        if tree.Jet_pt[i] < 1.1*tree.bFromGSplit_pT[gl]:
#                            if tree.bFromGSplit_phi[gl] < 1.1*tree.Jet_phi[i] and tree.bFromGSplit_phi[gl] > 0.9*tree.Jet_phi[i] :
#                                if tree.bFromGSplit_eta[gl] < 1.1*tree.Jet_eta[i] and tree.bFromGSplit_eta[gl] > 0.9*tree.Jet_phi[i] :
#                                    if tree.bFromGSplit_eta[gl] < 2.5 :
#                                        rc_flav.setLabel("g")
#                                        print "b from gluon splitting!!!"
                
#   #check if (nBFromGSplit>0) {
#   #    for (int igluon =0; igluon<nBFromGSplit; igluon++){
#   #    double comp = fabs( bFromGSplit_pT[igluon] - ptjet) ;  comp = comp/bFromGSplit_pT[igluon] ;
#   #    if ( comp > 1.1 )  continue;
#   #    if (bFromGSplit_eta[igluon] < 0.8*EtaMin )  continue;
#   #    if (bFromGSplit_eta[igluon] > 1.2*EtaMax )  continue;
#   #    double test = deltaR(etajet, phijet , bFromGSplit_eta[igluon],bFromGSplit_phi[igluon]) ;
#   #    DeltaRGluonSp->Fill(test,ww);
#   #
#   #    if (test < 0.15){issplit = 1 ; DeltaRGluonMass->Fill(test,mass2vx); break;}#
##
#


                #elif tree.Jet_flavour[ i ] == 5                         :
                #    rc_flav.setLabel("b")
                #    print "JUST b"
                #else                                                    : rc_flav.setLabel("x")
                weight = Double(1.)
                numSaved += 1
                myRDS.add(RooArgSet(rrv_msv,
                                    rrv_pT,
                                    rrv_eta,
                                    rrv_bTagHE,
                                    rrv_bTagHP,
                                    rrv_nPU,
                                    rrv_nPV,
                                    rc_flav,
                                    rc_sel
                                    ))


ws = RooWorkspace("ws","workspace")
getattr(ws,'import')(myRDS)
ws.writeToFile("bTagPurRDS_QCD_"+str(whichSample)+".root")
gDirectory.Add(ws)
                        
                
#    for JPT in mychain.Jet_pt :    
#        print "JPT = ", JPT
#    for JETA in mychain.Jet_eta:
#        print "JETA = ", JETA
#    for JET_FLV in mychain.Jet_flavour:
#        print "JET_FLV = ", JET_FLV
#    for JSVM in mychain.Jet_SvxMass :
#        print "JSVM = ", JSVM



###---------------------------------------------------------------------------------------------####

#    for (int ijet = 0; ijet < nJet; ijet++) {
#        float residual = 1.
#        if ( Run > 0 ) residual = Jet_residual[ijet]
#        float ptjet = Jet_pt[ijet] * Jet_jes[ijet] * residual
#         float etajet = fabs(Jet_eta[ijet])
#         if ( !(etajet >= EtaMin && etajet < EtaMax) ) continue#
#
#         ngoodj++; selecjet[ngoodj]=ijet; #
#
## njets = nJet;
## int npv = nPV; 
## if ( npv >= 20 ) npv = 20;
## int npu = nPU; 
##
## if ( pthat > 0. ){
##   if (PU_bunch[nPU] != 0) continue;#
#
#     #### make weight #
#
#    ### Loop on jets
#    for (int isel = 0; isel < ngoodj; isel++) :
#        
#        int ijet = selecjet[isel];
#   if ( ijet == 0 ) {
#     allevents++;
#     if ( allevents%100000 == 0 ) std::cout << "events : " << allevents << std::endl ;
#      hData_All_NJets->Fill( njets , ww1 );
#     hData_NJets->Fill( numjet , ww1 );
##
#
#     numjet = 0;
#     ntagjet = 0;
#   }
#
#   float ptjet = Jet_pt[ijet] * Jet_jes[ijet] * residual;
#   int flavour = abs( Jet_flavour[ijet] );
#   if ( flavour >= 1 && flavour <= 3 ) flavour = 1;#
#
#   if ( !(ptjet >= PtMin && ptjet < PtMax) ) continue;
#   if ( !(etajet >= EtaMin && etajet < EtaMax) ) continue;
#
#   hData_All_JetPV->Fill( npv , 1. );
#   hData_All_JetPt->Fill( ptjet , ww1 );
#   hData_All_JetEta->Fill( fabs(etajet) , 1. );
#   hData_All_JetRun->Fill( Run , 1. );
#   hAllFlav_All_Flavour->Fill( flavour , 1. );
#
#   double mass2vx ;
#
#   #if (Jet_SvxMass[ijet] >6.5) mass2vx =6.499 ;
#   #else if (Jet_SvxMass[ijet] <0.05) mass2vx =-0.99 ;
#   else mass2vx=Jet_SvxMass[ijet];
#   
##// High Purity Secondary Vertex
##   else if ( NN == 5 ) {
##     if ( Jet_SvxHP[ijet] > 1.  )  varpos =  5.*Jet_SvxHP[ijet];
##     if ( Jet_SvxNHP[ijet] < -1. ) varneg = -5.*Jet_SvxNHP[ijet];
##     if ( Jet_SvxHP[ijet] > TagCut )  TagPos = true;
##     if (-Jet_SvxNHP[ijet] > TagCut ) TagNeg = true;
##     cat = Jet_histSvx[ijet];
##   }
#
#   if ( flavour == 1 || 2 || 3 || flavour == 21 ) : LIGHT
#   elif (flavour == 4)                            : C  
#   elif (flavour == 5)                            : B#
#
#   #check if (nBFromGSplit>0) {
#   #    for (int igluon =0; igluon<nBFromGSplit; igluon++){
#   #	 double comp = fabs( bFromGSplit_pT[igluon] - ptjet) ;  comp = comp/bFromGSplit_pT[igluon] ;
#   #	 if ( comp > 1.1 )  continue;
#   #	 if (bFromGSplit_eta[igluon] < 0.8*EtaMin )  continue;
#   #	 if (bFromGSplit_eta[igluon] > 1.2*EtaMax )  continue;
#   #	 double test = deltaR(etajet, phijet , bFromGSplit_eta[igluon],bFromGSplit_phi[igluon]) ;
#   #	 DeltaRGluonSp->Fill(test,ww);
#   #
#   #	 if (test < 0.15){issplit = 1 ; DeltaRGluonMass->Fill(test,mass2vx); break;}#
##
#
#  # todo: also check pos/neg



### some beautiful hardcoded arrays of weights

# float nevt[14] = {0,1650000,6583068,6600000,6589956,6127528,6220160,6432669,3990085,4245695,
#	4053888,2093222,2196200,293139};
# float xsec[14] = {3.675e+10, 8.159e+08, 5.312e+07, 6.359e+06, 7.843e+05, 1.151e+05, 2.426e+04, 1.168e+03, 7.022e+01,
#		  1.555e+01,1.8444,3.321e-01,1.087e-02,3.575e-04};

# float WeightPtHat[14];
# for (Int_t k=0; k<14; k++){
#   WeightPtHat[k] = lumidata*xsec[k]/nevt[k]/1000. ;
#   cout << "WeightPtHat[" << k << "] = " << WeightPtHat[k] << endl;
# }

# float WeightPU[20] = {0.747694 ,0.853661 ,0.882735 ,0.915668 ,0.951334 ,0.987061 ,1.021296 ,1.052876 ,1.081233 ,1.105996 ,1.126985 ,1.144090 ,1.157152 ,1.165910 ,1.169945 ,1.168780 ,1.161875 ,1.148769 ,1.129215 ,0.631684};
# float WeightPt[15] ={ 1., 0.617427, 0.181917, 0.720309, 2.317049, 8.048693, 18.743258, 35.954548, 107.985794, 130.051636, 219.512650, 331.493652, 340.109497, 
#346.113312, 350.579224};

#Long64_t nentries = fChain->GetEntriesFast();

#f = TFile("/scratch/tdupree/bMistagTuples/ForTristan/qcd30a50/JetTree_10_1_Hth.root");
##f.cd("JetTree_10_1_Hth.root.root:/mistag")
##tree = gDirectory.Get("ttree;3")
#mytsjeen = f.Get("mistag/ttree;3")
