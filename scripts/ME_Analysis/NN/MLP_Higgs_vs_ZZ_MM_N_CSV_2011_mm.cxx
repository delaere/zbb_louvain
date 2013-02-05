#include "../NN/MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.2374)/1.32546;
   input1 = (in1 - 11.4634)/1.19767;
   input2 = (in2 - 24.6224)/1.19824;
   input3 = (in3 - 13.2101)/1.2793;
   switch(index) {
     case 0:
         return neuron0x1ef40b90();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 21.2374)/1.32546;
   input1 = (input[1] - 11.4634)/1.19767;
   input2 = (input[2] - 24.6224)/1.19824;
   input3 = (input[3] - 13.2101)/1.2793;
   switch(index) {
     case 0:
         return neuron0x1ef40b90();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef3db90() {
   return input0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef3dea0() {
   return input1;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef3e1b0() {
   return input2;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef3e4c0() {
   return input3;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1ef3e910() {
   double input = -1.93718;
   input += synapse0x1eee6ae0();
   input += synapse0x1ef3eb90();
   input += synapse0x1ef3ebd0();
   input += synapse0x1ef3ec10();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef3e910() {
   double input = input0x1ef3e910();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1ef3ec50() {
   double input = -1.97687;
   input += synapse0x1ef3ef60();
   input += synapse0x1ef3efa0();
   input += synapse0x1ef3efe0();
   input += synapse0x1ef3f020();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef3ec50() {
   double input = input0x1ef3ec50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1ef3f060() {
   double input = -2.60725;
   input += synapse0x1ef3f370();
   input += synapse0x1ef3f3b0();
   input += synapse0x1ef3f3f0();
   input += synapse0x1ef3f430();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef3f060() {
   double input = input0x1ef3f060();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1ef3f470() {
   double input = -2.57815;
   input += synapse0x1ef3f780();
   input += synapse0x1ef3f7c0();
   input += synapse0x1ef3f800();
   input += synapse0x1ef3f840();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef3f470() {
   double input = input0x1ef3f470();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1ef3f880() {
   double input = -1.82327;
   input += synapse0x1ef3fb90();
   input += synapse0x1eee66e0();
   input += synapse0x1ee7ceb0();
   input += synapse0x1ee7cef0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef3f880() {
   double input = input0x1ef3f880();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1ef3fce0() {
   double input = -5.41615;
   input += synapse0x1ef3fff0();
   input += synapse0x1ef40030();
   input += synapse0x1ef40070();
   input += synapse0x1ef400b0();
   input += synapse0x1ef400f0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef3fce0() {
   double input = input0x1ef3fce0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1ef40130() {
   double input = 0.919066;
   input += synapse0x1ef40440();
   input += synapse0x1ef40480();
   input += synapse0x1ef404c0();
   input += synapse0x1ef40500();
   input += synapse0x1ef40540();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef40130() {
   double input = input0x1ef40130();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1ef40580() {
   double input = -1.53609;
   input += synapse0x1ef408c0();
   input += synapse0x1ef40900();
   input += synapse0x1ef40940();
   input += synapse0x1ef18680();
   input += synapse0x1ef448c0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef40580() {
   double input = input0x1ef40580();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1ef40b90() {
   double input = 1.05464;
   input += synapse0x1ef40ed0();
   input += synapse0x1ef40f10();
   input += synapse0x1ef40f50();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1ef40b90() {
   double input = input0x1ef40b90();
   return (input * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1eee6ae0() {
   return (neuron0x1ef3db90()*-4.09945);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3eb90() {
   return (neuron0x1ef3dea0()*1.94803);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3ebd0() {
   return (neuron0x1ef3e1b0()*3.61359);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3ec10() {
   return (neuron0x1ef3e4c0()*3.23802);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3ef60() {
   return (neuron0x1ef3db90()*4.69346);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3efa0() {
   return (neuron0x1ef3dea0()*-0.110265);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3efe0() {
   return (neuron0x1ef3e1b0()*-3.48642);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3f020() {
   return (neuron0x1ef3e4c0()*0.67079);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3f370() {
   return (neuron0x1ef3db90()*1.25691);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3f3b0() {
   return (neuron0x1ef3dea0()*-2.80393);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3f3f0() {
   return (neuron0x1ef3e1b0()*0.344701);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3f430() {
   return (neuron0x1ef3e4c0()*0.808471);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3f780() {
   return (neuron0x1ef3db90()*-4.08881);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3f7c0() {
   return (neuron0x1ef3dea0()*5.55529);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3f800() {
   return (neuron0x1ef3e1b0()*2.28207);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3f840() {
   return (neuron0x1ef3e4c0()*-3.93678);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3fb90() {
   return (neuron0x1ef3db90()*-0.1782);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1eee66e0() {
   return (neuron0x1ef3dea0()*-1.11649);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ee7ceb0() {
   return (neuron0x1ef3e1b0()*-1.37351);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ee7cef0() {
   return (neuron0x1ef3e4c0()*5.14349);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef3fff0() {
   return (neuron0x1ef3e910()*2.2737);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef40030() {
   return (neuron0x1ef3ec50()*3.26452);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef40070() {
   return (neuron0x1ef3f060()*9.37003);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef400b0() {
   return (neuron0x1ef3f470()*-6.43176);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef400f0() {
   return (neuron0x1ef3f880()*-4.10664);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef40440() {
   return (neuron0x1ef3e910()*-1.01779);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef40480() {
   return (neuron0x1ef3ec50()*-5.80661);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef404c0() {
   return (neuron0x1ef3f060()*-3.24454);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef40500() {
   return (neuron0x1ef3f470()*2.2036);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef40540() {
   return (neuron0x1ef3f880()*2.44265);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef408c0() {
   return (neuron0x1ef3e910()*-0.0941511);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef40900() {
   return (neuron0x1ef3ec50()*-5.21201);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef40940() {
   return (neuron0x1ef3f060()*-5.88017);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef18680() {
   return (neuron0x1ef3f470()*8.8497);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef448c0() {
   return (neuron0x1ef3f880()*5.27414);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef40ed0() {
   return (neuron0x1ef3fce0()*-1.12744);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef40f10() {
   return (neuron0x1ef40130()*0.071161);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1ef40f50() {
   return (neuron0x1ef40580()*-1.12429);
}

