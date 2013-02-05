#include "../NN/MLP_Higgs_vs_TT_ML_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_TT_ML_CSV_2011::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 22.4378)/1.57798;
   input1 = (in1 - 25.9218)/1.78791;
   input2 = (in2 - 14.9314)/2.30019;
   switch(index) {
     case 0:
         return neuron0xc198310();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ML_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 22.4378)/1.57798;
   input1 = (input[1] - 25.9218)/1.78791;
   input2 = (input[2] - 14.9314)/2.30019;
   switch(index) {
     case 0:
         return neuron0xc198310();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc1840e0() {
   return input0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc1843f0() {
   return input1;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc195250() {
   return input2;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc1956a0() {
   double input = -1.04492;
   input += synapse0xc1523a0();
   input += synapse0xc16c310();
   input += synapse0xc152430();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc1956a0() {
   double input = input0xc1956a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc195920() {
   double input = -3.05248;
   input += synapse0xc184670();
   input += synapse0xc195c30();
   input += synapse0xc195c70();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc195920() {
   double input = input0xc195920();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc195cb0() {
   double input = -1.31562;
   input += synapse0xc195fc0();
   input += synapse0xc196000();
   input += synapse0xc196040();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc195cb0() {
   double input = input0xc195cb0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc196080() {
   double input = 0.753567;
   input += synapse0xc196390();
   input += synapse0xc1963d0();
   input += synapse0xc196410();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc196080() {
   double input = input0xc196080();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc196450() {
   double input = -1.92273;
   input += synapse0xc196760();
   input += synapse0xc1967a0();
   input += synapse0xc1967e0();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc196450() {
   double input = input0xc196450();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc196820() {
   double input = -2.6572;
   input += synapse0xc196b30();
   input += synapse0xc196b70();
   input += synapse0xbee33b0();
   input += synapse0xbee33f0();
   input += synapse0xc196cc0();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc196820() {
   double input = input0xc196820();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc196d00() {
   double input = 1.74177;
   input += synapse0xc197040();
   input += synapse0xc197080();
   input += synapse0xc1970c0();
   input += synapse0xc197100();
   input += synapse0xc197140();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc196d00() {
   double input = input0xc196d00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc197180() {
   double input = 0.453561;
   input += synapse0xc1974c0();
   input += synapse0xc197500();
   input += synapse0xc197540();
   input += synapse0xc197580();
   input += synapse0xc1975c0();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc197180() {
   double input = input0xc197180();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc197600() {
   double input = 2.30089;
   input += synapse0xc197940();
   input += synapse0xc197980();
   input += synapse0xc1979c0();
   input += synapse0xc183f50();
   input += synapse0xc16cba0();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc197600() {
   double input = input0xc197600();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc197c10() {
   double input = 0.357337;
   input += synapse0xc151fd0();
   input += synapse0xc196c40();
   input += synapse0xc196c80();
   input += synapse0xc197e90();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc197c10() {
   double input = input0xc197c10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc197ed0() {
   double input = 0.939482;
   input += synapse0xc198210();
   input += synapse0xc198250();
   input += synapse0xc198290();
   input += synapse0xc1982d0();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc197ed0() {
   double input = input0xc197ed0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::input0xc198310() {
   double input = 0.68687;
   input += synapse0xc195620();
   input += synapse0xc195660();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::neuron0xc198310() {
   double input = input0xc198310();
   return (input * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc1523a0() {
   return (neuron0xc1840e0()*3.15084);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc16c310() {
   return (neuron0xc1843f0()*-0.330955);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc152430() {
   return (neuron0xc195250()*-6.73065);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc184670() {
   return (neuron0xc1840e0()*2.40846);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc195c30() {
   return (neuron0xc1843f0()*-1.31342);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc195c70() {
   return (neuron0xc195250()*0.26279);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc195fc0() {
   return (neuron0xc1840e0()*-1.453);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc196000() {
   return (neuron0xc1843f0()*2.09407);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc196040() {
   return (neuron0xc195250()*0.954562);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc196390() {
   return (neuron0xc1840e0()*-0.99114);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc1963d0() {
   return (neuron0xc1843f0()*-0.0504968);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc196410() {
   return (neuron0xc195250()*1.68565);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc196760() {
   return (neuron0xc1840e0()*-0.634546);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc1967a0() {
   return (neuron0xc1843f0()*-5.96673);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc1967e0() {
   return (neuron0xc195250()*7.91993);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc196b30() {
   return (neuron0xc1956a0()*1.80226);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc196b70() {
   return (neuron0xc195920()*-1.61229);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xbee33b0() {
   return (neuron0xc195cb0()*2.42505);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xbee33f0() {
   return (neuron0xc196080()*6.65511);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc196cc0() {
   return (neuron0xc196450()*-3.10868);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc197040() {
   return (neuron0xc1956a0()*-1.52472);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc197080() {
   return (neuron0xc195920()*0.904096);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc1970c0() {
   return (neuron0xc195cb0()*0.35159);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc197100() {
   return (neuron0xc196080()*-1.19113);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc197140() {
   return (neuron0xc196450()*-0.130873);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc1974c0() {
   return (neuron0xc1956a0()*1.66945);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc197500() {
   return (neuron0xc195920()*-4.74446);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc197540() {
   return (neuron0xc195cb0()*-3.88459);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc197580() {
   return (neuron0xc196080()*-2.47012);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc1975c0() {
   return (neuron0xc196450()*-4.24165);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc197940() {
   return (neuron0xc1956a0()*0.89015);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc197980() {
   return (neuron0xc195920()*-0.451757);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc1979c0() {
   return (neuron0xc195cb0()*2.31515);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc183f50() {
   return (neuron0xc196080()*1.04589);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc16cba0() {
   return (neuron0xc196450()*-0.0657962);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc151fd0() {
   return (neuron0xc196820()*-0.547718);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc196c40() {
   return (neuron0xc196d00()*2.72113);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc196c80() {
   return (neuron0xc197180()*4.38754);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc197e90() {
   return (neuron0xc197600()*2.21729);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc198210() {
   return (neuron0xc196820()*-3.36341);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc198250() {
   return (neuron0xc196d00()*2.95286);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc198290() {
   return (neuron0xc197180()*3.43713);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc1982d0() {
   return (neuron0xc197600()*0.557122);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc195620() {
   return (neuron0xc197c10()*-2.1563);
}

double MLP_Higgs_vs_TT_ML_CSV_2011::synapse0xc195660() {
   return (neuron0xc197ed0()*2.51586);
}

