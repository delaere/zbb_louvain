#include "../NN/MLP_TT_vs_DY_MM_N_CSV_2011.h"
#include <cmath>

double MLP_TT_vs_DY_MM_N_CSV_2011::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 20.0953)/1.10154;
   input1 = (in1 - 20.8124)/1.0736;
   input2 = (in2 - 22.1159)/0.981618;
   switch(index) {
     case 0:
         return neuron0x16eee620();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_MM_N_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 20.0953)/1.10154;
   input1 = (input[1] - 20.8124)/1.0736;
   input2 = (input[2] - 22.1159)/0.981618;
   switch(index) {
     case 0:
         return neuron0x16eee620();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x16edba00() {
   return input0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x16edbd10() {
   return input1;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x16eecb70() {
   return input2;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x16eecfc0() {
   double input = 0.674313;
   input += synapse0x16ea9cc0();
   input += synapse0x16ec3c30();
   input += synapse0x16ea9d50();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x16eecfc0() {
   double input = input0x16eecfc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x16eed240() {
   double input = -1.1999;
   input += synapse0x16edbf90();
   input += synapse0x16eed550();
   input += synapse0x16eed590();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x16eed240() {
   double input = input0x16eed240();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x16eed5d0() {
   double input = -3.45415;
   input += synapse0x16eed8e0();
   input += synapse0x16eed920();
   input += synapse0x16eed960();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x16eed5d0() {
   double input = input0x16eed5d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x16eed9a0() {
   double input = 0.251945;
   input += synapse0x16eedcb0();
   input += synapse0x16eedcf0();
   input += synapse0x16eedd30();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x16eed9a0() {
   double input = input0x16eed9a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x16eedd70() {
   double input = 3.10026;
   input += synapse0x16eee080();
   input += synapse0x16eee0c0();
   input += synapse0x16eee100();
   input += synapse0x16eee140();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x16eedd70() {
   double input = input0x16eedd70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x16eee180() {
   double input = 2.86304;
   input += synapse0x16eee490();
   input += synapse0x16c3a8b0();
   input += synapse0x16c3a8f0();
   input += synapse0x16eee5e0();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x16eee180() {
   double input = input0x16eee180();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::input0x16eee620() {
   double input = 0.997566;
   input += synapse0x16eecf40();
   input += synapse0x16eecf80();
   return input;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::neuron0x16eee620() {
   double input = input0x16eee620();
   return (input * 1)+0;
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16ea9cc0() {
   return (neuron0x16edba00()*0.209339);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16ec3c30() {
   return (neuron0x16edbd10()*0.984247);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16ea9d50() {
   return (neuron0x16eecb70()*-1.21754);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16edbf90() {
   return (neuron0x16edba00()*-1.57765);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eed550() {
   return (neuron0x16edbd10()*-0.767861);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eed590() {
   return (neuron0x16eecb70()*-1.58605);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eed8e0() {
   return (neuron0x16edba00()*-1.45507);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eed920() {
   return (neuron0x16edbd10()*1.94037);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eed960() {
   return (neuron0x16eecb70()*0.242029);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eedcb0() {
   return (neuron0x16edba00()*1.56354);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eedcf0() {
   return (neuron0x16edbd10()*-2.15937);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eedd30() {
   return (neuron0x16eecb70()*-0.051876);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eee080() {
   return (neuron0x16eecfc0()*-5.02362);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eee0c0() {
   return (neuron0x16eed240()*1.37173);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eee100() {
   return (neuron0x16eed5d0()*-2.97813);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eee140() {
   return (neuron0x16eed9a0()*-2.04675);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eee490() {
   return (neuron0x16eecfc0()*2.66184);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16c3a8b0() {
   return (neuron0x16eed240()*3.57737);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16c3a8f0() {
   return (neuron0x16eed5d0()*1.64096);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eee5e0() {
   return (neuron0x16eed9a0()*-1.56153);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eecf40() {
   return (neuron0x16eedd70()*1.13709);
}

double MLP_TT_vs_DY_MM_N_CSV_2011::synapse0x16eecf80() {
   return (neuron0x16eee180()*-1.063);
}

