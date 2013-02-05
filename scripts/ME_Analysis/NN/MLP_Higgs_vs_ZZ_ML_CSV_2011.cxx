#include "../NN/MLP_Higgs_vs_ZZ_ML_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_ZZ_ML_CSV_2011::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 21.3432)/1.34697;
   input1 = (in1 - 11.2533)/1.19039;
   input2 = (in2 - 24.8123)/1.27883;
   input3 = (in3 - 13.5042)/1.54388;
   switch(index) {
     case 0:
         return neuron0x175dd9b0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 21.3432)/1.34697;
   input1 = (input[1] - 11.2533)/1.19039;
   input2 = (input[2] - 24.8123)/1.27883;
   input3 = (input[3] - 13.5042)/1.54388;
   switch(index) {
     case 0:
         return neuron0x175dd9b0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175da9b0() {
   return input0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175dacc0() {
   return input1;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175dafd0() {
   return input2;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175db2e0() {
   return input3;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::input0x175db730() {
   double input = -7.25081;
   input += synapse0x17583900();
   input += synapse0x175db9b0();
   input += synapse0x175db9f0();
   input += synapse0x175dba30();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175db730() {
   double input = input0x175db730();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::input0x175dba70() {
   double input = 4.04242;
   input += synapse0x175dbd80();
   input += synapse0x175dbdc0();
   input += synapse0x175dbe00();
   input += synapse0x175dbe40();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175dba70() {
   double input = input0x175dba70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::input0x175dbe80() {
   double input = 2.73134;
   input += synapse0x175dc190();
   input += synapse0x175dc1d0();
   input += synapse0x175dc210();
   input += synapse0x175dc250();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175dbe80() {
   double input = input0x175dbe80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::input0x175dc290() {
   double input = -1.20257;
   input += synapse0x175dc5a0();
   input += synapse0x175dc5e0();
   input += synapse0x175dc620();
   input += synapse0x175dc660();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175dc290() {
   double input = input0x175dc290();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::input0x175dc6a0() {
   double input = -0.0260113;
   input += synapse0x175dc9b0();
   input += synapse0x17583500();
   input += synapse0x173144f0();
   input += synapse0x17314530();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175dc6a0() {
   double input = input0x175dc6a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::input0x175dcb00() {
   double input = -0.259819;
   input += synapse0x175dce10();
   input += synapse0x175dce50();
   input += synapse0x175dce90();
   input += synapse0x175dced0();
   input += synapse0x175dcf10();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175dcb00() {
   double input = input0x175dcb00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::input0x175dcf50() {
   double input = 0.534923;
   input += synapse0x175dd260();
   input += synapse0x175dd2a0();
   input += synapse0x175dd2e0();
   input += synapse0x175dd320();
   input += synapse0x175dd360();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175dcf50() {
   double input = input0x175dcf50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::input0x175dd3a0() {
   double input = 0.8171;
   input += synapse0x175dd6e0();
   input += synapse0x175dd720();
   input += synapse0x175dd760();
   input += synapse0x1759e160();
   input += synapse0x175e16b0();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175dd3a0() {
   double input = input0x175dd3a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::input0x175dd9b0() {
   double input = -0.777628;
   input += synapse0x175ddcf0();
   input += synapse0x175ddd30();
   input += synapse0x175ddd70();
   return input;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::neuron0x175dd9b0() {
   double input = input0x175dd9b0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x17583900() {
   return (neuron0x175da9b0()*-4.42395);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175db9b0() {
   return (neuron0x175dacc0()*-0.617631);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175db9f0() {
   return (neuron0x175dafd0()*1.32947);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dba30() {
   return (neuron0x175db2e0()*3.28057);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dbd80() {
   return (neuron0x175da9b0()*-1.05869);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dbdc0() {
   return (neuron0x175dacc0()*4.25109);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dbe00() {
   return (neuron0x175dafd0()*-2.28891);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dbe40() {
   return (neuron0x175db2e0()*-1.17526);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dc190() {
   return (neuron0x175da9b0()*-6.10588);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dc1d0() {
   return (neuron0x175dacc0()*2.55713);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dc210() {
   return (neuron0x175dafd0()*2.65076);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dc250() {
   return (neuron0x175db2e0()*-0.24724);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dc5a0() {
   return (neuron0x175da9b0()*-8.27749);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dc5e0() {
   return (neuron0x175dacc0()*3.87678);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dc620() {
   return (neuron0x175dafd0()*3.33626);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dc660() {
   return (neuron0x175db2e0()*-3.37747);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dc9b0() {
   return (neuron0x175da9b0()*1.11636);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x17583500() {
   return (neuron0x175dacc0()*-0.146237);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x173144f0() {
   return (neuron0x175dafd0()*1.4896);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x17314530() {
   return (neuron0x175db2e0()*-4.52556);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dce10() {
   return (neuron0x175db730()*-4.47585);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dce50() {
   return (neuron0x175dba70()*4.27383);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dce90() {
   return (neuron0x175dbe80()*-4.16147);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dced0() {
   return (neuron0x175dc290()*0.248131);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dcf10() {
   return (neuron0x175dc6a0()*0.000334901);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dd260() {
   return (neuron0x175db730()*-0.249424);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dd2a0() {
   return (neuron0x175dba70()*3.89845);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dd2e0() {
   return (neuron0x175dbe80()*-0.750169);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dd320() {
   return (neuron0x175dc290()*-1.81919);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dd360() {
   return (neuron0x175dc6a0()*0.0984348);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dd6e0() {
   return (neuron0x175db730()*0.106737);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dd720() {
   return (neuron0x175dba70()*-2.05886);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175dd760() {
   return (neuron0x175dbe80()*0.0761513);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x1759e160() {
   return (neuron0x175dc290()*1.4285);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175e16b0() {
   return (neuron0x175dc6a0()*1.72719);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175ddcf0() {
   return (neuron0x175dcb00()*0.730536);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175ddd30() {
   return (neuron0x175dcf50()*0.554008);
}

double MLP_Higgs_vs_ZZ_ML_CSV_2011::synapse0x175ddd70() {
   return (neuron0x175dd3a0()*0.804241);
}

