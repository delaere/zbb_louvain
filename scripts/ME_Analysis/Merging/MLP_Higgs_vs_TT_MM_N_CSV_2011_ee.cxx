#include "MLP_Higgs_vs_TT_MM_N_CSV_2011_ee.h"
#include <cmath>

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.5229)/1.8106;
   input1 = (in1 - 25.2664)/1.59636;
   input2 = (in2 - 14.1289)/2.06328;
   switch(index) {
     case 0:
         return neuron0xd1f6c10();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::Value(int index, double* input) {
   input0 = (input[0] - 22.5229)/1.8106;
   input1 = (input[1] - 25.2664)/1.59636;
   input2 = (input[2] - 14.1289)/2.06328;
   switch(index) {
     case 0:
         return neuron0xd1f6c10();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::neuron0xd1e3970() {
   return input0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::neuron0xd1e3cb0() {
   return input1;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::neuron0xd1f4bf0() {
   return input2;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::input0xd1f4fd0() {
   double input = -0.405625;
   input += synapse0xd1ca660();
   input += synapse0xd1ac0b0();
   input += synapse0xd1f5280();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::neuron0xd1f4fd0() {
   double input = input0xd1f4fd0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::input0xd1f52c0() {
   double input = 3.55211;
   input += synapse0xd1f5600();
   input += synapse0xd1f5640();
   input += synapse0xd1f5680();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::neuron0xd1f52c0() {
   double input = input0xd1f52c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::input0xd1f56c0() {
   double input = -0.608235;
   input += synapse0xd1f5a00();
   input += synapse0xd1f5a40();
   input += synapse0xd1f5a80();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::neuron0xd1f56c0() {
   double input = input0xd1f56c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::input0xd1f5ac0() {
   double input = -1.35775;
   input += synapse0xd1f5e00();
   input += synapse0xd1f5e40();
   input += synapse0xd1f5e80();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::neuron0xd1f5ac0() {
   double input = input0xd1f5ac0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::input0xd1f5ec0() {
   double input = -3.05507;
   input += synapse0xd1f6200();
   input += synapse0xd1f6240();
   input += synapse0xd1f6280();
   input += synapse0xd1f62c0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::neuron0xd1f5ec0() {
   double input = input0xd1f5ec0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::input0xd1f6300() {
   double input = -0.858627;
   input += synapse0xd1f6640();
   input += synapse0xcf86c90();
   input += synapse0xcf86cd0();
   input += synapse0xd1f6790();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::neuron0xd1f6300() {
   double input = input0xd1f6300();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::input0xd1f67d0() {
   double input = 0.153608;
   input += synapse0xd1f6b10();
   input += synapse0xd1f6b50();
   input += synapse0xd1f6b90();
   input += synapse0xd1f6bd0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::neuron0xd1f67d0() {
   double input = input0xd1f67d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::input0xd1f6c10() {
   double input = 1.62702;
   input += synapse0xd1f6e30();
   input += synapse0xd1f6e70();
   input += synapse0xd1f6eb0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::neuron0xd1f6c10() {
   double input = input0xd1f6c10();
   return (input * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1ca660() {
   return (neuron0xd1e3970()*-1.63124);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1ac0b0() {
   return (neuron0xd1e3cb0()*1.13103);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f5280() {
   return (neuron0xd1f4bf0()*0.607423);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f5600() {
   return (neuron0xd1e3970()*3.55214);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f5640() {
   return (neuron0xd1e3cb0()*-12.8513);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f5680() {
   return (neuron0xd1f4bf0()*-0.810582);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f5a00() {
   return (neuron0xd1e3970()*-1.65318);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f5a40() {
   return (neuron0xd1e3cb0()*1.20848);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f5a80() {
   return (neuron0xd1f4bf0()*2.3802);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f5e00() {
   return (neuron0xd1e3970()*-1.11058);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f5e40() {
   return (neuron0xd1e3cb0()*3.71641);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f5e80() {
   return (neuron0xd1f4bf0()*-4.26322);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6200() {
   return (neuron0xd1f4fd0()*-18.6584);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6240() {
   return (neuron0xd1f52c0()*5.60704);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6280() {
   return (neuron0xd1f56c0()*14.2952);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f62c0() {
   return (neuron0xd1f5ac0()*6.5911);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6640() {
   return (neuron0xd1f4fd0()*0.722903);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xcf86c90() {
   return (neuron0xd1f52c0()*1.30767);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xcf86cd0() {
   return (neuron0xd1f56c0()*2.06335);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6790() {
   return (neuron0xd1f5ac0()*-0.0774771);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6b10() {
   return (neuron0xd1f4fd0()*-8.83512);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6b50() {
   return (neuron0xd1f52c0()*4.52439);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6b90() {
   return (neuron0xd1f56c0()*2.31319);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6bd0() {
   return (neuron0xd1f5ac0()*9.74333);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6e30() {
   return (neuron0xd1f5ec0()*0.822745);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6e70() {
   return (neuron0xd1f6300()*-1.86614);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_ee::synapse0xd1f6eb0() {
   return (neuron0xd1f67d0()*-0.276587);
}

