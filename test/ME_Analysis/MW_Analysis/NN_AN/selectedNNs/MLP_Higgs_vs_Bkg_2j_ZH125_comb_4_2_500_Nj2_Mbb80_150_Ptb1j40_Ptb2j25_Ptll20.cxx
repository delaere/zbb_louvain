#include "MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.492195)/0.255462;
   input1 = (in1 - 0.567862)/0.324105;
   input2 = (in2 - 0.596078)/0.304322;
   switch(index) {
     case 0:
         return neuron0x3a6db5a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 0.492195)/0.255462;
   input1 = (input[1] - 0.567862)/0.324105;
   input2 = (input[2] - 0.596078)/0.304322;
   switch(index) {
     case 0:
         return neuron0x3a6db5a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a6d9270() {
   return input0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a6d95b0() {
   return input1;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a6d98f0() {
   return input2;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x3a6d9d60() {
   double input = 1.55242;
   input += synapse0x3a6e1f70();
   input += synapse0x3a6da010();
   input += synapse0x3a6da050();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a6d9d60() {
   double input = input0x3a6d9d60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x3a6da090() {
   double input = 6.38049;
   input += synapse0x3a6da3d0();
   input += synapse0x3a6da410();
   input += synapse0x3a6da450();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a6da090() {
   double input = input0x3a6da090();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x3a6da490() {
   double input = 1.71672;
   input += synapse0x3a6da7d0();
   input += synapse0x3a6da810();
   input += synapse0x3a6da850();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a6da490() {
   double input = input0x3a6da490();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x3a6da890() {
   double input = 3.61959;
   input += synapse0x3a6dabd0();
   input += synapse0x3a6dac10();
   input += synapse0x3a6dac50();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a6da890() {
   double input = input0x3a6da890();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x3a6dac90() {
   double input = 3.38776;
   input += synapse0x3a6dafd0();
   input += synapse0x3a6db010();
   input += synapse0x3a6db050();
   input += synapse0x3a6db090();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a6dac90() {
   double input = input0x3a6dac90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x3a6db0d0() {
   double input = -2.56364;
   input += synapse0x3a6db410();
   input += synapse0x3a66ddd0();
   input += synapse0x3a66de10();
   input += synapse0x3a6db560();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a6db0d0() {
   double input = input0x3a6db0d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x3a6db5a0() {
   double input = -0.20283;
   input += synapse0x3a6d9c30();
   input += synapse0x3a6db8e0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3a6db5a0() {
   double input = input0x3a6db5a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6e1f70() {
   return (neuron0x3a6d9270()*0.767233);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6da010() {
   return (neuron0x3a6d95b0()*0.0149494);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6da050() {
   return (neuron0x3a6d98f0()*1.5602);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6da3d0() {
   return (neuron0x3a6d9270()*2.22895);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6da410() {
   return (neuron0x3a6d95b0()*1.31885);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6da450() {
   return (neuron0x3a6d98f0()*0.0337837);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6da7d0() {
   return (neuron0x3a6d9270()*1.32181);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6da810() {
   return (neuron0x3a6d95b0()*-0.315246);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6da850() {
   return (neuron0x3a6d98f0()*-0.716874);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6dabd0() {
   return (neuron0x3a6d9270()*-1.13616);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6dac10() {
   return (neuron0x3a6d95b0()*-0.134219);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6dac50() {
   return (neuron0x3a6d98f0()*-0.276811);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6dafd0() {
   return (neuron0x3a6d9d60()*-2.07323);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6db010() {
   return (neuron0x3a6da090()*-4.14259);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6db050() {
   return (neuron0x3a6da490()*-4.93308);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6db090() {
   return (neuron0x3a6da890()*2.66719);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6db410() {
   return (neuron0x3a6d9d60()*3.25251);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a66ddd0() {
   return (neuron0x3a6da090()*-0.855535);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a66de10() {
   return (neuron0x3a6da490()*3.50037);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6db560() {
   return (neuron0x3a6da890()*-4.83074);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6d9c30() {
   return (neuron0x3a6dac90()*-8.57098);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3a6db8e0() {
   return (neuron0x3a6db0d0()*8.2086);
}

