#include "../NN/MLP_Higgs_vs_TT_ML_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 21.9627)/1.14982;
   input1 = (in1 - 26.0002)/1.80421;
   input2 = (in2 - 14.9802)/2.27791;
   switch(index) {
     case 0:
         return neuron0x4210470();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 21.9627)/1.14982;
   input1 = (input[1] - 26.0002)/1.80421;
   input2 = (input[2] - 14.9802)/2.27791;
   switch(index) {
     case 0:
         return neuron0x4210470();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420cb60() {
   return input0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420ce70() {
   return input1;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420d180() {
   return input2;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x420d5d0() {
   double input = -0.576015;
   input += synapse0x3f1cc80();
   input += synapse0x3f1cd10();
   input += synapse0x420d850();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420d5d0() {
   double input = input0x420d5d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x420d890() {
   double input = 0.519866;
   input += synapse0x420dba0();
   input += synapse0x420dbe0();
   input += synapse0x420dc20();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420d890() {
   double input = input0x420d890();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x420dc60() {
   double input = -2.2387;
   input += synapse0x420df70();
   input += synapse0x420dfb0();
   input += synapse0x420dff0();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420dc60() {
   double input = input0x420dc60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x420e030() {
   double input = -1.12683;
   input += synapse0x420e340();
   input += synapse0x420e380();
   input += synapse0x420e3c0();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420e030() {
   double input = input0x420e030();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x420e400() {
   double input = -1.32264;
   input += synapse0x420e710();
   input += synapse0x420e750();
   input += synapse0x420e790();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420e400() {
   double input = input0x420e400();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x420e7d0() {
   double input = -2.83739;
   input += synapse0x420eb10();
   input += synapse0x420eb50();
   input += synapse0x3e2ce50();
   input += synapse0x3e2ce90();
   input += synapse0x420eca0();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420e7d0() {
   double input = input0x420e7d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x420ece0() {
   double input = -2.2134;
   input += synapse0x420f020();
   input += synapse0x420f060();
   input += synapse0x420f0a0();
   input += synapse0x420f0e0();
   input += synapse0x420f120();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420ece0() {
   double input = input0x420ece0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x420f160() {
   double input = 0.984403;
   input += synapse0x420f4a0();
   input += synapse0x420f4e0();
   input += synapse0x420f520();
   input += synapse0x420f560();
   input += synapse0x420f5a0();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420f160() {
   double input = input0x420f160();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x420f5e0() {
   double input = -0.923037;
   input += synapse0x420f920();
   input += synapse0x420f960();
   input += synapse0x420f9a0();
   input += synapse0x301d140();
   input += synapse0x3f1c910();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420f5e0() {
   double input = input0x420f5e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x420fbf0() {
   double input = 0.603902;
   input += synapse0x420ff30();
   input += synapse0x420ff70();
   input += synapse0x420ffb0();
   input += synapse0x420fff0();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x420fbf0() {
   double input = input0x420fbf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x4210030() {
   double input = -0.0515209;
   input += synapse0x4210370();
   input += synapse0x42103b0();
   input += synapse0x42103f0();
   input += synapse0x4210430();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x4210030() {
   double input = input0x4210030();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::input0x4210470() {
   double input = 0.38192;
   input += synapse0x42107b0();
   input += synapse0x42107f0();
   return input;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::neuron0x4210470() {
   double input = input0x4210470();
   return (input * 1)+0;
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x3f1cc80() {
   return (neuron0x420cb60()*-0.735517);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x3f1cd10() {
   return (neuron0x420ce70()*-2.14925);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420d850() {
   return (neuron0x420d180()*6.26584);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420dba0() {
   return (neuron0x420cb60()*0.215407);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420dbe0() {
   return (neuron0x420ce70()*-2.42178);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420dc20() {
   return (neuron0x420d180()*4.03983);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420df70() {
   return (neuron0x420cb60()*1.50999);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420dfb0() {
   return (neuron0x420ce70()*-2.11744);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420dff0() {
   return (neuron0x420d180()*0.396258);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420e340() {
   return (neuron0x420cb60()*-0.303727);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420e380() {
   return (neuron0x420ce70()*4.91585);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420e3c0() {
   return (neuron0x420d180()*-1.23967);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420e710() {
   return (neuron0x420cb60()*-2.8044);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420e750() {
   return (neuron0x420ce70()*0.865778);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420e790() {
   return (neuron0x420d180()*-0.319977);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420eb10() {
   return (neuron0x420d5d0()*-2.91487);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420eb50() {
   return (neuron0x420d890()*4.21133);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x3e2ce50() {
   return (neuron0x420dc60()*-4.66232);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x3e2ce90() {
   return (neuron0x420e030()*1.55761);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420eca0() {
   return (neuron0x420e400()*2.25409);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f020() {
   return (neuron0x420d5d0()*1.25062);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f060() {
   return (neuron0x420d890()*-2.80924);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f0a0() {
   return (neuron0x420dc60()*-3.24815);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f0e0() {
   return (neuron0x420e030()*-2.56314);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f120() {
   return (neuron0x420e400()*1.9235);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f4a0() {
   return (neuron0x420d5d0()*-1.52216);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f4e0() {
   return (neuron0x420d890()*1.54415);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f520() {
   return (neuron0x420dc60()*2.03615);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f560() {
   return (neuron0x420e030()*2.44173);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f5a0() {
   return (neuron0x420e400()*0.0269924);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f920() {
   return (neuron0x420d5d0()*-0.322958);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f960() {
   return (neuron0x420d890()*0.0445294);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420f9a0() {
   return (neuron0x420dc60()*1.49279);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x301d140() {
   return (neuron0x420e030()*1.25686);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x3f1c910() {
   return (neuron0x420e400()*1.1342);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420ff30() {
   return (neuron0x420e7d0()*-4.99781);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420ff70() {
   return (neuron0x420ece0()*2.95094);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420ffb0() {
   return (neuron0x420f160()*-1.55923);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x420fff0() {
   return (neuron0x420f5e0()*1.14885);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x4210370() {
   return (neuron0x420e7d0()*-1.14378);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x42103b0() {
   return (neuron0x420ece0()*0.304622);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x42103f0() {
   return (neuron0x420f160()*-0.152798);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x4210430() {
   return (neuron0x420f5e0()*0.491256);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x42107b0() {
   return (neuron0x420fbf0()*2.92185);
}

double MLP_Higgs_vs_TT_ML_CSV_2011_mm::synapse0x42107f0() {
   return (neuron0x4210030()*-1.3425);
}

