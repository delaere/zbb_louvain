#include "MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb.h"
#include <cmath>

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.50292)/0.333385;
   input1 = (in1 - 0.531842)/0.319461;
   input2 = (in2 - 0.494778)/0.360323;
   switch(index) {
     case 0:
         return neuron0x143264b0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::Value(int index, double* input) {
   input0 = (input[0] - 0.50292)/0.333385;
   input1 = (input[1] - 0.531842)/0.319461;
   input2 = (input[2] - 0.494778)/0.360323;
   switch(index) {
     case 0:
         return neuron0x143264b0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14322690() {
   return input0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x143229a0() {
   return input1;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14322cb0() {
   return input2;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x14323100() {
   double input = 1.65813;
   input += synapse0x12771410();
   input += synapse0x119e9690();
   input += synapse0x119e9310();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14323100() {
   double input = input0x14323100();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x14323380() {
   double input = 0.626952;
   input += synapse0x14323690();
   input += synapse0x143236d0();
   input += synapse0x14323710();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14323380() {
   double input = input0x14323380();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x14323750() {
   double input = 0.953075;
   input += synapse0x14323a60();
   input += synapse0x14323aa0();
   input += synapse0x14323ae0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14323750() {
   double input = input0x14323750();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x14323b20() {
   double input = -1.31498;
   input += synapse0x14323e30();
   input += synapse0x14323e70();
   input += synapse0x14323eb0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14323b20() {
   double input = input0x14323b20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x14323ef0() {
   double input = -0.805429;
   input += synapse0x14324200();
   input += synapse0x14324240();
   input += synapse0x14324280();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14323ef0() {
   double input = input0x14323ef0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x143242c0() {
   double input = -1.36434;
   input += synapse0x143245d0();
   input += synapse0x14324610();
   input += synapse0x12dace50();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x143242c0() {
   double input = input0x143242c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x14324760() {
   double input = -0.98275;
   input += synapse0x14324aa0();
   input += synapse0x14324ae0();
   input += synapse0x14324b20();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14324760() {
   double input = input0x14324760();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x14324b60() {
   double input = 0.966547;
   input += synapse0x14324ea0();
   input += synapse0x14324ee0();
   input += synapse0x14324f20();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14324b60() {
   double input = input0x14324b60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x14324f60() {
   double input = 0.325086;
   input += synapse0x143252a0();
   input += synapse0x143252e0();
   input += synapse0x14325320();
   input += synapse0x14325360();
   input += synapse0x143253a0();
   input += synapse0x143253e0();
   input += synapse0x14325420();
   input += synapse0x14325460();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14324f60() {
   double input = input0x14324f60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x143254a0() {
   double input = 0.0755175;
   input += synapse0x143257e0();
   input += synapse0x12dace90();
   input += synapse0x12644960();
   input += synapse0x126449a0();
   input += synapse0x14324650();
   input += synapse0x14324690();
   input += synapse0x143246d0();
   input += synapse0x14324710();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x143254a0() {
   double input = input0x143254a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x14325a30() {
   double input = 0.418749;
   input += synapse0x14325d70();
   input += synapse0x14325db0();
   input += synapse0x14325df0();
   input += synapse0x14325e30();
   input += synapse0x14325e70();
   input += synapse0x14325eb0();
   input += synapse0x14325ef0();
   input += synapse0x14325f30();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14325a30() {
   double input = input0x14325a30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x14325f70() {
   double input = 0.0917084;
   input += synapse0x143262b0();
   input += synapse0x143262f0();
   input += synapse0x14326330();
   input += synapse0x14326370();
   input += synapse0x143263b0();
   input += synapse0x143263f0();
   input += synapse0x14326430();
   input += synapse0x14326470();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x14325f70() {
   double input = input0x14325f70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::input0x143264b0() {
   double input = -2.26699;
   input += synapse0x143267f0();
   input += synapse0x14326830();
   input += synapse0x14326870();
   input += synapse0x143268b0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::neuron0x143264b0() {
   double input = input0x143264b0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x12771410() {
   return (neuron0x14322690()*2.55646);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x119e9690() {
   return (neuron0x143229a0()*-0.905835);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x119e9310() {
   return (neuron0x14322cb0()*-1.94896);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14323690() {
   return (neuron0x14322690()*2.6891);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143236d0() {
   return (neuron0x143229a0()*-1.88299);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14323710() {
   return (neuron0x14322cb0()*-0.643953);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14323a60() {
   return (neuron0x14322690()*0.447543);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14323aa0() {
   return (neuron0x143229a0()*0.358809);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14323ae0() {
   return (neuron0x14322cb0()*-1.66741);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14323e30() {
   return (neuron0x14322690()*1.95665);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14323e70() {
   return (neuron0x143229a0()*3.56794);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14323eb0() {
   return (neuron0x14322cb0()*4.53857);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324200() {
   return (neuron0x14322690()*1.37495);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324240() {
   return (neuron0x143229a0()*-1.77335);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324280() {
   return (neuron0x14322cb0()*0.102773);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143245d0() {
   return (neuron0x14322690()*-1.40422);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324610() {
   return (neuron0x143229a0()*1.62701);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x12dace50() {
   return (neuron0x14322cb0()*-1.10904);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324aa0() {
   return (neuron0x14322690()*0.943994);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324ae0() {
   return (neuron0x143229a0()*-2.05643);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324b20() {
   return (neuron0x14322cb0()*2.65224);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324ea0() {
   return (neuron0x14322690()*1.03233);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324ee0() {
   return (neuron0x143229a0()*0.106195);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324f20() {
   return (neuron0x14322cb0()*-1.48754);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143252a0() {
   return (neuron0x14323100()*0.477509);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143252e0() {
   return (neuron0x14323380()*0.156935);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325320() {
   return (neuron0x14323750()*-2.55617);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325360() {
   return (neuron0x14323b20()*-4.89074);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143253a0() {
   return (neuron0x14323ef0()*4.07014);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143253e0() {
   return (neuron0x143242c0()*-0.896528);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325420() {
   return (neuron0x14324760()*-4.18308);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325460() {
   return (neuron0x14324b60()*-2.9619);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143257e0() {
   return (neuron0x14323100()*0.334919);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x12dace90() {
   return (neuron0x14323380()*-1.32749);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x12644960() {
   return (neuron0x14323750()*-0.421928);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x126449a0() {
   return (neuron0x14323b20()*0.905368);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324650() {
   return (neuron0x14323ef0()*-1.14379);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324690() {
   return (neuron0x143242c0()*-0.453296);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143246d0() {
   return (neuron0x14324760()*-0.308938);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14324710() {
   return (neuron0x14324b60()*1.42319);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325d70() {
   return (neuron0x14323100()*-1.80412);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325db0() {
   return (neuron0x14323380()*1.6487);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325df0() {
   return (neuron0x14323750()*-2.9989);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325e30() {
   return (neuron0x14323b20()*-0.585852);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325e70() {
   return (neuron0x14323ef0()*0.01688);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325eb0() {
   return (neuron0x143242c0()*-1.25476);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325ef0() {
   return (neuron0x14324760()*-0.700521);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14325f30() {
   return (neuron0x14324b60()*2.34997);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143262b0() {
   return (neuron0x14323100()*0.900172);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143262f0() {
   return (neuron0x14323380()*0.576829);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14326330() {
   return (neuron0x14323750()*0.610892);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14326370() {
   return (neuron0x14323b20()*0.403672);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143263b0() {
   return (neuron0x14323ef0()*-0.511315);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143263f0() {
   return (neuron0x143242c0()*-0.429356);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14326430() {
   return (neuron0x14324760()*-1.57474);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14326470() {
   return (neuron0x14324b60()*2.25432);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143267f0() {
   return (neuron0x14324f60()*-4.47096);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14326830() {
   return (neuron0x143254a0()*1.31031);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x14326870() {
   return (neuron0x14325a30()*4.41685);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011_comb::synapse0x143268b0() {
   return (neuron0x14325f70()*1.32652);
}

