#include "MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.467176)/0.243159;
   input1 = (in1 - 0.52708)/0.296356;
   input2 = (in2 - 0.534793)/0.314261;
   switch(index) {
     case 0:
         return neuron0x2d8835c0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::Value(int index, double* input) {
   input0 = (input[0] - 0.467176)/0.243159;
   input1 = (input[1] - 0.52708)/0.296356;
   input2 = (input[2] - 0.534793)/0.314261;
   switch(index) {
     case 0:
         return neuron0x2d8835c0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x2d8817a0() {
   return input0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x2d881ae0() {
   return input1;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x2d881e20() {
   return input2;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::input0x2d882290() {
   double input = -7.90421;
   input += synapse0x2d826930();
   input += synapse0x2d882540();
   input += synapse0x2d882580();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x2d882290() {
   double input = input0x2d882290();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::input0x2d8825c0() {
   double input = 2.18231;
   input += synapse0x2d882900();
   input += synapse0x2d882940();
   input += synapse0x2d882980();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x2d8825c0() {
   double input = input0x2d8825c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::input0x2d8829c0() {
   double input = 1.70494;
   input += synapse0x2d882d00();
   input += synapse0x2d882d40();
   input += synapse0x2d882d80();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x2d8829c0() {
   double input = input0x2d8829c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::input0x2d882dc0() {
   double input = 1.9539;
   input += synapse0x2d883100();
   input += synapse0x2d883140();
   input += synapse0x2d883180();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x2d882dc0() {
   double input = input0x2d882dc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::input0x2d8831c0() {
   double input = -6.40271;
   input += synapse0x2d883500();
   input += synapse0x2d883540();
   input += synapse0x2d883580();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x2d8831c0() {
   double input = input0x2d8831c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::input0x2d8835c0() {
   double input = -4.20094;
   input += synapse0x2d883900();
   input += synapse0x2d883940();
   input += synapse0x2d816b40();
   input += synapse0x2d816b80();
   input += synapse0x2d826a40();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::neuron0x2d8835c0() {
   double input = input0x2d8835c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d826930() {
   return (neuron0x2d8817a0()*-1.81316);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d882540() {
   return (neuron0x2d881ae0()*-2.79159);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d882580() {
   return (neuron0x2d881e20()*0.382289);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d882900() {
   return (neuron0x2d8817a0()*0.771404);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d882940() {
   return (neuron0x2d881ae0()*-0.770748);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d882980() {
   return (neuron0x2d881e20()*1.41563);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d882d00() {
   return (neuron0x2d8817a0()*0.882241);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d882d40() {
   return (neuron0x2d881ae0()*0.774728);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d882d80() {
   return (neuron0x2d881e20()*-1.18669);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d883100() {
   return (neuron0x2d8817a0()*-0.110115);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d883140() {
   return (neuron0x2d881ae0()*2.03634);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d883180() {
   return (neuron0x2d881e20()*-2.21034);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d883500() {
   return (neuron0x2d8817a0()*1.57379);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d883540() {
   return (neuron0x2d881ae0()*1.84907);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d883580() {
   return (neuron0x2d881e20()*0.222873);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d883900() {
   return (neuron0x2d882290()*-5.57171);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d883940() {
   return (neuron0x2d8825c0()*2.76523);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d816b40() {
   return (neuron0x2d8829c0()*4.52041);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d816b80() {
   return (neuron0x2d882dc0()*-2.25213);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1::synapse0x2d826a40() {
   return (neuron0x2d8831c0()*5.49871);
}

