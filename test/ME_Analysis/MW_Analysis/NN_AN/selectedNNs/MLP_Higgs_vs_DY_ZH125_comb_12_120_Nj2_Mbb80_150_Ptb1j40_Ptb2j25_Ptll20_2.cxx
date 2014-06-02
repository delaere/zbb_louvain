#include "MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2.h"
#include <cmath>

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.5711)/0.977992;
   input1 = (in1 - 20.2766)/0.818811;
   input2 = (in2 - 24.2646)/1.23737;
   input3 = (in3 - 12.5907)/0.782629;
   switch(index) {
     case 0:
         return neuron0x24a38250();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::Value(int index, double* input) {
   input0 = (input[0] - 19.5711)/0.977992;
   input1 = (input[1] - 20.2766)/0.818811;
   input2 = (input[2] - 24.2646)/1.23737;
   input3 = (input[3] - 12.5907)/0.782629;
   switch(index) {
     case 0:
         return neuron0x24a38250();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a34050() {
   return input0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a34390() {
   return input1;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a346d0() {
   return input2;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a34a10() {
   return input3;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a34e80() {
   double input = 0.244718;
   input += synapse0x24a3cd20();
   input += synapse0x24a35130();
   input += synapse0x24a35170();
   input += synapse0x24a351b0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a34e80() {
   double input = input0x24a34e80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a351f0() {
   double input = 0.638656;
   input += synapse0x24a35530();
   input += synapse0x24a35570();
   input += synapse0x24a355b0();
   input += synapse0x24a355f0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a351f0() {
   double input = input0x24a351f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a35630() {
   double input = 0.216967;
   input += synapse0x24a35970();
   input += synapse0x24a359b0();
   input += synapse0x24a359f0();
   input += synapse0x24a35a30();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a35630() {
   double input = input0x24a35630();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a35a70() {
   double input = -0.633879;
   input += synapse0x24a35db0();
   input += synapse0x24a35df0();
   input += synapse0x24a35e30();
   input += synapse0x24a35e70();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a35a70() {
   double input = input0x24a35a70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a35eb0() {
   double input = 0.837594;
   input += synapse0x24a361f0();
   input += synapse0x24a3cd60();
   input += synapse0x17e31ed0();
   input += synapse0x17e31f10();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a35eb0() {
   double input = input0x24a35eb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a36340() {
   double input = 1.16185;
   input += synapse0x24a36680();
   input += synapse0x24a366c0();
   input += synapse0x24a36700();
   input += synapse0x24a36740();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a36340() {
   double input = input0x24a36340();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a36780() {
   double input = -1.44389;
   input += synapse0x24a36ac0();
   input += synapse0x24a36b00();
   input += synapse0x24a36b40();
   input += synapse0x24a36b80();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a36780() {
   double input = input0x24a36780();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a36bc0() {
   double input = 0.862406;
   input += synapse0x24a36f00();
   input += synapse0x24a36f40();
   input += synapse0x24a36f80();
   input += synapse0x24a36fc0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a36bc0() {
   double input = input0x24a36bc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a37000() {
   double input = 0.476175;
   input += synapse0x24a37340();
   input += synapse0x17e322e0();
   input += synapse0x24a0ccd0();
   input += synapse0x24a0cd10();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a37000() {
   double input = input0x24a37000();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a37590() {
   double input = 0.0225882;
   input += synapse0x24a378d0();
   input += synapse0x24a37910();
   input += synapse0x24a37950();
   input += synapse0x24a37990();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a37590() {
   double input = input0x24a37590();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a379d0() {
   double input = -0.31207;
   input += synapse0x24a37d10();
   input += synapse0x24a37d50();
   input += synapse0x24a37d90();
   input += synapse0x24a37dd0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a379d0() {
   double input = input0x24a379d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a37e10() {
   double input = 0.391683;
   input += synapse0x24a38150();
   input += synapse0x24a38190();
   input += synapse0x24a381d0();
   input += synapse0x24a38210();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a37e10() {
   double input = input0x24a37e10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::input0x24a38250() {
   double input = 0.653114;
   input += synapse0x24a38590();
   input += synapse0x24a385d0();
   input += synapse0x24a38610();
   input += synapse0x24a38650();
   input += synapse0x24a38690();
   input += synapse0x24a386d0();
   input += synapse0x24a38710();
   input += synapse0x24a38750();
   input += synapse0x24a38790();
   input += synapse0x24a387d0();
   input += synapse0x24a38810();
   input += synapse0x24a38850();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::neuron0x24a38250() {
   double input = input0x24a38250();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a3cd20() {
   return (neuron0x24a34050()*-0.313444);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a35130() {
   return (neuron0x24a34390()*0.254269);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a35170() {
   return (neuron0x24a346d0()*-0.140457);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a351b0() {
   return (neuron0x24a34a10()*0.941615);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a35530() {
   return (neuron0x24a34050()*0.183672);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a35570() {
   return (neuron0x24a34390()*-1.31587);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a355b0() {
   return (neuron0x24a346d0()*-0.360918);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a355f0() {
   return (neuron0x24a34a10()*1.4911);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a35970() {
   return (neuron0x24a34050()*0.222196);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a359b0() {
   return (neuron0x24a34390()*-0.167023);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a359f0() {
   return (neuron0x24a346d0()*0.585595);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a35a30() {
   return (neuron0x24a34a10()*-0.217972);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a35db0() {
   return (neuron0x24a34050()*0.454001);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a35df0() {
   return (neuron0x24a34390()*-0.0637628);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a35e30() {
   return (neuron0x24a346d0()*-0.149209);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a35e70() {
   return (neuron0x24a34a10()*-1.92397);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a361f0() {
   return (neuron0x24a34050()*0.562058);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a3cd60() {
   return (neuron0x24a34390()*-0.018284);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x17e31ed0() {
   return (neuron0x24a346d0()*-0.870783);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x17e31f10() {
   return (neuron0x24a34a10()*-0.0362116);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a36680() {
   return (neuron0x24a34050()*-0.197269);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a366c0() {
   return (neuron0x24a34390()*-1.13907);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a36700() {
   return (neuron0x24a346d0()*0.391518);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a36740() {
   return (neuron0x24a34a10()*0.28271);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a36ac0() {
   return (neuron0x24a34050()*-2.5024);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a36b00() {
   return (neuron0x24a34390()*2.02869);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a36b40() {
   return (neuron0x24a346d0()*0.660873);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a36b80() {
   return (neuron0x24a34a10()*-0.720041);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a36f00() {
   return (neuron0x24a34050()*0.476874);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a36f40() {
   return (neuron0x24a34390()*0.295996);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a36f80() {
   return (neuron0x24a346d0()*-0.357037);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a36fc0() {
   return (neuron0x24a34a10()*-0.655346);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a37340() {
   return (neuron0x24a34050()*0.586445);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x17e322e0() {
   return (neuron0x24a34390()*0.103591);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a0ccd0() {
   return (neuron0x24a346d0()*-0.364288);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a0cd10() {
   return (neuron0x24a34a10()*-1.22428);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a378d0() {
   return (neuron0x24a34050()*1.67802);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a37910() {
   return (neuron0x24a34390()*0.136795);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a37950() {
   return (neuron0x24a346d0()*-0.639887);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a37990() {
   return (neuron0x24a34a10()*-1.42471);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a37d10() {
   return (neuron0x24a34050()*-1.16364);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a37d50() {
   return (neuron0x24a34390()*-1.17647);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a37d90() {
   return (neuron0x24a346d0()*3.61525);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a37dd0() {
   return (neuron0x24a34a10()*-0.0913012);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38150() {
   return (neuron0x24a34050()*-1.29886);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38190() {
   return (neuron0x24a34390()*-0.274124);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a381d0() {
   return (neuron0x24a346d0()*1.1995);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38210() {
   return (neuron0x24a34a10()*1.73493);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38590() {
   return (neuron0x24a34e80()*-1.18698);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a385d0() {
   return (neuron0x24a351f0()*-2.85439);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38610() {
   return (neuron0x24a35630()*-0.291235);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38650() {
   return (neuron0x24a35a70()*0.7626);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38690() {
   return (neuron0x24a35eb0()*2.65399);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a386d0() {
   return (neuron0x24a36340()*-1.93391);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38710() {
   return (neuron0x24a36780()*-3.30073);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38750() {
   return (neuron0x24a36bc0()*1.87909);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38790() {
   return (neuron0x24a37000()*0.058986);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a387d0() {
   return (neuron0x24a37590()*-0.259473);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38810() {
   return (neuron0x24a379d0()*1.92949);
}

double MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2::synapse0x24a38850() {
   return (neuron0x24a37e10()*0.112681);
}

