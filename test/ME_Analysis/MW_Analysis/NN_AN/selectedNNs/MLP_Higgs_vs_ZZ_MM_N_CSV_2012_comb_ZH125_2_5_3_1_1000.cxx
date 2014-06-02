#include "MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.1539)/1.32058;
   input1 = (in1 - 10.9056)/1.12483;
   input2 = (in2 - 24.8086)/1.23731;
   input3 = (in3 - 13.3364)/1.43408;
   switch(index) {
     case 0:
         return neuron0x91363a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::Value(int index, double* input) {
   input0 = (input[0] - 21.1539)/1.32058;
   input1 = (input[1] - 10.9056)/1.12483;
   input2 = (input[2] - 24.8086)/1.23731;
   input3 = (input[3] - 13.3364)/1.43408;
   switch(index) {
     case 0:
         return neuron0x91363a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x91326a0() {
   return input0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x91329e0() {
   return input1;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x9132d20() {
   return input2;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x9133060() {
   return input3;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x91334d0() {
   double input = -4.6461;
   input += synapse0x90d3a00();
   input += synapse0x9133780();
   input += synapse0x91337c0();
   input += synapse0x9133800();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x91334d0() {
   double input = input0x91334d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x9133840() {
   double input = -2.70191;
   input += synapse0x9133b80();
   input += synapse0x9133bc0();
   input += synapse0x9133c00();
   input += synapse0x9133c40();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x9133840() {
   double input = input0x9133840();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x9133c80() {
   double input = 1.36485;
   input += synapse0x9133fc0();
   input += synapse0x9134000();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x9133c80() {
   double input = input0x9133c80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x9134040() {
   double input = -0.381182;
   input += synapse0x9134380();
   input += synapse0x91343c0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x9134040() {
   double input = input0x9134040();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x9134400() {
   double input = -0.284706;
   input += synapse0x9134740();
   input += synapse0x9134780();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x9134400() {
   double input = input0x9134400();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x91347c0() {
   double input = 0.179155;
   input += synapse0x9134b00();
   input += synapse0x9134b40();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x91347c0() {
   double input = input0x91347c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x9134b80() {
   double input = 0.0387919;
   input += synapse0x9134ec0();
   input += synapse0x90d3550();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x9134b80() {
   double input = input0x9134b80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x9135010() {
   double input = 0.880776;
   input += synapse0x9135350();
   input += synapse0x9135390();
   input += synapse0x91353d0();
   input += synapse0x9135410();
   input += synapse0x9135450();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x9135010() {
   double input = input0x9135010();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x9135490() {
   double input = 0.614782;
   input += synapse0x91357d0();
   input += synapse0x9135810();
   input += synapse0x9135850();
   input += synapse0x9135890();
   input += synapse0x91358d0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x9135490() {
   double input = input0x9135490();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x9135910() {
   double input = 0.025953;
   input += synapse0x9135c50();
   input += synapse0x9135c90();
   input += synapse0x9135cd0();
   input += synapse0x9135d10();
   input += synapse0x9135d50();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x9135910() {
   double input = input0x9135910();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x9135fa0() {
   double input = 1.61742;
   input += synapse0x91362e0();
   input += synapse0x9136320();
   input += synapse0x9136360();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x9135fa0() {
   double input = input0x9135fa0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::input0x91363a0() {
   double input = -5.1674;
   input += synapse0x91366e0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::neuron0x91363a0() {
   double input = input0x91363a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x90d3a00() {
   return (neuron0x91326a0()*-0.208856);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9133780() {
   return (neuron0x91329e0()*-1.64744);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x91337c0() {
   return (neuron0x9132d20()*0.870751);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9133800() {
   return (neuron0x9133060()*0.918699);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9133b80() {
   return (neuron0x91326a0()*0.077417);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9133bc0() {
   return (neuron0x91329e0()*0.544463);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9133c00() {
   return (neuron0x9132d20()*0.194996);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9133c40() {
   return (neuron0x9133060()*-1.32701);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9133fc0() {
   return (neuron0x91334d0()*-3.1224);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9134000() {
   return (neuron0x9133840()*1.27502);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9134380() {
   return (neuron0x91334d0()*-1.75918);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x91343c0() {
   return (neuron0x9133840()*1.82139);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9134740() {
   return (neuron0x91334d0()*0.910201);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9134780() {
   return (neuron0x9133840()*0.352387);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9134b00() {
   return (neuron0x91334d0()*1.75034);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9134b40() {
   return (neuron0x9133840()*-1.76515);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9134ec0() {
   return (neuron0x91334d0()*-1.55551);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x90d3550() {
   return (neuron0x9133840()*-0.306353);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135350() {
   return (neuron0x9133c80()*-2.47365);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135390() {
   return (neuron0x9134040()*-1.97223);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x91353d0() {
   return (neuron0x9134400()*0.153109);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135410() {
   return (neuron0x91347c0()*2.37891);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135450() {
   return (neuron0x9134b80()*0.154376);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x91357d0() {
   return (neuron0x9133c80()*-2.24361);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135810() {
   return (neuron0x9134040()*-1.64461);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135850() {
   return (neuron0x9134400()*0.366173);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135890() {
   return (neuron0x91347c0()*2.21227);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x91358d0() {
   return (neuron0x9134b80()*0.101487);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135c50() {
   return (neuron0x9133c80()*0.75679);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135c90() {
   return (neuron0x9134040()*1.3409);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135cd0() {
   return (neuron0x9134400()*-0.203427);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135d10() {
   return (neuron0x91347c0()*-1.34807);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9135d50() {
   return (neuron0x9134b80()*0.0852285);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x91362e0() {
   return (neuron0x9135010()*-5.20618);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9136320() {
   return (neuron0x9135490()*-4.08309);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x9136360() {
   return (neuron0x9135910()*2.68076);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000::synapse0x91366e0() {
   return (neuron0x9135fa0()*11.6261);
}

