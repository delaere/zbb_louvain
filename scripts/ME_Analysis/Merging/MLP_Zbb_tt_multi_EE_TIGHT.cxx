#include "MLP_Zbb_tt_multi_EE_TIGHT.h"
#include <cmath>

double MLP_Zbb_tt_multi_EE_TIGHT::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 20.3256)/1.0298;
   input1 = (in1 - 21.0098)/0.967296;
   input2 = (in2 - 21.5918)/0.86144;
   input3 = (in3 - 0.482557)/0.499696;
   switch(index) {
     case 0:
         return neuron0x1c7d2d30();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_multi_EE_TIGHT::Value(int index, double* input) {
   input0 = (input[0] - 20.3256)/1.0298;
   input1 = (input[1] - 21.0098)/0.967296;
   input2 = (input[2] - 21.5918)/0.86144;
   input3 = (input[3] - 0.482557)/0.499696;
   switch(index) {
     case 0:
         return neuron0x1c7d2d30();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_multi_EE_TIGHT::neuron0x1cc3ec10() {
   return input0;
}

double MLP_Zbb_tt_multi_EE_TIGHT::neuron0x1cc3ef20() {
   return input1;
}

double MLP_Zbb_tt_multi_EE_TIGHT::neuron0x1e7c1c80() {
   return input2;
}

double MLP_Zbb_tt_multi_EE_TIGHT::neuron0x1e7c1fc0() {
   return input3;
}

double MLP_Zbb_tt_multi_EE_TIGHT::input0x1e7c2440() {
   double input = -1.23802;
   input += synapse0x1e7072f0();
   input += synapse0x1e7c2750();
   input += synapse0x1e7c2790();
   input += synapse0x1e7c27d0();
   return input;
}

double MLP_Zbb_tt_multi_EE_TIGHT::neuron0x1e7c2440() {
   double input = input0x1e7c2440();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_multi_EE_TIGHT::input0x1e7c2810() {
   double input = -1.76325;
   input += synapse0x1cc3f110();
   input += synapse0x1cb52d10();
   input += synapse0x1cb525e0();
   input += synapse0x1c7d1c20();
   return input;
}

double MLP_Zbb_tt_multi_EE_TIGHT::neuron0x1e7c2810() {
   double input = input0x1e7c2810();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_multi_EE_TIGHT::input0x1c7d1c60() {
   double input = -0.655245;
   input += synapse0x1c7d1f70();
   input += synapse0x1c7d1fb0();
   input += synapse0x1c7d1ff0();
   input += synapse0x1c7d2030();
   return input;
}

double MLP_Zbb_tt_multi_EE_TIGHT::neuron0x1c7d1c60() {
   double input = input0x1c7d1c60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_multi_EE_TIGHT::input0x1c7d2070() {
   double input = 1.39535;
   input += synapse0x1c7d2380();
   input += synapse0x1c7d23c0();
   input += synapse0x1c7d2400();
   input += synapse0x1c7d2440();
   return input;
}

double MLP_Zbb_tt_multi_EE_TIGHT::neuron0x1c7d2070() {
   double input = input0x1c7d2070();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_multi_EE_TIGHT::input0x1c7d2480() {
   double input = -0.453309;
   input += synapse0x1c7d2790();
   input += synapse0x1cb52c80();
   input += synapse0x1cb52cc0();
   input += synapse0x1c7d28e0();
   return input;
}

double MLP_Zbb_tt_multi_EE_TIGHT::neuron0x1c7d2480() {
   double input = input0x1c7d2480();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_multi_EE_TIGHT::input0x1c7d2920() {
   double input = 0.604664;
   input += synapse0x1c7d2c30();
   input += synapse0x1c7d2c70();
   input += synapse0x1c7d2cb0();
   input += synapse0x1c7d2cf0();
   return input;
}

double MLP_Zbb_tt_multi_EE_TIGHT::neuron0x1c7d2920() {
   double input = input0x1c7d2920();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_multi_EE_TIGHT::input0x1c7d2d30() {
   double input = 0.28926;
   input += synapse0x1c7d3040();
   input += synapse0x1c7d3080();
   return input;
}

double MLP_Zbb_tt_multi_EE_TIGHT::neuron0x1c7d2d30() {
   double input = input0x1c7d2d30();
   return (input * 1)+0;
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1e7072f0() {
   return (neuron0x1cc3ec10()*1.40394);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1e7c2750() {
   return (neuron0x1cc3ef20()*-1.83345);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1e7c2790() {
   return (neuron0x1e7c1c80()*0.153575);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1e7c27d0() {
   return (neuron0x1e7c1fc0()*-0.0370547);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1cc3f110() {
   return (neuron0x1cc3ec10()*0.177378);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1cb52d10() {
   return (neuron0x1cc3ef20()*4.60774);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1cb525e0() {
   return (neuron0x1e7c1c80()*-2.34981);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d1c20() {
   return (neuron0x1e7c1fc0()*0.8095);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d1f70() {
   return (neuron0x1cc3ec10()*-3.58995);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d1fb0() {
   return (neuron0x1cc3ef20()*3.65448);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d1ff0() {
   return (neuron0x1e7c1c80()*2.07263);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d2030() {
   return (neuron0x1e7c1fc0()*-1.34232);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d2380() {
   return (neuron0x1cc3ec10()*2.55796);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d23c0() {
   return (neuron0x1cc3ef20()*0.158797);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d2400() {
   return (neuron0x1e7c1c80()*-1.89307);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d2440() {
   return (neuron0x1e7c1fc0()*-0.956663);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d2790() {
   return (neuron0x1e7c2440()*2.66334);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1cb52c80() {
   return (neuron0x1e7c2810()*-3.41164);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1cb52cc0() {
   return (neuron0x1c7d1c60()*1.7547);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d28e0() {
   return (neuron0x1c7d2070()*-2.31266);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d2c30() {
   return (neuron0x1e7c2440()*-0.0971791);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d2c70() {
   return (neuron0x1e7c2810()*-0.480779);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d2cb0() {
   return (neuron0x1c7d1c60()*-0.0206634);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d2cf0() {
   return (neuron0x1c7d2070()*-0.952291);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d3040() {
   return (neuron0x1c7d2480()*1.27519);
}

double MLP_Zbb_tt_multi_EE_TIGHT::synapse0x1c7d3080() {
   return (neuron0x1c7d2920()*-0.772065);
}

