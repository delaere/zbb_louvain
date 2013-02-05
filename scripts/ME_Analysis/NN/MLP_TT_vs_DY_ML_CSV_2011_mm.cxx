#include "../NN/MLP_TT_vs_DY_ML_CSV_2011_mm.h"
#include <cmath>

double MLP_TT_vs_DY_ML_CSV_2011_mm::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 20.3707)/1.37091;
   input1 = (in1 - 21.1326)/1.34189;
   input2 = (in2 - 21.9451)/1.01905;
   switch(index) {
     case 0:
         return neuron0x1bf05ae0();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 20.3707)/1.37091;
   input1 = (input[1] - 21.1326)/1.34189;
   input2 = (input[2] - 21.9451)/1.01905;
   switch(index) {
     case 0:
         return neuron0x1bf05ae0();
     default:
         return 0.;
   }
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::neuron0x1bef2ec0() {
   return input0;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::neuron0x1bef31d0() {
   return input1;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::neuron0x1bf04030() {
   return input2;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::input0x1bf04480() {
   double input = -1.57917;
   input += synapse0x1bec1180();
   input += synapse0x1bedb0f0();
   input += synapse0x1bec1210();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::neuron0x1bf04480() {
   double input = input0x1bf04480();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::input0x1bf04700() {
   double input = 0.358835;
   input += synapse0x1bef3450();
   input += synapse0x1bf04a10();
   input += synapse0x1bf04a50();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::neuron0x1bf04700() {
   double input = input0x1bf04700();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::input0x1bf04a90() {
   double input = -1.93847;
   input += synapse0x1bf04da0();
   input += synapse0x1bf04de0();
   input += synapse0x1bf04e20();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::neuron0x1bf04a90() {
   double input = input0x1bf04a90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::input0x1bf04e60() {
   double input = -1.66433;
   input += synapse0x1bf05170();
   input += synapse0x1bf051b0();
   input += synapse0x1bf051f0();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::neuron0x1bf04e60() {
   double input = input0x1bf04e60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::input0x1bf05230() {
   double input = -0.15086;
   input += synapse0x1bf05540();
   input += synapse0x1bf05580();
   input += synapse0x1bf055c0();
   input += synapse0x1bf05600();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::neuron0x1bf05230() {
   double input = input0x1bf05230();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::input0x1bf05640() {
   double input = -0.0929485;
   input += synapse0x1bf05950();
   input += synapse0x1bc51cd0();
   input += synapse0x1bc51d10();
   input += synapse0x1bf05aa0();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::neuron0x1bf05640() {
   double input = input0x1bf05640();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::input0x1bf05ae0() {
   double input = 0.387846;
   input += synapse0x1bf04400();
   input += synapse0x1bf04440();
   return input;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::neuron0x1bf05ae0() {
   double input = input0x1bf05ae0();
   return (input * 1)+0;
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bec1180() {
   return (neuron0x1bef2ec0()*-3.18632);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bedb0f0() {
   return (neuron0x1bef31d0()*2.71847);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bec1210() {
   return (neuron0x1bf04030()*-0.970492);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bef3450() {
   return (neuron0x1bef2ec0()*1.20288);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf04a10() {
   return (neuron0x1bef31d0()*0.704169);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf04a50() {
   return (neuron0x1bf04030()*-0.970866);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf04da0() {
   return (neuron0x1bef2ec0()*0.912515);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf04de0() {
   return (neuron0x1bef31d0()*-1.91204);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf04e20() {
   return (neuron0x1bf04030()*1.11887);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf05170() {
   return (neuron0x1bef2ec0()*-0.843744);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf051b0() {
   return (neuron0x1bef31d0()*1.95655);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf051f0() {
   return (neuron0x1bf04030()*-2.69465);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf05540() {
   return (neuron0x1bf04480()*0.404085);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf05580() {
   return (neuron0x1bf04700()*0.440097);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf055c0() {
   return (neuron0x1bf04a90()*0.898652);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf05600() {
   return (neuron0x1bf04e60()*-0.26426);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf05950() {
   return (neuron0x1bf04480()*2.26553);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bc51cd0() {
   return (neuron0x1bf04700()*-2.75464);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bc51d10() {
   return (neuron0x1bf04a90()*3.75482);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf05aa0() {
   return (neuron0x1bf04e60()*-1.52592);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf04400() {
   return (neuron0x1bf05230()*-0.769414);
}

double MLP_TT_vs_DY_ML_CSV_2011_mm::synapse0x1bf04440() {
   return (neuron0x1bf05640()*1.15211);
}

