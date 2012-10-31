#include "MLP_Higgs_vs_bkg_MU.h"
#include <cmath>

double MLP_Higgs_vs_bkg_MU::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.387839)/0.295659;
   input1 = (in1 - 1.00829)/0.054482;
   input2 = (in2 - 1.27601)/0.269311;
   switch(index) {
     case 0:
         return neuron0xbe46320();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_MU::Value(int index, double* input) {
   input0 = (input[0] - 0.387839)/0.295659;
   input1 = (input[1] - 1.00829)/0.054482;
   input2 = (input[2] - 1.27601)/0.269311;
   switch(index) {
     case 0:
         return neuron0xbe46320();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_MU::neuron0xbe334c0() {
   return input0;
}

double MLP_Higgs_vs_bkg_MU::neuron0xbe33800() {
   return input1;
}

double MLP_Higgs_vs_bkg_MU::neuron0xbe447d0() {
   return input2;
}

double MLP_Higgs_vs_bkg_MU::input0xbe44b20() {
   double input = -0.850348;
   input += synapse0xbdfbd10();
   input += synapse0xbe1a260();
   input += synapse0xbe44dd0();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xbe44b20() {
   double input = input0xbe44b20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xbe44e10() {
   double input = 1.22273;
   input += synapse0xbe45150();
   input += synapse0xbe45190();
   input += synapse0xbe451d0();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xbe44e10() {
   double input = input0xbe44e10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xbe45210() {
   double input = 0.847483;
   input += synapse0xbe45550();
   input += synapse0xbe45590();
   input += synapse0xbe455d0();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xbe45210() {
   double input = input0xbe45210();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xbe45610() {
   double input = 0.18467;
   input += synapse0xbe45950();
   input += synapse0xbe45990();
   input += synapse0xbe459d0();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xbe45610() {
   double input = input0xbe45610();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xbe45a10() {
   double input = -0.333344;
   input += synapse0xbe45d50();
   input += synapse0xbe45d90();
   input += synapse0xbe45dd0();
   input += synapse0xbe45e10();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xbe45a10() {
   double input = input0xbe45a10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xbe45e50() {
   double input = -1.29751;
   input += synapse0xbe46190();
   input += synapse0xbc20df0();
   input += synapse0xbc20e30();
   input += synapse0xbe462e0();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xbe45e50() {
   double input = input0xbe45e50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xbe46320() {
   double input = -0.370862;
   input += synapse0xbe46540();
   input += synapse0xbe46580();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xbe46320() {
   double input = input0xbe46320();
   return (input * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::synapse0xbdfbd10() {
   return (neuron0xbe334c0()*0.841371);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe1a260() {
   return (neuron0xbe33800()*-0.0478218);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe44dd0() {
   return (neuron0xbe447d0()*-0.899818);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe45150() {
   return (neuron0xbe334c0()*0.96203);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe45190() {
   return (neuron0xbe33800()*0.278344);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe451d0() {
   return (neuron0xbe447d0()*0.469051);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe45550() {
   return (neuron0xbe334c0()*-1.59739);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe45590() {
   return (neuron0xbe33800()*0.515265);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe455d0() {
   return (neuron0xbe447d0()*-0.345508);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe45950() {
   return (neuron0xbe334c0()*-0.229593);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe45990() {
   return (neuron0xbe33800()*-0.131975);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe459d0() {
   return (neuron0xbe447d0()*0.0893068);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe45d50() {
   return (neuron0xbe44b20()*-0.455112);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe45d90() {
   return (neuron0xbe44e10()*0.457998);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe45dd0() {
   return (neuron0xbe45210()*0.393809);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe45e10() {
   return (neuron0xbe45610()*-0.0714145);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe46190() {
   return (neuron0xbe44b20()*1.03326);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbc20df0() {
   return (neuron0xbe44e10()*0.940893);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbc20e30() {
   return (neuron0xbe45210()*-1.78763);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe462e0() {
   return (neuron0xbe45610()*-1.09366);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe46540() {
   return (neuron0xbe45a10()*0.543581);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbe46580() {
   return (neuron0xbe45e50()*2.52276);
}

