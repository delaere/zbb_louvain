#include "../NN/MLP_Higgs_vs_DY_MM_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.6576)/1.15823;
   input1 = (in1 - 20.3074)/1.03292;
   input2 = (in2 - 24.6966)/1.35474;
   input3 = (in3 - 13.4484)/1.64745;
   switch(index) {
     case 0:
         return neuron0x1163da70();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 19.6576)/1.15823;
   input1 = (input[1] - 20.3074)/1.03292;
   input2 = (input[2] - 24.6966)/1.35474;
   input3 = (input[3] - 13.4484)/1.64745;
   switch(index) {
     case 0:
         return neuron0x1163da70();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163aa70() {
   return input0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163ad80() {
   return input1;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163b090() {
   return input2;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163b3a0() {
   return input3;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::input0x1163b7f0() {
   double input = -5.01022;
   input += synapse0x115e39c0();
   input += synapse0x1163ba70();
   input += synapse0x1163bab0();
   input += synapse0x1163baf0();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163b7f0() {
   double input = input0x1163b7f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::input0x1163bb30() {
   double input = -2.47505;
   input += synapse0x1163be40();
   input += synapse0x1163be80();
   input += synapse0x1163bec0();
   input += synapse0x1163bf00();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163bb30() {
   double input = input0x1163bb30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::input0x1163bf40() {
   double input = 0.949403;
   input += synapse0x1163c250();
   input += synapse0x1163c290();
   input += synapse0x1163c2d0();
   input += synapse0x1163c310();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163bf40() {
   double input = input0x1163bf40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::input0x1163c350() {
   double input = 3.78282;
   input += synapse0x1163c660();
   input += synapse0x1163c6a0();
   input += synapse0x1163c6e0();
   input += synapse0x1163c720();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163c350() {
   double input = input0x1163c350();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::input0x1163c760() {
   double input = -0.537223;
   input += synapse0x1163ca70();
   input += synapse0x115e35c0();
   input += synapse0x11548f90();
   input += synapse0x11548fd0();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163c760() {
   double input = input0x1163c760();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::input0x1163cbc0() {
   double input = 2.79616;
   input += synapse0x1163ced0();
   input += synapse0x1163cf10();
   input += synapse0x1163cf50();
   input += synapse0x1163cf90();
   input += synapse0x1163cfd0();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163cbc0() {
   double input = input0x1163cbc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::input0x1163d010() {
   double input = -0.971869;
   input += synapse0x1163d320();
   input += synapse0x1163d360();
   input += synapse0x1163d3a0();
   input += synapse0x1163d3e0();
   input += synapse0x1163d420();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163d010() {
   double input = input0x1163d010();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::input0x1163d460() {
   double input = -0.0537748;
   input += synapse0x1163d7a0();
   input += synapse0x1163d7e0();
   input += synapse0x1163d820();
   input += synapse0x11615560();
   input += synapse0x116417a0();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163d460() {
   double input = input0x1163d460();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::input0x1163da70() {
   double input = -0.522105;
   input += synapse0x1163ddb0();
   input += synapse0x1163ddf0();
   input += synapse0x1163de30();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::neuron0x1163da70() {
   double input = input0x1163da70();
   return (input * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x115e39c0() {
   return (neuron0x1163aa70()*-0.83373);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163ba70() {
   return (neuron0x1163ad80()*-1.58903);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163bab0() {
   return (neuron0x1163b090()*4.53914);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163baf0() {
   return (neuron0x1163b3a0()*0.868218);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163be40() {
   return (neuron0x1163aa70()*-1.27595);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163be80() {
   return (neuron0x1163ad80()*-0.340137);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163bec0() {
   return (neuron0x1163b090()*2.40981);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163bf00() {
   return (neuron0x1163b3a0()*1.20015);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163c250() {
   return (neuron0x1163aa70()*-1.11402);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163c290() {
   return (neuron0x1163ad80()*2.3929);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163c2d0() {
   return (neuron0x1163b090()*-1.46063);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163c310() {
   return (neuron0x1163b3a0()*3.46806);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163c660() {
   return (neuron0x1163aa70()*-2.02789);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163c6a0() {
   return (neuron0x1163ad80()*4.05279);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163c6e0() {
   return (neuron0x1163b090()*-2.4257);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163c720() {
   return (neuron0x1163b3a0()*2.91111);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163ca70() {
   return (neuron0x1163aa70()*0.901211);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x115e35c0() {
   return (neuron0x1163ad80()*0.755343);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x11548f90() {
   return (neuron0x1163b090()*-0.225761);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x11548fd0() {
   return (neuron0x1163b3a0()*-2.44624);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163ced0() {
   return (neuron0x1163b7f0()*4.50404);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163cf10() {
   return (neuron0x1163bb30()*1.83116);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163cf50() {
   return (neuron0x1163bf40()*-0.642628);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163cf90() {
   return (neuron0x1163c350()*-3.71691);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163cfd0() {
   return (neuron0x1163c760()*2.16137);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163d320() {
   return (neuron0x1163b7f0()*-0.265061);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163d360() {
   return (neuron0x1163bb30()*-1.12537);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163d3a0() {
   return (neuron0x1163bf40()*-1.35422);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163d3e0() {
   return (neuron0x1163c350()*-1.57672);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163d420() {
   return (neuron0x1163c760()*-0.377017);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163d7a0() {
   return (neuron0x1163b7f0()*1.26849);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163d7e0() {
   return (neuron0x1163bb30()*6.1156);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163d820() {
   return (neuron0x1163bf40()*-1.84483);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x11615560() {
   return (neuron0x1163c350()*-2.47278);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x116417a0() {
   return (neuron0x1163c760()*1.71537);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163ddb0() {
   return (neuron0x1163cbc0()*2.58165);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163ddf0() {
   return (neuron0x1163d010()*-0.261563);
}

double MLP_Higgs_vs_DY_MM_CSV_2011_mm::synapse0x1163de30() {
   return (neuron0x1163d460()*-2.10042);
}

