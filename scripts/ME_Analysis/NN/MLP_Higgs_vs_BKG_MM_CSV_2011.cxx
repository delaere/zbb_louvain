#include "../NN/MLP_Higgs_vs_BKG_MM_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_BKG_MM_CSV_2011::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.460993)/0.340009;
   input1 = (in1 - 0.50449)/0.334883;
   input2 = (in2 - 0.43239)/0.390486;
   switch(index) {
     case 0:
         return neuron0xfa26830();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 0.460993)/0.340009;
   input1 = (input[1] - 0.50449)/0.334883;
   input2 = (input[2] - 0.43239)/0.390486;
   switch(index) {
     case 0:
         return neuron0xfa26830();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::neuron0xfa137c0() {
   return input0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::neuron0xfa13ad0() {
   return input1;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::neuron0xfa24990() {
   return input2;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::input0xfa24d50() {
   double input = -5.39665;
   input += synapse0xf9fc2c0();
   input += synapse0xf9e1b70();
   input += synapse0xf772780();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::neuron0xfa24d50() {
   double input = input0xfa24d50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::input0xfa24fd0() {
   double input = -4.3065;
   input += synapse0xfa252e0();
   input += synapse0xfa25320();
   input += synapse0xfa25360();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::neuron0xfa24fd0() {
   double input = input0xfa24fd0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::input0xfa253a0() {
   double input = -2.36416;
   input += synapse0xfa256b0();
   input += synapse0xfa256f0();
   input += synapse0xfa25730();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::neuron0xfa253a0() {
   double input = input0xfa253a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::input0xfa25770() {
   double input = -0.28836;
   input += synapse0xfa25a80();
   input += synapse0xfa25ac0();
   input += synapse0xfa25b00();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::neuron0xfa25770() {
   double input = input0xfa25770();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::input0xfa25b40() {
   double input = 0.382506;
   input += synapse0xfa25e50();
   input += synapse0xfa25e90();
   input += synapse0xfa25ed0();
   input += synapse0xfa25f10();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::neuron0xfa25b40() {
   double input = input0xfa25b40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::input0xfa25f50() {
   double input = -2.12109;
   input += synapse0xfa26260();
   input += synapse0xf7726f0();
   input += synapse0xf772730();
   input += synapse0xfa263b0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::neuron0xfa25f50() {
   double input = input0xfa25f50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::input0xfa263f0() {
   double input = 1.87015;
   input += synapse0xfa26730();
   input += synapse0xfa26770();
   input += synapse0xfa267b0();
   input += synapse0xfa267f0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::neuron0xfa263f0() {
   double input = input0xfa263f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::input0xfa26830() {
   double input = -0.30984;
   input += synapse0xfa24cd0();
   input += synapse0xfa24d10();
   input += synapse0xfa26ab0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::neuron0xfa26830() {
   double input = input0xfa26830();
   return (input * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xf9fc2c0() {
   return (neuron0xfa137c0()*1.20665);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xf9e1b70() {
   return (neuron0xfa13ad0()*-0.654654);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xf772780() {
   return (neuron0xfa24990()*2.87665);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa252e0() {
   return (neuron0xfa137c0()*-2.77697);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa25320() {
   return (neuron0xfa13ad0()*-2.9527);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa25360() {
   return (neuron0xfa24990()*2.02136);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa256b0() {
   return (neuron0xfa137c0()*-0.114106);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa256f0() {
   return (neuron0xfa13ad0()*-0.505372);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa25730() {
   return (neuron0xfa24990()*1.81396);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa25a80() {
   return (neuron0xfa137c0()*-1.42536);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa25ac0() {
   return (neuron0xfa13ad0()*0.721614);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa25b00() {
   return (neuron0xfa24990()*-1.91952);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa25e50() {
   return (neuron0xfa24d50()*-0.470385);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa25e90() {
   return (neuron0xfa24fd0()*-2.4501);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa25ed0() {
   return (neuron0xfa253a0()*0.237166);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa25f10() {
   return (neuron0xfa25770()*0.958149);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa26260() {
   return (neuron0xfa24d50()*0.503866);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xf7726f0() {
   return (neuron0xfa24fd0()*3.38179);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xf772730() {
   return (neuron0xfa253a0()*2.51663);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa263b0() {
   return (neuron0xfa25770()*0.133277);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa26730() {
   return (neuron0xfa24d50()*2.9298);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa26770() {
   return (neuron0xfa24fd0()*-0.60036);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa267b0() {
   return (neuron0xfa253a0()*-1.14191);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa267f0() {
   return (neuron0xfa25770()*-0.679917);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa24cd0() {
   return (neuron0xfa25b40()*-2.78385);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa24d10() {
   return (neuron0xfa25f50()*-1.65358);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011::synapse0xfa26ab0() {
   return (neuron0xfa263f0()*3.54835);
}

