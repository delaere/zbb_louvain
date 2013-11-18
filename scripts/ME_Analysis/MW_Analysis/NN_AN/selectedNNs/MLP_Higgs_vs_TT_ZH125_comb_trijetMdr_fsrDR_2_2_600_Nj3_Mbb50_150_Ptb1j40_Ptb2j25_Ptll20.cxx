#include "MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3,double in4) {
   input0 = (in0 - 22.3555)/3.33759;
   input1 = (in1 - 24.8885)/1.622;
   input2 = (in2 - 13.4369)/2.90769;
   input3 = (in3 - 8.31698)/32.0035;
   input4 = (in4 - 1.78431)/0.808376;
   switch(index) {
     case 0:
         return neuron0x2205e270();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 22.3555)/3.33759;
   input1 = (input[1] - 24.8885)/1.622;
   input2 = (input[2] - 13.4369)/2.90769;
   input3 = (input[3] - 8.31698)/32.0035;
   input4 = (input[4] - 1.78431)/0.808376;
   switch(index) {
     case 0:
         return neuron0x2205e270();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2205c190() {
   return input0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2205c4d0() {
   return input1;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2205c810() {
   return input2;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2205cb50() {
   return input3;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2205ce90() {
   return input4;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2205d300() {
   double input = 3.64902;
   input += synapse0x21fd2430();
   input += synapse0x22064eb0();
   input += synapse0x2205d5b0();
   input += synapse0x2205d5f0();
   input += synapse0x2205d630();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2205d300() {
   double input = input0x2205d300();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2205d670() {
   double input = 1.50372;
   input += synapse0x2205d9b0();
   input += synapse0x2205d9f0();
   input += synapse0x2205da30();
   input += synapse0x2205da70();
   input += synapse0x2205dab0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2205d670() {
   double input = input0x2205d670();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2205daf0() {
   double input = 1.34087;
   input += synapse0x2205de30();
   input += synapse0x2205de70();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2205daf0() {
   double input = input0x2205daf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2205deb0() {
   double input = -0.615766;
   input += synapse0x2205e1f0();
   input += synapse0x2205e230();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2205deb0() {
   double input = input0x2205deb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x2205e270() {
   double input = 3.98207;
   input += synapse0x2205e5b0();
   input += synapse0x2205e5f0();
   return input;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x2205e270() {
   double input = input0x2205e270();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x21fd2430() {
   return (neuron0x2205c190()*-2.90113);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x22064eb0() {
   return (neuron0x2205c4d0()*-1.68057);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205d5b0() {
   return (neuron0x2205c810()*7.88095);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205d5f0() {
   return (neuron0x2205cb50()*0.186782);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205d630() {
   return (neuron0x2205ce90()*-0.317133);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205d9b0() {
   return (neuron0x2205c190()*1.0251);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205d9f0() {
   return (neuron0x2205c4d0()*-0.261704);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205da30() {
   return (neuron0x2205c810()*-0.0407685);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205da70() {
   return (neuron0x2205cb50()*0.00374991);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205dab0() {
   return (neuron0x2205ce90()*-0.00582011);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205de30() {
   return (neuron0x2205d300()*3.54168);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205de70() {
   return (neuron0x2205d670()*-6.9041);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205e1f0() {
   return (neuron0x2205d300()*-0.513862);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205e230() {
   return (neuron0x2205d670()*-0.475211);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205e5b0() {
   return (neuron0x2205daf0()*-12.5103);
}

double MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x2205e5f0() {
   return (neuron0x2205deb0()*-0.3838);
}

