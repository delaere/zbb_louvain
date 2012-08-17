#include "MLP_Higgs_vs_tt_EE_TIGHT.h"
#include <cmath>

double MLP_Higgs_vs_tt_EE_TIGHT::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 27.8048)/34.9677;
   input1 = (in1 - 14.9961)/2.15676;
   input2 = (in2 - 25.3918)/49.0691;
   switch(index) {
     case 0:
         return neuron0xe469db0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_tt_EE_TIGHT::Value(int index, double* input) {
   input0 = (input[0] - 27.8048)/34.9677;
   input1 = (input[1] - 14.9961)/2.15676;
   input2 = (input[2] - 25.3918)/49.0691;
   switch(index) {
     case 0:
         return neuron0xe469db0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe455260() {
   return input0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe455570() {
   return input1;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe4663e0() {
   return input2;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe466830() {
   double input = 1.99809;
   input += synapse0xe4234a0();
   input += synapse0xe43d460();
   input += synapse0xe4550a0();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe466830() {
   double input = input0xe466830();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe466ab0() {
   double input = 6.80188;
   input += synapse0xe423530();
   input += synapse0xe455760();
   input += synapse0xe466dc0();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe466ab0() {
   double input = input0xe466ab0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe466e00() {
   double input = -2.11647;
   input += synapse0xe467110();
   input += synapse0xe467150();
   input += synapse0xe467190();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe466e00() {
   double input = input0xe466e00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe4671d0() {
   double input = 3.66371;
   input += synapse0xe4674e0();
   input += synapse0xe467520();
   input += synapse0xe467560();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe4671d0() {
   double input = input0xe4671d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe4675a0() {
   double input = -1.77029;
   input += synapse0xe4678b0();
   input += synapse0xe4678f0();
   input += synapse0xe467930();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe4675a0() {
   double input = input0xe4675a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe467970() {
   double input = -2.09866;
   input += synapse0xe467c80();
   input += synapse0xe467cc0();
   input += synapse0xe243460();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe467970() {
   double input = input0xe467970();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe467e10() {
   double input = 4.91589;
   input += synapse0xe2434a0();
   input += synapse0xe468120();
   input += synapse0xe468160();
   input += synapse0xe4681a0();
   input += synapse0xe4681e0();
   input += synapse0xe468220();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe467e10() {
   double input = input0xe467e10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe468260() {
   double input = -0.613516;
   input += synapse0xe4685a0();
   input += synapse0xe4685e0();
   input += synapse0xe468620();
   input += synapse0xe468660();
   input += synapse0xe4686a0();
   input += synapse0xe4686e0();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe468260() {
   double input = input0xe468260();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe468720() {
   double input = 1.36662;
   input += synapse0xe468a60();
   input += synapse0xe468aa0();
   input += synapse0xe468ae0();
   input += synapse0xe423090();
   input += synapse0xe455000();
   input += synapse0xe455040();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe468720() {
   double input = input0xe468720();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe468d30() {
   double input = -0.556504;
   input += synapse0xe467dc0();
   input += synapse0xe468fb0();
   input += synapse0xe468ff0();
   input += synapse0xe469030();
   input += synapse0xe469070();
   input += synapse0xe4690b0();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe468d30() {
   double input = input0xe468d30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe4690f0() {
   double input = -1.43368;
   input += synapse0xe469430();
   input += synapse0xe469470();
   input += synapse0xe4694b0();
   input += synapse0xe4694f0();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe4690f0() {
   double input = input0xe4690f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe469530() {
   double input = 1.28662;
   input += synapse0xe469870();
   input += synapse0xe4698b0();
   input += synapse0xe4698f0();
   input += synapse0xe469930();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe469530() {
   double input = input0xe469530();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe469970() {
   double input = 3.04581;
   input += synapse0xe469cb0();
   input += synapse0xe469cf0();
   input += synapse0xe469d30();
   input += synapse0xe469d70();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe469970() {
   double input = input0xe469970();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::input0xe469db0() {
   double input = 0.97252;
   input += synapse0xe4667b0();
   input += synapse0xe4667f0();
   input += synapse0xe46a030();
   return input;
}

double MLP_Higgs_vs_tt_EE_TIGHT::neuron0xe469db0() {
   double input = input0xe469db0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4234a0() {
   return (neuron0xe455260()*-7.32973);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe43d460() {
   return (neuron0xe455570()*-1.52868);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4550a0() {
   return (neuron0xe4663e0()*7.87401);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe423530() {
   return (neuron0xe455260()*-1.46588);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe455760() {
   return (neuron0xe455570()*6.86891);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe466dc0() {
   return (neuron0xe4663e0()*-1.42781);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe467110() {
   return (neuron0xe455260()*2.59125);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe467150() {
   return (neuron0xe455570()*-1.80375);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe467190() {
   return (neuron0xe4663e0()*-4.13827);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4674e0() {
   return (neuron0xe455260()*-5.0144);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe467520() {
   return (neuron0xe455570()*5.13471);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe467560() {
   return (neuron0xe4663e0()*-16.8438);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4678b0() {
   return (neuron0xe455260()*4.2983);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4678f0() {
   return (neuron0xe455570()*1.8766);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe467930() {
   return (neuron0xe4663e0()*9.53877);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe467c80() {
   return (neuron0xe455260()*0.407848);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe467cc0() {
   return (neuron0xe455570()*-0.021503);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe243460() {
   return (neuron0xe4663e0()*8.26156);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe2434a0() {
   return (neuron0xe466830()*-10.4601);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe468120() {
   return (neuron0xe466ab0()*-5.0277);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe468160() {
   return (neuron0xe466e00()*5.8152);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4681a0() {
   return (neuron0xe4671d0()*9.54932);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4681e0() {
   return (neuron0xe4675a0()*-7.38097);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe468220() {
   return (neuron0xe467970()*-6.05836);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4685a0() {
   return (neuron0xe466830()*-1.3716);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4685e0() {
   return (neuron0xe466ab0()*-0.825829);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe468620() {
   return (neuron0xe466e00()*-1.47685);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe468660() {
   return (neuron0xe4671d0()*0.781618);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4686a0() {
   return (neuron0xe4675a0()*-1.04931);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4686e0() {
   return (neuron0xe467970()*-0.910429);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe468a60() {
   return (neuron0xe466830()*0.449294);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe468aa0() {
   return (neuron0xe466ab0()*0.618718);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe468ae0() {
   return (neuron0xe466e00()*2.0403);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe423090() {
   return (neuron0xe4671d0()*-0.518967);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe455000() {
   return (neuron0xe4675a0()*0.950146);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe455040() {
   return (neuron0xe467970()*0.586363);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe467dc0() {
   return (neuron0xe466830()*-1.26507);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe468fb0() {
   return (neuron0xe466ab0()*-1.08143);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe468ff0() {
   return (neuron0xe466e00()*-0.272368);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe469030() {
   return (neuron0xe4671d0()*0.240625);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe469070() {
   return (neuron0xe4675a0()*-1.35777);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4690b0() {
   return (neuron0xe467970()*-1.08672);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe469430() {
   return (neuron0xe467e10()*0.798491);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe469470() {
   return (neuron0xe468260()*0.92935);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4694b0() {
   return (neuron0xe468720()*-1.85411);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4694f0() {
   return (neuron0xe468d30()*0.595942);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe469870() {
   return (neuron0xe467e10()*3.54095);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4698b0() {
   return (neuron0xe468260()*-0.107876);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4698f0() {
   return (neuron0xe468720()*0.949754);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe469930() {
   return (neuron0xe468d30()*0.0321892);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe469cb0() {
   return (neuron0xe467e10()*-12.5255);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe469cf0() {
   return (neuron0xe468260()*-0.513484);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe469d30() {
   return (neuron0xe468720()*3.09321);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe469d70() {
   return (neuron0xe468d30()*-1.09161);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4667b0() {
   return (neuron0xe4690f0()*0.0958289);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe4667f0() {
   return (neuron0xe469530()*-0.989885);
}

double MLP_Higgs_vs_tt_EE_TIGHT::synapse0xe46a030() {
   return (neuron0xe469970()*0.925804);
}

