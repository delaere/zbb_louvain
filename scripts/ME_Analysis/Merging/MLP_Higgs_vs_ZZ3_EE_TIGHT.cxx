#include "MLP_Higgs_vs_ZZ3_EE_TIGHT.h"
#include <cmath>

double MLP_Higgs_vs_ZZ3_EE_TIGHT::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 30.4024)/59.2816;
   input1 = (in1 - 13.2646)/2.00861;
   input2 = (in2 - 21.0831)/1.29632;
   input3 = (in3 - 28.6701)/106.361;
   switch(index) {
     case 0:
         return neuron0x7bf2e80();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::Value(int index, double* input) {
   input0 = (input[0] - 30.4024)/59.2816;
   input1 = (input[1] - 13.2646)/2.00861;
   input2 = (input[2] - 21.0831)/1.29632;
   input3 = (input[3] - 28.6701)/106.361;
   switch(index) {
     case 0:
         return neuron0x7bf2e80();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf0490() {
   return input0;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf07a0() {
   return input1;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf0ab0() {
   return input2;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf0dc0() {
   return input3;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::input0x7bf1210() {
   double input = -1.43601;
   input += synapse0x7b993e0();
   input += synapse0x7bf1490();
   input += synapse0x7bf14d0();
   input += synapse0x7bf1510();
   return input;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf1210() {
   double input = input0x7bf1210();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::input0x7bf1550() {
   double input = -0.59519;
   input += synapse0x7bf1860();
   input += synapse0x7bf18a0();
   input += synapse0x7bf18e0();
   input += synapse0x7bf1920();
   return input;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf1550() {
   double input = input0x7bf1550();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::input0x7bf1960() {
   double input = -0.0203072;
   input += synapse0x7bf1c70();
   input += synapse0x7bf1cb0();
   input += synapse0x7bf1cf0();
   input += synapse0x7bf1d30();
   return input;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf1960() {
   double input = input0x7bf1960();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::input0x7bf1d70() {
   double input = 2.5427;
   input += synapse0x7bf2080();
   input += synapse0x7bf20c0();
   input += synapse0x7bf2100();
   input += synapse0x7bf2140();
   return input;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf1d70() {
   double input = input0x7bf1d70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::input0x7bf2180() {
   double input = 0.529708;
   input += synapse0x7bf2490();
   input += synapse0x7b98fa0();
   input += synapse0x7968a40();
   input += synapse0x7968a80();
   return input;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf2180() {
   double input = input0x7bf2180();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::input0x7bf25e0() {
   double input = -2.4239;
   input += synapse0x7bf28f0();
   input += synapse0x7bf2930();
   input += synapse0x7bf2970();
   input += synapse0x7bf29b0();
   input += synapse0x7bf29f0();
   return input;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf25e0() {
   double input = input0x7bf25e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::input0x7bf2a30() {
   double input = -0.179646;
   input += synapse0x7bf2d40();
   input += synapse0x7bf2d80();
   input += synapse0x7bf2dc0();
   input += synapse0x7bf2e00();
   input += synapse0x7bf2e40();
   return input;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf2a30() {
   double input = input0x7bf2a30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::input0x7bf2e80() {
   double input = -1.74976;
   input += synapse0x7bf31c0();
   input += synapse0x7bf3200();
   return input;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::neuron0x7bf2e80() {
   double input = input0x7bf2e80();
   return (input * 1)+0;
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7b993e0() {
   return (neuron0x7bf0490()*1.4962);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf1490() {
   return (neuron0x7bf07a0()*-1.44025);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf14d0() {
   return (neuron0x7bf0ab0()*-1.43334);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf1510() {
   return (neuron0x7bf0dc0()*0.0832138);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf1860() {
   return (neuron0x7bf0490()*0.248409);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf18a0() {
   return (neuron0x7bf07a0()*-3.03586);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf18e0() {
   return (neuron0x7bf0ab0()*0.589235);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf1920() {
   return (neuron0x7bf0dc0()*4.1005);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf1c70() {
   return (neuron0x7bf0490()*-0.316721);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf1cb0() {
   return (neuron0x7bf07a0()*-0.444447);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf1cf0() {
   return (neuron0x7bf0ab0()*-0.444859);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf1d30() {
   return (neuron0x7bf0dc0()*-5.19455);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf2080() {
   return (neuron0x7bf0490()*0.470146);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf20c0() {
   return (neuron0x7bf07a0()*-1.74085);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf2100() {
   return (neuron0x7bf0ab0()*0.133608);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf2140() {
   return (neuron0x7bf0dc0()*2.35436);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf2490() {
   return (neuron0x7bf0490()*-3.71404);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7b98fa0() {
   return (neuron0x7bf07a0()*1.00176);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7968a40() {
   return (neuron0x7bf0ab0()*-0.771317);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7968a80() {
   return (neuron0x7bf0dc0()*5.58005);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf28f0() {
   return (neuron0x7bf1210()*-0.986644);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf2930() {
   return (neuron0x7bf1550()*5.80388);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf2970() {
   return (neuron0x7bf1960()*-6.28479);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf29b0() {
   return (neuron0x7bf1d70()*5.185);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf29f0() {
   return (neuron0x7bf2180()*6.27548);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf2d40() {
   return (neuron0x7bf1210()*1.19227);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf2d80() {
   return (neuron0x7bf1550()*2.55834);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf2dc0() {
   return (neuron0x7bf1960()*0.404019);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf2e00() {
   return (neuron0x7bf1d70()*0.932097);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf2e40() {
   return (neuron0x7bf2180()*2.17333);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf31c0() {
   return (neuron0x7bf25e0()*5.01232);
}

double MLP_Higgs_vs_ZZ3_EE_TIGHT::synapse0x7bf3200() {
   return (neuron0x7bf2a30()*-2.25603);
}

