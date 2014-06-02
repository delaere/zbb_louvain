#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.445235)/0.307413;
   input1 = (in1 - 0.487302)/0.29068;
   input2 = (in2 - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x148c6220();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::Value(int index, double* input) {
   input0 = (input[0] - 0.445235)/0.307413;
   input1 = (input[1] - 0.487302)/0.29068;
   input2 = (input[2] - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x148c6220();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::neuron0x148b35d0() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::neuron0x148b3910() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::neuron0x148c48e0() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::input0x148c4c30() {
   double input = 4.83359;
   input += synapse0x1487be20();
   input += synapse0x1489a370();
   input += synapse0x148c4ee0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::neuron0x148c4c30() {
   double input = input0x148c4c30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::input0x148c4f20() {
   double input = 1.1964;
   input += synapse0x148c5260();
   input += synapse0x148c52a0();
   input += synapse0x148c52e0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::neuron0x148c4f20() {
   double input = input0x148c4f20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::input0x148c5320() {
   double input = 0.810954;
   input += synapse0x148c5660();
   input += synapse0x148c56a0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::neuron0x148c5320() {
   double input = input0x148c5320();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::input0x148c56e0() {
   double input = 2.11072;
   input += synapse0x148c5a20();
   input += synapse0x148c5a60();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::neuron0x148c56e0() {
   double input = input0x148c56e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::input0x148c5aa0() {
   double input = -0.846577;
   input += synapse0x148c5de0();
   input += synapse0x148c5e20();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::neuron0x148c5aa0() {
   double input = input0x148c5aa0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::input0x148c5e60() {
   double input = 0.642514;
   input += synapse0x148c61a0();
   input += synapse0x148c61e0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::neuron0x148c5e60() {
   double input = input0x148c5e60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::input0x148c6220() {
   double input = 1.6725;
   input += synapse0x148c6440();
   input += synapse0x148c6480();
   input += synapse0x148c64c0();
   input += synapse0x14826550();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::neuron0x148c6220() {
   double input = input0x148c6220();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x1487be20() {
   return (neuron0x148b35d0()*-1.79157);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x1489a370() {
   return (neuron0x148b3910()*0.169991);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c4ee0() {
   return (neuron0x148c48e0()*-0.657211);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c5260() {
   return (neuron0x148b35d0()*1.93715);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c52a0() {
   return (neuron0x148b3910()*-0.214402);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c52e0() {
   return (neuron0x148c48e0()*0.212965);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c5660() {
   return (neuron0x148c4c30()*-0.784926);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c56a0() {
   return (neuron0x148c4f20()*6.2193);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c5a20() {
   return (neuron0x148c4c30()*5.86289);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c5a60() {
   return (neuron0x148c4f20()*-6.13878);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c5de0() {
   return (neuron0x148c4c30()*0.535953);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c5e20() {
   return (neuron0x148c4f20()*-2.43749);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c61a0() {
   return (neuron0x148c4c30()*-0.120776);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c61e0() {
   return (neuron0x148c4f20()*2.86315);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c6440() {
   return (neuron0x148c5320()*5.6212);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c6480() {
   return (neuron0x148c56e0()*-9.90454);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x148c64c0() {
   return (neuron0x148c5aa0()*-2.68929);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000::synapse0x14826550() {
   return (neuron0x148c5e60()*2.59564);
}

