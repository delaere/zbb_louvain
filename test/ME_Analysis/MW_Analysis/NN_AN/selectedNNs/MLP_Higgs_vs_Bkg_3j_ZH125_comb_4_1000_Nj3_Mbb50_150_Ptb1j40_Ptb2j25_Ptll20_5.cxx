#include "MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.467176)/0.243159;
   input1 = (in1 - 0.52708)/0.296356;
   input2 = (in2 - 0.534793)/0.314261;
   switch(index) {
     case 0:
         return neuron0x1af461f0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::Value(int index, double* input) {
   input0 = (input[0] - 0.467176)/0.243159;
   input1 = (input[1] - 0.52708)/0.296356;
   input2 = (input[2] - 0.534793)/0.314261;
   switch(index) {
     case 0:
         return neuron0x1af461f0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::neuron0x1af447d0() {
   return input0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::neuron0x1af44b10() {
   return input1;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::neuron0x1af44e50() {
   return input2;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::input0x1af452c0() {
   double input = 1.83721;
   input += synapse0x1aee98b0();
   input += synapse0x1af45570();
   input += synapse0x1af455b0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::neuron0x1af452c0() {
   double input = input0x1af452c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::input0x1af455f0() {
   double input = -6.69762;
   input += synapse0x1af45930();
   input += synapse0x1af45970();
   input += synapse0x1af459b0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::neuron0x1af455f0() {
   double input = input0x1af455f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::input0x1af459f0() {
   double input = 3.02561;
   input += synapse0x1af45d30();
   input += synapse0x1af45d70();
   input += synapse0x1af45db0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::neuron0x1af459f0() {
   double input = input0x1af459f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::input0x1af45df0() {
   double input = 5.51948;
   input += synapse0x1af46130();
   input += synapse0x1af46170();
   input += synapse0x1af461b0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::neuron0x1af45df0() {
   double input = input0x1af45df0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::input0x1af461f0() {
   double input = -5.15244;
   input += synapse0x1af46530();
   input += synapse0x1af46570();
   input += synapse0x1af465b0();
   input += synapse0x1af465f0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::neuron0x1af461f0() {
   double input = input0x1af461f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1aee98b0() {
   return (neuron0x1af447d0()*1.43032);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af45570() {
   return (neuron0x1af44b10()*-0.667705);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af455b0() {
   return (neuron0x1af44e50()*0.503382);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af45930() {
   return (neuron0x1af447d0()*1.17169);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af45970() {
   return (neuron0x1af44b10()*2.05728);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af459b0() {
   return (neuron0x1af44e50()*0.23943);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af45d30() {
   return (neuron0x1af447d0()*-1.56588);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af45d70() {
   return (neuron0x1af44b10()*0.414075);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af45db0() {
   return (neuron0x1af44e50()*-0.522695);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af46130() {
   return (neuron0x1af447d0()*1.44453);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af46170() {
   return (neuron0x1af44b10()*1.96007);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af461b0() {
   return (neuron0x1af44e50()*-0.584645);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af46530() {
   return (neuron0x1af452c0()*2.96846);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af46570() {
   return (neuron0x1af455f0()*5.70525);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af465b0() {
   return (neuron0x1af459f0()*-2.50075);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5::synapse0x1af465f0() {
   return (neuron0x1af45df0()*5.10093);
}

