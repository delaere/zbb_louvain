#include "MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR-2-4_501_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3,double in4,double in5,double in6) {
   input0 = (in0 - 21.2603)/1.24213;
   input1 = (in1 - 10.925)/1.0292;
   input2 = (in2 - 24.8133)/1.20085;
   input3 = (in3 - 13.128)/1.2544;
   input4 = (in4 - 8.01918)/31.6482;
   input5 = (in5 - 1.81682)/0.811669;
   input6 = (in6 - 1.95854)/0.692368;
   switch(index) {
     case 0:
         return neuron0x2dfb01b0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 21.2603)/1.24213;
   input1 = (input[1] - 10.925)/1.0292;
   input2 = (input[2] - 24.8133)/1.20085;
   input3 = (input[3] - 13.128)/1.2544;
   input4 = (input[4] - 8.01918)/31.6482;
   input5 = (input[5] - 1.81682)/0.811669;
   input6 = (input[6] - 1.95854)/0.692368;
   switch(index) {
     case 0:
         return neuron0x2dfb01b0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfad150() {
   return input0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfad490() {
   return input1;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfad7d0() {
   return input2;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfadb10() {
   return input3;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfade50() {
   return input4;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfae190() {
   return input5;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfae4d0() {
   return input6;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2dfae940() {
   double input = 3.26482;
   input += synapse0x2df571f0();
   input += synapse0x2dfaebf0();
   input += synapse0x2dfaec30();
   input += synapse0x2dfaec70();
   input += synapse0x2dfaecb0();
   input += synapse0x2dfaecf0();
   input += synapse0x2dfaed30();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfae940() {
   double input = input0x2dfae940();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2dfaed70() {
   double input = 0.145062;
   input += synapse0x2dfaf0b0();
   input += synapse0x2dfaf0f0();
   input += synapse0x2dfaf130();
   input += synapse0x2dfaf170();
   input += synapse0x2dfaf1b0();
   input += synapse0x2dfaf1f0();
   input += synapse0x2dfaf230();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfaed70() {
   double input = input0x2dfaed70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2dfaf270() {
   double input = -0.281069;
   input += synapse0x2dfaf5b0();
   input += synapse0x2dfaf5f0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfaf270() {
   double input = input0x2dfaf270();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2dfaf630() {
   double input = 0.196249;
   input += synapse0x2dfaf970();
   input += synapse0x2cc4fa50();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfaf630() {
   double input = input0x2dfaf630();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2dfafac0() {
   double input = 0.239937;
   input += synapse0x2dfafd70();
   input += synapse0x2dfafdb0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfafac0() {
   double input = input0x2dfafac0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2dfafdf0() {
   double input = 0.186459;
   input += synapse0x2dfb0130();
   input += synapse0x2dfb0170();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfafdf0() {
   double input = input0x2dfafdf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2dfb01b0() {
   double input = 0.709598;
   input += synapse0x2dfb04f0();
   input += synapse0x2dfb0530();
   input += synapse0x2dfb0570();
   input += synapse0x2dfb05b0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2dfb01b0() {
   double input = input0x2dfb01b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2df571f0() {
   return (neuron0x2dfad150()*-0.624413);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaebf0() {
   return (neuron0x2dfad490()*2.19807);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaec30() {
   return (neuron0x2dfad7d0()*-1.37307);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaec70() {
   return (neuron0x2dfadb10()*-0.15223);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaecb0() {
   return (neuron0x2dfade50()*0.0467743);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaecf0() {
   return (neuron0x2dfae190()*-0.231604);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaed30() {
   return (neuron0x2dfae4d0()*0.23783);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaf0b0() {
   return (neuron0x2dfad150()*-0.243255);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaf0f0() {
   return (neuron0x2dfad490()*0.0453616);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaf130() {
   return (neuron0x2dfad7d0()*0.0189165);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaf170() {
   return (neuron0x2dfadb10()*0.319285);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaf1b0() {
   return (neuron0x2dfade50()*0.0197834);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaf1f0() {
   return (neuron0x2dfae190()*-0.0525457);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaf230() {
   return (neuron0x2dfae4d0()*0.130258);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaf5b0() {
   return (neuron0x2dfae940()*1.8961);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaf5f0() {
   return (neuron0x2dfaed70()*-2.8178);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfaf970() {
   return (neuron0x2dfae940()*1.31506);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2cc4fa50() {
   return (neuron0x2dfaed70()*-2.54901);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfafd70() {
   return (neuron0x2dfae940()*-1.60978);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfafdb0() {
   return (neuron0x2dfaed70()*2.36786);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfb0130() {
   return (neuron0x2dfae940()*-1.78024);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfb0170() {
   return (neuron0x2dfaed70()*3.38453);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfb04f0() {
   return (neuron0x2dfaf270()*4.76768);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfb0530() {
   return (neuron0x2dfaf630()*3.78289);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfb0570() {
   return (neuron0x2dfafac0()*-2.74774);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR_2_4_501_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2dfb05b0() {
   return (neuron0x2dfafdf0()*-5.20935);
}

