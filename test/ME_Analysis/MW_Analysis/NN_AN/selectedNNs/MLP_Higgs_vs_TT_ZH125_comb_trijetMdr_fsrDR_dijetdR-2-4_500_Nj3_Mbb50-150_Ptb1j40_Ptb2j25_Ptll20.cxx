#include "MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR-2-4_500_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3,double in4,double in5) {
   input0 = (in0 - 22.3628)/3.40518;
   input1 = (in1 - 24.8571)/1.64412;
   input2 = (in2 - 13.3589)/2.81791;
   input3 = (in3 - 7.75963)/31.5808;
   input4 = (in4 - 1.78919)/0.803089;
   input5 = (in5 - 1.96887)/0.681436;
   switch(index) {
     case 0:
         return neuron0x11b78c60();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 22.3628)/3.40518;
   input1 = (input[1] - 24.8571)/1.64412;
   input2 = (input[2] - 13.3589)/2.81791;
   input3 = (input[3] - 7.75963)/31.5808;
   input4 = (input[4] - 1.78919)/0.803089;
   input5 = (input[5] - 1.96887)/0.681436;
   switch(index) {
     case 0:
         return neuron0x11b78c60();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b75fc0() {
   return input0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b76270() {
   return input1;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b765b0() {
   return input2;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b768f0() {
   return input3;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b76c30() {
   return input4;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b76f70() {
   return input5;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x11b773e0() {
   double input = 2.62788;
   input += synapse0x11b77690();
   input += synapse0x11b776d0();
   input += synapse0x11b77710();
   input += synapse0x11b77750();
   input += synapse0x11b77790();
   input += synapse0x11b777d0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b773e0() {
   double input = input0x11b773e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x11b77810() {
   double input = 0.330282;
   input += synapse0x11b77b50();
   input += synapse0x11b77b90();
   input += synapse0x11b77bd0();
   input += synapse0x11b77c10();
   input += synapse0x11b77c50();
   input += synapse0x11b77c90();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b77810() {
   double input = input0x11b77810();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x11b77cd0() {
   double input = 0.518616;
   input += synapse0x11b78010();
   input += synapse0x11b78050();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b77cd0() {
   double input = input0x11b77cd0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x11b78090() {
   double input = -0.316929;
   input += synapse0x11b783d0();
   input += synapse0x11b78410();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b78090() {
   double input = input0x11b78090();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x11b78450() {
   double input = 0.928831;
   input += synapse0x11b78790();
   input += synapse0xea230d0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b78450() {
   double input = input0x11b78450();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x11b788e0() {
   double input = 0.0131023;
   input += synapse0xea23110();
   input += synapse0x11b78c20();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b788e0() {
   double input = input0x11b788e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x11b78c60() {
   double input = -5.95166;
   input += synapse0x11b78e80();
   input += synapse0x11b78ec0();
   input += synapse0x11b78f00();
   input += synapse0x11b78f40();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x11b78c60() {
   double input = input0x11b78c60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b77690() {
   return (neuron0x11b75fc0()*-3.48485);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b776d0() {
   return (neuron0x11b76270()*-2.82706);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b77710() {
   return (neuron0x11b765b0()*9.76656);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b77750() {
   return (neuron0x11b768f0()*0.308223);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b77790() {
   return (neuron0x11b76c30()*-0.475155);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b777d0() {
   return (neuron0x11b76f70()*-0.738268);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b77b50() {
   return (neuron0x11b75fc0()*1.32742);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b77b90() {
   return (neuron0x11b76270()*-0.350923);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b77bd0() {
   return (neuron0x11b765b0()*-0.0672746);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b77c10() {
   return (neuron0x11b768f0()*0.0202848);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b77c50() {
   return (neuron0x11b76c30()*-0.0216912);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b77c90() {
   return (neuron0x11b76f70()*-0.126896);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b78010() {
   return (neuron0x11b773e0()*-1.62919);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b78050() {
   return (neuron0x11b77810()*2.86456);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b783d0() {
   return (neuron0x11b773e0()*-0.845078);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b78410() {
   return (neuron0x11b77810()*3.2039);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b78790() {
   return (neuron0x11b773e0()*1.47102);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0xea230d0() {
   return (neuron0x11b77810()*-4.31152);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0xea23110() {
   return (neuron0x11b773e0()*-1.48961);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b78c20() {
   return (neuron0x11b77810()*6.10685);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b78e80() {
   return (neuron0x11b77cd0()*0.880602);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b78ec0() {
   return (neuron0x11b78090()*1.75315);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b78f00() {
   return (neuron0x11b78450()*-5.43143);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x11b78f40() {
   return (neuron0x11b788e0()*7.8027);
}

