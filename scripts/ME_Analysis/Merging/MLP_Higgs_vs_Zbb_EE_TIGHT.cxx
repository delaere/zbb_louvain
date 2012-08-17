#include "MLP_Higgs_vs_Zbb_EE_TIGHT.h"
#include <cmath>

double MLP_Higgs_vs_Zbb_EE_TIGHT::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.385)/2.76408;
   input1 = (in1 - 20.3306)/0.893865;
   input2 = (in2 - 24.5391)/3.03816;
   input3 = (in3 - 13.5769)/1.78677;
   switch(index) {
     case 0:
         return neuron0x1c3542d0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::Value(int index, double* input) {
   input0 = (input[0] - 19.385)/2.76408;
   input1 = (input[1] - 20.3306)/0.893865;
   input2 = (input[2] - 24.5391)/3.03816;
   input3 = (input[3] - 13.5769)/1.78677;
   switch(index) {
     case 0:
         return neuron0x1c3542d0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c3518e0() {
   return input0;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c351bf0() {
   return input1;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c351f00() {
   return input2;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c352210() {
   return input3;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::input0x1c352660() {
   double input = -0.404452;
   input += synapse0x1c2fa830();
   input += synapse0x1c3528e0();
   input += synapse0x1c352920();
   input += synapse0x1c352960();
   return input;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c352660() {
   double input = input0x1c352660();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::input0x1c3529a0() {
   double input = 0.10734;
   input += synapse0x1c352cb0();
   input += synapse0x1c352cf0();
   input += synapse0x1c352d30();
   input += synapse0x1c352d70();
   return input;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c3529a0() {
   double input = input0x1c3529a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::input0x1c352db0() {
   double input = -1.77711;
   input += synapse0x1c3530c0();
   input += synapse0x1c353100();
   input += synapse0x1c353140();
   input += synapse0x1c353180();
   return input;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c352db0() {
   double input = input0x1c352db0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::input0x1c3531c0() {
   double input = 3.18284;
   input += synapse0x1c3534d0();
   input += synapse0x1c353510();
   input += synapse0x1c353550();
   input += synapse0x1c353590();
   return input;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c3531c0() {
   double input = input0x1c3531c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::input0x1c3535d0() {
   double input = 2.45468;
   input += synapse0x1c3538e0();
   input += synapse0x1c2fa400();
   input += synapse0x1bd93320();
   input += synapse0x1bd93360();
   return input;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c3535d0() {
   double input = input0x1c3535d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::input0x1c353a30() {
   double input = -1.04453;
   input += synapse0x1c353d40();
   input += synapse0x1c353d80();
   input += synapse0x1c353dc0();
   input += synapse0x1c353e00();
   input += synapse0x1c353e40();
   return input;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c353a30() {
   double input = input0x1c353a30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::input0x1c353e80() {
   double input = -0.70577;
   input += synapse0x1c354190();
   input += synapse0x1c3541d0();
   input += synapse0x1c354210();
   input += synapse0x1c354250();
   input += synapse0x1c354290();
   return input;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c353e80() {
   double input = input0x1c353e80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::input0x1c3542d0() {
   double input = 0.582702;
   input += synapse0x1c354610();
   input += synapse0x1c354650();
   return input;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::neuron0x1c3542d0() {
   double input = input0x1c3542d0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c2fa830() {
   return (neuron0x1c3518e0()*0.466913);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c3528e0() {
   return (neuron0x1c351bf0()*-0.311804);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c352920() {
   return (neuron0x1c351f00()*0.682556);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c352960() {
   return (neuron0x1c352210()*2.90057);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c352cb0() {
   return (neuron0x1c3518e0()*-5.02608);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c352cf0() {
   return (neuron0x1c351bf0()*-0.265894);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c352d30() {
   return (neuron0x1c351f00()*0.426595);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c352d70() {
   return (neuron0x1c352210()*2.78648);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c3530c0() {
   return (neuron0x1c3518e0()*-2.21882);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c353100() {
   return (neuron0x1c351bf0()*-1.57317);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c353140() {
   return (neuron0x1c351f00()*1.40338);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c353180() {
   return (neuron0x1c352210()*2.33986);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c3534d0() {
   return (neuron0x1c3518e0()*0.0983891);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c353510() {
   return (neuron0x1c351bf0()*0.249377);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c353550() {
   return (neuron0x1c351f00()*-1.5369);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c353590() {
   return (neuron0x1c352210()*-1.89457);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c3538e0() {
   return (neuron0x1c3518e0()*-1.86745);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c2fa400() {
   return (neuron0x1c351bf0()*0.0947542);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1bd93320() {
   return (neuron0x1c351f00()*-0.980736);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1bd93360() {
   return (neuron0x1c352210()*-1.56747);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c353d40() {
   return (neuron0x1c352660()*-2.18525);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c353d80() {
   return (neuron0x1c3529a0()*-1.89702);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c353dc0() {
   return (neuron0x1c352db0()*2.69508);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c353e00() {
   return (neuron0x1c3531c0()*1.5268);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c353e40() {
   return (neuron0x1c3535d0()*-0.841952);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c354190() {
   return (neuron0x1c352660()*-0.390669);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c3541d0() {
   return (neuron0x1c3529a0()*1.41733);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c354210() {
   return (neuron0x1c352db0()*-0.523279);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c354250() {
   return (neuron0x1c3531c0()*-1.66613);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c354290() {
   return (neuron0x1c3535d0()*1.44056);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c354610() {
   return (neuron0x1c353a30()*2.00176);
}

double MLP_Higgs_vs_Zbb_EE_TIGHT::synapse0x1c354650() {
   return (neuron0x1c353e80()*-1.51571);
}

