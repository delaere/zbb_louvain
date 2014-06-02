#include "MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000.h"
#include <cmath>

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.445235)/0.307413;
   input1 = (in1 - 0.487302)/0.29068;
   input2 = (in2 - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x1de98920();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::Value(int index, double* input) {
   input0 = (input[0] - 0.445235)/0.307413;
   input1 = (input[1] - 0.487302)/0.29068;
   input2 = (input[2] - 0.530975)/0.330691;
   switch(index) {
     case 0:
         return neuron0x1de98920();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de84530() {
   return input0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de84870() {
   return input1;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de95840() {
   return input2;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de95b90() {
   double input = -4.65978;
   input += synapse0x1de4cd00();
   input += synapse0x1de6b290();
   input += synapse0x1de95e40();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de95b90() {
   double input = input0x1de95b90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de95e80() {
   double input = -4.12053;
   input += synapse0x1de961c0();
   input += synapse0x1de96200();
   input += synapse0x1de96240();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de95e80() {
   double input = input0x1de95e80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de96280() {
   double input = 0.189403;
   input += synapse0x1de965c0();
   input += synapse0x1de96600();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de96280() {
   double input = input0x1de96280();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de96640() {
   double input = -0.207938;
   input += synapse0x1de96980();
   input += synapse0x1de969c0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de96640() {
   double input = input0x1de96640();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de96a00() {
   double input = -0.34606;
   input += synapse0x1de96d40();
   input += synapse0x1de96d80();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de96a00() {
   double input = input0x1de96a00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de96dc0() {
   double input = -0.254256;
   input += synapse0x1de97100();
   input += synapse0x1de97140();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de96dc0() {
   double input = input0x1de96dc0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de97180() {
   double input = 0.563476;
   input += synapse0x1de974c0();
   input += synapse0x1de97500();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de97180() {
   double input = input0x1de97180();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de97540() {
   double input = 0.0875851;
   input += synapse0x1de97880();
   input += synapse0x1ddf74a0();
   input += synapse0x1ddf74e0();
   input += synapse0x1de979d0();
   input += synapse0x1de97a10();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de97540() {
   double input = input0x1de97540();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de97a50() {
   double input = -0.287523;
   input += synapse0x1de97d90();
   input += synapse0x1de97dd0();
   input += synapse0x1de97e10();
   input += synapse0x1de97e50();
   input += synapse0x1de97e90();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de97a50() {
   double input = input0x1de97a50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de97ed0() {
   double input = -0.063349;
   input += synapse0x1de98210();
   input += synapse0x1de98250();
   input += synapse0x1de98290();
   input += synapse0x1de982d0();
   input += synapse0x1de98310();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de97ed0() {
   double input = input0x1de97ed0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de98350() {
   double input = -2.69858;
   input += synapse0x1de98690();
   input += synapse0x1de986d0();
   input += synapse0x1de6b330();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de98350() {
   double input = input0x1de98350();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::input0x1de98920() {
   double input = -4.6907;
   input += synapse0x1de95af0();
   return input;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::neuron0x1de98920() {
   double input = input0x1de98920();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de4cd00() {
   return (neuron0x1de84530()*1.36824);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de6b290() {
   return (neuron0x1de84870()*-0.190458);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de95e40() {
   return (neuron0x1de95840()*0.367418);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de961c0() {
   return (neuron0x1de84530()*-1.73995);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de96200() {
   return (neuron0x1de84870()*0.122952);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de96240() {
   return (neuron0x1de95840()*-0.165155);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de965c0() {
   return (neuron0x1de95b90()*-0.134061);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de96600() {
   return (neuron0x1de95e80()*-0.175466);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de96980() {
   return (neuron0x1de95b90()*0.777708);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de969c0() {
   return (neuron0x1de95e80()*-1.61514);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de96d40() {
   return (neuron0x1de95b90()*1.94481);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de96d80() {
   return (neuron0x1de95e80()*-1.96929);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de97100() {
   return (neuron0x1de95b90()*1.98922);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de97140() {
   return (neuron0x1de95e80()*-2.01413);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de974c0() {
   return (neuron0x1de95b90()*-2.67226);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de97500() {
   return (neuron0x1de95e80()*2.03552);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de97880() {
   return (neuron0x1de96280()*0.41126);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1ddf74a0() {
   return (neuron0x1de96640()*-0.612838);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1ddf74e0() {
   return (neuron0x1de96a00()*-1.21539);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de979d0() {
   return (neuron0x1de96dc0()*-0.654902);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de97a10() {
   return (neuron0x1de97180()*1.33093);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de97d90() {
   return (neuron0x1de96280()*0.245568);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de97dd0() {
   return (neuron0x1de96640()*0.905254);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de97e10() {
   return (neuron0x1de96a00()*2.01441);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de97e50() {
   return (neuron0x1de96dc0()*2.53087);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de97e90() {
   return (neuron0x1de97180()*-4.10296);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de98210() {
   return (neuron0x1de96280()*-0.0392889);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de98250() {
   return (neuron0x1de96640()*0.518912);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de98290() {
   return (neuron0x1de96a00()*0.679865);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de982d0() {
   return (neuron0x1de96dc0()*0.7057);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de98310() {
   return (neuron0x1de97180()*-1.58642);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de98690() {
   return (neuron0x1de97540()*-2.35477);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de986d0() {
   return (neuron0x1de97a50()*7.26011);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de6b330() {
   return (neuron0x1de97ed0()*1.63993);
}

double MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000::synapse0x1de95af0() {
   return (neuron0x1de98350()*11.5346);
}

