#include "MLP_Higgs_vs_zbb_MU.h"
#include <cmath>

double MLP_Higgs_vs_zbb_MU::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.7142)/1.09795;
   input1 = (in1 - 20.3278)/1.00331;
   input2 = (in2 - 24.9454)/1.56918;
   input3 = (in3 - 13.8299)/1.94115;
   switch(index) {
     case 0:
         return neuron0x1ab45060();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_zbb_MU::Value(int index, double* input) {
   input0 = (input[0] - 19.7142)/1.09795;
   input1 = (input[1] - 20.3278)/1.00331;
   input2 = (input[2] - 24.9454)/1.56918;
   input3 = (input[3] - 13.8299)/1.94115;
   switch(index) {
     case 0:
         return neuron0x1ab45060();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab42430() {
   return input0;
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab42770() {
   return input1;
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab42ab0() {
   return input2;
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab42df0() {
   return input3;
}

double MLP_Higgs_vs_zbb_MU::input0x1ab43260() {
   double input = 0.0857904;
   input += synapse0x1ab1b660();
   input += synapse0x1ab43510();
   input += synapse0x1ab43550();
   input += synapse0x1ab43590();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab43260() {
   double input = input0x1ab43260();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x1ab435d0() {
   double input = 0.0805814;
   input += synapse0x1ab43910();
   input += synapse0x1ab43950();
   input += synapse0x1ab43990();
   input += synapse0x1ab439d0();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab435d0() {
   double input = input0x1ab435d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x1ab43a10() {
   double input = -1.51409;
   input += synapse0x1ab43d50();
   input += synapse0x1ab43d90();
   input += synapse0x1ab43dd0();
   input += synapse0x1ab43e10();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab43a10() {
   double input = input0x1ab43a10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x1ab43e50() {
   double input = -0.75207;
   input += synapse0x1ab44190();
   input += synapse0x1ab441d0();
   input += synapse0x1ab44210();
   input += synapse0x1ab44250();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab43e50() {
   double input = input0x1ab43e50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x1ab44290() {
   double input = 0.684446;
   input += synapse0x1ab445d0();
   input += synapse0x1aa91050();
   input += synapse0x1aa91090();
   input += synapse0x1ab44720();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab44290() {
   double input = input0x1ab44290();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x1ab44760() {
   double input = 0.106551;
   input += synapse0x1ab44aa0();
   input += synapse0x1ab44ae0();
   input += synapse0x1ab44b20();
   input += synapse0x1ab44b60();
   input += synapse0x1ab44ba0();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab44760() {
   double input = input0x1ab44760();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x1ab44be0() {
   double input = -0.0199043;
   input += synapse0x1ab44f20();
   input += synapse0x1ab44f60();
   input += synapse0x1ab44fa0();
   input += synapse0x1ab44fe0();
   input += synapse0x1ab45020();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab44be0() {
   double input = input0x1ab44be0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x1ab45060() {
   double input = 0.122216;
   input += synapse0x1ab453a0();
   input += synapse0x1ab453e0();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x1ab45060() {
   double input = input0x1ab45060();
   return (input * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab1b660() {
   return (neuron0x1ab42430()*-2.60752);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab43510() {
   return (neuron0x1ab42770()*-0.664165);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab43550() {
   return (neuron0x1ab42ab0()*3.0775);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab43590() {
   return (neuron0x1ab42df0()*0.588573);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab43910() {
   return (neuron0x1ab42430()*0.212515);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab43950() {
   return (neuron0x1ab42770()*0.735305);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab43990() {
   return (neuron0x1ab42ab0()*-0.425547);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab439d0() {
   return (neuron0x1ab42df0()*-0.253628);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab43d50() {
   return (neuron0x1ab42430()*1.44817);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab43d90() {
   return (neuron0x1ab42770()*-0.118141);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab43dd0() {
   return (neuron0x1ab42ab0()*0.065663);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab43e10() {
   return (neuron0x1ab42df0()*-3.26893);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44190() {
   return (neuron0x1ab42430()*0.259171);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab441d0() {
   return (neuron0x1ab42770()*-0.712255);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44210() {
   return (neuron0x1ab42ab0()*-0.434542);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44250() {
   return (neuron0x1ab42df0()*-1.63135);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab445d0() {
   return (neuron0x1ab42430()*-0.594297);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1aa91050() {
   return (neuron0x1ab42770()*0.978047);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1aa91090() {
   return (neuron0x1ab42ab0()*0.809443);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44720() {
   return (neuron0x1ab42df0()*-0.141989);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44aa0() {
   return (neuron0x1ab43260()*-0.525197);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44ae0() {
   return (neuron0x1ab435d0()*-2.31117);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44b20() {
   return (neuron0x1ab43a10()*-2.09484);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44b60() {
   return (neuron0x1ab43e50()*0.541744);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44ba0() {
   return (neuron0x1ab44290()*1.25495);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44f20() {
   return (neuron0x1ab43260()*1.38172);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44f60() {
   return (neuron0x1ab435d0()*0.54387);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44fa0() {
   return (neuron0x1ab43a10()*1.90481);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab44fe0() {
   return (neuron0x1ab43e50()*-0.110079);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab45020() {
   return (neuron0x1ab44290()*-1.55097);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab453a0() {
   return (neuron0x1ab44760()*-1.77713);
}

double MLP_Higgs_vs_zbb_MU::synapse0x1ab453e0() {
   return (neuron0x1ab44be0()*1.31865);
}

