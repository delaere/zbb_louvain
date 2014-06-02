#include "../NN/MLP_TT_vs_DY_MM_CSV_2011_mm.h"
#include <cmath>

double MLP_TT_vs_DY_MM_CSV_2011_mm::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 20.7164)/1.23483;
   input1 = (in1 - 21.4222)/1.20596;
   input2 = (in2 - 21.7041)/0.826038;
   switch(index) {
     case 0:
         return neuron0xf354cb0();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 20.7164)/1.23483;
   input1 = (input[1] - 21.4222)/1.20596;
   input2 = (input[2] - 21.7041)/0.826038;
   switch(index) {
     case 0:
         return neuron0xf354cb0();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::neuron0xf342090() {
   return input0;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::neuron0xf3423a0() {
   return input1;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::neuron0xf353200() {
   return input2;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::input0xf353650() {
   double input = -1.70405;
   input += synapse0xf310350();
   input += synapse0xf32a2c0();
   input += synapse0xf3103e0();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::neuron0xf353650() {
   double input = input0xf353650();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::input0xf3538d0() {
   double input = -0.123664;
   input += synapse0xf342620();
   input += synapse0xf353be0();
   input += synapse0xf353c20();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::neuron0xf3538d0() {
   double input = input0xf3538d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::input0xf353c60() {
   double input = 2.10125;
   input += synapse0xf353f70();
   input += synapse0xf353fb0();
   input += synapse0xf353ff0();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::neuron0xf353c60() {
   double input = input0xf353c60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::input0xf354030() {
   double input = 1.60483;
   input += synapse0xf354340();
   input += synapse0xf354380();
   input += synapse0xf3543c0();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::neuron0xf354030() {
   double input = input0xf354030();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::input0xf354400() {
   double input = 1.19251;
   input += synapse0xf354710();
   input += synapse0xf354750();
   input += synapse0xf354790();
   input += synapse0xf3547d0();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::neuron0xf354400() {
   double input = input0xf354400();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::input0xf354810() {
   double input = 1.33598;
   input += synapse0xf354b20();
   input += synapse0xf0a0ea0();
   input += synapse0xf0a0ee0();
   input += synapse0xf354c70();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::neuron0xf354810() {
   double input = input0xf354810();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::input0xf354cb0() {
   double input = 0.787324;
   input += synapse0xf3535d0();
   input += synapse0xf353610();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::neuron0xf354cb0() {
   double input = input0xf354cb0();
   return (input * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf310350() {
   return (neuron0xf342090()*-2.47649);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf32a2c0() {
   return (neuron0xf3423a0()*-1.14937);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf3103e0() {
   return (neuron0xf353200()*0.271897);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf342620() {
   return (neuron0xf342090()*-5.05502);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf353be0() {
   return (neuron0xf3423a0()*1.56027);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf353c20() {
   return (neuron0xf353200()*1.92682);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf353f70() {
   return (neuron0xf342090()*-1.0796);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf353fb0() {
   return (neuron0xf3423a0()*4.28423);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf353ff0() {
   return (neuron0xf353200()*-0.822853);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf354340() {
   return (neuron0xf342090()*0.932312);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf354380() {
   return (neuron0xf3423a0()*1.60092);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf3543c0() {
   return (neuron0xf353200()*-1.55089);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf354710() {
   return (neuron0xf353650()*-0.970433);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf354750() {
   return (neuron0xf3538d0()*-1.45631);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf354790() {
   return (neuron0xf353c60()*-1.40023);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf3547d0() {
   return (neuron0xf354030()*-1.66693);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf354b20() {
   return (neuron0xf353650()*-1.44486);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf0a0ea0() {
   return (neuron0xf3538d0()*-0.68131);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf0a0ee0() {
   return (neuron0xf353c60()*-2.12272);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf354c70() {
   return (neuron0xf354030()*1.05962);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf3535d0() {
   return (neuron0xf354400()*4.1269);
}

double MLP_TT_vs_DY_MM_CSV_2011_mm::synapse0xf353610() {
   return (neuron0xf354810()*-2.32869);
}

