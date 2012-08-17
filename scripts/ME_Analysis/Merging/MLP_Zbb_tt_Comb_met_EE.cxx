#include "MLP_Zbb_tt_Comb_met_EE.h"
#include <cmath>

double MLP_Zbb_tt_Comb_met_EE::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 20.3256)/1.0298;
   input1 = (in1 - 21.0098)/0.967296;
   input2 = (in2 - 21.5918)/0.86144;
   input3 = (in3 - 31.892)/15.308;
   switch(index) {
     case 0:
         return neuron0x11b9afe0();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_Comb_met_EE::Value(int index, double* input) {
   input0 = (input[0] - 20.3256)/1.0298;
   input1 = (input[1] - 21.0098)/0.967296;
   input2 = (input[2] - 21.5918)/0.86144;
   input3 = (input[3] - 31.892)/15.308;
   switch(index) {
     case 0:
         return neuron0x11b9afe0();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11bc2690() {
   return input0;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11bc29a0() {
   return input1;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b981e0() {
   return input2;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b98520() {
   return input3;
}

double MLP_Zbb_tt_Comb_met_EE::input0x11b989a0() {
   double input = -0.0341202;
   input += synapse0x11b3e9b0();
   input += synapse0x15416360();
   input += synapse0x154162e0();
   input += synapse0x11bc2490();
   return input;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b989a0() {
   double input = input0x11b989a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_met_EE::input0x11b98c20() {
   double input = 0.630851;
   input += synapse0x11b3ea40();
   input += synapse0x11b98f30();
   input += synapse0x11b98f70();
   input += synapse0x11b98fb0();
   return input;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b98c20() {
   double input = input0x11b98c20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_met_EE::input0x11b98ff0() {
   double input = -1.13902;
   input += synapse0x11b99300();
   input += synapse0x11b99340();
   input += synapse0x11b99380();
   input += synapse0x11b993c0();
   return input;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b98ff0() {
   double input = input0x11b98ff0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_met_EE::input0x11b99400() {
   double input = -0.906292;
   input += synapse0x11b99710();
   input += synapse0x11b99750();
   input += synapse0x11b99790();
   input += synapse0x11b997d0();
   return input;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b99400() {
   double input = input0x11b99400();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_met_EE::input0x11b99810() {
   double input = -3.20617;
   input += synapse0x11b99b20();
   input += synapse0x11bc2b90();
   input += synapse0x12a12040();
   input += synapse0x12ab56c0();
   return input;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b99810() {
   double input = input0x11b99810();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_met_EE::input0x11b99c70() {
   double input = 0.0619692;
   input += synapse0x11b99f80();
   input += synapse0x11b99fc0();
   input += synapse0x11b9a000();
   input += synapse0x11b9a040();
   return input;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b99c70() {
   double input = input0x11b99c70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_met_EE::input0x11b9a080() {
   double input = 1.74288;
   input += synapse0x11b9a390();
   input += synapse0x11b9a3d0();
   input += synapse0x11b9a410();
   input += synapse0x11b9a450();
   input += synapse0x11b9a490();
   input += synapse0x11b9a4d0();
   return input;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b9a080() {
   double input = input0x11b9a080();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_met_EE::input0x11b9a510() {
   double input = -4.33016;
   input += synapse0x11b9a850();
   input += synapse0x11b9a890();
   input += synapse0x11b9a8d0();
   input += synapse0x11bc2440();
   input += synapse0x11b438c0();
   input += synapse0x12ab5700();
   return input;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b9a510() {
   double input = input0x11b9a510();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_met_EE::input0x11b9ab20() {
   double input = 0.835206;
   input += synapse0x11b9ae60();
   input += synapse0x11b9aea0();
   input += synapse0x11b9aee0();
   input += synapse0x11b9af20();
   input += synapse0x11b9af60();
   input += synapse0x11b9afa0();
   return input;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b9ab20() {
   double input = input0x11b9ab20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_met_EE::input0x11b9afe0() {
   double input = 3.06218;
   input += synapse0x11b9b320();
   input += synapse0x11b9b360();
   input += synapse0x11b9b3a0();
   return input;
}

double MLP_Zbb_tt_Comb_met_EE::neuron0x11b9afe0() {
   double input = input0x11b9afe0();
   return (input * 1)+0;
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b3e9b0() {
   return (neuron0x11bc2690()*1.35509);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x15416360() {
   return (neuron0x11bc29a0()*-0.0876492);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x154162e0() {
   return (neuron0x11b981e0()*3.83336);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11bc2490() {
   return (neuron0x11b98520()*0.0141313);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b3ea40() {
   return (neuron0x11bc2690()*-1.39583);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b98f30() {
   return (neuron0x11bc29a0()*-5.61967);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b98f70() {
   return (neuron0x11b981e0()*3.50269);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b98fb0() {
   return (neuron0x11b98520()*-0.969692);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b99300() {
   return (neuron0x11bc2690()*-3.36786);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b99340() {
   return (neuron0x11bc29a0()*-0.721964);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b99380() {
   return (neuron0x11b981e0()*2.0201);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b993c0() {
   return (neuron0x11b98520()*-1.0777);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b99710() {
   return (neuron0x11bc2690()*-1.01606);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b99750() {
   return (neuron0x11bc29a0()*-1.39868);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b99790() {
   return (neuron0x11b981e0()*3.24592);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b997d0() {
   return (neuron0x11b98520()*-4.59873);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b99b20() {
   return (neuron0x11bc2690()*-1.37829);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11bc2b90() {
   return (neuron0x11bc29a0()*-0.660048);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x12a12040() {
   return (neuron0x11b981e0()*2.73114);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x12ab56c0() {
   return (neuron0x11b98520()*-1.92307);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b99f80() {
   return (neuron0x11bc2690()*0.399087);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b99fc0() {
   return (neuron0x11bc29a0()*0.0322995);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9a000() {
   return (neuron0x11b981e0()*1.67433);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9a040() {
   return (neuron0x11b98520()*0.0343952);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9a390() {
   return (neuron0x11b989a0()*0.130654);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9a3d0() {
   return (neuron0x11b98c20()*0.190429);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9a410() {
   return (neuron0x11b98ff0()*1.78991);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9a450() {
   return (neuron0x11b99400()*-1.28782);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9a490() {
   return (neuron0x11b99810()*1.28355);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9a4d0() {
   return (neuron0x11b99c70()*-0.523429);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9a850() {
   return (neuron0x11b989a0()*-0.202836);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9a890() {
   return (neuron0x11b98c20()*2.00151);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9a8d0() {
   return (neuron0x11b98ff0()*-0.398815);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11bc2440() {
   return (neuron0x11b99400()*1.84242);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b438c0() {
   return (neuron0x11b99810()*2.20245);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x12ab5700() {
   return (neuron0x11b99c70()*-0.0137901);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9ae60() {
   return (neuron0x11b989a0()*0.919129);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9aea0() {
   return (neuron0x11b98c20()*0.299754);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9aee0() {
   return (neuron0x11b98ff0()*-1.21633);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9af20() {
   return (neuron0x11b99400()*0.739003);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9af60() {
   return (neuron0x11b99810()*2.36841);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9afa0() {
   return (neuron0x11b99c70()*-1.56115);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9b320() {
   return (neuron0x11b9a080()*-1.89611);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9b360() {
   return (neuron0x11b9a510()*2.55145);
}

double MLP_Zbb_tt_Comb_met_EE::synapse0x11b9b3a0() {
   return (neuron0x11b9ab20()*-2.37445);
}

