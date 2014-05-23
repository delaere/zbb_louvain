#include "MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.4315)/3.22594;
   input1 = (in1 - 24.3204)/1.258;
   input2 = (in2 - 12.6542)/1.62116;
   switch(index) {
     case 0:
         return neuron0x145d1eb0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 22.4315)/3.22594;
   input1 = (input[1] - 24.3204)/1.258;
   input2 = (input[2] - 12.6542)/1.62116;
   switch(index) {
     case 0:
         return neuron0x145d1eb0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145ce500() {
   return input0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145ce840() {
   return input1;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145ceb80() {
   return input2;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145ceff0() {
   double input = -0.21842;
   input += synapse0x145d7190();
   input += synapse0x10201270();
   input += synapse0x145cf2a0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145ceff0() {
   double input = input0x145ceff0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145cf2e0() {
   double input = 0.234063;
   input += synapse0x145cf620();
   input += synapse0x145cf660();
   input += synapse0x145cf6a0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145cf2e0() {
   double input = input0x145cf2e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145cf6e0() {
   double input = 1.94767;
   input += synapse0x145cfa20();
   input += synapse0x145cfa60();
   input += synapse0x145cfaa0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145cf6e0() {
   double input = input0x145cf6e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145cfae0() {
   double input = -0.936175;
   input += synapse0x145cfe20();
   input += synapse0x145cfe60();
   input += synapse0x145cfea0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145cfae0() {
   double input = input0x145cfae0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145cfee0() {
   double input = -0.698;
   input += synapse0x145d0220();
   input += synapse0x145d0260();
   input += synapse0x145d02a0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145cfee0() {
   double input = input0x145cfee0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145d02e0() {
   double input = -0.0212373;
   input += synapse0x145d0620();
   input += synapse0x145d0660();
   input += synapse0x102012b0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145d02e0() {
   double input = input0x145d02e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145d07b0() {
   double input = -0.225922;
   input += synapse0x145d0a60();
   input += synapse0x145d0aa0();
   input += synapse0x145d0ae0();
   input += synapse0x145d0b20();
   input += synapse0x145d0b60();
   input += synapse0x145d0ba0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145d07b0() {
   double input = input0x145d07b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145d0be0() {
   double input = 0.00277653;
   input += synapse0x145d0f20();
   input += synapse0x145d0f60();
   input += synapse0x145d0fa0();
   input += synapse0x145d0fe0();
   input += synapse0x145d1020();
   input += synapse0x145d1060();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145d0be0() {
   double input = input0x145d0be0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145d10a0() {
   double input = 0.141791;
   input += synapse0x145d13e0();
   input += synapse0x145d1420();
   input += synapse0x145d1460();
   input += synapse0x145d7140();
   input += synapse0x141969f0();
   input += synapse0x10201300();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145d10a0() {
   double input = input0x145d10a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145d16b0() {
   double input = -3.06108;
   input += synapse0x145d19f0();
   input += synapse0x145d1a30();
   input += synapse0x145d1a70();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145d16b0() {
   double input = input0x145d16b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145d1ab0() {
   double input = 1.22665;
   input += synapse0x145d1df0();
   input += synapse0x145d1e30();
   input += synapse0x145d1e70();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145d1ab0() {
   double input = input0x145d1ab0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x145d1eb0() {
   double input = -2.75751;
   input += synapse0x145d21f0();
   input += synapse0x145d2230();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x145d1eb0() {
   double input = input0x145d1eb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d7190() {
   return (neuron0x145ce500()*-1.26606);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x10201270() {
   return (neuron0x145ce840()*-0.317126);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145cf2a0() {
   return (neuron0x145ceb80()*0.510375);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145cf620() {
   return (neuron0x145ce500()*0.514202);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145cf660() {
   return (neuron0x145ce840()*0.29468);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145cf6a0() {
   return (neuron0x145ceb80()*-0.268197);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145cfa20() {
   return (neuron0x145ce500()*1.4078);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145cfa60() {
   return (neuron0x145ce840()*-1.10335);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145cfaa0() {
   return (neuron0x145ceb80()*0.509504);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145cfe20() {
   return (neuron0x145ce500()*-2.00457);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145cfe60() {
   return (neuron0x145ce840()*0.810179);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145cfea0() {
   return (neuron0x145ceb80()*0.310367);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0220() {
   return (neuron0x145ce500()*1.54575);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0260() {
   return (neuron0x145ce840()*-0.821963);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d02a0() {
   return (neuron0x145ceb80()*-1.65624);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0620() {
   return (neuron0x145ce500()*0.471635);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0660() {
   return (neuron0x145ce840()*-2.52576);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x102012b0() {
   return (neuron0x145ceb80()*1.6523);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0a60() {
   return (neuron0x145ceff0()*0.274968);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0aa0() {
   return (neuron0x145cf2e0()*-0.9211);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0ae0() {
   return (neuron0x145cf6e0()*-1.36777);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0b20() {
   return (neuron0x145cfae0()*0.963055);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0b60() {
   return (neuron0x145cfee0()*-1.07571);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0ba0() {
   return (neuron0x145d02e0()*0.88895);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0f20() {
   return (neuron0x145ceff0()*-0.507435);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0f60() {
   return (neuron0x145cf2e0()*0.244033);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0fa0() {
   return (neuron0x145cf6e0()*1.36259);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d0fe0() {
   return (neuron0x145cfae0()*-1.23828);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d1020() {
   return (neuron0x145cfee0()*0.621996);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d1060() {
   return (neuron0x145d02e0()*-1.06103);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d13e0() {
   return (neuron0x145ceff0()*-0.349201);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d1420() {
   return (neuron0x145cf2e0()*-0.421742);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d1460() {
   return (neuron0x145cf6e0()*1.27432);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d7140() {
   return (neuron0x145cfae0()*-1.9526);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x141969f0() {
   return (neuron0x145cfee0()*0.740902);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x10201300() {
   return (neuron0x145d02e0()*-1.38474);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d19f0() {
   return (neuron0x145d07b0()*-1.42833);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d1a30() {
   return (neuron0x145d0be0()*3.75747);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d1a70() {
   return (neuron0x145d10a0()*3.00697);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d1df0() {
   return (neuron0x145d07b0()*0.598386);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d1e30() {
   return (neuron0x145d0be0()*-2.48567);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d1e70() {
   return (neuron0x145d10a0()*-2.32495);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d21f0() {
   return (neuron0x145d16b0()*8.88343);
}

double MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x145d2230() {
   return (neuron0x145d1ab0()*-3.72635);
}

