#include "MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3,double in4) {
   input0 = (in0 - 22.1385)/2.5002;
   input1 = (in1 - 21.3492)/1.92682;
   input2 = (in2 - 10.929)/1.53598;
   input3 = (in3 - 10.1565)/34.0949;
   input4 = (in4 - 1.77307)/0.814378;
   switch(index) {
     case 0:
         return neuron0x346a9400();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 22.1385)/2.5002;
   input1 = (input[1] - 21.3492)/1.92682;
   input2 = (input[2] - 10.929)/1.53598;
   input3 = (input[3] - 10.1565)/34.0949;
   input4 = (input[4] - 1.77307)/0.814378;
   switch(index) {
     case 0:
         return neuron0x346a9400();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x346a6e60() {
   return input0;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x346a7110() {
   return input1;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x346a7450() {
   return input2;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x346a7790() {
   return input3;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x346a7ad0() {
   return input4;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x346a7f40() {
   double input = -0.459377;
   input += synapse0x346677e0();
   input += synapse0x3460eb60();
   input += synapse0x346962d0();
   input += synapse0x346a81f0();
   input += synapse0x346a8230();
   return input;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x346a7f40() {
   double input = input0x346a7f40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x346a8270() {
   double input = -2.89946;
   input += synapse0x346a85b0();
   input += synapse0x346a85f0();
   input += synapse0x346a8630();
   input += synapse0x346a8670();
   input += synapse0x346a86b0();
   return input;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x346a8270() {
   double input = input0x346a8270();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x346a86f0() {
   double input = 5.20711;
   input += synapse0x346a8a30();
   input += synapse0x346a8a70();
   input += synapse0x346a8ab0();
   input += synapse0x346a8af0();
   input += synapse0x346a8b30();
   return input;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x346a86f0() {
   double input = input0x346a86f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x346a8b70() {
   double input = -2.06274;
   input += synapse0x346a8eb0();
   input += synapse0x346a8ef0();
   input += synapse0x3460e6a0();
   return input;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x346a8b70() {
   double input = input0x346a8b70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x346a9040() {
   double input = 4.31137;
   input += synapse0x3460e6e0();
   input += synapse0x346a9380();
   input += synapse0x346a93c0();
   return input;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x346a9040() {
   double input = input0x346a9040();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x346a9400() {
   double input = 0.627507;
   input += synapse0x346a9620();
   input += synapse0x346a9660();
   return input;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x346a9400() {
   double input = input0x346a9400();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346677e0() {
   return (neuron0x346a6e60()*1.96967);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3460eb60() {
   return (neuron0x346a7110()*0.274329);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346962d0() {
   return (neuron0x346a7450()*-1.90656);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a81f0() {
   return (neuron0x346a7790()*-0.0151211);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a8230() {
   return (neuron0x346a7ad0()*0.0775719);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a85b0() {
   return (neuron0x346a6e60()*-0.0906499);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a85f0() {
   return (neuron0x346a7110()*0.020969);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a8630() {
   return (neuron0x346a7450()*2.33168);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a8670() {
   return (neuron0x346a7790()*0.024352);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a86b0() {
   return (neuron0x346a7ad0()*-0.0900179);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a8a30() {
   return (neuron0x346a6e60()*1.46146);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a8a70() {
   return (neuron0x346a7110()*-3.23227);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a8ab0() {
   return (neuron0x346a7450()*-0.963121);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a8af0() {
   return (neuron0x346a7790()*-0.00474405);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a8b30() {
   return (neuron0x346a7ad0()*0.0489739);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a8eb0() {
   return (neuron0x346a7f40()*1.69497);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a8ef0() {
   return (neuron0x346a8270()*1.19567);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3460e6a0() {
   return (neuron0x346a86f0()*2.40614);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3460e6e0() {
   return (neuron0x346a7f40()*-3.1946);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a9380() {
   return (neuron0x346a8270()*-3.87097);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a93c0() {
   return (neuron0x346a86f0()*-3.37775);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a9620() {
   return (neuron0x346a8b70()*4.10422);
}

double MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x346a9660() {
   return (neuron0x346a9040()*-9.32061);
}

