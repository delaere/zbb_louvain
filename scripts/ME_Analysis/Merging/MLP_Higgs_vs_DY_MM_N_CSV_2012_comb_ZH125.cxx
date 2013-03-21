#include "MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125.h"
#include <cmath>

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.4255)/1.13211;
   input1 = (in1 - 20.1628)/1.00425;
   input2 = (in2 - 24.7219)/1.34625;
   input3 = (in3 - 13.46)/1.74634;
   switch(index) {
     case 0:
         return neuron0x380c130();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::Value(int index, double* input) {
   input0 = (input[0] - 19.4255)/1.13211;
   input1 = (input[1] - 20.1628)/1.00425;
   input2 = (input[2] - 24.7219)/1.34625;
   input3 = (input[3] - 13.46)/1.74634;
   switch(index) {
     case 0:
         return neuron0x380c130();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x3808ef0() {
   return input0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x3809230() {
   return input1;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x3809570() {
   return input2;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x38098b0() {
   return input3;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::input0x3809d20() {
   double input = 0.629203;
   input += synapse0x37aa250();
   input += synapse0x3809fd0();
   input += synapse0x380a010();
   input += synapse0x380a050();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x3809d20() {
   double input = input0x3809d20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::input0x380a090() {
   double input = -1.59776;
   input += synapse0x380a3d0();
   input += synapse0x380a410();
   input += synapse0x380a450();
   input += synapse0x380a490();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x380a090() {
   double input = input0x380a090();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::input0x380a4d0() {
   double input = 6.52028;
   input += synapse0x380a810();
   input += synapse0x380a850();
   input += synapse0x380a890();
   input += synapse0x380a8d0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x380a4d0() {
   double input = input0x380a4d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::input0x380a910() {
   double input = 0.242125;
   input += synapse0x380ac50();
   input += synapse0x380ac90();
   input += synapse0x380acd0();
   input += synapse0x380ad10();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x380a910() {
   double input = input0x380a910();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::input0x380ad50() {
   double input = -0.431;
   input += synapse0x380b090();
   input += synapse0x37a9da0();
   input += synapse0x37a9de0();
   input += synapse0x380b1e0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x380ad50() {
   double input = input0x380ad50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::input0x380b220() {
   double input = 1.21763;
   input += synapse0x380b560();
   input += synapse0x380b5a0();
   input += synapse0x380b5e0();
   input += synapse0x380b620();
   input += synapse0x380b660();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x380b220() {
   double input = input0x380b220();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::input0x380b6a0() {
   double input = -0.276665;
   input += synapse0x380b9e0();
   input += synapse0x380ba20();
   input += synapse0x380ba60();
   input += synapse0x380baa0();
   input += synapse0x380bae0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x380b6a0() {
   double input = input0x380b6a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::input0x380bb20() {
   double input = -1.42084;
   input += synapse0x380be60();
   input += synapse0x380bea0();
   input += synapse0x380bee0();
   input += synapse0x37aa200();
   input += synapse0x37c8780();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x380bb20() {
   double input = input0x380bb20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::input0x380c130() {
   double input = 0.65172;
   input += synapse0x37c87c0();
   input += synapse0x380c470();
   input += synapse0x380c4b0();
   return input;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::neuron0x380c130() {
   double input = input0x380c130();
   return (input * 1)+0;
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x37aa250() {
   return (neuron0x3808ef0()*-0.850568);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x3809fd0() {
   return (neuron0x3809230()*-0.574772);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380a010() {
   return (neuron0x3809570()*0.776724);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380a050() {
   return (neuron0x38098b0()*1.35228);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380a3d0() {
   return (neuron0x3808ef0()*5.33418);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380a410() {
   return (neuron0x3809230()*-2.80684);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380a450() {
   return (neuron0x3809570()*-2.15751);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380a490() {
   return (neuron0x38098b0()*-0.378717);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380a810() {
   return (neuron0x3808ef0()*3.64669);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380a850() {
   return (neuron0x3809230()*1.94127);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380a890() {
   return (neuron0x3809570()*-7.58206);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380a8d0() {
   return (neuron0x38098b0()*2.5958);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380ac50() {
   return (neuron0x3808ef0()*-0.944428);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380ac90() {
   return (neuron0x3809230()*-0.561935);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380acd0() {
   return (neuron0x3809570()*4.28815);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380ad10() {
   return (neuron0x38098b0()*-1.40226);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380b090() {
   return (neuron0x3808ef0()*-2.98787);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x37a9da0() {
   return (neuron0x3809230()*5.07905);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x37a9de0() {
   return (neuron0x3809570()*-2.11919);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380b1e0() {
   return (neuron0x38098b0()*1.28899);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380b560() {
   return (neuron0x3809d20()*-1.16597);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380b5a0() {
   return (neuron0x380a090()*-2.78273);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380b5e0() {
   return (neuron0x380a4d0()*0.465354);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380b620() {
   return (neuron0x380a910()*1.08203);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380b660() {
   return (neuron0x380ad50()*0.371707);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380b9e0() {
   return (neuron0x3809d20()*0.989045);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380ba20() {
   return (neuron0x380a090()*-2.91216);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380ba60() {
   return (neuron0x380a4d0()*1.14383);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380baa0() {
   return (neuron0x380a910()*1.27018);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380bae0() {
   return (neuron0x380ad50()*0.785272);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380be60() {
   return (neuron0x3809d20()*7.79235);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380bea0() {
   return (neuron0x380a090()*-4.44714);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380bee0() {
   return (neuron0x380a4d0()*-4.37179);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x37aa200() {
   return (neuron0x380a910()*-2.67042);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x37c8780() {
   return (neuron0x380ad50()*4.12766);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x37c87c0() {
   return (neuron0x380b220()*2.42559);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380c470() {
   return (neuron0x380b6a0()*-2.00574);
}

double MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125::synapse0x380c4b0() {
   return (neuron0x380bb20()*-0.702107);
}

