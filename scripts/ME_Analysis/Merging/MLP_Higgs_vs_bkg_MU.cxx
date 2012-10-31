#include "MLP_Higgs_vs_bkg_MU.h"
#include <cmath>

double MLP_Higgs_vs_bkg_MU::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.387839)/0.295659;
   input1 = (in1 - 1.00829)/0.054482;
   input2 = (in2 - 1.27601)/0.269311;
   switch(index) {
     case 0:
         return neuron0xc147670();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_MU::Value(int index, double* input) {
   input0 = (input[0] - 0.387839)/0.295659;
   input1 = (input[1] - 1.00829)/0.054482;
   input2 = (input[2] - 1.27601)/0.269311;
   switch(index) {
     case 0:
         return neuron0xc147670();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_MU::neuron0xc134810() {
   return input0;
}

double MLP_Higgs_vs_bkg_MU::neuron0xc134b50() {
   return input1;
}

double MLP_Higgs_vs_bkg_MU::neuron0xc145b20() {
   return input2;
}

double MLP_Higgs_vs_bkg_MU::input0xc145e70() {
   double input = 1.31904;
   input += synapse0xc0fd060();
   input += synapse0xc11b5b0();
   input += synapse0xc146120();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xc145e70() {
   double input = input0xc145e70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xc146160() {
   double input = 0.881956;
   input += synapse0xc1464a0();
   input += synapse0xc1464e0();
   input += synapse0xc146520();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xc146160() {
   double input = input0xc146160();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xc146560() {
   double input = 0.492398;
   input += synapse0xc1468a0();
   input += synapse0xc1468e0();
   input += synapse0xc146920();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xc146560() {
   double input = input0xc146560();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xc146960() {
   double input = 1.68812;
   input += synapse0xc146ca0();
   input += synapse0xc146ce0();
   input += synapse0xc146d20();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xc146960() {
   double input = input0xc146960();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xc146d60() {
   double input = -0.629308;
   input += synapse0xc1470a0();
   input += synapse0xc1470e0();
   input += synapse0xc147120();
   input += synapse0xc147160();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xc146d60() {
   double input = input0xc146d60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xc1471a0() {
   double input = -0.365523;
   input += synapse0xc1474e0();
   input += synapse0xbf22140();
   input += synapse0xbf22180();
   input += synapse0xc147630();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xc1471a0() {
   double input = input0xc1471a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::input0xc147670() {
   double input = -0.226891;
   input += synapse0xc147890();
   input += synapse0xc1478d0();
   return input;
}

double MLP_Higgs_vs_bkg_MU::neuron0xc147670() {
   double input = input0xc147670();
   return (input * 1)+0;
}

double MLP_Higgs_vs_bkg_MU::synapse0xc0fd060() {
   return (neuron0xc134810()*-1.89004);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc11b5b0() {
   return (neuron0xc134b50()*0.486873);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc146120() {
   return (neuron0xc145b20()*-0.0267085);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc1464a0() {
   return (neuron0xc134810()*-0.467487);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc1464e0() {
   return (neuron0xc134b50()*-0.0612667);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc146520() {
   return (neuron0xc145b20()*0.514962);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc1468a0() {
   return (neuron0xc134810()*-0.321481);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc1468e0() {
   return (neuron0xc134b50()*0.074264);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc146920() {
   return (neuron0xc145b20()*-0.0842636);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc146ca0() {
   return (neuron0xc134810()*0.491302);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc146ce0() {
   return (neuron0xc134b50()*0.463572);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc146d20() {
   return (neuron0xc145b20()*0.580597);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc1470a0() {
   return (neuron0xc145e70()*-1.26767);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc1470e0() {
   return (neuron0xc146160()*-1.50654);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc147120() {
   return (neuron0xc146560()*-0.366042);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc147160() {
   return (neuron0xc146960()*1.04086);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc1474e0() {
   return (neuron0xc145e70()*-1.30754);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbf22140() {
   return (neuron0xc146160()*-0.215257);
}

double MLP_Higgs_vs_bkg_MU::synapse0xbf22180() {
   return (neuron0xc146560()*-1.17432);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc147630() {
   return (neuron0xc146960()*0.875143);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc147890() {
   return (neuron0xc146d60()*1.8369);
}

double MLP_Higgs_vs_bkg_MU::synapse0xc1478d0() {
   return (neuron0xc1471a0()*1.1924);
}

