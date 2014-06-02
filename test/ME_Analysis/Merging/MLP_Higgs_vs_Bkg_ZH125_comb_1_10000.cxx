#include "MLP_Higgs_vs_Bkg_ZH125_comb_1_10000.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.445235)/0.307413;
   input1 = (in1 - 0.487302)/0.29068;
   input2 = (in2 - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x14e09de0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::Value(int index, double* input) {
   input0 = (input[0] - 0.445235)/0.307413;
   input1 = (input[1] - 0.487302)/0.29068;
   input2 = (input[2] - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x14e09de0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::neuron0x14df8490() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::neuron0x14df87d0() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::neuron0x14e097a0() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::input0x14e09af0() {
   double input = -1.00626;
   input += synapse0x14dc0ce0();
   input += synapse0x14ddf230();
   input += synapse0x14e09da0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::neuron0x14e09af0() {
   double input = input0x14e09af0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::input0x14e09de0() {
   double input = -21.1476;
   input += synapse0x14e0a000();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::neuron0x14e09de0() {
   double input = input0x14e09de0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::synapse0x14dc0ce0() {
   return (neuron0x14df8490()*0.104863);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::synapse0x14ddf230() {
   return (neuron0x14df87d0()*-0.0160283);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::synapse0x14e09da0() {
   return (neuron0x14e097a0()*0.0192012);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_10000::synapse0x14e0a000() {
   return (neuron0x14e09af0()*78.0741);
}

