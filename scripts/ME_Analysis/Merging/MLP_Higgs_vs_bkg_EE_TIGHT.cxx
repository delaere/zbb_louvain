#include "MLP_Higgs_vs_bkg_EE_TIGHT.h"
#include <cmath>

double MLP_Higgs_vs_bkg_EE_TIGHT::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.370858)/0.320569;
   input1 = (in1 - 0.404877)/0.337655;
   input2 = (in2 - 0.320068)/0.333628;
   switch(index) {
     case 0:
         return neuron0x183957a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_EE_TIGHT::Value(int index, double* input) {
   input0 = (input[0] - 0.370858)/0.320569;
   input1 = (input[1] - 0.404877)/0.337655;
   input2 = (input[2] - 0.320068)/0.333628;
   switch(index) {
     case 0:
         return neuron0x183957a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x18382b20() {
   return input0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x18382e30() {
   return input1;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x18393cc0() {
   return input2;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x18394110() {
   double input = -1.06966;
   input += synapse0x17df5f60();
   input += synapse0x17de3000();
   input += synapse0x18383140();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x18394110() {
   double input = input0x18394110();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x18394390() {
   double input = -0.428179;
   input += synapse0x18383180();
   input += synapse0x183946a0();
   input += synapse0x183946e0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x18394390() {
   double input = input0x18394390();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x18394720() {
   double input = 0.0606603;
   input += synapse0x18394a30();
   input += synapse0x18394a70();
   input += synapse0x18394ab0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x18394720() {
   double input = input0x18394720();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x18394af0() {
   double input = -2.40285;
   input += synapse0x18394e00();
   input += synapse0x18394e40();
   input += synapse0x18394e80();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x18394af0() {
   double input = input0x18394af0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x18394ec0() {
   double input = -2.90998;
   input += synapse0x183951d0();
   input += synapse0x18395210();
   input += synapse0x18395250();
   input += synapse0x18395290();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x18394ec0() {
   double input = input0x18394ec0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x183952d0() {
   double input = -0.205292;
   input += synapse0x18395610();
   input += synapse0x17de3470();
   input += synapse0x17de34b0();
   input += synapse0x18395760();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x183952d0() {
   double input = input0x183952d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::input0x183957a0() {
   double input = -0.468295;
   input += synapse0x18394090();
   input += synapse0x183940d0();
   return input;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::neuron0x183957a0() {
   double input = input0x183957a0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x17df5f60() {
   return (neuron0x18382b20()*1.10096);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x17de3000() {
   return (neuron0x18382e30()*-0.394348);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18383140() {
   return (neuron0x18393cc0()*-0.96008);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18383180() {
   return (neuron0x18382b20()*1.94405);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x183946a0() {
   return (neuron0x18382e30()*-0.335159);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x183946e0() {
   return (neuron0x18393cc0()*-3.06053);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18394a30() {
   return (neuron0x18382b20()*0.855291);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18394a70() {
   return (neuron0x18382e30()*4.25836);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18394ab0() {
   return (neuron0x18393cc0()*0.527835);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18394e00() {
   return (neuron0x18382b20()*-0.0447699);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18394e40() {
   return (neuron0x18382e30()*0.33354);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18394e80() {
   return (neuron0x18393cc0()*0.755976);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x183951d0() {
   return (neuron0x18394110()*4.65699);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18395210() {
   return (neuron0x18394390()*-2.11612);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18395250() {
   return (neuron0x18394720()*0.407723);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18395290() {
   return (neuron0x18394af0()*2.66545);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18395610() {
   return (neuron0x18394110()*-1.31169);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x17de3470() {
   return (neuron0x18394390()*1.10567);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x17de34b0() {
   return (neuron0x18394720()*0.124764);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18395760() {
   return (neuron0x18394af0()*-0.412639);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x18394090() {
   return (neuron0x18394ec0()*3.63175);
}

double MLP_Higgs_vs_bkg_EE_TIGHT::synapse0x183940d0() {
   return (neuron0x183952d0()*0.651784);
}

