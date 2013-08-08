#include "MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.0514)/2.02154;
   input1 = (in1 - 20.8812)/1.67352;
   input2 = (in2 - 10.5466)/1.32501;
   switch(index) {
     case 0:
         return neuron0x32d403e0();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 22.0514)/2.02154;
   input1 = (input[1] - 20.8812)/1.67352;
   input2 = (input[2] - 10.5466)/1.32501;
   switch(index) {
     case 0:
         return neuron0x32d403e0();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x32d3f2d0() {
   return input0;
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x32d3f580() {
   return input1;
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x32d3f8c0() {
   return input2;
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x32d3fd30() {
   double input = -4.98325;
   input += synapse0x32cd3100();
   input += synapse0x32d2e740();
   input += synapse0x32cd3140();
   return input;
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x32d3fd30() {
   double input = input0x32d3fd30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x32d3ffe0() {
   double input = -0.0845866;
   input += synapse0x32d40320();
   input += synapse0x32d40360();
   input += synapse0x32d403a0();
   return input;
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x32d3ffe0() {
   double input = input0x32d3ffe0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x32d403e0() {
   double input = 5.81714;
   input += synapse0x32d3fc00();
   input += synapse0x32d3fcd0();
   return input;
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x32d403e0() {
   double input = input0x32d403e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x32cd3100() {
   return (neuron0x32d3f2d0()*0.399729);
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x32d2e740() {
   return (neuron0x32d3f580()*0.357057);
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x32cd3140() {
   return (neuron0x32d3f8c0()*-0.991288);
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x32d40320() {
   return (neuron0x32d3f2d0()*-1.61681);
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x32d40360() {
   return (neuron0x32d3f580()*-0.0396754);
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x32d403a0() {
   return (neuron0x32d3f8c0()*1.18689);
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x32d3fc00() {
   return (neuron0x32d3fd30()*-10.2156);
}

double MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x32d3fcd0() {
   return (neuron0x32d3ffe0()*-9.94511);
}

