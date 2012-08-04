#include "MLP_Zbb_tt_EE.h"
#include <cmath>

double MLP_Zbb_tt_EE::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 20.9125)/1.08293;
   input1 = (in1 - 21.6321)/1.05575;
   input2 = (in2 - 21.6884)/0.800382;
   input3 = (in3 - 65.8143)/37.6943;
   switch(index) {
     case 0:
         return neuron0x5361c30();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_EE::Value(int index, double* input) {
   input0 = (input[0] - 20.9125)/1.08293;
   input1 = (input[1] - 21.6321)/1.05575;
   input2 = (input[2] - 21.6884)/0.800382;
   input3 = (input[3] - 65.8143)/37.6943;
   switch(index) {
     case 0:
         return neuron0x5361c30();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_EE::neuron0x535fa70() {
   return input0;
}

double MLP_Zbb_tt_EE::neuron0x535fd80() {
   return input1;
}

double MLP_Zbb_tt_EE::neuron0x5360090() {
   return input2;
}

double MLP_Zbb_tt_EE::neuron0x53603a0() {
   return input3;
}

double MLP_Zbb_tt_EE::input0x5360820() {
   double input = 3.49937;
   input += synapse0x53089c0();
   input += synapse0x5360aa0();
   input += synapse0x5360ae0();
   input += synapse0x5360b20();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x5360820() {
   double input = input0x5360820();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_EE::input0x5360b60() {
   double input = -2.31755;
   input += synapse0x5360e70();
   input += synapse0x5360eb0();
   input += synapse0x5360ef0();
   input += synapse0x5360f30();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x5360b60() {
   double input = input0x5360b60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_EE::input0x5360f70() {
   double input = -0.403654;
   input += synapse0x5361280();
   input += synapse0x53612c0();
   input += synapse0x5361300();
   input += synapse0x5361340();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x5360f70() {
   double input = input0x5360f70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_EE::input0x5361380() {
   double input = 0.254478;
   input += synapse0x5361690();
   input += synapse0x53616d0();
   input += synapse0x5361710();
   input += synapse0x5361750();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x5361380() {
   double input = input0x5361380();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_EE::input0x5361790() {
   double input = -0.165301;
   input += synapse0x5361aa0();
   input += synapse0x4d6d220();
   input += synapse0x4d6d260();
   input += synapse0x5361bf0();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x5361790() {
   double input = input0x5361790();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_EE::input0x5361c30() {
   double input = 2.15354;
   input += synapse0x5361f40();
   input += synapse0x5361f80();
   input += synapse0x5361fc0();
   input += synapse0x5362000();
   input += synapse0x5362040();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x5361c30() {
   double input = input0x5361c30();
   return (input * 1)+0;
}

double MLP_Zbb_tt_EE::synapse0x53089c0() {
   return (neuron0x535fa70()*0.968667);
}

double MLP_Zbb_tt_EE::synapse0x5360aa0() {
   return (neuron0x535fd80()*0.585526);
}

double MLP_Zbb_tt_EE::synapse0x5360ae0() {
   return (neuron0x5360090()*-1.19738);
}

double MLP_Zbb_tt_EE::synapse0x5360b20() {
   return (neuron0x53603a0()*3.00339);
}

double MLP_Zbb_tt_EE::synapse0x5360e70() {
   return (neuron0x535fa70()*-0.50648);
}

double MLP_Zbb_tt_EE::synapse0x5360eb0() {
   return (neuron0x535fd80()*-0.917869);
}

double MLP_Zbb_tt_EE::synapse0x5360ef0() {
   return (neuron0x5360090()*1.12753);
}

double MLP_Zbb_tt_EE::synapse0x5360f30() {
   return (neuron0x53603a0()*-2.68942);
}

double MLP_Zbb_tt_EE::synapse0x5361280() {
   return (neuron0x535fa70()*-0.793497);
}

double MLP_Zbb_tt_EE::synapse0x53612c0() {
   return (neuron0x535fd80()*-0.114063);
}

double MLP_Zbb_tt_EE::synapse0x5361300() {
   return (neuron0x5360090()*0.170865);
}

double MLP_Zbb_tt_EE::synapse0x5361340() {
   return (neuron0x53603a0()*0.296807);
}

double MLP_Zbb_tt_EE::synapse0x5361690() {
   return (neuron0x535fa70()*-0.010018);
}

double MLP_Zbb_tt_EE::synapse0x53616d0() {
   return (neuron0x535fd80()*0.0670894);
}

double MLP_Zbb_tt_EE::synapse0x5361710() {
   return (neuron0x5360090()*0.0886149);
}

double MLP_Zbb_tt_EE::synapse0x5361750() {
   return (neuron0x53603a0()*-0.109301);
}

double MLP_Zbb_tt_EE::synapse0x5361aa0() {
   return (neuron0x535fa70()*-0.76846);
}

double MLP_Zbb_tt_EE::synapse0x4d6d220() {
   return (neuron0x535fd80()*-0.118074);
}

double MLP_Zbb_tt_EE::synapse0x4d6d260() {
   return (neuron0x5360090()*-0.651483);
}

double MLP_Zbb_tt_EE::synapse0x5361bf0() {
   return (neuron0x53603a0()*0.160447);
}

double MLP_Zbb_tt_EE::synapse0x5361f40() {
   return (neuron0x5360820()*-1.24147);
}

double MLP_Zbb_tt_EE::synapse0x5361f80() {
   return (neuron0x5360b60()*-0.110809);
}

double MLP_Zbb_tt_EE::synapse0x5361fc0() {
   return (neuron0x5360f70()*-0.0577178);
}

double MLP_Zbb_tt_EE::synapse0x5362000() {
   return (neuron0x5361380()*-1.48454);
}

double MLP_Zbb_tt_EE::synapse0x5362040() {
   return (neuron0x5361790()*-0.181895);
}

