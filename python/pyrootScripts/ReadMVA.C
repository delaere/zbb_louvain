#include "TMVA/Reader.h"
using namespace TMVA;
double ReadMVA(float ptz, float drll, float ptbb, float drbb, float ptllbb, float dphillbb, float costhetab1, float met){
  TMVA::Reader* reader = new TMVA::Reader( "!Color:!Silent" );
  reader->AddVariable("max(boostselectionbestzptMu,boostselectionbestzptEle)",&ptz);
  reader->AddVariable("max(boostselectiondrllMu,boostselectiondrllEle)",&drll);
  reader->AddVariable("boostselectiondijetPt",&ptbb);
  reader->AddVariable("boostselectiondijetdR",&drbb);
  reader->AddVariable("boostselectionZbbPt",&ptllbb);
  reader->AddVariable("boostselectiondphiZbb",&dphillbb);
  reader->AddVariable("abs(boostselectionCosThetab1)",&costhetab1);
  reader->AddVariable("jetmetMET",&met);
  reader->BookMVA( "MLP", "./weights/2HDM_MLP.weights.xml" );
  double mvaValue = reader->EvaluateMVA( "MLP" );
  return mvaValue;
}
