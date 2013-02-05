#include "../NN/MLP_Higgs_vs_ZZ_MM_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_MM_CSV_2011::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.3188)/1.30222;
   input1 = (in1 - 11.1967)/1.1103;
   input2 = (in2 - 24.6463)/1.20041;
   input3 = (in3 - 13.207)/1.30868;
   switch(index) {
     case 0:
         return neuron0x6485a10();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 21.3188)/1.30222;
   input1 = (input[1] - 11.1967)/1.1103;
   input2 = (input[2] - 24.6463)/1.20041;
   input3 = (input[3] - 13.207)/1.30868;
   switch(index) {
     case 0:
         return neuron0x6485a10();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6482a10() {
   return input0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6482d20() {
   return input1;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6483030() {
   return input2;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6483340() {
   return input3;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::input0x6483790() {
   double input = -2.93517;
   input += synapse0x642b960();
   input += synapse0x6483a10();
   input += synapse0x6483a50();
   input += synapse0x6483a90();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6483790() {
   double input = input0x6483790();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::input0x6483ad0() {
   double input = -7.83954;
   input += synapse0x6483de0();
   input += synapse0x6483e20();
   input += synapse0x6483e60();
   input += synapse0x6483ea0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6483ad0() {
   double input = input0x6483ad0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::input0x6483ee0() {
   double input = 1.15082;
   input += synapse0x64841f0();
   input += synapse0x6484230();
   input += synapse0x6484270();
   input += synapse0x64842b0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6483ee0() {
   double input = input0x6483ee0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::input0x64842f0() {
   double input = 4.03833;
   input += synapse0x6484600();
   input += synapse0x6484640();
   input += synapse0x6484680();
   input += synapse0x64846c0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x64842f0() {
   double input = input0x64842f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::input0x6484700() {
   double input = -2.64442;
   input += synapse0x6484a10();
   input += synapse0x642b560();
   input += synapse0x61c7f60();
   input += synapse0x61c7fa0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6484700() {
   double input = input0x6484700();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::input0x6484b60() {
   double input = 2.82051;
   input += synapse0x6484e70();
   input += synapse0x6484eb0();
   input += synapse0x6484ef0();
   input += synapse0x6484f30();
   input += synapse0x6484f70();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6484b60() {
   double input = input0x6484b60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::input0x6484fb0() {
   double input = -2.7525;
   input += synapse0x64852c0();
   input += synapse0x6485300();
   input += synapse0x6485340();
   input += synapse0x6485380();
   input += synapse0x64853c0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6484fb0() {
   double input = input0x6484fb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::input0x6485400() {
   double input = 0.199429;
   input += synapse0x6485740();
   input += synapse0x6485780();
   input += synapse0x64857c0();
   input += synapse0x64461c0();
   input += synapse0x6489710();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6485400() {
   double input = input0x6485400();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::input0x6485a10() {
   double input = -1.91076;
   input += synapse0x6485d50();
   input += synapse0x6485d90();
   input += synapse0x6485dd0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::neuron0x6485a10() {
   double input = input0x6485a10();
   return (input * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x642b960() {
   return (neuron0x6482a10()*0.414481);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6483a10() {
   return (neuron0x6482d20()*0.0448185);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6483a50() {
   return (neuron0x6483030()*-1.28083);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6483a90() {
   return (neuron0x6483340()*-4.53059);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6483de0() {
   return (neuron0x6482a10()*0.331561);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6483e20() {
   return (neuron0x6482d20()*-2.82934);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6483e60() {
   return (neuron0x6483030()*-1.57943);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6483ea0() {
   return (neuron0x6483340()*-6.36513);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x64841f0() {
   return (neuron0x6482a10()*-4.61755);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6484230() {
   return (neuron0x6482d20()*5.26361);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6484270() {
   return (neuron0x6483030()*2.28689);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x64842b0() {
   return (neuron0x6483340()*-4.73782);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6484600() {
   return (neuron0x6482a10()*3.1183);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6484640() {
   return (neuron0x6482d20()*0.567376);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6484680() {
   return (neuron0x6483030()*-2.12907);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x64846c0() {
   return (neuron0x6483340()*-1.65893);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6484a10() {
   return (neuron0x6482a10()*-1.09979);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x642b560() {
   return (neuron0x6482d20()*3.51486);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x61c7f60() {
   return (neuron0x6483030()*1.506);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x61c7fa0() {
   return (neuron0x6483340()*-4.53096);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6484e70() {
   return (neuron0x6483790()*-0.597457);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6484eb0() {
   return (neuron0x6483ad0()*0.35976);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6484ef0() {
   return (neuron0x6483ee0()*-1.17379);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6484f30() {
   return (neuron0x64842f0()*-1.51551);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6484f70() {
   return (neuron0x6484700()*0.300763);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x64852c0() {
   return (neuron0x6483790()*2.5827);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6485300() {
   return (neuron0x6483ad0()*-1.9479);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6485340() {
   return (neuron0x6483ee0()*1.47125);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6485380() {
   return (neuron0x64842f0()*2.56268);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x64853c0() {
   return (neuron0x6484700()*5.12449);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6485740() {
   return (neuron0x6483790()*-2.16565);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6485780() {
   return (neuron0x6483ad0()*1.06896);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x64857c0() {
   return (neuron0x6483ee0()*-0.396884);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x64461c0() {
   return (neuron0x64842f0()*0.0240632);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6489710() {
   return (neuron0x6484700()*-0.126484);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6485d50() {
   return (neuron0x6484b60()*2.54754);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6485d90() {
   return (neuron0x6484fb0()*1.74757);
}

double MLP_Higgs_vs_ZZ_MM_CSV_2011::synapse0x6485dd0() {
   return (neuron0x6485400()*-0.966994);
}

