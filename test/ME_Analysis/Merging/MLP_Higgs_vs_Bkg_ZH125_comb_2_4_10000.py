from math import exp

from math import tanh

class MLP_Higgs_vs_Bkg_ZH125_comb_2_4_10000:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.445235)/0.307413
		self.input1 = (in1 - 0.487302)/0.29068
		self.input2 = (in2 - 0.530975)/0.330691
		if index==0: return self.neuron0x148c6220();
		return 0.
	def neuron0x148b35d0(self):
		return self.input0
	def neuron0x148b3910(self):
		return self.input1
	def neuron0x148c48e0(self):
		return self.input2
	def neuron0x148c4c30(self):
		input = 4.83359
		input = input + self.synapse0x1487be20()
		input = input + self.synapse0x1489a370()
		input = input + self.synapse0x148c4ee0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x148c4f20(self):
		input = 1.1964
		input = input + self.synapse0x148c5260()
		input = input + self.synapse0x148c52a0()
		input = input + self.synapse0x148c52e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x148c5320(self):
		input = 0.810954
		input = input + self.synapse0x148c5660()
		input = input + self.synapse0x148c56a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x148c56e0(self):
		input = 2.11072
		input = input + self.synapse0x148c5a20()
		input = input + self.synapse0x148c5a60()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x148c5aa0(self):
		input = -0.846577
		input = input + self.synapse0x148c5de0()
		input = input + self.synapse0x148c5e20()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x148c5e60(self):
		input = 0.642514
		input = input + self.synapse0x148c61a0()
		input = input + self.synapse0x148c61e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x148c6220(self):
		input = 1.6725
		input = input + self.synapse0x148c6440()
		input = input + self.synapse0x148c6480()
		input = input + self.synapse0x148c64c0()
		input = input + self.synapse0x14826550()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x1487be20(self):
		return (self.neuron0x148b35d0()*-1.79157)
	def synapse0x1489a370(self):
		return (self.neuron0x148b3910()*0.169991)
	def synapse0x148c4ee0(self):
		return (self.neuron0x148c48e0()*-0.657211)
	def synapse0x148c5260(self):
		return (self.neuron0x148b35d0()*1.93715)
	def synapse0x148c52a0(self):
		return (self.neuron0x148b3910()*-0.214402)
	def synapse0x148c52e0(self):
		return (self.neuron0x148c48e0()*0.212965)
	def synapse0x148c5660(self):
		return (self.neuron0x148c4c30()*-0.784926)
	def synapse0x148c56a0(self):
		return (self.neuron0x148c4f20()*6.2193)
	def synapse0x148c5a20(self):
		return (self.neuron0x148c4c30()*5.86289)
	def synapse0x148c5a60(self):
		return (self.neuron0x148c4f20()*-6.13878)
	def synapse0x148c5de0(self):
		return (self.neuron0x148c4c30()*0.535953)
	def synapse0x148c5e20(self):
		return (self.neuron0x148c4f20()*-2.43749)
	def synapse0x148c61a0(self):
		return (self.neuron0x148c4c30()*-0.120776)
	def synapse0x148c61e0(self):
		return (self.neuron0x148c4f20()*2.86315)
	def synapse0x148c6440(self):
		return (self.neuron0x148c5320()*5.6212)
	def synapse0x148c6480(self):
		return (self.neuron0x148c56e0()*-9.90454)
	def synapse0x148c64c0(self):
		return (self.neuron0x148c5aa0()*-2.68929)
	def synapse0x14826550(self):
		return (self.neuron0x148c5e60()*2.59564)
