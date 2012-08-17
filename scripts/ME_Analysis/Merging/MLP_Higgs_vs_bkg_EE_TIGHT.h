#ifndef MLP_Higgs_vs_bkg_EE_TIGHT_h
#define MLP_Higgs_vs_bkg_EE_TIGHT_h

class MLP_Higgs_vs_bkg_EE_TIGHT { 
public:
   MLP_Higgs_vs_bkg_EE_TIGHT() {}
   ~MLP_Higgs_vs_bkg_EE_TIGHT() {}
   double Value(int index,double in0,double in1,double in2);
   double Value(int index, double* input);
private:
   double input0;
   double input1;
   double input2;
   double neuron0x18382b20();
   double neuron0x18382e30();
   double neuron0x18393cc0();
   double input0x18394110();
   double neuron0x18394110();
   double input0x18394390();
   double neuron0x18394390();
   double input0x18394720();
   double neuron0x18394720();
   double input0x18394af0();
   double neuron0x18394af0();
   double input0x18394ec0();
   double neuron0x18394ec0();
   double input0x183952d0();
   double neuron0x183952d0();
   double input0x183957a0();
   double neuron0x183957a0();
   double synapse0x17df5f60();
   double synapse0x17de3000();
   double synapse0x18383140();
   double synapse0x18383180();
   double synapse0x183946a0();
   double synapse0x183946e0();
   double synapse0x18394a30();
   double synapse0x18394a70();
   double synapse0x18394ab0();
   double synapse0x18394e00();
   double synapse0x18394e40();
   double synapse0x18394e80();
   double synapse0x183951d0();
   double synapse0x18395210();
   double synapse0x18395250();
   double synapse0x18395290();
   double synapse0x18395610();
   double synapse0x17de3470();
   double synapse0x17de34b0();
   double synapse0x18395760();
   double synapse0x18394090();
   double synapse0x183940d0();
};

#endif // MLP_Higgs_vs_bkg_EE_TIGHT_h

