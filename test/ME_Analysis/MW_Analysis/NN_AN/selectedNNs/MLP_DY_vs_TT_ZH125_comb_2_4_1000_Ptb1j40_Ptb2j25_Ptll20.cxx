#include "MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 20.0771)/1.45611;
   input1 = (in1 - 20.9022)/1.93203;
   input2 = (in2 - 22.264)/3.23887;
   switch(index) {
     case 0:
         return neuron0x174e4f50();
     default:
         return 0.;
   }
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 20.0771)/1.45611;
   input1 = (input[1] - 20.9022)/1.93203;
   input2 = (input[2] - 22.264)/3.23887;
   switch(index) {
     case 0:
         return neuron0x174e4f50();
     default:
         return 0.;
   }
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::neuron0x17488210() {
   return input0;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::neuron0x174e31f0() {
   return input1;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::neuron0x174e3530() {
   return input2;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::input0x174e39a0() {
   double input = 0.443761;
   input += synapse0x1747a120();
   input += synapse0x17488120();
   input += synapse0x174884c0();
   return input;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::neuron0x174e39a0() {
   double input = input0x174e39a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::input0x174e3c50() {
   double input = -0.743688;
   input += synapse0x174e3f90();
   input += synapse0x174e3fd0();
   input += synapse0x174e4010();
   return input;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::neuron0x174e3c50() {
   double input = input0x174e3c50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::input0x174e4050() {
   double input = 0.151966;
   input += synapse0x174e4390();
   input += synapse0x174e43d0();
   return input;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::neuron0x174e4050() {
   double input = input0x174e4050();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::input0x174e4410() {
   double input = -0.956538;
   input += synapse0x174e4750();
   input += synapse0x174e4790();
   return input;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::neuron0x174e4410() {
   double input = input0x174e4410();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::input0x174e47d0() {
   double input = 6.18471;
   input += synapse0x174e4b10();
   input += synapse0x174e4b50();
   return input;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::neuron0x174e47d0() {
   double input = input0x174e47d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::input0x174e4b90() {
   double input = -1.77205;
   input += synapse0x174e4ed0();
   input += synapse0x174e4f10();
   return input;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::neuron0x174e4b90() {
   double input = input0x174e4b90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::input0x174e4f50() {
   double input = -3.07214;
   input += synapse0x174e3870();
   input += synapse0x174e5290();
   input += synapse0x174e52d0();
   input += synapse0x17478310();
   return input;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::neuron0x174e4f50() {
   double input = input0x174e4f50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x1747a120() {
   return (neuron0x17488210()*-0.401226);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x17488120() {
   return (neuron0x174e31f0()*-0.32369);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174884c0() {
   return (neuron0x174e3530()*0.180795);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e3f90() {
   return (neuron0x17488210()*-0.0260718);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e3fd0() {
   return (neuron0x174e31f0()*-0.244625);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e4010() {
   return (neuron0x174e3530()*2.73986);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e4390() {
   return (neuron0x174e39a0()*1.92033);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e43d0() {
   return (neuron0x174e3c50()*2.33217);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e4750() {
   return (neuron0x174e39a0()*3.6486);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e4790() {
   return (neuron0x174e3c50()*3.41052);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e4b10() {
   return (neuron0x174e39a0()*-7.975);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e4b50() {
   return (neuron0x174e3c50()*-4.67028);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e4ed0() {
   return (neuron0x174e39a0()*4.69354);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e4f10() {
   return (neuron0x174e3c50()*3.87672);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e3870() {
   return (neuron0x174e4050()*0.373968);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e5290() {
   return (neuron0x174e4410()*2.85367);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x174e52d0() {
   return (neuron0x174e47d0()*-6.58874);
}

double MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20::synapse0x17478310() {
   return (neuron0x174e4b90()*3.96429);
}

