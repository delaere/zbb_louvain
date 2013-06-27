#include "MLP_Higgs_vs_TT_ZH125_comb-5-10_700_Nj2_Mbb50-200_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.2852)/3.17236;
   input1 = (in1 - 24.6937)/1.64914;
   input2 = (in2 - 13.2477)/2.49485;
   switch(index) {
     case 0:
         return neuron0x1feb9470();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 22.2852)/3.17236;
   input1 = (input[1] - 24.6937)/1.64914;
   input2 = (input[2] - 13.2477)/2.49485;
   switch(index) {
     case 0:
         return neuron0x1feb9470();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb6480() {
   return input0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb67c0() {
   return input1;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb6b00() {
   return input2;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb6f70() {
   double input = 1.05308;
   input += synapse0x1c315ca0();
   input += synapse0x1feb7220();
   input += synapse0x1feb7260();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb6f70() {
   double input = input0x1feb6f70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb72a0() {
   double input = 2.30227;
   input += synapse0x1feb75e0();
   input += synapse0x1feb7620();
   input += synapse0x1feb7660();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb72a0() {
   double input = input0x1feb72a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb76a0() {
   double input = 0.560261;
   input += synapse0x1feb79e0();
   input += synapse0x1feb7a20();
   input += synapse0x1feb7a60();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb76a0() {
   double input = input0x1feb76a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb7aa0() {
   double input = 2.39589;
   input += synapse0x1feb7de0();
   input += synapse0x1feb7e20();
   input += synapse0x1feb7e60();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb7aa0() {
   double input = input0x1feb7aa0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb7ea0() {
   double input = -4.39203;
   input += synapse0x1feb81e0();
   input += synapse0x1feb8220();
   input += synapse0x1feb8260();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb7ea0() {
   double input = input0x1feb7ea0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb82a0() {
   double input = -0.561386;
   input += synapse0x1feb85e0();
   input += synapse0x1feb8620();
   input += synapse0x1febf0f0();
   input += synapse0x1c315850();
   input += synapse0x1c315890();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb82a0() {
   double input = input0x1feb82a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb8770() {
   double input = -0.385217;
   input += synapse0x1feb8ab0();
   input += synapse0x1feb8af0();
   input += synapse0x1feb8b30();
   input += synapse0x1feb8b70();
   input += synapse0x1feb8bb0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb8770() {
   double input = input0x1feb8770();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb8bf0() {
   double input = -1.63269;
   input += synapse0x1feb8f30();
   input += synapse0x1feb8f70();
   input += synapse0x1feb8fb0();
   input += synapse0x1feb8ff0();
   input += synapse0x1feb9030();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb8bf0() {
   double input = input0x1feb8bf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb9070() {
   double input = -0.232771;
   input += synapse0x1feb93b0();
   input += synapse0x1feb93f0();
   input += synapse0x1feb9430();
   input += synapse0x1c315c50();
   input += synapse0x1c315ce0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb9070() {
   double input = input0x1feb9070();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb9680() {
   double input = 0.23155;
   input += synapse0x1feb99c0();
   input += synapse0x1feb9a00();
   input += synapse0x1feb9a40();
   input += synapse0x1feb9a80();
   input += synapse0x1feb9ac0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb9680() {
   double input = input0x1feb9680();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb9b00() {
   double input = 0.164734;
   input += synapse0x1feb9e40();
   input += synapse0x1feb9e80();
   input += synapse0x1feb9ec0();
   input += synapse0x1feb9f00();
   input += synapse0x1feb9f40();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb9b00() {
   double input = input0x1feb9b00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb9f80() {
   double input = -0.0622124;
   input += synapse0x1feba2c0();
   input += synapse0x1feba300();
   input += synapse0x1feba340();
   input += synapse0x1feba380();
   input += synapse0x1feba3c0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb9f80() {
   double input = input0x1feb9f80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feba400() {
   double input = -0.145791;
   input += synapse0x1feba740();
   input += synapse0x1feba780();
   input += synapse0x1feba7c0();
   input += synapse0x1feba800();
   input += synapse0x1feba840();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feba400() {
   double input = input0x1feba400();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feba880() {
   double input = 0.525667;
   input += synapse0x1c3156a0();
   input += synapse0x1c3156e0();
   input += synapse0x1c315d20();
   input += synapse0x1c315d60();
   input += synapse0x1febabc0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feba880() {
   double input = input0x1feba880();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1febac00() {
   double input = -0.61746;
   input += synapse0x1febaf40();
   input += synapse0x1febaf80();
   input += synapse0x1febafc0();
   input += synapse0x1febb000();
   input += synapse0x1febb040();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1febac00() {
   double input = input0x1febac00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0x1feb9470() {
   double input = 1.33348;
   input += synapse0x1feb6e40();
   input += synapse0x1febb5b0();
   input += synapse0x1febb5f0();
   input += synapse0x1febb630();
   input += synapse0x1febb670();
   input += synapse0x1febb6b0();
   input += synapse0x1febb6f0();
   input += synapse0x1febb730();
   input += synapse0x1febb770();
   input += synapse0x1febb7b0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0x1feb9470() {
   double input = input0x1feb9470();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c315ca0() {
   return (neuron0x1feb6480()*-2.52939);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb7220() {
   return (neuron0x1feb67c0()*1.09034);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb7260() {
   return (neuron0x1feb6b00()*0.14284);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb75e0() {
   return (neuron0x1feb6480()*2.46768);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb7620() {
   return (neuron0x1feb67c0()*-1.22782);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb7660() {
   return (neuron0x1feb6b00()*-0.396988);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb79e0() {
   return (neuron0x1feb6480()*-1.94415);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb7a20() {
   return (neuron0x1feb67c0()*2.75575);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb7a60() {
   return (neuron0x1feb6b00()*-0.32658);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb7de0() {
   return (neuron0x1feb6480()*-1.44844);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb7e20() {
   return (neuron0x1feb67c0()*1.75343);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb7e60() {
   return (neuron0x1feb6b00()*1.90229);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb81e0() {
   return (neuron0x1feb6480()*1.8418);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8220() {
   return (neuron0x1feb67c0()*-3.19946);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8260() {
   return (neuron0x1feb6b00()*-0.291179);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb85e0() {
   return (neuron0x1feb6f70()*1.17416);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8620() {
   return (neuron0x1feb72a0()*-2.02943);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febf0f0() {
   return (neuron0x1feb76a0()*-0.601345);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c315850() {
   return (neuron0x1feb7aa0()*1.87006);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c315890() {
   return (neuron0x1feb7ea0()*0.568974);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8ab0() {
   return (neuron0x1feb6f70()*-3.32266);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8af0() {
   return (neuron0x1feb72a0()*1.25988);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8b30() {
   return (neuron0x1feb76a0()*2.22746);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8b70() {
   return (neuron0x1feb7aa0()*-1.20519);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8bb0() {
   return (neuron0x1feb7ea0()*-3.05458);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8f30() {
   return (neuron0x1feb6f70()*2.19755);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8f70() {
   return (neuron0x1feb72a0()*-2.55671);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8fb0() {
   return (neuron0x1feb76a0()*-0.597393);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb8ff0() {
   return (neuron0x1feb7aa0()*2.79433);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb9030() {
   return (neuron0x1feb7ea0()*0.361818);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb93b0() {
   return (neuron0x1feb6f70()*0.255753);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb93f0() {
   return (neuron0x1feb72a0()*-0.712838);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb9430() {
   return (neuron0x1feb76a0()*-0.529931);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c315c50() {
   return (neuron0x1feb7aa0()*0.493946);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c315ce0() {
   return (neuron0x1feb7ea0()*-0.593921);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb99c0() {
   return (neuron0x1feb6f70()*-1.21451);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb9a00() {
   return (neuron0x1feb72a0()*1.46038);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb9a40() {
   return (neuron0x1feb76a0()*1.68849);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb9a80() {
   return (neuron0x1feb7aa0()*-2.66613);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb9ac0() {
   return (neuron0x1feb7ea0()*-2.55601);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb9e40() {
   return (neuron0x1feb6f70()*-0.122763);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb9e80() {
   return (neuron0x1feb72a0()*0.413952);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb9ec0() {
   return (neuron0x1feb76a0()*-0.0931631);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb9f00() {
   return (neuron0x1feb7aa0()*-0.337579);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb9f40() {
   return (neuron0x1feb7ea0()*0.322298);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feba2c0() {
   return (neuron0x1feb6f70()*0.768169);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feba300() {
   return (neuron0x1feb72a0()*-1.00786);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feba340() {
   return (neuron0x1feb76a0()*-1.19658);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feba380() {
   return (neuron0x1feb7aa0()*1.36646);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feba3c0() {
   return (neuron0x1feb7ea0()*2.41849);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feba740() {
   return (neuron0x1feb6f70()*0.187899);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feba780() {
   return (neuron0x1feb72a0()*-0.485648);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feba7c0() {
   return (neuron0x1feb76a0()*-1.00856);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feba800() {
   return (neuron0x1feb7aa0()*0.647257);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feba840() {
   return (neuron0x1feb7ea0()*-0.0621195);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c3156a0() {
   return (neuron0x1feb6f70()*-1.22343);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c3156e0() {
   return (neuron0x1feb72a0()*1.53206);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c315d20() {
   return (neuron0x1feb76a0()*3.45116);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c315d60() {
   return (neuron0x1feb7aa0()*-4.29137);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febabc0() {
   return (neuron0x1feb7ea0()*-3.45858);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febaf40() {
   return (neuron0x1feb6f70()*1.42943);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febaf80() {
   return (neuron0x1feb72a0()*-1.78329);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febafc0() {
   return (neuron0x1feb76a0()*-0.841965);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febb000() {
   return (neuron0x1feb7aa0()*1.68853);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febb040() {
   return (neuron0x1feb7ea0()*0.121791);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1feb6e40() {
   return (neuron0x1feb82a0()*-2.54589);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febb5b0() {
   return (neuron0x1feb8770()*5.25403);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febb5f0() {
   return (neuron0x1feb8bf0()*-5.44708);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febb630() {
   return (neuron0x1feb9070()*0.141637);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febb670() {
   return (neuron0x1feb9680()*4.65298);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febb6b0() {
   return (neuron0x1feb9b00()*0.66026);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febb6f0() {
   return (neuron0x1feb9f80()*-2.66777);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febb730() {
   return (neuron0x1feba400()*-0.278248);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febb770() {
   return (neuron0x1feba880()*7.54434);
}

double MLP_Higgs_vs_TT_ZH125_comb_5_10_700_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0x1febb7b0() {
   return (neuron0x1febac00()*-1.82458);
}

