#include "MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500.h"
#include <cmath>

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.1454)/2.02206;
   input1 = (in1 - 25.1712)/2.09579;
   input2 = (in2 - 13.8698)/2.37204;
   switch(index) {
     case 0:
         return neuron0x5a24cf0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::Value(int index, double* input) {
   input0 = (input[0] - 22.1454)/2.02206;
   input1 = (input[1] - 25.1712)/2.09579;
   input2 = (input[2] - 13.8698)/2.37204;
   switch(index) {
     case 0:
         return neuron0x5a24cf0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a10900() {
   return input0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a10c40() {
   return input1;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a21b80() {
   return input2;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a21f60() {
   double input = -0.0588938;
   input += synapse0x59f75c0();
   input += synapse0x59d9080();
   input += synapse0x5a22210();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a21f60() {
   double input = input0x5a21f60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a22250() {
   double input = 2.79388;
   input += synapse0x5a22590();
   input += synapse0x5a225d0();
   input += synapse0x5a22610();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a22250() {
   double input = input0x5a22250();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a22650() {
   double input = -1.46534;
   input += synapse0x5a22990();
   input += synapse0x5a229d0();
   input += synapse0x5a22a10();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a22650() {
   double input = input0x5a22650();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a22a50() {
   double input = 0.521133;
   input += synapse0x5a22d90();
   input += synapse0x5a22dd0();
   input += synapse0x5a22e10();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a22a50() {
   double input = input0x5a22a50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a22e50() {
   double input = -0.310288;
   input += synapse0x5a23190();
   input += synapse0x5a231d0();
   input += synapse0x5a23210();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a22e50() {
   double input = input0x5a22e50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a23250() {
   double input = -0.704482;
   input += synapse0x5a23590();
   input += synapse0x5a235d0();
   input += synapse0x59d8bb0();
   input += synapse0x59d8bf0();
   input += synapse0x5a23720();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a23250() {
   double input = input0x5a23250();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a23760() {
   double input = 0.240326;
   input += synapse0x5a23aa0();
   input += synapse0x5a23ae0();
   input += synapse0x5a23b20();
   input += synapse0x5a23b60();
   input += synapse0x5a23ba0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a23760() {
   double input = input0x5a23760();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a23be0() {
   double input = -0.729438;
   input += synapse0x5a23f20();
   input += synapse0x5a23f60();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a23be0() {
   double input = input0x5a23be0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a23fa0() {
   double input = 1.18112;
   input += synapse0x5a242e0();
   input += synapse0x5a24320();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a23fa0() {
   double input = input0x5a23fa0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a24360() {
   double input = -1.11026;
   input += synapse0x5a246a0();
   input += synapse0x5a246e0();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a24360() {
   double input = input0x5a24360();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a24720() {
   double input = 0.850224;
   input += synapse0x5a24a60();
   input += synapse0x5a24aa0();
   input += synapse0x59f7540();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a24720() {
   double input = input0x5a24720();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::input0x5a24cf0() {
   double input = 6.06658;
   input += synapse0x59f7580();
   return input;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::neuron0x5a24cf0() {
   double input = input0x5a24cf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x59f75c0() {
   return (neuron0x5a10900()*-0.919716);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x59d9080() {
   return (neuron0x5a10c40()*0.453358);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a22210() {
   return (neuron0x5a21b80()*3.03902);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a22590() {
   return (neuron0x5a10900()*0.820969);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a225d0() {
   return (neuron0x5a10c40()*-2.13804);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a22610() {
   return (neuron0x5a21b80()*1.19974);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a22990() {
   return (neuron0x5a10900()*0.653192);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a229d0() {
   return (neuron0x5a10c40()*2.00153);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a22a10() {
   return (neuron0x5a21b80()*-3.6891);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a22d90() {
   return (neuron0x5a10900()*-1.11734);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a22dd0() {
   return (neuron0x5a10c40()*1.93581);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a22e10() {
   return (neuron0x5a21b80()*-2.11766);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a23190() {
   return (neuron0x5a10900()*0.484215);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a231d0() {
   return (neuron0x5a10c40()*-1.28345);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a23210() {
   return (neuron0x5a21b80()*2.10527);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a23590() {
   return (neuron0x5a21f60()*1.0904);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a235d0() {
   return (neuron0x5a22250()*2.85411);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x59d8bb0() {
   return (neuron0x5a22650()*0.641853);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x59d8bf0() {
   return (neuron0x5a22a50()*-2.27269);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a23720() {
   return (neuron0x5a22e50()*-3.01609);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a23aa0() {
   return (neuron0x5a21f60()*0.5849);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a23ae0() {
   return (neuron0x5a22250()*-0.644956);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a23b20() {
   return (neuron0x5a22650()*-0.732079);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a23b60() {
   return (neuron0x5a22a50()*0.925675);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a23ba0() {
   return (neuron0x5a22e50()*1.3573);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a23f20() {
   return (neuron0x5a23250()*2.76996);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a23f60() {
   return (neuron0x5a23760()*-0.771015);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a242e0() {
   return (neuron0x5a23250()*-3.91347);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a24320() {
   return (neuron0x5a23760()*1.16068);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a246a0() {
   return (neuron0x5a23250()*4.01207);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a246e0() {
   return (neuron0x5a23760()*-1.71203);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a24a60() {
   return (neuron0x5a23be0()*-3.03156);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x5a24aa0() {
   return (neuron0x5a23fa0()*5.16055);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x59f7540() {
   return (neuron0x5a24360()*-5.26779);
}

double MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500::synapse0x59f7580() {
   return (neuron0x5a24720()*-12.482);
}

