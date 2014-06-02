from math import exp

from math import tanh

class Final12/MLP_ZZ_vs_TT_ZH125_comb_2_1000_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 22.0514)/2.02154
		self.input1 = (in1 - 20.8812)/1.67352
		self.input2 = (in2 - 10.5466)/1.32501
		if index==0: return self.neuron0x32d403e0();
		return 0.
	def neuron0x32d3f2d0(self):
		return self.input0
	def neuron0x32d3f580(self):
		return self.input1
	def neuron0x32d3f8c0(self):
		return self.input2
	def neuron0x32d3fd30(self):
		input = -4.98325
		input = input + self.synapse0x32cd3100()
		input = input + self.synapse0x32d2e740()
		input = input + self.synapse0x32cd3140()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x32d3ffe0(self):
		input = -0.0845866
		input = input + self.synapse0x32d40320()
		input = input + self.synapse0x32d40360()
		input = input + self.synapse0x32d403a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x32d403e0(self):
		input = 5.81714
		input = input + self.synapse0x32d3fc00()
		input = input + self.synapse0x32d3fcd0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x32cd3100(self):
		return (self.neuron0x32d3f2d0()*0.399729)
	def synapse0x32d2e740(self):
		return (self.neuron0x32d3f580()*0.357057)
	def synapse0x32cd3140(self):
		return (self.neuron0x32d3f8c0()*-0.991288)
	def synapse0x32d40320(self):
		return (self.neuron0x32d3f2d0()*-1.61681)
	def synapse0x32d40360(self):
		return (self.neuron0x32d3f580()*-0.0396754)
	def synapse0x32d403a0(self):
		return (self.neuron0x32d3f8c0()*1.18689)
	def synapse0x32d3fc00(self):
		return (self.neuron0x32d3fd30()*-10.2156)
	def synapse0x32d3fcd0(self):
		return (self.neuron0x32d3ffe0()*-9.94511)
