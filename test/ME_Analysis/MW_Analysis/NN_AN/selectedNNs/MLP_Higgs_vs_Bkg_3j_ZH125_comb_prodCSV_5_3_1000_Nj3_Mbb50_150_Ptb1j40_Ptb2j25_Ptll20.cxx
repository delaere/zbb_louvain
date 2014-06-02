#include "MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 0.46033)/0.237691;
   input1 = (in1 - 0.512403)/0.275496;
   input2 = (in2 - 0.527936)/0.286352;
   input3 = (in3 - 0.639559)/0.256908;
   switch(index) {
     case 0:
         return neuron0x35da7aa0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 0.46033)/0.237691;
   input1 = (input[1] - 0.512403)/0.275496;
   input2 = (input[2] - 0.527936)/0.286352;
   input3 = (input[3] - 0.639559)/0.256908;
   switch(index) {
     case 0:
         return neuron0x35da7aa0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da48e0() {
   return input0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da4c20() {
   return input1;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da4f60() {
   return input2;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da52a0() {
   return input3;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x35da5710() {
   double input = -1.02591;
   input += synapse0x35d93b40();
   input += synapse0x35d21ba0();
   input += synapse0x35d21be0();
   input += synapse0x35da59c0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da5710() {
   double input = input0x35da5710();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x35da5a00() {
   double input = 3.83862;
   input += synapse0x35da5d40();
   input += synapse0x35da5d80();
   input += synapse0x35da5dc0();
   input += synapse0x35da5e00();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da5a00() {
   double input = input0x35da5a00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x35da5e40() {
   double input = 4.24296;
   input += synapse0x35da6180();
   input += synapse0x35da61c0();
   input += synapse0x35da6200();
   input += synapse0x35da6240();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da5e40() {
   double input = input0x35da5e40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x35da6280() {
   double input = 3.5656;
   input += synapse0x35da65c0();
   input += synapse0x35da6600();
   input += synapse0x35da6640();
   input += synapse0x35da6680();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da6280() {
   double input = input0x35da6280();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x35da66c0() {
   double input = -1.62931;
   input += synapse0x35da6a00();
   input += synapse0x35d21700();
   input += synapse0x35d21740();
   input += synapse0x35da6b50();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da66c0() {
   double input = input0x35da66c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x35da6b90() {
   double input = 0.932811;
   input += synapse0x35da6ed0();
   input += synapse0x35da6f10();
   input += synapse0x35da6f50();
   input += synapse0x35da6f90();
   input += synapse0x35da6fd0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da6b90() {
   double input = input0x35da6b90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x35da7010() {
   double input = -0.989269;
   input += synapse0x35da7350();
   input += synapse0x35da7390();
   input += synapse0x35da73d0();
   input += synapse0x35da7410();
   input += synapse0x35da7450();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da7010() {
   double input = input0x35da7010();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x35da7490() {
   double input = -0.563702;
   input += synapse0x35da77d0();
   input += synapse0x35da7810();
   input += synapse0x35da7850();
   input += synapse0x35d21b50();
   input += synapse0x35d93ac0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da7490() {
   double input = input0x35da7490();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x35da7aa0() {
   double input = 3.03419;
   input += synapse0x35d93b00();
   input += synapse0x35da5670();
   input += synapse0x35da56b0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x35da7aa0() {
   double input = input0x35da7aa0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35d93b40() {
   return (neuron0x35da48e0()*-0.432204);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35d21ba0() {
   return (neuron0x35da4c20()*0.454449);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35d21be0() {
   return (neuron0x35da4f60()*1.01856);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da59c0() {
   return (neuron0x35da52a0()*-0.130958);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da5d40() {
   return (neuron0x35da48e0()*0.995659);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da5d80() {
   return (neuron0x35da4c20()*0.995967);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da5dc0() {
   return (neuron0x35da4f60()*0.0842328);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da5e00() {
   return (neuron0x35da52a0()*-0.33623);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6180() {
   return (neuron0x35da48e0()*-1.16313);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da61c0() {
   return (neuron0x35da4c20()*0.0745181);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6200() {
   return (neuron0x35da4f60()*-0.676147);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6240() {
   return (neuron0x35da52a0()*-0.22729);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da65c0() {
   return (neuron0x35da48e0()*0.337888);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6600() {
   return (neuron0x35da4c20()*-0.780896);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6640() {
   return (neuron0x35da4f60()*1.29326);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6680() {
   return (neuron0x35da52a0()*-0.528718);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6a00() {
   return (neuron0x35da48e0()*-0.557046);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35d21700() {
   return (neuron0x35da4c20()*-0.232388);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35d21740() {
   return (neuron0x35da4f60()*-0.394391);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6b50() {
   return (neuron0x35da52a0()*-0.895533);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6ed0() {
   return (neuron0x35da5710()*-0.250882);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6f10() {
   return (neuron0x35da5a00()*-1.24711);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6f50() {
   return (neuron0x35da5e40()*2.0887);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6f90() {
   return (neuron0x35da6280()*-1.24785);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da6fd0() {
   return (neuron0x35da66c0()*0.707453);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da7350() {
   return (neuron0x35da5710()*1.03249);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da7390() {
   return (neuron0x35da5a00()*1.02468);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da73d0() {
   return (neuron0x35da5e40()*-2.42174);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da7410() {
   return (neuron0x35da6280()*1.05023);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da7450() {
   return (neuron0x35da66c0()*-1.43649);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da77d0() {
   return (neuron0x35da5710()*2.53838);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da7810() {
   return (neuron0x35da5a00()*-2.94391);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da7850() {
   return (neuron0x35da5e40()*4.2163);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35d21b50() {
   return (neuron0x35da6280()*-3.34918);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35d93ac0() {
   return (neuron0x35da66c0()*1.1416);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35d93b00() {
   return (neuron0x35da6b90()*-3.1046);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da5670() {
   return (neuron0x35da7010()*4.51598);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x35da56b0() {
   return (neuron0x35da7490()*-9.70837);
}

