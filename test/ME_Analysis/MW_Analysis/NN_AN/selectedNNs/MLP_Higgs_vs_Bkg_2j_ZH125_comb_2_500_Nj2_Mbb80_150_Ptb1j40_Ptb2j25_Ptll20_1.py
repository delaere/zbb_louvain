from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_Bkg_2j_ZH125_comb_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_1:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.500017)/0.25242
		self.input1 = (in1 - 0.592179)/0.338539
		self.input2 = (in2 - 0.679468)/0.281065
		if index==0: return self.neuron0x1dda5fb0();
		return 0.
	def neuron0x1dda4d90(self):
		return self.input0
	def neuron0x1dda50d0(self):
		return self.input1
	def neuron0x1dda5410(self):
		return self.input2
	def neuron0x1dda5880(self):
		input = 3.61475
		input = input + self.synapse0x1dd49fd0()
		input = input + self.synapse0x1dda5b30()
		input = input + self.synapse0x1dda5b70()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1dda5bb0(self):
		input = 2.80419
		input = input + self.synapse0x1dda5ef0()
		input = input + self.synapse0x1dda5f30()
		input = input + self.synapse0x1dda5f70()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1dda5fb0(self):
		input = 3.69251
		input = input + self.synapse0x1dd4a080()
		input = input + self.synapse0x1dda62f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x1dd49fd0(self):
		return (self.neuron0x1dda4d90()*-1.30708)
	def synapse0x1dda5b30(self):
		return (self.neuron0x1dda50d0()*0.104347)
	def synapse0x1dda5b70(self):
		return (self.neuron0x1dda5410()*-0.495562)
	def synapse0x1dda5ef0(self):
		return (self.neuron0x1dda4d90()*1.40391)
	def synapse0x1dda5f30(self):
		return (self.neuron0x1dda50d0()*-0.0852811)
	def synapse0x1dda5f70(self):
		return (self.neuron0x1dda5410()*0.0720031)
	def synapse0x1dd4a080(self):
		return (self.neuron0x1dda5880()*-9.63864)
	def synapse0x1dda62f0(self):
		return (self.neuron0x1dda5bb0()*6.18629)
