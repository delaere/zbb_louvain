#include "MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR-3-9_500_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3,double in4,double in5,double in6) {
   input0 = (in0 - 19.6877)/1.00516;
   input1 = (in1 - 20.3334)/0.841532;
   input2 = (in2 - 24.7404)/1.53228;
   input3 = (in3 - 13.1628)/1.41155;
   input4 = (in4 - 7.80632)/30.3041;
   input5 = (in5 - 1.82521)/0.806727;
   input6 = (in6 - 2.01039)/0.715387;
   switch(index) {
     case 0:
         return neuron0x26f17d80();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 19.6877)/1.00516;
   input1 = (input[1] - 20.3334)/0.841532;
   input2 = (input[2] - 24.7404)/1.53228;
   input3 = (input[3] - 13.1628)/1.41155;
   input4 = (input[4] - 7.80632)/30.3041;
   input5 = (input[5] - 1.82521)/0.806727;
   input6 = (input[6] - 2.01039)/0.715387;
   switch(index) {
     case 0:
         return neuron0x26f17d80();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f131d0() {
   return input0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f13480() {
   return input1;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f137c0() {
   return input2;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f13b00() {
   return input3;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f13e40() {
   return input4;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f14180() {
   return input5;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f144c0() {
   return input6;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f14930() {
   double input = -0.0791932;
   input += synapse0x26f14be0();
   input += synapse0x26f14c20();
   input += synapse0x26f14c60();
   input += synapse0x26f14ca0();
   input += synapse0x26f14ce0();
   input += synapse0x26f14d20();
   input += synapse0x26f14d60();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f14930() {
   double input = input0x26f14930();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f14da0() {
   double input = 0.832154;
   input += synapse0x26f150e0();
   input += synapse0x26f15120();
   input += synapse0x26f15160();
   input += synapse0x26f151a0();
   input += synapse0x26f151e0();
   input += synapse0x26f15220();
   input += synapse0x26f15260();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f14da0() {
   double input = input0x26f14da0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f152a0() {
   double input = -0.290078;
   input += synapse0x26f155e0();
   input += synapse0x26f15620();
   input += synapse0x26f15660();
   input += synapse0x1a95d2c0();
   input += synapse0x1a95d300();
   input += synapse0x26f157b0();
   input += synapse0x26f157f0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f152a0() {
   double input = input0x26f152a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f15830() {
   double input = -0.747521;
   input += synapse0x26f15b70();
   input += synapse0x26f15bb0();
   input += synapse0x26f15bf0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f15830() {
   double input = input0x26f15830();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f15c30() {
   double input = -0.364505;
   input += synapse0x26f15f70();
   input += synapse0x26f15fb0();
   input += synapse0x26f15ff0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f15c30() {
   double input = input0x26f15c30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f16030() {
   double input = 0.245571;
   input += synapse0x26f16370();
   input += synapse0x26f163b0();
   input += synapse0x26f163f0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f16030() {
   double input = input0x26f16030();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f16430() {
   double input = 0.377598;
   input += synapse0x26f16770();
   input += synapse0x26f167b0();
   input += synapse0x26f167f0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f16430() {
   double input = input0x26f16430();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f16a40() {
   double input = 0.0748596;
   input += synapse0x26f16d80();
   input += synapse0x26f16dc0();
   input += synapse0x26f16e00();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f16a40() {
   double input = input0x26f16a40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f16e40() {
   double input = 1.83033;
   input += synapse0x26f17180();
   input += synapse0x26f171c0();
   input += synapse0x26f17200();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f16e40() {
   double input = input0x26f16e40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f17240() {
   double input = -0.190767;
   input += synapse0x1a95d710();
   input += synapse0x26eb4fd0();
   input += synapse0x1a95d110();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f17240() {
   double input = input0x26f17240();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f17580() {
   double input = 0.197151;
   input += synapse0x26f178c0();
   input += synapse0x26f17900();
   input += synapse0x26f17940();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f17580() {
   double input = input0x26f17580();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f17980() {
   double input = 0.590029;
   input += synapse0x26f17cc0();
   input += synapse0x26f17d00();
   input += synapse0x26f17d40();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f17980() {
   double input = input0x26f17980();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x26f17d80() {
   double input = 0.741835;
   input += synapse0x26f180c0();
   input += synapse0x26f18100();
   input += synapse0x26f18140();
   input += synapse0x26f18180();
   input += synapse0x26f181c0();
   input += synapse0x26f18200();
   input += synapse0x26f18240();
   input += synapse0x26f18280();
   input += synapse0x26f182c0();
   return input;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x26f17d80() {
   double input = input0x26f17d80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f14be0() {
   return (neuron0x26f131d0()*-0.217271);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f14c20() {
   return (neuron0x26f13480()*-0.293244);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f14c60() {
   return (neuron0x26f137c0()*0.0372355);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f14ca0() {
   return (neuron0x26f13b00()*0.684313);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f14ce0() {
   return (neuron0x26f13e40()*-0.708682);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f14d20() {
   return (neuron0x26f14180()*-0.254362);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f14d60() {
   return (neuron0x26f144c0()*-0.124115);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f150e0() {
   return (neuron0x26f131d0()*-0.709187);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15120() {
   return (neuron0x26f13480()*-1.18048);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15160() {
   return (neuron0x26f137c0()*3.67021);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f151a0() {
   return (neuron0x26f13b00()*-1.10393);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f151e0() {
   return (neuron0x26f13e40()*0.985699);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15220() {
   return (neuron0x26f14180()*-0.0406826);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15260() {
   return (neuron0x26f144c0()*-0.795947);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f155e0() {
   return (neuron0x26f131d0()*-0.46398);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15620() {
   return (neuron0x26f13480()*-0.10932);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15660() {
   return (neuron0x26f137c0()*1.53969);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1a95d2c0() {
   return (neuron0x26f13b00()*-0.492586);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1a95d300() {
   return (neuron0x26f13e40()*0.71214);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f157b0() {
   return (neuron0x26f14180()*0.201821);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f157f0() {
   return (neuron0x26f144c0()*-0.0263456);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15b70() {
   return (neuron0x26f14930()*1.72136);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15bb0() {
   return (neuron0x26f14da0()*-0.963301);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15bf0() {
   return (neuron0x26f152a0()*1.47649);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15f70() {
   return (neuron0x26f14930()*0.884488);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15fb0() {
   return (neuron0x26f14da0()*-1.07128);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f15ff0() {
   return (neuron0x26f152a0()*1.62929);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f16370() {
   return (neuron0x26f14930()*-1.72888);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f163b0() {
   return (neuron0x26f14da0()*0.0213662);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f163f0() {
   return (neuron0x26f152a0()*-1.95412);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f16770() {
   return (neuron0x26f14930()*-1.47743);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f167b0() {
   return (neuron0x26f14da0()*0.31491);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f167f0() {
   return (neuron0x26f152a0()*-1.63441);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f16d80() {
   return (neuron0x26f14930()*0.21085);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f16dc0() {
   return (neuron0x26f14da0()*-0.446804);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f16e00() {
   return (neuron0x26f152a0()*0.842039);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f17180() {
   return (neuron0x26f14930()*-2.52132);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f171c0() {
   return (neuron0x26f14da0()*3.2338);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f17200() {
   return (neuron0x26f152a0()*-4.40572);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1a95d710() {
   return (neuron0x26f14930()*1.78929);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26eb4fd0() {
   return (neuron0x26f14da0()*0.0736811);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1a95d110() {
   return (neuron0x26f152a0()*1.95629);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f178c0() {
   return (neuron0x26f14930()*0.840356);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f17900() {
   return (neuron0x26f14da0()*-0.459371);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f17940() {
   return (neuron0x26f152a0()*1.39455);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f17cc0() {
   return (neuron0x26f14930()*-1.03629);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f17d00() {
   return (neuron0x26f14da0()*0.503676);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f17d40() {
   return (neuron0x26f152a0()*-1.58736);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f180c0() {
   return (neuron0x26f15830()*-2.40138);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f18100() {
   return (neuron0x26f15c30()*-2.07782);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f18140() {
   return (neuron0x26f16030()*3.3634);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f18180() {
   return (neuron0x26f16430()*2.02871);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f181c0() {
   return (neuron0x26f16a40()*-1.21972);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f18200() {
   return (neuron0x26f16e40()*6.27032);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f18240() {
   return (neuron0x26f17240()*-3.40602);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f18280() {
   return (neuron0x26f17580()*-1.24328);
}

double MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR_3_9_500_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x26f182c0() {
   return (neuron0x26f17980()*1.39809);
}

