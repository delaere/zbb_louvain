#include "MLP_Higgs_vs_zz_MU.h"
#include <cmath>

double MLP_Higgs_vs_zz_MU::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.0182)/1.36719;
   input1 = (in1 - 10.854)/1.10222;
   input2 = (in2 - 24.9474)/1.3522;
   input3 = (in3 - 13.5311)/1.37938;
   switch(index) {
     case 0:
         return neuron0x12120820();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_zz_MU::Value(int index, double* input) {
   input0 = (input[0] - 21.0182)/1.36719;
   input1 = (input[1] - 10.854)/1.10222;
   input2 = (input[2] - 24.9474)/1.3522;
   input3 = (input[3] - 13.5311)/1.37938;
   switch(index) {
     case 0:
         return neuron0x12120820();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_zz_MU::neuron0x1211dbf0() {
   return input0;
}

double MLP_Higgs_vs_zz_MU::neuron0x1211df30() {
   return input1;
}

double MLP_Higgs_vs_zz_MU::neuron0x1211e270() {
   return input2;
}

double MLP_Higgs_vs_zz_MU::neuron0x1211e5b0() {
   return input3;
}

double MLP_Higgs_vs_zz_MU::input0x1211ea20() {
   double input = 2.11716;
   input += synapse0x120f6e20();
   input += synapse0x1211ecd0();
   input += synapse0x1211ed10();
   input += synapse0x1211ed50();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x1211ea20() {
   double input = input0x1211ea20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x1211ed90() {
   double input = -0.811308;
   input += synapse0x1211f0d0();
   input += synapse0x1211f110();
   input += synapse0x1211f150();
   input += synapse0x1211f190();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x1211ed90() {
   double input = input0x1211ed90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x1211f1d0() {
   double input = 0.459436;
   input += synapse0x1211f510();
   input += synapse0x1211f550();
   input += synapse0x1211f590();
   input += synapse0x1211f5d0();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x1211f1d0() {
   double input = input0x1211f1d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x1211f610() {
   double input = 0.724417;
   input += synapse0x1211f950();
   input += synapse0x1211f990();
   input += synapse0x1211f9d0();
   input += synapse0x1211fa10();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x1211f610() {
   double input = input0x1211f610();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x1211fa50() {
   double input = -0.145833;
   input += synapse0x1211fd90();
   input += synapse0x1206c7e0();
   input += synapse0x1206c820();
   input += synapse0x1211fee0();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x1211fa50() {
   double input = input0x1211fa50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x1211ff20() {
   double input = -0.351249;
   input += synapse0x12120260();
   input += synapse0x121202a0();
   input += synapse0x121202e0();
   input += synapse0x12120320();
   input += synapse0x12120360();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x1211ff20() {
   double input = input0x1211ff20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x121203a0() {
   double input = 0.586385;
   input += synapse0x121206e0();
   input += synapse0x12120720();
   input += synapse0x12120760();
   input += synapse0x121207a0();
   input += synapse0x121207e0();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x121203a0() {
   double input = input0x121203a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x12120820() {
   double input = 2.47511;
   input += synapse0x12120b60();
   input += synapse0x12120ba0();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x12120820() {
   double input = input0x12120820();
   return (input * 1)+0;
}

double MLP_Higgs_vs_zz_MU::synapse0x120f6e20() {
   return (neuron0x1211dbf0()*-0.523443);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211ecd0() {
   return (neuron0x1211df30()*0.255648);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211ed10() {
   return (neuron0x1211e270()*-0.455615);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211ed50() {
   return (neuron0x1211e5b0()*-0.238698);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211f0d0() {
   return (neuron0x1211dbf0()*-0.728591);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211f110() {
   return (neuron0x1211df30()*0.24254);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211f150() {
   return (neuron0x1211e270()*2.16838);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211f190() {
   return (neuron0x1211e5b0()*-0.279944);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211f510() {
   return (neuron0x1211dbf0()*-1.00481);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211f550() {
   return (neuron0x1211df30()*4.26733);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211f590() {
   return (neuron0x1211e270()*1.19086);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211f5d0() {
   return (neuron0x1211e5b0()*-4.67692);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211f950() {
   return (neuron0x1211dbf0()*-1.10769);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211f990() {
   return (neuron0x1211df30()*0.850296);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211f9d0() {
   return (neuron0x1211e270()*-0.193452);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211fa10() {
   return (neuron0x1211e5b0()*2.17292);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211fd90() {
   return (neuron0x1211dbf0()*0.524261);
}

double MLP_Higgs_vs_zz_MU::synapse0x1206c7e0() {
   return (neuron0x1211df30()*0.272782);
}

double MLP_Higgs_vs_zz_MU::synapse0x1206c820() {
   return (neuron0x1211e270()*-1.67238);
}

double MLP_Higgs_vs_zz_MU::synapse0x1211fee0() {
   return (neuron0x1211e5b0()*-0.652964);
}

double MLP_Higgs_vs_zz_MU::synapse0x12120260() {
   return (neuron0x1211ea20()*1.2637);
}

double MLP_Higgs_vs_zz_MU::synapse0x121202a0() {
   return (neuron0x1211ed90()*1.51489);
}

double MLP_Higgs_vs_zz_MU::synapse0x121202e0() {
   return (neuron0x1211f1d0()*-1.09318);
}

double MLP_Higgs_vs_zz_MU::synapse0x12120320() {
   return (neuron0x1211f610()*0.296953);
}

double MLP_Higgs_vs_zz_MU::synapse0x12120360() {
   return (neuron0x1211fa50()*-0.525676);
}

double MLP_Higgs_vs_zz_MU::synapse0x121206e0() {
   return (neuron0x1211ea20()*3.39393);
}

double MLP_Higgs_vs_zz_MU::synapse0x12120720() {
   return (neuron0x1211ed90()*-0.129004);
}

double MLP_Higgs_vs_zz_MU::synapse0x12120760() {
   return (neuron0x1211f1d0()*-2.72285);
}

double MLP_Higgs_vs_zz_MU::synapse0x121207a0() {
   return (neuron0x1211f610()*0.955466);
}

double MLP_Higgs_vs_zz_MU::synapse0x121207e0() {
   return (neuron0x1211fa50()*0.102591);
}

double MLP_Higgs_vs_zz_MU::synapse0x12120b60() {
   return (neuron0x1211ff20()*-1.2231);
}

double MLP_Higgs_vs_zz_MU::synapse0x12120ba0() {
   return (neuron0x121203a0()*-1.38455);
}

