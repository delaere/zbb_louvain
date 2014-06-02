#include "MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.49429)/0.331839;
   input1 = (in1 - 0.512165)/0.329606;
   input2 = (in2 - 0.483693)/0.358498;
   switch(index) {
     case 0:
         return neuron0x1ebd0950();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 0.49429)/0.331839;
   input1 = (input[1] - 0.512165)/0.329606;
   input2 = (input[2] - 0.483693)/0.358498;
   switch(index) {
     case 0:
         return neuron0x1ebd0950();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x2150a770() {
   return input0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x2150aa80() {
   return input1;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebcd3a0() {
   return input2;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebcd7f0() {
   double input = -0.646689;
   input += synapse0x1fce40d0();
   input += synapse0x1fcf2040();
   input += synapse0x1ebcda70();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebcd7f0() {
   double input = input0x1ebcd7f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebcdab0() {
   double input = 7.14597;
   input += synapse0x1ebcddc0();
   input += synapse0x1ebcde00();
   input += synapse0x1ebcde40();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebcdab0() {
   double input = input0x1ebcdab0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebcde80() {
   double input = 2.97222;
   input += synapse0x1ebce190();
   input += synapse0x1ebce1d0();
   input += synapse0x1ebce210();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebcde80() {
   double input = input0x1ebcde80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebce250() {
   double input = -1.38871;
   input += synapse0x1ebce560();
   input += synapse0x1ebce5a0();
   input += synapse0x1ebce5e0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebce250() {
   double input = input0x1ebce250();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebce620() {
   double input = -0.10162;
   input += synapse0x1ebce930();
   input += synapse0x1ebce970();
   input += synapse0x1ebce9b0();
   input += synapse0x1ebce9f0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebce620() {
   double input = input0x1ebce620();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebcea30() {
   double input = -0.696;
   input += synapse0x1ebced70();
   input += synapse0x2150ad90();
   input += synapse0x1ec44580();
   input += synapse0x1ec445c0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebcea30() {
   double input = input0x1ebcea30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebceec0() {
   double input = 0.717789;
   input += synapse0x1ebcf1d0();
   input += synapse0x1ebcf210();
   input += synapse0x1ebcf250();
   input += synapse0x1ebcf290();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebceec0() {
   double input = input0x1ebceec0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebcf2d0() {
   double input = 2.94812;
   input += synapse0x1ebcf610();
   input += synapse0x1ebcf650();
   input += synapse0x1ebcf690();
   input += synapse0x1ebcf6d0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebcf2d0() {
   double input = input0x1ebcf2d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebcf710() {
   double input = 0.340415;
   input += synapse0x1ebcfa50();
   input += synapse0x1ebcfa90();
   input += synapse0x1ebcfad0();
   input += synapse0x1ebcfb10();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebcf710() {
   double input = input0x1ebcf710();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebcfb50() {
   double input = -1.93932;
   input += synapse0x1ebcfe90();
   input += synapse0x1fcf20d0();
   input += synapse0x1fcf1ca0();
   input += synapse0x1ebcedb0();
   input += synapse0x1ebcedf0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebcfb50() {
   double input = input0x1ebcfb50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebd00e0() {
   double input = 0.0673508;
   input += synapse0x1ebd0390();
   input += synapse0x1ebd03d0();
   input += synapse0x1ebd0410();
   input += synapse0x1ebd0450();
   input += synapse0x1ebd0490();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebd00e0() {
   double input = input0x1ebd00e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebd04d0() {
   double input = 0.284723;
   input += synapse0x1ebd0810();
   input += synapse0x1ebd0850();
   input += synapse0x1ebd0890();
   input += synapse0x1ebd08d0();
   input += synapse0x1ebd0910();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebd04d0() {
   double input = input0x1ebd04d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x1ebd0950() {
   double input = -1.98483;
   input += synapse0x1ebd0c90();
   input += synapse0x1ebd0cd0();
   input += synapse0x1ebd0d10();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x1ebd0950() {
   double input = input0x1ebd0950();
   return (input * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1fce40d0() {
   return (neuron0x2150a770()*-1.02367);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1fcf2040() {
   return (neuron0x2150aa80()*1.76943);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcda70() {
   return (neuron0x1ebcd3a0()*-2.12306);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcddc0() {
   return (neuron0x2150a770()*-1.14691);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcde00() {
   return (neuron0x2150aa80()*0.0423124);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcde40() {
   return (neuron0x1ebcd3a0()*6.53671);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebce190() {
   return (neuron0x2150a770()*2.6103);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebce1d0() {
   return (neuron0x2150aa80()*-4.23236);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebce210() {
   return (neuron0x1ebcd3a0()*5.21312);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebce560() {
   return (neuron0x2150a770()*-0.516428);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebce5a0() {
   return (neuron0x2150aa80()*-0.0550416);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebce5e0() {
   return (neuron0x1ebcd3a0()*0.0708549);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebce930() {
   return (neuron0x1ebcd7f0()*-0.33981);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebce970() {
   return (neuron0x1ebcdab0()*1.16973);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebce9b0() {
   return (neuron0x1ebcde80()*0.661892);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebce9f0() {
   return (neuron0x1ebce250()*1.82136);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebced70() {
   return (neuron0x1ebcd7f0()*0.562777);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x2150ad90() {
   return (neuron0x1ebcdab0()*0.227733);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ec44580() {
   return (neuron0x1ebcde80()*1.27777);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ec445c0() {
   return (neuron0x1ebce250()*1.95694);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcf1d0() {
   return (neuron0x1ebcd7f0()*-2.13497);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcf210() {
   return (neuron0x1ebcdab0()*4.65966);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcf250() {
   return (neuron0x1ebcde80()*0.409801);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcf290() {
   return (neuron0x1ebce250()*-0.546003);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcf610() {
   return (neuron0x1ebcd7f0()*1.23466);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcf650() {
   return (neuron0x1ebcdab0()*1.35011);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcf690() {
   return (neuron0x1ebcde80()*-4.59841);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcf6d0() {
   return (neuron0x1ebce250()*-2.2518);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcfa50() {
   return (neuron0x1ebcd7f0()*-2.9598);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcfa90() {
   return (neuron0x1ebcdab0()*-0.304482);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcfad0() {
   return (neuron0x1ebcde80()*2.95296);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcfb10() {
   return (neuron0x1ebce250()*-1.32517);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcfe90() {
   return (neuron0x1ebce620()*-2.77815);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1fcf20d0() {
   return (neuron0x1ebcea30()*-2.93202);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1fcf1ca0() {
   return (neuron0x1ebceec0()*2.62799);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcedb0() {
   return (neuron0x1ebcf2d0()*1.44503);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebcedf0() {
   return (neuron0x1ebcf710()*3.19689);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd0390() {
   return (neuron0x1ebce620()*-0.653659);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd03d0() {
   return (neuron0x1ebcea30()*-1.72296);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd0410() {
   return (neuron0x1ebceec0()*-0.155959);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd0450() {
   return (neuron0x1ebcf2d0()*1.71966);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd0490() {
   return (neuron0x1ebcf710()*0.0169726);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd0810() {
   return (neuron0x1ebce620()*-0.758165);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd0850() {
   return (neuron0x1ebcea30()*-0.563493);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd0890() {
   return (neuron0x1ebceec0()*0.326974);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd08d0() {
   return (neuron0x1ebcf2d0()*0.747502);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd0910() {
   return (neuron0x1ebcf710()*0.606088);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd0c90() {
   return (neuron0x1ebcfb50()*5.15118);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd0cd0() {
   return (neuron0x1ebd00e0()*2.15863);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x1ebd0d10() {
   return (neuron0x1ebd04d0()*0.627856);
}

