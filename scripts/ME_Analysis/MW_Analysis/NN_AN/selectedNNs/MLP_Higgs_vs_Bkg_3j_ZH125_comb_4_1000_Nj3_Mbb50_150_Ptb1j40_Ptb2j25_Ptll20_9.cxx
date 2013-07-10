#include "MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.467176)/0.243159;
   input1 = (in1 - 0.52708)/0.296356;
   input2 = (in2 - 0.534793)/0.314261;
   switch(index) {
     case 0:
         return neuron0x2841f170();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::Value(int index, double* input) {
   input0 = (input[0] - 0.467176)/0.243159;
   input1 = (input[1] - 0.52708)/0.296356;
   input2 = (input[2] - 0.534793)/0.314261;
   switch(index) {
     case 0:
         return neuron0x2841f170();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::neuron0x2841d750() {
   return input0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::neuron0x2841da90() {
   return input1;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::neuron0x2841ddd0() {
   return input2;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::input0x2841e240() {
   double input = 5.94125;
   input += synapse0x283c2830();
   input += synapse0x2841e4f0();
   input += synapse0x2841e530();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::neuron0x2841e240() {
   double input = input0x2841e240();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::input0x2841e570() {
   double input = 3.39967;
   input += synapse0x2841e8b0();
   input += synapse0x2841e8f0();
   input += synapse0x2841e930();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::neuron0x2841e570() {
   double input = input0x2841e570();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::input0x2841e970() {
   double input = -1.50806;
   input += synapse0x2841ecb0();
   input += synapse0x2841ecf0();
   input += synapse0x2841ed30();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::neuron0x2841e970() {
   double input = input0x2841e970();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::input0x2841ed70() {
   double input = 1.73542;
   input += synapse0x2841f0b0();
   input += synapse0x2841f0f0();
   input += synapse0x2841f130();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::neuron0x2841ed70() {
   double input = input0x2841ed70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::input0x2841f170() {
   double input = -4.27819;
   input += synapse0x2841f4b0();
   input += synapse0x2841f4f0();
   input += synapse0x2841f530();
   input += synapse0x2841f570();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::neuron0x2841f170() {
   double input = input0x2841f170();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x283c2830() {
   return (neuron0x2841d750()*-0.927533);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841e4f0() {
   return (neuron0x2841da90()*-1.91728);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841e530() {
   return (neuron0x2841ddd0()*-0.442914);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841e8b0() {
   return (neuron0x2841d750()*1.01507);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841e8f0() {
   return (neuron0x2841da90()*0.819626);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841e930() {
   return (neuron0x2841ddd0()*-0.474331);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841ecb0() {
   return (neuron0x2841d750()*-1.779);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841ecf0() {
   return (neuron0x2841da90()*2.50767);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841ed30() {
   return (neuron0x2841ddd0()*0.910969);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841f0b0() {
   return (neuron0x2841d750()*0.27185);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841f0f0() {
   return (neuron0x2841da90()*-0.18447);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841f130() {
   return (neuron0x2841ddd0()*0.876041);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841f4b0() {
   return (neuron0x2841e240()*-7.43548);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841f4f0() {
   return (neuron0x2841e570()*8.52666);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841f530() {
   return (neuron0x2841e970()*-1.26515);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9::synapse0x2841f570() {
   return (neuron0x2841ed70()*4.76686);
}

