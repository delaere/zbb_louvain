#include "MLP_Higgs_vs_bkg_EE_FULLL.h"
#include <cmath>

double MLP_Higgs_vs_bkg_EE_FULLL::Value(int index,double in0,double in1,double in2,double in3,double in4,double in5,double in6) {
   input0 = (in0 - 20.0727)/1.59748;
   input1 = (in1 - 20.7823)/1.0162;
   input2 = (in2 - 21.6177)/2.17535;
   input3 = (in3 - 22.2861)/1.50218;
   input4 = (in4 - 12.0833)/1.83307;
   input5 = (in5 - 25.7269)/2.01147;
   input6 = (in6 - 14.7947)/2.23962;
   switch(index) {
     case 0:
         return neuron0x12b0e7c0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_EE_FULLL::Value(int index, double* input) {
   input0 = (input[0] - 20.0727)/1.59748;
   input1 = (input[1] - 20.7823)/1.0162;
   input2 = (input[2] - 21.6177)/2.17535;
   input3 = (input[3] - 22.2861)/1.50218;
   input4 = (input[4] - 12.0833)/1.83307;
   input5 = (input[5] - 25.7269)/2.01147;
   input6 = (input[6] - 14.7947)/2.23962;
   switch(index) {
     case 0:
         return neuron0x12b0e7c0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0b8f0() {
   return input0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0bc00() {
   return input1;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0bf10() {
   return input2;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0c220() {
   return input3;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0c530() {
   return input4;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0c870() {
   return input5;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0cbb0() {
   return input6;
}

double MLP_Higgs_vs_bkg_EE_FULLL::input0x12b0d030() {
   double input = 0.732919;
   input += synapse0x12a729f0();
   input += synapse0x12b0d2b0();
   input += synapse0x12b0d2f0();
   input += synapse0x12b0d330();
   input += synapse0x12b0d370();
   input += synapse0x12b0d3b0();
   input += synapse0x12b0d3f0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0d030() {
   double input = input0x12b0d030();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::input0x12b0d430() {
   double input = 3.22867;
   input += synapse0x12b0d740();
   input += synapse0x12b0d780();
   input += synapse0x12b0d7c0();
   input += synapse0x12b0d800();
   input += synapse0x12b0d840();
   input += synapse0x12b0d880();
   input += synapse0x12b0d8c0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0d430() {
   double input = input0x12b0d430();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::input0x12b0d900() {
   double input = 4.55916;
   input += synapse0x12b0dc10();
   input += synapse0x12b0dc50();
   input += synapse0x12b0dc90();
   input += synapse0x1250e4f0();
   input += synapse0x1250e530();
   input += synapse0x12b0dde0();
   input += synapse0x12b0de20();
   return input;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0d900() {
   double input = input0x12b0d900();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::input0x12b0de60() {
   double input = 0.693358;
   input += synapse0x12b0e170();
   input += synapse0x12b0e1b0();
   input += synapse0x12b0e1f0();
   input += synapse0x12b0e230();
   input += synapse0x12b0e270();
   input += synapse0x12b0e2b0();
   input += synapse0x12b0e2f0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0de60() {
   double input = input0x12b0de60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::input0x12b0e330() {
   double input = 4.73303;
   input += synapse0x12b0e640();
   input += synapse0x12b0e680();
   input += synapse0x12b0e6c0();
   input += synapse0x12b0e700();
   input += synapse0x12b0e740();
   input += synapse0x12a72860();
   input += synapse0x12a72550();
   return input;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0e330() {
   double input = input0x12b0e330();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::input0x12b0e990() {
   double input = 5.48043;
   input += synapse0x12a72590();
   input += synapse0x12b0eca0();
   input += synapse0x12b0ece0();
   input += synapse0x12b0ed20();
   input += synapse0x12b0ed60();
   input += synapse0x12b0eda0();
   input += synapse0x12b0ede0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0e990() {
   double input = input0x12b0e990();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::input0x12b0ee20() {
   double input = -3.86267;
   input += synapse0x12b0f130();
   input += synapse0x12b0f170();
   input += synapse0x12b0f1b0();
   input += synapse0x12b0f1f0();
   input += synapse0x12b0f230();
   input += synapse0x12b0f270();
   input += synapse0x12b0f2b0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0ee20() {
   double input = input0x12b0ee20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::input0x12b0f2f0() {
   double input = 1.96949;
   input += synapse0x12b0f630();
   input += synapse0x12b0f670();
   input += synapse0x12b0f6b0();
   input += synapse0x12b0f6f0();
   input += synapse0x12b0f730();
   input += synapse0x12b0f770();
   input += synapse0x12b0f7b0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0f2f0() {
   double input = input0x12b0f2f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::input0x12b0f7f0() {
   double input = 0.469845;
   input += synapse0x12b0fb30();
   input += synapse0x12b0fb70();
   input += synapse0x12b0fbb0();
   input += synapse0x12b0fbf0();
   input += synapse0x12b0fc30();
   input += synapse0x12b0fc70();
   input += synapse0x12b0fcb0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0f7f0() {
   double input = input0x12b0f7f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::input0x12b0fcf0() {
   double input = -0.192853;
   input += synapse0x1250e340();
   input += synapse0x1250e380();
   input += synapse0x12a72b80();
   input += synapse0x12a72bc0();
   input += synapse0x12a72c00();
   input += synapse0x12a72c40();
   input += synapse0x12b0e780();
   return input;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0fcf0() {
   double input = input0x12b0fcf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::input0x12b0e7c0() {
   double input = 1.00216;
   input += synapse0x12b0e950();
   input += synapse0x12b104d0();
   input += synapse0x12b10510();
   return input;
}

double MLP_Higgs_vs_bkg_EE_FULLL::neuron0x12b0e7c0() {
   double input = input0x12b0e7c0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12a729f0() {
   return (neuron0x12b0b8f0()*-0.21527);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d2b0() {
   return (neuron0x12b0bc00()*1.82);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d2f0() {
   return (neuron0x12b0bf10()*-0.433492);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d330() {
   return (neuron0x12b0c220()*-0.995098);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d370() {
   return (neuron0x12b0c530()*2.77812);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d3b0() {
   return (neuron0x12b0c870()*-0.505798);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d3f0() {
   return (neuron0x12b0cbb0()*2.29401);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d740() {
   return (neuron0x12b0b8f0()*4.9281);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d780() {
   return (neuron0x12b0bc00()*2.01155);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d7c0() {
   return (neuron0x12b0bf10()*-3.88596);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d800() {
   return (neuron0x12b0c220()*2.82687);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d840() {
   return (neuron0x12b0c530()*-1.90646);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d880() {
   return (neuron0x12b0c870()*-6.96748);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0d8c0() {
   return (neuron0x12b0cbb0()*1.80914);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0dc10() {
   return (neuron0x12b0b8f0()*0.517705);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0dc50() {
   return (neuron0x12b0bc00()*-0.0889806);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0dc90() {
   return (neuron0x12b0bf10()*0.37792);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x1250e4f0() {
   return (neuron0x12b0c220()*1.84586);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x1250e530() {
   return (neuron0x12b0c530()*-0.0968734);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0dde0() {
   return (neuron0x12b0c870()*-6.31012);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0de20() {
   return (neuron0x12b0cbb0()*1.68235);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e170() {
   return (neuron0x12b0b8f0()*1.92298);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e1b0() {
   return (neuron0x12b0bc00()*-1.39013);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e1f0() {
   return (neuron0x12b0bf10()*-3.50486);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e230() {
   return (neuron0x12b0c220()*4.08507);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e270() {
   return (neuron0x12b0c530()*-2.98865);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e2b0() {
   return (neuron0x12b0c870()*-2.52537);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e2f0() {
   return (neuron0x12b0cbb0()*0.186474);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e640() {
   return (neuron0x12b0b8f0()*0.994323);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e680() {
   return (neuron0x12b0bc00()*1.53798);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e6c0() {
   return (neuron0x12b0bf10()*2.82056);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e700() {
   return (neuron0x12b0c220()*-3.50005);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e740() {
   return (neuron0x12b0c530()*3.02113);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12a72860() {
   return (neuron0x12b0c870()*-0.43073);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12a72550() {
   return (neuron0x12b0cbb0()*0.272869);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12a72590() {
   return (neuron0x12b0b8f0()*3.2244);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0eca0() {
   return (neuron0x12b0bc00()*-3.24085);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0ece0() {
   return (neuron0x12b0bf10()*5.28314);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0ed20() {
   return (neuron0x12b0c220()*1.60439);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0ed60() {
   return (neuron0x12b0c530()*-1.13558);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0eda0() {
   return (neuron0x12b0c870()*0.0681698);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0ede0() {
   return (neuron0x12b0cbb0()*2.36693);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f130() {
   return (neuron0x12b0b8f0()*-0.145755);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f170() {
   return (neuron0x12b0bc00()*1.53235);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f1b0() {
   return (neuron0x12b0bf10()*-0.220154);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f1f0() {
   return (neuron0x12b0c220()*-0.867376);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f230() {
   return (neuron0x12b0c530()*0.334087);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f270() {
   return (neuron0x12b0c870()*-0.471698);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f2b0() {
   return (neuron0x12b0cbb0()*-2.68669);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f630() {
   return (neuron0x12b0d030()*1.45494);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f670() {
   return (neuron0x12b0d430()*-2.20046);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f6b0() {
   return (neuron0x12b0d900()*-4.38025);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f6f0() {
   return (neuron0x12b0de60()*2.30953);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f730() {
   return (neuron0x12b0e330()*6.82828);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f770() {
   return (neuron0x12b0e990()*-3.93885);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0f7b0() {
   return (neuron0x12b0ee20()*-5.26886);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0fb30() {
   return (neuron0x12b0d030()*0.347289);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0fb70() {
   return (neuron0x12b0d430()*-0.436667);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0fbb0() {
   return (neuron0x12b0d900()*-3.24497);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0fbf0() {
   return (neuron0x12b0de60()*0.782826);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0fc30() {
   return (neuron0x12b0e330()*3.38338);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0fc70() {
   return (neuron0x12b0e990()*-1.19002);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0fcb0() {
   return (neuron0x12b0ee20()*-0.849487);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x1250e340() {
   return (neuron0x12b0d030()*-0.577878);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x1250e380() {
   return (neuron0x12b0d430()*1.727);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12a72b80() {
   return (neuron0x12b0d900()*-3.91606);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12a72bc0() {
   return (neuron0x12b0de60()*-0.501731);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12a72c00() {
   return (neuron0x12b0e330()*2.11047);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12a72c40() {
   return (neuron0x12b0e990()*0.0204437);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e780() {
   return (neuron0x12b0ee20()*1.62897);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b0e950() {
   return (neuron0x12b0f2f0()*-2.37893);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b104d0() {
   return (neuron0x12b0f7f0()*2.56698);
}

double MLP_Higgs_vs_bkg_EE_FULLL::synapse0x12b10510() {
   return (neuron0x12b0fcf0()*-1.21058);
}

