#include "MLP_Higgs_vs_zbb_MU.h"
#include <cmath>

double MLP_Higgs_vs_zbb_MU::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.8379)/1.06876;
   input1 = (in1 - 20.4191)/0.934631;
   input2 = (in2 - 24.4183)/1.24436;
   input3 = (in3 - 12.966)/1.29195;
   switch(index) {
     case 0:
         return neuron0x40442e0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_zbb_MU::Value(int index, double* input) {
   input0 = (input[0] - 19.8379)/1.06876;
   input1 = (input[1] - 20.4191)/0.934631;
   input2 = (input[2] - 24.4183)/1.24436;
   input3 = (input[3] - 12.966)/1.29195;
   switch(index) {
     case 0:
         return neuron0x40442e0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_zbb_MU::neuron0x40416b0() {
   return input0;
}

double MLP_Higgs_vs_zbb_MU::neuron0x40419f0() {
   return input1;
}

double MLP_Higgs_vs_zbb_MU::neuron0x4041d30() {
   return input2;
}

double MLP_Higgs_vs_zbb_MU::neuron0x4042070() {
   return input3;
}

double MLP_Higgs_vs_zbb_MU::input0x40424e0() {
   double input = -0.353083;
   input += synapse0x401a8e0();
   input += synapse0x4042790();
   input += synapse0x40427d0();
   input += synapse0x4042810();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x40424e0() {
   double input = input0x40424e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x4042850() {
   double input = -0.213182;
   input += synapse0x4042b90();
   input += synapse0x4042bd0();
   input += synapse0x4042c10();
   input += synapse0x4042c50();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x4042850() {
   double input = input0x4042850();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x4042c90() {
   double input = 0.338285;
   input += synapse0x4042fd0();
   input += synapse0x4043010();
   input += synapse0x4043050();
   input += synapse0x4043090();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x4042c90() {
   double input = input0x4042c90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x40430d0() {
   double input = 0.127723;
   input += synapse0x4043410();
   input += synapse0x4043450();
   input += synapse0x4043490();
   input += synapse0x40434d0();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x40430d0() {
   double input = input0x40430d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x4043510() {
   double input = 0.00265086;
   input += synapse0x4043850();
   input += synapse0x3f902c0();
   input += synapse0x3f90300();
   input += synapse0x40439a0();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x4043510() {
   double input = input0x4043510();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x40439e0() {
   double input = 0.450185;
   input += synapse0x4043d20();
   input += synapse0x4043d60();
   input += synapse0x4043da0();
   input += synapse0x4043de0();
   input += synapse0x4043e20();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x40439e0() {
   double input = input0x40439e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x4043e60() {
   double input = 0.0916609;
   input += synapse0x40441a0();
   input += synapse0x40441e0();
   input += synapse0x4044220();
   input += synapse0x4044260();
   input += synapse0x40442a0();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x4043e60() {
   double input = input0x4043e60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::input0x40442e0() {
   double input = -0.650335;
   input += synapse0x4044620();
   input += synapse0x4044660();
   return input;
}

double MLP_Higgs_vs_zbb_MU::neuron0x40442e0() {
   double input = input0x40442e0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_zbb_MU::synapse0x401a8e0() {
   return (neuron0x40416b0()*0.404967);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4042790() {
   return (neuron0x40419f0()*-0.713739);
}

double MLP_Higgs_vs_zbb_MU::synapse0x40427d0() {
   return (neuron0x4041d30()*-0.0324895);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4042810() {
   return (neuron0x4042070()*-1.03379);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4042b90() {
   return (neuron0x40416b0()*0.0612294);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4042bd0() {
   return (neuron0x40419f0()*0.69625);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4042c10() {
   return (neuron0x4041d30()*1.40402);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4042c50() {
   return (neuron0x4042070()*0.850449);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4042fd0() {
   return (neuron0x40416b0()*0.21774);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043010() {
   return (neuron0x40419f0()*0.315635);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043050() {
   return (neuron0x4041d30()*-0.257303);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043090() {
   return (neuron0x4042070()*0.0507942);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043410() {
   return (neuron0x40416b0()*-0.733812);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043450() {
   return (neuron0x40419f0()*-0.21069);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043490() {
   return (neuron0x4041d30()*-0.673032);
}

double MLP_Higgs_vs_zbb_MU::synapse0x40434d0() {
   return (neuron0x4042070()*2.35093);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043850() {
   return (neuron0x40416b0()*-0.239168);
}

double MLP_Higgs_vs_zbb_MU::synapse0x3f902c0() {
   return (neuron0x40419f0()*0.252338);
}

double MLP_Higgs_vs_zbb_MU::synapse0x3f90300() {
   return (neuron0x4041d30()*0.587475);
}

double MLP_Higgs_vs_zbb_MU::synapse0x40439a0() {
   return (neuron0x4042070()*0.17702);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043d20() {
   return (neuron0x40424e0()*0.108328);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043d60() {
   return (neuron0x4042850()*-0.232801);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043da0() {
   return (neuron0x4042c90()*0.415953);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043de0() {
   return (neuron0x40430d0()*-0.0576473);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4043e20() {
   return (neuron0x4043510()*-0.413766);
}

double MLP_Higgs_vs_zbb_MU::synapse0x40441a0() {
   return (neuron0x40424e0()*1.35212);
}

double MLP_Higgs_vs_zbb_MU::synapse0x40441e0() {
   return (neuron0x4042850()*0.765008);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4044220() {
   return (neuron0x4042c90()*0.993685);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4044260() {
   return (neuron0x40430d0()*-1.52278);
}

double MLP_Higgs_vs_zbb_MU::synapse0x40442a0() {
   return (neuron0x4043510()*-1.26809);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4044620() {
   return (neuron0x40439e0()*0.563273);
}

double MLP_Higgs_vs_zbb_MU::synapse0x4044660() {
   return (neuron0x4043e60()*1.76549);
}

