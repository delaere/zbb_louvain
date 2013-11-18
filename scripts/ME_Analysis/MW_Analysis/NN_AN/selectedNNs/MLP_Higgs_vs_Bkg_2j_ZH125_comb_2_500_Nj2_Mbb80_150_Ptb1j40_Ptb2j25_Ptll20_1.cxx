#include "MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.500017)/0.25242;
   input1 = (in1 - 0.592179)/0.338539;
   input2 = (in2 - 0.679468)/0.281065;
   switch(index) {
     case 0:
         return neuron0x1dda5fb0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::Value(int index, double* input) {
   input0 = (input[0] - 0.500017)/0.25242;
   input1 = (input[1] - 0.592179)/0.338539;
   input2 = (input[2] - 0.679468)/0.281065;
   switch(index) {
     case 0:
         return neuron0x1dda5fb0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x1dda4d90() {
   return input0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x1dda50d0() {
   return input1;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x1dda5410() {
   return input2;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::input0x1dda5880() {
   double input = 3.61475;
   input += synapse0x1dd49fd0();
   input += synapse0x1dda5b30();
   input += synapse0x1dda5b70();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x1dda5880() {
   double input = input0x1dda5880();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::input0x1dda5bb0() {
   double input = 2.80419;
   input += synapse0x1dda5ef0();
   input += synapse0x1dda5f30();
   input += synapse0x1dda5f70();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x1dda5bb0() {
   double input = input0x1dda5bb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::input0x1dda5fb0() {
   double input = 3.69251;
   input += synapse0x1dd4a080();
   input += synapse0x1dda62f0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x1dda5fb0() {
   double input = input0x1dda5fb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x1dd49fd0() {
   return (neuron0x1dda4d90()*-1.30708);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x1dda5b30() {
   return (neuron0x1dda50d0()*0.104347);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x1dda5b70() {
   return (neuron0x1dda5410()*-0.495562);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x1dda5ef0() {
   return (neuron0x1dda4d90()*1.40391);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x1dda5f30() {
   return (neuron0x1dda50d0()*-0.0852811);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x1dda5f70() {
   return (neuron0x1dda5410()*0.0720031);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x1dd4a080() {
   return (neuron0x1dda5880()*-9.63864);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x1dda62f0() {
   return (neuron0x1dda5bb0()*6.18629);
}

