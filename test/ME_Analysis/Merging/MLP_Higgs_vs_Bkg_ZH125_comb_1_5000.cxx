#include "MLP_Higgs_vs_Bkg_ZH125_comb_1_5000.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.445235)/0.307413;
   input1 = (in1 - 0.487302)/0.29068;
   input2 = (in2 - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0xfc104b0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::Value(int index, double* input) {
   input0 = (input[0] - 0.445235)/0.307413;
   input1 = (input[1] - 0.487302)/0.29068;
   input2 = (input[2] - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0xfc104b0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::neuron0xfbfeb20() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::neuron0xfbfee60() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::neuron0xfc0fe30() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::input0xfc10180() {
   double input = -4.42997;
   input += synapse0xfbc6f30();
   input += synapse0xfc10430();
   input += synapse0xfc10470();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::neuron0xfc10180() {
   double input = input0xfc10180();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::input0xfc104b0() {
   double input = -5.20712;
   input += synapse0xfc106d0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::neuron0xfc104b0() {
   double input = input0xfc104b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::synapse0xfbc6f30() {
   return (neuron0xfbfeb20()*0.16128);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::synapse0xfc10430() {
   return (neuron0xfbfee60()*0.0499317);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::synapse0xfc10470() {
   return (neuron0xfc0fe30()*0.141556);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_1_5000::synapse0xfc106d0() {
   return (neuron0xfc10180()*397.746);
}

