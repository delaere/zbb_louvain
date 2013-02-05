#include "../NN/MLP_Higgs_vs_TT_MM_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_TT_MM_CSV_2011::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.3415)/1.59175;
   input1 = (in1 - 25.9164)/1.8104;
   input2 = (in2 - 14.8962)/2.32414;
   switch(index) {
     case 0:
         return neuron0x1b2bdcf0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 22.3415)/1.59175;
   input1 = (input[1] - 25.9164)/1.8104;
   input2 = (input[2] - 14.8962)/2.32414;
   switch(index) {
     case 0:
         return neuron0x1b2bdcf0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2a9ac0() {
   return input0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2a9dd0() {
   return input1;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bac30() {
   return input2;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bb080() {
   double input = -0.171086;
   input += synapse0x1b277d80();
   input += synapse0x1b291cf0();
   input += synapse0x1b277e10();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bb080() {
   double input = input0x1b2bb080();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bb300() {
   double input = -4.22905;
   input += synapse0x1b2aa050();
   input += synapse0x1b2bb610();
   input += synapse0x1b2bb650();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bb300() {
   double input = input0x1b2bb300();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bb690() {
   double input = -0.892798;
   input += synapse0x1b2bb9a0();
   input += synapse0x1b2bb9e0();
   input += synapse0x1b2bba20();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bb690() {
   double input = input0x1b2bb690();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bba60() {
   double input = 0.215353;
   input += synapse0x1b2bbd70();
   input += synapse0x1b2bbdb0();
   input += synapse0x1b2bbdf0();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bba60() {
   double input = input0x1b2bba60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bbe30() {
   double input = 1.73731;
   input += synapse0x1b2bc140();
   input += synapse0x1b2bc180();
   input += synapse0x1b2bc1c0();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bbe30() {
   double input = input0x1b2bbe30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bc200() {
   double input = 1.2911;
   input += synapse0x1b2bc510();
   input += synapse0x1b2bc550();
   input += synapse0x1b008940();
   input += synapse0x1b008980();
   input += synapse0x1b2bc6a0();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bc200() {
   double input = input0x1b2bc200();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bc6e0() {
   double input = -1.98193;
   input += synapse0x1b2bca20();
   input += synapse0x1b2bca60();
   input += synapse0x1b2bcaa0();
   input += synapse0x1b2bcae0();
   input += synapse0x1b2bcb20();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bc6e0() {
   double input = input0x1b2bc6e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bcb60() {
   double input = 1.2147;
   input += synapse0x1b2bcea0();
   input += synapse0x1b2bcee0();
   input += synapse0x1b2bcf20();
   input += synapse0x1b2bcf60();
   input += synapse0x1b2bcfa0();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bcb60() {
   double input = input0x1b2bcb60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bcfe0() {
   double input = 0.415817;
   input += synapse0x1b2bd320();
   input += synapse0x1b2bd360();
   input += synapse0x1b2bd3a0();
   input += synapse0x1b2a9930();
   input += synapse0x1b292580();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bcfe0() {
   double input = input0x1b2bcfe0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bd5f0() {
   double input = -0.736623;
   input += synapse0x1b2779b0();
   input += synapse0x1b2bc620();
   input += synapse0x1b2bc660();
   input += synapse0x1b2bd870();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bd5f0() {
   double input = input0x1b2bd5f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bd8b0() {
   double input = -0.921715;
   input += synapse0x1b2bdbf0();
   input += synapse0x1b2bdc30();
   input += synapse0x1b2bdc70();
   input += synapse0x1b2bdcb0();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bd8b0() {
   double input = input0x1b2bd8b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::input0x1b2bdcf0() {
   double input = -1.16187;
   input += synapse0x1b2bb000();
   input += synapse0x1b2bb040();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::neuron0x1b2bdcf0() {
   double input = input0x1b2bdcf0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b277d80() {
   return (neuron0x1b2a9ac0()*-1.60558);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b291cf0() {
   return (neuron0x1b2a9dd0()*-1.64874);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b277e10() {
   return (neuron0x1b2bac30()*4.64331);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2aa050() {
   return (neuron0x1b2a9ac0()*-3.56348);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bb610() {
   return (neuron0x1b2a9dd0()*-1.09779);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bb650() {
   return (neuron0x1b2bac30()*-1.29487);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bb9a0() {
   return (neuron0x1b2a9ac0()*-1.46775);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bb9e0() {
   return (neuron0x1b2a9dd0()*-4.39282);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bba20() {
   return (neuron0x1b2bac30()*9.64347);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bbd70() {
   return (neuron0x1b2a9ac0()*1.16628);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bbdb0() {
   return (neuron0x1b2a9dd0()*-1.79586);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bbdf0() {
   return (neuron0x1b2bac30()*-1.70211);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bc140() {
   return (neuron0x1b2a9ac0()*-4.65498);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bc180() {
   return (neuron0x1b2a9dd0()*4.25961);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bc1c0() {
   return (neuron0x1b2bac30()*-0.705655);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bc510() {
   return (neuron0x1b2bb080()*-2.61122);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bc550() {
   return (neuron0x1b2bb300()*0.259926);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b008940() {
   return (neuron0x1b2bb690()*5.06314);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b008980() {
   return (neuron0x1b2bba60()*5.41524);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bc6a0() {
   return (neuron0x1b2bbe30()*-3.14023);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bca20() {
   return (neuron0x1b2bb080()*3.02329);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bca60() {
   return (neuron0x1b2bb300()*3.09075);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bcaa0() {
   return (neuron0x1b2bb690()*4.71191);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bcae0() {
   return (neuron0x1b2bba60()*0.99162);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bcb20() {
   return (neuron0x1b2bbe30()*-1.58427);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bcea0() {
   return (neuron0x1b2bb080()*2.29302);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bcee0() {
   return (neuron0x1b2bb300()*-2.93842);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bcf20() {
   return (neuron0x1b2bb690()*-6.2358);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bcf60() {
   return (neuron0x1b2bba60()*-0.333698);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bcfa0() {
   return (neuron0x1b2bbe30()*1.55783);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bd320() {
   return (neuron0x1b2bb080()*2.67368);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bd360() {
   return (neuron0x1b2bb300()*-4.00961);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bd3a0() {
   return (neuron0x1b2bb690()*-2.42273);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2a9930() {
   return (neuron0x1b2bba60()*-2.85599);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b292580() {
   return (neuron0x1b2bbe30()*0.731145);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2779b0() {
   return (neuron0x1b2bc200()*5.87593);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bc620() {
   return (neuron0x1b2bc6e0()*-4.36136);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bc660() {
   return (neuron0x1b2bcb60()*-5.2194);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bd870() {
   return (neuron0x1b2bcfe0()*-3.10898);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bdbf0() {
   return (neuron0x1b2bc200()*0.994961);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bdc30() {
   return (neuron0x1b2bc6e0()*-0.210539);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bdc70() {
   return (neuron0x1b2bcb60()*0.607813);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bdcb0() {
   return (neuron0x1b2bcfe0()*0.938576);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bb000() {
   return (neuron0x1b2bd5f0()*1.9158);
}

double MLP_Higgs_vs_TT_MM_CSV_2011::synapse0x1b2bb040() {
   return (neuron0x1b2bd8b0()*1.91226);
}

