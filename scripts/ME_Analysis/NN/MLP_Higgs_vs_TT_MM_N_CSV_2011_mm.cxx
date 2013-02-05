#include "../NN/MLP_Higgs_vs_TT_MM_N_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.0127)/1.28167;
   input1 = (in1 - 25.3374)/1.62247;
   input2 = (in2 - 14.2033)/2.05586;
   switch(index) {
     case 0:
         return neuron0x1a6098d0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 22.0127)/1.28167;
   input1 = (input[1] - 25.3374)/1.62247;
   input2 = (input[2] - 14.2033)/2.05586;
   switch(index) {
     case 0:
         return neuron0x1a6098d0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a5f56f0() {
   return input0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a5f5a00() {
   return input1;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a606870() {
   return input2;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a606cc0() {
   double input = 0.181927;
   input += synapse0x19398b90();
   input += synapse0x1a5df7f0();
   input += synapse0x1a5f5530();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a606cc0() {
   double input = input0x1a606cc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a606f40() {
   double input = -1.32978;
   input += synapse0x19398c20();
   input += synapse0x1a5f5bf0();
   input += synapse0x1a607250();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a606f40() {
   double input = input0x1a606f40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a607290() {
   double input = 2.32207;
   input += synapse0x1a6075a0();
   input += synapse0x1a6075e0();
   input += synapse0x1a607620();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a607290() {
   double input = input0x1a607290();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a607660() {
   double input = 1.35685;
   input += synapse0x1a607970();
   input += synapse0x1a6079b0();
   input += synapse0x1a6079f0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a607660() {
   double input = input0x1a607660();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a607a30() {
   double input = -2.05401;
   input += synapse0x1a607d40();
   input += synapse0x1a607d80();
   input += synapse0x1a607dc0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a607a30() {
   double input = input0x1a607a30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a607e00() {
   double input = -0.568809;
   input += synapse0x1a608110();
   input += synapse0x1a608150();
   input += synapse0x1941c9e0();
   input += synapse0x1941ca20();
   input += synapse0x1a6082a0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a607e00() {
   double input = input0x1a607e00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a6082e0() {
   double input = 0.990474;
   input += synapse0x1a6085f0();
   input += synapse0x1a608630();
   input += synapse0x1a608670();
   input += synapse0x1a6086b0();
   input += synapse0x1a6086f0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a6082e0() {
   double input = input0x1a6082e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a608730() {
   double input = -0.731949;
   input += synapse0x1a608a70();
   input += synapse0x1a608ab0();
   input += synapse0x1a608af0();
   input += synapse0x1a608b30();
   input += synapse0x1a608b70();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a608730() {
   double input = input0x1a608730();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a608bb0() {
   double input = -0.258583;
   input += synapse0x1a608ef0();
   input += synapse0x1a608f30();
   input += synapse0x1a608f70();
   input += synapse0x193987c0();
   input += synapse0x1a5f5490();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a608bb0() {
   double input = input0x1a608bb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a6091c0() {
   double input = 1.623;
   input += synapse0x1a608220();
   input += synapse0x1a608260();
   input += synapse0x1a609440();
   input += synapse0x1a609480();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a6091c0() {
   double input = input0x1a6091c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a6094c0() {
   double input = 0.134376;
   input += synapse0x1a6097d0();
   input += synapse0x1a609810();
   input += synapse0x1a609850();
   input += synapse0x1a609890();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a6094c0() {
   double input = input0x1a6094c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::input0x1a6098d0() {
   double input = -2.44911;
   input += synapse0x1a606c40();
   input += synapse0x1a606c80();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::neuron0x1a6098d0() {
   double input = input0x1a6098d0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x19398b90() {
   return (neuron0x1a5f56f0()*-1.87388);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a5df7f0() {
   return (neuron0x1a5f5a00()*2.5433);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a5f5530() {
   return (neuron0x1a606870()*-0.623514);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x19398c20() {
   return (neuron0x1a5f56f0()*1.23651);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a5f5bf0() {
   return (neuron0x1a5f5a00()*-2.57473);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a607250() {
   return (neuron0x1a606870()*-1.58734);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a6075a0() {
   return (neuron0x1a5f56f0()*-1.54943);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a6075e0() {
   return (neuron0x1a5f5a00()*0.844714);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a607620() {
   return (neuron0x1a606870()*3.13682);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a607970() {
   return (neuron0x1a5f56f0()*1.38435);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a6079b0() {
   return (neuron0x1a5f5a00()*-5.90547);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a6079f0() {
   return (neuron0x1a606870()*0.786726);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a607d40() {
   return (neuron0x1a5f56f0()*-2.35281);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a607d80() {
   return (neuron0x1a5f5a00()*2.2144);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a607dc0() {
   return (neuron0x1a606870()*0.236809);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608110() {
   return (neuron0x1a606cc0()*-0.355525);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608150() {
   return (neuron0x1a606f40()*1.78775);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1941c9e0() {
   return (neuron0x1a607290()*0.033102);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1941ca20() {
   return (neuron0x1a607660()*-1.32246);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a6082a0() {
   return (neuron0x1a607a30()*0.321803);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a6085f0() {
   return (neuron0x1a606cc0()*4.38827);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608630() {
   return (neuron0x1a606f40()*-2.82764);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608670() {
   return (neuron0x1a607290()*-4.20647);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a6086b0() {
   return (neuron0x1a607660()*1.59248);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a6086f0() {
   return (neuron0x1a607a30()*-2.77104);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608a70() {
   return (neuron0x1a606cc0()*-1.14974);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608ab0() {
   return (neuron0x1a606f40()*-0.258518);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608af0() {
   return (neuron0x1a607290()*-2.88757);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608b30() {
   return (neuron0x1a607660()*5.67864);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608b70() {
   return (neuron0x1a607a30()*-2.16822);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608ef0() {
   return (neuron0x1a606cc0()*3.79783);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608f30() {
   return (neuron0x1a606f40()*0.63812);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608f70() {
   return (neuron0x1a607290()*-0.699389);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x193987c0() {
   return (neuron0x1a607660()*-0.598294);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a5f5490() {
   return (neuron0x1a607a30()*1.97745);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608220() {
   return (neuron0x1a607e00()*-0.926112);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a608260() {
   return (neuron0x1a6082e0()*-0.664365);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a609440() {
   return (neuron0x1a608730()*-4.52958);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a609480() {
   return (neuron0x1a608bb0()*0.0553374);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a6097d0() {
   return (neuron0x1a607e00()*0.282912);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a609810() {
   return (neuron0x1a6082e0()*4.50365);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a609850() {
   return (neuron0x1a608730()*2.72925);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a609890() {
   return (neuron0x1a608bb0()*-4.48034);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a606c40() {
   return (neuron0x1a6091c0()*3.02325);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_mm::synapse0x1a606c80() {
   return (neuron0x1a6094c0()*3.53354);
}

