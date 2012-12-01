#include "MLP_Higgs_vs_tt_MU.h"
#include <cmath>

double MLP_Higgs_vs_tt_MU::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.2104)/2.23892;
   input1 = (in1 - 24.5744)/1.37402;
   input2 = (in2 - 13.1737)/1.51773;
   switch(index) {
     case 0:
         return neuron0x16a40490();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_tt_MU::Value(int index, double* input) {
   input0 = (input[0] - 22.2104)/2.23892;
   input1 = (input[1] - 24.5744)/1.37402;
   input2 = (input[2] - 13.1737)/1.51773;
   switch(index) {
     case 0:
         return neuron0x16a40490();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_tt_MU::neuron0x16a2d630() {
   return input0;
}

double MLP_Higgs_vs_tt_MU::neuron0x16a2d970() {
   return input1;
}

double MLP_Higgs_vs_tt_MU::neuron0x16a3e8b0() {
   return input2;
}

double MLP_Higgs_vs_tt_MU::input0x16a3ec90() {
   double input = -0.0040373;
   input += synapse0x16a14320();
   input += synapse0x169f5d70();
   input += synapse0x16a3ef40();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0x16a3ec90() {
   double input = input0x16a3ec90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0x16a3ef80() {
   double input = 5.0467;
   input += synapse0x16a3f2c0();
   input += synapse0x16a3f300();
   input += synapse0x16a3f340();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0x16a3ef80() {
   double input = input0x16a3ef80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0x16a3f380() {
   double input = -1.11168;
   input += synapse0x16a3f6c0();
   input += synapse0x16a3f700();
   input += synapse0x16a3f740();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0x16a3f380() {
   double input = input0x16a3f380();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0x16a3f780() {
   double input = -0.671259;
   input += synapse0x16a3fac0();
   input += synapse0x16a3fb00();
   input += synapse0x16a3fb40();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0x16a3f780() {
   double input = input0x16a3f780();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0x16a3fb80() {
   double input = 2.78911;
   input += synapse0x16a3fec0();
   input += synapse0x16a3ff00();
   input += synapse0x16a3ff40();
   input += synapse0x16a3ff80();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0x16a3fb80() {
   double input = input0x16a3fb80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0x16a3ffc0() {
   double input = 3.75997;
   input += synapse0x16a40300();
   input += synapse0x169a3650();
   input += synapse0x169a3690();
   input += synapse0x16a40450();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0x16a3ffc0() {
   double input = input0x16a3ffc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_tt_MU::input0x16a40490() {
   double input = -0.682528;
   input += synapse0x16a406b0();
   input += synapse0x16a406f0();
   return input;
}

double MLP_Higgs_vs_tt_MU::neuron0x16a40490() {
   double input = input0x16a40490();
   return (input * 1)+0;
}

double MLP_Higgs_vs_tt_MU::synapse0x16a14320() {
   return (neuron0x16a2d630()*3.5232);
}

double MLP_Higgs_vs_tt_MU::synapse0x169f5d70() {
   return (neuron0x16a2d970()*0.52242);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3ef40() {
   return (neuron0x16a3e8b0()*-4.38437);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3f2c0() {
   return (neuron0x16a2d630()*3.15732);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3f300() {
   return (neuron0x16a2d970()*1.07087);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3f340() {
   return (neuron0x16a3e8b0()*0.906114);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3f6c0() {
   return (neuron0x16a2d630()*1.1377);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3f700() {
   return (neuron0x16a2d970()*-1.76228);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3f740() {
   return (neuron0x16a3e8b0()*-0.546545);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3fac0() {
   return (neuron0x16a2d630()*2.33704);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3fb00() {
   return (neuron0x16a2d970()*-1.15689);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3fb40() {
   return (neuron0x16a3e8b0()*0.0302528);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3fec0() {
   return (neuron0x16a3ec90()*0.879299);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3ff00() {
   return (neuron0x16a3ef80()*-0.401651);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3ff40() {
   return (neuron0x16a3f380()*-0.00196914);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a3ff80() {
   return (neuron0x16a3f780()*1.08402);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a40300() {
   return (neuron0x16a3ec90()*4.22072);
}

double MLP_Higgs_vs_tt_MU::synapse0x169a3650() {
   return (neuron0x16a3ef80()*-3.5587);
}

double MLP_Higgs_vs_tt_MU::synapse0x169a3690() {
   return (neuron0x16a3f380()*-3.48569);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a40450() {
   return (neuron0x16a3f780()*3.41753);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a406b0() {
   return (neuron0x16a3fb80()*-0.746437);
}

double MLP_Higgs_vs_tt_MU::synapse0x16a406f0() {
   return (neuron0x16a3ffc0()*2.42402);
}

