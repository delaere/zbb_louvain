#include "../NN/MLP_TT_vs_DY_ML_CSV_2011.h"
#include <cmath>

double MLP_TT_vs_DY_ML_CSV_2011::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 20.3806)/1.3345;
   input1 = (in1 - 21.1498)/1.31311;
   input2 = (in2 - 22.3183)/1.1481;
   switch(index) {
     case 0:
         return neuron0xc3be5b0();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_ML_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 20.3806)/1.3345;
   input1 = (input[1] - 21.1498)/1.31311;
   input2 = (input[2] - 22.3183)/1.1481;
   switch(index) {
     case 0:
         return neuron0xc3be5b0();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_ML_CSV_2011::neuron0xc3ab990() {
   return input0;
}

double MLP_TT_vs_DY_ML_CSV_2011::neuron0xc3abca0() {
   return input1;
}

double MLP_TT_vs_DY_ML_CSV_2011::neuron0xc3bcb00() {
   return input2;
}

double MLP_TT_vs_DY_ML_CSV_2011::input0xc3bcf50() {
   double input = -2.03679;
   input += synapse0xc379c50();
   input += synapse0xc393bc0();
   input += synapse0xc379ce0();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011::neuron0xc3bcf50() {
   double input = input0xc3bcf50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011::input0xc3bd1d0() {
   double input = 1.16911;
   input += synapse0xc3abf20();
   input += synapse0xc3bd4e0();
   input += synapse0xc3bd520();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011::neuron0xc3bd1d0() {
   double input = input0xc3bd1d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011::input0xc3bd560() {
   double input = -0.704457;
   input += synapse0xc3bd870();
   input += synapse0xc3bd8b0();
   input += synapse0xc3bd8f0();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011::neuron0xc3bd560() {
   double input = input0xc3bd560();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011::input0xc3bd930() {
   double input = -0.981285;
   input += synapse0xc3bdc40();
   input += synapse0xc3bdc80();
   input += synapse0xc3bdcc0();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011::neuron0xc3bd930() {
   double input = input0xc3bd930();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011::input0xc3bdd00() {
   double input = -0.0385311;
   input += synapse0xc3be010();
   input += synapse0xc3be050();
   input += synapse0xc3be090();
   input += synapse0xc3be0d0();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011::neuron0xc3bdd00() {
   double input = input0xc3bdd00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011::input0xc3be110() {
   double input = -0.527185;
   input += synapse0xc3be420();
   input += synapse0xc1162b0();
   input += synapse0xc1162f0();
   input += synapse0xc3be570();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011::neuron0xc3be110() {
   double input = input0xc3be110();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011::input0xc3be5b0() {
   double input = 0.283142;
   input += synapse0xc3bced0();
   input += synapse0xc3bcf10();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011::neuron0xc3be5b0() {
   double input = input0xc3be5b0();
   return (input * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc379c50() {
   return (neuron0xc3ab990()*0.026004);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc393bc0() {
   return (neuron0xc3abca0()*2.87429);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc379ce0() {
   return (neuron0xc3bcb00()*-1.241);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3abf20() {
   return (neuron0xc3ab990()*1.50472);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3bd4e0() {
   return (neuron0xc3abca0()*0.613862);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3bd520() {
   return (neuron0xc3bcb00()*-1.32782);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3bd870() {
   return (neuron0xc3ab990()*-1.17847);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3bd8b0() {
   return (neuron0xc3abca0()*-0.766573);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3bd8f0() {
   return (neuron0xc3bcb00()*1.41697);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3bdc40() {
   return (neuron0xc3ab990()*2.39645);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3bdc80() {
   return (neuron0xc3abca0()*-0.0143946);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3bdcc0() {
   return (neuron0xc3bcb00()*-2.08862);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3be010() {
   return (neuron0xc3bcf50()*-0.209841);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3be050() {
   return (neuron0xc3bd1d0()*-0.778555);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3be090() {
   return (neuron0xc3bd560()*-0.00383627);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3be0d0() {
   return (neuron0xc3bd930()*0.413647);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3be420() {
   return (neuron0xc3bcf50()*-1.91289);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc1162b0() {
   return (neuron0xc3bd1d0()*-1.14613);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc1162f0() {
   return (neuron0xc3bd560()*1.05499);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3be570() {
   return (neuron0xc3bd930()*-1.54545);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3bced0() {
   return (neuron0xc3bdd00()*-0.813508);
}

double MLP_TT_vs_DY_ML_CSV_2011::synapse0xc3bcf10() {
   return (neuron0xc3be110()*1.77929);
}

