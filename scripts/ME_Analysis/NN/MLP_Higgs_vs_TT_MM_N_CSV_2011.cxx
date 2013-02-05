#include "../NN/MLP_Higgs_vs_TT_MM_N_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_TT_MM_N_CSV_2011::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.5229)/1.8106;
   input1 = (in1 - 25.2664)/1.59636;
   input2 = (in2 - 14.1289)/2.06328;
   switch(index) {
     case 0:
         return neuron0x6b78c20();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 22.5229)/1.8106;
   input1 = (input[1] - 25.2664)/1.59636;
   input2 = (input[2] - 14.1289)/2.06328;
   switch(index) {
     case 0:
         return neuron0x6b78c20();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b649f0() {
   return input0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b64d00() {
   return input1;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b75b60() {
   return input2;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b75fb0() {
   double input = -2.66773;
   input += synapse0x6b32cb0();
   input += synapse0x6b4cc20();
   input += synapse0x6b32d40();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b75fb0() {
   double input = input0x6b75fb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b76230() {
   double input = -3.82703;
   input += synapse0x6b64f80();
   input += synapse0x6b76540();
   input += synapse0x6b76580();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b76230() {
   double input = input0x6b76230();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b765c0() {
   double input = -0.458517;
   input += synapse0x6b768d0();
   input += synapse0x6b76910();
   input += synapse0x6b76950();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b765c0() {
   double input = input0x6b765c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b76990() {
   double input = 6.72614;
   input += synapse0x6b76ca0();
   input += synapse0x6b76ce0();
   input += synapse0x6b76d20();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b76990() {
   double input = input0x6b76990();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b76d60() {
   double input = 0.861063;
   input += synapse0x6b77070();
   input += synapse0x6b770b0();
   input += synapse0x6b770f0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b76d60() {
   double input = input0x6b76d60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b77130() {
   double input = 0.330908;
   input += synapse0x6b77440();
   input += synapse0x6b77480();
   input += synapse0x68c3880();
   input += synapse0x68c38c0();
   input += synapse0x6b775d0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b77130() {
   double input = input0x6b77130();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b77610() {
   double input = 3.70466;
   input += synapse0x6b77950();
   input += synapse0x6b77990();
   input += synapse0x6b779d0();
   input += synapse0x6b77a10();
   input += synapse0x6b77a50();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b77610() {
   double input = input0x6b77610();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b77a90() {
   double input = 3.70026;
   input += synapse0x6b77dd0();
   input += synapse0x6b77e10();
   input += synapse0x6b77e50();
   input += synapse0x6b77e90();
   input += synapse0x6b77ed0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b77a90() {
   double input = input0x6b77a90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b77f10() {
   double input = 0.647069;
   input += synapse0x6b78250();
   input += synapse0x6b78290();
   input += synapse0x6b782d0();
   input += synapse0x6b64860();
   input += synapse0x6b4d4b0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b77f10() {
   double input = input0x6b77f10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b78520() {
   double input = 0.615598;
   input += synapse0x6b328e0();
   input += synapse0x6b77550();
   input += synapse0x6b77590();
   input += synapse0x6b787a0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b78520() {
   double input = input0x6b78520();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b787e0() {
   double input = -0.861617;
   input += synapse0x6b78b20();
   input += synapse0x6b78b60();
   input += synapse0x6b78ba0();
   input += synapse0x6b78be0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b787e0() {
   double input = input0x6b787e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::input0x6b78c20() {
   double input = -1.77792;
   input += synapse0x6b75f30();
   input += synapse0x6b75f70();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::neuron0x6b78c20() {
   double input = input0x6b78c20();
   return (input * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b32cb0() {
   return (neuron0x6b649f0()*1.34246);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b4cc20() {
   return (neuron0x6b64d00()*0.056477);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b32d40() {
   return (neuron0x6b75b60()*-3.82853);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b64f80() {
   return (neuron0x6b649f0()*6.36703);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b76540() {
   return (neuron0x6b64d00()*-0.938668);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b76580() {
   return (neuron0x6b75b60()*-3.18408);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b768d0() {
   return (neuron0x6b649f0()*-2.75358);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b76910() {
   return (neuron0x6b64d00()*3.13073);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b76950() {
   return (neuron0x6b75b60()*0.331594);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b76ca0() {
   return (neuron0x6b649f0()*6.82695);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b76ce0() {
   return (neuron0x6b64d00()*3.94211);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b76d20() {
   return (neuron0x6b75b60()*-0.054752);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77070() {
   return (neuron0x6b649f0()*-0.990283);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b770b0() {
   return (neuron0x6b64d00()*0.835622);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b770f0() {
   return (neuron0x6b75b60()*2.35286);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77440() {
   return (neuron0x6b75fb0()*-0.885946);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77480() {
   return (neuron0x6b76230()*-0.31172);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x68c3880() {
   return (neuron0x6b765c0()*0.132295);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x68c38c0() {
   return (neuron0x6b76990()*0.0152269);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b775d0() {
   return (neuron0x6b76d60()*-0.570549);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77950() {
   return (neuron0x6b75fb0()*-8.16245);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77990() {
   return (neuron0x6b76230()*-2.4944);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b779d0() {
   return (neuron0x6b765c0()*2.6198);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77a10() {
   return (neuron0x6b76990()*-7.09237);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77a50() {
   return (neuron0x6b76d60()*0.363558);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77dd0() {
   return (neuron0x6b75fb0()*-1.16161);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77e10() {
   return (neuron0x6b76230()*0.753818);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77e50() {
   return (neuron0x6b765c0()*-2.92786);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77e90() {
   return (neuron0x6b76990()*-2.19949);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77ed0() {
   return (neuron0x6b76d60()*-1.56745);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b78250() {
   return (neuron0x6b75fb0()*3.34349);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b78290() {
   return (neuron0x6b76230()*1.60266);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b782d0() {
   return (neuron0x6b765c0()*-1.7194);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b64860() {
   return (neuron0x6b76990()*-0.991092);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b4d4b0() {
   return (neuron0x6b76d60()*1.02989);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b328e0() {
   return (neuron0x6b77130()*-0.405868);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77550() {
   return (neuron0x6b77610()*-5.64643);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b77590() {
   return (neuron0x6b77a90()*-1.70041);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b787a0() {
   return (neuron0x6b77f10()*3.8972);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b78b20() {
   return (neuron0x6b77130()*-0.155824);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b78b60() {
   return (neuron0x6b77610()*1.61168);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b78ba0() {
   return (neuron0x6b77a90()*-0.884613);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b78be0() {
   return (neuron0x6b77f10()*1.88257);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b75f30() {
   return (neuron0x6b78520()*1.35636);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2011::synapse0x6b75f70() {
   return (neuron0x6b787e0()*2.58497);
}

