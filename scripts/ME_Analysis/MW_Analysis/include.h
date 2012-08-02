
#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <vector>

#include "TROOT.h"
#include "TApplication.h"

#include "TChain.h"
#include "TClonesArray.h"
#include "TString.h"
#include "TCanvas.h"
#include "TH2.h"
#include "THStack.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TLorentzVector.h"
#include "TVector2.h"
#include "TLegend.h"
#include "TStyle.h"
#include "TMinuit.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TMultiGraph.h"
#include "TFile.h"

#include "TH1.h"
#include "TF1.h"
#include "TRandom3.h"
#include "TVirtualFitter.h"
#include "Minuit2/FCNBase.h"
#include "TFitterMinuit.h"
#include "TSystem.h"
#include "TStopwatch.h"
#include <vector>

//Indicate path to your ExRootAnalysis Directory. 

#include "ExRootAnalysis/ExRootAnalysis/ExRootClasses.h"
#include "ExRootAnalysis/ExRootAnalysis/ExRootTreeReader.h"
#include "ExRootAnalysis/ExRootAnalysis/ExRootTreeWriter.h"
#include "ExRootAnalysis/ExRootAnalysis/ExRootTreeBranch.h"
#include "ExRootAnalysis/ExRootAnalysis/ExRootResult.h"
#include "ExRootAnalysis/ExRootAnalysis/ExRootUtilities.h"
