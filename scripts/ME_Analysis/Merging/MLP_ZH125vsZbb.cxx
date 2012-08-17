#include "MLP_ZH125vsZbb.h"
#include <cmath>

double MLP_ZH125vsZbb::Value(int index,double in0,double in1,double in2,double in3) {
   input0 = (in0 - 29.5334)/79.1197;
   input1 = (in1 - 20.3306)/0.893865;
   input2 = (in2 - 31.888)/66.9445;
   input3 = (in3 - 13.5769)/1.78677;
   switch(index) {
     case 0:
         return neuron0x7674b40();
     default:
         return 0.;
   }
}

double MLP_ZH125vsZbb::Value(int index, double* input) {
   input0 = (input[0] - 29.5334)/79.1197;
   input1 = (input[1] - 20.3306)/0.893865;
   input2 = (input[2] - 31.888)/66.9445;
   input3 = (input[3] - 13.5769)/1.78677;
   switch(index) {
     case 0:
         return neuron0x7674b40();
     default:
         return 0.;
   }
}

double MLP_ZH125vsZbb::neuron0x76705a0() {
   return input0;
}

double MLP_ZH125vsZbb::neuron0x76708b0() {
   return input1;
}

double MLP_ZH125vsZbb::neuron0x7670bc0() {
   return input2;
}

double MLP_ZH125vsZbb::neuron0x7670ed0() {
   return input3;
}

double MLP_ZH125vsZbb::input0x7671320() {
   double input = 0.810425;
   input += synapse0x9a72da0();
   input += synapse0x764b640();
   input += synapse0x76772f0();
   input += synapse0x76715a0();
   return input;
}

