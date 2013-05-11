#ifndef MLP_Higgs_vs_Bkg_ZH125_comb_1_5000_h
#define MLP_Higgs_vs_Bkg_ZH125_comb_1_5000_h

class MLP_Higgs_vs_Bkg_ZH125_comb_1_5000 { 
public:
   MLP_Higgs_vs_Bkg_ZH125_comb_1_5000() {}
   ~MLP_Higgs_vs_Bkg_ZH125_comb_1_5000() {}
   double Value(int index,double in0,double in1,double in2);
   double Value(int index, double* input);
private:
   double input0;
   double input1;
   double input2;
   double neuron0xfbfeb20();
   double neuron0xfbfee60();
   double neuron0xfc0fe30();
   double input0xfc10180();
   double neuron0xfc10180();
   double input0xfc104b0();
   double neuron0xfc104b0();
   double synapse0xfbc6f30();
   double synapse0xfc10430();
   double synapse0xfc10470();
   double synapse0xfc106d0();
};

#endif // MLP_Higgs_vs_Bkg_ZH125_comb_1_5000_h

