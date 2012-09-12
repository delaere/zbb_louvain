#include "MLP_Zbb_tt_Mll_MeTtest_Mll_MET.h"
#include <cmath>

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::Value(int index,double in0,double in1) {
   input0 = (in0 - 90.603)/8.17209;
   input1 = (in1 - 31.892)/15.308;
   switch(index) {
     case 0:
         return neuron0x1dbf7b20();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::Value(int index, double* input) {
   input0 = (input[0] - 90.603)/8.17209;
   input1 = (input[1] - 31.892)/15.308;
   switch(index) {
     case 0:
         return neuron0x1dbf7b20();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::neuron0x1dbe4030() {
   return input0;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::neuron0x1dbe4340() {
   return input1;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::input0x1dbf6560() {
   double input = 1.76023;
   input += synapse0x1dbc9bb0();
   input += synapse0x1dbf67e0();
   return input;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::neuron0x1dbf6560() {
   double input = input0x1dbf6560();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::input0x1dbf6820() {
   double input = 0.792277;
   input += synapse0x1dbf6b30();
   input += synapse0x1dbf6b70();
   return input;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::neuron0x1dbf6820() {
   double input = input0x1dbf6820();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::input0x1dbf6bb0() {
   double input = -0.177403;
   input += synapse0x1dbf6ec0();
   input += synapse0x1dbf6f00();
   return input;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::neuron0x1dbf6bb0() {
   double input = input0x1dbf6bb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::input0x1dbf6f40() {
   double input = -2.30033;
   input += synapse0x1dbf7250();
   input += synapse0x1dbf7290();
   return input;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::neuron0x1dbf6f40() {
   double input = input0x1dbf6f40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::input0x1dbf72d0() {
   double input = -5.28077;
   input += synapse0x1dbf75e0();
   input += synapse0x1dbf7620();
   input += synapse0x1dbf7660();
   input += synapse0x1dbf76a0();
   return input;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::neuron0x1dbf72d0() {
   double input = input0x1dbf72d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::input0x1dbf76e0() {
   double input = -3.55739;
   input += synapse0x1dbf7a20();
   input += synapse0x1dbf7a60();
   input += synapse0x1dbf7aa0();
   input += synapse0x1dbf7ae0();
   return input;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::neuron0x1dbf76e0() {
   double input = input0x1dbf76e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::input0x1dbf7b20() {
   double input = -0.398429;
   input += synapse0x1dbf7e60();
   input += synapse0x1dbe3ea0();
   return input;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::neuron0x1dbf7b20() {
   double input = input0x1dbf7b20();
   return (input * 1)+0;
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbc9bb0() {
   return (neuron0x1dbe4030()*-4.48812);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf67e0() {
   return (neuron0x1dbe4340()*-0.777702);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf6b30() {
   return (neuron0x1dbe4030()*4.52696);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf6b70() {
   return (neuron0x1dbe4340()*0.00387279);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf6ec0() {
   return (neuron0x1dbe4030()*1.6155);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf6f00() {
   return (neuron0x1dbe4340()*-1.78228);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf7250() {
   return (neuron0x1dbe4030()*5.74323);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf7290() {
   return (neuron0x1dbe4340()*-4.65807);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf75e0() {
   return (neuron0x1dbf6560()*4.15835);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf7620() {
   return (neuron0x1dbf6820()*0.934207);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf7660() {
   return (neuron0x1dbf6bb0()*1.05327);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf76a0() {
   return (neuron0x1dbf6f40()*2.7402);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf7a20() {
   return (neuron0x1dbf6560()*0.550295);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf7a60() {
   return (neuron0x1dbf6820()*1.76196);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf7aa0() {
   return (neuron0x1dbf6bb0()*1.58609);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf7ae0() {
   return (neuron0x1dbf6f40()*-3.27387);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbf7e60() {
   return (neuron0x1dbf72d0()*1.26667);
}

double MLP_Zbb_tt_Mll_MeTtest_Mll_MET::synapse0x1dbe3ea0() {
   return (neuron0x1dbf76e0()*3.06987);
}

