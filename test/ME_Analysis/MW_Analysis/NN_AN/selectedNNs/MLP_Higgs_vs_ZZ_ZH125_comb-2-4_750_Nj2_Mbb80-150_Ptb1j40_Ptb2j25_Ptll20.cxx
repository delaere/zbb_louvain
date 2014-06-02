#include "MLP_Higgs_vs_ZZ_ZH125_comb-2-4_750_Nj2_Mbb80-150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.1193)/1.28039;
   input1 = (in1 - 10.8967)/1.04615;
   input2 = (in2 - 24.4553)/1.1302;
   input3 = (in3 - 12.6886)/0.870338;
   switch(index) {
     case 0:
         return neuron0x2a6a63a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 21.1193)/1.28039;
   input1 = (input[1] - 10.8967)/1.04615;
   input2 = (input[2] - 24.4553)/1.1302;
   input3 = (input[3] - 12.6886)/0.870338;
   switch(index) {
     case 0:
         return neuron0x2a6a63a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2a6a3ec0() {
   return input0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2a6a4200() {
   return input1;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2a6a4540() {
   return input2;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2a6a4880() {
   return input3;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2a6a4cf0() {
   double input = -1.14901;
   input += synapse0x2a67ca50();
   input += synapse0x2a6a4fa0();
   input += synapse0x2a6a4fe0();
   input += synapse0x2a6a5020();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2a6a4cf0() {
   double input = input0x2a6a4cf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2a6a5060() {
   double input = -1.19692;
   input += synapse0x2a6a53a0();
   input += synapse0x2a6a53e0();
   input += synapse0x2a6a5420();
   input += synapse0x2a6a5460();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2a6a5060() {
   double input = input0x2a6a5060();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2a6a54a0() {
   double input = -7.26315;
   input += synapse0x2a6a57e0();
   input += synapse0x2a6a5820();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2a6a54a0() {
   double input = input0x2a6a54a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2a6a5860() {
   double input = 2.08904;
   input += synapse0x2a6a5ba0();
   input += synapse0x2a6a5be0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2a6a5860() {
   double input = input0x2a6a5860();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2a6a5c20() {
   double input = 1.47028;
   input += synapse0x2a6a5f60();
   input += synapse0x2a6a5fa0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2a6a5c20() {
   double input = input0x2a6a5c20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2a6a5fe0() {
   double input = -0.0858749;
   input += synapse0x2a6a6320();
   input += synapse0x2a6a6360();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2a6a5fe0() {
   double input = input0x2a6a5fe0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2a6a63a0() {
   double input = 0.303812;
   input += synapse0x2a6a66e0();
   input += synapse0x293ac0f0();
   input += synapse0x293ac130();
   input += synapse0x2a6a4bc0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2a6a63a0() {
   double input = input0x2a6a63a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a67ca50() {
   return (neuron0x2a6a3ec0()*0.116502);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a4fa0() {
   return (neuron0x2a6a4200()*-0.982646);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a4fe0() {
   return (neuron0x2a6a4540()*0.606143);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a5020() {
   return (neuron0x2a6a4880()*0.141795);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a53a0() {
   return (neuron0x2a6a3ec0()*0.099688);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a53e0() {
   return (neuron0x2a6a4200()*-1.08078);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a5420() {
   return (neuron0x2a6a4540()*-0.913825);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a5460() {
   return (neuron0x2a6a4880()*1.90247);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a57e0() {
   return (neuron0x2a6a4cf0()*12.6531);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a5820() {
   return (neuron0x2a6a5060()*-2.39328);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a5ba0() {
   return (neuron0x2a6a4cf0()*1.20778);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a5be0() {
   return (neuron0x2a6a5060()*-5.32313);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a5f60() {
   return (neuron0x2a6a4cf0()*0.703596);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a5fa0() {
   return (neuron0x2a6a5060()*0.342612);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a6320() {
   return (neuron0x2a6a4cf0()*7.8293);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a6360() {
   return (neuron0x2a6a5060()*4.66366);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a66e0() {
   return (neuron0x2a6a54a0()*-10.958);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x293ac0f0() {
   return (neuron0x2a6a5860()*3.09474);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x293ac130() {
   return (neuron0x2a6a5c20()*6.35123);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_2_4_750_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2a6a4bc0() {
   return (neuron0x2a6a5fe0()*-7.5753);
}

