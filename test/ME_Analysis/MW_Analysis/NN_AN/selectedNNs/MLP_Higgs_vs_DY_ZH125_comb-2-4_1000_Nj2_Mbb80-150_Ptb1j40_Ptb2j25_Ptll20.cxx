#include "MLP_Higgs_vs_DY_ZH125_comb-2-4_1000_Nj2_Mbb80-150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.6657)/0.978734;
   input1 = (in1 - 20.3358)/0.823507;
   input2 = (in2 - 24.2001)/1.26245;
   input3 = (in3 - 12.5004)/0.729006;
   switch(index) {
     case 0:
         return neuron0x2555a6e0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 19.6657)/0.978734;
   input1 = (input[1] - 20.3358)/0.823507;
   input2 = (input[2] - 24.2001)/1.26245;
   input3 = (input[3] - 12.5004)/0.729006;
   switch(index) {
     case 0:
         return neuron0x2555a6e0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x25558170() {
   return input0;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x255584b0() {
   return input1;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x255587f0() {
   return input2;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x25558b30() {
   return input3;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x25558fa0() {
   double input = -1.40779;
   input += synapse0x18970ad0();
   input += synapse0x255592e0();
   input += synapse0x25559320();
   input += synapse0x25559360();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x25558fa0() {
   double input = input0x25558fa0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x255593a0() {
   double input = -5.59548;
   input += synapse0x255596e0();
   input += synapse0x25559720();
   input += synapse0x25559760();
   input += synapse0x255597a0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x255593a0() {
   double input = input0x255593a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x255597e0() {
   double input = 0.250241;
   input += synapse0x25559b20();
   input += synapse0x25559b60();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x255597e0() {
   double input = input0x255597e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x25559ba0() {
   double input = -0.324374;
   input += synapse0x25559ee0();
   input += synapse0x25559f20();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x25559ba0() {
   double input = input0x25559ba0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x25559f60() {
   double input = -0.0813556;
   input += synapse0x2555a2a0();
   input += synapse0x2555a2e0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x25559f60() {
   double input = input0x25559f60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2555a320() {
   double input = 0.178193;
   input += synapse0x2555a660();
   input += synapse0x2555a6a0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2555a320() {
   double input = input0x2555a320();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::input0x2555a6e0() {
   double input = -5.51206;
   input += synapse0x2555aa20();
   input += synapse0x18970b10();
   input += synapse0x25548520();
   input += synapse0x18970710();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2555a6e0() {
   double input = input0x2555a6e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x18970ad0() {
   return (neuron0x25558170()*1.43023);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x255592e0() {
   return (neuron0x255584b0()*-0.0653412);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x25559320() {
   return (neuron0x255587f0()*0.301925);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x25559360() {
   return (neuron0x25558b30()*-1.47065);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x255596e0() {
   return (neuron0x25558170()*-3.02778);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x25559720() {
   return (neuron0x255584b0()*1.24588);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x25559760() {
   return (neuron0x255587f0()*0.50992);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x255597a0() {
   return (neuron0x25558b30()*1.0818);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x25559b20() {
   return (neuron0x25558fa0()*-1.17793);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x25559b60() {
   return (neuron0x255593a0()*1.59896);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x25559ee0() {
   return (neuron0x25558fa0()*1.86754);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x25559f20() {
   return (neuron0x255593a0()*-2.50637);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2555a2a0() {
   return (neuron0x25558fa0()*1.53611);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2555a2e0() {
   return (neuron0x255593a0()*-2.61328);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2555a660() {
   return (neuron0x25558fa0()*1.61364);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2555a6a0() {
   return (neuron0x255593a0()*-3.10554);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2555aa20() {
   return (neuron0x255597e0()*-2.77924);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x18970b10() {
   return (neuron0x25559ba0()*3.56299);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x25548520() {
   return (neuron0x25559f60()*3.10756);
}

double MLP_Higgs_vs_DY_ZH125_comb_2_4_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x18970710() {
   return (neuron0x2555a320()*5.7461);
}

