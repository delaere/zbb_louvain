#include "MLP_Zbb_tt_Mll_test_Mll_deta.h"
#include <cmath>

double MLP_Zbb_tt_Mll_test_Mll_deta::Value(int index,double in0) {
   input0 = (in0 - 90.603)/8.17209;
   switch(index) {
     case 0:
         return neuron0x1cef1d80();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_Mll_test_Mll_deta::Value(int index, double* input) {
   input0 = (input[0] - 90.603)/8.17209;
   switch(index) {
     case 0:
         return neuron0x1cef1d80();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_Mll_test_Mll_deta::neuron0x1cef07f0() {
   return input0;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::input0x1cef0c40() {
   double input = -5.30242;
   input += synapse0x1cedb6a0();
   return input;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::neuron0x1cef0c40() {
   double input = input0x1cef0c40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::input0x1cef0ec0() {
   double input = 0.817508;
   input += synapse0x1cef6f10();
   return input;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::neuron0x1cef0ec0() {
   double input = input0x1cef0ec0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::input0x1cef1200() {
   double input = 1.1001;
   input += synapse0x1cef1540();
   return input;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::neuron0x1cef1200() {
   double input = input0x1cef1200();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::input0x1cef1580() {
   double input = 0.933163;
   input += synapse0x1cef18c0();
   input += synapse0x1cef1900();
   input += synapse0x1cef1940();
   return input;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::neuron0x1cef1580() {
   double input = input0x1cef1580();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::input0x1cef1980() {
   double input = 0.530851;
   input += synapse0x1cef1cc0();
   input += synapse0x1cef1d00();
   input += synapse0x1cef1d40();
   return input;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::neuron0x1cef1980() {
   double input = input0x1cef1980();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::input0x1cef1d80() {
   double input = -3.0261;
   input += synapse0x1cef20c0();
   input += synapse0x1cef2100();
   return input;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::neuron0x1cef1d80() {
   double input = input0x1cef1d80();
   return (input * 1)+0;
}

double MLP_Zbb_tt_Mll_test_Mll_deta::synapse0x1cedb6a0() {
   return (neuron0x1cef07f0()*-2.30354);
}

double MLP_Zbb_tt_Mll_test_Mll_deta::synapse0x1cef6f10() {
   return (neuron0x1cef07f0()*4.956);
}

double MLP_Zbb_tt_Mll_test_Mll_deta::synapse0x1cef1540() {
   return (neuron0x1cef07f0()*-3.81329);
}

double MLP_Zbb_tt_Mll_test_Mll_deta::synapse0x1cef18c0() {
   return (neuron0x1cef0c40()*0.762208);
}

double MLP_Zbb_tt_Mll_test_Mll_deta::synapse0x1cef1900() {
   return (neuron0x1cef0ec0()*-1.01763);
}

double MLP_Zbb_tt_Mll_test_Mll_deta::synapse0x1cef1940() {
   return (neuron0x1cef1200()*5.62997);
}

double MLP_Zbb_tt_Mll_test_Mll_deta::synapse0x1cef1cc0() {
   return (neuron0x1cef0c40()*-2.21854);
}

double MLP_Zbb_tt_Mll_test_Mll_deta::synapse0x1cef1d00() {
   return (neuron0x1cef0ec0()*2.94739);
}

double MLP_Zbb_tt_Mll_test_Mll_deta::synapse0x1cef1d40() {
   return (neuron0x1cef1200()*0.624086);
}

double MLP_Zbb_tt_Mll_test_Mll_deta::synapse0x1cef20c0() {
   return (neuron0x1cef1580()*1.43667);
}

double MLP_Zbb_tt_Mll_test_Mll_deta::synapse0x1cef2100() {
   return (neuron0x1cef1980()*2.50219);
}

