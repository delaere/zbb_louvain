#include "MLP_Higgs_vs_Bkg_ZH125_comb_3_5000.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.445235)/0.307413;
   input1 = (in1 - 0.487302)/0.29068;
   input2 = (in2 - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x154a9c90();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::Value(int index, double* input) {
   input0 = (input[0] - 0.445235)/0.307413;
   input1 = (input[1] - 0.487302)/0.29068;
   input2 = (input[2] - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x154a9c90();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::neuron0x15497b00() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::neuron0x15497e40() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::neuron0x154a8e10() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::input0x154a9160() {
   double input = 2.7711;
   input += synapse0x1545ff10();
   input += synapse0x154a9410();
   input += synapse0x154a9450();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::neuron0x154a9160() {
   double input = input0x154a9160();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::input0x154a9490() {
   double input = -2.45782;
   input += synapse0x154a97d0();
   input += synapse0x154a9810();
   input += synapse0x154a9850();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::neuron0x154a9490() {
   double input = input0x154a9490();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::input0x154a9890() {
   double input = 7.00581;
   input += synapse0x154a9bd0();
   input += synapse0x154a9c10();
   input += synapse0x154a9c50();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::neuron0x154a9890() {
   double input = input0x154a9890();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::input0x154a9c90() {
   double input = -1.10986;
   input += synapse0x154a9eb0();
   input += synapse0x154a9ef0();
   input += synapse0x154a9f30();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::neuron0x154a9c90() {
   double input = input0x154a9c90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x1545ff10() {
   return (neuron0x15497b00()*0.364174);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x154a9410() {
   return (neuron0x15497e40()*0.597486);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x154a9450() {
   return (neuron0x154a8e10()*-0.107634);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x154a97d0() {
   return (neuron0x15497b00()*-0.67245);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x154a9810() {
   return (neuron0x15497e40()*1.14845);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x154a9850() {
   return (neuron0x154a8e10()*-1.47236);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x154a9bd0() {
   return (neuron0x15497b00()*-1.46949);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x154a9c10() {
   return (neuron0x15497e40()*-0.512995);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x154a9c50() {
   return (neuron0x154a8e10()*-1.4266);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x154a9eb0() {
   return (neuron0x154a9160()*18.8978);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x154a9ef0() {
   return (neuron0x154a9490()*-5.10573);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_5000::synapse0x154a9f30() {
   return (neuron0x154a9890()*-16.2122);
}

