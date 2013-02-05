#include "MLP_Higgs_vs_DY_MM_N_CSV_2011_comb.h"
#include <cmath>

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.6127)/1.09359;
   input1 = (in1 - 20.2543)/0.95874;
   input2 = (in2 - 24.618)/1.2857;
   input3 = (in3 - 13.3383)/1.57357;
   switch(index) {
     case 0:
         return neuron0x7242770();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::Value(int index, double* input) {
   input0 = (input[0] - 19.6127)/1.09359;
   input1 = (input[1] - 20.2543)/0.95874;
   input2 = (input[2] - 24.618)/1.2857;
   input3 = (input[3] - 13.3383)/1.57357;
   switch(index) {
     case 0:
         return neuron0x7242770();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x723f530() {
   return input0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x723f870() {
   return input1;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x723fbb0() {
   return input2;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x723fef0() {
   return input3;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::input0x7240360() {
   double input = 5.69741;
   input += synapse0x7218760();
   input += synapse0x7240610();
   input += synapse0x7240650();
   input += synapse0x7240690();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x7240360() {
   double input = input0x7240360();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::input0x72406d0() {
   double input = -0.440065;
   input += synapse0x7240a10();
   input += synapse0x7240a50();
   input += synapse0x7240a90();
   input += synapse0x7240ad0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x72406d0() {
   double input = input0x72406d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::input0x7240b10() {
   double input = -1.4131;
   input += synapse0x7240e50();
   input += synapse0x7240e90();
   input += synapse0x7240ed0();
   input += synapse0x7240f10();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x7240b10() {
   double input = input0x7240b10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::input0x7240f50() {
   double input = -2.33525;
   input += synapse0x7241290();
   input += synapse0x72412d0();
   input += synapse0x7241310();
   input += synapse0x7241350();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x7240f50() {
   double input = input0x7240f50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::input0x7241390() {
   double input = 0.963082;
   input += synapse0x72416d0();
   input += synapse0x6ce3f40();
   input += synapse0x6ce3f80();
   input += synapse0x7241820();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x7241390() {
   double input = input0x7241390();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::input0x7241860() {
   double input = 1.48305;
   input += synapse0x7241ba0();
   input += synapse0x7241be0();
   input += synapse0x7241c20();
   input += synapse0x7241c60();
   input += synapse0x7241ca0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x7241860() {
   double input = input0x7241860();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::input0x7241ce0() {
   double input = 3.3452;
   input += synapse0x7242020();
   input += synapse0x7242060();
   input += synapse0x72420a0();
   input += synapse0x72420e0();
   input += synapse0x7242120();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x7241ce0() {
   double input = input0x7241ce0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::input0x7242160() {
   double input = 1.9486;
   input += synapse0x72424a0();
   input += synapse0x72424e0();
   input += synapse0x7242520();
   input += synapse0x71e0840();
   input += synapse0x72187a0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x7242160() {
   double input = input0x7242160();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::input0x7242770() {
   double input = -2.84635;
   input += synapse0x7242ab0();
   input += synapse0x7242af0();
   input += synapse0x7242b30();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::neuron0x7242770() {
   double input = input0x7242770();
   return (input * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7218760() {
   return (neuron0x723f530()*1.53308);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7240610() {
   return (neuron0x723f870()*2.24112);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7240650() {
   return (neuron0x723fbb0()*-4.17278);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7240690() {
   return (neuron0x723fef0()*0.702808);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7240a10() {
   return (neuron0x723f530()*1.15663);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7240a50() {
   return (neuron0x723f870()*0.454738);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7240a90() {
   return (neuron0x723fbb0()*-1.27479);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7240ad0() {
   return (neuron0x723fef0()*0.126725);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7240e50() {
   return (neuron0x723f530()*3.75485);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7240e90() {
   return (neuron0x723f870()*-4.15488);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7240ed0() {
   return (neuron0x723fbb0()*0.814156);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7240f10() {
   return (neuron0x723fef0()*-1.15422);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7241290() {
   return (neuron0x723f530()*-0.0517638);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x72412d0() {
   return (neuron0x723f870()*2.59925);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7241310() {
   return (neuron0x723fbb0()*0.406252);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7241350() {
   return (neuron0x723fef0()*-4.2225);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x72416d0() {
   return (neuron0x723f530()*-0.502419);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x6ce3f40() {
   return (neuron0x723f870()*-1.66163);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x6ce3f80() {
   return (neuron0x723fbb0()*0.982836);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7241820() {
   return (neuron0x723fef0()*1.27948);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7241ba0() {
   return (neuron0x7240360()*-0.57615);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7241be0() {
   return (neuron0x72406d0()*1.1499);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7241c20() {
   return (neuron0x7240b10()*-0.186106);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7241c60() {
   return (neuron0x7240f50()*-7.54977);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7241ca0() {
   return (neuron0x7241390()*-0.644324);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7242020() {
   return (neuron0x7240360()*3.54821);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7242060() {
   return (neuron0x72406d0()*-6.58606);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x72420a0() {
   return (neuron0x7240b10()*-6.21228);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x72420e0() {
   return (neuron0x7240f50()*-5.61635);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7242120() {
   return (neuron0x7241390()*-8.09617);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x72424a0() {
   return (neuron0x7240360()*2.67734);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x72424e0() {
   return (neuron0x72406d0()*-5.3315);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7242520() {
   return (neuron0x7240b10()*0.455854);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x71e0840() {
   return (neuron0x7240f50()*4.97575);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x72187a0() {
   return (neuron0x7241390()*-4.87151);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7242ab0() {
   return (neuron0x7241860()*3.88084);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7242af0() {
   return (neuron0x7241ce0()*-4.74907);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2011_comb::synapse0x7242b30() {
   return (neuron0x7242160()*3.84203);
}

