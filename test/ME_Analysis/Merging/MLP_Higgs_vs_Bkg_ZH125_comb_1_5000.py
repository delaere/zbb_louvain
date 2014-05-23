from math import exp

from math import tanh

class MLP_Higgs_vs_Bkg_ZH125_comb_1_5000:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.445235)/0.307413
		self.input1 = (in1 - 0.487302)/0.29068
		self.input2 = (in2 - 0.530975)/0.330691
		if index==0: return self.neuron0xfc104b0();
		return 0.
	def neuron0xfbfeb20(self):
		return self.input0
	def neuron0xfbfee60(self):
		return self.input1
	def neuron0xfc0fe30(self):
		return self.input2
	def neuron0xfc10180(self):
		input = -4.42997
		input = input + self.synapse0xfbc6f30()
		input = input + self.synapse0xfc10430()
		input = input + self.synapse0xfc10470()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xfc104b0(self):
		input = -5.20712
		input = input + self.synapse0xfc106d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0xfbc6f30(self):
		return (self.neuron0xfbfeb20()*0.16128)
	def synapse0xfc10430(self):
		return (self.neuron0xfbfee60()*0.0499317)
	def synapse0xfc10470(self):
		return (self.neuron0xfc0fe30()*0.141556)
	def synapse0xfc106d0(self):
		return (self.neuron0xfc10180()*397.746)
