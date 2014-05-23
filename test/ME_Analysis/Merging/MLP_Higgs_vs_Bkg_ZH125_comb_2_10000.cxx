#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_10000.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.445235)/0.307413;
   input1 = (in1 - 0.487302)/0.29068;
   input2 = (in2 - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x5cfe1e0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::Value(int index, double* input) {
   input0 = (input[0] - 0.445235)/0.307413;
   input1 = (input[1] - 0.487302)/0.29068;
   input2 = (input[2] - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x5cfe1e0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::neuron0x5cec490() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::neuron0x5cec7d0() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::neuron0x5cfd7a0() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::input0x5cfdaf0() {
   double input = -0.0143284;
   input += synapse0x5cb4ce0();
   input += synapse0x5cd3230();
   input += synapse0x5cfdda0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::neuron0x5cfdaf0() {
   double input = input0x5cfdaf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::input0x5cfdde0() {
   double input = 0.826485;
   input += synapse0x5cfe120();
   input += synapse0x5cfe160();
   input += synapse0x5cfe1a0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::neuron0x5cfdde0() {
   double input = input0x5cfdde0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::input0x5cfe1e0() {
   double input = -13.4646;
   input += synapse0x5cfe400();
   input += synapse0x5cfe440();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::neuron0x5cfe1e0() {
   double input = input0x5cfe1e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::synapse0x5cb4ce0() {
   return (neuron0x5cec490()*0.181738);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::synapse0x5cd3230() {
   return (neuron0x5cec7d0()*0.0361336);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::synapse0x5cfdda0() {
   return (neuron0x5cfd7a0()*0.0324666);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::synapse0x5cfe120() {
   return (neuron0x5cec490()*10.5766);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::synapse0x5cfe160() {
   return (neuron0x5cec7d0()*-11.0485);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::synapse0x5cfe1a0() {
   return (neuron0x5cfd7a0()*1.36167);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::synapse0x5cfe400() {
   return (neuron0x5cfdaf0()*25.7712);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_10000::synapse0x5cfe440() {
   return (neuron0x5cfdde0()*0.891194);
}

