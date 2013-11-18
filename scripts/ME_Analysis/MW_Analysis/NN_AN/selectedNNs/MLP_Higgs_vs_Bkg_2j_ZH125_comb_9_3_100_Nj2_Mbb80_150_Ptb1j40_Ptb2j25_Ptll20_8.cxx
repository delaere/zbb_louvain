#include "MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.500017)/0.25242;
   input1 = (in1 - 0.592179)/0.338539;
   input2 = (in2 - 0.679468)/0.281065;
   switch(index) {
     case 0:
         return neuron0x18c5f7b0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::Value(int index, double* input) {
   input0 = (input[0] - 0.500017)/0.25242;
   input1 = (input[1] - 0.592179)/0.338539;
   input2 = (input[2] - 0.679468)/0.281065;
   switch(index) {
     case 0:
         return neuron0x18c5f7b0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5b780() {
   return input0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5bac0() {
   return input1;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5be00() {
   return input2;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5c270() {
   double input = 1.83652;
   input += synapse0x18c00920();
   input += synapse0x18c5c520();
   input += synapse0x18c5c560();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5c270() {
   double input = input0x18c5c270();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5c5a0() {
   double input = -0.065199;
   input += synapse0x18c5c8e0();
   input += synapse0x18c5c920();
   input += synapse0x18c5c960();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5c5a0() {
   double input = input0x18c5c5a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5c9a0() {
   double input = -0.15171;
   input += synapse0x18c5cce0();
   input += synapse0x18c5cd20();
   input += synapse0x18c5cd60();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5c9a0() {
   double input = input0x18c5c9a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5cda0() {
   double input = -0.583318;
   input += synapse0x18c5d0e0();
   input += synapse0x18c5d120();
   input += synapse0x18c5d160();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5cda0() {
   double input = input0x18c5cda0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5d1a0() {
   double input = 2.5169;
   input += synapse0x18c5d4e0();
   input += synapse0x18c5d520();
   input += synapse0x18c5d560();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5d1a0() {
   double input = input0x18c5d1a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5d5a0() {
   double input = 1.34963;
   input += synapse0x18c5d8e0();
   input += synapse0x18c5d920();
   input += synapse0x18c00960();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5d5a0() {
   double input = input0x18c5d5a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5da70() {
   double input = 0.847552;
   input += synapse0x18c5dd20();
   input += synapse0x18c5dd60();
   input += synapse0x18c5dda0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5da70() {
   double input = input0x18c5da70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5dde0() {
   double input = 0.308146;
   input += synapse0x18c5e120();
   input += synapse0x18c5e160();
   input += synapse0x18c5e1a0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5dde0() {
   double input = input0x18c5dde0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5e1e0() {
   double input = 0.543133;
   input += synapse0x18c5e520();
   input += synapse0x18c5e560();
   input += synapse0x18c5e5a0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5e1e0() {
   double input = input0x18c5e1e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5e5e0() {
   double input = -0.243548;
   input += synapse0x18c5e920();
   input += synapse0x18c5e960();
   input += synapse0x18c5e9a0();
   input += synapse0x18c5e9e0();
   input += synapse0x18c5ea20();
   input += synapse0x18c5ea60();
   input += synapse0x18bf0f60();
   input += synapse0x18bf1040();
   input += synapse0x18bf1080();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5e5e0() {
   double input = input0x18c5e5e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5ecb0() {
   double input = 1.5258;
   input += synapse0x18c5eff0();
   input += synapse0x18c5f030();
   input += synapse0x18c5f070();
   input += synapse0x18c5f0b0();
   input += synapse0x18c5f0f0();
   input += synapse0x18c5f130();
   input += synapse0x18c5f170();
   input += synapse0x18c5f1b0();
   input += synapse0x18c5f1f0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5ecb0() {
   double input = input0x18c5ecb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5f230() {
   double input = 0.148596;
   input += synapse0x18c5f570();
   input += synapse0x18c5f5b0();
   input += synapse0x18c5f5f0();
   input += synapse0x18c5f630();
   input += synapse0x18c5f670();
   input += synapse0x18c5f6b0();
   input += synapse0x18c5f6f0();
   input += synapse0x18c5f730();
   input += synapse0x18c5f770();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5f230() {
   double input = input0x18c5f230();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::input0x18c5f7b0() {
   double input = 4.76233;
   input += synapse0x18c009e0();
   input += synapse0x18c5faf0();
   input += synapse0x18c5fb30();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::neuron0x18c5f7b0() {
   double input = input0x18c5f7b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c00920() {
   return (neuron0x18c5b780()*-2.48711);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5c520() {
   return (neuron0x18c5bac0()*0.752282);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5c560() {
   return (neuron0x18c5be00()*-0.200274);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5c8e0() {
   return (neuron0x18c5b780()*1.80406);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5c920() {
   return (neuron0x18c5bac0()*0.953523);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5c960() {
   return (neuron0x18c5be00()*-0.0458923);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5cce0() {
   return (neuron0x18c5b780()*-1.88959);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5cd20() {
   return (neuron0x18c5bac0()*-0.0341409);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5cd60() {
   return (neuron0x18c5be00()*-0.600231);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5d0e0() {
   return (neuron0x18c5b780()*-0.918071);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5d120() {
   return (neuron0x18c5bac0()*-0.316664);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5d160() {
   return (neuron0x18c5be00()*0.455631);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5d4e0() {
   return (neuron0x18c5b780()*0.636445);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5d520() {
   return (neuron0x18c5bac0()*0.674723);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5d560() {
   return (neuron0x18c5be00()*-0.493185);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5d8e0() {
   return (neuron0x18c5b780()*2.08925);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5d920() {
   return (neuron0x18c5bac0()*-1.45334);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c00960() {
   return (neuron0x18c5be00()*0.912624);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5dd20() {
   return (neuron0x18c5b780()*-1.48984);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5dd60() {
   return (neuron0x18c5bac0()*-3.44398);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5dda0() {
   return (neuron0x18c5be00()*-0.174005);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5e120() {
   return (neuron0x18c5b780()*1.1768);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5e160() {
   return (neuron0x18c5bac0()*0.362673);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5e1a0() {
   return (neuron0x18c5be00()*0.929067);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5e520() {
   return (neuron0x18c5b780()*0.283246);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5e560() {
   return (neuron0x18c5bac0()*-0.571649);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5e5a0() {
   return (neuron0x18c5be00()*-0.924393);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5e920() {
   return (neuron0x18c5c270()*1.42685);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5e960() {
   return (neuron0x18c5c5a0()*-1.81641);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5e9a0() {
   return (neuron0x18c5c9a0()*1.39762);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5e9e0() {
   return (neuron0x18c5cda0()*2.48768);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5ea20() {
   return (neuron0x18c5d1a0()*-3.21294);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5ea60() {
   return (neuron0x18c5d5a0()*-1.94541);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18bf0f60() {
   return (neuron0x18c5da70()*-1.83081);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18bf1040() {
   return (neuron0x18c5dde0()*0.282928);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18bf1080() {
   return (neuron0x18c5e1e0()*-0.0947616);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5eff0() {
   return (neuron0x18c5c270()*4.81593);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f030() {
   return (neuron0x18c5c5a0()*-2.54011);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f070() {
   return (neuron0x18c5c9a0()*2.78227);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f0b0() {
   return (neuron0x18c5cda0()*3.99593);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f0f0() {
   return (neuron0x18c5d1a0()*-0.745601);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f130() {
   return (neuron0x18c5d5a0()*-0.0656231);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f170() {
   return (neuron0x18c5da70()*0.00927977);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f1b0() {
   return (neuron0x18c5dde0()*0.692425);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f1f0() {
   return (neuron0x18c5e1e0()*1.47633);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f570() {
   return (neuron0x18c5c270()*-0.383763);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f5b0() {
   return (neuron0x18c5c5a0()*0.536909);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f5f0() {
   return (neuron0x18c5c9a0()*-0.504128);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f630() {
   return (neuron0x18c5cda0()*0.482966);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f670() {
   return (neuron0x18c5d1a0()*0.976153);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f6b0() {
   return (neuron0x18c5d5a0()*-0.34625);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f6f0() {
   return (neuron0x18c5da70()*0.467057);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f730() {
   return (neuron0x18c5dde0()*0.831468);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5f770() {
   return (neuron0x18c5e1e0()*-0.932493);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c009e0() {
   return (neuron0x18c5e5e0()*-4.86466);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5faf0() {
   return (neuron0x18c5ecb0()*-6.47404);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8::synapse0x18c5fb30() {
   return (neuron0x18c5f230()*2.96932);
}

