#include "../NN/MLP_Higgs_vs_BKG_ML_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.468998)/0.304782;
   input1 = (in1 - 0.511748)/0.271728;
   input2 = (in2 - 0.404868)/0.354892;
   switch(index) {
     case 0:
         return neuron0xa207f20();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 0.468998)/0.304782;
   input1 = (input[1] - 0.511748)/0.271728;
   input2 = (input[2] - 0.404868)/0.354892;
   switch(index) {
     case 0:
         return neuron0xa207f20();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::neuron0xa0f9190() {
   return input0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::neuron0xa0f94a0() {
   return input1;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::neuron0xa209f10() {
   return input2;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::input0xa20a360() {
   double input = -3.03665;
   input += synapse0xa0f8f70();
   input += synapse0xa17ab10();
   input += synapse0x9f9a4b0();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::neuron0xa20a360() {
   double input = input0xa20a360();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::input0xa20a5e0() {
   double input = -1.09016;
   input += synapse0xa20a8f0();
   input += synapse0xa20a930();
   input += synapse0xa20a970();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::neuron0xa20a5e0() {
   double input = input0xa20a5e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::input0xa20a9b0() {
   double input = 2.40298;
   input += synapse0xa17ab90();
   input += synapse0xa0f9600();
   input += synapse0xa0f9640();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::neuron0xa20a9b0() {
   double input = input0xa20a9b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::input0xa206e60() {
   double input = -1.63217;
   input += synapse0xa207170();
   input += synapse0xa2071b0();
   input += synapse0xa2071f0();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::neuron0xa206e60() {
   double input = input0xa206e60();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::input0xa207230() {
   double input = -0.187934;
   input += synapse0xa207540();
   input += synapse0xa207580();
   input += synapse0xa2075c0();
   input += synapse0xa207600();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::neuron0xa207230() {
   double input = input0xa207230();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::input0xa207640() {
   double input = -0.914768;
   input += synapse0xa207950();
   input += synapse0xa0b9cf0();
   input += synapse0xa0b9d30();
   input += synapse0xa207aa0();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::neuron0xa207640() {
   double input = input0xa207640();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::input0xa207ae0() {
   double input = 1.24754;
   input += synapse0xa207e20();
   input += synapse0xa207e60();
   input += synapse0xa207ea0();
   input += synapse0xa207ee0();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::neuron0xa207ae0() {
   double input = input0xa207ae0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::input0xa207f20() {
   double input = 0.978421;
   input += synapse0xa208260();
   input += synapse0xa2082a0();
   input += synapse0xa2082e0();
   return input;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::neuron0xa207f20() {
   double input = input0xa207f20();
   return (input * 1)+0;
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa0f8f70() {
   return (neuron0xa0f9190()*-1.14409);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa17ab10() {
   return (neuron0xa0f94a0()*-1.96816);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0x9f9a4b0() {
   return (neuron0xa209f10()*-1.24906);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa20a8f0() {
   return (neuron0xa0f9190()*0.565774);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa20a930() {
   return (neuron0xa0f94a0()*0.0169901);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa20a970() {
   return (neuron0xa209f10()*-0.112847);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa17ab90() {
   return (neuron0xa0f9190()*-0.568019);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa0f9600() {
   return (neuron0xa0f94a0()*-0.565316);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa0f9640() {
   return (neuron0xa209f10()*3.38675);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa207170() {
   return (neuron0xa0f9190()*0.880099);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa2071b0() {
   return (neuron0xa0f94a0()*0.504828);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa2071f0() {
   return (neuron0xa209f10()*-1.97404);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa207540() {
   return (neuron0xa20a360()*1.02092);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa207580() {
   return (neuron0xa20a5e0()*-1.17507);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa2075c0() {
   return (neuron0xa20a9b0()*0.818128);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa207600() {
   return (neuron0xa206e60()*0.0156058);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa207950() {
   return (neuron0xa20a360()*0.384053);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa0b9cf0() {
   return (neuron0xa20a5e0()*-4.10683);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa0b9d30() {
   return (neuron0xa20a9b0()*0.0808084);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa207aa0() {
   return (neuron0xa206e60()*2.76472);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa207e20() {
   return (neuron0xa20a360()*0.967707);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa207e60() {
   return (neuron0xa20a5e0()*1.05099);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa207ea0() {
   return (neuron0xa20a9b0()*-1.55182);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa207ee0() {
   return (neuron0xa206e60()*0.901498);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa208260() {
   return (neuron0xa207230()*-1.46105);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa2082a0() {
   return (neuron0xa207640()*-4.28713);
}

double MLP_Higgs_vs_BKG_ML_CSV_2011_mm::synapse0xa2082e0() {
   return (neuron0xa207ae0()*2.06888);
}

