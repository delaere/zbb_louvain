#ifndef MLP_Higgs_vs_Bkg_ZH125_comb_1_10000_h
#define MLP_Higgs_vs_Bkg_ZH125_comb_1_10000_h

class MLP_Higgs_vs_Bkg_ZH125_comb_1_10000 { 
public:
   MLP_Higgs_vs_Bkg_ZH125_comb_1_10000() {}
   ~MLP_Higgs_vs_Bkg_ZH125_comb_1_10000() {}
   double Value(int index,double in0,double in1,double in2);
   double Value(int index, double* input);
private:
   double input0;
   double input1;
   double input2;
   double neuron0x14df8490();
   double neuron0x14df87d0();
   double neuron0x14e097a0();
   double input0x14e09af0();
   double neuron0x14e09af0();
   double input0x14e09de0();
   double neuron0x14e09de0();
   double synapse0x14dc0ce0();
   double synapse0x14ddf230();
   double synapse0x14e09da0();
   double synapse0x14e0a000();
};

#endif // MLP_Higgs_vs_Bkg_ZH125_comb_1_10000_h

