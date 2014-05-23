#include "MLP_Higgs_vs_DY_MM_N_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.6041)/1.12509;
   input1 = (in1 - 20.2509)/0.989093;
   input2 = (in2 - 24.6395)/1.32045;
   input3 = (in3 - 13.3934)/1.61576;
   switch(index) {
     case 0:
         return neuron0x16dc4310();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 19.6041)/1.12509;
   input1 = (input[1] - 20.2509)/0.989093;
   input2 = (input[2] - 24.6395)/1.32045;
   input3 = (input[3] - 13.3934)/1.61576;
   switch(index) {
     case 0:
         return neuron0x16dc4310();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc10d0() {
   return input0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc1410() {
   return input1;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc1750() {
   return input2;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc1a90() {
   return input3;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0x16dc1f00() {
   double input = -0.475713;
   input += synapse0x16d9a300();
   input += synapse0x16dc21b0();
   input += synapse0x16dc21f0();
   input += synapse0x16dc2230();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc1f00() {
   double input = input0x16dc1f00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0x16dc2270() {
   double input = -0.173894;
   input += synapse0x16dc25b0();
   input += synapse0x16dc25f0();
   input += synapse0x16dc2630();
   input += synapse0x16dc2670();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc2270() {
   double input = input0x16dc2270();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0x16dc26b0() {
   double input = -5.15449;
   input += synapse0x16dc29f0();
   input += synapse0x16dc2a30();
   input += synapse0x16dc2a70();
   input += synapse0x16dc2ab0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc26b0() {
   double input = input0x16dc26b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0x16dc2af0() {
   double input = -3.17992;
   input += synapse0x16dc2e30();
   input += synapse0x16dc2e70();
   input += synapse0x16dc2eb0();
   input += synapse0x16dc2ef0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc2af0() {
   double input = input0x16dc2af0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0x16dc2f30() {
   double input = -0.234227;
   input += synapse0x16dc3270();
   input += synapse0x16b3c850();
   input += synapse0x16b3c890();
   input += synapse0x16dc33c0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc2f30() {
   double input = input0x16dc2f30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0x16dc3400() {
   double input = 1.14675;
   input += synapse0x16dc3740();
   input += synapse0x16dc3780();
   input += synapse0x16dc37c0();
   input += synapse0x16dc3800();
   input += synapse0x16dc3840();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc3400() {
   double input = input0x16dc3400();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0x16dc3880() {
   double input = -0.234373;
   input += synapse0x16dc3bc0();
   input += synapse0x16dc3c00();
   input += synapse0x16dc3c40();
   input += synapse0x16dc3c80();
   input += synapse0x16dc3cc0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc3880() {
   double input = input0x16dc3880();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0x16dc3d00() {
   double input = 2.14924;
   input += synapse0x16dc4040();
   input += synapse0x16dc4080();
   input += synapse0x16dc40c0();
   input += synapse0x16d623e0();
   input += synapse0x16d9a340();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc3d00() {
   double input = input0x16dc3d00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0x16dc4310() {
   double input = 1.86412;
   input += synapse0x16dc4650();
   input += synapse0x16dc4690();
   input += synapse0x16dc46d0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0x16dc4310() {
   double input = input0x16dc4310();
   return (input * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16d9a300() {
   return (neuron0x16dc10d0()*2.10722);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc21b0() {
   return (neuron0x16dc1410()*-1.27829);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc21f0() {
   return (neuron0x16dc1750()*0.453924);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc2230() {
   return (neuron0x16dc1a90()*-2.23545);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc25b0() {
   return (neuron0x16dc10d0()*0.986947);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc25f0() {
   return (neuron0x16dc1410()*-0.821574);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc2630() {
   return (neuron0x16dc1750()*-1.72104);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc2670() {
   return (neuron0x16dc1a90()*-0.35294);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc29f0() {
   return (neuron0x16dc10d0()*0.871823);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc2a30() {
   return (neuron0x16dc1410()*-4.57078);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc2a70() {
   return (neuron0x16dc1750()*5.49874);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc2ab0() {
   return (neuron0x16dc1a90()*-1.30372);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc2e30() {
   return (neuron0x16dc10d0()*0.899982);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc2e70() {
   return (neuron0x16dc1410()*-3.41288);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc2eb0() {
   return (neuron0x16dc1750()*3.53396);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc2ef0() {
   return (neuron0x16dc1a90()*-0.539077);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc3270() {
   return (neuron0x16dc10d0()*1.08775);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16b3c850() {
   return (neuron0x16dc1410()*-0.457794);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16b3c890() {
   return (neuron0x16dc1750()*-0.135153);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc33c0() {
   return (neuron0x16dc1a90()*-1.39016);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc3740() {
   return (neuron0x16dc1f00()*-1.75901);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc3780() {
   return (neuron0x16dc2270()*0.353439);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc37c0() {
   return (neuron0x16dc26b0()*-1.51503);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc3800() {
   return (neuron0x16dc2af0()*-0.31703);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc3840() {
   return (neuron0x16dc2f30()*0.114212);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc3bc0() {
   return (neuron0x16dc1f00()*0.765577);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc3c00() {
   return (neuron0x16dc2270()*0.594983);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc3c40() {
   return (neuron0x16dc26b0()*2.204);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc3c80() {
   return (neuron0x16dc2af0()*0.697016);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc3cc0() {
   return (neuron0x16dc2f30()*-0.460805);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc4040() {
   return (neuron0x16dc1f00()*-0.786401);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc4080() {
   return (neuron0x16dc2270()*0.554811);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc40c0() {
   return (neuron0x16dc26b0()*-0.710005);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16d623e0() {
   return (neuron0x16dc2af0()*-3.1878);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16d9a340() {
   return (neuron0x16dc2f30()*-4.05838);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc4650() {
   return (neuron0x16dc3400()*2.26393);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc4690() {
   return (neuron0x16dc3880()*-2.36429);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0x16dc46d0() {
   return (neuron0x16dc3d00()*-2.82111);
}

