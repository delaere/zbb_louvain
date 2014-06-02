#include "MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 0.46033)/0.237691;
   input1 = (in1 - 0.512403)/0.275496;
   input2 = (in2 - 0.527936)/0.286352;
   input3 = (in3 - 0.639559)/0.256908;
   switch(index) {
     case 0:
         return neuron0x3c605c80();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 0.46033)/0.237691;
   input1 = (input[1] - 0.512403)/0.275496;
   input2 = (input[2] - 0.527936)/0.286352;
   input3 = (input[3] - 0.639559)/0.256908;
   switch(index) {
     case 0:
         return neuron0x3c605c80();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3c603a10() {
   return input0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3c603d50() {
   return input1;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3c604090() {
   return input2;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3c6043d0() {
   return input3;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x3c604840() {
   double input = 3.06454;
   input += synapse0x3c5f2c70();
   input += synapse0x3c580cd0();
   input += synapse0x3c580d10();
   input += synapse0x3c604af0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3c604840() {
   double input = input0x3c604840();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x3c604b30() {
   double input = -3.06524;
   input += synapse0x3c604e70();
   input += synapse0x3c604eb0();
   input += synapse0x3c604ef0();
   input += synapse0x3c604f30();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3c604b30() {
   double input = input0x3c604b30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x3c604f70() {
   double input = 1.26953;
   input += synapse0x3c6052b0();
   input += synapse0x3c6052f0();
   input += synapse0x3c605330();
   input += synapse0x3c605370();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3c604f70() {
   double input = input0x3c604f70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x3c6053b0() {
   double input = -3.61494;
   input += synapse0x3c6056f0();
   input += synapse0x3c605730();
   input += synapse0x3c605770();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3c6053b0() {
   double input = input0x3c6053b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x3c6057b0() {
   double input = 4.00689;
   input += synapse0x3c605af0();
   input += synapse0x3c605b30();
   input += synapse0x3c580830();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3c6057b0() {
   double input = input0x3c6057b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x3c605c80() {
   double input = 0.0596264;
   input += synapse0x3c605ea0();
   input += synapse0x3c605ee0();
   return input;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x3c605c80() {
   double input = input0x3c605c80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c5f2c70() {
   return (neuron0x3c603a10()*0.0789822);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c580cd0() {
   return (neuron0x3c603d50()*-0.00446146);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c580d10() {
   return (neuron0x3c604090()*1.43575);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c604af0() {
   return (neuron0x3c6043d0()*-0.733502);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c604e70() {
   return (neuron0x3c603a10()*1.06431);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c604eb0() {
   return (neuron0x3c603d50()*-0.31494);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c604ef0() {
   return (neuron0x3c604090()*0.482415);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c604f30() {
   return (neuron0x3c6043d0()*0.195342);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c6052b0() {
   return (neuron0x3c603a10()*1.05861);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c6052f0() {
   return (neuron0x3c603d50()*0.0476278);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c605330() {
   return (neuron0x3c604090()*-0.468373);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c605370() {
   return (neuron0x3c6043d0()*0.534139);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c6056f0() {
   return (neuron0x3c604840()*-0.443136);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c605730() {
   return (neuron0x3c604b30()*5.25324);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c605770() {
   return (neuron0x3c604f70()*2.14199);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c605af0() {
   return (neuron0x3c604840()*-3.99508);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c605b30() {
   return (neuron0x3c604b30()*-1.75747);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c580830() {
   return (neuron0x3c604f70()*-3.69247);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c605ea0() {
   return (neuron0x3c6053b0()*6.58762);
}

double MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x3c605ee0() {
   return (neuron0x3c6057b0()*-9.26856);
}

