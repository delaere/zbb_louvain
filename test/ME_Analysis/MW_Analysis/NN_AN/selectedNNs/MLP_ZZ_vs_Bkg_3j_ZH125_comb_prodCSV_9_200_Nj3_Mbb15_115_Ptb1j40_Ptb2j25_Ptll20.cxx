#include "MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.477235)/0.179129;
   input1 = (in1 - 0.563571)/0.303163;
   input2 = (in2 - 0.614876)/0.258553;
   switch(index) {
     case 0:
         return neuron0x36ca7740();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 0.477235)/0.179129;
   input1 = (input[1] - 0.563571)/0.303163;
   input2 = (input[2] - 0.614876)/0.258553;
   switch(index) {
     case 0:
         return neuron0x36ca7740();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36c93d60() {
   return input0;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36c940a0() {
   return input1;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36ca5070() {
   return input2;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x36ca53c0() {
   double input = 0.602971;
   input += synapse0x36c3b7a0();
   input += synapse0x36c3b7e0();
   input += synapse0x36ca5670();
   return input;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36ca53c0() {
   double input = input0x36ca53c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x36ca56b0() {
   double input = 1.29742;
   input += synapse0x36ca59f0();
   input += synapse0x36ca5a30();
   input += synapse0x36ca5a70();
   return input;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36ca56b0() {
   double input = input0x36ca56b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x36ca5ab0() {
   double input = 0.131621;
   input += synapse0x36ca5df0();
   input += synapse0x36ca5e30();
   input += synapse0x36ca5e70();
   return input;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36ca5ab0() {
   double input = input0x36ca5ab0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x36ca5eb0() {
   double input = -0.710056;
   input += synapse0x36ca61f0();
   input += synapse0x36ca6230();
   input += synapse0x36ca6270();
   return input;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36ca5eb0() {
   double input = input0x36ca5eb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x36ca62b0() {
   double input = 2.67348;
   input += synapse0x36ca65f0();
   input += synapse0x36ca6630();
   input += synapse0x36ca6670();
   return input;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36ca62b0() {
   double input = input0x36ca62b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x36ca66b0() {
   double input = 0.926045;
   input += synapse0x36ca69f0();
   input += synapse0x36ca6a30();
   input += synapse0x36c3b380();
   return input;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36ca66b0() {
   double input = input0x36ca66b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x36ca6b80() {
   double input = -0.25386;
   input += synapse0x36c3b3c0();
   input += synapse0x36ca6ec0();
   input += synapse0x36ca6f00();
   return input;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36ca6b80() {
   double input = input0x36ca6b80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x36ca6f40() {
   double input = -4.5283;
   input += synapse0x36ca7280();
   input += synapse0x36ca72c0();
   input += synapse0x36ca7300();
   return input;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36ca6f40() {
   double input = input0x36ca6f40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x36ca7340() {
   double input = 3.40211;
   input += synapse0x36ca7680();
   input += synapse0x36ca76c0();
   input += synapse0x36ca7700();
   return input;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36ca7340() {
   double input = input0x36ca7340();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x36ca7740() {
   double input = -0.521386;
   input += synapse0x36ca5290();
   input += synapse0x36ca5360();
   input += synapse0x36ca79f0();
   input += synapse0x36ca7a30();
   input += synapse0x36ca7a70();
   input += synapse0x36ca7ab0();
   input += synapse0x36775170();
   input += synapse0x36c3b830();
   input += synapse0x36c3b870();
   return input;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x36ca7740() {
   double input = input0x36ca7740();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36c3b7a0() {
   return (neuron0x36c93d60()*-2.18335);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36c3b7e0() {
   return (neuron0x36c940a0()*0.0857444);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca5670() {
   return (neuron0x36ca5070()*-0.38929);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca59f0() {
   return (neuron0x36c93d60()*2.56531);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca5a30() {
   return (neuron0x36c940a0()*-0.141882);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca5a70() {
   return (neuron0x36ca5070()*5.84083);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca5df0() {
   return (neuron0x36c93d60()*0.388345);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca5e30() {
   return (neuron0x36c940a0()*0.0496091);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca5e70() {
   return (neuron0x36ca5070()*-0.156401);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca61f0() {
   return (neuron0x36c93d60()*-1.15639);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca6230() {
   return (neuron0x36c940a0()*0.581205);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca6270() {
   return (neuron0x36ca5070()*-0.294001);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca65f0() {
   return (neuron0x36c93d60()*-0.822051);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca6630() {
   return (neuron0x36c940a0()*-0.812958);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca6670() {
   return (neuron0x36ca5070()*-1.45747);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca69f0() {
   return (neuron0x36c93d60()*-0.284668);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca6a30() {
   return (neuron0x36c940a0()*-0.165089);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36c3b380() {
   return (neuron0x36ca5070()*0.660346);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36c3b3c0() {
   return (neuron0x36c93d60()*0.711735);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca6ec0() {
   return (neuron0x36c940a0()*-0.297217);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca6f00() {
   return (neuron0x36ca5070()*-0.102536);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca7280() {
   return (neuron0x36c93d60()*-0.443815);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca72c0() {
   return (neuron0x36c940a0()*-2.11611);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca7300() {
   return (neuron0x36ca5070()*0.606064);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca7680() {
   return (neuron0x36c93d60()*0.599568);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca76c0() {
   return (neuron0x36c940a0()*-0.645846);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca7700() {
   return (neuron0x36ca5070()*-1.63897);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca5290() {
   return (neuron0x36ca53c0()*0.909905);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca5360() {
   return (neuron0x36ca56b0()*0.958483);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca79f0() {
   return (neuron0x36ca5ab0()*1.20556);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca7a30() {
   return (neuron0x36ca5eb0()*-1.44344);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca7a70() {
   return (neuron0x36ca62b0()*-1.81856);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36ca7ab0() {
   return (neuron0x36ca66b0()*-1.52492);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36775170() {
   return (neuron0x36ca6b80()*0.369875);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36c3b830() {
   return (neuron0x36ca6f40()*-3.65439);
}

double MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x36c3b870() {
   return (neuron0x36ca7340()*2.15357);
}

