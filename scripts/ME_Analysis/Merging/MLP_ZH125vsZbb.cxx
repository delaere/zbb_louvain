#include "MLP_ZH125vsZbb.h"
#include <cmath>

double MLP_ZH125vsZbb::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 29.6752)/79.3677;
   input1 = (in1 - 20.3921)/0.941904;
   input2 = (in2 - 13.6377)/1.80608;
   switch(index) {
     case 0:
         return neuron0x12c54700();
     default:
         return 0.;
   }
}

double MLP_ZH125vsZbb::Value(int index, double* input) {
   input0 = (input[0] - 29.6752)/79.3677;
   input1 = (input[1] - 20.3921)/0.941904;
   input2 = (input[2] - 13.6377)/1.80608;
   switch(index) {
     case 0:
         return neuron0x12c54700();
     default:
         return 0.;
   }
}

double MLP_ZH125vsZbb::neuron0x11c79960() {
   return input0;
}

double MLP_ZH125vsZbb::neuron0x11c79c70() {
   return input1;
}

double MLP_ZH125vsZbb::neuron0x11c79f80() {
   return input2;
}

double MLP_ZH125vsZbb::input0x11c7a400() {
   double input = -0.601754;
   input += synapse0x11efa8e0();
   input += synapse0x11efa970();
   input += synapse0x16bd01e0();
   return input;
}

double MLP_ZH125vsZbb::neuron0x11c7a400() {
   double input = input0x11c7a400();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x12c532c0() {
   double input = -0.767042;
   input += synapse0x12c535d0();
   input += synapse0x12c53610();
   input += synapse0x12c53650();
   return input;
}

double MLP_ZH125vsZbb::neuron0x12c532c0() {
   double input = input0x12c532c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x12c53690() {
   double input = -0.466068;
   input += synapse0x12c539a0();
   input += synapse0x12c539e0();
   input += synapse0x12c53a20();
   return input;
}

double MLP_ZH125vsZbb::neuron0x12c53690() {
   double input = input0x12c53690();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x12c53a60() {
   double input = 1.5829;
   input += synapse0x12c53d70();
   input += synapse0x12c53db0();
   input += synapse0x12c53df0();
   return input;
}

double MLP_ZH125vsZbb::neuron0x12c53a60() {
   double input = input0x12c53a60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x12c53e30() {
   double input = 0.00445029;
   input += synapse0x12c54170();
   input += synapse0x12c541b0();
   input += synapse0x12c541f0();
   input += synapse0x12c54230();
   return input;
}

double MLP_ZH125vsZbb::neuron0x12c53e30() {
   double input = input0x12c53e30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x12c54270() {
   double input = 0.49323;
   input += synapse0x12c545b0();
   input += synapse0x11c7a680();
   input += synapse0x11c7a6c0();
   input += synapse0x16bc06a0();
   return input;
}

double MLP_ZH125vsZbb::neuron0x12c54270() {
   double input = input0x12c54270();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x12c54700() {
   double input = -0.557084;
   input += synapse0x12c54a10();
   input += synapse0x12c54a50();
   return input;
}

double MLP_ZH125vsZbb::neuron0x12c54700() {
   double input = input0x12c54700();
   return (input * 1)+0;
}

double MLP_ZH125vsZbb::synapse0x11efa8e0() {
   return (neuron0x11c79960()*-0.635354);
}

double MLP_ZH125vsZbb::synapse0x11efa970() {
   return (neuron0x11c79c70()*0.00502211);
}

double MLP_ZH125vsZbb::synapse0x16bd01e0() {
   return (neuron0x11c79f80()*0.392144);
}

double MLP_ZH125vsZbb::synapse0x12c535d0() {
   return (neuron0x11c79960()*0.788344);
}

double MLP_ZH125vsZbb::synapse0x12c53610() {
   return (neuron0x11c79c70()*0.163098);
}

double MLP_ZH125vsZbb::synapse0x12c53650() {
   return (neuron0x11c79f80()*2.01312);
}

double MLP_ZH125vsZbb::synapse0x12c539a0() {
   return (neuron0x11c79960()*0.10848);
}

double MLP_ZH125vsZbb::synapse0x12c539e0() {
   return (neuron0x11c79c70()*-0.187738);
}

double MLP_ZH125vsZbb::synapse0x12c53a20() {
   return (neuron0x11c79f80()*0.95908);
}

double MLP_ZH125vsZbb::synapse0x12c53d70() {
   return (neuron0x11c79960()*-1.18575);
}

double MLP_ZH125vsZbb::synapse0x12c53db0() {
   return (neuron0x11c79c70()*-1.96879);
}

double MLP_ZH125vsZbb::synapse0x12c53df0() {
   return (neuron0x11c79f80()*3.78482);
}

double MLP_ZH125vsZbb::synapse0x12c54170() {
   return (neuron0x11c7a400()*-0.118604);
}

double MLP_ZH125vsZbb::synapse0x12c541b0() {
   return (neuron0x12c532c0()*0.446733);
}

double MLP_ZH125vsZbb::synapse0x12c541f0() {
   return (neuron0x12c53690()*-2.0381);
}

double MLP_ZH125vsZbb::synapse0x12c54230() {
   return (neuron0x12c53a60()*-0.82689);
}

double MLP_ZH125vsZbb::synapse0x12c545b0() {
   return (neuron0x11c7a400()*-0.354013);
}

double MLP_ZH125vsZbb::synapse0x11c7a680() {
   return (neuron0x12c532c0()*0.485732);
}

double MLP_ZH125vsZbb::synapse0x11c7a6c0() {
   return (neuron0x12c53690()*-1.96464);
}

double MLP_ZH125vsZbb::synapse0x16bc06a0() {
   return (neuron0x12c53a60()*-0.349389);
}

double MLP_ZH125vsZbb::synapse0x12c54a10() {
   return (neuron0x12c53e30()*1.50348);
}

double MLP_ZH125vsZbb::synapse0x12c54a50() {
   return (neuron0x12c54270()*1.82801);
}

