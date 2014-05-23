#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.445235)/0.307413;
   input1 = (in1 - 0.487302)/0.29068;
   input2 = (in2 - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0xc2487d0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::Value(int index, double* input) {
   input0 = (input[0] - 0.445235)/0.307413;
   input1 = (input[1] - 0.487302)/0.29068;
   input2 = (input[2] - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0xc2487d0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::neuron0xc235630() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::neuron0xc235970() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::neuron0xc246940() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::input0xc246c90() {
   double input = -3.00789;
   input += synapse0xc21c020();
   input += synapse0xc246f40();
   input += synapse0xc246f80();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::neuron0xc246c90() {
   double input = input0xc246c90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::input0xc246fc0() {
   double input = 3.15243;
   input += synapse0xc247300();
   input += synapse0xc247340();
   input += synapse0xc247380();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::neuron0xc246fc0() {
   double input = input0xc246fc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::input0xc2473c0() {
   double input = -1.82836;
   input += synapse0xc247700();
   input += synapse0xc247740();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::neuron0xc2473c0() {
   double input = input0xc2473c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::input0xc247780() {
   double input = -0.453903;
   input += synapse0xc247ac0();
   input += synapse0xc247b00();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::neuron0xc247780() {
   double input = input0xc247780();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::input0xc247b40() {
   double input = 7.47677;
   input += synapse0xc247e80();
   input += synapse0xc247ec0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::neuron0xc247b40() {
   double input = input0xc247b40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::input0xc247f00() {
   double input = -3.97876;
   input += synapse0xc248240();
   input += synapse0xc248280();
   input += synapse0xc2482c0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::neuron0xc247f00() {
   double input = input0xc247f00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::input0xc248300() {
   double input = 6.39321;
   input += synapse0xc248640();
   input += synapse0xc248680();
   input += synapse0xc1a7df0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::neuron0xc248300() {
   double input = input0xc248300();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::input0xc2487d0() {
   double input = 3.98922;
   input += synapse0xc2489f0();
   input += synapse0xc248a30();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::neuron0xc2487d0() {
   double input = input0xc2487d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc21c020() {
   return (neuron0xc235630()*0.529408);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc246f40() {
   return (neuron0xc235970()*0.284559);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc246f80() {
   return (neuron0xc246940()*0.633835);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc247300() {
   return (neuron0xc235630()*2.81423);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc247340() {
   return (neuron0xc235970()*0.565852);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc247380() {
   return (neuron0xc246940()*1.30298);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc247700() {
   return (neuron0xc246c90()*-2.0992);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc247740() {
   return (neuron0xc246fc0()*-3.69901);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc247ac0() {
   return (neuron0xc246c90()*-3.15759);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc247b00() {
   return (neuron0xc246fc0()*-9.53144);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc247e80() {
   return (neuron0xc246c90()*-10.4858);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc247ec0() {
   return (neuron0xc246fc0()*-4.64298);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc248240() {
   return (neuron0xc2473c0()*1.92283);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc248280() {
   return (neuron0xc247780()*3.23264);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc2482c0() {
   return (neuron0xc247b40()*14.8926);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc248640() {
   return (neuron0xc2473c0()*0.451754);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc248680() {
   return (neuron0xc247780()*-2.9629);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc1a7df0() {
   return (neuron0xc247b40()*-5.85746);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc2489f0() {
   return (neuron0xc247f00()*-11.8163);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000::synapse0xc248a30() {
   return (neuron0xc248300()*10.2919);
}

