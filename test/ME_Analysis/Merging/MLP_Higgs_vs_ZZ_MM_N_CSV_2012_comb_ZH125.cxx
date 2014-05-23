#include "MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.106)/1.33958;
   input1 = (in1 - 10.8689)/1.14011;
   input2 = (in2 - 24.8784)/1.24273;
   input3 = (in3 - 13.4134)/1.45305;
   switch(index) {
     case 0:
         return neuron0x18228890();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::Value(int index, double* input) {
   input0 = (input[0] - 21.106)/1.33958;
   input1 = (input[1] - 10.8689)/1.14011;
   input2 = (input[2] - 24.8784)/1.24273;
   input3 = (input[3] - 13.4134)/1.45305;
   switch(index) {
     case 0:
         return neuron0x18228890();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x18225650() {
   return input0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x18225990() {
   return input1;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x18225cd0() {
   return input2;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x18226010() {
   return input3;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::input0x18226480() {
   double input = 5.61476;
   input += synapse0x181c69b0();
   input += synapse0x18226730();
   input += synapse0x18226770();
   input += synapse0x182267b0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x18226480() {
   double input = input0x18226480();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::input0x182267f0() {
   double input = -0.720812;
   input += synapse0x18226b30();
   input += synapse0x18226b70();
   input += synapse0x18226bb0();
   input += synapse0x18226bf0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x182267f0() {
   double input = input0x182267f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::input0x18226c30() {
   double input = -2.51343;
   input += synapse0x18226f70();
   input += synapse0x18226fb0();
   input += synapse0x18226ff0();
   input += synapse0x18227030();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x18226c30() {
   double input = input0x18226c30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::input0x18227070() {
   double input = 2.30628;
   input += synapse0x182273b0();
   input += synapse0x182273f0();
   input += synapse0x18227430();
   input += synapse0x18227470();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x18227070() {
   double input = input0x18227070();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::input0x182274b0() {
   double input = -1.56488;
   input += synapse0x182277f0();
   input += synapse0x181c6500();
   input += synapse0x181c6540();
   input += synapse0x18227940();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x182274b0() {
   double input = input0x182274b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::input0x18227980() {
   double input = 0.100976;
   input += synapse0x18227cc0();
   input += synapse0x18227d00();
   input += synapse0x18227d40();
   input += synapse0x18227d80();
   input += synapse0x18227dc0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x18227980() {
   double input = input0x18227980();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::input0x18227e00() {
   double input = 1.05798;
   input += synapse0x18228140();
   input += synapse0x18228180();
   input += synapse0x182281c0();
   input += synapse0x18228200();
   input += synapse0x18228240();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x18227e00() {
   double input = input0x18227e00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::input0x18228280() {
   double input = 0.0597526;
   input += synapse0x182285c0();
   input += synapse0x18228600();
   input += synapse0x18228640();
   input += synapse0x181c6960();
   input += synapse0x181e4ee0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x18228280() {
   double input = input0x18228280();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::input0x18228890() {
   double input = 1.16431;
   input += synapse0x181e4f20();
   input += synapse0x18228bd0();
   input += synapse0x18228c10();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::neuron0x18228890() {
   double input = input0x18228890();
   return (input * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x181c69b0() {
   return (neuron0x18225650()*-1.12351);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18226730() {
   return (neuron0x18225990()*3.68857);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18226770() {
   return (neuron0x18225cd0()*-3.7102);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x182267b0() {
   return (neuron0x18226010()*2.98245);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18226b30() {
   return (neuron0x18225650()*-1.79451);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18226b70() {
   return (neuron0x18225990()*1.15469);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18226bb0() {
   return (neuron0x18225cd0()*1.69448);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18226bf0() {
   return (neuron0x18226010()*-3.08304);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18226f70() {
   return (neuron0x18225650()*3.40203);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18226fb0() {
   return (neuron0x18225990()*-3.42345);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18226ff0() {
   return (neuron0x18225cd0()*-4.61451);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18227030() {
   return (neuron0x18226010()*-0.432005);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x182273b0() {
   return (neuron0x18225650()*-2.01132);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x182273f0() {
   return (neuron0x18225990()*0.603576);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18227430() {
   return (neuron0x18225cd0()*0.96674);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18227470() {
   return (neuron0x18226010()*0.295215);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x182277f0() {
   return (neuron0x18225650()*-0.98832);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x181c6500() {
   return (neuron0x18225990()*-0.313554);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x181c6540() {
   return (neuron0x18225cd0()*0.789237);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18227940() {
   return (neuron0x18226010()*0.258406);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18227cc0() {
   return (neuron0x18226480()*1.4741);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18227d00() {
   return (neuron0x182267f0()*-0.818274);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18227d40() {
   return (neuron0x18226c30()*-1.74792);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18227d80() {
   return (neuron0x18227070()*-0.292008);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18227dc0() {
   return (neuron0x182274b0()*-0.687658);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18228140() {
   return (neuron0x18226480()*0.787366);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18228180() {
   return (neuron0x182267f0()*-1.09482);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x182281c0() {
   return (neuron0x18226c30()*-2.03236);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18228200() {
   return (neuron0x18227070()*-0.91011);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18228240() {
   return (neuron0x182274b0()*-0.82236);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x182285c0() {
   return (neuron0x18226480()*-4.97061);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18228600() {
   return (neuron0x182267f0()*-3.88676);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18228640() {
   return (neuron0x18226c30()*1.35185);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x181c6960() {
   return (neuron0x18227070()*5.0167);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x181e4ee0() {
   return (neuron0x182274b0()*6.49009);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x181e4f20() {
   return (neuron0x18227980()*-1.34058);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18228bd0() {
   return (neuron0x18227e00()*1.12899);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125::synapse0x18228c10() {
   return (neuron0x18228280()*-0.929143);
}

