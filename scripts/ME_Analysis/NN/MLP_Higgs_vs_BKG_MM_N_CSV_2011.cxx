#include "../NN/MLP_Higgs_vs_BKG_MM_N_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.507455)/0.336965;
   input1 = (in1 - 0.565711)/0.318639;
   input2 = (in2 - 0.512517)/0.362242;
   switch(index) {
     case 0:
         return neuron0xd8a7850();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 0.507455)/0.336965;
   input1 = (input[1] - 0.565711)/0.318639;
   input2 = (input[2] - 0.512517)/0.362242;
   switch(index) {
     case 0:
         return neuron0xd8a7850();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0xd8947e0() {
   return input0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0xd894af0() {
   return input1;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0xd8a59b0() {
   return input2;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0xd8a5d70() {
   double input = -1.32356;
   input += synapse0xd87d2e0();
   input += synapse0xd862b90();
   input += synapse0xd5f37a0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0xd8a5d70() {
   double input = input0xd8a5d70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0xd8a5ff0() {
   double input = -1.53434;
   input += synapse0xd8a6300();
   input += synapse0xd8a6340();
   input += synapse0xd8a6380();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0xd8a5ff0() {
   double input = input0xd8a5ff0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0xd8a63c0() {
   double input = 2.66392;
   input += synapse0xd8a66d0();
   input += synapse0xd8a6710();
   input += synapse0xd8a6750();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0xd8a63c0() {
   double input = input0xd8a63c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0xd8a6790() {
   double input = 2.54651;
   input += synapse0xd8a6aa0();
   input += synapse0xd8a6ae0();
   input += synapse0xd8a6b20();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0xd8a6790() {
   double input = input0xd8a6790();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0xd8a6b60() {
   double input = -0.0927941;
   input += synapse0xd8a6e70();
   input += synapse0xd8a6eb0();
   input += synapse0xd8a6ef0();
   input += synapse0xd8a6f30();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0xd8a6b60() {
   double input = input0xd8a6b60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0xd8a6f70() {
   double input = -0.244648;
   input += synapse0xd8a7280();
   input += synapse0xd5f3710();
   input += synapse0xd5f3750();
   input += synapse0xd8a73d0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0xd8a6f70() {
   double input = input0xd8a6f70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0xd8a7410() {
   double input = -1.00616;
   input += synapse0xd8a7750();
   input += synapse0xd8a7790();
   input += synapse0xd8a77d0();
   input += synapse0xd8a7810();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0xd8a7410() {
   double input = input0xd8a7410();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0xd8a7850() {
   double input = -0.196225;
   input += synapse0xd8a5cf0();
   input += synapse0xd8a5d30();
   input += synapse0xd8a7ad0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0xd8a7850() {
   double input = input0xd8a7850();
   return (input * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd87d2e0() {
   return (neuron0xd8947e0()*-2.11451);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd862b90() {
   return (neuron0xd894af0()*0.297929);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd5f37a0() {
   return (neuron0xd8a59b0()*2.13353);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6300() {
   return (neuron0xd8947e0()*-2.559);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6340() {
   return (neuron0xd894af0()*1.97731);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6380() {
   return (neuron0xd8a59b0()*-0.993133);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a66d0() {
   return (neuron0xd8947e0()*-1.5638);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6710() {
   return (neuron0xd894af0()*1.5264);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6750() {
   return (neuron0xd8a59b0()*2.00616);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6aa0() {
   return (neuron0xd8947e0()*0.512473);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6ae0() {
   return (neuron0xd894af0()*-0.604287);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6b20() {
   return (neuron0xd8a59b0()*-3.13947);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6e70() {
   return (neuron0xd8a5d70()*4.21374);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6eb0() {
   return (neuron0xd8a5ff0()*-0.775555);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6ef0() {
   return (neuron0xd8a63c0()*-4.84602);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a6f30() {
   return (neuron0xd8a6790()*-0.462846);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a7280() {
   return (neuron0xd8a5d70()*-4.84257);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd5f3710() {
   return (neuron0xd8a5ff0()*-1.81282);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd5f3750() {
   return (neuron0xd8a63c0()*-0.988987);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a73d0() {
   return (neuron0xd8a6790()*0.251943);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a7750() {
   return (neuron0xd8a5d70()*1.19087);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a7790() {
   return (neuron0xd8a5ff0()*-0.965074);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a77d0() {
   return (neuron0xd8a63c0()*1.00677);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a7810() {
   return (neuron0xd8a6790()*-1.27315);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a5cf0() {
   return (neuron0xd8a6b60()*-4.09388);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a5d30() {
   return (neuron0xd8a6f70()*2.57954);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0xd8a7ad0() {
   return (neuron0xd8a7410()*2.03629);
}

