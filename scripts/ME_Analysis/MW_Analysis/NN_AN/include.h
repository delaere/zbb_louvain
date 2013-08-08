using namespace std;
#include <TMultiLayerPerceptron.h>
#include <TMLPAnalyzer.h>
#include <TTree.h>
#include <TCanvas.h>
#include <TGraph.h>
#include <TGraph2D.h>
#include <TSystem.h>
#include <fstream>
#include <iostream>

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
#include "TStyle.h"
#include "TMinuit.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TMultiGraph.h"
#include "TFile.h"
#include "TMVA/Factory.h"
#include "TMVA/Reader.h"

using namespace TMVA;

#include "TH1.h"
#include "TF1.h"
#include "TRandom3.h"
#include "TVirtualFitter.h"
#include "Minuit2/FCNBase.h"
#include "TFitterMinuit.h"
#include "TSystem.h"
#include "TStopwatch.h"
#include <vector>
#include "TFractionFitter.h"

#include <map>
