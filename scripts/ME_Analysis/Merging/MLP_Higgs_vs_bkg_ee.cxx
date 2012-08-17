#include "MLP_Higgs_vs_bkg_EE_TIGHT.h"
#include <cmath>

double MLP_Higgs_vs_bkg_EE_TIGHT::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 0.370858)/0.320569;
   input1 = (in1 - 0.404877)/0.337655;
   input2 = (in2 - 0.320068)/0.333628;
   input3 = (in3 - 20.0727)/1.59748;
   switch(index) {
     case 0:
         return neuron0x14c099a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_EE_TIGHT::Value(int index, double* input) {
   input0 = (input[0] - 0.370858)/0.320569;
   input1 = (input[1] - 0.404877)/0.337655;
   input2 = (input[2] - 0.320068)/0.333628;
   input3 = (input[3] - 20.0727)/1.59748;
   switch(index) {
     case 0:
         return neuron0x14c099a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c06f40() {
   return input0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c07250() {
   return input1;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c07560() {
   return input2;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c07870() {
   return input3;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x14c07cf0() {
   double input = -0.939393;
   input += synapse0x14654f60();
   input += synapse0x14c07f70();
   input += synapse0x14c07fb0();
   input += synapse0x14c07ff0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c07cf0() {
   double input = input0x14c07cf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x14c08030() {
   double input = -0.0568138;
   input += synapse0x14c08340();
   input += synapse0x14c08380();
   input += synapse0x14c083c0();
   input += synapse0x14c08400();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c08030() {
   double input = input0x14c08030();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x14c08440() {
   double input = 5.12853;
   input += synapse0x14c08750();
   input += synapse0x14c08790();
   input += synapse0x14c087d0();
   input += synapse0x14c08810();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c08440() {
   double input = input0x14c08440();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x14c08850() {
   double input = -1.54865;
   input += synapse0x14c08b60();
   input += synapse0x14c08ba0();
   input += synapse0x14c08be0();
   input += synapse0x14c08c20();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c08850() {
   double input = input0x14c08850();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x14c08c60() {
   double input = -1.89389;
   input += synapse0x14c08f70();
   input += synapse0x14642430();
   input += synapse0x14642470();
   input += synapse0x14c090c0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c08c60() {
   double input = input0x14c08c60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x14c09100() {
   double input = -0.316925;
   input += synapse0x14c09410();
   input += synapse0x14c09450();
   input += synapse0x14c09490();
   input += synapse0x14c094d0();
   input += synapse0x14c09510();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c09100() {
   double input = input0x14c09100();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x14c09550() {
   double input = 1.03497;
   input += synapse0x14c09860();
   input += synapse0x14c098a0();
   input += synapse0x14c098e0();
   input += synapse0x14c09920();
   input += synapse0x14c09960();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c09550() {
   double input = input0x14c09550();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x14c099a0() {
   double input = -1.14;
   input += synapse0x14c09ce0();
   input += synapse0x14c09d20();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x14c099a0() {
   double input = input0x14c099a0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14654f60() {
   return (neuron0x14c06f40()*0.502137);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c07f70() {
   return (neuron0x14c07250()*-0.20797);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c07fb0() {
   return (neuron0x14c07560()*0.114069);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c07ff0() {
   return (neuron0x14c07870()*-0.032458);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c08340() {
   return (neuron0x14c06f40()*-2.35224);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c08380() {
   return (neuron0x14c07250()*0.863295);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c083c0() {
   return (neuron0x14c07560()*0.733678);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c08400() {
   return (neuron0x14c07870()*5.07111);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c08750() {
   return (neuron0x14c06f40()*-1.09634);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c08790() {
   return (neuron0x14c07250()*0.00896431);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c087d0() {
   return (neuron0x14c07560()*2.59829);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c08810() {
   return (neuron0x14c07870()*-0.531932);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c08b60() {
   return (neuron0x14c06f40()*-0.519393);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c08ba0() {
   return (neuron0x14c07250()*-0.891847);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c08be0() {
   return (neuron0x14c07560()*2.41334);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c08c20() {
   return (neuron0x14c07870()*0.882718);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c08f70() {
   return (neuron0x14c06f40()*-0.0921405);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14642430() {
   return (neuron0x14c07250()*-1.60406);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14642470() {
   return (neuron0x14c07560()*2.26798);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c090c0() {
   return (neuron0x14c07870()*0.239029);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c09410() {
   return (neuron0x14c07cf0()*0.536988);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c09450() {
   return (neuron0x14c08030()*0.0392028);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c09490() {
   return (neuron0x14c08440()*1.25728);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c094d0() {
   return (neuron0x14c08850()*1.80316);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c09510() {
   return (neuron0x14c08c60()*0.190054);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c09860() {
   return (neuron0x14c07cf0()*3.09844);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c098a0() {
   return (neuron0x14c08030()*-0.393757);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c098e0() {
   return (neuron0x14c08440()*-1.16872);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c09920() {
   return (neuron0x14c08850()*2.52565);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c09960() {
   return (neuron0x14c08c60()*-2.0661);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c09ce0() {
   return (neuron0x14c09100()*-1.13075);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x14c09d20() {
   return (neuron0x14c09550()*3.6086);
}

