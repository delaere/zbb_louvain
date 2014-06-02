#include "MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3,double in4,double in5) {
   input0 = (in0 - 19.5959)/1.02856;
   input1 = (in1 - 20.2647)/0.838707;
   input2 = (in2 - 24.8357)/1.49412;
   input3 = (in3 - 13.3413)/1.47218;
   input4 = (in4 - 8.50219)/30.9864;
   input5 = (in5 - 1.8064)/0.811333;
   switch(index) {
     case 0:
         return neuron0x1ca66330();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 19.5959)/1.02856;
   input1 = (input[1] - 20.2647)/0.838707;
   input2 = (input[2] - 24.8357)/1.49412;
   input3 = (input[3] - 13.3413)/1.47218;
   input4 = (input[4] - 8.50219)/30.9864;
   input5 = (input[5] - 1.8064)/0.811333;
   switch(index) {
     case 0:
         return neuron0x1ca66330();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5a7c0() {
   return input0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5aa70() {
   return input1;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5adb0() {
   return input2;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5b0f0() {
   return input3;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5b430() {
   return input4;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5b770() {
   return input5;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5bbe0() {
   double input = -0.259774;
   input += synapse0x1ca5be90();
   input += synapse0x1ca5bed0();
   input += synapse0x1ca5bf10();
   input += synapse0x1ca5bf50();
   input += synapse0x1ca5bf90();
   input += synapse0x1ca5bfd0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5bbe0() {
   double input = input0x1ca5bbe0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5c010() {
   double input = 0.138746;
   input += synapse0x1ca5c350();
   input += synapse0x1ca5c390();
   input += synapse0x1ca5c3d0();
   input += synapse0x1ca5c410();
   input += synapse0x1ca5c450();
   input += synapse0x1ca5c490();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5c010() {
   double input = input0x1ca5c010();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5c4d0() {
   double input = 0.0672574;
   input += synapse0x1ca5c810();
   input += synapse0x1ca5c850();
   input += synapse0x1ca5c890();
   input += synapse0x1ca5c8d0();
   input += synapse0x1ca5c910();
   input += synapse0x1c9a8270();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5c4d0() {
   double input = input0x1ca5c4d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5ca60() {
   double input = -0.600926;
   input += synapse0x1c9a82b0();
   input += synapse0x1ca5cda0();
   input += synapse0x1ca5cde0();
   input += synapse0x1ca5ce20();
   input += synapse0x1ca5ce60();
   input += synapse0x1ca5cea0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5ca60() {
   double input = input0x1ca5ca60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5cee0() {
   double input = -0.370899;
   input += synapse0x1ca5d220();
   input += synapse0x1ca5d260();
   input += synapse0x1ca5d2a0();
   input += synapse0x1ca5d2e0();
   input += synapse0x1ca5d320();
   input += synapse0x1ca5d360();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5cee0() {
   double input = input0x1ca5cee0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5d3a0() {
   double input = 0.148826;
   input += synapse0x1ca5d6e0();
   input += synapse0x1ca5d720();
   input += synapse0x1ca5d760();
   input += synapse0x1ca49b40();
   input += synapse0x1c9b8030();
   input += synapse0x1c9a8650();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5d3a0() {
   double input = input0x1ca5d3a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5d9b0() {
   double input = 0.105755;
   input += synapse0x1ca5c9e0();
   input += synapse0x1ca5ca20();
   input += synapse0x1ca5db40();
   input += synapse0x1ca5db80();
   input += synapse0x1ca5dbc0();
   input += synapse0x1ca5dc00();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5d9b0() {
   double input = input0x1ca5d9b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5dc40() {
   double input = 1.97535;
   input += synapse0x1ca5df80();
   input += synapse0x1ca5dfc0();
   input += synapse0x1ca5e000();
   input += synapse0x1ca5e040();
   input += synapse0x1ca5e080();
   input += synapse0x1ca5e0c0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5dc40() {
   double input = input0x1ca5dc40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5e100() {
   double input = -0.315596;
   input += synapse0x1ca5e440();
   input += synapse0x1ca5e480();
   input += synapse0x1ca5e4c0();
   input += synapse0x1ca5e500();
   input += synapse0x1ca5e540();
   input += synapse0x1ca5e580();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5e100() {
   double input = input0x1ca5e100();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5e5c0() {
   double input = 0.563446;
   input += synapse0x1ca5e900();
   input += synapse0x1ca5e940();
   input += synapse0x1ca5e980();
   input += synapse0x1ca5e9c0();
   input += synapse0x1ca5ea00();
   input += synapse0x1ca5ea40();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5e5c0() {
   double input = input0x1ca5e5c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5ea80() {
   double input = -0.876319;
   input += synapse0x1c9a80c0();
   input += synapse0x1c9a8100();
   input += synapse0x1ca5eed0();
   input += synapse0x1ca5ef10();
   input += synapse0x1ca5ef50();
   input += synapse0x1ca5d7a0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5ea80() {
   double input = input0x1ca5ea80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5d7e0() {
   double input = 0.366995;
   input += synapse0x1ca5d970();
   input += synapse0x1ca5f550();
   input += synapse0x1ca5f590();
   input += synapse0x1ca5f5d0();
   input += synapse0x1ca5f610();
   input += synapse0x1ca5f650();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5d7e0() {
   double input = input0x1ca5d7e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5f690() {
   double input = -0.104546;
   input += synapse0x1ca5f9d0();
   input += synapse0x1ca5fa10();
   input += synapse0x1ca5fa50();
   input += synapse0x1ca5fa90();
   input += synapse0x1ca5fad0();
   input += synapse0x1ca5fb10();
   input += synapse0x1ca5fb50();
   input += synapse0x1ca5fb90();
   input += synapse0x1ca5fbd0();
   input += synapse0x1ca5fc10();
   input += synapse0x1ca5fc50();
   input += synapse0x1ca5fc90();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5f690() {
   double input = input0x1ca5f690();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5fcd0() {
   double input = 0.280206;
   input += synapse0x1ca60010();
   input += synapse0x1ca60050();
   input += synapse0x1ca60090();
   input += synapse0x1ca600d0();
   input += synapse0x1ca60110();
   input += synapse0x1ca60150();
   input += synapse0x1ca60190();
   input += synapse0x1ca601d0();
   input += synapse0x1ca60210();
   input += synapse0x1ca60250();
   input += synapse0x1ca60290();
   input += synapse0x1ca602d0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5fcd0() {
   double input = input0x1ca5fcd0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca60310() {
   double input = -0.36015;
   input += synapse0x1ca60650();
   input += synapse0x1ca60690();
   input += synapse0x1ca606d0();
   input += synapse0x1ca60710();
   input += synapse0x1ca60750();
   input += synapse0x1ca60790();
   input += synapse0x1ca607d0();
   input += synapse0x1ca60810();
   input += synapse0x1ca60850();
   input += synapse0x1ca60890();
   input += synapse0x1ca608d0();
   input += synapse0x1ca60910();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca60310() {
   double input = input0x1ca60310();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca60950() {
   double input = 0.464581;
   input += synapse0x1ca60c90();
   input += synapse0x1ca60cd0();
   input += synapse0x1ca60d10();
   input += synapse0x1ca60d50();
   input += synapse0x1ca60d90();
   input += synapse0x1ca60dd0();
   input += synapse0x1ca60e10();
   input += synapse0x1ca60e50();
   input += synapse0x1ca60e90();
   input += synapse0x1ca60ed0();
   input += synapse0x1ca60f10();
   input += synapse0x1ca60f50();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca60950() {
   double input = input0x1ca60950();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca60f90() {
   double input = 0.104663;
   input += synapse0x1ca612d0();
   input += synapse0x1ca61310();
   input += synapse0x1ca61350();
   input += synapse0x1ca61390();
   input += synapse0x1ca613d0();
   input += synapse0x1ca61410();
   input += synapse0x1ca61450();
   input += synapse0x1ca61490();
   input += synapse0x1ca614d0();
   input += synapse0x1ca5ef90();
   input += synapse0x1ca5efd0();
   input += synapse0x1ca5f010();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca60f90() {
   double input = input0x1ca60f90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca5f050() {
   double input = -0.212921;
   input += synapse0x1ca61d20();
   input += synapse0x1ca61d60();
   input += synapse0x1ca61da0();
   input += synapse0x1ca61de0();
   input += synapse0x1ca61e20();
   input += synapse0x1ca61e60();
   input += synapse0x1ca61ea0();
   input += synapse0x1ca61ee0();
   input += synapse0x1ca61f20();
   input += synapse0x1ca61f60();
   input += synapse0x1ca61fa0();
   input += synapse0x1ca61fe0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca5f050() {
   double input = input0x1ca5f050();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca62020() {
   double input = 0.0120629;
   input += synapse0x1ca62360();
   input += synapse0x1ca623a0();
   input += synapse0x1ca623e0();
   input += synapse0x1ca62420();
   input += synapse0x1ca62460();
   input += synapse0x1ca624a0();
   input += synapse0x1ca624e0();
   input += synapse0x1ca62520();
   input += synapse0x1ca62560();
   input += synapse0x1ca625a0();
   input += synapse0x1ca625e0();
   input += synapse0x1ca62620();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca62020() {
   double input = input0x1ca62020();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca62660() {
   double input = 0.146341;
   input += synapse0x1ca629a0();
   input += synapse0x1ca629e0();
   input += synapse0x1ca62a20();
   input += synapse0x1ca62a60();
   input += synapse0x1ca62aa0();
   input += synapse0x1ca62ae0();
   input += synapse0x1ca62b20();
   input += synapse0x1ca62b60();
   input += synapse0x1ca62ba0();
   input += synapse0x1ca62be0();
   input += synapse0x1ca62c20();
   input += synapse0x1ca62c60();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca62660() {
   double input = input0x1ca62660();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca62ca0() {
   double input = -0.865624;
   input += synapse0x1ca62fe0();
   input += synapse0x1ca63020();
   input += synapse0x1ca63060();
   input += synapse0x1ca630a0();
   input += synapse0x1ca630e0();
   input += synapse0x1ca63120();
   input += synapse0x1ca63160();
   input += synapse0x1ca631a0();
   input += synapse0x1ca631e0();
   input += synapse0x1ca63220();
   input += synapse0x1ca63260();
   input += synapse0x1ca632a0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca62ca0() {
   double input = input0x1ca62ca0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca632e0() {
   double input = -0.0821723;
   input += synapse0x1ca63620();
   input += synapse0x1ca63660();
   input += synapse0x1ca636a0();
   input += synapse0x1ca636e0();
   input += synapse0x1ca63720();
   input += synapse0x1ca63760();
   input += synapse0x1ca637a0();
   input += synapse0x1ca637e0();
   input += synapse0x1ca63820();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca632e0() {
   double input = input0x1ca632e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca63860() {
   double input = 0.315089;
   input += synapse0x1ca63ba0();
   input += synapse0x1ca63be0();
   input += synapse0x1ca63c20();
   input += synapse0x1ca63c60();
   input += synapse0x1ca63ca0();
   input += synapse0x1ca63ce0();
   input += synapse0x1ca63d20();
   input += synapse0x1ca63d60();
   input += synapse0x1ca63da0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca63860() {
   double input = input0x1ca63860();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca63de0() {
   double input = 0.0989284;
   input += synapse0x1ca64120();
   input += synapse0x1ca64160();
   input += synapse0x1ca641a0();
   input += synapse0x1ca641e0();
   input += synapse0x1ca64220();
   input += synapse0x1ca64260();
   input += synapse0x1ca642a0();
   input += synapse0x1ca642e0();
   input += synapse0x1ca64320();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca63de0() {
   double input = input0x1ca63de0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca64360() {
   double input = -0.680248;
   input += synapse0x1ca646a0();
   input += synapse0x1ca646e0();
   input += synapse0x1ca64720();
   input += synapse0x1ca64760();
   input += synapse0x1ca647a0();
   input += synapse0x1ca647e0();
   input += synapse0x1ca64820();
   input += synapse0x1ca64860();
   input += synapse0x1ca648a0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca64360() {
   double input = input0x1ca64360();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca648e0() {
   double input = 0.0477673;
   input += synapse0x1ca64c20();
   input += synapse0x1ca64c60();
   input += synapse0x1ca64ca0();
   input += synapse0x1ca64ce0();
   input += synapse0x1ca64d20();
   input += synapse0x1ca64d60();
   input += synapse0x1ca64da0();
   input += synapse0x1ca64de0();
   input += synapse0x1ca64e20();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca648e0() {
   double input = input0x1ca648e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca64e60() {
   double input = 0.110013;
   input += synapse0x1ca5edc0();
   input += synapse0x1ca5ee00();
   input += synapse0x1ca5ee40();
   input += synapse0x1ca5ee80();
   input += synapse0x1ca653b0();
   input += synapse0x1ca653f0();
   input += synapse0x1ca65430();
   input += synapse0x1ca65470();
   input += synapse0x1ca654b0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca64e60() {
   double input = input0x1ca64e60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca654f0() {
   double input = 0.271156;
   input += synapse0x1ca65830();
   input += synapse0x1ca65870();
   input += synapse0x1ca658b0();
   input += synapse0x1ca658f0();
   input += synapse0x1ca65930();
   input += synapse0x1ca65970();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca654f0() {
   double input = input0x1ca654f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca659b0() {
   double input = 0.0293537;
   input += synapse0x1ca65cf0();
   input += synapse0x1ca65d30();
   input += synapse0x1ca65d70();
   input += synapse0x1ca65db0();
   input += synapse0x1ca65df0();
   input += synapse0x1ca65e30();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca659b0() {
   double input = input0x1ca659b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca65e70() {
   double input = -0.0792383;
   input += synapse0x1ca661b0();
   input += synapse0x1ca661f0();
   input += synapse0x1ca66230();
   input += synapse0x1ca66270();
   input += synapse0x1ca662b0();
   input += synapse0x1ca662f0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca65e70() {
   double input = input0x1ca65e70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1ca66330() {
   double input = -0.15943;
   input += synapse0x1ca66550();
   input += synapse0x1ca66590();
   input += synapse0x1ca665d0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1ca66330() {
   double input = input0x1ca66330();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5be90() {
   return (neuron0x1ca5a7c0()*-0.353815);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5bed0() {
   return (neuron0x1ca5aa70()*0.170272);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5bf10() {
   return (neuron0x1ca5adb0()*1.00017);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5bf50() {
   return (neuron0x1ca5b0f0()*-0.370854);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5bf90() {
   return (neuron0x1ca5b430()*0.936689);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5bfd0() {
   return (neuron0x1ca5b770()*0.344474);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c350() {
   return (neuron0x1ca5a7c0()*0.825059);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c390() {
   return (neuron0x1ca5aa70()*-0.676046);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c3d0() {
   return (neuron0x1ca5adb0()*-0.42661);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c410() {
   return (neuron0x1ca5b0f0()*-0.192055);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c450() {
   return (neuron0x1ca5b430()*1.25546);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c490() {
   return (neuron0x1ca5b770()*0.644279);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c810() {
   return (neuron0x1ca5a7c0()*0.654433);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c850() {
   return (neuron0x1ca5aa70()*1.66198);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c890() {
   return (neuron0x1ca5adb0()*-2.48814);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c8d0() {
   return (neuron0x1ca5b0f0()*-0.79154);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c910() {
   return (neuron0x1ca5b430()*0.499872);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c9a8270() {
   return (neuron0x1ca5b770()*-0.137821);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c9a82b0() {
   return (neuron0x1ca5a7c0()*-0.0489799);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5cda0() {
   return (neuron0x1ca5aa70()*0.490612);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5cde0() {
   return (neuron0x1ca5adb0()*0.518565);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5ce20() {
   return (neuron0x1ca5b0f0()*-0.980488);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5ce60() {
   return (neuron0x1ca5b430()*0.331811);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5cea0() {
   return (neuron0x1ca5b770()*0.0148684);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5d220() {
   return (neuron0x1ca5a7c0()*0.811245);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5d260() {
   return (neuron0x1ca5aa70()*0.494022);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5d2a0() {
   return (neuron0x1ca5adb0()*0.0317268);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5d2e0() {
   return (neuron0x1ca5b0f0()*-1.21947);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5d320() {
   return (neuron0x1ca5b430()*0.29712);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5d360() {
   return (neuron0x1ca5b770()*-0.295108);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5d6e0() {
   return (neuron0x1ca5a7c0()*-0.0331715);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5d720() {
   return (neuron0x1ca5aa70()*-0.394247);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5d760() {
   return (neuron0x1ca5adb0()*0.25673);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca49b40() {
   return (neuron0x1ca5b0f0()*0.836115);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c9b8030() {
   return (neuron0x1ca5b430()*0.323178);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c9a8650() {
   return (neuron0x1ca5b770()*-0.477245);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5c9e0() {
   return (neuron0x1ca5a7c0()*0.115592);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5ca20() {
   return (neuron0x1ca5aa70()*0.0919475);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5db40() {
   return (neuron0x1ca5adb0()*0.147539);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5db80() {
   return (neuron0x1ca5b0f0()*0.334577);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5dbc0() {
   return (neuron0x1ca5b430()*-0.263489);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5dc00() {
   return (neuron0x1ca5b770()*0.812386);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5df80() {
   return (neuron0x1ca5a7c0()*0.86916);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5dfc0() {
   return (neuron0x1ca5aa70()*0.641911);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e000() {
   return (neuron0x1ca5adb0()*-2.41273);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e040() {
   return (neuron0x1ca5b0f0()*0.395809);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e080() {
   return (neuron0x1ca5b430()*0.25692);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e0c0() {
   return (neuron0x1ca5b770()*-0.0212319);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e440() {
   return (neuron0x1ca5a7c0()*0.591311);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e480() {
   return (neuron0x1ca5aa70()*0.775978);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e4c0() {
   return (neuron0x1ca5adb0()*-2.30873);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e500() {
   return (neuron0x1ca5b0f0()*-0.815425);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e540() {
   return (neuron0x1ca5b430()*-0.125579);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e580() {
   return (neuron0x1ca5b770()*0.37859);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e900() {
   return (neuron0x1ca5a7c0()*-0.666062);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e940() {
   return (neuron0x1ca5aa70()*0.0652179);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e980() {
   return (neuron0x1ca5adb0()*-0.602585);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5e9c0() {
   return (neuron0x1ca5b0f0()*2.13163);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5ea00() {
   return (neuron0x1ca5b430()*-0.15076);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5ea40() {
   return (neuron0x1ca5b770()*-0.415346);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c9a80c0() {
   return (neuron0x1ca5a7c0()*-0.0708338);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1c9a8100() {
   return (neuron0x1ca5aa70()*0.876557);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5eed0() {
   return (neuron0x1ca5adb0()*-0.0481722);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5ef10() {
   return (neuron0x1ca5b0f0()*-1.53615);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5ef50() {
   return (neuron0x1ca5b430()*0.0291664);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5d7a0() {
   return (neuron0x1ca5b770()*-0.292204);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5d970() {
   return (neuron0x1ca5a7c0()*0.119794);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5f550() {
   return (neuron0x1ca5aa70()*-0.772332);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5f590() {
   return (neuron0x1ca5adb0()*-1.22096);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5f5d0() {
   return (neuron0x1ca5b0f0()*-0.611475);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5f610() {
   return (neuron0x1ca5b430()*1.4446);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5f650() {
   return (neuron0x1ca5b770()*0.323551);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5f9d0() {
   return (neuron0x1ca5bbe0()*0.736745);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5fa10() {
   return (neuron0x1ca5c010()*-0.0291903);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5fa50() {
   return (neuron0x1ca5c4d0()*-0.0516619);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5fa90() {
   return (neuron0x1ca5ca60()*0.328414);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5fad0() {
   return (neuron0x1ca5cee0()*-0.356765);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5fb10() {
   return (neuron0x1ca5d3a0()*0.105569);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5fb50() {
   return (neuron0x1ca5d9b0()*-0.451963);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5fb90() {
   return (neuron0x1ca5dc40()*0.267876);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5fbd0() {
   return (neuron0x1ca5e100()*-0.026707);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5fc10() {
   return (neuron0x1ca5e5c0()*-0.191121);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5fc50() {
   return (neuron0x1ca5ea80()*-0.126975);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5fc90() {
   return (neuron0x1ca5d7e0()*-0.563936);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60010() {
   return (neuron0x1ca5bbe0()*0.361071);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60050() {
   return (neuron0x1ca5c010()*-0.688781);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60090() {
   return (neuron0x1ca5c4d0()*0.784987);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca600d0() {
   return (neuron0x1ca5ca60()*0.413866);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60110() {
   return (neuron0x1ca5cee0()*0.228377);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60150() {
   return (neuron0x1ca5d3a0()*0.227095);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60190() {
   return (neuron0x1ca5d9b0()*0.0928625);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca601d0() {
   return (neuron0x1ca5dc40()*-1.30078);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60210() {
   return (neuron0x1ca5e100()*0.812997);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60250() {
   return (neuron0x1ca5e5c0()*-0.525417);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60290() {
   return (neuron0x1ca5ea80()*-0.47495);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca602d0() {
   return (neuron0x1ca5d7e0()*0.381863);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60650() {
   return (neuron0x1ca5bbe0()*0.588607);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60690() {
   return (neuron0x1ca5c010()*-0.829706);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca606d0() {
   return (neuron0x1ca5c4d0()*0.173879);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60710() {
   return (neuron0x1ca5ca60()*0.0724313);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60750() {
   return (neuron0x1ca5cee0()*0.0915354);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60790() {
   return (neuron0x1ca5d3a0()*0.281663);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca607d0() {
   return (neuron0x1ca5d9b0()*0.38661);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60810() {
   return (neuron0x1ca5dc40()*-1.33952);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60850() {
   return (neuron0x1ca5e100()*0.47519);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60890() {
   return (neuron0x1ca5e5c0()*-0.213025);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca608d0() {
   return (neuron0x1ca5ea80()*-0.252472);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60910() {
   return (neuron0x1ca5d7e0()*0.208455);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60c90() {
   return (neuron0x1ca5bbe0()*-0.629453);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60cd0() {
   return (neuron0x1ca5c010()*0.678428);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60d10() {
   return (neuron0x1ca5c4d0()*-0.850422);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60d50() {
   return (neuron0x1ca5ca60()*0.0511772);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60d90() {
   return (neuron0x1ca5cee0()*-0.273791);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60dd0() {
   return (neuron0x1ca5d3a0()*-0.185488);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60e10() {
   return (neuron0x1ca5d9b0()*-0.231436);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60e50() {
   return (neuron0x1ca5dc40()*1.18615);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60e90() {
   return (neuron0x1ca5e100()*-0.414598);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60ed0() {
   return (neuron0x1ca5e5c0()*-0.079186);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60f10() {
   return (neuron0x1ca5ea80()*0.207305);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca60f50() {
   return (neuron0x1ca5d7e0()*-0.454743);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca612d0() {
   return (neuron0x1ca5bbe0()*0.115397);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61310() {
   return (neuron0x1ca5c010()*0.164871);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61350() {
   return (neuron0x1ca5c4d0()*0.258162);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61390() {
   return (neuron0x1ca5ca60()*0.230612);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca613d0() {
   return (neuron0x1ca5cee0()*0.619123);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61410() {
   return (neuron0x1ca5d3a0()*-0.632136);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61450() {
   return (neuron0x1ca5d9b0()*-0.311799);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61490() {
   return (neuron0x1ca5dc40()*0.0558619);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca614d0() {
   return (neuron0x1ca5e100()*0.432654);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5ef90() {
   return (neuron0x1ca5e5c0()*-0.332534);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5efd0() {
   return (neuron0x1ca5ea80()*-0.0443237);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5f010() {
   return (neuron0x1ca5d7e0()*0.349896);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61d20() {
   return (neuron0x1ca5bbe0()*0.861959);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61d60() {
   return (neuron0x1ca5c010()*-0.159767);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61da0() {
   return (neuron0x1ca5c4d0()*0.244556);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61de0() {
   return (neuron0x1ca5ca60()*-0.106722);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61e20() {
   return (neuron0x1ca5cee0()*0.341346);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61e60() {
   return (neuron0x1ca5d3a0()*0.377302);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61ea0() {
   return (neuron0x1ca5d9b0()*0.375653);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61ee0() {
   return (neuron0x1ca5dc40()*-1.59955);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61f20() {
   return (neuron0x1ca5e100()*0.98465);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61f60() {
   return (neuron0x1ca5e5c0()*-0.538036);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61fa0() {
   return (neuron0x1ca5ea80()*-0.70508);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca61fe0() {
   return (neuron0x1ca5d7e0()*-0.378267);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62360() {
   return (neuron0x1ca5bbe0()*0.0145672);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca623a0() {
   return (neuron0x1ca5c010()*0.541401);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca623e0() {
   return (neuron0x1ca5c4d0()*0.424618);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62420() {
   return (neuron0x1ca5ca60()*0.297554);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62460() {
   return (neuron0x1ca5cee0()*0.358224);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca624a0() {
   return (neuron0x1ca5d3a0()*0.0685963);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca624e0() {
   return (neuron0x1ca5d9b0()*-0.135476);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62520() {
   return (neuron0x1ca5dc40()*0.3224);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62560() {
   return (neuron0x1ca5e100()*-0.101328);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca625a0() {
   return (neuron0x1ca5e5c0()*-0.467139);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca625e0() {
   return (neuron0x1ca5ea80()*0.559314);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62620() {
   return (neuron0x1ca5d7e0()*-0.0820615);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca629a0() {
   return (neuron0x1ca5bbe0()*-0.118865);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca629e0() {
   return (neuron0x1ca5c010()*0.152673);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62a20() {
   return (neuron0x1ca5c4d0()*0.396076);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62a60() {
   return (neuron0x1ca5ca60()*-0.826773);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62aa0() {
   return (neuron0x1ca5cee0()*0.529868);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62ae0() {
   return (neuron0x1ca5d3a0()*-0.226547);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62b20() {
   return (neuron0x1ca5d9b0()*-0.570651);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62b60() {
   return (neuron0x1ca5dc40()*-0.200784);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62ba0() {
   return (neuron0x1ca5e100()*0.0258732);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62be0() {
   return (neuron0x1ca5e5c0()*-0.571443);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62c20() {
   return (neuron0x1ca5ea80()*0.0347524);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62c60() {
   return (neuron0x1ca5d7e0()*0.432986);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca62fe0() {
   return (neuron0x1ca5bbe0()*-0.551628);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63020() {
   return (neuron0x1ca5c010()*1.60361);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63060() {
   return (neuron0x1ca5c4d0()*-1.14716);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca630a0() {
   return (neuron0x1ca5ca60()*0.957502);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca630e0() {
   return (neuron0x1ca5cee0()*0.0991849);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63120() {
   return (neuron0x1ca5d3a0()*-1.31208);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63160() {
   return (neuron0x1ca5d9b0()*-1.326);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca631a0() {
   return (neuron0x1ca5dc40()*1.45022);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca631e0() {
   return (neuron0x1ca5e100()*-0.17163);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63220() {
   return (neuron0x1ca5e5c0()*-2.04288);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63260() {
   return (neuron0x1ca5ea80()*2.09757);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca632a0() {
   return (neuron0x1ca5d7e0()*-0.934316);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63620() {
   return (neuron0x1ca5f690()*-0.210126);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63660() {
   return (neuron0x1ca5fcd0()*0.114146);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca636a0() {
   return (neuron0x1ca60310()*-0.453747);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca636e0() {
   return (neuron0x1ca60950()*0.385174);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63720() {
   return (neuron0x1ca60f90()*-0.503646);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63760() {
   return (neuron0x1ca5f050()*-0.477515);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca637a0() {
   return (neuron0x1ca62020()*0.260288);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca637e0() {
   return (neuron0x1ca62660()*-0.179993);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63820() {
   return (neuron0x1ca62ca0()*1.2239);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63ba0() {
   return (neuron0x1ca5f690()*-0.554097);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63be0() {
   return (neuron0x1ca5fcd0()*-0.517609);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63c20() {
   return (neuron0x1ca60310()*-0.389608);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63c60() {
   return (neuron0x1ca60950()*0.210168);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63ca0() {
   return (neuron0x1ca60f90()*0.127572);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63ce0() {
   return (neuron0x1ca5f050()*-0.299713);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63d20() {
   return (neuron0x1ca62020()*-0.274208);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63d60() {
   return (neuron0x1ca62660()*0.0707227);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca63da0() {
   return (neuron0x1ca62ca0()*0.657427);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64120() {
   return (neuron0x1ca5f690()*-0.502835);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64160() {
   return (neuron0x1ca5fcd0()*1.4006);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca641a0() {
   return (neuron0x1ca60310()*0.772327);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca641e0() {
   return (neuron0x1ca60950()*-1.81985);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64220() {
   return (neuron0x1ca60f90()*0.218056);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64260() {
   return (neuron0x1ca5f050()*1.76843);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca642a0() {
   return (neuron0x1ca62020()*-0.00238647);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca642e0() {
   return (neuron0x1ca62660()*-0.0835135);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64320() {
   return (neuron0x1ca62ca0()*-4.54038);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca646a0() {
   return (neuron0x1ca5f690()*0.217003);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca646e0() {
   return (neuron0x1ca5fcd0()*-0.406905);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64720() {
   return (neuron0x1ca60310()*0.154373);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64760() {
   return (neuron0x1ca60950()*1.01441);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca647a0() {
   return (neuron0x1ca60f90()*0.283446);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca647e0() {
   return (neuron0x1ca5f050()*-0.826947);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64820() {
   return (neuron0x1ca62020()*0.500192);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64860() {
   return (neuron0x1ca62660()*-0.373014);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca648a0() {
   return (neuron0x1ca62ca0()*1.03667);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64c20() {
   return (neuron0x1ca5f690()*1.03897);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64c60() {
   return (neuron0x1ca5fcd0()*0.530599);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64ca0() {
   return (neuron0x1ca60310()*0.181898);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64ce0() {
   return (neuron0x1ca60950()*0.498963);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64d20() {
   return (neuron0x1ca60f90()*0.0910804);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64d60() {
   return (neuron0x1ca5f050()*0.233226);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64da0() {
   return (neuron0x1ca62020()*0.895023);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64de0() {
   return (neuron0x1ca62660()*0.104448);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca64e20() {
   return (neuron0x1ca62ca0()*0.146414);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5edc0() {
   return (neuron0x1ca5f690()*-0.776394);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5ee00() {
   return (neuron0x1ca5fcd0()*-1.23798);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5ee40() {
   return (neuron0x1ca60310()*-1.18905);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca5ee80() {
   return (neuron0x1ca60950()*-1.08688);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca653b0() {
   return (neuron0x1ca60f90()*-0.262002);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca653f0() {
   return (neuron0x1ca5f050()*0.0941113);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65430() {
   return (neuron0x1ca62020()*-0.103659);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65470() {
   return (neuron0x1ca62660()*0.410103);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca654b0() {
   return (neuron0x1ca62ca0()*1.55839);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65830() {
   return (neuron0x1ca632e0()*1.7456);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65870() {
   return (neuron0x1ca63860()*1.0944);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca658b0() {
   return (neuron0x1ca63de0()*-3.81127);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca658f0() {
   return (neuron0x1ca64360()*0.675101);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65930() {
   return (neuron0x1ca648e0()*-0.435656);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65970() {
   return (neuron0x1ca64e60()*1.16258);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65cf0() {
   return (neuron0x1ca632e0()*0.0115586);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65d30() {
   return (neuron0x1ca63860()*-1.83135);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65d70() {
   return (neuron0x1ca63de0()*2.86874);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65db0() {
   return (neuron0x1ca64360()*-1.39902);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65df0() {
   return (neuron0x1ca648e0()*1.12897);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca65e30() {
   return (neuron0x1ca64e60()*-2.73726);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca661b0() {
   return (neuron0x1ca632e0()*-0.422741);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca661f0() {
   return (neuron0x1ca63860()*-0.202768);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca66230() {
   return (neuron0x1ca63de0()*2.36101);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca66270() {
   return (neuron0x1ca64360()*-0.0427773);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca662b0() {
   return (neuron0x1ca648e0()*-0.252003);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca662f0() {
   return (neuron0x1ca64e60()*-0.252152);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca66550() {
   return (neuron0x1ca654f0()*4.69306);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca66590() {
   return (neuron0x1ca659b0()*-2.89429);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1ca665d0() {
   return (neuron0x1ca65e70()*-2.26607);
}

