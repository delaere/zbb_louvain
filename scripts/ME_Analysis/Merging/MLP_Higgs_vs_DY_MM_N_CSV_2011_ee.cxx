#include "MLP_Higgs_vs_DY_MM_N_CSV_2011_ee.h"
#include <cmath>

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.623)/1.05526;
   input1 = (in1 - 20.2582)/0.921746;
   input2 = (in2 - 24.5927)/1.2431;
   input3 = (in3 - 13.2734)/1.51989;
   switch(index) {
     case 0:
         return neuron0x8e80040();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::Value(int index, double* input) {
   input0 = (input[0] - 19.623)/1.05526;
   input1 = (input[1] - 20.2582)/0.921746;
   input2 = (input[2] - 24.5927)/1.2431;
   input3 = (input[3] - 13.2734)/1.51989;
   switch(index) {
     case 0:
         return neuron0x8e80040();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7ce00() {
   return input0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7d140() {
   return input1;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7d480() {
   return input2;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7d7c0() {
   return input3;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::input0x8e7dc30() {
   double input = 1.95908;
   input += synapse0x8e56030();
   input += synapse0x8e7dee0();
   input += synapse0x8e7df20();
   input += synapse0x8e7df60();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7dc30() {
   double input = input0x8e7dc30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::input0x8e7dfa0() {
   double input = 1.55599;
   input += synapse0x8e7e2e0();
   input += synapse0x8e7e320();
   input += synapse0x8e7e360();
   input += synapse0x8e7e3a0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7dfa0() {
   double input = input0x8e7dfa0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::input0x8e7e3e0() {
   double input = -1.45701;
   input += synapse0x8e7e720();
   input += synapse0x8e7e760();
   input += synapse0x8e7e7a0();
   input += synapse0x8e7e7e0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7e3e0() {
   double input = input0x8e7e3e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::input0x8e7e820() {
   double input = 9.00607;
   input += synapse0x8e7eb60();
   input += synapse0x8e7eba0();
   input += synapse0x8e7ebe0();
   input += synapse0x8e7ec20();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7e820() {
   double input = input0x8e7e820();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::input0x8e7ec60() {
   double input = -7.2149;
   input += synapse0x8e7efa0();
   input += synapse0x8bf85d0();
   input += synapse0x8bf8610();
   input += synapse0x8e7f0f0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7ec60() {
   double input = input0x8e7ec60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::input0x8e7f130() {
   double input = -2.66385;
   input += synapse0x8e7f470();
   input += synapse0x8e7f4b0();
   input += synapse0x8e7f4f0();
   input += synapse0x8e7f530();
   input += synapse0x8e7f570();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7f130() {
   double input = input0x8e7f130();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::input0x8e7f5b0() {
   double input = 0.00378352;
   input += synapse0x8e7f8f0();
   input += synapse0x8e7f930();
   input += synapse0x8e7f970();
   input += synapse0x8e7f9b0();
   input += synapse0x8e7f9f0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7f5b0() {
   double input = input0x8e7f5b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::input0x8e7fa30() {
   double input = -1.14181;
   input += synapse0x8e7fd70();
   input += synapse0x8e7fdb0();
   input += synapse0x8e7fdf0();
   input += synapse0x8e1e110();
   input += synapse0x8e56070();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e7fa30() {
   double input = input0x8e7fa30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::input0x8e80040() {
   double input = -0.317425;
   input += synapse0x8e80380();
   input += synapse0x8e803c0();
   input += synapse0x8e80400();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::neuron0x8e80040() {
   double input = input0x8e80040();
   return (input * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e56030() {
   return (neuron0x8e7ce00()*-1.5222);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7dee0() {
   return (neuron0x8e7d140()*-0.922538);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7df20() {
   return (neuron0x8e7d480()*-0.377478);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7df60() {
   return (neuron0x8e7d7c0()*2.94206);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7e2e0() {
   return (neuron0x8e7ce00()*7.38961);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7e320() {
   return (neuron0x8e7d140()*-6.79607);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7e360() {
   return (neuron0x8e7d480()*0.462224);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7e3a0() {
   return (neuron0x8e7d7c0()*-2.55472);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7e720() {
   return (neuron0x8e7ce00()*-1.90894);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7e760() {
   return (neuron0x8e7d140()*2.38693);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7e7a0() {
   return (neuron0x8e7d480()*-1.0644);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7e7e0() {
   return (neuron0x8e7d7c0()*-4.03057);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7eb60() {
   return (neuron0x8e7ce00()*-2.4021);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7eba0() {
   return (neuron0x8e7d140()*7.02496);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7ebe0() {
   return (neuron0x8e7d480()*-6.14014);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7ec20() {
   return (neuron0x8e7d7c0()*1.46499);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7efa0() {
   return (neuron0x8e7ce00()*5.62368);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8bf85d0() {
   return (neuron0x8e7d140()*1.18202);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8bf8610() {
   return (neuron0x8e7d480()*0.0611741);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7f0f0() {
   return (neuron0x8e7d7c0()*-8.19637);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7f470() {
   return (neuron0x8e7dc30()*3.56014);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7f4b0() {
   return (neuron0x8e7dfa0()*-1.5265);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7f4f0() {
   return (neuron0x8e7e3e0()*-0.318925);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7f530() {
   return (neuron0x8e7e820()*-0.669192);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7f570() {
   return (neuron0x8e7ec60()*0.141685);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7f8f0() {
   return (neuron0x8e7dc30()*1.01833);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7f930() {
   return (neuron0x8e7dfa0()*1.51973);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7f970() {
   return (neuron0x8e7e3e0()*0.368364);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7f9b0() {
   return (neuron0x8e7e820()*0.895105);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7f9f0() {
   return (neuron0x8e7ec60()*2.08282);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7fd70() {
   return (neuron0x8e7dc30()*4.66453);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7fdb0() {
   return (neuron0x8e7dfa0()*-1.37617);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e7fdf0() {
   return (neuron0x8e7e3e0()*3.68995);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e1e110() {
   return (neuron0x8e7e820()*1.34398);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e56070() {
   return (neuron0x8e7ec60()*5.88403);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e80380() {
   return (neuron0x8e7f130()*-2.08404);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e803c0() {
   return (neuron0x8e7f5b0()*-2.42036);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_ee::synapse0x8e80400() {
   return (neuron0x8e7fa30()*3.70322);
}

