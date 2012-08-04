#include "MLP_Zbb_tt_Comb_EE_TIGHT.h"
#include <cmath>

double MLP_Zbb_tt_Comb_EE_TIGHT::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 20.2731)/1.05371;
   input1 = (in1 - 20.9484)/1.00144;
   input2 = (in2 - 21.8744)/11.3556;
   switch(index) {
     case 0:
         return neuron0xc8e4630();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_Comb_EE_TIGHT::Value(int index, double* input) {
   input0 = (input[0] - 20.2731)/1.05371;
   input1 = (input[1] - 20.9484)/1.00144;
   input2 = (input[2] - 21.8744)/11.3556;
   switch(index) {
     case 0:
         return neuron0xc8e4630();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8d1160() {
   return input0;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8d1470() {
   return input1;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8e22b0() {
   return input2;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::input0xc8e2700() {
   double input = -2.34048;
   input += synapse0xc89f370();
   input += synapse0xc8b9330();
   input += synapse0xc8d0f20();
   return input;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8e2700() {
   double input = input0xc8e2700();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::input0xc8e2980() {
   double input = 0.485312;
   input += synapse0xc89f400();
   input += synapse0xc8e2c90();
   input += synapse0xc8e2cd0();
   return input;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8e2980() {
   double input = input0xc8e2980();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::input0xc8e2d10() {
   double input = -1.20788;
   input += synapse0xc8e3020();
   input += synapse0xc8e3060();
   input += synapse0xc8e30a0();
   return input;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8e2d10() {
   double input = input0xc8e2d10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::input0xc8e30e0() {
   double input = -1.72698;
   input += synapse0xc8e33f0();
   input += synapse0xc8e3430();
   input += synapse0xc8e3470();
   return input;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8e30e0() {
   double input = input0xc8e30e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::input0xc8e34b0() {
   double input = -5.9007;
   input += synapse0xc8e37c0();
   input += synapse0xc8e3800();
   input += synapse0xc8e3840();
   return input;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8e34b0() {
   double input = input0xc8e34b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::input0xc8e3880() {
   double input = 2.84982;
   input += synapse0xc8e3b90();
   input += synapse0xc8e3bd0();
   input += synapse0xc56cc40();
   input += synapse0xc56cc80();
   input += synapse0xc8e3d20();
   return input;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8e3880() {
   double input = input0xc8e3880();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::input0xc8e3d60() {
   double input = 0.452289;
   input += synapse0xc8e4070();
   input += synapse0xc8e40b0();
   input += synapse0xc8e40f0();
   input += synapse0xc8e4130();
   input += synapse0xc8e4170();
   return input;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8e3d60() {
   double input = input0xc8e3d60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::input0xc8e41b0() {
   double input = 2.07118;
   input += synapse0xc8e44f0();
   input += synapse0xc8e4530();
   input += synapse0xc8e4570();
   input += synapse0xc8e45b0();
   input += synapse0xc8e45f0();
   return input;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8e41b0() {
   double input = input0xc8e41b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::input0xc8e4630() {
   double input = 0.290166;
   input += synapse0xc8e2680();
   input += synapse0xc8e26c0();
   input += synapse0xc8e48b0();
   return input;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::neuron0xc8e4630() {
   double input = input0xc8e4630();
   return (input * 1)+0;
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc89f370() {
   return (neuron0xc8d1160()*2.2132);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8b9330() {
   return (neuron0xc8d1470()*-0.594272);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8d0f20() {
   return (neuron0xc8e22b0()*5.91654);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc89f400() {
   return (neuron0xc8d1160()*3.17722);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e2c90() {
   return (neuron0xc8d1470()*-4.86037);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e2cd0() {
   return (neuron0xc8e22b0()*-2.42604);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e3020() {
   return (neuron0xc8d1160()*0.199142);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e3060() {
   return (neuron0xc8d1470()*1.91832);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e30a0() {
   return (neuron0xc8e22b0()*-5.4752);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e33f0() {
   return (neuron0xc8d1160()*-0.324169);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e3430() {
   return (neuron0xc8d1470()*-0.672533);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e3470() {
   return (neuron0xc8e22b0()*8.84682);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e37c0() {
   return (neuron0xc8d1160()*0.131276);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e3800() {
   return (neuron0xc8d1470()*-0.346288);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e3840() {
   return (neuron0xc8e22b0()*4.19378);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e3b90() {
   return (neuron0xc8e2700()*-0.463377);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e3bd0() {
   return (neuron0xc8e2980()*2.28165);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc56cc40() {
   return (neuron0xc8e2d10()*2.56746);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc56cc80() {
   return (neuron0xc8e30e0()*1.18974);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e3d20() {
   return (neuron0xc8e34b0()*1.86594);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e4070() {
   return (neuron0xc8e2700()*4.07625);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e40b0() {
   return (neuron0xc8e2980()*-1.75436);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e40f0() {
   return (neuron0xc8e2d10()*-5.11615);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e4130() {
   return (neuron0xc8e30e0()*7.15315);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e4170() {
   return (neuron0xc8e34b0()*-0.7233);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e44f0() {
   return (neuron0xc8e2700()*1.99833);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e4530() {
   return (neuron0xc8e2980()*-0.0611633);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e4570() {
   return (neuron0xc8e2d10()*-1.96515);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e45b0() {
   return (neuron0xc8e30e0()*1.7151);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e45f0() {
   return (neuron0xc8e34b0()*1.36399);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e2680() {
   return (neuron0xc8e3880()*0.206597);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e26c0() {
   return (neuron0xc8e3d60()*1.21384);
}

double MLP_Zbb_tt_Comb_EE_TIGHT::synapse0xc8e48b0() {
   return (neuron0xc8e41b0()*-0.729666);
}

