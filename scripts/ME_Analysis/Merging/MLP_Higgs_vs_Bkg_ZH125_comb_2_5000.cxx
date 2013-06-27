#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_5000.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.445235)/0.307413;
   input1 = (in1 - 0.487302)/0.29068;
   input2 = (in2 - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x8ef5870();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::Value(int index, double* input) {
   input0 = (input[0] - 0.445235)/0.307413;
   input1 = (input[1] - 0.487302)/0.29068;
   input2 = (input[2] - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x8ef5870();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::neuron0x8ee3ae0() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::neuron0x8ee3e20() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::neuron0x8ef4df0() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::input0x8ef5140() {
   double input = -1.24181;
   input += synapse0x8eabef0();
   input += synapse0x8ef53f0();
   input += synapse0x8ef5430();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::neuron0x8ef5140() {
   double input = input0x8ef5140();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::input0x8ef5470() {
   double input = 0.886138;
   input += synapse0x8ef57b0();
   input += synapse0x8ef57f0();
   input += synapse0x8ef5830();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::neuron0x8ef5470() {
   double input = input0x8ef5470();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::input0x8ef5870() {
   double input = 125.051;
   input += synapse0x8ef5a90();
   input += synapse0x8ef5ad0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::neuron0x8ef5870() {
   double input = input0x8ef5870();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::synapse0x8eabef0() {
   return (neuron0x8ee3ae0()*0.104354);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::synapse0x8ef53f0() {
   return (neuron0x8ee3e20()*-0.356602);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::synapse0x8ef5430() {
   return (neuron0x8ef4df0()*0.354925);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::synapse0x8ef57b0() {
   return (neuron0x8ee3ae0()*-0.0769232);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::synapse0x8ef57f0() {
   return (neuron0x8ee3e20()*0.160928);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::synapse0x8ef5830() {
   return (neuron0x8ef4df0()*-0.186599);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::synapse0x8ef5a90() {
   return (neuron0x8ef5140()*-82.5782);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5000::synapse0x8ef5ad0() {
   return (neuron0x8ef5470()*-150.58);
}

