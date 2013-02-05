#include "../NN/MLP_Higgs_vs_DY_ML_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_DY_ML_CSV_2011::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.4793)/1.12773;
   input1 = (in1 - 20.1867)/1.03855;
   input2 = (in2 - 24.9663)/1.41119;
   input3 = (in3 - 13.9146)/1.89048;
   switch(index) {
     case 0:
         return neuron0x1dca3800();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ML_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 19.4793)/1.12773;
   input1 = (input[1] - 20.1867)/1.03855;
   input2 = (input[2] - 24.9663)/1.41119;
   input3 = (input[3] - 13.9146)/1.89048;
   switch(index) {
     case 0:
         return neuron0x1dca3800();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca0800() {
   return input0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca0b10() {
   return input1;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca0e20() {
   return input2;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca1130() {
   return input3;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::input0x1dca1580() {
   double input = -1.87827;
   input += synapse0x1dc49750();
   input += synapse0x1dca1800();
   input += synapse0x1dca1840();
   input += synapse0x1dca1880();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca1580() {
   double input = input0x1dca1580();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::input0x1dca18c0() {
   double input = 1.51714;
   input += synapse0x1dca1bd0();
   input += synapse0x1dca1c10();
   input += synapse0x1dca1c50();
   input += synapse0x1dca1c90();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca18c0() {
   double input = input0x1dca18c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::input0x1dca1cd0() {
   double input = 4.95614;
   input += synapse0x1dca1fe0();
   input += synapse0x1dca2020();
   input += synapse0x1dca2060();
   input += synapse0x1dca20a0();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca1cd0() {
   double input = input0x1dca1cd0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::input0x1dca20e0() {
   double input = 3.12949;
   input += synapse0x1dca23f0();
   input += synapse0x1dca2430();
   input += synapse0x1dca2470();
   input += synapse0x1dca24b0();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca20e0() {
   double input = input0x1dca20e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::input0x1dca24f0() {
   double input = 0.746039;
   input += synapse0x1dca2800();
   input += synapse0x1dc49350();
   input += synapse0x1d9da2e0();
   input += synapse0x1d9da320();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca24f0() {
   double input = input0x1dca24f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::input0x1dca2950() {
   double input = -2.25407;
   input += synapse0x1dca2c60();
   input += synapse0x1dca2ca0();
   input += synapse0x1dca2ce0();
   input += synapse0x1dca2d20();
   input += synapse0x1dca2d60();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca2950() {
   double input = input0x1dca2950();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::input0x1dca2da0() {
   double input = 1.66614;
   input += synapse0x1dca30b0();
   input += synapse0x1dca30f0();
   input += synapse0x1dca3130();
   input += synapse0x1dca3170();
   input += synapse0x1dca31b0();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca2da0() {
   double input = input0x1dca2da0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::input0x1dca31f0() {
   double input = -2.51955;
   input += synapse0x1dca3530();
   input += synapse0x1dca3570();
   input += synapse0x1dca35b0();
   input += synapse0x1dc63fb0();
   input += synapse0x1dca7500();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca31f0() {
   double input = input0x1dca31f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::input0x1dca3800() {
   double input = 2.09858;
   input += synapse0x1dca3b40();
   input += synapse0x1dca3b80();
   input += synapse0x1dca3bc0();
   return input;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::neuron0x1dca3800() {
   double input = input0x1dca3800();
   return (input * 1)+0;
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dc49750() {
   return (neuron0x1dca0800()*-3.27537);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca1800() {
   return (neuron0x1dca0b10()*2.73736);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca1840() {
   return (neuron0x1dca0e20()*-1.1605);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca1880() {
   return (neuron0x1dca1130()*1.02111);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca1bd0() {
   return (neuron0x1dca0800()*4.31825);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca1c10() {
   return (neuron0x1dca0b10()*0.359287);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca1c50() {
   return (neuron0x1dca0e20()*-1.29652);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca1c90() {
   return (neuron0x1dca1130()*-3.04434);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca1fe0() {
   return (neuron0x1dca0800()*1.86734);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca2020() {
   return (neuron0x1dca0b10()*2.80079);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca2060() {
   return (neuron0x1dca0e20()*-6.16549);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca20a0() {
   return (neuron0x1dca1130()*1.34563);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca23f0() {
   return (neuron0x1dca0800()*-0.746022);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca2430() {
   return (neuron0x1dca0b10()*-1.48415);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca2470() {
   return (neuron0x1dca0e20()*0.672528);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca24b0() {
   return (neuron0x1dca1130()*4.03085);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca2800() {
   return (neuron0x1dca0800()*0.0720833);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dc49350() {
   return (neuron0x1dca0b10()*-4.13748);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1d9da2e0() {
   return (neuron0x1dca0e20()*6.40945);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1d9da320() {
   return (neuron0x1dca1130()*-4.43726);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca2c60() {
   return (neuron0x1dca1580()*-3.85603);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca2ca0() {
   return (neuron0x1dca18c0()*-3.44818);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca2ce0() {
   return (neuron0x1dca1cd0()*3.95356);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca2d20() {
   return (neuron0x1dca20e0()*-0.58702);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca2d60() {
   return (neuron0x1dca24f0()*3.5303);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca30b0() {
   return (neuron0x1dca1580()*3.22564);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca30f0() {
   return (neuron0x1dca18c0()*3.09059);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca3130() {
   return (neuron0x1dca1cd0()*-3.23421);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca3170() {
   return (neuron0x1dca20e0()*0.951888);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca31b0() {
   return (neuron0x1dca24f0()*-2.58378);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca3530() {
   return (neuron0x1dca1580()*-1.74693);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca3570() {
   return (neuron0x1dca18c0()*2.52003);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca35b0() {
   return (neuron0x1dca1cd0()*4.08631);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dc63fb0() {
   return (neuron0x1dca20e0()*-5.06701);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca7500() {
   return (neuron0x1dca24f0()*2.79098);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca3b40() {
   return (neuron0x1dca2950()*-1.48606);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca3b80() {
   return (neuron0x1dca2da0()*-2.03447);
}

double MLP_Higgs_vs_DY_ML_CSV_2011::synapse0x1dca3bc0() {
   return (neuron0x1dca31f0()*0.791545);
}

