#include "../NN/MLP_Zbb_tt_EE.h"
#include <cmath>

double MLP_Zbb_tt_EE::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.6321)/1.05575;
   input1 = (in1 - 20.9125)/1.08293;
   input2 = (in2 - 21.6884)/0.800382;
   input3 = (in3 - 65.8143)/37.6943;
   switch(index) {
     case 0:
         return neuron0x84e43f0();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_EE::Value(int index, double* input) {
   input0 = (input[0] - 21.6321)/1.05575;
   input1 = (input[1] - 20.9125)/1.08293;
   input2 = (input[2] - 21.6884)/0.800382;
   input3 = (input[3] - 65.8143)/37.6943;
   switch(index) {
     case 0:
         return neuron0x84e43f0();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_EE::neuron0x84e2230() {
   return input0;
}

double MLP_Zbb_tt_EE::neuron0x84e2540() {
   return input1;
}

double MLP_Zbb_tt_EE::neuron0x84e2850() {
   return input2;
}

double MLP_Zbb_tt_EE::neuron0x84e2b60() {
   return input3;
}

double MLP_Zbb_tt_EE::input0x84e2fe0() {
   double input = 3.91307;
   input += synapse0x7eedcc0();
   input += synapse0x84e3260();
   input += synapse0x84e32a0();
   input += synapse0x84e32e0();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x84e2fe0() {
   double input = input0x84e2fe0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_EE::input0x84e3320() {
   double input = -4.78883;
   input += synapse0x84e3630();
   input += synapse0x84e3670();
   input += synapse0x84e36b0();
   input += synapse0x84e36f0();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x84e3320() {
   double input = input0x84e3320();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_EE::input0x84e3730() {
   double input = 0.183607;
   input += synapse0x84e3a40();
   input += synapse0x84e3a80();
   input += synapse0x84e3ac0();
   input += synapse0x84e3b00();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x84e3730() {
   double input = input0x84e3730();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_EE::input0x84e3b40() {
   double input = -0.727824;
   input += synapse0x84e3e50();
   input += synapse0x84e3e90();
   input += synapse0x84e3ed0();
   input += synapse0x84e3f10();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x84e3b40() {
   double input = input0x84e3b40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_EE::input0x84e3f50() {
   double input = 0.678719;
   input += synapse0x84e4260();
   input += synapse0x7ec7c50();
   input += synapse0x7ec7c90();
   input += synapse0x84e43b0();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x84e3f50() {
   double input = input0x84e3f50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_EE::input0x84e43f0() {
   double input = 0.0873911;
   input += synapse0x84e4700();
   input += synapse0x84e4740();
   input += synapse0x84e4780();
   input += synapse0x84e47c0();
   input += synapse0x84e4800();
   return input;
}

double MLP_Zbb_tt_EE::neuron0x84e43f0() {
   double input = input0x84e43f0();
   return (input * 1)+0;
}

double MLP_Zbb_tt_EE::synapse0x7eedcc0() {
   return (neuron0x84e2230()*1.06069);
}

double MLP_Zbb_tt_EE::synapse0x84e3260() {
   return (neuron0x84e2540()*0.878525);
}

double MLP_Zbb_tt_EE::synapse0x84e32a0() {
   return (neuron0x84e2850()*-1.09927);
}

double MLP_Zbb_tt_EE::synapse0x84e32e0() {
   return (neuron0x84e2b60()*2.92194);
}

double MLP_Zbb_tt_EE::synapse0x84e3630() {
   return (neuron0x84e2230()*-0.994501);
}

double MLP_Zbb_tt_EE::synapse0x84e3670() {
   return (neuron0x84e2540()*-0.954715);
}

double MLP_Zbb_tt_EE::synapse0x84e36b0() {
   return (neuron0x84e2850()*1.57134);
}

double MLP_Zbb_tt_EE::synapse0x84e36f0() {
   return (neuron0x84e2b60()*-3.78254);
}

double MLP_Zbb_tt_EE::synapse0x84e3a40() {
   return (neuron0x84e2230()*0.367564);
}

double MLP_Zbb_tt_EE::synapse0x84e3a80() {
   return (neuron0x84e2540()*0.140711);
}

double MLP_Zbb_tt_EE::synapse0x84e3ac0() {
   return (neuron0x84e2850()*0.633645);
}

double MLP_Zbb_tt_EE::synapse0x84e3b00() {
   return (neuron0x84e2b60()*0.639149);
}

double MLP_Zbb_tt_EE::synapse0x84e3e50() {
   return (neuron0x84e2230()*-1.11863);
}

double MLP_Zbb_tt_EE::synapse0x84e3e90() {
   return (neuron0x84e2540()*-1.35516);
}

double MLP_Zbb_tt_EE::synapse0x84e3ed0() {
   return (neuron0x84e2850()*0.649655);
}

double MLP_Zbb_tt_EE::synapse0x84e3f10() {
   return (neuron0x84e2b60()*-0.809122);
}

double MLP_Zbb_tt_EE::synapse0x84e4260() {
   return (neuron0x84e2230()*0.0529839);
}

double MLP_Zbb_tt_EE::synapse0x7ec7c50() {
   return (neuron0x84e2540()*-0.0992181);
}

double MLP_Zbb_tt_EE::synapse0x7ec7c90() {
   return (neuron0x84e2850()*0.557022);
}

double MLP_Zbb_tt_EE::synapse0x84e43b0() {
   return (neuron0x84e2b60()*0.373086);
}

double MLP_Zbb_tt_EE::synapse0x84e4700() {
   return (neuron0x84e2fe0()*0.0255088);
}

double MLP_Zbb_tt_EE::synapse0x84e4740() {
   return (neuron0x84e3320()*1.01198);
}

double MLP_Zbb_tt_EE::synapse0x84e4780() {
   return (neuron0x84e3730()*0.139235);
}

double MLP_Zbb_tt_EE::synapse0x84e47c0() {
   return (neuron0x84e3b40()*0.0446161);
}

double MLP_Zbb_tt_EE::synapse0x84e4800() {
   return (neuron0x84e3f50()*-0.289454);
}

