#include "MLP_Higgs_vs_TT_MM_N_CSV_2011_comb.h"
#include <cmath>

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.2369)/1.55881;
   input1 = (in1 - 25.314)/1.61215;
   input2 = (in2 - 14.1811)/2.06162;
   switch(index) {
     case 0:
         return neuron0x212c5a70();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::Value(int index, double* input) {
   input0 = (input[0] - 22.2369)/1.55881;
   input1 = (input[1] - 25.314)/1.61215;
   input2 = (input[2] - 14.1811)/2.06162;
   switch(index) {
     case 0:
         return neuron0x212c5a70();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::neuron0x212b27d0() {
   return input0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::neuron0x212b2b10() {
   return input1;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::neuron0x212c3a50() {
   return input2;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::input0x212c3e30() {
   double input = -3.61975;
   input += synapse0x212994c0();
   input += synapse0x2127af10();
   input += synapse0x212c40e0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::neuron0x212c3e30() {
   double input = input0x212c3e30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::input0x212c4120() {
   double input = -4.82879;
   input += synapse0x212c4460();
   input += synapse0x212c44a0();
   input += synapse0x212c44e0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::neuron0x212c4120() {
   double input = input0x212c4120();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::input0x212c4520() {
   double input = -1.18975;
   input += synapse0x212c4860();
   input += synapse0x212c48a0();
   input += synapse0x212c48e0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::neuron0x212c4520() {
   double input = input0x212c4520();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::input0x212c4920() {
   double input = -3.88739;
   input += synapse0x212c4c60();
   input += synapse0x212c4ca0();
   input += synapse0x212c4ce0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::neuron0x212c4920() {
   double input = input0x212c4920();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::input0x212c4d20() {
   double input = 2.18879;
   input += synapse0x212c5060();
   input += synapse0x212c50a0();
   input += synapse0x212c50e0();
   input += synapse0x212c5120();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::neuron0x212c4d20() {
   double input = input0x212c4d20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::input0x212c5160() {
   double input = -1.15936;
   input += synapse0x212c54a0();
   input += synapse0x21052f00();
   input += synapse0x21052f40();
   input += synapse0x212c55f0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::neuron0x212c5160() {
   double input = input0x212c5160();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::input0x212c5630() {
   double input = -1.76505;
   input += synapse0x212c5970();
   input += synapse0x212c59b0();
   input += synapse0x212c59f0();
   input += synapse0x212c5a30();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::neuron0x212c5630() {
   double input = input0x212c5630();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::input0x212c5a70() {
   double input = -0.699315;
   input += synapse0x212c5c90();
   input += synapse0x212c5cd0();
   input += synapse0x212c5d10();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::neuron0x212c5a70() {
   double input = input0x212c5a70();
   return (input * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212994c0() {
   return (neuron0x212b27d0()*-2.24588);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x2127af10() {
   return (neuron0x212b2b10()*-3.77508);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c40e0() {
   return (neuron0x212c3a50()*-0.189216);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c4460() {
   return (neuron0x212b27d0()*5.3455);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c44a0() {
   return (neuron0x212b2b10()*0.364195);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c44e0() {
   return (neuron0x212c3a50()*-2.02284);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c4860() {
   return (neuron0x212b27d0()*-1.62313);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c48a0() {
   return (neuron0x212b2b10()*2.45409);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c48e0() {
   return (neuron0x212c3a50()*0.35144);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c4c60() {
   return (neuron0x212b27d0()*1.14113);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c4ca0() {
   return (neuron0x212b2b10()*-0.61469);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c4ce0() {
   return (neuron0x212c3a50()*-5.09339);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c5060() {
   return (neuron0x212c3e30()*-4.58176);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c50a0() {
   return (neuron0x212c4120()*1.3456);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c50e0() {
   return (neuron0x212c4520()*-5.01366);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c5120() {
   return (neuron0x212c4920()*4.02414);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c54a0() {
   return (neuron0x212c3e30()*-0.329664);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x21052f00() {
   return (neuron0x212c4120()*3.41842);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x21052f40() {
   return (neuron0x212c4520()*3.20179);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c55f0() {
   return (neuron0x212c4920()*2.99588);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c5970() {
   return (neuron0x212c3e30()*1.84006);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c59b0() {
   return (neuron0x212c4120()*-1.96908);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c59f0() {
   return (neuron0x212c4520()*-1.00032);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c5a30() {
   return (neuron0x212c4920()*-1.66849);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c5c90() {
   return (neuron0x212c4d20()*1.05193);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c5cd0() {
   return (neuron0x212c5160()*0.63713);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011_comb::synapse0x212c5d10() {
   return (neuron0x212c5630()*1.33332);
}

