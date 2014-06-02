from math import exp

from math import tanh

class MLP_Higgs_vs_TT_MM_N_CSV_2012_comb_ZH125_5_2_3_1_500:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 22.1454)/2.02206
		self.input1 = (in1 - 25.1712)/2.09579
		self.input2 = (in2 - 13.8698)/2.37204
		if index==0: return self.neuron0x5a24cf0();
		return 0.
	def neuron0x5a10900(self):
		return self.input0
	def neuron0x5a10c40(self):
		return self.input1
	def neuron0x5a21b80(self):
		return self.input2
	def neuron0x5a21f60(self):
		input = -0.0588938
		input = input + self.synapse0x59f75c0()
		input = input + self.synapse0x59d9080()
		input = input + self.synapse0x5a22210()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5a22250(self):
		input = 2.79388
		input = input + self.synapse0x5a22590()
		input = input + self.synapse0x5a225d0()
		input = input + self.synapse0x5a22610()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5a22650(self):
		input = -1.46534
		input = input + self.synapse0x5a22990()
		input = input + self.synapse0x5a229d0()
		input = input + self.synapse0x5a22a10()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5a22a50(self):
		input = 0.521133
		input = input + self.synapse0x5a22d90()
		input = input + self.synapse0x5a22dd0()
		input = input + self.synapse0x5a22e10()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5a22e50(self):
		input = -0.310288
		input = input + self.synapse0x5a23190()
		input = input + self.synapse0x5a231d0()
		input = input + self.synapse0x5a23210()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5a23250(self):
		input = -0.704482
		input = input + self.synapse0x5a23590()
		input = input + self.synapse0x5a235d0()
		input = input + self.synapse0x59d8bb0()
		input = input + self.synapse0x59d8bf0()
		input = input + self.synapse0x5a23720()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5a23760(self):
		input = 0.240326
		input = input + self.synapse0x5a23aa0()
		input = input + self.synapse0x5a23ae0()
		input = input + self.synapse0x5a23b20()
		input = input + self.synapse0x5a23b60()
		input = input + self.synapse0x5a23ba0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5a23be0(self):
		input = -0.729438
		input = input + self.synapse0x5a23f20()
		input = input + self.synapse0x5a23f60()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5a23fa0(self):
		input = 1.18112
		input = input + self.synapse0x5a242e0()
		input = input + self.synapse0x5a24320()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5a24360(self):
		input = -1.11026
		input = input + self.synapse0x5a246a0()
		input = input + self.synapse0x5a246e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5a24720(self):
		input = 0.850224
		input = input + self.synapse0x5a24a60()
		input = input + self.synapse0x5a24aa0()
		input = input + self.synapse0x59f7540()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5a24cf0(self):
		input = 6.06658
		input = input + self.synapse0x59f7580()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x59f75c0(self):
		return (self.neuron0x5a10900()*-0.919716)
	def synapse0x59d9080(self):
		return (self.neuron0x5a10c40()*0.453358)
	def synapse0x5a22210(self):
		return (self.neuron0x5a21b80()*3.03902)
	def synapse0x5a22590(self):
		return (self.neuron0x5a10900()*0.820969)
	def synapse0x5a225d0(self):
		return (self.neuron0x5a10c40()*-2.13804)
	def synapse0x5a22610(self):
		return (self.neuron0x5a21b80()*1.19974)
	def synapse0x5a22990(self):
		return (self.neuron0x5a10900()*0.653192)
	def synapse0x5a229d0(self):
		return (self.neuron0x5a10c40()*2.00153)
	def synapse0x5a22a10(self):
		return (self.neuron0x5a21b80()*-3.6891)
	def synapse0x5a22d90(self):
		return (self.neuron0x5a10900()*-1.11734)
	def synapse0x5a22dd0(self):
		return (self.neuron0x5a10c40()*1.93581)
	def synapse0x5a22e10(self):
		return (self.neuron0x5a21b80()*-2.11766)
	def synapse0x5a23190(self):
		return (self.neuron0x5a10900()*0.484215)
	def synapse0x5a231d0(self):
		return (self.neuron0x5a10c40()*-1.28345)
	def synapse0x5a23210(self):
		return (self.neuron0x5a21b80()*2.10527)
	def synapse0x5a23590(self):
		return (self.neuron0x5a21f60()*1.0904)
	def synapse0x5a235d0(self):
		return (self.neuron0x5a22250()*2.85411)
	def synapse0x59d8bb0(self):
		return (self.neuron0x5a22650()*0.641853)
	def synapse0x59d8bf0(self):
		return (self.neuron0x5a22a50()*-2.27269)
	def synapse0x5a23720(self):
		return (self.neuron0x5a22e50()*-3.01609)
	def synapse0x5a23aa0(self):
		return (self.neuron0x5a21f60()*0.5849)
	def synapse0x5a23ae0(self):
		return (self.neuron0x5a22250()*-0.644956)
	def synapse0x5a23b20(self):
		return (self.neuron0x5a22650()*-0.732079)
	def synapse0x5a23b60(self):
		return (self.neuron0x5a22a50()*0.925675)
	def synapse0x5a23ba0(self):
		return (self.neuron0x5a22e50()*1.3573)
	def synapse0x5a23f20(self):
		return (self.neuron0x5a23250()*2.76996)
	def synapse0x5a23f60(self):
		return (self.neuron0x5a23760()*-0.771015)
	def synapse0x5a242e0(self):
		return (self.neuron0x5a23250()*-3.91347)
	def synapse0x5a24320(self):
		return (self.neuron0x5a23760()*1.16068)
	def synapse0x5a246a0(self):
		return (self.neuron0x5a23250()*4.01207)
	def synapse0x5a246e0(self):
		return (self.neuron0x5a23760()*-1.71203)
	def synapse0x5a24a60(self):
		return (self.neuron0x5a23be0()*-3.03156)
	def synapse0x5a24aa0(self):
		return (self.neuron0x5a23fa0()*5.16055)
	def synapse0x59f7540(self):
		return (self.neuron0x5a24360()*-5.26779)
	def synapse0x59f7580(self):
		return (self.neuron0x5a24720()*-12.482)
