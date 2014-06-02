#include "MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125.h"
#include <cmath>

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.4354)/2.00854;
   input1 = (in1 - 24.6518)/1.39453;
   input2 = (in2 - 13.1691)/1.61596;
   switch(index) {
     case 0:
         return neuron0x12161e30();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::Value(int index, double* input) {
   input0 = (input[0] - 22.4354)/2.00854;
   input1 = (input[1] - 24.6518)/1.39453;
   input2 = (input[2] - 13.1691)/1.61596;
   switch(index) {
     case 0:
         return neuron0x12161e30();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x1214e6d0() {
   return input0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x1214ea10() {
   return input1;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x1215f950() {
   return input2;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::input0x1215fd30() {
   double input = -0.137108;
   input += synapse0x12135390();
   input += synapse0x12116e10();
   input += synapse0x1215ffe0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x1215fd30() {
   double input = input0x1215fd30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::input0x12160020() {
   double input = 0.289962;
   input += synapse0x12160360();
   input += synapse0x121603a0();
   input += synapse0x121603e0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x12160020() {
   double input = input0x12160020();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::input0x12160420() {
   double input = 0.133216;
   input += synapse0x12160760();
   input += synapse0x121607a0();
   input += synapse0x121607e0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x12160420() {
   double input = input0x12160420();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::input0x12160820() {
   double input = 0.206899;
   input += synapse0x12160b60();
   input += synapse0x12160ba0();
   input += synapse0x12160be0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x12160820() {
   double input = input0x12160820();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::input0x12160c20() {
   double input = -4.1134;
   input += synapse0x12160f60();
   input += synapse0x12160fa0();
   input += synapse0x12160fe0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x12160c20() {
   double input = input0x12160c20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::input0x12161020() {
   double input = -1.77511;
   input += synapse0x12161360();
   input += synapse0x121613a0();
   input += synapse0x12116990();
   input += synapse0x121169d0();
   input += synapse0x121614f0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x12161020() {
   double input = input0x12161020();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::input0x12161530() {
   double input = 1.41998;
   input += synapse0x12161870();
   input += synapse0x121618b0();
   input += synapse0x121618f0();
   input += synapse0x12161930();
   input += synapse0x12161970();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x12161530() {
   double input = input0x12161530();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::input0x121619b0() {
   double input = -3.12755;
   input += synapse0x12161cf0();
   input += synapse0x12161d30();
   input += synapse0x12161d70();
   input += synapse0x12161db0();
   input += synapse0x12161df0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x121619b0() {
   double input = input0x121619b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::input0x12161e30() {
   double input = 0.812242;
   input += synapse0x12162050();
   input += synapse0x12162090();
   input += synapse0x121620d0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::neuron0x12161e30() {
   double input = input0x12161e30();
   return (input * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12135390() {
   return (neuron0x1214e6d0()*-1.21304);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12116e10() {
   return (neuron0x1214ea10()*1.68715);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x1215ffe0() {
   return (neuron0x1215f950()*-0.981722);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12160360() {
   return (neuron0x1214e6d0()*0.588685);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x121603a0() {
   return (neuron0x1214ea10()*8.86322);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x121603e0() {
   return (neuron0x1215f950()*-3.84115);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12160760() {
   return (neuron0x1214e6d0()*-0.829379);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x121607a0() {
   return (neuron0x1214ea10()*4.16628);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x121607e0() {
   return (neuron0x1215f950()*-3.39162);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12160b60() {
   return (neuron0x1214e6d0()*5.62101);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12160ba0() {
   return (neuron0x1214ea10()*3.49448);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12160be0() {
   return (neuron0x1215f950()*-6.96072);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12160f60() {
   return (neuron0x1214e6d0()*-2.19142);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12160fa0() {
   return (neuron0x1214ea10()*1.75361);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12160fe0() {
   return (neuron0x1215f950()*-4.53499);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12161360() {
   return (neuron0x1215fd30()*-0.408253);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x121613a0() {
   return (neuron0x12160020()*0.105021);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12116990() {
   return (neuron0x12160420()*-0.0846583);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x121169d0() {
   return (neuron0x12160820()*0.707311);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x121614f0() {
   return (neuron0x12160c20()*1.53098);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12161870() {
   return (neuron0x1215fd30()*-5.63232);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x121618b0() {
   return (neuron0x12160020()*8.05422);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x121618f0() {
   return (neuron0x12160420()*-1.19837);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12161930() {
   return (neuron0x12160820()*2.97017);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12161970() {
   return (neuron0x12160c20()*4.04014);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12161cf0() {
   return (neuron0x1215fd30()*6.14196);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12161d30() {
   return (neuron0x12160020()*0.887176);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12161d70() {
   return (neuron0x12160420()*-1.7303);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12161db0() {
   return (neuron0x12160820()*-1.83921);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12161df0() {
   return (neuron0x12160c20()*-2.9483);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12162050() {
   return (neuron0x12161020()*-1.25399);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x12162090() {
   return (neuron0x12161530()*0.531111);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125::synapse0x121620d0() {
   return (neuron0x121619b0()*-1.39914);
}

