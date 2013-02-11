#include "MLP_Higgs_vs_BKG_MM_N_CSV_2011.h"
#include <cmath>

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.514094)/0.333508;
   input1 = (in1 - 0.566862)/0.316671;
   input2 = (in2 - 0.512574)/0.363402;
   switch(index) {
     case 0:
         return neuron0x1b3173a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::Value(int index, double* input) {
   input0 = (input[0] - 0.514094)/0.333508;
   input1 = (input[1] - 0.566862)/0.316671;
   input2 = (input[2] - 0.512574)/0.363402;
   switch(index) {
     case 0:
         return neuron0x1b3173a0();
     default:
         return 0.;
   }
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b302b40() {
   return input0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b302e80() {
   return input1;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b313e50() {
   return input2;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b3141a0() {
   double input = -3.02687;
   input += synapse0x1b2cb310();
   input += synapse0x1b2e98a0();
   input += synapse0x1b314450();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b3141a0() {
   double input = input0x1b3141a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b314490() {
   double input = -2.47678;
   input += synapse0x1b3147d0();
   input += synapse0x1b314810();
   input += synapse0x1b314850();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b314490() {
   double input = input0x1b314490();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b314890() {
   double input = -0.257161;
   input += synapse0x1b314bd0();
   input += synapse0x1b314c10();
   input += synapse0x1b314c50();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b314890() {
   double input = input0x1b314890();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b314c90() {
   double input = 0.937001;
   input += synapse0x1b314fd0();
   input += synapse0x1b315010();
   input += synapse0x1b315050();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b314c90() {
   double input = input0x1b314c90();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b315090() {
   double input = 0.482086;
   input += synapse0x1b3153d0();
   input += synapse0x1b315410();
   input += synapse0x1b315450();
   input += synapse0x1b315490();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b315090() {
   double input = input0x1b315090();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b3154d0() {
   double input = 0.825113;
   input += synapse0x1b315810();
   input += synapse0x1b271a30();
   input += synapse0x1b271a70();
   input += synapse0x1b315960();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b3154d0() {
   double input = input0x1b3154d0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b3159a0() {
   double input = 1.99621;
   input += synapse0x1b315ce0();
   input += synapse0x1b315d20();
   input += synapse0x1b315d60();
   input += synapse0x1b315da0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b3159a0() {
   double input = input0x1b3159a0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b315de0() {
   double input = -0.324221;
   input += synapse0x1b316120();
   input += synapse0x1b316160();
   input += synapse0x1b3161a0();
   input += synapse0x1b3161e0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b315de0() {
   double input = input0x1b315de0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b316220() {
   double input = -0.152773;
   input += synapse0x1b316560();
   input += synapse0x1b3165a0();
   input += synapse0x1b3165e0();
   input += synapse0x1b316620();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b316220() {
   double input = input0x1b316220();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b316660() {
   double input = -0.189447;
   input += synapse0x1b3169a0();
   input += synapse0x1b2e9940();
   input += synapse0x1b2cb2c0();
   input += synapse0x1b2cb350();
   input += synapse0x1b2cb390();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b316660() {
   double input = input0x1b316660();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b316bf0() {
   double input = -0.000540106;
   input += synapse0x1b2cb3d0();
   input += synapse0x1b3158e0();
   input += synapse0x1b315920();
   input += synapse0x1b316ea0();
   input += synapse0x1b316ee0();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b316bf0() {
   double input = input0x1b316bf0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b316f20() {
   double input = 0.25496;
   input += synapse0x1b317260();
   input += synapse0x1b3172a0();
   input += synapse0x1b3172e0();
   input += synapse0x1b317320();
   input += synapse0x1b317360();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b316f20() {
   double input = input0x1b316f20();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::input0x1b3173a0() {
   double input = -0.685555;
   input += synapse0x1b3175c0();
   input += synapse0x1b317600();
   input += synapse0x1b317640();
   return input;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::neuron0x1b3173a0() {
   double input = input0x1b3173a0();
   return (input * 1)+0;
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b2cb310() {
   return (neuron0x1b302b40()*-5.41636);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b2e98a0() {
   return (neuron0x1b302e80()*1.19259);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b314450() {
   return (neuron0x1b313e50()*-0.164032);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b3147d0() {
   return (neuron0x1b302b40()*1.16836);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b314810() {
   return (neuron0x1b302e80()*-2.56389);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b314850() {
   return (neuron0x1b313e50()*1.40462);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b314bd0() {
   return (neuron0x1b302b40()*2.73989);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b314c10() {
   return (neuron0x1b302e80()*-1.14752);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b314c50() {
   return (neuron0x1b313e50()*-0.0750095);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b314fd0() {
   return (neuron0x1b302b40()*-1.16823);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315010() {
   return (neuron0x1b302e80()*0.468576);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315050() {
   return (neuron0x1b313e50()*0.716137);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b3153d0() {
   return (neuron0x1b3141a0()*1.52886);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315410() {
   return (neuron0x1b314490()*-2.28727);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315450() {
   return (neuron0x1b314890()*2.08182);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315490() {
   return (neuron0x1b314c90()*2.90147);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315810() {
   return (neuron0x1b3141a0()*0.482446);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b271a30() {
   return (neuron0x1b314490()*-1.9091);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b271a70() {
   return (neuron0x1b314890()*0.39683);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315960() {
   return (neuron0x1b314c90()*0.728684);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315ce0() {
   return (neuron0x1b3141a0()*-3.52452);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315d20() {
   return (neuron0x1b314490()*0.580456);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315d60() {
   return (neuron0x1b314890()*-0.618224);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315da0() {
   return (neuron0x1b314c90()*-1.24089);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b316120() {
   return (neuron0x1b3141a0()*-4.08078);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b316160() {
   return (neuron0x1b314490()*-0.802508);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b3161a0() {
   return (neuron0x1b314890()*1.34962);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b3161e0() {
   return (neuron0x1b314c90()*3.00394);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b316560() {
   return (neuron0x1b3141a0()*0.255485);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b3165a0() {
   return (neuron0x1b314490()*0.65396);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b3165e0() {
   return (neuron0x1b314890()*-2.1876);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b316620() {
   return (neuron0x1b314c90()*0.900606);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b3169a0() {
   return (neuron0x1b315090()*-1.25206);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b2e9940() {
   return (neuron0x1b3154d0()*1.49591);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b2cb2c0() {
   return (neuron0x1b3159a0()*1.86926);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b2cb350() {
   return (neuron0x1b315de0()*-1.63022);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b2cb390() {
   return (neuron0x1b316220()*0.807045);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b2cb3d0() {
   return (neuron0x1b315090()*-0.170788);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b3158e0() {
   return (neuron0x1b3154d0()*0.123255);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b315920() {
   return (neuron0x1b3159a0()*0.0425499);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b316ea0() {
   return (neuron0x1b315de0()*-0.135911);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b316ee0() {
   return (neuron0x1b316220()*-0.104301);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b317260() {
   return (neuron0x1b315090()*2.75792);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b3172a0() {
   return (neuron0x1b3154d0()*-0.349998);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b3172e0() {
   return (neuron0x1b3159a0()*-2.97055);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b317320() {
   return (neuron0x1b315de0()*2.03436);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b317360() {
   return (neuron0x1b316220()*-2.03114);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b3175c0() {
   return (neuron0x1b316660()*-2.96572);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b317600() {
   return (neuron0x1b316bf0()*-0.486602);
}

double MLP_Higgs_vs_BKG_MM_N_CSV_2011::synapse0x1b317640() {
   return (neuron0x1b316f20()*3.42326);
}

