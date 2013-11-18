#include "MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.2663)/0.885575;
   input1 = (in1 - 19.8397)/0.749967;
   input2 = (in2 - 20.7205)/1.37919;
   input3 = (in3 - 10.4438)/0.936439;
   switch(index) {
     case 0:
         return neuron0x3a9f04a0();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 19.2663)/0.885575;
   input1 = (input[1] - 19.8397)/0.749967;
   input2 = (input[2] - 20.7205)/1.37919;
   input3 = (input[3] - 10.4438)/0.936439;
   switch(index) {
     case 0:
         return neuron0x3a9f04a0();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ec2a0() {
   return input0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ec5e0() {
   return input1;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ec920() {
   return input2;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ecc60() {
   return input3;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9ed0d0() {
   double input = -1.22419;
   input += synapse0x3a969920();
   input += synapse0x3a9ed380();
   input += synapse0x3a9ed3c0();
   input += synapse0x3a9ed400();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ed0d0() {
   double input = input0x3a9ed0d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9ed440() {
   double input = -1.0744;
   input += synapse0x3a9ed780();
   input += synapse0x3a9ed7c0();
   input += synapse0x3a9ed800();
   input += synapse0x3a9ed840();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ed440() {
   double input = input0x3a9ed440();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9ed880() {
   double input = -0.0676176;
   input += synapse0x3a9edbc0();
   input += synapse0x3a9edc00();
   input += synapse0x3a9edc40();
   input += synapse0x3a9edc80();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ed880() {
   double input = input0x3a9ed880();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9edcc0() {
   double input = 0.474989;
   input += synapse0x3a9ee000();
   input += synapse0x3a9ee040();
   input += synapse0x3a9ee080();
   input += synapse0x3a9ee0c0();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9edcc0() {
   double input = input0x3a9edcc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9ee100() {
   double input = 0.779235;
   input += synapse0x3a9ee440();
   input += synapse0x3a969960();
   input += synapse0x3a9f4f10();
   input += synapse0x3a969520();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ee100() {
   double input = input0x3a9ee100();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9ee590() {
   double input = 0.696128;
   input += synapse0x3a9ee8d0();
   input += synapse0x3a9ee910();
   input += synapse0x3a9ee950();
   input += synapse0x3a9ee990();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ee590() {
   double input = input0x3a9ee590();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9ee9d0() {
   double input = -0.216513;
   input += synapse0x3a9eed10();
   input += synapse0x3a9eed50();
   input += synapse0x3a9eed90();
   input += synapse0x3a9eedd0();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ee9d0() {
   double input = input0x3a9ee9d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9eee10() {
   double input = 0.521203;
   input += synapse0x3a9ef150();
   input += synapse0x3a9ef190();
   input += synapse0x3a9ef1d0();
   input += synapse0x3a9ef210();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9eee10() {
   double input = input0x3a9eee10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9ef250() {
   double input = 0.168264;
   input += synapse0x3a9ef590();
   input += synapse0x3a969560();
   input += synapse0x3a9698d0();
   input += synapse0x3a9699b0();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ef250() {
   double input = input0x3a9ef250();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9ef7e0() {
   double input = 0.160099;
   input += synapse0x3a9efb20();
   input += synapse0x3a9efb60();
   input += synapse0x3a9efba0();
   input += synapse0x3a9efbe0();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9ef7e0() {
   double input = input0x3a9ef7e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9efc20() {
   double input = -0.212836;
   input += synapse0x3a9eff60();
   input += synapse0x3a9effa0();
   input += synapse0x3a9effe0();
   input += synapse0x3a9f0020();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9efc20() {
   double input = input0x3a9efc20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9f0060() {
   double input = 0.256782;
   input += synapse0x3a9f03a0();
   input += synapse0x3a9f03e0();
   input += synapse0x3a9f0420();
   input += synapse0x3a9f0460();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9f0060() {
   double input = input0x3a9f0060();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x3a9f04a0() {
   double input = 0.814346;
   input += synapse0x3a9f07e0();
   input += synapse0x3a9f0820();
   input += synapse0x3a9f0860();
   input += synapse0x3a9f08a0();
   input += synapse0x3a9f08e0();
   input += synapse0x3a9f0920();
   input += synapse0x3a9f0960();
   input += synapse0x3a9f09a0();
   input += synapse0x3a9f09e0();
   input += synapse0x3a9f0a20();
   input += synapse0x3a9f0a60();
   input += synapse0x3a9f0aa0();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a9f04a0() {
   double input = input0x3a9f04a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a969920() {
   return (neuron0x3a9ec2a0()*-2.3358);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ed380() {
   return (neuron0x3a9ec5e0()*1.78118);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ed3c0() {
   return (neuron0x3a9ec920()*-2.15553);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ed400() {
   return (neuron0x3a9ecc60()*1.62274);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ed780() {
   return (neuron0x3a9ec2a0()*-1.70767);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ed7c0() {
   return (neuron0x3a9ec5e0()*1.43062);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ed800() {
   return (neuron0x3a9ec920()*-1.81733);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ed840() {
   return (neuron0x3a9ecc60()*1.97876);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9edbc0() {
   return (neuron0x3a9ec2a0()*0.786361);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9edc00() {
   return (neuron0x3a9ec5e0()*0.187866);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9edc40() {
   return (neuron0x3a9ec920()*-0.101959);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9edc80() {
   return (neuron0x3a9ecc60()*-1.08329);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ee000() {
   return (neuron0x3a9ec2a0()*0.264152);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ee040() {
   return (neuron0x3a9ec5e0()*0.0377118);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ee080() {
   return (neuron0x3a9ec920()*-0.656572);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ee0c0() {
   return (neuron0x3a9ecc60()*-0.055897);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ee440() {
   return (neuron0x3a9ec2a0()*-1.3883);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a969960() {
   return (neuron0x3a9ec5e0()*0.471855);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f4f10() {
   return (neuron0x3a9ec920()*0.574879);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a969520() {
   return (neuron0x3a9ecc60()*1.80636);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ee8d0() {
   return (neuron0x3a9ec2a0()*-0.527318);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ee910() {
   return (neuron0x3a9ec5e0()*-0.270297);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ee950() {
   return (neuron0x3a9ec920()*0.232225);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ee990() {
   return (neuron0x3a9ecc60()*0.192438);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9eed10() {
   return (neuron0x3a9ec2a0()*-0.306298);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9eed50() {
   return (neuron0x3a9ec5e0()*0.122609);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9eed90() {
   return (neuron0x3a9ec920()*-0.028788);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9eedd0() {
   return (neuron0x3a9ecc60()*0.847179);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ef150() {
   return (neuron0x3a9ec2a0()*1.02101);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ef190() {
   return (neuron0x3a9ec5e0()*-0.418922);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ef1d0() {
   return (neuron0x3a9ec920()*0.0328314);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ef210() {
   return (neuron0x3a9ecc60()*-0.781338);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9ef590() {
   return (neuron0x3a9ec2a0()*-0.610183);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a969560() {
   return (neuron0x3a9ec5e0()*-0.276835);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9698d0() {
   return (neuron0x3a9ec920()*0.146308);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9699b0() {
   return (neuron0x3a9ecc60()*0.50681);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9efb20() {
   return (neuron0x3a9ec2a0()*0.855684);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9efb60() {
   return (neuron0x3a9ec5e0()*0.133946);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9efba0() {
   return (neuron0x3a9ec920()*-0.858929);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9efbe0() {
   return (neuron0x3a9ecc60()*-0.705682);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9eff60() {
   return (neuron0x3a9ec2a0()*-0.826402);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9effa0() {
   return (neuron0x3a9ec5e0()*0.927211);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9effe0() {
   return (neuron0x3a9ec920()*-0.263607);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f0020() {
   return (neuron0x3a9ecc60()*0.607531);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f03a0() {
   return (neuron0x3a9ec2a0()*0.363037);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f03e0() {
   return (neuron0x3a9ec5e0()*-0.152221);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f0420() {
   return (neuron0x3a9ec920()*-0.450761);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f0460() {
   return (neuron0x3a9ecc60()*-0.500271);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f07e0() {
   return (neuron0x3a9ed0d0()*-1.16953);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f0820() {
   return (neuron0x3a9ed440()*-1.73841);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f0860() {
   return (neuron0x3a9ed880()*0.116625);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f08a0() {
   return (neuron0x3a9edcc0()*0.614163);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f08e0() {
   return (neuron0x3a9ee100()*-0.691127);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f0920() {
   return (neuron0x3a9ee590()*-1.37224);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f0960() {
   return (neuron0x3a9ee9d0()*-0.758421);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f09a0() {
   return (neuron0x3a9eee10()*-0.347869);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f09e0() {
   return (neuron0x3a9ef250()*-0.951586);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f0a20() {
   return (neuron0x3a9ef7e0()*0.274388);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f0a60() {
   return (neuron0x3a9efc20()*1.44305);
}

double MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a9f0aa0() {
   return (neuron0x3a9f0060()*2.05229);
}

