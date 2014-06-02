#include "MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.392068)/0.290776;
   input1 = (in1 - 0.502534)/0.347166;
   input2 = (in2 - 0.565438)/0.340056;
   switch(index) {
     case 0:
         return neuron0xf5f4730();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 0.392068)/0.290776;
   input1 = (input[1] - 0.502534)/0.347166;
   input2 = (input[2] - 0.565438)/0.340056;
   switch(index) {
     case 0:
         return neuron0xf5f4730();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0xf5f2610() {
   return input0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0xf5f2950() {
   return input1;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0xf5f2c90() {
   return input2;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0xf5f3100() {
   double input = 2.39646;
   input += synapse0xf597800();
   input += synapse0xf5f33b0();
   input += synapse0xf5f33f0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0xf5f3100() {
   double input = input0xf5f3100();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0xf5f3430() {
   double input = 4.47938;
   input += synapse0xf5f3770();
   input += synapse0xf5f37b0();
   input += synapse0xf5f37f0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0xf5f3430() {
   double input = input0xf5f3430();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0xf5f3830() {
   double input = -0.0812917;
   input += synapse0xf5f3b70();
   input += synapse0xf5f3bb0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0xf5f3830() {
   double input = input0xf5f3830();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0xf5f3bf0() {
   double input = -0.1319;
   input += synapse0xf5f3f30();
   input += synapse0xf5f3f70();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0xf5f3bf0() {
   double input = input0xf5f3bf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0xf5f3fb0() {
   double input = 0.0387131;
   input += synapse0xf5f42f0();
   input += synapse0xf5f4330();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0xf5f3fb0() {
   double input = input0xf5f3fb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0xf5f4370() {
   double input = 0.00861021;
   input += synapse0xf5f46b0();
   input += synapse0xf5f46f0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0xf5f4370() {
   double input = input0xf5f4370();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::input0xf5f4730() {
   double input = 1.39664;
   input += synapse0xf5978e0();
   input += synapse0xf5f4a70();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::neuron0xf5f4730() {
   double input = input0xf5f4730();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf597800() {
   return (neuron0xf5f2610()*1.17098);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f33b0() {
   return (neuron0xf5f2950()*-0.119476);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f33f0() {
   return (neuron0xf5f2c90()*0.0840931);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f3770() {
   return (neuron0xf5f2610()*-1.0315);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f37b0() {
   return (neuron0xf5f2950()*-0.186701);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f37f0() {
   return (neuron0xf5f2c90()*-0.707374);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f3b70() {
   return (neuron0xf5f3100()*-3.41378);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f3bb0() {
   return (neuron0xf5f3430()*1.63603);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f3f30() {
   return (neuron0xf5f3100()*2.31649);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f3f70() {
   return (neuron0xf5f3430()*-3.29337);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f42f0() {
   return (neuron0xf5f3830()*-3.58734);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f4330() {
   return (neuron0xf5f3bf0()*3.12002);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f46b0() {
   return (neuron0xf5f3830()*4.47806);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f46f0() {
   return (neuron0xf5f3bf0()*-3.77194);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5978e0() {
   return (neuron0xf5f3fb0()*5.86748);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20::synapse0xf5f4a70() {
   return (neuron0xf5f4370()*-8.87691);
}

