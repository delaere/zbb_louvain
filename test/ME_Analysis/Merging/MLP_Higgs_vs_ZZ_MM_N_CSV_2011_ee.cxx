#include "MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.2702)/1.27149;
   input1 = (in1 - 11.1467)/1.07286;
   input2 = (in2 - 24.5933)/1.16134;
   input3 = (in3 - 13.1535)/1.27098;
   switch(index) {
     case 0:
         return neuron0x1e3c9f80();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::Value(int index, double* input) {
   input0 = (input[0] - 21.2702)/1.27149;
   input1 = (input[1] - 11.1467)/1.07286;
   input2 = (input[2] - 24.5933)/1.16134;
   input3 = (input[3] - 13.1535)/1.27098;
   switch(index) {
     case 0:
         return neuron0x1e3c9f80();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c6d40() {
   return input0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c7080() {
   return input1;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c73c0() {
   return input2;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c7700() {
   return input3;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::input0x1e3c7b70() {
   double input = 2.28034;
   input += synapse0x1e39ff70();
   input += synapse0x1e3c7e20();
   input += synapse0x1e3c7e60();
   input += synapse0x1e3c7ea0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c7b70() {
   double input = input0x1e3c7b70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::input0x1e3c7ee0() {
   double input = -2.20416;
   input += synapse0x1e3c8220();
   input += synapse0x1e3c8260();
   input += synapse0x1e3c82a0();
   input += synapse0x1e3c82e0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c7ee0() {
   double input = input0x1e3c7ee0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::input0x1e3c8320() {
   double input = 6.25859;
   input += synapse0x1e3c8660();
   input += synapse0x1e3c86a0();
   input += synapse0x1e3c86e0();
   input += synapse0x1e3c8720();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c8320() {
   double input = input0x1e3c8320();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::input0x1e3c8760() {
   double input = 0.613592;
   input += synapse0x1e3c8aa0();
   input += synapse0x1e3c8ae0();
   input += synapse0x1e3c8b20();
   input += synapse0x1e3c8b60();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c8760() {
   double input = input0x1e3c8760();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::input0x1e3c8ba0() {
   double input = 0.513199;
   input += synapse0x1e3c8ee0();
   input += synapse0x1e142570();
   input += synapse0x1e1425b0();
   input += synapse0x1e3c9030();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c8ba0() {
   double input = input0x1e3c8ba0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::input0x1e3c9070() {
   double input = 2.39156;
   input += synapse0x1e3c93b0();
   input += synapse0x1e3c93f0();
   input += synapse0x1e3c9430();
   input += synapse0x1e3c9470();
   input += synapse0x1e3c94b0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c9070() {
   double input = input0x1e3c9070();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::input0x1e3c94f0() {
   double input = -4.09811;
   input += synapse0x1e3c9830();
   input += synapse0x1e3c9870();
   input += synapse0x1e3c98b0();
   input += synapse0x1e3c98f0();
   input += synapse0x1e3c9930();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c94f0() {
   double input = input0x1e3c94f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::input0x1e3c9970() {
   double input = 3.63011;
   input += synapse0x1e3c9cb0();
   input += synapse0x1e3c9cf0();
   input += synapse0x1e3c9d30();
   input += synapse0x1e368050();
   input += synapse0x1e39ffb0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c9970() {
   double input = input0x1e3c9970();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::input0x1e3c9f80() {
   double input = -0.803802;
   input += synapse0x1e3ca2c0();
   input += synapse0x1e3ca300();
   input += synapse0x1e3ca340();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::neuron0x1e3c9f80() {
   double input = input0x1e3c9f80();
   return (input * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e39ff70() {
   return (neuron0x1e3c6d40()*-2.54773);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c7e20() {
   return (neuron0x1e3c7080()*2.03125);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c7e60() {
   return (neuron0x1e3c73c0()*-0.753851);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c7ea0() {
   return (neuron0x1e3c7700()*0.44019);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c8220() {
   return (neuron0x1e3c6d40()*1.76049);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c8260() {
   return (neuron0x1e3c7080()*-1.42016);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c82a0() {
   return (neuron0x1e3c73c0()*0.100899);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c82e0() {
   return (neuron0x1e3c7700()*0.13797);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c8660() {
   return (neuron0x1e3c6d40()*3.41112);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c86a0() {
   return (neuron0x1e3c7080()*2.26111);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c86e0() {
   return (neuron0x1e3c73c0()*-1.29493);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c8720() {
   return (neuron0x1e3c7700()*-3.89899);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c8aa0() {
   return (neuron0x1e3c6d40()*1.76963);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c8ae0() {
   return (neuron0x1e3c7080()*5.26031);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c8b20() {
   return (neuron0x1e3c73c0()*0.233731);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c8b60() {
   return (neuron0x1e3c7700()*-5.53268);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c8ee0() {
   return (neuron0x1e3c6d40()*1.87574);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e142570() {
   return (neuron0x1e3c7080()*-2.1582);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e1425b0() {
   return (neuron0x1e3c73c0()*0.175935);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c9030() {
   return (neuron0x1e3c7700()*1.43266);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c93b0() {
   return (neuron0x1e3c7b70()*-0.400434);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c93f0() {
   return (neuron0x1e3c7ee0()*3.1789);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c9430() {
   return (neuron0x1e3c8320()*-1.05519);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c9470() {
   return (neuron0x1e3c8760()*0.0498873);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c94b0() {
   return (neuron0x1e3c8ba0()*-0.347655);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c9830() {
   return (neuron0x1e3c7b70()*-1.70448);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c9870() {
   return (neuron0x1e3c7ee0()*-4.41881);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c98b0() {
   return (neuron0x1e3c8320()*1.58817);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c98f0() {
   return (neuron0x1e3c8760()*-0.728119);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c9930() {
   return (neuron0x1e3c8ba0()*3.65151);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c9cb0() {
   return (neuron0x1e3c7b70()*-2.2228);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c9cf0() {
   return (neuron0x1e3c7ee0()*1.43003);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3c9d30() {
   return (neuron0x1e3c8320()*-3.43507);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e368050() {
   return (neuron0x1e3c8760()*-14.5997);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e39ffb0() {
   return (neuron0x1e3c8ba0()*-0.621319);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3ca2c0() {
   return (neuron0x1e3c9070()*2.33199);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3ca300() {
   return (neuron0x1e3c94f0()*-3.43491);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_ee::synapse0x1e3ca340() {
   return (neuron0x1e3c9970()*-1.30796);
}

