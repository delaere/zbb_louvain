#include "MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.500017)/0.25242;
   input1 = (in1 - 0.592179)/0.338539;
   input2 = (in2 - 0.679468)/0.281065;
   switch(index) {
     case 0:
         return neuron0x2923b480();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::Value(int index, double* input) {
   input0 = (input[0] - 0.500017)/0.25242;
   input1 = (input[1] - 0.592179)/0.338539;
   input2 = (input[2] - 0.679468)/0.281065;
   switch(index) {
     case 0:
         return neuron0x2923b480();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x292375e0() {
   return input0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x29237890() {
   return input1;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x29237bd0() {
   return input2;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x29238040() {
   double input = -3.54726;
   input += synapse0x29226a10();
   input += synapse0x29226a50();
   input += synapse0x292382f0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x29238040() {
   double input = input0x29238040();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x29238330() {
   double input = -0.0812031;
   input += synapse0x29238670();
   input += synapse0x292386b0();
   input += synapse0x292386f0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x29238330() {
   double input = input0x29238330();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x29238730() {
   double input = 1.67389;
   input += synapse0x29238a70();
   input += synapse0x29238ab0();
   input += synapse0x29238af0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x29238730() {
   double input = input0x29238730();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x29238b30() {
   double input = -1.79907;
   input += synapse0x29238e70();
   input += synapse0x29238eb0();
   input += synapse0x29238ef0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x29238b30() {
   double input = input0x29238b30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x29238f30() {
   double input = 1.17917;
   input += synapse0x29239270();
   input += synapse0x292392b0();
   input += synapse0x292392f0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x29238f30() {
   double input = input0x29238f30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x29239330() {
   double input = -1.87417;
   input += synapse0x29239670();
   input += synapse0x292396b0();
   input += synapse0x291cba60();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x29239330() {
   double input = input0x29239330();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x29239800() {
   double input = -0.140583;
   input += synapse0x291cbaa0();
   input += synapse0x29239b40();
   input += synapse0x29239b80();
   input += synapse0x29239bc0();
   input += synapse0x29239c00();
   input += synapse0x29239c40();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x29239800() {
   double input = input0x29239800();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x29239c80() {
   double input = -0.00171116;
   input += synapse0x29239fc0();
   input += synapse0x2923a000();
   input += synapse0x2923a040();
   input += synapse0x2923a080();
   input += synapse0x2923a0c0();
   input += synapse0x2923a100();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x29239c80() {
   double input = input0x29239c80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x2923a140() {
   double input = -0.196101;
   input += synapse0x2923a480();
   input += synapse0x2923a4c0();
   input += synapse0x2923a500();
   input += synapse0x291cbe70();
   input += synapse0x291cbf50();
   input += synapse0x291cbf90();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x2923a140() {
   double input = input0x2923a140();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x2923a750() {
   double input = 0.039299;
   input += synapse0x29239780();
   input += synapse0x292397c0();
   input += synapse0x2923aa00();
   input += synapse0x2923aa40();
   input += synapse0x2923aa80();
   input += synapse0x2923aac0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x2923a750() {
   double input = input0x2923a750();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x2923ab00() {
   double input = 0.0163075;
   input += synapse0x2923ae40();
   input += synapse0x2923ae80();
   input += synapse0x2923aec0();
   input += synapse0x2923af00();
   input += synapse0x2923af40();
   input += synapse0x2923af80();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x2923ab00() {
   double input = input0x2923ab00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x2923afc0() {
   double input = 0.106204;
   input += synapse0x2923b300();
   input += synapse0x2923b340();
   input += synapse0x2923b380();
   input += synapse0x2923b3c0();
   input += synapse0x2923b400();
   input += synapse0x2923b440();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x2923afc0() {
   double input = input0x2923afc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::input0x2923b480() {
   double input = 0.488792;
   input += synapse0x29237f10();
   input += synapse0x29237fe0();
   input += synapse0x2923b730();
   input += synapse0x2923b770();
   input += synapse0x2923b7b0();
   input += synapse0x2923b7f0();
   return input;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::neuron0x2923b480() {
   double input = input0x2923b480();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29226a10() {
   return (neuron0x292375e0()*-1.82401);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29226a50() {
   return (neuron0x29237890()*-0.246655);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x292382f0() {
   return (neuron0x29237bd0()*0.0696949);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29238670() {
   return (neuron0x292375e0()*0.0395607);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x292386b0() {
   return (neuron0x29237890()*0.784165);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x292386f0() {
   return (neuron0x29237bd0()*0.0522537);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29238a70() {
   return (neuron0x292375e0()*-0.894786);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29238ab0() {
   return (neuron0x29237890()*1.72249);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29238af0() {
   return (neuron0x29237bd0()*0.221621);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29238e70() {
   return (neuron0x292375e0()*0.770492);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29238eb0() {
   return (neuron0x29237890()*0.138352);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29238ef0() {
   return (neuron0x29237bd0()*0.232703);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29239270() {
   return (neuron0x292375e0()*0.150702);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x292392b0() {
   return (neuron0x29237890()*0.452883);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x292392f0() {
   return (neuron0x29237bd0()*0.0777144);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29239670() {
   return (neuron0x292375e0()*0.744193);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x292396b0() {
   return (neuron0x29237890()*-0.0841958);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x291cba60() {
   return (neuron0x29237bd0()*0.16081);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x291cbaa0() {
   return (neuron0x29238040()*1.83441);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29239b40() {
   return (neuron0x29238330()*0.580619);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29239b80() {
   return (neuron0x29238730()*-0.8446);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29239bc0() {
   return (neuron0x29238b30()*-1.38016);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29239c00() {
   return (neuron0x29238f30()*1.3331);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29239c40() {
   return (neuron0x29239330()*-1.06921);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29239fc0() {
   return (neuron0x29238040()*-1.14034);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923a000() {
   return (neuron0x29238330()*-1.23978);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923a040() {
   return (neuron0x29238730()*0.741657);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923a080() {
   return (neuron0x29238b30()*1.58621);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923a0c0() {
   return (neuron0x29238f30()*-1.25438);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923a100() {
   return (neuron0x29239330()*1.51565);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923a480() {
   return (neuron0x29238040()*-1.34674);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923a4c0() {
   return (neuron0x29238330()*-0.194419);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923a500() {
   return (neuron0x29238730()*0.560091);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x291cbe70() {
   return (neuron0x29238b30()*0.940709);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x291cbf50() {
   return (neuron0x29238f30()*-0.287631);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x291cbf90() {
   return (neuron0x29239330()*0.825554);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29239780() {
   return (neuron0x29238040()*-1.04247);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x292397c0() {
   return (neuron0x29238330()*-0.51005);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923aa00() {
   return (neuron0x29238730()*0.0959321);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923aa40() {
   return (neuron0x29238b30()*0.338553);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923aa80() {
   return (neuron0x29238f30()*-0.679893);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923aac0() {
   return (neuron0x29239330()*1.30021);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923ae40() {
   return (neuron0x29238040()*-0.162993);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923ae80() {
   return (neuron0x29238330()*-0.643888);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923aec0() {
   return (neuron0x29238730()*1.2564);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923af00() {
   return (neuron0x29238b30()*0.60598);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923af40() {
   return (neuron0x29238f30()*-0.184876);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923af80() {
   return (neuron0x29239330()*0.071494);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923b300() {
   return (neuron0x29238040()*1.39966);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923b340() {
   return (neuron0x29238330()*0.565472);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923b380() {
   return (neuron0x29238730()*-1.01402);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923b3c0() {
   return (neuron0x29238b30()*-1.65903);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923b400() {
   return (neuron0x29238f30()*1.32508);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923b440() {
   return (neuron0x29239330()*-0.963351);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29237f10() {
   return (neuron0x29239800()*-4.76678);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x29237fe0() {
   return (neuron0x29239c80()*5.55044);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923b730() {
   return (neuron0x2923a140()*2.07243);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923b770() {
   return (neuron0x2923a750()*1.75912);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923b7b0() {
   return (neuron0x2923ab00()*1.00721);
}

double MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3::synapse0x2923b7f0() {
   return (neuron0x2923afc0()*-3.82828);
}

