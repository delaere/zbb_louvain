#include "MLP_Higgs_vs_zz_MU.h"
#include <cmath>

double MLP_Higgs_vs_zz_MU::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.4103)/1.30941;
   input1 = (in1 - 11.2359)/1.0772;
   input2 = (in2 - 24.4493)/1.21323;
   input3 = (in3 - 12.9476)/1.14412;
   switch(index) {
     case 0:
         return neuron0x7017d60();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_zz_MU::Value(int index, double* input) {
   input0 = (input[0] - 21.4103)/1.30941;
   input1 = (input[1] - 11.2359)/1.0772;
   input2 = (input[2] - 24.4493)/1.21323;
   input3 = (input[3] - 12.9476)/1.14412;
   switch(index) {
     case 0:
         return neuron0x7017d60();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_zz_MU::neuron0x7014b20() {
   return input0;
}

double MLP_Higgs_vs_zz_MU::neuron0x7014e60() {
   return input1;
}

double MLP_Higgs_vs_zz_MU::neuron0x70151a0() {
   return input2;
}

double MLP_Higgs_vs_zz_MU::neuron0x70154e0() {
   return input3;
}

double MLP_Higgs_vs_zz_MU::input0x7015950() {
   double input = -1.22467;
   input += synapse0x6fedd50();
   input += synapse0x7015c00();
   input += synapse0x7015c40();
   input += synapse0x7015c80();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x7015950() {
   double input = input0x7015950();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x7015cc0() {
   double input = -0.509363;
   input += synapse0x7016000();
   input += synapse0x7016040();
   input += synapse0x7016080();
   input += synapse0x70160c0();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x7015cc0() {
   double input = input0x7015cc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x7016100() {
   double input = -4.4415;
   input += synapse0x7016440();
   input += synapse0x7016480();
   input += synapse0x70164c0();
   input += synapse0x7016500();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x7016100() {
   double input = input0x7016100();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x7016540() {
   double input = 2.10246;
   input += synapse0x7016880();
   input += synapse0x70168c0();
   input += synapse0x7016900();
   input += synapse0x7016940();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x7016540() {
   double input = input0x7016540();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x7016980() {
   double input = -0.493015;
   input += synapse0x7016cc0();
   input += synapse0x6f63730();
   input += synapse0x6f63770();
   input += synapse0x7016e10();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x7016980() {
   double input = input0x7016980();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x7016e50() {
   double input = -0.947799;
   input += synapse0x7017190();
   input += synapse0x70171d0();
   input += synapse0x7017210();
   input += synapse0x7017250();
   input += synapse0x7017290();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x7016e50() {
   double input = input0x7016e50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x70172d0() {
   double input = 1.93004;
   input += synapse0x7017610();
   input += synapse0x7017650();
   input += synapse0x7017690();
   input += synapse0x70176d0();
   input += synapse0x7017710();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x70172d0() {
   double input = input0x70172d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x7017750() {
   double input = 0.115498;
   input += synapse0x7017a90();
   input += synapse0x7017ad0();
   input += synapse0x7017b10();
   input += synapse0x6fb5e30();
   input += synapse0x6fedd90();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x7017750() {
   double input = input0x7017750();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zz_MU::input0x7017d60() {
   double input = 0.424596;
   input += synapse0x70180a0();
   input += synapse0x70180e0();
   input += synapse0x7018120();
   return input;
}

double MLP_Higgs_vs_zz_MU::neuron0x7017d60() {
   double input = input0x7017d60();
   return (input * 1)+0;
}

double MLP_Higgs_vs_zz_MU::synapse0x6fedd50() {
   return (neuron0x7014b20()*-1.13063);
}

double MLP_Higgs_vs_zz_MU::synapse0x7015c00() {
   return (neuron0x7014e60()*0.510146);
}

double MLP_Higgs_vs_zz_MU::synapse0x7015c40() {
   return (neuron0x70151a0()*-0.13239);
}

double MLP_Higgs_vs_zz_MU::synapse0x7015c80() {
   return (neuron0x70154e0()*2.65317);
}

double MLP_Higgs_vs_zz_MU::synapse0x7016000() {
   return (neuron0x7014b20()*0.262534);
}

double MLP_Higgs_vs_zz_MU::synapse0x7016040() {
   return (neuron0x7014e60()*-2.51692);
}

double MLP_Higgs_vs_zz_MU::synapse0x7016080() {
   return (neuron0x70151a0()*-0.0995399);
}

double MLP_Higgs_vs_zz_MU::synapse0x70160c0() {
   return (neuron0x70154e0()*2.07301);
}

double MLP_Higgs_vs_zz_MU::synapse0x7016440() {
   return (neuron0x7014b20()*0.133591);
}

double MLP_Higgs_vs_zz_MU::synapse0x7016480() {
   return (neuron0x7014e60()*-2.4422);
}

double MLP_Higgs_vs_zz_MU::synapse0x70164c0() {
   return (neuron0x70151a0()*2.77675);
}

double MLP_Higgs_vs_zz_MU::synapse0x7016500() {
   return (neuron0x70154e0()*0.0864247);
}

double MLP_Higgs_vs_zz_MU::synapse0x7016880() {
   return (neuron0x7014b20()*-0.420838);
}

double MLP_Higgs_vs_zz_MU::synapse0x70168c0() {
   return (neuron0x7014e60()*3.08863);
}

double MLP_Higgs_vs_zz_MU::synapse0x7016900() {
   return (neuron0x70151a0()*0.0494237);
}

double MLP_Higgs_vs_zz_MU::synapse0x7016940() {
   return (neuron0x70154e0()*-2.94086);
}

double MLP_Higgs_vs_zz_MU::synapse0x7016cc0() {
   return (neuron0x7014b20()*0.223198);
}

double MLP_Higgs_vs_zz_MU::synapse0x6f63730() {
   return (neuron0x7014e60()*0.0225364);
}

double MLP_Higgs_vs_zz_MU::synapse0x6f63770() {
   return (neuron0x70151a0()*0.781829);
}

double MLP_Higgs_vs_zz_MU::synapse0x7016e10() {
   return (neuron0x70154e0()*0.493065);
}

double MLP_Higgs_vs_zz_MU::synapse0x7017190() {
   return (neuron0x7015950()*-0.791986);
}

double MLP_Higgs_vs_zz_MU::synapse0x70171d0() {
   return (neuron0x7015cc0()*1.81123);
}

double MLP_Higgs_vs_zz_MU::synapse0x7017210() {
   return (neuron0x7016100()*3.2141);
}

double MLP_Higgs_vs_zz_MU::synapse0x7017250() {
   return (neuron0x7016540()*-2.82243);
}

double MLP_Higgs_vs_zz_MU::synapse0x7017290() {
   return (neuron0x7016980()*-0.639113);
}

double MLP_Higgs_vs_zz_MU::synapse0x7017610() {
   return (neuron0x7015950()*-1.3944);
}

double MLP_Higgs_vs_zz_MU::synapse0x7017650() {
   return (neuron0x7015cc0()*-0.296985);
}

double MLP_Higgs_vs_zz_MU::synapse0x7017690() {
   return (neuron0x7016100()*2.68736);
}

double MLP_Higgs_vs_zz_MU::synapse0x70176d0() {
   return (neuron0x7016540()*-0.67629);
}

double MLP_Higgs_vs_zz_MU::synapse0x7017710() {
   return (neuron0x7016980()*0.648489);
}

double MLP_Higgs_vs_zz_MU::synapse0x7017a90() {
   return (neuron0x7015950()*-0.341995);
}

double MLP_Higgs_vs_zz_MU::synapse0x7017ad0() {
   return (neuron0x7015cc0()*0.761265);
}

double MLP_Higgs_vs_zz_MU::synapse0x7017b10() {
   return (neuron0x7016100()*0.713042);
}

double MLP_Higgs_vs_zz_MU::synapse0x6fb5e30() {
   return (neuron0x7016540()*0.562224);
}

double MLP_Higgs_vs_zz_MU::synapse0x6fedd90() {
   return (neuron0x7016980()*0.89098);
}

double MLP_Higgs_vs_zz_MU::synapse0x70180a0() {
   return (neuron0x7016e50()*-1.14015);
}

double MLP_Higgs_vs_zz_MU::synapse0x70180e0() {
   return (neuron0x70172d0()*1.99687);
}

double MLP_Higgs_vs_zz_MU::synapse0x7018120() {
   return (neuron0x7017750()*-1.41403);
}

