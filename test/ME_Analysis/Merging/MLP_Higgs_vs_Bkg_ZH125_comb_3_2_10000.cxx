#include "MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.445235)/0.307413;
   input1 = (in1 - 0.487302)/0.29068;
   input2 = (in2 - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x11ddaf20();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::Value(int index, double* input) {
   input0 = (input[0] - 0.445235)/0.307413;
   input1 = (input[1] - 0.487302)/0.29068;
   input2 = (input[2] - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x11ddaf20();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::neuron0x11dc85d0() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::neuron0x11dc8910() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::neuron0x11dd98e0() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::input0x11dd9c30() {
   double input = -0.0885877;
   input += synapse0x11d90e20();
   input += synapse0x11daf370();
   input += synapse0x11dd9ee0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::neuron0x11dd9c30() {
   double input = input0x11dd9c30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::input0x11dd9f20() {
   double input = -7.30954;
   input += synapse0x11dda260();
   input += synapse0x11dda2a0();
   input += synapse0x11dda2e0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::neuron0x11dd9f20() {
   double input = input0x11dd9f20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::input0x11dda320() {
   double input = -0.618381;
   input += synapse0x11dda660();
   input += synapse0x11dda6a0();
   input += synapse0x11dda6e0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::neuron0x11dda320() {
   double input = input0x11dda320();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::input0x11dda720() {
   double input = 9.94111;
   input += synapse0x11ddaa60();
   input += synapse0x11ddaaa0();
   input += synapse0x11ddaae0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::neuron0x11dda720() {
   double input = input0x11dda720();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::input0x11ddab20() {
   double input = 8.87164;
   input += synapse0x11ddae60();
   input += synapse0x11ddaea0();
   input += synapse0x11ddaee0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::neuron0x11ddab20() {
   double input = input0x11ddab20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::input0x11ddaf20() {
   double input = -2.51561;
   input += synapse0x11ddb140();
   input += synapse0x11ddb180();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::neuron0x11ddaf20() {
   double input = input0x11ddaf20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11d90e20() {
   return (neuron0x11dc85d0()*-0.108109);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11daf370() {
   return (neuron0x11dc8910()*-0.210235);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11dd9ee0() {
   return (neuron0x11dd98e0()*0.00137662);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11dda260() {
   return (neuron0x11dc85d0()*0.255684);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11dda2a0() {
   return (neuron0x11dc8910()*0.72954);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11dda2e0() {
   return (neuron0x11dd98e0()*-2.24323);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11dda660() {
   return (neuron0x11dc85d0()*-1.67782);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11dda6a0() {
   return (neuron0x11dc8910()*3.60838);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11dda6e0() {
   return (neuron0x11dd98e0()*-0.289525);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11ddaa60() {
   return (neuron0x11dd9c30()*-15.5859);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11ddaaa0() {
   return (neuron0x11dd9f20()*-7.16614);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11ddaae0() {
   return (neuron0x11dda320()*-5.22764);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11ddae60() {
   return (neuron0x11dd9c30()*-11.8756);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11ddaea0() {
   return (neuron0x11dd9f20()*7.96331);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11ddaee0() {
   return (neuron0x11dda320()*-6.47921);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11ddb140() {
   return (neuron0x11dda720()*20.2899);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000::synapse0x11ddb180() {
   return (neuron0x11ddab20()*-15.3469);
}

