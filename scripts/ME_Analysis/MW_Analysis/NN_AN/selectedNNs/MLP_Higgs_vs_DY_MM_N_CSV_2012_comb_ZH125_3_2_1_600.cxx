#include "MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600.h"
#include <cmath>

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.4187)/1.13986;
   input1 = (in1 - 20.1808)/1.02782;
   input2 = (in2 - 25.0021)/1.84057;
   input3 = (in3 - 13.943)/1.94542;
   switch(index) {
     case 0:
         return neuron0xc545ec0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::Value(int index, double* input) {
   input0 = (input[0] - 19.4187)/1.13986;
   input1 = (input[1] - 20.1808)/1.02782;
   input2 = (input[2] - 25.0021)/1.84057;
   input3 = (input[3] - 13.943)/1.94542;
   switch(index) {
     case 0:
         return neuron0xc545ec0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::neuron0xc543810() {
   return input0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::neuron0xc543b50() {
   return input1;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::neuron0xc543e90() {
   return input2;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::neuron0xc5441d0() {
   return input3;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::input0xc544640() {
   double input = 2.321;
   input += synapse0xc4e4b70();
   input += synapse0xc5448f0();
   input += synapse0xc544930();
   input += synapse0xc544970();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::neuron0xc544640() {
   double input = input0xc544640();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::input0xc5449b0() {
   double input = -5.5918;
   input += synapse0xc544cf0();
   input += synapse0xc544d30();
   input += synapse0xc544d70();
   input += synapse0xc544db0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::neuron0xc5449b0() {
   double input = input0xc5449b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::input0xc544df0() {
   double input = -3.8749;
   input += synapse0xc545130();
   input += synapse0xc545170();
   input += synapse0xc5451b0();
   input += synapse0xc5451f0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::neuron0xc544df0() {
   double input = input0xc544df0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::input0xc545230() {
   double input = -2.2867;
   input += synapse0xc545570();
   input += synapse0xc5455b0();
   input += synapse0xc5455f0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::neuron0xc545230() {
   double input = input0xc545230();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::input0xc545630() {
   double input = -1.0896;
   input += synapse0xc545970();
   input += synapse0xc5459b0();
   input += synapse0xc4e46c0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::neuron0xc545630() {
   double input = input0xc545630();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::input0xc545b00() {
   double input = 3.45277;
   input += synapse0xc545e40();
   input += synapse0xc545e80();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::neuron0xc545b00() {
   double input = input0xc545b00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::input0xc545ec0() {
   double input = -3.21877;
   input += synapse0xc546200();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::neuron0xc545ec0() {
   double input = input0xc545ec0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc4e4b70() {
   return (neuron0xc543810()*-0.556269);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc5448f0() {
   return (neuron0xc543b50()*0.0235877);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc544930() {
   return (neuron0xc543e90()*-0.228767);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc544970() {
   return (neuron0xc5441d0()*1.62826);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc544cf0() {
   return (neuron0xc543810()*-1.70472);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc544d30() {
   return (neuron0xc543b50()*-0.0897515);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc544d70() {
   return (neuron0xc543e90()*5.0335);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc544db0() {
   return (neuron0xc5441d0()*0.618993);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc545130() {
   return (neuron0xc543810()*-2.91263);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc545170() {
   return (neuron0xc543b50()*1.73561);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc5451b0() {
   return (neuron0xc543e90()*-0.402805);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc5451f0() {
   return (neuron0xc5441d0()*1.42651);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc545570() {
   return (neuron0xc544640()*2.27052);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc5455b0() {
   return (neuron0xc5449b0()*1.82516);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc5455f0() {
   return (neuron0xc544df0()*2.901);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc545970() {
   return (neuron0xc544640()*2.05092);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc5459b0() {
   return (neuron0xc5449b0()*0.873522);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc4e46c0() {
   return (neuron0xc544df0()*1.73391);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc545e40() {
   return (neuron0xc545230()*-5.21073);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc545e80() {
   return (neuron0xc545630()*-2.69348);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600::synapse0xc546200() {
   return (neuron0xc545b00()*9.61136);
}

