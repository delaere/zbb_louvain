#include "MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.2524)/1.30119;
   input1 = (in1 - 11.1194)/1.08162;
   input2 = (in2 - 24.6091)/1.18162;
   input3 = (in3 - 13.1842)/1.27582;
   switch(index) {
     case 0:
         return neuron0xdba7750();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::Value(int index, double* input) {
   input0 = (input[0] - 21.2524)/1.30119;
   input1 = (input[1] - 11.1194)/1.08162;
   input2 = (input[2] - 24.6091)/1.18162;
   input3 = (input[3] - 13.1842)/1.27582;
   switch(index) {
     case 0:
         return neuron0xdba7750();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba4510() {
   return input0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba4850() {
   return input1;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba4b90() {
   return input2;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba4ed0() {
   return input3;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::input0xdba5340() {
   double input = -4.88331;
   input += synapse0xdb7d740();
   input += synapse0xdba55f0();
   input += synapse0xdba5630();
   input += synapse0xdba5670();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba5340() {
   double input = input0xdba5340();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::input0xdba56b0() {
   double input = 1.34997;
   input += synapse0xdba59f0();
   input += synapse0xdba5a30();
   input += synapse0xdba5a70();
   input += synapse0xdba5ab0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba56b0() {
   double input = input0xdba56b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::input0xdba5af0() {
   double input = -0.628441;
   input += synapse0xdba5e30();
   input += synapse0xdba5e70();
   input += synapse0xdba5eb0();
   input += synapse0xdba5ef0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba5af0() {
   double input = input0xdba5af0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::input0xdba5f30() {
   double input = 1.19096;
   input += synapse0xdba6270();
   input += synapse0xdba62b0();
   input += synapse0xdba62f0();
   input += synapse0xdba6330();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba5f30() {
   double input = input0xdba5f30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::input0xdba6370() {
   double input = 3.8488;
   input += synapse0xdba66b0();
   input += synapse0xd922620();
   input += synapse0xd922660();
   input += synapse0xdba6800();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba6370() {
   double input = input0xdba6370();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::input0xdba6840() {
   double input = 0.744;
   input += synapse0xdba6b80();
   input += synapse0xdba6bc0();
   input += synapse0xdba6c00();
   input += synapse0xdba6c40();
   input += synapse0xdba6c80();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba6840() {
   double input = input0xdba6840();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::input0xdba6cc0() {
   double input = -1.52511;
   input += synapse0xdba7000();
   input += synapse0xdba7040();
   input += synapse0xdba7080();
   input += synapse0xdba70c0();
   input += synapse0xdba7100();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba6cc0() {
   double input = input0xdba6cc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::input0xdba7140() {
   double input = 0.107665;
   input += synapse0xdba7480();
   input += synapse0xdba74c0();
   input += synapse0xdba7500();
   input += synapse0xdb45820();
   input += synapse0xdb7d780();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba7140() {
   double input = input0xdba7140();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::input0xdba7750() {
   double input = -0.609423;
   input += synapse0xdba7a90();
   input += synapse0xdba7ad0();
   input += synapse0xdba7b10();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::neuron0xdba7750() {
   double input = input0xdba7750();
   return (input * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdb7d740() {
   return (neuron0xdba4510()*0.722212);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba55f0() {
   return (neuron0xdba4850()*-3.45094);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba5630() {
   return (neuron0xdba4b90()*2.64671);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba5670() {
   return (neuron0xdba4ed0()*-0.232425);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba59f0() {
   return (neuron0xdba4510()*-1.15905);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba5a30() {
   return (neuron0xdba4850()*-3.65893);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba5a70() {
   return (neuron0xdba4b90()*4.10691);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba5ab0() {
   return (neuron0xdba4ed0()*6.06192);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba5e30() {
   return (neuron0xdba4510()*2.46347);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba5e70() {
   return (neuron0xdba4850()*2.80045);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba5eb0() {
   return (neuron0xdba4b90()*-6.80582);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba5ef0() {
   return (neuron0xdba4ed0()*-3.52457);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba6270() {
   return (neuron0xdba4510()*-0.0495804);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba62b0() {
   return (neuron0xdba4850()*-0.896821);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba62f0() {
   return (neuron0xdba4b90()*-0.419428);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba6330() {
   return (neuron0xdba4ed0()*2.23829);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba66b0() {
   return (neuron0xdba4510()*1.41);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xd922620() {
   return (neuron0xdba4850()*0.38005);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xd922660() {
   return (neuron0xdba4b90()*0.811501);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba6800() {
   return (neuron0xdba4ed0()*-2.35508);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba6b80() {
   return (neuron0xdba5340()*0.183918);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba6bc0() {
   return (neuron0xdba56b0()*-0.292655);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba6c00() {
   return (neuron0xdba5af0()*0.819742);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba6c40() {
   return (neuron0xdba5f30()*0.841143);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba6c80() {
   return (neuron0xdba6370()*-0.744069);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba7000() {
   return (neuron0xdba5340()*-2.83109);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba7040() {
   return (neuron0xdba56b0()*2.21517);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba7080() {
   return (neuron0xdba5af0()*3.13542);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba70c0() {
   return (neuron0xdba5f30()*-3.83678);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba7100() {
   return (neuron0xdba6370()*2.5107);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba7480() {
   return (neuron0xdba5340()*0.83228);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba74c0() {
   return (neuron0xdba56b0()*1.37483);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba7500() {
   return (neuron0xdba5af0()*-0.973338);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdb45820() {
   return (neuron0xdba5f30()*0.508189);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdb7d780() {
   return (neuron0xdba6370()*-1.08906);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba7a90() {
   return (neuron0xdba6840()*-0.0119375);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba7ad0() {
   return (neuron0xdba6cc0()*1.55366);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_comb::synapse0xdba7b10() {
   return (neuron0xdba7140()*0.691674);
}

