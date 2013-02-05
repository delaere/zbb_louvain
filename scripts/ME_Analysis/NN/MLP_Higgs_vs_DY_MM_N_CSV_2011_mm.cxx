#include "../NN/MLP_Higgs_vs_DY_MM_N_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.6041)/1.12509;
   input1 = (in1 - 20.2509)/0.989093;
   input2 = (in2 - 24.6395)/1.32045;
   input3 = (in3 - 13.3934)/1.61576;
   switch(index) {
     case 0:
         return neuron0xeace870();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 19.6041)/1.12509;
   input1 = (input[1] - 20.2509)/0.989093;
   input2 = (input[2] - 24.6395)/1.32045;
   input3 = (input[3] - 13.3934)/1.61576;
   switch(index) {
     case 0:
         return neuron0xeace870();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeacb870() {
   return input0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeacbb80() {
   return input1;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeacbe90() {
   return input2;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeacc1a0() {
   return input3;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0xeacc5f0() {
   double input = -1.37441;
   input += synapse0xea747c0();
   input += synapse0xeacc870();
   input += synapse0xeacc8b0();
   input += synapse0xeacc8f0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeacc5f0() {
   double input = input0xeacc5f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0xeacc930() {
   double input = -0.470811;
   input += synapse0xeaccc40();
   input += synapse0xeaccc80();
   input += synapse0xeacccc0();
   input += synapse0xeaccd00();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeacc930() {
   double input = input0xeacc930();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0xeaccd40() {
   double input = 3.60613;
   input += synapse0xeacd050();
   input += synapse0xeacd090();
   input += synapse0xeacd0d0();
   input += synapse0xeacd110();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeaccd40() {
   double input = input0xeaccd40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0xeacd150() {
   double input = 1.57923;
   input += synapse0xeacd460();
   input += synapse0xeacd4a0();
   input += synapse0xeacd4e0();
   input += synapse0xeacd520();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeacd150() {
   double input = input0xeacd150();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0xeacd560() {
   double input = 0.0989808;
   input += synapse0xeacd870();
   input += synapse0xea743c0();
   input += synapse0xe9d9d90();
   input += synapse0xe9d9dd0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeacd560() {
   double input = input0xeacd560();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0xeacd9c0() {
   double input = -0.3962;
   input += synapse0xeacdcd0();
   input += synapse0xeacdd10();
   input += synapse0xeacdd50();
   input += synapse0xeacdd90();
   input += synapse0xeacddd0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeacd9c0() {
   double input = input0xeacd9c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0xeacde10() {
   double input = -0.966663;
   input += synapse0xeace120();
   input += synapse0xeace160();
   input += synapse0xeace1a0();
   input += synapse0xeace1e0();
   input += synapse0xeace220();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeacde10() {
   double input = input0xeacde10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0xeace260() {
   double input = -2.59604;
   input += synapse0xeace5a0();
   input += synapse0xeace5e0();
   input += synapse0xeace620();
   input += synapse0xeaa6360();
   input += synapse0xead25a0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeace260() {
   double input = input0xeace260();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::input0xeace870() {
   double input = 1.68075;
   input += synapse0xeacebb0();
   input += synapse0xeacebf0();
   input += synapse0xeacec30();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::neuron0xeace870() {
   double input = input0xeace870();
   return (input * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xea747c0() {
   return (neuron0xeacb870()*-0.135444);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacc870() {
   return (neuron0xeacbb80()*1.20875);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacc8b0() {
   return (neuron0xeacbe90()*-0.915424);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacc8f0() {
   return (neuron0xeacc1a0()*-1.38715);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeaccc40() {
   return (neuron0xeacb870()*-1.09433);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeaccc80() {
   return (neuron0xeacbb80()*0.57787);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacccc0() {
   return (neuron0xeacbe90()*-1.06033);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeaccd00() {
   return (neuron0xeacc1a0()*1.44992);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacd050() {
   return (neuron0xeacb870()*1.26868);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacd090() {
   return (neuron0xeacbb80()*2.20242);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacd0d0() {
   return (neuron0xeacbe90()*-5.82213);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacd110() {
   return (neuron0xeacc1a0()*2.08463);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacd460() {
   return (neuron0xeacb870()*0.86101);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacd4a0() {
   return (neuron0xeacbb80()*2.81147);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacd4e0() {
   return (neuron0xeacbe90()*-5.75814);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacd520() {
   return (neuron0xeacc1a0()*2.48794);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacd870() {
   return (neuron0xeacb870()*-3.05086);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xea743c0() {
   return (neuron0xeacbb80()*5.41733);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xe9d9d90() {
   return (neuron0xeacbe90()*1.15855);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xe9d9dd0() {
   return (neuron0xeacc1a0()*-4.72041);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacdcd0() {
   return (neuron0xeacc5f0()*-4.7681);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacdd10() {
   return (neuron0xeacc930()*3.2446);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacdd50() {
   return (neuron0xeaccd40()*-3.69029);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacdd90() {
   return (neuron0xeacd150()*3.23202);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacddd0() {
   return (neuron0xeacd560()*1.6834);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeace120() {
   return (neuron0xeacc5f0()*1.42155);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeace160() {
   return (neuron0xeacc930()*-0.488722);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeace1a0() {
   return (neuron0xeaccd40()*1.52286);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeace1e0() {
   return (neuron0xeacd150()*-1.43334);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeace220() {
   return (neuron0xeacd560()*-0.418708);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeace5a0() {
   return (neuron0xeacc5f0()*3.19562);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeace5e0() {
   return (neuron0xeacc930()*6.59719);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeace620() {
   return (neuron0xeaccd40()*1.78283);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeaa6360() {
   return (neuron0xeacd150()*-2.38446);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xead25a0() {
   return (neuron0xeacd560()*5.59881);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacebb0() {
   return (neuron0xeacd9c0()*-2.00854);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacebf0() {
   return (neuron0xeacde10()*-3.07422);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_mm::synapse0xeacec30() {
   return (neuron0xeace260()*0.832799);
}

