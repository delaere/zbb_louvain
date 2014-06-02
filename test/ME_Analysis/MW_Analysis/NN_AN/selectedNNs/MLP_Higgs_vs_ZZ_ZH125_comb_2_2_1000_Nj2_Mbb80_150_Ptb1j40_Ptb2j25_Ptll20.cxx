#include "MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.0522)/1.27673;
   input1 = (in1 - 10.8558)/1.04163;
   input2 = (in2 - 24.4862)/1.13705;
   input3 = (in3 - 12.7271)/0.888688;
   switch(index) {
     case 0:
         return neuron0x19c9b9e0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 21.0522)/1.27673;
   input1 = (input[1] - 10.8558)/1.04163;
   input2 = (input[2] - 24.4862)/1.13705;
   input3 = (input[3] - 12.7271)/0.888688;
   switch(index) {
     case 0:
         return neuron0x19c9b9e0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x19c99c80() {
   return input0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x19c99fc0() {
   return input1;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x19c9a300() {
   return input2;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x19c9a640() {
   return input3;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x19c9aab0() {
   double input = -0.660511;
   input += synapse0x19ca2950();
   input += synapse0x19c9ad60();
   input += synapse0x19c9ada0();
   input += synapse0x19c9ade0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x19c9aab0() {
   double input = input0x19c9aab0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x19c9ae20() {
   double input = 4.71466;
   input += synapse0x19c9b160();
   input += synapse0x19c9b1a0();
   input += synapse0x19c9b1e0();
   input += synapse0x19c9b220();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x19c9ae20() {
   double input = input0x19c9ae20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x19c9b260() {
   double input = -0.402894;
   input += synapse0x19c9b5a0();
   input += synapse0x19c9b5e0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x19c9b260() {
   double input = input0x19c9b260();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x19c9b620() {
   double input = 7.88185;
   input += synapse0x19c9b960();
   input += synapse0x19c9b9a0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x19c9b620() {
   double input = input0x19c9b620();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x19c9b9e0() {
   double input = 2.27311;
   input += synapse0x19c9bd20();
   input += synapse0x19c9bd60();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x19c9b9e0() {
   double input = input0x19c9b9e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19ca2950() {
   return (neuron0x19c99c80()*0.461181);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9ad60() {
   return (neuron0x19c99fc0()*-0.0647124);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9ada0() {
   return (neuron0x19c9a300()*-0.0595913);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9ade0() {
   return (neuron0x19c9a640()*-0.301952);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9b160() {
   return (neuron0x19c99c80()*-1.55528);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9b1a0() {
   return (neuron0x19c99fc0()*5.17936);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9b1e0() {
   return (neuron0x19c9a300()*-2.33392);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9b220() {
   return (neuron0x19c9a640()*-0.922679);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9b5a0() {
   return (neuron0x19c9aab0()*3.98986);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9b5e0() {
   return (neuron0x19c9ae20()*1.41217);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9b960() {
   return (neuron0x19c9aab0()*-9.4781);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9b9a0() {
   return (neuron0x19c9ae20()*-2.06902);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9bd20() {
   return (neuron0x19c9b260()*9.75169);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x19c9bd60() {
   return (neuron0x19c9b620()*-11.3571);
}

