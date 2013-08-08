#include "MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3,double in4,double in5) {
   input0 = (in0 - 19.3926)/1.0044;
   input1 = (in1 - 19.9308)/0.807903;
   input2 = (in2 - 21.1534)/1.47427;
   input3 = (in3 - 10.8329)/1.15652;
   input4 = (in4 - 10.2844)/32.8326;
   input5 = (in5 - 1.79526)/0.816131;
   switch(index) {
     case 0:
         return neuron0x350f7950();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 19.3926)/1.0044;
   input1 = (input[1] - 19.9308)/0.807903;
   input2 = (input[2] - 21.1534)/1.47427;
   input3 = (input[3] - 10.8329)/1.15652;
   input4 = (input[4] - 10.2844)/32.8326;
   input5 = (input[5] - 1.79526)/0.816131;
   switch(index) {
     case 0:
         return neuron0x350f7950();
     default:
         return 0.;
   }
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f29a0() {
   return input0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f2c50() {
   return input1;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f2f90() {
   return input2;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f32d0() {
   return input3;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f3610() {
   return input4;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f3950() {
   return input5;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f3dc0() {
   double input = 0.160298;
   input += synapse0x350f4070();
   input += synapse0x350f40b0();
   input += synapse0x350f40f0();
   input += synapse0x350f4130();
   input += synapse0x350f4170();
   input += synapse0x350f41b0();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f3dc0() {
   double input = input0x350f3dc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f41f0() {
   double input = -0.216985;
   input += synapse0x350f4530();
   input += synapse0x350f4570();
   input += synapse0x350f45b0();
   input += synapse0x350f45f0();
   input += synapse0x350f4630();
   input += synapse0x350f4670();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f41f0() {
   double input = input0x350f41f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f46b0() {
   double input = 0.976081;
   input += synapse0x350f49f0();
   input += synapse0x350f4a30();
   input += synapse0x350f4a70();
   input += synapse0x350f4ab0();
   input += synapse0x350f4af0();
   input += synapse0x35043ac0();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f46b0() {
   double input = input0x350f46b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f4c40() {
   double input = -0.858104;
   input += synapse0x350f4f80();
   input += synapse0x350f4fc0();
   input += synapse0x350f5000();
   input += synapse0x350f5040();
   input += synapse0x350f5080();
   input += synapse0x350f50c0();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f4c40() {
   double input = input0x350f4c40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f5100() {
   double input = 0.398313;
   input += synapse0x350f5440();
   input += synapse0x350f5480();
   input += synapse0x350f54c0();
   input += synapse0x350f5500();
   input += synapse0x350f5540();
   input += synapse0x350f5580();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f5100() {
   double input = input0x350f5100();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f55c0() {
   double input = -0.295446;
   input += synapse0x350f5900();
   input += synapse0x350f5940();
   input += synapse0x350f5980();
   input += synapse0x35043b00();
   input += synapse0x3509ccc0();
   input += synapse0x35043ef0();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f55c0() {
   double input = input0x350f55c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f5bd0() {
   double input = -0.508062;
   input += synapse0x350f5f10();
   input += synapse0x350f5f50();
   input += synapse0x350f5f90();
   input += synapse0x350f5fd0();
   input += synapse0x350f6010();
   input += synapse0x350f6050();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f5bd0() {
   double input = input0x350f5bd0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f6090() {
   double input = -1.25804;
   input += synapse0x350f63d0();
   input += synapse0x350f6410();
   input += synapse0x350f6450();
   input += synapse0x350f6490();
   input += synapse0x350f64d0();
   input += synapse0x350f6510();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f6090() {
   double input = input0x350f6090();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f6550() {
   double input = 0.613561;
   input += synapse0x350f6890();
   input += synapse0x350f68d0();
   input += synapse0x350f6910();
   input += synapse0x350f6950();
   input += synapse0x350f6990();
   input += synapse0x350f69d0();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f6550() {
   double input = input0x350f6550();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f6a10() {
   double input = 0.322181;
   input += synapse0x350f6d50();
   input += synapse0x350f6d90();
   input += synapse0x350f6dd0();
   input += synapse0x350f6e10();
   input += synapse0x350f6e50();
   input += synapse0x350f6e90();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f6a10() {
   double input = input0x350f6a10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f6ed0() {
   double input = 0.118194;
   input += synapse0x35043910();
   input += synapse0x35043950();
   input += synapse0x35043fd0();
   input += synapse0x35044010();
   input += synapse0x35044050();
   input += synapse0x35044090();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f6ed0() {
   double input = input0x350f6ed0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f59c0() {
   double input = -0.329053;
   input += synapse0x350f77d0();
   input += synapse0x350f7810();
   input += synapse0x350f7850();
   input += synapse0x350f7890();
   input += synapse0x350f78d0();
   input += synapse0x350f7910();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f59c0() {
   double input = input0x350f59c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::input0x350f7950() {
   double input = 0.115615;
   input += synapse0x350f7c90();
   input += synapse0x350f7cd0();
   input += synapse0x350f7d10();
   input += synapse0x350f7d50();
   input += synapse0x350f7d90();
   input += synapse0x350f7dd0();
   input += synapse0x350f7e10();
   input += synapse0x350f7e50();
   input += synapse0x350f7e90();
   input += synapse0x350f7ed0();
   input += synapse0x350f7f10();
   input += synapse0x350f7f50();
   return input;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::neuron0x350f7950() {
   double input = input0x350f7950();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4070() {
   return (neuron0x350f29a0()*-0.31432);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f40b0() {
   return (neuron0x350f2c50()*-0.367962);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f40f0() {
   return (neuron0x350f2f90()*0.0511627);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4130() {
   return (neuron0x350f32d0()*0.475635);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4170() {
   return (neuron0x350f3610()*0.49283);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f41b0() {
   return (neuron0x350f3950()*-0.16639);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4530() {
   return (neuron0x350f29a0()*-0.0901252);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4570() {
   return (neuron0x350f2c50()*0.219055);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f45b0() {
   return (neuron0x350f2f90()*0.0230232);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f45f0() {
   return (neuron0x350f32d0()*-0.561968);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4630() {
   return (neuron0x350f3610()*0.10566);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4670() {
   return (neuron0x350f3950()*-0.425009);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f49f0() {
   return (neuron0x350f29a0()*-0.981285);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4a30() {
   return (neuron0x350f2c50()*-0.598048);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4a70() {
   return (neuron0x350f2f90()*0.0922043);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4ab0() {
   return (neuron0x350f32d0()*1.7487);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4af0() {
   return (neuron0x350f3610()*0.410047);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x35043ac0() {
   return (neuron0x350f3950()*0.401386);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4f80() {
   return (neuron0x350f29a0()*0.987683);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f4fc0() {
   return (neuron0x350f2c50()*0.254622);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5000() {
   return (neuron0x350f2f90()*-0.0434669);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5040() {
   return (neuron0x350f32d0()*-1.54208);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5080() {
   return (neuron0x350f3610()*0.502725);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f50c0() {
   return (neuron0x350f3950()*-0.175024);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5440() {
   return (neuron0x350f29a0()*0.430249);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5480() {
   return (neuron0x350f2c50()*-0.0555825);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f54c0() {
   return (neuron0x350f2f90()*-0.0496314);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5500() {
   return (neuron0x350f32d0()*-0.277336);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5540() {
   return (neuron0x350f3610()*-0.249382);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5580() {
   return (neuron0x350f3950()*-0.309406);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5900() {
   return (neuron0x350f29a0()*-0.023686);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5940() {
   return (neuron0x350f2c50()*0.227811);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5980() {
   return (neuron0x350f2f90()*-0.388208);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x35043b00() {
   return (neuron0x350f32d0()*-0.308062);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x3509ccc0() {
   return (neuron0x350f3610()*0.152196);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x35043ef0() {
   return (neuron0x350f3950()*-0.0928856);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5f10() {
   return (neuron0x350f29a0()*0.250036);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5f50() {
   return (neuron0x350f2c50()*-0.0152426);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5f90() {
   return (neuron0x350f2f90()*0.0204375);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f5fd0() {
   return (neuron0x350f32d0()*-0.519459);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6010() {
   return (neuron0x350f3610()*0.183515);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6050() {
   return (neuron0x350f3950()*-0.381374);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f63d0() {
   return (neuron0x350f29a0()*1.07634);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6410() {
   return (neuron0x350f2c50()*0.185244);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6450() {
   return (neuron0x350f2f90()*-0.0538494);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6490() {
   return (neuron0x350f32d0()*-1.80956);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f64d0() {
   return (neuron0x350f3610()*0.307455);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6510() {
   return (neuron0x350f3950()*-0.00127505);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6890() {
   return (neuron0x350f29a0()*-0.547745);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f68d0() {
   return (neuron0x350f2c50()*1.02157);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6910() {
   return (neuron0x350f2f90()*-0.981821);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6950() {
   return (neuron0x350f32d0()*1.02453);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6990() {
   return (neuron0x350f3610()*0.336625);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f69d0() {
   return (neuron0x350f3950()*-0.829306);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6d50() {
   return (neuron0x350f29a0()*-0.387269);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6d90() {
   return (neuron0x350f2c50()*-0.356806);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6dd0() {
   return (neuron0x350f2f90()*0.610161);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6e10() {
   return (neuron0x350f32d0()*0.158236);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6e50() {
   return (neuron0x350f3610()*0.00755696);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f6e90() {
   return (neuron0x350f3950()*-0.263707);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x35043910() {
   return (neuron0x350f29a0()*-0.28274);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x35043950() {
   return (neuron0x350f2c50()*0.231032);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x35043fd0() {
   return (neuron0x350f2f90()*-0.0622014);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x35044010() {
   return (neuron0x350f32d0()*-0.464265);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x35044050() {
   return (neuron0x350f3610()*-0.0242093);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x35044090() {
   return (neuron0x350f3950()*-0.245147);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f77d0() {
   return (neuron0x350f29a0()*-0.0845056);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7810() {
   return (neuron0x350f2c50()*-0.00865707);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7850() {
   return (neuron0x350f2f90()*-0.530099);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7890() {
   return (neuron0x350f32d0()*0.495103);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f78d0() {
   return (neuron0x350f3610()*-0.249793);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7910() {
   return (neuron0x350f3950()*-0.0650909);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7c90() {
   return (neuron0x350f3dc0()*-0.210485);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7cd0() {
   return (neuron0x350f41f0()*0.226373);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7d10() {
   return (neuron0x350f46b0()*-1.10105);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7d50() {
   return (neuron0x350f4c40()*0.950439);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7d90() {
   return (neuron0x350f5100()*0.216467);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7dd0() {
   return (neuron0x350f55c0()*0.0846223);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7e10() {
   return (neuron0x350f5bd0()*0.0997765);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7e50() {
   return (neuron0x350f6090()*1.13438);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7e90() {
   return (neuron0x350f6550()*-1.08389);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7ed0() {
   return (neuron0x350f6a10()*0.431581);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7f10() {
   return (neuron0x350f6ed0()*0.231566);
}

double MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20::synapse0x350f7f50() {
   return (neuron0x350f59c0()*-0.255982);
}

