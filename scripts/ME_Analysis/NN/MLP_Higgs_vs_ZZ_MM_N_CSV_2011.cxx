#include "../NN/MLP_Higgs_vs_ZZ_MM_N_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.2702)/1.27149;
   input1 = (in1 - 11.1467)/1.07286;
   input2 = (in2 - 24.5933)/1.16134;
   input3 = (in3 - 13.1535)/1.27098;
   switch(index) {
     case 0:
         return neuron0xf9c1840();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 21.2702)/1.27149;
   input1 = (input[1] - 11.1467)/1.07286;
   input2 = (input[2] - 24.5933)/1.16134;
   input3 = (input[3] - 13.1535)/1.27098;
   switch(index) {
     case 0:
         return neuron0xf9c1840();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9be840() {
   return input0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9beb50() {
   return input1;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9bee60() {
   return input2;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9bf170() {
   return input3;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::input0xf9bf5c0() {
   double input = 1.96968;
   input += synapse0xf967790();
   input += synapse0xf9bf840();
   input += synapse0xf9bf880();
   input += synapse0xf9bf8c0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9bf5c0() {
   double input = input0xf9bf5c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::input0xf9bf900() {
   double input = -0.346412;
   input += synapse0xf9bfc10();
   input += synapse0xf9bfc50();
   input += synapse0xf9bfc90();
   input += synapse0xf9bfcd0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9bf900() {
   double input = input0xf9bf900();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::input0xf9bfd10() {
   double input = -1.33769;
   input += synapse0xf9c0020();
   input += synapse0xf9c0060();
   input += synapse0xf9c00a0();
   input += synapse0xf9c00e0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9bfd10() {
   double input = input0xf9bfd10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::input0xf9c0120() {
   double input = -6.35164;
   input += synapse0xf9c0430();
   input += synapse0xf9c0470();
   input += synapse0xf9c04b0();
   input += synapse0xf9c04f0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9c0120() {
   double input = input0xf9c0120();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::input0xf9c0530() {
   double input = -1.78818;
   input += synapse0xf9c0840();
   input += synapse0xf967390();
   input += synapse0xf703d90();
   input += synapse0xf703dd0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9c0530() {
   double input = input0xf9c0530();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::input0xf9c0990() {
   double input = -0.894;
   input += synapse0xf9c0ca0();
   input += synapse0xf9c0ce0();
   input += synapse0xf9c0d20();
   input += synapse0xf9c0d60();
   input += synapse0xf9c0da0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9c0990() {
   double input = input0xf9c0990();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::input0xf9c0de0() {
   double input = -0.992821;
   input += synapse0xf9c10f0();
   input += synapse0xf9c1130();
   input += synapse0xf9c1170();
   input += synapse0xf9c11b0();
   input += synapse0xf9c11f0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9c0de0() {
   double input = input0xf9c0de0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::input0xf9c1230() {
   double input = -1.01122;
   input += synapse0xf9c1570();
   input += synapse0xf9c15b0();
   input += synapse0xf9c15f0();
   input += synapse0xf981ff0();
   input += synapse0xf9c5540();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9c1230() {
   double input = input0xf9c1230();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::input0xf9c1840() {
   double input = -2.3865;
   input += synapse0xf9c1b80();
   input += synapse0xf9c1bc0();
   input += synapse0xf9c1c00();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::neuron0xf9c1840() {
   double input = input0xf9c1840();
   return (input * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf967790() {
   return (neuron0xf9be840()*1.83792);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9bf840() {
   return (neuron0xf9beb50()*1.91937);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9bf880() {
   return (neuron0xf9bee60()*-0.502388);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9bf8c0() {
   return (neuron0xf9bf170()*-0.823784);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9bfc10() {
   return (neuron0xf9be840()*-2.18805);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9bfc50() {
   return (neuron0xf9beb50()*-0.293444);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9bfc90() {
   return (neuron0xf9bee60()*0.147448);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9bfcd0() {
   return (neuron0xf9bf170()*-0.304136);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c0020() {
   return (neuron0xf9be840()*1.40427);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c0060() {
   return (neuron0xf9beb50()*-2.37329);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c00a0() {
   return (neuron0xf9bee60()*0.322321);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c00e0() {
   return (neuron0xf9bf170()*1.87391);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c0430() {
   return (neuron0xf9be840()*-3.98096);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c0470() {
   return (neuron0xf9beb50()*-1.03931);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c04b0() {
   return (neuron0xf9bee60()*1.67222);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c04f0() {
   return (neuron0xf9bf170()*2.95659);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c0840() {
   return (neuron0xf9be840()*3.33966);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf967390() {
   return (neuron0xf9beb50()*0.189088);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf703d90() {
   return (neuron0xf9bee60()*0.505595);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf703dd0() {
   return (neuron0xf9bf170()*-1.51966);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c0ca0() {
   return (neuron0xf9bf5c0()*1.3189);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c0ce0() {
   return (neuron0xf9bf900()*2.63049);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c0d20() {
   return (neuron0xf9bfd10()*-1.9653);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c0d60() {
   return (neuron0xf9c0120()*3.27031);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c0da0() {
   return (neuron0xf9c0530()*3.5591);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c10f0() {
   return (neuron0xf9bf5c0()*-1.98159);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c1130() {
   return (neuron0xf9bf900()*-3.22643);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c1170() {
   return (neuron0xf9bfd10()*4.20373);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c11b0() {
   return (neuron0xf9c0120()*-3.10441);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c11f0() {
   return (neuron0xf9c0530()*-5.13396);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c1570() {
   return (neuron0xf9bf5c0()*3.14869);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c15b0() {
   return (neuron0xf9bf900()*2.3845);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c15f0() {
   return (neuron0xf9bfd10()*-1.04638);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf981ff0() {
   return (neuron0xf9c0120()*-2.83898);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c5540() {
   return (neuron0xf9c0530()*-0.396245);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c1b80() {
   return (neuron0xf9c0990()*2.3988);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c1bc0() {
   return (neuron0xf9c0de0()*2.23452);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011::synapse0xf9c1c00() {
   return (neuron0xf9c1230()*1.1529);
}

