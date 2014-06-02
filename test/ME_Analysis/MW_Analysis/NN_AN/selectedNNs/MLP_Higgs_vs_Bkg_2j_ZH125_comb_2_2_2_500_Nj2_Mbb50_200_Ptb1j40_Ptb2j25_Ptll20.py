from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_2_2_500_Nj2_Mbb50_200_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.392068)/0.290776
		self.input1 = (in1 - 0.502534)/0.347166
		self.input2 = (in2 - 0.565438)/0.340056
		if index==0: return self.neuron0xf5f4730();
		return 0.
	def neuron0xf5f2610(self):
		return self.input0
	def neuron0xf5f2950(self):
		return self.input1
	def neuron0xf5f2c90(self):
		return self.input2
	def neuron0xf5f3100(self):
		input = 2.39646
		input = input + self.synapse0xf597800()
		input = input + self.synapse0xf5f33b0()
		input = input + self.synapse0xf5f33f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xf5f3430(self):
		input = 4.47938
		input = input + self.synapse0xf5f3770()
		input = input + self.synapse0xf5f37b0()
		input = input + self.synapse0xf5f37f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xf5f3830(self):
		input = -0.0812917
		input = input + self.synapse0xf5f3b70()
		input = input + self.synapse0xf5f3bb0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xf5f3bf0(self):
		input = -0.1319
		input = input + self.synapse0xf5f3f30()
		input = input + self.synapse0xf5f3f70()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xf5f3fb0(self):
		input = 0.0387131
		input = input + self.synapse0xf5f42f0()
		input = input + self.synapse0xf5f4330()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xf5f4370(self):
		input = 0.00861021
		input = input + self.synapse0xf5f46b0()
		input = input + self.synapse0xf5f46f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xf5f4730(self):
		input = 1.39664
		input = input + self.synapse0xf5978e0()
		input = input + self.synapse0xf5f4a70()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0xf597800(self):
		return (self.neuron0xf5f2610()*1.17098)
	def synapse0xf5f33b0(self):
		return (self.neuron0xf5f2950()*-0.119476)
	def synapse0xf5f33f0(self):
		return (self.neuron0xf5f2c90()*0.0840931)
	def synapse0xf5f3770(self):
		return (self.neuron0xf5f2610()*-1.0315)
	def synapse0xf5f37b0(self):
		return (self.neuron0xf5f2950()*-0.186701)
	def synapse0xf5f37f0(self):
		return (self.neuron0xf5f2c90()*-0.707374)
	def synapse0xf5f3b70(self):
		return (self.neuron0xf5f3100()*-3.41378)
	def synapse0xf5f3bb0(self):
		return (self.neuron0xf5f3430()*1.63603)
	def synapse0xf5f3f30(self):
		return (self.neuron0xf5f3100()*2.31649)
	def synapse0xf5f3f70(self):
		return (self.neuron0xf5f3430()*-3.29337)
	def synapse0xf5f42f0(self):
		return (self.neuron0xf5f3830()*-3.58734)
	def synapse0xf5f4330(self):
		return (self.neuron0xf5f3bf0()*3.12002)
	def synapse0xf5f46b0(self):
		return (self.neuron0xf5f3830()*4.47806)
	def synapse0xf5f46f0(self):
		return (self.neuron0xf5f3bf0()*-3.77194)
	def synapse0xf5978e0(self):
		return (self.neuron0xf5f3fb0()*5.86748)
	def synapse0xf5f4a70(self):
		return (self.neuron0xf5f4370()*-8.87691)
