#include "../NN/MLP_Zbb_tt_Comb_multi_EE_TIGHT.h"
#include <cmath>

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 20.3256)/1.0298;
   input1 = (in1 - 21.0098)/0.967296;
   input2 = (in2 - 21.5918)/0.86144;
   input3 = (in3 - 0)/1;
   switch(index) {
     case 0:
         return neuron0x18c785a0();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::Value(int index, double* input) {
   input0 = (input[0] - 20.3256)/1.0298;
   input1 = (input[1] - 21.0098)/0.967296;
   input2 = (input[2] - 21.5918)/0.86144;
   input3 = (input[3] - 0)/1;
   switch(index) {
     case 0:
         return neuron0x18c785a0();
     default:
         return 0.;
   }
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c74c80() {
   return input0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c74f90() {
   return input1;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c752a0() {
   return input2;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c755e0() {
   return input3;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::input0x18c75a60() {
   double input = -0.601068;
   input += synapse0x19184d30();
   input += synapse0x18c7ba60();
   input += synapse0x19184ec0();
   input += synapse0x17cc3d40();
   return input;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c75a60() {
   double input = input0x18c75a60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::input0x18c75ce0() {
   double input = -3.06172;
   input += synapse0x17cc3cc0();
   input += synapse0x18c75ff0();
   input += synapse0x18c76030();
   input += synapse0x18c76070();
   return input;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c75ce0() {
   double input = input0x18c75ce0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::input0x18c760b0() {
   double input = 3.52414;
   input += synapse0x18c763c0();
   input += synapse0x18c76400();
   input += synapse0x18c76440();
   input += synapse0x18c76480();
   return input;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c760b0() {
   double input = input0x18c760b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::input0x18c764c0() {
   double input = 0.469669;
   input += synapse0x18c767d0();
   input += synapse0x18c76810();
   input += synapse0x18c76850();
   input += synapse0x18c76890();
   return input;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c764c0() {
   double input = input0x18c764c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::input0x18c768d0() {
   double input = 1.68449;
   input += synapse0x18c76be0();
   input += synapse0x18c13100();
   input += synapse0x18c13140();
   input += synapse0x18c76d30();
   return input;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c768d0() {
   double input = input0x18c768d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::input0x18c76d70() {
   double input = -0.788179;
   input += synapse0x18c77080();
   input += synapse0x18c770c0();
   input += synapse0x18c77100();
   input += synapse0x18c77140();
   return input;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c76d70() {
   double input = input0x18c76d70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::input0x18c77180() {
   double input = -0.310165;
   input += synapse0x18c774c0();
   input += synapse0x18c77500();
   input += synapse0x18c77540();
   input += synapse0x18c77580();
   input += synapse0x18c775c0();
   input += synapse0x18c77600();
   return input;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c77180() {
   double input = input0x18c77180();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::input0x18c77640() {
   double input = -0.167871;
   input += synapse0x18c77980();
   input += synapse0x18c779c0();
   input += synapse0x18c77a00();
   input += synapse0x18c4f720();
   input += synapse0x190301b0();
   input += synapse0x18c4fe70();
   return input;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c77640() {
   double input = input0x18c77640();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::input0x18c77c50() {
   double input = -0.205393;
   input += synapse0x18c77f60();
   input += synapse0x18c77fa0();
   input += synapse0x18c77fe0();
   input += synapse0x18c78020();
   input += synapse0x18c78060();
   input += synapse0x18c780a0();
   return input;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c77c50() {
   double input = input0x18c77c50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::input0x18c780e0() {
   double input = -0.807477;
   input += synapse0x18c78420();
   input += synapse0x18c78460();
   input += synapse0x18c784a0();
   input += synapse0x18c784e0();
   input += synapse0x18c78520();
   input += synapse0x18c78560();
   return input;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c780e0() {
   double input = input0x18c780e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::input0x18c785a0() {
   double input = -1.39168;
   input += synapse0x18c788e0();
   input += synapse0x18c78920();
   input += synapse0x18c78960();
   input += synapse0x18c789a0();
   return input;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::neuron0x18c785a0() {
   double input = input0x18c785a0();
   return (input * 1)+0;
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x19184d30() {
   return (neuron0x18c74c80()*5.6302);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c7ba60() {
   return (neuron0x18c74f90()*-2.87301);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x19184ec0() {
   return (neuron0x18c752a0()*-0.0347006);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x17cc3d40() {
   return (neuron0x18c755e0()*2.33852);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x17cc3cc0() {
   return (neuron0x18c74c80()*0.653125);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c75ff0() {
   return (neuron0x18c74f90()*-0.0941637);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c76030() {
   return (neuron0x18c752a0()*3.16059);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c76070() {
   return (neuron0x18c755e0()*0.0917836);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c763c0() {
   return (neuron0x18c74c80()*0.914501);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c76400() {
   return (neuron0x18c74f90()*-1.09653);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c76440() {
   return (neuron0x18c752a0()*-0.333608);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c76480() {
   return (neuron0x18c755e0()*-2.40984);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c767d0() {
   return (neuron0x18c74c80()*0.00123641);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c76810() {
   return (neuron0x18c74f90()*-0.03693);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c76850() {
   return (neuron0x18c752a0()*0.504818);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c76890() {
   return (neuron0x18c755e0()*-1.54285);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c76be0() {
   return (neuron0x18c74c80()*0.604251);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c13100() {
   return (neuron0x18c74f90()*-0.979577);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c13140() {
   return (neuron0x18c752a0()*0.389037);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c76d30() {
   return (neuron0x18c755e0()*-1.14729);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77080() {
   return (neuron0x18c74c80()*-0.924641);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c770c0() {
   return (neuron0x18c74f90()*-1.68171);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77100() {
   return (neuron0x18c752a0()*1.3222);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77140() {
   return (neuron0x18c755e0()*0.157107);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c774c0() {
   return (neuron0x18c75a60()*0.717927);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77500() {
   return (neuron0x18c75ce0()*0.843772);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77540() {
   return (neuron0x18c760b0()*-1.19451);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77580() {
   return (neuron0x18c764c0()*-0.578345);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c775c0() {
   return (neuron0x18c768d0()*1.65896);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77600() {
   return (neuron0x18c76d70()*0.285775);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77980() {
   return (neuron0x18c75a60()*-3.09825);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c779c0() {
   return (neuron0x18c75ce0()*1.83959);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77a00() {
   return (neuron0x18c760b0()*-2.28791);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c4f720() {
   return (neuron0x18c764c0()*-1.23118);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x190301b0() {
   return (neuron0x18c768d0()*1.05833);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c4fe70() {
   return (neuron0x18c76d70()*3.51175);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77f60() {
   return (neuron0x18c75a60()*0.774306);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77fa0() {
   return (neuron0x18c75ce0()*-1.54804);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c77fe0() {
   return (neuron0x18c760b0()*0.205874);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c78020() {
   return (neuron0x18c764c0()*-0.121683);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c78060() {
   return (neuron0x18c768d0()*0.903193);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c780a0() {
   return (neuron0x18c76d70()*-1.36964);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c78420() {
   return (neuron0x18c75a60()*-0.627764);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c78460() {
   return (neuron0x18c75ce0()*1.61505);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c784a0() {
   return (neuron0x18c760b0()*-2.34918);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c784e0() {
   return (neuron0x18c764c0()*-0.909455);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c78520() {
   return (neuron0x18c768d0()*1.9199);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c78560() {
   return (neuron0x18c76d70()*1.75392);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c788e0() {
   return (neuron0x18c77180()*0.583385);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c78920() {
   return (neuron0x18c77640()*1.02338);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c78960() {
   return (neuron0x18c77c50()*1.31132);
}

double MLP_Zbb_tt_Comb_multi_EE_TIGHT::synapse0x18c789a0() {
   return (neuron0x18c780e0()*0.785026);
}

