#include "MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1) {
   input0 = (in0 - 0.491067)/0.220463;
   input1 = (in1 - 0.606248)/0.330761;
   switch(index) {
     case 0:
         return neuron0x41374c40();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 0.491067)/0.220463;
   input1 = (input[1] - 0.606248)/0.330761;
   switch(index) {
     case 0:
         return neuron0x41374c40();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x41371820() {
   return input0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x41371b60() {
   return input1;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x41371fd0() {
   double input = -0.144035;
   input += synapse0x41372280();
   input += synapse0x413722c0();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x41371fd0() {
   double input = input0x41371fd0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x41372300() {
   double input = 0.597115;
   input += synapse0x41372640();
   input += synapse0x41372680();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x41372300() {
   double input = input0x41372300();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x413726c0() {
   double input = -0.160709;
   input += synapse0x41372a00();
   input += synapse0x41372a40();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x413726c0() {
   double input = input0x413726c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x41372a80() {
   double input = 0.410107;
   input += synapse0x41372dc0();
   input += synapse0x41372e00();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x41372a80() {
   double input = input0x41372a80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x41372e40() {
   double input = 0.0559335;
   input += synapse0x41373180();
   input += synapse0x413731c0();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x41372e40() {
   double input = input0x41372e40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x41373200() {
   double input = -0.436213;
   input += synapse0x41373540();
   input += synapse0x41373580();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x41373200() {
   double input = input0x41373200();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x413735c0() {
   double input = 0.805806;
   input += synapse0x41373900();
   input += synapse0x41373940();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x413735c0() {
   double input = input0x413735c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x41373980() {
   double input = 0.491489;
   input += synapse0x41373cc0();
   input += synapse0x41373d00();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x41373980() {
   double input = input0x41373980();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x41373d40() {
   double input = 0.18814;
   input += synapse0x41374080();
   input += synapse0x4132f0e0();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x41373d40() {
   double input = input0x41373d40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x413741d0() {
   double input = -1.00563;
   input += synapse0x4132f120();
   input += synapse0x41374480();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x413741d0() {
   double input = input0x413741d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x413744c0() {
   double input = 0.114423;
   input += synapse0x41374800();
   input += synapse0x41374840();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x413744c0() {
   double input = input0x413744c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x41374880() {
   double input = -0.667612;
   input += synapse0x41374bc0();
   input += synapse0x41374c00();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x41374880() {
   double input = input0x41374880();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::input0x41374c40() {
   double input = -0.483024;
   input += synapse0x41374f80();
   input += synapse0x41374fc0();
   input += synapse0x41375000();
   input += synapse0x41375040();
   input += synapse0x41375080();
   input += synapse0x413750c0();
   input += synapse0x41375100();
   input += synapse0x41375140();
   input += synapse0x41375180();
   input += synapse0x4131e000();
   input += synapse0x4131e0e0();
   input += synapse0x413740c0();
   return input;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x41374c40() {
   double input = input0x41374c40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41372280() {
   return (neuron0x41371820()*0.0398217);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x413722c0() {
   return (neuron0x41371b60()*-0.537504);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41372640() {
   return (neuron0x41371820()*0.804773);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41372680() {
   return (neuron0x41371b60()*-0.348322);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41372a00() {
   return (neuron0x41371820()*-1.71855);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41372a40() {
   return (neuron0x41371b60()*1.73137);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41372dc0() {
   return (neuron0x41371820()*0.627778);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41372e00() {
   return (neuron0x41371b60()*-0.375924);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41373180() {
   return (neuron0x41371820()*0.107145);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x413731c0() {
   return (neuron0x41371b60()*-0.12927);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41373540() {
   return (neuron0x41371820()*-0.556725);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41373580() {
   return (neuron0x41371b60()*-0.064672);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41373900() {
   return (neuron0x41371820()*-0.0221106);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41373940() {
   return (neuron0x41371b60()*0.602384);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41373cc0() {
   return (neuron0x41371820()*-0.819521);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41373d00() {
   return (neuron0x41371b60()*0.374839);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41374080() {
   return (neuron0x41371820()*0.0436693);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x4132f0e0() {
   return (neuron0x41371b60()*0.547566);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x4132f120() {
   return (neuron0x41371820()*-0.044613);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41374480() {
   return (neuron0x41371b60()*-0.545472);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41374800() {
   return (neuron0x41371820()*0.15246);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41374840() {
   return (neuron0x41371b60()*-0.433231);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41374bc0() {
   return (neuron0x41371820()*-0.984465);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41374c00() {
   return (neuron0x41371b60()*0.540921);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41374f80() {
   return (neuron0x41371fd0()*-1.24548);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41374fc0() {
   return (neuron0x41372300()*1.08568);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41375000() {
   return (neuron0x413726c0()*-1.95304);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41375040() {
   return (neuron0x41372a80()*1.20831);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41375080() {
   return (neuron0x41372e40()*-0.198044);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x413750c0() {
   return (neuron0x41373200()*-0.609693);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41375100() {
   return (neuron0x413735c0()*1.79505);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41375140() {
   return (neuron0x41373980()*1.65336);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x41375180() {
   return (neuron0x41373d40()*1.01976);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x4131e000() {
   return (neuron0x413741d0()*-2.27322);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x4131e0e0() {
   return (neuron0x413744c0()*-1.46106);
}

double MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x413740c0() {
   return (neuron0x41374880()*-1.23503);
}

