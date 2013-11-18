#include "MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.492195)/0.255462;
   input1 = (in1 - 0.567862)/0.324105;
   input2 = (in2 - 0.596078)/0.304322;
   switch(index) {
     case 0:
         return neuron0x2f8c5a60();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 0.492195)/0.255462;
   input1 = (input[1] - 0.567862)/0.324105;
   input2 = (input[2] - 0.596078)/0.304322;
   switch(index) {
     case 0:
         return neuron0x2f8c5a60();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2f8c4040() {
   return input0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2f8c4380() {
   return input1;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2f8c46c0() {
   return input2;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2f8c4b30() {
   double input = 0.345579;
   input += synapse0x2f8ccd40();
   input += synapse0x2f8c4de0();
   input += synapse0x2f8c4e20();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2f8c4b30() {
   double input = input0x2f8c4b30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2f8c4e60() {
   double input = 0.569005;
   input += synapse0x2f8c51a0();
   input += synapse0x2f8c51e0();
   input += synapse0x2f8c5220();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2f8c4e60() {
   double input = input0x2f8c4e60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2f8c5260() {
   double input = -9.5062;
   input += synapse0x2f8c55a0();
   input += synapse0x2f8c55e0();
   input += synapse0x2f8c5620();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2f8c5260() {
   double input = input0x2f8c5260();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2f8c5660() {
   double input = 2.84143;
   input += synapse0x2f8c59a0();
   input += synapse0x2f8c59e0();
   input += synapse0x2f8c5a20();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2f8c5660() {
   double input = input0x2f8c5660();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2f8c5a60() {
   double input = -4.02792;
   input += synapse0x2f8c4a00();
   input += synapse0x2f8c5da0();
   input += synapse0x2f8c5de0();
   input += synapse0x2f8c5e20();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2f8c5a60() {
   double input = input0x2f8c5a60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8ccd40() {
   return (neuron0x2f8c4040()*-1.27089);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c4de0() {
   return (neuron0x2f8c4380()*0.611048);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c4e20() {
   return (neuron0x2f8c46c0()*0.844143);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c51a0() {
   return (neuron0x2f8c4040()*-1.16844);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c51e0() {
   return (neuron0x2f8c4380()*0.823278);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c5220() {
   return (neuron0x2f8c46c0()*1.03581);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c55a0() {
   return (neuron0x2f8c4040()*-5.13407);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c55e0() {
   return (neuron0x2f8c4380()*0.0061512);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c5620() {
   return (neuron0x2f8c46c0()*0.752944);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c59a0() {
   return (neuron0x2f8c4040()*-0.0815118);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c59e0() {
   return (neuron0x2f8c4380()*-0.587444);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c5a20() {
   return (neuron0x2f8c46c0()*0.787141);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c4a00() {
   return (neuron0x2f8c4b30()*-12.967);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c5da0() {
   return (neuron0x2f8c4e60()*10.8267);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c5de0() {
   return (neuron0x2f8c5260()*-9.34735);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2f8c5e20() {
   return (neuron0x2f8c5660()*5.38594);
}

