#include "MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.500017)/0.25242;
   input1 = (in1 - 0.592179)/0.338539;
   input2 = (in2 - 0.679468)/0.281065;
   switch(index) {
     case 0:
         return neuron0x136ce990();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::Value(int index, double* input) {
   input0 = (input[0] - 0.500017)/0.25242;
   input1 = (input[1] - 0.592179)/0.338539;
   input2 = (input[2] - 0.679468)/0.281065;
   switch(index) {
     case 0:
         return neuron0x136ce990();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136caa00() {
   return input0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136cad40() {
   return input1;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136cb080() {
   return input2;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136cb3c0() {
   double input = -1.45806;
   input += synapse0x1366fb80();
   input += synapse0x136cb670();
   input += synapse0x136cb6b0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136cb3c0() {
   double input = input0x136cb3c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136cb6f0() {
   double input = -0.768892;
   input += synapse0x136cba30();
   input += synapse0x136cba70();
   input += synapse0x136cbab0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136cb6f0() {
   double input = input0x136cb6f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136cbaf0() {
   double input = -1.0523;
   input += synapse0x136cbe30();
   input += synapse0x136cbe70();
   input += synapse0x136cbeb0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136cbaf0() {
   double input = input0x136cbaf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136cbef0() {
   double input = 0.741483;
   input += synapse0x136cc230();
   input += synapse0x136cc270();
   input += synapse0x136cc2b0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136cbef0() {
   double input = input0x136cbef0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136cc2f0() {
   double input = -0.466653;
   input += synapse0x136cc630();
   input += synapse0x136cc670();
   input += synapse0x136cc6b0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136cc2f0() {
   double input = input0x136cc2f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136cc6f0() {
   double input = -0.651768;
   input += synapse0x136cca30();
   input += synapse0x136cca70();
   input += synapse0x1365fdc0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136cc6f0() {
   double input = input0x136cc6f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136ccbc0() {
   double input = -1.10573;
   input += synapse0x136ccf00();
   input += synapse0x136ccf40();
   input += synapse0x136ccf80();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136ccbc0() {
   double input = input0x136ccbc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136ccfc0() {
   double input = 0.918854;
   input += synapse0x136cd300();
   input += synapse0x136cd340();
   input += synapse0x136cd380();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136ccfc0() {
   double input = input0x136ccfc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136cd3c0() {
   double input = -0.0641341;
   input += synapse0x136cd700();
   input += synapse0x136cd740();
   input += synapse0x136cd780();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136cd3c0() {
   double input = input0x136cd3c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136cd7c0() {
   double input = 0.77846;
   input += synapse0x136cdb00();
   input += synapse0x136cdb40();
   input += synapse0x136cdb80();
   input += synapse0x136cdbc0();
   input += synapse0x136cdc00();
   input += synapse0x136cdc40();
   input += synapse0x1365fe00();
   input += synapse0x13660200();
   input += synapse0x136602e0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136cd7c0() {
   double input = input0x136cd7c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136cde90() {
   double input = -1.38461;
   input += synapse0x136ce1d0();
   input += synapse0x136ce210();
   input += synapse0x136ce250();
   input += synapse0x136ce290();
   input += synapse0x136ce2d0();
   input += synapse0x136ce310();
   input += synapse0x136ce350();
   input += synapse0x136ce390();
   input += synapse0x136ce3d0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136cde90() {
   double input = input0x136cde90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136ce410() {
   double input = -0.287511;
   input += synapse0x136ce750();
   input += synapse0x136ce790();
   input += synapse0x136ce7d0();
   input += synapse0x136ce810();
   input += synapse0x136ce850();
   input += synapse0x136ce890();
   input += synapse0x136ce8d0();
   input += synapse0x136ce910();
   input += synapse0x136ce950();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136ce410() {
   double input = input0x136ce410();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::input0x136ce990() {
   double input = 1.34852;
   input += synapse0x136cecd0();
   input += synapse0x136ced10();
   input += synapse0x136ced50();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::neuron0x136ce990() {
   double input = input0x136ce990();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x1366fb80() {
   return (neuron0x136caa00()*-0.20565);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cb670() {
   return (neuron0x136cad40()*0.0777419);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cb6b0() {
   return (neuron0x136cb080()*1.03242);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cba30() {
   return (neuron0x136caa00()*-0.281481);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cba70() {
   return (neuron0x136cad40()*-0.531079);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cbab0() {
   return (neuron0x136cb080()*0.798855);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cbe30() {
   return (neuron0x136caa00()*-0.571457);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cbe70() {
   return (neuron0x136cad40()*-0.304806);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cbeb0() {
   return (neuron0x136cb080()*1.2937);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cc230() {
   return (neuron0x136caa00()*0.011078);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cc270() {
   return (neuron0x136cad40()*0.289356);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cc2b0() {
   return (neuron0x136cb080()*-0.724542);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cc630() {
   return (neuron0x136caa00()*-0.553766);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cc670() {
   return (neuron0x136cad40()*0.467186);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cc6b0() {
   return (neuron0x136cb080()*-0.186003);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cca30() {
   return (neuron0x136caa00()*-0.288457);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cca70() {
   return (neuron0x136cad40()*-0.430509);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x1365fdc0() {
   return (neuron0x136cb080()*-0.212088);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ccf00() {
   return (neuron0x136caa00()*0.467024);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ccf40() {
   return (neuron0x136cad40()*-0.9291);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ccf80() {
   return (neuron0x136cb080()*-0.212492);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cd300() {
   return (neuron0x136caa00()*0.543042);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cd340() {
   return (neuron0x136cad40()*-0.917385);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cd380() {
   return (neuron0x136cb080()*-0.376285);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cd700() {
   return (neuron0x136caa00()*-0.0333071);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cd740() {
   return (neuron0x136cad40()*0.213805);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cd780() {
   return (neuron0x136cb080()*-0.192208);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cdb00() {
   return (neuron0x136cb3c0()*1.60743);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cdb40() {
   return (neuron0x136cb6f0()*-1.04442);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cdb80() {
   return (neuron0x136cbaf0()*-1.39612);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cdbc0() {
   return (neuron0x136cbef0()*-1.40995);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cdc00() {
   return (neuron0x136cc2f0()*-0.560093);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cdc40() {
   return (neuron0x136cc6f0()*-0.668486);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x1365fe00() {
   return (neuron0x136ccbc0()*-1.01784);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x13660200() {
   return (neuron0x136ccfc0()*1.35918);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136602e0() {
   return (neuron0x136cd3c0()*-1.17116);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce1d0() {
   return (neuron0x136cb3c0()*-1.63514);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce210() {
   return (neuron0x136cb6f0()*1.13727);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce250() {
   return (neuron0x136cbaf0()*1.00397);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce290() {
   return (neuron0x136cbef0()*1.59581);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce2d0() {
   return (neuron0x136cc2f0()*-0.0460608);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce310() {
   return (neuron0x136cc6f0()*0.843075);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce350() {
   return (neuron0x136ccbc0()*1.41318);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce390() {
   return (neuron0x136ccfc0()*-2.15426);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce3d0() {
   return (neuron0x136cd3c0()*1.5814);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce750() {
   return (neuron0x136cb3c0()*-1.23811);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce790() {
   return (neuron0x136cb6f0()*0.702581);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce7d0() {
   return (neuron0x136cbaf0()*0.401896);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce810() {
   return (neuron0x136cbef0()*0.441683);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce850() {
   return (neuron0x136cc2f0()*0.334033);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce890() {
   return (neuron0x136cc6f0()*0.509851);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce8d0() {
   return (neuron0x136ccbc0()*0.795843);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce910() {
   return (neuron0x136ccfc0()*-0.734003);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ce950() {
   return (neuron0x136cd3c0()*0.921218);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136cecd0() {
   return (neuron0x136cd7c0()*9.03548);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ced10() {
   return (neuron0x136cde90()*-5.72764);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21::synapse0x136ced50() {
   return (neuron0x136ce410()*-1.5543);
}

