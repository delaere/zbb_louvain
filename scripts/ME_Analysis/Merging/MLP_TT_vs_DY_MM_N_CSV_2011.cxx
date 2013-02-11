#include "MLP_TT_vs_DY_MM_N_CSV_2011.h"
#include <cmath>

double MLP_TT_vs_DY_MM_N_CSV_2011::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 19.116)/1.12999;
   input1 = (in1 - 19.885)/1.08241;
   input2 = (in2 - 0.809398)/0.124437;
   switch(index) {
     case 0:
         return neuron0x1a6ed820();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_MM_N_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 19.116)/1.12999;
   input1 = (input[1] - 19.885)/1.08241;
   input2 = (input[2] - 0.809398)/0.124437;
   switch(index) {
     case 0:
         return neuron0x1a6ed820();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6da240() {
   return input0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6da550() {
   return input1;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6eb440() {
   return input2;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x1a6eb890() {
   double input = 1.62884;
   input += synapse0x1bcbd610();
   input += synapse0x1a6c3630();
   input += synapse0x1bcbd6a0();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6eb890() {
   double input = input0x1a6eb890();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x1a6ebb10() {
   double input = 1.68026;
   input += synapse0x1a6ebe20();
   input += synapse0x1a6ebe60();
   input += synapse0x1a6ebea0();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6ebb10() {
   double input = input0x1a6ebb10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x1a6ebee0() {
   double input = 1.825;
   input += synapse0x1a6ec1f0();
   input += synapse0x1a6ec230();
   input += synapse0x1a6ec270();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6ebee0() {
   double input = input0x1a6ebee0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x1a6ec2b0() {
   double input = -1.4712;
   input += synapse0x1a6ec5c0();
   input += synapse0x1a6ec600();
   input += synapse0x1a6ec640();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6ec2b0() {
   double input = input0x1a6ec2b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x1a6ec680() {
   double input = -1.54527;
   input += synapse0x1a6ec990();
   input += synapse0x1a6ec9d0();
   input += synapse0x1a6eca10();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6ec680() {
   double input = input0x1a6ec680();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x1a6eca50() {
   double input = 0.319897;
   input += synapse0x1a6ecd90();
   input += synapse0x1a6ecdd0();
   input += synapse0x1bd1cc30();
   input += synapse0x1bd1cc70();
   input += synapse0x1a6da860();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6eca50() {
   double input = input0x1a6eca50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x1a6ecf20() {
   double input = -1.1218;
   input += synapse0x1a6ed260();
   input += synapse0x1a6ed2a0();
   input += synapse0x1a6ed2e0();
   input += synapse0x1a6ed320();
   input += synapse0x1a6ed360();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6ecf20() {
   double input = input0x1a6ecf20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x1a6ed3a0() {
   double input = 0.531821;
   input += synapse0x1a6ed6e0();
   input += synapse0x1a6ed720();
   input += synapse0x1a6ed760();
   input += synapse0x1a6ed7a0();
   input += synapse0x1a6ed7e0();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6ed3a0() {
   double input = input0x1a6ed3a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x1a6ed820() {
   double input = -1.33132;
   input += synapse0x1a6edb60();
   input += synapse0x1a6edba0();
   input += synapse0x1a6edbe0();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x1a6ed820() {
   double input = input0x1a6ed820();
   return (input * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1bcbd610() {
   return (neuron0x1a6da240()*0.558474);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6c3630() {
   return (neuron0x1a6da550()*-1.48463);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1bcbd6a0() {
   return (neuron0x1a6eb440()*2.78669);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ebe20() {
   return (neuron0x1a6da240()*2.6542);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ebe60() {
   return (neuron0x1a6da550()*-1.92831);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ebea0() {
   return (neuron0x1a6eb440()*-0.696503);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ec1f0() {
   return (neuron0x1a6da240()*1.75616);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ec230() {
   return (neuron0x1a6da550()*0.566008);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ec270() {
   return (neuron0x1a6eb440()*-3.47449);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ec5c0() {
   return (neuron0x1a6da240()*-0.11324);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ec600() {
   return (neuron0x1a6da550()*0.450153);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ec640() {
   return (neuron0x1a6eb440()*3.93763);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ec990() {
   return (neuron0x1a6da240()*0.811788);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ec9d0() {
   return (neuron0x1a6da550()*-1.38302);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6eca10() {
   return (neuron0x1a6eb440()*0.232447);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ecd90() {
   return (neuron0x1a6eb890()*-0.339549);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ecdd0() {
   return (neuron0x1a6ebb10()*1.58581);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1bd1cc30() {
   return (neuron0x1a6ebee0()*-0.959045);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1bd1cc70() {
   return (neuron0x1a6ec2b0()*0.781163);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6da860() {
   return (neuron0x1a6ec680()*-2.25744);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ed260() {
   return (neuron0x1a6eb890()*-3.37642);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ed2a0() {
   return (neuron0x1a6ebb10()*1.8403);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ed2e0() {
   return (neuron0x1a6ebee0()*-0.929498);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ed320() {
   return (neuron0x1a6ec2b0()*0.809945);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ed360() {
   return (neuron0x1a6ec680()*-0.76519);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ed6e0() {
   return (neuron0x1a6eb890()*-1.61135);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ed720() {
   return (neuron0x1a6ebb10()*1.17191);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ed760() {
   return (neuron0x1a6ebee0()*0.501141);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ed7a0() {
   return (neuron0x1a6ec2b0()*0.18448);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6ed7e0() {
   return (neuron0x1a6ec680()*-0.368031);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6edb60() {
   return (neuron0x1a6eca50()*2.54647);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6edba0() {
   return (neuron0x1a6ecf20()*-2.32362);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x1a6edbe0() {
   return (neuron0x1a6ed3a0()*0.801783);
}

