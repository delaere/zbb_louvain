#include "../NN/MLP_TT_vs_DY_MM_CSV_2011.h"
#include <cmath>

double MLP_TT_vs_DY_MM_CSV_2011::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 20.7013)/1.21319;
   input1 = (in1 - 21.4158)/1.18978;
   input2 = (in2 - 22.0353)/0.891669;
   switch(index) {
     case 0:
         return neuron0x2ec3620();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_MM_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 20.7013)/1.21319;
   input1 = (input[1] - 21.4158)/1.18978;
   input2 = (input[2] - 22.0353)/0.891669;
   switch(index) {
     case 0:
         return neuron0x2ec3620();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_MM_CSV_2011::neuron0x2eb0a00() {
   return input0;
}

double MLP_TT_vs_DY_MM_CSV_2011::neuron0x2eb0d10() {
   return input1;
}

double MLP_TT_vs_DY_MM_CSV_2011::neuron0x2ec1b70() {
   return input2;
}

double MLP_TT_vs_DY_MM_CSV_2011::input0x2ec1fc0() {
   double input = 0.25164;
   input += synapse0x2e7ecc0();
   input += synapse0x2e98c30();
   input += synapse0x2e7ed50();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011::neuron0x2ec1fc0() {
   double input = input0x2ec1fc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011::input0x2ec2240() {
   double input = -2.26692;
   input += synapse0x2eb0f90();
   input += synapse0x2ec2550();
   input += synapse0x2ec2590();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011::neuron0x2ec2240() {
   double input = input0x2ec2240();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011::input0x2ec25d0() {
   double input = 0.49738;
   input += synapse0x2ec28e0();
   input += synapse0x2ec2920();
   input += synapse0x2ec2960();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011::neuron0x2ec25d0() {
   double input = input0x2ec25d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011::input0x2ec29a0() {
   double input = 0.589069;
   input += synapse0x2ec2cb0();
   input += synapse0x2ec2cf0();
   input += synapse0x2ec2d30();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011::neuron0x2ec29a0() {
   double input = input0x2ec29a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011::input0x2ec2d70() {
   double input = -0.681624;
   input += synapse0x2ec3080();
   input += synapse0x2ec30c0();
   input += synapse0x2ec3100();
   input += synapse0x2ec3140();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011::neuron0x2ec2d70() {
   double input = input0x2ec2d70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011::input0x2ec3180() {
   double input = -0.0937068;
   input += synapse0x2ec3490();
   input += synapse0x2c0f8b0();
   input += synapse0x2c0f8f0();
   input += synapse0x2ec35e0();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011::neuron0x2ec3180() {
   double input = input0x2ec3180();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011::input0x2ec3620() {
   double input = 0.10213;
   input += synapse0x2ec1f40();
   input += synapse0x2ec1f80();
   return input;
}

double MLP_TT_vs_DY_MM_CSV_2011::neuron0x2ec3620() {
   double input = input0x2ec3620();
   return (input * 1)+0;
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2e7ecc0() {
   return (neuron0x2eb0a00()*2.12048);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2e98c30() {
   return (neuron0x2eb0d10()*2.89899);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2e7ed50() {
   return (neuron0x2ec1b70()*-2.89087);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2eb0f90() {
   return (neuron0x2eb0a00()*-1.18933);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec2550() {
   return (neuron0x2eb0d10()*-1.12065);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec2590() {
   return (neuron0x2ec1b70()*1.33401);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec28e0() {
   return (neuron0x2eb0a00()*-1.92627);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec2920() {
   return (neuron0x2eb0d10()*-0.641244);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec2960() {
   return (neuron0x2ec1b70()*0.50616);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec2cb0() {
   return (neuron0x2eb0a00()*-0.258863);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec2cf0() {
   return (neuron0x2eb0d10()*-0.440461);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec2d30() {
   return (neuron0x2ec1b70()*0.954777);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec3080() {
   return (neuron0x2ec1fc0()*-3.14113);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec30c0() {
   return (neuron0x2ec2240()*1.70013);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec3100() {
   return (neuron0x2ec25d0()*-0.622052);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec3140() {
   return (neuron0x2ec29a0()*-0.634393);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec3490() {
   return (neuron0x2ec1fc0()*-0.522654);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2c0f8b0() {
   return (neuron0x2ec2240()*-0.092235);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2c0f8f0() {
   return (neuron0x2ec25d0()*-0.234238);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec35e0() {
   return (neuron0x2ec29a0()*-0.462601);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec1f40() {
   return (neuron0x2ec2d70()*2.21509);
}

double MLP_TT_vs_DY_MM_CSV_2011::synapse0x2ec1f80() {
   return (neuron0x2ec3180()*-0.321657);
}

