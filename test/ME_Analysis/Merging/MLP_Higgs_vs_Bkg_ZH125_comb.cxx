#include "MLP_Higgs_vs_Bkg_ZH125_comb.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.533743)/0.324675;
   input1 = (in1 - 0.463381)/0.315087;
   input2 = (in2 - 0.627984)/0.298602;
   switch(index) {
     case 0:
         return neuron0xe1c4e70();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb::Value(int index, double* input) {
   input0 = (input[0] - 0.533743)/0.324675;
   input1 = (input[1] - 0.463381)/0.315087;
   input2 = (input[2] - 0.627984)/0.298602;
   switch(index) {
     case 0:
         return neuron0xe1c4e70();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1b1710() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1b1a50() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1c2a20() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::input0xe1c2d70() {
   double input = 2.74532;
   input += synapse0xe179f60();
   input += synapse0xe1984b0();
   input += synapse0xe1c3020();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1c2d70() {
   double input = input0xe1c2d70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::input0xe1c3060() {
   double input = 0.215631;
   input += synapse0xe1c33a0();
   input += synapse0xe1c33e0();
   input += synapse0xe1c3420();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1c3060() {
   double input = input0xe1c3060();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::input0xe1c3460() {
   double input = 0.876409;
   input += synapse0xe1c37a0();
   input += synapse0xe1c37e0();
   input += synapse0xe1c3820();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1c3460() {
   double input = input0xe1c3460();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::input0xe1c3860() {
   double input = 3.06196;
   input += synapse0xe1c3ba0();
   input += synapse0xe1c3be0();
   input += synapse0xe1c3c20();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1c3860() {
   double input = input0xe1c3860();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::input0xe1c3c60() {
   double input = -0.0583123;
   input += synapse0xe1c3fa0();
   input += synapse0xe1c3fe0();
   input += synapse0xe1c4020();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1c3c60() {
   double input = input0xe1c3c60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::input0xe1c4060() {
   double input = -0.51065;
   input += synapse0xe1c43a0();
   input += synapse0xe1c43e0();
   input += synapse0xdf4dc90();
   input += synapse0xdf4dcd0();
   input += synapse0xe1c4530();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1c4060() {
   double input = input0xe1c4060();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::input0xe1c4570() {
   double input = 0.824126;
   input += synapse0xe1c48b0();
   input += synapse0xe1c48f0();
   input += synapse0xe1c4930();
   input += synapse0xe1c4970();
   input += synapse0xe1c49b0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1c4570() {
   double input = input0xe1c4570();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::input0xe1c49f0() {
   double input = 2.90807;
   input += synapse0xe1c4d30();
   input += synapse0xe1c4d70();
   input += synapse0xe1c4db0();
   input += synapse0xe1c4df0();
   input += synapse0xe1c4e30();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1c49f0() {
   double input = input0xe1c49f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::input0xe1c4e70() {
   double input = 0.723816;
   input += synapse0xe1c5090();
   input += synapse0xe1c50d0();
   input += synapse0xe1c5110();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::neuron0xe1c4e70() {
   double input = input0xe1c4e70();
   return (input * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe179f60() {
   return (neuron0xe1b1710()*1.82629);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1984b0() {
   return (neuron0xe1b1a50()*1.84683);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c3020() {
   return (neuron0xe1c2a20()*0.186935);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c33a0() {
   return (neuron0xe1b1710()*0.226544);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c33e0() {
   return (neuron0xe1b1a50()*0.51078);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c3420() {
   return (neuron0xe1c2a20()*-0.680665);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c37a0() {
   return (neuron0xe1b1710()*1.17962);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c37e0() {
   return (neuron0xe1b1a50()*-0.712485);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c3820() {
   return (neuron0xe1c2a20()*0.67144);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c3ba0() {
   return (neuron0xe1b1710()*-2.12037);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c3be0() {
   return (neuron0xe1b1a50()*0.931902);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c3c20() {
   return (neuron0xe1c2a20()*-1.17041);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c3fa0() {
   return (neuron0xe1b1710()*1.12044);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c3fe0() {
   return (neuron0xe1b1a50()*0.426054);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c4020() {
   return (neuron0xe1c2a20()*-0.720995);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c43a0() {
   return (neuron0xe1c2d70()*0.38029);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c43e0() {
   return (neuron0xe1c3060()*0.514339);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xdf4dc90() {
   return (neuron0xe1c3460()*-2.45269);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xdf4dcd0() {
   return (neuron0xe1c3860()*-0.000641104);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c4530() {
   return (neuron0xe1c3c60()*-1.40584);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c48b0() {
   return (neuron0xe1c2d70()*2.67081);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c48f0() {
   return (neuron0xe1c3060()*0.598299);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c4930() {
   return (neuron0xe1c3460()*-0.0713833);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c4970() {
   return (neuron0xe1c3860()*1.61522);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c49b0() {
   return (neuron0xe1c3c60()*-5.05839);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c4d30() {
   return (neuron0xe1c2d70()*0.995139);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c4d70() {
   return (neuron0xe1c3060()*-5.44356);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c4db0() {
   return (neuron0xe1c3460()*-2.16484);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c4df0() {
   return (neuron0xe1c3860()*2.25193);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c4e30() {
   return (neuron0xe1c3c60()*0.505518);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c5090() {
   return (neuron0xe1c4060()*-1.57928);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c50d0() {
   return (neuron0xe1c4570()*4.33307);
}

double MLP_Higgs_vs_Bkg_ZH125_comb::synapse0xe1c5110() {
   return (neuron0xe1c49f0()*-4.74407);
}

