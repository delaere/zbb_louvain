#include "../NN/MLP_Higgs_vs_DY_ML_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.4497)/1.1857;
   input1 = (in1 - 20.1669)/1.09435;
   input2 = (in2 - 25.0327)/1.4596;
   input3 = (in3 - 14.0458)/1.92936;
   switch(index) {
     case 0:
         return neuron0x146a49d0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 19.4497)/1.1857;
   input1 = (input[1] - 20.1669)/1.09435;
   input2 = (input[2] - 25.0327)/1.4596;
   input3 = (input[3] - 14.0458)/1.92936;
   switch(index) {
     case 0:
         return neuron0x146a49d0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a1a00() {
   return input0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a1d10() {
   return input1;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a2020() {
   return input2;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a2330() {
   return input3;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::input0x146a2780() {
   double input = -1.16223;
   input += synapse0x12cd4b60();
   input += synapse0x146a2a00();
   input += synapse0x146a2a40();
   input += synapse0x146a2a80();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a2780() {
   double input = input0x146a2780();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::input0x146a2ac0() {
   double input = 0.236559;
   input += synapse0x146a2dd0();
   input += synapse0x146a2e10();
   input += synapse0x146a2e50();
   input += synapse0x146a2e90();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a2ac0() {
   double input = input0x146a2ac0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::input0x146a2ed0() {
   double input = -6.33508;
   input += synapse0x146a31e0();
   input += synapse0x146a3220();
   input += synapse0x146a3260();
   input += synapse0x146a32a0();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a2ed0() {
   double input = input0x146a2ed0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::input0x146a32e0() {
   double input = -2.39012;
   input += synapse0x146a35f0();
   input += synapse0x146a3630();
   input += synapse0x146a3670();
   input += synapse0x146a36b0();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a32e0() {
   double input = input0x146a32e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::input0x146a36f0() {
   double input = 3.71038;
   input += synapse0x146a3a00();
   input += synapse0x1462e5e0();
   input += synapse0x12d3d720();
   input += synapse0x12d3d760();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a36f0() {
   double input = input0x146a36f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::input0x146a3b50() {
   double input = -0.859866;
   input += synapse0x146a3e60();
   input += synapse0x146a3ea0();
   input += synapse0x146a3ee0();
   input += synapse0x146a3f20();
   input += synapse0x146a3f60();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a3b50() {
   double input = input0x146a3b50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::input0x146a3fa0() {
   double input = 3.19006;
   input += synapse0x146a42b0();
   input += synapse0x146a42f0();
   input += synapse0x146a4330();
   input += synapse0x146a4370();
   input += synapse0x146a43b0();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a3fa0() {
   double input = input0x146a3fa0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::input0x146a43f0() {
   double input = -0.712909;
   input += synapse0x146a4700();
   input += synapse0x146a4740();
   input += synapse0x146a4780();
   input += synapse0x1467c4f0();
   input += synapse0x146a8730();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a43f0() {
   double input = input0x146a43f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::input0x146a49d0() {
   double input = 1.25792;
   input += synapse0x146a4d10();
   input += synapse0x146a4d50();
   input += synapse0x146a4d90();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::neuron0x146a49d0() {
   double input = input0x146a49d0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x12cd4b60() {
   return (neuron0x146a1a00()*-4.2665);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a2a00() {
   return (neuron0x146a1d10()*4.55434);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a2a40() {
   return (neuron0x146a2020()*-0.160241);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a2a80() {
   return (neuron0x146a2330()*0.139139);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a2dd0() {
   return (neuron0x146a1a00()*0.586085);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a2e10() {
   return (neuron0x146a1d10()*1.27256);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a2e50() {
   return (neuron0x146a2020()*-4.30294);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a2e90() {
   return (neuron0x146a2330()*3.15619);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a31e0() {
   return (neuron0x146a1a00()*-3.90425);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a3220() {
   return (neuron0x146a1d10()*-1.41318);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a3260() {
   return (neuron0x146a2020()*4.78793);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a32a0() {
   return (neuron0x146a2330()*0.477206);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a35f0() {
   return (neuron0x146a1a00()*0.275512);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a3630() {
   return (neuron0x146a1d10()*1.42797);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a3670() {
   return (neuron0x146a2020()*-0.822139);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a36b0() {
   return (neuron0x146a2330()*-2.29274);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a3a00() {
   return (neuron0x146a1a00()*-0.737577);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x1462e5e0() {
   return (neuron0x146a1d10()*3.25381);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x12d3d720() {
   return (neuron0x146a2020()*-4.78526);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x12d3d760() {
   return (neuron0x146a2330()*1.92668);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a3e60() {
   return (neuron0x146a2780()*-0.163182);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a3ea0() {
   return (neuron0x146a2ac0()*-0.652545);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a3ee0() {
   return (neuron0x146a2ed0()*-1.24912);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a3f20() {
   return (neuron0x146a32e0()*4.46462);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a3f60() {
   return (neuron0x146a36f0()*1.1109);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a42b0() {
   return (neuron0x146a2780()*2.13237);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a42f0() {
   return (neuron0x146a2ac0()*2.19943);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a4330() {
   return (neuron0x146a2ed0()*3.24703);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a4370() {
   return (neuron0x146a32e0()*-6.7125);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a43b0() {
   return (neuron0x146a36f0()*-4.06522);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a4700() {
   return (neuron0x146a2780()*-0.0721107);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a4740() {
   return (neuron0x146a2ac0()*-0.205888);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a4780() {
   return (neuron0x146a2ed0()*-1.01842);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x1467c4f0() {
   return (neuron0x146a32e0()*0.990479);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a8730() {
   return (neuron0x146a36f0()*0.589107);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a4d10() {
   return (neuron0x146a3b50()*-1.79488);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a4d50() {
   return (neuron0x146a3fa0()*-1.39063);
}

double MLP_Higgs_vs_DY_ML_CSV_2011_mm::synapse0x146a4d90() {
   return (neuron0x146a43f0()*2.35089);
}

