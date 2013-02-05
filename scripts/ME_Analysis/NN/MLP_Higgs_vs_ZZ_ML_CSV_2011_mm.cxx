#include "../NN/MLP_Higgs_vs_ZZ_ML_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.3169)/1.39482;
   input1 = (in1 - 11.5405)/1.26362;
   input2 = (in2 - 24.8477)/1.30714;
   input3 = (in3 - 13.5521)/1.53844;
   switch(index) {
     case 0:
         return neuron0x215d9650();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 21.3169)/1.39482;
   input1 = (input[1] - 11.5405)/1.26362;
   input2 = (input[2] - 24.8477)/1.30714;
   input3 = (input[3] - 13.5521)/1.53844;
   switch(index) {
     case 0:
         return neuron0x215d9650();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x21968b50() {
   return input0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x2167e4b0() {
   return input1;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x2167e7c0() {
   return input2;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x2167ead0() {
   return input3;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::input0x215defe0() {
   double input = 2.0341;
   input += synapse0x21966050();
   input += synapse0x215df260();
   input += synapse0x215df2a0();
   input += synapse0x215df2e0();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x215defe0() {
   double input = input0x215defe0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::input0x215df320() {
   double input = 1.3963;
   input += synapse0x215df630();
   input += synapse0x215df670();
   input += synapse0x215df6b0();
   input += synapse0x215df6f0();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x215df320() {
   double input = input0x215df320();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::input0x215df730() {
   double input = 5.57804;
   input += synapse0x215dfa40();
   input += synapse0x215dfa80();
   input += synapse0x215dfac0();
   input += synapse0x215dfb00();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x215df730() {
   double input = input0x215df730();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::input0x215d7f60() {
   double input = -1.91764;
   input += synapse0x215d8270();
   input += synapse0x215d82b0();
   input += synapse0x215d82f0();
   input += synapse0x215d8330();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x215d7f60() {
   double input = input0x215d7f60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::input0x215d8370() {
   double input = -2.53737;
   input += synapse0x215d8680();
   input += synapse0x21968e60();
   input += synapse0x21965c80();
   input += synapse0x219ae390();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x215d8370() {
   double input = input0x215d8370();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::input0x215d87d0() {
   double input = -2.14001;
   input += synapse0x215d8ae0();
   input += synapse0x215d8b20();
   input += synapse0x215d8b60();
   input += synapse0x215d8ba0();
   input += synapse0x215d8be0();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x215d87d0() {
   double input = input0x215d87d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::input0x215d8c20() {
   double input = -9.27329;
   input += synapse0x215d8f30();
   input += synapse0x215d8f70();
   input += synapse0x215d8fb0();
   input += synapse0x215d8ff0();
   input += synapse0x215d9030();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x215d8c20() {
   double input = input0x215d8c20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::input0x215d9070() {
   double input = -7.19197;
   input += synapse0x215d9380();
   input += synapse0x215d93c0();
   input += synapse0x215d9400();
   input += synapse0x219ae3d0();
   input += synapse0x219680d0();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x215d9070() {
   double input = input0x215d9070();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::input0x215d9650() {
   double input = 0.0017477;
   input += synapse0x215d9990();
   input += synapse0x215d99d0();
   input += synapse0x215d9a10();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::neuron0x215d9650() {
   double input = input0x215d9650();
   return (input * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x21966050() {
   return (neuron0x21968b50()*4.40906);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215df260() {
   return (neuron0x2167e4b0()*-4.83372);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215df2a0() {
   return (neuron0x2167e7c0()*-1.80565);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215df2e0() {
   return (neuron0x2167ead0()*1.90595);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215df630() {
   return (neuron0x21968b50()*-3.1647);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215df670() {
   return (neuron0x2167e4b0()*5.45242);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215df6b0() {
   return (neuron0x2167e7c0()*1.03581);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215df6f0() {
   return (neuron0x2167ead0()*-2.99846);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215dfa40() {
   return (neuron0x21968b50()*2.43403);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215dfa80() {
   return (neuron0x2167e4b0()*1.78483);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215dfac0() {
   return (neuron0x2167e7c0()*-5.61687);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215dfb00() {
   return (neuron0x2167ead0()*0.24457);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8270() {
   return (neuron0x21968b50()*1.07354);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d82b0() {
   return (neuron0x2167e4b0()*-2.15627);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d82f0() {
   return (neuron0x2167e7c0()*-0.376886);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8330() {
   return (neuron0x2167ead0()*-0.445528);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8680() {
   return (neuron0x21968b50()*5.45311);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x21968e60() {
   return (neuron0x2167e4b0()*-2.73717);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x21965c80() {
   return (neuron0x2167e7c0()*-3.26971);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x219ae390() {
   return (neuron0x2167ead0()*1.72396);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8ae0() {
   return (neuron0x215defe0()*0.650501);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8b20() {
   return (neuron0x215df320()*-8.11607);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8b60() {
   return (neuron0x215df730()*-6.97413);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8ba0() {
   return (neuron0x215d7f60()*9.47468);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8be0() {
   return (neuron0x215d8370()*6.26955);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8f30() {
   return (neuron0x215defe0()*8.10738);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8f70() {
   return (neuron0x215df320()*5.99463);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8fb0() {
   return (neuron0x215df730()*-3.92173);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d8ff0() {
   return (neuron0x215d7f60()*9.69086);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d9030() {
   return (neuron0x215d8370()*8.33261);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d9380() {
   return (neuron0x215defe0()*-1.87932);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d93c0() {
   return (neuron0x215df320()*-3.47861);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d9400() {
   return (neuron0x215df730()*4.49117);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x219ae3d0() {
   return (neuron0x215d7f60()*-4.5676);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x219680d0() {
   return (neuron0x215d8370()*4.1146);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d9990() {
   return (neuron0x215d87d0()*-0.985359);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d99d0() {
   return (neuron0x215d8c20()*0.995916);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011_mm::synapse0x215d9a10() {
   return (neuron0x215d9070()*-3.13125);
}

