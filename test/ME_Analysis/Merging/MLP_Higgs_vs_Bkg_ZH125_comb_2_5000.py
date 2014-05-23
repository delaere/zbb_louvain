from math import exp

from math import tanh

class MLP_Higgs_vs_Bkg_ZH125_comb_2_5000:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.445235)/0.307413
		self.input1 = (in1 - 0.487302)/0.29068
		self.input2 = (in2 - 0.530975)/0.330691
		if index==0: return self.neuron0x8ef5870();
		return 0.
	def neuron0x8ee3ae0(self):
		return self.input0
	def neuron0x8ee3e20(self):
		return self.input1
	def neuron0x8ef4df0(self):
		return self.input2
	def neuron0x8ef5140(self):
		input = -1.24181
		input = input + self.synapse0x8eabef0()
		input = input + self.synapse0x8ef53f0()
		input = input + self.synapse0x8ef5430()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x8ef5470(self):
		input = 0.886138
		input = input + self.synapse0x8ef57b0()
		input = input + self.synapse0x8ef57f0()
		input = input + self.synapse0x8ef5830()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x8ef5870(self):
		input = 125.051
		input = input + self.synapse0x8ef5a90()
		input = input + self.synapse0x8ef5ad0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x8eabef0(self):
		return (self.neuron0x8ee3ae0()*0.104354)
	def synapse0x8ef53f0(self):
		return (self.neuron0x8ee3e20()*-0.356602)
	def synapse0x8ef5430(self):
		return (self.neuron0x8ef4df0()*0.354925)
	def synapse0x8ef57b0(self):
		return (self.neuron0x8ee3ae0()*-0.0769232)
	def synapse0x8ef57f0(self):
		return (self.neuron0x8ee3e20()*0.160928)
	def synapse0x8ef5830(self):
		return (self.neuron0x8ef4df0()*-0.186599)
	def synapse0x8ef5a90(self):
		return (self.neuron0x8ef5140()*-82.5782)
	def synapse0x8ef5ad0(self):
		return (self.neuron0x8ef5470()*-150.58)
