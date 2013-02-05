#include "../NN/MLP_Higgs_vs_BKG_ML_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_BKG_ML_CSV_2011::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.475354)/0.304336;
   input1 = (in1 - 0.503382)/0.273779;
   input2 = (in2 - 0.470322)/0.36961;
   switch(index) {
     case 0:
         return neuron0x91d9250();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 0.475354)/0.304336;
   input1 = (input[1] - 0.503382)/0.273779;
   input2 = (input[2] - 0.470322)/0.36961;
   switch(index) {
     case 0:
         return neuron0x91d9250();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::neuron0x91c61e0() {
   return input0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::neuron0x91c64f0() {
   return input1;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::neuron0x91d73b0() {
   return input2;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::input0x91d7770() {
   double input = -1.38539;
   input += synapse0x91aece0();
   input += synapse0x9194590();
   input += synapse0x8f25220();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::neuron0x91d7770() {
   double input = input0x91d7770();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::input0x91d79f0() {
   double input = -1.11399;
   input += synapse0x91d7d00();
   input += synapse0x91d7d40();
   input += synapse0x91d7d80();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::neuron0x91d79f0() {
   double input = input0x91d79f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::input0x91d7dc0() {
   double input = 0.270128;
   input += synapse0x91d80d0();
   input += synapse0x91d8110();
   input += synapse0x91d8150();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::neuron0x91d7dc0() {
   double input = input0x91d7dc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::input0x91d8190() {
   double input = 2.18982;
   input += synapse0x91d84a0();
   input += synapse0x91d84e0();
   input += synapse0x91d8520();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::neuron0x91d8190() {
   double input = input0x91d8190();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::input0x91d8560() {
   double input = -2.61198;
   input += synapse0x91d8870();
   input += synapse0x91d88b0();
   input += synapse0x91d88f0();
   input += synapse0x91d8930();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::neuron0x91d8560() {
   double input = input0x91d8560();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::input0x91d8970() {
   double input = -1.09631;
   input += synapse0x91d8c80();
   input += synapse0x8f25190();
   input += synapse0x8f251d0();
   input += synapse0x91d8dd0();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::neuron0x91d8970() {
   double input = input0x91d8970();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::input0x91d8e10() {
   double input = -0.74994;
   input += synapse0x91d9150();
   input += synapse0x91d9190();
   input += synapse0x91d91d0();
   input += synapse0x91d9210();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::neuron0x91d8e10() {
   double input = input0x91d8e10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::input0x91d9250() {
   double input = -0.684325;
   input += synapse0x91d76f0();
   input += synapse0x91d7730();
   input += synapse0x91d94d0();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::neuron0x91d9250() {
   double input = input0x91d9250();
   return (input * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91aece0() {
   return (neuron0x91c61e0()*1.74774);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x9194590() {
   return (neuron0x91c64f0()*0.560615);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x8f25220() {
   return (neuron0x91d73b0()*0.921151);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d7d00() {
   return (neuron0x91c61e0()*1.12432);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d7d40() {
   return (neuron0x91c64f0()*0.113292);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d7d80() {
   return (neuron0x91d73b0()*0.415);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d80d0() {
   return (neuron0x91c61e0()*-1.00072);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d8110() {
   return (neuron0x91c64f0()*-0.238454);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d8150() {
   return (neuron0x91d73b0()*1.08203);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d84a0() {
   return (neuron0x91c61e0()*-3.38954);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d84e0() {
   return (neuron0x91c64f0()*-1.10914);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d8520() {
   return (neuron0x91d73b0()*-1.63045);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d8870() {
   return (neuron0x91d7770()*-5.98927);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d88b0() {
   return (neuron0x91d79f0()*4.40362);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d88f0() {
   return (neuron0x91d7dc0()*4.7137);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d8930() {
   return (neuron0x91d8190()*-2.11505);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d8c80() {
   return (neuron0x91d7770()*-4.6964);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x8f25190() {
   return (neuron0x91d79f0()*6.81539);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x8f251d0() {
   return (neuron0x91d7dc0()*2.60592);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d8dd0() {
   return (neuron0x91d8190()*-1.06153);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d9150() {
   return (neuron0x91d7770()*-4.29617);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d9190() {
   return (neuron0x91d79f0()*4.20331);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d91d0() {
   return (neuron0x91d7dc0()*2.69294);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d9210() {
   return (neuron0x91d8190()*-1.64136);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d76f0() {
   return (neuron0x91d8560()*-1.62869);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d7730() {
   return (neuron0x91d8970()*2.56438);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011::synapse0x91d94d0() {
   return (neuron0x91d8e10()*-0.335217);
}

