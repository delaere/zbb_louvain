#include "../NN/MLP_Higgs_vs_BKG_MM_CSV_2011_mm.h"
#include <cmath>

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.456021)/0.340486;
   input1 = (in1 - 0.531952)/0.359895;
   input2 = (in2 - 0.369995)/0.373797;
   switch(index) {
     case 0:
         return neuron0x2034bf60();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::Value(int index, double* input) {
   input0 = (input[0] - 0.456021)/0.340486;
   input1 = (input[1] - 0.531952)/0.359895;
   input2 = (input[2] - 0.369995)/0.373797;
   switch(index) {
     case 0:
         return neuron0x2034bf60();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::neuron0x212e4da0() {
   return input0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::neuron0x212e50b0() {
   return input1;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::neuron0x212e53c0() {
   return input2;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::input0x2034a430() {
   double input = 1.43867;
   input += synapse0x1fbf6af0();
   input += synapse0x1fc72050();
   input += synapse0x20dceb10();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::neuron0x2034a430() {
   double input = input0x2034a430();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::input0x2034a740() {
   double input = -3.1139;
   input += synapse0x2034aa50();
   input += synapse0x2034aa90();
   input += synapse0x2034aad0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::neuron0x2034a740() {
   double input = input0x2034a740();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::input0x2034ab10() {
   double input = 4.58753;
   input += synapse0x2034ae20();
   input += synapse0x2034ae60();
   input += synapse0x2034aea0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::neuron0x2034ab10() {
   double input = input0x2034ab10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::input0x2034aee0() {
   double input = -0.386109;
   input += synapse0x2034b1f0();
   input += synapse0x2034b230();
   input += synapse0x2034b270();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::neuron0x2034aee0() {
   double input = input0x2034aee0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::input0x2034b2b0() {
   double input = -1.21075;
   input += synapse0x2034b5c0();
   input += synapse0x2034b600();
   input += synapse0x2034b640();
   input += synapse0x2034b680();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::neuron0x2034b2b0() {
   double input = input0x2034b2b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::input0x2034b6c0() {
   double input = -3.14048;
   input += synapse0x2034b9d0();
   input += synapse0x1fc720d0();
   input += synapse0x1fc2bdc0();
   input += synapse0x1fc2be00();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::neuron0x2034b6c0() {
   double input = input0x2034b6c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::input0x2034bb20() {
   double input = 0.586287;
   input += synapse0x2034be60();
   input += synapse0x2034bea0();
   input += synapse0x2034bee0();
   input += synapse0x2034bf20();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::neuron0x2034bb20() {
   double input = input0x2034bb20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::input0x2034bf60() {
   double input = 1.27037;
   input += synapse0x2034c2a0();
   input += synapse0x2034c2e0();
   input += synapse0x2034c320();
   return input;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::neuron0x2034bf60() {
   double input = input0x2034bf60();
   return (input * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x1fbf6af0() {
   return (neuron0x212e4da0()*-4.03474);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x1fc72050() {
   return (neuron0x212e50b0()*1.12755);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x20dceb10() {
   return (neuron0x212e53c0()*1.45817);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034aa50() {
   return (neuron0x212e4da0()*-1.95207);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034aa90() {
   return (neuron0x212e50b0()*-0.632339);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034aad0() {
   return (neuron0x212e53c0()*1.68356);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034ae20() {
   return (neuron0x212e4da0()*0.495789);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034ae60() {
   return (neuron0x212e50b0()*-3.97358);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034aea0() {
   return (neuron0x212e53c0()*1.04534);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034b1f0() {
   return (neuron0x212e4da0()*0.0042611);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034b230() {
   return (neuron0x212e50b0()*-0.206813);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034b270() {
   return (neuron0x212e53c0()*1.18422);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034b5c0() {
   return (neuron0x2034a430()*-2.02783);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034b600() {
   return (neuron0x2034a740()*1.08474);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034b640() {
   return (neuron0x2034ab10()*1.15163);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034b680() {
   return (neuron0x2034aee0()*0.0358636);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034b9d0() {
   return (neuron0x2034a430()*-2.73472);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x1fc720d0() {
   return (neuron0x2034a740()*-2.92693);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x1fc2bdc0() {
   return (neuron0x2034ab10()*3.8898);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x1fc2be00() {
   return (neuron0x2034aee0()*5.97092);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034be60() {
   return (neuron0x2034a430()*2.84183);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034bea0() {
   return (neuron0x2034a740()*1.625);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034bee0() {
   return (neuron0x2034ab10()*-0.174457);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034bf20() {
   return (neuron0x2034aee0()*-2.07763);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034c2a0() {
   return (neuron0x2034b2b0()*-1.79262);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034c2e0() {
   return (neuron0x2034b6c0()*0.807365);
}

double MLP_Higgs_vs_BKG_MM_CSV_2011_mm::synapse0x2034c320() {
   return (neuron0x2034bb20()*-1.25294);
}

