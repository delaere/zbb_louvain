#include "MLP_Higgs_vs_tt_MU.h"
#include <cmath>

double MLP_Higgs_vs_tt_MU::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 21.8234)/1.25048;
   input1 = (in1 - 25.4827)/1.69395;
   input2 = (in2 - 14.5024)/2.08321;
   switch(index) {
     case 0:
         return neuron0xc6dc240();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_tt_MU::Value(int index, double* input) {
   input0 = (input[0] - 21.8234)/1.25048;
   input1 = (input[1] - 25.4827)/1.69395;
   input2 = (input[2] - 14.5024)/2.08321;
   switch(index) {
     case 0:
         return neuron0xc6dc240();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_tt_MU::neuron0xc6c93e0() {
   return input0;
}

double MLP_Higgs_vs_tt_MU::neuron0xc6c9720() {
   return input1;
}

double MLP_Higgs_vs_tt_MU::neuron0xc6da660() {
   return input2;
}

double MLP_Higgs_vs_tt_MU::input0xc6daa40() {
   double input = 0.989024;
   input += synapse0xc6b00d0();
   input += synapse0xc691b20();
   input += synapse0xc6dacf0();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0xc6daa40() {
   double input = input0xc6daa40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0xc6dad30() {
   double input = 0.6541;
   input += synapse0xc6db070();
   input += synapse0xc6db0b0();
   input += synapse0xc6db0f0();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0xc6dad30() {
   double input = input0xc6dad30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0xc6db130() {
   double input = 2.61591;
   input += synapse0xc6db470();
   input += synapse0xc6db4b0();
   input += synapse0xc6db4f0();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0xc6db130() {
   double input = input0xc6db130();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0xc6db530() {
   double input = -1.56426;
   input += synapse0xc6db870();
   input += synapse0xc6db8b0();
   input += synapse0xc6db8f0();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0xc6db530() {
   double input = input0xc6db530();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0xc6db930() {
   double input = 0.471778;
   input += synapse0xc6dbc70();
   input += synapse0xc6dbcb0();
   input += synapse0xc6dbcf0();
   input += synapse0xc6dbd30();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0xc6db930() {
   double input = input0xc6db930();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0xc6dbd70() {
   double input = -1.29217;
   input += synapse0xc6dc0b0();
   input += synapse0xc63f380();
   input += synapse0xc63f3c0();
   input += synapse0xc6dc200();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0xc6dbd70() {
   double input = input0xc6dbd70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0xc6dc240() {
   double input = 0.95956;
   input += synapse0xc6dc460();
   input += synapse0xc6dc4a0();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0xc6dc240() {
   double input = input0xc6dc240();
   return (input * 1)+0;
}

double MLP_Higgs_vs_tt_MU::synapse0xc6b00d0() {
   return (neuron0xc6c93e0()*-0.332559);
}

double MLP_Higgs_vs_tt_MU::synapse0xc691b20() {
   return (neuron0xc6c9720()*-1.56723);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6dacf0() {
   return (neuron0xc6da660()*-1.90656);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6db070() {
   return (neuron0xc6c93e0()*-4.37675);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6db0b0() {
   return (neuron0xc6c9720()*0.704394);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6db0f0() {
   return (neuron0xc6da660()*1.24985);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6db470() {
   return (neuron0xc6c93e0()*-1.38984);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6db4b0() {
   return (neuron0xc6c9720()*-1.08393);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6db4f0() {
   return (neuron0xc6da660()*4.75593);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6db870() {
   return (neuron0xc6c93e0()*4.19659);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6db8b0() {
   return (neuron0xc6c9720()*0.572231);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6db8f0() {
   return (neuron0xc6da660()*-5.89405);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6dbc70() {
   return (neuron0xc6daa40()*1.96084);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6dbcb0() {
   return (neuron0xc6dad30()*-1.83212);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6dbcf0() {
   return (neuron0xc6db130()*3.48704);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6dbd30() {
   return (neuron0xc6db530()*-5.22513);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6dc0b0() {
   return (neuron0xc6daa40()*1.5183);
}

double MLP_Higgs_vs_tt_MU::synapse0xc63f380() {
   return (neuron0xc6dad30()*-2.16037);
}

double MLP_Higgs_vs_tt_MU::synapse0xc63f3c0() {
   return (neuron0xc6db130()*0.196266);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6dc200() {
   return (neuron0xc6db530()*-3.36768);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6dc460() {
   return (neuron0xc6db930()*-1.18534);
}

double MLP_Higgs_vs_tt_MU::synapse0xc6dc4a0() {
   return (neuron0xc6dbd70()*2.74774);
}

