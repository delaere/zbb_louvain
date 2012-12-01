#include "MLP_Higgs_vs_bkg_MU.h"
#include <cmath>

double MLP_Higgs_vs_bkg_MU::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.594168)/0.307663;
   input1 = (in1 - 0.672491)/0.306233;
   input2 = (in2 - 0.701168)/0.346345;
   switch(index) {
     case 0:
         return neuron0x9f0c580();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_MU::Value(int index, double* input) {
   input0 = (input[0] - 0.594168)/0.307663;
   input1 = (input[1] - 0.672491)/0.306233;
   input2 = (input[2] - 0.701168)/0.346345;
   switch(index) {
     case 0:
         return neuron0x9f0c580();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_MU::neuron0x9ef92e0() {
   return input0;
}

double MLP_Higgs_vs_bkg_MU::neuron0x9ef9620() {
   return input1;
}

double MLP_Higgs_vs_bkg_MU::neuron0x9f0a5f0() {
   return input2;
}

double MLP_Higgs_vs_bkg_MU::input0x9f0a940() {
   double input = 1.17072;
   input += synapse0x9ec1b30();
   input += synapse0x9ee0080();
   input += synapse0x9f0abf0();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0x9f0a940() {
   double input = input0x9f0a940();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0x9f0ac30() {
   double input = -0.687789;
   input += synapse0x9f0af70();
   input += synapse0x9f0afb0();
   input += synapse0x9f0aff0();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0x9f0ac30() {
   double input = input0x9f0ac30();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0x9f0b030() {
   double input = -0.361735;
   input += synapse0x9f0b370();
   input += synapse0x9f0b3b0();
   input += synapse0x9f0b3f0();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0x9f0b030() {
   double input = input0x9f0b030();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0x9f0b430() {
   double input = -3.65638;
   input += synapse0x9f0b770();
   input += synapse0x9f0b7b0();
   input += synapse0x9f0b7f0();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0x9f0b430() {
   double input = input0x9f0b430();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0x9f0b830() {
   double input = 0.204801;
   input += synapse0x9f0bb70();
   input += synapse0x9f0bbb0();
   input += synapse0x9f0bbf0();
   input += synapse0x9f0bc30();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0x9f0b830() {
   double input = input0x9f0b830();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0x9f0bc70() {
   double input = 0.513738;
   input += synapse0x9f0bfb0();
   input += synapse0x9ce6bd0();
   input += synapse0x9ce6c10();
   input += synapse0x9f0c100();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0x9f0bc70() {
   double input = input0x9f0bc70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0x9f0c140() {
   double input = 1.28699;
   input += synapse0x9f0c480();
   input += synapse0x9f0c4c0();
   input += synapse0x9f0c500();
   input += synapse0x9f0c540();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0x9f0c140() {
   double input = input0x9f0c140();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0x9f0c580() {
   double input = 0.762666;
   input += synapse0x9f0c7a0();
   input += synapse0x9f0c7e0();
   input += synapse0x9f0c820();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0x9f0c580() {
   double input = input0x9f0c580();
   return (input * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::synapse0x9ec1b30() {
   return (neuron0x9ef92e0()*-0.664398);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9ee0080() {
   return (neuron0x9ef9620()*3.28078);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0abf0() {
   return (neuron0x9f0a5f0()*-2.05123);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0af70() {
   return (neuron0x9ef92e0()*-1.80811);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0afb0() {
   return (neuron0x9ef9620()*2.76519);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0aff0() {
   return (neuron0x9f0a5f0()*-1.11513);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0b370() {
   return (neuron0x9ef92e0()*-0.774031);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0b3b0() {
   return (neuron0x9ef9620()*1.46156);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0b3f0() {
   return (neuron0x9f0a5f0()*0.268652);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0b770() {
   return (neuron0x9ef92e0()*0.422259);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0b7b0() {
   return (neuron0x9ef9620()*-1.80322);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0b7f0() {
   return (neuron0x9f0a5f0()*-0.334714);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0bb70() {
   return (neuron0x9f0a940()*2.87919);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0bbb0() {
   return (neuron0x9f0ac30()*-1.14311);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0bbf0() {
   return (neuron0x9f0b030()*-2.01172);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0bc30() {
   return (neuron0x9f0b430()*0.608544);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0bfb0() {
   return (neuron0x9f0a940()*-1.81599);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9ce6bd0() {
   return (neuron0x9f0ac30()*1.19623);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9ce6c10() {
   return (neuron0x9f0b030()*-2.46599);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0c100() {
   return (neuron0x9f0b430()*-0.289563);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0c480() {
   return (neuron0x9f0a940()*-0.0536535);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0c4c0() {
   return (neuron0x9f0ac30()*1.15945);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0c500() {
   return (neuron0x9f0b030()*-2.7796);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0c540() {
   return (neuron0x9f0b430()*2.94299);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0c7a0() {
   return (neuron0x9f0b830()*2.24253);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0c7e0() {
   return (neuron0x9f0bc70()*2.68766);
}

double MLP_Higgs_vs_bkg_MU::synapse0x9f0c820() {
   return (neuron0x9f0c140()*-3.89402);
}

