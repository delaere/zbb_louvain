#include "../NN/MLP_Higgs_vs_TT_MM_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 21.8741)/1.13258;
   input1 = (in1 - 25.9969)/1.81838;
   input2 = (in2 - 14.958)/2.28932;
   switch(index) {
     case 0:
         return neuron0x1ac4ecc0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 21.8741)/1.13258;
   input1 = (input[1] - 25.9969)/1.81838;
   input2 = (input[2] - 14.958)/2.28932;
   switch(index) {
     case 0:
         return neuron0x1ac4ecc0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x19dbb3c0() {
   return input0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x19dbb6d0() {
   return input1;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4ba50() {
   return input2;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4bea0() {
   double input = 1.12881;
   input += synapse0x19d9aa90();
   input += synapse0x1ad404c0();
   input += synapse0x19d9ab20();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4bea0() {
   double input = input0x1ac4bea0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4c120() {
   double input = 11.6051;
   input += synapse0x1ac4c430();
   input += synapse0x1ac4c470();
   input += synapse0x1ac4c4b0();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4c120() {
   double input = input0x1ac4c120();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4c4f0() {
   double input = 2.89708;
   input += synapse0x1ac4c800();
   input += synapse0x1ac4c840();
   input += synapse0x1ac4c880();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4c4f0() {
   double input = input0x1ac4c4f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4c8c0() {
   double input = 0.286249;
   input += synapse0x1ac4cbd0();
   input += synapse0x1ac4cc10();
   input += synapse0x1ac4cc50();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4c8c0() {
   double input = input0x1ac4c8c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4cc90() {
   double input = 0.887004;
   input += synapse0x1ac4cfa0();
   input += synapse0x1ac4cfe0();
   input += synapse0x1ac4d020();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4cc90() {
   double input = input0x1ac4cc90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4d060() {
   double input = 1.93577;
   input += synapse0x1ac4d3a0();
   input += synapse0x1ac4d3e0();
   input += synapse0x19de8020();
   input += synapse0x19de8060();
   input += synapse0x19dbb9e0();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4d060() {
   double input = input0x1ac4d060();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4d530() {
   double input = -0.887841;
   input += synapse0x1ac4d870();
   input += synapse0x1ac4d8b0();
   input += synapse0x1ac4d8f0();
   input += synapse0x1ac4d930();
   input += synapse0x1ac4d970();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4d530() {
   double input = input0x1ac4d530();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4d9b0() {
   double input = -2.54944;
   input += synapse0x1ac4dcf0();
   input += synapse0x1ac4dd30();
   input += synapse0x1ac4dd70();
   input += synapse0x1ac4ddb0();
   input += synapse0x1ac4ddf0();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4d9b0() {
   double input = input0x1ac4d9b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4de30() {
   double input = 0.444494;
   input += synapse0x1ac4e170();
   input += synapse0x1ac4e1b0();
   input += synapse0x1ac4e1f0();
   input += synapse0x19d2f7c0();
   input += synapse0x19563160();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4de30() {
   double input = input0x1ac4de30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4e440() {
   double input = -0.470204;
   input += synapse0x1ac4e780();
   input += synapse0x1ac4e7c0();
   input += synapse0x1ac4e800();
   input += synapse0x1ac4e840();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4e440() {
   double input = input0x1ac4e440();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4e880() {
   double input = 4.11601;
   input += synapse0x1ac4ebc0();
   input += synapse0x1ac4ec00();
   input += synapse0x1ac4ec40();
   input += synapse0x1ac4ec80();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4e880() {
   double input = input0x1ac4e880();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::input0x1ac4ecc0() {
   double input = 1.48914;
   input += synapse0x1ac4f000();
   input += synapse0x1ac4f040();
   return input;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::neuron0x1ac4ecc0() {
   double input = input0x1ac4ecc0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x19d9aa90() {
   return (neuron0x19dbb3c0()*1.29074);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ad404c0() {
   return (neuron0x19dbb6d0()*4.67015);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x19d9ab20() {
   return (neuron0x1ac4ba50()*-10.3784);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4c430() {
   return (neuron0x19dbb3c0()*5.783);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4c470() {
   return (neuron0x19dbb6d0()*2.25517);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4c4b0() {
   return (neuron0x1ac4ba50()*-0.939441);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4c800() {
   return (neuron0x19dbb3c0()*1.69542);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4c840() {
   return (neuron0x19dbb6d0()*-5.88748);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4c880() {
   return (neuron0x1ac4ba50()*1.65761);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4cbd0() {
   return (neuron0x19dbb3c0()*1.36873);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4cc10() {
   return (neuron0x19dbb6d0()*0.59933);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4cc50() {
   return (neuron0x1ac4ba50()*-3.43088);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4cfa0() {
   return (neuron0x19dbb3c0()*-1.74434);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4cfe0() {
   return (neuron0x19dbb6d0()*-1.89095);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4d020() {
   return (neuron0x1ac4ba50()*6.79577);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4d3a0() {
   return (neuron0x1ac4bea0()*-1.45178);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4d3e0() {
   return (neuron0x1ac4c120()*1.99472);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x19de8020() {
   return (neuron0x1ac4c4f0()*-0.353229);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x19de8060() {
   return (neuron0x1ac4c8c0()*-2.22592);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x19dbb9e0() {
   return (neuron0x1ac4cc90()*1.05912);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4d870() {
   return (neuron0x1ac4bea0()*1.99767);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4d8b0() {
   return (neuron0x1ac4c120()*0.418491);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4d8f0() {
   return (neuron0x1ac4c4f0()*-1.10187);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4d930() {
   return (neuron0x1ac4c8c0()*-2.01763);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4d970() {
   return (neuron0x1ac4cc90()*-2.2737);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4dcf0() {
   return (neuron0x1ac4bea0()*6.2995);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4dd30() {
   return (neuron0x1ac4c120()*5.80603);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4dd70() {
   return (neuron0x1ac4c4f0()*-5.72386);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4ddb0() {
   return (neuron0x1ac4c8c0()*-4.15693);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4ddf0() {
   return (neuron0x1ac4cc90()*3.55238);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4e170() {
   return (neuron0x1ac4bea0()*-0.121965);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4e1b0() {
   return (neuron0x1ac4c120()*-1.15235);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4e1f0() {
   return (neuron0x1ac4c4f0()*0.220818);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x19d2f7c0() {
   return (neuron0x1ac4c8c0()*-0.934296);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x19563160() {
   return (neuron0x1ac4cc90()*-0.688172);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4e780() {
   return (neuron0x1ac4d060()*2.10435);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4e7c0() {
   return (neuron0x1ac4d530()*1.80991);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4e800() {
   return (neuron0x1ac4d9b0()*-1.03342);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4e840() {
   return (neuron0x1ac4de30()*2.09143);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4ebc0() {
   return (neuron0x1ac4d060()*-0.487992);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4ec00() {
   return (neuron0x1ac4d530()*-0.555121);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4ec40() {
   return (neuron0x1ac4d9b0()*-6.53267);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4ec80() {
   return (neuron0x1ac4de30()*0.0547668);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4f000() {
   return (neuron0x1ac4e440()*-2.06014);
}

double MLP_Higgs_vs_TT_MM_CSV_2011_mm::synapse0x1ac4f040() {
   return (neuron0x1ac4e880()*1.23967);
}

