#include "MLP_Higgs_vs_TT_MM_N_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.0056)/1.27451;
   input1 = (in1 - 25.3525)/1.62377;
   input2 = (in2 - 14.2232)/2.05931;
   switch(index) {
     case 0:
         return neuron0x20b7aec0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 22.0056)/1.27451;
   input1 = (input[1] - 25.3525)/1.62377;
   input2 = (input[2] - 14.2232)/2.05931;
   switch(index) {
     case 0:
         return neuron0x20b7aec0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x20b67c20() {
   return input0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x20b67f60() {
   return input1;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x20b78ea0() {
   return input2;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x20b79280() {
   double input = -0.0675873;
   input += synapse0x20b4e910();
   input += synapse0x20b30360();
   input += synapse0x20b79530();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x20b79280() {
   double input = input0x20b79280();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x20b79570() {
   double input = 3.36102;
   input += synapse0x20b798b0();
   input += synapse0x20b798f0();
   input += synapse0x20b79930();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x20b79570() {
   double input = input0x20b79570();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x20b79970() {
   double input = 2.98209;
   input += synapse0x20b79cb0();
   input += synapse0x20b79cf0();
   input += synapse0x20b79d30();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x20b79970() {
   double input = input0x20b79970();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x20b79d70() {
   double input = -4.07448;
   input += synapse0x20b7a0b0();
   input += synapse0x20b7a0f0();
   input += synapse0x20b7a130();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x20b79d70() {
   double input = input0x20b79d70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x20b7a170() {
   double input = 4.25239;
   input += synapse0x20b7a4b0();
   input += synapse0x20b7a4f0();
   input += synapse0x20b7a530();
   input += synapse0x20b7a570();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x20b7a170() {
   double input = input0x20b7a170();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x20b7a5b0() {
   double input = 2.82766;
   input += synapse0x20b7a8f0();
   input += synapse0x20ad6b20();
   input += synapse0x20ad6b60();
   input += synapse0x20b7aa40();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x20b7a5b0() {
   double input = input0x20b7a5b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x20b7aa80() {
   double input = 2.13704;
   input += synapse0x20b7adc0();
   input += synapse0x20b7ae00();
   input += synapse0x20b7ae40();
   input += synapse0x20b7ae80();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x20b7aa80() {
   double input = input0x20b7aa80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x20b7aec0() {
   double input = -0.868643;
   input += synapse0x20b7b0e0();
   input += synapse0x20b7b120();
   input += synapse0x20b7b160();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x20b7aec0() {
   double input = input0x20b7aec0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b4e910() {
   return (neuron0x20b67c20()*-0.511776);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b30360() {
   return (neuron0x20b67f60()*-0.0215387);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b79530() {
   return (neuron0x20b78ea0()*-0.0473927);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b798b0() {
   return (neuron0x20b67c20()*0.644309);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b798f0() {
   return (neuron0x20b67f60()*-4.35125);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b79930() {
   return (neuron0x20b78ea0()*-0.587777);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b79cb0() {
   return (neuron0x20b67c20()*1.43551);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b79cf0() {
   return (neuron0x20b67f60()*-0.728635);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b79d30() {
   return (neuron0x20b78ea0()*0.136533);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7a0b0() {
   return (neuron0x20b67c20()*1.04241);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7a0f0() {
   return (neuron0x20b67f60()*0.228959);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7a130() {
   return (neuron0x20b78ea0()*-5.37236);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7a4b0() {
   return (neuron0x20b79280()*-10.9985);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7a4f0() {
   return (neuron0x20b79570()*6.43527);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7a530() {
   return (neuron0x20b79970()*-4.35095);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7a570() {
   return (neuron0x20b79d70()*4.30786);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7a8f0() {
   return (neuron0x20b79280()*0.363385);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20ad6b20() {
   return (neuron0x20b79570()*0.0189737);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20ad6b60() {
   return (neuron0x20b79970()*-1.42975);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7aa40() {
   return (neuron0x20b79d70()*-0.230483);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7adc0() {
   return (neuron0x20b79280()*7.11489);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7ae00() {
   return (neuron0x20b79570()*-7.77483);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7ae40() {
   return (neuron0x20b79970()*0.075818);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7ae80() {
   return (neuron0x20b79d70()*-5.47769);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7b0e0() {
   return (neuron0x20b7a170()*2.79778);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7b120() {
   return (neuron0x20b7a5b0()*-1.18515);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x20b7b160() {
   return (neuron0x20b7aa80()*1.87682);
}

