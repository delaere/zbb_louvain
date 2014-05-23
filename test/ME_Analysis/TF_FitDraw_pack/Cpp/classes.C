/*
 *  classes.C
 *  
 *
 *  Created by Arnaud Pin on 27/03/09.
 *  Copyright 2009 __MyCompanyName__. All rights reserved.
 *
 */

#include "include.h"

//--------------------------------------------------------
class ExRootDATA: public TObject
{
public:

  Double_t PT;
  Double_t PTjet;
  Double_t DELTA_PT;
  Double_t DELTA_E;
  Double_t E;
  Double_t Ejet;
  Double_t Eta;
  Double_t Eta_jet;
  Double_t Phi;
  Double_t Phi_jet;
  ClassDef(ExRootDATA, 1)

};
//--------------------------------------------------------