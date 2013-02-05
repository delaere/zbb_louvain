#include "../NN/MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.496378)/0.335528;
   input1 = (in1 - 0.587486)/0.316279;
   input2 = (in2 - 0.428683)/0.350983;
   switch(index) {
     case 0:
         return neuron0x55b6130();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 0.496378)/0.335528;
   input1 = (input[1] - 0.587486)/0.316279;
   input2 = (input[2] - 0.428683)/0.350983;
   switch(index) {
     case 0:
         return neuron0x55b6130();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x533cff0() {
   return input0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x524f9a0() {
   return input1;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x524fcb0() {
   return input2;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x55b4720() {
   double input = 0.182161;
   input += synapse0x533cdb0();
   input += synapse0x49b2910();
   input += synapse0x46201e0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x55b4720() {
   double input = input0x55b4720();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x55b49a0() {
   double input = -0.728252;
   input += synapse0x55b4cb0();
   input += synapse0x55b4cf0();
   input += synapse0x55b4d30();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x55b49a0() {
   double input = input0x55b49a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x55b4d70() {
   double input = 1.91083;
   input += synapse0x55b5080();
   input += synapse0x55b50c0();
   input += synapse0x55b5100();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x55b4d70() {
   double input = input0x55b4d70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x55b5140() {
   double input = 1.8498;
   input += synapse0x55b5450();
   input += synapse0x55b5490();
   input += synapse0x55b54d0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x55b5140() {
   double input = input0x55b5140();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x55b5510() {
   double input = -2.53566;
   input += synapse0x55b5820();
   input += synapse0x55b5860();
   input += synapse0x55b58a0();
   input += synapse0x55b58e0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x55b5510() {
   double input = input0x55b5510();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x55b5920() {
   double input = 0.0763606;
   input += synapse0x55b5c30();
   input += synapse0x49b2990();
   input += synapse0x533d1e0();
   input += synapse0x5250100();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x55b5920() {
   double input = input0x55b5920();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x55b5d80() {
   double input = 0.0395502;
   input += synapse0x55b6030();
   input += synapse0x55b6070();
   input += synapse0x55b60b0();
   input += synapse0x55b60f0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x55b5d80() {
   double input = input0x55b5d80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::input0x55b6130() {
   double input = -2.5268;
   input += synapse0x55b6470();
   input += synapse0x55b64b0();
   input += synapse0x55b64f0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::neuron0x55b6130() {
   double input = input0x55b6130();
   return (input * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x533cdb0() {
   return (neuron0x533cff0()*1.72772);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x49b2910() {
   return (neuron0x524f9a0()*-1.58162);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x46201e0() {
   return (neuron0x524fcb0()*0.233846);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b4cb0() {
   return (neuron0x533cff0()*0.788171);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b4cf0() {
   return (neuron0x524f9a0()*-1.04494);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b4d30() {
   return (neuron0x524fcb0()*-0.821885);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b5080() {
   return (neuron0x533cff0()*-0.59964);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b50c0() {
   return (neuron0x524f9a0()*5.32919);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b5100() {
   return (neuron0x524fcb0()*1.22469);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b5450() {
   return (neuron0x533cff0()*0.567652);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b5490() {
   return (neuron0x524f9a0()*1.26804);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b54d0() {
   return (neuron0x524fcb0()*-0.660395);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b5820() {
   return (neuron0x55b4720()*2.94139);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b5860() {
   return (neuron0x55b49a0()*-3.80601);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b58a0() {
   return (neuron0x55b4d70()*-2.25455);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b58e0() {
   return (neuron0x55b5140()*5.35565);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b5c30() {
   return (neuron0x55b4720()*-2.72849);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x49b2990() {
   return (neuron0x55b49a0()*1.74473);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x533d1e0() {
   return (neuron0x55b4d70()*0.133765);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x5250100() {
   return (neuron0x55b5140()*-1.47603);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b6030() {
   return (neuron0x55b4720()*3.25491);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b6070() {
   return (neuron0x55b49a0()*0.323887);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b60b0() {
   return (neuron0x55b4d70()*2.51841);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b60f0() {
   return (neuron0x55b5140()*-2.60684);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b6470() {
   return (neuron0x55b5510()*2.09393);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b64b0() {
   return (neuron0x55b5920()*3.20464);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_mm::synapse0x55b64f0() {
   return (neuron0x55b5d80()*1.58054);
}

