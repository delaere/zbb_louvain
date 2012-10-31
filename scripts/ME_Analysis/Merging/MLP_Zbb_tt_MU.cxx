#include "MLP_Zbb_tt_MU.h"
#include <cmath>

double MLP_Zbb_tt_MU::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 20.1672)/1.10924;
   input1 = (in1 - 20.8337)/1.0806;
   input2 = (in2 - 21.871)/1.33148;
   switch(index) {
     case 0:
         return neuron0xb7d6be0();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_MU::Value(int index, double* input) {
   input0 = (input[0] - 20.1672)/1.10924;
   input1 = (input[1] - 20.8337)/1.0806;
   input2 = (input[2] - 21.871)/1.33148;
   switch(index) {
     case 0:
         return neuron0xb7d6be0();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_MU::neuron0xb7c44a0() {
   return input0;
}

double MLP_Zbb_tt_MU::neuron0xb7c47b0() {
   return input1;
}

double MLP_Zbb_tt_MU::neuron0xb7d5610() {
   return input2;
}

double MLP_Zbb_tt_MU::input0xb7d5a60() {
   double input = -0.164809;
   input += synapse0xb792780();
   input += synapse0xb7ac6f0();
   input += synapse0xb792810();
   return input;
}

double MLP_Zbb_tt_MU::neuron0xb7d5a60() {
   double input = input0xb7d5a60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_MU::input0xb7d5ce0() {
   double input = -3.00728;
   input += synapse0xb7c4a30();
   input += synapse0xb7d5ff0();
   input += synapse0xb7d6030();
   return input;
}

double MLP_Zbb_tt_MU::neuron0xb7d5ce0() {
   double input = input0xb7d5ce0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_MU::input0xb7d6070() {
   double input = -0.288036;
   input += synapse0xb7d6380();
   input += synapse0xb7d63c0();
   input += synapse0xb7d6400();
   return input;
}

double MLP_Zbb_tt_MU::neuron0xb7d6070() {
   double input = input0xb7d6070();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_MU::input0xb7d6440() {
   double input = 0.598723;
   input += synapse0xb7d6750();
   input += synapse0xb7d6790();
   input += synapse0xb7d67d0();
   return input;
}

double MLP_Zbb_tt_MU::neuron0xb7d6440() {
   double input = input0xb7d6440();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_MU::input0xb7d6810() {
   double input = -0.333228;
   input += synapse0xb7d6b20();
   input += synapse0xb7d6b60();
   input += synapse0xb7d6ba0();
   return input;
}

double MLP_Zbb_tt_MU::neuron0xb7d6810() {
   double input = input0xb7d6810();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_MU::input0xb7d6be0() {
   double input = 2.82666;
   input += synapse0xb7d6dd0();
   input += synapse0xb7d6e10();
   return input;
}

double MLP_Zbb_tt_MU::neuron0xb7d6be0() {
   double input = input0xb7d6be0();
   return (input * 1)+0;
}

double MLP_Zbb_tt_MU::synapse0xb792780() {
   return (neuron0xb7c44a0()*1.87074);
}

double MLP_Zbb_tt_MU::synapse0xb7ac6f0() {
   return (neuron0xb7c47b0()*-2.29198);
}

double MLP_Zbb_tt_MU::synapse0xb792810() {
   return (neuron0xb7d5610()*4.2697);
}

double MLP_Zbb_tt_MU::synapse0xb7c4a30() {
   return (neuron0xb7c44a0()*3.33889);
}

double MLP_Zbb_tt_MU::synapse0xb7d5ff0() {
   return (neuron0xb7c47b0()*1.65654);
}

double MLP_Zbb_tt_MU::synapse0xb7d6030() {
   return (neuron0xb7d5610()*-6.2811);
}

double MLP_Zbb_tt_MU::synapse0xb7d6380() {
   return (neuron0xb7c44a0()*-1.3132);
}

double MLP_Zbb_tt_MU::synapse0xb7d63c0() {
   return (neuron0xb7c47b0()*-0.388597);
}

double MLP_Zbb_tt_MU::synapse0xb7d6400() {
   return (neuron0xb7d5610()*1.32457);
}

double MLP_Zbb_tt_MU::synapse0xb7d6750() {
   return (neuron0xb7d5a60()*-1.72513);
}

double MLP_Zbb_tt_MU::synapse0xb7d6790() {
   return (neuron0xb7d5ce0()*2.62861);
}

double MLP_Zbb_tt_MU::synapse0xb7d67d0() {
   return (neuron0xb7d6070()*0.178889);
}

double MLP_Zbb_tt_MU::synapse0xb7d6b20() {
   return (neuron0xb7d5a60()*4.43563);
}

double MLP_Zbb_tt_MU::synapse0xb7d6b60() {
   return (neuron0xb7d5ce0()*-5.52503);
}

double MLP_Zbb_tt_MU::synapse0xb7d6ba0() {
   return (neuron0xb7d6070()*-2.48097);
}

double MLP_Zbb_tt_MU::synapse0xb7d6dd0() {
   return (neuron0xb7d6440()*-2.80474);
}

double MLP_Zbb_tt_MU::synapse0xb7d6e10() {
   return (neuron0xb7d6810()*-1.22702);
}

