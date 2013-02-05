#include "../NN/MLP_Higgs_vs_ZZ_MM_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.2955)/1.35928;
   input1 = (in1 - 11.4941)/1.20924;
   input2 = (in2 - 24.681)/1.24004;
   input3 = (in3 - 13.2657)/1.32035;
   switch(index) {
     case 0:
         return neuron0xbf34c90();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 21.2955)/1.35928;
   input1 = (input[1] - 11.4941)/1.20924;
   input2 = (input[2] - 24.681)/1.24004;
   input3 = (input[3] - 13.2657)/1.32035;
   switch(index) {
     case 0:
         return neuron0xbf34c90();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf31c90() {
   return input0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf31fa0() {
   return input1;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf322b0() {
   return input2;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf325c0() {
   return input3;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::input0xbf32a10() {
   double input = 1.2724;
   input += synapse0xbedabe0();
   input += synapse0xbf32c90();
   input += synapse0xbf32cd0();
   input += synapse0xbf32d10();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf32a10() {
   double input = input0xbf32a10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::input0xbf32d50() {
   double input = 8.39526;
   input += synapse0xbf33060();
   input += synapse0xbf330a0();
   input += synapse0xbf330e0();
   input += synapse0xbf33120();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf32d50() {
   double input = input0xbf32d50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::input0xbf33160() {
   double input = -1.4867;
   input += synapse0xbf33470();
   input += synapse0xbf334b0();
   input += synapse0xbf334f0();
   input += synapse0xbf33530();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf33160() {
   double input = input0xbf33160();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::input0xbf33570() {
   double input = 1.14448;
   input += synapse0xbf33880();
   input += synapse0xbf338c0();
   input += synapse0xbf33900();
   input += synapse0xbf33940();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf33570() {
   double input = input0xbf33570();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::input0xbf33980() {
   double input = 4.03597;
   input += synapse0xbf33c90();
   input += synapse0xbeda7a0();
   input += synapse0xb0a8530();
   input += synapse0xb0a8570();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf33980() {
   double input = input0xbf33980();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::input0xbf33de0() {
   double input = -1.51136;
   input += synapse0xbf340f0();
   input += synapse0xbf34130();
   input += synapse0xbf34170();
   input += synapse0xbf341b0();
   input += synapse0xbf341f0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf33de0() {
   double input = input0xbf33de0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::input0xbf34230() {
   double input = 3.77081;
   input += synapse0xbf34540();
   input += synapse0xbf34580();
   input += synapse0xbf345c0();
   input += synapse0xbf34600();
   input += synapse0xbf34640();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf34230() {
   double input = input0xbf34230();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::input0xbf34680() {
   double input = -3.16826;
   input += synapse0xbf349c0();
   input += synapse0xbf34a00();
   input += synapse0xbf34a40();
   input += synapse0xbf0c780();
   input += synapse0xbf389c0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf34680() {
   double input = input0xbf34680();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::input0xbf34c90() {
   double input = -0.118976;
   input += synapse0xbf34fd0();
   input += synapse0xbf35010();
   input += synapse0xbf35050();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::neuron0xbf34c90() {
   double input = input0xbf34c90();
   return (input * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbedabe0() {
   return (neuron0xbf31c90()*-4.94111);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf32c90() {
   return (neuron0xbf31fa0()*6.66575);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf32cd0() {
   return (neuron0xbf322b0()*2.75088);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf32d10() {
   return (neuron0xbf325c0()*-5.42739);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf33060() {
   return (neuron0xbf31c90()*-3.61114);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf330a0() {
   return (neuron0xbf31fa0()*5.3463);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf330e0() {
   return (neuron0xbf322b0()*-1.00845);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf33120() {
   return (neuron0xbf325c0()*-1.18123);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf33470() {
   return (neuron0xbf31c90()*3.70868);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf334b0() {
   return (neuron0xbf31fa0()*-1.43076);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf334f0() {
   return (neuron0xbf322b0()*-1.49005);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf33530() {
   return (neuron0xbf325c0()*0.145469);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf33880() {
   return (neuron0xbf31c90()*3.56967);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf338c0() {
   return (neuron0xbf31fa0()*-4.59041);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf33900() {
   return (neuron0xbf322b0()*-1.26506);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf33940() {
   return (neuron0xbf325c0()*2.23213);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf33c90() {
   return (neuron0xbf31c90()*-1.57543);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbeda7a0() {
   return (neuron0xbf31fa0()*3.93789);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xb0a8530() {
   return (neuron0xbf322b0()*2.95219);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xb0a8570() {
   return (neuron0xbf325c0()*-0.467533);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf340f0() {
   return (neuron0xbf32a10()*-1.69852);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf34130() {
   return (neuron0xbf32d50()*-0.223764);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf34170() {
   return (neuron0xbf33160()*-3.35352);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf341b0() {
   return (neuron0xbf33570()*-2.20407);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf341f0() {
   return (neuron0xbf33980()*2.03874);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf34540() {
   return (neuron0xbf32a10()*-8.05133);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf34580() {
   return (neuron0xbf32d50()*-8.10774);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf345c0() {
   return (neuron0xbf33160()*3.8468);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf34600() {
   return (neuron0xbf33570()*4.42074);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf34640() {
   return (neuron0xbf33980()*-4.33246);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf349c0() {
   return (neuron0xbf32a10()*5.59623);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf34a00() {
   return (neuron0xbf32d50()*-3.55232);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf34a40() {
   return (neuron0xbf33160()*7.39947);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf0c780() {
   return (neuron0xbf33570()*8.75424);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf389c0() {
   return (neuron0xbf33980()*-3.94719);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf34fd0() {
   return (neuron0xbf33de0()*0.580101);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf35010() {
   return (neuron0xbf34230()*-1.00154);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011_mm::synapse0xbf35050() {
   return (neuron0xbf34680()*1.10833);
}

