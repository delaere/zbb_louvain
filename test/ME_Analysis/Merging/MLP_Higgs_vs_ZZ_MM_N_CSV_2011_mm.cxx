#include "MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.2374)/1.32546;
   input1 = (in1 - 11.0964)/1.0884;
   input2 = (in2 - 24.6224)/1.19824;
   input3 = (in3 - 13.2101)/1.2793;
   switch(index) {
     case 0:
         return neuron0x1a979250();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 21.2374)/1.32546;
   input1 = (input[1] - 11.0964)/1.0884;
   input2 = (input[2] - 24.6224)/1.19824;
   input3 = (input[3] - 13.2101)/1.2793;
   switch(index) {
     case 0:
         return neuron0x1a979250();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a976010() {
   return input0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a976350() {
   return input1;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a976690() {
   return input2;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a9769d0() {
   return input3;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1a976e40() {
   double input = 0.38706;
   input += synapse0x1a94f240();
   input += synapse0x1a9770f0();
   input += synapse0x1a977130();
   input += synapse0x1a977170();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a976e40() {
   double input = input0x1a976e40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1a9771b0() {
   double input = -3.55374;
   input += synapse0x1a9774f0();
   input += synapse0x1a977530();
   input += synapse0x1a977570();
   input += synapse0x1a9775b0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a9771b0() {
   double input = input0x1a9771b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1a9775f0() {
   double input = 1.06241;
   input += synapse0x1a977930();
   input += synapse0x1a977970();
   input += synapse0x1a9779b0();
   input += synapse0x1a9779f0();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a9775f0() {
   double input = input0x1a9775f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1a977a30() {
   double input = -9.90993;
   input += synapse0x1a977d70();
   input += synapse0x1a977db0();
   input += synapse0x1a977df0();
   input += synapse0x1a977e30();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a977a30() {
   double input = input0x1a977a30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1a977e70() {
   double input = 1.26067;
   input += synapse0x1a9781b0();
   input += synapse0x1a6e7c50();
   input += synapse0x1a6e7c90();
   input += synapse0x1a978300();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a977e70() {
   double input = input0x1a977e70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1a978340() {
   double input = 1.6187;
   input += synapse0x1a978680();
   input += synapse0x1a9786c0();
   input += synapse0x1a978700();
   input += synapse0x1a978740();
   input += synapse0x1a978780();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a978340() {
   double input = input0x1a978340();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1a9787c0() {
   double input = -1.96872;
   input += synapse0x1a978b00();
   input += synapse0x1a978b40();
   input += synapse0x1a978b80();
   input += synapse0x1a978bc0();
   input += synapse0x1a978c00();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a9787c0() {
   double input = input0x1a9787c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1a978c40() {
   double input = -5.33881;
   input += synapse0x1a978f80();
   input += synapse0x1a978fc0();
   input += synapse0x1a979000();
   input += synapse0x1a917320();
   input += synapse0x1a94f280();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a978c40() {
   double input = input0x1a978c40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::input0x1a979250() {
   double input = 0.075798;
   input += synapse0x1a979590();
   input += synapse0x1a9795d0();
   input += synapse0x1a979610();
   return input;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::neuron0x1a979250() {
   double input = input0x1a979250();
   return (input * 1)+0;
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a94f240() {
   return (neuron0x1a976010()*1.07387);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a9770f0() {
   return (neuron0x1a976350()*-2.85908);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a977130() {
   return (neuron0x1a976690()*-0.24384);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a977170() {
   return (neuron0x1a9769d0()*1.28999);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a9774f0() {
   return (neuron0x1a976010()*-7.93592);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a977530() {
   return (neuron0x1a976350()*-0.810567);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a977570() {
   return (neuron0x1a976690()*7.53551);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a9775b0() {
   return (neuron0x1a9769d0()*5.00669);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a977930() {
   return (neuron0x1a976010()*-0.235409);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a977970() {
   return (neuron0x1a976350()*1.53198);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a9779b0() {
   return (neuron0x1a976690()*-0.0100206);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a9779f0() {
   return (neuron0x1a9769d0()*-1.04234);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a977d70() {
   return (neuron0x1a976010()*0.422146);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a977db0() {
   return (neuron0x1a976350()*-7.32648);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a977df0() {
   return (neuron0x1a976690()*10.047);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a977e30() {
   return (neuron0x1a9769d0()*-1.40943);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a9781b0() {
   return (neuron0x1a976010()*1.01191);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a6e7c50() {
   return (neuron0x1a976350()*2.01583);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a6e7c90() {
   return (neuron0x1a976690()*-1.18901);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978300() {
   return (neuron0x1a9769d0()*-1.82558);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978680() {
   return (neuron0x1a976e40()*-0.773971);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a9786c0() {
   return (neuron0x1a9771b0()*0.843725);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978700() {
   return (neuron0x1a9775f0()*0.357408);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978740() {
   return (neuron0x1a977a30()*-0.00147705);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978780() {
   return (neuron0x1a977e70()*-3.63804);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978b00() {
   return (neuron0x1a976e40()*0.870406);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978b40() {
   return (neuron0x1a9771b0()*4.20326);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978b80() {
   return (neuron0x1a9775f0()*-9.01094);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978bc0() {
   return (neuron0x1a977a30()*6.75789);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978c00() {
   return (neuron0x1a977e70()*4.93833);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978f80() {
   return (neuron0x1a976e40()*1.56411);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a978fc0() {
   return (neuron0x1a9771b0()*-0.482223);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a979000() {
   return (neuron0x1a9775f0()*7.25437);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a917320() {
   return (neuron0x1a977a30()*-2.3659);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a94f280() {
   return (neuron0x1a977e70()*-3.41491);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a979590() {
   return (neuron0x1a978340()*-1.78299);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a9795d0() {
   return (neuron0x1a9787c0()*1.43998);
}

double MLP_Higgs_vs_ZZ_MM_N_CSV_2011_mm::synapse0x1a979610() {
   return (neuron0x1a978c40()*6.96865);
}

