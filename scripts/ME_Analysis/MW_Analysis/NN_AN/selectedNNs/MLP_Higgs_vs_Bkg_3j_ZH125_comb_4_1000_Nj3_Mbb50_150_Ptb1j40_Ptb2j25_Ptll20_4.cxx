#include "MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.467176)/0.243159;
   input1 = (in1 - 0.52708)/0.296356;
   input2 = (in2 - 0.534793)/0.314261;
   switch(index) {
     case 0:
         return neuron0x25593ed0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::Value(int index, double* input) {
   input0 = (input[0] - 0.467176)/0.243159;
   input1 = (input[1] - 0.52708)/0.296356;
   input2 = (input[2] - 0.534793)/0.314261;
   switch(index) {
     case 0:
         return neuron0x25593ed0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x255924b0() {
   return input0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x255927f0() {
   return input1;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x25592b30() {
   return input2;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x25592fa0() {
   double input = -4.55567;
   input += synapse0x25537690();
   input += synapse0x25593250();
   input += synapse0x25593290();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x25592fa0() {
   double input = input0x25592fa0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x255932d0() {
   double input = -0.932204;
   input += synapse0x25593610();
   input += synapse0x25593650();
   input += synapse0x25593690();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x255932d0() {
   double input = input0x255932d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x255936d0() {
   double input = -4.08063;
   input += synapse0x25593a10();
   input += synapse0x25593a50();
   input += synapse0x25593a90();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x255936d0() {
   double input = input0x255936d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x25593ad0() {
   double input = -1.85149;
   input += synapse0x25593e10();
   input += synapse0x25593e50();
   input += synapse0x25593e90();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x25593ad0() {
   double input = input0x25593ad0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x25593ed0() {
   double input = 1.40773;
   input += synapse0x25537720();
   input += synapse0x25594210();
   input += synapse0x25594250();
   input += synapse0x25594290();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x25593ed0() {
   double input = input0x25593ed0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25537690() {
   return (neuron0x255924b0()*0.804113);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25593250() {
   return (neuron0x255927f0()*0.969853);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25593290() {
   return (neuron0x25592b30()*0.548829);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25593610() {
   return (neuron0x255924b0()*-0.930656);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25593650() {
   return (neuron0x255927f0()*1.11734);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25593690() {
   return (neuron0x25592b30()*0.510812);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25593a10() {
   return (neuron0x255924b0()*-1.21567);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25593a50() {
   return (neuron0x255927f0()*-1.19317);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25593a90() {
   return (neuron0x25592b30()*0.52627);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25593e10() {
   return (neuron0x255924b0()*-0.359804);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25593e50() {
   return (neuron0x255927f0()*0.0877854);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25593e90() {
   return (neuron0x25592b30()*-1.13552);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25537720() {
   return (neuron0x25592fa0()*8.39681);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25594210() {
   return (neuron0x255932d0()*-2.26312);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25594250() {
   return (neuron0x255936d0()*-6.63535);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x25594290() {
   return (neuron0x25593ad0()*-3.43646);
}

