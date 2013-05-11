#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.445235)/0.307413;
   input1 = (in1 - 0.487302)/0.29068;
   input2 = (in2 - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x17eb9750();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::Value(int index, double* input) {
   input0 = (input[0] - 0.445235)/0.307413;
   input1 = (input[1] - 0.487302)/0.29068;
   input2 = (input[2] - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x17eb9750();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::neuron0x17ea65f0() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::neuron0x17ea6930() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::neuron0x17eb7900() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::input0x17eb7c50() {
   double input = -0.15607;
   input += synapse0x17e6edc0();
   input += synapse0x17e8d350();
   input += synapse0x17eb7f00();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::neuron0x17eb7c50() {
   double input = input0x17eb7c50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::input0x17eb7f40() {
   double input = 1.1345;
   input += synapse0x17eb8280();
   input += synapse0x17eb82c0();
   input += synapse0x17eb8300();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::neuron0x17eb7f40() {
   double input = input0x17eb7f40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::input0x17eb8340() {
   double input = 9.07702;
   input += synapse0x17eb8680();
   input += synapse0x17eb86c0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::neuron0x17eb8340() {
   double input = input0x17eb8340();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::input0x17eb8700() {
   double input = 3.29866;
   input += synapse0x17eb8a40();
   input += synapse0x17eb8a80();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::neuron0x17eb8700() {
   double input = input0x17eb8700();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::input0x17eb8ac0() {
   double input = -6.35498;
   input += synapse0x17eb8e00();
   input += synapse0x17eb8e40();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::neuron0x17eb8ac0() {
   double input = input0x17eb8ac0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::input0x17eb8e80() {
   double input = 6.73508;
   input += synapse0x17eb91c0();
   input += synapse0x17eb9200();
   input += synapse0x17eb9240();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::neuron0x17eb8e80() {
   double input = input0x17eb8e80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::input0x17eb9280() {
   double input = 8.61803;
   input += synapse0x17eb95c0();
   input += synapse0x17eb9600();
   input += synapse0x17e19560();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::neuron0x17eb9280() {
   double input = input0x17eb9280();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::input0x17eb9750() {
   double input = 12.5818;
   input += synapse0x17eb9970();
   input += synapse0x17eb99b0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::neuron0x17eb9750() {
   double input = input0x17eb9750();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17e6edc0() {
   return (neuron0x17ea65f0()*0.427614);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17e8d350() {
   return (neuron0x17ea6930()*0.223767);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb7f00() {
   return (neuron0x17eb7900()*0.0361055);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb8280() {
   return (neuron0x17ea65f0()*-2.69032);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb82c0() {
   return (neuron0x17ea6930()*2.83829);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb8300() {
   return (neuron0x17eb7900()*-0.629683);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb8680() {
   return (neuron0x17eb7c50()*-10.2648);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb86c0() {
   return (neuron0x17eb7f40()*-4.9344);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb8a40() {
   return (neuron0x17eb7c50()*-2.91887);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb8a80() {
   return (neuron0x17eb7f40()*-3.79877);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb8e00() {
   return (neuron0x17eb7c50()*14.825);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb8e40() {
   return (neuron0x17eb7f40()*4.12621);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb91c0() {
   return (neuron0x17eb8340()*5.98097);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb9200() {
   return (neuron0x17eb8700()*-7.19742);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb9240() {
   return (neuron0x17eb8ac0()*-5.29588);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb95c0() {
   return (neuron0x17eb8340()*0.715516);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb9600() {
   return (neuron0x17eb8700()*-10.2471);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17e19560() {
   return (neuron0x17eb8ac0()*-9.49324);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb9970() {
   return (neuron0x17eb8e80()*-12.6019);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000::synapse0x17eb99b0() {
   return (neuron0x17eb9280()*-14.8207);
}

