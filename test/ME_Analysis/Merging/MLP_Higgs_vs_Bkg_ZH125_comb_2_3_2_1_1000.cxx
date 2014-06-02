#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.445235)/0.307413;
   input1 = (in1 - 0.487302)/0.29068;
   input2 = (in2 - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x7a87a10();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::Value(int index, double* input) {
   input0 = (input[0] - 0.445235)/0.307413;
   input1 = (input[1] - 0.487302)/0.29068;
   input2 = (input[2] - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x7a87a10();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a74530() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a74870() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a85840() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::input0x7a85b90() {
   double input = -0.259654;
   input += synapse0x7a3cd00();
   input += synapse0x7a5b290();
   input += synapse0x7a85e40();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a85b90() {
   double input = input0x7a85b90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::input0x7a85e80() {
   double input = -0.905738;
   input += synapse0x7a861c0();
   input += synapse0x7a86200();
   input += synapse0x7a86240();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a85e80() {
   double input = input0x7a85e80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::input0x7a86280() {
   double input = -0.193664;
   input += synapse0x7a865c0();
   input += synapse0x7a86600();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a86280() {
   double input = input0x7a86280();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::input0x7a86640() {
   double input = -0.750552;
   input += synapse0x7a86980();
   input += synapse0x7a869c0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a86640() {
   double input = input0x7a86640();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::input0x7a86a00() {
   double input = 0.0260944;
   input += synapse0x7a86d40();
   input += synapse0x7a86d80();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a86a00() {
   double input = input0x7a86a00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::input0x7a86dc0() {
   double input = -1.60122;
   input += synapse0x7a87100();
   input += synapse0x7a87140();
   input += synapse0x7a87180();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a86dc0() {
   double input = input0x7a86dc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::input0x7a871c0() {
   double input = 0.698238;
   input += synapse0x7a87500();
   input += synapse0x7a87540();
   input += synapse0x79e74a0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a871c0() {
   double input = input0x7a871c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::input0x7a87690() {
   double input = -2.71241;
   input += synapse0x79e74e0();
   input += synapse0x7a879d0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a87690() {
   double input = input0x7a87690();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::input0x7a87a10() {
   double input = 11.2457;
   input += synapse0x7a85a60();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::neuron0x7a87a10() {
   double input = input0x7a87a10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a3cd00() {
   return (neuron0x7a74530()*0.134396);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a5b290() {
   return (neuron0x7a74870()*0.148151);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a85e40() {
   return (neuron0x7a85840()*-0.251209);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a861c0() {
   return (neuron0x7a74530()*0.0558178);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a86200() {
   return (neuron0x7a74870()*0.0984276);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a86240() {
   return (neuron0x7a85840()*-0.163423);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a865c0() {
   return (neuron0x7a85b90()*-2.15285);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a86600() {
   return (neuron0x7a85e80()*3.78466);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a86980() {
   return (neuron0x7a85b90()*-1.92636);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a869c0() {
   return (neuron0x7a85e80()*4.33177);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a86d40() {
   return (neuron0x7a85b90()*2.41261);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a86d80() {
   return (neuron0x7a85e80()*-4.11169);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a87100() {
   return (neuron0x7a86280()*3.33367);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a87140() {
   return (neuron0x7a86640()*4.87019);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a87180() {
   return (neuron0x7a86a00()*-4.22842);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a87500() {
   return (neuron0x7a86280()*-3.08046);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a87540() {
   return (neuron0x7a86640()*-2.22503);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x79e74a0() {
   return (neuron0x7a86a00()*3.43274);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x79e74e0() {
   return (neuron0x7a86dc0()*10.5679);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a879d0() {
   return (neuron0x7a871c0()*-5.96202);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000::synapse0x7a85a60() {
   return (neuron0x7a87690()*-23.9937);
}

