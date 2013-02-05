#include "../NN/MLP_Higgs_vs_DY_MM_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_DY_MM_CSV_2011::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 19.6727)/1.09096;
   input1 = (in1 - 20.3089)/0.96465;
   input2 = (in2 - 24.6459)/1.27911;
   input3 = (in3 - 13.33)/1.55541;
   switch(index) {
     case 0:
         return neuron0x7440730();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 19.6727)/1.09096;
   input1 = (input[1] - 20.3089)/0.96465;
   input2 = (input[2] - 24.6459)/1.27911;
   input3 = (input[3] - 13.33)/1.55541;
   switch(index) {
     case 0:
         return neuron0x7440730();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x743d730() {
   return input0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x743da40() {
   return input1;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x743dd50() {
   return input2;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x743e060() {
   return input3;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::input0x743e4b0() {
   double input = -1.80249;
   input += synapse0x73e6680();
   input += synapse0x743e730();
   input += synapse0x743e770();
   input += synapse0x743e7b0();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x743e4b0() {
   double input = input0x743e4b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::input0x743e7f0() {
   double input = 4.2818;
   input += synapse0x743eb00();
   input += synapse0x743eb40();
   input += synapse0x743eb80();
   input += synapse0x743ebc0();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x743e7f0() {
   double input = input0x743e7f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::input0x743ec00() {
   double input = 0.380195;
   input += synapse0x743ef10();
   input += synapse0x743ef50();
   input += synapse0x743ef90();
   input += synapse0x743efd0();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x743ec00() {
   double input = input0x743ec00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::input0x743f010() {
   double input = 0.118371;
   input += synapse0x743f320();
   input += synapse0x743f360();
   input += synapse0x743f3a0();
   input += synapse0x743f3e0();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x743f010() {
   double input = input0x743f010();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::input0x743f420() {
   double input = 3.18881;
   input += synapse0x743f730();
   input += synapse0x73e62d0();
   input += synapse0x7182cd0();
   input += synapse0x7182d10();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x743f420() {
   double input = input0x743f420();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::input0x743f880() {
   double input = -0.565741;
   input += synapse0x743fb90();
   input += synapse0x743fbd0();
   input += synapse0x743fc10();
   input += synapse0x743fc50();
   input += synapse0x743fc90();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x743f880() {
   double input = input0x743f880();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::input0x743fcd0() {
   double input = 0.0485814;
   input += synapse0x743ffe0();
   input += synapse0x7440020();
   input += synapse0x7440060();
   input += synapse0x74400a0();
   input += synapse0x74400e0();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x743fcd0() {
   double input = input0x743fcd0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::input0x7440120() {
   double input = 0.278277;
   input += synapse0x7440460();
   input += synapse0x74404a0();
   input += synapse0x74404e0();
   input += synapse0x7400ee0();
   input += synapse0x7444430();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x7440120() {
   double input = input0x7440120();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::input0x7440730() {
   double input = 0.0554279;
   input += synapse0x7440a70();
   input += synapse0x7440ab0();
   input += synapse0x7440af0();
   return input;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::neuron0x7440730() {
   double input = input0x7440730();
   return (input * 1)+0;
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x73e6680() {
   return (neuron0x743d730()*-8.23045);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743e730() {
   return (neuron0x743da40()*-4.41845);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743e770() {
   return (neuron0x743dd50()*6.57124);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743e7b0() {
   return (neuron0x743e060()*5.67068);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743eb00() {
   return (neuron0x743d730()*4.45522);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743eb40() {
   return (neuron0x743da40()*-0.666568);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743eb80() {
   return (neuron0x743dd50()*-5.10835);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743ebc0() {
   return (neuron0x743e060()*0.410921);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743ef10() {
   return (neuron0x743d730()*0.881885);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743ef50() {
   return (neuron0x743da40()*-0.249619);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743ef90() {
   return (neuron0x743dd50()*0.439842);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743efd0() {
   return (neuron0x743e060()*-1.82032);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743f320() {
   return (neuron0x743d730()*-2.83154);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743f360() {
   return (neuron0x743da40()*2.27531);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743f3a0() {
   return (neuron0x743dd50()*-0.3933);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743f3e0() {
   return (neuron0x743e060()*2.41695);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743f730() {
   return (neuron0x743d730()*2.07047);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x73e62d0() {
   return (neuron0x743da40()*4.50666);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x7182cd0() {
   return (neuron0x743dd50()*-7.94865);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x7182d10() {
   return (neuron0x743e060()*2.08744);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743fb90() {
   return (neuron0x743e4b0()*-3.8871);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743fbd0() {
   return (neuron0x743e7f0()*1.201);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743fc10() {
   return (neuron0x743ec00()*3.50057);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743fc50() {
   return (neuron0x743f010()*2.99217);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743fc90() {
   return (neuron0x743f420()*-5.96292);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x743ffe0() {
   return (neuron0x743e4b0()*-1.95313);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x7440020() {
   return (neuron0x743e7f0()*-0.801911);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x7440060() {
   return (neuron0x743ec00()*2.37745);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x74400a0() {
   return (neuron0x743f010()*-0.143337);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x74400e0() {
   return (neuron0x743f420()*-3.31217);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x7440460() {
   return (neuron0x743e4b0()*-0.198348);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x74404a0() {
   return (neuron0x743e7f0()*-1.41186);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x74404e0() {
   return (neuron0x743ec00()*3.15741);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x7400ee0() {
   return (neuron0x743f010()*-2.35571);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x7444430() {
   return (neuron0x743f420()*-0.54939);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x7440a70() {
   return (neuron0x743f880()*2.41453);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x7440ab0() {
   return (neuron0x743fcd0()*-5.8065);
}

double MLP_Higgs_vs_DY_MM_CSV_2011::synapse0x7440af0() {
   return (neuron0x7440120()*1.86502);
}

