from math import exp

from math import tanh

class MLP_Higgs_vs_Bkg_ZH125_comb_1_10000:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.445235)/0.307413
		self.input1 = (in1 - 0.487302)/0.29068
		self.input2 = (in2 - 0.530975)/0.330691
		if index==0: return self.neuron0x14e09de0();
		return 0.
	def neuron0x14df8490(self):
		return self.input0
	def neuron0x14df87d0(self):
		return self.input1
	def neuron0x14e097a0(self):
		return self.input2
	def neuron0x14e09af0(self):
		input = -1.00626
		input = input + self.synapse0x14dc0ce0()
		input = input + self.synapse0x14ddf230()
		input = input + self.synapse0x14e09da0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x14e09de0(self):
		input = -21.1476
		input = input + self.synapse0x14e0a000()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x14dc0ce0(self):
		return (self.neuron0x14df8490()*0.104863)
	def synapse0x14ddf230(self):
		return (self.neuron0x14df87d0()*-0.0160283)
	def synapse0x14e09da0(self):
		return (self.neuron0x14e097a0()*0.0192012)
	def synapse0x14e0a000(self):
		return (self.neuron0x14e09af0()*78.0741)
