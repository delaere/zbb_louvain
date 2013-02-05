#include "../NN/MLP_Higgs_vs_DY_MM_N_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_DY_MM_N_CSV_2011::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.623)/1.05526;
   input1 = (in1 - 20.2582)/0.921746;
   input2 = (in2 - 24.5927)/1.2431;
   input3 = (in3 - 13.2734)/1.51989;
   switch(index) {
     case 0:
         return neuron0x1a1cb800();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 19.623)/1.05526;
   input1 = (input[1] - 20.2582)/0.921746;
   input2 = (input[2] - 24.5927)/1.2431;
   input3 = (input[3] - 13.2734)/1.51989;
   switch(index) {
     case 0:
         return neuron0x1a1cb800();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1c8800() {
   return input0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1c8b10() {
   return input1;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1c8e20() {
   return input2;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1c9130() {
   return input3;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::input0x1a1c9580() {
   double input = 0.237925;
   input += synapse0x1a171750();
   input += synapse0x1a1c9800();
   input += synapse0x1a1c9840();
   input += synapse0x1a1c9880();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1c9580() {
   double input = input0x1a1c9580();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::input0x1a1c98c0() {
   double input = -4.15789;
   input += synapse0x1a1c9bd0();
   input += synapse0x1a1c9c10();
   input += synapse0x1a1c9c50();
   input += synapse0x1a1c9c90();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1c98c0() {
   double input = input0x1a1c98c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::input0x1a1c9cd0() {
   double input = -3.1324;
   input += synapse0x1a1c9fe0();
   input += synapse0x1a1ca020();
   input += synapse0x1a1ca060();
   input += synapse0x1a1ca0a0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1c9cd0() {
   double input = input0x1a1c9cd0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::input0x1a1ca0e0() {
   double input = -0.300817;
   input += synapse0x1a1ca3f0();
   input += synapse0x1a1ca430();
   input += synapse0x1a1ca470();
   input += synapse0x1a1ca4b0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1ca0e0() {
   double input = input0x1a1ca0e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::input0x1a1ca4f0() {
   double input = -0.497772;
   input += synapse0x1a1ca800();
   input += synapse0x1a171350();
   input += synapse0x19f0dd50();
   input += synapse0x19f0dd90();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1ca4f0() {
   double input = input0x1a1ca4f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::input0x1a1ca950() {
   double input = -1.22379;
   input += synapse0x1a1cac60();
   input += synapse0x1a1caca0();
   input += synapse0x1a1cace0();
   input += synapse0x1a1cad20();
   input += synapse0x1a1cad60();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1ca950() {
   double input = input0x1a1ca950();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::input0x1a1cada0() {
   double input = 0.951407;
   input += synapse0x1a1cb0b0();
   input += synapse0x1a1cb0f0();
   input += synapse0x1a1cb130();
   input += synapse0x1a1cb170();
   input += synapse0x1a1cb1b0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1cada0() {
   double input = input0x1a1cada0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::input0x1a1cb1f0() {
   double input = 2.22154;
   input += synapse0x1a1cb530();
   input += synapse0x1a1cb570();
   input += synapse0x1a1cb5b0();
   input += synapse0x1a18bfb0();
   input += synapse0x1a1cf500();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1cb1f0() {
   double input = input0x1a1cb1f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::input0x1a1cb800() {
   double input = 0.0462611;
   input += synapse0x1a1cbb40();
   input += synapse0x1a1cbb80();
   input += synapse0x1a1cbbc0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::neuron0x1a1cb800() {
   double input = input0x1a1cb800();
   return (input * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a171750() {
   return (neuron0x1a1c8800()*1.46233);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1c9800() {
   return (neuron0x1a1c8b10()*-0.84231);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1c9840() {
   return (neuron0x1a1c8e20()*0.516833);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1c9880() {
   return (neuron0x1a1c9130()*-2.21685);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1c9bd0() {
   return (neuron0x1a1c8800()*4.11652);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1c9c10() {
   return (neuron0x1a1c8b10()*-6.04305);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1c9c50() {
   return (neuron0x1a1c8e20()*-0.548504);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1c9c90() {
   return (neuron0x1a1c9130()*-2.56194);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1c9fe0() {
   return (neuron0x1a1c8800()*2.01123);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1ca020() {
   return (neuron0x1a1c8b10()*0.976257);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1ca060() {
   return (neuron0x1a1c8e20()*0.0861876);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1ca0a0() {
   return (neuron0x1a1c9130()*-2.82722);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1ca3f0() {
   return (neuron0x1a1c8800()*-4.47477);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1ca430() {
   return (neuron0x1a1c8b10()*0.310119);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1ca470() {
   return (neuron0x1a1c8e20()*1.364);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1ca4b0() {
   return (neuron0x1a1c9130()*-2.23318);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1ca800() {
   return (neuron0x1a1c8800()*-1.24702);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a171350() {
   return (neuron0x1a1c8b10()*0.0557675);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x19f0dd50() {
   return (neuron0x1a1c8e20()*-0.366245);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x19f0dd90() {
   return (neuron0x1a1c9130()*-0.435469);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cac60() {
   return (neuron0x1a1c9580()*0.647706);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1caca0() {
   return (neuron0x1a1c98c0()*-1.77979);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cace0() {
   return (neuron0x1a1c9cd0()*0.876676);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cad20() {
   return (neuron0x1a1ca0e0()*0.0656234);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cad60() {
   return (neuron0x1a1ca4f0()*2.69876);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cb0b0() {
   return (neuron0x1a1c9580()*1.93573);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cb0f0() {
   return (neuron0x1a1c98c0()*-0.364291);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cb130() {
   return (neuron0x1a1c9cd0()*6.91588);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cb170() {
   return (neuron0x1a1ca0e0()*-1.38139);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cb1b0() {
   return (neuron0x1a1ca4f0()*1.01878);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cb530() {
   return (neuron0x1a1c9580()*-0.198575);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cb570() {
   return (neuron0x1a1c98c0()*3.24003);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cb5b0() {
   return (neuron0x1a1c9cd0()*-2.74703);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a18bfb0() {
   return (neuron0x1a1ca0e0()*-1.03285);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cf500() {
   return (neuron0x1a1ca4f0()*-5.87953);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cbb40() {
   return (neuron0x1a1ca950()*-2.22807);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cbb80() {
   return (neuron0x1a1cada0()*2.67365);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011::synapse0x1a1cbbc0() {
   return (neuron0x1a1cb1f0()*-1.57086);
}

