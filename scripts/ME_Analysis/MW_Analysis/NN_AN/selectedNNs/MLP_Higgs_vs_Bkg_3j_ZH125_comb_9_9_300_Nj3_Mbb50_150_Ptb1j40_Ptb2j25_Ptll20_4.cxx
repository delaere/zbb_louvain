#include "MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.467176)/0.243159;
   input1 = (in1 - 0.52708)/0.296356;
   input2 = (in2 - 0.534793)/0.314261;
   switch(index) {
     case 0:
         return neuron0x2834d9e0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::Value(int index, double* input) {
   input0 = (input[0] - 0.467176)/0.243159;
   input1 = (input[1] - 0.52708)/0.296356;
   input2 = (input[2] - 0.534793)/0.314261;
   switch(index) {
     case 0:
         return neuron0x2834d9e0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x283476e0() {
   return input0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x28347a20() {
   return input1;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x28347d60() {
   return input2;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x283481d0() {
   double input = -0.0121004;
   input += synapse0x282ec870();
   input += synapse0x28348480();
   input += synapse0x283484c0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x283481d0() {
   double input = input0x283481d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x28348500() {
   double input = 0.84672;
   input += synapse0x28348840();
   input += synapse0x28348880();
   input += synapse0x283488c0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x28348500() {
   double input = input0x28348500();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x28348900() {
   double input = 5.40581;
   input += synapse0x28348c40();
   input += synapse0x28348c80();
   input += synapse0x28348cc0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x28348900() {
   double input = input0x28348900();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x28348d00() {
   double input = 1.82563;
   input += synapse0x28349040();
   input += synapse0x28349080();
   input += synapse0x283490c0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x28348d00() {
   double input = input0x28348d00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x28349100() {
   double input = -0.61836;
   input += synapse0x28349440();
   input += synapse0x28349480();
   input += synapse0x283494c0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x28349100() {
   double input = input0x28349100();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x28349500() {
   double input = -6.69411;
   input += synapse0x28349840();
   input += synapse0x28349880();
   input += synapse0x282ec8b0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x28349500() {
   double input = input0x28349500();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x283499d0() {
   double input = 2.14497;
   input += synapse0x28349c80();
   input += synapse0x28349cc0();
   input += synapse0x28349d00();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x283499d0() {
   double input = input0x283499d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x28349d40() {
   double input = 0.458339;
   input += synapse0x2834a080();
   input += synapse0x2834a0c0();
   input += synapse0x2834a100();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x28349d40() {
   double input = input0x28349d40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x2834a140() {
   double input = -0.54645;
   input += synapse0x2834a480();
   input += synapse0x2834a4c0();
   input += synapse0x2834a500();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x2834a140() {
   double input = input0x2834a140();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x2834a540() {
   double input = 0.0653596;
   input += synapse0x2834a880();
   input += synapse0x2834a8c0();
   input += synapse0x2834a900();
   input += synapse0x2834a940();
   input += synapse0x2834a980();
   input += synapse0x2834a9c0();
   input += synapse0x282dcec0();
   input += synapse0x282dcfa0();
   input += synapse0x282dcfe0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x2834a540() {
   double input = input0x2834a540();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x2834ac10() {
   double input = 0.285103;
   input += synapse0x2834af50();
   input += synapse0x2834af90();
   input += synapse0x2834afd0();
   input += synapse0x2834b010();
   input += synapse0x2834b050();
   input += synapse0x2834b090();
   input += synapse0x2834b0d0();
   input += synapse0x2834b110();
   input += synapse0x2834b150();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x2834ac10() {
   double input = input0x2834ac10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x2834b190() {
   double input = 0.41309;
   input += synapse0x2834b4d0();
   input += synapse0x2834b510();
   input += synapse0x2834b550();
   input += synapse0x2834b590();
   input += synapse0x2834b5d0();
   input += synapse0x2834b610();
   input += synapse0x2834b650();
   input += synapse0x2834b690();
   input += synapse0x2834b6d0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x2834b190() {
   double input = input0x2834b190();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x2834b710() {
   double input = 0.459789;
   input += synapse0x2834ba50();
   input += synapse0x2834ba90();
   input += synapse0x2834bad0();
   input += synapse0x2834bb10();
   input += synapse0x2834bb50();
   input += synapse0x2834bb90();
   input += synapse0x2834bbd0();
   input += synapse0x2834bc10();
   input += synapse0x2834bc50();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x2834b710() {
   double input = input0x2834b710();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x2834bc90() {
   double input = 0.315334;
   input += synapse0x282dc8d0();
   input += synapse0x282dc910();
   input += synapse0x282ec980();
   input += synapse0x282ec9c0();
   input += synapse0x282eca00();
   input += synapse0x2834aa00();
   input += synapse0x2834aa40();
   input += synapse0x2834aa80();
   input += synapse0x2834aac0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x2834bc90() {
   double input = input0x2834bc90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x2834c3e0() {
   double input = 0.230944;
   input += synapse0x2834c720();
   input += synapse0x2834c760();
   input += synapse0x2834c7a0();
   input += synapse0x2834c7e0();
   input += synapse0x2834c820();
   input += synapse0x2834c860();
   input += synapse0x2834c8a0();
   input += synapse0x2834c8e0();
   input += synapse0x2834c920();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x2834c3e0() {
   double input = input0x2834c3e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x2834c960() {
   double input = 0.332741;
   input += synapse0x2834cca0();
   input += synapse0x2834cce0();
   input += synapse0x2834cd20();
   input += synapse0x2834cd60();
   input += synapse0x2834cda0();
   input += synapse0x2834cde0();
   input += synapse0x2834ce20();
   input += synapse0x2834ce60();
   input += synapse0x2834cea0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x2834c960() {
   double input = input0x2834c960();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x2834cee0() {
   double input = 0.0379295;
   input += synapse0x2834d220();
   input += synapse0x2834d260();
   input += synapse0x2834d2a0();
   input += synapse0x2834d2e0();
   input += synapse0x2834d320();
   input += synapse0x2834d360();
   input += synapse0x2834d3a0();
   input += synapse0x2834d3e0();
   input += synapse0x2834d420();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x2834cee0() {
   double input = input0x2834cee0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x2834d460() {
   double input = -0.233368;
   input += synapse0x2834d7a0();
   input += synapse0x2834d7e0();
   input += synapse0x2834d820();
   input += synapse0x2834d860();
   input += synapse0x2834d8a0();
   input += synapse0x2834d8e0();
   input += synapse0x2834d920();
   input += synapse0x2834d960();
   input += synapse0x2834d9a0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x2834d460() {
   double input = input0x2834d460();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::input0x2834d9e0() {
   double input = 0.0196513;
   input += synapse0x2834ab00();
   input += synapse0x2834dd20();
   input += synapse0x2834dd60();
   input += synapse0x2834dda0();
   input += synapse0x2834dde0();
   input += synapse0x2834de20();
   input += synapse0x2834de60();
   input += synapse0x2834dea0();
   input += synapse0x2834dee0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::neuron0x2834d9e0() {
   double input = input0x2834d9e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x282ec870() {
   return (neuron0x283476e0()*-1.41749);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28348480() {
   return (neuron0x28347a20()*-0.803547);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x283484c0() {
   return (neuron0x28347d60()*-0.290594);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28348840() {
   return (neuron0x283476e0()*-0.123158);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28348880() {
   return (neuron0x28347a20()*-0.282542);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x283488c0() {
   return (neuron0x28347d60()*-1.06627);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28348c40() {
   return (neuron0x283476e0()*-1.38565);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28348c80() {
   return (neuron0x28347a20()*-1.48189);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28348cc0() {
   return (neuron0x28347d60()*-0.705154);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28349040() {
   return (neuron0x283476e0()*0.0249757);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28349080() {
   return (neuron0x28347a20()*0.136413);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x283490c0() {
   return (neuron0x28347d60()*0.996174);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28349440() {
   return (neuron0x283476e0()*1.76989);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28349480() {
   return (neuron0x28347a20()*-0.748787);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x283494c0() {
   return (neuron0x28347d60()*-1.82891);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28349840() {
   return (neuron0x283476e0()*-2.92811);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28349880() {
   return (neuron0x28347a20()*-0.862399);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x282ec8b0() {
   return (neuron0x28347d60()*0.0150819);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28349c80() {
   return (neuron0x283476e0()*0.710978);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28349cc0() {
   return (neuron0x28347a20()*0.339911);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x28349d00() {
   return (neuron0x28347d60()*-1.2952);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a080() {
   return (neuron0x283476e0()*-0.769277);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a0c0() {
   return (neuron0x28347a20()*0.646728);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a100() {
   return (neuron0x28347d60()*0.66923);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a480() {
   return (neuron0x283476e0()*0.117861);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a4c0() {
   return (neuron0x28347a20()*1.8162);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a500() {
   return (neuron0x28347d60()*-0.214971);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a880() {
   return (neuron0x283481d0()*0.763315);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a8c0() {
   return (neuron0x28348500()*-0.430257);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a900() {
   return (neuron0x28348900()*0.386164);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a940() {
   return (neuron0x28348d00()*-1.58458);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a980() {
   return (neuron0x28349100()*-0.573771);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834a9c0() {
   return (neuron0x28349500()*1.81683);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x282dcec0() {
   return (neuron0x283499d0()*-0.390124);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x282dcfa0() {
   return (neuron0x28349d40()*-0.844297);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x282dcfe0() {
   return (neuron0x2834a140()*0.83986);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834af50() {
   return (neuron0x283481d0()*0.771972);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834af90() {
   return (neuron0x28348500()*0.555804);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834afd0() {
   return (neuron0x28348900()*2.22315);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b010() {
   return (neuron0x28348d00()*-0.817834);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b050() {
   return (neuron0x28349100()*-0.173353);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b090() {
   return (neuron0x28349500()*0.645791);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b0d0() {
   return (neuron0x283499d0()*-0.063577);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b110() {
   return (neuron0x28349d40()*-0.517941);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b150() {
   return (neuron0x2834a140()*0.537281);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b4d0() {
   return (neuron0x283481d0()*-0.947103);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b510() {
   return (neuron0x28348500()*0.226327);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b550() {
   return (neuron0x28348900()*-0.087863);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b590() {
   return (neuron0x28348d00()*0.372048);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b5d0() {
   return (neuron0x28349100()*1.04705);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b610() {
   return (neuron0x28349500()*-2.2397);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b650() {
   return (neuron0x283499d0()*1.35673);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b690() {
   return (neuron0x28349d40()*0.535024);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834b6d0() {
   return (neuron0x2834a140()*-0.664003);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834ba50() {
   return (neuron0x283481d0()*-0.610669);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834ba90() {
   return (neuron0x28348500()*-0.0874786);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834bad0() {
   return (neuron0x28348900()*-0.699082);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834bb10() {
   return (neuron0x28348d00()*1.07797);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834bb50() {
   return (neuron0x28349100()*0.0731239);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834bb90() {
   return (neuron0x28349500()*-0.993717);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834bbd0() {
   return (neuron0x283499d0()*0.00848937);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834bc10() {
   return (neuron0x28349d40()*0.471066);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834bc50() {
   return (neuron0x2834a140()*-0.866111);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x282dc8d0() {
   return (neuron0x283481d0()*0.783725);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x282dc910() {
   return (neuron0x28348500()*0.63941);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x282ec980() {
   return (neuron0x28348900()*3.09591);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x282ec9c0() {
   return (neuron0x28348d00()*-0.868737);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x282eca00() {
   return (neuron0x28349100()*-1.26341);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834aa00() {
   return (neuron0x28349500()*0.375027);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834aa40() {
   return (neuron0x283499d0()*-0.145154);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834aa80() {
   return (neuron0x28349d40()*-0.899224);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834aac0() {
   return (neuron0x2834a140()*0.577264);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834c720() {
   return (neuron0x283481d0()*-0.704435);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834c760() {
   return (neuron0x28348500()*0.0993559);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834c7a0() {
   return (neuron0x28348900()*-0.245827);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834c7e0() {
   return (neuron0x28348d00()*0.787721);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834c820() {
   return (neuron0x28349100()*0.392731);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834c860() {
   return (neuron0x28349500()*-1.68999);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834c8a0() {
   return (neuron0x283499d0()*0.746027);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834c8e0() {
   return (neuron0x28349d40()*0.841724);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834c920() {
   return (neuron0x2834a140()*-0.497657);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834cca0() {
   return (neuron0x283481d0()*0.247236);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834cce0() {
   return (neuron0x28348500()*-0.0136343);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834cd20() {
   return (neuron0x28348900()*-0.221489);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834cd60() {
   return (neuron0x28348d00()*0.850157);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834cda0() {
   return (neuron0x28349100()*-0.0845061);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834cde0() {
   return (neuron0x28349500()*0.11551);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834ce20() {
   return (neuron0x283499d0()*-0.248293);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834ce60() {
   return (neuron0x28349d40()*-0.240807);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834cea0() {
   return (neuron0x2834a140()*0.195182);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d220() {
   return (neuron0x283481d0()*-0.88239);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d260() {
   return (neuron0x28348500()*0.22196);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d2a0() {
   return (neuron0x28348900()*-0.519075);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d2e0() {
   return (neuron0x28348d00()*0.193653);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d320() {
   return (neuron0x28349100()*1.35107);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d360() {
   return (neuron0x28349500()*-2.49219);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d3a0() {
   return (neuron0x283499d0()*1.83986);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d3e0() {
   return (neuron0x28349d40()*1.60586);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d420() {
   return (neuron0x2834a140()*-0.600599);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d7a0() {
   return (neuron0x283481d0()*0.693275);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d7e0() {
   return (neuron0x28348500()*-0.262024);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d820() {
   return (neuron0x28348900()*0.790701);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d860() {
   return (neuron0x28348d00()*-0.996847);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d8a0() {
   return (neuron0x28349100()*-0.122814);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d8e0() {
   return (neuron0x28349500()*0.871803);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d920() {
   return (neuron0x283499d0()*-0.351741);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d960() {
   return (neuron0x28349d40()*-0.56876);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834d9a0() {
   return (neuron0x2834a140()*0.995015);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834ab00() {
   return (neuron0x2834a540()*-3.62899);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834dd20() {
   return (neuron0x2834ac10()*-3.1429);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834dd60() {
   return (neuron0x2834b190()*2.51094);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834dda0() {
   return (neuron0x2834b710()*2.55656);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834dde0() {
   return (neuron0x2834bc90()*-3.34613);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834de20() {
   return (neuron0x2834c3e0()*1.93597);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834de60() {
   return (neuron0x2834c960()*0.432997);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834dea0() {
   return (neuron0x2834cee0()*2.77182);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4::synapse0x2834dee0() {
   return (neuron0x2834d460()*-3.26342);
}

