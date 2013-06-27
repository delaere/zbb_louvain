from math import exp

from math import tanh

class MLP_Higgs_vs_Bkg_ZH125_comb_2_10000:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.445235)/0.307413
		self.input1 = (in1 - 0.487302)/0.29068
		self.input2 = (in2 - 0.530975)/0.330691
		if index==0: return self.neuron0x5cfe1e0();
		return 0.
	def neuron0x5cec490(self):
		return self.input0
	def neuron0x5cec7d0(self):
		return self.input1
	def neuron0x5cfd7a0(self):
		return self.input2
	def neuron0x5cfdaf0(self):
		input = -0.0143284
		input = input + self.synapse0x5cb4ce0()
		input = input + self.synapse0x5cd3230()
		input = input + self.synapse0x5cfdda0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5cfdde0(self):
		input = 0.826485
		input = input + self.synapse0x5cfe120()
		input = input + self.synapse0x5cfe160()
		input = input + self.synapse0x5cfe1a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5cfe1e0(self):
		input = -13.4646
		input = input + self.synapse0x5cfe400()
		input = input + self.synapse0x5cfe440()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x5cb4ce0(self):
		return (self.neuron0x5cec490()*0.181738)
	def synapse0x5cd3230(self):
		return (self.neuron0x5cec7d0()*0.0361336)
	def synapse0x5cfdda0(self):
		return (self.neuron0x5cfd7a0()*0.0324666)
	def synapse0x5cfe120(self):
		return (self.neuron0x5cec490()*10.5766)
	def synapse0x5cfe160(self):
		return (self.neuron0x5cec7d0()*-11.0485)
	def synapse0x5cfe1a0(self):
		return (self.neuron0x5cfd7a0()*1.36167)
	def synapse0x5cfe400(self):
		return (self.neuron0x5cfdaf0()*25.7712)
	def synapse0x5cfe440(self):
		return (self.neuron0x5cfdde0()*0.891194)
