#include "MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index,double in0,double in1,double in2,double in3,double in4,double in5) {
   input0 = (in0 - 21.226)/1.24166;
   input1 = (in1 - 10.9087)/1.03117;
   input2 = (in2 - 24.8606)/1.19624;
   input3 = (in3 - 13.2278)/1.29862;
   input4 = (in4 - 8.4161)/32.0247;
   input5 = (in5 - 1.80644)/0.815831;
   switch(index) {
     case 0:
         return neuron0x1dcb0ad0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::Value(int index, double* input) {
   input0 = (input[0] - 21.226)/1.24166;
   input1 = (input[1] - 10.9087)/1.03117;
   input2 = (input[2] - 24.8606)/1.19624;
   input3 = (input[3] - 13.2278)/1.29862;
   input4 = (input[4] - 8.4161)/32.0247;
   input5 = (input[5] - 1.80644)/0.815831;
   switch(index) {
     case 0:
         return neuron0x1dcb0ad0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcaccc0() {
   return input0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcad000() {
   return input1;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcad340() {
   return input2;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcad680() {
   return input3;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcad9c0() {
   return input4;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcadd00() {
   return input5;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1dcae170() {
   double input = -0.566393;
   input += synapse0x1dbfa800();
   input += synapse0x1dc9bf30();
   input += synapse0x1dcae420();
   input += synapse0x1dcae460();
   input += synapse0x1dcae4a0();
   input += synapse0x1dcae4e0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcae170() {
   double input = input0x1dcae170();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1dcae520() {
   double input = -0.64416;
   input += synapse0x1dcae860();
   input += synapse0x1dcae8a0();
   input += synapse0x1dcae8e0();
   input += synapse0x1dcae920();
   input += synapse0x1dcae960();
   input += synapse0x1dcae9a0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcae520() {
   double input = input0x1dcae520();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1dcae9e0() {
   double input = 0.330788;
   input += synapse0x1dcaed20();
   input += synapse0x1dcaed60();
   input += synapse0x1dcaeda0();
   input += synapse0x1dcaede0();
   input += synapse0x1dcaee20();
   input += synapse0x1dbfa770();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcae9e0() {
   double input = input0x1dcae9e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1dcaef70() {
   double input = 0.441;
   input += synapse0x1dbfa7b0();
   input += synapse0x1dcaf2b0();
   input += synapse0x1dcaf2f0();
   input += synapse0x1dcaf330();
   input += synapse0x1dcaf370();
   input += synapse0x1dcaf3b0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcaef70() {
   double input = input0x1dcaef70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1dcaf3f0() {
   double input = 0.765082;
   input += synapse0x1dcaf730();
   input += synapse0x1dcaf770();
   input += synapse0x1dcaf7b0();
   input += synapse0x1dcaf7f0();
   input += synapse0x1dcaf830();
   input += synapse0x1dcaf870();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcaf3f0() {
   double input = input0x1dcaf3f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1dcaf8b0() {
   double input = -4.36451;
   input += synapse0x1dcafbf0();
   input += synapse0x1dcafc30();
   input += synapse0x1dcafc70();
   input += synapse0x1dc9c040();
   input += synapse0x1dc0a530();
   input += synapse0x1dbfab50();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcaf8b0() {
   double input = input0x1dcaf8b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1dcafec0() {
   double input = -0.362429;
   input += synapse0x1dcaeef0();
   input += synapse0x1dcaef30();
   input += synapse0x1dcb0050();
   input += synapse0x1dcb0090();
   input += synapse0x1dcb00d0();
   input += synapse0x1dcb0110();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcafec0() {
   double input = input0x1dcafec0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1dcb0150() {
   double input = -3.20514;
   input += synapse0x1dcb0490();
   input += synapse0x1dcb04d0();
   input += synapse0x1dcb0510();
   input += synapse0x1dcb0550();
   input += synapse0x1dcb0590();
   input += synapse0x1dcb05d0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcb0150() {
   double input = input0x1dcb0150();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1dcb0610() {
   double input = -0.478475;
   input += synapse0x1dcb0950();
   input += synapse0x1dcb0990();
   input += synapse0x1dcb09d0();
   input += synapse0x1dcb0a10();
   input += synapse0x1dcb0a50();
   input += synapse0x1dcb0a90();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcb0610() {
   double input = input0x1dcb0610();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::input0x1dcb0ad0() {
   double input = 0.686873;
   input += synapse0x1dcb0cf0();
   input += synapse0x1dcb0d30();
   input += synapse0x1dcb0d70();
   input += synapse0x1dcb0db0();
   input += synapse0x1dcb0df0();
   input += synapse0x1dcb0e30();
   input += synapse0x1dcb0e70();
   input += synapse0x1dcb0eb0();
   input += synapse0x1dcb0ef0();
   return input;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::neuron0x1dcb0ad0() {
   double input = input0x1dcb0ad0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dbfa800() {
   return (neuron0x1dcaccc0()*-0.126561);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dc9bf30() {
   return (neuron0x1dcad000()*-0.246783);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcae420() {
   return (neuron0x1dcad340()*0.414073);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcae460() {
   return (neuron0x1dcad680()*-0.285194);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcae4a0() {
   return (neuron0x1dcad9c0()*-0.222319);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcae4e0() {
   return (neuron0x1dcadd00()*-0.411402);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcae860() {
   return (neuron0x1dcaccc0()*-0.633385);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcae8a0() {
   return (neuron0x1dcad000()*-0.40439);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcae8e0() {
   return (neuron0x1dcad340()*1.04567);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcae920() {
   return (neuron0x1dcad680()*-2.95414);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcae960() {
   return (neuron0x1dcad9c0()*-0.298041);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcae9a0() {
   return (neuron0x1dcadd00()*0.370507);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaed20() {
   return (neuron0x1dcaccc0()*-0.26742);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaed60() {
   return (neuron0x1dcad000()*-0.124502);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaeda0() {
   return (neuron0x1dcad340()*-0.685238);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaede0() {
   return (neuron0x1dcad680()*1.77335);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaee20() {
   return (neuron0x1dcad9c0()*0.576958);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dbfa770() {
   return (neuron0x1dcadd00()*-0.213641);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dbfa7b0() {
   return (neuron0x1dcaccc0()*0.135909);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaf2b0() {
   return (neuron0x1dcad000()*0.0309498);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaf2f0() {
   return (neuron0x1dcad340()*-0.204472);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaf330() {
   return (neuron0x1dcad680()*-0.287807);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaf370() {
   return (neuron0x1dcad9c0()*-0.155076);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaf3b0() {
   return (neuron0x1dcadd00()*-0.287008);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaf730() {
   return (neuron0x1dcaccc0()*-1.20315);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaf770() {
   return (neuron0x1dcad000()*0.452141);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaf7b0() {
   return (neuron0x1dcad340()*-0.601491);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaf7f0() {
   return (neuron0x1dcad680()*-1.18633);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaf830() {
   return (neuron0x1dcad9c0()*-0.60432);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaf870() {
   return (neuron0x1dcadd00()*-0.15516);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcafbf0() {
   return (neuron0x1dcaccc0()*-0.426349);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcafc30() {
   return (neuron0x1dcad000()*-2.49766);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcafc70() {
   return (neuron0x1dcad340()*1.99126);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dc9c040() {
   return (neuron0x1dcad680()*1.0297);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dc0a530() {
   return (neuron0x1dcad9c0()*-0.144313);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dbfab50() {
   return (neuron0x1dcadd00()*0.541006);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaeef0() {
   return (neuron0x1dcaccc0()*0.121397);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcaef30() {
   return (neuron0x1dcad000()*-0.235707);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0050() {
   return (neuron0x1dcad340()*0.154195);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0090() {
   return (neuron0x1dcad680()*-1.33835);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb00d0() {
   return (neuron0x1dcad9c0()*-0.574202);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0110() {
   return (neuron0x1dcadd00()*0.532217);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0490() {
   return (neuron0x1dcaccc0()*1.14769);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb04d0() {
   return (neuron0x1dcad000()*0.731311);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0510() {
   return (neuron0x1dcad340()*0.246479);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0550() {
   return (neuron0x1dcad680()*-2.87691);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0590() {
   return (neuron0x1dcad9c0()*0.102693);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb05d0() {
   return (neuron0x1dcadd00()*-0.277343);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0950() {
   return (neuron0x1dcaccc0()*0.0110437);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0990() {
   return (neuron0x1dcad000()*-0.492624);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb09d0() {
   return (neuron0x1dcad340()*0.804748);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0a10() {
   return (neuron0x1dcad680()*-0.316554);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0a50() {
   return (neuron0x1dcad9c0()*-0.0833357);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0a90() {
   return (neuron0x1dcadd00()*-0.301951);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0cf0() {
   return (neuron0x1dcae170()*-0.379318);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0d30() {
   return (neuron0x1dcae520()*1.23547);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0d70() {
   return (neuron0x1dcae9e0()*-0.727572);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0db0() {
   return (neuron0x1dcaef70()*0.399726);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0df0() {
   return (neuron0x1dcaf3f0()*-1.24247);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0e30() {
   return (neuron0x1dcaf8b0()*-3.7156);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0e70() {
   return (neuron0x1dcafec0()*0.486469);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0eb0() {
   return (neuron0x1dcb0150()*2.99347);
}

double MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20::synapse0x1dcb0ef0() {
   return (neuron0x1dcb0610()*-0.600311);
}