double MLP_ZH125vsZbb::neuron0x7671320() {
   double input = input0x7671320();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x76715e0() {
   double input = -0.740808;
   input += synapse0x76718f0();
   input += synapse0x7671930();
   input += synapse0x7671970();
   input += synapse0x76719b0();
   return input;
}

double MLP_ZH125vsZbb::neuron0x76715e0() {
   double input = input0x76715e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x76719f0() {
   double input = -2.36173;
   input += synapse0x7671d00();
   input += synapse0x7671d40();
   input += synapse0x7671d80();
   input += synapse0x7671dc0();
   return input;
}

double MLP_ZH125vsZbb::neuron0x76719f0() {
   double input = input0x76719f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x7671e00() {
   double input = -1.12339;
   input += synapse0x7672110();
   input += synapse0x7672150();
   input += synapse0x7672190();
   input += synapse0x76721d0();
   return input;
}

double MLP_ZH125vsZbb::neuron0x7671e00() {
   double input = input0x7671e00();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x7672210() {
   double input = -7.12581;
   input += synapse0x7672520();
   input += synapse0x760c830();
   input += synapse0x7606ee0();
   input += synapse0x7606f20();
   return input;
}

double MLP_ZH125vsZbb::neuron0x7672210() {
   double input = input0x7672210();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x7672670() {
   double input = -3.24825;
   input += synapse0x7672980();
   input += synapse0x76729c0();
   input += synapse0x7672a00();
   input += synapse0x7672a40();
   return input;
}

double MLP_ZH125vsZbb::neuron0x7672670() {
   double input = input0x7672670();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x7672a80() {
   double input = 0.273577;
   input += synapse0x7672d90();
   input += synapse0x7672dd0();
   input += synapse0x7672e10();
   input += synapse0x7672e50();
   input += synapse0x7672e90();
   input += synapse0x7672ed0();
   return input;
}

double MLP_ZH125vsZbb::neuron0x7672a80() {
   double input = input0x7672a80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x7672f10() {
   double input = -0.258079;
   input += synapse0x7673250();
   input += synapse0x7673290();
   input += synapse0x76732d0();
   input += synapse0x76772a0();
   input += synapse0x7606f60();
   input += synapse0x7672560();
   return input;
}

double MLP_ZH125vsZbb::neuron0x7672f10() {
   double input = input0x7672f10();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x7673520() {
   double input = -0.196638;
   input += synapse0x7673830();
   input += synapse0x7673870();
   input += synapse0x76738b0();
   input += synapse0x76738f0();
   input += synapse0x7673930();
   input += synapse0x7673970();
   return input;
}

double MLP_ZH125vsZbb::neuron0x7673520() {
   double input = input0x7673520();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x76739b0() {
   double input = -2.54922;
   input += synapse0x7673cf0();
   input += synapse0x7673d30();
   input += synapse0x7673d70();
   input += synapse0x7673db0();
   input += synapse0x7673df0();
   input += synapse0x7673e30();
   return input;
}

double MLP_ZH125vsZbb::neuron0x76739b0() {
   double input = input0x76739b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x7673e70() {
   double input = 0.216156;
   input += synapse0x76741b0();
   input += synapse0x76741f0();
   input += synapse0x7674230();
   input += synapse0x7674270();
   return input;
}

double MLP_ZH125vsZbb::neuron0x7673e70() {
   double input = input0x7673e70();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x76742b0() {
   double input = -0.966667;
   input += synapse0x76745f0();
   input += synapse0x7674630();
   input += synapse0x7674670();
   input += synapse0x76746b0();
   return input;
}

double MLP_ZH125vsZbb::neuron0x76742b0() {
   double input = input0x76742b0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x76746f0() {
   double input = 0.120587;
   input += synapse0x7606d30();
   input += synapse0x7606d70();
   input += synapse0x76725a0();
   input += synapse0x76725e0();
   return input;
}

double MLP_ZH125vsZbb::neuron0x76746f0() {
   double input = input0x76746f0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_ZH125vsZbb::input0x7674b40() {
   double input = 1.71485;
   input += synapse0x7674e80();
   input += synapse0x7674ec0();
   input += synapse0x7674f00();
   return input;
}

double MLP_ZH125vsZbb::neuron0x7674b40() {
   double input = input0x7674b40();
   return (input * 1)+0;
}

double MLP_ZH125vsZbb::synapse0x9a72da0() {
   return (neuron0x76705a0()*7.13994);
}

double MLP_ZH125vsZbb::synapse0x764b640() {
   return (neuron0x76708b0()*-1.40628);
}

double MLP_ZH125vsZbb::synapse0x76772f0() {
   return (neuron0x7670bc0()*0.347982);
}

double MLP_ZH125vsZbb::synapse0x76715a0() {
   return (neuron0x7670ed0()*1.72856);
}

double MLP_ZH125vsZbb::synapse0x76718f0() {
   return (neuron0x76705a0()*-5.29901);
}

double MLP_ZH125vsZbb::synapse0x7671930() {
   return (neuron0x76708b0()*-2.3719);
}

double MLP_ZH125vsZbb::synapse0x7671970() {
   return (neuron0x7670bc0()*1.36);
}

double MLP_ZH125vsZbb::synapse0x76719b0() {
   return (neuron0x7670ed0()*3.05109);
}

double MLP_ZH125vsZbb::synapse0x7671d00() {
   return (neuron0x76705a0()*2.08036);
}

double MLP_ZH125vsZbb::synapse0x7671d40() {
   return (neuron0x76708b0()*-6.60821);
}

double MLP_ZH125vsZbb::synapse0x7671d80() {
   return (neuron0x7670bc0()*1.5454);
}

double MLP_ZH125vsZbb::synapse0x7671dc0() {
   return (neuron0x7670ed0()*0.330792);
}

double MLP_ZH125vsZbb::synapse0x7672110() {
   return (neuron0x76705a0()*-5.96762);
}

double MLP_ZH125vsZbb::synapse0x7672150() {
   return (neuron0x76708b0()*-0.844186);
}

double MLP_ZH125vsZbb::synapse0x7672190() {
   return (neuron0x7670bc0()*-0.293688);
}

double MLP_ZH125vsZbb::synapse0x76721d0() {
   return (neuron0x7670ed0()*1.29739);
}

double MLP_ZH125vsZbb::synapse0x7672520() {
   return (neuron0x76705a0()*3.59872);
}

double MLP_ZH125vsZbb::synapse0x760c830() {
   return (neuron0x76708b0()*-4.6353);
}

double MLP_ZH125vsZbb::synapse0x7606ee0() {
   return (neuron0x7670bc0()*2.0546);
}

double MLP_ZH125vsZbb::synapse0x7606f20() {
   return (neuron0x7670ed0()*-2.95734);
}

double MLP_ZH125vsZbb::synapse0x7672980() {
   return (neuron0x76705a0()*-0.541656);
}

double MLP_ZH125vsZbb::synapse0x76729c0() {
   return (neuron0x76708b0()*1.40395);
}

double MLP_ZH125vsZbb::synapse0x7672a00() {
   return (neuron0x7670bc0()*1.65861);
}

double MLP_ZH125vsZbb::synapse0x7672a40() {
   return (neuron0x7670ed0()*-3.93731);
}

double MLP_ZH125vsZbb::synapse0x7672d90() {
   return (neuron0x7671320()*0.000227596);
}

double MLP_ZH125vsZbb::synapse0x7672dd0() {
   return (neuron0x76715e0()*-3.12884);
}

double MLP_ZH125vsZbb::synapse0x7672e10() {
   return (neuron0x76719f0()*1.26218);
}

double MLP_ZH125vsZbb::synapse0x7672e50() {
   return (neuron0x7671e00()*-1.0912);
}

double MLP_ZH125vsZbb::synapse0x7672e90() {
   return (neuron0x7672210()*0.487518);
}

double MLP_ZH125vsZbb::synapse0x7672ed0() {
   return (neuron0x7672670()*1.50837);
}

double MLP_ZH125vsZbb::synapse0x7673250() {
   return (neuron0x7671320()*-6.28759);
}

double MLP_ZH125vsZbb::synapse0x7673290() {
   return (neuron0x76715e0()*2.73349);
}

double MLP_ZH125vsZbb::synapse0x76732d0() {
   return (neuron0x76719f0()*0.187868);
}

double MLP_ZH125vsZbb::synapse0x76772a0() {
   return (neuron0x7671e00()*5.39289);
}

double MLP_ZH125vsZbb::synapse0x7606f60() {
   return (neuron0x7672210()*-3.26692);
}

double MLP_ZH125vsZbb::synapse0x7672560() {
   return (neuron0x7672670()*-0.693817);
}

double MLP_ZH125vsZbb::synapse0x7673830() {
   return (neuron0x7671320()*-0.355233);
}

double MLP_ZH125vsZbb::synapse0x7673870() {
   return (neuron0x76715e0()*0.817001);
}

double MLP_ZH125vsZbb::synapse0x76738b0() {
   return (neuron0x76719f0()*2.41266);
}

double MLP_ZH125vsZbb::synapse0x76738f0() {
   return (neuron0x7671e00()*-0.0875163);
}

double MLP_ZH125vsZbb::synapse0x7673930() {
   return (neuron0x7672210()*-1.2487);
}

double MLP_ZH125vsZbb::synapse0x7673970() {
   return (neuron0x7672670()*0.0680388);
}

double MLP_ZH125vsZbb::synapse0x7673cf0() {
   return (neuron0x7671320()*-0.117472);
}

double MLP_ZH125vsZbb::synapse0x7673d30() {
   return (neuron0x76715e0()*-2.52199);
}

double MLP_ZH125vsZbb::synapse0x7673d70() {
   return (neuron0x76719f0()*1.87333);
}

double MLP_ZH125vsZbb::synapse0x7673db0() {
   return (neuron0x7671e00()*1.23367);
}

double MLP_ZH125vsZbb::synapse0x7673df0() {
   return (neuron0x7672210()*2.7203);
}

double MLP_ZH125vsZbb::synapse0x7673e30() {
   return (neuron0x7672670()*1.68869);
}

double MLP_ZH125vsZbb::synapse0x76741b0() {
   return (neuron0x7672a80()*-0.571783);
}

double MLP_ZH125vsZbb::synapse0x76741f0() {
   return (neuron0x7672f10()*1.40897);
}

double MLP_ZH125vsZbb::synapse0x7674230() {
   return (neuron0x7673520()*-0.0984802);
}

double MLP_ZH125vsZbb::synapse0x7674270() {
   return (neuron0x76739b0()*0.658342);
}

double MLP_ZH125vsZbb::synapse0x76745f0() {
   return (neuron0x7672a80()*-2.63149);
}

double MLP_ZH125vsZbb::synapse0x7674630() {
   return (neuron0x7672f10()*6.00999);
}

double MLP_ZH125vsZbb::synapse0x7674670() {
   return (neuron0x7673520()*-1.39304);
}

double MLP_ZH125vsZbb::synapse0x76746b0() {
   return (neuron0x76739b0()*2.86647);
}

double MLP_ZH125vsZbb::synapse0x7606d30() {
   return (neuron0x7672a80()*-2.16649);
}

double MLP_ZH125vsZbb::synapse0x7606d70() {
   return (neuron0x7672f10()*0.660061);
}

double MLP_ZH125vsZbb::synapse0x76725a0() {
   return (neuron0x7673520()*0.882249);
}

double MLP_ZH125vsZbb::synapse0x76725e0() {
   return (neuron0x76739b0()*-2.8561);
}

double MLP_ZH125vsZbb::synapse0x7674e80() {
   return (neuron0x7673e70()*-0.224894);
}

double MLP_ZH125vsZbb::synapse0x7674ec0() {
   return (neuron0x76742b0()*-4.35118);
}

double MLP_ZH125vsZbb::synapse0x7674f00() {
   return (neuron0x76746f0()*3.53655);
}

