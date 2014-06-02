#include "../NN/MLP_TT_vs_DY_MM_N_CSV_2011_mm.h"
#include <cmath>

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 20.117)/1.13053;
   input1 = (in1 - 20.8257)/1.09136;
   input2 = (in2 - 21.7901)/0.931963;
   switch(index) {
     case 0:
         return neuron0x133d5650();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 20.117)/1.13053;
   input1 = (input[1] - 20.8257)/1.09136;
   input2 = (input[2] - 21.7901)/0.931963;
   switch(index) {
     case 0:
         return neuron0x133d5650();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::neuron0x133c2a30() {
   return input0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::neuron0x133c2d40() {
   return input1;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::neuron0x133d3ba0() {
   return input2;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::input0x133d3ff0() {
   double input = 1.61999;
   input += synapse0x13390cf0();
   input += synapse0x133aac60();
   input += synapse0x13390d80();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::neuron0x133d3ff0() {
   double input = input0x133d3ff0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::input0x133d4270() {
   double input = 0.247183;
   input += synapse0x133c2fc0();
   input += synapse0x133d4580();
   input += synapse0x133d45c0();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::neuron0x133d4270() {
   double input = input0x133d4270();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::input0x133d4600() {
   double input = -1.45657;
   input += synapse0x133d4910();
   input += synapse0x133d4950();
   input += synapse0x133d4990();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::neuron0x133d4600() {
   double input = input0x133d4600();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::input0x133d49d0() {
   double input = 1.14498;
   input += synapse0x133d4ce0();
   input += synapse0x133d4d20();
   input += synapse0x133d4d60();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::neuron0x133d49d0() {
   double input = input0x133d49d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::input0x133d4da0() {
   double input = -1.30813;
   input += synapse0x133d50b0();
   input += synapse0x133d50f0();
   input += synapse0x133d5130();
   input += synapse0x133d5170();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::neuron0x133d4da0() {
   double input = input0x133d4da0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::input0x133d51b0() {
   double input = -0.501339;
   input += synapse0x133d54c0();
   input += synapse0x13121850();
   input += synapse0x13121890();
   input += synapse0x133d5610();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::neuron0x133d51b0() {
   double input = input0x133d51b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::input0x133d5650() {
   double input = 0.42538;
   input += synapse0x133d3f70();
   input += synapse0x133d3fb0();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::neuron0x133d5650() {
   double input = input0x133d5650();
   return (input * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x13390cf0() {
   return (neuron0x133c2a30()*-5.59486);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133aac60() {
   return (neuron0x133c2d40()*-0.406715);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x13390d80() {
   return (neuron0x133d3ba0()*0.971849);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133c2fc0() {
   return (neuron0x133c2a30()*2.30704);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d4580() {
   return (neuron0x133c2d40()*-0.708645);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d45c0() {
   return (neuron0x133d3ba0()*-3.55911);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d4910() {
   return (neuron0x133c2a30()*-1.57486);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d4950() {
   return (neuron0x133c2d40()*-0.913274);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d4990() {
   return (neuron0x133d3ba0()*1.66334);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d4ce0() {
   return (neuron0x133c2a30()*-6.04622);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d4d20() {
   return (neuron0x133c2d40()*-0.240985);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d4d60() {
   return (neuron0x133d3ba0()*1.49984);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d50b0() {
   return (neuron0x133d3ff0()*3.28299);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d50f0() {
   return (neuron0x133d4270()*-1.15878);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d5130() {
   return (neuron0x133d4600()*0.385395);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d5170() {
   return (neuron0x133d49d0()*0.422854);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d54c0() {
   return (neuron0x133d3ff0()*0.052515);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x13121850() {
   return (neuron0x133d4270()*-0.593807);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x13121890() {
   return (neuron0x133d4600()*-2.61938);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d5610() {
   return (neuron0x133d49d0()*4.2275);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d3f70() {
   return (neuron0x133d4da0()*2.51886);
}

double MLP_TT_vs_DY_MM_N_CSV_2011_mm::synapse0x133d3fb0() {
   return (neuron0x133d51b0()*-2.37287);
}

