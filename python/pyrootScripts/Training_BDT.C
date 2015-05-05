
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>

#include "TChain.h"
#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TObjString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "test/TMVAGui.C"

#include "TMVA/Factory.h"
#include "TMVA/Tools.h"

// channel="Mu";
// isZHvsOther=True;
// cat="2j";

void Training_BDT(TString channel, bool isZHvsOther, TString cat){

  TString name;
  if (isZHvsOther) name="ZHvsOther";
  else name="TTvsDY";
  if (channel=="Mu") name=name+"_Mu";
  else name=name+"_El";   
  if (cat=="2j")name=name+"_2j";
  else if(cat=="2j") name=name+"_3j";
  else name=name+"_noCat";
  

  
  TMVA::Tools::Instance();

  TFile* outputFile = TFile::Open( "outputtrainning"+name+".root", "RECREATE" );
  
  
  TMVA::Factory *factory = new TMVA::Factory( "BDT_NN_trainning"+name, outputFile,"!V:!Silent:Color:DrawProgressBar:Transformations=I;D;P;G,D:AnalysisType=Classification" );;

  //TFile *input   = TFile::Open( "study_histo.root" );

  TFile *inputTT   = TFile::Open( "/home/fynu/cbeluffi/storage/RDS/5320_JP_Skimmed_V5/llbbX/TTFullLept_Summer12_final_skimed_llbbX_withWeights_V3.root" );
  TFile *inputDYM10   = TFile::Open( "/home/fynu/cbeluffi/storage/RDS/5320_JP_Skimmed_V5/llbbX/DYjets_M10to50_Summer12_final_skimed_llbbX_withWeights_V3.root" );
  TFile *inputDY   = TFile::Open( "/home/fynu/cbeluffi/storage/RDS/5320_JP_Skimmed_V5/llbbX/DYjets_Summer12_final_skimed_llbbX_withWeights_V3.root" );
  TFile *inputZZ   = TFile::Open( "/home/fynu/cbeluffi/storage/RDS/5320_JP_Skimmed_V5/llbbX/ZZ_Summer12_final_skimed_llbbX_withWeights_V3.root" );
  TFile *inputZH   = TFile::Open( "/home/fynu/cbeluffi/storage/RDS/5320_JP_Skimmed_V5/llbbX/ZH125_Summer12_final_skimed_llbbX_withWeights_V3.root" ); 
  TFile *inputWW   = TFile::Open( "/home/fynu/cbeluffi/storage/RDS/5320_JP_Skimmed_V5/llbbX/WW_Summer12_final_skimed_llbbX_withWeights_V3.root" );
  TFile *inputWZ   = TFile::Open( "/home/fynu/cbeluffi/storage/RDS/5320_JP_Skimmed_V5/llbbX/WZ_Summer12_final_skimed_llbbX_withWeights_V3.root" );
  TFile *inputWt   = TFile::Open( "/home/fynu/cbeluffi/storage/RDS/5320_JP_Skimmed_V5/llbbX/Wt_Summer12_final_skimed_llbbX_withWeights_V3.root" );
  TFile *inputWtbar   = TFile::Open( "/home/fynu/cbeluffi/storage/RDS/5320_JP_Skimmed_V5/llbbX/Wtbar_Summer12_final_skimed_llbbX_withWeights_V3.root" );
  TFile *inputTTSemi   = TFile::Open( "/home/fynu/cbeluffi/storage/RDS/5320_JP_Skimmed_V5/llbbX/TTSemiLept_Summer12_final_skimed_llbbX_withWeights_V3.root" );

  
  
  TTree *signal     = (TTree*)inputZH->Get("rds_zbb");
  TTree *backgroundDY = (TTree*)inputDY->Get("rds_zbb");
  TTree *backgroundZZ = (TTree*)inputZZ->Get("rds_zbb");
  TTree *backgroundTT = (TTree*)inputTT->Get("rds_zbb");
  TTree *backgroundDYM10 = (TTree*)inputDYM10->Get("rds_zbb");
  TTree *backgroundWW = (TTree*)inputWW->Get("rds_zbb");
  TTree *backgroundWZ = (TTree*)inputWZ->Get("rds_zbb");
  TTree *backgroundWt = (TTree*)inputWt->Get("rds_zbb");
  TTree *backgroundWtbar = (TTree*)inputWtbar->Get("rds_zbb");
  TTree *backgroundTTSemi = (TTree*)inputTTSemi->Get("rds_zbb");
  
  if (isZHvsOther ){
    factory->AddSignalTree( signal    , 1.2);
    factory->AddBackgroundTree( backgroundDY, 0.54);
    factory->AddBackgroundTree( backgroundZZ, 0.1);
    factory->AddBackgroundTree( backgroundDYM10, 0.02);
    factory->AddBackgroundTree( backgroundTT, 0.3); 
    factory->AddBackgroundTree(backgroundWW , 0.005);
    factory->AddBackgroundTree(backgroundWZ , 0.005);
    factory->AddBackgroundTree(backgroundWt , 0.01);
    factory->AddBackgroundTree(backgroundWtbar ,0.01 );  
    factory->AddBackgroundTree(backgroundTTSemi ,0.01 );
  }
 else{
    factory->AddSignalTree( backgroundDY    , 1.0);
    factory->AddBackgroundTree( backgroundTT, 1.0);
 }
  if (isZHvsOther ){
    factory->AddVariable("MinusLogW_ZH_cor3",   'F');
    factory->AddVariable("MinusLogW_ZH_cor0", 'F');
    factory->AddVariable("MinusLogW_ZZ_cor3",   'F');
    factory->AddVariable("MinusLogW_ZZ_cor0", 'F');  
    factory->AddVariable("MinusLogW_TT",   'F');
    factory->AddVariable("MinusLogW_gg_Zbb",  'F');
    factory->AddVariable("MinusLogW_qq_Zbb",     'F');
  }
  else{
    factory->AddVariable("MinusLogW_TT",   'F');
    factory->AddVariable("MinusLogW_gg_Zbb",  'F');
    factory->AddVariable("MinusLogW_qq_Zbb",     'F');  
  }
  

  TCut mycuts, mycutb;
  
  if(isZHvsOther){
    if(channel=="Mu"){ 
      if(cat=="2j"){ 
        mycuts = "(MinusLogW_ZH_cor3 > 2 && MinusLogW_ZH_cor0 > 2 &&MinusLogW_ZZ_cor0> 2 &&MinusLogW_ZZ_cor3> 2 &&MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_ZH_cor3<50 && MinusLogW_ZH_cor0<50 &&MinusLogW_ZZ_cor0<50 &&MinusLogW_ZZ_cor3<50 &&MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_6_idx && eventSelectionmu1pt_inc>20 && eventSelectionmu2pt_inc>20 &&  eventSelectiondilepM_inc > 76 &&  eventSelectiondilepM_inc < 106 && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30&& jetmetnj==2 && (eventSelectiondijetM_inc > 80 && eventSelectiondijetM_inc < 150))";
        mycutb = "(MinusLogW_ZH_cor3 > 2 && MinusLogW_ZH_cor0 > 2 &&MinusLogW_ZZ_cor0> 2 &&MinusLogW_ZZ_cor3> 2 &&MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_ZH_cor3<50 && MinusLogW_ZH_cor0<50 &&MinusLogW_ZZ_cor0<50 &&MinusLogW_ZZ_cor3<50 &&MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_6_idx && eventSelectionmu1pt_inc>20 && eventSelectionmu2pt_inc>20 &&  eventSelectiondilepM_inc > 76 &&  eventSelectiondilepM_inc < 106 && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30&& jetmetnj==2 && (eventSelectiondijetM_inc > 80 && eventSelectiondijetM_inc < 150))";
      }
      else{
        mycuts = "(MinusLogW_ZH_cor3 > 2 && MinusLogW_ZH_cor0 > 2 &&MinusLogW_ZZ_cor0> 2 &&MinusLogW_ZZ_cor3> 2 &&MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_ZH_cor3<50 && MinusLogW_ZH_cor0<50 &&MinusLogW_ZZ_cor0<50 &&MinusLogW_ZZ_cor3<50 &&MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_6_idx && eventSelectionmu1pt_inc>20 && eventSelectionmu2pt_inc>20 &&  eventSelectiondilepM_inc > 76 &&  eventSelectiondilepM_inc < 106 && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30&& jetmetnj>2 && (eventSelectiondijetM_inc > 50 && eventSelectiondijetM_inc < 150))";
        mycutb = "(MinusLogW_ZH_cor3 > 2 && MinusLogW_ZH_cor0 > 2 &&MinusLogW_ZZ_cor0> 2 &&MinusLogW_ZZ_cor3> 2 &&MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_ZH_cor3<50 && MinusLogW_ZH_cor0<50 &&MinusLogW_ZZ_cor0<50 &&MinusLogW_ZZ_cor3<50 &&MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_6_idx && eventSelectionmu1pt_inc>20 && eventSelectionmu2pt_inc>20 &&  eventSelectiondilepM_inc > 76 &&  eventSelectiondilepM_inc < 106 && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30&& jetmetnj>2 && (eventSelectiondijetM_inc > 50 && eventSelectiondijetM_inc < 150))";
      }
    }
    else {
      if(cat=="2j"){ 
        mycuts = "(MinusLogW_ZH_cor3 > 2 && MinusLogW_ZH_cor0 > 2 &&MinusLogW_ZZ_cor0> 2 &&MinusLogW_ZZ_cor3> 2 &&MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_ZH_cor3<50 && MinusLogW_ZH_cor0<50 &&MinusLogW_ZZ_cor0<50 &&MinusLogW_ZZ_cor3<50 &&MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_16_idx && eventSelectionel1pt_inc>20 && eventSelectionel2pt_inc>20 &&  eventSelectiondilepM_inc > 76 &&  eventSelectiondilepM_inc < 106  && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30&& jetmetnj==2 && (eventSelectiondijetM_inc > 80 && eventSelectiondijetM_inc < 150))";
        mycutb = "(MinusLogW_ZH_cor3 > 2 && MinusLogW_ZH_cor0 > 2 &&MinusLogW_ZZ_cor0> 2 &&MinusLogW_ZZ_cor3> 2 &&MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_ZH_cor3<50 && MinusLogW_ZH_cor0<50 &&MinusLogW_ZZ_cor0<50 &&MinusLogW_ZZ_cor3<50 &&MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_16_idx && eventSelectionel1pt_inc>20 && eventSelectionel2pt_inc>20 &&  eventSelectiondilepM_inc > 76 &&  eventSelectiondilepM_inc < 106  && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30&& jetmetnj==2 && (eventSelectiondijetM_inc > 80 && eventSelectiondijetM_inc < 150))";
      }
      else{
        mycuts = "(MinusLogW_ZH_cor3 > 2 && MinusLogW_ZH_cor0 > 2 &&MinusLogW_ZZ_cor0> 2 &&MinusLogW_ZZ_cor3> 2 &&MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_ZH_cor3<50 && MinusLogW_ZH_cor0<50 &&MinusLogW_ZZ_cor0<50 &&MinusLogW_ZZ_cor3<50 &&MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_16_idx && eventSelectionel1pt_inc>20 && eventSelectionel2pt_inc>20 &&  eventSelectiondilepM_inc > 76 &&  eventSelectiondilepM_inc < 106  && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30&& jetmetnj>2 && (eventSelectiondijetM_inc > 50 && eventSelectiondijetM_inc < 150))";
        mycutb = "(MinusLogW_ZH_cor3 > 2 && MinusLogW_ZH_cor0 > 2 &&MinusLogW_ZZ_cor0> 2 &&MinusLogW_ZZ_cor3> 2 &&MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_ZH_cor3<50 && MinusLogW_ZH_cor0<50 &&MinusLogW_ZZ_cor0<50 &&MinusLogW_ZZ_cor3<50 &&MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_16_idx && eventSelectionel1pt_inc>20 && eventSelectionel2pt_inc>20 &&  eventSelectiondilepM_inc > 76 &&  eventSelectiondilepM_inc < 106  && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30&& jetmetnj>2 && (eventSelectiondijetM_inc > 50 && eventSelectiondijetM_inc < 150))";
      
      }
    }
  }
  
  else{
    if(channel=="Mu"){ 
     
        mycuts = "(MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_6_idx && eventSelectionmu1pt_inc>20 && eventSelectionmu2pt_inc>20 &&  eventSelectiondilepM_inc > 60 &&  eventSelectiondilepM_inc < 120 && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30)";
        mycutb = "(MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_6_idx && eventSelectionmu1pt_inc>20 && eventSelectionmu2pt_inc>20 &&  eventSelectiondilepM_inc > 60 &&  eventSelectiondilepM_inc < 120 && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30)";
      
    }
    else {
        mycuts = "(MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_16_idx && eventSelectionel1pt_inc>20 && eventSelectionel2pt_inc>20 &&  eventSelectiondilepM_inc > 60 &&  eventSelectiondilepM_inc < 120 && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30)";
        mycutb = "(MinusLogW_TT> 2 &&MinusLogW_gg_Zbb> 2 &&MinusLogW_qq_Zbb> 2)&&(MinusLogW_TT<50 &&MinusLogW_gg_Zbb<50 &&MinusLogW_qq_Zbb<50)&& (rc_stage_16_idx && eventSelectionel1pt_inc>20 && eventSelectionel2pt_inc>20 &&  eventSelectiondilepM_inc > 60 &&  eventSelectiondilepM_inc < 120 && jetmetMETsignificance<10 && jetmetbjet1pt>30 && jetmetbjet2pt>30)";
      
  
    }
  }
    
  factory->PrepareTrainingAndTestTree( mycuts, mycutb,
                                        "nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V" );
   
  
  
  if (isZHvsOther)factory->BookMethod( TMVA::Types::kBDT, "BDT", "!H:!V:NTrees=40:nEventsMin=600:MaxDepth=10:BoostType=AdaBoost:SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning:VarTransform=Decorrelate" );
  else factory->BookMethod( TMVA::Types::kBDT, "BDT", "!H:!V:NTrees=50:nEventsMin=1000:MaxDepth=20:BoostType=AdaBoost:SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning:VarTransform=Decorrelate" );
  
  if (isZHvsOther)factory->BookMethod( TMVA::Types::kMLP, "MLP", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=1000:HiddenLayers=N+6:TestRate=5:!UseRegulator" );
  else factory->BookMethod( TMVA::Types::kMLP, "MLP", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=500:HiddenLayers=N+2:TestRate=5:!UseRegulator" );
  // Train MVAs using the set of training events
  factory->TrainAllMethods();

  // ---- Evaluate all MVAs using the set of test events
  factory->TestAllMethods();

  // ----- Evaluate and compare performance of all configured MVAs
  factory->EvaluateAllMethods();
   
  outputFile->Close();

  
  std::cout << "==> Wrote root file: " << outputFile->GetName() << std::endl;
  std::cout << "==> TMVAClassification is done!" << std::endl;

  delete factory;

  // Launch the GUI for the root macros
  if (!gROOT->IsBatch() ) TMVAGui( "outputtrainning"+name+".root" );


  
  


}

void TrainAll(){
Training_BDT("Mu", 0, "2j");
Training_BDT("Mu", 1, "2j");
Training_BDT("Mu", 0, "3j");
Training_BDT("Mu", 1, "3j");
Training_BDT("El", 0, "2j");
Training_BDT("El", 1, "2j");
Training_BDT("El", 0, "3j");
Training_BDT("El", 1, "3j");



}
